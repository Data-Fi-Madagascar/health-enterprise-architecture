---
title: ART-4 — Référentiels de métadonnées de gestion
id: art-4-referentiels-metadonnees
domain: 02_artsn
version: "0.1.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-4, referentiels, niveau-3]
---

# ART-4 — Référentiels de métadonnées de gestion

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

**Contenu normatif.** La maintenance et le stockage des structures de gestion (établissements, programmes sanitaires, indicateurs) doivent obligatoirement utiliser une **modélisation temporelle**. Tout changement ou divergence de hiérarchie organisationnelle doit être historisé et versionné, selon le pattern cible *Slowly Changing Dimension* (SCD) **type 2**.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (évolutions administratives, réorganisations territoriales) : elle seule permet de garantir qu'une analyse ou un rapport statistique passé pointe vers l'arborescence exacte en vigueur au moment précis de l'événement sans rompre le pipeline.

- **Rattachement** : [CAP-14](../../00_caesn/03_capabilities/index.md) (interopérabilité et infrastructure partagée).
- **Pattern cible** : SCD type 2.
- **Déduit selon** : [ENF-4](../02_exigences-contextuelles.md#enf-4--cloisonnement-inter-institutionnel-et-étanchéité-des-données-one-health) (cloisonnement inter-institutionnel).
- **Statut : Stable.**

Ce chapitre se décline en quatre sous-chapitres :
- [ART-4a — Résolution d'identité](./art-4a-resolution-identite.md)
- [ART-4b — Bases d'autorisation](./art-4b-bases-autorisation.md)
- [ART-4c — Éligibilité et couverture](./art-4c-eligibilite-couverture.md)
- [ART-4d — Référentiel géospatial et d'exploitation partagé](./art-4d-referentiel-geospatial.md)

## Liens

- [Index des chapitres](./index.md)
- [Couche 4 — Interopérabilité et services partagés](../04_cartographie-cible.md)
