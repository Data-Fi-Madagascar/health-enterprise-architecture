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

Ce dépôt contient la documentation d'architecture du secteur santé numérique de Madagascar, organisée selon la hiérarchie documentaire du [CAESN](00_caesn/00_overview/index.md) en **quatre familles de documents** : cadre, interopérabilité, architecture de référence technique et profils d'implémentation. L'ensemble est documenté *as code* : Markdown structuré avec frontmatter YAML, versionné et relisible par machine.

L'approche est celle d'une **Value-Driven Enterprise Architecture** : partir des résultats attendus pour les bénéficiaires et remonter vers les capabilités et les technologies nécessaires pour les produire.

## Structure (4 familles)

| Niveau | Dossier | Document | Destinataires |
|--------|---------|----------|---------------|
| 1 | [`00_caesn/`](./00_caesn/) | Cadre d'Architecture d'Entreprise de la Santé Numérique : valeur, capabilités, principes, gouvernance | Décideurs, directions métiers, partenaires |
| 2 | [`01_cnisn/`](./01_cnisn/) | Cadre National d'Interopérabilité de la Santé Numérique : standards d'échange, référentiels, profils | DEPSI, architectes, intégrateurs |
| 3 | [`02_artsn/`](./02_artsn/) | Architecture de Référence Technique de la Santé Numérique : standards, solutions, homologation | DEPSI, architectes, intégrateurs |
| 4 | [`03_ptisn/`](./03_ptisn/) | Profils techniques d'implémentation par initiative : API, contrats d'interfaces, configurations | Développeurs, fournisseurs, équipes techniques |

### Niveau 1 — `00_caesn/` (CAESN)

| Domaine | Chemin | Contenu |
|---------|--------|---------|
| Vue d'ensemble | [`00_caesn/00_overview/`](./00_caesn/00_overview/) | Fondements stratégiques, modèle national de valeur |
| Flux de valeur | [`00_caesn/01_value-streams/`](./00_caesn/01_value-streams/) | Flux de valeur nationaux de santé (VS-01 à VS-04) |
| Principes | [`00_caesn/02_principles/`](./00_caesn/02_principles/) | Principes transversaux (PA) et de domaine (PD) |
| Capabilités | [`00_caesn/03_capabilities/`](./00_caesn/03_capabilities/) | Capabilités CAP-01..16, maturité, runway |
| Données | [`00_caesn/04_data/`](./00_caesn/04_data/) | Architecture des données et de l'information sanitaire |
| Applications | [`00_caesn/05_application/`](./00_caesn/05_application/) | Architecture applicative et systèmes numériques |
| Portefeuille | [`00_caesn/06_portfolio/`](./00_caesn/06_portfolio/) | Portefeuille d'initiatives orienté valeur |
| Gouvernance | [`00_caesn/07_governance/`](./00_caesn/07_governance/) | Instances, RACI, Bureau de Réalisation de la Valeur |
| Décisions | [`00_caesn/08_decisions/`](./00_caesn/08_decisions/) | Architecture Decision Records (ADR) |
| Normes | [`00_caesn/09_standards/`](./00_caesn/09_standards/) | Normes obligatoires et standards recommandés |
| Annexes | [`00_caesn/10_annexes/`](./00_caesn/10_annexes/) | Matrice de lecture, glossaire, acronymes |

## Conventions

- Chaque fichier inclut un frontmatter YAML (title, id, domain, version, status, last_reviewed, owner, tags)
- **Règle « le nom reflète la localisation »** : le champ `domain:` porte le nom du dossier d'appartenance, préfixe numérique inclus (ex. `domain: 01_value-streams`). Voir [`AGENTS.md`](./AGENTS.md)
- Chaque document ouvre sur un bloc **« Pour qui lire ce document »** : niveaux de lecture par profil (●◐○) + renvoi à la matrice de lecture de son niveau
- Les références croisées utilisent des liens Markdown relatifs
- Les ADR suivent le [modèle de décision](00_caesn/08_decisions/adr-0000-template.md)
- Les normes suivent le [modèle de norme](00_caesn/09_standards/std-0000-template.md)
- Statuts : `draft`, `review`, `approved`, `deprecated`, `superseded`
- Les tags et identifiants utilisent le kebab-case

## Guide de lecture

Chaque niveau dispose de sa **matrice de lecture** croisant ses documents avec les profils d'utilisateur (décideurs institutionnels, directions métier, DEPSI / équipes techniques, SIS / données, partenaires techniques et financiers) :

| Niveau | Matrice de lecture |
|--------|--------------------|
| 1 — CAESN | [Matrice de lecture](00_caesn/reading-matrix.md) |
| 2 — CNISN | [Matrice de lecture](01_cnisn/reading-matrix.md) |
| 3 — ARTSN | [Matrice de lecture](02_artsn/reading-matrix.md) |
| 4 — PTISN | [Matrice de lecture](03_ptisn/reading-matrix.md) |

Chaque document commence par un bloc **« Pour qui lire ce document »** qui indique, pour les cinq profils, le niveau de lecture recommandé (● prioritaire, ◐ complémentaire, ○ ponctuelle) et renvoie à la matrice de son niveau.

## Liens utiles

- [Modèle de valeur](00_caesn/00_overview/value-model.md)
- [Registre national des initiatives](00_caesn/06_portfolio/index.md)
- [Gouvernance](00_caesn/07_governance/index.md)
- [Glossaire](00_caesn/10_annexes/glossary.md)