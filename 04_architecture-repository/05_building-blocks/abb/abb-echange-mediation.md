---
domain: abb
id: ABB-ECHANGE-MEDIATION
type: architecture-building-block
niveau: "2"
title: Échange et médiation inter-systèmes
status: candidate
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-03
envelope: 01_cnisn/02_capacites/index.md
building_block_role: ABB
building_block_domain: application
togaf_repository_section: reference-library
togaf_adm_phase: C
architecture_level: enterprise-transversal
architecture_domain: application
architecture_scope: interoperability
architecture_state: target
partitions: ["PART-TRANSVERSE-INTEROPERABILITE"]
maps_to: ["CAP-13", "CAP-14", "CAP-18"]
implements: ["ART-1", "ART-2", "F-3"]
related: ["PAT-ECHANGE-MEDIATION", "PART-TRANSVERSE-INTEROPERABILITE", "P-INT-05", "P-INT-06", "P-INT-07", "P-INT-08", "P-INT-09", "P-INT-10", "P-INT-11", "P-INT-12", "P-INT-13", "P-INT-18", "P-INT-19", "P-INT-20", "P-INT-21", "P-INT-22", "P-INT-23", "P-INT-24", "P-INT-25"]
tags: ["cnisn", "abb", "interoperabilite", "mediation"]
---
# Échange et médiation inter-systèmes

## Finalité

Permettre aux systèmes de transmettre, recevoir, transformer et acheminer des données ou commandes de manière gouvernée.

## Services attendus

- réception ;
- publication ;
- interrogation ;
- notification ;
- synchronisation ;
- routage ;
- transformation ;
- validation ;
- gestion des erreurs ;
- corrélation ;
- réconciliation ;
- intégration sortante.

## Principes associés

- [P-INT-05: Contrat explicite](../../02_architecture-elements/motivation/principles/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../02_architecture-elements/motivation/principles/p-int-06.md)
- [P-INT-07: Responsabilité de la donnée](../../02_architecture-elements/motivation/principles/p-int-07.md)
- [P-INT-08: Publication au catalogue des services](../../02_architecture-elements/motivation/principles/p-int-08.md)
- [P-INT-09: Publication des contrats](../../02_architecture-elements/motivation/principles/p-int-09.md)
- [P-INT-10: Accord préalable](../../02_architecture-elements/motivation/principles/p-int-10.md)
- [P-INT-11: Arbitrage des conflits d'autorité](../../02_architecture-elements/motivation/principles/p-int-11.md)
- [P-INT-12: Dérogation explicite](../../02_architecture-elements/motivation/principles/p-int-12.md)
- [P-INT-13: Dérogation d'urgence](../../02_architecture-elements/motivation/principles/p-int-13.md)
- [P-INT-18: Traçabilité différenciée](../../02_architecture-elements/motivation/principles/p-int-18.md)
- [P-INT-19: Neutralité technologique](../../02_architecture-elements/motivation/principles/p-int-19.md)
- [P-INT-20: Portabilité et réversibilité](../../02_architecture-elements/motivation/principles/p-int-20.md)
- [P-INT-21: Progressivité](../../02_architecture-elements/motivation/principles/p-int-21.md)
- [P-INT-22: Fonctionnement en connectivité contrainte](../../02_architecture-elements/motivation/principles/p-int-22.md)
- [P-INT-23: Conformité fondée sur des preuves](../../02_architecture-elements/motivation/principles/p-int-23.md)
- [P-INT-24: Applicabilité déclarée](../../02_architecture-elements/motivation/principles/p-int-24.md)
- [P-INT-25: Réévaluation continue](../../02_architecture-elements/motivation/principles/p-int-25.md)

## Rattachement

- [Pattern d'échange et médiation](../../04_patterns/pat-echange-mediation.md)
- [Partition transverse - Interopérabilité](../../01_partitions/transverses/part-transverse-interoperabilite.md)
