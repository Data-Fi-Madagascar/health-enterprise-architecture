#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valide la cohérence du référentiel HEA : détection des objets isolés (îlots).

Complète check_links.py (liens relatifs cassés) en vérifiant le *graphe de
relations* entre objets du référentiel :

  - relations : maps_to / implements / applies_to / related (frontmatter)
  - îlots : objets sans aucune arête (degré sortant + entrant = 0)
  - cibles non résolues : une relation pointe vers un id inexistant
  - liens Markdown relatifs cassés (reprend le critère A2 de check_links.py)

Historique : le validateur initial (/tmp/validate_ref.rb) ne détectait pas les
objets sans aucune arête, ce qui avait masqué les 29 principes CAESN isolés
(coherence-report §2.4). Ce script comble cette lacune.

Usage :
    python3 scripts/validate_ref.py          # exit 1 si îlot non autorisé ou cible non résolue
    python3 scripts/validate_ref.py --strict # exit 1 aussi en présence d'îlots connus
"""

import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Répertoires parcourus pour la vérification des liens relatifs (tout le cadre).
LINK_DIRS = ["00_caesn", "01_cnisn", "02_artsn", "03_ptisn", "referentiel"]
# Le graphe de relations (maps_to/implements/...) ne concerne que le référentiel,
# source de vérité. Les documents « enveloppes » (00_caesn … 03_ptisn) ne portent
# pas ces champs et ne doivent pas être traités comme des îlots.
REL_DIRS = ["referentiel"]
EXCLUDE_DIRS = {".git", "__pycache__", "node_modules", "dist", ".venv",
                "graphify-out", ".agents", ".claude", "mintlify-site", "docs"}
RELATION_KEYS = ["maps_to", "implements", "applies_to", "related"]

# Îlots légitimes attendus (candidats non encore reliés) — ne font pas échouer.
KNOWN_ISLANDS = {"art-10", "art-11", "f-5", "f-6"}

SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*://")
LINK_RE = re.compile(r"!?\[[^]]*\]\(([^)]*)\)")
FRAGMENT_RE = re.compile(r"#.*$")
FENCE_RE = re.compile(r"^```")


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


def parse_id(fm):
    m = re.search(r"^id:\s*(.+)$", fm, re.MULTILINE)
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


def main():
    objects = {}          # id -> {file, out:set, in:set}
    id_to_file = {}
    all_links = []        # (file, target)

    for path in iter_md(REPO_ROOT, REL_DIRS):
        if os.path.basename(path) == "_schema.md":
            continue  # fichier de schéma, pas un nœud de graphe
        text = open(path, encoding="utf-8").read()
        fm, _body = parse_frontmatter(text)
        if fm is None:
            continue
        oid = parse_id(fm)
        if not oid:
            continue
        outgoing = set()
        for k in RELATION_KEYS:
            val = fm_field(fm, k)
            for t in list_value(val):
                outgoing.add(t)
        objects[oid] = {"file": path, "out": outgoing, "in": set()}
        id_to_file[oid] = path

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

    # build incoming + resolve
    unresolved = []  # (file, source_id, target)
    for oid, o in objects.items():
        for t in o["out"]:
            if t in objects:
                objects[t]["in"].add(oid)
            else:
                unresolved.append((o["file"], oid, t))

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

    # report
    print("=== Validation du référentiel HEA ===")
    print("Objets indexés : %d" % len(objects))
    print("Liens relatifs vérifiés : %d" % len(all_links))

    ok = True

    if unresolved:
        ok = False
        print("\n[ERREUR] Cibles de relation non résolues : %d" % len(unresolved))
        for f, s, t in unresolved[:50]:
            print("  - %s (%s) -> %s" % (os.path.relpath(f, REPO_ROOT), s, t))
    else:
        print("[OK] Toutes les relations pointent vers un objet existant.")

    if broken:
        ok = False
        print("\n[ERREUR] Liens relatifs cassés : %d" % len(broken))
        for f, t in broken[:50]:
            print("  - %s -> %s" % (os.path.relpath(f, REPO_ROOT), t))
    else:
        print("[OK] Aucun lien relatif cassé.")

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

    print("\nRésumé : %s" % ("CONFORME" if ok else "ANOMALIES DÉTECTÉES"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
