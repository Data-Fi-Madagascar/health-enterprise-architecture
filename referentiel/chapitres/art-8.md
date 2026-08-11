---
id: art-8
type: chapitre
niveau: "3"
title: ART-8 — Orchestration de processus
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/03_chapitres/art-8-orchestration-processus-borne.md
maps_to: ["cap-13", "cap-14"]
implements: []
applies_to: []
related: ["art-8a", "art-8b", "art-8c", "art-8d"]
tags: ['artsn', 'niveau-3', 'chapitre', 'art-8']
---
# ART-8 — Orchestration de processus

**Contenu normatif.** Pour tout processus métier distribué, asynchrone et à étapes multiples, l’architecture impose l’utilisation d’un **gestionnaire de transactions longues**. Ce composant doit suivre l’état du parcours, maintenir la cohérence sans verrouiller les bases distantes, et déclencher obligatoirement des transactions d’annulation ou de correction en cas d’échec d’une étape.

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (établissements hospitaliers autonomes, cliniques privées, rupture de liaison réseau d’un des nœuds) : elle seule permet d’assurer la continuité et la traçabilité complète du parcours patient sans bloquer les systèmes locaux et sans rompre le pipeline.

- **Rattachement** : [CAP-13](../capabilites/cap-13.md), [CAP-14](../capabilites/cap-14.md).
- **Pattern cible** : Saga / Process Manager (transactions de compensation).

Ce chapitre se décline en quatre sous-chapitres :
- [ART-8a — Orchestration de processus borné](art-8a.md)
- [ART-8b — Modélisation de relations en graphe](art-8b.md)
- [ART-8c — Agrégation par lot](art-8c.md)
- [ART-8d — Chorégraphie inter-institutionnelle](art-8d.md)
