---
title: Objets de données métier
id: data-business-objects
domain: 04_data
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: Cellule du Système d'Information Sanitaire
tags: ["données", "objets", "métier", "caesn"]
---

# Objets de données métier

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

Les décideurs institutionnels et les directions métier y trouveront une lecture complémentaire, tandis que l'équipe DEPSI, les équipes techniques, et les équipes SIS, données et suivi-évaluation y trouveront une lecture prioritaire. Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

Ce document définit les **objets de données métier** (BO) du niveau 1 (CAESN) : l'atome d'information porteur de sens pour l'action publique, indépendant de toute technologie. Chaque objet métier est **réalisé** par un ou plusieurs objets de données de l'ARTSN (`../../02_artsn/03_objets-de-donnees/index.md`), qui en fixent la forme normalisée et les contrats d'interfaces.

## 01. Patient & identité

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/objets-metier/bo-01.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### BO-01 : Patient & identité

Identité de la personne prise en charge, épisodes de soins, dossier et référencements. Pilier de toute continuité de prise en charge.

- **Réalise (ARTSN)** : [P-01 Patient, P-02 Identifiant national, P-03 Dossier patient, P-04 Épisode de soins](../../02_artsn/03_objets-de-donnees/index.md)
- **Flux de valeur** : VS-01, VS-03

<!-- END:GENERATED -->

## 02. Prestation & soins

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/objets-metier/bo-02.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### BO-02 : Prestation & soins

Actes cliniques, prescriptions, références et évacuations constituant le parcours de soins.

- **Réalise (ARTSN)** : [S-01 Consultation, S-02 Prescription, S-03 Référence, S-04 Contre-référence, S-05 Évacuation sanitaire](../../02_artsn/03_objets-de-donnees/index.md)
- **Flux de valeur** : VS-01, VS-02

<!-- END:GENERATED -->

## 03. Dispensation & produits

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/objets-metier/bo-03.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### BO-03 : Dispensation & produits

Médicaments, produits de santé, lots et stocks dispensés sur le terrain.

- **Réalise (ARTSN)** : [D-01 Dispensation, D-02 Produit de santé, D-03 Lot, D-04 Stock](../../02_artsn/03_objets-de-donnees/index.md)
- **Flux de valeur** : VS-01, VS-02, VS-04

<!-- END:GENERATED -->

## 04. Financement & couverture

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/objets-metier/bo-04.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### BO-04 : Financement & couverture

Éligibilité, couverture, facturation et vérification financière des soins.

- **Réalise (ARTSN)** : [F-01 Éligibilité, F-02 Couverture sanitaire, F-03 Facturation, F-04 Vérification d'éligibilité](../../02_artsn/03_objets-de-donnees/index.md)
- **Flux de valeur** : VS-03, VS-04

<!-- END:GENERATED -->

## 05. Risque & surveillance

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/objets-metier/bo-05.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### BO-05 : Risque & surveillance

Signaux, foyers, investigations et alertes de surveillance sanitaire (y compris One Health).

- **Réalise (ARTSN)** : [R-01 Signal, R-02 Foyer, R-03 Investigation, R-04 Notification sanitaire, R-05 Alerte sanitaire](../../02_artsn/03_objets-de-donnees/index.md)
- **Flux de valeur** : VS-02, VS-04

<!-- END:GENERATED -->

## 06. Exploitation & gestion

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/objets-metier/bo-06.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### BO-06 : Exploitation & gestion

Structures, agents, indicateurs, zones et tableaux de bord de pilotage.

- **Réalise (ARTSN)** : [E-01 Formation sanitaire, E-02 Agent de santé, E-03 Indicateur sanitaire, E-04 Zone sanitaire, E-05 Tâche, E-06 Tableau de bord](../../02_artsn/03_objets-de-donnees/index.md)
- **Flux de valeur** : Tous les VS

<!-- END:GENERATED -->

## 07. Interopérabilité transfrontalière

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/objets-metier/bo-07.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### BO-07 : Interopérabilité transfrontalière

Résumé patient international, sections et confiance pour les échanges hors frontières.

- **Réalise (ARTSN)** : [T-01 Résumé international du patient, T-02 Section du résumé, T-03 Confiance internationale](../../02_artsn/03_objets-de-donnees/index.md)
- **Flux de valeur** : VS-02

<!-- END:GENERATED -->

## Liens

- Domaines de données prioritaires (`00_caesn/04_data/domains.md`)
- Objets de données de l'ARTSN (`../../02_artsn/03_objets-de-donnees/index.md`)

## Références

- **Domaines de données** : Domaines de données prioritaires (`00_caesn/04_data/domains.md`)
- **Objets de données ARTSN** : Objets de données (`../../02_artsn/03_objets-de-donnees/index.md`)
- **Chapitre ART-2 (médiation)** : Médiation et normalisation (`../../referentiel/chapitres/art-2.md`)
