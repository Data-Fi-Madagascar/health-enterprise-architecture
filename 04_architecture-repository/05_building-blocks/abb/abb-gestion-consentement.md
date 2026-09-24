---
domain: abb
id: ABB-GESTION-CONSENTEMENT
type: architecture-building-block
niveau: "2"
title: Gestion des consentements et bases d'autorisation
status: candidate
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-09
envelope: 01_cnisn/02_capacites/index.md
building_block_role: ABB
building_block_domain: data
togaf_repository_section: reference-library
togaf_adm_phase: C
architecture_level: enterprise-transversal
architecture_domain: data
architecture_scope: interoperability
architecture_state: target
partitions: ["PART-TRANSVERSE-SECURITE-CONFIANCE"]
maps_to: ["CAP-15", "CAP-17"]
implements: ["ART-0", "ART-4B", "ART-7", "ART-11"]
related: ["PART-TRANSVERSE-SECURITE-CONFIANCE", "P-INT-14", "P-INT-15", "P-INT-16", "P-INT-17"]
tags: ["cnisn", "abb", "consentement", "autorisation"]
---
# Gestion des consentements et bases d'autorisation

## Finalité

Permettre de déterminer et de prouver la base autorisant un traitement ou un accès.

## Services attendus

- enregistrement d'une base d'autorisation ;
- consultation ;
- vérification ;
- gestion des finalités ;
- gestion des périodes ;
- retrait lorsque applicable ;
- preuve ;
- application des politiques ;
- traçabilité des décisions.

## Principe

Le consentement est une base possible parmi plusieurs bases légales ou fonctionnelles.

## Principes associés

- [P-INT-14: Base d'autorisation explicite](../../02_architecture-elements/motivation/principles/p-int-14.md)
- [P-INT-15: Limitation à la finalité](../../02_architecture-elements/motivation/principles/p-int-15.md)
- [P-INT-16: Résidence et non-réplication](../../02_architecture-elements/motivation/principles/p-int-16.md)
- [P-INT-17: Minimisation](../../02_architecture-elements/motivation/principles/p-int-17.md)

## Rattachement

- [Partition transverse - Sécurité et confiance](../../01_partitions/transverses/part-transverse-securite-confiance.md)
- [ART-4B: Bases d'autorisation](../../04_patterns/artsn-rules/art-4b.md)
