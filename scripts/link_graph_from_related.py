#!/usr/bin/env python3
"""Restaure dans graphify-out/graph.json les aretes 'related' definies dans le
frontmatter des .md (source de verite), que le builder semantique de graphify
(0.9.48) ignore.

Le builder d'origine frontmatter-aware etant absent et la regeneration
semantique bloquee (budget/clause API), ce script tient lieu de composant
manquant : il derive les aretes du graphe a partir des champs 'related' du
frontmatter, de facon idempotente et re-jouable.

Usage : python3 scripts/link_graph_from_related.py
"""
import json
import os
import re
import sys

GRAPH = "graphify-out/graph.json"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parse_frontmatter(path):
    try:
        txt = open(path, encoding="utf-8").read()
    except OSError:
        return {"id": None, "related": []}
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", txt, re.S)
    if not m:
        return {"id": None, "related": []}
    fm = m.group(1)
    meta = {"id": None, "related": []}
    idm = re.search(r"^id:\s*(.+)$", fm, re.M)
    if idm:
        meta["id"] = idm.group(1).strip().strip('"').strip("'")
    rm = re.search(r"^related:\s*(.*)$", fm, re.M)
    if rm:
        val = rm.group(1).strip()
        if val.startswith("["):
            meta["related"] = re.findall(r'"([^"]+)"', val)
        elif val:
            meta["related"] = [v.strip().strip('"').strip("'") for v in val.split(",") if v.strip()]
    return meta


def main():
    gpath = os.path.join(ROOT, GRAPH)
    if not os.path.exists(gpath):
        print("graph.json absent:", gpath)
        sys.exit(1)
    g = json.load(open(gpath, encoding="utf-8"))
    nodes = g["nodes"]
    links = g["links"]

    # index : frontmatter id -> [graph node ids]
    id_to_nodes = {}
    file_to_node = {}
    metas = {}
    for n in nodes:
        sf = n.get("source_file")
        if not sf:
            continue
        file_to_node[sf] = n["id"]
        meta = parse_frontmatter(os.path.join(ROOT, sf))
        metas[sf] = meta
        if meta["id"]:
            id_to_nodes.setdefault(meta["id"], []).append(n["id"])

    def edge_exists(s, t):
        return any(l.get("source") == s and l.get("target") == t for l in links)

    added = 0
    for n in nodes:
        sf = n.get("source_file")
        if not sf or sf not in metas:
            continue
        for rel in metas[sf]["related"]:
            for tgt in id_to_nodes.get(rel, []):
                if tgt == n["id"]:
                    continue
                if edge_exists(n["id"], tgt):
                    continue
                links.append({
                    "source": n["id"],
                    "target": tgt,
                    "type": "related",
                    "derived_from": "frontmatter",
                })
                added += 1

    g["links"] = links
    json.dump(g, open(gpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Aretes 'related' ajoutees : {added} ; total liens : {len(links)}")


if __name__ == "__main__":
    main()
