#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit de conformité du portefeuille d'initiatives via SPARQL.

Vérifie pour chaque composant (hea:Composant) :
  1. Un propriétaire fonctionnel est désigné (hea:owner)
  2. Un rattachement à un flux de valeur national existe (direct ou indirect)

Critères : ART-SN F.4, P-INT-07
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import sparql, sparql_rows, section, ok, warn, err, info


def audit_conformite():
    section("AUDIT DE CONFORMITÉ — Portefeuille d'initiatives")

    # Composants sans owner
    no_owner = sparql_rows("""
        SELECT ?id ?title WHERE {
            ?s rdf:type hea:Composant .
            ?s hea:id ?id .
            ?s hea:title ?title .
            FILTER NOT EXISTS { ?s hea:owner ?o }
        }
        ORDER BY ?id
    """)

    # Composants sans lien VS (ni direct ni indirect via CAP-INT → FluxValeur)
    # Direct : ?s hea:related/contributesTo/realizedBy/appliesTo → hea:FluxValeur
    # Indirect : ?s hea:mapsTo → ?capInt ?capInt hea:mapsTo → hea:FluxValeur
    no_vs = sparql_rows("""
        SELECT ?id ?title ?owner WHERE {
            ?s rdf:type hea:Composant .
            ?s hea:id ?id .
            ?s hea:title ?title .
            OPTIONAL { ?s hea:owner ?owner }
            # Pas de lien direct vers FluxValeur
            FILTER NOT EXISTS {
                ?s hea:related ?target .
                ?target rdf:type hea:FluxValeur .
            }
            FILTER NOT EXISTS {
                ?s hea:contributesTo ?target .
                ?target rdf:type hea:FluxValeur .
            }
            FILTER NOT EXISTS {
                ?s hea:realizedBy ?target .
                ?target rdf:type hea:FluxValeur .
            }
            FILTER NOT EXISTS {
                ?s hea:appliesTo ?target .
                ?target rdf:type hea:FluxValeur .
            }
            # Pas de lien indirect non plus (via CAP-INT → FluxValeur)
            FILTER NOT EXISTS {
                ?s hea:mapsTo ?capInt .
                ?capInt hea:mapsTo ?fv .
                ?fv rdf:type hea:FluxValeur .
            }
        }
        ORDER BY ?id
    """)

    # Composants avec lien VS direct uniquement
    has_direct = sparql_rows("""
        SELECT DISTINCT ?id WHERE {
            { ?s hea:related ?t . ?t rdf:type hea:FluxValeur }
            UNION
            { ?s hea:contributesTo ?t . ?t rdf:type hea:FluxValeur }
            UNION
            { ?s hea:realizedBy ?t . ?t rdf:type hea:FluxValeur }
            UNION
            { ?s hea:appliesTo ?t . ?t rdf:type hea:FluxValeur }
            ?s rdf:type hea:Composant .
            ?s hea:id ?id .
        }
    """)
    direct_ids = {r["id"] for r in has_direct}

    # Tous les composants
    all_comp = sparql_rows("""
        SELECT ?id ?title WHERE {
            ?s rdf:type hea:Composant .
            ?s hea:id ?id .
            ?s hea:title ?title .
        }
        ORDER BY ?id
    """)

    info("Composants : %d" % len(all_comp))

    # Comptage
    no_owner_ids = {r["id"] for r in no_owner}
    no_vs_ids = {r["id"] for r in no_vs}

    conforms = [c for c in all_comp if c["id"] not in no_owner_ids and c["id"] not in no_vs_ids]
    vs_indirect = [c for c in all_comp if c["id"] in no_vs_ids and c["id"] not in no_owner_ids
                   and c["id"] not in direct_ids]

    info("Conformes : %d / %d" % (len(conforms), len(all_comp)))
    for c in conforms:
        ok("%s — %s" % (c["id"], c["title"][:55]))

    if no_owner:
        err("Sans propriétaire : %d" % len(no_owner))
        for r in no_owner:
            err("%s — %s" % (r["id"], r["title"][:55]))

    if no_vs:
        warn("Sans aucun rattachement VS : %d" % len(no_vs))
        for r in no_vs:
            owner = r.get("owner", "?")
            warn("%s — %s (owner: %s)" % (r["id"], r["title"][:55], owner))

    total_issues = len(no_owner) + len(no_vs)
    print()
    if total_issues == 0:
        ok("PORTFEUILLE CONFORME")
    else:
        err("ANOMALIES DÉTECTÉES : %d" % total_issues)

    return total_issues == 0


if __name__ == "__main__":
    ok_status = audit_conformite()
    sys.exit(0 if ok_status else 1)
