---

title: "Accéder à des services de santé essentiels, intégrés, équitables et de qualité"
id: caesn-VS-01
domain: 01_value-streams
version: "1.0.0"
status: draft
last_reviewed: 2026-07-03
owner: Direction des soins
tags: ["flux-de-valeur", "value-stream"]
related: ["CAP-01", "CAP-02"]
---

# Accéder à des services de santé essentiels, intégrés, équitables et de qualité

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ◐ |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

<!-- BEGIN:GENERATED mode=monographie source=04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

## Valeur produite

Un patient ou usager reçoit des soins accessibles, continus, sûrs et de qualité, quel que soit son lieu de résidence, son niveau de revenu ou son profil.

## Bénéficiaires principaux

- [PP-01: Patient et usager](../../04_architecture-repository/02_architecture-elements/motivation/stakeholders/pp-01.md)
- [PP-02: Ménage et famille](../../04_architecture-repository/02_architecture-elements/motivation/stakeholders/pp-02.md)
- [PP-04: Communauté](../../04_architecture-repository/02_architecture-elements/motivation/stakeholders/pp-04.md)
- [PP-05: Agent de santé](../../04_architecture-repository/02_architecture-elements/motivation/stakeholders/pp-05.md)
- [PP-06: Formation sanitaire](../../04_architecture-repository/02_architecture-elements/motivation/stakeholders/pp-06.md)

## Description du flux

Ce flux couvre l’ensemble du parcours d’un patient, depuis la reconnaissance d’un besoin de soins jusqu’au suivi post-traitement et à l’amélioration continue de la qualité des services reçus. Il inclut les soins préventifs, curatifs et de réhabilitation, à tous les niveaux de la pyramide sanitaire.

## Étapes de valeur

- [VS-01-01: Reconnaissance du besoin et orientation](../../04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-01.md)
- [VS-01-02: Accueil et enregistrement](../../04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-02.md)
- [VS-01-03: Consultation et diagnostic](../../04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-03.md)
- [VS-01-04: Traitement et prise en charge](../../04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-04.md)
- [VS-01-05: Référence et contre-référence](../../04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-05.md)
- [VS-01-06: Suivi et continuité des soins](../../04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-06.md)
- [VS-01-07: Amélioration de la qualité](../../04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-07.md)


## Capabilités mobilisées

- [CAP-01: Offre de soins et continuité des services](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-01.md)
- [CAP-02: Gestion du parcours patient, référence et contre-référence](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-02.md)
- [CAP-03: Qualité, sécurité des soins et amélioration continue](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-03.md)
- [CAP-04: Santé communautaire et engagement des communautés](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-04.md)
- [CAP-09: Gestion des ressources humaines en santé](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-09.md)
- [CAP-10: Gestion des médicaments, vaccins, intrants et chaîne d'approvisionnement](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-10.md)
- [CAP-11: Gestion des infrastructures, équipements et maintenance](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-11.md)
- [CAP-13: Système d'information sanitaire, données et recherche](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-13.md)
- [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-14.md)
- [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-15.md)

<!-- END:GENERATED -->

<!-- BEGIN:GENERATED mode=catalogue source=04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-01.md,04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-02.md,04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-03.md,04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-04.md,04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-05.md,04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-06.md,04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-07.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Reconnaissance du besoin et orientation

#### Objectif

Réaliser l'étape de valeur « Reconnaissance du besoin et orientation » du flux [VS-01: Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md).

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

### Accueil et enregistrement

#### Objectif

Réaliser l'étape de valeur « Accueil et enregistrement » du flux [VS-01: Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md).

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

### Consultation et diagnostic

#### Objectif

Réaliser l'étape de valeur « Consultation et diagnostic » du flux [VS-01: Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md).

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

### Traitement et prise en charge

#### Objectif

Réaliser l'étape de valeur « Traitement et prise en charge » du flux [VS-01: Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md).

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

### Référence et contre-référence

#### Objectif

Réaliser l'étape de valeur « Référence et contre-référence » du flux [VS-01: Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md).

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

### Suivi et continuité des soins

#### Objectif

Réaliser l'étape de valeur « Suivi et continuité des soins » du flux [VS-01: Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md).

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

### Amélioration de la qualité

#### Objectif

Réaliser l'étape de valeur « Amélioration de la qualité » du flux [VS-01: Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md).

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

<!-- END:GENERATED -->
## Processus métier

<!-- BEGIN:GENERATED mode=catalogue source=04_architecture-repository/02_architecture-elements/business/processes/prc-01.md,04_architecture-repository/02_architecture-elements/business/processes/prc-02.md,04_architecture-repository/02_architecture-elements/business/processes/prc-03.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Accès, orientation et admission du patient

#### Objectif

Assurer l'entrée du patient dans le système de soins : reconnaissance du besoin, orientation vers le niveau de soins approprié, accueil et enregistrement.

#### Étapes couvertes

- [VS-01-01: Reconnaissance du besoin et orientation](../../04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-01.md)
- [VS-01-02: Accueil et enregistrement](../../04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-02.md)

#### Acteurs

Patient, famille, agent de santé communautaire, personnel d'accueil, registre patient

#### Indicateurs

Taux de recours aux soins, délai moyen d'accès à une formation sanitaire, taux de dossiers ouverts, délai d'enregistrement

### Prestation des soins cliniques

#### Objectif

Assurer le cœur clinique du parcours : consultation et diagnostic, traitement et prise en charge, référence et contre-référence vers le niveau de soins supérieur.

#### Étapes couvertes

- [VS-01-03: Consultation et diagnostic](../../04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-03.md)
- [VS-01-04: Traitement et prise en charge](../../04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-04.md)
- [VS-01-05: Référence et contre-référence](../../04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-05.md)

#### Acteurs

Clinicien, dossier patient, pharmacie, laboratoire, formation sanitaire référente, formation cible, système de transport

#### Indicateurs

Taux de consultations avec diagnostic documenté, taux de disponibilité des médicaments traceurs, taux de référence complétée avec retour d'information

### Continuité, suivi et qualité des soins

#### Objectif

Garantir la continuité des soins après l'épisode et l'amélioration continue de la qualité des services : suivi du patient, observance thérapeutique et revues qualité.

#### Étapes couvertes

- [VS-01-06: Suivi et continuité des soins](../../04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-06.md)
- [VS-01-07: Amélioration de la qualité](../../04_architecture-repository/02_architecture-elements/strategy/value-stages/vs-01-07.md)

#### Acteurs

Agent de santé communautaire, clinicien, patient, gestionnaire de formation sanitaire, district, comité qualité

#### Indicateurs

Taux de patients perdus de vue, taux d'observance thérapeutique, proportion de formations sanitaires ayant réalisé une revue qualité dans le mois

<!-- END:GENERATED -->
## Liens

- [Flux de valeur](index.md)
- Capabilités

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Capabilités** : Capabilités du système de santé (`00_caesn/03_capabilities/index.md`)
