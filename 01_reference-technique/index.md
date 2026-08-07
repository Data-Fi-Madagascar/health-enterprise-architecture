---
title: Architecture de Référence Technique (ART)
id: art
domain: 01_reference-technique
version: "0.0.1"
status: draft
last_reviewed: 2026-08-07
owner: DEPSI
tags: [art, niveau-2, standards]
---

# Architecture de Référence Technique (ART)

## Place dans la hiérarchie documentaire

Niveau **2** de la hiérarchie du [Cadre d'Architecture d'Entreprise](../00_framework/00_overview/index.md). Ce dossier est volontairement distinct du dossier [`00_framework/`](../00_framework/) qui contient le niveau 1 (valeur, capabilités, principes, gouvernance).

| Niveau | Dossier | Document |
|--------|---------|----------|
| 1 | [`00_framework/`](../00_framework/) | Cadre d'Architecture d'Entreprise (CAESN) |
| 2 | [`reference-technique/`](./index.md) | Architecture de Référence Technique (ce dossier) |
| 3 | [`implementations/`](../02_implementations/) | Spécifications d'implémentation par initiative |

## Rôle de l'ART

L'Architecture de Référence Technique décline le CAESN au niveau opérationnel et technique. Elle traduit les principes architecturaux (PA, PD, AA, DA) en **standards techniques précis**, **solutions logicielles retenues**, **configurations** et **règles d'homologation**.

Contrairement au cadre (niveau 1), l'ART peut intégrer la sélection de produits, formats, API, protocoles, hébergements et configurations. Elle s'adresse au DEPSI, aux architectes et aux intégrateurs.

Points couverts (à compléter) :
- Standards d'échange et formats (FHIR, HL7, OpenHIE, etc.)
- Solutions logicielles et briques retenues pour les [couches applicatives](../00_framework/05_application/layers.md)
- Règles d'homologation et critères de conformité technique
- Modèle d'hébergement, cybersécurité, journalisation
- Normes et standards déclinés depuis [`00_framework/09_standards/`](../00_framework/09_standards/index.md)

## Structure proposée

| Document | Objet | État |
|----------|-------|------|
| (ART en cours de constitution) | Standards techniques, solutions, homologation | à rédiger |

## Liens

- [Cadre (niveau 1)](../00_framework/00_overview/index.md)
- [Implémentations (niveau 3)](../02_implementations/index.md)