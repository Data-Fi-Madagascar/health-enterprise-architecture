#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valide la cohérence du référentiel HEA : îlots, liens cassés, portée CAP.

Complète check_links.py (liens relatifs cassés) en vérifiant le *graphe de
relations* entre objets du référentiel :

  - relations : maps_to / implements / realizes / applies_to / related (frontmatter)
  - îlots : objets sans aucune arête (degré sortant + entrant = 0)
  - cibles non résolues : une relation pointe vers un id inexistant
  - liens Markdown relatifs cassés (reprend le critère A2 de check_links.py)
  - portée CAP : tout profil ou SBB doit atteindre une capabilité CAESN
  - garde-fou : les anciens IDs d'interopérabilité ne sont plus actifs
  - couverture des 18 capabilités CAESN par les profils

Historique : le validateur initial (/tmp/validate_ref.rb) ne détectait pas les
objets sans aucune arête, ce qui avait masqué les 29 principes CAESN isolés
(coherence-report §2.4). Ce script comble cette lacune.

Usage :
    python3 scripts/validate_ref.py          # exit 1 si îlot non autorisé ou cible non résolue
    python3 scripts/validate_ref.py --strict # exit 1 aussi en présence d'îlots connus
"""

import argparse
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCH_REPOSITORY_DIR = "04_architecture-repository"
ARCH_REPOSITORY_ROOT = os.path.join(REPO_ROOT, ARCH_REPOSITORY_DIR)

# Répertoires parcourus pour la vérification des liens relatifs (tout le cadre).
LINK_DIRS = ["00_caesn", "01_cnisn", "02_artsn", "03_ptisn", ARCH_REPOSITORY_DIR]
# Le graphe de relations (maps_to/implements/...) ne concerne que le référentiel,
# source de vérité. Les documents « enveloppes » (00_caesn … 03_ptisn) ne portent
# pas ces champs et ne doivent pas être traités comme des îlots.
REL_DIRS = [ARCH_REPOSITORY_DIR]

# Répertoires contenant les ADR (Architecture Decision Records)
ADR_DIRS = ["01_cnisn/06_decisions"]
EXCLUDE_DIRS = {".git", "__pycache__", "node_modules", "dist", ".venv",
                "graphify-out", ".agents", ".claude", "mintlify-site", "docs"}
DERIVED_ARCH_REPOSITORY_DOCS = {
    os.path.join(ARCH_REPOSITORY_DIR, "01_partitions", "index.md"),
    os.path.join(ARCH_REPOSITORY_DIR, "08_views", "togaf", "architecture-landscape.md"),
    os.path.join(ARCH_REPOSITORY_DIR, "08_views", "togaf", "standards-information-base.md"),
    os.path.join(ARCH_REPOSITORY_DIR, "08_views", "togaf", "reference-library.md"),
    os.path.join(ARCH_REPOSITORY_DIR, "08_views", "togaf", "governance-log.md"),
    os.path.join(ARCH_REPOSITORY_DIR, "08_views", "togaf", "requirements-repository.md"),
    os.path.join(ARCH_REPOSITORY_DIR, "08_views", "togaf", "solutions-landscape.md"),
    os.path.join(ARCH_REPOSITORY_DIR, "08_views", "togaf", "adm-traceability.md"),
    os.path.join(ARCH_REPOSITORY_DIR, "08_views", "togaf", "partition-traceability.md"),
}
STATIC_ARCH_REPOSITORY_DOCS = {
    os.path.join(ARCH_REPOSITORY_DIR, "08_views", "togaf", "cap-int-migration.md"),
}
LEGACY_INTEROP_ALLOWED_FILES = {
    os.path.join(ARCH_REPOSITORY_DIR, "00_metamodel", "cap-int-migration.yaml"),
    os.path.join(ARCH_REPOSITORY_DIR, "08_views", "togaf", "cap-int-migration.md"),
}
EXCLUDED_GRAPH_DOCS = {
    os.path.join(ARCH_REPOSITORY_DIR, "00_metamodel", "schema.md"),
    os.path.join(ARCH_REPOSITORY_DIR, "00_metamodel", "togaf-mapping.md"),
    os.path.join(ARCH_REPOSITORY_DIR, "00_metamodel", "archimate-mapping.md"),
    os.path.join(ARCH_REPOSITORY_DIR, "00_metamodel", "cap-int-migration.yaml"),
} | DERIVED_ARCH_REPOSITORY_DOCS | STATIC_ARCH_REPOSITORY_DOCS
EXTERNAL_RELATION_DIRS = [
    "01_cnisn/05_standards",
    "01_cnisn/06_decisions",
]
REACHABILITY_KEYS = [
    "maps_to", "realizes", "implements", "applies_to", "related",
    "contributes_to", "governs", "serves", "accesses",
]
RELATION_KEYS = REACHABILITY_KEYS + [
                 "realized_by", "performs", "accessed_by", "represents",
                 "assigned_to", "has_role", "located_at", "produced_by",
                 "detenu_par", "soutient_flux_de_valeur",
                 "utilise_composant", "supporte_standard",
                 "a_pour_proprietaire_fonctionnel", "partitions"]

# Îlots légitimes attendus (candidats non encore reliés) — ne font pas échouer.
KNOWN_ISLANDS = {"art-10", "art-11", "f-5", "f-6"}

# Types de niveaux hiérarchiques pour vérification de portée.
TYPE_PROFIL = "profil"               # niveau 4 (PT-*)
TYPE_SBB = "solution-building-block"  # niveau 4 (SBB)
TYPE_CAPACITE = "capacite"            # ancien type supprimé des objets actifs
TYPE_CAPABILITE = "capabilite"        # niveau 1 (CAP-*)
TYPE_CHAPITRE = "chapitre"            # niveau 3 (ART-*)
TYPE_COMPOSANT = "composant-applicatif"  # et variantes infra/securite/gouvernance
TYPE_PARTITION = "architecture-partition"

SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*://")
LINK_RE = re.compile(r"!?\[[^]]*\]\(([^)]*)\)")
FRAGMENT_RE = re.compile(r"#.*$")
FENCE_RE = re.compile(r"^```")
LEGACY_INTEROP_PREFIX = "CAP" + "-INT-"
LEGACY_INTEROP_RE = re.compile(r"\b" + re.escape(LEGACY_INTEROP_PREFIX) + r"\d{2}\b")


def list_value(raw):
    """Parse a simple YAML inline list: ["a", "b"] or [] or a, b."""
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


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    fm = text[3:end].strip("\n")
    body = text[end + 4:]
    return fm, body


def fm_field(fm, key):
    m = re.search(r"^%s:\s*(.*)$" % re.escape(key), fm, re.MULTILINE)
    return m.group(1) if m else None


def check_frontmatter_validity(fm):
    """Renvoie la liste des erreurs de syntaxe YAML du bloc frontmatter.

    Utilise PyYAML si disponible (validation stricte), sinon un heuristique
    couvrant les cas observés en production :
      - frontmatter replié sur une seule ligne (champs sans saut de ligne) ;
      - valeur scalaire non quotée contenant ': ' (deux-points + espace) ;
      - guillemets non balancés (ex. ``version: "1.0.0"`` redoublé).
    """
    errors = []
    try:
        import yaml  # disponible dans certains environnements
        try:
            yaml.safe_load(fm)
            return errors
        except yaml.YAMLError as exc:
            errors.append("YAML invalide: %s" % str(exc).splitlines()[0])
            return errors
    except ImportError:
        pass
    lines = fm.split("\n")
    if len(lines) <= 1 and ":" in fm:
        errors.append("frontmatter replié sur une seule ligne (manque les sauts de ligne entre champs)")
        return errors
    for ln in lines:
        s = ln.strip()
        if not s or s.startswith("#") or s == "---":
            continue
        if ln[:1].isspace():
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", s)
        if not m:
            errors.append("ligne de champ non analysable: %r" % ln)
            continue
        val = m.group(2).strip()
        if val == "" or val.startswith("["):
            continue
        if val in ("|", ">", "|-", ">-", "|-", ">-"):
            continue  # bloc scalaire, non validable simplement
        if val.startswith('"'):
            inner = val[1:]
            if not inner.endswith('"') or '"' in inner[:-1]:
                errors.append("guillemets doubles non balancés: %r" % ln)
            continue
        if val.startswith("'"):
            inner = val[1:]
            if not inner.endswith("'"):
                errors.append("guillemets simples non balancés: %r" % ln)
            continue
        if re.search(r":\s", val):
            errors.append("valeur non quotée contenant ': ' (à encadrer de guillemets): %r" % ln)
    return errors


def parse_id(fm):
    m = re.search(r"^id:\s*(.+)$", fm, re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip().strip('"').strip("'")


def parse_type(fm):
    m = re.search(r"^type:\s*(.+)$", fm, re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip().strip('"').strip("'")


def iter_md(root, bases):
    for base in bases:
        d = os.path.join(root, base)
        if not os.path.isdir(d):
            continue
        for dirpath, dirnames, filenames in os.walk(d):
            dirnames[:] = [dn for dn in dirnames if dn not in EXCLUDE_DIRS]
            for fn in filenames:
                if fn.endswith(".md"):
                    yield os.path.join(dirpath, fn)


def collect_external_relation_ids():
    """IDs documentaires hors référentiel acceptés comme cibles de relation."""
    ids = set()
    for path in iter_md(REPO_ROOT, EXTERNAL_RELATION_DIRS):
        text = open(path, encoding="utf-8").read()
        fm, _body = parse_frontmatter(text)
        if fm:
            oid = parse_id(fm)
            if oid:
                ids.add(oid.upper())
            title = fm_field(fm, "title") or ""
            ids.update(re.findall(r"\b(?:STD|ADR)-\d{4}\b", title.upper()))
    return ids


def is_legacy_interop_id(value):
    return bool(value and LEGACY_INTEROP_RE.fullmatch(value))


def iter_checkable_text_files():
    """Fichiers où l'ancien préfixe ne doit plus apparaître activement."""
    explicit = ["README.md", "AGENTS.md"]
    for rel in explicit:
        path = os.path.join(REPO_ROOT, rel)
        if os.path.exists(path):
            yield path
    bases = LINK_DIRS + ["scripts"]
    suffixes = (".md", ".yaml", ".yml", ".json", ".py")
    for base in bases:
        d = os.path.join(REPO_ROOT, base)
        if not os.path.isdir(d):
            continue
        for dirpath, dirnames, filenames in os.walk(d):
            dirnames[:] = [dn for dn in dirnames if dn not in EXCLUDE_DIRS]
            for fn in filenames:
                if fn.endswith(suffixes):
                    yield os.path.join(dirpath, fn)


def is_allowed_legacy_line(rel_path, line):
    if rel_path in LEGACY_INTEROP_ALLOWED_FILES:
        return True
    single = r"['\"]?%s\d{2}['\"]?" % re.escape(LEGACY_INTEROP_PREFIX)
    inline_list = r"\[\s*%s(?:\s*,\s*%s)*\s*\]" % (single, single)
    return bool(re.match(r"^\s*legacy_id:\s*(?:%s|%s)\s*$" % (single, inline_list),
                         line))


def check_legacy_interop_usage():
    errors = []
    seen_files = set()
    for path in iter_checkable_text_files():
        if path in seen_files:
            continue
        seen_files.add(path)
        rel_path = os.path.relpath(path, REPO_ROOT)
        try:
            text = open(path, encoding="utf-8").read()
        except UnicodeDecodeError:
            continue
        for line_no, line in enumerate(text.splitlines(), 1):
            matches = LEGACY_INTEROP_RE.findall(line)
            if not matches:
                continue
            if is_allowed_legacy_line(rel_path, line):
                continue
            errors.append((rel_path, line_no, ", ".join(sorted(set(matches)))))
    return errors


def load_relation_graph():
    """Charge les objets du référentiel et résout leurs relations."""
    objects = {}
    id_to_file = {}
    unresolved = []
    legacy_relation_errors = []
    external_relation_ids = collect_external_relation_ids()

    for path in iter_md(REPO_ROOT, REL_DIRS):
        rel_path = os.path.relpath(path, REPO_ROOT)
        if rel_path in EXCLUDED_GRAPH_DOCS:
            continue  # fichier de métamodèle, pas un nœud de graphe
        text = open(path, encoding="utf-8").read()
        fm, _body = parse_frontmatter(text)
        if fm is None:
            continue
        oid = parse_id(fm)
        if not oid:
            continue
        otype = parse_type(fm)
        status = (fm_field(fm, "status") or "").strip().strip('"').strip("'")
        outgoing = set()
        reach_outgoing = set()
        relations = {}
        for k in RELATION_KEYS:
            val = fm_field(fm, k)
            targets = set(list_value(val))
            relations[k] = targets
            outgoing.update(targets)
            if k in REACHABILITY_KEYS:
                reach_outgoing.update(targets)
        objects[oid] = {
            "id": oid,
            "file": path,
            "out": outgoing,
            "reach_out": reach_outgoing,
            "in": set(),
            "type": otype,
            "status": status,
            "relations": relations,
        }
        id_to_file[oid] = path

    for oid, o in objects.items():
        for target in o["out"]:
            if is_legacy_interop_id(target):
                legacy_relation_errors.append((o["file"], oid, target))
            if target in objects:
                objects[target]["in"].add(oid)
            elif target not in external_relation_ids:
                unresolved.append((o["file"], oid, target))

    return objects, id_to_file, unresolved, legacy_relation_errors


# ---------------------------------------------------------------------------
# Vérifications de cohérence multi-niveaux
# ---------------------------------------------------------------------------

def check_legacy_objects(objects):
    """Vérifie que l'ancien type d'interopérabilité n'est plus un objet actif."""
    errors = []
    for oid, o in sorted(objects.items()):
        if is_legacy_interop_id(oid):
            rel_path = os.path.relpath(o["file"], REPO_ROOT)
            errors.append((rel_path, oid,
                           "Ancien identifiant d'interopérabilité présent comme objet actif"))
        if o.get("type") == TYPE_CAPACITE:
            rel_path = os.path.relpath(o["file"], REPO_ROOT)
            errors.append((rel_path, oid,
                           "Ancien type 'capacite' présent comme objet actif"))
    return errors


def check_partition_relation_types(objects):
    """Vérifie que `partitions` cible uniquement des partitions TOGAF."""
    errors = []
    for oid, obj in sorted(objects.items()):
        for target_id in sorted(obj.get("relations", {}).get("partitions", set())):
            target = objects.get(target_id)
            if target is None:
                continue  # la cible non résolue est signalée par load_relation_graph
            if target.get("type") != TYPE_PARTITION:
                errors.append((
                    obj["file"],
                    oid,
                    target_id,
                    "La relation partitions doit cibler un objet de type "
                    "architecture-partition, pas %s" % target.get("type"),
                ))
    return errors


def reachable_capabilities(objects, source_id):
    """Retourne les capabilités atteignables depuis un objet par les clés admises."""
    reached = set()
    seen = {source_id}
    stack = list(objects.get(source_id, {}).get("reach_out", set()))

    while stack:
        target_id = stack.pop()
        if target_id in seen:
            continue
        seen.add(target_id)
        target = objects.get(target_id)
        if not target:
            continue
        if target.get("type") == TYPE_CAPABILITE:
            reached.add(target_id)
        stack.extend(target.get("reach_out", set()) - seen)

    return reached


def check_reachability_to_capability(objects, source_types=(TYPE_PROFIL, TYPE_SBB)):
    """Vérifie que chaque profil ou SBB atteint au moins une capabilité CAESN."""
    errors = []
    for oid, o in sorted(objects.items()):
        if o.get("type") not in source_types:
            continue
        caps = reachable_capabilities(objects, oid)
        if not caps:
            rel_path = os.path.relpath(o["file"], REPO_ROOT)
            errors.append((rel_path, oid,
                           "Aucune capabilité CAESN atteignable par le graphe relationnel"))
    return errors


def check_coverage(objects, id_to_file):
    """Génère un rapport de couverture des capabilités CAESN.

    Renvoie (warnings, info_lines) où warnings sont des problèmes
    et info_lines des informations de couverture.
    """
    warnings = []
    info = []

    capabilites = {oid: o for oid, o in objects.items()
                   if o.get("type") == TYPE_CAPABILITE}
    sources = {oid: o for oid, o in objects.items()
               if o.get("type") in (TYPE_PROFIL, TYPE_SBB)}

    # Construire la couverture : quels CAP sont atteints par des profils/SBB.
    covered_caps = set()
    for source_id in sources:
        covered_caps.update(reachable_capabilities(objects, source_id))

    # CAP sans aucun profil/SBB atteignant.
    unreachable_caps = sorted(set(capabilites.keys()) - covered_caps)
    if unreachable_caps:
        for cap_id in unreachable_caps:
            rel_path = os.path.relpath(id_to_file[cap_id], REPO_ROOT)
            warnings.append((rel_path, cap_id,
                             "Capabilité CAESN non atteinte par aucun profil ou SBB"))
    info.append("CAP atteints par au moins un profil ou SBB : %d/%d"
                % (len(covered_caps), len(capabilites)))
    if unreachable_caps:
        info.append("CAP non atteints : %s" % ", ".join(unreachable_caps))

    return warnings, info


def load_all_adrs():
    """Charge tous les ADR des répertoires ADR_DIRS."""
    adrs = {}  # Maps both full ID (adr-0001-x-road) and simple ID (adr-0001) to filepath
    for adr_dir in ADR_DIRS:
        full_dir = os.path.join(REPO_ROOT, adr_dir)
        if not os.path.isdir(full_dir):
            continue
        for filename in os.listdir(full_dir):
            if filename.startswith("adr-") and filename.endswith(".md"):
                filepath = os.path.join(full_dir, filename)
                try:
                    with open(filepath, encoding="utf-8") as f:
                        text = f.read()
                    fm, _ = parse_frontmatter(text)
                    if fm:
                        adr_id = parse_id(fm)
                        if adr_id:
                            # Store both the simple ID and the filename-based ID
                            adrs[adr_id] = filepath
                            # Also store with filename (without .md) as key
                            file_id = filename[:-3]  # Remove .md
                            if file_id != adr_id:
                                adrs[file_id] = filepath
                except Exception:
                    continue
    return adrs


def main():
    objects, id_to_file, unresolved, legacy_relation_errors = load_relation_graph()
    all_links = []        # (file, target)
    adrs = load_all_adrs()

    # Liens relatifs : tous les documents du cadre.
    for path in iter_md(REPO_ROOT, LINK_DIRS):
        text = open(path, encoding="utf-8").read()
        fm, body = parse_frontmatter(text)
        in_fence = False
        for line in body.splitlines():
            if FENCE_RE.match(line.strip()):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for m in LINK_RE.finditer(line):
                target = m.group(1).strip()
                if not target:
                    continue
                if SCHEME_RE.match(target):
                    continue
                if target.startswith(("mailto:", "tel:", "data:")):
                    continue
                if target.startswith("/"):
                    continue
                if target.startswith("#"):
                    continue
                all_links.append((path, FRAGMENT_RE.sub("", target)))

    # island detection
    islands = []
    for oid, o in objects.items():
        if not o["out"] and not o["in"]:
            islands.append(oid)

    # broken relative links
    broken = []
    for path, target in all_links:
        if not target:
            continue
        resolved = os.path.normpath(os.path.join(os.path.dirname(path), target))
        if not os.path.exists(resolved):
            broken.append((path, target))

    # frontmatter YAML validity (récurrence des frontmatter brisés)
    fm_errors = []
    for path in iter_md(REPO_ROOT, LINK_DIRS):
        text = open(path, encoding="utf-8").read()
        fm, _ = parse_frontmatter(text)
        if fm is None:
            continue
        for err in check_frontmatter_validity(fm):
            fm_errors.append((path, err))

    # ADR reference validation - check references to ADRs in all markdown files
    adr_ref_errors = []
    adr_ref_pattern = re.compile(r"(?:ADR|adr)-\d{4}(?:-[a-z0-9-]+)?", re.IGNORECASE)
    for adr_dir in ADR_DIRS:
        full_dir = os.path.join(REPO_ROOT, adr_dir)
        if not os.path.isdir(full_dir):
            continue
        for dirpath, dirnames, filenames in os.walk(full_dir):
            dirnames[:] = [dn for dn in dirnames if dn not in EXCLUDE_DIRS]
            for filename in filenames:
                if filename.endswith(".md"):
                    filepath = os.path.join(dirpath, filename)
                    try:
                        with open(filepath, encoding="utf-8") as f:
                            content = f.read()
                        # Find all ADR references in the body
                        fm, body = parse_frontmatter(content)
                        if fm:
                            # Check related field for ADR references
                            related_val = fm_field(fm, "related")
                            for ref in list_value(related_val):
                                ref_upper = ref.upper()
                                if ref_upper.startswith("ADR-"):
                                    # Check if referenced ADR exists
                                    found = False
                                    for existing_adr_id in adrs:
                                        if existing_adr_id.upper() == ref_upper:
                                            found = True
                                            break
                                    if not found:
                                        adr_ref_errors.append((filepath, ref))
                        # Also check in body text
                        for match in adr_ref_pattern.finditer(body):
                            ref = match.group(0)
                            if ref.upper().startswith("ADR-0000"):
                                continue  # Skip template
                            ref_upper = ref.upper()
                            found = False
                            for existing_adr_id in adrs:
                                if existing_adr_id.upper() == ref_upper:
                                    found = True
                                    break
                            if not found:
                                adr_ref_errors.append((filepath, ref))
                    except Exception:
                        continue

    # report
    print("=== Validation du référentiel HEA ===")
    print("Objets indexés : %d" % len(objects))
    print("Liens relatifs vérifiés : %d" % len(all_links))
    print("ADR chargés : %d" % len(adrs))

    ok = True

    legacy_usage = check_legacy_interop_usage()
    if legacy_usage:
        ok = False
        print("\n[ERREUR] Usages actifs d'anciens identifiants d'interopérabilité : %d"
              % len(legacy_usage))
        for f, line_no, matches in legacy_usage[:50]:
            print("  - %s:%d : %s" % (f, line_no, matches))
    else:
        print("[OK] Aucun ancien identifiant d'interopérabilité hors migration ou legacy_id.")

    legacy_object_errors = check_legacy_objects(objects)
    if legacy_object_errors:
        ok = False
        print("\n[ERREUR] Anciens objets d'interopérabilité actifs : %d"
              % len(legacy_object_errors))
        for f, oid, msg in legacy_object_errors[:50]:
            print("  - %s (%s) : %s" % (f, oid, msg))
    else:
        print("[OK] Aucun ancien objet d'interopérabilité actif.")

    if legacy_relation_errors:
        ok = False
        print("\n[ERREUR] Relations vers anciens identifiants d'interopérabilité : %d"
              % len(legacy_relation_errors))
        for f, s, t in legacy_relation_errors[:50]:
            print("  - %s (%s) -> %s" % (os.path.relpath(f, REPO_ROOT), s, t))
    else:
        print("[OK] Aucune relation ne pointe vers un ancien identifiant d'interopérabilité.")

    if unresolved:
        ok = False
        print("\n[ERREUR] Cibles de relation non résolues : %d" % len(unresolved))
        for f, s, t in unresolved[:50]:
            print("  - %s (%s) -> %s" % (os.path.relpath(f, REPO_ROOT), s, t))
    else:
        print("[OK] Toutes les relations pointent vers un objet existant.")

    partition_relation_errors = check_partition_relation_types(objects)
    if partition_relation_errors:
        ok = False
        print("\n[ERREUR] Relations de partition invalides : %d"
              % len(partition_relation_errors))
        for f, source_id, target_id, message in partition_relation_errors[:50]:
            print("  - %s (%s) -> %s : %s"
                  % (os.path.relpath(f, REPO_ROOT), source_id, target_id, message))
    else:
        print("[OK] Toutes les relations partitions ciblent une architecture-partition.")

    if adr_ref_errors:
        ok = False
        print("\n[ERREUR] Références ADR non résolues : %d" % len(adr_ref_errors))
        for f, ref in adr_ref_errors[:50]:
            print("  - %s : référence à %s" % (os.path.relpath(f, REPO_ROOT), ref))
    else:
        print("[OK] Toutes les références ADR sont valides.")

    if broken:
        ok = False
        print("\n[ERREUR] Liens relatifs cassés : %d" % len(broken))
        for f, t in broken[:50]:
            print("  - %s -> %s" % (os.path.relpath(f, REPO_ROOT), t))
    else:
        print("[OK] Aucun lien relatif cassé.")

    if fm_errors:
        ok = False
        print("\n[ERREUR] Frontmatter YAML invalide : %d" % len(fm_errors))
        for f, e in fm_errors[:50]:
            print("  - %s : %s" % (os.path.relpath(f, REPO_ROOT), e))
    else:
        print("[OK] Tous les frontmatter sont du YAML valide.")

    known = [i for i in islands if i in KNOWN_ISLANDS]
    unknown = [i for i in islands if i not in KNOWN_ISLANDS]
    if islands:
        print("\n[AVERTISSEMENT] Objets isolés (îlots, degré 0) : %d" % len(islands))
        for i in known:
            print("  ~ %s (%s) [attendu/candidat]" % (i, os.path.relpath(id_to_file[i], REPO_ROOT)))
        for i in unknown:
            print("  ! %s (%s) [NON AUTORISÉ]" % (i, os.path.relpath(id_to_file[i], REPO_ROOT)))
        if unknown:
            ok = False
    else:
        print("[OK] Aucun objet isolé.")

    # --- Vérifications de cohérence multi-niveaux ---

    # 1. Portée PT/SBB vers capabilité CAESN
    reachability_errors = check_reachability_to_capability(objects)
    if reachability_errors:
        ok = False
        print("\n[ERREUR] Portée PT/SBB vers capabilité CAESN rompue : %d"
              % len(reachability_errors))
        for f, oid, msg in reachability_errors[:30]:
            print("  - %s (%s) : %s" % (f, oid, msg))
    else:
        print("[OK] Tous les profils et SBB atteignent une capabilité CAESN.")

    # 2. Couverture des capabilités CAESN
    cov_warns, cov_info = check_coverage(objects, id_to_file)
    if cov_warns:
        print("\n[AVERTISSEMENT] Couverture CAESN incomplète : %d" % len(cov_warns))
        for f, oid, msg in cov_warns[:30]:
            print("  ~ %s (%s) : %s" % (f, oid, msg))
    for line in cov_info:
        print("  [INFO] %s" % line)
    if not cov_warns:
        print("[OK] Toutes les capabilités CAESN sont atteintes par au moins un profil ou SBB.")

    print("\nRésumé : %s" % ("CONFORME" if ok else "ANOMALIES DÉTECTÉES"))
    return 0 if ok else 1


def validate_frontmatter_only():
    """Vérifie uniquement que tous les frontmatter sont du YAML valide."""
    import yaml
    errors = []
    
    for dirpath, _dirs, files in os.walk(REPO_ROOT):
        if any(d in dirpath for d in EXCLUDE_DIRS):
            continue
        for name in files:
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, REPO_ROOT)
            if rel == "README.md":
                continue
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            fm, _ = parse_frontmatter(text)
            if fm is None:
                errors.append("%s : frontmatter manquant" % rel)
                continue
            try:
                yaml.safe_load(fm)
            except yaml.YAMLError as exc:
                errors.append("%s : YAML invalide - %s" % (rel, str(exc).splitlines()[0]))
    
    if errors:
        print("\n[ERREUR] Frontmatter invalides : %d" % len(errors))
        for err in errors[:30]:
            print("  - %s" % err)
        return 1
    else:
        print("[OK] Tous les frontmatter sont du YAML valide.")
        return 0


def validate_quick():
    """Validation rapide : frontmatter + liens cassés seulement."""
    import subprocess
    
    print("=== Validation rapide ===")
    
    # 1. Frontmatter
    if validate_frontmatter_only() != 0:
        return 1
    
    # 2. Liens cassés
    result = subprocess.run(
        [sys.executable, os.path.join(REPO_ROOT, "scripts", "check_links.py")],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.returncode != 0:
        return 1
    
    print("[OK] Validation rapide : tout est conforme.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Valide la cohérence du référentiel HEA")
    parser.add_argument("--frontmatter-only", action="store_true",
                        help="Vérifie uniquement la validité des frontmatter YAML")
    parser.add_argument("--quick", action="store_true",
                        help="Validation rapide (frontmatter + liens seulement)")
    args = parser.parse_args()
    
    if args.frontmatter_only:
        sys.exit(validate_frontmatter_only())
    elif args.quick:
        sys.exit(validate_quick())
    else:
        sys.exit(main())
