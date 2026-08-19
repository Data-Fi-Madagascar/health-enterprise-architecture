---
title: "ART-4 — Référentiels de métadonnées de gestion"
id: art-4
domain: 02_artsn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-4, niveau-3]
related: ['cap-int-03']
---

# ART-4 — Référentiels de métadonnées de gestion

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.


ART-4 — Référentiels de métadonnées de gestion constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `art-4`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

**Contenu normatif.** La maintenance et le stockage des structures de gestion (établissements, programmes sanitaires, indicateurs) doivent obligatoirement utiliser une **modélisation temporelle**. Tout changement ou divergence de hiérarchie organisationnelle doit être historisé et versionné, selon le pattern cible *Slowly Changing Dimension* (SCD) **type 2**.

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (évolutions administratives, réorganisations territoriales) : elle seule permet de garantir qu’une analyse ou un rapport statistique passé pointe vers l’arborescence exacte en vigueur au moment précis de l’événement sans rompre le pipeline.

- **Rattachement** : CAP-14 (interopérabilité et infrastructure partagée).
- **Pattern cible** : SCD type 2.
- **Déduit selon** : ENF-4 (cloisonnement inter-institutionnel).
- **Statut : Stable.**

Ce chapitre se décline en quatre sous-chapitres :
- ART-4a — Résolution d’identité
- ART-4b — Bases d’autorisation
- ART-4c — Éligibilité et couverture
- ART-4d — Référentiel géospatial et d’exploitation partagé

*Rattachement : ENF-4, CAP-14 · fiche ART-4*

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles — Partie III

## Références

- **matrice de lecture** — Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`art-4`** — Référentiels de métadonnées de gestion (`referentiel/chapitres/art-4.md`)
- **Index des chapitres** — Chapitres et patterns de référence (`02_artsn/03_chapitres/index.md`)
- **Exigences contextuelles — Partie III** — Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
