---
title: ART-6 — Analytique et restitution
id: art-6-analytique-restitution
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-6, analytique, cqrs, niveau-3]
---

# ART-6 — Analytique et restitution

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

**Contenu normatif.** L'architecture doit imposer une **séparation étanche entre le stockage opérationnel et le stockage analytique** (CQRS). L'entrepôt analytique doit être alimenté par des pipelines automatisés intégrant un moteur de masquage irréversible, et doit supporter nativement quatre types de requêtes : projections tabulaires, parcours de graphes, réconciliation comptable et fusion de signaux géospatiaux.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (requêtes lourdes des décideurs, extractions massives pour la recherche) : elle seule permet de garantir des performances de restitution constantes et une sécurité réglementaire absolue sans surcharger les serveurs de soins et sans rompre le pipeline.

- **Rattachement** : [CAP-13](../../00_caesn/03_capabilities/index.md), [CAP-08](../../00_caesn/03_capabilities/index.md) (analytics & décisionnel).
- **Infrastructure cible** : Data Lakehouse.
- **Pattern cible** : modèle de séparation CQRS.
- **Déduit selon** : [ENF-4](../02_exigences-contextuelles.md#enf-4--cloisonnement-inter-institutionnel-et-étanchéité-des-données-one-health) (protection One Health).
- **Statut : Provisoire.**

## Liens

- [Index des chapitres](./index.md)
- [VS-04 — Pilotage et performance](../01_flux-de-valeur.md#vs-04--piloter-coordonner-et-améliorer-la-performance-du-système-de-santé)
- [Couche 5 — Projections analytiques et modèles](../04_cartographie-cible.md)
