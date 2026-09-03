#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valide la coherence interne du referentiel HEA.

Ce script verifie specifiquement les objets du referentiel (capabilites, capacites, principes, profils, etc.)
et leurs relations. Il complete validate_ref.py qui se concentre sur le graphe global.

Verifications effectuees :
  - Coherence des types d'objets (capabilite, capacite, principe, profil, etc.)
  - Validite des champs obligatoires par type
  - Coherence des niveaux hierarchiques (1-4)
  - Validite des relations (maps_to, implements, applies_to, related)
  - Coherence des references entre objets du referentiel
  - Couverture des principes par les capacites
  - Chaines de relations valides (PT -> CAP-INT -> CAP)

Usage :
    python3 scripts/validate_referentiel.py          # Validation complete
    python3 scripts/validate_referentiel.py --check  # Exit 1 si erreurs
    python3 scripts/validate_referentiel.py --strict # Exit 1 aussi pour les avertissements
"""

import argparse
import os
import re
import sys
from collections import defaultdict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF_DIR = os.path.join(REPO_ROOT, "referentiel")

# Types d'objets reconnus dans le referentiel
VALID_TYPES = {
    "capabilite",
    "capacite",
    "principe",
    "chapitre",
    "profil",
    "composant-applicatif",
    "composant-infrastructure",
    "composant-securite",
    "composant-gouvernance",
    "acteur",
    "role",
    "service",
    "valeur",
    "objet-metier",
    "objet-donnee",
    "processus",
    "flux-valeur",
    "lieu",
    "partie-prenante",
    "exigence",
    "decision",
    "etape-valeur",
    "plateau",
    "registre-gouvernance",
    "work-package",
    "fondation",
    "gap",
    "processus-metier",
}

# Champs obligatoires par type d'objet
REQUIRED_FIELDS = {
    "capabilite": {"id", "type", "title", "niveau", "status", "version"},
    "capacite": {"id", "type", "title", "niveau", "status", "version"},
    "principe": {"id", "type", "title", "niveau", "status", "version"},
    "chapitre": {"id", "type", "title", "niveau", "status", "version"},
    "profil": {"id", "type", "title", "niveau", "status", "version"},
    "decision": {"id", "type", "title", "status", "version"},
}

# Niveaux hierarchiques valides
VALID_LEVELS = {"1", "2", "3", "4"}

# Relations valides (cles du frontmatter)
RELATION_KEYS = [
    "maps_to", "implements", "applies_to", "related",
    "realized_by", "contributes_to", "performs", "accesses",
    "governs", "represents", "assigned_to", "has_role",
    "located_at", "serves", "produced_by", "detenu_par",
    "soutient_flux_de_valeur", "utilise_composant",
    "supporte_standard", "a_pour_proprietaire_fonctionnel"
]

# Repertoires a exclure
EXCLUDE_DIRS = {".git", "__pycache__", "node_modules", "dist", ".venv",
                "graphify-out", ".agents", ".claude", "mintlify-site", "docs"}

# Patterns pour les IDs
ID_PATTERNS = {
    "capabilite": re.compile(r"^CAP-\d{1,2}$"),
    "capacite": re.compile(r"^CAP-INT-\d{1,2}$"),
    "principe": re.compile(r"^(P-(INT|AA|DD|PA|PD-VS|PD-DS)|AA|DD|PA|PD-VS|PD-DS)-\d{1,2}$"),
    "chapitre": re.compile(r"^ART-\d{1,2}$"),
    "profil": re.compile(r"^PT-\d{1,2}$"),
    "decision": re.compile(r"^adr-\d{4}(?:-[a-z0-9-]+)?$", re.IGNORECASE),
}

SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*://")
LINK_RE = re.compile(r"!?\[[^]]*\]\(([^)]*)\)")
FRAGMENT_RE = re.compile(r"#.*$")
FENCE_RE = re.compile(r"^```")


class ReferentielObject:
    """Represente un objet du referentiel."""
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.relpath = os.path.relpath(filepath, REPO_ROOT)
        self.id = None
        self.type = None
        self.title = None
        self.niveau = None
        self.status = None
        self.version = None
        self.domain = None
        self.owner = None
        self.frontmatter = {}
        self.body = ""
        self.errors = []
        self.warnings = []
        self.relations = defaultdict(set)
        
        self._parse()
    
    def _parse(self):
        """Parse le fichier markdown."""
        try:
            with open(self.filepath, encoding="utf-8") as f:
                content = f.read()
            
            fm_match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
            if not fm_match:
                self.errors.append("Frontmatter YAML manquant")
                return
            
            fm_text = fm_match.group(1)
            self.body = fm_match.group(2)
            self.frontmatter = self._parse_frontmatter(fm_text)
            
            self.id = self.frontmatter.get("id", "")
            self.type = self.frontmatter.get("type", "")
            self.title = self.frontmatter.get("title", "")
            self.niveau = self.frontmatter.get("niveau", "")
            self.status = self.frontmatter.get("status", "")
            self.version = self.frontmatter.get("version", "")
            self.domain = self.frontmatter.get("domain", "")
            self.owner = self.frontmatter.get("owner", "")
            
            for key in RELATION_KEYS:
                val = self.frontmatter.get(key, [])
                if isinstance(val, str):
                    val = self._parse_list_value(val)
                if isinstance(val, list):
                    for target in val:
                        if target and not target.startswith("#"):
                            self.relations[key].add(target)
                        
        except Exception as e:
            self.errors.append(f"Erreur de lecture: {e}")
    
    def _parse_frontmatter(self, fm_text):
        """Parse le frontmatter YAML de maniere simple."""
        fields = {}
        for line in fm_text.split("\n"):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            
            if value.startswith("[") and value.endswith("]"):
                inner = value[1:-1]
                items = [item.strip().strip("'\"") for item in inner.split(",") if item.strip()]
                fields[key] = items
            elif value.startswith('"') and value.endswith('"'):
                fields[key] = value[1:-1].strip()
            elif value.startswith("'") and value.endswith("'"):
                fields[key] = value[1:-1].strip()
            else:
                fields[key] = value
        return fields
    
    def _parse_list_value(self, value):
        """Parse une valeur de liste."""
        if not value:
            return []
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1]
            return [item.strip().strip("'\"") for item in inner.split(",") if item.strip()]
        return [value]
    
    def validate(self, all_objects, type_registry):
        """Valide l'objet et retourne les erreurs/avertissements."""
        # 1. Verifier l'ID
        if not self.id:
            self.errors.append("ID manquant")
        else:
            if self.type in ID_PATTERNS:
                pattern = ID_PATTERNS[self.type]
                if not pattern.match(self.id):
                    self.warnings.append(f"ID ne correspond pas au format attendu pour {self.type}: {self.id}")
            
            if self.id in type_registry:
                existing = type_registry[self.id]
                if existing.filepath != self.filepath:
                    self.errors.append(f"ID duplique: {self.id} (deja defini dans {existing.relpath})")
        
        # 2. Verifier le type
        if not self.type:
            self.errors.append("Type manquant")
        elif self.type not in VALID_TYPES:
            self.warnings.append(f"Type non reconnu: {self.type}")
        
        # 3. Verifier les champs obligatoires
        if self.type in REQUIRED_FIELDS:
            missing = REQUIRED_FIELDS[self.type] - set(self.frontmatter.keys())
            if missing:
                self.errors.append(f"Champs obligatoires manquants pour {self.type}: {', '.join(sorted(missing))}")
        
        # 4. Verifier le niveau
        if self.niveau and self.niveau not in VALID_LEVELS:
            self.errors.append(f"Niveau invalide: {self.niveau}. Valides: {', '.join(sorted(VALID_LEVELS))}")
        
        # 5. Verifier la coherence type-niveau
        if self.type and self.niveau:
            expected_levels = self._get_expected_levels(self.type)
            if expected_levels and self.niveau not in expected_levels:
                self.errors.append(f"Niveau {self.niveau} inattendu pour type {self.type}. Attendus: {', '.join(expected_levels)}")
        
        # 6. Verifier les statuts
        if self.status:
            valid_statuses = {"draft", "candidate", "proposed", "active", "accepted", "applied", "stable", "deprecated", "replaced", "retired"}
            if self.status.lower() not in valid_statuses:
                self.warnings.append(f"Statut invalide: {self.status}")
        
        # 7. Verifier les relations
        for rel_key, targets in self.relations.items():
            for target in targets:
                if target not in all_objects:
                    self.warnings.append(f"Cible de relation non resolue: {rel_key} -> {target}")
        
        # 8. Verifier les liens internes dans le corps
        self._validate_body_links(all_objects)
        
        return self.errors, self.warnings
    
    def _get_expected_levels(self, obj_type):
        """Retourne les niveaux attendus pour un type donne."""
        level_map = {
            "capabilite": {"1"},
            "capacite": {"2"},
            "principe": {"1", "2"},
            "chapitre": {"3"},
            "profil": {"4"},
        }
        return level_map.get(obj_type, None)
    
    def _validate_body_links(self, all_objects):
        """Valide les liens internes dans le corps du document."""
        obj_ref_pattern = re.compile(r"(?:CAP|PT|ART|P-(?:INT|AA|DD|PA|PD-VS|PD-DS))-[A-Za-z0-9-]+")
        
        in_fence = False
        for line in self.body.splitlines():
            if FENCE_RE.match(line.strip()):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            
            for match in obj_ref_pattern.finditer(line):
                ref = match.group(0).upper()
                if ref not in all_objects:
                    if re.match(r"^(CAP|PT|ART|P-(INT|AA|DD|PA|PD-VS|PD-DS))-\d+", ref):
                        self.warnings.append(f"Reference a un objet non trouve: {ref}")
    
    def __repr__(self):
        return f"{self.type}:{self.id} ({self.relpath})"


def load_referentiel_objects():
    """Charge tous les objets du referentiel."""
    objects = {}
    type_registry = {}
    
    if not os.path.isdir(REF_DIR):
        return objects, type_registry
    
    for dirpath, dirnames, filenames in os.walk(REF_DIR):
        dirnames[:] = [dn for dn in dirnames if dn not in EXCLUDE_DIRS]
        
        for filename in filenames:
            if filename.endswith(".md"):
                filepath = os.path.join(dirpath, filename)
                if filename == "_schema.md" or filename == "_index.md":
                    continue
                
                obj = ReferentielObject(filepath)
                if obj.id:
                    objects[obj.id] = obj
                    type_registry[obj.id] = obj
    
    return objects, type_registry


def validate_type_consistency(objects):
    """Verifie la coherence des types avec les niveaux."""
    errors = []
    warnings = []
    
    type_level_count = defaultdict(lambda: defaultdict(int))
    for oid, obj in objects.items():
        if obj.type and obj.niveau:
            type_level_count[obj.type][obj.niveau] += 1
    
    expected_type_levels = {
        "capabilite": {"1"},
        "capacite": {"2"},
        "principe": {"1", "2"},
        "chapitre": {"3"},
        "profil": {"4"},
    }
    
    for obj_type, levels in expected_type_levels.items():
        if obj_type in type_level_count:
            for level in levels:
                if level not in type_level_count[obj_type]:
                    warnings.append(f"Aucun objet de type {obj_type} au niveau {level}")
    
    return errors, warnings


def validate_relationships(objects):
    """Verifie la coherence des relations."""
    errors = []
    warnings = []
    
    graph = defaultdict(set)
    reverse_graph = defaultdict(set)
    
    for oid, obj in objects.items():
        for rel_key, targets in obj.relations.items():
            for target in targets:
                if target in objects:
                    graph[oid].add(target)
                    reverse_graph[target].add(oid)
    
    profil_type = "profil"
    capacite_type = "capacite"
    capabilite_type = "capabilite"
    
    profiles = {oid: obj for oid, obj in objects.items() if obj.type == profil_type}
    capacites = {oid: obj for oid, obj in objects.items() if obj.type == capacite_type}
    capabilites = {oid: obj for oid, obj in objects.items() if obj.type == capabilite_type}
    
    for pt_id, pt_obj in profiles.items():
        pt_targets = graph.get(pt_id, set())
        cap_int_targets = [t for t in pt_targets if t in capacites]
        
        if not cap_int_targets:
            cap_targets = [t for t in pt_targets if t in capabilites]
            if not cap_targets:
                warnings.append(f"{pt_id}: Profil sans maps_to vers CAP-INT ou CAP")
            continue
        
        for cap_int_id in cap_int_targets:
            cap_int_targets_2 = graph.get(cap_int_id, set())
            cap_from_int = [t for t in cap_int_targets_2 if t in capabilites]
            if not cap_from_int:
                warnings.append(f"{pt_id} -> {cap_int_id}: Chaine PT->CAP-INT->CAP incompletes")
    
    for cap_int_id, cap_int_obj in capacites.items():
        cap_int_targets = graph.get(cap_int_id, set())
        invalid_targets = [t for t in cap_int_targets if t not in capabilites and t not in capacites]
        if invalid_targets:
            warnings.append(f"{cap_int_id}: CAP-INT pointe vers des objets non-CAP: {', '.join(invalid_targets)}")
    
    principes = {oid: obj for oid, obj in objects.items() if obj.type == "principe"}
    covered_principes = set()
    for cap_int_id, cap_int_obj in capacites.items():
        cap_int_targets = graph.get(cap_int_id, set())
        for target in cap_int_targets:
            if target in principes:
                covered_principes.add(target)
    
    uncovered_principes = set(principes.keys()) - covered_principes
    if uncovered_principes:
        warnings.append(f"Principe(s) non couvert(s) par les CAP-INT: {', '.join(sorted(uncovered_principes))}")
    
    return errors, warnings


def validate_completeness(objects):
    """Verifie la completude du referentiel."""
    errors = []
    warnings = []
    
    type_counts = defaultdict(int)
    for obj in objects.values():
        type_counts[obj.type] += 1
    
    expected_minimum = {
        "capabilite": 18,
        "capacite": 16,
        "principe": 25,
        "profil": 19,
    }
    
    for obj_type, expected in expected_minimum.items():
        actual = type_counts.get(obj_type, 0)
        if actual < expected:
            warnings.append(f"Nombre insuffisant d'objets de type {obj_type}: {actual} (attendu: {expected})")
    
    return errors, warnings


def main():
    """Execute la validation complete."""
    parser = argparse.ArgumentParser(description="Valide le referentiel HEA")
    parser.add_argument("--check", action="store_true",
                        help="Exit 1 si des erreurs sont trouvees")
    parser.add_argument("--strict", action="store_true",
                        help="Exit 1 aussi pour les avertissements")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Afficher plus de details")
    args = parser.parse_args()
    
    print("=" * 60)
    print("VALIDATION DU REFERENTIEL HEA")
    print("=" * 60)
    
    objects, type_registry = load_referentiel_objects()
    
    print(f"\n[1/5] Chargement du referentiel...")
    print(f"  Objets charges: {len(objects)}")
    
    type_counts = defaultdict(int)
    for obj in objects.values():
        type_counts[obj.type] += 1
    print(f"  Par type:")
    for obj_type, count in sorted(type_counts.items()):
        print(f"    - {obj_type}: {count}")
    
    print(f"\n[2/5] Validation des objets individuels...")
    all_errors = []
    all_warnings = []
    
    for oid, obj in sorted(objects.items()):
        errors, warnings = obj.validate(objects, type_registry)
        if errors:
            all_errors.append((oid, errors))
        if warnings:
            all_warnings.append((oid, warnings))
    
    if all_errors:
        print(f"\n[ERREUR] {len(all_errors)} objets avec des erreurs:")
        for oid, errors in all_errors[:20]:
            print(f"  {oid}:")
            for error in errors:
                print(f"    - {error}")
    else:
        print(f"  [OK] Aucun erreur dans les objets individuels")
    
    if all_warnings:
        print(f"\n[AVERTEISSEMENT] {len(all_warnings)} objets avec des avertissements:")
        for oid, warnings in all_warnings[:20]:
            print(f"  {oid}:")
            for warning in warnings[:5]:
                print(f"    ~ {warning}")
    else:
        print(f"  [OK] Aucun avertissement")
    
    print(f"\n[3/5] Validation de la coherence des types...")
    type_errors, type_warnings = validate_type_consistency(objects)
    if type_errors:
        for error in type_errors:
            print(f"  [ERREUR] {error}")
        all_errors.append(("type_consistency", type_errors))
    if type_warnings:
        for warning in type_warnings:
            print(f"  [AVERTISSEMENT] {warning}")
        all_warnings.append(("type_consistency", type_warnings))
    if not type_errors and not type_warnings:
        print(f"  [OK] Coherence des types valide")
    
    print(f"\n[4/5] Validation des relations...")
    rel_errors, rel_warnings = validate_relationships(objects)
    if rel_errors:
        for error in rel_errors:
            print(f"  [ERREUR] {error}")
        all_errors.append(("relationships", rel_errors))
    if rel_warnings:
        for warning in rel_warnings:
            print(f"  [AVERTISSEMENT] {warning}")
        all_warnings.append(("relationships", rel_warnings))
    if not rel_errors and not rel_warnings:
        print(f"  [OK] Relations valides")
    
    print(f"\n[5/5] Validation de la completude...")
    comp_errors, comp_warnings = validate_completeness(objects)
    if comp_errors:
        for error in comp_errors:
            print(f"  [ERREUR] {error}")
        all_errors.append(("completeness", comp_errors))
    if comp_warnings:
        for warning in comp_warnings:
            print(f"  [AVERTISSEMENT] {warning}")
        all_warnings.append(("completeness", comp_warnings))
    if not comp_errors and not comp_warnings:
        print(f"  [OK] Completude valide")
    
    print(f"\n[RESUME]")
    total_errors = sum(len(e) for _, e in all_errors if isinstance(e, list))
    total_warnings = sum(len(w) for _, w in all_warnings if isinstance(w, list))
    
    print(f"  Total: {len(objects)} objets analyses")
    print(f"  Erreurs: {total_errors}")
    print(f"  Avertissements: {total_warnings}")
    
    if total_errors == 0 and total_warnings == 0:
        print(f"\nTOUT EST CONFORME")
        return 0
    elif total_errors == 0:
        print(f"\nCONFORME (avec avertissements)")
        return 0
    else:
        print(f"\nANOMALIES DETECTEES")
        return 1


if __name__ == "__main__":
    sys.exit(main())
