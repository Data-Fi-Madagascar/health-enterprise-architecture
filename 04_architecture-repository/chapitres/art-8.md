---
domain: chapitres

id: ART-8
type: chapitre
niveau: "3"
title: Orchestration de processus
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-8-orchestration-processus-borne.md
maps_to: ["CAP-13", "CAP-14"]
implements: []
applies_to: []
related: ["ART-8A", "ART-8B", "ART-8C", "ART-8D"]
tags: ["artsn", "niveau-3", "chapitre", "ART-8"]
---
# Orchestration de processus

**Contenu normatif.** Pour tout processus métier distribué, asynchrone et à étapes multiples, l’architecture impose l’utilisation d’un **gestionnaire de transactions longues**. Ce composant doit suivre l’état du parcours, maintenir la cohérence sans verrouiller les bases distantes, et déclencher obligatoirement des transactions d’annulation ou de correction en cas d’échec d’une étape.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (établissements hospitaliers autonomes, cliniques privées, rupture de liaison réseau d’un des nœuds), cette discipline seule permet d’assurer la continuité et la traçabilité complète du parcours patient sans bloquer les systèmes locaux et sans rompre le pipeline.

- **Rattachement** : [CAP-13: Système d'information sanitaire, données et recherche](../capabilites/cap-13.md), [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../capabilites/cap-14.md).
- **Pattern cible** : Saga / Process Manager (transactions de compensation).

Ce chapitre se décline en quatre sous-chapitres :
- [ART-8A: Orchestration de processus borné](art-8a.md)
- [ART-8B: Modélisation de relations en graphe](art-8b.md)
- [ART-8C: Agrégation par lot](art-8c.md)
- [ART-8D: Chorégraphie inter-institutionnelle](art-8d.md)

## Profils PTISN qui implémentent ce chapitre

Les profils techniques nationaux ci-dessous déclarent implémenter ce chapitre ART dans leur champ `implements` (frontmatter du référentiel). Le profil constitue la spécification implémentable et testable ; le chapitre demeure le cadre normatif opposable.

- [PT-02 : Médiation intra-secteur](../profils/pt-02.md)

