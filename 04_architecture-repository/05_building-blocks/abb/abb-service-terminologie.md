---
domain: abb
id: ABB-SERVICE-TERMINOLOGIE
type: architecture-building-block
niveau: "2"
title: Service de terminologie et codification communes
status: candidate
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-05
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
maps_to: ["CAP-13", "CAP-14"]
implements: ["ART-2", "ART-4", "ART-5"]
related: ["TERM-CODIFICATION-COMMUNE", "PART-TRANSVERSE-DONNEES-REFERENTIELLES", "STD-0007", "P-INT-01", "P-INT-02", "P-INT-03", "P-INT-04", "P-INT-05", "P-INT-06"]
tags: ["cnisn", "abb", "terminologie", "codification"]
---
# Service de terminologie et codification communes

## Finalité

Permettre aux systèmes de partager des définitions et codifications cohérentes.

## Services attendus

- consultation de systèmes de codes ;
- consultation d'ensembles de valeurs ;
- validation de codes ;
- expansion ;
- recherche de concepts ;
- traduction ;
- publication de correspondances ;
- gestion des versions ;
- dépréciation.

## Principes associés

- [P-INT-01: Autorité désignée](../../02_architecture-elements/motivation/principles/p-int-01.md)
- [P-INT-02: Résolution contre l'autorité](../../02_architecture-elements/motivation/principles/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../../02_architecture-elements/motivation/principles/p-int-03.md)
- [P-INT-04: Historisation des références](../../02_architecture-elements/motivation/principles/p-int-04.md)
- [P-INT-05: Contrat explicite](../../02_architecture-elements/motivation/principles/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../02_architecture-elements/motivation/principles/p-int-06.md)

## Rattachement

- [Terminologie de codification commune](../../02_architecture-elements/data/terminologies/term-codification-commune.md)
- [STD-0007: SNOMED CT](../../../01_cnisn/05_standards/std-0007-snomed-ct.md)
