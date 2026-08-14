---
title: Matrice de lecture de l'ARTSN (niveau 3)
id: artsn-reading-matrix
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-09
owner: DEPSI
tags: [artsn, lecture, niveau-3, profils]
---

# Matrice de lecture de l'ARTSN (niveau 3)

Légende : **●** = lecture prioritaire, **◐** = lecture complémentaire, **○** = lecture ponctuelle.

L'ARTSN décline le niveau 1 en **familles de patterns validées**, **standards techniques et formats d'échange**, **contrats d'interfaces** et **règles d'homologation**. Elle s'adresse en priorité au DEPSI, aux architectes et aux intégrateurs ; les décideurs et directions métier ne la consultent que sur des points précis.

| Document du niveau 3 | Décideurs institutionnels | Directions métier / programmes | DEPSI / équipes techniques | SIS / données / suivi-évaluation | Partenaires techniques et financiers |
|----------------------|---------------------------|-------------------------------|----------------------------|----------------------------------|--------------------------------------|
| [Guide de lecture de l'ARTSN](./reading-guide.md) | ● | ◐ | ● | ◐ | ● |
| [Index de l'ARTSN](./index.md) | ● | ◐ | ● | ◐ | ● |
| [Partie I — Fondations invariantes](00_fondations/index.md) | ● | ◐ | ● | ◐ | ● |
| [Partie II — Flux de valeur](01_flux-de-valeur/index.md) | ◐ | ● | ● | ◐ | ◐ |
| [Partie III — Exigences contextuelles nationales](02_exigences-contextuelles/index.md) | ◐ | ◐ | ● | ◐ | ◐ |
| [Partie IV — Chapitres et patterns de référence](./03_chapitres/index.md) | ○ | ◐ | ● | ● | ◐ |
| [ART-0 — Accords de partage](../referentiel/chapitres/art-0.md) | ◐ | ● | ● | ◐ | ◐ |
| [ART-1 — Intégration et ingestion](../referentiel/chapitres/art-1.md) | ○ | ○ | ● | ● | ◐ |
| [ART-2 — Médiation et normalisation](../referentiel/chapitres/art-2.md) | ○ | ○ | ● | ● | ◐ |
| [ART-3 — Historisation événementielle](../referentiel/chapitres/art-3.md) | ○ | ○ | ● | ● | ◐ |
| [ART-4 — Référentiels de métadonnées](../referentiel/chapitres/art-4.md) | ○ | ○ | ● | ● | ◐ |
| [ART-4a — Résolution d'identité](../referentiel/chapitres/art-4a.md) | ○ | ○ | ● | ● | ◐ |
| [ART-4b — Bases d'autorisation](../referentiel/chapitres/art-4b.md) | ○ | ○ | ● | ● | ◐ |
| [ART-4c — Éligibilité et couverture](../referentiel/chapitres/art-4c.md) | ○ | ● | ● | ◐ | ◐ |
| [ART-4d — Référentiel géospatial](../referentiel/chapitres/art-4d.md) | ○ | ● | ● | ◐ | ◐ |
| [ART-5 — Cohérence et qualité des données](../referentiel/chapitres/art-5.md) | ○ | ○ | ● | ● | ◐ |
| [ART-6 — Analytique et restitution](../referentiel/chapitres/art-6.md) | ◐ | ● | ● | ● | ◐ |
| [ART-7 — Sécurité et contrôle d'accès](../referentiel/chapitres/art-7.md) | ◐ | ◐ | ● | ● | ◐ |
| [ART-8 — Orchestration de processus](../referentiel/chapitres/art-8.md) | ○ | ◐ | ● | ● | ◐ |
| [ART-8a — Orchestration de processus borné](../referentiel/chapitres/art-8a.md) | ○ | ○ | ● | ● | ◐ |
| [ART-8b — Modélisation en graphe](../referentiel/chapitres/art-8b.md) | ○ | ○ | ● | ● | ◐ |
| [ART-8c — Agrégation par lot](../referentiel/chapitres/art-8c.md) | ○ | ○ | ● | ● | ◐ |
| [ART-8d — Chorégraphie inter-institutionnelle](../referentiel/chapitres/art-8d.md) | ◐ | ● | ● | ◐ | ◐ |
| [ART-9 — Garanties transactionnelles](../referentiel/chapitres/art-9.md) | ○ | ● | ● | ◐ | ◐ |
| [Partie V — Cartographie conceptuelle cible](04_cartographie-cible/index.md) | ◐ | ◐ | ● | ● | ◐ |
| [Partie VI — Dictionnaire de données](05_dictionnaire/index.md) | ○ | ◐ | ● | ● | ◐ |
| [Partie VI — Gouvernance de l'ARTSN](06_gouvernance/index.md) | ● | ◐ | ● | ◐ | ● |
| [Annexe A — Table de maturité](./07_annexes/a-table-de-maturite.md) | ○ | ◐ | ● | ◐ | ◐ |
| [Annexe B — Glossaire des patterns](./07_annexes/b-glossaire-patterns.md) | ○ | ○ | ● | ◐ | ◐ |
| [Glossaire de l'ARTSN](./glossary.md) | ○ | ◐ | ● | ◐ | ◐ |
| [Acronymes de l'ARTSN](./acronyms.md) | ○ | ◐ | ● | ◐ | ◐ |
| [Annexe C — Renvoi CAESN et capacités candidates](./07_annexes/c-renvoi-capacites-candidates.md) | ● | ● | ● | ◐ | ● |

## Lectures croisées

- Architecture applicative (couches, composants) : [CAESN — applications](../00_caesn/05_application/index.md)
- Standards et normes déclinés : [CAESN — normes](../00_caesn/09_standards/index.md)
- Chapitres par rattachement CAESN : voir [index des chapitres](./03_chapitres/index.md) et la [table de maturité](./07_annexes/a-table-de-maturite.md)

## Matrices des autres niveaux

- [Niveau 1 — CAESN](../00_caesn/reading-matrix.md)
- [Niveau 2 — CNISN](../01_cnisn/reading-matrix.md)
- [Niveau 4 — PTISN](../03_ptisn/reading-matrix.md)

## Liens

- [Index de l'ARTSN](./index.md)
- [Glossaire de l'ARTSN](./glossary.md)
- [Acronymes de l'ARTSN](./acronyms.md)
- [Chapitres ART-0..ART-9](./03_chapitres/index.md)
- [CAESN (niveau 1)](../00_caesn/00_overview/index.md)