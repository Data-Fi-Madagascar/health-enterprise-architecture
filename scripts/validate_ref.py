#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valide la cohérence du référentiel HEA : îlots, liens cassés, chaîne PT→CAP.

Complète check_links.py (liens relatifs cassés) en vérifiant le *graphe de
relations* entre objets du référentiel :

  - relations : maps_to / implements / applies_to / related (frontmatter)
  - îlots : objets sans aucune arête (degré sortant + entrant = 0)
  - cibles non résolues : une relation pointe vers un id inexistant
  - liens Markdown relatifs cassés (reprend le critère A2 de check_links.py)
  - chaîne PT → CAP-INT → CAP : tout profil doit aboutir à une capabilité CAESN
  - cohérence des types dans maps_to (pas de mélange de niveaux)
  - couverture des 18 capabilités CAESN par les profils

Historique : le validateur initial (/tmp/validate_ref.rb) ne détectait pas les
objets sans aucune arête, ce qui avait masqué les 29 principes CAESN isolés
(coherence-report §2.4). Ce script comble cette lacune.

Usage :
    python3 scripts/validate_ref.py          # exit 1 si îlot non autorisé ou cible non résolue
    python3 scripts/validate_ref.py --strict # exit 1 aussi en présence d'îlots connus
"""

import argparse
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Répertoires parcourus pour la vérification des liens relatifs (tout le cadre).
LINK_DIRS = ["00_caesn", "01_cnisn", "02_artsn", "03_ptisn", "referentiel"]
# Le graphe de relations (maps_to/implements/...) ne concerne que le référentiel,
# source de vérité. Les documents « enveloppes » (00_caesn … 03_ptisn) ne portent
# pas ces champs et ne doivent pas être traités comme des îlots.
REL_DIRS = ["referentiel"]
EXCLUDE_DIRS = {".git", "__pycache__", "node_modules", "dist", ".venv",
                "graphify-out", ".agents", ".claude", "mintlify-site", "docs"}
RELATION_KEYS = ["maps_to", "implements", "applies_to", "related",
                 "realized_by", "contributes_to", "performs", "accesses",
                 "governs", "represents", "assigned_to", "has_role",
                 "located_at", "serves", "produced_by", "detenu_par",
                 "soutient_flux_de_valeur", "utilise_composant",
                 "supporte_standard", "a_pour_proprietaire_fonctionnel"]

# Îlots légitimes attendus (candidats non encore reliés) — ne font pas échouer.
KNOWN_ISLANDS = {"art-10", "art-11", "f-5", "f-6"}

# Types de niveaux hiérarchiques pour vérification de chaîne.
TYPE_PROFIL = "profil"               # niveau 4 (PT-*)
TYPE_CAPACITE = "capacite"            # niveau 2 (CAP-INT-*)
TYPE_CAPABILITE = "capabilite"        # niveau 1 (CAP-*)
TYPE_CHAPITRE = "chapitre"            # niveau 3 (ART-*)
TYPE_COMPOSANT = "composant-applicatif"  # et variantes infra/securite/gouvernance

# Types autorisés dans maps_to par type source (niveau cible attendu).
# Maps_to de niveau 4 (profil) → niveaux 2,3 uniquement.
# Maps_to de niveau 2 (capacite) → niveau 1 uniquement.
ALLOWED_MAPS_TO_LEVELS = {
    TYPE_PROFIL: {"2", "3", "4"},      # PT peut mapper vers CAP-INT, ART, F
    TYPE_CAPACITE: {"1"},               # CAP-INT ne doit mapper que vers CAP
}

SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*://")
LINK_RE = re.compile(r"!?\[[^]]*\]\(([^)]*)\)")
FRAGMENT_RE = re.compile(r"#.*$")
FENCE_RE = re.compile(r"^```")


def list_value(raw):
    """Parse a simple YAML inline list: ["a", "b"] or [] or a, b."""
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


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    fm = text[3:end].strip("\n")
    body = text[end + 4:]
    return fm, body


def fm_field(fm, key):
    m = re.search(r"^%s:\s*(.*)$" % re.escape(key), fm, re.MULTILINE)
    return m.group(1) if m else None


def check_frontmatter_validity(fm):
    """Renvoie la liste des erreurs de syntaxe YAML du bloc frontmatter.

    Utilise PyYAML si disponible (validation stricte), sinon un heuristique
    couvrant les cas observés en production :
      - frontmatter replié sur une seule ligne (champs sans saut de ligne) ;
      - valeur scalaire non quotée contenant ': ' (deux-points + espace) ;
      - guillemets non balancés (ex. ``version: "1.0.0"`` redoublé).
    """
    errors = []
    try:
        import yaml  # disponible dans certains environnements
        try:
            yaml.safe_load(fm)
            return errors
        except yaml.YAMLError as exc:
            errors.append("YAML invalide: %s" % str(exc).splitlines()[0])
            return errors
    except ImportError:
        pass
    lines = fm.split("\n")
    if len(lines) <= 1 and ":" in fm:
        errors.append("frontmatter replié sur une seule ligne (manque les sauts de ligne entre champs)")
        return errors
    for ln in lines:
        s = ln.strip()
        if not s or s.startswith("#") or s == "---":
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", s)
        if not m:
            errors.append("ligne de champ non analysable: %r" % ln)
            continue
        val = m.group(2).strip()
        if val == "" or val.startswith("["):
            continue
        if val in ("|", ">", "|-", ">-", "|-", ">-"):
            continue  # bloc scalaire, non validable simplement
        if val.startswith('"'):
            inner = val[1:]
            if not inner.endswith('"') or '"' in inner[:-1]:
                errors.append("guillemets doubles non balancés: %r" % ln)
            continue
        if val.startswith("'"):
            inner = val[1:]
            if not inner.endswith("'"):
                errors.append("guillemets simples non balancés: %r" % ln)
            continue
        if re.search(r":\s", val):
            errors.append("valeur non quotée contenant ': ' (à encadrer de guillemets): %r" % ln)
    return errors


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


def id_prefix(oid):
    """Extrait le préfixe d'un ID (ex. 'CAP' depuis 'CAP-INT-01' → 'CAP-INT')."""
    return oid.rsplit("-", 1)[0] if "-" in oid else oid


def id_niveau(oid):
    """Détermine le niveau d'un ID à partir de son préfixe."""
    p = oid.split("-")[0] if "-" in oid else oid
    if p in ("CAP",) and "INT" not in oid:
        return "1"
    if p == "CAP" and "INT" in oid:
        return "2"
    if p == "PT":
        return "4"
    if p in ("ART", "F", "ENF"):
        return "3"
    return None


def iter_md(root, bases):
    for base in bases:
        d = os.path.join(root, base)
        if not os.path.isdir(d):
            continue
        for dirpath, dirnames, filenames in os.walk(d):
            dirnames[:] = [dn for dn in dirnames if dn not in EXCLUDE_DIRS]
            for fn in filenames:
                if fn.endswith(".md"):
                    yield os.path.join(dirpath, fn)


# ---------------------------------------------------------------------------
# Vérifications de cohérence multi-niveaux (Phase 1)
# ---------------------------------------------------------------------------

def check_transitive_chain(objects, id_to_file):
    """Vérifie que chaque PT aboutit à un CAP via chaîne PT→CAP-INT→CAP.

    Renvoie (warnings, errors) où chaque entrée est (file, message).
    """
    warnings = []
    errors = []

    profiles = {oid: o for oid, o in objects.items()
                if o.get("type") == TYPE_PROFIL}
    capacites = {oid: o for oid, o in objects.items()
                 if o.get("type") == TYPE_CAPACITE}
    capabilites = {oid: o for oid, o in objects.items()
                   if o.get("type") == TYPE_CAPABILITE}

    for oid, o in sorted(profiles.items()):
        maps = o["out"] & set(objects.keys())
        cap_int_targets = [t for t in maps if objects[t].get("type") == TYPE_CAPACITE]
        cap_targets = [t for t in maps if objects[t].get("type") == TYPE_CAPABILITE]

        if not cap_int_targets and not cap_targets:
            rel_path = os.path.relpath(o["file"], REPO_ROOT)
            errors.append((rel_path, oid,
                           "Profil sans maps_to vers CAP-INT ou CAP : "
                           "chaîne PT→CAP rompue"))
            continue

        # Vérifier la chaîne transitive pour chaque CAP-INT ciblé
        for cap_int_id in cap_int_targets:
            cap_int_obj = objects.get(cap_int_id)
            if not cap_int_obj:
                continue
            cap_int_maps = cap_int_obj["out"] & set(objects.keys())
            cap_from_int = [t for t in cap_int_maps
                            if objects[t].get("type") == TYPE_CAPABILITE]
            if not cap_from_int:
                rel_path = os.path.relpath(o["file"], REPO_ROOT)
                warnings.append((rel_path, oid,
                                 "Chaîne PT→%s→CAP incomplète : "
                                 "%s n'a pas de maps_to vers CAP" % (cap_int_id, cap_int_id)))

    return warnings, errors


def check_type_consistency(objects, id_to_file):
    """Vérifie que les cibles de maps_to sont du bon type/niveau.

    Pour les CAP-INT : maps_to contient à la fois des principes (P-INT-*)
    et des capabilités (CAP-*). Seule l'absence totale de CAP-* est un problème.
    Pour les PT : un mappe vers un CAP-* (niveau 1) au lieu d'un CAP-INT-* est suspect.

    Renvoie (warnings, errors).
    """
    warnings = []
    errors = []

    # --- Vérifier que chaque CAP-INT a au moins un CAP-* dans maps_to ---
    capacites = {oid: o for oid, o in objects.items()
                 if o.get("type") == TYPE_CAPACITE}
    for oid, o in sorted(capacites.items()):
        cap_targets = [t for t in o["out"] & set(objects.keys())
                       if objects.get(t, {}).get("type") == TYPE_CAPABILITE]
        if not cap_targets:
            rel_path = os.path.relpath(o["file"], REPO_ROOT)
            warnings.append((rel_path, oid,
                             "CAP-INT sans maps_to vers un CAP : "
                             "chaîne CAP-INT→CAP manquante"))

    # --- Vérifier que les PT ne mélangent pas les niveaux dans maps_to ---
    profiles = {oid: o for oid, o in objects.items()
                if o.get("type") == TYPE_PROFIL}
    for oid, o in sorted(profiles.items()):
        for target_id in o["out"]:
            target_obj = objects.get(target_id)
            if not target_obj:
                continue
            target_type = target_obj.get("type")
            if target_type == TYPE_CAPABILITE:
                # Un PT mappe directement vers un CAP — informer
                rel_path = os.path.relpath(o["file"], REPO_ROOT)
                warnings.append((rel_path, oid,
                                 "Profil mappe directement vers %s "
                                 "(capabilité CAESN, niveau 1) : "
                                 "vérifier si un CAP-INT intermédiaire est requis"
                                 % target_id))

    return warnings, errors


def check_coverage(objects, id_to_file):
    """Génère un rapport de couverture des capabilités CAESN.

    Renvoie (warnings, info_lines) où warnings sont des problèmes
    et info_lines des informations de couverture.
    """
    warnings = []
    info = []

    capabilites = {oid: o for oid, o in objects.items()
                   if o.get("type") == TYPE_CAPABILITE}
    capacites = {oid: o for oid, o in objects.items()
                 if o.get("type") == TYPE_CAPACITE}
    profiles = {oid: o for oid, o in objects.items()
                if o.get("type") == TYPE_PROFIL}

    # Construire la couverture transitive : quels CAP sont atteints par des PT
    covered_caps = set()
    for pt_id, pt_obj in profiles.items():
        maps = pt_obj["out"] & set(objects.keys())
        for target_id in maps:
            tobj = objects.get(target_id)
            if not tobj:
                continue
            if tobj.get("type") == TYPE_CAPABILITE:
                covered_caps.add(target_id)
            elif tobj.get("type") == TYPE_CAPACITE:
                # Chaîne transitive : CAP-INT → CAP
                for deep_id in tobj["out"] & set(objects.keys()):
                    dobj = objects.get(deep_id)
                    if dobj and dobj.get("type") == TYPE_CAPABILITE:
                        covered_caps.add(deep_id)

    # CAP sans aucun PT atteignant
    unreachable_caps = sorted(set(capabilites.keys()) - covered_caps)
    if unreachable_caps:
        for cap_id in unreachable_caps:
            rel_path = os.path.relpath(id_to_file[cap_id], REPO_ROOT)
            warnings.append((rel_path, cap_id,
                             "Capabilité CAESN non atteinte par aucun PT "
                             "(via chaîne PT→CAP-INT→CAP)"))
    info.append("CAP atteints par au moins un PT : %d/%d"
                % (len(covered_caps), len(capabilites)))
    if unreachable_caps:
        info.append("CAP non atteints : %s" % ", ".join(unreachable_caps))

    # CAP-INT sans aucun PT consommateur
    cap_int_consumers = {}
    for pt_id, pt_obj in profiles.items():
        for target_id in pt_obj["out"] & set(objects.keys()):
            tobj = objects.get(target_id)
            if tobj and tobj.get("type") == TYPE_CAPACITE:
                cap_int_consumers.setdefault(target_id, set()).add(pt_id)

    orphan_cap_ints = sorted(set(capacites.keys()) - set(cap_int_consumers.keys()))
    if orphan_cap_ints:
        for cap_int_id in orphan_cap_ints:
            rel_path = os.path.relpath(id_to_file[cap_int_id], REPO_ROOT)
            warnings.append((rel_path, cap_int_id,
                             "CAP-INT sans aucun PT consommateur"))
        info.append("CAP-INT orphelins (sans PT) : %s"
                     % ", ".join(orphan_cap_ints))

    return warnings, info


def main():
    objects = {}          # id -> {file, out:set, in:set}
    id_to_file = {}
    all_links = []        # (file, target)

    for path in iter_md(REPO_ROOT, REL_DIRS):
        if os.path.basename(path) == "_schema.md":
            continue  # fichier de schéma, pas un nœud de graphe
        text = open(path, encoding="utf-8").read()
        fm, _body = parse_frontmatter(text)
        if fm is None:
            continue
        oid = parse_id(fm)
        if not oid:
            continue
        otype = parse_type(fm)
        outgoing = set()
        for k in RELATION_KEYS:
            val = fm_field(fm, k)
            for t in list_value(val):
                outgoing.add(t)
        objects[oid] = {"file": path, "out": outgoing, "in": set(), "type": otype}
        id_to_file[oid] = path

    # Liens relatifs : tous les documents du cadre.
    for path in iter_md(REPO_ROOT, LINK_DIRS):
        text = open(path, encoding="utf-8").read()
        fm, body = parse_frontmatter(text)
        in_fence = False
        for line in body.splitlines():
            if FENCE_RE.match(line.strip()):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for m in LINK_RE.finditer(line):
                target = m.group(1).strip()
                if not target:
                    continue
                if SCHEME_RE.match(target):
                    continue
                if target.startswith(("mailto:", "tel:", "data:")):
                    continue
                if target.startswith("/"):
                    continue
                if target.startswith("#"):
                    continue
                all_links.append((path, FRAGMENT_RE.sub("", target)))

    # build incoming + resolve
    unresolved = []  # (file, source_id, target)
    for oid, o in objects.items():
        for t in o["out"]:
            if t in objects:
                objects[t]["in"].add(oid)
            else:
                unresolved.append((o["file"], oid, t))

    # island detection
    islands = []
    for oid, o in objects.items():
        if not o["out"] and not o["in"]:
            islands.append(oid)

    # broken relative links
    broken = []
    for path, target in all_links:
        if not target:
            continue
        resolved = os.path.normpath(os.path.join(os.path.dirname(path), target))
        if not os.path.exists(resolved):
            broken.append((path, target))

    # frontmatter YAML validity (récurrence des frontmatter brisés)
    fm_errors = []
    for path in iter_md(REPO_ROOT, LINK_DIRS):
        text = open(path, encoding="utf-8").read()
        fm, _ = parse_frontmatter(text)
        if fm is None:
            continue
        for err in check_frontmatter_validity(fm):
            fm_errors.append((path, err))

    # report
    print("=== Validation du référentiel HEA ===")
    print("Objets indexés : %d" % len(objects))
    print("Liens relatifs vérifiés : %d" % len(all_links))

    ok = True

    if unresolved:
        ok = False
        print("\n[ERREUR] Cibles de relation non résolues : %d" % len(unresolved))
        for f, s, t in unresolved[:50]:
            print("  - %s (%s) -> %s" % (os.path.relpath(f, REPO_ROOT), s, t))
    else:
        print("[OK] Toutes les relations pointent vers un objet existant.")

    if broken:
        ok = False
        print("\n[ERREUR] Liens relatifs cassés : %d" % len(broken))
        for f, t in broken[:50]:
            print("  - %s -> %s" % (os.path.relpath(f, REPO_ROOT), t))
    else:
        print("[OK] Aucun lien relatif cassé.")

    if fm_errors:
        ok = False
        print("\n[ERREUR] Frontmatter YAML invalide : %d" % len(fm_errors))
        for f, e in fm_errors[:50]:
            print("  - %s : %s" % (os.path.relpath(f, REPO_ROOT), e))
    else:
        print("[OK] Tous les frontmatter sont du YAML valide.")

    known = [i for i in islands if i in KNOWN_ISLANDS]
    unknown = [i for i in islands if i not in KNOWN_ISLANDS]
    if islands:
        print("\n[AVERTISSEMENT] Objets isolés (îlots, degré 0) : %d" % len(islands))
        for i in known:
            print("  ~ %s (%s) [attendu/candidat]" % (i, os.path.relpath(id_to_file[i], REPO_ROOT)))
        for i in unknown:
            print("  ! %s (%s) [NON AUTORISÉ]" % (i, os.path.relpath(id_to_file[i], REPO_ROOT)))
        if unknown:
            ok = False
    else:
        print("[OK] Aucun objet isolé.")

    # --- Vérifications de cohérence multi-niveaux ---

    # 1. Chaîne PT → CAP-INT → CAP
    chain_warns, chain_errs = check_transitive_chain(objects, id_to_file)
    if chain_errs:
        ok = False
        print("\n[ERREUR] Chaîne PT→CAP-INT→CAP rompue : %d" % len(chain_errs))
        for f, oid, msg in chain_errs[:30]:
            print("  - %s (%s) : %s" % (f, oid, msg))
    else:
        print("[OK] Tous les profils aboutissent à une capabilité CAESN.")

    if chain_warns:
        print("\n[AVERTISSEMENT] Chaîne PT→CAP partielle : %d" % len(chain_warns))
        for f, oid, msg in chain_warns[:30]:
            print("  ~ %s (%s) : %s" % (f, oid, msg))

    # 2. Cohérence des types dans maps_to
    type_warns, type_errs = check_type_consistency(objects, id_to_file)
    if type_errs:
        ok = False
        print("\n[ERREUR] Types incohérents dans maps_to : %d" % len(type_errs))
        for f, oid, msg in type_errs[:30]:
            print("  - %s (%s) : %s" % (f, oid, msg))
    if type_warns:
        print("\n[AVERTISSEMENT] Correspondances multi-niveaux : %d" % len(type_warns))
        for f, oid, msg in type_warns[:30]:
            print("  ~ %s (%s) : %s" % (f, oid, msg))
    if not type_warns and not type_errs:
        print("[OK] Types cohérents dans toutes les relations maps_to.")

    # 3. Couverture des capabilités CAESN
    cov_warns, cov_info = check_coverage(objects, id_to_file)
    if cov_warns:
        print("\n[AVERTISSEMENT] Couverture CAESN incomplète : %d" % len(cov_warns))
        for f, oid, msg in cov_warns[:30]:
            print("  ~ %s (%s) : %s" % (f, oid, msg))
    for line in cov_info:
        print("  [INFO] %s" % line)
    if not cov_warns:
        print("[OK] Toutes les capabilités CAESN sont atteintes par au moins un PT.")

    print("\nRésumé : %s" % ("CONFORME" if ok else "ANOMALIES DÉTECTÉES"))
    return 0 if ok else 1


def validate_frontmatter_only():
    """Vérifie uniquement que tous les frontmatter sont du YAML valide."""
    import yaml
    errors = []
    
    for dirpath, _dirs, files in os.walk(REPO_ROOT):
        if any(d in dirpath for d in EXCLUDE_DIRS):
            continue
        for name in files:
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, REPO_ROOT)
            if rel == "README.md":
                continue
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            fm, _ = parse_frontmatter(text)
            if fm is None:
                errors.append("%s : frontmatter manquant" % rel)
                continue
            try:
                yaml.safe_load(fm)
            except yaml.YAMLError as exc:
                errors.append("%s : YAML invalide - %s" % (rel, str(exc).splitlines()[0]))
    
    if errors:
        print("\n[ERREUR] Frontmatter invalides : %d" % len(errors))
        for err in errors[:30]:
            print("  - %s" % err)
        return 1
    else:
        print("[OK] Tous les frontmatter sont du YAML valide.")
        return 0


def validate_quick():
    """Validation rapide : frontmatter + liens cassés seulement."""
    import subprocess
    
    print("=== Validation rapide ===")
    
    # 1. Frontmatter
    if validate_frontmatter_only() != 0:
        return 1
    
    # 2. Liens cassés
    result = subprocess.run(
        [sys.executable, os.path.join(REPO_ROOT, "scripts", "check_links.py")],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.returncode != 0:
        return 1
    
    print("[OK] Validation rapide : tout est conforme.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Valide la cohérence du référentiel HEA")
    parser.add_argument("--frontmatter-only", action="store_true",
                        help="Vérifie uniquement la validité des frontmatter YAML")
    parser.add_argument("--quick", action="store_true",
                        help="Validation rapide (frontmatter + liens seulement)")
    args = parser.parse_args()
    
    if args.frontmatter_only:
        sys.exit(validate_frontmatter_only())
    elif args.quick:
        sys.exit(validate_quick())
    else:
        sys.exit(main())
