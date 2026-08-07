---
title: Architecture applicative et systèmes numériques
id: application-architecture
domain: application
version: "0.1.0"
status: draft
last_reviewed: 2026-07-03
owner: Direction des Systèmes d'Information
tags: [applications, systèmes, numériques]
---

# Architecture applicative et systèmes numériques

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
| [Principes de l'architecture applicative](./principles.md) | Règles AA-01 à AA-09 |
| [Paysage applicatif cible](./layers.md) | Les six couches du paysage national |
| [Domaines applicatifs par flux de valeur](./application-domains.md) | Familles de systèmes et services |
| [Services numériques partagés](./shared-services.md) | Composants partagés prioritaires |
| [Urbanisation applicative](./urbanisation.md) | Règles d'organisation des systèmes |
| [Contraintes d'exploitation](./constraints.md) | Contextes connecté / intermittent / hors ligne |
| [Cycle de vie et homologation](./lifecycle.md) | De cadrage au retrait, de critères d'homologation |
| [Rationalisation du paysage](./rationalization.md) | Trajectoires : conserver, intégrer, moderniser, fusion, remplacer, retirer |

## Relation avec l'Architecture de Référence Technique

Le présent cadre définit le **pourquoi et le quoi** (organisation fonctionnelle et applicative cible). L'**Architecture de Référence Technique** définit le **comment technique** : standards d'échange, formats, API, sécurité, hébergement, journalisation, développement, tests et homologation technique.

## Liens

- [Données](../data/index.md)
- [Capabilités](../capabilities/index.md)
- [Flux de valeur](../value-streams/index.md)
- [Portefeuille](../portfolio/index.md)