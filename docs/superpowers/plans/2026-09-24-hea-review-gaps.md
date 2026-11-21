---
domain: plans
id: hea-review-gaps-plan
title: Plan de correction des gaps de revue HEA
version: "1.0"
status: active
last_reviewed: 2026-09-24
owner: DEPSI
tags: ["hea", "validation", "togaf", "mappings"]
---

# HEA Review Gaps Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Corriger le pipeline, formaliser le métamodèle TOGAF, réparer les mappings hérités et générer une vue de traçabilité par partition.

**Architecture:** `04_architecture-repository` demeure la source canonique. `scripts/validate_ref.py` contrôle les relations et leurs types, tandis que `scripts/build_wrappers.py` produit les vues et enveloppes dérivées de manière déterministe.

**Tech Stack:** Python 3, `unittest`, Markdown avec frontmatter YAML, Make.

**Spec:** `docs/superpowers/specs/2026-09-24-hea-review-gaps-design.md`

## Global Constraints

- Conserver `REL_DIRS = [ARCH_REPOSITORY_DIR]` et `ADR_DIRS = ["01_cnisn/06_decisions"]`.
- Utiliser uniquement `draft|active|stable|candidate|deprecated` pour les statuts.
- Ne jamais éditer manuellement le contenu interne des blocs `BEGIN:GENERATED`.
- Régénérer les enveloppes après toute modification des sources canoniques.
- Exclure `graphify-out/` et `.obsidian/` des commits.
- Terminer par un `make check` complet avec code de sortie nul.

### Task 1: Réparer le validateur et rétablir une base exécutable

**Files:**
- Create: `tests/test_validate_ref.py`
- Modify: `scripts/validate_ref.py`
- Regenerate: artefacts signalés par `scripts/build_wrappers.py --check`

**Interfaces:**
- Consumes: constantes de configuration du validateur.
- Produces: module Python importable, `REL_DIRS` canonique et découverte des ADR active.

- [ ] **Step 1: écrire le test de régression qui lit `scripts/validate_ref.py`, interdit `<<<<<<<`, `=======`, `>>>>>>>`, importe le module et vérifie les deux constantes.**
- [ ] **Step 2: exécuter `python3 -m unittest tests.test_validate_ref.ValidatorConfigurationTests -v` et constater l'échec d'import causé par les marqueurs.**
- [ ] **Step 3: supprimer uniquement les marqueurs et la branche `REL_DIRS = ["referentiel"]`, puis placer `ADR_DIRS` après `REL_DIRS`.**
- [ ] **Step 4: exécuter le test ciblé, puis `python3 scripts/build_wrappers.py` et `python3 scripts/validate_ref.py`.**
- [ ] **Step 5: committer avec `fix: restore repository validation pipeline`.**

### Task 2: Formaliser et contrôler les relations de partition

**Files:**
- Modify: `tests/test_validate_ref.py`
- Modify: `scripts/validate_ref.py`
- Modify: `04_architecture-repository/00_metamodel/schema.md`

**Interfaces:**
- Consumes: `load_relation_graph()` et les champs de relation du frontmatter.
- Produces: `check_partition_relation_types(objects)` retournant des tuples `(file, source_id, target_id, message)` et intégration de `partitions` dans `RELATION_KEYS`.

- [ ] **Step 1: ajouter un test où `partitions: ["PART-VS-01"]` est accepté lorsque la cible est `architecture-partition`, et un test où une cible `capabilite` produit une erreur typée.**
- [ ] **Step 2: exécuter les tests et constater l'échec dû à l'absence de relation typée.**
- [ ] **Step 3: conserver les relations par clé dans les objets chargés, ajouter `partitions` aux relations et implémenter le contrôle de type.**
- [ ] **Step 4: intégrer les erreurs dans `main()` et documenter les onze champs TOGAF dans le tableau des champs du schéma.**
- [ ] **Step 5: exécuter les tests, `python3 scripts/validate_ref.py` et `python3 scripts/build_wrappers.py --check`, puis committer avec `feat: formalize TOGAF partition metadata`.**

### Task 3: Corriger les mappings sémantiques hérités

**Files:**
- Modify: `04_architecture-repository/05_building-blocks/abb/legacy-services/srv-03.md` à `srv-06.md`
- Modify: `04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-01.md`
- Modify: `04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-10.md`, `cmp-11.md`, `cmp-12.md`, `cmp-14.md`, `cmp-23.md`
- Regenerate: `02_artsn/`, `03_ptisn/` et vues TOGAF concernées

**Interfaces:**
- Consumes: responsabilités métier décrites dans chaque fiche et ABB canoniques existants.
- Produces: relations `maps_to` ou `realizes` alignées sur la responsabilité principale, avec prose et liens cohérents.

- [ ] **Step 1: ajouter des assertions de mapping attendues dans `tests/test_validate_ref.py` pour chaque objet ciblé.**
- [ ] **Step 2: exécuter ces assertions et constater les mappings erronés actuels.**
- [ ] **Step 3: remapper SRV-03 vers `ABB-SERVICE-TERMINOLOGIE`, SRV-04 et PT-01 vers `ABB-ECHANGE-MEDIATION`, SRV-05 vers `ABB-ECHANGE-LOGISTIQUE-LMIS`, SRV-06 vers `ABB-EXPOSITION-DONNEES-ANALYTIQUES`.**
- [ ] **Step 4: remapper CMP-10, CMP-11, CMP-12, CMP-14 et CMP-23 selon leur fonction, puis ajuster les liens narratifs sans remplacement global.**
- [ ] **Step 5: régénérer les enveloppes, vérifier la matrice PTISN, exécuter le validateur et committer avec `fix: align legacy mappings with canonical ABBs`.**

### Task 4: Générer la vue de traçabilité par partition

**Files:**
- Create: `tests/test_partition_view.py`
- Modify: `scripts/build_wrappers.py`
- Create: `04_architecture-repository/08_views/togaf/partition-traceability.md`
- Modify: `scripts/validate_ref.py`

**Interfaces:**
- Consumes: objets chargés par `load_objects()` et relations canoniques.
- Produces: `render_partition_traceability(objects, path_by_id, to_dir)` et mode de bloc `partition-traceability`.

- [ ] **Step 1: écrire un test synthétique exigeant une ligne ou section contenant `PART-VS-01`, `VS-01`, une `CAP`, un `PRC` et au moins une cible `DO`, `ABB` ou `SBB`.**
- [ ] **Step 2: exécuter le test et constater l'absence du moteur de rendu.**
- [ ] **Step 3: charger le type et `partitions`, parcourir le graphe dans le sens canonique et produire un tableau déterministe par partition.**
- [ ] **Step 4: ajouter la vue avec un bloc généré, l'enregistrer parmi les documents dérivés et régénérer toutes les enveloppes.**
- [ ] **Step 5: exécuter le test ciblé, `python3 scripts/build_wrappers.py --check`, `python3 scripts/validate_ref.py`, puis committer avec `feat: add partition traceability view`.**

### Task 5: Validation finale et PR

**Files:**
- Modify only if required by failing checks: generated artefacts within the declared scope.

**Interfaces:**
- Consumes: quatre lots commités.
- Produces: branche poussée et PR non fusionnée.

- [ ] **Step 1: exécuter `python3 -m unittest discover -s tests -v`.**
- [ ] **Step 2: exécuter `make check`, lire l'intégralité du résultat et corriger toute dérive dans son lot d'origine.**
- [ ] **Step 3: exécuter `git diff --check`, vérifier l'absence de `graphify-out/` et `.obsidian/`, puis pousser la branche.**
- [ ] **Step 4: ouvrir la PR avec des sections P0, P1, mappings corrigés, validations et ambiguïtés restantes, sans fusionner.**
