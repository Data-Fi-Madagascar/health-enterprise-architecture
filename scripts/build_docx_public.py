#!/usr/bin/env python3
"""Build public DOCX documents for external readers (decision-makers, PTF).

Strips technical identifiers (CAP-*, CMP-*, ART-*), internal cross-references,
and governance documents. Keeps substantive prose from GENERATED blocks.

Output:
  dist/public/<KEY>-public-v<VER>.docx   one per level (caesn, cnisn, artsn)
  dist/public/HEA-public-v<VER>.docx     global document (all 3 levels)

Usage:
  python scripts/build_docx_public.py [--version 1.0.0] [--date 2026-08-20]
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

# ── Import existing functions from build_docx ──
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_docx import (
    FRONTMATTER_RE, LINK_RE, POURQUI_RE, HR_RE, PLANTUML_RE,
    strip_frontmatter, strip_pourqui, strip_separators,
    rewrite_links, render_plantuml_diagrams, render_docx
)

# ── Public-specific filters ──

# Technical identifiers: CAP-04, CMP-12, ART-4a, PT-01, STD-0001, PP-01, VS-01, PA-01, PRC-01, F.3, ENF-1
TECH_ID_RE = re.compile(
    r'\b(?:CAP|CMP|ART|PT|STD|PP|VS|PA|PRC)-\d+[a-z]?\b'
    r'|\b(?:CAP-INT|CAP)-\d+[a-z]?\b'
    r'|\bF\.\d+\b'
    r'|\bENF-\d+\b',
    re.I
)

# *Rattachement : CAP-03, CMP-01...* lines (italic, full line)
RATTACHEMENT_RE = re.compile(r'^\s*\*Rattachement\s*:.*\*\s*\n', re.M)

# ## Liens section (everything until next ## or #)
LIENS_RE = re.compile(
    r'##\s+Liens\s*\n.*?(?=\n##\s|\n#\s|\Z)',
    re.S | re.M
)

# *Répond à : ...* lines
REPOND_RE = re.compile(r'^\s*\*Répond à\s*:.*\*\s*\n', re.M)

# GENERATED block markers (HTML comments)
MARKER_RE = re.compile(
    r'^<!--\s*(?:BEGIN:GENERATED|END:GENERATED|Généré par).*-->\s*$',
    re.M
)

# Titles with codes: ### CMP-01 — Title → ### Title
TITRE_CODE_RE = re.compile(
    r'^(#{2,4})\s+(?:CMP|EV|CAP|PRC|ART|PT|VS|PA|F)-\d+[a-z]?\s*—\s*',
    re.M
)

# Isolated capability list lines: - CAP-01, - VS-01, - CMP-03 → remove entire line
CAP_LIST_RE = re.compile(r'^\s*-\s+(?:CAP|CMP|ART|PT|PP|VS|PA|PRC|STD)-\d+[a-z]?\s*\n', re.M)

# Empty bullet points left after ID removal: just "- " on a line
EMPTY_BULLET_RE = re.compile(r'^\s*-\s*$', re.M)

# Niveau/diagnostic lines referencing technical IDs
NIVEAU_RE = re.compile(
    r'^\s*\*Niveau\s*:.*(?:CAP|CMP|ART|PT|VS)-\d+.*\*\s*\n',
    re.M
)


def strip_technical_ids(text):
    """Remove technical identifiers from prose, keeping surrounding text."""
    return TECH_ID_RE.sub("", text)


def strip_rattachement(text):
    """Remove *Rattachement: ...* lines."""
    return RATTACHEMENT_RE.sub("", text)


def strip_internal_links(text):
    """Remove ## Liens section (keep ## Références)."""
    return LIENS_RE.sub("", text)


def strip_repond_a(text):
    """Remove *Répond à: ...* lines."""
    return REPOND_RE.sub("", text)


def strip_markers(text):
    """Remove GENERATED block markers."""
    return MARKER_RE.sub("", text)


def clean_titre_codes(text):
    """### CMP-01 — Title → ### Title."""
    return TITRE_CODE_RE.sub(r"\1 ", text)


def strip_cap_list(text):
    """Remove isolated - CAP-xx lines (entire line including newline)."""
    return CAP_LIST_RE.sub("", text)


def strip_empty_bullets(text):
    """Remove empty bullet points '- ' left after ID removal."""
    return EMPTY_BULLET_RE.sub("", text)


def strip_niveau_lines(text):
    """Remove *Niveau : CAP-xx...* diagnostic lines."""
    return NIVEAU_RE.sub("", text)


def clean_multiple_blanks(text):
    """Collapse 3+ consecutive blank lines into 2."""
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove empty section headings (## Title followed immediately by another heading)
    # Apply in loop since re.sub doesn't re-scan after replacements
    prev = None
    while prev != text:
        prev = text
        text = re.sub(r'(?:^|\n)(##\s+[^\n]+)\n+(?=(##\s|#{1,6}\s))', r'\n', text)
    return text


EM_DASH_RE = re.compile(r'\s*—\s*')


def replace_em_dashes(text):
    """Replace all em-dashes (—) with a colon separator."""
    return EM_DASH_RE.sub(' : ', text).strip()


def clean_for_public(text):
    """Full cleaning pipeline for public documents."""
    text = strip_frontmatter(text)
    text = strip_pourqui(text)
    text = strip_separators(text)
    text = strip_markers(text)
    text = clean_titre_codes(text)
    # Strip line-level patterns BEFORE inline IDs
    text = strip_cap_list(text)
    text = strip_rattachement(text)
    text = strip_niveau_lines(text)
    text = strip_internal_links(text)
    text = strip_repond_a(text)
    # Then strip remaining inline technical IDs
    text = strip_technical_ids(text)
    text = strip_empty_bullets(text)
    text = rewrite_links(text)
    text = replace_em_dashes(text)
    text = clean_multiple_blanks(text)
    return text


def merge_documents_public(file_list, img_dir):
    """Merge documents with public cleaning applied."""
    parts = []
    for rel in file_list:
        src = ROOT / rel
        if not src.exists():
            print(f"  ⚠ fichier manquant, ignoré : {rel}")
            continue
        content = src.read_text(encoding="utf-8")
        content = clean_for_public(content)
        if content.strip():
            parts.append(content)
    merged = "\n\n".join(parts)
    merged = render_plantuml_diagrams(merged, img_dir)
    return merged


def main():
    ap = argparse.ArgumentParser(description="Build public DOCX for external readers")
    ap.add_argument("--out", default=str(ROOT / "dist" / "public"))
    ap.add_argument("--version", default="0.0.1")
    ap.add_argument("--date", default=date.today().isoformat())
    ap.add_argument("--toc-depth", type=int, default=2)
    args = ap.parse_args()

    version = os.environ.get("TAG_VERSION", "").lstrip("v") or args.version
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    manifest_path = ROOT / "scripts" / "manifest-public.json"
    if not manifest_path.exists():
        sys.exit("ERREUR : scripts/manifest-public.json manquant")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    levels = manifest["levels"]

    level_docs = []
    img_dir = out / "diagrams"

    for lv in levels:
        name, title, subtitle = lv["key"], lv["title"], lv["subtitle"]
        body = merge_documents_public(lv["list"], img_dir / name)

        if not body.strip():
            print(f"  ⚠ [{name}] corps vide, ignoré")
            continue

        md_path = out / f"{name}-public-v{version}.md"
        md_path.write_text(
            f"# {title}\n\n*{subtitle}*\n\n*Version {version} — {args.date}*\n\n"
            + body,
            encoding="utf-8"
        )
        print(f"[{name}] {title}")
        render_docx(md_path, out / f"{name}-public-v{version}.docx", args.toc_depth, out)
        md_path.unlink()
        level_docs.append((name, title, subtitle, body))

    # Document global (3 levels only — no PTISN)
    if level_docs:
        part_blocks = []
        for idx, (name, title, subtitle, body) in enumerate(level_docs, start=1):
            part_blocks.append(f"\n\n# Niveau {idx} — {title}\n\n*{subtitle}*\n\n{body}")

        global_md = (
            f"# Architecture d'Entreprise de la Santé Numérique de Madagascar\n\n"
            f"*CAESN · CNISN · ARTSN*\n\n"
            f"*Version {version} — {args.date}*\n\n"
            + "\n\n".join(part_blocks)
        )
        gmd = out / f"HEA-public-v{version}.md"
        gmd.write_text(global_md, encoding="utf-8")
        print("[hea-public] Architecture d'Entreprise de la Santé Numérique de Madagascar")
        render_docx(gmd, out / f"HEA-public-v{version}.docx", args.toc_depth, out)
        gmd.unlink()

    docx_files = [f for f in out.glob("*.docx") if not f.name.startswith("~$")]
    print(f"\nTerminé ✅  {len(docx_files)} DOCX publics dans {out}")


if __name__ == "__main__":
    main()
