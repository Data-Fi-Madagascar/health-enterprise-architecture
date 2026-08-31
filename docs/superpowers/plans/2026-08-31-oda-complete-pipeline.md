# ODA Complete Pipeline — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete the ODA pipeline so it generates payload schemas for all 31 DOs and derives OpenAPI specs from PT YAML, producing a full implementation model in `03_ptisn/schemas/`.

**Architecture:** Extend `compile_oda.py` to handle DOs (not just nomenclatures), rewrite `compile_openapi.py` to derive from PT YAML frontmatter/transactions, fix the fosa-status bug, and wire everything through `compile_all.py` + CI.

**Tech Stack:** Python 3, JSON Schema Draft-07, OpenAPI 3.0.3, FHIR R4 CodeSystem/ValueSet

---

## Context

### Current state
- `compile_oda.py` — only handles nomenclatures (1 file: fosa-status). Generates payload JSON Schema + FHIR CodeSystem to `03_ptisn/schemas/`
- `compile_jsonschema.py` — generates JSON Schema for 31 DOs to `dist/schemas/` (separate from ODA)
- `compile_fhir.py` — generates FHIR resources for 31 DOs to `dist/fhir/`
- `compile_openapi.py` — hardcoded OpenAPI 3.0.3 for 4 PTs (PT-01/03/06/07), not derived from YAML
- `compile_all.py` — orchestrates rdf→jsonschema→fhir→openapi sequentially

### Bugs found
- `fosa-status.json` has a parasite enum value: `"- \`status\` : statut du concept dans le code system (active"` — the `extract_concepts_from_body()` function captures markdown bullet lines containing `|` as table rows
- `hea-fosa-status-cs.json` has 6 concepts instead of 5 — same bug propagated to FHIR CodeSystem

### Architecture decision
The ODA implementation model lives in `03_ptisn/schemas/`:
- `payloads/*.json` — JSON Schema Draft-07 for REST message validation
- `terminologies/*.json` — FHIR R4 CodeSystem/ValueSet
- `openapi/*.json` — OpenAPI 3.0.3 derived from PT YAML

The `dist/` folder continues to hold compilation artifacts (RDF, JSON Schema from DOs, FHIR from DOs, OpenAPI from PTs). The ODA schemas in `03_ptisn/schemas/` are the **authoritative implementation contracts** referenced by PTISN profiles.

---

## File Structure

| Action | File | Responsibility |
|--------|------|----------------|
| Fix | `scripts/compilers/compile_oda.py:61-93` | Fix `extract_concepts_from_body()` to skip bullet lines |
| Extend | `scripts/compilers/compile_oda.py` | Add DO→payload compilation (31 DOs → 31 payload schemas) |
| Rewrite | `scripts/compilers/compile_openapi.py` | Derive OpenAPI from PT YAML instead of hardcoded |
| Modify | `scripts/compilers/compile_all.py` | Add ODA step (nomenclatures + DOs) |
| Modify | `.github/workflows/ci.yml` | Add ODA validation step |
| Regenerate | `03_ptisn/schemas/payloads/fosa-status.json` | Fix parasite enum |
| Regenerate | `03_ptisn/schemas/terminologies/hea-fosa-status-cs.json` | Fix parasite concept |
| Create | `03_ptisn/schemas/payloads/do-01.json` ... `do-31.json` | 31 payload schemas |
| Create/Overwrite | `03_ptisn/schemas/openapi/pt-*.json` | OpenAPI derived from YAML |

---

## Task 1: Fix fosa-status extraction bug

**Files:**
- Modify: `scripts/compilers/compile_oda.py:61-93`
- Regenerate: `03_ptisn/schemas/payloads/fosa-status.json`
- Regenerate: `03_ptisn/schemas/terminologies/hea-fosa-status-cs.json`

- [ ] **Step 1: Identify the bug in `extract_concepts_from_body()`**

The function at line 61-93 in `compile_oda.py` iterates all lines with `|` and splits by `|`. The markdown body has:

```markdown
- **Contraintes** : Unicité : Chaque code est unique au sein de cette nomenclature
...
| Code | Libellé | Description | Statut |
|------|---------|-------------|--------|
| `actif` | Actif | ... | active |
...
- `status` : statut du concept dans le code system (active | deprecated | retired)
```

The bullet line contains `|` (in `active | deprecated | retired`) and gets captured as a row. The header detection only skips `Code`, `---`, `----` — not bullet lines.

- [ ] **Step 2: Fix `extract_concepts_from_body()` to skip non-table lines**

Replace the function in `compile_oda.py`:

```python
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
```

Key changes:
- Only process lines starting with `|`
- Use regex to skip separator rows (`|---|---|`)
- Check `len(parts) >= 3` (need at least code + label + description)

- [ ] **Step 3: Run compilation and verify output**

```bash
cd /Users/dimbinirina/Work/Palladium/hea
.venv/bin/python3 scripts/compilers/compile_oda.py --nomenclature FOSA-STATUS --validate
```

Expected output:
- `03_ptisn/schemas/payloads/fosa-status.json` — enum with exactly 5 values: `["actif", "inactif", "temporaire", "ferme", "projet"]`
- `03_ptisn/schemas/terminologies/hea-fosa-status-cs.json` — count: 5, concept array with 5 entries
- No parasite values

- [ ] **Step 4: Verify the generated files**

Check `03_ptisn/schemas/payloads/fosa-status.json`:
```json
{
  "enum": ["actif", "inactif", "temporaire", "ferme", "projet"]
}
```

Check `03_ptisn/schemas/terminologies/hea-fosa-status-cs.json`:
```json
{
  "count": 5,
  "concept": [{"code": "actif"}, {"code": "inactif"}, {"code": "temporaire"}, {"code": "ferme"}, {"code": "projet"}]
}
```

- [ ] **Step 5: Commit**

```bash
git add scripts/compilers/compile_oda.py 03_ptisn/schemas/payloads/fosa-status.json 03_ptisn/schemas/terminologies/hea-fosa-status-cs.json
git commit -m "fix(oda): fix fosa-status extraction bug - skip markdown bullet lines"
```

---

## Task 2: Extend compile_oda.py with DO→payload compilation

**Files:**
- Modify: `scripts/compilers/compile_oda.py` (add DO collection + payload generation)

- [ ] **Step 1: Add DO type-to-FHIR mapping at the top of compile_oda.py**

After the existing constants (line ~27), add:

```python
# Mapping DO type keywords → JSON Schema type + FHIR resource
DO_FHIR_MAP = {
    "patient": {"json_type": "object", "fhir_resource": "Patient", "fhir_profile": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"},
    "identifiant": {"json_type": "string", "fhir_resource": "Identifier"},
    "dossier": {"json_type": "object", "fhir_resource": "Patient"},
    "evenement": {"json_type": "object", "fhir_resource": "Encounter"},
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
    "stock": {"json_type": "object", "fhir_resource": "InventoryItem"},
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
```

- [ ] **Step 2: Add DO extraction functions**

After the existing `extract_concepts_from_body()` function, add:

```python
def extract_do_type(body):
    """Extrait le type d'objet depuis **Type** : ... dans le corps."""
    m = re.search(r"\*\*Type\*\*\s*:\s*(.+)", body)
    return m.group(1).strip().lower() if m else None


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
```

- [ ] **Step 3: Add `collect_do_objects()` function**

```python
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
```

- [ ] **Step 4: Add `generate_do_payload_schema()` function**

```python
def generate_do_payload_schema(obj):
    """Génère un JSON Schema Draft-07 pour le payload d'un DO."""
    do_id = obj["id"]
    title = obj["title"]
    version = obj["version"]
    body = obj["body"]

    # Extraire le type d'objet
    do_type = extract_do_type(body)
    type_info = DO_FHIR_MAP.get(do_type, {"json_type": "object"})

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
        "$id": "%s/schemas/payloads/%s.json" % (SCHEMAS_NS, do_id.lower()),
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

    if type_info.get("fhir_profile"):
        schema["x-hea-fhir-profile"] = type_info["fhir_profile"]

    if source_ref:
        schema["x-hea-source-ref"] = source_ref

    return schema
```

- [ ] **Step 5: Add DO compilation to `main()`**

In `main()`, after the nomenclature compilation block (around line 368), add DO compilation:

```python
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
```

- [ ] **Step 6: Run and verify**

```bash
.venv/bin/python3 scripts/compilers/compile_oda.py --validate
```

Expected:
- 1 nomenclature (fosa-status) → payload + FHIR CodeSystem
- 31 DOs → 31 payload schemas in `03_ptisn/schemas/payloads/`
- All files valid JSON

Check a sample:
```bash
cat 03_ptisn/schemas/payloads/do-01.json | python3 -m json.tool | head -20
```

Expected: `"$id": "https://healmadagascar.mg/schemas/payloads/do-01.json"`, `"x-hea-fhir-resource": "Patient"`

- [ ] **Step 7: Commit**

```bash
git add scripts/compilers/compile_oda.py 03_ptisn/schemas/payloads/
git commit -m "feat(oda): extend compile_oda.py to generate payload schemas for 31 DOs"
```

---

## Task 3: Rewrite compile_openapi.py to derive from PT YAML

**Files:**
- Rewrite: `scripts/compilers/compile_openapi.py`

- [ ] **Step 1: Replace the entire file with YAML-derived compiler**

The new compiler will:
1. Read each `referentiel/profils/pt-*.md`
2. Extract frontmatter (title, id, version, status, owner, implements, maps_to)
3. Parse the Transactions table from the body (section 5)
4. Parse Content Modules from the body (section 6)
5. Generate an OpenAPI 3.0.3 spec with paths derived from transactions
6. Map content modules to FHIR schemas in components/schemas

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compile les profils techniques HEA en spécifications OpenAPI 3.0.

Dérive les spécifications OpenAPI à partir du YAML/Markdown des PT
plutôt que de les hardcoder.

Usage :
    python3 scripts/compilers/compile_openapi.py              # génère dist/openapi/
    python3 scripts/compilers/compile_openapi.py --validate   # valide les specs
    python3 scripts/compilers/compile_openapi.py --output /tmp/...  # répertoire custom
"""

import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPENAPI_VERSION = "3.0.3"
FHIR_NS = "https://healmadagascar.mg/fhir"
HEA_NS = "https://healmadagascar.mg"

# Mapping des standards IHE → FHIR resources
IHE_FHIR_MAP = {
    "IHE mCSD": {
        "resources": ["Organization", "Location", "HealthcareService"],
        "base_url": "/fhir",
        "tags": ["mCSD"],
    },
    "IHE SVCM": {
        "resources": ["CodeSystem", "ValueSet", "ConceptMap"],
        "base_url": "/fhir",
        "tags": ["SVCM"],
    },
    "IHE PDQ": {
        "resources": ["Patient"],
        "base_url": "/fhir",
        "tags": ["PDQ"],
    },
    "IHE PIX": {
        "resources": ["Patient"],
        "base_url": "/fhir",
        "tags": ["PIX"],
    },
    "X-Road": {
        "resources": [],
        "base_url": "/api/v1",
        "tags": ["X-Road"],
    },
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


def extract_transactions(body):
    """Extrait les transactions depuis le tableau de la section 5."""
    transactions = []
    in_table = False
    header_skipped = False

    for line in body.split("\n"):
        stripped = line.strip()
        if not stripped.startswith("|"):
            if in_table:
                break
            continue

        in_table = True
        parts = [p.strip() for p in stripped.split("|") if p.strip()]

        # Skip header row and separator
        if not header_skipped:
            if parts and parts[0] in ("Transaction", "transaction"):
                header_skipped = True
            continue

        if len(parts) >= 4:
            transactions.append({
                "name": parts[0],
                "actors": parts[1],
                "required": parts[2].upper() == "R",
                "standard": parts[3],
            })

    return transactions


def extract_content_modules(body):
    """Extrait les content modules (FHIR resources) depuis la section 6."""
    modules = []
    in_section = False

    for line in body.split("\n"):
        stripped = line.strip()
        if stripped.startswith("## 6.") or "Content Module" in stripped:
            in_section = True
            continue
        if in_section and stripped.startswith("## "):
            break
        if in_section and stripped.startswith("- **"):
            m = re.match(r"-\s+\*\*(.+?)\*\*\s*:\s*(.+)", stripped)
            if m:
                modules.append({"name": m.group(1), "description": m.group(2)})

    return modules


def extract_actors(body):
    """Extrait les acteurs depuis la section 4."""
    actors = []
    in_section = False

    for line in body.split("\n"):
        stripped = line.strip()
        if stripped.startswith("## 4.") or "Acteurs" in stripped:
            in_section = True
            continue
        if in_section and stripped.startswith("## "):
            break
        if in_section and stripped.startswith("- **"):
            m = re.match(r"-\s+\*\*(.+?)\*\*\s*[—–-]\s*(.+)", stripped)
            if m:
                actors.append({"name": m.group(1), "description": m.group(2)})

    return actors


def extract_first_paragraph_after_title(body):
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


def detect_ihe_standards(implements, body):
    """Détecte les standards IHE utilisés par ce PT."""
    standards = set()
    for impl in implements:
        impl_upper = impl.upper()
        if "MCCSD" in impl_upper or "MCSD" in impl_upper or "IHE MCSD" in impl_upper:
            standards.add("IHE mCSD")
        elif "SVCM" in impl_upper:
            standards.add("IHE SVCM")
        elif "PDQ" in impl_upper:
            standards.add("IHE PDQ")
        elif "PIX" in impl_upper:
            standards.add("IHE PIX")

    # Also check body text
    body_upper = body.upper()
    if "MCSD" in body_upper or "CARE SERVICES DISCOVERY" in body_upper:
        standards.add("IHE mCSD")
    if "SVCM" in body_upper or "SHARING VALUESETS" in body_upper:
        standards.add("IHE SVCM")
    if "X-ROAD" in body_upper:
        standards.add("X-Road")

    return list(standards)


def generate_openapi_from_pt(pt_fm, body, pt_id):
    """Génère une spécification OpenAPI 3.0 à partir du YAML d'un PT."""
    title = (fm_field(pt_fm, "title") or pt_id).strip().strip('"')
    version = (fm_field(pt_fm, "version") or "0.1.0").strip().strip('"')
    owner = (fm_field(pt_fm, "owner") or "DEPSI").strip().strip('"')
    implements = list_value(fm_field(pt_fm, "implements") or "[]")
    maps_to = list_value(fm_field(pt_fm, "maps_to") or "[]")

    description = extract_first_paragraph_after_title(body)
    transactions = extract_transactions(body)
    content_modules = extract_content_modules(body)
    actors = extract_actors(body)
    standards = detect_ihe_standards(implements, body)

    # Déterminer les standards IHE
    ihe_info = {}
    for std in standards:
        if std in IHE_FHIR_MAP:
            ihe_info[std] = IHE_FHIR_MAP[std]

    # Base URL
    base_url = "https://health.mg/api/v1"
    if ihe_info:
        first_std = list(ihe_info.values())[0]
        base_url = "https://fhir.health.mg" + first_std["base_url"]

    # Tags
    all_tags = set()
    for info in ihe_info.values():
        all_tags.update(info["tags"])
    if not all_tags:
        all_tags = {pt_id}

    # Paths depuis les transactions
    paths = {}
    schemas = {}

    # Générer les paths pour chaque transaction
    for i, txn in enumerate(transactions):
        txn_name = txn["name"]
        # Extraire le nom court (avant la —)
        short_name = txn_name.split("—")[0].strip() if "—" in txn_name else txn_name.split("-")[0].strip()
        # Slugifier
        path_name = re.sub(r"[^a-zA-Z0-9]+", "-", short_name).strip("-").lower()
        if not path_name:
            path_name = "transaction-%d" % (i + 1)

        path = "/%s" % path_name
        method = "post" if txn.get("required", True) else "get"

        # Générer le schema de réponse
        response_schema = None
        if content_modules:
            first_module = content_modules[0]["name"]
            # Mapper vers un schema FHIR
            fhir_resource = first_module.split(":")[0].strip() if ":" in first_module else first_module
            if fhir_resource.startswith("HL7 FHIR "):
                fhir_resource = fhir_resource[9:]
            response_schema = {"$ref": "#/components/schemas/%s" % fhir_resource}
            schemas[fhir_resource] = _generate_fhir_schema(fhir_resource)

        operation = {
            "operationId": "operation%s" % path_name.replace("-",.title()),
            "summary": txn_name,
            "description": "Transaction %s" % txn_name,
            "tags": list(all_tags),
            "responses": {
                "200": {
                    "description": "Succès",
                    "content": {
                        "application/json": {
                            "schema": response_schema or {"type": "object"}
                        }
                    } if response_schema else {}
                },
                "400": {"description": "Requête invalide"},
                "500": {"description": "Erreur serveur"},
            }
        }

        if method == "post":
            operation["requestBody"] = {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": response_schema or {"type": "object"}
                    }
                }
            }

        paths[path] = {method: operation}

    # Ajouter des paths pour les content modules FHIR
    for module in content_modules:
        name = module["name"]
        description_text = module["description"]
        # Extraire le nom FHIR
        fhir_resource = name.split(":")[0].strip() if ":" in name else name
        if fhir_resource.startswith("HL7 FHIR "):
            fhir_resource = fhir_resource[9:]

        if fhir_resource not in schemas:
            schemas[fhir_resource] = _generate_fhir_schema(fhir_resource)

        # GET /{Resource}
        resource_path = "/%s" % fhir_resource
        if resource_path not in paths:
            paths[resource_path] = {
                "get": {
                    "operationId": "search%s" % fhir_resource,
                    "summary": "Rechercher des %s" % fhir_resource.lower(),
                    "description": description_text,
                    "tags": list(all_tags),
                    "parameters": [
                        {"name": "_count", "in": "query", "schema": {"type": "integer"}, "description": "Nombre max de résultats"}
                    ],
                    "responses": {
                        "200": {
                            "description": "Bundle de résultats",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/FHIRBundle"}
                                }
                            }
                        }
                    }
                },
                "post": {
                    "operationId": "create%s" % fhir_resource,
                    "summary": "Créer un %s" % fhir_resource.lower(),
                    "description": description_text,
                    "tags": list(all_tags),
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/%s" % fhir_resource}
                            }
                        }
                    },
                    "responses": {
                        "201": {"description": "%s créé" % fhir_resource}
                    }
                }
            }

        # GET /{Resource}/{id}
        resource_id_path = "/%s/{id}" % fhir_resource
        if resource_id_path not in paths:
            paths[resource_id_path] = {
                "get": {
                    "operationId": "get%s" % fhir_resource,
                    "summary": "Récupérer un %s par ID" % fhir_resource.lower(),
                    "tags": list(all_tags),
                    "parameters": [
                        {"name": "id", "in": "path", "required": True, "schema": {"type": "string"}}
                    ],
                    "responses": {
                        "200": {
                            "description": "%s trouvé" % fhir_resource,
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/%s" % fhir_resource}
                                }
                            }
                        },
                        "404": {"description": "%s non trouvé" % fhir_resource}
                    }
                }
            }

    # Ajouter les schemas FHIR de base
    schemas["FHIRBundle"] = {
        "type": "object",
        "properties": {
            "resourceType": {"type": "string", "const": "Bundle"},
            "type": {"type": "string", "enum": ["searchset", "transaction", "batch"]},
            "total": {"type": "integer"},
            "entry": {"type": "array", "items": {"type": "object"}},
        }
    }
    schemas["FHIRIdentifier"] = {
        "type": "object",
        "properties": {
            "system": {"type": "string"},
            "value": {"type": "string"},
        }
    }

    # Construire la spec
    spec = {
        "openapi": OPENAPI_VERSION,
        "info": {
            "title": "HEA - %s (%s)" % (title, pt_id),
            "description": description or "Spécification OpenAPI pour %s" % title,
            "version": version,
            "contact": {"name": "%s - Madagascar" % owner},
        },
        "servers": [
            {"url": base_url, "description": "Point d'accès national"}
        ],
        "paths": paths,
        "components": {
            "schemas": schemas,
        }
    }

    # Security schemes si X-Road
    if "X-Road" in standards:
        spec["components"]["securitySchemes"] = {
            "xroadHeader": {
                "type": "apiKey",
                "in": "header",
                "name": "X-Road-Client",
                "description": "Identifiant du membre X-Road",
            }
        }
        spec["security"] = [{"xroadHeader": []}]

    return spec


def _generate_fhir_schema(resource_type):
    """Génère un JSON Schema basique pour une ressource FHIR."""
    common_props = {
        "resourceType": {"type": "string", "const": resource_type},
        "id": {"type": "string", "description": "Identifiant de la ressource"},
        "meta": {
            "type": "object",
            "properties": {
                "versionId": {"type": "string"},
                "lastUpdated": {"type": "string", "format": "date-time"},
            }
        },
    }

    # Propriétés spécifiques par type
    specific = {
        "Patient": {
            "identifier": {"type": "array", "items": {"$ref": "#/components/schemas/FHIRIdentifier"}},
            "name": {"type": "array", "items": {"type": "object"}},
            "gender": {"type": "string", "enum": ["male", "female", "other", "unknown"]},
            "birthDate": {"type": "string", "format": "date"},
            "active": {"type": "boolean"},
        },
        "Organization": {
            "identifier": {"type": "array", "items": {"$ref": "#/components/schemas/FHIRIdentifier"}},
            "name": {"type": "string"},
            "type": {"type": "array", "items": {"type": "object"}},
            "active": {"type": "boolean"},
            "address": {"type": "array", "items": {"type": "object"}},
        },
        "Location": {
            "identifier": {"type": "array", "items": {"$ref": "#/components/schemas/FHIRIdentifier"}},
            "name": {"type": "string"},
            "status": {"type": "string", "enum": ["active", "suspended", "inactive"]},
            "type": {"type": "array", "items": {"type": "object"}},
            "position": {
                "type": "object",
                "properties": {
                    "longitude": {"type": "number"},
                    "latitude": {"type": "number"},
                }
            },
        },
        "HealthcareService": {
            "identifier": {"type": "array", "items": {"$ref": "#/components/schemas/FHIRIdentifier"}},
            "name": {"type": "string"},
            "active": {"type": "boolean"},
            "providedBy": {"type": "object"},
        },
        "Encounter": {
            "identifier": {"type": "array", "items": {"$ref": "#/components/schemas/FHIRIdentifier"}},
            "status": {"type": "string"},
            "class": {"type": "object"},
            "subject": {"type": "object"},
            "period": {"type": "object"},
        },
        "CodeSystem": {
            "url": {"type": "string"},
            "version": {"type": "string"},
            "name": {"type": "string"},
            "status": {"type": "string", "enum": ["draft", "active", "retired", "unknown"]},
            "content": {"type": "string", "enum": ["not-present", "example", "fragment", "complete", "supplement"]},
            "concept": {"type": "array", "items": {"type": "object"}},
        },
        "ValueSet": {
            "url": {"type": "string"},
            "version": {"type": "string"},
            "name": {"type": "string"},
            "status": {"type": "string"},
            "compose": {"type": "object"},
        },
        "ConceptMap": {
            "url": {"type": "string"},
            "version": {"type": "string"},
            "name": {"type": "string"},
            "status": {"type": "string"},
            "source": {"type": "string"},
            "target": {"type": "string"},
        },
    }

    props = dict(common_props)
    if resource_type in specific:
        props.update(specific[resource_type])

    return {
        "type": "object",
        "properties": props,
    }


def compile_openapi_specs(output_dir):
    """Compile toutes les specs OpenAPI à partir des PT YAML."""
    specs = []
    pattern = os.path.join(REPO_ROOT, "referentiel", "profils", "pt-*.md")

    for path in sorted(glob.glob(pattern)):
        text = open(path, encoding="utf-8").read()
        fm = parse_frontmatter(text)
        if fm is None:
            continue

        pt_id = fm_field(fm, "id")
        if not pt_id:
            continue

        # Extraire le corps
        end = text.find("\n---", 3)
        body = text[end + 4:] if end != -1 else text

        # Générer la spec OpenAPI
        spec = generate_openapi_from_pt(fm, body, pt_id)

        # Écrire le fichier
        filename = "%s.json" % pt_id.lower()
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(spec, f, indent=2, ensure_ascii=False)
        specs.append(filepath)

    return specs


def validate_openapi_specs(output_dir):
    """Valide les spécifications OpenAPI générées."""
    errors = []
    count = 0

    for filepath in sorted(glob.glob(os.path.join(output_dir, "pt-*.json"))):
        count += 1
        try:
            with open(filepath, encoding="utf-8") as f:
                spec = json.load(f)

            if "openapi" not in spec:
                errors.append((filepath, "Champ openapi manquant"))
            if "info" not in spec:
                errors.append((filepath, "Champ info manquant"))
            if "paths" not in spec:
                errors.append((filepath, "Champ paths manquant"))
            if not spec.get("paths"):
                errors.append((filepath, "Aucune path générée"))

        except json.JSONDecodeError as e:
            errors.append((filepath, "JSON invalide: %s" % str(e)))

    return count, errors


def main():
    parser = argparse.ArgumentParser(
        description="Compile les profils techniques HEA en OpenAPI 3.0 (dérivé du YAML)")
    parser.add_argument("--output", "-o", default=None,
                        help="Répertoire de sortie (défaut: dist/openapi/)")
    parser.add_argument("--validate", action="store_true",
                        help="Valider les specs après compilation")
    args = parser.parse_args()

    output_dir = args.output or os.path.join(REPO_ROOT, "dist", "openapi")
    os.makedirs(output_dir, exist_ok=True)

    compiled = compile_openapi_specs(output_dir)

    print("=== Compilation OpenAPI 3.0 (dérivée du YAML) ===")
    print("Spécifications générées : %d" % len(compiled))
    print("Répertoire : %s" % os.path.relpath(output_dir, REPO_ROOT))

    for fp in compiled:
        print("  %s" % os.path.relpath(fp, REPO_ROOT))

    if args.validate:
        count, errors = validate_openapi_specs(output_dir)
        if errors:
            print("\n[ERREUR] %d erreurs de validation :" % len(errors))
            for filepath, err in errors[:10]:
                print("  - %s : %s" % (os.path.relpath(filepath, REPO_ROOT), err))
            sys.exit(1)
        else:
            print("[OK] %s spécifications valides." % count)

    print("\nRésumé : OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Run and verify OpenAPI generation**

```bash
.venv/bin/python3 scripts/compilers/compile_openapi.py --validate
```

Expected:
- 19 specs generated (one per PT)
- All valid JSON
- Each spec has paths derived from the PT's transactions and content modules

Check a sample:
```bash
cat dist/openapi/pt-06.json | python3 -m json.tool | head -30
```

Expected: paths with `/Organization`, `/Location`, `/HealthcareService`, tags `["mCSD"]`

- [ ] **Step 3: Verify PT-01 (X-Road)**

```bash
cat dist/openapi/pt-01.json | python3 -m json.tool | grep -A2 "securitySchemes"
```

Expected: `xroadHeader` security scheme present

- [ ] **Step 4: Commit**

```bash
git add scripts/compilers/compile_openapi.py dist/openapi/
git commit -m "feat(oda): derive OpenAPI specs from PT YAML instead of hardcoding"
```

---

## Task 4: Update compile_all.py and CI

**Files:**
- Modify: `scripts/compilers/compile_all.py`
- Modify: `.github/workflows/ci.yml`

- [ ] **Step 1: Add ODA step to compile_all.py**

After the OpenAPI compilation block, add:

```python
    # --- ODA ---
    print("\n--- ODA (Nomenclatures + DO Payloads) ---")
    oda_script = os.path.join(REPO_ROOT, "scripts", "compilers", "compile_oda.py")
    subprocess.run([sys.executable, oda_script, "--validate"], check=True)
```

Also add ODA governance check:

```python
    # --- ODA Governance ---
    print("\n--- ODA Governance ---")
    subprocess.run([sys.executable, oda_script, "--check-governance"], check=True)
```

- [ ] **Step 2: Add ODA validation step to CI**

In `.github/workflows/ci.yml`, after the existing "Validation finale" step, add:

```yaml
      - name: ODA — Compilation nomenclatures + DO payloads
        run: python3 scripts/compilers/compile_oda.py --validate

      - name: ODA — Validation gouvernance
        run: python3 scripts/compilers/compile_oda.py --check-governance
```

- [ ] **Step 3: Run full pipeline and verify**

```bash
.venv/bin/python3 scripts/compilers/compile_all.py --validate
```

Expected:
- RDF/OWL: OK
- JSON Schema: 31 schemas
- FHIR R4: 33 resources
- OpenAPI: 19 specs (was 4)
- ODA: 32 payload schemas (31 DO + 1 nomenclature) + 1 FHIR CodeSystem
- Governance: 51 files conformant

- [ ] **Step 4: Commit**

```bash
git add scripts/compilers/compile_all.py .github/workflows/ci.yml
git commit -m "feat(oda): add ODA compilation + governance to compile_all and CI"
```

---

## Task 5: Final validation and cleanup

- [ ] **Step 1: Run all validators**

```bash
.venv/bin/python3 scripts/validate_ref.py
.venv/bin/python3 scripts/compilers/compile_all.py --validate
.venv/bin/python3 scripts/audit/audit_sparql.py
```

Expected: all CONFORME / TOUT OK / COHÉRENCE SPARQL VÉRIFIÉE

- [ ] **Step 2: Check total file counts**

```bash
echo "Payloads:" && ls 03_ptisn/schemas/payloads/*.json | wc -l
echo "FHIR:" && ls 03_ptisn/schemas/terminologies/*.json | wc -l
echo "OpenAPI:" && ls dist/openapi/pt-*.json | wc -l
echo "Governance:" && .venv/bin/python3 scripts/compilers/compile_oda.py --check-governance 2>&1 | grep "Fichiers vérifiés"
```

Expected:
- Payloads: 32 (31 DO + 1 nomenclature)
- FHIR: 1 (fosa-status CodeSystem)
- OpenAPI: 19 (all PTs)
- Governance: 51 files

- [ ] **Step 3: Final commit**

```bash
git add -A
git status
git commit -m "feat(oda): complete ODA pipeline - DO payloads + YAML-derived OpenAPI"
```

---

## Success Criteria

1. `fosa-status.json` has exactly 5 enum values (no parasite)
2. `03_ptisn/schemas/payloads/` contains 32 JSON files (31 DO + 1 nomenclature)
3. `dist/openapi/` contains 19 OpenAPI specs (all PTs), derived from YAML
4. `compile_all.py --validate` passes all steps
5. `compile_oda.py --check-governance` validates 51 files
6. `validate_ref.py` reports CONFORME
7. `audit_sparql.py` reports COHÉRENCE SPARQL VÉRIFIÉE
