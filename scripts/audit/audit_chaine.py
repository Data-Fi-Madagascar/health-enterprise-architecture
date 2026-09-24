#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit de chaîne PT/SBB -> objets TOGAF -> capabilités CAESN.

L'audit reprend la même logique que le validateur principal : chaque profil
technique ou bloc de solution doit atteindre au moins une capabilité CAESN par
les relations déclarées dans le frontmatter.
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))

sys.path.insert(0, SCRIPT_DIR)
sys.path.insert(0, os.path.join(REPO_ROOT, "scripts"))
from utils import section, ok, err, info
from validate_ref import (
    TYPE_CAPABILITE,
    TYPE_PROFIL,
    TYPE_SBB,
    check_reachability_to_capability,
    fm_field,
    load_relation_graph,
    parse_frontmatter,
    reachable_capabilities,
)


def object_title(path):
    text = open(path, encoding="utf-8").read()
    fm, _body = parse_frontmatter(text)
    return (fm_field(fm or "", "title") or "").strip().strip('"').strip("'")


def audit_chaine():
    section("AUDIT DE CHAINE - PT/SBB -> ABB/PAT/REQ/PART -> CAP")

    objects, _id_to_file, unresolved, legacy_relation_errors = load_relation_graph()
    sources = sorted((oid, o) for oid, o in objects.items()
                     if o.get("type") in (TYPE_PROFIL, TYPE_SBB))
    capabilites = [o for o in objects.values() if o.get("type") == TYPE_CAPABILITE]
    reachability_errors = check_reachability_to_capability(objects)
    error_ids = {oid for _path, oid, _msg in reachability_errors}

    info("Sources PT/SBB : %d | CAP : %d" % (len(sources), len(capabilites)))

    for oid, o in sources:
        title = object_title(o["file"])[:50]
        caps = sorted(reachable_capabilities(objects, oid))
        label = "%s - %s" % (oid, title) if title else oid
        if caps:
            ok("%s -> %s" % (label, ", ".join(caps)))
        else:
            err("%s : aucune capabilité CAESN atteignable" % label)

    if unresolved:
        err("Relations non résolues : %d" % len(unresolved))
        for f, source_id, target_id in unresolved[:30]:
            err("  %s (%s) -> %s" % (os.path.relpath(f, REPO_ROOT), source_id, target_id))

    if legacy_relation_errors:
        err("Relations vers anciens identifiants d'interopérabilité : %d"
            % len(legacy_relation_errors))
        for f, source_id, target_id in legacy_relation_errors[:30]:
            err("  %s (%s) -> %s" % (os.path.relpath(f, REPO_ROOT), source_id, target_id))

    print()
    if not error_ids and not unresolved and not legacy_relation_errors:
        ok("CHAINE COMPLETE - toutes les sources PT/SBB atteignent une CAP")
    else:
        err("ANOMALIES : %d source(s) sans portée CAP" % len(error_ids))

    return not error_ids and not unresolved and not legacy_relation_errors


if __name__ == "__main__":
    ok_status = audit_chaine()
    sys.exit(0 if ok_status else 1)
