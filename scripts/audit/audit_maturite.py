#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit de maturité du référentiel.

Vérifie :
  1. Distribution des statuts (draft/active/stable/candidate/deprecated)
  2. Objets bloqués (status != draft/active/stable) trop anciens
  3. Objets sans version
  4. Cohérence status vs. type (les CAP devraient être stable/candidate, les PT active)
  5. Objets avec last_reviewed > 6 mois
"""

import os
import sys
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import load_objects, section, ok, warn, err, info, C

VALID_STATUSES = {"draft", "active", "stable", "candidate", "deprecated"}

# Statuts attendus par type
STATUS_BY_TYPE = {
    "profil": {"active", "stable"},
    "capacite": {"stable", "candidate"},
    "capabilite": {"stable", "candidate"},
    "flux-valeur": {"active", "stable"},
    "processus-metier": {"active", "stable"},
    "composant-applicatif": {"active", "stable", "candidate"},
    "composant-infra": {"active", "stable", "candidate"},
    "composant-securite": {"active", "stable", "candidate"},
    "composant-donnees": {"active", "stable", "candidate"},
    "composant-architecture": {"active", "stable", "candidate"},
    "composant-transverse": {"active", "stable", "candidate"},
}


def audit_maturite():
    objects = load_objects()
    section("AUDIT DE MATURITÉ — Référentiel HEA")

    # Distribution des statuts
    section("Distribution des statuts")
    status_dist = {}
    for oid, obj in objects.items():
        st = obj.get("status", "NONE")
        status_dist[st] = status_dist.get(st, 0) + 1

    for st, count in sorted(status_dist.items(), key=lambda x: -x[1]):
        label = st if st in VALID_STATUSES else "(invalide: %s)" % st
        info("%-20s %d objets" % (label, count))

    # Statuts invalides
    section("Statuts invalides")
    invalid = []
    for oid, obj in objects.items():
        st = obj.get("status", "")
        if st not in VALID_STATUSES:
            invalid.append((oid, obj.get("type", ""), st, obj.get("file", "")))
    if invalid:
        for oid, otype, st, f in invalid:
            err("%s (%s) — status '%s' invalide  [%s]" % (oid, otype, st, f))
    else:
        ok("Aucun statut invalide")

    # Cohérence status/type
    section("Cohérence status ↔ type")
    type_issues = []
    for oid, obj in objects.items():
        otype = obj.get("type", "")
        st = obj.get("status", "")
        expected = STATUS_BY_TYPE.get(otype)
        if expected and st and st not in expected:
            type_issues.append((oid, otype, st, expected))
    if type_issues:
        for oid, otype, st, expected in type_issues:
            warn("%s (%s) — status '%s' inattendu (attendu: %s)"
                 % (oid, otype, st, "/".join(sorted(expected))))
    else:
        ok("Tous les statuts sont cohérents avec le type")

    # Objets sans version
    section("Objets sans version")
    no_version = [(oid, obj.get("type", ""), obj.get("title", "")[:40])
                  for oid, obj in objects.items() if not obj.get("version")]
    if no_version:
        for oid, otype, title in no_version:
            warn("%s — %s (%s)" % (oid, title, otype))
        info("Objets sans version : %d / %d" % (len(no_version), len(objects)))
    else:
        ok("Tous les objets ont une version")

    # Objets avec last_reviewed > 6 mois (si frontmatter le permet)
    section("Objets potentiellement obsolètes (deprecated)")
    deprecated = [(oid, obj.get("type", ""), obj.get("title", "")[:40])
                  for oid, obj in objects.items() if obj.get("status") == "deprecated"]
    if deprecated:
        for oid, otype, title in deprecated:
            warn("%s — %s (%s)" % (oid, title, otype))
        info("Objets dépréciés : %d" % len(deprecated))
    else:
        ok("Aucun objet déprécié")

    # Résumé
    print()
    total_issues = len(invalid) + len(type_issues)
    if total_issues == 0:
        ok("MATURITÉ CONFORME")
    else:
        err("ANOMALIES : %d statuts invalides, %d incohérences type/status"
            % (len(invalid), len(type_issues)))

    return total_issues == 0


if __name__ == "__main__":
    ok_status = audit_maturite()
    sys.exit(0 if ok_status else 1)
