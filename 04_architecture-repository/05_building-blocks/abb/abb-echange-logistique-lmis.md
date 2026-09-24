---
domain: abb
id: ABB-ECHANGE-LOGISTIQUE-LMIS
type: architecture-building-block
niveau: "2"
title: Échange logistique LMIS
status: candidate
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-15
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
maps_to: ["CAP-06", "CAP-10", "CAP-11"]
implements: ["ART-10"]
related: ["CMP-23", "ENF-2", "PART-TRANSVERSE-INTEROPERABILITE", "P-INT-03", "P-INT-07", "P-INT-18"]
tags: ["cnisn", "abb", "lmis", "logistique"]
---
# Échange logistique LMIS

## Finalité

Permettre l'interopérabilité des données de la chaîne d'approvisionnement sanitaire (médicaments, vaccins, intrants, équipements) : catalogue produit partagé, niveaux de stock, lots et traçabilité des mouvements, afin d'éviter les ruptures et les péremptions.

## Services attendus

- catalogue produit normalisé (désignation, code, unité, seuils) ;
- remontée des niveaux de stock par établissement ;
- traçabilité des lots et des mouvements (réception, transfert, distribution) ;
- alerte de rupture et de péremption ;
- corrélation stock vers consommation vers épidémiologie.

## Principe de séparation

Ce bloc normalise l'échange et la traçabilité inter-initiatives. Il ne remplace pas le système métier de gestion des stocks.

## Principes associés

- [P-INT-03: Copies locales non autoritatives](../../02_architecture-elements/motivation/principles/p-int-03.md)
- [P-INT-07: Responsabilité de la donnée](../../02_architecture-elements/motivation/principles/p-int-07.md)
- [P-INT-18: Traçabilité différenciée](../../02_architecture-elements/motivation/principles/p-int-18.md)

## Rattachement

- [CMP-23: Chaîne logistique LMIS](legacy-components/cmp-23.md)
- [ART-10: Logistique](../../04_patterns/artsn-rules/art-10.md)
