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


def iter_sources(manifest):
    for level in manifest.get("levels", []):
        for rel in level.get("list", []):
            yield rel


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
