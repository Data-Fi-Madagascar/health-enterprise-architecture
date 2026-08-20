---
title: Architecture applicative et systèmes numériques
id: application-architecture
domain: 05_application
version: "1.0.0"
status: draft
last_reviewed: 2026-07-03
owner: Direction des Systèmes d'Information
tags: [applications, systèmes, numériques]
---

# Architecture applicative et systèmes numériques

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

## Rôle de l'architecture applicative

L'architecture applicative définit l'organisation cible des applications, plateformes, services numériques et composants partagés nécessaires pour soutenir les flux de valeur nationaux de santé. Elle n'est pas un catalogue de logiciels : elle décrit les domaines applicatifs à maîtriser, les responsabilités de chaque famille d'applications, les interactions entre systèmes et les règles pour éviter la fragmentation.

Elle répond à quatre questions :

1. Quels services numériques sont nécessaires pour exécuter les flux de valeur ?
2. Quelles familles d'applications doivent soutenir ces services ?
3. Quelles données doivent être échangées entre systèmes ?
4. Quelles règles guident le choix, l'homologation, l'intégration et l'évolution des applications ?

Une application n'est pertinente que si elle renforce une capabilité nationale et contribue à un flux de valeur mesurable.

## Distinctions clés

| Notion | Définition | Exemple |
|--------|------------|---------|
| Service numérique | Fonction numérique attendue par un utilisateur ou un processus métier | Vérifier les droits d'un bénéficiaire, notifier une alerte, consulter l'historique patient, suivre un stock |
| Application | Logiciel fournissant un ou plusieurs services à un groupe d'utilisateurs | Dossier patient électronique, système de surveillance, gestion logistique, gestion de la CSU |
| Plateforme partagée | Composant national réutilisable par plusieurs applications | Référentiel FOSA, registre des bénéficiaires, couche d'échange, service d'identité |

Cette distinction évite de confondre le besoin métier avec l'outil technique : le cadre dit « il faut tel service numérique pour renforcer telle capabilité au service de tel flux », non « il faut telle application ».

## Structure de ce domaine

| Document | Contenu |
|----------|---------|
| Principes de l'architecture applicative | Règles AA-01 à AA-09 |
| Paysage applicatif cible | Les six couches du paysage national |
| Domaines applicatifs par flux de valeur | Familles de systèmes et services |
| Services numériques partagés | Composants partagés prioritaires |
| Urbanisation applicative | Règles d'organisation des systèmes |
| Contraintes d'exploitation | Contextes connecté / intermittent / hors ligne |
| Cycle de vie et homologation | De cadrage au retrait, de critères d'homologation |
| Rationalisation du paysage | Trajectoires : conserver, intégrer, moderniser, fusion, remplacer, retirer |

## Relation avec l'Architecture de Référence Technique

Le présent cadre définit le **pourquoi et le quoi** (organisation fonctionnelle et applicative cible). L'**Architecture de Référence Technique** définit le **comment technique** : standards d'échange, formats, API, sécurité, hébergement, journalisation, développement, tests et homologation technique.

## Liens

- Données
- Capabilités
- Flux de valeur
- Portefeuille

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Principes de l'architecture applicative** : Principes de l'architecture applicative (`00_caesn/05_application/principles.md`)
- **Paysage applicatif cible** : Paysage applicatif cible (`00_caesn/05_application/layers.md`)
- **Domaines applicatifs par flux de valeur** : Domaines applicatifs cibles par flux de valeur (`00_caesn/05_application/application-domains.md`)
- **Services numériques partagés** : Services numériques partagés prioritaires (`00_caesn/05_application/shared-services.md`)
- **Urbanisation applicative** : Règles d'urbanisation applicative (`00_caesn/05_application/urbanisation.md`)
- **Contraintes d'exploitation** : Contraintes d'exploitation différenciées (`00_caesn/05_application/constraints.md`)
- **Cycle de vie et homologation** : Cycle de vie applicatif et critères d'homologation (`00_caesn/05_application/lifecycle.md`)
- **Rationalisation du paysage** : Trajectoire de rationalisation du paysage applicatif (`00_caesn/05_application/rationalization.md`)
- **Données** : Architecture des données et de l'information sanitaire (`00_caesn/04_data/index.md`)
- **Capabilités** : Capabilités du système de santé (`00_caesn/03_capabilities/index.md`)
- **Flux de valeur** : Flux de valeur nationaux de santé (`00_caesn/01_value-streams/index.md`)
- **Portefeuille** : Portefeuille d'initiatives orienté valeur (`00_caesn/06_portfolio/index.md`)
