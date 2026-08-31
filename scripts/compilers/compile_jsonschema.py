#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compile les objets de données HEA en JSON Schema vDraft-07.

Ce script transforme les métadonnées YAML des objets de données (DO-01..31)
en schémas JSON conformes au Draft-07 du standard JSON Schema.

Usage :
    python3 scripts/compilers/compile_jsonschema.py              # génère dist/schemas/
    python3 scripts/compilers/compile_jsonschema.py --validate   # valide les schémas
    python3 scripts/compilers/compile_jsonschema.py --output /tmp/...  # répertoire custom
"""

import argparse
import glob
import json
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HEA_NS = "https://healmadagascar.mg/ontologie/hea#"
JSON_SCHEMA_DRAFT = "http://json-schema.org/draft-07/schema#"

# Mapping des types DO → propriétés JSON Schema
DO_TYPE_MAP = {
    "patient": {"type": "object", "fhir_resource": "Patient"},
    "identifiant": {"type": "string", "pattern": "^[0-9]{12}$"},
    "dossier": {"type": "object", "fhir_resource": "Patient"},
    "evenement": {"type": "object"},
    "produit": {"type": "object", "fhir_resource": "Medication"},
    "observation": {"type": "object", "fhir_resource": "Observation"},
    "acte": {"type": "object", "fhir_resource": "Procedure"},
    "organisation": {"type": "object", "fhir_resource": "Organization"},
    "lieu": {"type": "object", "fhir_resource": "Location"},
    "praticien": {"type": "object", "fhir_resource": "Practitioner"},
    "prescription": {"type": "object", "fhir_resource": "MedicationRequest"},
    "dispensation": {"type": "object", "fhir_resource": "MedicationDispense"},
    "laboratoire": {"type": "object", "fhir_resource": "Organization"},
    "signal": {"type": "object"},
    "investigation": {"type": "object"},
    "alerte": {"type": "object", "fhir_resource": "Flag"},
    "stock": {"type": "object"},
    "commande": {"type": "object", "fhir_resource": "MedicationRequest"},
    "facturation": {"type": "object", "fhir_resource": "Claim"},
    "remboursement": {"type": "object", "fhir_resource": "ClaimResponse"},
    "couverture": {"type": "object", "fhir_resource": "Coverage"},
    "adhesion": {"type": "object", "fhir_resource": "CoverageEligibilityRequest"},
    "prestation": {"type": "object", "fhir_resource": "ExplanationOfBenefit"},
    "compte": {"type": "object", "fhir_resource": "Account"},
    "utilisateur": {"type": "object", "fhir_resource": "Person"},
    "droit": {"type": "object", "fhir_resource": "Permission"},
    "journal": {"type": "object", "fhir_resource": "AuditEvent"},
    "configuration": {"type": "object"},
    "referentiel": {"type": "object"},
    "metrique": {"type": "object"},
    "rapport": {"type": "object", "fhir_resource": "DiagnosticReport"},
    "notification": {"type": "object", "fhir_resource": "Communication"},
}


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
        return m.group(1).strip().lower()
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


def generate_properties_from_constraints(constraints, do_id):
    """Génère les propriétés JSON Schema à partir des contraintes textuelles."""
    properties = {
        "id": {
            "type": "string",
            "description": "Identifiant unique de l'objet",
            "const": do_id
        },
        "version": {
            "type": "string",
            "description": "Version de l'objet",
            "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$"
        }
    }

    if not constraints:
        return properties

    # Patterns communs dans les contraintes
    if "identifiant" in constraints.lower() or "nin" in constraints.lower():
        properties["identifiant"] = {
            "type": "string",
            "description": "Identifiant unique"
        }
        if "12 chiffres" in constraints:
            properties["identifiant"]["pattern"] = "^[0-9]{12}$"

    if "date" in constraints.lower():
        properties["date"] = {
            "type": "string",
            "format": "date-time",
            "description": "Date de l'événement"
        }

    if "quantité" in constraints.lower() or "quantite" in constraints.lower():
        properties["quantite"] = {
            "type": "integer",
            "minimum": 0,
            "description": "Quantité"
        }

    if "lot" in constraints.lower():
        properties["lot"] = {
            "type": "string",
            "description": "Numéro de lot"
        }

    if "dci" in constraints.lower() or "produit" in constraints.lower():
        properties["produit"] = {
            "type": "string",
            "description": "Identifiant du produit"
        }

    if "patient" in constraints.lower():
        properties["patientRef"] = {
            "type": "string",
            "description": "Référence au patient (DO-01)"
        }

    if "statut" in constraints.lower() or "confirmé" in constraints.lower():
        properties["statut"] = {
            "type": "string",
            "enum": ["en_cours", "confirme", "infirme", "cloture"],
            "description": "Statut de l'objet"
        }

    return properties


def compile_do(obj, body, output_dir):
    """Compile un objet de données en JSON Schema."""
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
    type_info = DO_TYPE_MAP.get(do_type, {"type": "object"})

    # Extraire les contraintes
    constraints = extract_constraints_from_body(body)
    source_ref = extract_source_ref_from_body(body)

    # Générer les propriétés
    properties = generate_properties_from_constraints(constraints, do_id)

    # Ajouter lespropriétés relationnelles
    related = list_value(fm_field(obj.get("_raw_fm", ""), "related") or "")
    for rel_id in related:
        prop_name = rel_id.lower().replace("-", "_") + "Ref"
        properties[prop_name] = {
            "type": "string",
            "description": "Référence à %s" % rel_id
        }

    # Construire le schéma
    schema = {
        "$schema": JSON_SCHEMA_DRAFT,
        "$id": "%s/schemas/%s.json" % (HEA_NS, do_id.lower()),
        "title": title,
        "description": description,
        "type": "object",
        "properties": properties,
        "required": ["id", "version"],
        "version": version,
        "x-hea-id": do_id,
        "x-hea-type": "objet-de-donnees",
        "x-hea-status": obj.get("status", "draft"),
        "x-hea-owner": obj.get("owner", ""),
        "x-hea-tags": obj.get("tags", [])
    }

    if source_ref:
        schema["x-hea-source-ref"] = source_ref

    # Écrire le fichier
    filename = "%s.json" % do_id.lower()
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(schema, f, indent=2, ensure_ascii=False)

    return filepath


def collect_do_objects():
    """Collecte tous les objets de données du référentiel."""
    objects = []
    pattern = os.path.join(REPO_ROOT, "referentiel", "objets-de-donnees", "do-*.md")

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
            "file": os.path.relpath(path, REPO_ROOT),
            "_raw_fm": fm
        }

        # Extraire les champs scalaires
        for field in ["title", "status", "owner", "version", "niveau",
                       "family", "envelope", "source"]:
            val = fm_field(fm, field)
            if val is not None:
                val = val.strip().strip('"').strip("'")
                obj[field] = val

        # Extraire les tags
        tags_val = fm_field(fm, "tags")
        if tags_val is not None:
            obj["tags"] = list_value(tags_val)

        objects.append((obj, body))

    return objects


def validate_schemas(output_dir):
    """Valide les schémas JSON générés."""
    errors = []
    count = 0

    for filepath in sorted(glob.glob(os.path.join(output_dir, "do-*.json"))):
        count += 1
        try:
            with open(filepath, encoding="utf-8") as f:
                schema = json.load(f)

            # Vérifications de base
            if "$schema" not in schema:
                errors.append((filepath, "Champ $schema manquant"))
            if "type" not in schema:
                errors.append((filepath, "Champ type manquant"))
            if "properties" not in schema:
                errors.append((filepath, "Champ properties manquant"))

        except json.JSONDecodeError as e:
            errors.append((filepath, "JSON invalide: %s" % str(e)))

    return count, errors


def main():
    parser = argparse.ArgumentParser(
        description="Compile les objets de données HEA en JSON Schema vDraft-07")
    parser.add_argument("--output", "-o", default=None,
                        help="Répertoire de sortie (défaut: dist/schemas/)")
    parser.add_argument("--validate", action="store_true",
                        help="Valider les schémas après compilation")
    args = parser.parse_args()

    output_dir = args.output or os.path.join(REPO_ROOT, "dist", "schemas")
    os.makedirs(output_dir, exist_ok=True)

    # Collecter les objets
    objects = collect_do_objects()
    if not objects:
        print("[ERREUR] Aucun objet de données trouvé dans referentiel/objets-de-donnees/")
        sys.exit(1)

    # Compiler chaque objet
    compiled = []
    for obj, body in objects:
        filepath = compile_do(obj, body, output_dir)
        compiled.append(filepath)

    print("=== Compilation JSON Schema ===")
    print("Objets traités : %d" % len(compiled))
    print("Répertoire : %s" % os.path.relpath(output_dir, REPO_ROOT))

    # Validation optionnelle
    if args.validate:
        count, errors = validate_schemas(output_dir)
        if errors:
            print("\n[ERREUR] %d erreurs de validation :" % len(errors))
            for filepath, err in errors[:10]:
                print("  - %s : %s" % (os.path.relpath(filepath, REPO_ROOT), err))
            sys.exit(1)
        else:
            print("[OK] %d schémas valides." % count)

    print("\nRésumé : OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
