---
domain: abb
id: ABB-REFERENTIEL-STRUCTURES-SERVICES
type: architecture-building-block
niveau: "2"
title: Référentiel des structures et services de santé
status: candidate
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-04
envelope: 01_cnisn/02_capacites/index.md
building_block_role: ABB
building_block_domain: data
togaf_repository_section: reference-library
togaf_adm_phase: C
architecture_level: enterprise-transversal
architecture_domain: data
architecture_scope: interoperability
architecture_state: target
partitions: ["PART-TRANSVERSE-DONNEES-REFERENTIELLES"]
maps_to: ["CAP-11", "CAP-13", "CAP-14"]
implements: ["ART-4", "ART-5", "ART-6"]
related: ["RD-STRUCTURES-SERVICES", "PART-TRANSVERSE-DONNEES-REFERENTIELLES", "DO-23", "P-INT-01", "P-INT-02", "P-INT-03", "P-INT-04"]
tags: ["cnisn", "abb", "referentiel", "structures"]
---
# Référentiel des structures et services de santé

## Finalité

Fournir une autorité commune sur :

- les formations sanitaires ;
- les structures communautaires ;
- les laboratoires ;
- les services de santé ;
- les rattachements ;
- les localisations ;
- les périodes d'activité.

## Services attendus

- recherche ;
- consultation ;
- résolution d'identifiants ;
- historique ;
- synchronisation ;
- publication ;
- gestion des correspondances ;
- vérification de validité.

## Principes associés

- [P-INT-01: Autorité désignée](../../02_architecture-elements/motivation/principles/p-int-01.md)
- [P-INT-02: Résolution contre l'autorité](../../02_architecture-elements/motivation/principles/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../../02_architecture-elements/motivation/principles/p-int-03.md)
- [P-INT-04: Historisation des références](../../02_architecture-elements/motivation/principles/p-int-04.md)

## Rattachement

- [Données de référence des structures et services](../../02_architecture-elements/data/reference-data/rd-structures-services.md)
- [Partition transverse - Données référentielles](../../01_partitions/transverses/part-transverse-donnees-referentielles.md)
