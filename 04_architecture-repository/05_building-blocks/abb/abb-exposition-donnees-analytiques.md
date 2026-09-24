---
domain: abb
id: ABB-EXPOSITION-DONNEES-ANALYTIQUES
type: architecture-building-block
niveau: "2"
title: Accès et exposition des données analytiques
status: candidate
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-07
envelope: 01_cnisn/02_capacites/index.md
building_block_role: ABB
building_block_domain: data
togaf_repository_section: reference-library
togaf_adm_phase: C
architecture_level: enterprise-transversal
architecture_domain: data
architecture_scope: interoperability
architecture_state: target
partitions: ["PART-TRANSVERSE-ANALYTICS-PILOTAGE"]
maps_to: ["CAP-05", "CAP-13"]
implements: ["ART-3", "ART-5", "ART-6", "ART-7"]
related: ["PART-TRANSVERSE-ANALYTICS-PILOTAGE", "P-INT-05", "P-INT-06", "P-INT-07", "P-INT-08", "P-INT-09", "P-INT-17", "P-INT-18", "P-INT-19", "P-INT-20", "P-INT-21", "P-INT-22", "P-INT-23", "P-INT-24", "P-INT-25"]
tags: ["cnisn", "abb", "analytique", "donnees"]
---
# Accès et exposition des données analytiques

## Finalité

Permettre l'accès gouverné aux données et indicateurs destinés à la décision, sans imposer une charge excessive aux systèmes opérationnels.

## Services attendus

- publication d'indicateurs ;
- consultation de données agrégées ;
- publication de métadonnées analytiques ;
- accès aux modèles validés ;
- exposition de données historiques ;
- publication de la qualité ;
- export contrôlé ;
- catalogue des données disponibles.

## Limite de portée

Cet ABB concerne l'exposition et l'accès interopérables.

La conception interne des entrepôts, projections et modèles analytiques relève de l'ARTSN et des architectures propres aux initiatives.

## Principes associés

- [P-INT-05: Contrat explicite](../../02_architecture-elements/motivation/principles/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../02_architecture-elements/motivation/principles/p-int-06.md)
- [P-INT-07: Responsabilité de la donnée](../../02_architecture-elements/motivation/principles/p-int-07.md)
- [P-INT-08: Publication au catalogue des services](../../02_architecture-elements/motivation/principles/p-int-08.md)
- [P-INT-09: Publication des contrats](../../02_architecture-elements/motivation/principles/p-int-09.md)
- [P-INT-17: Minimisation](../../02_architecture-elements/motivation/principles/p-int-17.md)
- [P-INT-18: Traçabilité différenciée](../../02_architecture-elements/motivation/principles/p-int-18.md)
- [P-INT-19: Neutralité technologique](../../02_architecture-elements/motivation/principles/p-int-19.md)
- [P-INT-20: Portabilité et réversibilité](../../02_architecture-elements/motivation/principles/p-int-20.md)
- [P-INT-21: Progressivité](../../02_architecture-elements/motivation/principles/p-int-21.md)
- [P-INT-22: Fonctionnement en connectivité contrainte](../../02_architecture-elements/motivation/principles/p-int-22.md)
- [P-INT-23: Conformité fondée sur des preuves](../../02_architecture-elements/motivation/principles/p-int-23.md)
- [P-INT-24: Applicabilité déclarée](../../02_architecture-elements/motivation/principles/p-int-24.md)
- [P-INT-25: Réévaluation continue](../../02_architecture-elements/motivation/principles/p-int-25.md)

## Rattachement

- [Partition transverse - Analytics et pilotage](../../01_partitions/transverses/part-transverse-analytics-pilotage.md)
- [ART-6: Analytique et restitution](../../04_patterns/artsn-rules/art-6.md)
