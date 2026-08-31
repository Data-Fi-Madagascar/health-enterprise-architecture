#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utilitaires partagés pour les scripts d'audit HEA — tous basés sur SPARQL."""

import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TTL_PATH = os.path.join(REPO_ROOT, "dist", "hea.ttl")

# Namespace HEA
HEA = "https://healmadagascar.mg/ontologie/hea#"
PREFIXES = """
PREFIX hea: <https://healmadagascar.mg/ontologie/hea#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
"""


class C:
    OK = "\033[92m"
    WARN = "\033[93m"
    ERR = "\033[91m"
    INFO = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


_graph = None


def load_graph():
    """Charge le graphe RDF (une seule fois)."""
    global _graph
    if _graph is not None:
        return _graph
    try:
        from rdflib import Graph
    except ImportError:
        print("%s[ERREUR]%s rdflib non installé. pip install -r requirements.txt"
              % (C.ERR, C.RESET))
        sys.exit(1)
    if not os.path.exists(TTL_PATH):
        print("%s[ERREUR]%s Fichier RDF introuvable : %s" % (C.ERR, C.RESET, TTL_PATH))
        print("  Exécutez : python3 scripts/compile_rdf.py")
        sys.exit(1)
    _graph = Graph()
    _graph.parse(TTL_PATH, format="turtle")
    return _graph


def sparql(query):
    """Exécute une requête SPARQL et retourne les résultats."""
    g = load_graph()
    return list(g.query(PREFIXES + query))


def sparql_one(query, col):
    """Retourne une liste de valeurs pour une colonne donnée."""
    rows = sparql(query)
    return [getattr(row, col) for row in rows if getattr(row, col) is not None]


def sparql_rows(query):
    """Retourne une liste de dicts (plus pratique)."""
    g = load_graph()
    results = g.query(PREFIXES + query)
    cols = results.vars
    return [{str(c): str(row[c]) if row[c] is not None else None for c in cols}
            for row in results]


def str_val(v):
    """Extrait la valeur string d'un Literal RDF."""
    return str(v) if v is not None else None


def section(title):
    print("\n%s%s%s" % (C.BOLD, title, C.RESET))
    print("-" * len(title))


def ok(msg):
    print("  %s[OK]%s %s" % (C.OK, C.RESET, msg))


def warn(msg):
    print("  %s[!!]%s %s" % (C.WARN, C.RESET, msg))


def err(msg):
    print("  %s[ERREUR]%s %s" % (C.ERR, C.RESET, msg))


def info(msg):
    print("  %s[i]%s %s" % (C.INFO, C.RESET, msg))
