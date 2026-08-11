#!/usr/bin/env python3
"""Generate the Mintlify website as a derived artifact.

The 94 source .md documents (docs as code) are the single source of truth and
stay untouched: this script reads them + scripts/manifest.json and emits a
self-contained Mintlify site into mintlify-site/ (pages .mdx, docs.json,
homepage, static assets). The artifact is regenerated on every build and never
edited by hand — same philosophy as scripts/build_pdf.py -> dist/ .

Output layout mirrors the manifest:
  mintlify-site/index.mdx            landing page (Accueil HEA)
  mintlify-site/quickstart.mdx       parcours de lecture
  mintlify-site/docs.json            site + navigation (tabs per level)
  mintlify-site/favicon.svg, logo/…  static assets copied from the repo root
  mintlify-site/<level>/…            one .mdx per source document

Links are rewritten to root-relative Mintlify paths (/… without extension) so
the artifact has no broken internal links.

Usage:
  python scripts/build_mintlify.py [--out mintlify-site] [--repo OWNER/NAME]
                                   [--tag v0.1.1] [--check]

--check regenerates into a temp dir and fails with a diff listing if the
existing artifact is stale (used in CI to enforce idempotency).
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from difflib import unified_diff
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n?", re.S)
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
NUM_PREFIX_RE = re.compile(r"^\d+_")

# Human labels keyed by the source sub-directory (numeric-prefixed form).
GROUP_LABELS = {
    "00_overview": "Vue d'ensemble",
    "00_fondations": "Fondations",
    "01_flux-de-valeur": "Flux de valeur",
    "01_value-streams": "Flux de valeur",
    "02_exigences-contextuelles": "Exigences contextuelles",
    "02_principles": "Principes",
    "02_principles/domain": "Principes de domaine",
    "03_capabilities": "Capabilités",
    "03_chapitres": "Chapitres de référence",
    "04_cartographie-cible": "Cartographie cible",
    "04_data": "Données",
    "05_application": "Applications",
    "05_dictionnaire": "Dictionnaire de données",
    "06_gouvernance": "Gouvernance",
    "06_portfolio": "Portefeuille",
    "07_annexes": "Annexes",
    "07_governance": "Gouvernance",
    "08_decisions": "Décisions (ADR)",
    "09_standards": "Normes & standards",
    "10_annexes": "Annexes",
}

# Short sidebar labels for coded titles (VS-xx, ART-x, ADR-x, STD-x, …).
SIDEBAR_CODE_RE = re.compile(
    r"^\s*(VS-\d+|ART-\d+[a-z]?|ART\s*\d+[a-z]?|PD-VS\d+|ADR-\d+|STD-\d+)\b")

DEFAULT_REPO = "Data-Fi-Madagascar/health-enterprise-architecture"
DEFAULT_REPO_URL = f"https://github.com/{DEFAULT_REPO}"


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def artifact_relpath(src_rel: str) -> str:
    """Transform a source path (0x_level/…/file.md) into an artifact path."""
    parts = PurePosixPath(src_rel).parts
    level = parts[0][3:]  # e.g. 00_caesn -> caesn
    if len(parts) == 1:
        return level
    tail = [NUM_PREFIX_RE.sub("", p) for p in parts[1:]]
    return "/".join([level] + tail)


def url_for(src_rel: str) -> str:
    """Mintlify root-relative URL (/path, no extension) for a source doc."""
    return "/" + artifact_relpath(src_rel)[: -len(".md")]


def build_url_map(manifest):
    """path source (canonical) -> URL Mintlify racine."""
    return {rel: url_for(rel) for lvl in manifest["levels"] for rel in lvl["list"]}


def parse_source(src_rel: str):
    """Return (title, meta) for a source document."""
    text = (ROOT / src_rel).read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    title, meta = None, {}
    if not m:
        return None, {}
    fm = m.group(0)
    for line in fm.splitlines():
        line = line.strip()
        if not line or line in ("---",):
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip().strip('"')
        if key == "title":
            title = val
        meta[key] = val
    return title, meta


def body_without_frontmatter(src_rel: str) -> str:
    text = (ROOT / src_rel).read_text(encoding="utf-8")
    return FRONTMATTER_RE.sub("", text, count=1)


def strip_leading_h1(text: str) -> str:
    """Remove the leading H1 (title) — frontmatter `title` already renders it."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == "":
            continue
        if line.strip().startswith("# "):
            del lines[i]
        break
    return "\n".join(lines).lstrip("\n")


def rewrite_links(text: str, src_rel: str, url_map: dict) -> str:
    """Rewrite relative intra-doc links to root-relative Mintlify URLs."""
    base = PurePosixPath(src_rel).parent

    def repl(m):
        label, target = m.group(1), m.group(2)
        if re.match(r"(https?://|mailto:)", target):
            return m.group(0)
        if target.startswith("/"):
            return m.group(0)
        if target.startswith("#"):
            return m.group(0)
        # Strip anchor before resolution, reapply after.
        anchor = ""
        if "#" in target:
            target, anchor = target.split("#", 1)
            anchor = "#" + anchor
        if target.endswith("/"):
            target = target + "index.md"
        if not target:
            return label or ""
        if PurePosixPath(target).suffix not in (".md", ".mdx"):
            # Extension-less or directory link.
            trial = os.path.normpath(os.path.join(str(base), target))
            if not trial.endswith(".md"):
                trial = trial + ".md"
        else:
            trial = os.path.normpath(os.path.join(str(base), target))
        trial = trial.replace(os.sep, "/")
        url = url_map.get(trial)
        if url is None:
            return label or ""  # degrade instead of leaving a broken link
        return f"[{label}]({url}{anchor})"

    return LINK_RE.sub(repl, text)


def sidebar_title_for(title: str):
    m = SIDEBAR_CODE_RE.match(title)
    return m.group(1).strip() if m else None


def render_page(dest: Path, src_rel: str, url_map: dict, subtitle: str):
    title, meta = parse_source(src_rel)
    title = title or PurePosixPath(src_rel).stem
    body = rewrite_links(body_without_frontmatter(src_rel), src_rel, url_map)
    lines = ["---",
             f"title: {json.dumps(title, ensure_ascii=False)}"]
    sb = sidebar_title_for(title)
    if sb:
        lines.append(f"sidebarTitle: {json.dumps(sb, ensure_ascii=False)}")
    lines.append(f"description: {json.dumps(subtitle, ensure_ascii=False)}")
    for key in ("owner", "version", "status", "last_reviewed"):
        if key in meta:
            lines.append(f"{key}: {json.dumps(meta[key], ensure_ascii=False)}")
    lines.append("---")
    lines.append("")
    lines.append(strip_leading_h1(body))
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------
# Navigation
# --------------------------------------------------------------------------

def group_label(apath_dir: str) -> str:
    label = GROUP_LABELS.get(apath_dir)
    if label:
        return label
    return NUM_PREFIX_RE.sub("", apath_dir).replace("-", " ").capitalize()


def build_tabs(manifest, url_map):
    """Generate per-level tab payloads (groups + root pages)."""
    tabs = []
    for lvl in manifest["levels"]:
        # Group pages by artifact parent dir, preserving reading order.
        groups = {}
        order = []
        for rel in lvl["list"]:
            ap = artifact_relpath(rel)
            parent = str(PurePosixPath(ap).parent)
            if parent in (".", PurePosixPath(".").as_posix(), ""):
                parent = ""
            if parent not in groups:
                groups[parent] = []
                order.append(parent)
            groups[parent].append(rel)

        pages = []
        for dirkey in order:
            rels = groups[dirkey]
            urls = [url_for(r) for r in rels]
            if dirkey == "":
                pages.extend(urls)  # level-intro files (index, matrices, …)
                continue
            root = None
            for r, u in zip(rels, urls):
                if NUM_PREFIX_RE.sub("", PurePosixPath(r).name) == "index.md":
                    root = u
                    urls.remove(u)
                    break
            item = {"group": group_label(dirkey), "pages": urls}
            if root:
                item["root"] = root
            pages.append(item)

        tabs.append({"pages": pages})
    return tabs


# --------------------------------------------------------------------------
# Homepage / quickstart / config (pure content, no Mintlify-specific hacks)
# --------------------------------------------------------------------------

def latest_release_tag():
    try:
        tag = subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"],
                                      cwd=ROOT, stderr=subprocess.DEVNULL).decode().strip()
        return tag if tag.startswith("v") else f"v{tag}"
    except Exception:
        return None


def build_home(repo_url, tag):
    level_cards = """<Cards>
  <Card title="CAESN — Niveau 1" icon="landmark" href="/caesn/overview">
    Cadre d'Architecture d'Entreprise de la Santé Numérique.
  </Card>
  <Card title="CNISN — Niveau 2" icon="handshake" href="/cnisn">
    Cadre National d'Interopérabilité de la Santé Numérique.
  </Card>
  <Card title="ARTSN — Niveau 3" icon="network" href="/artsn">
    Architecture de Référence Technique de la Santé Numérique.
  </Card>
  <Card title="PTISN — Niveau 4" icon="terminal" href="/ptisn">
    Profils techniques d'implémentation de la Santé Numérique.
  </Card>
</Cards>"""
    if tag:
        ver = tag[1:]
        lines = [f"- [**HEA — document complet**]({repo_url}/releases/download/{tag}/HEA-{ver}.pdf)"]
        for key, label in (("caesn", "CAESN (niveau 1)"), ("cnisn", "CNISN (niveau 2)"),
                           ("artsn", "ARTSN (niveau 3)"), ("ptisn", "PTISN (niveau 4)")):
            lines.append(f"- [{label}]({repo_url}/releases/download/{tag}/{key}-{ver}.pdf)")
        pdfs = "\n".join(lines)
    else:
        pdfs = f"-> **Télécharger les PDF de la dernière release :** [{repo_url}/releases/latest]({repo_url}/releases/latest)"
    return f"""---
title: "Santé numérique de Madagascar — Architecture d'entreprise"
description: "CAESN · CNISN · ARTSN · PTISN — 4 niveaux d'architecture, documentation as code"
mode: "wide"
---

# Architecture d'entreprise de la santé numérique de Madagascar

Ce portail rassemble les 4 niveaux d'architecture de la santé numérique à Madagascar,
rédigés en documentation as code et versionnés. Les documents sources restent
édités dans le référentiel Git — ce site est généré automatiquement à chaque publication.

{level_cards}

## Téléchargements (PDF de la dernière release)

{pdfs}

## Parcours de lecture

Un [parcours de lecture](/quickstart) guide votre entrée selon votre profil :
décideurs, directions métier, équipes techniques, partenaires.
"""


def build_quickstart():
    return """---
title: "Parcours de lecture"
description: "Comment naviguer dans les 4 niveaux d'architecture de la santé numérique"
---

# Parcours de lecture

## Qui lit quoi ?

| Profil | Lecture prioritaire |
|--------|---------------------|
| Décideurs institutionnels | [Niveau 1 — CAESN](/caesn/overview) |
| Directions métier / programmes | [Niveau 1](/caesn/overview), [Niveau 2](/cnisn) |
| DEPSI / équipes techniques | [Niveau 2](/cnisn), [Niveau 3](/artsn), [Niveau 4](/ptisn) |
| SIS / données / suivi-évaluation | [Niveau 1](/caesn/overview), [Niveau 3](/artsn) |
| Partenaires techniques et financiers | [Niveau 1](/caesn/overview) |

## Matrices de lecture par niveau

- [CAESN — matrice de lecture](/caesn/reading-matrix)
- [CNISN — matrice de lecture](/cnisn/reading-matrix)
- [ARTSN — matrice de lecture](/artsn/reading-matrix)
- [PTISN — matrice de lecture](/ptisn/reading-matrix)
"""


def build_docs_json(tabs, repo_url):
    return {
        "$schema": "https://mintlify.com/docs.json",
        "theme": "mint",
        "name": "Santé numérique de Madagascar — Architecture d'entreprise",
        "colors": {"primary": "#0E7490", "light": "#06B6D4", "dark": "#155E75"},
        "favicon": "/favicon.svg",
        "navigation": {
            "tabs": [
                {"tab": "CAESN", "icon": "landmark", **tabs[0]},
                {"tab": "CNISN", "icon": "handshake", **tabs[1]},
                {"tab": "ARTSN", "icon": "network", **tabs[2]},
                {"tab": "PTISN", "icon": "terminal", **tabs[3]},
            ],
            "global": {
                "anchors": [
                    {"anchor": "Accueil", "icon": "house", "href": "/index"},
                    {"anchor": "Téléchargements", "icon": "download",
                     "href": f"{repo_url}/releases"},
                ]
            },
        },
        "logo": {"light": "/logo/light.svg", "dark": "/logo/dark.svg"},
        "navbar": {
            "links": [{"label": "GitHub", "href": repo_url}],
        },
        "contextual": {"options": ["copy", "view", "chatgpt", "claude",
                                   "perplexity", "mcp", "cursor", "vscode"]},
        "metadata": {"timestamp": True},
    }


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------

def generate(out: Path, args) -> int:
    manifest = json.loads((ROOT / "scripts" / "manifest.json").read_text(encoding="utf-8"))
    url_map = build_url_map(manifest)
    tabs = build_tabs(manifest, url_map)
    repo_url = args.repo if args.repo else DEFAULT_REPO_URL
    tag = args.tag if args.tag else latest_release_tag()

    if args.check:
        target = Path(tempfile.mkdtemp(prefix="mintlify-check-"))
    else:
        target = out
        if out.exists():
            shutil.rmtree(out)
        out.mkdir(parents=True, exist_ok=True)

    for lvl in manifest["levels"]:
        for rel in lvl["list"]:
            ap = artifact_relpath(rel)
            if ap.endswith(".md"):
                ap = ap[: -3] + ".mdx"
            render_page(target / ap, rel, url_map, lvl["subtitle"])

    (target / "index.mdx").write_text(build_home(repo_url, tag), encoding="utf-8")
    (target / "quickstart.mdx").write_text(build_quickstart(), encoding="utf-8")
    (target / "docs.json").write_text(
        json.dumps(build_docs_json(tabs, repo_url), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")

    # Static assets from the repo root.
    for fn in ("favicon.svg",):
        src = ROOT / fn
        if src.exists():
            shutil.copy2(src, target / fn)
    logo = ROOT / "logo"
    if logo.exists():
        shutil.copytree(logo, target / "logo", dirs_exist_ok=True)

    if args.check:
        diffs = []
        for p in sorted(target.rglob("*")):
            if not p.is_file():
                continue
            relp = p.relative_to(target)
            q = out / relp
            if not q.exists():
                diffs.append(f"  + {relp}")
            elif q.read_bytes() != p.read_bytes():
                diffs.append(f"  M {relp}")
        shutil.rmtree(target, ignore_errors=True)
        if diffs:
            print("Artefact Mintlify obsolète — différences :")
            for d in diffs:
                print(d)
            return 1
        print("Artefact Mintlify à jour ✅")
        return 0

    print(f"Terminé ✅  artefact Mintlify généré dans {out}")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Build the Mintlify artifact")
    ap.add_argument("--out", default=str(ROOT / "mintlify-site"))
    ap.add_argument("--repo", default=None,
                    help="repo GitHub 'owner/name' (défaut: %(default)s)")
    ap.add_argument("--tag", default=None,
                    help="tag de release pour liens PDF (défaut: détection git)")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if args.repo and not args.repo.startswith("http"):
        args.repo = f"https://github.com/{args.repo}"
    rc = generate(Path(args.out), args)
    sys.exit(rc)


if __name__ == "__main__":
    main()