---
title: PT-09 — Profil technique national
id: ptisn-pt-09-analytique-exposition-donnees
domain: 03_ptisn
version: "0.4"
status: draft
last_reviewed: 2026-07-31
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "profils", "pt-09"]
---

# PT-09 — Profil technique national


## 1. Capacité CNISN

**CAP-INT-07 — Accès et exposition des données analytiques**

## 2. Chapitres ART applicables

- ART-3 selon le profil retenu ;
- ART-5 ;
- ART-6 ;
- ART-7.

## 3. Services nationaux

- entrepôt analytique national ;
- service d’indicateurs ;
- service de consultation des données agrégées ;
- service de qualité ;
- service de réconciliation ;
- service de tableaux de bord ;
- service de publication de jeux de données autorisés.

## 4. Patrons applicables

Les initiatives peuvent appliquer :

- séparation lecture-écriture ;
- projections tabulaires ;
- modèles historiques ;
- modèles d’état courant ;
- modèles spatio-temporels ;
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

Le PTISN ne retient pas, à ce stade, de produit national unique pour :

- l’entrepôt analytique ;
- la visualisation ;
- le moteur de projection ;
- l’historisation événementielle.

Ces choix relèvent :

- de l’architecture de solution ;
- de l’analyse comparative ;
- de l’homologation ;
- des exigences de performance ;
- du coût total de possession.

## 7. Première implémentation

La plateforme de traçabilité RMA est reconnue comme **première initiative de validation** du profil analytique national.

Son architecture ne devient pas automatiquement obligatoire pour toutes les initiatives.

------------------------------------------------------------------------
