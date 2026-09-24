---
domain: 04_patterns
id: PAT-QUALITE-RECONCILIATION
type: architecture-pattern
niveau: "2"
title: Pattern qualité et réconciliation
status: candidate
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-11
envelope: 01_cnisn/02_capacites/index.md
togaf_repository_section: reference-library
togaf_adm_phase: C
architecture_level: enterprise-transversal
architecture_domain: data
architecture_scope: interoperability
architecture_state: target
maps_to: ["CAP-13", "CAP-14"]
implements: ["ART-4", "ART-5", "ART-6"]
related: ["ABB-RECONCILIATION-DONNEES"]
tags: ["cnisn", "pattern", "qualite", "reconciliation"]
---
# Pattern qualité et réconciliation

## Finalité

Organiser la détection et le traitement des divergences entre systèmes, référentiels et projections.

## Mécanismes attendus

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

- [P-INT-01: Autorité désignée](../02_architecture-elements/motivation/principles/p-int-01.md)
- [P-INT-02: Résolution contre l'autorité](../02_architecture-elements/motivation/principles/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../02_architecture-elements/motivation/principles/p-int-03.md)
- [P-INT-04: Historisation des références](../02_architecture-elements/motivation/principles/p-int-04.md)
- [P-INT-23: Conformité fondée sur des preuves](../02_architecture-elements/motivation/principles/p-int-23.md)
- [P-INT-24: Applicabilité déclarée](../02_architecture-elements/motivation/principles/p-int-24.md)
- [P-INT-25: Réévaluation continue](../02_architecture-elements/motivation/principles/p-int-25.md)

## Rattachement

- [ABB qualité et réconciliation](../05_building-blocks/abb/abb-reconciliation-donnees.md)
