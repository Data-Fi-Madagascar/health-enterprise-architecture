#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pipeline bidirectionnel RDF ↔ Graphify.

Maintient la cohérence entre les deux structures de connaissance :
  - dist/hea.ttl          (RDF/OWL, 338 instances, propriétés ArchiMate)
  - graphify-out/graph.json (Graphify, 1432 nœuds, 2956 arêtes)

Usages :
    python3 scripts/sync_rdf_graphify.py                    # sync complet
    python3 scripts/sync_rdf_graphify.py --direction rdf    # enrichir RDF seulement
    python3 scripts/sync_rdf_graphify.py --direction gf     # enrichir Graphify seulement
    python3 scripts/sync_rdf_graphify.py --check            # vérifier sans écrire
    python3 scripts/sync_rdf_graphify.py --report           # rapport de cohérence seul
"""
import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
HEA_NS = "https://healmadagascar.mg/ontologie/hea#"
GRAPH_PATH = REPO_ROOT / "graphify-out" / "graph.json"
RDF_PATH = REPO_ROOT / "dist" / "hea.ttl"
ONTOLOGY_PATH = REPO_ROOT / "ontologie" / "hea.ttl"
SHAPES_PATH = REPO_ROOT / "ontologie" / "hea-shapes.ttl"
REPORT_PATH = REPO_ROOT / "graphify-out" / "COHERENCE_REPORT.md"


# ---------------------------------------------------------------------------
# 1. Parsing
# ---------------------------------------------------------------------------

def parse_rdf_instances(rdf_path):
    """Parse dist/hea.ttl et retourne {id: {type, title, status, owner, niveau, tags, props}}."""
    from rdflib import Graph, Namespace
    HEA = Namespace(HEA_NS)
    RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"

    g = Graph()
    g.parse(str(rdf_path), format="turtle")

    instances = {}
    for subj in g.subjects():
        s_str = str(subj)
        if "#" not in s_str:
            continue
        oid = s_str.split("#")[-1]
        if oid.startswith(("owl:", "rdfs:", "rdf:")):
            continue

        inst = {"id": oid, "rdf_type": None, "props": {}, "out_edges": []}

        for _, pred, obj in g.triples((subj, None, None)):
            p_str = str(pred)
            if p_str == RDF_NS + "type":
                inst["rdf_type"] = str(obj).split("#")[-1]
            elif p_str.startswith(HEA_NS):
                prop_name = p_str.split("#")[-1]
                val = str(obj).split("#")[-1] if "#" in str(obj) else str(obj)
                if prop_name not in inst["props"]:
                    inst["props"][prop_name] = []
                inst["props"][prop_name].append(val)
                if "#" in str(obj):
                    inst["out_edges"].append((prop_name, val))

        instances[oid] = inst

    return instances


def parse_graphify(graph_path):
    """Parse graphify-out/graph.json et retourne nodes, links."""
    with open(graph_path, encoding="utf-8") as f:
        gf = json.load(f)
    return gf["nodes"], gf.get("links", [])


# ---------------------------------------------------------------------------
# 2. Mapping file_path ↔ semantic_id
# ---------------------------------------------------------------------------

def build_id_mapping(rdf_instances, gf_nodes):
    """Construit la correspondance bidirectionnelle entre IDs RDF et Graphify.

    Stratégie :
      1. Match direct : node.id == rdf_instance.id (ex. SRV-01)
      2. Match par fichier : node.source_file contient le nom du fichier RDF
      3. Match par label : node.label ≈ rdf_instance.title
    """
    # Index RDF par title (normalisé)
    rdf_by_title = {}
    for oid, inst in rdf_instances.items():
        title = inst["props"].get("title", [""])[0].lower().strip()
        if title:
            rdf_by_title[oid] = title

    # Index RDF par file pattern (extraire le nom de fichier du path)
    rdf_by_file = {}
    for oid, inst in rdf_instances.items():
        # Chercher dans le referentiel le fichier qui contient cet ID
        rdf_by_file[oid] = oid.lower().replace("-", "_")

    mapping = {
        "gf_to_rdf": {},   # graphify_node_id → rdf_instance_id
        "rdf_to_gf": {},   # rdf_instance_id → [graphify_node_ids]
        "unmatched_rdf": [],
        "unmatched_gf": [],
    }

    # Pass 1: Match direct par ID
    rdf_ids = set(rdf_instances.keys())
    gf_ids_with_semantic = set()
    for node in gf_nodes:
        nid = node.get("id", "")
        # Vérifier si c'est un ID sémantique HEA (CAP-xx, VS-xx, etc.)
        if re.match(r"^[A-Z]+-\d+", nid):
            gf_ids_with_semantic.add(nid)
            if nid in rdf_ids:
                mapping["gf_to_rdf"][nid] = nid
                mapping["rdf_to_gf"].setdefault(nid, []).append(nid)

    # Pass 2: Match par source_file
    for node in gf_nodes:
        nid = node.get("id", "")
        src = node.get("source_file", "")
        if not src or nid in mapping["gf_to_rdf"]:
            continue
        # Extraire le pattern du fichier (ex. vs-02, cap-15, cmp-39)
        fname = Path(src).stem  # vs-02
        match = re.match(r"([a-z]+-\d+[a-z]?)", fname)
        if match:
            pattern = match.group(1).upper().replace("-", "-")
            # Chercher dans RDF
            for rdf_id in rdf_ids:
                if rdf_id.lower().replace("-", "-") == pattern.lower():
                    mapping["gf_to_rdf"][nid] = rdf_id
                    mapping["rdf_to_gf"].setdefault(rdf_id, []).append(nid)
                    break

    # Pass 3: Match par label (fuzzy)
    for node in gf_nodes:
        nid = node.get("id", "")
        if nid in mapping["gf_to_rdf"]:
            continue
        label = node.get("label", "").lower().strip()
        if not label or len(label) < 5:
            continue
        for rdf_id, rdf_title in rdf_by_title.items():
            if rdf_id in mapping["rdf_to_gf"]:
                continue
            # Match si le label est contenu dans le titre RDF ou vice versa
            if label in rdf_title or rdf_title in label:
                mapping["gf_to_rdf"][nid] = rdf_id
                mapping["rdf_to_gf"].setdefault(rdf_id, []).append(nid)
                break

    # Orphelins
    mapped_rdf = set(mapping["rdf_to_gf"].keys())
    mapping["unmatched_rdf"] = sorted(rdf_ids - mapped_rdf)
    mapped_gf = set(mapping["gf_to_rdf"].keys())
    all_gf_ids = {n.get("id", "") for n in gf_nodes}
    mapping["unmatched_gf"] = sorted(all_gf_ids - mapped_gf - {""})

    return mapping


# ---------------------------------------------------------------------------
# 3. Enrichir Graphify (direction GF ← RDF)
# ---------------------------------------------------------------------------

def enrich_graphify(gf_nodes, gf_links, rdf_instances, mapping):
    """Ajoute aux nœuds graphify les métadonnées RDF correspondantes."""
    enriched_nodes = 0
    enriched_links = 0

    for node in gf_nodes:
        nid = node.get("id", "")
        rdf_id = mapping["gf_to_rdf"].get(nid)
        if not rdf_id or rdf_id not in rdf_instances:
            continue

        inst = rdf_instances[rdf_id]
        node["rdf_type"] = inst["rdf_type"]
        node["rdf_id"] = rdf_id
        node["rdf_status"] = inst["props"].get("status", [""])[0]
        node["rdf_owner"] = inst["props"].get("owner", [""])[0]
        node["rdf_niveau"] = inst["props"].get("niveau", [""])[0]
        node["rdf_tags"] = inst["props"].get("tag", [])
        enriched_nodes += 1

    # Enrichir les arêtes : ajouter rdf_type si source et target sont dans RDF
    for link in gf_links:
        src_rdf = mapping["gf_to_rdf"].get(link.get("source", ""))
        tgt_rdf = mapping["gf_to_rdf"].get(link.get("target", ""))
        if src_rdf and tgt_rdf:
            # Chercher le type de propriété RDF correspondant
            src_inst = rdf_instances.get(src_rdf, {})
            for prop_name, targets in src_inst.get("props", {}).items():
                if tgt_rdf in targets:
                    link["rdf_property"] = prop_name
                    link["rdf_typed"] = True
                    enriched_links += 1
                    break

    return enriched_nodes, enriched_links


# ---------------------------------------------------------------------------
# 4. Enrichir RDF (direction RDF ← Graphify)
# ---------------------------------------------------------------------------

def compute_centrality(gf_nodes, gf_links):
    """Calcule la centralité de degré normalisée pour chaque nœud."""
    from collections import Counter
    degree = Counter()
    for link in gf_links:
        degree[link.get("source", "")] += 1
        degree[link.get("target", "")] += 1
    max_deg = max(degree.values()) if degree else 1
    return {nid: round(d / max_deg, 4) for nid, d in degree.items()}


def compute_communities(gf_nodes):
    """Extrait les communautés depuis les nœuds graphify."""
    communities = defaultdict(list)
    for node in gf_nodes:
        cid = node.get("community")
        cname = node.get("community_name", "")
        nid = node.get("id", "")
        if cid is not None and nid:
            communities[cid].append({"id": nid, "label": node.get("label", ""), "name": cname})
    return dict(communities)


def enrich_rdf(rdf_instances, gf_nodes, gf_links, mapping):
    """Génère les propriétés RDF à ajouter (community, centrality)."""
    centrality = compute_centrality(gf_nodes, gf_links)
    communities = compute_communities(gf_nodes)

    # Inverser le mapping rdf_to_gf
    rdf_to_gf = mapping["rdf_to_gf"]

    additions = {}  # rdf_id → {prop: value}

    for rdf_id, gf_ids in rdf_to_gf.items():
        props = {}
        # Centralité maximale parmi les nœuds graphify correspondants
        max_centrality = 0
        all_communities = set()
        for gid in gf_ids:
            c = centrality.get(gid, 0)
            if c > max_centrality:
                max_centrality = c
            # Trouver la communauté
            for node in gf_nodes:
                if node.get("id") == gid:
                    cid = node.get("community")
                    cname = node.get("community_name", "")
                    if cid is not None:
                        all_communities.add(f"{cid}:{cname}")
                    break

        if max_centrality > 0:
            props["centrality"] = str(max_centrality)
        if all_communities:
            props["community"] = list(all_communities)

        if props:
            additions[rdf_id] = props

    return additions


# ---------------------------------------------------------------------------
# 5. Écrire les enrichissements
# ---------------------------------------------------------------------------

def write_enriched_graph(gf_nodes, gf_links, output_path):
    """Écrit graph.json enrichi avec les métadonnées RDF."""
    enriched = {
        "directed": False,
        "multigraph": False,
        "graph": {"enriched_with_rdf": True, "sync_version": "1.0"},
        "nodes": gf_nodes,
        "links": gf_links,
        "hyperedges": [],
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(enriched, f, indent=2, ensure_ascii=False)
    return output_path


def write_enriched_rdf(rdf_path, additions, output_path):
    """Écrit hea.ttl enrichi avec community et centrality depuis Graphify."""
    content = Path(rdf_path).read_text(encoding="utf-8")

    # Insérer avant le dernier point final de chaque instance
    lines = content.split("\n")
    new_lines = []
    current_id = None

    for line in lines:
        # Détecter le début d'une instance
        m = re.match(r"^(hea:\S+)\s+rdf:type\s+hea:", line)
        if m:
            current_id = m.group(1).replace("hea:", "")

        new_lines.append(line)

        # Si on arrive à la fin d'une instance (ligne se terminant par " .")
        if current_id and line.rstrip().endswith(" .") and current_id in additions:
            props = additions[current_id]
            insert_lines = []
            # Retirer le point final de la ligne précédente
            if new_lines[-1].rstrip().endswith(" ."):
                new_lines[-1] = new_lines[-1].rstrip()[:-2] + " ;"

            if "centrality" in props:
                val = props["centrality"]
                insert_lines.append(f'    hea:centrality "{val}" ;')
            if "community" in props:
                for comm in props["community"]:
                    insert_lines.append(f'    hea:community "{comm}" ;')

            # Dernière ligne insérée se termine par point
            if insert_lines:
                insert_lines[-1] = insert_lines[-1].rstrip()[:-2] + " ."

            new_lines.extend(insert_lines)
            current_id = None

    Path(output_path).write_text("\n".join(new_lines), encoding="utf-8")
    return output_path


# ---------------------------------------------------------------------------
# 6. Rapport de cohérence
# ---------------------------------------------------------------------------

def generate_report(rdf_instances, gf_nodes, gf_links, mapping, additions,
                    enriched_nodes, enriched_links):
    """Génère un rapport de cohérence markdown."""
    total_rdf = len(rdf_instances)
    total_gf = len(gf_nodes)
    mapped = len(mapping["gf_to_rdf"])
    unmatched_rdf = len(mapping["unmatched_rdf"])
    unmatched_gf_count = len(mapping["unmatched_gf"])

    # Arêtes RDF typées dans graphify
    typed_edges = sum(1 for l in gf_links if l.get("rdf_typed"))

    # Communautés graphify
    communities = compute_communities(gf_nodes)

    # Distribution des types RDF
    rdf_types = Counter(inst.get("rdf_type", "?") for inst in rdf_instances.values())

    # Centralité
    centrality = compute_centrality(gf_nodes, gf_links)

    # Top nœuds enrichis
    enriched_gf_nodes = [n for n in gf_nodes if n.get("rdf_type")]
    enriched_gf_nodes.sort(key=lambda n: centrality.get(n["id"], 0), reverse=True)

    lines = []
    lines.append("# Rapport de cohérence RDF ↔ Graphify")
    lines.append("")
    lines.append(f"**Date** : généré par `scripts/sync_rdf_graphify.py`")
    lines.append("")

    lines.append("## Vue d'ensemble")
    lines.append("")
    lines.append("| Métrique | Valeur |")
    lines.append("|----------|--------|")
    lines.append(f"| Instances RDF | {total_rdf} |")
    lines.append(f"| Nœuds Graphify | {total_gf} |")
    lines.append(f"| **Objets mappés** | **{mapped}** ({100*mapped/max(total_rdf,1):.0f}% du RDF) |")
    lines.append(f"| RDF non mappé | {unmatched_rdf} |")
    lines.append(f"| Graphify non mappé | {unmatched_gf_count} |")
    lines.append(f"| Arêtes RDF typées dans Graphify | {typed_edges} |")
    lines.append(f"| Nœuds Graphify enrichis RDF | {enriched_nodes} |")
    lines.append(f"| Communautés Graphify | {len(communities)} |")
    lines.append("")

    lines.append("## Mapping détaillé (objets mappés)")
    lines.append("")
    lines.append("| RDF ID | Type RDF | Graphify ID | Label Graphify |")
    lines.append("|--------|----------|-------------|----------------|")
    for rdf_id in sorted(mapping["rdf_to_gf"].keys()):
        inst = rdf_instances.get(rdf_id, {})
        rdf_type = inst.get("rdf_type", "?")
        for gid in mapping["rdf_to_gf"][rdf_id]:
            gf_node = next((n for n in gf_nodes if n["id"] == gid), {})
            label = gf_node.get("label", "?")[:50]
            lines.append(f"| {rdf_id} | {rdf_type} | {gid} | {label} |")

    lines.append("")
    lines.append("## Top 10 nœuds enrichis (par centralité)")
    lines.append("")
    lines.append("| Nœud | RDF Type | Centralité | Communauté |")
    lines.append("|------|----------|------------|------------|")
    for node in enriched_gf_nodes[:10]:
        nid = node["id"]
        c = centrality.get(nid, 0)
        cname = node.get("community_name", "?")
        lines.append(f"| {nid[:35]} | {node.get('rdf_type','?')} | {c:.4f} | {cname} |")

    lines.append("")
    lines.append("## RDF non mappé (20 premiers)")
    lines.append("")
    for oid in mapping["unmatched_rdf"][:20]:
        inst = rdf_instances.get(oid, {})
        lines.append(f"- `{oid}` ({inst.get('rdf_type', '?')}) — {inst.get('props', {}).get('title', ['?'])[0]}")

    lines.append("")
    lines.append("## Propriétés enrichies ajoutées au RDF")
    lines.append("")
    lines.append("| Instance | centrality | community |")
    lines.append("|----------|------------|-----------|")
    for rdf_id, props in sorted(additions.items())[:20]:
        c = props.get("centrality", "-")
        comm = ", ".join(props.get("community", []))[:50]
        lines.append(f"| {rdf_id} | {c} | {comm} |")

    lines.append("")
    lines.append("## Recommandations")
    lines.append("")
    if unmatched_rdf > 50:
        lines.append(f"- **{unmatched_rdf} instances RDF non mappées** — ajouter des `source_file` ou des `id` dans le frontmatter pour améliorer le matching")
    if unmatched_gf_count > 500:
        lines.append(f"- **{unmatched_gf_count} nœuds Graphify non mappés** — ce sont des sections, headings, fragments de texte qui n'ont pas d'instance RDF correspondante (normal)")
    if typed_edges < 10:
        lines.append(f"- **Seulement {typed_edges} arêtes RDF typées** — le mapping fichier→ID pourrait être amélioré")
    lines.append(f"- `scripts/compile_rdf.py --validate` doit rester CONFORME après ajout des propriétés enrichies")
    lines.append(f"- Relancer `python3 scripts/sync_rdf_graphify.py` après chaque `graphify update`")

    report = "\n".join(lines)
    REPORT_PATH.write_text(report, encoding="utf-8")
    return report


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Pipeline bidirectionnel RDF ↔ Graphify")
    parser.add_argument("--direction", choices=["rdf", "gf", "both"], default="both",
                        help="Sens du sync (défaut: both)")
    parser.add_argument("--check", action="store_true",
                        help="Vérifier sans écrire")
    parser.add_argument("--report", action="store_true",
                        help="Générer le rapport de cohérence seul")
    args = parser.parse_args()

    print("=" * 60)
    print("SYNC RDF ↔ GRAPHIFY")
    print("=" * 60)

    # Vérifier l'existence des fichiers
    if not RDF_PATH.exists():
        print(f"[ERREUR] {RDF_PATH} introuvable. Lancer d'abord compile_rdf.py")
        sys.exit(1)
    if not GRAPH_PATH.exists():
        if args.check:
            print(f"[AVERTISSEMENT] {GRAPH_PATH} introuvable. Sync RDF↔Graphify ignoré en mode --check.")
            print("[MODE CHECK] Aucune écriture effectuée. Sync RDF↔Graphify: SKIP (fichier manquant)")
            return
        else:
            print(f"[ERREUR] {GRAPH_PATH} introuvable. Lancer d'abord graphify")
            sys.exit(1)

    # 1. Charger les deux graphes
    print("\n[1/6] Chargement des graphes...")
    rdf_instances = parse_rdf_instances(RDF_PATH)
    gf_nodes, gf_links = parse_graphify(GRAPH_PATH)
    print(f"  RDF: {len(rdf_instances)} instances")
    print(f"  Graphify: {len(gf_nodes)} nœuds, {len(gf_links)} arêtes")

    # 2. Construire le mapping
    print("\n[2/6] Construction du mapping...")
    mapping = build_id_mapping(rdf_instances, gf_nodes)
    print(f"  Mappés: {len(mapping['gf_to_rdf'])} nœuds GF → RDF")
    print(f"  RDF→GF: {len(mapping['rdf_to_gf'])} instances")
    print(f"  RDF orphelins: {len(mapping['unmatched_rdf'])}")
    print(f"  GF orphelins: {len(mapping['unmatched_gf'])}")

    if args.check:
        print("\n[MODE CHECK] Aucune écriture effectuée.")
        print(f"  Mapping: {len(mapping['gf_to_rdf'])} objets mappés")
        return

    # 3. Enrichir Graphify
    enriched_nodes = enriched_links = 0
    if args.direction in ("gf", "both"):
        print("\n[3/6] Enrichissement Graphify (← RDF)...")
        enriched_nodes, enriched_links = enrich_graphify(
            gf_nodes, gf_links, rdf_instances, mapping)
        print(f"  Nœuds enrichis: {enriched_nodes}")
        print(f"  Arêtes typées: {enriched_links}")
    else:
        print("\n[3/6] Enrichissement Graphify: SKIP")

    # 4. Enrichir RDF
    additions = {}
    if args.direction in ("rdf", "both"):
        print("\n[4/6] Enrichissement RDF (← Graphify)...")
        additions = enrich_rdf(rdf_instances, gf_nodes, gf_links, mapping)
        print(f"  Instances à enrichir: {len(additions)}")
    else:
        print("\n[4/6] Enrichissement RDF: SKIP")

    # 5. Écrire
    if not args.report:
        print("\n[5/6] Écriture...")
        if args.direction in ("gf", "both"):
            out_gf = GRAPH_PATH  # overwrite
            write_enriched_graph(gf_nodes, gf_links, out_gf)
            print(f"  Graphify écrit: {out_gf}")
        if args.direction in ("rdf", "both") and additions:
            out_rdf = RDF_PATH.parent / "hea-enriched.ttl"
            write_enriched_rdf(RDF_PATH, additions, out_rdf)
            print(f"  RDF enrichi écrit: {out_rdf}")
            print(f"  (le fichier original {RDF_PATH} n'est pas modifié)")
    else:
        print("\n[5/6] Écriture: SKIP (mode report)")

    # 6. Rapport
    print("\n[6/6] Rapport de cohérence...")
    report = generate_report(
        rdf_instances, gf_nodes, gf_links, mapping, additions,
        enriched_nodes, enriched_links)
    print(f"  Rapport écrit: {REPORT_PATH}")

    # Résumé
    print("\n" + "=" * 60)
    print("RÉSUMÉ")
    print("=" * 60)
    print(f"  Mapping: {len(mapping['gf_to_rdf'])} objets mappés")
    print(f"  Graphify enrichi: {enriched_nodes} nœuds, {enriched_links} arêtes RDF typées")
    print(f"  RDF enrichi: {len(additions)} instances avec community/centrality")
    print(f"  Rapport: {REPORT_PATH}")

    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
