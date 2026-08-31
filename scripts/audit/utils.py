#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utilitaires partagés pour les scripts d'audit HEA."""

import os
import re
import glob

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REFERENTIEL = os.path.join(REPO_ROOT, "referentiel")

# Couleurs ANSI pour la sortie console
class C:
    OK = "\033[92m"
    WARN = "\033[93m"
    ERR = "\033[91m"
    INFO = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    return text[3:end].strip("\n"), text[end + 4:]


def fm_field(fm, key):
    m = re.search(r"^%s:\s*(.*)$" % re.escape(key), fm, re.MULTILINE)
    return m.group(1).strip().strip('"').strip("'") if m else None


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


def load_objects():
    """Charge tous les objets du référentiel avec leur frontmatter."""
    objects = {}
    for path in sorted(glob.glob(os.path.join(REFERENTIEL, "**", "*.md"), recursive=True)):
        if os.path.basename(path) in ("_schema.md", "_index.yaml"):
            continue
        text = open(path, encoding="utf-8").read()
        fm, _ = parse_frontmatter(text)
        if fm is None:
            continue
        oid = fm_field(fm, "id")
        otype = fm_field(fm, "type")
        if not oid or not otype:
            continue
        obj = {"id": oid, "type": otype, "file": os.path.relpath(path, REPO_ROOT)}
        for field in ["title", "status", "owner", "version", "niveau", "family"]:
            val = fm_field(fm, field)
            if val is not None:
                obj[field] = val
        for rel in ["maps_to", "implements", "applies_to", "related",
                     "realized_by", "contributes_to", "performs", "accesses",
                     "governs", "represents", "assigned_to", "has_role",
                     "located_at", "serves"]:
            val = fm_field(fm, rel)
            if val is not None:
                items = list_value(val)
                if items:
                    obj[rel] = items
        objects[oid] = obj
    return objects


def section(title):
    print("\n%s%s%s" % (C.BOLD, title, C.RESET))
    print("-" * len(title))


def ok(msg):
    print("  %s[OK]%s %s" % (C.OK, C.RESET, msg))


def warn(msg):
    print("  %s[!!]%s %s" % (C.WARN, C.RESET, msg))


def err(msg):
    print("  %s[ERREUR]%s %s" % (C.ERR, C.RESET, msg))


def info(msg):
    print("  %s[i]%s %s" % (C.INFO, C.RESET, msg))
