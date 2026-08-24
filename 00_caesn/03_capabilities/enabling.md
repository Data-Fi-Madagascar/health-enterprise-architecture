---

title: "Capabilités habilitantes du système"
id: capabilities-enabling
domain: 03_capabilities
version: "1.0.0""
status: draft
last_reviewed: 2026-07-03
owner: Responsables de capabilités habilitantes
tags: ["capabilités", "habilitantes", "catalogue"]
---

# Capabilités habilitantes du système

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

### Gestion des ressources humaines en santé

#### Rôle dans le système

La capabilité garantit la disponibilité et la compétence des ressources humaines en santé : recrutement, formation, affectation, supervision et motivation des agents. Elle est un facteur déterminant de la performance de toutes les autres capabilités, car un service de santé ne peut pas fonctionner sans personnel présent, compétent et soutenu.

Elle couvre :

- **Planification des effectifs** : anticipation des besoins en personnel par établissement, programme et niveau de soins
- **Recrutement et affectation** : mobilisation, orientation et suivi des agents sur l'ensemble du territoire
- **Formation et développement des compétences** : qualification continue, encadrement et certification des personnels
- **Suivi de carrière et motivation** : gestion des données de carrière, rémunération et conditions de travail
- **Données de référence du personnel** : registres et référentiels des agents sanitaires interopérables

Son absence fragilise la gestion des ressources humaines et compromet la continuité des soins ([VS-01: Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../referentiel/flux-valeur/vs-01.md), [VS-02: Prévenir, détecter et répondre aux risques sanitaires](../../referentiel/flux-valeur/vs-02.md)) comme le pilotage du système ([VS-04: Piloter, coordonner et améliorer la performance du système de santé](../../referentiel/flux-valeur/vs-04.md)).

#### Flux de valeur

- [VS-01: Soins essentiels](../../referentiel/flux-valeur/vs-01.md)
- [VS-02: Prévention et surveillance](../../referentiel/flux-valeur/vs-02.md)
- [VS-04: Pilotage du système](../../referentiel/flux-valeur/vs-04.md)

#### Rattachement ARTSN

- [ART-4: Référentiels de métadonnées de gestion](../../referentiel/chapitres/art-4.md)
- [F-2: Préservation de la souveraineté intersectorielle](../../referentiel/fondations/f-2.md)
- [F-1: Résilience face à la réalité géographique du pays](../../referentiel/fondations/f-1.md)

#### Maturité

| Niveau actuel | Niveau cible (3 ans) |
|---------------|----------------------|
| 1/5 | 3/5 |

#### Propriétaire

Responsables de capabilités habilitantes

### Gestion des médicaments, vaccins, intrants et chaîne d’approvisionnement

#### Rôle dans le système

La capabilité assure la disponibilité des produits de santé au point de service : médicaments, vaccins, intrants et consommables. Elle couvre la chaîne d’approvisionnement, du stock central jusqu’au comptoir, et conditionne directement la qualité des soins : une rupture de stock peut empêcher un traitement ou une vaccination programmée.

Elle couvre :

- **Prévision et planification des besoins** : estimation des besoins en médicaments, vaccins et intrants par niveau de soins
- **Approvisionnement et achats** : centralisation, contrats et réception des produits de santé
- **Gestion des stocks et entrepôts** : suivi des niveaux, péremption et entreposage
- **Distribution et logistique** : acheminement du stock central jusqu’au point de service
- **Traçabilité et qualité** : lots, chaîne du froid et sécurité des produits

Son absence expose le système à des ruptures de stock qui compromettent les soins ([VS-01: Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../referentiel/flux-valeur/vs-01.md)) et la prévention ([VS-02: Prévenir, détecter et répondre aux risques sanitaires](../../referentiel/flux-valeur/vs-02.md)).

#### Flux de valeur

- [VS-01: Soins essentiels](../../referentiel/flux-valeur/vs-01.md)
- [VS-02: Prévention et surveillance](../../referentiel/flux-valeur/vs-02.md)

#### Rattachement ARTSN

- [ART-4: Référentiels de métadonnées de gestion](../../referentiel/chapitres/art-4.md)
- [PT-14: Interopérabilité transfrontalière](../../referentiel/profils/pt-14.md)
- [F-2: Préservation de la souveraineté intersectorielle](../../referentiel/fondations/f-2.md)

#### Maturité

| Niveau actuel | Niveau cible (3 ans) |
|---------------|----------------------|
| 1/5 | 3/5 |

#### Propriétaire

Responsables de capabilités habilitantes

### Gestion des infrastructures, équipements et maintenance

#### Rôle dans le système

La capabilité garantit un environnement physique fonctionnel pour la prestation de soins : bâtiments, équipements, énergie et maintenance. Sans elle, les autres capabilités s’effondrent : un équipement en panne ou un site sans énergie rend impossible l’acte clinique, même lorsque le personnel et les produits sont disponibles.

Elle couvre :

- **Patrimoine bâti et sites** : bâtiments, structures et aménagements des établissements de santé
- **Équipements biomédicaux** : acquisition, installation et maintien en état du parc matériel
- **Énergie et utilities** : électricité, eau, climatisation et continuité énergétique
- **Maintenance et réparations** : maintenance préventive et interventions curatives
- **Cartographie et localisation** : référencement géospatial des sites et équipements

Son absence rend impossible l’acte clinique, même lorsque le personnel et les produits sont disponibles ([VS-01: Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../referentiel/flux-valeur/vs-01.md), [VS-02: Prévenir, détecter et répondre aux risques sanitaires](../../referentiel/flux-valeur/vs-02.md)).

#### Flux de valeur

- [VS-01: Soins essentiels](../../referentiel/flux-valeur/vs-01.md)
- [VS-02: Prévention et surveillance](../../referentiel/flux-valeur/vs-02.md)

#### Rattachement ARTSN

- [ART-4: Référentiels de métadonnées de gestion](../../referentiel/chapitres/art-4.md)
- [ART-4D: Référentiel géospatial et d'exploitation partagé](../../referentiel/chapitres/art-4d.md)
- [F-1: Résilience face à la réalité géographique du pays](../../referentiel/fondations/f-1.md)

#### Maturité

| Niveau actuel | Niveau cible (3 ans) |
|---------------|----------------------|
| 1/5 | 3/5 |

#### Propriétaire

Responsables de capabilités habilitantes

### Finances publiques, budget et allocation des ressources

#### Rôle dans le système

La capabilité soutient le financement du système de santé : exécution budgétaire, planification financière, allocation équitable des ressources et soutenabilité des financements. Elle garantit que les moyens financiers suivent les priorités de santé publique et que chaque niveau dispose des ressources nécessaires pour assurer ses fonctions.

Elle couvre :

- **Exécution budgétaire** : engagement, liquidation et suivi des dépenses de santé
- **Planification financière** : programmation pluriannuelle et allocations par établissement et programme
- **Allocation équitable des ressources** : répartition selon les priorités de santé publique
- **Soutenabilité des financements** : mobilisation et protection des ressources à long terme
- **Couverture et protection financière** : appui à l’éligibilité et au tiers-payant (CSU)

Son absence compromet la protection financière des ménages ([VS-03: Protéger financièrement la population face aux dépenses de santé](../../referentiel/flux-valeur/vs-03.md)) et le pilotage du système ([VS-04: Piloter, coordonner et améliorer la performance du système de santé](../../referentiel/flux-valeur/vs-04.md)).

#### Flux de valeur

- [VS-03: Protection financière](../../referentiel/flux-valeur/vs-03.md)
- [VS-04: Pilotage du système](../../referentiel/flux-valeur/vs-04.md)

#### Rattachement ARTSN

- [ART-4C: Éligibilité et couverture](../../referentiel/chapitres/art-4c.md)
- [F-2: Préservation de la souveraineté intersectorielle](../../referentiel/fondations/f-2.md)
- [ART-4: Référentiels de métadonnées de gestion](../../referentiel/chapitres/art-4.md)

#### Maturité

| Niveau actuel | Niveau cible (3 ans) |
|---------------|----------------------|
| 1/5 | 3/5 |

#### Propriétaire

Responsables de capabilités habilitantes

### Système d’information sanitaire, données et recherche

#### Rôle dans le système

La capabilité transforme les données du système de santé en information utile : production, gestion, intégration, analyse et utilisation pour la décision, la recherche, le pilotage et la redevabilité. Elle est transversale à tous les flux de valeur, car aucun flux ne peut être mesuré, amélioré ou gouverné sans données fiables. Elle couvre :

- **Production et collecte** : génération et capture des données de santé aux points de service
- **Intégration et ingestion** : centralisation, validation d'intégrité et routage asynchrone des flux
- **Historisation événementielle** : journal d'événements immuable, source unique de vérité
- **Qualité et cohérence** : audit continu, traçabilité et fiabilité des données
- **Analyse et recherche** : entrepôt analytique, projections et exploitation pour la décision

Ces quatre capabilités ([CAP-13: Système d'information sanitaire, données et recherche](../../referentiel/capabilites/cap-13.md), [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../../referentiel/capabilites/cap-14.md), [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../../referentiel/capabilites/cap-15.md), [CAP-16: Gestion du portefeuille d'initiatives numériques](../../referentiel/capabilites/cap-16.md)) constituent le **socle commun (architecture runway)** dont l'absence bloque de nombreuses initiatives.

#### Flux de valeur

- [VS-01: Soins essentiels](../../referentiel/flux-valeur/vs-01.md)
- [VS-02: Prévention et surveillance](../../referentiel/flux-valeur/vs-02.md)
- [VS-03: Protection financière](../../referentiel/flux-valeur/vs-03.md)
- [VS-04: Pilotage du système](../../referentiel/flux-valeur/vs-04.md)

#### Rattachement ARTSN

- [ART-1: Intégration et ingestion](../../referentiel/chapitres/art-1.md)
- [ART-3: Historisation événementielle et profils de déploiement](../../referentiel/chapitres/art-3.md)
- [ART-5: Cohérence et qualité des données](../../referentiel/chapitres/art-5.md)

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 4/5 |

#### Propriétaire

Responsables de capabilités habilitantes

### Interopérabilité, référentiels nationaux et infrastructure numérique partagée

#### Rôle dans le système

La capabilité assure la cohérence, l’intégration, la souveraineté et la réutilisation des données et composants communs : référentiels partagés, couche d’échange, standards et services transverses. Elle évite la fragmentation du système en garantissant que chaque initiative réutilise les briques nationales au lieu de les dupliquer. Elle couvre :

- **Référentiels nationaux** : registres partagés, terminologies et structures de référence
- **Médiation et normalisation** : traduction et validation sémantique des payloads hétérogènes
- **Couche d’échange** : API Gateway, broker asynchrone et registre de schémas
- **Standards et interopérabilité** : alignement sur les profils techniques nationaux
- **Éradication des silos** : homologation obligatoire et réutilisation des briques communes

Ces quatre capabilités ([CAP-13: Système d'information sanitaire, données et recherche](../../referentiel/capabilites/cap-13.md), [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../../referentiel/capabilites/cap-14.md), [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../../referentiel/capabilites/cap-15.md), [CAP-16: Gestion du portefeuille d'initiatives numériques](../../referentiel/capabilites/cap-16.md)) constituent le **socle commun (architecture runway)** dont l’absence bloque et fragilise de nombreuses initiatives.

#### Flux de valeur

- [VS-01: Soins essentiels](../../referentiel/flux-valeur/vs-01.md)
- [VS-02: Prévention et surveillance](../../referentiel/flux-valeur/vs-02.md)
- [VS-03: Protection financière](../../referentiel/flux-valeur/vs-03.md)
- [VS-04: Pilotage du système](../../referentiel/flux-valeur/vs-04.md)

#### Rattachement ARTSN

- [ART-0: Accords de partage inter-institutionnels](../../referentiel/chapitres/art-0.md)
- [ART-2: Médiation et normalisation](../../referentiel/chapitres/art-2.md)
- [F-3: Éradication des silos technologiques](../../referentiel/fondations/f-3.md)
- [PT-01: Profil technique national](../../referentiel/profils/pt-01.md)

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 3/5 |

#### Propriétaire

Responsables de capabilités habilitantes

### Cybersécurité, confidentialité et gouvernance des données personnelles

#### Rôle dans le système

La capabilité garantit la confiance, la sécurité, la confidentialité et la protection des données personnelles de santé. Elle est la condition de l’adoption du système par les patients et les agents : une protection défaillante érode la confiance de toute la population dans le numérique de santé, quel que soit le service concerné. Elle couvre :

- **Sécurité et résilience** : chiffrement, journalisation immuable et protection des accès
- **Contrôle d’accès** : modèle strict par défaut, Zero-Trust et résidence de la donnée
- **Confidentialité** : minimisation, consentement et protection des données personnelles
- **Gouvernance de la sécurité** : homologation, conformité et responsabilité

Ces quatre capabilités ([CAP-13: Système d'information sanitaire, données et recherche](../../referentiel/capabilites/cap-13.md), [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../../referentiel/capabilites/cap-14.md), [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../../referentiel/capabilites/cap-15.md), [CAP-16: Gestion du portefeuille d'initiatives numériques](../../referentiel/capabilites/cap-16.md)) constituent le **socle commun (architecture runway)** dont l’absence bloque de nombreuses initiatives.

#### Flux de valeur

- [VS-01: Soins essentiels](../../referentiel/flux-valeur/vs-01.md)
- [VS-02: Prévention et surveillance](../../referentiel/flux-valeur/vs-02.md)
- [VS-03: Protection financière](../../referentiel/flux-valeur/vs-03.md)
- [VS-04: Pilotage du système](../../referentiel/flux-valeur/vs-04.md)

#### Rattachement ARTSN

- [ART-7: Sécurité, contrôle d'accès et résidence de la donnée](../../referentiel/chapitres/art-7.md)
- [F-4: Homologation obligatoire](../../referentiel/fondations/f-4.md)

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 1/5 | 3/5 |

#### Propriétaire

Responsables de capabilités habilitantes

### Gestion du portefeuille d’initiatives numériques

#### Rôle dans le système

La capabilité gouverne les investissements numériques du secteur : priorisation, coordination, rationalisation, suivi et évaluation selon leur contribution aux flux de valeur. Elle garantit que chaque financement sert une finalité de santé publique mesurable et que le portefeuille national évolue sans s’accumuler. Elle couvre :

- **Priorisation** : choix et rationnement des investissements numériques
- **Coordination** : alignement des initiatives sur les flux de valeur
- **Suivi et évaluation** : pilotage, tableaux de bord et redevabilité
- **Rationalisation** : évitement des doublons et gouvernance du portefeuille

Ces quatre capabilités ([CAP-13: Système d'information sanitaire, données et recherche](../../referentiel/capabilites/cap-13.md), [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../../referentiel/capabilites/cap-14.md), [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../../referentiel/capabilites/cap-15.md), [CAP-16: Gestion du portefeuille d'initiatives numériques](../../referentiel/capabilites/cap-16.md)) constituent le **socle commun (architecture runway)** dont l’absence bloque de nombreuses initiatives.

#### Flux de valeur

- [VS-03: Protection financière](../../referentiel/flux-valeur/vs-03.md)
- [VS-04: Pilotage du système](../../referentiel/flux-valeur/vs-04.md)

#### Rattachement ARTSN

- [ART-9: Garanties transactionnelles fortes](../../referentiel/chapitres/art-9.md)
- [F-4: Homologation obligatoire](../../referentiel/fondations/f-4.md)
- [F-6: Observabilité](../../referentiel/fondations/f-6.md)

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 1/5 | 3/5 |

#### Propriétaire

Responsables de capabilités habilitantes

### Engagement patient et identité numérique

#### Rôle dans le système

La capabilité garantit l'existence d'une identité unique, sécurisée et partagée pour chaque patient à travers le système d'information sanitaire national. Elle couvre :

- **Résolution d'identité** : recherche démographique, rapprochement de dossiers, détection des doublons
- **Gestion du consentement** : recueil, stockage et vérification du consentement du patient pour le partage de ses données
- **Identitovigilance** : surveillance et correction des erreurs d'identité, protection contre les usurpations
- **Engagement du patient** : accès du patient à ses données, participation active à la gestion de sa santé

Cette capabilité est **habilitante** : son absence bloque la continuité des soins ([VS-01: Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../referentiel/flux-valeur/vs-01.md)) et la protection financière ([VS-03: Protéger financièrement la population face aux dépenses de santé](../../referentiel/flux-valeur/vs-03.md)).

#### Flux de valeur

- [VS-01: Soins essentiels](../../referentiel/flux-valeur/vs-01.md)
- [VS-03: Protection financière](../../referentiel/flux-valeur/vs-03.md)

#### Rattachement ARTSN

- [F-1: Résilience face à la réalité géographique du pays](../../referentiel/fondations/f-1.md)
- [ART-4A: Résolution d'identité](../../referentiel/chapitres/art-4a.md)
- [ART-4B: Bases d'autorisation](../../referentiel/chapitres/art-4b.md)
- [PT-04: Profil technique national](../../referentiel/profils/pt-04.md)

#### Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 1/5 | 3/5 |

#### Propriétaire

DEPSI + Direction des Systèmes d'Information

### Coordination intersectorielle (One Health)

#### Rôle dans le système

La capabilité organise les échanges de données entre le secteur santé et les autres secteurs de l'État impliqués dans la coordination One Health : agriculture (WOAH/FAO), environnement (PNUE), intérieur (administrations territoriales). Elle couvre :

- **Échanges inter-institutionnels** : accords de partage, protocoles d'échange, médiation des données
- **Coordination épidémique** : partage d'informations entre santé humaine, animale et environnementale
- **Surveillance conjointe** : détection précoce des événements de santé publique à interface homme-animal-environnement
- **Riposte coordonnée** : orchestration des réponses inter-ministérielles

Cette capabilité est **habilitante** : son absence bloque la surveillance sanitaire ([VS-02: Prévenir, détecter et répondre aux risques sanitaires](../../referentiel/flux-valeur/vs-02.md)) conformément aux obligations du RSI.

#### Flux de valeur

- [VS-02: Prévention et surveillance](../../referentiel/flux-valeur/vs-02.md)

#### Rattachement ARTSN

- [ART-0: Accords de partage inter-institutionnels](../../referentiel/chapitres/art-0.md)
- [ART-8D: Chorégraphie inter-institutionnelle](../../referentiel/chapitres/art-8d.md)
- [PT-01: Profil technique national](../../referentiel/profils/pt-01.md)

#### Référentiels normatifs

- **RSI** — Règlement Sanitaire International (2005)
- **Tripartite Plus** — OMS–WOAH–FAO–PNUE

#### Maturité

| Niveau actuel | Niveau cible (3 ans) |
|---------------|----------------------|
| 1/5 | 2/5 |

#### Propriétaire

Secrétariat Général du Ministère + DEPSI

<!-- END:GENERATED -->
## Liens

- [Capabilités](./index.md)

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
