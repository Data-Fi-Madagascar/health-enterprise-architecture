---
domain: externes
id: PART-ECHANGE-TRANSFRONTALIER
type: architecture-partition
niveau: "2"
title: Partition échange transfrontalier
status: draft
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-13
partition_kind: externe
togaf_repository_section: architecture-landscape
togaf_adm_phase: C
architecture_level: extended-enterprise
architecture_domain: application
architecture_scope: cross-border-exchange
architecture_state: target
applies_to: ["CAP-15", "CAP-18", "DO-29", "DO-30", "DO-31"]
related: []
tags: ["togaf", "partition", "externe"]
---
# Partition échange transfrontalier

## Finalité

Cette partition externe cadre les échanges sanitaires transfrontaliers et les objets de données qui exigent une interopérabilité hors des frontières administratives nationales.

## Périmètre

- Capabilités couvertes : [CAP-15](../../02_architecture-elements/strategy/capabilities/cap-15.md), [CAP-18](../../02_architecture-elements/strategy/capabilities/cap-18.md)
- Objets de données couverts : [DO-29](../../02_architecture-elements/data/data-objects/do-29.md), [DO-30](../../02_architecture-elements/data/data-objects/do-30.md), [DO-31](../../02_architecture-elements/data/data-objects/do-31.md)
- Niveau TOGAF : extended-enterprise
- Etat d'architecture : cible

## Règle de cohérence

Toute évolution de cette partition doit préserver la résidence de la copie maîtresse nationale et limiter l'échange transfrontalier aux jeux de données, consentements et mécanismes de confiance explicitement autorisés.
