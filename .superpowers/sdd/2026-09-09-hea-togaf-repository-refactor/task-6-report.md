---
domain: 2026-09-09-hea-togaf-repository-refactor
id: task-6-report
title: Rapport Task 6 - Décomposition des CAP-INT CNISN
version: 1.0.0
status: stable
last_reviewed: 2026-09-10
owner: Codex
tags:
  - togaf
  - cnisn
  - architecture-repository
---

# Rapport Task 6 - Décomposition des CAP-INT CNISN

## 1. Objet

La Task 6 remplace les anciens objets `CAP-INT-*` par des objets d'architecture TOGAF de nature explicite. Les fichiers historiques `04_architecture-repository/capacites/cap-int-*.md` sont conservés pour la Task 7, mais ils ne sont plus rendus dans l'enveloppe CNISN active.

Cette approche maintient la traçabilité par `legacy_id` sans présenter les nouveaux objets comme des capacités. Les capacités canoniques restent les `CAP-*` du CAESN.

## 2. Changements réalisés

Le fichier `04_architecture-repository/00_metamodel/cap-int-migration.yaml` a été créé pour définir la correspondance de migration entre les 16 anciens `CAP-INT-*`, les objets de remplacement, l'objet primaire et les `CAP-*` CAESN concernés.

La vue statique `04_architecture-repository/08_views/togaf/cap-int-migration.md` a été créée pour exposer cette migration sous forme lisible. Elle n'est pas traitée comme enveloppe générée afin d'éviter un conflit avec les marqueurs `BEGIN:GENERATED`.

Les objets de remplacement ont été créés dans les familles TOGAF appropriées:

| Famille | Objets créés |
|---------|--------------|
| ABB | `ABB-IDENTITE-BENEFICIAIRE`, `ABB-REGISTRE-PROFESSIONNELS`, `ABB-ECHANGE-MEDIATION`, `ABB-REFERENTIEL-STRUCTURES-SERVICES`, `ABB-SERVICE-TERMINOLOGIE`, `ABB-CATALOGUE-CONTRATS`, `ABB-EXPOSITION-DONNEES-ANALYTIQUES`, `ABB-CONFIANCE-AUTORISATION`, `ABB-GESTION-CONSENTEMENT`, `ABB-AUDIT-PROVENANCE`, `ABB-RECONCILIATION-DONNEES`, `ABB-ECHANGE-LOGISTIQUE-LMIS` |
| Patterns | `PAT-ECHANGE-MEDIATION`, `PAT-QUALITE-RECONCILIATION`, `PAT-ECHANGE-INTERNATIONAL-IPS` |
| Références de données et terminologie | `RD-STRUCTURES-SERVICES`, `RD-DONNEES-ENVIRONNEMENTALES-CLIMAT`, `TERM-CODIFICATION-COMMUNE` |
| Gouvernance et preuves | `AC-CATALOGUE-SERVICES`, `COMP-HOMOLOGATION-INTEROPERABILITE`, `EVID-TESTS-INTEROPERABILITE` |
| Exigences | `REQ-TF-01` à `REQ-TF-08`, `REQ-OH-01` à `REQ-OH-07` |

Chaque nouvel objet porte un frontmatter valide avec `legacy_id`, métadonnées TOGAF, `maps_to` vers les capacités CAESN, `envelope: 01_cnisn/02_capacites/index.md` et relations non isolées.

## 3. Enveloppe CNISN

Le chapitre `01_cnisn/02_capacites/index.md` a été réorienté vers les objets d'interopérabilité requis. Il explique que les anciens `CAP-INT-*` sont des bundles de migration historiques et rend désormais les nouveaux objets d'architecture, les partitions associées et les exigences.

Les anciens fichiers `04_architecture-repository/capacites/cap-int-*.md` sont conservés, mais leur rattachement `envelope` a été retiré pour éviter qu'ils soient publiés comme objets actifs dans ce chapitre.

## 4. Génération et validation

Les générateurs ont été adaptés pour prendre en compte la vue statique de migration et les références externes `STD-*` et `ADR-*` utilisées dans les relations:

| Script | Adaptation |
|--------|------------|
| `scripts/build_ref_index.py` | Exclusion de la vue statique `cap-int-migration.md` de l'index d'objets. |
| `scripts/build_wrappers.py` | Exclusion de cette vue statique de la génération d'enveloppes. |
| `scripts/validate_ref.py` | Reconnaissance des identifiants relationnels externes issus de `01_cnisn/05_standards` et `01_cnisn/06_decisions`. |
| `04_architecture-repository/08_views/togaf/reference-library.md` | Inclusion des objets ABB et patterns situés directement dans les dossiers concernés. |

Les artefacts générés ont été régénérés:

| Commande | Résultat |
|----------|----------|
| `python3 scripts/build_ref_index.py` | `04_architecture-repository/_index.yaml` généré. |
| `python3 scripts/build_wrappers.py` | `109 enveloppes écrites`. |
| `python3 scripts/build_mintlify.py` | Artefact Mintlify CNISN régénéré. |

## 5. Résultats de validation

| Commande | Résultat |
|----------|----------|
| `python3 scripts/build_ref_index.py --check` | OK, index à jour. |
| `python3 scripts/build_wrappers.py --check` | OK, `109 enveloppes à jour`. |
| `python3 scripts/validate_ref.py` | CONFORME, `385` objets indexés, `6157` liens relatifs vérifiés, aucune relation isolée. |
| `make check` | OK. Inclut index, enveloppes, liens, manifestes, référentiel, RDF/SHACL, FHIR, graphify sync, JSON Schema, OpenAPI, ODA, gouvernance et Mintlify. |

Le validateur signale encore quatre avertissements préexistants sur les profils `PT-14` et `PT-15`, qui pointent directement vers `CAP-*`. Ces avertissements n'empêchent pas le statut `CONFORME` et ne relèvent pas de la Task 6.

## 6. Exclusions

La modification préexistante de `.gitignore` a été laissée hors périmètre. Les dossiers `graphify-out/` et `.obsidian/` n'ont pas été inclus dans les changements de la Task 6.
