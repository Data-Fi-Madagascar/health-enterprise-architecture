#!/usr/bin/env python3
"""Batch fix des statuts + orphelins dans le référentiel."""
import os
import re
import glob

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARCH_REPOSITORY_DIR = "04_architecture-repository"
ARCH_REPOSITORY_ROOT = os.path.join(REPO_ROOT, ARCH_REPOSITORY_DIR)

STATUS_FIXES = {
    os.path.join(ARCH_REPOSITORY_ROOT, "profils", "pt-*.md"):
        ("status: draft", "status: active"),
    os.path.join(ARCH_REPOSITORY_ROOT, "capabilites", "cap-*.md"):
        ("status: draft", "status: stable"),
    os.path.join(ARCH_REPOSITORY_ROOT, "capacites", "cap-int-*.md"):
        ("status: active", "status: candidate"),
    os.path.join(ARCH_REPOSITORY_ROOT, "composants", "cmp-*.md"):
        ("status: draft", "status: active"),
    os.path.join(ARCH_REPOSITORY_ROOT, "flux-valeur", "vs-*.md"):
        ("status: draft", "status: active"),
    os.path.join(ARCH_REPOSITORY_ROOT, "processus", "prc-*.md"):
        ("status: draft", "status: active"),
}

count = 0
for pattern, (old, new) in STATUS_FIXES.items():
    for path in sorted(glob.glob(pattern)):
        text = open(path, encoding="utf-8").read()
        if old in text:
            text = text.replace(old, new, 1)
            open(path, "w", encoding="utf-8").write(text)
            count += 1
            rel = os.path.relpath(path, REPO_ROOT)
            print("  FIXED %s : %s → %s" % (rel, old.split(": ")[1], new.split(": ")[1]))

# --- Fix orphelins : ajouter CAP-INT-15 à PT-17, CAP-INT-16 à PT-15 ---
orphelin_fixes = {
    os.path.join(ARCH_REPOSITORY_ROOT, "profils", "pt-17.md"):
        ("CAP-INT-10\"]", "CAP-INT-10\", \"CAP-INT-15\"]"),
    os.path.join(ARCH_REPOSITORY_ROOT, "profils", "pt-15.md"):
        ("CAP-INT-14\"]", "CAP-INT-14\", \"CAP-INT-16\"]"),
}

for path, (old, new) in orphelin_fixes.items():
    rel_path = os.path.relpath(path, REPO_ROOT)
    text = open(path, encoding="utf-8").read()
    if old in text and new not in text:
        text = text.replace(old, new, 1)
        open(path, "w", encoding="utf-8").write(text)
        count += 1
        print("  FIXED %s : ajout lien orphelin" % rel_path)
    else:
        print("  SKIP  %s : déjà corrigé ou pattern introuvable" % rel_path)

print("\nTotal : %d fichiers modifiés" % count)
