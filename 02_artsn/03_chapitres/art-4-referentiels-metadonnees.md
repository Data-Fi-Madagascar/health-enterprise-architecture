---
title: "ART-4 — Référentiels de métadonnées de gestion"
id: art-4
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-4, niveau-3]
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

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).


ART-4 — Référentiels de métadonnées de gestion constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : [`art-4`](../../referentiel/chapitres/art-4.md).

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

**Contenu normatif.** La maintenance et le stockage des structures de gestion (établissements, programmes sanitaires, indicateurs) doivent obligatoirement utiliser une **modélisation temporelle**. Tout changement ou divergence de hiérarchie organisationnelle doit être historisé et versionné, selon le pattern cible *Slowly Changing Dimension* (SCD) **type 2**.

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (évolutions administratives, réorganisations territoriales) : elle seule permet de garantir qu’une analyse ou un rapport statistique passé pointe vers l’arborescence exacte en vigueur au moment précis de l’événement sans rompre le pipeline.

- **Rattachement** : [CAP-14](../../referentiel/capabilites/cap-14.md) (interopérabilité et infrastructure partagée).
- **Pattern cible** : SCD type 2.
- **Déduit selon** : [ENF-4](../../referentiel/exigences/enf-4.md) (cloisonnement inter-institutionnel).
- **Statut : Stable.**

Ce chapitre se décline en quatre sous-chapitres :
- [ART-4a — Résolution d’identité](../../referentiel/chapitres/art-4a.md)
- [ART-4b — Bases d’autorisation](../../referentiel/chapitres/art-4b.md)
- [ART-4c — Éligibilité et couverture](../../referentiel/chapitres/art-4c.md)
- [ART-4d — Référentiel géospatial et d’exploitation partagé](../../referentiel/chapitres/art-4d.md)

*Rattachement : [ENF-4](../../referentiel/exigences/enf-4.md), [CAP-14](../../referentiel/capabilites/cap-14.md) · [fiche](../../referentiel/chapitres/art-4.md)*

<!-- END:GENERATED -->
## Liens

- [Index des chapitres](./index.md)
- [Exigences contextuelles — Partie III](../02_exigences-contextuelles/index.md)
