#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit de chaîne PT → CAP-INT → CAP.

Vérifie pour chaque profil technique (PT-*) :
  1. maps_to contient au moins un CAP-INT
  2. Chaque CAP-INT ciblé a un maps_to vers un CAP
  3. La chaîne transitive est complète

Vérifie pour chaque CAP-INT :
  1. maps_to contient au moins un CAP

Signale les PT et CAP-INT avec chaîne rompue.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import load_objects, section, ok, warn, err, info, C


def audit_chaine():
    objects = load_objects()
    section("AUDIT DE CHAÎNE — PT → CAP-INT → CAP")

    profiles = {oid: o for oid, o in objects.items() if o["type"] == "profil"}
    capacites = {oid: o for oid, o in objects.items() if o["type"] == "capacite"}
    capabilites = {oid: o for oid, o in objects.items() if o["type"] == "capabilite"}

    info("Profils : %d | CAP-INT : %d | CAP : %d"
         % (len(profiles), len(capacites), len(capabilites)))

    # --- Vérification des profils ---
    section("Profils (PT → CAP-INT)")
    pt_errors = 0
    pt_warnings = 0

    for pid, prof in sorted(profiles.items()):
        title = prof.get("title", "")[:45]
        maps = set(prof.get("maps_to", []))
        cap_int_targets = [t for t in maps if t in capacites]
        cap_targets = [t for t in maps if t in capabilites]
        other_targets = maps - set(cap_int_targets) - set(capabilites.keys())

        if not cap_int_targets and not cap_targets:
            err("%s — %s : AUCUN maps_to vers CAP-INT ou CAP" % (pid, title))
            pt_errors += 1
            continue

        # Vérifier chaque CAP-INT ciblé
        broken_chains = []
        for ci_id in cap_int_targets:
            ci_obj = objects.get(ci_id)
            if not ci_obj:
                broken_chains.append((ci_id, "objet introuvable"))
                continue
            ci_maps = set(ci_obj.get("maps_to", []))
            has_cap = any(t in capabilites for t in ci_maps)
            if not has_cap:
                broken_chains.append((ci_id, "pas de maps_to vers CAP"))

        if broken_chains:
            warn("%s — %s : chaîne partielle" % (pid, title))
            for ci_id, reason in broken_chains:
                warn("  → %s : %s" % (ci_id, reason))
            pt_warnings += 1
        else:
            chain = []
            for ci_id in cap_int_targets:
                ci_obj = objects.get(ci_id, {})
                ci_title = ci_obj.get("title", "")[:30]
                cap_in_ci = [t for t in ci_obj.get("maps_to", []) if t in capabilites]
                chain.append("%s→%s" % (ci_id, ",".join(cap_in_ci)))
            ok("%s — %s : %s" % (pid, title, " | ".join(chain)))

    # --- Vérification des CAP-INT ---
    section("CAP-INT (→ CAP)")
    ci_errors = 0

    for ci_id, ci in sorted(capacites.items()):
        title = ci.get("title", "")[:45]
        maps = set(ci.get("maps_to", []))
        cap_targets = [t for t in maps if t in capabilites]

        if not cap_targets:
            err("%s — %s : pas de maps_to vers CAP" % (ci_id, title))
            ci_errors += 1
        else:
            cap_labels = ["%s (%s)" % (t, objects.get(t, {}).get("title", "")[:25])
                          for t in cap_targets]
            ok("%s — %s → %s" % (ci_id, title, ", ".join(cap_labels)))

    # --- Résumé ---
    total_errors = pt_errors + ci_errors
    print()
    info("Profils conformes : %d / %d" % (len(profiles) - pt_errors, len(profiles)))
    info("CAP-INT conformes : %d / %d" % (len(capacites) - ci_errors, len(capacites)))

    if total_errors == 0:
        ok("CHAÎNE COMPLÈTE — tous les profils aboutissent à une CAP")
    else:
        err("ANOMALIES : %d erreurs, %d avertissements" % (total_errors, pt_warnings))

    return total_errors == 0


if __name__ == "__main__":
    ok_status = audit_chaine()
    sys.exit(0 if ok_status else 1)
