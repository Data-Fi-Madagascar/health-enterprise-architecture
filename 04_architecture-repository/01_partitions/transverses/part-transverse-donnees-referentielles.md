---
domain: transverses
id: PART-TRANSVERSE-DONNEES-REFERENTIELLES
type: architecture-partition
niveau: "2"
title: Partition transverse - Données référentielles
status: draft
owner: DEPSI
version: "0.1"
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
# Partition transverse - Données référentielles

## Finalité

Cette partition transverse cadre la production, la publication et la gouvernance des référentiels partagés utilisés par les quatre flux de valeur.

## Périmètre

- Partitions couvertes : [PART-VS-01](../value-streams/part-vs-01.md), [PART-VS-02](../value-streams/part-vs-02.md), [PART-VS-03](../value-streams/part-vs-03.md), [PART-VS-04](../value-streams/part-vs-04.md)
- Niveau TOGAF : enterprise-transversal
- Domaine principal : data
- Etat d'architecture : cible

## Règle de cohérence

Toute évolution de cette partition doit préserver la source d'autorité de chaque référentiel, la traçabilité des versions et la consommation contrôlée par les profils techniques.
