---
title: Cadre d'Architecture d'Entreprise de la Santé Numérique
description: Architecture d'entreprise du secteur santé numérique de Madagascar, documentée as code
version: "0.1.0"
status: draft
last_reviewed: 2026-08-07
review_cycle: quarterly
owner: Bureau de Réalisation de la Valeur
---

# Cadre d'Architecture d'Entreprise de la Santé Numérique

Ce dépôt contient la documentation d'architecture du secteur santé numérique de Madagascar, organisée selon la hiérarchie documentaire du [CAESN](00_framework/overview/index.md) en **trois familles de documents** : cadre, architecture de référence technique et spécifications d'implémentation. L'ensemble est documenté *as code* : Markdown structuré avec frontmatter YAML, versionné et relisible par machine.

L'approche est celle d'une **Value-Driven Enterprise Architecture** : partir des résultats attendus pour les bénéficiaires et remonter vers les capabilités et les technologies nécessaires pour les produire.

## Structure (3 familles)

| Niveau | Dossier | Document | Destinataires |
|--------|---------|----------|---------------|
| 1 | [`00_framework/`](./00_framework/) | Cadre d'Architecture d'Entreprise : valeur, capabilités, principes, gouvernance | Décideurs, directions métiers, partenaires |
| 2 | [`01_reference-technique/`](./01_reference-technique/) | Architecture de Référence Technique : standards, solutions, homologation | DEPSI, architectes, intégrateurs |
| 3 | [`02_implementations/`](./02_implementations/) | Spécifications par initiative : API, contrats d'interfaces, configurations | Développeurs, fournisseurs, équipes techniques |

### Niveau 1 — `00_framework/` (CAESN)

| Domaine | Chemin | Contenu |
|---------|--------|---------|
| Vue d'ensemble | [`00_framework/overview/`](./00_framework/overview/) | Fondements stratégiques, modèle national de valeur |
| Flux de valeur | [`00_framework/value-streams/`](./00_framework/value-streams/) | Flux de valeur nationaux de santé (VS-01 à VS-04) |
| Principes | [`00_framework/principles/`](./00_framework/principles/) | Principes transversaux (PA) et de domaine (PD) |
| Capabilités | [`00_framework/capabilities/`](./00_framework/capabilities/) | Capabilités CAP-01..16, maturité, runway |
| Données | [`00_framework/data/`](./00_framework/data/) | Architecture des données et de l'information sanitaire |
| Applications | [`00_framework/application/`](./00_framework/application/) | Architecture applicative et systèmes numériques |
| Portefeuille | [`00_framework/portfolio/`](./00_framework/portfolio/) | Portefeuille d'initiatives orienté valeur |
| Gouvernance | [`00_framework/governance/`](./00_framework/governance/) | Instances, RACI, Bureau de Réalisation de la Valeur |
| Décisions | [`00_framework/decisions/`](./00_framework/decisions/) | Architecture Decision Records (ADR) |
| Normes | [`00_framework/standards/`](./00_framework/standards/) | Normes obligatoires et standards recommandés |
| Annexes | [`00_framework/annexes/`](./00_framework/annexes/) | Matrice de lecture, glossaire, acronymes |

## Conventions

- Chaque fichier inclut un frontmatter YAML (title, id, domain, version, status, last_reviewed, owner, tags)
- Les références croisées utilisent des liens Markdown relatifs
- Les ADR suivent le [modèle de décision](00_framework/decisions/adr-0000-template.md)
- Les normes suivent le [modèle de norme](00_framework/standards/std-0000-template.md)
- Statuts : `draft`, `review`, `approved`, `deprecated`, `superseded`
- Les tags et identifiants utilisent le kebab-case

## Guide de lecture

La [matrice de lecture par profil](00_framework/annexes/reading-matrix.md) indique quelles sections lire selon le profil (décideurs institutionnels, directions métier, DEPSI / équipes techniques, SIS / données, partenaires techniques et financiers).

## Liens utiles

- [Modèle de valeur](00_framework/overview/value-model.md)
- [Registre national des initiatives](00_framework/portfolio/index.md)
- [Gouvernance](00_framework/governance/index.md)
- [Glossaire](00_framework/annexes/glossary.md)