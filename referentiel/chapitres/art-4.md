---
id: art-4
type: chapitre
niveau: "3"
title: ART-4 — Référentiels de métadonnées de gestion
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/03_chapitres/art-4-referentiels-metadonnees.md
maps_to: ["cap-14"]
implements: []
applies_to: ["enf-4"]
related: ["art-4a", "art-4b", "art-4c", "art-4d"]
tags: ['artsn', 'niveau-3', 'chapitre', 'art-4']
---
# ART-4 — Référentiels de métadonnées de gestion

**Contenu normatif.** La maintenance et le stockage des structures de gestion (établissements, programmes sanitaires, indicateurs) doivent obligatoirement utiliser une **modélisation temporelle**. Tout changement ou divergence de hiérarchie organisationnelle doit être historisé et versionné, selon le pattern cible *Slowly Changing Dimension* (SCD) **type 2**.

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (évolutions administratives, réorganisations territoriales) : elle seule permet de garantir qu’une analyse ou un rapport statistique passé pointe vers l’arborescence exacte en vigueur au moment précis de l’événement sans rompre le pipeline.

- **Rattachement** : [CAP-14](../capabilites/cap-14.md) (interopérabilité et infrastructure partagée).
- **Pattern cible** : SCD type 2.
- **Déduit selon** : [ENF-4](../exigences/enf-4.md) (cloisonnement inter-institutionnel).
- **Statut : Stable.**

Ce chapitre se décline en quatre sous-chapitres :
- [ART-4a — Résolution d’identité](art-4a.md)
- [ART-4b — Bases d’autorisation](art-4b.md)
- [ART-4c — Éligibilité et couverture](art-4c.md)
- [ART-4d — Référentiel géospatial et d’exploitation partagé](art-4d.md)
