#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate source paths declared by documentation manifests."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFESTS = (
    ROOT / "scripts" / "manifest.json",
    ROOT / "scripts" / "manifest-public.json",
)

# Le manifeste public ne publie pas l'intégralité du corpus : la liste ci-dessous
# matérialise les exclusions assumées. Toute autre divergence entre les fichiers
# présents sur le disque et les entrées déclarées est considérée comme une dérive.
MANIFEST_EXCLUSIONS = {
    "manifest.json": frozenset(),
    "manifest-public.json": frozenset({
        "00_caesn/reading-matrix.md",
        "00_caesn/06_portfolio/migration-existant.md",
        "00_caesn/07_governance/processus-gouvernance.md",
        "00_caesn/07_governance/point-de-vigilance-caesn.md",
        "00_caesn/07_governance/fondement-legal.md",
        "01_cnisn/reading-matrix.md",
        "01_cnisn/04_conformite/programme-conformite.md",
        "01_cnisn/06_decisions/adr-0010-cadre-legal.md",
        "02_artsn/reading-matrix.md",
    }),
}


def iter_sources(manifest):
    for level in manifest.get("levels", []):
        for rel in level.get("list", []):
            yield rel


def level_roots(manifest):
    """Racine de dossier (00_caesn, 01_cnisn, …) déclarée par chaque niveau."""
    roots = []
    for level in manifest.get("levels", []):
        entries = level.get("list", [])
        if entries:
            roots.append(entries[0].split("/")[0])
    return roots


def on_disk_sources(root):
    """Documents Markdown présents sous une racine de niveau."""
    found = []
    base = ROOT / root
    if not base.is_dir():
        return found
    for path in sorted(base.rglob("*.md")):
        found.append(path.relative_to(ROOT).as_posix())
    return found


def main():
    errors = []
    for manifest_path in MANIFESTS:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append("%s : JSON invalide : %s" %
                          (manifest_path.relative_to(ROOT), exc))
            continue

        seen = set()
        for rel in iter_sources(manifest):
            if rel in seen:
                errors.append("%s : entrée dupliquée : %s" %
                              (manifest_path.relative_to(ROOT), rel))
            seen.add(rel)
            if not (ROOT / rel).exists():
                errors.append("%s : source manquante : %s" %
                              (manifest_path.relative_to(ROOT), rel))

        # Complétude : toute source présente sur le disque doit être déclarée.
        exclusions = MANIFEST_EXCLUSIONS.get(manifest_path.name, frozenset())
        for root in level_roots(manifest):
            for rel in on_disk_sources(root):
                if rel not in seen and rel not in exclusions:
                    errors.append("%s : source non déclarée : %s" %
                                  (manifest_path.relative_to(ROOT), rel))

    if errors:
        print("[ERREUR] Manifestes invalides :")
        for err in errors[:80]:
            print("  - %s" % err)
        if len(errors) > 80:
            print("  ... %d erreurs supplémentaires" % (len(errors) - 80))
        return 1

    print("[OK] Manifestes valides.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
