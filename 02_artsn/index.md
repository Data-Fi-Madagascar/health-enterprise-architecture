---
title: Architecture de Référence Technique de la Santé Numérique (ARTSN)
id: artsn
domain: 02_artsn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-18
owner: DEPSI
tags: [artsn, niveau-3, standards]
---

# Architecture de Référence Technique de la Santé Numérique (ARTSN)

## Pour qui lire ce document

**Niveau :** niveau 3 : Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## Place dans la hiérarchie documentaire

L'ARTSN constitue le troisième niveau de la hiérarchie documentaire du secteur santé. Ce dossier est volontairement distinct du dossier de premier niveau qui contient le cadre d'architecture d'entreprise avec ses value streams, capacités et gouvernance.

| Niveau | Dossier | Document |
|--------|---------|----------|
| 1 | `00_caesn/` | Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) |
| 2 | `01_cnisn/` | Cadre National d'Interopérabilité de la Santé Numérique (CNISN) + Standards |
| 3 | `artsn/` | Architecture de Référence Technique de la Santé Numérique (ce dossier) |
| 4 | `03_ptisn/` | Profils techniques d'implémentation par initiative (PTISN) : découle de l'UGD |

## Rôle de l'ARTSN

L'Architecture de Référence Technique décline le CAESN au niveau opérationnel et technique. Elle traduit les principes architecturaux en familles de patterns validées avec des critères de sélection explicites, en standards techniques et formats d'échange, en contrats d'interfaces et en règles d'homologation.

Contrairement au cadre de premier niveau, l'ARTSN précise le niveau technique : standards, familles de patterns et règles d'homologation. Elle ne sélectionne pas de produits ni de configurations : ces choix d'implémentation par initiative relèvent du PTISN de quatrième niveau. Elle s'adresse au DEPSI, aux architectes et aux intégrateurs.

L'ARTSN couvre les standards d'échange et formats (FHIR, HL7, OpenHIE, etc.), les familles de patterns et composants par couche applicative, les règles d'homologation et critères de conformité technique, le modèle d'hébergement, la cybersécurité et la journalisation, ainsi que les normes et standards déclinés depuis le CNISN.

## Structure du document

| Partie | Document | Objet | État |
|--------|----------|-------|------|
| I | Fondations invariantes | F.1 résilience géographique, F.2 souveraineté intersectorielle, F.3 éradication des silos, F.4 homologation obligatoire | rédigé |
| II | Flux de valeur | VS-01 à VS-04 déclinés en exigences techniques | rédigé |
| III | Exigences contextuelles nationales | ENF-1 à ENF-5 | rédigé |
| IV | Chapitres et patterns de référence | ART-0 à ART-11 (règles d'or et contrats d'interfaces) | rédigé |
| V | Cartographie conceptuelle cible | 6 couches + 2 axes verticaux | rédigé |
| VI | Dictionnaire de données fonctionnelles | Sémantique universelle interministérielle | cadre posé |
| VII | Gouvernance de l'ARTSN | Cycle de vie, versionnement, revue, rôle du CNASN | rédigé |
| A | Table de maturité par chapitre | Statuts et conditions de promotion | rédigé |
| B | Glossaire des patterns cités | Définitions des patterns techniques | rédigé |
| C | Renvoi CAESN et capacités candidates | Écarts CAESN, One Health | rédigé |
| : | Glossaire de l'ARTSN | Termes du périmètre technique | rédigé |
| : | Acronymes de l'ARTSN | Sigles du périmètre technique | rédigé |

## Source et version

Ce dossier est la déclinaison as code du document source `[Draft]TECHNICAL-Reference-Architecture-1.pdf` (version 0.1, 17/07/2026, archivé dans ce dossier). Les statuts de chapitres (Stable / Provisoire / Proposition ouverte) sont reportés tels quels dans la table de maturité.

## Liens

- Guide de lecture de l'ARTSN
- Matrice de lecture de l'ARTSN
- Glossaire de l'ARTSN
- Acronymes de l'ARTSN

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`artsn/`** : Architecture de Référence Technique de la Santé Numérique (ARTSN) (`02_artsn/index.md`)
- **Fondations invariantes** : Fondations de l'ARTSN (`02_artsn/00_fondations/index.md`)
- **Flux de valeur** : Flux de valeur (`02_artsn/01_flux-de-valeur/index.md`)
- **Exigences contextuelles nationales** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
- **Chapitres et patterns de référence** : Chapitres et patterns de référence (`02_artsn/03_chapitres/index.md`)
- **Cartographie conceptuelle cible** : Cartographie conceptuelle cible (`02_artsn/04_cartographie-cible/index.md`)
- **Dictionnaire de données fonctionnelles** : Dictionnaire de données fonctionnelles (`02_artsn/05_dictionnaire/index.md`)
- **Gouvernance de l'ARTSN** : Gouvernance de l'ARTSN (`02_artsn/06_gouvernance/index.md`)
- **Table de maturité par chapitre** : Annexe A : Table de maturité par chapitre (`02_artsn/07_annexes/a-table-de-maturite.md`)
- **Glossaire des patterns cités** : Annexe B : Glossaire des patterns cités (`02_artsn/07_annexes/b-glossaire-patterns.md`)
- **Renvoi CAESN et capacités candidates** : Annexe C : Renvoi CAESN et capacités candidates (`02_artsn/07_annexes/c-renvoi-capacites-candidates.md`)
- **Glossaire de l'ARTSN** : Glossaire de l'ARTSN (niveau 3) (`02_artsn/glossary.md`)
- **Acronymes de l'ARTSN** : Acronymes et abréviations de l'ARTSN (niveau 3) (`02_artsn/acronyms.md`)
- **Guide de lecture de l'ARTSN** : Guide de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-guide.md`)
- **Matrice de lecture de l'ARTSN** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
