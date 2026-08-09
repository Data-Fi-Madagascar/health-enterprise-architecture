---
title: Matrice de lecture de l'ARTSN (niveau 3)
id: artsn-reading-matrix
domain: 02_artsn
version: "0.1.0"
status: draft
last_reviewed: 2026-08-09
owner: DEPSI
tags: [artsn, lecture, niveau-3, profils]
---

# Matrice de lecture de l'ARTSN (niveau 3)

Légende : **●** = lecture prioritaire, **◐** = lecture complémentaire, **○** = lecture ponctuelle.

L'ARTSN décline le niveau 1 en **standards techniques précis**, **solutions logicielles**, **configurations** et **règles d'homologation**. Elle s'adresse en priorité au DEPSI, aux architectes et aux intégrateurs ; les décideurs et directions métier ne la consultent que sur des points précis.

| Document du niveau 3 | Décideurs institutionnels | Directions métier / programmes | DEPSI / équipes techniques | SIS / données / suivi-évaluation | Partenaires techniques et financiers |
|----------------------|---------------------------|-------------------------------|----------------------------|----------------------------------|--------------------------------------|
| [Index de l'ARTSN](./index.md) | ● | ◐ | ● | ◐ | ● |
| [Partie I — Fondations invariantes](./00_fondations.md) | ● | ◐ | ● | ◐ | ● |
| [Partie II — Flux de valeur](./01_flux-de-valeur.md) | ◐ | ● | ● | ◐ | ◐ |
| [Partie III — Exigences contextuelles nationales](./02_exigences-contextuelles.md) | ◐ | ◐ | ● | ◐ | ◐ |
| [Partie IV — Chapitres et patterns de référence](./03_chapitres/index.md) | ○ | ◐ | ● | ● | ◐ |
| [ART-0 — Accords de partage](./03_chapitres/art-0-accords-partage.md) | ◐ | ● | ● | ◐ | ◐ |
| [ART-1 — Intégration et ingestion](./03_chapitres/art-1-integration-ingestion.md) | ○ | ○ | ● | ● | ◐ |
| [ART-2 — Médiation et normalisation](./03_chapitres/art-2-mediation-normalisation.md) | ○ | ○ | ● | ● | ◐ |
| [ART-3 — Historisation événementielle](./03_chapitres/art-3-historisation-evenementielle.md) | ○ | ○ | ● | ● | ◐ |
| [ART-4 — Référentiels de métadonnées](./03_chapitres/art-4-referentiels-metadonnees.md) | ○ | ○ | ● | ● | ◐ |
| [ART-4a — Résolution d'identité](./03_chapitres/art-4a-resolution-identite.md) | ○ | ○ | ● | ● | ◐ |
| [ART-4b — Bases d'autorisation](./03_chapitres/art-4b-bases-autorisation.md) | ○ | ○ | ● | ● | ◐ |
| [ART-4c — Éligibilité et couverture](./03_chapitres/art-4c-eligibilite-couverture.md) | ○ | ● | ● | ◐ | ◐ |
| [ART-4d — Référentiel géospatial](./03_chapitres/art-4d-referentiel-geospatial.md) | ○ | ● | ● | ◐ | ◐ |
| [ART-5 — Cohérence et qualité des données](./03_chapitres/art-5-coherence-qualite-donnees.md) | ○ | ○ | ● | ● | ◐ |
| [ART-6 — Analytique et restitution](./03_chapitres/art-6-analytique-restitution.md) | ◐ | ● | ● | ● | ◐ |
| [ART-7 — Sécurité et contrôle d'accès](./03_chapitres/art-7-securite-controle-acces.md) | ◐ | ◐ | ● | ● | ◐ |
| [ART-8 — Orchestration de processus](./03_chapitres/art-8-orchestration-processus-borne.md) | ○ | ◐ | ● | ● | ◐ |
| [ART-8a — Orchestration de processus borné](./03_chapitres/art-8a-orchestration-processus-borne.md) | ○ | ○ | ● | ● | ◐ |
| [ART-8b — Modélisation en graphe](./03_chapitres/art-8b-modelisation-graphe.md) | ○ | ○ | ● | ● | ◐ |
| [ART-8c — Agrégation par lot](./03_chapitres/art-8c-agregation-par-lot.md) | ○ | ○ | ● | ● | ◐ |
| [ART-8d — Chorégraphie inter-institutionnelle](./03_chapitres/art-8d-choregraphie-interinstitutionnelle.md) | ◐ | ● | ● | ◐ | ◐ |
| [ART-9 — Garanties transactionnelles](./03_chapitres/art-9-garanties-transactionnelles.md) | ○ | ● | ● | ◐ | ◐ |
| [Partie V — Cartographie conceptuelle cible](./04_cartographie-cible.md) | ◐ | ◐ | ● | ● | ◐ |
| [Partie VI — Dictionnaire de données](./05_dictionnaire.md) | ○ | ◐ | ● | ● | ◐ |
| [Partie VI — Gouvernance de l'ARTSN](./06_gouvernance.md) | ● | ◐ | ● | ◐ | ● |
| [Annexe A — Table de maturité](./07_annexes/a-table-de-maturite.md) | ○ | ◐ | ● | ◐ | ◐ |
| [Annexe B — Glossaire des patterns](./07_annexes/b-glossaire-patterns.md) | ○ | ○ | ● | ◐ | ◐ |
| [Annexe C — Renvoi CAESN et capacités candidates](./07_annexes/c-renvoi-capacites-candidates.md) | ● | ● | ● | ◐ | ● |

## Lectures croisées

- Architecture applicative (couches, composants) : [CAESN — applications](../00_caesn/05_application/index.md)
- Standards et normes déclinés : [CAESN — normes](../00_caesn/09_standards/index.md)
- Chapitres par rattachement CAESN : voir [index des chapitres](./03_chapitres/index.md) et la [table de maturité](./07_annexes/a-table-de-maturite.md)

## Matrices des autres niveaux

- [Niveau 1 — CAESN](../00_caesn/10_annexes/reading-matrix.md)
- [Niveau 2 — CNISN](../01_cnisn/reading-matrix.md)
- [Niveau 4 — PTISN](../03_ptisn/reading-matrix.md)

## Liens

- [Index de l'ARTSN](./index.md)
- [Chapitres ART-0..ART-9](./03_chapitres/index.md)
- [CAESN (niveau 1)](../00_caesn/00_overview/index.md)