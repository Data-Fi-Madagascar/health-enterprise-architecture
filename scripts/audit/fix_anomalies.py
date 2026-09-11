#!/usr/bin/env python3
"""Batch fix des statuts dans le référentiel."""
import os
import re
import glob

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARCH_REPOSITORY_DIR = "04_architecture-repository"
ARCH_REPOSITORY_ROOT = os.path.join(REPO_ROOT, ARCH_REPOSITORY_DIR)
PROFILES_DIR = os.path.join(ARCH_REPOSITORY_ROOT, "05_building-blocks", "sbb", "legacy-profiles")
CAPABILITIES_DIR = os.path.join(ARCH_REPOSITORY_ROOT, "02_architecture-elements", "strategy", "capabilities")
COMPONENTS_DIR = os.path.join(ARCH_REPOSITORY_ROOT, "05_building-blocks", "abb", "legacy-components")
VALUE_STREAMS_DIR = os.path.join(ARCH_REPOSITORY_ROOT, "02_architecture-elements", "strategy", "value-streams")
PROCESSES_DIR = os.path.join(ARCH_REPOSITORY_ROOT, "02_architecture-elements", "business", "processes")

STATUS_FIXES = {
    os.path.join(PROFILES_DIR, "pt-*.md"):
        ("status: draft", "status: active"),
    os.path.join(CAPABILITIES_DIR, "cap-*.md"):
        ("status: draft", "status: stable"),
    os.path.join(COMPONENTS_DIR, "cmp-*.md"):
        ("status: draft", "status: active"),
    os.path.join(VALUE_STREAMS_DIR, "vs-*.md"):
        ("status: draft", "status: active"),
    os.path.join(PROCESSES_DIR, "prc-*.md"):
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

print("\nTotal : %d fichiers modifiés" % count)
