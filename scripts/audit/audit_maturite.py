#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit de maturité du référentiel via SPARQL.

Vérifie :
  1. Distribution des statuts (draft/active/stable/candidate/deprecated)
  2. Statuts invalides
  3. Cohérence status ↔ type (CAP devrait être stable/candidate, PT active)
  4. Objets sans version
  5. Objets dépréciés
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import sparql_rows, section, ok, warn, err, info

VALID_STATUSES = {"draft", "active", "stable", "candidate", "deprecated"}

# Statuts attendus par type OWL
STATUS_BY_TYPE = {
    "Profil": {"active", "stable"},
    "CapaciteInteroperabilite": {"stable", "candidate"},
    "Capabilite": {"stable", "candidate"},
    "FluxValeur": {"active", "stable"},
    "ProcessusMetier": {"active", "stable"},
    "Composant": {"active", "stable", "candidate"},
}


def audit_maturite():
    section("AUDIT DE MATURITÉ — Référentiel HEA")

    # Distribution des statuts
    section("Distribution des statuts")
    dist = sparql_rows("""
        SELECT ?status (COUNT(?s) AS ?nb) WHERE {
            ?s hea:status ?status .
        }
        GROUP BY ?status
        ORDER BY DESC(?nb)
    """)
    for r in dist:
        st = r["status"]
        nb = int(r["nb"])
        label = st if st in VALID_STATUSES else "(invalide: %s)" % st
        info("%-20s %d objets" % (label, nb))

    # Statuts invalides
    section("Statuts invalides")
    invalid = sparql_rows("""
        SELECT ?id ?type ?status WHERE {
            ?s hea:id ?id .
            ?s hea:status ?status .
            ?s rdf:type ?type .
            FILTER (?status NOT IN ("draft","active","stable","candidate","deprecated"))
        }
        ORDER BY ?id
    """)
    if invalid:
        for r in invalid:
            type_short = r["type"].split("#")[-1]
            err("%s (%s) — status '%s' invalide" % (r["id"], type_short, r["status"]))
    else:
        ok("Aucun statut invalide")

    # Cohérence status/type
    section("Cohérence status ↔ type")
    incoherent = []
    for owl_class, expected in STATUS_BY_TYPE.items():
        rows = sparql_rows("""
            SELECT ?id ?status WHERE {
                ?s rdf:type hea:%s .
                ?s hea:id ?id .
                ?s hea:status ?status .
                FILTER (?status NOT IN (%s))
            }
            ORDER BY ?id
        """ % (owl_class, ",".join('"%s"' % s for s in sorted(expected))))
        for r in rows:
            incoherent.append((r["id"], owl_class, r["status"], expected))

    if incoherent:
        for oid, otype, st, expected in incoherent:
            warn("%s (%s) — status '%s' inattendu (attendu: %s)"
                 % (oid, otype, st, "/".join(sorted(expected))))
    else:
        ok("Tous les statuts sont cohérents avec le type")

    # Objets sans version
    section("Objets sans version")
    no_version = sparql_rows("""
        SELECT ?id ?type WHERE {
            ?s hea:id ?id .
            ?s rdf:type ?type .
            FILTER NOT EXISTS { ?s hea:version ?v }
        }
        ORDER BY ?id
    """)
    total = sparql_rows("SELECT (COUNT(?s) AS ?nb) WHERE { ?s hea:id ?id }")
    total_count = int(total[0]["nb"]) if total else 0
    if no_version:
        for r in no_version:
            type_short = r["type"].split("#")[-1]
            warn("%s (%s)" % (r["id"], type_short))
        info("Objets sans version : %d / %d" % (len(no_version), total_count))
    else:
        ok("Tous les objets ont une version")

    # Objets dépréciés
    section("Objets dépréciés")
    deprecated = sparql_rows("""
        SELECT ?id ?type ?title WHERE {
            ?s hea:id ?id .
            ?s hea:status "deprecated" .
            ?s rdf:type ?type .
            ?s hea:title ?title .
        }
        ORDER BY ?id
    """)
    if deprecated:
        for r in deprecated:
            type_short = r["type"].split("#")[-1]
            warn("%s — %s (%s)" % (r["id"], r["title"][:40], type_short))
        info("Objets dépréciés : %d" % len(deprecated))
    else:
        ok("Aucun objet déprécié")

    # Résumé
    print()
    total_issues = len(invalid) + len(incoherent)
    if total_issues == 0:
        ok("MATURITÉ CONFORME")
    else:
        err("ANOMALIES : %d statuts invalides, %d incohérences type/status"
            % (len(invalid), len(incoherent)))

    return total_issues == 0


if __name__ == "__main__":
    ok_status = audit_maturite()
    sys.exit(0 if ok_status else 1)
