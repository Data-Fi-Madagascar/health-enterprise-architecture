---
title: "ADR-0003 — Utilisation de HL7 FHIR comme standard d'interopérabilité"
id: adr-0003
domain: 08_decisions
version: "0.1.0"
status: accepté
date: 2026-07-01
owner: DEPSI
tags: [adr, interopérabilité, fhir, normes]
---

# ADR-0003 — Utilisation de HL7 FHIR comme standard d'interopérabilité

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ○ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

- **Statut** : accepté
- **Date** : 2026-07-01
- **Groupe concerné** : DEPSI, développeurs, intégrateurs

## Contexte

L'interopérabilité sanitaire nécessite un standard de données commun pour l'échange, le stockage et l'exposition des informations de santé. Les systèmes existants utilisent des formats variés (HL7 v2, XML, CSV, JSON propriétaire) ce qui fragmente l'écosystème et complique les intégrations.

HL7 FHIR (Fast Healthcare Interoperability Resources) est le standard moderne pour les données de santé, reconnu par l'OMS, l'IHE et les principaux systèmes d'information sanitaire mondiaux.

## Décision

Adopter **HL7 FHIR** comme standard national pour la modélisation, l'échange et l'exposition des données de santé, en complément des profils IHE existants.

## Justification

FHIR répond aux exigences de l'ARTSN :

- **ART-2** : Médiation et normalisation sémantique
- **ART-4** : Référentiels nationaux
- **F.2** : Fondation de normalisation
- **F.3** : Fondation d'interopérabilité

Il offre :
- Une API REST légère et moderne
- Un modèle de données basé sur des ressources modulaires
- Un mécanisme de profiling pour les besoins nationaux
- Une large communauté internationale et des outils open source

## Conséquences

### Positives
- Standard international reconnu et maintenu
- API REST moderne et facile à implémenter
- Modulaire et extensible selon les besoins nationaux
- Large écosystème d'outils et de bibliothèques

### Négatives
- Nécessite la formation des développeurs
- Complexité du profiling national
- Coût de migration des systèmes existants
- Nécessite un registre de schémas national

## Alternatives considérées

| Alternative | Raison du refus |
|-------------|-----------------|
| HL7 v2 | Standard ancien, pas de API REST |
| CDA (Clinical Document Architecture) | Orienté documents, pas ressources |
| OpenEHR | Modèle différent, moins de traction internationale |

## Références

- [ARTSN — Fondation F.2](../../referentiel/fondations/f-2.md)
- [ARTSN — Fondation F.3](../../referentiel/fondations/f-3.md)
- [ARTSN — Chapitre ART-2](../../02_artsn/03_chapitres/art-2-mediation-normalisation.md)
- [Dictionnaire de données](../../02_artsn/05_dictionnaire/index.md)
