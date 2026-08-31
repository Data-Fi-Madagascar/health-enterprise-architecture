#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit SPARQL de cohérence — requêtes avancées sur le graphe RDF.

Exécute des requêtes SPARQL complémentaires sur dist/hea.ttl pour vérifier
la cohérence sémantique du référentiel. Nécessite rdflib (requirements.txt).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import sparql_rows, load_graph, section, ok, warn, err, info, C

QUERIES = {
    "Composants sans owner": """
        SELECT ?id ?title WHERE {
            ?s rdf:type hea:Composant .
            ?s hea:id ?id .
            ?s hea:title ?title .
            FILTER NOT EXISTS { ?s hea:owner ?o }
        }
        ORDER BY ?id
    """,

    "Composants sans FluxValeur": """
        SELECT ?id ?title WHERE {
            ?s rdf:type hea:Composant .
            ?s hea:id ?id .
            ?s hea:title ?title .
            FILTER NOT EXISTS { ?s hea:related ?x }
            FILTER NOT EXISTS { ?s hea:contributesTo ?x }
        }
        ORDER BY ?id
    """,

    "PT sans maps_to": """
        SELECT ?id ?title WHERE {
            ?s rdf:type hea:Profil .
            ?s hea:id ?id .
            ?s hea:title ?title .
            FILTER NOT EXISTS { ?s hea:mapsTo ?m }
        }
        ORDER BY ?id
    """,

    "Objets orphelins (aucun lien sortant)": """
        SELECT ?id ?type WHERE {
            ?s hea:id ?id .
            ?s rdf:type ?type .
            FILTER NOT EXISTS { ?s hea:related ?x }
            FILTER NOT EXISTS { ?s hea:mapsTo ?x }
            FILTER NOT EXISTS { ?s hea:contributesTo ?x }
            FILTER NOT EXISTS { ?s hea:realizedBy ?x }
            FILTER NOT EXISTS { ?s hea:performs ?x }
            FILTER NOT EXISTS { ?s hea:accesses ?x }
            FILTER NOT EXISTS { ?s hea:governs ?x }
            FILTER NOT EXISTS { ?s hea:appliesTo ?x }
            FILTER NOT EXISTS { ?s hea:implements ?x }
            FILTER NOT EXISTS { ?s hea:represents ?x }
        }
        ORDER BY ?id
    """,

    "Comptage par type RDF": """
        SELECT ?type (COUNT(?s) AS ?nb) WHERE {
            ?s rdf:type ?type .
        }
        GROUP BY ?type
        ORDER BY DESC(?nb)
    """,

    "Liens maps_to cassés (target absent du graphe)": """
        SELECT ?id ?mapsTo WHERE {
            ?s hea:id ?id .
            ?s hea:mapsTo ?target .
            BIND(STRAFTER(STR(?target), "#") AS ?mapsTo)
            FILTER NOT EXISTS { ?x hea:id ?mapsTo }
        }
        ORDER BY ?id
    """,

    # --- ART F.4 : Composants sans attache FluxValeur ---
    # Chaque composant doit être rattaché à au moins un flux de valeur
    "ART F.4 — Composants sans attache FluxValeur": """
        SELECT ?id ?title WHERE {
            ?s rdf:type hea:Composant .
            ?s hea:id ?id .
            ?s hea:title ?title .
            FILTER NOT EXISTS { ?s hea:soutientFluxDeValeur ?fv }
            FILTER NOT EXISTS { ?s hea:related ?fv . ?fv rdf:type hea:FluxValeur }
            FILTER NOT EXISTS { ?s hea:contributesTo ?fv . ?fv rdf:type hea:FluxValeur }
            FILTER NOT EXISTS { ?s hea:serves ?cap . ?cap rdf:type hea:Capabilite .
                               ?cap hea:contributesTo ?fv . ?fv rdf:type hea:FluxValeur }
        }
        ORDER BY ?id
    """,

    # --- P-INT-07 : Capabilités sans propriétaire fonctionnel ---
    # Chaque capabilité CNISN doit avoir un propriétaire désigné
    "P-INT-07 — Capabilités sans propriétaire": """
        SELECT ?id ?title WHERE {
            ?s rdf:type hea:CapaciteInteroperabilite .
            ?s hea:id ?id .
            ?s hea:title ?title .
            FILTER NOT EXISTS { ?s hea:owner ?o }
        }
        ORDER BY ?id
    """,

    # --- Composants sans owner (rappel) ---
    "Composants sans owner (rappel)": """
        SELECT ?id ?title WHERE {
            ?s rdf:type hea:Composant .
            ?s hea:id ?id .
            ?s hea:title ?title .
            FILTER NOT EXISTS { ?s hea:owner ?o }
        }
        ORDER BY ?id
    """,

    # --- Profils sans propriétaire fonctionnel ---
    "Profils sans propriétaire fonctionnel": """
        SELECT ?id ?title WHERE {
            ?s rdf:type hea:Profil .
            ?s hea:id ?id .
            ?s hea:title ?title .
            FILTER NOT EXISTS { ?s hea:aPourProprietaireFonctionnel ?pp }
            FILTER NOT EXISTS { ?s hea:owner ?o }
        }
        ORDER BY ?id
    """,
}


def audit_sparql():
    try:
        import rdflib  # noqa
    except ImportError:
        err("rdflib non installé. Exécutez : pip install -r requirements.txt")
        return False

    section("AUDIT SPARQL — Cohérence sémantique")

    g = load_graph()
    info("Graphe chargé : %d triples" % len(g))

    all_ok = True
    for title, sparql_query in QUERIES.items():
        section(title)
        try:
            results = sparql_rows(sparql_query)
        except Exception as e:
            err("Erreur SPARQL : %s" % e)
            all_ok = False
            continue

        if not results:
            ok("Aucune anomalie")
            continue

        if "Comptage" in title:
            for r in results:
                type_iri = r["type"]
                type_short = type_iri.split("#")[-1] if "#" in type_iri else type_iri.split("/")[-1]
                info("%-35s %s" % (type_short, r["nb"]))
        else:
            count = len(results)
            is_error = "sans owner" in title.lower() or "cassé" in title.lower()
            if is_error:
                err("%d anomalie(s) trouvée(s)" % count)
            else:
                warn("%d anomalie(s) trouvée(s)" % count)
            for r in results:
                parts = [v for v in r.values() if v]
                line = "  ".join(parts)
                if is_error:
                    err("  %s" % line)
                else:
                    warn("  %s" % line)
            if is_error:
                all_ok = False

    print()
    if all_ok:
        ok("COHÉRENCE SPARQL VÉRIFIÉE")
    else:
        err("ANOMALIES SPARQL DÉTECTÉES")

    return all_ok


if __name__ == "__main__":
    ok_status = audit_sparql()
    sys.exit(0 if ok_status else 1)
