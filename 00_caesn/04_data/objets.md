---
title: Thèmes de données
id: data-themes
domain: 04_data
version: "1.1.0"
status: draft
last_reviewed: 2026-11-21
owner: Cellule du Système d'Information Sanitaire
tags: ["données", "thèmes", "caesn"]
---

# Thèmes de données

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

Les décideurs institutionnels et les directions métier y trouveront une lecture complémentaire, tandis que l'équipe DEPSI, les équipes techniques, et les équipes SIS, données et suivi-évaluation y trouveront une lecture prioritaire. Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

Ce document présente les **thèmes de données** du niveau 1 (CAESN). Un thème n'est pas un objet du référentiel : c'est une facette de classification qui rassemble des objets de données partageant une même finalité métier. Chaque objet de données de l'ARTSN porte la propriété `theme` qui l'inscrit dans l'un de ces thèmes ; le vocabulaire et l'ordre de présentation sont fixés par le référentiel d'architecture, et la partition elle-même ne se lit qu'à un seul endroit, dans la propriété `theme` de chaque objet.

Cette organisation remplace les sept « objets métier » retirés du catalogue par l'ADR-0017. Leur contenu utile n'a pas disparu : les thèmes conservent le périmètre, la description et la couverture en flux de valeur qui étaient attachés à ces objets, et les objets de données conservent leur rattachement fonctionnel.

## Vue par thème

<!-- BEGIN:GENERATED mode=theme source=04_architecture-repository/02_architecture-elements/data/data-objects/do-*.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

<a id="patient-identite"></a>

## Patient & identité

Identité de la personne prise en charge, épisodes de soins, dossier et référencements. Pilier de toute continuité de prise en charge.

**Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md)

**Dictionnaire** : [Dictionnaire de données fonctionnelles](../../02_artsn/03_objets-de-donnees/index.md#patient-identite)

| Objet de données | Tier | Système de référence |
|---|---|---|
| [DO-01 : Patient](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-01.md) | A | [CMP-11](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-11.md) |
| [DO-03 : Dossier et épisode de soins](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-03.md) | B | [CMP-08](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-08.md) |

<a id="prestation-soins"></a>

## Prestation & soins

Actes cliniques, prescriptions, références et évacuations constituant le parcours de soins.

**Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md)

**Dictionnaire** : [Dictionnaire de données fonctionnelles](../../02_artsn/03_objets-de-donnees/index.md#prestation-soins)

| Objet de données | Tier | Système de référence |
|---|---|---|
| [DO-05 : Consultation](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-05.md) | B | [CMP-19](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-19.md) |
| [DO-06 : Prescription](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-06.md) | B | [CMP-19](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-19.md) |
| [DO-07 : Référence et contre-référence](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-07.md) | B | [CMP-19](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-19.md) |
| [DO-09 : Évacuation sanitaire](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-09.md) | B | [CMP-19](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-19.md) |
| [DO-32 : Examen et résultat de laboratoire](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-32.md) | B | [CMP-19](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-19.md), [CMP-24](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-24.md) |

<a id="dispensation-produits"></a>

## Dispensation & produits

Médicaments, produits de santé, lots et stocks dispensés sur le terrain.

**Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)

**Dictionnaire** : [Dictionnaire de données fonctionnelles](../../02_artsn/03_objets-de-donnees/index.md#dispensation-produits)

| Objet de données | Tier | Système de référence |
|---|---|---|
| [DO-10 : Dispensation](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-10.md) | B | [CMP-20](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-20.md) |
| [DO-11 : Produit de santé](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-11.md) | A | [CMP-14](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-14.md) |
| [DO-12 : Lot et stock](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-12.md) | B | [CMP-23](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-23.md) |

<a id="financement-couverture"></a>

## Financement & couverture

Éligibilité, couverture, facturation et vérification financière des soins.

**Flux de valeur** : [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)

**Dictionnaire** : [Dictionnaire de données fonctionnelles](../../02_artsn/03_objets-de-donnees/index.md#financement-couverture)

| Objet de données | Tier | Système de référence |
|---|---|---|
| [DO-14 : Couverture sanitaire et éligibilité](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-14.md) | B | [CMP-12](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-12.md) |
| [DO-16 : Facturation et demande de remboursement](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-16.md) | B | [CMP-12](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-12.md) |
| [DO-17 : Demande et preuve de vérification d'éligibilité](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-17.md) | B | [CMP-12](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-12.md) |

<a id="risque-surveillance"></a>

## Risque & surveillance

Signaux, foyers, investigations et alertes de surveillance sanitaire, y compris dans une perspective One Health.

**Flux de valeur** : [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)

**Dictionnaire** : [Dictionnaire de données fonctionnelles](../../02_artsn/03_objets-de-donnees/index.md#risque-surveillance)

| Objet de données | Tier | Système de référence |
|---|---|---|
| [DO-18 : Signal, notification et alerte sanitaires](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-18.md) | B | [CMP-02](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-02.md) |
| [DO-19 : Foyer épidémique](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-19.md) | B | [CMP-02](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-02.md) |
| [DO-20 : Investigation épidémiologique](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-20.md) | B | [CMP-02](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-02.md) |

<a id="exploitation-gestion"></a>

## Exploitation & gestion

Structures, agents, indicateurs, zones et tableaux de bord de pilotage.

**Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)

**Dictionnaire** : [Dictionnaire de données fonctionnelles](../../02_artsn/03_objets-de-donnees/index.md#exploitation-gestion)

| Objet de données | Tier | Système de référence |
|---|---|---|
| [DO-23 : Formation sanitaire](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-23.md) | A | [ABB-REFERENTIEL-STRUCTURES-SERVICES](../../04_architecture-repository/05_building-blocks/abb/abb-referentiel-structures-services.md), [CMP-05](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-05.md) |
| [DO-24 : Agent de santé](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-24.md) | A | [CMP-13](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-13.md) |
| [DO-25 : Indicateur sanitaire](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-25.md) | C | [CMP-14](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-14.md) |
| [DO-26 : Zone sanitaire](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-26.md) | A | [ABB-REFERENTIEL-STRUCTURES-SERVICES](../../04_architecture-repository/05_building-blocks/abb/abb-referentiel-structures-services.md), [CMP-05](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-05.md) |
| [DO-27 : Tâche et action de suivi](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-27.md) | B | [CMP-01](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-01.md) |

<a id="interop-transfrontalier"></a>

## Interopérabilité transfrontalière

Résumé patient international, sections et confiance pour les échanges hors frontières.

**Flux de valeur** : [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md)

**Dictionnaire** : [Dictionnaire de données fonctionnelles](../../02_artsn/03_objets-de-donnees/index.md#interop-transfrontalier)

| Objet de données | Tier | Système de référence |
|---|---|---|
| [DO-29 : Résumé international du patient](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-29.md) | B | [CMP-06](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-06.md) |
| [DO-31 : Ancre de confiance](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-31.md) | A | [CMP-35](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-35.md), [CMP-36](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-36.md) |

<!-- END:GENERATED -->

## Liens

- Domaines de données prioritaires (`00_caesn/04_data/domains.md`)
- Objets de données de l'ARTSN (`../../02_artsn/03_objets-de-donnees/index.md`)

## Références

- **Domaines de données** : Domaines de données prioritaires (`00_caesn/04_data/domains.md`)
- **Objets de données ARTSN** : Objets de données (`../../02_artsn/03_objets-de-donnees/index.md`)
- **Chapitre ART-2 (médiation)** : Médiation et normalisation (`../../04_architecture-repository/04_patterns/artsn-rules/art-2.md`)
- **Vocabulaire des thèmes** : Thèmes de données (`04_architecture-repository/00_metamodel/themes.yaml`)
