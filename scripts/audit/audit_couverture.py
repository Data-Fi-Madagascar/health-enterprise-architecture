#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit de couverture des capabilités CAESN via SPARQL.

Vérifie :
  1. Chaque CAP (hea:Capabilite) est couverte par au moins un PT via chaîne transitive
  2. Les CAP-INT orphelins (pas de PT qui les pointe) sont listés
  3. Les CAP non couvertes sont identifiées
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import sparql_rows, section, ok, warn, err, info


def audit_couverture():
    section("AUDIT DE COUVERTURE — Capabilités CAESN")

    # Couverture transitive : PT → CAP-INT → CAP
    covered = sparql_rows("""
        SELECT DISTINCT ?capId ?capTitle ?ptId ?viaCi WHERE {
            ?pt rdf:type hea:Profil .
            ?pt hea:id ?ptId .
            ?pt hea:mapsTo ?ci .
            ?ci rdf:type hea:CapaciteInteroperabilite .
            ?ci hea:id ?viaCi .
            ?ci hea:mapsTo ?cap .
            ?cap rdf:type hea:Capabilite .
            ?cap hea:id ?capId .
            ?cap hea:title ?capTitle .
        }
        ORDER BY ?capId ?ptId
    """)

    # Couverture directe : PT → CAP (bypass CAP-INT)
    covered_direct = sparql_rows("""
        SELECT DISTINCT ?capId ?capTitle ?ptId WHERE {
            ?pt rdf:type hea:Profil .
            ?pt hea:id ?ptId .
            ?pt hea:mapsTo ?cap .
            ?cap rdf:type hea:Capabilite .
            ?cap hea:id ?capId .
            ?cap hea:title ?capTitle .
        }
        ORDER BY ?capId ?ptId
    """)

    # CAP-INT orphelins (pas de PT qui les pointe)
    orphelins = sparql_rows("""
        SELECT ?id ?title WHERE {
            ?ci rdf:type hea:CapaciteInteroperabilite .
            ?ci hea:id ?id .
            ?ci hea:title ?title .
            FILTER NOT EXISTS {
                ?pt rdf:type hea:Profil .
                ?pt hea:mapsTo ?ci .
            }
        }
        ORDER BY ?id
    """)

    # Toutes les CAP
    all_caps = sparql_rows("""
        SELECT ?id ?title WHERE {
            ?s rdf:type hea:Capabilite .
            ?s hea:id ?id .
            ?s hea:title ?title .
        }
        ORDER BY ?id
    """)

    # Index : capId → [(ptId, viaCi)]
    cov = {}
    for r in covered:
        cov.setdefault(r["capId"], []).append((r["ptId"], r["viaCi"]))
    for r in covered_direct:
        cov.setdefault(r["capId"], []).append((r["ptId"], "direct"))

    section("Couverture des CAP (hea:Capabilite)")
    uncovered = []
    for cap in all_caps:
        cid = cap["id"]
        title = cap["title"][:45]
        sources = cov.get(cid, [])
        if not sources:
            uncovered.append((cid, title))
        else:
            labels = ["%s via %s" % (pt, via) if via != "direct" else "%s (direct)" % pt
                       for pt, via in sources]
            ok("%s — %s ← %s" % (cid, title, ", ".join(labels)))

    section("CAP-INT orphelins (pas de PT qui les pointe)")
    for r in orphelins:
        warn("%s — %s : aucun PT ne cible cette CAP-INT" % (r["id"], r["title"][:45]))

    section("Résumé")
    # Séparer les CAP sans aucune référence (gap pur) de celles référencées mais non couvertes
    unreferenced = []
    referenced_but_uncovered = []
    for cid, title in uncovered:
        has_ref = sparql_rows("""
            SELECT ?id WHERE {
                { ?x hea:related ?s . ?s hea:id "%s" }
                UNION
                { ?x hea:appliesTo ?s . ?s hea:id "%s" }
                UNION
                { ?s hea:appliesTo ?x . ?x hea:id "%s" }
                ?x hea:id ?id .
                FILTER (?id != "%s")
            }
            LIMIT 1
        """ % (cid, cid, cid, cid))
        if has_ref:
            referenced_but_uncovered.append((cid, title))
        else:
            unreferenced.append((cid, title))

    info("CAP couvertes : %d / %d" % (len(all_caps) - len(uncovered), len(all_caps)))
    info("CAP-INT orphelins : %d" % len(orphelins))

    total_issues = len(orphelins)
    if unreferenced:
        err("CAP non couvertes (gap stratégique — aucune chaîne PT) : %d" % len(unreferenced))
        for cid, title in unreferenced:
            err("  %s — %s" % (cid, title))
    if referenced_but_uncovered:
        warn("CAP référencées mais sans chaîne PT→CAP-INT : %d" % len(referenced_but_uncovered))
        for cid, title in referenced_but_uncovered:
            warn("  %s — %s" % (cid, title))

    print()
    if total_issues == 0 and not unreferenced:
        ok("COUVERTURE CONFORME")
    elif total_issues == 0:
        warn("COUVERTURE PARTIELLE — %d CAP stratégiques sans chaîne PT (gap documenté)"
            % len(unreferenced))
    else:
        err("ANOMALIES : %d CAP-INT orphelins, %d gaps stratégiques"
            % (len(orphelins), len(unreferenced)))

    return total_issues == 0


if __name__ == "__main__":
    ok_status = audit_couverture()
    sys.exit(0 if ok_status else 1)
