---
domain: transverses
id: PART-TRANSVERSE-ANALYTICS-PILOTAGE
type: architecture-partition
niveau: "2"
title: Partition transverse - Analytics et pilotage
status: draft
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-07
partition_kind: transverse
togaf_repository_section: architecture-landscape
togaf_adm_phase: C
architecture_level: enterprise-transversal
architecture_domain: data
architecture_scope: transverse
architecture_state: target
applies_to: ["PART-VS-01", "PART-VS-02", "PART-VS-03", "PART-VS-04"]
related: []
tags: ["togaf", "partition", "transverse"]
---
# Partition transverse - Analytics et pilotage

## Finalité

Cette partition transverse cadre les mécanismes d'analyse, d'indicateurs, d'exposition de données et de pilotage qui alimentent les décisions nationales et opérationnelles.

## Périmètre

- Partitions couvertes : [PART-VS-01](../value-streams/part-vs-01.md), [PART-VS-02](../value-streams/part-vs-02.md), [PART-VS-03](../value-streams/part-vs-03.md), [PART-VS-04](../value-streams/part-vs-04.md)
- Niveau TOGAF : enterprise-transversal
- Domaine principal : data
- Etat d'architecture : cible

## Règle de cohérence

Toute évolution de cette partition doit distinguer données opérationnelles, données agrégées, indicateurs et produits analytiques, afin de préserver la qualité de pilotage sans fragiliser la confidentialité.
