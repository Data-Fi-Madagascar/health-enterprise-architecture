---
title: Domaines de données prioritaires
id: data-domains
domain: 04_data
version: "1.0.0"
status: draft
last_reviewed: 2026-07-03
owner: Cellule du Système d'Information Sanitaire
tags: [données, domaines, gouvernance]
---

# Domaines de données prioritaires

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

Le système d'information sanitaire national couvre plusieurs domaines de données correspondant aux différentes dimensions de la valeur produite et aux capabilités nécessaires à son exécution.

| Domaine | Description | Flux de valeur |
|---------|-------------|----------------|
| Données patient et usager | Identité, épisodes de soins, dossier médical, référence, contre-référence, suivi, résultats cliniques | VS-01, VS-03 |
| Données communautaires | Activités des agents communautaires, alertes, suivi des ménages, sensibilisation, observance | VS-01, VS-02 |
| Données des formations sanitaires | Identification des structures, services, activités, capacité, performance, qualité, équipements | Tous les VS |
| Données de surveillance sanitaire | Signaux, cas suspects, alertes, investigations, confirmations, ripostes, urgences | VS-02, VS-04 |
| Données logistiques | Stocks, commandes, approvisionnement, disponibilité médicaments/vaccins/intrants, chaîne du froid | VS-01, VS-02, VS-04 |
| Données ressources humaines | Agents, affectations, compétences, formation, supervision, disponibilité, charge de travail | Tous les VS |
| Données financières | Budgets, dépenses, remboursements, exemptions, paiements, exécution budgétaire, coûts | VS-03, VS-04 |
| Données des programmes de santé | Couverture, interventions, cibles, résultats des programmes prioritaires | VS-01, VS-02, VS-04 |
| Données qualité des soins | Incidents, audits cliniques, revues de décès, satisfaction, conformité, actions correctives | VS-01, VS-04 |
| Données géographiques | Régions, districts, communes, fokontany, zones sanitaires, localisation | Tous les VS |
| Données de gouvernance | Initiatives, financements, partenaires, alignement stratégique, bénéfices, maturité des capabilités | VS-04 |

## Exigences par domaine

Chaque domaine de données doit disposer de :

- un responsable métier ;
- des règles de qualité ;
- des règles d'accès ;
- un usage décisionnel explicite ;
- un lien avec les référentiels nationaux correspondants.

## Rôles

| Rôle | Responsabilité |
|------|----------------|
| Propriétaire métier de la donnée | Définit la signification métier, ses usages, ses règles de qualité |
| Producteur de données | Produit ou saisit la donnée à la source, selon les standards définis |
| Gestionnaire / steward | Contrôle la qualité, documente les définitions, suit les corrections, coordonne les mises à jour |
| Utilisateur autorisé | Utilise la donnée pour une finalité légitime : soins, surveillance, financement, pilotage, recherche, redevabilité |

## Liens

- Référentiels nationaux
- Flux de valeur
- Gouvernance des données

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Référentiels nationaux** : Référentiels nationaux (`00_caesn/04_data/referentials.md`)
- **Dictionnaire de données ARTSN** : Dictionnaire de données fonctionnelles (`02_artsn/05_dictionnaire/index.md`)
- **Flux de valeur** : Flux de valeur nationaux de santé (`00_caesn/01_value-streams/index.md`)
- **Gouvernance des données** : Gouvernance, qualité et protection des données (`00_caesn/04_data/governance.md`)
