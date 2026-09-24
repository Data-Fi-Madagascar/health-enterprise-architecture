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

<!-- BEGIN:GENERATED mode=catalogue source=04_architecture-repository/02_architecture-elements/business/business-objects/bo-01.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### BO-01 : Patient & identité

Identité de la personne prise en charge, épisodes de soins, dossier et référencements. Pilier de toute continuité de prise en charge.

#### Description

L'objet métier BO-01 : Patient & identité structure et pilote les concepts de données suivants, garants de la cohérence métier de la prise en charge. Il alimente les flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md) et s'inscrit dans la continuité des chapitres ARTSN (médiation et normalisation, échange et résidence).

#### Objets de données réalisés (ARTSN)

- [DO-01 : Patient](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-01.md)
- [DO-02 : Identifiant national](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-02.md)
- [DO-03 : Dossier patient](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-03.md)
- [DO-04 : Épisode de soins](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-04.md)

#### Flux de valeur

- [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md)
- [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md)

#### Réalise (ARTSN)

- **Dictionnaire de données fonctionnelles** : [Dictionnaire de données fonctionnelles](../../02_artsn/03_objets-de-donnees/index.md)

<!-- END:GENERATED -->

## 02. Prestation & soins

<!-- BEGIN:GENERATED mode=catalogue source=04_architecture-repository/02_architecture-elements/business/business-objects/bo-02.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### BO-02 : Prestation & soins

Actes cliniques, prescriptions, références et évacuations constituant le parcours de soins.

#### Description

L'objet métier BO-02 : Prestation & soins structure et pilote les concepts de données suivants, garants de la cohérence métier de la prise en charge. Il alimente les flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md) et s'inscrit dans la continuité des chapitres ARTSN (médiation et normalisation, échange et résidence).

#### Objets de données réalisés (ARTSN)

- [DO-05 : Consultation](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-05.md)
- [DO-06 : Prescription](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-06.md)
- [DO-07 : Référence](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-07.md)
- [DO-08 : Contre-référence](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-08.md)
- [DO-09 : Évacuation sanitaire](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-09.md)

#### Flux de valeur

- [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md)
- [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md)

#### Réalise (ARTSN)

- **Dictionnaire de données fonctionnelles** : [Dictionnaire de données fonctionnelles](../../02_artsn/03_objets-de-donnees/index.md)

<!-- END:GENERATED -->

## 03. Dispensation & produits

<!-- BEGIN:GENERATED mode=catalogue source=04_architecture-repository/02_architecture-elements/business/business-objects/bo-03.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### BO-03 : Dispensation & produits

Médicaments, produits de santé, lots et stocks dispensés sur le terrain.

#### Description

L'objet métier BO-03 : Dispensation & produits structure et pilote les concepts de données suivants, garants de la cohérence métier de la prise en charge. Il alimente les flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md) et s'inscrit dans la continuité des chapitres ARTSN (médiation et normalisation, échange et résidence).

#### Objets de données réalisés (ARTSN)

- [DO-10 : Dispensation](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-10.md)
- [DO-11 : Produit de santé](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-11.md)
- [DO-12 : Lot](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-12.md)
- [DO-13 : Stock](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-13.md)

#### Flux de valeur

- [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md)
- [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md)
- [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)

#### Réalise (ARTSN)

- **Dictionnaire de données fonctionnelles** : [Dictionnaire de données fonctionnelles](../../02_artsn/03_objets-de-donnees/index.md)

<!-- END:GENERATED -->

## 04. Financement & couverture

<!-- BEGIN:GENERATED mode=catalogue source=04_architecture-repository/02_architecture-elements/business/business-objects/bo-04.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### BO-04 : Financement & couverture

Éligibilité, couverture, facturation et vérification financière des soins.

#### Description

L'objet métier BO-04 : Financement & couverture structure et pilote les concepts de données suivants, garants de la cohérence métier de la prise en charge. Il alimente les flux de valeur [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md) et s'inscrit dans la continuité des chapitres ARTSN (médiation et normalisation, échange et résidence).

#### Objets de données réalisés (ARTSN)

- [DO-14 : Éligibilité](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-14.md)
- [DO-15 : Couverture sanitaire](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-15.md)
- [DO-16 : Facturation](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-16.md)
- [DO-17 : Vérification d'éligibilité](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-17.md)

#### Flux de valeur

- [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md)
- [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)

#### Réalise (ARTSN)

- **Dictionnaire de données fonctionnelles** : [Dictionnaire de données fonctionnelles](../../02_artsn/03_objets-de-donnees/index.md)

<!-- END:GENERATED -->

## 05. Risque & surveillance

<!-- BEGIN:GENERATED mode=catalogue source=04_architecture-repository/02_architecture-elements/business/business-objects/bo-05.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### BO-05 : Risque & surveillance

Signaux, foyers, investigations et alertes de surveillance sanitaire (y compris One Health).

#### Description

L'objet métier BO-05 : Risque & surveillance structure et pilote les concepts de données suivants, garants de la cohérence métier de la prise en charge. Il alimente les flux de valeur [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md) et s'inscrit dans la continuité des chapitres ARTSN (médiation et normalisation, échange et résidence).

#### Objets de données réalisés (ARTSN)

- [DO-18 : Signal](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-18.md)
- [DO-19 : Foyer](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-19.md)
- [DO-20 : Investigation](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-20.md)
- [DO-21 : Notification sanitaire](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-21.md)
- [DO-22 : Alerte sanitaire](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-22.md)

#### Flux de valeur

- [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md)
- [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)

#### Réalise (ARTSN)

- **Dictionnaire de données fonctionnelles** : [Dictionnaire de données fonctionnelles](../../02_artsn/03_objets-de-donnees/index.md)

<!-- END:GENERATED -->

## 06. Exploitation & gestion

<!-- BEGIN:GENERATED mode=catalogue source=04_architecture-repository/02_architecture-elements/business/business-objects/bo-06.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### BO-06 : Exploitation & gestion

Structures, agents, indicateurs, zones et tableaux de bord de pilotage.

#### Description

L'objet métier BO-06 : Exploitation & gestion structure et pilote les concepts de données suivants, garants de la cohérence métier de la prise en charge. Il alimente les flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md) et s'inscrit dans la continuité des chapitres ARTSN (médiation et normalisation, échange et résidence).

#### Objets de données réalisés (ARTSN)

- [DO-23 : Formation sanitaire](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-23.md)
- [DO-24 : Agent de santé](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-24.md)
- [DO-25 : Indicateur sanitaire](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-25.md)
- [DO-26 : Zone sanitaire](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-26.md)
- [DO-27 : Tâche](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-27.md)
- [DO-28 : Tableau de bord](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-28.md)

#### Flux de valeur

- [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md)
- [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md)
- [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md)
- [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)

#### Réalise (ARTSN)

- **Dictionnaire de données fonctionnelles** : [Dictionnaire de données fonctionnelles](../../02_artsn/03_objets-de-donnees/index.md)

<!-- END:GENERATED -->

## 07. Interopérabilité transfrontalière

<!-- BEGIN:GENERATED mode=catalogue source=04_architecture-repository/02_architecture-elements/business/business-objects/bo-07.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### BO-07 : Interopérabilité transfrontalière

Résumé patient international, sections et confiance pour les échanges hors frontières.

#### Description

L'objet métier BO-07 : Interopérabilité transfrontalière structure et pilote les concepts de données suivants, garants de la cohérence métier de la prise en charge. Il alimente les flux de valeur [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md) et s'inscrit dans la continuité des chapitres ARTSN (médiation et normalisation, échange et résidence).

#### Objets de données réalisés (ARTSN)

- [DO-29 : Résumé international du patient](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-29.md)
- [DO-30 : Section du résumé](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-30.md)
- [DO-31 : Confiance internationale](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-31.md)

#### Flux de valeur

- [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md)

#### Réalise (ARTSN)

- **Dictionnaire de données fonctionnelles** : [Dictionnaire de données fonctionnelles](../../02_artsn/03_objets-de-donnees/index.md)

<!-- END:GENERATED -->

## Liens

- Domaines de données prioritaires (`00_caesn/04_data/domains.md`)
- Objets de données de l'ARTSN (`../../02_artsn/03_objets-de-donnees/index.md`)

## Références

- **Domaines de données** : Domaines de données prioritaires (`00_caesn/04_data/domains.md`)
- **Objets de données ARTSN** : Objets de données (`../../02_artsn/03_objets-de-donnees/index.md`)
- **Chapitre ART-2 (médiation)** : Médiation et normalisation (`../../04_architecture-repository/04_patterns/artsn-rules/art-2.md`)
