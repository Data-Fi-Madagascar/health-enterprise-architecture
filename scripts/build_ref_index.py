#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build or check referentiel/_index.yaml from Markdown frontmatter.

The Markdown files under referentiel/ are the source of truth. This derived
index gives reviewers a compact inventory and gives CI a stable drift check.
"""

import argparse
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REF_ROOT = REPO_ROOT / "referentiel"
INDEX_PATH = REF_ROOT / "_index.yaml"
CONTROLLED_STATUSES = ("draft", "active", "stable", "candidate", "deprecated")
TYPE_ORDER = [
    "flux-valeur",
    "capabilite",
    "principe",
    "etape-valeur",
    "processus-metier",
    "composant-applicatif",
    "composant-infrastructure",
    "composant-securite",
    "registre-gouvernance",
    "partie-prenante",
    "acteur",
    "role",
    "lieu",
    "service",
    "capacite",
    "fondation",
    "exigence",
    "chapitre",
    "profil",
    "work-package",
    "plateau",
    "gap",
    "objet-de-donnees",
    "objet-metier",
    "valeur",
]


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return text[3:end].strip("\n")


def fm_field(fm, key):
    m = re.search(r"^%s:\s*(.*)$" % re.escape(key), fm, re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip().strip('"').strip("'")


def natural_key(value):
    return [int(part) if part.isdigit() else part.lower()
            for part in re.split(r"(\d+)", value)]


def collect_entries():
    entries = []
    errors = []
    for path in sorted(REF_ROOT.rglob("*.md")):
        if path.name in ("_index.yaml", "_schema.md"):
            continue
        rel = path.relative_to(REF_ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append("%s : frontmatter manquant" % rel)
            continue
        entry = {
            "id": fm_field(fm, "id"),
            "type": fm_field(fm, "type"),
            "niveau": fm_field(fm, "niveau") or "",
            "chemin": rel,
            "status": fm_field(fm, "status"),
        }
        title = fm_field(fm, "title")
        if title:
            entry["title"] = title

        for key in ("id", "type", "status"):
            if not entry.get(key):
                errors.append("%s : champ %s manquant" % (rel, key))
        if entry.get("status") and entry["status"] not in CONTROLLED_STATUSES:
            errors.append("%s : status non contrôlé %s" % (rel, entry["status"]))

        entries.append(entry)

    ids = Counter(entry["id"] for entry in entries if entry.get("id"))
    for oid, count in sorted(ids.items()):
        if count > 1:
            paths = [entry["chemin"] for entry in entries if entry.get("id") == oid]
            errors.append("%s : identifiant dupliqué dans %s" %
                          (oid, ", ".join(paths)))

    if errors:
        print("[ERREUR] Index référentiel impossible :")
        for err in errors[:40]:
            print("  - %s" % err)
        if len(errors) > 40:
            print("  ... %d erreurs supplémentaires" % (len(errors) - 40))
        sys.exit(1)

    type_rank = {name: idx for idx, name in enumerate(TYPE_ORDER)}

    def sort_key(entry):
        niveau = entry.get("niveau") or "9"
        try:
            niveau_key = int(niveau)
        except ValueError:
            niveau_key = 9
        return (
            niveau_key,
            type_rank.get(entry["type"], len(TYPE_ORDER)),
            natural_key(entry["id"]),
            entry["chemin"],
        )

    return sorted(entries, key=sort_key)


def q(value):
    return json.dumps(str(value), ensure_ascii=False)


def render(entries):
    by_type = Counter(entry["type"] for entry in entries)
    by_status = Counter(entry["status"] for entry in entries)

    lines = [
        "# Registre des objets du référentiel",
        "# Fichier généré par scripts/build_ref_index.py. Ne pas éditer à la main.",
        "# Source de vérité : frontmatter Markdown sous referentiel/.",
        "# Champs : id, type, niveau, chemin, status, title.",
        "# Statuts : %s" % " | ".join(CONTROLLED_STATUSES),
        "# Total : %d objets" % len(entries),
        "#",
        "# Comptes par type :",
    ]
    for typ in sorted(by_type):
        lines.append("# - %s : %d" % (typ, by_type[typ]))
    lines.extend(["#", "# Comptes par status :"])
    for status in CONTROLLED_STATUSES:
        lines.append("# - %s : %d" % (status, by_status.get(status, 0)))

    current_group = None
    for entry in entries:
        group = (entry.get("niveau") or "?", entry["type"])
        if group != current_group:
            current_group = group
            lines.extend([
                "",
                "# niveau %s / %s (%d)" % (group[0], group[1], by_type[entry["type"]]),
            ])
        lines.append("- id: %s" % q(entry["id"]))
        lines.append("  type: %s" % q(entry["type"]))
        lines.append("  niveau: %s" % q(entry.get("niveau") or ""))
        lines.append("  chemin: %s" % q(entry["chemin"]))
        lines.append("  status: %s" % q(entry["status"]))
        if entry.get("title"):
            lines.append("  title: %s" % q(entry["title"]))

    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="Build referentiel/_index.yaml")
    parser.add_argument("--check", action="store_true",
                        help="Vérifier sans écrire que l'index est à jour")
    args = parser.parse_args()

    content = render(collect_entries())

    if args.check:
        existing = INDEX_PATH.read_text(encoding="utf-8") if INDEX_PATH.exists() else ""
        if existing != content:
            print("[ERREUR] referentiel/_index.yaml obsolète.")
            print("Exécuter : python3 scripts/build_ref_index.py")
            return 1
        print("[OK] referentiel/_index.yaml à jour.")
        return 0

    INDEX_PATH.write_text(content, encoding="utf-8")
    print("[OK] referentiel/_index.yaml généré.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
