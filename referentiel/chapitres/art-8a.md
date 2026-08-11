---
id: art-8a
type: chapitre
niveau: "3"
title: ART-8a — Orchestration de processus borné
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/03_chapitres/art-8a-orchestration-processus-borne.md
maps_to: ["cap-13", "cap-14"]
implements: []
applies_to: ["enf-5"]
related: ["art-8"]
tags: ['artsn', 'niveau-3', 'chapitre', 'art-8a']
---
# ART-8a — Orchestration de processus borné

**Contenu normatif.** Pour tout processus métier distribué, asynchrone et à étapes multiples, l’architecture impose l’utilisation d’un **gestionnaire de transactions longues**. Ce composant doit suivre l’état du parcours, maintenir la cohérence sans verrouiller les bases distantes, et déclencher obligatoirement des transactions d’annulation ou de correction en cas d’échec d’une étape.

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (établissements hospitaliers autonomes, cliniques privées, rupture de liaison réseau d’un des nœuds) : elle seule permet d’assurer la continuité et la traçabilité complète du parcours patient sans bloquer les systèmes locaux et sans rompre le pipeline.

- **Rattachement** : [CAP-13](../capabilites/cap-13.md), [CAP-14](../capabilites/cap-14.md).
- **Pattern cible** : Saga / Process Manager (transactions de compensation).
- **Déduit selon** : [ENF-5](../exigences/enf-5.md) (processus complexes).
- **Statut : Provisoire.**
