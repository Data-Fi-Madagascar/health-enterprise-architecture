---
title: Fondements stratégiques et normatifs
id: fondements
domain: 00_overview
version: "1.0.0"
status: draft
last_reviewed: 2026-08-19
owner: Ministère de la Santé Publique
tags: [fondements, stratégie, normes, madagascar]
---

# Fondements stratégiques et normatifs

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ◐ |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## Ancrage dans les stratégies nationales

Le cadre tire sa légitimité et son orientation de trois documents stratégiques nationaux et d'un cadre juridique structurant :

- **Plan de Développement du Secteur Santé (PDSS) 2020-2024** — référence principale de planification. Définit huit axes stratégiques que le cadre traduit en flux de valeur et capabilités.
- **Stratégie Nationale de Santé Digitale (SNSD) 2023-2027** — orientations pour le numérique en santé, repositionnées comme capabilités numériques transversales au service des priorités de santé. Deuxième édition, succédant à la stratégie 2019-2023.
- **Plan Stratégique de Renforcement du Système d'Information Sanitaire (PSRSIS) 2023-2027** — priorités relatives aux données de santé ; constitue la fondation informationnelle du cadre.

## Cadre juridique

Le cadre est structuré par un cadre juridique national et continental :

- **Loi n°2014-038 sur la protection des données à caractère personnel** (promulguée le 9 janvier 2015, décret d'application 2023-1541) — La loi institue la Commission Malagasy de l'Informatique et des Libertés (CMIL) comme autorité indépendante. Elle définit les principes de protection des données personnelles (finalité, loyauté, minimisation, sécurité, droit d'accès, consentement) qui sont intégrés dans les règles de gouvernance des données du cadre (§Protection des données personnelles de santé). L'article 23 prévoit explicitement que les données de santé peuvent être communiquées à la personne concernée, directement ou par l'intermédiaire du médecin qu'elle désigne.
- **Convention de Malabo** (ratifiée par Madagascar, loi 2024-004) — Convention de l'Union Africaine sur la cybersécurité et la protection des données à caractère personnel. Elle renforce le cadre juridique transfrontalier et s'aligne sur les principes de la loi 2014-038.
- **Plan Stratégique quinquennal du Numérique 2023-2028** — Vision nationale de transformation numérique, intégrant la santé parmi les secteurs prioritaires.

## Lecture des axes stratégiques du PDSS dans le cadre

Certains axes génèrent directement un flux de valeur pour la population ; d'autres constituent des capabilités habilitantes.

| Code | Axe stratégique PDSS | Lecture dans le cadre |
|------|----------------------|------------------------|
| AXE-01 | Gouvernance, cadre institutionnel et coordination | Capabilité de gouvernance soutenant le flux de pilotage |
| AXE-02 | Gestion rationnelle des ressources | Capabilité habilitante ressources |
| AXE-03 | Renforcement du capital humain | Capabilité habilitante ressources humaines |
| AXE-04 | Accès équitable aux soins essentiels intégrés de qualité | Flux de valeur — soins |
| AXE-05 | Prévention, promotion, urgences, épidémies et catastrophes | Flux de valeur — protection sanitaire |
| AXE-06 | Financement de la santé et protection financière | Flux de valeur — protection financière |
| AXE-07 | Système d'information sanitaire et recherche | Capabilité décisionnelle transversale |
| AXE-08 | Santé communautaire | Canal et capabilité transversale de proximité |

Les quatre axes de la SNSD (gouvernance digitale, solutions, ressources, financement) sont lus comme des capabilités numériques transversales qui servent les flux de valeur santé sans en constituer eux-mêmes.

## Référentiels normatifs internationaux

Trois référentiels internationaux opèrent à des niveaux différents et complémentaires. Ils définissent des principes et modèles d'organisation, sans prescrire de logiciels. Ensemble, ils forment un cadre de référence pour l'architecture numérique santé que Madagascar adapte à son contexte.

### Infrastructure Numérique de Données pour la Santé (DPI-H) — OMS/ITU

Le cadre **Digital Public Infrastructure for Health (DPI-H)** est une initiative conjointe de l'OMS et de l'ITU dans le cadre du Global Initiative on Digital Health (GIDH). Il définit l'infrastructure numérique que tout système de santé national doit développer comme **bien commun**, en distinguant deux niveaux :

**Infrastructure numérique transversale (DPI-F)** — composantes partagées entre tous les secteurs de l'administration publique : identité numérique, paiements, échange de données, consentement. Ces composantes sont fournies par l'État et réutilisées par le secteur santé.

**Infrastructure numérique santé (DPI-H)** — composantes spécifiques au secteur santé qui s'appuient sur la DPI-F :

| Composante DPI-H | Fonction | Réponse HEA |
|-------------------|----------|-------------|
| Registre des bénéficiaires (Client Registry) | Identifier de manière unique les patients | PT-04, ART-4a |
| Registre des formations sanitaires (Facility Registry) | Identifier les lieux de soins | PT-06, ART-4 |
| Registre des professionnels de santé (Health Worker Registry) | Identifier les prestataires | PT-05, ART-4a |
| Couche d'échange (Interoperability Layer) | Router et transformer les messages | PT-01, PT-02, ART-1, ART-2 |
| Service de terminologie | Codes et classifications communs | PT-07, STD-0006, STD-0007 |
| Dossier partagé (Shared Health Record) | Repository longitudinal patient | Couche 4 ARTSN |
| Système de gestion de l'information sanitaire (HMIS) | Données agrégées et tableaux de bord | PT-08, PT-09, ART-6 |
| Gestion logistique (LMIS) | Visibilité sur les produits de santé | ART-10 |
| Cadre de confiance-sécurité | Authentification, autorisation, journalisation | PT-10, PT-12, ART-7 |

La **Référence Architecture DPI-H** (publiée par l'OMS via SMART Guidelines) fournit les spécifications techniques pour chaque composante, basées sur HL7 FHIR R4. Elle est directement applicable à l'HEA : les 9 composantes DPI-H correspondent aux 16 profils PTISN.

*Répond à :* que doit posséder le système national comme infrastructure partagée ?

### Architecture OpenHIE (Open Health Information Exchange)

**OpenHIE** est une communauté de pratique mondiale qui fournit un **cadre architectural réutilisable** pour l'échange d'informations de santé à grande échelle. Contrairement à un logiciel, OpenHIE définit un **patron d'architecture** (pattern) que les pays adaptent à leur contexte.

L'architecture OpenHIE s'organise en **trois couches** :

| Couche | Composantes | Fonction |
|--------|-------------|----------|
| **Couche 1 — Services métier et registres** | Client Registry, Facility Registry, Health Worker Registry, Terminology Service, Shared Health Record, HMIS, LMIS, Finance & Insurance | Source de vérité et référence pour chaque entité du système |
| **Couche 2 — Couche d'interopérabilité** | Interopability Layer (authentification, routage, correspondance d'entités) | Passerelle entre les sources de vérité et les applications de terrain |
| **Couche 3 — Points de service** | EMR, DHIS2, applications mobiles, outils communautaires | Interfaces utilisateurs au contact des patients et agents de santé |

La force d'OpenHIE est son approche **"for whom, by whom, where, what"** : chaque échange de données est contextualisé par l'identité du patient, du prestataire, du lieu et de l'activité. Cette approche est directement reflétée dans l'HEA à travers les capacités CAP-INT-01 (identité bénéficiaire), CAP-INT-02 (professionnels), CAP-INT-04 (structures) et CAP-INT-05 (terminologie).

OpenHIE s'appuie sur les standards IHE (Integrating the Healthcare Enterprise) et est reconnu par l'OMS comme cadre de référence pour la DPI-H.

*Répond à :* comment organiser les composantes d'un système d'information de santé cohérent et interopérable ?

### GovStack — blocs de construction réutilisables

**GovStack** est une initiative mondiale qui fournit des **spécifications techniques** pour construire des services publics numériques souverains, interopérables et centrés sur le citoyen. Il ne s'agit pas d'un logiciel mais d'un ensemble de **blocs de construction** (Building Blocks) modulaires et réutilisables.

GovStack distingue deux catégories de blocs :

**Blocs fondationnels** — dépendances universelles pour tout l'écosystème numérique :

| Bloc fondationnel | Fonction | Application santé |
|-------------------|----------|-------------------|
| **Identité numérique** | Authentification et vérification des personnes | INP (PT-04), identification des patients |
| **Médiateur d'information** | Échange de données sécurisé entre systèmes | X-Road (PT-01), couche d'échange |
| **Workflow** | Orchestration des processus métier | Orchestration bornée (PT-16, ART-8a) |
| **Registre** | Sources de vérité pour les entités référentes | Registres nationaux (PT-05, PT-06) |

**Blocs fonctionnels** — fonctions autonomes qui améliorent le stack sans être des prérequis :

| Bloc fonctionnel | Fonction | Application santé |
|------------------|----------|-------------------|
| **Paiements** | Transactions financières sécurisées | Couverture sanitaire (VS-02) |
| **Messaging** | Notifications et alertes | Alertes sanitaires, surveillance |
| **Géospatial** | Services de géolocalisation | Cartographie sanitaire (ART-4d) |
| **Génération de documents** | Production de documents structurés | Certificats, rapports |

L'approche GovStack par **API ouvertes** et **conteneurs** permet l'interopérabilité sans vendor lock-in. Elle est alignée sur le DPI-H de l'OMS et est directement applicable à l'HEA : les blocs fondationnels GovStack correspondent aux capacités transversales du CNISN, tandis que les blocs fonctionnels se traduisent par les profils PTISN.

*Répond à :* comment le système santé s'intègre-t-il dans l'Infrastructure Numérique de l'État malgache ?

## Articulation entre les trois référentiels

| Question | DPI-H (OMS) | OpenHIE | GovStack |
|----------|-------------|---------|----------|
| *Que doit-on construire ?* | 9 composantes santé | — | Blocs fondationnels + fonctionnels |
| *Comment l'organiser ?* | — | 3 couches architecturales | Architecture modulaire par API |
| *Comment relier à l'État ?* | DPI-F → DPI-H | — | Blocs transversaux → services sectoriels |
| *Quels standards ?* | FHIR R4, SMART Guidelines | IHE, HL7 | API ouvertes, conteneurs |

L'HEA utilise les trois référentiels de manière complémentaire : le DPI-H définit les composantes nécessaires, OpenHIE fournit le patron d'architecture, et GovStack offer les spécifications techniques pour l'intégration dans l'État numérique malgache.

## Liens

- Modèle de valeur
- Flux de valeur
- Principes

## Références

- **matrice de lecture** — Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Modèle de valeur** — Modèle national de valeur (`00_caesn/00_overview/value-model.md`)
- **Flux de valeur** — Flux de valeur nationaux de santé (`00_caesn/01_value-streams/index.md`)
- **Principes** — Principes d'architecture (`00_caesn/02_principles/index.md`)
- **DPI-H Reference Architecture** — OMS/ITU (`https://smart.who.int/ra/`)
- **OpenHIE Architecture Specification** — Communauté de pratique (`https://guides.ohie.org/arch-spec/`)
- **GovStack Implementation Playbook** — Initiative mondiale (`https://specs.govstack.global/`)
