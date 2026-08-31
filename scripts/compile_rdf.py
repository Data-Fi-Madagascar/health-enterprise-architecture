#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compile le référentiel HEA (YAML/Markdown) en graphe RDF Turtle.

Ce script est le pont entre la couche d'auteur humaine (Markdown + YAML
frontmatter) et la couche de raisonnement machine (RDF/OWL). Il parcourt
tous les objets du référentiel, extrait leurs métadonnées et génère un
graphe de triplets unifié au format Turtle.

Usage :
    python3 scripts/compile_rdf.py                    # génère dist/hea.ttl
    python3 scripts/compile_rdf.py --validate          # valide avec SHACL
    python3 scripts/compile_rdf.py --check             # vérifie sans écrire
    python3 scripts/compile_rdf.py --output /tmp/...   # chemin de sortie custom
"""

import argparse
import glob
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Namespace HEA
HEA_NS = "https://healmadagascar.mg/ontologie/hea#"
HEA_PREFIX = "hea"

# Mapping type YAML → classe OWL
TYPE_TO_CLASS = {
    "flux-valeur": "FluxValeur",
    "capabilite": "Capabilite",
    "principe": "Principe",
    "etape-valeur": "EtapeValeur",
    "processus-metier": "ProcessusMetier",
    "composant-applicatif": "Composant",
    "composant-infrastructure": "Composant",
    "composant-securite": "Composant",
    "composant-gouvernance": "Composant",
    "partie-prenante": "PartiePrenante",
    "capacite": "CapaciteInteroperabilite",
    "fondation": "Fondation",
    "exigence": "Exigence",
    "chapitre": "Chapitre",
    "profil": "Profil",
    "service": "Service",
    "acteur": "Acteur",
    "role": "Role",
    "lieu": "Lieu",
    "work-package": "WorkPackage",
    "plateau": "Plateau",
    "gap": "Gap",
    "objet-de-donnees": "ObjetDeDonnees",
    "objet-metier": "ObjetMetier",
}

# Mapping type YAML → propriété de relation principale
RELATION_FIELDS = ["maps_to", "implements", "applies_to", "related",
                   "realized_by", "contributes_to", "performs", "accesses",
                   "governs", "represents", "assigned_to", "has_role",
                   "located_at", "serves"]

# Property name mapping (snake_case → camelCase ArchiMate)
PROPERTY_MAP = {
    "maps_to": "mapsTo",
    "implements": "implements",
    "applies_to": "serves",       # Serving ArchiMate
    "related": "related",
    "realized_by": "realizedBy",
    "contributes_to": "contributesTo",
    "performs": "performs",
    "accesses": "accesses",
    "governs": "serves",          # Serving ArchiMate (merge with applies_to)
    "represents": "represents",
    "assigned_to": "assignedTo",
    "has_role": "hasRole",
    "located_at": "locatedAt",
    "serves": "serves",
}


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return text[3:end].strip("\n")


def fm_field(fm, key):
    m = re.search(r"^%s:\s*(.*)$" % re.escape(key), fm, re.MULTILINE)
    return m.group(1) if m else None


def list_value(raw):
    if raw is None:
        return []
    raw = raw.strip()
    if not raw or raw == "[]":
        return []
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1]
        items = re.findall(r"['\"]([^'\"]*)['\"]", inner)
        if items:
            return [i for i in items if i]
        return [x.strip() for x in inner.split(",") if x.strip()]
    return [x.strip().strip("'\"") for x in raw.split(",") if x.strip()]


def parse_id(fm):
    m = re.search(r"^id:\s*(.+)$", fm, re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip().strip('"').strip("'")


def parse_type(fm):
    m = re.search(r"^type:\s*(.+)$", fm, re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip().strip('"').strip("'")


def turtle_escape(value):
    """Échappe une valeur pour l'inclure dans un literal Turtle."""
    return value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")


def collect_objects():
    """Parcourt referentiel/ et renvoie la liste des objets avec leur frontmatter."""
    objects = []
    for path in sorted(glob.glob(os.path.join(REPO_ROOT, "referentiel", "**", "*.md"),
                                  recursive=True)):
        if os.path.basename(path) == "_schema.md":
            continue
        if os.path.basename(path) == "_index.yaml":
            continue
        text = open(path, encoding="utf-8").read()
        fm = parse_frontmatter(text)
        if fm is None:
            continue
        oid = parse_id(fm)
        otype = parse_type(fm)
        if not oid or not otype:
            continue

        obj = {
            "id": oid,
            "type": otype,
            "file": os.path.relpath(path, REPO_ROOT),
        }

        # Extraire les champs scalaires
        for field in ["title", "status", "owner", "version", "niveau",
                       "family", "envelope", "source"]:
            val = fm_field(fm, field)
            if val is not None:
                val = val.strip().strip('"').strip("'")
                obj[field] = val

        # Extraire les listes de relations
        for rel in RELATION_FIELDS:
            val = fm_field(fm, rel)
            if val is not None:
                items = list_value(val)
                if items:
                    obj[rel] = items

        # Extraire les tags
        tags_val = fm_field(fm, "tags")
        if tags_val is not None:
            obj["tags"] = list_value(tags_val)

        objects.append(obj)

    return objects


def resolve_property(rel, source_type, target):
    """Résout la propriété RDF en fonction du type source et de la cible.
    
    ArchiMate strict : même champ frontmatter, propriété différente selon le contexte.
    - applies_to sur Composant → serves (Serving)
    - applies_to sur Capabilite → contributesTo (Influence) quand cible est FluxValeur
    - governs → serves (Serving)
    """
    base = PROPERTY_MAP.get(rel, rel)

    # Type-dependent overrides
    if rel == "applies_to":
        if source_type in ("capabilite", "capacite-interoperabilite", "principe"):
            # Capabilite/Principe → FluxValeur = Influence (contributesTo)
            if target.startswith("VS-"):
                return "contributesTo"
            # Capabilite → Capabilite = Association (related)
            if target.startswith("CAP-"):
                return "related"
        # Composant → Capabilite/Service = Serving (serves)
        return "serves"

    return base


def generate_rdf(objects, output_path):
    """Génère un fichier Turtle RDF à partir des objets du référentiel."""
    lines = []
    lines.append("@prefix hea: <%s> ." % HEA_NS)
    lines.append("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .")
    lines.append("@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .")
    lines.append("@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .")
    lines.append("@prefix owl: <http://www.w3.org/2002/07/owl#> .")
    lines.append("")

    for obj in objects:
        oid = obj["id"]
        otype = obj["type"]
        owl_class = TYPE_TO_CLASS.get(otype)

        if not owl_class:
            # Type non reconnu — on crée quand même le nœud
            lines.append("hea:%s rdf:type hea:%s ;" % (oid, otype))
        else:
            lines.append("hea:%s rdf:type hea:%s ;" % (oid, owl_class))

        # ID literal (pour validation SHACL)
        lines.append('    hea:id "%s" ;' % turtle_escape(oid))

        # Champs scalaires
        if "title" in obj:
            lines.append('    hea:title "%s" ;' % turtle_escape(obj["title"]))
        if "status" in obj:
            lines.append('    hea:status "%s" ;' % turtle_escape(obj["status"]))
        if "owner" in obj:
            lines.append('    hea:owner "%s" ;' % turtle_escape(obj["owner"]))
        if "version" in obj:
            lines.append('    hea:version "%s" ;' % turtle_escape(obj["version"]))
        if "niveau" in obj:
            lines.append('    hea:niveau %s ;' % obj["niveau"])

        # Tags (comma-separated)
        if "tags" in obj:
            for tag in obj["tags"]:
                lines.append('    hea:tag "%s" ;' % turtle_escape(tag))

        # Relations (object properties)
        for rel in RELATION_FIELDS:
            if rel in obj:
                targets = obj[rel]
                for target in targets:
                    prop = resolve_property(rel, obj["type"], target)
                    lines.append("    hea:%s hea:%s ;" % (prop, target))

        # Dernière ligne : terminer par point au lieu de point-virgule
        if lines[-1].endswith(" ;"):
            lines[-1] = lines[-1][:-2] + " ."
        lines.append("")

    # Écrire le fichier
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return len(objects)


def validate_shacl(data_path, shapes_path):
    """Valide le graph RDF contre les shapes SHACL."""
    try:
        from rdflib import Graph
        from pyshacl import validate as shacl_validate
    except ImportError:
        print("[ERREUR] rdflib ou pyshacl non installé. "
              "Installer avec : pip install rdflib pyshacl")
        return False

    data_g = Graph()
    data_g.parse(data_path, format="turtle")

    shapes_g = Graph()
    shapes_g.parse(shapes_path, format="turtle")

    r = shacl_validate(
        data_g,
        shacl_graph=shapes_g,
        shacl_graph_format="turtle",
        data_graph_format="turtle",
    )
    conforms, results_graph, results_text = r

    print("\n=== Validation SHACL ===")
    print(results_text)

    if not conforms:
        print("[ERREUR] Le graphe RDF ne conforme pas aux shapes SHACL.")
    else:
        print("[OK] Le graphe RDF conforme aux shapes SHACL.")

    return conforms


def check_existing(output_path):
    """Vérifie si le fichier RDF existant est à jour (mode --check)."""
    if not os.path.exists(output_path):
        print("[ERREUR] Fichier RDF inexistant : %s" % output_path)
        return False

    # Comparer le nombre d'objets référentiel vs triplets RDF
    objects = collect_objects()
    with open(output_path, encoding="utf-8") as f:
        content = f.read()
    rdf_triples = content.count("rdf:type")

    if rdf_triples < len(objects):
        print("[ERREUR] Le fichier RDF contient %d types mais le référentiel "
              "a %d objets. Fichier désuet." % (rdf_triples, len(objects)))
        return False

    print("[OK] Fichier RDF à jour (%d objets, %d types RDF)."
          % (len(objects), rdf_triples))
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Compile le référentiel HEA en RDF Turtle")
    parser.add_argument("--output", "-o", default=None,
                        help="Chemin de sortie (défaut: dist/hea.ttl)")
    parser.add_argument("--validate", action="store_true",
                        help="Valider avec SHACL après compilation")
    parser.add_argument("--check", action="store_true",
                        help="Vérifier sans écrire (compare avec existant)")
    args = parser.parse_args()

    output_path = args.output or os.path.join(REPO_ROOT, "dist", "hea.ttl")
    shapes_path = os.path.join(REPO_ROOT, "ontologie", "hea-shapes.ttl")

    if args.check:
        ok = check_existing(output_path)
        sys.exit(0 if ok else 1)

    # Collecter les objets
    objects = collect_objects()
    if not objects:
        print("[ERREUR] Aucun objet trouvé dans referentiel/")
        sys.exit(1)

    # Générer le RDF
    count = generate_rdf(objects, output_path)
    print("=== Compilation RDF ===")
    print("Objets traités : %d" % count)
    print("Fichier généré : %s" % os.path.relpath(output_path, REPO_ROOT))

    # Validation SHACL optionnelle
    if args.validate:
        if not os.path.exists(shapes_path):
            print("[AVERTISSEMENT] Shapes SHACL introuvable : %s" % shapes_path)
        else:
            conforms = validate_shacl(output_path, shapes_path)
            if not conforms:
                sys.exit(1)

    print("\nRésumé : OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
