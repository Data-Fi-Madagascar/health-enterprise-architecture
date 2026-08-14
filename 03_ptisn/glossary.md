---
title: Glossaire du PTISN (niveau 4)
id: ptisn-glossary
domain: 03_ptisn
version: "0.1.0"
status: draft
last_reviewed: 2026-08-13
owner: Équipes techniques des initiatives
tags: [ptisn, glossaire, terminologie, niveau-4]
---

# Glossaire du PTISN (niveau 4)

## Pour qui lire ce document

**Niveau :** niveau 4 — Profils techniques d'implémentation de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](./reading-matrix.md).

Termes propres au périmètre d'implémentation du niveau 4, qui décline le niveau 3 au niveau de chaque initiative. Les termes transverses et les patterns techniques sont définis respectivement dans le [glossaire du CAESN](../00_caesn/10_annexes/glossary.md) et le [glossaire de l'ARTSN](../02_artsn/glossary.md).

## Termes de profils d'initiative

**Contrat d'interface** — Spécification technique d'un échange (API, fichier, flux) défini par l'initiative : format, schéma, version du standard, authentification, invariants de sécurité. Il décline, pour l'initiative, le [contrat d'interface](../02_artsn/glossary.md) du niveau 3.

**Fiche d'initiative** — Document d'alignement valeur d'une initiative (alignement sur les flux de valeur, capabilités et principes), qui encadre la rédaction du profil technique. Voir la [fiche d'initiative](../00_caesn/06_portfolio/initiative-card.md).

**Profil technique d'implémentation** — Document du niveau 4 déclinant, pour une initiative donnée, l'ARTSN au niveau propre de la solution : configurations, API, contrats d'interfaces, scénarios de déploiement et de test.

**Scénario de test et d'homologation** — Séquence de validation (données, étapes, critères d'acceptation) démontrant qu'une configuration de l'initiative respecte les standards du niveau 3 et les [critères d'homologation](../00_caesn/05_application/lifecycle.md) du niveau 1.

**Spécification d'API** — Description formelle des ressources, méthodes, paramètres et réponses d'une API, versionnée et opposable, servant de base aux tests et à la documentation d'intégration.

## Termes de profils techniques (PT)

**PT-01 — Échange interinstitutionnel** — Profil technique national pour les échanges entre le secteur santé et les autres secteurs de l'État (état civil, protection sociale, finances publiques). Basé sur X-Road.

**PT-04 — Résolution d'identité** — Profil technique national pour la résolution d'identité du bénéficiaire, comprenant la recherche démographique, la gestion des identifiants et le rapprochement de dossiers. Basé sur IHE PIXm/PDQm.

**PT-08 — Données agrégées** — Profil technique national pour l'échange de données agrégées de santé publique (rapports périodiques, indicateurs). Basé sur IHE mADX.

**PT-02 — Consentement** — Profil technique national pour la gestion du consentement du patient pour le partage de ses données de santé.

**PT-03 — Terminologie** — Profil technique national pour la gestion des terminologies et des codifications (CIM-10, SNOMED CT, LOINC, ATC).

**PT-05 — Géolocalisation** — Profil technique national pour la localisation géographique des formations sanitaires et des points de service.

**PT-06 — Authentification** — Profil technique national pour l'authentification et l'autorisation des professionnels de santé.

**PT-07 — Traçabilité** — Profil technique national pour la journalisation des accès et des modifications des données.

**PT-09 — Alertes** — Profil technique national pour la détection et la réponse aux alertes sanitaires.

**PT-10 — Qualité des données** — Profil technique national pour le contrôle qualité des données échangées.

**PT-11 — Consentement (détaillé)** — Profil technique national pour la gestion fine du consentement patient, incluant les finalités, les destinataires et les durées.

**PT-12 — Déploiement** — Profil technique national pour la mise en production et la migration des systèmes.

**PT-13 — Supervision** — Profil technique national pour la surveillance du fonctionnement des systèmes.

**PT-14 — Interopérabilité transfrontalière** — Profil technique national pour les échanges cliniques avec les pays voisins. Basé sur HL7 FHIR IPS (International Patient Summary) et le réseau GDHCN (Global Digital Health Certificate Network). Trois interfaces : export IPS, vérification certificat, consultation distante.

**PT-15 — Surveillance One Health** — Profil technique national pour la surveillance intégrée des zoonoses et menaces sanitaires transversales. Intègre les données humain, animal et environnement via le standard OHDSI FHIR.

## Termes de sécurité et d'autorisation

**RBAC** — *Role-Based Access Control*. Modèle de contrôle d'accès basé sur les rôles. Le PT-10 définit 13 rôles (R-AS, R-MED, R-PH, R-ENC, R-CDIR, R-DDIST, R-DREG, R-PROG, R-INS, R-DMIN, R-API, R-MINS, R-INTER) organisés en 3 niveaux hiérarchiques.

**Politique d'autorisation (POL)** — Règle détaillée définissant les permissions d'un rôle sur une ressource donnée. 10 politiques定义ies (POL-01 à POL-01) couvrant : lecture, écriture, partage, consentement, administration, audit, etc.

**Niveau de service (SLA)** — Engagement de performance pour un profil technique. Trois niveaux : critique (99,95 % disponibilité, < 2s), important (99,9 %, < 5s), standard (99,5 %, < 10s). Chaque profil a ses propres seuils.

**Certification d'interopérabilité** — Label délivré après validation des tests N1 à N3, attestant qu'un système respecte les profils PTISN. Trois niveaux : Silver (conformité), Gold (composabilité), Platinum (bout-en-bout + charge).

## Termes d'initiative

**Initiative** — Projet ou programme numérique contribuant à l'exécution des flux de valeur du CAESN et au développement des capabilités du CNISN.

**Capacité CNISN** — Capacité d'interopérabilité du CNISN à laquelle l'initiative contribue (ex. : CAP-INT-01, CAP-INT-03).

**Chapitre ART** — Pattern architectural de l'ARTSN appliqué par l'initiative (ex. : ART-0, ART-1, ART-7).

**Composant technique** — Élément d'infrastructure ou de logiciel utilisé par l'initiative (ex. : serveur X-Road, base de données, application mobile).

**Indicateur de bénéfice** — Métrique mesurant la contribution de l'initiative aux résultats attendus (ex. : taux d'observance, temps de remontée des données).

**Risque** — Événement potentiellement défavorable pouvant affecter le succès de l'initiative, avec un impact et une probabilité identifiés.

## Termes de conformité

**Conformité obligatoire** — Exigence dont le non-respect empêche l'homologation et le déploiement de l'initiative.

**Conformité recommandée** — Exigence fortement encouragée mais dont le non-respect peut être justifié par des contraintes spécifiques.

**Dérogation** — Autorisation exceptionnelle de ne pas respecter une exigence de conformité, soumise à justification et à validation.

**Scénario de test** — Séquence de validation décrivant les données d'entrée, les étapes et les critères d'acceptation pour vérifier la conformité de l'initiative.

**Jeu de données de test** — Ensemble de données simulées utilisées pour valider le fonctionnement et la conformité de l'initiative.

## Termes techniques

**API** — *Application Programming Interface*. Interface de programmation permettant à deux systèmes de communiquer entre eux.

**API REST** — *Representational State Transfer Application Programming Interface*. Style d'architecture pour les interfaces web utilisant les méthodes HTTP (GET, POST, PUT, DELETE).

**Endpoint** — Point d'accès d'une API, identifié par une URL, recevant des requêtes et retournant des réponses.

**Payload** — Données transportées par un message ou une requête API.

**Schema** — Schéma définissant la structure et les contraintes des données échangées (JSON Schema, XML Schema).

**Versioning** — Mécanisme de gestion des versions des API et des schémas pour assurer la compatibilité ascendante.

**Chiffrement** — Processus de transformation des données pour les rendre illisibles à toute personne non autorisée.

**Signature numérique** — Mécanisme cryptographique garantissant l'authenticité et l'intégrité d'un message ou d'un document.

**Journalisation** — Processus d'enregistrement des événements (accès, modifications, erreurs) pour la traçabilité et l'audit.

**Mode hors-ligne** — Capabilité d'un système à fonctionner sans connexion réseau, en stockant les données localement et en les synchronisant lorsque la connexion est rétablie.

**Synchronisation différée** — Mécanisme de transmission des données collectées en mode hors-ligne lors de la prochaine connexion disponible.

**X-Road** — Plateforme d'échange de données sécurisé entre organisations membres, utilisant des serveurs de sécurité et une infrastructure de confiance commune.

**IHE** — *Integrating the Healthcare Enterprise*. Organisation internationale développant des profils d'intégration pour améliorer l'interopérabilité des systèmes de santé.

**HL7 FHIR** — *Fast Healthcare Interoperability Resources*. Standard moderne pour l'échange de données de santé, basé sur des ressources modulaires et une API REST.

**mADX** — *Mobile Aggregate Data Exchange*. Profil IHE pour l'échange de données agrégées de santé publique, basé sur FHIR.

**PIXm** — *Patient Identifier Cross-referencing for mobile*. Profil IHE pour la gestion et la recherche des identifiants patients entre domaines via une API REST.

**PDQm** — *Patient Demographics Query for mobile*. Profil IHE pour la recherche de patients à partir de données démographiques via une API REST.

## Liens

- [Index du PTISN](./index.md)
- [Matrice de lecture du PTISN](./reading-matrix.md)
- [Glossaire du CAESN (niveau 1)](../00_caesn/10_annexes/glossary.md)
- [Glossaire de l'ARTSN (niveau 3)](../02_artsn/glossary.md)
- [Exemples de profils d'initiative](./05_exemples/index.md)
