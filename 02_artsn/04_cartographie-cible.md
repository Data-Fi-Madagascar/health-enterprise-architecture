---
title: Cartographie conceptuelle cible
id: artsn-cartographie-cible
domain: 02_artsn
version: "0.1.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, cartographie, couches, axes, niveau-3]
---

# Cartographie conceptuelle cible

L'architecture conceptuelle présentée dans cette section est l'incarnation visuelle et l'application physique stricte des contraintes et des patterns définis dans les [chapitres](./03_chapitres/index.md). Chaque bloc horizontal et vertical exécute techniquement un ou plusieurs chapitres normatifs de l'ARTSN.

La cartographie est structurée en **six couches horizontales** (de l'infrastructure à la gouvernance) traversées par **deux axes verticaux** transversaux. Elle s'articule avec les [six couches applicatives du CAESN](../00_caesn/05_application/layers.md).

| Couche | Intitulé | Chapitres ARTSN associés |
|--------|----------|--------------------------|
| [6](#couche-6--pilotage-gouvernance-et-actions-intersectorielles) | Pilotage, Gouvernance et actions intersectorielles | VS-04, [ART-0](./03_chapitres/art-0-accords-partage.md) |
| [5](#couche-5--projections-analytiques-et-modèles) | Projections analytiques et Modèles | [ART-6](./03_chapitres/art-6-analytique-restitution.md), [ART-5](./03_chapitres/art-5-coherence-qualite-donnees.md), [ART-8b](./03_chapitres/art-8b-modelisation-graphe.md), [ART-4d](./03_chapitres/art-4d-referentiel-geospatial.md), [ART-9](./03_chapitres/art-9-garanties-transactionnelles.md) |
| [4](#couche-4--interopérabilité-et-services-partagés) | Interopérabilité et services partagés | [ART-3](./03_chapitres/art-3-historisation-evenementielle.md), [ART-4](./03_chapitres/art-4-referentiels-metadonnees.md), [ART-2](./03_chapitres/art-2-mediation-normalisation.md), [ART-8a](./03_chapitres/art-8a-orchestration-processus-borne.md), [ART-4a](./03_chapitres/art-4a-resolution-identite.md), [ART-4c](./03_chapitres/art-4c-eligibilite-couverture.md) |
| [3](#couche-3--échange-transport-et-ingestion) | Échange, transport et ingestion | [ART-1](./03_chapitres/art-1-integration-ingestion.md), F.3, [ART-8c](./03_chapitres/art-8c-agregation-par-lot.md) |
| [2](#couche-2--point-de-service) | Point de service | F.1, ENF-1 |
| [1](#couche-1--infrastructure) | Infrastructure | [ART-7](./03_chapitres/art-7-securite-controle-acces.md) |
| Axe 1 | Sécurité et confiance numérique | [ART-7](./03_chapitres/art-7-securite-controle-acces.md) |
| Axe 2 | Gouvernance de données | F.4, [ART-0](./03_chapitres/art-0-accords-partage.md) |

## Couche 6 — Pilotage, Gouvernance et actions intersectorielles

**Contenu normatif.** Cette couche constitue la **vitrine décisionnelle unique de l'État**. Elle possède un droit exclusif de lecture sur les projections analytiques et n'exécute aucune écriture opérationnelle. Elle a l'obligation de fournir des espaces de visualisation cloisonnés et partagés entre les ministères partenaires pour évaluer la performance sanitaire et guider l'action publique.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (cellules de crise multi-ministérielles, directions stratégiques) : elle seule permet de garantir que les décisions politiques s'appuient sur une vision macro-sanitaire unifiée, épurée de toute altération, sans rompre le pipeline.

- **Rattachement** : support du flux de valeur 4 ([VS-04](./01_flux-de-valeur.md#vs-04--piloter-coordonner-et-améliorer-la-performance-du-système-de-santé)).
- **Composants associés** : tableaux de bord de performance sanitaire nationale, portail de suivi de la CSU, portail de gestion des ressources du système, centre de commande des alertes épidémiques, plateforme de gestion des crises intersectorielles, portail de veille environnementale et sanitaire.
- **Statut : Stable.**

## Couche 5 — Projections analytiques et Modèles

**Contenu normatif.** Cette couche sépare structurellement les flux analytiques du stockage transactionnel. Elle a l'obligation d'**extraire, nettoyer et masquer de façon irréversible** les données opérationnelles et les flux des secteurs externes afin de les organiser selon les modèles de projections analytiques exigés par le pays.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (modèles prédictifs d'IA, requêtes lourdes des chercheurs, algorithmes de transmission) : elle seule permet d'exécuter des analyses de masse longitudinales transversales sans jamais ralentir les serveurs de soins et sans exposer l'identité des citoyens, sans rompre le pipeline.

- **Rattachement** : application physique directe du pattern CQRS ([ART-6](./03_chapitres/art-6-analytique-restitution.md)).
- **Composants associés** : pipeline d'ingestion ETL, moteur d'IA prédictive, routeur d'escalade et d'alertes (ART-5), entrepôt Lakehouse / projections tabulaires, moteur de graphes (Graph Store — ART-8b), référentiel spatio-temporel (ART-4d), réconciliation analytique (Grand Livre — ART-9).
- **Statut : Stable.**

## Couche 4 — Interopérabilité et services partagés

**Contenu normatif.** Cette couche est le **cœur applicatif de la santé au présent**. Elle a l'obligation de centraliser les registres nationaux et d'assurer la persistance clinique temps réel. Elle doit orchestrer les parcours et assurer la médiation sémantique universelle face aux ontologies de référence.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (échanges cliniques immédiats, consultations, identitovigilance probabiliste) : elle seule permet de recevoir et de valider la conformité des données médicales à la milliseconde et de fournir un dossier patient unique partagé sécurisé, sans rompre le pipeline.

- **Rattachement** : exécution de la source de vérité au présent (Profil B d'[ART-3](./03_chapitres/art-3-historisation-evenementielle.md)) et des Référentiels Nationaux ([ART-4](./03_chapitres/art-4-referentiels-metadonnees.md)).
- **Composants associés** : moteur d'intégration & médiation (ART-2), orchestrateur de parcours / gestionnaire de Sagas (ART-8a), répertoire de données cliniques opérationnelles, référentiel des métadonnées d'exploitation (ART-4), registre des terminologies, registre des clients / Index National des Patients (INP — ART-4a), registre d'éligibilité et de couverture (CSU — ART-4c), registre des personnels, registre des produits, intrants et indicateurs.
- **Statut : Stable.**

## Couche 3 — Échange, transport et ingestion

**Contenu normatif.** Cette couche gère l'infrastructure d'ingestion réseau. Elle est structurellement **dépourvue de toute logique ou intelligence métier**. Elle a l'obligation d'intercepter les requêtes à la périphérie, de bloquer les messages non conformes aux contrats, d'assurer la persistance tampon en file d'attente et d'exécuter les compensations par lots.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (connexions simultanées de milliers d'applications de terrain, micro-coupures télécoms) : elle seule permet d'encaisser la charge et de garantir la livraison des messages sans perte vers les couches supérieures, sans rompre le pipeline.

- **Rattachement** : exécution technique du transport asynchrone ([ART-1](./03_chapitres/art-1-integration-ingestion.md) et [F.3](./00_fondations.md#f3--éradication-des-silos-technologiques)).
- **Composants associés** : API Gateway, registre de schémas (F.3), message broker asynchrone, compensateur / regroupeur de flux (Netting — ART-8c).
- **Statut : Stable.**

## Couche 2 — Point de service

**Contenu normatif.** Cette couche constitue la **ligne de front logicielle**. Elle a l'obligation d'exécuter des applications capables de capturer les soins, les dispensations et les mouvements logistiques en l'absence totale de réseau Internet. Elle doit ordonner ses écritures locales sous forme de **journaux d'événements inaltérables**.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (prise en charge des patients dans les CSB isolés, saisie de stocks en entrepôts de brousse) : elle seule permet aux acteurs du terrain de travailler en toute autonomie sans dépendre d'une connexion centrale permanente, sans rompre le pipeline.

- **Rattachement** : application du principe d'autonomie locale ([ENF-1](./02_exigences-contextuelles.md#enf-1--résilience-à-l-instabilité-réseau)) et de l'historisation à la source ([F.1](./00_fondations.md#f1--résilience-face-à-la-réalité-géographique-du-pays)).
- **Composants associés** : dossiers & statistiques de santé (hôpitaux), gestion des pharmacies (PMIS), santé communautaire mobile (offline), espace santé patient, chaîne logistique (LMIS), surveillance de la santé animale (zoonoses), enquêtes & capteurs terrain.
- **Statut : Stable.**

## Couche 1 — Infrastructure

**Contenu normatif.** Cette couche est le **socle matériel de la Nation**. Elle a l'obligation d'héberger les données cliniques sur des infrastructures physiques situées sur le territoire national et d'organiser la topologie distribuée en cascade pour garantir le basculement automatique en cas de sinistre.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (datacenters nationaux, serveurs de districts, tunnels VPN gouvernementaux) : elle seule garantit la souveraineté numérique de l'État et la sécurité physique des données contre les pannes massives et les ingérences extérieures, sans rompre le pipeline.

- **Rattachement** : support matériel de la clause de résidence et de sécurité ([ART-7](./03_chapitres/art-7-securite-controle-acces.md)).
- **Composants associés** : nœud central (datacenters nationaux certifiés HDS), nœuds régionaux (clusters de district — Fog), nœuds locaux (équipements chiffrés — Edge), liaisons dédiées & VPN, réseau privé MPLS, réseaux mobiles privés (APN sécurisés).
- **Statut : Stable.**

## Axes verticaux transversaux

Les deux axes traversent l'ensemble des six couches et exécutent des obligations transversales.

### Axe vertical 1 — Sécurité et confiance numérique

**Contenu normatif.** Cet axe est le **bras armé technologique de la sécurité**. Il a l'obligation d'intercepter transversalement l'ensemble des six couches pour forcer le modèle de confiance, authentifier les acteurs, valider les consentements, chiffrer les données au repos et générer des journaux d'audit inaltérables.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (tentatives de cyberattaques, connexions illégitimes, vol de tablettes sur le terrain) : elle seule permet de garantir le respect absolu du secret médical et de bloquer les intrusions à la périphérie, sans rompre le pipeline.

- **Rattachement** : application transversale du cadre de cybersécurité ([ART-7](./03_chapitres/art-7-securite-controle-acces.md)).
- **Composants associés** : gestion des identités, contrôle d'accès fin (RBAC/ABAC), gestion des consentements, infrastructure de clés publiques (PKI), passerelle de confiance mondiale OMS (GDHCN), journal d'audit immuable, moteur de chiffrement.
- **Statut : Stable.**

### Axe vertical 2 — Gouvernance de données

**Contenu normatif.** Cet axe constitue l'**autorité politique, morale et éthique** de la plateforme. Il a l'obligation de fixer le cadre réglementaire humain, d'instruire et de valider l'homologation des projets de santé numérique, et de trancher les litiges de qualité ou de sécurité.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (comités humains, signatures de conventions, chartes juridiques de protection) : elle seule permet d'asseoir la légitimité politique de la plateforme et de garantir le respect des accords interministériels de partage de données, sans rompre le pipeline.

- **Rattachement** : cadre d'application du processus d'homologation obligatoire ([F.4](./00_fondations.md#f4--homologation-obligatoire)) et d'[ART-0](./03_chapitres/art-0-accords-partage.md).
- **Composants associés** : registre des accords inter-institutions, charte nationale de protection, conventions internationales, comité national d'homologation, registre des initiatives, comité d'éthique, cellule d'audit, arbitrage et risques.
- **Statut : Stable.**

## Liens

- [Chapitres et patterns de référence](./03_chapitres/index.md)
- [CAESN — couches applicatives](../00_caesn/05_application/layers.md)
- [VS-04 — Pilotage](./01_flux-de-valeur.md)
