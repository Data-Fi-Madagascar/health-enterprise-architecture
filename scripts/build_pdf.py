#!/usr/bin/env python3
"""Build 5 consolidated PDFs from the markdown documentation.

Reads scripts/manifest.json (reading order per level), merges each level's
docs into one markdown stream (stripping YAML frontmatter, rewriting relative
links), then renders with pandoc + a LaTeX engine:

  dist/<KEY>-v<VER>.pdf   one per level (caesn, cnisn, artsn, ptisn)
  dist/HEA-v<VER>.pdf     global document (all levels, one part each)

Usage:
  python scripts/build_pdf.py [--version 0.0.1] [--date 2026-08-09]
                              [--engine xelatex] [--font "DejaVu Sans"]
                              [--toc-depth 2] [--keep]

Env: TAG_VERSION overrides --version (set by the release workflow).
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


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def rewrite_links(text: str) -> str:
    """Keep http(s)/mailto links clickable; degrade relative/anchor links to
    plain text (they are meaningless in a merged single-file PDF)."""
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
            sys.exit(f"ERREUR : fichier manquant dans le manifeste : {rel}")
        parts.append(rewrite_links(strip_frontmatter(src.read_text(encoding="utf-8"))))
    return "\n\n---\n\n".join(parts)


def render(md_path: Path, pdf_path: Path, engine: str, font: str, toc_depth: int,
           version: str):
    header = ROOT / "templates" / "latex-header.tex"
    version_header = Path(pdf_path.parent) / "_version_header.tex"
    version_header.write_text(
        f"\\newcommand{{\\editionversion}}{{{version}}}\n",
        encoding="utf-8")
    cmd = [
        "pandoc", str(md_path), "-o", str(pdf_path), "--pdf-engine=" + engine,
        "-V", f"mainfont={font}", "-V", "fontsize=11pt",
        "-V", "geometry:margin=2.5cm", "-V", "colorlinks=true",
        "-V", "monofont=DejaVu Sans Mono",
        "--toc", f"--toc-depth={toc_depth}",
        "-H", str(header), "-H", str(version_header),
    ]
    print("  ▸ pandoc", md_path.name, "→", pdf_path.name)
    res = subprocess.run(cmd, cwd=ROOT)
    version_header.unlink(missing_ok=True)
    if res.returncode != 0:
        sys.exit(f"Échec pandoc pour {md_path.name}")


def main():
    ap = argparse.ArgumentParser(description="Build consolidated PDFs")
    ap.add_argument("--out", default=str(ROOT / "dist"))
    ap.add_argument("--version", default="0.0.1")
    ap.add_argument("--date", default=date.today().isoformat())
    ap.add_argument("--engine", default="xelatex")
    ap.add_argument("--font", default="DejaVu Sans")
    ap.add_argument("--toc-depth", type=int, default=2)
    ap.add_argument("--keep", action="store_true", help="conserver les .md intermédiaires")
    args = ap.parse_args()

    version = os.environ.get("TAG_VERSION", "").lstrip("v") or args.version
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    manifest = json.loads((ROOT / "scripts" / "manifest.json").read_text(encoding="utf-8"))
    levels = manifest["levels"]

    level_docs = []  # (titre niveau, corps md)
    for lv in levels:
        name, title, subtitle = lv["key"], lv["title"], lv["subtitle"]
        body = merge_documents(lv["list"])
        md_path = out / f"{name}-v{version}.md"
        md_path.write_text(
            f"---\ntitle: \"{title}\"\nsubtitle: \"{subtitle}\"\n"
            f"version: {version}\ndate: {args.date}\nlang: fr\n---\n\n{body}",
            encoding="utf-8")
        print(f"[{name}] {title}")
        render(md_path, out / f"{name}-v{version}.pdf",
               args.engine, args.font, args.toc_depth, version)
        if not args.keep:
            md_path.unlink()
        level_docs.append((title, body))

    # Document global : une « partie » par niveau, préfixée d'un H1.
    part_blocks = []
    for idx, (title, body) in enumerate(level_docs, start=1):
        part_blocks.append(f"\n# Niveau {idx} — {title}\n\n{body}")
    global_md = (
        "---\ntitle: \"Architecture d'Entreprise de la Santé Numérique de Madagascar\"\n"
        "subtitle: \"CAESN · CNISN · ARTSN · PTISN — documentation as code\"\n"
        f"version: {version}\ndate: {args.date}\nlang: fr\n---\n\n"
        + "\n\n\\newpage\n\n".join(part_blocks)
    )
    gmd = out / f"HEA-v{version}.md"
    gmd.write_text(global_md, encoding="utf-8")
    print("[hea] Architecture d'Entreprise de la Santé Numérique de Madagascar")
    render(gmd, out / f"HEA-v{version}.pdf", args.engine, args.font, args.toc_depth,
           version)
    if not args.keep:
        gmd.unlink()

    print(f"\nTerminé ✅  {len(list(out.glob('*.pdf')))} PDF dans {out}")


if __name__ == "__main__":
    main()