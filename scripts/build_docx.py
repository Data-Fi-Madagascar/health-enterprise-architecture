#!/usr/bin/env python3
"""Build consolidated DOCX documents from the markdown documentation.

Reads scripts/manifest.json (reading order per level), merges each level's
docs into one markdown stream (stripping YAML frontmatter, 'Pour qui lire'
blocks, and horizontal rules), then renders with pandoc to DOCX:

  dist/<KEY>-v<VER>.docx   one per level (caesn, cnisn, artsn, ptisn)
  dist/HEA-v<VER>.docx     global document (all levels)

Usage:
  python scripts/build_docx.py [--version 1.0.0] [--date 2026-08-13]
                               [--toc-depth 2]
"""
import argparse
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n?", re.S)
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
# Strip "Pour qui lire ce document" blocks: ## heading + everything until next ## or #
# Handles variations: Niveau line, table, Légende line
POURQUI_RE = re.compile(
    r"##\s+Pour qui lire ce document.*?(?=\n## |\n# |\Z)",
    re.S | re.M
)
# Strip horizontal rules (---, ***, ___) used as section separators
HR_RE = re.compile(r"\n{2,}---\s*\n{2,}", re.M)


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def strip_pourqui(text: str) -> str:
    return POURQUI_RE.sub("\n", text)


def strip_separators(text: str) -> str:
    return HR_RE.sub("\n\n", text)


def rewrite_links(text: str) -> str:
    """Keep http(s)/mailto links clickable; degrade relative links to plain text."""
    def repl(m):
        label, target = m.group(1), m.group(2)
        if re.match(r"(https?://|mailto:)", target):
            return f"[{label}]({target})"
        return label or target
    return LINK_RE.sub(repl, text)


def merge_documents(file_list) -> str:
    parts = []
    for rel in file_list:
        src = ROOT / rel
        if not src.exists():
            sys.exit(f"ERREUR : fichier manquant : {rel}")
        content = src.read_text(encoding="utf-8")
        content = strip_frontmatter(content)
        content = strip_pourqui(content)
        content = strip_separators(content)
        content = rewrite_links(content)
        parts.append(content)
    return "\n\n".join(parts)


def render_docx(md_path: Path, docx_path: Path, toc_depth: int):
    cmd = [
        "pandoc", str(md_path), "-o", str(docx_path),
        "--toc", f"--toc-depth={toc_depth}",
        "-f", "markdown",
        "-t", "docx",
    ]
    print(f"  ▸ pandoc {md_path.name} → {docx_path.name}")
    res = subprocess.run(cmd, cwd=ROOT)
    if res.returncode != 0:
        sys.exit(f"Échec pandoc pour {md_path.name}")


def main():
    ap = argparse.ArgumentParser(description="Build consolidated DOCX documents")
    ap.add_argument("--out", default=str(ROOT / "dist"))
    ap.add_argument("--version", default="0.0.1")
    ap.add_argument("--date", default=date.today().isoformat())
    ap.add_argument("--toc-depth", type=int, default=2)
    args = ap.parse_args()

    version = os.environ.get("TAG_VERSION", "").lstrip("v") or args.version
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    manifest = json.loads((ROOT / "scripts" / "manifest.json").read_text(encoding="utf-8"))
    levels = manifest["levels"]

    level_docs = []
    for lv in levels:
        name, title, subtitle = lv["key"], lv["title"], lv["subtitle"]
        body = merge_documents(lv["list"])
        md_path = out / f"{name}-v{version}.md"
        md_path.write_text(
            f"# {title}\n\n*{subtitle}*\n\n*Version {version} — {args.date}*\n\n"
            + body,
            encoding="utf-8")
        print(f"[{name}] {title}")
        render_docx(md_path, out / f"{name}-v{version}.docx", args.toc_depth)
        md_path.unlink()
        level_docs.append((title, subtitle, body))

    # Document global
    part_blocks = []
    for idx, (title, subtitle, body) in enumerate(level_docs, start=1):
        part_blocks.append(f"\n\n# Niveau {idx} — {title}\n\n*{subtitle}*\n\n{body}")
    global_md = (
        f"# Architecture d'Entreprise de la Santé Numérique de Madagascar\n\n"
        f"*CAESN · CNISN · ARTSN · PTISN*\n\n"
        f"*Version {version} — {args.date}*\n\n"
        + "\n\n".join(part_blocks)
    )
    gmd = out / f"HEA-v{version}.md"
    gmd.write_text(global_md, encoding="utf-8")
    print("[hea] Architecture d'Entreprise de la Santé Numérique de Madagascar")
    render_docx(gmd, out / f"HEA-v{version}.docx", args.toc_depth)
    gmd.unlink()

    docx_files = list(out.glob("*.docx"))
    print(f"\nTerminé ✅  {len(docx_files)} DOCX dans {out}")


if __name__ == "__main__":
    main()
