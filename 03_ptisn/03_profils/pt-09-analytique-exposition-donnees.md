---
title: Profil technique national
id: ptisn-PT-09
domain: 03_ptisn
version: "1.0.0"
status: draft
last_reviewed: 2026-07-31
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "profils", "PT-09"]
---

# Profil technique national

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

## 1. Capacité CNISN

[CAP-INT-07: Accès et exposition des données analytiques](../../referentiel/capacites/cap-int-07.md)

## 2. Chapitres ART applicables

- [ART-3: Historisation événementielle et profils de déploiement](../../referentiel/chapitres/art-3.md) selon le profil retenu ;
- [ART-5: Cohérence et qualité des données](../../referentiel/chapitres/art-5.md) ;
- [ART-6: Analytique et restitution](../../referentiel/chapitres/art-6.md) ;
- [ART-7: Sécurité, contrôle d'accès et résidence de la donnée](../../referentiel/chapitres/art-7.md).

## 3. Services nationaux

- entrepôt analytique national ;
- service d’indicateurs ;
- service de consultation des données agrégées ;
- service de qualité ;
- service de réconciliation ;
- service de tableaux de bord ;
- service de publication de jeux de données autorisés.

## 4. Patrons applicables

Les initiatives peuvent appliquer :

- séparation lecture-écriture ;
- projections tabulaires ;
- modèles historiques ;
- modèles d’état courant ;
- modèles spatio-temporels ;
- historisation événementielle lorsque justifiée.

Le choix du patron est défini dans l’ART et dans le profil d’applicabilité de l’initiative.

## 5. Standards d’exposition

| Usage                        | Standard ou profil recommandé         |
|------------------------------|---------------------------------------|
| Données agrégées structurées | mADX                                  |
| API de consultation          | REST/OpenAPI                          |
| Ressources de santé          | HL7 FHIR lorsque applicable           |
| Métadonnées                  | mCSD, SVCM ou profils nationaux       |
| Export tabulaire             | Format ouvert, documenté et versionné |
| Catalogue de données         | Profil national à définir             |

## 6. Produits

Le PTISN ne retient pas, à ce stade, de produit national unique pour :

- l’entrepôt analytique ;
- la visualisation ;
- le moteur de projection ;
- l’historisation événementielle.

Ces choix relèvent :

- de l’architecture de solution ;
- de l’analyse comparative ;
- de l’homologation ;
- des exigences de performance ;
- du coût total de possession.

## 7. Première implémentation

La plateforme de traçabilité RMA est reconnue comme **première initiative de validation** du profil analytique national.

Son architecture ne devient pas automatiquement obligatoire pour toutes les initiatives.

------------------------------------------------------------------------

*Rattachement : CMP-03, CMP-04, CAP-INT-07, ART-3, ART-5, ART-6, ART-7 · fiche PT-09*

<!-- END:GENERATED -->
