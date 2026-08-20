---

title: Glossaire du PTISN (niveau 4)
id: ptisn-glossary
domain: 03_ptisn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: Équipes techniques des initiatives
tags: ["ptisn", "glossaire", "terminologie", "niveau-4"]
---

# Glossaire du PTISN (niveau 4)

## Pour qui lire ce document

**Niveau :** niveau 4 : Profils techniques d'implémentation de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

Ce glossaire recense les termes propres au périmètre d'implémentation du niveau 4, qui décline le niveau 3 au niveau de chaque initiative. Les termes transverses et les patterns techniques sont définis respectivement dans le glossaire du CAESN et le glossaire de l'ARTSN.

## Termes de profils d'initiative

Le **contrat d'interface** désigne la spécification technique d'un échange (API, fichier, flux) défini par l'initiative : format, schéma, version du standard, authentification, invariants de sécurité. Il décline, pour l'initiative, le contrat d'interface du niveau 3.

La **fiche d'initiative** est le document d'alignement valeur d'une initiative (alignement sur les flux de valeur, capabilités et principes), qui encadre la rédaction du profil technique. Voir la fiche d'initiative.

Le **profil technique d'implémentation** est le document du niveau 4 déclinant, pour une initiative donnée, l'ARTSN au niveau propre de la solution : configurations, API, contrats d'interfaces, scénarios de déploiement et de test.

Le **scénario de test et d'homologation** est la séquence de validation (données, étapes, critères d'acceptation) démontrant qu'une configuration de l'initiative respecte les standards du niveau 3 et les critères d'homologation du niveau 1.

La **spécification d'API** est la description formelle des ressources, méthodes, paramètres et réponses d'une API, versionnée et opposable, servant de base aux tests et à la documentation d'intégration.

## Termes de profils techniques (PT)

Le **PT-01 : Échange interinstitutionnel** est le profil technique national pour les échanges entre le secteur santé et les autres secteurs de l'État (état civil, protection sociale, finances publiques). Il est basé sur X-Road.

Le **PT-04 : Résolution d'identité** est le profil technique national pour la résolution d'identité du bénéficiaire, comprenant la recherche démographique, la gestion des identifiants et le rapprochement de dossiers. Il est basé sur IHE PIXm/PDQm.

Le **PT-08 : Données agrégées** est le profil technique national pour l'échange de données agrégées de santé publique (rapports périodiques, indicateurs). Il est basé sur IHE mADX.

Le **PT-02 : Consentement** est le profil technique national pour la gestion du consentement du patient pour le partage de ses données de santé.

Le **PT-03 : Terminologie** est le profil technique national pour la gestion des terminologies et des codifications (CIM-10, SNOMED CT, LOINC, ATC).

Le **PT-05 : Géolocalisation** est le profil technique national pour la localisation géographique des formations sanitaires et des points de service.

Le **PT-06 : Authentification** est le profil technique national pour l'authentification et l'autorisation des professionnels de santé.

Le **PT-07 : Traçabilité** est le profil technique national pour la journalisation des accès et des modifications des données.

Le **PT-09 : Alertes** est le profil technique national pour la détection et la réponse aux alertes sanitaires.

Le **PT-10 : Qualité des données** est le profil technique national pour le contrôle qualité des données échangées.

Le **PT-11 : Consentement (détaillé)** est le profil technique national pour la gestion fine du consentement patient, incluant les finalités, les destinataires et les durées.

Le **PT-12 : Déploiement** est le profil technique national pour la mise en production et la migration des systèmes.

Le **PT-13 : Supervision** est le profil technique national pour la surveillance du fonctionnement des systèmes.

Le **PT-14 : Interopérabilité transfrontalière** est le profil technique national pour les échanges cliniques avec les pays voisins. Il est basé sur HL7 FHIR IPS (International Patient Summary) et le réseau GDHCN (Global Digital Health Certificate Network). Trois interfaces sont définies : export IPS, vérification certificat, consultation distante.

Le **PT-15 : Surveillance One Health** est le profil technique national pour la surveillance intégrée des zoonoses et menaces sanitaires transversales. Il intègre les données humain, animal et environnement via le standard OHDSI FHIR.

## Termes de sécurité et d'autorisation

Le **RBAC** (*Role-Based Access Control*) est le modèle de contrôle d'accès basé sur les rôles. Le PT-10 définit 13 rôles (R-AS, R-MED, R-PH, R-ENC, R-CDIR, R-DDIST, R-DREG, R-PROG, R-INS, R-DMIN, R-API, R-MINS, R-INTER) organisés en 3 niveaux hiérarchiques.

La **politique d'autorisation (POL)** est la règle détaillée définissant les permissions d'un rôle sur une ressource donnée. Dix politiques sont définies (POL-01 à POL-10) couvrant : lecture, écriture, partage, consentement, administration, audit, etc.

Le **niveau de service (SLA)** est l'engagement de performance pour un profil technique. Trois niveaux sont définis : critique (99,95 % disponibilité, < 2s), important (99,9 %, < 5s), standard (99,5 %, < 10s). Chaque profil a ses propres seuils.

La **certification d'interopérabilité** est le label délivré après validation des tests N1 à N3, attestant qu'un système respecte les profils PTISN. Trois niveaux existent : Silver (conformité), Gold (composabilité), Platinum (bout-en-bout + charge).

## Termes d'initiative

Une **initiative** est un projet ou programme numérique contribuant à l'exécution des flux de valeur du CAESN et au développement des capabilités du CNISN.

Une **capacité CNISN** est la capacité d'interopérabilité du CNISN à laquelle l'initiative contribue (ex. : CAP-INT-01, CAP-INT-03).

Un **chapitre ART** est le pattern architectural de l'ARTSN appliqué par l'initiative (ex. : ART-0, ART-1, ART-7).

Un **composant technique** est un élément d'infrastructure ou de logiciel utilisé par l'initiative (ex. : serveur X-Road, base de données, application mobile).

Un **indicateur de bénéfice** est la métrique mesurant la contribution de l'initiative aux résultats attendus (ex. : taux d'observance, temps de remontée des données).

Un **risque** est un événement potentiellement défavorable pouvant affecter le succès de l'initiative, avec un impact et une probabilité identifiés.

## Termes de conformité

La **conformité obligatoire** est l'exigence dont le non-respect empêche l'homologation et le déploiement de l'initiative.

La **conformité recommandée** est l'exigence fortement encouragée mais dont le non-respect peut être justifié par des contraintes spécifiques.

La **dérogation** est l'autorisation exceptionnelle de ne pas respecter une exigence de conformité, soumise à justification et à validation.

Le **scénario de test** est la séquence de validation décrivant les données d'entrée, les étapes et les critères d'acceptation pour vérifier la conformité de l'initiative.

Le **jeu de données de test** est l'ensemble de données simulées utilisées pour valider le fonctionnement et la conformité de l'initiative.

## Termes techniques

Une **API** (*Application Programming Interface*) est une interface de programmation permettant à deux systèmes de communiquer entre eux.

Une **API REST** (*Representational State Transfer Application Programming Interface*) est un style d'architecture pour les interfaces web utilisant les méthodes HTTP (GET, POST, PUT, DELETE).

Un **endpoint** est le point d'accès d'une API, identifié par une URL, recevant des requêtes et retournant des réponses.

Un **payload** est l'ensemble des données transportées par un message ou une requête API.

Un **schéma** (*schema*) est la structure et les contraintes des données échangées (JSON Schema, XML Schema).

Le **versioning** est le mécanisme de gestion des versions des API et des schémas pour assurer la compatibilité ascendante.

Le **chiffrement** est le processus de transformation des données pour les rendre illisibles à toute personne non autorisée.

La **signature numérique** est le mécanisme cryptographique garantissant l'authenticité et l'intégrité d'un message ou d'un document.

La **journalisation** est le processus d'enregistrement des événements (accès, modifications, erreurs) pour la traçabilité et l'audit.

Le **mode hors-ligne** est la capacité d'un système à fonctionner sans connexion réseau, en stockant les données localement et en les synchronisant lorsque la connexion est rétablie.

La **synchronisation différée** est le mécanisme de transmission des données collectées en mode hors-ligne lors de la prochaine connexion disponible.

**X-Road** est la plateforme d'échange de données sécurisé entre organisations membres, utilisant des serveurs de sécurité et une infrastructure de confiance commune.

**IHE** (*Integrating the Healthcare Enterprise*) est l'organisation internationale développant des profils d'intégration pour améliorer l'interopérabilité des systèmes de santé.

**HL7 FHIR** (*Fast Healthcare Interoperability Resources*) est le standard moderne pour l'échange de données de santé, basé sur des ressources modulaires et une API REST.

**mADX** (*Mobile Aggregate Data Exchange*) est le profil IHE pour l'échange de données agrégées de santé publique, basé sur FHIR.

**PIXm** (*Patient Identifier Cross-referencing for mobile*) est le profil IHE pour la gestion et la recherche des identifiants patients entre domaines via une API REST.

**PDQm** (*Patient Demographics Query for mobile*) est le profil IHE pour la recherche de patients à partir de données démographiques via une API REST.

## Liens

- Index du PTISN
- Matrice de lecture du PTISN
- Glossaire du CAESN (niveau 1)
- Glossaire de l'ARTSN (niveau 3)
- Exemples de profils d'initiative

## Références

- **matrice de lecture** : Matrice de lecture du PTISN (niveau 4) (`03_ptisn/reading-matrix.md`)
- **glossaire du CAESN** : Glossaire (`00_caesn/10_annexes/glossary.md`)
- **glossaire de l'ARTSN** : Glossaire de l'ARTSN (niveau 3) (`02_artsn/glossary.md`)
- **contrat d'interface** : Glossaire de l'ARTSN (niveau 3) (`02_artsn/glossary.md`)
- **fiche d'initiative** : Fiche standard d'initiative orientée valeur (`00_caesn/06_portfolio/initiative-card.md`)
- **critères d'homologation** : Cycle de vie applicatif et critères d'homologation (`00_caesn/05_application/lifecycle.md`)
- **Index du PTISN** : Profils techniques d'implémentation de la Santé Numérique (PTISN) (`03_ptisn/index.md`)
- **Matrice de lecture du PTISN** : Matrice de lecture du PTISN (niveau 4) (`03_ptisn/reading-matrix.md`)
- **Glossaire du CAESN (niveau 1)** : Glossaire (`00_caesn/10_annexes/glossary.md`)
- **Glossaire de l'ARTSN (niveau 3)** : Glossaire de l'ARTSN (niveau 3) (`02_artsn/glossary.md`)
- **Exemples de profils d'initiative** : Exemples de profils d'initiative remplis (`03_ptisn/05_exemples/index.md`)
