---
title: Services numériques partagés prioritaires
id: application-shared-services
domain: 05_application
version: "0.0.1"
status: draft
last_reviewed: 2026-07-03
owner: Direction des Systèmes d'Information
tags: [applications, services-partagés]
---

# Services numériques partagés prioritaires

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

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

## Composants des services partagés

<!-- BEGIN:GENERATED source=referentiel/composants/cmp-12.md,referentiel/composants/cmp-13.md -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

### CMP-12 — Référentiels nationaux et données de référence

#### Services numériques

FOSA, géographie, produits de santé, indicateurs, agents, bénéficiaires, terminologies

#### Flux de valeur soutenus

- [VS-01 — Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../referentiel/flux-valeur/vs-01.md)
- [VS-02 — Prévenir, détecter et répondre aux risques sanitaires](../../referentiel/flux-valeur/vs-02.md)
- [VS-03 — Protéger financièrement la population face aux dépenses de santé](../../referentiel/flux-valeur/vs-03.md)
- [VS-04 — Piloter, coordonner et améliorer la performance du système de santé](../../referentiel/flux-valeur/vs-04.md)

*Rattachement : [PRC-01](../../referentiel/processus/prc-01.md), [PRC-07](../../referentiel/processus/prc-07.md), [PRC-10](../../referentiel/processus/prc-10.md), [CAP-INT-02](../../referentiel/capacites/cap-int-02.md), [CAP-INT-04](../../referentiel/capacites/cap-int-04.md), [CAP-INT-05](../../referentiel/capacites/cap-int-05.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-4D](../../referentiel/chapitres/art-4d.md) · [fiche](../../referentiel/composants/cmp-12.md)*

### CMP-13 — Services partagés de confiance et d'interopérabilité

#### Services numériques

Identité patient/bénéficiaire, identité agent, authentification et gestion des accès, notification, consentement, catalogue des API et contrats d'interface

#### Flux de valeur soutenus

- [VS-01 — Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../referentiel/flux-valeur/vs-01.md)
- [VS-02 — Prévenir, détecter et répondre aux risques sanitaires](../../referentiel/flux-valeur/vs-02.md)
- [VS-03 — Protéger financièrement la population face aux dépenses de santé](../../referentiel/flux-valeur/vs-03.md)
- [VS-04 — Piloter, coordonner et améliorer la performance du système de santé](../../referentiel/flux-valeur/vs-04.md)

*Rattachement : [PRC-01](../../referentiel/processus/prc-01.md), [PRC-05](../../referentiel/processus/prc-05.md), [PRC-09](../../referentiel/processus/prc-09.md), [CAP-INT-01](../../referentiel/capacites/cap-int-01.md), [CAP-INT-06](../../referentiel/capacites/cap-int-06.md), [CAP-INT-08](../../referentiel/capacites/cap-int-08.md), [CAP-INT-09](../../referentiel/capacites/cap-int-09.md), [ART-1](../../referentiel/chapitres/art-1.md), [ART-2](../../referentiel/chapitres/art-2.md), [ART-4A](../../referentiel/chapitres/art-4a.md), [ART-4B](../../referentiel/chapitres/art-4b.md), [ART-7](../../referentiel/chapitres/art-7.md) · [fiche](../../referentiel/composants/cmp-13.md)*

<!-- END:GENERATED -->
## Liens

- [Paysage applicatif cible](./layers.md)
- [Domaines applicatifs](./application-domains.md)
- [Référentiels nationaux](../04_data/referentials.md)