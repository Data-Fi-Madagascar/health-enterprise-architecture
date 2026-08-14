---
title: Glossaire de l'ARTSN (niveau 3)
id: artsn-glossary
domain: 02_artsn
version: "0.1.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: [artsn, glossaire, terminologie, niveau-3]
---

# Glossaire de l'ARTSN (niveau 3)

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](./reading-matrix.md).

Termes techniques propres à l'ARTSN. Les définitions des patterns mobilisés par les chapitres (event sourcing, CQRS, médiateur, SCD, golden record…) sont détaillées dans l'[Annexe B — Glossaire des patterns](./07_annexes/b-glossaire-patterns.md) ; les termes transverses de l'architecture sont dans le [glossaire du CAESN](../00_caesn/10_annexes/glossary.md).

## Termes d'architecture technique

**Chapitre (ART-)** — Unité normative de la Partie IV de l'ARTSN définissant une règle d'or ou un contrat technique d'interface obligatoire. Les chapitres portent un statut Stable, Provisoire ou Proposition ouverte selon la [table de maturité](./07_annexes/a-table-de-maturite.md).

**Configurations et paramétrages** — Rapport des choix d'implémentation (valeurs, règles, réglages) qui transposent un standard technique dans une solution logicielle donnée, sur un périmètre et un environnement précis.

**Contrat d'interface** — Spécification technique opposable d'un échange entre composants : format, schéma, version du standard, invariants de sécurité et de résidence de la donnée. Le respect du contrat conditionne l'[homologation](../00_caesn/10_annexes/glossary.md).

**Couche applicative** — Niveau logique de la [cartographie cible](04_cartographie-cible/index.md) organisant les composants (infrastructure, données, services partagés, applications métier, intégration, présentation) selon des responsabilités séparées.

**Homologation technique** — Contrôle par lequel une solution est vérifiée pour conformité aux standards techniques et aux exigences de sécurité de l'ARTSN avant mise en production, indépendamment des règles d'homologation fonctionnelle du niveau 1.

**Modèle d'hébergement** — Choix d'hébergement (sur site national, cloud souverain, hybride) conforme à l'exigence de [résidence de la donnée](../referentiel/chapitres/art-7.md) et aux fondations du niveau.

**Norme et standard technique** — Spécification technique normative (formats, protocoles, API) retenue par l'ARTSN et opposable lors d'une homologation ; déclinée depuis les standards du [niveau 1](../00_caesn/09_standards/index.md).

**Pattern technique** — Solution réutilisable à niveau de conception d'un problème récurrent d'intégration, de données, de sécurité ou de processus (voir l'[Annexe B](./07_annexes/b-glossaire-patterns.md)).

## Termes de fondations

**F.1 — Identité et registres** — Fondation garantissant l'existence d'identifiants uniques et de registres partagés pour les patients, les professionnels et les formations sanitaires.

**F.2 — Normalisation** — Fondation assurant que les données échangées utilisent des codifications et des terminologies standardisées.

**F.3 — Interopérabilité** — Fondation garantissant la capacité des systèmes à échanger et à utiliser mutuellement les données.

**F.4 — Sécurité et protection** — Fondation assurant la confidentialité, l'intégrité et la disponibilité des données de santé.

**F.5 — Analytique et pilotage** — Fondation permettant la consolidation et l'analyse des données pour le pilotage du système de santé.

**F.6 — Gouvernance technique** — Fondation organisant la prise de décision technique et le suivi de la conformité.

## Termes de cartographie cible

**Cartographie cible** — Représentation de l'architecture technique finale du système d'information sanitaire, organisée en 6 couches et 2 axes transversaux.

**Couche infrastructure** — Niveau d'abstraction regroupant les composants matériels et logiciels de base (serveurs, réseaux, stockage).

**Couche données** — Niveau d'abstraction regroupant les bases de données, les entrepôts et les référentiels.

**Couche services partagés** — Niveau d'abstraction regroupant les services réutilisables par plusieurs applications (identité, terminologie, médiation).

**Couche applications métier** — Niveau d'abstraction regroupant les applications dédiées à des fonctions spécifiques (dossier patient, gestion des stocks, surveillance).

**Couche intégration** — Niveau d'abstraction regroupant les mécanismes d'échange entre les applications et les services.

**Couche présentation** — Niveau d'abstraction regroupant les interfaces utilisateur (applications mobiles, portails web, tableaux de bord).

**Axe transversal sécurité** — Dimension transversale assurant la sécurité sur toutes les couches (authentification, autorisation, chiffrement, audit).

**Axe transversal gouvernance** — Dimension transversale organisant la prise de décision et le suivi sur toutes les couches.

## Termes de chapitres ART

**ART-0 — Accords de partage** — Chapitre définissant les règles pour la formalisation des accords entre organisations concernant le partage de données.

**ART-1 — Intégration et ingestion** — Chapitre définissant les règles pour l'intégration des données provenant de sources multiples.

**ART-2 — Médiation et normalisation** — Chapitre définissant les règles pour la transformation et la normalisation sémantique des données.

**ART-3 — Authentification et autorisation** — Chapitre définissant les règles pour la gestion des identités et des droits d'accès.

**ART-4 — Référentiels** — Chapitre définissant les règles pour la gestion des bases de données de référence.

**ART-5 — Analytique et pilotage** — Chapitre définissant les règles pour la consolidation et l'analyse des données.

**ART-6 — Échange de données agrégées** — Chapitre définissant les règles pour l'échange de rapports périodiques et d'indicateurs.

**ART-7 — Sécurité et résidence** — Chapitre définissant les règles de sécurité et de localisation des données.

**ART-8 — Qualité et validation** — Chapitre définissant les règles pour le contrôle qualité des données.

**ART-9 — Déploiement et migration** — Chapitre définissant les règles pour la mise en production et la migration des systèmes.

**ART-10 — Supervision et monitoring** — Chapitre définissant les règles pour la surveillance du fonctionnement des systèmes.

**ART-11 — Coordination intersectorielle** — Chapitre définissant les règles pour les échanges avec d'autres secteurs de l'État.

## Termes de données

**Concept de données** — Unité atomique du dictionnaire, identifiant un objet d'information du système de santé. Chaque concept possède 7 attributs : nom, description, type, source, propriétaire, cycle de vie et référentiel source (mapping technique vers FHIR).

**Domaine de données** — Catégorie regroupant les concepts par affinité métier. Le dictionnaire ARTSN en définit 7 : Patient, Professions et acteurs, Structures et services, Produits de santé, Événements et actes, Géographie, Santé publique et pilotage.

**Référentiel source** — Champ technique d'un concept de données indiquant la ressource FHIR ou le standard technique correspondant (ex. : Patient FHIR R4, Organization FHIR R4).

**Niveau sémantique** — Niveau de description d'un concept de données indépendant de toute technologie, décrivant ce que le concept représente dans le monde réel (nom, description, type métier, propriétaire métier).

## Termes techniques

**API** — *Application Programming Interface*. Interface de programmation permettant à deux systèmes de communiquer entre eux.

**Endpoint** — Point d'accès d'une API, identifié par une URL, recevant des requêtes et retournant des réponses.

**Payload** — Données transportées par un message ou une requête API.

**Schema** — Schéma définissant la structure et les contraintes des données échangées (JSON Schema, XML Schema).

**Versioning** — Mécanisme de gestion des versions des API et des schémas pour assurer la compatibilité ascendante.

**Chiffrement** — Processus de transformation des données pour les rendre illisibles à toute personne non autorisée.

**Signature numérique** — Mécanisme cryptographique garantissant l'authenticité et l'intégrité d'un message ou d'un document.

**Journalisation** — Processus d'enregistrement des événements (accès, modifications, erreurs) pour la traçabilité et l'audit.

## Liens

- [Index de l'ARTSN](./index.md)
- [Matrice de lecture de l'ARTSN](./reading-matrix.md)
- [Acronymes de l'ARTSN](./acronyms.md)
- [Annexe B — Glossaire des patterns](./07_annexes/b-glossaire-patterns.md)
- [Glossaire du CAESN (niveau 1)](../00_caesn/10_annexes/glossary.md)
