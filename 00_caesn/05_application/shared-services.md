---
title: Services numériques partagés prioritaires
id: application-shared-services
domain: 05_application
version: "1.0.0"
status: draft
last_reviewed: 2026-07-03
owner: Direction des Systèmes d'Information
tags: [applications, services-partagés]
---

# Services numériques partagés prioritaires

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
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### CMP-12 : Référentiels nationaux et données de référence

#### Services numériques

FOSA, géographie, produits de santé, indicateurs, agents, bénéficiaires, terminologies

#### Flux de valeur soutenus

- VS-01 : Accéder à des services de santé essentiels, intégrés, équitables et de qualité
- VS-02 : Prévenir, détecter et répondre aux risques sanitaires
- VS-03 : Protéger financièrement la population face aux dépenses de santé
- VS-04 : Piloter, coordonner et améliorer la performance du système de santé

*Rattachement : PRC-01, PRC-07, PRC-10, CAP-INT-02, CAP-INT-04, CAP-INT-05, ART-4, ART-4D · fiche*

### CMP-13 : Services partagés de confiance et d'interopérabilité

#### Services numériques

Identité patient/bénéficiaire, identité agent, authentification et gestion des accès, notification, consentement, catalogue des API et contrats d'interface

#### Flux de valeur soutenus

- VS-01 : Accéder à des services de santé essentiels, intégrés, équitables et de qualité
- VS-02 : Prévenir, détecter et répondre aux risques sanitaires
- VS-03 : Protéger financièrement la population face aux dépenses de santé
- VS-04 : Piloter, coordonner et améliorer la performance du système de santé

*Rattachement : PRC-01, PRC-05, PRC-09, CAP-INT-01, CAP-INT-06, CAP-INT-08, CAP-INT-09, ART-1, ART-2, ART-4A, ART-4B, ART-7 · fiche*

<!-- END:GENERATED -->
## Liens

- Paysage applicatif cible
- Domaines applicatifs
- Référentiels nationaux

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **VS-01 : Accéder à des services de santé essentiels, intégrés, équitables et de qualité** : Accéder à des services de santé essentiels, intégrés, équitables et de qualité (`referentiel/flux-valeur/vs-01.md`)
- **VS-02 : Prévenir, détecter et répondre aux risques sanitaires** : Prévenir, détecter et répondre aux risques sanitaires (`referentiel/flux-valeur/vs-02.md`)
- **VS-03 : Protéger financièrement la population face aux dépenses de santé** : Protéger financièrement la population face aux dépenses de santé (`referentiel/flux-valeur/vs-03.md`)
- **VS-04 : Piloter, coordonner et améliorer la performance du système de santé** : Piloter, coordonner et améliorer la performance du système de santé (`referentiel/flux-valeur/vs-04.md`)
- **PRC-01** : Accès, orientation et admission du patient (`referentiel/processus/prc-01.md`)
- **PRC-07** : Identification et droits des bénéficiaires (`referentiel/processus/prc-07.md`)
- **PRC-10** : Planification et allocation des ressources (`referentiel/processus/prc-10.md`)
- **CAP-INT-02** : CAP-INT-02 : Registre et résolution des professionnels de santé (`referentiel/capacites/cap-int-02.md`)
- **CAP-INT-04** : CAP-INT-04 : Référentiel des structures et services de santé (`referentiel/capacites/cap-int-04.md`)
- **CAP-INT-05** : CAP-INT-05 : Terminologie et codification communes (`referentiel/capacites/cap-int-05.md`)
- **ART-4** : Référentiels de métadonnées de gestion (`referentiel/chapitres/art-4.md`)
- **ART-4D** : Référentiel géospatial et d'exploitation partagé (`referentiel/chapitres/art-4d.md`)
- **fiche** : Registre d'éligibilité et de couverture (CSU : ART-4c) (`referentiel/composants/cmp-12.md`)
- **PRC-05** : Alerte, investigation et riposte (`referentiel/processus/prc-05.md`)
- **PRC-09** : Remboursement et régulation des mécanismes (`referentiel/processus/prc-09.md`)
- **CAP-INT-01** : CAP-INT-01 : Résolution d’identité du bénéficiaire (`referentiel/capacites/cap-int-01.md`)
- **CAP-INT-06** : CAP-INT-06 : Catalogue des services et registre des contrats (`referentiel/capacites/cap-int-06.md`)
- **CAP-INT-08** : CAP-INT-08 : Confiance, sécurité et autorisation (`referentiel/capacites/cap-int-08.md`)
- **CAP-INT-09** : CAP-INT-09 : Gestion des consentements et bases d’autorisation (`referentiel/capacites/cap-int-09.md`)
- **ART-1** : Intégration et ingestion (`referentiel/chapitres/art-1.md`)
- **ART-2** : Médiation et normalisation (`referentiel/chapitres/art-2.md`)
- **ART-4A** : Résolution d'identité (`referentiel/chapitres/art-4a.md`)
- **ART-4B** : Bases d'autorisation (`referentiel/chapitres/art-4b.md`)
- **ART-7** : Sécurité, contrôle d'accès et résidence de la donnée (`referentiel/chapitres/art-7.md`)
- **Paysage applicatif cible** : Paysage applicatif cible (`00_caesn/05_application/layers.md`)
- **Domaines applicatifs** : Domaines applicatifs cibles par flux de valeur (`00_caesn/05_application/application-domains.md`)
- **Référentiels nationaux** : Référentiels nationaux (`00_caesn/04_data/referentials.md`)
