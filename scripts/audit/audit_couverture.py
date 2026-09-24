#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit de couverture des capabilités CAESN par reachability frontmatter."""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))

sys.path.insert(0, SCRIPT_DIR)
sys.path.insert(0, os.path.join(REPO_ROOT, "scripts"))
from utils import section, ok, warn, err, info
from validate_ref import (
    TYPE_CAPABILITE,
    TYPE_PROFIL,
    TYPE_SBB,
    check_coverage,
    load_relation_graph,
    reachable_capabilities,
)


def audit_couverture():
    section("AUDIT DE COUVERTURE - Capabilités CAESN")

    objects, id_to_file, unresolved, legacy_relation_errors = load_relation_graph()
    caps = sorted(oid for oid, o in objects.items() if o.get("type") == TYPE_CAPABILITE)
    sources = sorted(oid for oid, o in objects.items()
                     if o.get("type") in (TYPE_PROFIL, TYPE_SBB))

    cap_sources = {cap_id: [] for cap_id in caps}
    for source_id in sources:
        for cap_id in sorted(reachable_capabilities(objects, source_id)):
            cap_sources.setdefault(cap_id, []).append(source_id)

    section("Couverture des CAP")
    uncovered = []
    for cap_id in caps:
        linked_sources = cap_sources.get(cap_id, [])
        if linked_sources:
            ok("%s <- %s" % (cap_id, ", ".join(linked_sources)))
        else:
            uncovered.append(cap_id)
            warn("%s : aucune source PT/SBB atteignante" % cap_id)

    cov_warns, cov_info = check_coverage(objects, id_to_file)

    section("Résumé")
    for line in cov_info:
        info(line)

    if unresolved:
        err("Relations non résolues : %d" % len(unresolved))
    if legacy_relation_errors:
        err("Relations vers anciens identifiants d'interopérabilité : %d"
            % len(legacy_relation_errors))

    print()
    if not cov_warns and not unresolved and not legacy_relation_errors:
        ok("COUVERTURE CONFORME")
    elif not unresolved and not legacy_relation_errors:
        warn("COUVERTURE PARTIELLE - %d CAP sans source PT/SBB" % len(uncovered))
    else:
        err("ANOMALIES : couverture non exploitable")

    return not unresolved and not legacy_relation_errors


if __name__ == "__main__":
    ok_status = audit_couverture()
    sys.exit(0 if ok_status else 1)
