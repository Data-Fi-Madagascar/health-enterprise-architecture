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

Ce dépôt contient le Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN), documenté comme architecture *as code* : Markdown structuré avec frontmatter YAML, versionné et relisible par machine. Il traduit le document source `[Draft]HEA-Framework.docx` en une structure par concepts, orientée valeur.

L'approche est celle d'une **Value-Driven Enterprise Architecture** : partir des résultats attendus pour les bénéficiaires et remonter vers les capabilités et les technologies nécessaires pour les produire.

## Structure

| Domaine | Chemin | Contenu |
|---------|--------|---------|
| Vue d'ensemble | [`overview/`](./overview/) | Fondements stratégiques, modèle national de valeur |
| Flux de valeur | [`value-streams/`](./value-streams/) | Flux de valeur nationaux de santé |
| Principes | [`principles/`](./principles/) | Principes transversaux et de domaine |
| Capabilités | [`capabilities/`](./capabilities/) | Capabilités du système de santé et maturité |
| Données | [`data/`](./data/) | Architecture des données et de l'information sanitaire |
| Applications | [`application/`](./application/) | Architecture applicative et systèmes numériques |
| Portefeuille | [`portfolio/`](./portfolio/) | Portefeuille d'initiatives orienté valeur |
| Gouvernance | [`governance/`](./governance/) | Instances, RACI, Bureau de Réalisation de la Valeur |
| Décisions | [`decisions/`](./decisions/) | Architecture Decision Records (ADR) |
| Normes | [`standards/`](./standards/) | Normes obligatoires et standards recommandés |
| Annexes | [`annexes/`](./annexes/) | Matrice de lecture, glossaire, acronymes |

## Conventions

- Chaque fichier inclut un frontmatter YAML (title, id, domain, version, status, last_reviewed, owner, tags)
- Les références croisées utilisent des liens Markdown relatifs
- Les ADR suivent le [modèle de décision](decisions/adr-0000-template.md)
- Les normes suivent le [modèle de norme](standards/std-0000-template.md)
- Statuts : `draft`, `review`, `approved`, `deprecated`, `superseded`
- Les tags et identifiants utilisent le kebab-case

## Guide de lecture

La [matrice de lecture par profil](annexes/reading-matrix.md) indique quelles sections lire selon le profil (décideurs institutionnels, directions métier, DEPSI / équipes techniques, SIS / données, partenaires techniques et financiers).

## Liens utiles

- [Modèle de valeur](overview/value-model.md)
- [Registre national des initiatives](portfolio/index.md)
- [Gouvernance](governance/index.md)
- [Glossaire](annexes/glossary.md)