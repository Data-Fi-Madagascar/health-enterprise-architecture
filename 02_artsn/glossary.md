---

title: Glossaire de l'ARTSN (niveau 3)
id: artsn-glossary
domain: 02_artsn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: ["artsn", "glossaire", "terminologie", "niveau-3"]
---

# Glossaire de l'ARTSN (niveau 3)

## Pour qui lire ce document

**Niveau :** niveau 3 : Architecture de Référence Technique de la Santé Numérique.

Ce glossaire s'adresse prioritairement aux équipes DEPSI et techniques. Les directions métier et programmes ainsi que les équipes SIS, données et suivi-évaluation y trouveront un complément utile. Les décideurs institutionnels et les partenaires techniques et financiers peuvent le consulter ponctuellement lorsqu'ils rencontrent des termes techniques spécifiques. Pour une vue d'ensemble des niveaux de pertinence, consultez la matrice de lecture.

Termes techniques propres à l'ARTSN. Les définitions des patterns mobilisés par les chapitres (event sourcing, CQRS, médiateur, SCD, golden record…) sont détaillées dans l'Annexe B : Glossaire des patterns ; les termes transverses de l'architecture sont dans le glossaire du CAESN.

## Termes d'architecture technique

**Chapitre (ART-)** : Unité normative de la Partie IV de l'ARTSN définissant une règle d'or ou un contrat technique d'interface obligatoire. Les chapitres portent un statut Stable, Provisoire ou Proposition ouverte selon la table de maturité.

**Configurations et paramétrages** : Rapport des choix d'implémentation (valeurs, règles, réglages) qui transposent un standard technique dans une solution logicielle donnée, sur un périmètre et un environnement précis.

**Contrat d'interface** : Spécification technique opposable d'un échange entre composants : format, schéma, version du standard, invariants de sécurité et de résidence de la donnée. Le respect du contrat conditionne l'homologation.

**Couche applicative** : Niveau logique de la cartographie cible organisant les composants (infrastructure, données, services partagés, applications métier, intégration, présentation) selon des responsabilités séparées.

**Homologation technique** : Contrôle par lequel une solution est vérifiée pour conformité aux standards techniques et aux exigences de sécurité de l'ARTSN avant mise en production, indépendamment des règles d'homologation fonctionnelle du niveau 1.

**Modèle d'hébergement** : Choix d'hébergement (sur site national, cloud souverain, hybride) conforme à l'exigence de résidence de la donnée et aux fondations du niveau.

**Norme et standard technique** : Spécification technique normative (formats, protocoles, API) retenue par l'ARTSN et opposable lors d'une homologation ; déclinée depuis les standards du niveau 1.

**Pattern technique** : Solution réutilisable à niveau de conception d'un problème récurrent d'intégration, de données, de sécurité ou de processus (voir l'Annexe B).

## Termes de fondations

**F.1 : Identité et registres** : Fondation garantissant l'existence d'identifiants uniques et de registres partagés pour les patients, les professionnels et les formations sanitaires.

**F.2 : Normalisation** : Fondation assurant que les données échangées utilisent des codifications et des terminologies standardisées.

**F.3 : Interopérabilité** : Fondation garantissant la capacité des systèmes à échanger et à utiliser mutuellement les données.

**F.4 : Sécurité et protection** : Fondation assurant la confidentialité, l'intégrité et la disponibilité des données de santé.

**F.5 : Analytique et pilotage** : Fondation permettant la consolidation et l'analyse des données pour le pilotage du système de santé.

**F.6 : Gouvernance technique** : Fondation organisant la prise de décision technique et le suivi de la conformité.

## Termes de cartographie cible

**Cartographie cible** : Représentation de l'architecture technique finale du système d'information sanitaire, organisée en 6 couches et 2 axes transversaux.

**Couche infrastructure** : Niveau d'abstraction regroupant les composants matériels et logiciels de base (serveurs, réseaux, stockage).

**Couche données** : Niveau d'abstraction regroupant les bases de données, les entrepôts et les référentiels.

**Couche services partagés** : Niveau d'abstraction regroupant les services réutilisables par plusieurs applications (identité, terminologie, médiation).

**Couche applications métier** : Niveau d'abstraction regroupant les applications dédiées à des fonctions spécifiques (dossier patient, gestion des stocks, surveillance).

**Couche intégration** : Niveau d'abstraction regroupant les mécanismes d'échange entre les applications et les services.

**Couche présentation** : Niveau d'abstraction regroupant les interfaces utilisateur (applications mobiles, portails web, tableaux de bord).

**Axe transversal sécurité** : Dimension transversale assurant la sécurité sur toutes les couches (authentification, autorisation, chiffrement, audit).

**Axe transversal gouvernance** : Dimension transversale organisant la prise de décision et le suivi sur toutes les couches.

## Termes de chapitres ART

**ART-0 : Accords de partage** : Chapitre définissant les règles pour la formalisation des accords entre organisations concernant le partage de données.

**ART-1 : Intégration et ingestion** : Chapitre définissant les règles pour l'intégration des données provenant de sources multiples.

**ART-2 : Médiation et normalisation** : Chapitre définissant les règles pour la transformation et la normalisation sémantique des données.

**ART-3 : Authentification et autorisation** : Chapitre définissant les règles pour la gestion des identités et des droits d'accès.

**ART-4 : Référentiels** : Chapitre définissant les règles pour la gestion des bases de données de référence.

**ART-5 : Analytique et pilotage** : Chapitre définissant les règles pour la consolidation et l'analyse des données.

**ART-6 : Échange de données agrégées** : Chapitre définissant les règles pour l'échange de rapports périodiques et d'indicateurs.

**ART-7 : Sécurité et résidence** : Chapitre définissant les règles de sécurité et de localisation des données.

**ART-8 : Qualité et validation** : Chapitre définissant les règles pour le contrôle qualité des données.

**ART-9 : Déploiement et migration** : Chapitre définissant les règles pour la mise en production et la migration des systèmes.

**ART-10 : Supervision et monitoring** : Chapitre définissant les règles pour la surveillance du fonctionnement des systèmes.

**ART-11 : Coordination intersectorielle** : Chapitre définissant les règles pour les échanges avec d'autres secteurs de l'État.

## Termes de données

**Concept de données** : Unité atomique du dictionnaire, identifiant un objet d'information du système de santé. Chaque concept possède 7 attributs : nom, description, type, source, propriétaire, cycle de vie et référentiel source (mapping technique vers FHIR).

**Domaine de données** : Catégorie regroupant les concepts par affinité métier. Le dictionnaire ARTSN en définit 7 : Patient, Professions et acteurs, Structures et services, Produits de santé, Événements et actes, Géographie, Santé publique et pilotage.

**Référentiel source** : Champ technique d'un concept de données indiquant la ressource FHIR ou le standard technique correspondant (ex. : Patient FHIR R4, Organization FHIR R4).

**Niveau sémantique** : Niveau de description d'un concept de données indépendant de toute technologie, décrivant ce que le concept représente dans le monde réel (nom, description, type métier, propriétaire métier).

## Termes techniques

**API** : *Application Programming Interface*. Interface de programmation permettant à deux systèmes de communiquer entre eux.

**Endpoint** : Point d'accès d'une API, identifié par une URL, recevant des requêtes et retournant des réponses.

**Payload** : Données transportées par un message ou une requête API.

**Schema** : Schéma définissant la structure et les contraintes des données échangées (JSON Schema, XML Schema).

**Versioning** : Mécanisme de gestion des versions des API et des schémas pour assurer la compatibilité ascendante.

**Chiffrement** : Processus de transformation des données pour les rendre illisibles à toute personne non autorisée.

**Signature numérique** : Mécanisme cryptographique garantissant l'authenticité et l'intégrité d'un message ou d'un document.

**Journalisation** : Processus d'enregistrement des événements (accès, modifications, erreurs) pour la traçabilité et l'audit.

## Termes de sécurité

**Attribute-Based Access Control (ABAC)** : Modèle de contrôle d'accès basé sur les attributs, évaluant les permissions en fonction de caractéristiques de l'utilisateur, de la ressource, de l'action et de l'environnement.

**Zero-Trust** : Modèle de sécurité basé sur le principe "ne jamais faire confiance, toujours vérifier", où chaque accès est authentifié et autorisé, indépendamment de la localisation réseau.

**AES-256** : *Advanced Encryption Standard* avec clé de 256 bits, standard de chiffrement symétrique pour la protection des données au repos et en transit.

**TLS 1.2** : *Transport Layer Security* version 1.2, protocole de sécurisation des communications réseau garantissant la confidentialité et l'intégrité des données échangées.

**Mutual TLS (mTLS)** : Variante du TLS où les deux parties d'une communication s'authentifient mutuellement via des certificats numériques.

**OAuth2** : Protocole d'autorisation permettant à une application d'accéder à des ressources protégées au nom d'un utilisateur, sans partager ses identifiants.

**OpenID Connect (OIDC)** : Couche d'authentification au-dessus d'OAuth2, ajoutant la vérification de l'identité de l'utilisateur via un jeton d'identité.

**Public Key Infrastructure (PKI)** : Infrastructure à clés publiques, système de gestion des certificats numériques et des paires de clés pour le chiffrement et la signature numérique.

## Termes d'infrastructure et d'architecture

**ArchiMate** : Langage de modélisation d'architecture d'entreprise standardisé par l'Open Group, permettant de représenter les relations entre les composants organisationnels, applicatifs et technologiques.

**Extract, Transform, Load (ETL)** : Processus d'extraction de données depuis des sources multiples, de transformation selon les règles métier, et de chargement dans un entrepôt ou un lac de données.

**Lakehouse** : Architecture combinant les fonctionnalités des lacs de données (stockage flexible) et des entrepôts (structure et gouvernance), permettant le stockage et l'analyse de données à grande échelle.

**Graph Store** : Base de données spécialisée dans le stockage et l'interrogation de données en graphe (entités et relations), utilisée pour les cas d'usage nécessitant des requêtes relationnelles complexes.

**Grand Livre** : Registre centralisé assurant la réconciliation et la cohérence des données de référence entre les systèmes, agissant comme source de vérité pour les identifiants partagés.

**Pipeline ETL** : Chaîne de traitement automatisée orchestrant les étapes d'extraction, de transformation et de chargement des données.

**Fog Computing** : Architecture distribuée étendant le cloud computing vers le bord du réseau, plaçant le traitement et le stockage à proximité des sources de données pour réduire la latence.

**Edge Computing** : Architecture de traitement des données au plus près de leur source (bord du réseau), réduisant la latence et la bande passante pour les applications temps réel.

## Termes de patterns d'architecture

**Routeur d'escalade** : Composant dirigeant les alertes et les demandes vers le niveau de compétence ou d'autorité approprié selon la nature et la gravité de l'événement.

**Routeur d'alertes** : Composant distribuant les notifications aux destinataires appropriés selon des règles prédéfinies (canal, priorité, fréquence).

**Source de vérité** : Système ou référentiel désigné comme l'autorité unique pour un ensemble de données, garantissant l'unicité et la cohérence des informations.

**Atomicité logique** : Propriété garantissant qu'une opération est exécutée entièrement ou pas du tout, sans état intermédiaire visible.

**Persistance** : Capacité d'un système à conserver les données de manière durable après la fin du traitement ou la déconnexion.

**Compensation (transaction)** : Mécanisme annulant les effets d'une transaction précédente en cas d'échec, utilisé dans les systèmes distribués où les transactions classiques ne sont pas applicables.

**Cluster** : Groupe de serveurs ou de composants fonctionnant ensemble pour améliorer la disponibilité, la performance et la résilience du système.

**Topologie** : Organisation spatiale et logique des composants d'un système, décrivant leurs emplacements et leurs interconnexions.

**Irréversibilité** : Propriété d'une opération dont les effets ne peuvent pas être annulés, utilisée pour les transactions critiques (paiements, consentements).

**Masquage des identités** : Technique protégeant l'identité des utilisateurs dans les échanges de données, en remplaçant les identifiants réels par des identifiants anonymisés.

**Versionnage** : Mécanisme de gestion des versions des ressources et des API pour assurer la compatibilité ascendante et la traçabilité des changements.

**Données d'entraînement** : Ensemble de données utilisé pour entraîner les modèles d'intelligence artificielle ou d'apprentissage automatique.

**Audit des décisions automatisées** : Processus de vérification et de documentation des décisions prises par des systèmes automatisés, garantissant la transparence et la redevabilité.

**Requête de navigation relationnelle** : Interrogation de données en suivant les relations entre entités dans un graphe ou une base de données relationnelle.

**Cohérence topologique** : Propriété garantissant que la structure et les interconnexions des composants d'un système sont logiques et respectent les règles d'architecture définies.

**Résilience spatiale** : Capacité d'un système à maintenir ses services malgré des défaillances géographiques, grâce à la distribution et à la redondance.

**Fille d'attente** : Mécanisme de gestion des requêtes ou des tâches en attente de traitement, assurant l'ordre et la priorisation.

**Durabilité** : Capacité d'un système ou d'une initiative à continuer de fonctionner et de produire de la valeur après la fin du financement initial.

**Éradication des silos** : Démarche visant à supprimer les barrières entre les systèmes d'information pour faciliter le partage et l'utilisation cohérente des données.

**Compatibilité ascendante/descendante** : Capacité d'un système à interagir avec des versions plus récentes (ascendante) ou plus anciennes (descendante) d'un standard ou d'une API.

**Normalisation sémantique** : Processus d'harmonisation des significations des données échangées pour garantir que tous les systèmes interprètent de la même façon les informations partagées.

**Enrichissement** : Processus d'ajout d'informations complémentaires à des données existantes pour améliorer leur qualité, leur précision ou leur utilité.

**Bordure de la plateforme** : Zone de transition entre l'infrastructure interne et les systèmes externes, gérant les échanges sécurisés avec l'extérieur.

## Liens

L'Index de l'ARTSN fournit la page d'accueil de l'architecture. La Matrice de lecture de l'ARTSN propose une vue croisée parties et lecteurs. Les Acronymes de l'ARTSN listent l'ensemble des acronymes. L'Annexe B : Glossaire des patterns détaille les définitions des patterns mobilisés. Le Glossaire du CAESN (niveau 1) couvre les termes transverses de l'architecture.

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **Annexe B : Glossaire des patterns** : Annexe B : Glossaire des patterns cités (`02_artsn/08_annexes/b-glossaire-patterns.md`)
- **glossaire du CAESN** : Glossaire (`00_caesn/10_annexes/glossary.md`)
- **table de maturité** : Annexe A : Table de maturité par chapitre (`02_artsn/08_annexes/a-table-de-maturite.md`)
- **homologation** : Glossaire (`00_caesn/10_annexes/glossary.md`)
- **cartographie cible** : Cartographie conceptuelle cible (`02_artsn/05_cartographie/index.md`)
- **résidence de la donnée** : Sécurité, contrôle d'accès et résidence de la donnée (`referentiel/chapitres/art-7.md`)
- **niveau 1** : Normes et standards d'architecture (`01_cnisn/05_standards/index.md`)
- **Annexe B** : Annexe B : Glossaire des patterns cités (`02_artsn/08_annexes/b-glossaire-patterns.md`)
- **Index de l'ARTSN** : Architecture de Référence Technique de la Santé Numérique (ARTSN) (`02_artsn/index.md`)
- **Matrice de lecture de l'ARTSN** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **Acronymes de l'ARTSN** : Acronymes et abréviations de l'ARTSN (niveau 3) (`02_artsn/acronyms.md`)
- **Glossaire du CAESN (niveau 1)** : Glossaire (`00_caesn/10_annexes/glossary.md`)
