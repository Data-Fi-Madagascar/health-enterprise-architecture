---
domain: transverses
id: PART-TRANSVERSE-IDENTITE
type: architecture-partition
niveau: "2"
title: Partition transverse - Identité
status: draft
owner: DEPSI
version: "0.1"
legacy_id: ["CAP-INT-01", "CAP-INT-02"]
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
# Partition transverse - Identité

## Finalité

Cette partition transverse cadre les objets, référentiels et mécanismes d'identité utilisés par les quatre flux de valeur. Elle garantit que la résolution d'identité demeure commune sans imposer une concentration non maîtrisée des données.

## Périmètre

- Partitions couvertes : [PART-VS-01](../value-streams/part-vs-01.md), [PART-VS-02](../value-streams/part-vs-02.md), [PART-VS-03](../value-streams/part-vs-03.md), [PART-VS-04](../value-streams/part-vs-04.md)
- Niveau TOGAF : enterprise-transversal
- Domaine principal : data
- Etat d'architecture : cible

## Règle de cohérence

Toute évolution de cette partition doit préserver l'unicité fonctionnelle de l'identité, la séparation des responsabilités de gouvernance et la compatibilité avec les profils d'identification nationaux.
