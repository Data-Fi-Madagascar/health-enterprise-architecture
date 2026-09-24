---
domain: abb
id: ABB-CONFIANCE-AUTORISATION
type: architecture-building-block
niveau: "2"
title: Confiance, sécurité et autorisation
status: candidate
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-08
envelope: 01_cnisn/02_capacites/index.md
building_block_role: ABB
building_block_domain: technology
togaf_repository_section: reference-library
togaf_adm_phase: D
architecture_level: enterprise-transversal
architecture_domain: technology
architecture_scope: interoperability
architecture_state: target
partitions: ["PART-TRANSVERSE-SECURITE-CONFIANCE"]
maps_to: ["CAP-15"]
implements: ["ART-0", "ART-4B", "ART-7", "ART-9"]
related: ["PART-TRANSVERSE-SECURITE-CONFIANCE", "P-INT-14", "P-INT-15", "P-INT-16", "P-INT-17", "P-INT-18", "P-INT-19", "P-INT-20"]
tags: ["cnisn", "abb", "securite", "autorisation"]
---
# Confiance, sécurité et autorisation

## Finalité

Fournir les mécanismes nécessaires à l'identification, l'authentification, l'autorisation et la protection des échanges.

## Services attendus

- authentification des utilisateurs ;
- authentification des systèmes ;
- identité des organisations ;
- gestion des rôles ;
- gestion des attributs ;
- décision d'autorisation ;
- gestion des comptes techniques ;
- révocation ;
- gestion des secrets et certificats ;
- journalisation ;
- gestion des incidents.

## Principes associés

- [P-INT-14: Base d'autorisation explicite](../../02_architecture-elements/motivation/principles/p-int-14.md)
- [P-INT-15: Limitation à la finalité](../../02_architecture-elements/motivation/principles/p-int-15.md)
- [P-INT-16: Résidence et non-réplication](../../02_architecture-elements/motivation/principles/p-int-16.md)
- [P-INT-17: Minimisation](../../02_architecture-elements/motivation/principles/p-int-17.md)
- [P-INT-18: Traçabilité différenciée](../../02_architecture-elements/motivation/principles/p-int-18.md)
- [P-INT-19: Neutralité technologique](../../02_architecture-elements/motivation/principles/p-int-19.md)
- [P-INT-20: Portabilité et réversibilité](../../02_architecture-elements/motivation/principles/p-int-20.md)

## Rattachement

- [Partition transverse - Sécurité et confiance](../../01_partitions/transverses/part-transverse-securite-confiance.md)
- [ART-7: Sécurité, contrôle d'accès et résidence de la donnée](../../04_patterns/artsn-rules/art-7.md)
