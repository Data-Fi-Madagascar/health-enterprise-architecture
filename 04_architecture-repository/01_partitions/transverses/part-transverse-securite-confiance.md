---
domain: transverses
id: PART-TRANSVERSE-SECURITE-CONFIANCE
type: architecture-partition
niveau: "2"
title: Partition transverse - Sécurité et confiance
status: draft
owner: DEPSI
version: "0.1"
partition_kind: transverse
togaf_repository_section: architecture-landscape
togaf_adm_phase: D
architecture_level: enterprise-transversal
architecture_domain: technology
architecture_scope: transverse
architecture_state: target
applies_to: ["PART-VS-01", "PART-VS-02", "PART-VS-03", "PART-VS-04"]
related: []
tags: ["togaf", "partition", "transverse"]
---
# Partition transverse - Sécurité et confiance

## Finalité

Cette partition transverse cadre les mécanismes de sécurité, de confiance, d'auditabilité et de résidence des données applicables à l'ensemble des flux de valeur.

## Périmètre

- Partitions couvertes : [PART-VS-01](../value-streams/part-vs-01.md), [PART-VS-02](../value-streams/part-vs-02.md), [PART-VS-03](../value-streams/part-vs-03.md), [PART-VS-04](../value-streams/part-vs-04.md)
- Niveau TOGAF : enterprise-transversal
- Domaine principal : technology
- Etat d'architecture : cible

## Règle de cohérence

Toute évolution de cette partition doit maintenir une chaîne de confiance vérifiable entre authentification, autorisation, journalisation, chiffrement et gouvernance des données personnelles.
