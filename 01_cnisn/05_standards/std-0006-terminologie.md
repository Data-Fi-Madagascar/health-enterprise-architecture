---
title: "STD-0006 : Norme terminologique : CIM-10 + LOINC"
id: std-0006
domain: 05_standards
version: "1.0.0"
status: approved
last_reviewed: 2026-08-13
owner: Comité National d'Architecture Santé Numérique
tags: [standards, terminologie, cim-10, loinc, obligatoire]
---

# STD-0006 : Norme terminologique : CIM-10 + LOINC

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

- **Type** : norme (obligatoire)
- **Statut** : approuvé
- **ADR de référence** : ADR-0009
- **Date d'entrée en vigueur** : 2026-08-13

## Contexte

La terminologie médicale est le socle de la sémantique commune du système d'information sanitaire. Sans référentiel terminologique unifié, il est impossible de croiser les données entre systèmes, de calculer des indicateurs fiables ou d'interopérer avec les systèmes internationaux.

## Énoncé

Toute solution codant des données cliniques ou administratives **doit** :

1. **Utiliser la CIM-10** (Classification Internationale des Maladies, 10e révision) pour les diagnostics
2. **Utiliser LOINC** (Logical Observation Identifiers Names and Codes) pour les observations et résultats de laboratoire
3. **Utiliser la DCI** (Dénomination Commune Internationale) pour les médicaments
4. **Utiliser l'ATC** (Anatomical Therapeutic Chemical) pour la classification des médicaments
5. **Fournir un service de mapping** (code local → code standard) pour les systèmes legacy
6. **Mettre à jour annuellement** la CIM-10 et **trimestriellement** LOINC

## Champ d'application

Cette norme s'applique à :
- Toutes les données cliniques (diagnostics, observations, résultats)
- Toutes les données pharmaceutiques (prescriptions, dispensations, stocks)
- Le PT-07 (terminologie et codification)
- Toute exportation de données vers des systèmes internationaux

## Références au cadre

- **Principes** : PA-05 (Interopérabilité), PA-06 (Gouvernance des données)
- **ARTSN** : ART-2 (Médiation et normalisation), F.2 (Normalisation)
- **PTISN** : PT-07 (Terminologie et codification)
- **CNISN** : CAP-INT-11 (Qualité et réconciliation)

## Contrôle et conformité

| Critère | Vérification |
|---------|--------------|
| CIM-10 | Diagnostics codés en CIM-10 |
| LOINC | Observations codées en LOINC |
| DCI | Médicaments codés en DCI |
| ATC | Classification ATC utilisée |
| Mapping | Service de mapping opérationnel |
| Mise à jour | Cycle de mise à jour respecté |

## Dérogations

Les dérogations sont possibles pour :
- Les systèmes utilisant des codages locaux (migration progressive avec mapping obligatoire)
- Les programmes spécifiques avec des classifications dédiées (via médiation)

Toute dérogation doit être justifiée et approuvée par le Comité National.

## Références

- Normes et standards
- ADR-0009 : Terminologie
- PT-07 : Terminologie
- ARTSN : Chapitre ART-2

- **matrice de lecture** : Matrice de lecture du CNISN (niveau 2) (`01_cnisn/reading-matrix.md`)
