---
title: PT-07 : Profil technique national
id: ptisn-PT-07-terminologie-codification
domain: 03_ptisn
version: "1.0.0"
status: draft
last_reviewed: 2026-07-31
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "profils", "PT-07"]
---

# PT-07 : Profil technique national

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

## 1. Capacité CNISN

[CAP-INT-05: Terminologie et codification communes](../../referentiel/capacites/cap-int-05.md)

## 2. Chapitres ART applicables

- [ART-2: normalisation sémantique](../../referentiel/chapitres/art-2.md)antique ;
- [ART-4: référentiels](../../referentiel/chapitres/art-4.md)entiels ;
- [ART-5: qualité.](../../referentiel/chapitres/art-5.md)ualité.

## 3. Service national

**Service terminologique national de santé**

## 4. Responsabilités

Le service doit permettre :

- la consultation d’un système de codes ;
- la consultation d’un ensemble de valeurs ;
- l’expansion d’un ensemble de valeurs ;
- la validation d’un code ;
- la recherche d’un concept ;
- la traduction entre systèmes de codes ;
- la publication de mappings ;
- la gestion des versions ;
- la dépréciation des concepts.

## 5. Profil cible

**IHE SVCM — Sharing Valuesets, Codes, and Maps**

SVCM définit une interface légère, fondée sur FHIR, pour récupérer des nomenclatures, ensembles de valeurs et correspondances centralement gérés. Il prévoit notamment la consultation, l’expansion, la validation et la traduction de codes.

## 6. Ressources de base

- `CodeSystem` ;
- `ValueSet` ;
- `ConceptMap`.

## 7. Décisions

| Élément                              | Statut         |
|--------------------------------------|----------------|
| SVCM                                 | Recommandé     |
| Service terminologique national      | Requis         |
| Produit serveur terminologique       | À sélectionner |
| Catalogue national des terminologies | À constituer   |
| Extensions nationales                | À gouverner    |

## 8. Terminologies concernées

Le service peut gérer :

- diagnostics ;
- actes ;
- résultats de laboratoire ;
- produits de santé ;
- types de structures ;
- professions ;
- spécialités ;
- programmes ;
- indicateurs ;
- classifications nationales.

L’adoption d’une terminologie internationale doit être précédée d’une évaluation :

- des besoins nationaux ;
- de la langue ;
- des licences ;
- de la capacité d’exploitation ;
- des mappings nécessaires ;
- de la compatibilité avec les systèmes existants.

------------------------------------------------------------------------

*Rattachement : CMP-10, CAP-INT-05, ART-2, ART-4, ART-5 · fiche PT-07*

<!-- END:GENERATED -->
