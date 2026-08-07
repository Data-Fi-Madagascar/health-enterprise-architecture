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

Ce dépôt contient la documentation d'architecture du secteur santé numérique de Madagascar, organisée selon la hiérarchie documentaire du [CAESN](framework/overview/index.md) en **trois familles de documents** : cadre, architecture de référence technique et spécifications d'implémentation. L'ensemble est documenté *as code* : Markdown structuré avec frontmatter YAML, versionné et relisible par machine.

L'approche est celle d'une **Value-Driven Enterprise Architecture** : partir des résultats attendus pour les bénéficiaires et remonter vers les capabilités et les technologies nécessaires pour les produire.

## Structure (3 familles)

| Niveau | Dossier | Document | Destinataires |
|--------|---------|----------|---------------|
| 1 | [`framework/`](./framework/) | Cadre d'Architecture d'Entreprise : valeur, capabilités, principes, gouvernance | Décideurs, directions métiers, partenaires |
| 2 | [`reference-technique/`](./reference-technique/) | Architecture de Référence Technique : standards, solutions, homologation | DEPSI, architectes, intégrateurs |
| 3 | [`implementations/`](./implementations/) | Spécifications par initiative : API, contrats d'interfaces, configurations | Développeurs, fournisseurs, équipes techniques |

### Niveau 1 — `framework/` (CAESN)

| Domaine | Chemin | Contenu |
|---------|--------|---------|
| Vue d'ensemble | [`framework/overview/`](./framework/overview/) | Fondements stratégiques, modèle national de valeur |
| Flux de valeur | [`framework/value-streams/`](./framework/value-streams/) | Flux de valeur nationaux de santé (VS-01 à VS-04) |
| Principes | [`framework/principles/`](./framework/principles/) | Principes transversaux (PA) et de domaine (PD) |
| Capabilités | [`framework/capabilities/`](./framework/capabilities/) | Capabilités CAP-01..16, maturité, runway |
| Données | [`framework/data/`](./framework/data/) | Architecture des données et de l'information sanitaire |
| Applications | [`framework/application/`](./framework/application/) | Architecture applicative et systèmes numériques |
| Portefeuille | [`framework/portfolio/`](./framework/portfolio/) | Portefeuille d'initiatives orienté valeur |
| Gouvernance | [`framework/governance/`](./framework/governance/) | Instances, RACI, Bureau de Réalisation de la Valeur |
| Décisions | [`framework/decisions/`](./framework/decisions/) | Architecture Decision Records (ADR) |
| Normes | [`framework/standards/`](./framework/standards/) | Normes obligatoires et standards recommandés |
| Annexes | [`framework/annexes/`](./framework/annexes/) | Matrice de lecture, glossaire, acronymes |

## Conventions

- Chaque fichier inclut un frontmatter YAML (title, id, domain, version, status, last_reviewed, owner, tags)
- Les références croisées utilisent des liens Markdown relatifs
- Les ADR suivent le [modèle de décision](framework/decisions/adr-0000-template.md)
- Les normes suivent le [modèle de norme](framework/standards/std-0000-template.md)
- Statuts : `draft`, `review`, `approved`, `deprecated`, `superseded`
- Les tags et identifiants utilisent le kebab-case

## Guide de lecture

La [matrice de lecture par profil](framework/annexes/reading-matrix.md) indique quelles sections lire selon le profil (décideurs institutionnels, directions métier, DEPSI / équipes techniques, SIS / données, partenaires techniques et financiers).

## Liens utiles

- [Modèle de valeur](framework/overview/value-model.md)
- [Registre national des initiatives](framework/portfolio/index.md)
- [Gouvernance](framework/governance/index.md)
- [Glossaire](framework/annexes/glossary.md)