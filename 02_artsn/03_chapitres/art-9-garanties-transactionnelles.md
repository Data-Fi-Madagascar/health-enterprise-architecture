---
title: ART-9 — Garanties transactionnelles fortes
id: art-9-garanties-transactionnelles
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-9, transactions, anti-fraude, niveau-3]
---

# ART-9 — Garanties transactionnelles fortes

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

**Contenu normatif.** Pour tout mouvement de valeur monétaire ou physique, l'architecture impose une contrainte de **grade comptable strict** basée sur un registre immuable, garantissant l'équilibre parfait des comptes (équation cible : *entrées − sorties = solde*). Toute écriture doit être associée à une signature non répudiable et un numéro de suivi de lot.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (officines pharmaceutiques privées, gestionnaires de stocks régionaux, caisses de subventions) : elle seule permet d'empêcher les détournements de médicaments, de bloquer les marchés noirs et d'assurer la réconciliation à somme nulle de l'argent public, sans rompre le pipeline.

- **Rattachement** : recouvre partiellement [CAP-07](../../00_caesn/03_capabilities/index.md) (protection financière).
- **Équation cible** : entrées − sorties = solde.
- **Déduit selon** : [ENF-2](../02_exigences-contextuelles.md#enf-2--intégrité-des-flux-et-traçabilité-des-valeurs) (grade comptable anti-fraude).
- **Statut : Proposition ouverte.**

## Liens

- [Index des chapitres](./index.md)
- [VS-03 — Protection financière](../01_flux-de-valeur.md#vs-03--protéger-financièrement-la-population-face-aux-dépenses-de-santé)
- [ENF-2 — Intégrité des flux](../02_exigences-contextuelles.md#enf-2--intégrité-des-flux-et-traçabilité-des-valeurs)
