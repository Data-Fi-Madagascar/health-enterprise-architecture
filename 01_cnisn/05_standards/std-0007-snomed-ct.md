---
title: "STD-0007 : Standard terminologique : SNOMED CT"
id: std-0007
domain: 05_standards
version: "1.0.0"
status: draft
last_reviewed: 2026-08-19
owner: Comité National d'Architecture Santé Numérique
tags: [standards, terminologie, snomed-ct, recommande]
---

# STD-0007 : Standard terminologique : SNOMED CT

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

- **Type** : standard (recommandé)
- **Statut** : draft
- **ADR de référence** : À définir
- **Date d'entrée en vigueur** : : (à définir après validation par le CNASN)

## Contexte

SNOMED CT (Systematized Nomenclature of Medicine : Clinical Terms) est le référentiel terminologique clinique le plus complet au monde, reconnu par l'OMS comme norme pour l'échange de données cliniques structurées. Il est adopté par le Kenya, l'Afrique du Sud et de nombreux pays africains comme référentiel complémentaire à la CIM-10 et LOINC.

Madagascar utilise déjà la CIM-10 (STD-0006) pour les diagnostics et LOINC pour les observations de laboratoire. SNOMED CT complète ces référentiels en offrant une couverture sémantique plus fine pour les données cliniques structurées, les interactions entre concepts et le raisonnement clinique assisté.

## Énoncé

Toute solution souhaitant échanger des données cliniques structurées au-delà des diagnostics (CIM-10) et des observations (LOINC) **devrait** :

1. **Mapper les codes CIM-10 et LOINC** vers SNOMED CT lorsque des données cliniques structurées sont échangées
2. **Utiliser les concepts SNOMED CT** pour les données cliniques nécessitant une granularité supérieure à CIM-10/LOINC
3. **Fournir un service de mapping** SNOMED CT → codes locaux pour les systèmes legacy
4. **Respecter la politique de distribution SNOMED CT** de l'Organisation Internationale de Normalisation (SNOMED International)

## Champ d'application

Ce standard s'applique à :
- Les échanges de données cliniques structurées entre systèmes
- Les projets nécessitant un raisonnement clinique assisté
- Les exportations de données vers des systèmes internationaux utilisant SNOMED CT
- Les projets de recherche clinique nécessitant une terminologie normalisée

Ce standard ne remplace pas la CIM-10 (STD-0006) ni LOINC : il les complète pour des cas d'usage spécifiques nécessitant une granularité sémantique supérieure.

## Références au cadre

- **Principes** : PA-05 (Interopérabilité), PA-06 (Gouvernance des données)
- **ARTSN** : ART-2 (Médiation et normalisation), F.2 (Normalisation)
- **PTISN** : PT-07 (Terminologie et codification)
- **CNISN** : CAP-INT-11 (Qualité et réconciliation)
- **Norme existante** : STD-0006 (CIM-10 + LOINC) : SNOMED CT en complément

## Contrôle et conformité

| Critère | Vérification |
|---------|--------------|
| Mapping CIM-10 → SNOMED CT | Service de mapping disponible et fonctionnel |
| Mapping LOINC → SNOMED CT | Service de mapping disponible et fonctionnel |
| Distribution | Respect de la politique SNOMED International |
| Mise à jour | Cycle de mise à jour SNOMED CT respecté (2 éditions/an) |

## Dérogations

Les dérogations sont possibles pour :
- Les systèmes échangeant uniquement des diagnostics (CIM-10) et des observations (LOINC) sans données cliniques structurées supplémentaires
- Les programmes spécifiques avec des classifications dédiées

Toute dérogation doit être justifiée et approuvée par le Comité National.

## Références

- **Normes et standards** : Index des normes et standards (`01_cnisn/05_standards/index.md`)
- **STD-0006 : CIM-10 + LOINC** : Norme terminologique obligatoire (`01_cnisn/05_standards/std-0006-terminologie.md`)
- **PT-07 : Terminologie et codification** (`03_ptisn/03_profils/pt-07-terminologie-codification.md`)
- **ART-2 : Médiation et normalisation** (`02_artsn/03_chapitres/art-2-mediation-normalisation.md`)
