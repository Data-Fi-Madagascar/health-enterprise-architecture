---

title: Architecture des données et de l'information sanitaire
id: data-architecture
domain: 04_data
version: "1.0.0"
status: draft
last_reviewed: 2026-07-03
owner: Direction des Systèmes d'Information
tags: ["données", "architecture", "sis"]
---

# Architecture des données et de l'information sanitaire

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## Rôle de l'architecture des données

Les données de santé constituent un actif stratégique national. Elles ne valent que si elles sont de qualité suffisante, disponibles au bon moment, accessibles aux acteurs autorisés, protégées contre les usages non autorisés et effectivement utilisées pour améliorer les décisions, les services et les résultats de santé.

L'architecture des données définit comment les données sont produites, collectées, validées, référencées, échangées, stockées, protégées, analysées, restituées et utilisées pour la décision. Elle ne se limite pas aux bases de données ou aux tableaux de bord : elle définit les règles qui transforment des données disparates en information sanitaire fiable, gouvernée et utile.

Aucune initiative ne doit créer de nouvelles données, formulaires ou référentiels sans démontrer leur contribution à une capabilité, un flux de valeur et un usage décisionnel identifié.

## Structure de ce domaine

| Document | Contenu |
|----------|---------|
| Principes de l'architecture des données | Règles DA-01 à DA-08 |
| Domaines de données | Domaines de données prioritaires et stewards |
| Référentiels nationaux | Socles communs aux systèmes sanitaires |
| Cycle de vie des données | De la création à l'archivage |
| Gouvernance et protection des données | Rôles, qualité, accès, protection, entrepôt national |

## Données opérationnelles et analytiques

- **Données opérationnelles** : produites et utilisées dans l'exécution quotidienne des services (dossier patient, consultation, référence, alerte, stock, droit, affectation). Disponibles au point de service, y compris à connectivité limitée.
- **Données analytiques** : utilisées pour le pilotage, la planification, l'évaluation, la recherche et la redevabilité. Consolidées depuis plusieurs sources.

Les systèmes opérationnels soutiennent l'action ; les systèmes analytiques soutiennent la décision. Les données circulent des premiers vers les seconds selon des règles gouvernées : sécurisées, interopérables. Cette séparation évite de faire des outils de soins de simples outils de reporting et d'utiliser l'entrepôt comme substitut des systèmes opérationnels.

## Liens

- Capabilités
- Architecture applicative
- Flux de valeur

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Principes de l'architecture des données** : Principes de l'architecture des données (`00_caesn/04_data/principles.md`)
- **Domaines de données** : Domaines de données prioritaires (`00_caesn/04_data/domains.md`)
- **Référentiels nationaux** : Référentiels nationaux (`00_caesn/04_data/referentials.md`)
- **Cycle de vie des données** : Cycle de vie des données (`00_caesn/04_data/lifecycle.md`)
- **Gouvernance et protection des données** : Gouvernance, qualité et protection des données (`00_caesn/04_data/governance.md`)
- **Dictionnaire de données ARTSN** : Dictionnaire de données fonctionnelles, sémantique universelle (`02_artsn/03_objets-de-donnees/index.md`)
- **Objets de données métier** : Objets de données métier du CAESN (réalisés par l'ARTSN) (`00_caesn/04_data/objets.md`)
- **Capabilités** : Capabilités du système de santé (`00_caesn/03_capabilities/index.md`)
- **Architecture applicative** : Architecture applicative et systèmes numériques (`00_caesn/05_application/index.md`)
- **Flux de valeur** : Flux de valeur nationaux de santé (`00_caesn/01_value-streams/index.md`)

## Documents de la section

- [data-referentials: Référentiels nationaux](referentials.md)
- [data-lifecycle: Cycle de vie des données](lifecycle.md)
- [data-principles: Principes de l'architecture des données](principles.md)
- [data-governance: Gouvernance, qualité et protection des données](governance.md)
- [data-domains: Domaines de données prioritaires](domains.md)
- [data-business-objects: Objets de données métier](objets.md)

<!-- liens-section-auto -->
