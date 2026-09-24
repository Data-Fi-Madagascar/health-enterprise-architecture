---
domain: abb
id: ABB-RECONCILIATION-DONNEES
type: architecture-building-block
niveau: "2"
title: Qualité et réconciliation des données
status: candidate
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-11
envelope: 01_cnisn/02_capacites/index.md
building_block_role: ABB
building_block_domain: data
togaf_repository_section: reference-library
togaf_adm_phase: C
architecture_level: enterprise-transversal
architecture_domain: data
architecture_scope: interoperability
architecture_state: target
partitions: ["PART-TRANSVERSE-INTEROPERABILITE"]
maps_to: ["CAP-13", "CAP-14"]
implements: ["ART-4", "ART-5", "ART-6"]
related: ["PAT-QUALITE-RECONCILIATION", "PART-TRANSVERSE-INTEROPERABILITE", "P-INT-01", "P-INT-02", "P-INT-03", "P-INT-04", "P-INT-05", "P-INT-06", "P-INT-07", "P-INT-08", "P-INT-09", "P-INT-23", "P-INT-24", "P-INT-25"]
tags: ["cnisn", "abb", "qualite", "reconciliation"]
---
# Qualité et réconciliation des données

## Finalité

Permettre de détecter et traiter les divergences entre systèmes, référentiels et projections.

## Services attendus

- validation de contrats ;
- contrôle des métadonnées ;
- détection des messages manquants ;
- comparaison de versions ;
- comparaison de valeurs ;
- détection des doublons ;
- suivi des anomalies ;
- déclenchement de corrections ;
- publication d'indicateurs de qualité.

## Principes associés

- [P-INT-01: Autorité désignée](../../02_architecture-elements/motivation/principles/p-int-01.md)
- [P-INT-02: Résolution contre l'autorité](../../02_architecture-elements/motivation/principles/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../../02_architecture-elements/motivation/principles/p-int-03.md)
- [P-INT-04: Historisation des références](../../02_architecture-elements/motivation/principles/p-int-04.md)
- [P-INT-05: Contrat explicite](../../02_architecture-elements/motivation/principles/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../02_architecture-elements/motivation/principles/p-int-06.md)
- [P-INT-07: Responsabilité de la donnée](../../02_architecture-elements/motivation/principles/p-int-07.md)
- [P-INT-08: Publication au catalogue des services](../../02_architecture-elements/motivation/principles/p-int-08.md)
- [P-INT-09: Publication des contrats](../../02_architecture-elements/motivation/principles/p-int-09.md)
- [P-INT-23: Conformité fondée sur des preuves](../../02_architecture-elements/motivation/principles/p-int-23.md)
- [P-INT-24: Applicabilité déclarée](../../02_architecture-elements/motivation/principles/p-int-24.md)
- [P-INT-25: Réévaluation continue](../../02_architecture-elements/motivation/principles/p-int-25.md)

## Rattachement

- [Pattern qualité et réconciliation](../../04_patterns/pat-qualite-reconciliation.md)
- [Partition transverse - Interopérabilité](../../01_partitions/transverses/part-transverse-interoperabilite.md)
