---
title: ART-8a — Orchestration de processus borné
id: art-8a-orchestration-processus-borne
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-8a, saga, processus, niveau-3]
---

# ART-8a — Orchestration de processus borné

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

**Contenu normatif.** Pour tout processus métier distribué, asynchrone et à étapes multiples, l'architecture impose l'utilisation d'un **gestionnaire de transactions longues**. Ce composant doit suivre l'état du parcours, maintenir la cohérence sans verrouiller les bases distantes, et déclencher obligatoirement des transactions d'annulation ou de correction en cas d'échec d'une étape.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (établissements hospitaliers autonomes, cliniques privées, rupture de liaison réseau d'un des nœuds) : elle seule permet d'assurer la continuité et la traçabilité complète du parcours patient sans bloquer les systèmes locaux et sans rompre le pipeline.

- **Rattachement** : [CAP-13](../../00_caesn/03_capabilities/index.md), [CAP-14](../../00_caesn/03_capabilities/index.md).
- **Pattern cible** : Saga / Process Manager (transactions de compensation).
- **Déduit selon** : [ENF-5](../02_exigences-contextuelles.md#enf-5--coordination-des-processus-complexes-décentralisés-et-asynchrones) (processus complexes).
- **Statut : Provisoire.**

## Liens

- [Index des chapitres](./index.md)
- [ART-8 — Orchestration de processus borné](./art-8-orchestration-processus-borne.md)
- [Couche 4 — Interopérabilité et services partagés](../04_cartographie-cible.md)
