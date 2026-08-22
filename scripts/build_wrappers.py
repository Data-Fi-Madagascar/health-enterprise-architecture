#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Transclut les 150 objets du référentiel dans leurs 51 enveloppes.

Conventions (spec docs/superpowers/specs/2026-08-11-enveloppes-lisibilite-design.md) :

- Un bloc généré est délimité par :
      <!-- BEGIN:GENERATED [mode=table] source=referentiel/<type>/<pat>.md[,<pat2>.md] -->
      <!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->
      <contenu généré>
      <!-- END:GENERATED -->
- Sans `mode=table`, c'est une transclusion du corps complet :
    - monographie : 1 objet attaché (`envelope:` == chemin de l'enveloppe), H1 supprimé, `##` conservés ;
    - catalogue    : N objets attachés, H1 -> ### et hiérarchie → #### maximale ;
    chaque objet reçoit la ligne *Rattachement : … · [fiche](…)*.
    Le mode est déduit du nombre d'objets attachés à l'enveloppe, sauf si `mode=` est
    précisé explicitement sur le bloc (ex. enveloppe mixte : `mode=monographie` + `mode=catalogue`).
- Avec `mode=table`, un tableau `code | titre canonique | rattachement | statut | fiche`
  des objets qui matchent les motifs (réservé aux fichiers d'index et de matrices).
- Le filtre `source=` s'applique aux objets attachés à l'enveloppe (D3 : champ `envelope:`),
  sauf en `mode=table` où il sélectionne dans tout le référentiel.
- Vérifications : union des blocs couvre tous les objets attachés ; `envelope:` inexistant
  → erreur ; enveloppe sans marqueurs → erreur.

Usage :
    python scripts/build_wrappers.py               # écrit les 51 enveloppes
    python scripts/build_wrappers.py --check       # exit 1 + diff si dérive, n'écrit rien
    python scripts/build_wrappers.py --only 00_caesn/02_principles/transversal.md
"""

import fnmatch
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFERENTIEL = os.path.join(REPO_ROOT, "referentiel")

BANNER = "<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->"
BEGIN_RE = re.compile(r"^<!--\s*BEGIN:GENERATED\s*(.*?)\s*-->$")
END_RE = re.compile(r"^<!--\s*END:GENERATED\s*-->$")
ATTRIB = re.compile(r"(mode|source)=(?:(\"[^\"]*\")|([^\s]+))")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]*)\)")
FACE = ["candidate", "deprecated"]

NATURAL_RE = re.compile(r"(\d+)")


def natural_key(value):
    return [int(part) if part.isdigit() else part
            for part in NATURAL_RE.split(value)]


class FrontmatterError(Exception):
    pass


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        raise FrontmatterError("frontmatter YAML manquant")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise FrontmatterError("frontmatter YAML non fermé")
    yaml_block = text[4:end]
    fields = {}
    for line in yaml_block.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped == "---":
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", stripped)
        if not m:
            raise FrontmatterError("champ non analysable : %r" % line)
        key, value = m.group(1), m.group(2).strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            items = [item.strip().strip('"').strip("'")
                     for item in inner.split(",") if item.strip()]
            fields[key] = items
        elif not value:
            fields[key] = []
        else:
            fields[key] = value.strip('"').strip("'")
    return end + 4, fields


def load_objects():
    objects = {}
    for dirpath, _dirs, files in os.walk(REFERENTIEL):
        for name in files:
            if not name.endswith(".md") or name == "_schema.md":
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, REPO_ROOT)
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            try:
                end, fields = parse_frontmatter(text)
            except FrontmatterError as exc:
                raise SystemExit("frontmatter invalide %s : %s" % (rel, exc))
            body = text[end:].lstrip("\n")
            body_end = body.find("\n\n## Liens")
            if body_end != -1:
                body = body[:body_end].rstrip()
            objects[rel] = {
                "rel": rel,
                "id": fields.get("id", ""),
                "title": fields.get("title", ""),
                "status": fields.get("status", ""),
                "envelope": fields.get("envelope", ""),
                "maps_to": fields.get("maps_to", []) or [],
                "implements": fields.get("implements", []) or [],
                "applies_to": fields.get("applies_to", []) or [],
                "uses": fields.get("uses", []) or [],
                "body": body,
            }
    return objects


def id_to_path(objects):
    mapping = {}
    for obj in objects.values():
        mapping[obj["id"]] = obj["rel"]
    return mapping


def rewrite_links(text, from_dir, to_dir):
    """Rewrite resolvable relative links so they point to the correct file from
    the generated document's location, keeping every reference clickable.

    - A relative link whose target resolves to an existing file is rewritten to
      the path relative to the target doc (so cross-references stay live).
    - Links that do not resolve, plus external URLs, anchors and absolute paths,
      are preserved as-is (label kept).
    """
    def repl(match):
        label = match.group(1)
        target = match.group(2).strip()
        if not target or "://" in target or target.startswith("#"):
            return match.group(0)
        if target.startswith("/") or target.startswith("mailto:"):
            return match.group(0)
        src = os.path.normpath(os.path.join(from_dir, target))
        if os.path.isfile(src):
            new_target = os.path.relpath(src, to_dir).replace(os.sep, "/")
            return "[%s](%s)" % (label, new_target)
        return label

    return LINK_RE.sub(repl, text)


def demote_headings(text):
    """# -> ###, ## -> ####, et tout heading plus profond plafonné à ####."""
    lines = []
    for line in text.splitlines(keepends=True):
        m = HEADING_RE.match(line)
        if m:
            level = min(len(m.group(1)) + 2, 4)
            lines.append("#" * level + " " + m.group(2) + "\n")
        else:
            lines.append(line)
    return "".join(lines)


def rattachement_links(obj, path_by_id, to_dir):
    ids = []
    seen = set()
    for key in ("applies_to", "maps_to", "implements", "uses"):
        for oid in obj[key]:
            if oid and oid not in seen:
                seen.add(oid)
                ids.append(oid)
    labels = []
    for oid in ids:
        if oid:
            labels.append(oid.upper())
    return labels


def badge_for(obj):
    """Badge de statut : uniquement candidate/deprecated (décision utilisateur)."""
    if obj["status"] in FACE:
        return "**Statut : %s**" % obj["status"]
    return None


def render_transclusion(obj, mode, path_by_id):
    body = obj["body"]
    to_dir = os.path.dirname(os.path.join(REPO_ROOT, obj["envelope"]))
    from_dir = os.path.dirname(os.path.join(REPO_ROOT, obj["rel"]))
    body = rewrite_links(body, from_dir, to_dir)

    if mode == "monographie":
        lines = body.splitlines(keepends=True)
        if lines and lines[0].startswith("# "):
            lines = lines[1:]
        body = "".join(lines).lstrip("\n")
        badge = badge_for(obj)
        parts = []
        if badge:
            parts.append(badge)
        if body.strip():
            parts.append(body.rstrip("\n"))
        return "\n\n".join(parts)
    else:
        body = demote_headings(body)
        parts = []
        badge = badge_for(obj)
        if badge:
            parts.append(badge)
        if body.strip():
            parts.append(body.rstrip("\n"))
        return "\n\n".join(parts).replace("\n\n\n", "\n\n")


def render_table(objects, source_glob, path_by_id, to_dir):
    selected = []
    for rel, obj in objects.items():
        if any(fnmatch.fnmatch(rel, pattern) for pattern in source_glob):
            selected.append(obj)
    selected.sort(key=lambda o: natural_key(o["id"]))

    code_map = {o["id"]: o for o in selected}
    lines = ["| Code | Titre canonique | Rattachement | Statut | Fiche |",
             "|---|---|---|---|---|"]
    for obj in selected:
        code = obj["id"].upper()
        titre = re.sub(r"^[A-Za-z0-9.\- ]+ —\s*", "", obj["title"]) or obj["title"]
        rattachements = rattachement_links(obj, path_by_id, to_dir)
        rattachement = ", ".join(rattachements) if rattachements else "—"
        statut = obj["status"]
        lines.append("| %s | %s | %s | %s | %s |"
                     % (code, titre.replace("|", "\\|"), rattachement.replace("|", "\\|"),
                        statut, code))
    return "\n".join(lines)


def parse_attributes(attr_text):
    attrs = {"mode": None, "source": []}
    for match in ATTRIB.finditer(attr_text):
        key, quoted, bare = match.group(1), match.group(2), match.group(3)
        value = (quoted[1:-1] if quoted else bare).strip()
        if key == "mode":
            attrs["mode"] = value
        elif key == "source":
            attrs["source"] = [p.strip() for p in value.split(",") if p.strip()]
    return attrs


def find_blocks(text):
    """Retourne [(start_begin, end_begin, start_end, attrs)]. start_end = début de `<!-- END:GENERATED -->`."""
    blocks = []
    lines = text.splitlines(keepends=True)
    begin_index = None
    for idx, line in enumerate(lines):
        bm = BEGIN_RE.match(line.strip())
        em = END_RE.match(line.strip())
        if bm:
            begin_index = idx
            attrs = parse_attributes(bm.group(1))
        elif em and begin_index is not None:
            start_begin = sum(len(l) for l in lines[:begin_index])
            len_begin = len(lines[begin_index])
            start_end = sum(len(l) for l in lines[:idx])
            end_len = len(lines[idx])
            blocks.append((start_begin, start_begin + len_begin, start_end, start_end + end_len,
                           attrs))
            begin_index = None
    if begin_index is not None:
        raise SystemExit("marqueur BEGIN:GENERATED non fermé dans le fichier")
    return blocks


def attached_objects(objects, envelope):
    return [obj for obj in objects.values() if obj["envelope"] == envelope]


def generate_file(objects, path_by_id, rel):
    abs_path = os.path.join(REPO_ROOT, rel)
    with open(abs_path, encoding="utf-8") as fh:
        original = fh.read()

    blocks = find_blocks(original)
    if not blocks:
        raise SystemExit("enveloppe sans marqueurs %s : annoter le fichier" % rel)

    attached = attached_objects(objects, rel)
    pending = [obj["rel"] for obj in attached]

    output = []
    cursor = 0
    for start_begin, end_begin, start_end, end_end, attrs in blocks:
        output.append(original[cursor:start_begin])
        globs = attrs["source"]

        if attrs["mode"] == "table":
            selected = [obj for rel_obj, obj in objects.items()
                        if any(fnmatch.fnmatch(rel_obj, g) for g in globs)]
            selected.sort(key=lambda o: natural_key(o["id"]))
            if not selected:
                raise SystemExit("bloc tableau vide (%s) dans %s" % (", ".join(globs), rel))
            to_dir = os.path.dirname(abs_path)
            content = render_table(objects, globs, path_by_id, to_dir)
            body = content
        else:
            covered = []
            for obj in attached:
                if globs and not any(fnmatch.fnmatch(obj["rel"], g) for g in globs):
                    continue
                covered.append(obj["rel"])
            covered.sort(key=lambda r: natural_key(os.path.basename(r).split(".")[0]))
            for obj_rel in covered:
                if obj_rel in pending:
                    pending.remove(obj_rel)
            if not covered:
                raise SystemExit("bloc de transclusion vide (%s) dans %s" % (", ".join(globs), rel))

            mode = attrs["mode"] or ("monographie" if len(attached) == 1 else "catalogue")
            bodies = [render_transclusion(objects[obj_rel], mode, path_by_id)
                      for obj_rel in covered]
            body = "\n\n".join(bodies)

        block_text = "<!-- BEGIN:GENERATED%s -->\n%s" % (
            " " + attrs_text(attrs) if attrs_text(attrs) else "", BANNER)
        block_text += "\n\n" + body + "\n\n"
        block_text += "<!-- END:GENERATED -->\n"
        output.append(block_text)
        cursor = end_end
    output.append(original[cursor:])

    if pending:
        raise SystemExit("objets non couverts par la union des blocs de %s : %s"
                         % (rel, ", ".join(sorted(pending))))

    return "".join(output)


def attrs_text(attrs):
    parts = []
    if attrs["mode"]:
        parts.append("mode=%s" % attrs["mode"])
    if attrs["source"]:
        parts.append("source=%s" % ",".join(attrs["source"]))
    return " ".join(parts)


def main():
    check = "--check" in sys.argv
    only = None
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1]

    objects = load_objects()
    path_by_id = id_to_path(objects)

    sources = {obj["envelope"] for obj in objects.values()}
    for source in sorted(sources):
        if not os.path.exists(os.path.join(REPO_ROOT, source)):
            raise SystemExit("objet avec envelope: inexistante -> %s" % source)

    targets = set(sources)
    for rel in list(targets) + ["03_ptisn/03_profils/pt-00-index.md",
                                "01_cnisn/08_annexes/a-matrice-principes-capacites.md"]:
        path = os.path.join(REPO_ROOT, rel)
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                if "BEGIN:GENERATED" not in fh.read():
                    raise SystemExit("enveloppe sans marqueurs %s : annoter le fichier" % rel)
        targets.add(rel)

    if only:
        if only not in targets:
            raise SystemExit("fichier hors périmètre : %s" % only)
        ordered = [only]
    else:
        tables = ("03_ptisn/03_profils/pt-00-index.md",
                  "01_cnisn/08_annexes/a-matrice-principes-capacites.md")
        # les tableaux purs sont régénérés en dernier (prédictibilité des diffs)
        ordered = sorted(t for t in targets if t not in tables) + \
            sorted(t for t in targets if t in tables)

    drifted = 0
    for rel in ordered:
        generated = generate_file(objects, path_by_id, rel)
        abs_path = os.path.join(REPO_ROOT, rel)
        with open(abs_path, encoding="utf-8") as fh:
            current = fh.read()
        if check:
            if generated != current:
                drifted += 1
                import difflib
                diff = "\n".join(difflib.unified_diff(
                    current.splitlines(), generated.splitlines(),
                    fromfile=rel, tofile=rel + " (généré)", lineterm=""))
                sys.stderr.write("%s\n%s\n" % (rel, diff))
        else:
            with open(abs_path, "w", encoding="utf-8") as fh:
                fh.write(generated)
            print("régénéré  %s" % rel)

    if check:
        if drifted:
            sys.stderr.write("%d enveloppe(s) dérivée(s)\n" % drifted)
            sys.exit(1)
        print("OK : %d enveloppes à jour" % len(ordered))
    else:
        print("%d enveloppes écrites" % len(ordered))


if __name__ == "__main__":
    main()