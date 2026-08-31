#!/usr/bin/env python3
"""Batch fix des statuts + orphelins dans le référentiel."""
import os
import re
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REF = os.path.join(ROOT, "referentiel")

STATUS_FIXES = {
    "referentiel/profils/pt-*.md":        ("status: draft",    "status: active"),
    "referentiel/capabilites/cap-*.md":   ("status: draft",    "status: stable"),
    "referentiel/capacites/cap-int-*.md": ("status: active",   "status: candidate"),
    "referentiel/composants/cmp-*.md":    ("status: draft",    "status: active"),
    "referentiel/flux-valeur/vs-*.md":    ("status: draft",    "status: active"),
    "referentiel/processus/prc-*.md":     ("status: draft",    "status: active"),
}

count = 0
for pattern, (old, new) in STATUS_FIXES.items():
    for path in sorted(glob.glob(os.path.join(ROOT, pattern))):
        text = open(path, encoding="utf-8").read()
        if old in text:
            text = text.replace(old, new, 1)
            open(path, "w", encoding="utf-8").write(text)
            count += 1
            rel = os.path.relpath(path, ROOT)
            print("  FIXED %s : %s → %s" % (rel, old.split(": ")[1], new.split(": ")[1]))

# --- Fix orphelins : ajouter CAP-INT-15 à PT-17, CAP-INT-16 à PT-15 ---
orphelin_fixes = {
    "referentiel/profils/pt-17.md": ("CAP-INT-10\"]",  "CAP-INT-10\", \"CAP-INT-15\"]"),
    "referentiel/profils/pt-15.md": ("CAP-INT-14\"]",  "CAP-INT-14\", \"CAP-INT-16\"]"),
}

for rel_path, (old, new) in orphelin_fixes.items():
    path = os.path.join(ROOT, rel_path)
    text = open(path, encoding="utf-8").read()
    if old in text and new not in text:
        text = text.replace(old, new, 1)
        open(path, "w", encoding="utf-8").write(text)
        count += 1
        print("  FIXED %s : ajout lien orphelin" % rel_path)
    else:
        print("  SKIP  %s : déjà corrigé ou pattern introuvable" % rel_path)

print("\nTotal : %d fichiers modifiés" % count)
