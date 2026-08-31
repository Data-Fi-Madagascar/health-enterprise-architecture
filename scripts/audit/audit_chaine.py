#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit de chaîne PT → CAP-INT → CAP via SPARQL.

Vérifie pour chaque profil technique (hea:Profil) :
  1. hea:mapsTo contient au moins un hea:CapaciteInteroperabilite
  2. Chaque CAP-INT ciblée a un hea:mapsTo vers un hea:Capabilite

Vérifie pour chaque CAP-INT :
  1. hea:mapsTo contient au moins un hea:Capabilite
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import sparql_rows, section, ok, warn, err, info


def audit_chaine():
    section("AUDIT DE CHAÎNE — PT → CAP-INT → CAP")

    profiles = sparql_rows("""
        SELECT ?id ?title WHERE {
            ?s rdf:type hea:Profil .
            ?s hea:id ?id .
            ?s hea:title ?title .
        }
        ORDER BY ?id
    """)
    cap_int = sparql_rows("""
        SELECT ?id ?title WHERE {
            ?s rdf:type hea:CapaciteInteroperabilite .
            ?s hea:id ?id .
            ?s hea:title ?title .
        }
        ORDER BY ?id
    """)
    capabilites = sparql_rows("""
        SELECT ?id ?title WHERE {
            ?s rdf:type hea:Capabilite .
            ?s hea:id ?id .
            ?s hea:title ?title .
        }
        ORDER BY ?id
    """)

    info("Profils : %d | CAP-INT : %d | CAP : %d"
         % (len(profiles), len(cap_int), len(capabilites)))

    cap_int_ids = {r["id"] for r in cap_int}
    cap_ids = {r["id"] for r in capabilites}

    # --- Vérification des profils ---
    section("Profils (PT → CAP-INT)")
    pt_errors = 0

    for prof in profiles:
        pid = prof["id"]
        title = prof["title"][:45]

        # Quels CAP-INT ce profil cible ?
        targets = sparql_rows("""
            SELECT ?targetId WHERE {
                ?s hea:id "%s" .
                ?s hea:mapsTo ?t .
                ?t hea:id ?targetId .
                ?t rdf:type hea:CapaciteInteroperabilite .
            }
        """ % pid)

        cap_targets = sparql_rows("""
            SELECT ?targetId WHERE {
                ?s hea:id "%s" .
                ?s hea:mapsTo ?t .
                ?t hea:id ?targetId .
                ?t rdf:type hea:Capabilite .
            }
        """ % pid)

        if not targets and not cap_targets:
            err("%s — %s : AUCUN maps_to vers CAP-INT ou CAP" % (pid, title))
            pt_errors += 1
            continue

        # Vérifier chaque CAP-INT ciblé
        broken_chains = []
        for t in targets:
            ci_id = t["targetId"]
            has_cap = sparql_rows("""
                SELECT ?capId WHERE {
                    ?ci hea:id "%s" .
                    ?ci hea:mapsTo ?c .
                    ?c hea:id ?capId .
                    ?c rdf:type hea:Capabilite .
                }
            """ % ci_id)
            if not has_cap:
                broken_chains.append((ci_id, "pas de maps_to vers CAP"))

        if broken_chains:
            warn("%s — %s : chaîne partielle" % (pid, title))
            for ci_id, reason in broken_chains:
                warn("  → %s : %s" % (ci_id, reason))
        else:
            chain = []
            for t in targets:
                ci_id = t["targetId"]
                cap_in_ci = sparql_rows("""
                    SELECT ?capId WHERE {
                        ?ci hea:id "%s" .
                        ?ci hea:mapsTo ?c .
                        ?c hea:id ?capId .
                        ?c rdf:type hea:Capabilite .
                    }
                """ % ci_id)
                caps = ",".join(r["capId"] for r in cap_in_ci)
                chain.append("%s→%s" % (ci_id, caps))
            ok("%s — %s : %s" % (pid, title, " | ".join(chain)))

    # --- Vérification des CAP-INT ---
    section("CAP-INT (→ CAP)")
    ci_errors = 0

    for ci in cap_int:
        ci_id = ci["id"]
        title = ci["title"][:45]
        cap_targets = sparql_rows("""
            SELECT ?capId ?capTitle WHERE {
                ?ci hea:id "%s" .
                ?ci hea:mapsTo ?c .
                ?c hea:id ?capId .
                ?c hea:title ?capTitle .
                ?c rdf:type hea:Capabilite .
            }
        """ % ci_id)

        if not cap_targets:
            err("%s — %s : pas de maps_to vers CAP" % (ci_id, title))
            ci_errors += 1
        else:
            labels = ["%s (%s)" % (r["capId"], r["capTitle"][:25]) for r in cap_targets]
            ok("%s — %s → %s" % (ci_id, title, ", ".join(labels)))

    # --- Résumé ---
    total_errors = pt_errors + ci_errors
    print()
    info("Profils conformes : %d / %d" % (len(profiles) - pt_errors, len(profiles)))
    info("CAP-INT conformes : %d / %d" % (len(cap_int) - ci_errors, len(cap_int)))

    if total_errors == 0:
        ok("CHAÎNE COMPLÈTE — tous les profils aboutissent à une CAP")
    else:
        err("ANOMALIES : %d erreurs" % total_errors)

    return total_errors == 0


if __name__ == "__main__":
    ok_status = audit_chaine()
    sys.exit(0 if ok_status else 1)
