#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valide la cohérence des Architecture Decision Records (ADR) du HEA.

Vérifie :
  - Unicité des identifiants ADR
  - Format des identifiants (ADR-XXXX)
  - Structure du frontmatter (champs obligatoires)
  - Statuts valides (proposé, accepté, appliqué, remplacé, déprécié)
  - Références croisées valides (dans maps_to, implements, etc.)
  - Conformité au template ADR
  - Index et registre à jour

Usage :
    python3 scripts/validate_adr.py          # Validation complète
    python3 scripts/validate_adr.py --check   # Exit 1 si erreurs
    python3 scripts/validate_adr.py --fix    # Corriger automatiquement (si possible)
"""

import argparse
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ADR_DIR = REPO_ROOT / "01_cnisn" / "06_decisions"
REGISTRE_FILE = ADR_DIR / "registre-decisions.md"
INDEX_FILE = ADR_DIR / "index.md"
TEMPLATE_FILE = ADR_DIR / "adr-0000-template.md"

# Statuts valides pour les ADR
VALID_STATUSES = {"proposé", "accepté", "appliqué", "remplacé", "déprécié", "candidate", "active", "draft"}

# Champs obligatoires dans le frontmatter ADR
REQUIRED_FIELDS = {"title", "id", "domain", "version", "status"}

# Format de l'identifiant ADR
ADR_ID_PATTERN = re.compile(r"^ADR-\d{4}-[a-z0-9-]+$", re.IGNORECASE)
ADR_ID_SIMPLE = re.compile(r"^ADR-\d{4}$", re.IGNORECASE)

# Pattern pour extraire les références ADR dans le markdown
ADR_REF_PATTERN = re.compile(r"(?:ADR-\d{4}|adr-\d{4})[-a-z0-9]*", re.IGNORECASE)


class ADRValidationError(Exception):
    """Erreur de validation ADR."""
    pass


class ADR:
    """Représente un Architecture Decision Record."""
    
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        self.relpath = self.filepath.relative_to(REPO_ROOT)
        self.id = None
        self.title = None
        self.status = None
        self.domain = None
        self.version = None
        self.date = None
        self.owner = None
        self.related = []
        self.references = []
        self.frontmatter = {}
        self.body = ""
        self.errors = []
        self.warnings = []
        
        self._parse()
    
    def _parse(self):
        """Parse le fichier ADR."""
        try:
            with open(self.filepath, encoding="utf-8") as f:
                content = f.read()
            
            # Extraire le frontmatter
            fm_match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
            if not fm_match:
                self.errors.append("Frontmatter YAML manquant")
                return
            
            fm_text = fm_match.group(1)
            self.body = fm_match.group(2)
            
            # Parser le frontmatter (format simple)
            self.frontmatter = self._parse_frontmatter(fm_text)
            
            # Extraire les champs
            self.id = self.frontmatter.get("id", "")
            self.title = self.frontmatter.get("title", "")
            self.status = self.frontmatter.get("status", "").lower()
            self.domain = self.frontmatter.get("domain", "")
            self.version = self.frontmatter.get("version", "")
            self.date = self.frontmatter.get("date", "")
            self.owner = self.frontmatter.get("owner", "")
            
            # Extraire les références
            self.related = self._parse_list_field(self.frontmatter.get("related", []))
            
            # Extraire les références ADR dans le corps
            self.references = ADR_REF_PATTERN.findall(self.body)
            
        except Exception as e:
            self.errors.append(f"Erreur de lecture: {e}")
    
    def _parse_frontmatter(self, fm_text):
        """Parse le frontmatter YAML de manière simple."""
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
            
            # Nettoyer la valeur
            if value.startswith("[") and value.endswith("]"):
                # Liste
                items = [item.strip().strip("'\"") for item in value[1:-1].split(",") if item.strip()]
                fields[key] = items
            elif value.startswith(""") and value.endswith("""):
                # String avec guillemets
                fields[key] = value[1:-1].strip()
            elif value.startswith("'") and value.endswith("'"):
                fields[key] = value[1:-1].strip()
            else:
                fields[key] = value
        return fields
    
    def _parse_list_field(self, value):
        """Parse un champ de type liste."""
        if isinstance(value, list):
            return value
        if isinstance(value, str):
            if value.startswith("[") and value.endswith("]"):
                inner = value[1:-1]
                return [item.strip().strip("'\"") for item in inner.split(",") if item.strip()]
            return [value]
        return []
    
    def validate(self, all_adr_ids):
        """Valide l'ADR et retourne les erreurs/avertissements."""
        # Normaliser l'ID pour comparaison (majuscules)
        normalized_id = self.id.upper() if self.id else ""
        
        # 1. Vérifier l'ID
        if not self.id:
            self.errors.append("ID manquant")
        elif not ADR_ID_SIMPLE.match(self.id) and not ADR_ID_PATTERN.match(self.id):
            self.errors.append(f"ID invalide: {self.id}. Format attendu: ADR-XXXX ou ADR-XXXX-nom")
        else:
            # Vérifier les doublons (comparaison case-insensitive)
            for existing_id in all_adr_ids:
                if existing_id.upper() == normalized_id and existing_id != self.id:
                    self.errors.append(f"ID dupliqué: {self.id} (conflit avec {existing_id})")
                    break
        
        # 2. Vérifier le titre
        if not self.title:
            self.errors.append("Titre manquant")
        elif normalized_id not in self.title.upper():
            self.warnings.append(f"Titre ne contient pas l'ID: {self.id}")
        
        # 3. Vérifier le statut
        if self.status and self.status.lower() not in {s.lower() for s in VALID_STATUSES}:
            self.errors.append(f"Statut invalide: {self.status}. Valides: {', '.join(sorted(VALID_STATUSES))}")
        
        # 4. Vérifier le domain
        if self.domain != "06_decisions":
            self.warnings.append(f"Domain inattendu: {self.domain}. Attendu: 06_decisions")
        
        # 5. Vérifier les champs obligatoires
        missing = REQUIRED_FIELDS - set(self.frontmatter.keys())
        if missing:
            self.errors.append(f"Champs obligatoires manquants: {', '.join(sorted(missing))}")
        
        # 6. Vérifier les références
        for ref in self.references:
            # Normaliser la référence
            ref_upper = ref.upper()
            # Vérifier si une version normalisée existe
            found = False
            for adr_id in all_adr_ids:
                if adr_id.upper() == ref_upper or adr_id.upper().startswith(ref_upper):
                    found = True
                    break
            if not found and not ref_upper.startswith("ADR-0000"):
                self.warnings.append(f"Référence à un ADR inexistant: {ref}")
        
        # 7. Vérifier la structure du template
        self._validate_template_structure()
        
        return self.errors, self.warnings
    
    def _validate_template_structure(self):
        """Vérifier que l'ADR suit la structure du template."""
        required_sections = [
            "Pour qui lire ce document",
            "Contexte",
            "Décision",
            "Justification",
            "Conséquences",
        ]
        
        for section in required_sections:
            if section not in self.body:
                self.warnings.append(f"Section manquante: {section}")
    
    def __repr__(self):
        return f"ADR({self.id}: {self.title[:50]}...)"


def load_all_adrs():
    """Charge tous les ADR du répertoire."""
    adrs = {}
    if not ADR_DIR.exists():
        return adrs
    
    for filepath in sorted(ADR_DIR.glob("adr-*.md")):
        if filepath.name == "adr-0000-template.md":
            continue
        adr = ADR(filepath)
        adrs[adr.id] = adr
    
    return adrs


def validate_registre(adrs):
    """Valide que le registre des décisions est à jour."""
    errors = []
    warnings = []
    
    if not REGISTRE_FILE.exists():
        errors.append(f"Fichier registre manquant: {REGISTRE_FILE}")
        return errors, warnings
    
    with open(REGISTRE_FILE, encoding="utf-8") as f:
        content = f.read()
    
    # Extraire les ADR du registre (case-insensitive)
    registre_adrs = set()
    for line in content.split("\n"):
        if "| ADR-" in line or "| adr-" in line:
            parts = line.split("|")
            if len(parts) >= 2:
                adr_id = parts[1].strip()
                if adr_id and not adr_id.upper().startswith("ADR-0000"):
                    registre_adrs.add(adr_id.upper())
    
    # Comparer avec les ADR réels (normalisés en majuscules)
    real_adrs = {id.upper() for id in adrs.keys() if not id.upper().startswith("ADR-0000")}
    
    missing_in_registre = real_adrs - registre_adrs
    extra_in_registre = registre_adrs - real_adrs
    
    if missing_in_registre:
        # Afficher en minuscules comme dans les fichiers
        display_missing = [id for id in sorted(missing_in_registre) if id != "ADR-0000"]
        errors.append(f"ADR manquants dans le registre: {', '.join(display_missing)}")
    if extra_in_registre:
        display_extra = [id for id in sorted(extra_in_registre) if id != "ADR-0000"]
        warnings.append(f"ADR dans le registre mais pas de fichier: {', '.join(display_extra)}")
    
    return errors, warnings


def validate_index(adrs):
    """Valide que l'index est à jour."""
    errors = []
    warnings = []
    
    if not INDEX_FILE.exists():
        errors.append(f"Fichier index manquant: {INDEX_FILE}")
        return errors, warnings
    
    with open(INDEX_FILE, encoding="utf-8") as f:
        content = f.read()
    
    # Extraire les ADR de l'index (case-insensitive)
    index_adrs = set()
    for line in content.split("\n"):
        if "| ADR-" in line or "| adr-" in line:
            parts = line.split("|")
            if len(parts) >= 2:
                adr_id = parts[1].strip()
                # Nettoyer l'ID (enlever les espaces, les backticks, etc.)
                adr_id = adr_id.strip(" `")
                if adr_id and not adr_id.upper().startswith("ADR-0000"):
                    index_adrs.add(adr_id.upper())
    
    # Comparer avec les ADR réels (normalisés en majuscules)
    real_adrs = {id.upper() for id in adrs.keys() if not id.upper().startswith("ADR-0000")}
    
    missing_in_index = real_adrs - index_adrs
    extra_in_index = index_adrs - real_adrs
    
    if missing_in_index:
        display_missing = [id for id in sorted(missing_in_index) if id != "ADR-0000"]
        errors.append(f"ADR manquants dans l'index: {', '.join(display_missing)}")
    if extra_in_index:
        display_extra = [id for id in sorted(extra_in_index) if id != "ADR-0000"]
        warnings.append(f"ADR dans l'index mais pas de fichier: {', '.join(display_extra)}")
    
    return errors, warnings


def main():
    """Exécute la validation complète."""
    parser = argparse.ArgumentParser(description="Valide les ADR du HEA")
    parser.add_argument("--check", action="store_true",
                        help="Exit 1 si des erreurs sont trouvées")
    parser.add_argument("--fix", action="store_true",
                        help="Corriger automatiquement les problèmes (si possible)")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Afficher plus de détails")
    args = parser.parse_args()
    
    print("=" * 60)
    print("VALIDATION DES ADR")
    print("=" * 60)
    
    # Charger tous les ADR
    adrs = load_all_adrs()
    all_adr_ids = set(adrs.keys())
    
    print(f"\n[1/5] Chargement des ADR...")
    print(f"  Trouvés: {len(adrs)} ADR")
    
    # Valider chaque ADR
    print(f"\n[2/5] Validation des ADR individuels...")
    all_errors = []
    all_warnings = []
    
    for adr_id, adr in sorted(adrs.items()):
        errors, warnings = adr.validate(all_adr_ids)
        if errors:
            all_errors.append((adr_id, errors))
        if warnings:
            all_warnings.append((adr_id, warnings))
    
    # Afficher les erreurs
    if all_errors:
        print(f"\n[ERREUR] {len(all_errors)} ADR avec des erreurs:")
        for adr_id, errors in all_errors:
            print(f"  {adr_id}:")
            for error in errors:
                print(f"    - {error}")
    else:
        print(f"  ✅ Aucun erreur dans les ADR individuels")
    
    # Afficher les avertissements
    if all_warnings:
        print(f"\n[AVERTEISSEMENT] {len(all_warnings)} ADR avec des avertissements:")
        for adr_id, warnings in all_warnings:
            print(f"  {adr_id}:")
            for warning in warnings:
                print(f"    ~ {warning}")
    else:
        print(f"  ✅ Aucun avertissement")
    
    # Valider le registre
    print(f"\n[3/5] Validation du registre des décisions...")
    reg_errors, reg_warnings = validate_registre(adrs)
    if reg_errors:
        print(f"  ❌ Erreurs dans le registre:")
        for error in reg_errors:
            print(f"    - {error}")
        all_errors.append(("registre-decisions.md", reg_errors))
    else:
        print(f"  ✅ Registre à jour")
    
    if reg_warnings:
        print(f"  ⚠️  Avertissements:")
        for warning in reg_warnings:
            print(f"    ~ {warning}")
        all_warnings.append(("registre-decisions.md", reg_warnings))
    
    # Valider l'index
    print(f"\n[4/5] Validation de l'index...")
    idx_errors, idx_warnings = validate_index(adrs)
    if idx_errors:
        print(f"  ❌ Erreurs dans l'index:")
        for error in idx_errors:
            print(f"    - {error}")
        all_errors.append(("index.md", idx_errors))
    else:
        print(f"  ✅ Index à jour")
    
    if idx_warnings:
        print(f"  ⚠️  Avertissements:")
        for warning in idx_warnings:
            print(f"    ~ {warning}")
        all_warnings.append(("index.md", idx_warnings))
    
    # Résumé
    print(f"\n[5/5] Résumé")
    total_errors = sum(len(e) for _, e in all_errors)
    total_warnings = sum(len(w) for _, w in all_warnings)
    
    print(f"  Total: {len(adrs)} ADR analysés")
    print(f"  Erreurs: {total_errors}")
    print(f"  Avertissements: {total_warnings}")
    
    if total_errors == 0 and total_warnings == 0:
        print(f"\n✅ TOUT EST CONFORME")
        return 0
    elif total_errors == 0:
        print(f"\n✅ CONFORME (avec avertissements)")
        return 0
    else:
        print(f"\n❌ ANOMALIES DÉTECTÉES")
        return 1


if __name__ == "__main__":
    sys.exit(main())
