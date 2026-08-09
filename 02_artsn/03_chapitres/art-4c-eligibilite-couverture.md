---
title: ART-4c — Éligibilité et couverture
id: art-4c-eligibilite-couverture
domain: 02_artsn
version: "0.1.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-4c, eligibilite, couverture, csu, niveau-3]
---

# ART-4c — Éligibilité et couverture

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

**Contenu normatif.** L'architecture doit maintenir un référentiel des droits ouverts structurant **disjoint de l'identité** et versionné dans le temps. Ce registre doit être accessible instantanément pour permettre le calcul automatique de la couverture financière au point de vente. Pattern cible : modélisation temporelle SCD type 2.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (comptoirs de pharmacies privées, caisses d'hôpitaux autonomes) : elle seule permet d'appliquer la gratuité légale en ligne de front sans imposer d'avance de frais aux ménages vulnérables et sans rompre le pipeline.

- **Rattachement** : [CAP-07](../../00_caesn/03_capabilities/index.md) (protection financière, CSU).
- **Pattern cible** : modélisation temporelle SCD type 2.
- **Déduit selon** : [ENF-2](../02_exigences-contextuelles.md#enf-2--intégrité-des-flux-et-traçabilité-des-valeurs) (anti-fraude) et [ENF-1](../02_exigences-contextuelles.md#enf-1--résilience-à-l-instabilité-réseau) (autonomie locale).
- **Statut : Proposition ouverte.**

## Liens

- [Index des chapitres](./index.md)
- [ART-4 — Référentiels de métadonnées de gestion](./art-4-referentiels-metadonnees.md)
- [VS-03 — Protection financière](../01_flux-de-valeur.md#vs-03--protéger-financièrement-la-population-face-aux-dépenses-de-santé)
