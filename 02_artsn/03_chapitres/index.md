---
title: Chapitres et patterns de référence (ART-0 à ART-9)
id: artsn-chapitres
domain: 02_artsn
version: "0.1.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, patterns, niveau-3]
---

# Chapitres et patterns de référence

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

La Partie IV de l'ARTSN définit l'ensemble des **règles d'or et des contrats techniques d'interfaces obligatoires** imposés pour surmonter les contraintes contextuelles nationales décrites en [Partie III](../02_exigences-contextuelles.md). Les chapitres constituent le **cadre normatif opposable** par le Ministère de la Santé Publique pour valider ou rejeter toute solution numérique.

## Vue d'ensemble

| Chapitre | Intitulé | Rattachement CAESN | Statut |
|----------|----------|--------------------|--------|
| [ART-0](./art-0-accords-partage.md) | Accords de partage inter-institutionnels | Capacité candidate (coordination intersectorielle) | Proposition ouverte |
| [ART-1](./art-1-integration-ingestion.md) | Intégration et ingestion | CAP-14 | Stable |
| [ART-2](./art-2-mediation-normalisation.md) | Médiation et normalisation | CAP-14 | Stable |
| [ART-3](./art-3-historisation-evenementielle.md) | Historisation événementielle et profils de déploiement | CAP-13 | Stable |
| [ART-4](./art-4-referentiels-metadonnees.md) | Référentiels de métadonnées de gestion | CAP-14 | Stable |
| [ART-4a](./art-4a-resolution-identite.md) | Résolution d'identité | CAP-04bis | Provisoire |
| [ART-4b](./art-4b-bases-autorisation.md) | Bases d'autorisation | CAP-04bis, CAP-15 | Provisoire |
| [ART-4c](./art-4c-eligibilite-couverture.md) | Éligibilité et couverture | CAP-07 | Proposition ouverte |
| [ART-4d](./art-4d-referentiel-geospatial.md) | Référentiel géospatial et d'exploitation partagé | Capacité candidate (surveillance spatio-temporelle) | Proposition ouverte |
| [ART-5](./art-5-coherence-qualite-donnees.md) | Cohérence et qualité des données | CAP-13 | Stable / Proposition ouverte |
| [ART-6](./art-6-analytique-restitution.md) | Analytique et restitution | CAP-13, CAP-08 | Provisoire |
| [ART-7](./art-7-securite-controle-acces.md) | Sécurité, contrôle d'accès et résidence de la donnée | CAP-15 | Stable |
| [ART-8](./art-8-orchestration-processus-borne.md) | Orchestration de processus borné | CAP-13, CAP-14 | — |
| [ART-8a](./art-8a-orchestration-processus-borne.md) | Orchestration de processus borné | CAP-13, CAP-14 | Provisoire |
| [ART-8b](./art-8b-modelisation-graphe.md) | Modélisation de relations en graphe | CAP-13, CAP-14 | Proposition ouverte |
| [ART-8c](./art-8c-agregation-par-lot.md) | Agrégation par lot | CAP-13, CAP-14 | Proposition ouverte |
| [ART-8d](./art-8d-choregraphie-interinstitutionnelle.md) | Chorégraphie inter-institutionnelle | CAP-13, CAP-14 | Proposition ouverte |
| [ART-9](./art-9-garanties-transactionnelles.md) | Garanties transactionnelles fortes | CAP-07 | Proposition ouverte |

## Statuts

Les chapitres évoluent selon trois statuts : **Stable** (contrat pleinement opposable lors d'une homologation), **Provisoire** (oriente la conception sans être un contrat opposable) et **Proposition ouverte** (hypothèse à confirmer par une ou plusieurs initiatives indépendantes). Voir la [table de maturité](../07_annexes/a-table-de-maturite.md) et la [gouvernance](../06_gouvernance.md).

## Liens

- [Fondations](../00_fondations.md)
- [Flux de valeur](../01_flux-de-valeur.md)
- [Exigences contextuelles nationales](../02_exigences-contextuelles.md)
- [Cartographie cible](../04_cartographie-cible.md)
