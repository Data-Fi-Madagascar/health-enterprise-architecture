#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit de conformité du portefeuille d'initiatives.

Vérifie pour chaque composant (CMP-*) :
  1. Un propriétaire fonctionnel est désigné (hea:owner)
  2. Un rattachement à un flux de valeur national existe (direct ou indirect)

Critères : ART-SN F.4, P-INT-07
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import load_objects, section, ok, warn, err, info, C


def audit_conformite():
    objects = load_objects()
    section("AUDIT DE CONFORMITÉ — Portefeuille d'initiatives")

    composants = {oid: o for oid, o in objects.items()
                  if o["type"].startswith("composant-")}
    flux = {oid: o for oid, o in objects.items()
            if o["type"] == "flux-valeur"}
    processus = {oid: o for oid, o in objects.items()
                 if o["type"] == "processus-metier"}
    capacites_int = {oid: o for oid, o in objects.items()
                     if o["type"] == "capacite"}

    info("Composants : %d | Flux de valeur : %d" % (len(composants), len(flux)))

    # Index inversé : quels objets pointent vers un FluxValeur ?
    vs_reachers = set()
    for oid, o in objects.items():
        for rel in ["related", "applies_to", "realized_by", "contributes_to"]:
            for target in o.get(rel, []):
                if target in flux:
                    vs_reachers.add(oid)
                    break

    # Chaîne transitive : composant → CAP-INT → CAP → (éventuellement VS)
    comp_to_vs = {}
    for cid, comp in composants.items():
        reachable = set()
        # Direct VS links
        for rel in ["related", "applies_to", "realized_by", "contributes_to"]:
            for target in comp.get(rel, []):
                if target in flux:
                    reachable.add(target)
        # Indirect via CAP-INT → CAP
        for target in comp.get("maps_to", []):
            if target in capacites_int:
                for deep_target in capacites_int[target].get("maps_to", []):
                    if deep_target in flux:
                        reachable.add(deep_target)
        comp_to_vs[cid] = reachable

    # Rapport
    conforms = []
    no_owner = []
    no_vs_direct = []
    no_vs_indirect = []

    for cid, comp in sorted(composants.items()):
        title = comp.get("title", "")[:55]
        owner = comp.get("owner")
        has_vs_direct = cid in vs_reachers
        has_vs_indirect = bool(comp_to_vs.get(cid))

        if not owner:
            no_owner.append((cid, title))
        elif not has_vs_direct and not has_vs_indirect:
            no_vs_indirect.append((cid, title, owner))
        elif not has_vs_direct:
            no_vs_direct.append((cid, title, owner))
        else:
            conforms.append((cid, title, owner))

    # Résultats
    info("Conformes : %d / %d" % (len(conforms), len(composants)))
    for cid, title, owner in conforms:
        ok("%s — %s (owner: %s)" % (cid, title, owner))

    if no_owner:
        err("Sans propriétaire : %d" % len(no_owner))
        for cid, title in no_owner:
            err("%s — %s" % (cid, title))

    if no_vs_direct:
        warn("Sans lien VS direct (couvert indirectement) : %d" % len(no_vs_direct))
        for cid, title, owner in no_vs_direct:
            warn("%s — %s" % (cid, title))

    if no_vs_indirect:
        warn("Sans aucun rattachement VS : %d" % len(no_vs_indirect))
        for cid, title, owner in no_vs_indirect:
            warn("%s — %s (owner: %s)" % (cid, title, owner))

    total_issues = len(no_owner) + len(no_vs_indirect)
    print()
    if total_issues == 0:
        ok("PORTFEUILLE CONFORME")
    else:
        err("ANOMALIES DÉTECTÉES : %d" % total_issues)

    return total_issues == 0


if __name__ == "__main__":
    ok_status = audit_conformite()
    sys.exit(0 if ok_status else 1)
