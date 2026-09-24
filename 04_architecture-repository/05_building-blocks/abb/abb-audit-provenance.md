---
domain: abb
id: ABB-AUDIT-PROVENANCE
type: architecture-building-block
niveau: "2"
title: Provenance, audit et traçabilité
status: candidate
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-10
envelope: 01_cnisn/02_capacites/index.md
building_block_role: ABB
building_block_domain: application
togaf_repository_section: reference-library
togaf_adm_phase: C
architecture_level: enterprise-transversal
architecture_domain: application
architecture_scope: interoperability
architecture_state: target
partitions: ["PART-TRANSVERSE-SECURITE-CONFIANCE"]
maps_to: ["CAP-03", "CAP-08", "CAP-12", "CAP-13", "CAP-15"]
implements: ["ART-3", "ART-7", "ART-9", "F-1", "F-5", "F-6"]
related: ["PART-TRANSVERSE-SECURITE-CONFIANCE", "P-INT-07", "P-INT-17", "P-INT-18", "P-INT-23"]
tags: ["cnisn", "abb", "audit", "provenance"]
---
# Provenance, audit et traçabilité

## Finalité

Permettre de comprendre :

- l'origine d'une donnée ;
- les transformations appliquées ;
- les accès effectués ;
- les décisions prises ;
- les opérations techniques liées.

## Services attendus

- conservation de la provenance ;
- audit des accès ;
- audit des exports ;
- audit des opérations administratives ;
- corrélation de bout en bout ;
- consultation autorisée des traces ;
- politiques de conservation différenciées.

## Principes associés

- [P-INT-07: Responsabilité de la donnée](../../02_architecture-elements/motivation/principles/p-int-07.md)
- [P-INT-17: Minimisation](../../02_architecture-elements/motivation/principles/p-int-17.md)
- [P-INT-18: Traçabilité différenciée](../../02_architecture-elements/motivation/principles/p-int-18.md)
- [P-INT-23: Conformité fondée sur des preuves](../../02_architecture-elements/motivation/principles/p-int-23.md)

## Rattachement

- [Partition transverse - Sécurité et confiance](../../01_partitions/transverses/part-transverse-securite-confiance.md)
- [ART-9: Garanties transactionnelles fortes](../../04_patterns/artsn-rules/art-9.md)
