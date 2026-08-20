---

title: "Capabilités métier de santé"
id: capabilities-business
domain: 03_capabilities
version: "1.0.0""
status: draft
last_reviewed: 2026-07-03
owner: Responsables de capabilités métier
tags: ["capabilités", "métier", "catalogue"]
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

### Offre de soins et continuité des services

#### Rôle dans le système

La capabilité garantit que chaque citoyen accède à des services de santé essentiels, sûrs et de qualité, quel que soit son lieu de résidence ou sa situation. Elle conditionne le bon déroulement du parcours de soins décrit par le flux de valeur associé. Elle couvre :

- **Disponibilité des services** : présence et fonctionnement des formations sanitaires à tous les niveaux de la pyramide
- **Accessibilité géographique et financière** : réduction des barrières liées à la distance et au coût
- **Continuité de la prise en charge** : maintien du suivi du patient d'un niveau à l'autre
- **Qualité minimale garantie** : respect des normes de soins et de sécurité

Elle est **pivot** pour le parcours de soins et conditionne le bon déroulement du flux de valeur VS-01.

#### Flux de valeur

- [VS-01: Soins essentiels](../../referentiel/flux-valeur/vs-01.md)

#### Rattachement ARTSN

- **F.1** — Résilience face à la réalité géographique du pays
- **ART-4** — Référentiels de métadonnées de gestion
- **ART-1** — Intégration et ingestion
- **PT-06** — Référentiel des structures et services

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 3/5 |

#### Propriétaire

Responsables de capabilités métier

*Rattachement : VS-01 · fiche CAP-01*

### Gestion du parcours patient, référence et contre-référence

#### Rôle dans le système

La capabilité organise le parcours du patient entre les points de service : orientation vers le niveau adapté, référence vers une structure plus spécialisée et contre-référence vers la formation d'origine. Elle assure que l'information clinique suit le patient d'un niveau à l'autre, afin que la continuité des soins ne dépende pas d'un seul établissement. Sans elle, les ruptures de parcours (référence sans dossier, absence de retour d'information) fragmentent la prise en charge. Elle couvre :

- **Orientation et tri** : acheminement du patient vers le niveau de soins le plus adapté
- **Référence** : transfert vers une structure plus spécialisée avec transmission du dossier clinique
- **Contre-référence** : retour vers l'établissement d'origine avec compte-rendu et recommandations
- **Évacuation sanitaire** : transferts urgents nationaux et internationaux

Son absence fragilise la continuité des soins (VS-01) et provoque des ruptures de parcours.

#### Scénarios couverts

| Scénario | Description | Profils consommés |
|----------|-------------|-------------------|
| **Référence (S-03)** | Orientation d'un patient d'un niveau de soins vers un autre (CSB → hôpital régional) | PT-01, PT-02 |
| **Contre-référence (S-04)** | Retour du patient vers l'établissement d'origine avec compte-rendu et recommandations | PT-01, PT-02 |
| **Évacuation sanitaire nationale (S-05)** | Transfert urgent entre établissements nationaux | PT-01, PT-02, PT-11 |
| **Évacuation sanitaire internationale (S-05)** | Transfert vers un centre spécialisé à l'étranger | PT-01, PT-02, PT-11, PT-14 |

#### Flux de valeur

- [VS-01: Soins essentiels](../../referentiel/flux-valeur/vs-01.md)

#### Rattachement ARTSN

- **ART-8** — Orchestration de processus
- **ART-3** — Historisation événementielle et profils de déploiement
- **PT-01** — Échange interinstitutionnel (X-Road)
- **PT-02** — Médiation intra-secteur

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 3/5 |

#### Propriétaire

Responsables de capabilités métier

*Rattachement : VS-01, CAP-INT-03, CAP-INT-01, CAP-INT-13 · fiche CAP-02*

### Qualité, sécurité des soins et amélioration continue

#### Rôle dans le système

La capabilité mesure, améliore et sécurise la qualité des services de santé. Elle relie les données de qualité (résultats, incidents, retours patients) aux mécanismes d'amélioration continue, pour que la performance se traduise en actions correctives et pas seulement en rapports. Elle couvre :

- **Mesure de la qualité** : indicateurs de résultats, de sécurité et d'expérience patient
- **Sécurité des soins** : prévention des risques et des événements indésirables
- **Amélioration continue** : boucle de retour des données vers des actions correctives
- **Pilotage de la performance** : tableaux de bord et restitution aux décideurs

Elle alimente à la fois la qualité des soins (VS-01) et le pilotage du système (VS-04).

#### Flux de valeur

- [VS-01: Soins essentiels](../../referentiel/flux-valeur/vs-01.md)
- [VS-04: Pilotage du système](../../referentiel/flux-valeur/vs-04.md)

#### Rattachement ARTSN

- **ART-5** — Cohérence et qualité des données
- **ART-6** — Analytique et restitution
- **PT-13** — Qualité et réconciliation
- **PT-09** — Analytique et exposition de données

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 1/5 | 3/5 |

#### Propriétaire

Responsables de capabilités métier

*Rattachement : VS-01, VS-04 · fiche CAP-03*

### Santé communautaire et engagement des communautés

#### Rôle dans le système

La capabilité intègre les agents communautaires, les communautés et les patients comme acteurs du système de santé : prévention, alerte précoce, suivi des cas, observance des traitements et amélioration des services. Elle étend la couverture sanitaire au-delà des formations sanitaires, en particulier dans les zones où la distance et le coût limitent le recours aux soins. Elle couvre :

- **Prévention communautaire** : éducation, dépistage et promotion de la santé
- **Alerte précoce** : remontée des signaux depuis la communauté vers le système
- **Suivi des cas** : accompagnement, observance et lien avec la formation sanitaire
- **Renforcement de l'offre** : extension de la couverture sanitaire en zone éloignée

Elle renforce la couverture sanitaire sur les flux VS-01 (soins) et VS-02 (surveillance).

#### Flux de valeur

- [VS-01: Soins essentiels](../../referentiel/flux-valeur/vs-01.md)
- [VS-02: Prévention et surveillance](../../referentiel/flux-valeur/vs-02.md)

#### Rattachement ARTSN

- **F.1** — Résilience face à la réalité géographique du pays
- **ART-2** — Médiation et normalisation
- **PT-02** — Médiation intra-secteur
- **F.6** — Observabilité

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 3/5 |

#### Propriétaire

Responsables de capabilités métier

*Rattachement : VS-01, VS-02 · fiche CAP-04*

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

Son absence fragilise la surveillance sanitaire (VS-02).

#### Flux de valeur

- [VS-02: Prévention et surveillance](../../referentiel/flux-valeur/vs-02.md)

#### Rattachement ARTSN

- **F.1** — Résilience face à la réalité géographique du pays
- **ART-4d** — Référentiel géospatial et d'exploitation partagé
- **PT-05** — Profil technique géolocalisation
- **PT-15** — Surveillance One Health

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 3/5 |

#### Propriétaire

Responsables de capabilités métier

*Rattachement : VS-02 · fiche CAP-05*

### Vaccination, prévention et promotion de la santé

#### Rôle dans le système

La capabilité prévient les maladies et promeut les comportements favorables à la santé : prévention, promotion, campagnes et suivi des interventions préventives, dont la vaccination. Elle agit en amont du soin curatif pour réduire la morbidité et éviter les dépenses évitables, et sa planification est un des leviers de l’amélioration de la santé de la population.

Elle couvre :
- **Prévention et promotion** : éducation pour la santé, communication et comportements favorables
- **Vaccination** : planification, logistique et suivi de la couverture vaccinale
- **Campagnes sanitaires** : organisation et monitoring des campagnes de prévention
- **Surveillance des risques** : identification des facteurs de risque et des populations cibles

Son absence fragilise la prévention et la surveillance sanitaire (VS-02).

#### Flux de valeur

- [VS-02: Prévention et surveillance](../../referentiel/flux-valeur/vs-02.md)

#### Rattachement ARTSN

- **ART-4** — Référentiels de métadonnées de gestion
- **ART-6** — Analytique et restitution
- **PT-06** — Profil technique référentiel des structures et services de santé
- **PT-07** — Profil technique terminologie et codification communes

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 3/5 |

#### Propriétaire

Responsables de capabilités métier

*Rattachement : VS-02 · fiche CAP-06*

### Protection financière, couverture santé universelle

#### Rôle dans le système

La capabilité protège les ménages contre le risque financier lié aux soins : identification des bénéficiaires, vérification de leurs droits, application des mécanismes de protection financière et soutien à l’achat stratégique des services. Elle garantit que la couverture et la protection annoncées se traduisent effectivement au point de service, y compris en zone à connectivité limitée.

Elle couvre :
- **Identification des bénéficiaires** : enregistrement et résolution d'identité des ayants droit
- **Vérification des droits** : éligibilité et couverture selon les mécanismes de protection
- **Application de la protection** : prise en charge et dispense de paiement au point de service
- **Achat stratégique** : soutien à la contractualisation et au paiement des prestataires

Son absence fragilise la protection financière des ménages (VS-03).

#### Flux de valeur

- [VS-03: Protection financière](../../referentiel/flux-valeur/vs-03.md)

#### Rattachement ARTSN

- **ART-4** — Référentiels de métadonnées de gestion
- **ART-4c** — Éligibilité et couverture
- **PT-04** — Profil technique résolution d'identité du bénéficiaire
- **PT-12** — Profil technique provenance, audit et traçabilité

#### Maturité

| Niveau actuel | Niveau cible (3 ans) |
|---------------|----------------------|
| 1/5 | 3/5 |

#### Propriétaire

Responsables de capabilités métier

*Rattachement : VS-03 · fiche CAP-07*

### Gouvernance institutionnelle, planification, coordination et redevabilité

#### Rôle dans le système

La capabilité assure la gouvernance du système de santé : planification, coordination, régulation, suivi et redevabilité à tous les niveaux (national, régional, district, formation). Elle transforme les données et les plans en décisions de gestion, et garantit que chaque niveau rend compte de sa performance aux instances qui l’encadrent.

Elle couvre :
- **Planification** : élaboration et suivi des plans sanitaires nationaux et sectoriels
- **Coordination et régulation** : articulation des acteurs et régulation de l'offre de services
- **Pilotage et analytique** : tableaux de bord et restitution de la performance
- **Redevabilité** : reporting, contrôle et rendu de comptes aux instances de gouvernance

Son absence fragilise le pilotage du système (VS-04) et la protection financière (VS-03).

#### Flux de valeur

- [VS-03: Protection financière](../../referentiel/flux-valeur/vs-03.md)
- [VS-04: Pilotage du système](../../referentiel/flux-valeur/vs-04.md)

#### Rattachement ARTSN

- **ART-6** — Analytique et restitution
- **F.6** — Observabilité
- **PT-09** — Profil technique accès et exposition des données analytiques
- **PT-13** — Profil technique qualité et réconciliation

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 3/5 |

#### Propriétaire

Responsables de capabilités métier

*Rattachement : VS-03, VS-04 · fiche CAP-08*

<!-- END:GENERATED -->
## Liens

- [Capabilités](./index.md)

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
