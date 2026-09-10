---
domain: 04_patterns
id: PAT-ECHANGE-MEDIATION
type: architecture-pattern
niveau: "2"
title: Pattern d'échange et médiation
status: candidate
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-03
envelope: 01_cnisn/02_capacites/index.md
togaf_repository_section: reference-library
togaf_adm_phase: C
architecture_level: enterprise-transversal
architecture_domain: application
architecture_scope: interoperability
architecture_state: target
maps_to: ["CAP-13", "CAP-14", "CAP-18"]
implements: ["ART-1", "ART-2", "F-3"]
related: ["ABB-ECHANGE-MEDIATION"]
tags: ["cnisn", "pattern", "echange", "mediation"]
---
# Pattern d'échange et médiation

## Finalité

Structurer la transmission, la réception, la transformation et l'acheminement de données ou commandes entre systèmes de manière gouvernée.

## Mécanismes attendus

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

- [P-INT-05: Contrat explicite](../02_architecture-elements/motivation/principles/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../02_architecture-elements/motivation/principles/p-int-06.md)
- [P-INT-07: Responsabilité de la donnée](../02_architecture-elements/motivation/principles/p-int-07.md)
- [P-INT-08: Publication au catalogue des services](../02_architecture-elements/motivation/principles/p-int-08.md)
- [P-INT-09: Publication des contrats](../02_architecture-elements/motivation/principles/p-int-09.md)
- [P-INT-10: Accord préalable](../02_architecture-elements/motivation/principles/p-int-10.md)
- [P-INT-18: Traçabilité différenciée](../02_architecture-elements/motivation/principles/p-int-18.md)

## Rattachement

- [ABB échange et médiation](../05_building-blocks/abb/abb-echange-mediation.md)
- [Partition transverse - Interopérabilité](../01_partitions/transverses/part-transverse-interoperabilite.md)
