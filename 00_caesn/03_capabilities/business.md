---

domain: capabilites

id: CAP-05
type: capabilite
niveau: "1"
title: Surveillance épidémiologique, alerte, investigation et riposte
status: draft
owner: Responsables de capabilités métier
version: "0.1.0"
envelope: 00_caesn/03_capabilities/business.md
maps_to: []
implements: []
applies_to: ["VS-02"]
related: ["CAP-18"]
tags: ["caesn", "niveau-1", "capabilite", "CAP-05", "surveillance", "geospatial"]
---


# Capabilités métier de santé

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ◐ |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.


Chaque capabilité vit dans le référentiel : `referentiel/capabilites/cap-XX.md` (rôle, flux de valeur associés).

## Catalogue des capabilités

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

realized_by: ["SRV-02"]
### Offre de soins et continuité des services

#### Rôle dans le système

La capabilité garantit que chaque citoyen accède à des services de santé essentiels, sûrs et de qualité, quel que soit son lieu de résidence ou sa situation. Elle conditionne le bon déroulement du parcours de soins décrit par le flux de valeur associé. Elle couvre :

- **Disponibilité des services** : présence et fonctionnement des formations sanitaires à tous les niveaux de la pyramide
- **Accessibilité géographique et financière** : réduction des barrières liées à la distance et au coût
- **Continuité de la prise en charge** : maintien du suivi du patient d'un niveau à l'autre
- **Qualité minimale garantie** : respect des normes de soins et de sécurité

Elle est **pivot** pour le parcours de soins et conditionne le bon déroulement du flux de valeur [VS-01: Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../referentiel/flux-valeur/vs-01.md).

#### Flux de valeur

- [VS-01: Soins essentiels](../../referentiel/flux-valeur/vs-01.md)

#### Rattachement ARTSN

- [F-1: Résilience face à la réalité géographique du pays](../../referentiel/fondations/f-1.md)
- [ART-4: Référentiels de métadonnées de gestion](../../referentiel/chapitres/art-4.md)
- [ART-1: Intégration et ingestion](../../referentiel/chapitres/art-1.md)
- [PT-06: Profil technique national](../../referentiel/profils/pt-06.md)

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 3/5 |

#### Propriétaire

Responsables de capabilités métier

### Gestion du parcours patient, référence et contre-référence

#### Rôle dans le système

La capabilité organise le parcours du patient entre les points de service : orientation vers le niveau adapté, référence vers une structure plus spécialisée et contre-référence vers la formation d'origine. Elle assure que l'information clinique suit le patient d'un niveau à l'autre, afin que la continuité des soins ne dépende pas d'un seul établissement. Sans elle, les ruptures de parcours (référence sans dossier, absence de retour d'information) fragmentent la prise en charge. Elle couvre :

- **Orientation et tri** : acheminement du patient vers le niveau de soins le plus adapté
- **Référence** : transfert vers une structure plus spécialisée avec transmission du dossier clinique
- **Contre-référence** : retour vers l'établissement d'origine avec compte-rendu et recommandations
- **Évacuation sanitaire** : transferts urgents nationaux et internationaux

Son absence fragilise la continuité des soins ([VS-01: Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../referentiel/flux-valeur/vs-01.md)) et provoque des ruptures de parcours.

#### Scénarios couverts

| Scénario | Description | Profils consommés |
|----------|-------------|-------------------|
| **Référence (DO-07)** | Orientation d'un patient d'un niveau de soins vers un autre (CSB → hôpital régional) | [PT-01: Profil technique national](../../referentiel/profils/pt-01.md), [PT-02: Profil technique national](../../referentiel/profils/pt-02.md) |
| **Contre-référence (DO-08)** | Retour du patient vers l'établissement d'origine avec compte-rendu et recommandations | [PT-01: Profil technique national](../../referentiel/profils/pt-01.md), [PT-02: Profil technique national](../../referentiel/profils/pt-02.md) |
| **Évacuation sanitaire nationale (DO-09)** | Transfert urgent entre établissements nationaux | [PT-01: Profil technique national](../../referentiel/profils/pt-01.md), [PT-02: Profil technique national](../../referentiel/profils/pt-02.md), [PT-11: Profil technique national](../../referentiel/profils/pt-11.md) |
| **Évacuation sanitaire internationale (DO-09)** | Transfert vers un centre spécialisé à l'étranger | [PT-01: Profil technique national](../../referentiel/profils/pt-01.md), [PT-02: Profil technique national](../../referentiel/profils/pt-02.md), [PT-11: Profil technique national](../../referentiel/profils/pt-11.md), [PT-14: Interopérabilité transfrontalière](../../referentiel/profils/pt-14.md) |

#### Flux de valeur

- [VS-01: Soins essentiels](../../referentiel/flux-valeur/vs-01.md)

#### Rattachement ARTSN

- [ART-8: Orchestration de processus](../../referentiel/chapitres/art-8.md)
- [ART-3: Historisation événementielle et profils de déploiement](../../referentiel/chapitres/art-3.md)
- [PT-01: Profil technique national](../../referentiel/profils/pt-01.md)
- [PT-02: Profil technique national](../../referentiel/profils/pt-02.md)

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 3/5 |

#### Propriétaire

Responsables de capabilités métier

realized_by: ["SRV-06"]
### Qualité, sécurité des soins et amélioration continue

#### Rôle dans le système

La capabilité mesure, améliore et sécurise la qualité des services de santé. Elle relie les données de qualité (résultats, incidents, retours patients) aux mécanismes d'amélioration continue, pour que la performance se traduise en actions correctives et pas seulement en rapports. Elle couvre :

- **Mesure de la qualité** : indicateurs de résultats, de sécurité et d'expérience patient
- **Sécurité des soins** : prévention des risques et des événements indésirables
- **Amélioration continue** : boucle de retour des données vers des actions correctives
- **Pilotage de la performance** : tableaux de bord et restitution aux décideurs

Elle alimente à la fois la qualité des soins ([VS-01: Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../referentiel/flux-valeur/vs-01.md)) et le pilotage du système ([VS-04: Piloter, coordonner et améliorer la performance du système de santé](../../referentiel/flux-valeur/vs-04.md)).

#### Flux de valeur

- [VS-01: Soins essentiels](../../referentiel/flux-valeur/vs-01.md)
- [VS-04: Pilotage du système](../../referentiel/flux-valeur/vs-04.md)

#### Rattachement ARTSN

- [ART-5: Cohérence et qualité des données](../../referentiel/chapitres/art-5.md)
- [ART-6: Analytique et restitution](../../referentiel/chapitres/art-6.md)
- [PT-13: Profil technique national](../../referentiel/profils/pt-13.md)
- [PT-09: Profil technique national](../../referentiel/profils/pt-09.md)

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 1/5 | 3/5 |

#### Propriétaire

Responsables de capabilités métier

### Santé communautaire et engagement des communautés

#### Rôle dans le système

La capabilité intègre les agents communautaires, les communautés et les patients comme acteurs du système de santé : prévention, alerte précoce, suivi des cas, observance des traitements et amélioration des services. Elle étend la couverture sanitaire au-delà des formations sanitaires, en particulier dans les zones où la distance et le coût limitent le recours aux soins. Elle couvre :

- **Prévention communautaire** : éducation, dépistage et promotion de la santé
- **Alerte précoce** : remontée des signaux depuis la communauté vers le système
- **Suivi des cas** : accompagnement, observance et lien avec la formation sanitaire
- **Renforcement de l'offre** : extension de la couverture sanitaire en zone éloignée

Elle renforce la couverture sanitaire sur les flux [VS-01: soins](../../referentiel/flux-valeur/vs-01.md) et [VS-02: surveillance](../../referentiel/flux-valeur/vs-02.md).

#### Flux de valeur

- [VS-01: Soins essentiels](../../referentiel/flux-valeur/vs-01.md)
- [VS-02: Prévention et surveillance](../../referentiel/flux-valeur/vs-02.md)

#### Rattachement ARTSN

- [F-1: Résilience face à la réalité géographique du pays](../../referentiel/fondations/f-1.md)
- [ART-2: Médiation et normalisation](../../referentiel/chapitres/art-2.md)
- [PT-02: Profil technique national](../../referentiel/profils/pt-02.md)
- [F-6: Observabilité](../../referentiel/fondations/f-6.md)

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 3/5 |

#### Propriétaire

Responsables de capabilités métier

### Surveillance épidémiologique, alerte, investigation et riposte

#### Rôle dans le système

La capabilité couvre l'ensemble du cycle de gestion des risques sanitaires : détection des signaux, notification des cas, vérification, investigation, déclenchement de la riposte et retour d'expérience. Elle relie les formations sanitaires, les districts et le niveau central pour qu'une épidémie ou une urgence soit identifiée et traitée sans délai.

Elle couvre :
- **Détection et alerte** : surveillance sentinelle, notification des cas et signalement précoce des événements
- **Investigation** : vérification terrain, recherche des contacts et confirmation étiologique
- **Riposte** : coordination de la réponse, mesures de contrôle et retour d'expérience
- **Surveillance multisource** : agrégation des données laboratoires, cliniques et communautaires

La capabilité inclut désormais la **dimension géospatiale** :
- **Géolocalisation des formations sanitaires** : positionnement GPS de toutes les structures de soins
- **Cartographie des risques** : visualisation spatiale des foyers épidémiques et des zones à risque
- **Suivi temporel** : analyse des tendances épidémiques par zone géographique
- **Cloisonnement One Health** : surveillance conjointe santé humaine/animale/environnement par zone

Son absence fragilise la surveillance sanitaire ([VS-02: Prévenir, détecter et répondre aux risques sanitaires](../../referentiel/flux-valeur/vs-02.md)).

#### Flux de valeur

- [VS-02: Prévention et surveillance](../../referentiel/flux-valeur/vs-02.md)

#### Rattachement ARTSN

- [F-1: Résilience face à la réalité géographique du pays](../../referentiel/fondations/f-1.md)
- [ART-4D: Référentiel géospatial et d'exploitation partagé](../../referentiel/chapitres/art-4d.md)
- [PT-05: Profil technique national](../../referentiel/profils/pt-05.md)
- [PT-15: Surveillance One Health](../../referentiel/profils/pt-15.md)

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 3/5 |

#### Propriétaire

Responsables de capabilités métier

### Vaccination, prévention et promotion de la santé

#### Rôle dans le système

La capabilité prévient les maladies et promeut les comportements favorables à la santé : prévention, promotion, campagnes et suivi des interventions préventives, dont la vaccination. Elle agit en amont du soin curatif pour réduire la morbidité et éviter les dépenses évitables, et sa planification est un des leviers de l’amélioration de la santé de la population.

Elle couvre :
- **Prévention et promotion** : éducation pour la santé, communication et comportements favorables
- **Vaccination** : planification, logistique et suivi de la couverture vaccinale
- **Campagnes sanitaires** : organisation et monitoring des campagnes de prévention
- **Surveillance des risques** : identification des facteurs de risque et des populations cibles

Son absence fragilise la prévention et la surveillance sanitaire ([VS-02: Prévenir, détecter et répondre aux risques sanitaires](../../referentiel/flux-valeur/vs-02.md)).

#### Flux de valeur

- [VS-02: Prévention et surveillance](../../referentiel/flux-valeur/vs-02.md)

#### Rattachement ARTSN

- [ART-4: Référentiels de métadonnées de gestion](../../referentiel/chapitres/art-4.md)
- [ART-6: Analytique et restitution](../../referentiel/chapitres/art-6.md)
- [PT-06: Profil technique national](../../referentiel/profils/pt-06.md)
- [PT-07: Profil technique national](../../referentiel/profils/pt-07.md)

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 3/5 |

#### Propriétaire

Responsables de capabilités métier

### Protection financière, couverture santé universelle

#### Rôle dans le système

La capabilité protège les ménages contre le risque financier lié aux soins : identification des bénéficiaires, vérification de leurs droits, application des mécanismes de protection financière et soutien à l’achat stratégique des services. Elle garantit que la couverture et la protection annoncées se traduisent effectivement au point de service, y compris en zone à connectivité limitée.

Elle couvre :
- **Identification des bénéficiaires** : enregistrement et résolution d'identité des ayants droit
- **Vérification des droits** : éligibilité et couverture selon les mécanismes de protection
- **Application de la protection** : prise en charge et dispense de paiement au point de service
- **Achat stratégique** : soutien à la contractualisation et au paiement des prestataires

Son absence fragilise la protection financière des ménages ([VS-03: Protéger financièrement la population face aux dépenses de santé](../../referentiel/flux-valeur/vs-03.md)).

#### Flux de valeur

- [VS-03: Protection financière](../../referentiel/flux-valeur/vs-03.md)

#### Rattachement ARTSN

- [ART-4: Référentiels de métadonnées de gestion](../../referentiel/chapitres/art-4.md)
- [ART-4C: Éligibilité et couverture](../../referentiel/chapitres/art-4c.md)
- [PT-04: Profil technique national](../../referentiel/profils/pt-04.md)
- [PT-12: Profil technique national](../../referentiel/profils/pt-12.md)

#### Maturité

| Niveau actuel | Niveau cible (3 ans) |
|---------------|----------------------|
| 1/5 | 3/5 |

#### Propriétaire

Responsables de capabilités métier

### Gouvernance institutionnelle, planification, coordination et redevabilité

#### Rôle dans le système

La capabilité assure la gouvernance du système de santé : planification, coordination, régulation, suivi et redevabilité à tous les niveaux (national, régional, district, formation). Elle transforme les données et les plans en décisions de gestion, et garantit que chaque niveau rend compte de sa performance aux instances qui l’encadrent.

Elle couvre :
- **Planification** : élaboration et suivi des plans sanitaires nationaux et sectoriels
- **Coordination et régulation** : articulation des acteurs et régulation de l'offre de services
- **Pilotage et analytique** : tableaux de bord et restitution de la performance
- **Redevabilité** : reporting, contrôle et rendu de comptes aux instances de gouvernance

Son absence fragilise le pilotage du système ([VS-04: Piloter, coordonner et améliorer la performance du système de santé](../../referentiel/flux-valeur/vs-04.md)) et la protection financière ([VS-03: Protéger financièrement la population face aux dépenses de santé](../../referentiel/flux-valeur/vs-03.md)).

#### Flux de valeur

- [VS-03: Protection financière](../../referentiel/flux-valeur/vs-03.md)
- [VS-04: Pilotage du système](../../referentiel/flux-valeur/vs-04.md)

#### Rattachement ARTSN

- [ART-6: Analytique et restitution](../../referentiel/chapitres/art-6.md)
- [F-6: Observabilité](../../referentiel/fondations/f-6.md)
- [PT-09: Profil technique national](../../referentiel/profils/pt-09.md)
- [PT-13: Profil technique national](../../referentiel/profils/pt-13.md)

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 3/5 |

#### Propriétaire

Responsables de capabilités métier

<!-- END:GENERATED -->
## Liens

- [Capabilités](./index.md)

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
