---
title: "Partie III : Profils techniques nationaux"
id: ptisn-profils
domain: 03_profils
version: "1.0.0"
status: draft
last_reviewed: 2026-07-31
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "profils"]
---

# Partie III : Profils techniques nationaux

Catalogue des 19 profils techniques. Chaque profil est un objet du référentiel (`referentiel/profils/pt-XX.md`) ; les numéros de capacité et de chapitres ART ont été alignés sur le CNISN et l'ARTSN pendant la migration (voir `coherence-report.md`).

## Qu'est-ce qu'un PT (profil de mise en œuvre) ?

Un **PT (profil technique national)** est un *profil de mise en œuvre* : un document du niveau 4 qui prescrit, pour un service national, les standards, acteurs, transactions et règles d'échange à respecter. Il est rédigé sur le modèle des **profils IHE (Integrating the Healthcare Enterprise)**, c'est-à-dire comme une spécification implémentable et testable.

Chaque fiche PT suit un modèle canonique de 13 sections : objet et périmètre, capacité CNISN, chapitres ART, **acteurs**, **transactions (R/O)**, **content modules**, **options**, service national, formats/standards, exigences, **déclaration de conformité (Integration Statement)**, articulation, limites.

Pour éviter les confusions :

- **PT ≠ profil IHE** : le PT *prescrit et référence* les profils IHE (PIXm, PDQm, mCSD, SVCM, mADX, IUA, ATNA…) et les normes nationales, il ne les « porte » pas ; il adapte ces profils au contexte national.
- **PT ≠ contrat d'interface** : le *contrat d'interface* est la spécification technique d'un échange (API, fichier, flux) définie **par une initiative** pour décliner le PT au niveau de sa solution. Le PT fixe le cadre ; le contrat d'interface l'instancie.

<!-- BEGIN:GENERATED mode=table source=referentiel/profils/pt-*.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

| Code | Titre canonique | Rattachement | Statut | Fiche |
|---|---|---|---|---|
| PT-01 | Échange interinstitutionnel | CMP-06, CAP-INT-03, CAP-INT-12, ART-0, ART-1, ART-7, ART-11 | active | PT-01 |
| PT-02 | Médiation intra-secteur | CMP-06, CAP-INT-03, ART-1, ART-2, ART-5, ART-7, ART-8, ART-8C, ART-8D | active | PT-02 |
| PT-03 | Catalogue des services et registre des contrats | CMP-16, CAP-INT-06, F-3, F-4, ART-1, ART-2 | active | PT-03 |
| PT-04 | Résolution d’identité du bénéficiaire | CMP-11, CAP-INT-01, ART-4, ART-4A, ART-4B, ART-7 | active | PT-04 |
| PT-05 | Registre des professionnels | CMP-13, CAP-INT-02, ART-4, ART-4A, ART-7, ART-4C | active | PT-05 |
| PT-06 | Référentiel des structures et services de santé | CMP-08, CAP-INT-04, ART-4, ART-5, ART-6 | active | PT-06 |
| PT-07 | Terminologie et codification | CMP-10, CAP-INT-05, ART-2, ART-4, ART-5 | active | PT-07 |
| PT-08 | Échange de données agrégées | CMP-03, CMP-06, CAP-INT-03, CAP-INT-07, ART-1, ART-2, ART-5, ART-6 | active | PT-08 |
| PT-09 | Analytique et exposition de données | CMP-03, CMP-04, CAP-INT-07, ART-3, ART-5, ART-6, ART-7 | active | PT-09 |
| PT-10 | Confiance, authentification et autorisation | CMP-15, CAP-INT-08, ART-0, ART-4B, ART-7, ART-9 | active | PT-10 |
| PT-11 | Consentement et bases d’autorisation | CMP-12, CAP-INT-09, ART-0, ART-4B, ART-7, ART-11 | active | PT-11 |
| PT-12 | Audit, provenance et traçabilité | CMP-17, CAP-INT-10, F-1, F-5, F-6, ART-3, ART-7 | active | PT-12 |
| PT-13 | Qualité et réconciliation | CMP-05, CAP-INT-11, ART-4, ART-5, ART-6 | active | PT-13 |
| PT-14 | Interopérabilité transfrontalière | CAP-INT-13, CAP-15, CAP-17, CMP-06, CMP-15, ART-7, ART-0, ART-1 | active | PT-14 |
| PT-15 | Surveillance One Health | CAP-INT-14, CAP-INT-16, CAP-18, CAP-05, CMP-02, CMP-04, CMP-06, ART-11, ART-0, ART-4D, ART-8B | active | PT-15 |
| PT-16 | Orchestration de processus bornés | CMP-07, CMP-06, CAP-INT-03, ART-8A, ART-7 | active | PT-16 |
| PT-17 | Logistique & chaîne d'approvisionnement (LMIS) | CMP-23, CAP-INT-10, CAP-INT-15, ART-10 | active | PT-17 |
| PT-18 | Profil technique national | CAP-INT-07, ART-2, ART-9 | active | PT-18 |
| PT-19 | Profil technique national | CMP-08, CAP-INT-05, ART-12, ART-2 | active | PT-19 |

<!-- END:GENERATED -->

## Maturité et statuts des profils

L'ensemble des profils de référence est à l'état `draft`, à l'exception de PT-17 (`candidate`). Aucun profil n'est encore `recommandé`, `retenu` ou `homologué` ; cette table sera mise à jour au fil des décisions du Comité National (voir l'annexe `e-priorisation-decisions`).

| Statut | Profils |
|--------|---------|
| candidate | PT-17 |
| draft | PT-01, PT-02, PT-03, PT-04, PT-05, PT-06, PT-07, PT-08, PT-09, PT-10, PT-11, PT-12, PT-13, PT-14, PT-15, PT-16, PT-18, PT-19 |
