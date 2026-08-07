---
title: Services numériques partagés prioritaires
id: application-shared-services
domain: 05_application
version: "0.1.0"
status: draft
last_reviewed: 2026-07-03
owner: Direction des Systèmes d'Information
tags: [applications, services-partagés]
---

# Services numériques partagés prioritaires

Certains services doivent être conçus comme des services nationaux partagés, réutilisables par plusieurs applications. Ils sont réutilisés par défaut ; la création d'un service parallèle doit être justifiée, limitée et validée par la gouvernance.

| Service partagé | Rôle | Applications consommatrices |
|-----------------|------|------------------------------|
| Service d'identité patient / bénéficiaire | Identifier fiablement les patients et bénéficiaires pour la continuité et la protection | Dossier patient, CSU, référence, surveillance, entrepôt |
| Service d'identité agent de santé | Identifier les professionnels, rôles, affectations, droits d'accès | RH santé, dossier patient, surveillance, logistique, tableaux de bord |
| Référentiel FOSA | Identifier les structures et leurs caractéristiques | Tous les systèmes métier |
| Référentiel géographique | Harmoniser les zones administratives et sanitaires | Surveillance, planification, tableaux de bord, logistique, CSU |
| Référentiel produits de santé | Harmoniser médicaments, vaccins, intrants, consommables | Logistique, vaccination, FOSA, entrepôt |
| Référentiel indicateurs | Définitions communes et stables des indicateurs | DHIS2/HMIS, tableaux de bord, entrepôt, portefeuille |
| Service d'authentification et gestion des accès | Contrôler l'accès selon les rôles | Toutes les applications nationales |
| Service de notification | Envoyer alertes, rappels, messages opérationnels | Vaccination, référence, surveillance, CSU, supervision |
| Catalogue des API et contrats d'interface | Documenter les échanges autorisés | Applications métier, couche d'échange, intégrateurs |
| Registre national des initiatives numériques | Suivre projets, financements, partenaires, bénéfices | Gouvernance, portefeuille, VRO, Comité |

## Liens

- [Paysage applicatif cible](./layers.md)
- [Domaines applicatifs](./application-domains.md)
- [Référentiels nationaux](../04_data/referentials.md)