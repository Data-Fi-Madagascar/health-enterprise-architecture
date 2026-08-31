#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit de couverture des capabilités CAESN.

Vérifie :
  1. Chaque CAP (cap-*) est couvert par au moins un PT via la chaîne transitive
  2. Les PT-14/PT-15 qui ciblent directement des CAP (bypassant CAP-INT) sont signalés
  3. Les CAP-INT orphelins (pas de PT qui les pointe) sont listés
  4. Les CAP non couverts sont identifiés
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import load_objects, section, ok, warn, err, info, C


def audit_couverture():
    objects = load_objects()
    section("AUDIT DE COUVERTURE — Capabilités CAESN")

    profiles = {oid: o for oid, o in objects.items() if o["type"] == "profil"}
    capacites_int = {oid: o for oid, o in objects.items() if o["type"] == "capacite"}
    capabilites = {oid: o for oid, o in objects.items() if o["type"] == "capabilite"}

    # Construire la couverture transitive : PT → CAP-INT → CAP
    covered_by = {}  # cap_id → list of (pt_id, via_ci)
    for cid, cap in capabilites.items():
        covered_by[cid] = []

    # Index inversé : quels PT couvrent quelles CAP-INT
    ci_covered_by = {}
    for ci_id in capacites_int:
        ci_covered_by[ci_id] = []

    for pid, prof in profiles.items():
        maps = set(prof.get("maps_to", []))
        # Direct CAP targeting (bypassing CAP-INT)
        for target in maps:
            if target in capabilites:
                covered_by[target].append((pid, "direct"))
        # Via CAP-INT
        for target in maps:
            if target in capacites_int:
                ci_covered_by[target].append(pid)
                for deep_target in capacites_int[target].get("maps_to", []):
                    if deep_target in capabilites:
                        covered_by[deep_target].append((pid, target))

    # --- Rapport ---
    section("Couverture des CAP (cap-*)")
    uncovered = []
    partial = []
    for cid, cap in sorted(capabilites.items()):
        title = cap.get("title", "")[:45]
        sources = covered_by[cid]
        if not sources:
            uncovered.append((cid, title))
        else:
            labels = ["%s via %s" % (pt, via) if via != "direct" else "%s (direct)" % pt
                       for pt, via in sources]
            ok("%s — %s ← %s" % (cid, title, ", ".join(labels)))

    section("CAP-INT orphelins (pas de PT qui les pointe)")
    orphelins_ci = []
    for ci_id, ci in sorted(capacites_int.items()):
        title = ci.get("title", "")[:45]
        if not ci_covered_by[ci_id]:
            orphelins_ci.append((ci_id, title))
            warn("%s — %s : aucun PT ne cible cette CAP-INT" % (ci_id, title))

    section("Résumé")
    info("CAP couvertes : %d / %d" % (len(capabilites) - len(uncovered), len(capabilites)))
    info("CAP-INT orphelins : %d / %d" % (len(orphelins_ci), len(capacites_int)))

    total_issues = len(uncovered) + len(orphelins_ci)
    if uncovered:
        err("CAP non couvertes :")
        for cid, title in uncovered:
            err("  %s — %s" % (cid, title))

    print()
    if total_issues == 0:
        ok("COUVERTURE COMPLÈTE")
    else:
        err("ANOMALIES : %d CAP non couverts, %d CAP-INT orphelins" % (len(uncovered), len(orphelins_ci)))

    return total_issues == 0


if __name__ == "__main__":
    ok_status = audit_couverture()
    sys.exit(0 if ok_status else 1)
