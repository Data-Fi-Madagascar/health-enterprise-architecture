---
title: "VS-01 — Accéder à des services de santé essentiels, intégrés, équitables et de qualité"
id: vs-01
domain: 01_value-streams
version: "0.0.1"
status: draft
last_reviewed: 2026-07-03
owner: Direction des soins
tags: [flux-de-valeur, value-stream]
---

# VS-01 — Accéder à des services de santé essentiels, intégrés, équitables et de qualité

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ◐ |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

<!-- BEGIN:GENERATED mode=monographie source=referentiel/flux-valeur/vs-01.md -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

## Valeur produite

Un patient ou usager reçoit des soins accessibles, continus, sûrs et de qualité, quel que soit son lieu de résidence, son niveau de revenu ou son profil.

## Bénéficiaires principaux

Patients, ménages, communautés, agents de santé, formations sanitaires.

## Description du flux

Ce flux couvre l’ensemble du parcours d’un patient, depuis la reconnaissance d’un besoin de soins jusqu’au suivi post-traitement et à l’amélioration continue de la qualité des services reçus. Il inclut les soins préventifs, curatifs et de réhabilitation, à tous les niveaux de la pyramide sanitaire.

## Étapes de valeur

| # | Étape | Ce qui entre | Ce qui sort | Qui intervient | Ruptures fréquentes | Indicateurs |
|---|-------|--------------|-------------|----------------|---------------------|-------------|
| 1 | Reconnaissance du besoin et orientation | Symptôme ou besoin ressenti par le patient | Patient orienté vers le niveau de soins approprié | Patient, famille, agent de santé communautaire | Méconnaissance des services, distance géographique, coût perçu dissuasif | Taux de recours aux soins, délai moyen d’accès à une formation sanitaire |
| 2 | Accueil et enregistrement | Patient présent à la formation sanitaire | Dossier ouvert, identité vérifiée, patient pris en charge | Personnel d’accueil, registre patient | Absence de registre, identité non vérifiable, files d’attente prolongées | Taux de dossiers ouverts, délai d’enregistrement |
| 3 | Consultation et diagnostic | Dossier ouvert, patient examiné | Diagnostic posé, plan de soins défini et documenté | Clinicien, dossier patient | Absence d’historique médical, rupture de stock d’intrants de diagnostic | Taux de consultations avec diagnostic documenté |
| 4 | Traitement et prise en charge | Plan de soins validé | Traitement administré ou prescrit et disponible | Clinicien, pharmacie, laboratoire | Ruptures de médicaments essentiels, absence de laboratoire fonctionnel | Taux de disponibilité des médicaments traceurs |
| 5 | Référence et contre-référence | Décision médicale de référer | Patient reçu au niveau supérieur avec son dossier, information retournée à la formation d’origine | Formation sanitaire référente, formation cible, système de transport | Référence effectuée sans dossier, absence de transport, absence de retour d’information | Taux de référence complétée avec retour d’information |
| 6 | Suivi et continuité des soins | Épisode de soins terminé | Patient suivi, observance thérapeutique assurée | Agent de santé communautaire, clinicien, patient | Perte de vue du patient, absence de système de rappel, dossier longitudinal absent | Taux de patients perdus de vue, taux d’observance thérapeutique |
| 7 | Amélioration de la qualité | Données issues des soins et des retours patients | Actions correctives décidées et mises en œuvre | Gestionnaire de formation sanitaire, district, comité qualité | Données collectées mais non analysées, absence de revue qualité régulière | Proportion de formations sanitaires ayant réalisé une revue qualité dans le mois |

## Capabilités mobilisées

- [CAP-01](../../referentiel/capabilites/cap-01.md)
- [CAP-02](../../referentiel/capabilites/cap-02.md)
- [CAP-03](../../referentiel/capabilites/cap-03.md)
- [CAP-04](../../referentiel/capabilites/cap-04.md)
- [CAP-09](../../referentiel/capabilites/cap-09.md)
- [CAP-10](../../referentiel/capabilites/cap-10.md)
- [CAP-11](../../referentiel/capabilites/cap-11.md)
- [CAP-13](../../referentiel/capabilites/cap-13.md)
- [CAP-14](../../referentiel/capabilites/cap-14.md)
- [CAP-15](../../referentiel/capabilites/cap-15.md)

*Rattachement : [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-02](../../referentiel/capabilites/cap-02.md), [CAP-03](../../referentiel/capabilites/cap-03.md), [CAP-04](../../referentiel/capabilites/cap-04.md), [CAP-09](../../referentiel/capabilites/cap-09.md), [CAP-10](../../referentiel/capabilites/cap-10.md), [CAP-11](../../referentiel/capabilites/cap-11.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-15](../../referentiel/capabilites/cap-15.md), [PP-01](../../referentiel/parties-prenantes/pp-01.md), [PP-02](../../referentiel/parties-prenantes/pp-02.md), [PP-04](../../referentiel/parties-prenantes/pp-04.md), [PP-05](../../referentiel/parties-prenantes/pp-05.md), [PP-06](../../referentiel/parties-prenantes/pp-06.md) · [fiche](../../referentiel/flux-valeur/vs-01.md)*

<!-- END:GENERATED -->
## Processus métier

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/processus/prc-01.md,referentiel/processus/prc-02.md,referentiel/processus/prc-03.md,referentiel/processus/prc-04.md,referentiel/processus/prc-05.md,referentiel/processus/prc-06.md,referentiel/processus/prc-07.md -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

### PRC-01 — Reconnaissance du besoin et orientation

#### Objectif

Réaliser l'étape de valeur « Reconnaissance du besoin et orientation » du flux VS-01.

#### Entrées

Symptôme ou besoin ressenti par le patient

#### Sorties

Patient orienté vers le niveau de soins approprié

#### Acteurs

Patient, famille, agent de santé communautaire

#### Ruptures fréquentes

Méconnaissance des services, distance géographique, coût perçu dissuasif

#### Indicateurs

Taux de recours aux soins, délai moyen d'accès à une formation sanitaire

*Rattachement : [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-04](../../referentiel/capabilites/cap-04.md) · [fiche](../../referentiel/processus/prc-01.md)*

### PRC-02 — Accueil et enregistrement

#### Objectif

Réaliser l'étape de valeur « Accueil et enregistrement » du flux VS-01.

#### Entrées

Patient présent à la formation sanitaire

#### Sorties

Dossier ouvert, identité vérifiée, patient pris en charge

#### Acteurs

Personnel d'accueil, registre patient

#### Ruptures fréquentes

Absence de registre, identité non vérifiable, files d'attente prolongées

#### Indicateurs

Taux de dossiers ouverts, délai d'enregistrement

*Rattachement : [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-15](../../referentiel/capabilites/cap-15.md) · [fiche](../../referentiel/processus/prc-02.md)*

### PRC-03 — Consultation et diagnostic

#### Objectif

Réaliser l'étape de valeur « Consultation et diagnostic » du flux VS-01.

#### Entrées

Dossier ouvert, patient examiné

#### Sorties

Diagnostic posé, plan de soins défini et documenté

#### Acteurs

Clinicien, dossier patient

#### Ruptures fréquentes

Absence d'historique médical, rupture de stock d'intrants de diagnostic

#### Indicateurs

Taux de consultations avec diagnostic documenté

*Rattachement : [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-13](../../referentiel/capabilites/cap-13.md) · [fiche](../../referentiel/processus/prc-03.md)*

### PRC-04 — Traitement et prise en charge

#### Objectif

Réaliser l'étape de valeur « Traitement et prise en charge » du flux VS-01.

#### Entrées

Plan de soins validé

#### Sorties

Traitement administré ou prescrit et disponible

#### Acteurs

Clinicien, pharmacie, laboratoire

#### Ruptures fréquentes

Ruptures de médicaments essentiels, absence de laboratoire fonctionnel

#### Indicateurs

Taux de disponibilité des médicaments traceurs

*Rattachement : [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-10](../../referentiel/capabilites/cap-10.md), [CAP-11](../../referentiel/capabilites/cap-11.md) · [fiche](../../referentiel/processus/prc-04.md)*

### PRC-05 — Référence et contre-référence

#### Objectif

Réaliser l'étape de valeur « Référence et contre-référence » du flux VS-01.

#### Entrées

Décision médicale de référer

#### Sorties

Patient reçu au niveau supérieur avec son dossier, information retournée à la formation d'origine

#### Acteurs

Formation sanitaire référente, formation cible, système de transport

#### Ruptures fréquentes

Référence effectuée sans dossier, absence de transport, absence de retour d'information

#### Indicateurs

Taux de référence complétée avec retour d'information

*Rattachement : [CAP-02](../../referentiel/capabilites/cap-02.md) · [fiche](../../referentiel/processus/prc-05.md)*

### PRC-06 — Suivi et continuité des soins

#### Objectif

Réaliser l'étape de valeur « Suivi et continuité des soins » du flux VS-01.

#### Entrées

Épisode de soins terminé

#### Sorties

Patient suivi, observance thérapeutique assurée

#### Acteurs

Agent de santé communautaire, clinicien, patient

#### Ruptures fréquentes

Perte de vue du patient, absence de système de rappel, dossier longitudinal absent

#### Indicateurs

Taux de patients perdus de vue, taux d'observance thérapeutique

*Rattachement : [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-02](../../referentiel/capabilites/cap-02.md) · [fiche](../../referentiel/processus/prc-06.md)*

### PRC-07 — Amélioration de la qualité

#### Objectif

Réaliser l'étape de valeur « Amélioration de la qualité » du flux VS-01.

#### Entrées

Données issues des soins et des retours patients

#### Sorties

Actions correctives décidées et mises en œuvre

#### Acteurs

Gestionnaire de formation sanitaire, district, comité qualité

#### Ruptures fréquentes

Données collectées mais non analysées, absence de revue qualité régulière

#### Indicateurs

Proportion de formations sanitaires ayant réalisé une revue qualité dans le mois

*Rattachement : [CAP-03](../../referentiel/capabilites/cap-03.md), [CAP-13](../../referentiel/capabilites/cap-13.md) · [fiche](../../referentiel/processus/prc-07.md)*

<!-- END:GENERATED -->
## Liens

- [Flux de valeur](./index.md)
- [Capabilités](../03_capabilities/index.md)
