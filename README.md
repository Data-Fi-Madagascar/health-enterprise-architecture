---
title: Cadre d'Architecture d'Entreprise de la Santé Numérique
id: hea-readme
domain: root
description: Architecture d'entreprise du secteur santé numérique de Madagascar, documentée as code
version: "1.0.0"
status: approved
last_reviewed: 2026-08-13
review_cycle: quarterly
owner: Bureau de Réalisation de la Valeur
---

# Cadre d'Architecture d'Entreprise de la Santé Numérique (HEA)

Ce dépôt contient la documentation d'architecture du secteur santé numérique de Madagascar, organisée selon la hiérarchie documentaire du [CAESN](00_caesn/00_overview/index.md) en **quatre familles de documents** : cadre, interopérabilité, architecture de référence technique et profils d'implémentation. L'ensemble est documenté *as code* : Markdown structuré avec frontmatter YAML, versionné et relisible par machine.

L'approche est celle d'une **Value-Driven Enterprise Architecture** : partir des résultats attendus pour les bénéficiaires et remonter vers les capabilités et les technologies nécessaires pour les produire.

## Chiffres clés

| Indicateur | Valeur |
|------------|--------|
| Flux de valeur nationaux | 4 (VS-01 à VS-04) |
| Capabilités CAESN | 18 (CAP-01..18) |
| Capabilités CNISN | 14 (7 familles) |
| Chapitres ARTSN | 12+ (ART-0 à ART-11) |
| Concepts dictionnaire | 40 (7 domaines) |
| Profils PTISN | 15 (PT-01 à PT-15) |
| ADR | 9 (4 acceptées,5 proposées) |
| Standards | 6 (STD-0001..0006) + 2 normes internationales (NORM-007, NORM-008) |
| Politiques RBAC | 10 (POL-01 à POL-10) |
| Score architecture | 4.8/5 |

## Structure (4 familles + référentiel)

| Niveau | Dossier | Document | Destinataires |
|--------|---------|----------|---------------|
| 1 | [`00_caesn/`](./00_caesn/) | Cadre d'Architecture d'Entreprise de la Santé Numérique : valeur, capabilités, principes, gouvernance | Décideurs, directions métiers, partenaires |
| 2 | [`01_cnisn/`](./01_cnisn/) | Cadre National d'Interopérabilité de la Santé Numérique : principes, capacités, gouvernance, standards, décisions | DEPSI, architectes, intégrateurs |
| 3 | [`02_artsn/`](./02_artsn/) | Architecture de Référence Technique de la Santé Numérique : patterns, contrats, contraintes | DEPSI, architectes, intégrateurs |
| 4 | [`03_ptisn/`](./03_ptisn/) | Profils techniques d'implémentation par initiative : API, contrats d'interfaces, configurations (découle de l'UGD) | Développeurs, fournisseurs, équipes techniques |
| — | [`referentiel/`](./referentiel/) | Source de vérité : fondations, principes, capacités, chapitres, composants, profils | Machine, scripts de génération |

### Niveau 1 — `00_caesn/` (CAESN)

| Domaine | Chemin | Contenu |
|---------|--------|---------|
| Vue d'ensemble | [`00_overview/`](./00_caesn/00_overview/) | Fondements stratégiques, modèle national de valeur |
| Flux de valeur | [`01_value-streams/`](./00_caesn/01_value-streams/) | Flux de valeur nationaux de santé (VS-01 à VS-04) |
| Principes | [`02_principles/`](./00_caesn/02_principles/) | Principes transversaux (PA-01..12) et de domaine (PD) |
| Capabilités | [`03_capabilities/`](./00_caesn/03_capabilities/) | 18 capabilités (CAP-01..18), maturité, runway |
| Données | [`04_data/`](./00_caesn/04_data/) | Architecture des données et de l'information sanitaire |
| Applications | [`05_application/`](./00_caesn/05_application/) | Architecture applicative et systèmes numériques |
| Portefeuille | [`06_portfolio/`](./00_caesn/06_portfolio/) | Portefeuille d'initiatives orienté valeur, migration existant |
| Gouvernance | [`07_governance/`](./00_caesn/07_governance/) | Instances, RACI, homologation, processus gouvernance |
| Annexes | [`10_annexes/`](./00_caesn/10_annexes/) | Matrice de lecture, glossaire, acronymes |

> **Note :** Les Décisions (ADR) et Standards sont désormais dans le CNISN (niveau 2), dans les dossiers `01_cnisn/06_decisions/` et `01_cnisn/05_standards/`.

### Niveau 2 — `01_cnisn/` (CNISN)

| Domaine | Chemin | Contenu |
|---------|--------|---------|
| Introduction | [`00_introduction/`](./01_cnisn/00_introduction/) | Contexte, périmètre, objectifs, articulation UGD |
| Principes | [`01_principes/`](./01_cnisn/01_principes/) | Principes d'interopérabilité |
| Capacités | [`02_capacites/`](./01_cnisn/02_capacites/) | 14 capabilités interopérabilité (7 familles) |
| Gouvernance | [`03_gouvernance/`](./01_cnisn/03_gouvernance/) | Gouvernance de l'interopérabilité |
| Conformité | [`04_conformite/`](./01_cnisn/04_conformite/) | Conformité et audit |
| Standards | [`05_standards/`](./01_cnisn/05_standards/) | 6 normes obligatoires + 2 normes internationales |
| Décisions | [`06_decisions/`](./01_cnisn/06_decisions/) | 9 Architecture Decision Records (ADR-0001..0009) |
| Trajectoire | [`05_trajectoire/`](./01_cnisn/05_trajectoire/) | 7 phases T4 2026–T2 2030 |
| Indicateurs | [`06_indicateurs/`](./01_cnisn/06_indicateurs/) | KPIs interopérabilité |
| Annexes | [`08_annexes/`](./01_cnisn/08_annexes/) | Matrices de lecture, articulation CAESN/ARTSN |

### Niveau 3 — `02_artsn/` (ARTSN)

| Domaine | Chemin | Contenu |
|---------|--------|---------|
| Fondations | [`00_fondations/`](./02_artsn/00_fondations/) | Fondations architecturales |
| Flux de valeur | [`01_flux-de-valeur/`](./02_artsn/01_flux-de-valeur/) | Déclinaison technique des flux |
| Exigences | [`02_exigences-contextuelles/`](./02_artsn/02_exigences-contextuelles/) | Contraintes et exigences |
| Chapitres | [`03_chapitres/`](./02_artsn/03_chapitres/) | Chapitres ART (ART-0 à ART-11) |
| Cartographie | [`04_cartographie-cible/`](./02_artsn/04_cartographie-cible/) | Vue cible du système |
| Dictionnaire | [`05_dictionnaire/`](./02_artsn/05_dictionnaire/) | 40 concepts de données (7 domaines) |
| Gouvernance | [`06_gouvernance/`](./02_artsn/06_gouvernance/) | Veille, conformité, dépréciation |
| Annexes | [`07_annexes/`](./02_artsn/07_annexes/) | Protocole de test, SLA, maturité |
| Feuille de route | [`09_feuille-route/`](./02_artsn/09_feuille-route/) | Roadmap technique 6 phases, 98 MGA |

### Niveau 4 — `03_ptisn/` (PTISN)

| Domaine | Chemin | Contenu |
|---------|--------|---------|
| Introduction | [`00_introduction/`](./03_ptisn/00_introduction/) | Contexte et Objectifs du PTISN |
| Règles | [`01_regles-utilisation/`](./03_ptisn/01_regles-utilisation/) | Règles d'utilisation et templates |
| Topologie | [`02_topologie-nationale-cible/`](./03_ptisn/02_topologie-nationale-cible/) | Architecture réseau nationale |
| Profils | [`03_profils/`](./03_ptisn/03_profils/) | 15 profils techniques (PT-01 à PT-15) |
| Alignement | [`04_matrice-alignement/`](./03_ptisn/04_matrice-alignement/) | Matrice profils ↔ capabilités |
| Exemples | [`05_exemples/`](./03_ptisn/05_exemples/) | Exemples de profils remplis |
| Gouvernance | [`06_gouvernance/`](./03_ptisn/06_gouvernance/) | Gouvernance PTISN |
| Annexes | [`08_annexes/`](./03_ptisn/08_annexes/) | Cas d'usage VS-01..04, synthèses |

### Référentiel (source de vérité)

| Type | Chemin | Contenu |
|------|--------|---------|
| Fondations | [`referentiel/fondations/`](./referentiel/fondations/) | Fondations F-01..08 |
| Principes | [`referentiel/principes/`](./referentiel/principes/) | Principes P-01..18 |
| Capacités | [`referentiel/capacites/`](./referentiel/capacites/) | 14 capacités CNISN |
| Chapitres | [`referentiel/chapitres/`](./referentiel/chapitres/) | Chapitres ART-0..11 |
| Composants | [`referentiel/composants/`](./referentiel/composants/) | Composants logiques |
| Profils | [`referentiel/profils/`](./referentiel/profils/) | Profils PT-01..15 |
| Flux de valeur | [`referentiel/flux-valeur/`](./referentiel/flux-valeur/) | VS-01..04 |
| Étapes de valeur | [`referentiel/etapes-valeur/`](./referentiel/etapes-valeur/) | Étapes opérationnelles |

## Outils de gouvernance

| Outil | Chemin | Description |
|-------|--------|-------------|
| Registre des décisions | [`01_cnisn/06_decisions/registre-decisions.md`](./01_cnisn/06_decisions/registre-decisions.md) | Tableau central des 9 ADR |
| Template modification | [`01_cnisn/06_decisions/template-modification.md`](./01_cnisn/06_decisions/template-modification.md) | Formulaire de demande de changement |
| Processus gouvernance | [`00_caesn/07_governance/processus-gouvernance.md`](./00_caesn/07_governance/processus-gouvernance.md) | Workflows de validation |
| Homologation | [`00_caesn/07_governance/homologation.md`](./00_caesn/07_governance/homologation.md) | 12 critères, 5 phases |
| Dépréciation | [`02_artsn/06_gouvernance/depreciation.md`](./02_artsn/06_gouvernance/depreciation.md) | Processus 15 mois |
| Veille architecturale | [`02_artsn/06_gouvernance/veille-architecturale.md`](./02_artsn/06_gouvernance/veille-architecturale.md) | 7 domaines, 11 sources |
| Conformité | [`02_artsn/06_gouvernance/conformite.md`](./02_artsn/06_gouvernance/conformite.md) | Dashboard de conformité |

## Conventions

- Chaque fichier inclut un frontmatter YAML (`title`, `id`, `domain`, `version`, `status`, `last_reviewed`, `owner`, `tags`)
- **Règle « le nom reflète la localisation »** : le champ `domain:` porte le nom du dossier d'appartenance, préfixe numérique inclus (ex. `domain: 01_value-streams`). Voir [`AGENTS.md`](./AGENTS.md)
- Chaque document ouvre sur un bloc **« Pour qui lire ce document »** : niveaux de lecture par profil (●◐○) + renvoi à la matrice de lecture de son niveau
- Les références croisées utilisent des liens Markdown relatifs
- Les ADR suivent le [modèle de décision](01_cnisn/06_decisions/adr-0000-template.md)
- Statuts : `draft`, `review`, `approved`, `deprecated`, `superseded`
- Tags et identifiants en kebab-case
- Langue : français (noms de dossiers en kebab-case anglais)

## Guide de lecture

### Par profil d'utilisateur

| Profil | Parcours recommandé |
|--------|---------------------|
| **Décideur institutionnel** | CAESN overview → Flux de valeur → Gouvernance → ADR |
| **Direction métier / programme** | CAESN capabilités → CNISN trajectoire → PTISN cas d'usage |
| **DEPSI / équipes techniques** | ARTSN chapitres → Dictionnaire → PTISN profils → Protocole test |
| **SIS / données** | CNISN capacités → ARTSN dictionnaire → PTISN topologie |
| **Partenaires techniques** | CAESN portefeuille → ARTSN feuille de route → SLA |

→ [Guides de démarrage rapide](./quick-start-guides.md) pour chaque profil

### Par niveau

| Niveau | Matrice de lecture | Glossaire | Acronymes |
|--------|-------------------|-----------|-----------|
| 1 — CAESN | [Matrice](00_caesn/reading-matrix.md) | [Glossaire](00_caesn/10_annexes/glossary.md) | [Acronymes](00_caesn/10_annexes/acronyms.md) |
| 2 — CNISN | [Matrice](01_cnisn/reading-matrix.md) | [Glossaire](01_cnisn/glossary.md) | [Acronymes](01_cnisn/acronyms.md) |
| 3 — ARTSN | [Matrice](02_artsn/reading-matrix.md) | [Glossaire](02_artsn/glossary.md) | [Acronymes](02_artsn/acronyms.md) |
| 4 — PTISN | [Matrice](03_ptisn/reading-matrix.md) | [Glossaire](03_ptisn/glossary.md) | [Acronymes](03_ptisn/acronyms.md) |

### Guides de lecture détaillés

| Niveau | Guide |
|--------|-------|
| CAESN | [Guide de lecture](00_caesn/reading-guide.md) |
| CNISN | [Guide de lecture](01_cnisn/reading-guide.md) |
| ARTSN | [Guide de lecture](02_artsn/reading-guide.md) |
| PTISN | [Guide de lecture](03_ptisn/reading-guide.md) |

## Liens utiles

- [Guides de démarrage rapide](./quick-start-guides.md) — parcours pratiques par profil
- [Modèle de valeur](00_caesn/00_overview/value-model.md)
- [Registre national des initiatives](00_caesn/06_portfolio/index.md)
- [Gouvernance](00_caesn/07_governance/index.md)
- [Glossaire](00_caesn/10_annexes/glossary.md)
- [Feuille de route ARTSN](02_artsn/09_feuille-route/index.md)
- [Dictionnaire de données](02_artsn/05_dictionnaire/index.md)
- [Protocole de test interopérabilité](02_artsn/07_annexes/d-protocole-test-interopabilite.md)
- [SLA et performance](02_artsn/07_annexes/e-sla-performance.md)
