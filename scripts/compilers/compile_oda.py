#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compilateur ODA : transforme les fichiers d'auteur en schémas d'exécution.

Pont entre le Modèle de Gouvernance (YAML/Markdown) et le Modèle d'Implémentation
(JSON Schema, FHIR CodeSystem, OpenAPI).

Usage :
    python3 scripts/compilers/compile_oda.py                    # compile tout
    python3 scripts/compilers/compile_oda.py --validate         # valide après compilation
    python3 scripts/compilers/compile_oda.py --nomenclature FOSA-STATUS  # compile une nomenclature
    python3 scripts/compilers/compile_oda.py --check-governance # valide les fichiers d'auteur
"""

import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HEA_NS = "https://healmadagascar.mg"
FHIR_NS = "%s/fhir" % HEA_NS
SCHEMAS_NS = "%s/schemas" % HEA_NS

DO_FHIR_MAP = {
    "patient": {"json_type": "object", "fhir_resource": "Patient"},
    "identifiant": {"json_type": "string"},
    "dossier": {"json_type": "object", "fhir_resource": "Patient"},
    "evenement": {"json_type": "object", "fhir_resource": "Encounter"},
    "encounter": {"json_type": "object", "fhir_resource": "Encounter"},
    "observation": {"json_type": "object", "fhir_resource": "Observation"},
    "acte": {"json_type": "object", "fhir_resource": "Procedure"},
    "organisation": {"json_type": "object", "fhir_resource": "Organization"},
    "lieu": {"json_type": "object", "fhir_resource": "Location"},
    "praticien": {"json_type": "object", "fhir_resource": "Practitioner"},
    "prescription": {"json_type": "object", "fhir_resource": "MedicationRequest"},
    "dispensation": {"json_type": "object", "fhir_resource": "MedicationDispense"},
    "produit": {"json_type": "object", "fhir_resource": "Medication"},
    "laboratoire": {"json_type": "object", "fhir_resource": "Organization"},
    "signal": {"json_type": "object", "fhir_resource": "Flag"},
    "alerte": {"json_type": "object", "fhir_resource": "Flag"},
    "stock": {"json_type": "object"},
    "commande": {"json_type": "object", "fhir_resource": "MedicationRequest"},
    "facturation": {"json_type": "object", "fhir_resource": "Claim"},
    "remboursement": {"json_type": "object", "fhir_resource": "ClaimResponse"},
    "couverture": {"json_type": "object", "fhir_resource": "Coverage"},
    "adhesion": {"json_type": "object", "fhir_resource": "CoverageEligibilityRequest"},
    "prestation": {"json_type": "object", "fhir_resource": "ExplanationOfBenefit"},
    "compte": {"json_type": "object", "fhir_resource": "Account"},
    "utilisateur": {"json_type": "object", "fhir_resource": "Person"},
    "droit": {"json_type": "object", "fhir_resource": "Permission"},
    "journal": {"json_type": "object", "fhir_resource": "AuditEvent"},
    "configuration": {"json_type": "object"},
    "referentiel": {"json_type": "object"},
    "metrique": {"json_type": "object"},
    "rapport": {"json_type": "object", "fhir_resource": "DiagnosticReport"},
    "notification": {"json_type": "object", "fhir_resource": "Communication"},
}


def parse_frontmatter(text):
    """Extrait le frontmatter YAML d'un fichier Markdown."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return text[3:end].strip("\n")


def fm_field(fm, key):
    """Extrait un champ du frontmatter YAML (simple, sans PyYAML)."""
    m = re.search(r"^%s:\s*(.*)$" % re.escape(key), fm, re.MULTILINE)
    return m.group(1) if m else None


def list_value(raw):
    """Parse une liste YAML inline : ["a", "b"] ou [] ou a, b."""
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


def extract_table_from_body(body):
    """Extrait les lignes de tableau Markdown (| code | libellé | ...)."""
    rows = []
    for line in body.split("\n"):
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        # Skip separator rows (|---|---|)
        if re.match(r"^\|[\s\-:|]+\|$", stripped):
            continue
        parts = [p.strip() for p in stripped.split("|") if p.strip()]
        if len(parts) >= 3:
            # Skip header row
            if parts[0] in ("Code", "code", "---", "----"):
                continue
            rows.append(parts)
    return rows


def extract_concepts_from_body(body):
    """Extrait les concepts (code, libellé, description) depuis le corps Markdown."""
    concepts = []
    rows = extract_table_from_body(body)
    for row in rows:
        if len(row) >= 3:
            code = row[0].strip().strip("`")
            display = row[1].strip()
            definition = row[2].strip()
            status = row[3].strip() if len(row) > 3 else "active"
            concepts.append({
                "code": code,
                "display": display,
                "definition": definition,
                "status": status
            })
    return concepts


def resolve_fhir_resource(do_id, title, tags, body):
    """Résout la ressource FHIR à partir de l'ID, du titre, des tags et du corps.

    Priorité : titre > body (Référentiel source) > tags > ID.
    Le titre est la source la plus fiable pour le matching sémantique.
    """
    title_lower = title.lower()

    # 1. Try matching by title (most reliable semantic source)
    for keyword, info in DO_FHIR_MAP.items():
        if keyword in title_lower:
            return info

    # 2. Try matching by body — extract Référentiel source (explicit FHIR ref)
    ref_match = re.search(r"\*\*Référentiel source\*\*\s*:\s*(.+)", body)
    if ref_match:
        ref_text = ref_match.group(1).strip().lower()
        for keyword, info in DO_FHIR_MAP.items():
            if keyword in ref_text:
                return info

    # 3. Try matching by tags (fallback — can produce false positives)
    for tag in tags:
        tag_lower = tag.lower()
        for keyword, info in DO_FHIR_MAP.items():
            if keyword in tag_lower:
                return info

    # 4. Try matching by DO ID pattern
    do_id_lower = do_id.lower()
    for keyword, info in DO_FHIR_MAP.items():
        if keyword in do_id_lower:
            return info

    return {"json_type": "object"}


def extract_constraints(body):
    """Extrait les contraintes depuis **Contraintes** : ..."""
    m = re.search(r"\*\*Contraintes\*\*\s*:\s*(.+)", body)
    return m.group(1).strip() if m else None


def extract_source_ref(body):
    """Extrait le référentiel source depuis **Référentiel source** : ..."""
    m = re.search(r"\*\*Référentiel source\*\*\s*:\s*(.+)", body)
    return m.group(1).strip() if m else None


def extract_first_paragraph(body):
    """Extrait le premier paragraphe après le titre #."""
    lines = body.split("\n")
    in_title = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            in_title = True
            continue
        if in_title and stripped:
            return stripped
    return ""


def collect_do_objects():
    """Collecte tous les objets de données (DO-*) du référentiel."""
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

        # Extraire le corps (après le 2e ---)
        end = text.find("\n---", 3)
        body = text[end + 4:] if end != -1 else text

        obj = {
            "id": oid,
            "title": (fm_field(fm, "title") or oid).strip().strip('"'),
            "version": (fm_field(fm, "version") or "1.0.0").strip().strip('"'),
            "status": (fm_field(fm, "status") or "draft").strip().strip('"'),
            "owner": (fm_field(fm, "owner") or "DEPSI").strip().strip('"'),
            "tags": list_value(fm_field(fm, "tags") or "[]"),
            "related": list_value(fm_field(fm, "related") or "[]"),
            "body": body,
        }
        objects.append(obj)

    return objects


def generate_do_payload_schema(obj):
    """Génère un JSON Schema Draft-07 pour le payload d'un DO."""
    do_id = obj["id"]
    title = obj["title"]
    version = obj["version"]
    body = obj["body"]

    # Extraire le type d'objet
    type_info = resolve_fhir_resource(do_id, title, obj["tags"], body)

    # Extraire les contraintes
    constraints_text = extract_constraints(body)
    source_ref = extract_source_ref(body)
    description = extract_first_paragraph(body)

    # Construire les propriétés
    properties = {
        "id": {
            "type": "string",
            "description": "Identifiant unique de l'objet"
        },
        "version": {
            "type": "string",
            "description": "Version de l'objet",
            "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$"
        }
    }

    # Ajouter des propriétés basées sur les contraintes
    if constraints_text:
        cl = constraints_text.lower()
        if "identifiant" in cl or "nin" in cl:
            properties["identifiant"] = {"type": "string", "description": "Identifiant unique"}
        if "date" in cl:
            properties["date"] = {"type": "string", "format": "date-time", "description": "Date"}
        if "quantit" in cl:
            properties["quantite"] = {"type": "integer", "minimum": 0, "description": "Quantité"}
        if "lot" in cl:
            properties["lot"] = {"type": "string", "description": "Numéro de lot"}
        if "patient" in cl:
            properties["patientRef"] = {"type": "string", "description": "Référence au patient (DO-01)"}
        if "statut" in cl:
            properties["statut"] = {"type": "string", "description": "Statut de l'objet"}
        if "etablissement" in cl:
            properties["etablissementRef"] = {"type": "string", "description": "Référence à l'établissement"}

    # Ajouter les références relationnelles
    for rel_id in obj["related"]:
        prop_name = rel_id.lower().replace("-", "_") + "Ref"
        properties[prop_name] = {"type": "string", "description": "Référence à %s" % rel_id}

    # Construire le schéma
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "%s/payloads/%s.json" % (SCHEMAS_NS, do_id.lower()),
        "title": "%s — %s" % (do_id, title),
        "description": description or "Schéma de validation du payload %s." % do_id,
        "type": type_info["json_type"],
        "properties": properties,
        "required": ["id", "version"],
        "x-hea-id": do_id,
        "x-hea-type": "objet-de-donnees",
        "x-hea-version": version,
        "x-hea-status": obj["status"],
        "x-hea-owner": obj["owner"],
        "x-hea-fhir-resource": type_info.get("fhir_resource", ""),
    }

    if source_ref:
        schema["x-hea-source-ref"] = source_ref

    return schema


# ===================================================================
# GÉNÉRATION JSON Schema (Payload)
# ===================================================================

def generate_payload_schema(fm, concepts):
    """Génère un JSON Schema Draft-07 pour un payload de nomenclature."""
    nom_id = fm_field(fm, "id")
    title = fm_field(fm, "title") or nom_id
    version = fm_field(fm, "version") or "1.0.0"
    owner = fm_field(fm, "owner") or "DEPSI"

    codes = [c["code"] for c in concepts]

    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "%s/payloads/%s.json" % (SCHEMAS_NS, nom_id.lower()),
        "title": "%s - %s" % (nom_id, title),
        "description": "Schéma de validation du payload %s pour les messages REST du réseau national de santé." % nom_id,
        "type": "string",
        "enum": codes,
        "default": codes[0] if codes else None,
        "x-hea-nomenclature": nom_id,
        "x-hea-version": version,
        "x-hea-owner": owner,
        "x-hea-fhir-codesystem": "%s/CodeSystem/hea-%s" % (FHIR_NS, nom_id.lower())
    }

    return schema


# ===================================================================
# GÉNÉRATION FHIR CodeSystem
# ===================================================================

def generate_fhir_codesystem(fm, concepts):
    """Génère une ressource FHIR R4 CodeSystem pour une nomenclature."""
    nom_id = fm_field(fm, "id")
    title = fm_field(fm, "title") or nom_id
    version = fm_field(fm, "version") or "1.0.0"
    owner = fm_field(fm, "owner") or "DEPSI"
    fhir_url = fm_field(fm, "fhir_url") or "%s/CodeSystem/hea-%s" % (FHIR_NS, nom_id.lower())

    fhir_concepts = []
    for c in concepts:
        fhir_concept = {
            "code": c["code"],
            "display": c["display"],
            "definition": c["definition"],
            "property": [
                {"code": "status", "valueCode": c.get("status", "active")},
                {"code": "inactive", "valueBoolean": c.get("status") == "deprecated"}
            ]
        }
        fhir_concepts.append(fhir_concept)

    codesystem = {
        "resourceType": "CodeSystem",
        "id": "hea-%s" % nom_id.lower(),
        "meta": {
            "versionId": version,
            "lastUpdated": datetime.now().strftime("%Y-%m-%dT00:00:00+03:00"),
            "source": "%s/ontologie/hea#nomenclature/%s" % (HEA_NS, nom_id)
        },
        "url": fhir_url,
        "version": version,
        "name": "HEA%sCodeSystem" % nom_id.replace("-", ""),
        "title": "%s — %s" % (nom_id, title),
        "status": "active",
        "experimental": False,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "publisher": "%s - Madagascar" % owner,
        "description": title,
        "copyright": "Ministère de la Santé Publique - Madagascar",
        "content": "complete",
        "caseSensitive": True,
        "count": len(fhir_concepts),
        "concept": fhir_concepts
    }

    return codesystem


# ===================================================================
# COMPILATION PRINCIPALE
# ===================================================================

def collect_nomenclatures():
    """Collecte tous les fichiers nomenclature du référentiel."""
    nomenclatures = []
    patterns = [
        os.path.join(REPO_ROOT, "02_artsn", "03_objets-de-donnees", "nomenclatures", "*.md"),
        os.path.join(REPO_ROOT, "referentiel", "nomenclatures", "*.md"),
    ]

    for pattern in patterns:
        for path in sorted(glob.glob(pattern)):
            text = open(path, encoding="utf-8").read()
            fm = parse_frontmatter(text)
            if fm is None:
                continue

            otype = fm_field(fm, "type")
            if otype != "nomenclature":
                continue

            # Extraire le corps du document
            end = text.find("\n---", 3)
            body = text[end + 4:] if end != -1 else text

            # Extraire les concepts
            concepts = extract_concepts_from_body(body)
            if not concepts:
                print("[AVERTISSEMENT] Aucun concept trouvé dans %s" % os.path.relpath(path, REPO_ROOT))
                continue

            nomenclatures.append({
                "path": path,
                "frontmatter": fm,
                "concepts": concepts
            })

    return nomenclatures


def compile_nomenclature(nom, output_dir):
    """Compile une nomenclature en JSON Schema et FHIR CodeSystem."""
    fm = nom["frontmatter"]
    concepts = nom["concepts"]
    nom_id = fm_field(fm, "id")

    # Générer le JSON Schema payload
    payload_schema = generate_payload_schema(fm, concepts)
    payload_path = os.path.join(output_dir, "payloads", "%s.json" % nom_id.lower())
    os.makedirs(os.path.dirname(payload_path), exist_ok=True)
    with open(payload_path, "w", encoding="utf-8") as f:
        json.dump(payload_schema, f, indent=2, ensure_ascii=False)

    # Générer le FHIR CodeSystem
    codesystem = generate_fhir_codesystem(fm, concepts)
    cs_path = os.path.join(output_dir, "terminologies", "hea-%s-cs.json" % nom_id.lower())
    os.makedirs(os.path.dirname(cs_path), exist_ok=True)
    with open(cs_path, "w", encoding="utf-8") as f:
        json.dump(codesystem, f, indent=2, ensure_ascii=False)

    return payload_path, cs_path


def validate_governance():
    """Valide les fichiers d'auteur contre le méta-schéma de gouvernance."""
    schema_path = os.path.join(REPO_ROOT, "ontologie", "hea-governance-schema.json")
    if not os.path.exists(schema_path):
        print("[ERREUR] Méta-schéma de gouvernance introuvable : %s" % schema_path)
        return False

    with open(schema_path, encoding="utf-8") as f:
        governance_schema = json.load(f)

    errors = []
    warnings = []
    count = 0

    # Valider tous les fichiers d'auteur
    patterns = [
        os.path.join(REPO_ROOT, "02_artsn", "03_objets-de-donnees", "nomenclatures", "*.md"),
        os.path.join(REPO_ROOT, "referentiel", "objets-de-donnees", "do-*.md"),
        os.path.join(REPO_ROOT, "referentiel", "profils", "pt-*.md"),
    ]

    for pattern in patterns:
        for path in sorted(glob.glob(pattern)):
            text = open(path, encoding="utf-8").read()
            fm = parse_frontmatter(text)
            if fm is None:
                continue

            count += 1
            rel_path = os.path.relpath(path, REPO_ROOT)
            otype = fm_field(fm, "type")
            is_nomenclature = otype and otype.strip('"').strip("'") == "nomenclature"

            # Vérifications manuelles (sans jsonschema)
            required_fields = governance_schema.get("required", [])
            for field in required_fields:
                val = fm_field(fm, field)
                if val is None:
                    if is_nomenclature:
                        errors.append((rel_path, "Champ obligatoire manquant : %s" % field))
                    else:
                        warnings.append((rel_path, "Champ recommandé manquant : %s" % field))

            # Champs supplémentaires obligatoires pour les nomenclatures
            if is_nomenclature:
                for field in ["niveau", "artRef", "maps_to", "implements"]:
                    val = fm_field(fm, field)
                    if val is None:
                        errors.append((rel_path, "Nomenclature : champ obligatoire manquant : %s" % field))

            # Vérifier le pattern de l'id
            oid = fm_field(fm, "id")
            if oid and not re.match(r"^[A-Z][A-Z0-9-]+$", oid.strip('"').strip("'")):
                errors.append((rel_path, "L'id doit être uppercase kebab-case : %s" % oid))

            # Vérifier le status
            status = fm_field(fm, "status")
            if status and status.strip('"').strip("'") not in ("draft", "active", "stable", "candidate", "deprecated"):
                errors.append((rel_path, "Status invalide : %s" % status))

            # Vérifier la version (accepte semver complet ou partiel)
            version = fm_field(fm, "version")
            if version:
                v = version.strip('"').strip("'")
                if not re.match(r"^[0-9]+\.[0-9]+(\.[0-9]+)?$", v):
                    errors.append((rel_path, "Version invalide (attendu semver) : %s" % version))

    print("=== Validation Gouvernance ===")
    print("Fichiers vérifiés : %d" % count)

    if warnings:
        print("\n[AVERTISSEMENT] %d avertissements (champs recommandés manquants) :" % len(warnings))
        for path, warn in warnings[:10]:
            print("  ~ %s : %s" % (path, warn))
        if len(warnings) > 10:
            print("  ... et %d autres" % (len(warnings) - 10))

    if errors:
        print("\n[ERREUR] %d erreurs de gouvernance :" % len(errors))
        for path, err in errors[:20]:
            print("  - %s : %s" % (path, err))
        return False
    else:
        print("[OK] Tous les fichiers sont conformes au méta-schéma de gouvernance.")
        return True


def main():
    parser = argparse.ArgumentParser(
        description="Compilateur ODA : transforme les fichiers d'auteur en schémas d'exécution")
    parser.add_argument("--output", "-o", default=None,
                        help="Répertoire de sortie (défaut: 03_ptisn/schemas/)")
    parser.add_argument("--validate", action="store_true",
                        help="Valider après compilation")
    parser.add_argument("--check-governance", action="store_true",
                        help="Valider les fichiers d'auteur contre le méta-schéma")
    parser.add_argument("--nomenclature", type=str, default=None,
                        help="Compiler une nomenclature spécifique (ex: FOSA-STATUS)")
    args = parser.parse_args()

    if args.check_governance:
        ok = validate_governance()
        sys.exit(0 if ok else 1)

    output_dir = args.output or os.path.join(REPO_ROOT, "03_ptisn", "schemas")
    os.makedirs(output_dir, exist_ok=True)

    # Collecter les nomenclatures
    nomenclatures = collect_nomenclatures()
    if not nomenclatures:
        print("[AVERTISSEMENT] Aucune nomenclature trouvée.")
        print("Usage : placez des fichiers .md avec type: nomenclature dans")
        print("  02_artsn/03_objets-de-donnees/nomenclatures/ ou")
        print("  referentiel/nomenclatures/")
        sys.exit(0)

    # Filtrer si une nomenclature spécifique est demandée
    if args.nomenclature:
        nomenclatures = [n for n in nomenclatures
                        if fm_field(n["frontmatter"], "id") == args.nomenclature]
        if not nomenclatures:
            print("[ERREUR] Nomenclature introuvable : %s" % args.nomenclature)
            sys.exit(1)

    # Compiler chaque nomenclature
    compiled = []
    for nom in nomenclatures:
        payload_path, cs_path = compile_nomenclature(nom, output_dir)
        compiled.append((nom["frontmatter"], payload_path, cs_path))

    print("=== Compilation ODA ===")
    print("Nomenclatures traitées : %d" % len(compiled))
    print("Répertoire : %s" % os.path.relpath(output_dir, REPO_ROOT))

    for fm, payload_path, cs_path in compiled:
        nom_id = fm_field(fm, "id")
        print("  %s:" % nom_id)
        print("    Payload : %s" % os.path.relpath(payload_path, REPO_ROOT))
        print("    FHIR : %s" % os.path.relpath(cs_path, REPO_ROOT))

    # Compiler les objets de données (DO)
    do_objects = collect_do_objects()
    do_compiled = []
    for obj in do_objects:
        schema = generate_do_payload_schema(obj)
        do_id = obj["id"]
        payload_path = os.path.join(output_dir, "payloads", "%s.json" % do_id.lower())
        os.makedirs(os.path.dirname(payload_path), exist_ok=True)
        with open(payload_path, "w", encoding="utf-8") as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
        do_compiled.append((do_id, payload_path))

    print("\n=== Compilation ODA — Objets de données ===")
    print("DO traités : %d" % len(do_compiled))
    for do_id, payload_path in do_compiled:
        print("  %s → %s" % (do_id, os.path.relpath(payload_path, REPO_ROOT)))

    # Validation optionnelle
    if args.validate:
        print("\n=== Validation des schémas générés ===")
        all_ok = True

        # Valider les schémas nomenclature
        for fm, payload_path, cs_path in compiled:
            for path in [payload_path, cs_path]:
                try:
                    with open(path, encoding="utf-8") as f:
                        json.load(f)
                    print("[OK] %s" % os.path.relpath(path, REPO_ROOT))
                except json.JSONDecodeError as e:
                    print("[ERREUR] %s : %s" % (os.path.relpath(path, REPO_ROOT), e))
                    all_ok = False

        # Valider les schémas DO
        for do_id, payload_path in do_compiled:
            try:
                with open(payload_path, encoding="utf-8") as f:
                    json.load(f)
                print("[OK] %s" % os.path.relpath(payload_path, REPO_ROOT))
            except json.JSONDecodeError as e:
                print("[ERREUR] %s : %s" % (os.path.relpath(payload_path, REPO_ROOT), e))
                all_ok = False

        if not all_ok:
            sys.exit(1)

    total = len(compiled) + len(do_compiled)
    print("\nRésumé : %d schémas compilés (nomenclatures: %d, DO: %d)" % (total, len(compiled), len(do_compiled)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
