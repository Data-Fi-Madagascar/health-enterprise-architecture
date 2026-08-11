---
id: art-6
type: chapitre
niveau: "4"
title: ART-6 — Analytique et restitution
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/03_chapitres/art-6-analytique-restitution.md
maps_to: ["cap-13", "cap-08"]
implements: []
applies_to: ["enf-4"]
related: []
tags: ['artsn', 'niveau-4', 'chapitre', 'art-6']
---
# ART-6 — Analytique et restitution

**Contenu normatif.** L'architecture doit imposer une **séparation étanche entre le stockage opérationnel et le stockage analytique** (CQRS). L'entrepôt analytique doit être alimenté par des pipelines automatisés intégrant un moteur de masquage irréversible, et doit supporter nativement quatre types de requêtes : projections tabulaires, parcours de graphes, réconciliation comptable et fusion de signaux géospatiaux.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (requêtes lourdes des décideurs, extractions massives pour la recherche) : elle seule permet de garantir des performances de restitution constantes et une sécurité réglementaire absolue sans surcharger les serveurs de soins et sans rompre le pipeline.

- **Rattachement** : [CAP-13](../capabilites/cap-13.md), [CAP-08](../capabilites/cap-08.md) (analytics & décisionnel).
- **Infrastructure cible** : Data Lakehouse.
- **Pattern cible** : modèle de séparation CQRS.
- **Déduit selon** : [ENF-4](../exigences/enf-4.md) (protection One Health).
- **Statut : Provisoire.**
