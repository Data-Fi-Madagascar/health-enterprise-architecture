#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérifie qu'aucun lien relatif n'est cassé sur l'ensemble du dépôt.

Critère A2 de la spec docs/superpowers/specs/2026-08-11-enveloppes-lisibilite-design.md :
0 lien relatif cassé (1 222 liens relatifs avant le lot, dont 215 cassés).

Périmètre :
- Tous les fichiers `*.md` du dépôt, à l'exception de `.git/`, `__pycache__/`,
  `node_modules/` et `dist/`.
- Liens Markdown `[texte](cible)` et `![alt](cible)` dont la cible est relative
  (pas de schéma `://`, pas de `mailto:`, pas de `/` absolu, pas d'ancre `#` seule).
- La partie fragment (`#…`) est ignorée pour la résolution ; l'ancre elle-même
  n'est pas validée.

Usage :
    python3 scripts/check_links.py      # exit 1 si au moins un lien cassé
"""

import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXCLUDE_DIRS = {".git", "__pycache__", "node_modules", "dist"}
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*://")
LINK_RE = re.compile(r"!?\[[^]]*\]\(([^)]*)\)")
FRAGMENT_RE = re.compile(r"#.*$")
FENCE_RE = re.compile(r"^```")


def is_relative(target):
    target = target.strip()
    if not target:
        return False
    if SCHEME_RE.match(target):
        return False
    if target.startswith("mailto:") or target.startswith("tel:") or target.startswith("data:"):
        return False
    if target.startswith("/"):
        return False
    return True


def resolve(target, base_dir):
    target = target.strip()
    target = FRAGMENT_RE.sub("", target)
    if not target:
        return None
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if target.startswith('"') and target.endswith('"'):
        target = target[1:-1]
    path = os.path.normpath(os.path.join(base_dir, target))
    return path


def strip_code_blocks(text):
    """Neutralise les blocs de code fencés (```) et les spans de code inline (`)."""
    lines = text.splitlines(keepends=True)
    code = False
    out = []
    for line in lines:
        if FENCE_RE.match(line.strip()):
            code = not code
            out.append("\n")
            continue
        if code:
            out.append("\n")
            continue
        out.append(re.sub(r"`[^`]*`", "", line))
    return "".join(out)


def main():
    broken = []
    total = 0
    for dirpath, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for name in sorted(files):
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            base_dir = os.path.dirname(path)
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            rel = os.path.relpath(path, REPO_ROOT)
            for match in LINK_RE.finditer(strip_code_blocks(text)):
                target = match.group(1).strip()
                if not is_relative(target):
                    continue
                total += 1
                resolved = resolve(target, base_dir)
                if resolved and not os.path.exists(resolved):
                    broken.append((rel, target))

    if broken:
        sys.stderr.write("%d lien(s) relatif(s) cassé(s) :\n" % len(broken))
        for rel, target in broken:
            sys.stderr.write("  %s -> %s\n" % (rel, target))
        sys.stderr.write("Total : %d lien(s) relatif(s) vérifié(s)\n" % total)
        sys.exit(1)

    print("OK : 0 lien relatif cassé sur %d vérifiés" % total)


if __name__ == "__main__":
    main()
