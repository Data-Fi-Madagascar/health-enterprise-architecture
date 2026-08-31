#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit SPARQL de cohérence sur le graphe RDF.

Exécute des requêtes SPARQL sur dist/hea.ttl pour vérifier la cohérence
sémantique du référentiel. Nécessite rdflib (pip install -r requirements.txt).

Requêtes :
  1. Composants sans propriétaire (owner)
  2. Composants sans rattachement VS (via processus ou directement)
  3. PT sans maps_to valide
  4. Objets orphelins (aucun lien sortant)
  5. Liens cassés (target inexistant dans le graphe)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import REPO_ROOT, section, ok, warn, err, info, C

TTL_PATH = os.path.join(REPO_ROOT, "dist", "hea.ttl")

PREFIXES = """
PREFIX hea: <https://healmadagascar.mg/ontologie/hea#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
"""

QUERIES = {
    "Composants sans owner": """
        SELECT ?id ?title WHERE {
            ?s a hea:Composant .
            ?s hea:id ?id .
            ?s hea:title ?title .
            OPTIONAL { ?s hea:owner ?o }
            FILTER (!BOUND(?o))
        }
        ORDER BY ?id
    """,

    "Composants sans FluxValeur": """
        SELECT ?id ?title WHERE {
            ?s a hea:Composant .
            ?s hea:id ?id .
            ?s hea:title ?title .
            OPTIONAL { ?s hea:related ?target }
            OPTIONAL { ?s hea:contributesTo ?target2 }
            FILTER (!BOUND(?target) && !BOUND(?target2))
        }
        ORDER BY ?id
    """,

    "PT sans maps_to": """
        SELECT ?id ?title WHERE {
            ?s a hea:Profil .
            ?s hea:id ?id .
            ?s hea:title ?title .
            OPTIONAL { ?s hea:mapsTo ?m }
            FILTER (!BOUND(?m))
        }
        ORDER BY ?id
    """,

    "Objets orphelins (aucun lien sortant)": """
        SELECT ?id ?type WHERE {
            ?s hea:id ?id .
            ?s a ?type .
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

    "Comptage par type": """
        SELECT ?type (COUNT(?s) AS ?nb) WHERE {
            ?s a ?type .
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
}


def audit_sparql():
    try:
        from rdflib import Graph
    except ImportError:
        err("rdflib non installé. Exécutez : pip install -r requirements.txt")
        return False

    if not os.path.exists(TTL_PATH):
        err("Fichier RDF introuvable : %s" % TTL_PATH)
        err("Exécutez d'abord : python3 scripts/compile_rdf.py")
        return False

    section("AUDIT SPARQL — Cohérence sémantique")

    g = Graph()
    g.parse(TTL_PATH, format="turtle")
    triples = len(g)
    info("Graphe chargé : %d triples" % triples)

    all_ok = True
    for title, sparql in QUERIES.items():
        section(title)
        try:
            results = list(g.query(PREFIXES + sparql))
        except Exception as e:
            err("Erreur SPARQL : %s" % e)
            all_ok = False
            continue

        if not results:
            ok("Aucune anomalie")
            continue

        if title == "Comptage par type":
            for row in results:
                type_iri = str(row.type)
                type_short = type_iri.split("#")[-1] if "#" in type_iri else type_iri.split("/")[-1]
                info("%-35s %d" % (type_short, int(row.nb)))
        else:
            count = len(results)
            is_error = "sans owner" in title.lower() or "cassé" in title.lower()
            if is_error:
                err("%d anomalie(s) trouvée(s)" % count)
            else:
                warn("%d anomalie(s) trouvée(s)" % count)
            for row in results:
                row_str = "  ".join(str(v) for v in row if v is not None)
                if is_error:
                    err("  %s" % row_str)
                else:
                    warn("  %s" % row_str)
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
