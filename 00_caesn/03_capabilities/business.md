---
title: "Capabilités métier de santé"
id: capabilities-business
domain: 03_capabilities
version: "0.0.1"
status: draft
last_reviewed: 2026-07-03
owner: Responsables de capabilités métier
tags: [capabilités, métier, catalogue]
---

# Capabilités métier de santé

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ◐ |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.


Chaque capabilité vit dans le référentiel : `referentiel/capabilites/cap-XX.md` (rôle, flux de valeur associés).

## Catalogue des capabilités

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

### CAP-01 — Offre de soins et continuité des services

#### Rôle dans le système

La capabilité garantit que chaque citoyen accède à des services de santé essentiels, sûrs et de qualité, quel que soit son lieu de résidence ou sa situation. Elle couvre l’offre de soins à tous les niveaux de la pyramide sanitaire : disponibilité des services, accessibilité géographique et financière, continuité de la prise en charge et qualité minimale garantie. Elle conditionne le bon déroulement du parcours de soins décrit par le flux de valeur associé.

#### Flux de valeur

- VS-01

*Rattachement : VS-01 · fiche CAP-01*

### CAP-02 — Gestion du parcours patient, référence et contre-référence

#### Rôle dans le système

La capabilité organise le parcours du patient entre les points de service : orientation vers le niveau adapté, référence vers une structure plus spécialisée et contre-référence vers la formation d'origine. Elle assure que l'information clinique suit le patient d'un niveau à l'autre, afin que la continuité des soins ne dépende pas d'un seul établissement. Sans elle, les ruptures de parcours (référence sans dossier, absence de retour d'information) fragmentent la prise en charge.

#### Scénarios couverts

| Scénario | Description | Profils consommés |
|----------|-------------|-------------------|
| **Référence (S-03)** | Orientation d'un patient d'un niveau de soins vers un autre (CSB → hôpital régional) | PT-01, PT-02 |
| **Contre-référence (S-04)** | Retour du patient vers l'établissement d'origine avec compte-rendu et recommandations | PT-01, PT-02 |
| **Évacuation sanitaire nationale (S-05)** | Transfert urgent entre établissements nationaux | PT-01, PT-02, PT-11 |
| **Évacuation sanitaire internationale (S-05)** | Transfert vers un centre spécialisé à l'étranger | PT-01, PT-02, PT-11, PT-14 |

#### Flux de valeur

- VS-01

*Rattachement : VS-01, CAP-INT-03, CAP-INT-01, CAP-INT-13 · fiche CAP-02*

### CAP-03 — Qualité, sécurité des soins et amélioration continue

#### Rôle dans le système

La capabilité mesure, améliore et sécurise la qualité des services de santé. Elle relie les données de qualité (résultats, incidents, retours patients) aux mécanismes d’amélioration continue, pour que la performance se traduise en actions correctives et pas seulement en rapports. Elle alimente à la fois la qualité des soins et le pilotage du système de santé.

#### Flux de valeur

- VS-01
- VS-04

*Rattachement : VS-01, VS-04 · fiche CAP-03*

### CAP-04 — Santé communautaire et engagement des communautés

#### Rôle dans le système

La capabilité intègre les agents communautaires, les communautés et les patients comme acteurs du système de santé : prévention, alerte précoce, suivi des cas, observance des traitements et amélioration des services. Elle étend la couverture sanitaire au-delà des formations sanitaires, en particulier dans les zones où la distance et le coût limitent le recours aux soins.

#### Flux de valeur

- VS-01
- VS-02

*Rattachement : VS-01, VS-02 · fiche CAP-04*

### CAP-05 — Surveillance épidémiologique, alerte, investigation et riposte

#### Rôle dans le système

La capabilité couvre l'ensemble du cycle de gestion des risques sanitaires : détection des signaux, notification des cas, vérification, investigation, déclenchement de la riposte et retour d'expérience. Elle relie les formations sanitaires, les districts et le niveau central pour qu'une épidémie ou une urgence soit identifiée et traitée sans délai.

La capabilité inclut désormais la **dimension géospatiale** :
- **Géolocalisation des formations sanitaires** : positionnement GPS de toutes les structures de soins
- **Cartographie des risques** : visualisation spatiale des foyers épidémiques et des zones à risque
- **Suivi temporel** : analyse des tendances épidémiques par zone géographique
- **Cloisonnement One Health** : surveillance conjointe santé humaine/animale/environnement par zone

#### Flux de valeur

- VS-02

#### Rattachement ARTSN

- **ART-4d** — Référentiel géospatial et d'exploitation partagé
- **PT-05** — Profil technique géolocalisation

*Rattachement : VS-02 · fiche CAP-05*

### CAP-06 — Vaccination, prévention et promotion de la santé

#### Rôle dans le système

La capabilité prévient les maladies et promeut les comportements favorables à la santé : prévention, promotion, campagnes et suivi des interventions préventives, dont la vaccination. Elle agit en amont du soin curatif pour réduire la morbidité et éviter les dépenses évitables, et sa planification est un des leviers de l’amélioration de la santé de la population.

#### Flux de valeur

- VS-02

*Rattachement : VS-02 · fiche CAP-06*

### CAP-07 — Protection financière, couverture santé universelle

#### Rôle dans le système

La capabilité protège les ménages contre le risque financier lié aux soins : identification des bénéficiaires, vérification de leurs droits, application des mécanismes de protection financière et soutien à l’achat stratégique des services. Elle garantit que la couverture et la protection annoncées se traduisent effectivement au point de service, y compris en zone à connectivité limitée.

#### Flux de valeur

- VS-03

*Rattachement : VS-03 · fiche CAP-07*

### CAP-08 — Gouvernance institutionnelle, planification, coordination et redevabilité

#### Rôle dans le système

La capabilité assure la gouvernance du système de santé : planification, coordination, régulation, suivi et redevabilité à tous les niveaux (national, régional, district, formation). Elle transforme les données et les plans en décisions de gestion, et garantit que chaque niveau rend compte de sa performance aux instances qui l’encadrent.

#### Flux de valeur

- VS-03
- VS-04

*Rattachement : VS-03, VS-04 · fiche CAP-08*

<!-- END:GENERATED -->
## Liens

- [Capabilités](./index.md)

## Références

- **matrice de lecture** — Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
