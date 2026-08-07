---
title: Cycle de vie applicatif et critères d'homologation
id: application-lifecycle
domain: 05_application
version: "0.1.0"
status: draft
last_reviewed: 2026-07-03
owner: Direction des Systèmes d'Information
tags: [applications, cycle-de-vie, homologation]
---

# Cycle de vie applicatif et critères d'homologation

## Cycle de vie applicatif (app)

| Étape | Objectif | Décision attendue |
|-------|----------|-------------------|
| Cadrage | Vérifier le lien flux, capabilite, données, principes | Autoriser ou non la conception |
| Conception | Définir services utiles, interfaces, données, sécurité, exploitation, indicateurs | Valider l'architecture |
| Pilote | Tester usage, valeur, intégration, adoption en conditions réelles | Généraliser, corriger, intégrer ou arrêter |
| Déploiement | Étendre progressivement selon la valeur démontrée | Autoriser l'extension |
| Exploitation | Assurer support, maintenance, sécurité, supervision, amélioration continue | Maintenir, moderniser ou rationaliser |
| Retrait / remplacement | Éviter l'accumulation de systèmes obsolètes | Archiver, migrer les données, désactiver ou remplacer |

Aucune application ne devra être généralisée sans preuve minimale d'usage, de valeur, d'interopérabilité, de soutenabilité et de conformité.

## Critères de sélection et d'homologation

Le cadre ne prescrit pas de logiciel. Toute application proposée doit satisfaire des critères minimaux.

| Critère | Question d'évaluation |
|---------|------------------------|
| Alignement valeur | Quel flux de valeur et quelle capabilité l'application renforce-t-elle ? |
| Bénéfice mesurable | Quel indicateur vérifiera que l'application produit de la valeur ? |
| Interopérabilité | Peut-elle échanger des données selon les standards nationaux ? |
| Référentiels nationaux | Utilise-t-elle les référentiels applicables ? |
| Gouvernance des données | Les données sont-elles documentées et gouvernées ? |
| Protection des données | Accès, confidentialité, traçabilité, sécurité garantis ? |
| Adaptation terrain | Fonctionne-t-elle dans les conditions réelles des utilisateurs ciblés ? |
| Soutenabilité | Coût total, maintenance, support et compétences maîtrisables ? |
| Réversibilité | Les données peuvent-elles être exportées, migrées ou restituées ? |
| Non-fragmentation | Évite-t-elle les doublons avec l'existant ? |
| Adoption | Les utilisateurs finaux ont-ils été associés à la conception, tests, déploiement ? |
| Exploitation | Responsabilités de support, maintenance, supervision définies ? |

Une application qui ne satisfait pas ces critères ne doit pas être homologuée pour un déploiement national.

## Liens

- [Architecture applicative](./index.md)
- [Rationalisation](./rationalization.md)
- [Normes et homologation](../09_standards/index.md)