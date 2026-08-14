---
title: Architecture de Référence Technique de la Santé Numérique (ARTSN)
id: artsn
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, niveau-3, standards]
---

# Architecture de Référence Technique de la Santé Numérique (ARTSN)

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](reading-matrix.md).

## Place dans la hiérarchie documentaire

Niveau **3** de la hiérarchie du [Cadre d'Architecture d'Entreprise](../00_caesn/00_overview/index.md). Ce dossier est volontairement distinct du dossier [`00_caesn/`](../00_caesn/) qui contient le niveau 1 (valeur, capabilités, principes, gouvernance).

| Niveau | Dossier | Document |
|--------|---------|----------|
| 1 | [`00_caesn/`](../00_caesn/) | Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) |
| 2 | [`01_cnisn/`](../01_cnisn/) | Cadre National d'Interopérabilité de la Santé Numérique (CNISN) |
| 3 | [`artsn/`](./index.md) | Architecture de Référence Technique de la Santé Numérique (ce dossier) |
| 4 | [`03_ptisn/`](../03_ptisn/) | Profils techniques d'implémentation par initiative (PTISN) |

## Rôle de l'ARTSN

L'Architecture de Référence Technique décline le CAESN au niveau opérationnel et technique. Elle traduit les principes architecturaux (PA, PD, AA, DA) en **familles de patterns validées avec critères de sélection explicites**, **standards techniques et formats d'échange**, **contrats d'interfaces** et **règles d'homologation**.

Contrairement au cadre (niveau 1), l'ARTSN précise le niveau technique : standards, familles de patterns et règles d'homologation. Elle ne sélectionne pas de produits ni de configurations : ces choix d'implémentation par initiative relèvent du [PTISN (niveau 4)](../03_ptisn/index.md). Elle s'adresse au DEPSI, aux architectes et aux intégrateurs.

Points couverts :
- Standards d'échange et formats (FHIR, HL7, OpenHIE, etc.)
- Familles de patterns et composants par [couche applicative](../00_caesn/05_application/layers.md)
- Règles d'homologation et critères de conformité technique
- Modèle d'hébergement, cybersécurité, journalisation
- Normes et standards déclinés depuis [`00_caesn/09_standards/`](../00_caesn/09_standards/index.md)

## Structure du document

| Partie | Document | Objet | État |
|--------|----------|-------|------|
| I | [Fondations invariantes](00_fondations/index.md) | F.1 résilience géographique, F.2 souveraineté intersectorielle, F.3 éradication des silos, F.4 homologation obligatoire | rédigé |
| II | [Flux de valeur](01_flux-de-valeur/index.md) | VS-01 à VS-04 déclinés en exigences techniques | rédigé |
| III | [Exigences contextuelles nationales](02_exigences-contextuelles/index.md) | ENF-1 à ENF-5 | rédigé |
| IV | [Chapitres et patterns de référence](./03_chapitres/index.md) | ART-0 à ART-9 (règles d'or et contrats d'interfaces) | rédigé |
| V | [Cartographie conceptuelle cible](04_cartographie-cible/index.md) | 6 couches + 2 axes verticaux | rédigé |
| VI | [Dictionnaire de données fonctionnelles](05_dictionnaire/index.md) | Sémantique universelle interministérielle | cadre posé |
| VI | [Gouvernance de l'ARTSN](06_gouvernance/index.md) | Cycle de vie, versionnement, revue, rôle du CNASN | rédigé |
| A | [Table de maturité par chapitre](./07_annexes/a-table-de-maturite.md) | Statuts et conditions de promotion | rédigé |
| B | [Glossaire des patterns cités](./07_annexes/b-glossaire-patterns.md) | Définitions des patterns techniques | rédigé |
| C | [Renvoi CAESN et capacités candidates](./07_annexes/c-renvoi-capacites-candidates.md) | Écarts CAESN, One Health | rédigé |
| — | [Glossaire de l'ARTSN](./glossary.md) | Termes du périmètre technique | rédigé |
| — | [Acronymes de l'ARTSN](./acronyms.md) | Sigles du périmètre technique | rédigé |

## Source et version

Ce dossier est la déclinaison **as code** du document source `[Draft]TECHNICAL-Reference-Architecture-1.pdf` (version 0.1, 17/07/2026, archivé dans ce dossier). Les statuts de chapitres (Stable / Provisoire / Proposition ouverte) sont reportés tels quels dans la [table de maturité](./07_annexes/a-table-de-maturite.md).

## Liens

- [Guide de lecture de l'ARTSN](./reading-guide.md)
- [Matrice de lecture de l'ARTSN](./reading-matrix.md)
- [Glossaire de l'ARTSN](./glossary.md)
- [Acronymes de l'ARTSN](./acronyms.md)
