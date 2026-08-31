#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compile le référentiel HEA en ressources FHIR R4.

Génère :
- CodeSystem : systèmes de codes nationaux (terminologies)
- ValueSet : ensembles de valeurs versionnés
- StructureDefinition : définitions de ressources FHIR pour les objets de données

Usage :
    python3 scripts/compilers/compile_fhir.py              # génère dist/fhir/
    python3 scripts/compilers/compile_fhir.py --validate    # valide les ressources
    python3 scripts/compilers/compile_fhir.py --output /tmp/...  # répertoire custom
"""

import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FHIR_VERSION = "4.0.1"
FHIR_NS = "https://healmadagascar.mg/fhir"


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return text[3:end].strip("\n")


def fm_field(fm, key):
    m = re.search(r"^%s:\s*(.*)$" % re.escape(key), fm, re.MULTILINE)
    return m.group(1) if m else None


def list_value(raw):
    if raw is None:
        return []
    raw = raw.strip()
    if not raw or raw == "[]":
        return []
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1]
        items = re.findall(r"['\"]([^'\"]*)['\"]", inner)
        if items:
            return [i for i in items if i]
        return [x.strip() for x in inner.split(",") if x.strip()]
    return [x.strip().strip("'\"") for x in raw.split(",") if x.strip()]


def extract_do_type_from_body(body):
    """Extrait le type d'objet depuis le corps du document."""
    m = re.search(r"\*\*Type\*\*\s*:\s*(.+)", body)
    if m:
        raw = m.group(1).strip()
        # Extraire le type principal (avant la parenthèse si présente)
        main_type = re.split(r"\s*\(", raw)[0].strip().lower()
        return main_type
    return None


def extract_constraints_from_body(body):
    """Extrait les contraintes depuis le corps du document."""
    m = re.search(r"\*\*Contraintes\*\*\s*:\s*(.+)", body)
    if m:
        return m.group(1).strip()
    return None


def extract_source_ref_from_body(body):
    """Extrait le référentiel source depuis le corps du document."""
    m = re.search(r"\*\*Référentiel source\*\*\s*:\s*(.+)", body)
    if m:
        return m.group(1).strip()
    return None


# Mapping des types DO → types FHIR
DO_TO_FHIR_TYPE = {
    "entité": "Patient",
    "entite": "Patient",
    "identifiant": "Identifier",
    "entité composite": "Patient",
    "entite composite": "Patient",
    "événement": "Encounter",
    "evenement": "Encounter",
    "produit": "Medication",
    "observation": "Observation",
    "acte": "Procedure",
    "organisation": "Organization",
    "lieu": "Location",
    "praticien": "Practitioner",
    "prescription": "MedicationRequest",
    "dispensation": "MedicationDispense",
    "laboratoire": "Organization",
    "signal": "Flag",
    "investigation": "DiagnosticReport",
    "alerte": "Flag",
    "stock": "InventoryItem",
    "commande": "MedicationRequest",
    "facturation": "Claim",
    "remboursement": "ClaimResponse",
    "couverture": "Coverage",
    "adhésion": "CoverageEligibilityRequest",
    "adhesion": "CoverageEligibilityRequest",
    "prestation": "ExplanationOfBenefit",
    "compte": "Account",
    "utilisateur": "Person",
    "droit": "Permission",
    "journal": "AuditEvent",
    "configuration": "Basic",
    "référentiel": "ValueSet",
    "referentiel": "ValueSet",
    "métrique": "Measure",
    "metrique": "Measure",
    "rapport": "DiagnosticReport",
    "notification": "Communication",
}


def generate_codesystem():
    """Génère le CodeSystem national de terminologies."""
    return {
        "resourceType": "CodeSystem",
        "id": "hea-terminology-cs",
        "url": "%s/CodeSystem/hea-terminology" % FHIR_NS,
        "version": "1.0.0",
        "name": "HEATerminologyCodeSystem",
        "title": "Système de codes national - Terminologies HEA",
        "status": "active",
        "experimental": False,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "publisher": "DEPSI - Madagascar",
        "description": "Système de codes centralisé pour les terminologies nationales de santé",
        "content": "fragment",
        "caseSensitive": True,
        "valueSet": "%s/ValueSet/hea-terminology-vs" % FHIR_NS,
        "concept": [
            {
                "code": "patient",
                "display": "Patient",
                "definition": "Personne physique bénéficiaire de soins"
            },
            {
                "code": "dossier",
                "display": "Dossier patient",
                "definition": "Ensemble structuré des informations cliniques"
            },
            {
                "code": "evenement",
                "display": "Événement clinique",
                "definition": "Épisode de soins ou encounter"
            },
            {
                "code": "produit",
                "display": "Produit de santé",
                "definition": "Médicament, vaccin ou intrant"
            },
            {
                "code": "observation",
                "display": "Observation",
                "definition": "Résultat de laboratoire ou mesure clinique"
            },
            {
                "code": "prescription",
                "display": "Prescription",
                "definition": "Ordonnance médicale"
            },
            {
                "code": "dispensation",
                "display": "Dispensation",
                "definition": "Fourniture effective d'un produit de santé"
            },
            {
                "code": "organisation",
                "display": "Organisation",
                "definition": "Établissement ou structure sanitaire"
            },
            {
                "code": "praticien",
                "display": "Praticien",
                "definition": "Professionnel de santé"
            },
            {
                "code": "signal",
                "display": "Signal épidémiologique",
                "definition": "Signal de surveillance sanitaire"
            },
            {
                "code": "investigation",
                "display": "Investigation",
                "definition": "Enquête épidémiologique"
            },
            {
                "code": "stock",
                "display": "Stock",
                "definition": "Gestion des stocks de produits"
            },
            {
                "code": "facturation",
                "display": "Facturation",
                "definition": "Transaction financière"
            },
            {
                "code": "couverture",
                "display": "Couverture",
                "definition": "Couverture sanitaire ou assurance"
            }
        ]
    }


def generate_valueset():
    """Génère le ValueSet des types d'objets de données."""
    return {
        "resourceType": "ValueSet",
        "id": "hea-data-object-types-vs",
        "url": "%s/ValueSet/hea-data-object-types" % FHIR_NS,
        "version": "1.0.0",
        "name": "HEADataObjectTypesValueSet",
        "title": "Types d'objets de données HEA",
        "status": "active",
        "experimental": False,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "publisher": "DEPSI - Madagascar",
        "description": "Ensemble de valeurs des types d'objets de données du référentiel HEA",
        "compose": {
            "include": [
                {
                    "system": "%s/CodeSystem/hea-terminology" % FHIR_NS,
                    "concept": [
                        {"code": "patient", "display": "Patient"},
                        {"code": "dossier", "display": "Dossier patient"},
                        {"code": "evenement", "display": "Événement clinique"},
                        {"code": "produit", "display": "Produit de santé"},
                        {"code": "observation", "display": "Observation"},
                        {"code": "prescription", "display": "Prescription"},
                        {"code": "dispensation", "display": "Dispensation"},
                        {"code": "organisation", "display": "Organisation"},
                        {"code": "praticien", "display": "Praticien"},
                        {"code": "signal", "display": "Signal épidémiologique"},
                        {"code": "investigation", "display": "Investigation"},
                        {"code": "stock", "display": "Stock"},
                        {"code": "facturation", "display": "Facturation"},
                        {"code": "couverture", "display": "Couverture"}
                    ]
                }
            ]
        }
    }


def generate_structuredefinition(obj, body):
    """Génère un StructureDefinition pour un objet de données."""
    do_id = obj["id"]
    title = obj.get("title", do_id)
    version = obj.get("version", "1.0.0")
    description = ""

    # Extraire la première paragraph après le titre
    lines = body.split("\n")
    in_title = False
    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            in_title = True
            continue
        if in_title and line:
            description = line
            break

    # Extraire le type d'objet
    do_type = extract_do_type_from_body(body)
    fhir_type = DO_TO_FHIR_TYPE.get(do_type, "Basic")

    # Extraire les contraintes
    constraints = extract_constraints_from_body(body)

    # Générer les éléments de base
    elements = [
        {
            "id": "Resource.id",
            "path": "Resource.id",
            "type": [{"code": "id"}]
        },
        {
            "id": "Resource.meta",
            "path": "Resource.meta",
            "type": [{"code": "BackboneElement"}]
        },
        {
            "id": "Resource.meta.versionId",
            "path": "Resource.meta.versionId",
            "type": [{"code": "id"}]
        },
        {
            "id": "Resource.meta.lastUpdated",
            "path": "Resource.meta.lastUpdated",
            "type": [{"code": "instant"}]
        }
    ]

    # Ajouter les propriétés spécifiques au type
    if fhir_type == "Patient":
        elements.extend([
            {
                "id": "Patient.identifier",
                "path": "Patient.identifier",
                "type": [{"code": "Identifier"}],
                "short": "Identifiant national du patient"
            },
            {
                "id": "Patient.name",
                "path": "Patient.name",
                "type": [{"code": "HumanName"}],
                "short": "Nom du patient"
            },
            {
                "id": "Patient.birthDate",
                "path": "Patient.birthDate",
                "type": [{"code": "date"}],
                "short": "Date de naissance"
            }
        ])
    elif fhir_type == "Medication":
        elements.extend([
            {
                "id": "Medication.code",
                "path": "Medication.code",
                "type": [{"code": "CodeableConcept"}],
                "short": "Code du médicament (DCI, nom commercial)"
            },
            {
                "id": "Medication.status",
                "path": "Medication.status",
                "type": [{"code": "code"}],
                "short": "Statut (active, inactive, entered-in-error)"
            }
        ])
    elif fhir_type == "Organization":
        elements.extend([
            {
                "id": "Organization.identifier",
                "path": "Organization.identifier",
                "type": [{"code": "Identifier"}],
                "short": "Identifiant de l'organisation"
            },
            {
                "id": "Organization.name",
                "path": "Organization.name",
                "type": [{"code": "string"}],
                "short": "Nom de l'organisation"
            },
            {
                "id": "Organization.type",
                "path": "Organization.type",
                "type": [{"code": "CodeableConcept"}],
                "short": "Type de structure sanitaire"
            }
        ])

    # Construire le StructureDefinition
    sd = {
        "resourceType": "StructureDefinition",
        "id": "hea-%s" % do_id.lower(),
        "url": "%s/StructureDefinition/hea-%s" % (FHIR_NS, do_id.lower()),
        "version": version,
        "name": "HEA%sDefinition" % do_id.replace("-", ""),
        "title": "Définition HEA - %s" % title,
        "status": "active",
        "experimental": False,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "publisher": "DEPSI - Madagascar",
        "description": description,
        "kind": "resource",
        "abstract": False,
        "type": fhir_type,
        "baseDefinition": "http://hl7.org/fhir/StructureDefinition/%s" % fhir_type,
        "derivation": "constraint",
        "differential": {
            "element": elements
        }
    }

    # Ajouter les extensions HEA
    sd["extension"] = [
        {
            "url": "https://healmadagascar.mg/fhir/StructureDefinition/hea-id",
            "valueString": do_id
        },
        {
            "url": "https://healmadagascar.mg/fhir/StructureDefinition/hea-status",
            "valueString": obj.get("status", "draft")
        },
        {
            "url": "https://healmadagascar.mg/fhir/StructureDefinition/hea-owner",
            "valueString": obj.get("owner", "")
        }
    ]

    return sd


def compile_fhir_resources(output_dir):
    """Compile toutes les ressources FHIR."""
    # Générer le CodeSystem
    cs = generate_codesystem()
    cs_path = os.path.join(output_dir, "hea-terminology-cs.json")
    with open(cs_path, "w", encoding="utf-8") as f:
        json.dump(cs, f, indent=2, ensure_ascii=False)

    # Générer le ValueSet
    vs = generate_valueset()
    vs_path = os.path.join(output_dir, "hea-data-object-types-vs.json")
    with open(vs_path, "w", encoding="utf-8") as f:
        json.dump(vs, f, indent=2, ensure_ascii=False)

    # Collecter et compiler les objets de données
    pattern = os.path.join(REPO_ROOT, "referentiel", "objets-de-donnees", "do-*.md")
    compiled = [cs_path, vs_path]

    for path in sorted(glob.glob(pattern)):
        text = open(path, encoding="utf-8").read()
        fm = parse_frontmatter(text)
        if fm is None:
            continue

        oid = fm_field(fm, "id")
        otype = fm_field(fm, "type")
        if not oid or not otype:
            continue

        # Extraire le corps du document
        end = text.find("\n---", 3)
        body = text[end + 4:] if end != -1 else text

        obj = {
            "id": oid,
            "type": otype,
            "file": os.path.relpath(path, REPO_ROOT)
        }

        # Extraire les champs scalaires
        for field in ["title", "status", "owner", "version", "niveau",
                       "family", "envelope", "source"]:
            val = fm_field(fm, field)
            if val is not None:
                val = val.strip().strip('"').strip("'")
                obj[field] = val

        # Générer le StructureDefinition
        sd = generate_structuredefinition(obj, body)
        sd_filename = "hea-%s-sd.json" % oid.lower()
        sd_path = os.path.join(output_dir, sd_filename)
        with open(sd_path, "w", encoding="utf-8") as f:
            json.dump(sd, f, indent=2, ensure_ascii=False)
        compiled.append(sd_path)

    return compiled


def validate_fhir_resources(output_dir):
    """Valide les ressources FHIR générées."""
    errors = []
    count = 0

    for filepath in sorted(glob.glob(os.path.join(output_dir, "*.json"))):
        count += 1
        try:
            with open(filepath, encoding="utf-8") as f:
                resource = json.load(f)

            # Vérifications de base
            if "resourceType" not in resource:
                errors.append((filepath, "Champ resourceType manquant"))
            if "id" not in resource:
                errors.append((filepath, "Champ id manquant"))
            if "url" not in resource:
                errors.append((filepath, "Champ url manquant"))

        except json.JSONDecodeError as e:
            errors.append((filepath, "JSON invalide: %s" % str(e)))

    return count, errors


def main():
    parser = argparse.ArgumentParser(
        description="Compile le référentiel HEA en ressources FHIR R4")
    parser.add_argument("--output", "-o", default=None,
                        help="Répertoire de sortie (défaut: dist/fhir/)")
    parser.add_argument("--validate", action="store_true",
                        help="Valider les ressources après compilation")
    args = parser.parse_args()

    output_dir = args.output or os.path.join(REPO_ROOT, "dist", "fhir")
    os.makedirs(output_dir, exist_ok=True)

    # Compiler les ressources
    compiled = compile_fhir_resources(output_dir)

    print("=== Compilation FHIR R4 ===")
    print("Ressources générées : %d" % len(compiled))
    print("Répertoire : %s" % os.path.relpath(output_dir, REPO_ROOT))

    # Validation optionnelle
    if args.validate:
        count, errors = validate_fhir_resources(output_dir)
        if errors:
            print("\n[ERREUR] %d erreurs de validation :" % len(errors))
            for filepath, err in errors[:10]:
                print("  - %s : %s" % (os.path.relpath(filepath, REPO_ROOT), err))
            sys.exit(1)
        else:
            print("[OK] %d ressources valides." % count)

    print("\nRésumé : OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
