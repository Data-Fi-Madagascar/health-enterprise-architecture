# Plan d'amendement des feedbacks de validation technique

> **Référence** : HEA-PLAN-AMEN-001
> **Date** : 30 août 2026
> **Version** : 1.0
> **Objet** : Plan directeur pour le traitement des 356 observations issues de la validation technique du CAESN et du CNISN
> **Sources** : analyse-feedbacks-caesn.md, analyse-feedbacks-cnisn.md, consolidation-feedbacks-validation-technique.md
> **Statut** : Projet de plan - à valider avant exécution

## 1. Contexte et objectif

L'atelier de validation technique HEA a produit 356 observations réparties entre le CAESN (208) et le CNISN (136). Ces observations, issues de quatre groupes d'experts (G1, G2, G3, G4), couvrent des domaines variés allant de la rédaction à la gouvernance, en passant par les références stratégiques et les indicateurs.

Le présent plan définit la stratégie de traitement de ces observations. Il ne s'agit pas simplement de corriger des fautes : il s'agit de transformer un ensemble brut de feedbacks en un **plan d'action exécutable** qui permettra aux deux documents d'atteindre le statut de documents de référence nationale fiables, cohérents et opérationnels.

L'objectif final est d'assurer que chaque observation est traitée, classée et priorisée de manière à ce que les corrections à impact maximal soient réalisées en premier, tout en garantissant la traçabilité complète du processus.

## 2. Principes directeurs

Avant de détailler les phases, il convient de définir les principes qui guideront l'ensemble du processus d'amendement.

**Priorité à la cohérence stratégique.** Les références obsolètes (PDSS 2020-2024, CIM-10) et les incohérences factuelles (CNASN vs CAESN, "malagasy" vs "malagasy") constituent des blocages fondamentaux. Un document qui référence un plan périmé ou utilise des termes erronés perd immédiatement sa crédibilité aux yeux des décideurs et des partenaires techniques et financiers. Ces corrections doivent donc précéder toute autre intervention.

**Complétude du lexique technique.** L'absence de glossaire est identifiée par trois groupes comme un obstacle majeur à l'adoption. Le CAESN et le CNISN utilisent un vocabulaire technique dense (FOSA, DEPSI, CAP-13, architecture runway, steward de données, HL7 FHIR, X-Road) sans toujours en fournir la définition. La rédaction d'un glossaire complet est une condition préalable à la compréhension du document par des parties prenantes non techniques.

**Opérationnalisation de la gouvernance.** La matrice RACI, la clarification des rôles et la définition des instances de gouvernance sont des prérequis pour que les documents puissent effectivement être appliqués. Sans gouvernance claire, le CAESN et le CNISN resteront des documents de principes sans mécanisme d'application.

**Traçabilité des décisions.** Chaque observation doit être tracée de son identification à sa résolution. Cette traçabilité est essentielle pour la crédibilité du processus : elle permet de démontrer que chaque feedback a été pris en compte, et de justifier les arbitrages réalisés.

## 3. Phases d'amendement

### Phase 1 : Corrections immédiates (Semaine 1)

Cette phase vise à corriger les incohérences factuelles et les erreurs identifiées par plusieurs groupes. Ces corrections sont simples à réaliser mais critiques pour la crédibilité du document.

**CAESN :**
- Mise à jour du PDSS 2020-2024 vers le PDSS 2026-2030 (7 Orientations stratégiques) - validé par 4 groupes
- Insertion de la PNS 2025-2030 dans les références stratégiques - identifié par G3
- Correction de "malagasy" en "malagasy" ou reformulation - identifié par G1, G3
- Mise à jour du nom du Ministère vers la dénomination officielle actuelle - identifié par G1
- Correction de "l'État numérique malgache" en "système numérique malagasy" - identifié par G3

**CNISN :**
- Remplacement de CIM-10 par CIM-11 - validé par 3 groupes (G1, G3, G4)
- Remplacement de "through" par "à travers" (3 occurrences) - identifié par G1, G2, G3
- Correction de "CNASN" en "CAESN" dans la section interopérabilité organisationnelle - identifié par G1, G3
- Retrait de "Malagasy" - identifié par G1
- Insertion de la gestion de version - identifié par G1, G2

**Livrables :**
- Fichiers CAESN et CNISN mis à jour avec les corrections
- Tableau de traçabilité des corrections réalisées

### Phase 2 : Rédaction du glossaire (Semaines 2-3)

Cette phase consiste à rédiger un glossaire complet pour chaque document, couvrant l'ensemble des termes techniques utilisés.

**CAESN :**
- Définition de "capabilité" (harmoniser corps vs glossaire)
- Définition de "architecture runway" (proposition G2 : "socle d'architecture prioritaire")
- Définition de "steward de données"
- Définition de "FOSA" (Formation Sanitaire)
- Définition de "DEPSI"
- Liste complète des acronymes et sigles

**CNISN :**
- Définition de "capabilité"
- Définition des termes techniques (HL7 FHIR, X-Road, mADX, ATNA)
- Définition de "source faisant autorité" (remplacement de "authoritative")
- Définition de "copies locales sans valeur de référence"
- Liste complète des acronymes et sigles

**Livrables :**
- Glossaire CAESN complet
- Glossaire CNISN complet
- Liste d'acronymes pour chaque document

### Phase 3 : Décision sur les annexes (Semaine 4)

Cette phase nécessite une décision formelle sur le sort des annexes référencées mais inexistantes.

**Questions à arbitrer :**
- Faut-il créer les annexes B-G du CNISN ou retirer les références ?
- Quel contenu pour les annexes E-J du CAESN ?
- Quelle priorité pour la création des annexes ?

**Recommandation :**
- Créer les annexes une par une en commençant par l'Annexe G (matrice d'interopérabilité) pour le CNISN
- Pour le CAESN, compléter les annexes E-J avec le contenu minimum nécessaire (matrices de correspondance, modèles de fiche, grilles de priorisation)

**Livrables :**
- Décision arbitrale sur les annexes
- Plan de création des annexes avec calendrier

### Phase 4 : Harmonisation terminologique (Semaines 5-6)

Cette phase consiste à harmoniser l'ensemble du vocabulaire utilisé dans les deux documents.

**Travaux :**
- Remplacement de "value streams" par "chaîne de valeur" - identifié par G3
- Harmonisation de "ART-SN" en "ARTSN" - identifié par G3
- Correction des fautes de frappe ("lla date", "es sources") - identifié par G1
- Harmonisation des sigles ministères (MSANP, MIASA/MinEL, MEF) - identifié par G1, G3
- Traduction de "Architecture Decision Records" en "Registre des Décisions" - identifié par G3
- Traduction de "ATNA" en "Traçabilité des accès et authentification des systèmes" - identifié par G3

**Livrables :**
- CAESN harmonisé terminologiquement
- CNISN harmonisé terminologiquement
- Tableau de correspondance ancien/nouveau terme

### Phase 5 : Élargissement de la portée (Semaine 7)

Cette phase vise à clarifier et élargir la portée des deux documents.

**CAESN :**
- Clarification de la portée : "secteur santé à Madagascar" (pas uniquement MSANP)
- Transformation du titre "Ce que ce cadre n'est pas" en paragraphe narratif
- Remplacement de "acteurs régionaux et districts sanitaires" par "acteurs locaux"
- Clarification de la cumulative des 9 critères

**CNISN :**
- Élargissement de la portée : "systèmes d'information sanitaire" (pas uniquement MSANP)
- Insertion d'une clause de proportionnalité pour la décentralisation
- Précision des catégories de partenaires privés autorisés
- Clarification de l'obligation d'application

**Livrables :**
- CAESN avec portée clarifiée
- CNISN avec portée élargie

### Phase 6 : Structure de gouvernance (Semaines 8-10)

Cette phase est la plus critique : elle consiste à établir la structure de gouvernance permettant l'application des documents.

**Travaux :**
- Production de la matrice RACI de gouvernance des données - identifié par G1, G2, G3
- Définition des responsabilités des acteurs - identifié par G1, G2, G3
- Complétion de la composition du Comité National d'Architecture - identifié par G3
- Définition du Bureau de Réalisation de la Valeur - identifié par G1
- Mise en place du registre ADR - identifié par G1, G2
- Création de la matrice des pouvoirs de décision - identifié par G1, G2
- Établissement de la procédure de nomination des propriétaires - identifié par G1

**Livrables :**
- Matrice RACI complète
- Description des rôles et responsabilités
- Modèle de registre ADR
- Matrice des pouvoirs de décision

### Phase 7 : Flux de valeur et indicateurs (Semaines 11-12)

Cette phase consiste à ajuster les flux de valeur et les indicateurs pour les rendre opérationnels.

**CAESN :**
- Ajustement des indicateurs de VS-01, VS-02, VS-03, VS-04
- Création de l'étape 8 pour VS-03 ("Ajustement des mécanismes")
- Standardisation de la chaîne de valeur des initiatives
- Instauration du scoring d'évaluation (0-4)
- Ajout de la colonne "Niveau de criticité" aux tableaux de ruptures

**CNISN :**
- Ajustement des indicateurs de gouvernance
- Ajout des baseline, cibles et responsables
- Création de la fiche KPI standard
- Ajout des indicateurs de résilience

**Livrables :**
- Flux de valeur CAESN ajustés
- Indicateurs CAESN et CNISN complets
- Modèle de scoring d'évaluation

### Phase 8 : Intégration des exigences techniques (Semaines 13-14)

Cette phase concerne principalement le CNISN et porte sur l'intégration des exigences techniques.

**Travaux :**
- Détail des règles d'utilisation FHIR, X-Road, mADX - identifié par G4
- Modèle de contrat et registre - identifié par G4
- Exigences minimales de sécurité - identifié par G4
- Critères d'acceptation des tests - identifié par G4
- Classification des preuves (obligatoire, conditionnelle, complémentaire) - identifié par G2
- Hiérarchie de vérification des preuves - identifié par G2

**Livrables :**
- Section standards techniques complétée
- Modèle de contrat
- Exigences de sécurité
- Grille de classification des preuves

### Phase 9 : Priorisation et finalités (Semaine 15)

Cette phase consiste à prioriser les finalités et les principes pour l'opérationnalisation.

**Travaux :**
- Identification des finalités prioritaires phase 1 - identifié par G2
- Priorisation des principes P-INT (obligatoires vs progressifs) - identifié par G2
- Tableau récapitulatif des principes et catégories - identifié par G2
- Ajout de la pérennité comme caractéristique de l'information - identifié par G2

**Livrables :**
- Liste des finalités prioritaires
- Tableau de priorisation des principes
- Principes classés par niveau d'obligation

### Phase 10 : Relecture et validation finale (Semaines 16-17)

Cette phase finale consiste à relire l'ensemble des documents pour garantir la cohérence et la qualité.

**Travaux :**
- Relecture complète du CAESN
- Relecture complète du CNISN
- Vérification de la cohérence entre les deux documents
- Validation de la conformité aux standards Gartner
- Mise à jour de la table des matières
- Vérification de tous les liens internes

**Livrables :**
- CAESN version finale
- CNISN version finale
- Rapport de cohérence

## 4. Gouvernance du processus

**Instance de pilotage :** Comité National d'Architecture Santé Numérique

**Fréquence :** Hebdomadaire pendant 17 semaines

**Arbitrages nécessaires :**
- Décision sur les annexes B-G (Phase 3)
- Statut du document (draft vs cadre de référence)
- Portée du cadre (MSANP vs secteur santé)
- Rôle de l'État comme financeur

**Indicateurs de suivi :**
- Nombre d'observations traitées par phase
- Taux de convergence des décisions
- Respect du calendrier

## 5. Risques et mitigations

**Risque 1 : Volume de travail sous-estimé.**
Les 356 observations représentent un volume significatif. Mitigation : prioriser les observations convergentes (35%) et déléguer les observations isolées.

**Risque 2 : Arbitrages retardés.**
Les décisions sur les annexes et la portée peuvent retarder le processus. Mitigation : organiser une session d'arbitrage dédiée en Phase 3.

**Risque 3 : Incohérence entre documents.**
Le CAESN et le CNISN étant traités séparément, des incohérences peuvent apparaître. Mitigation : phase de relecture croisée en Phase 10.

**Risque 4 : Résistance au changement.**
Les auteurs originaux peuvent être réticents à modifier leur travail. Mitigation : impliquer les auteurs dans le processus d'amendement et valoriser leur contribution initiale.

## 6. Calendrier prévisionnel

| Phase | Description | Durée | Dates cibles |
|-------|-------------|-------|--------------|
| 1 | Corrections immédiates | 1 semaine | Semaine 1 |
| 2 | Rédaction du glossaire | 2 semaines | Semaines 2-3 |
| 3 | Décision sur les annexes | 1 semaine | Semaine 4 |
| 4 | Harmonisation terminologique | 2 semaines | Semaines 5-6 |
| 5 | Élargissement de la portée | 1 semaine | Semaine 7 |
| 6 | Structure de gouvernance | 3 semaines | Semaines 8-10 |
| 7 | Flux de valeur et indicateurs | 2 semaines | Semaines 11-12 |
| 8 | Intégration des exigences techniques | 2 semaines | Semaines 13-14 |
| 9 | Priorisation et finalités | 1 semaine | Semaine 15 |
| 10 | Relecture et validation finale | 2 semaines | Semaines 16-17 |
| **Total** | | **17 semaines** | **4 mois** |

## 7. Recommandations finales

Ce plan d'amendement constitue un cadre de travail structuré pour traiter les 356 observations issues de la validation technique. Il est conçu pour être à la fois complet et adaptable : chaque phase peut être ajustée en fonction des arbitrages réalisés et des contraintes de calendrier.

La clé du succès réside dans la discipline de suivi : chaque observation doit être tracée de son identification à sa résolution, et chaque phase doit être validée avant de passer à la suivante. Cette rigueur est essentielle pour que le CAESN et le CNISN atteignent le statut de documents de référence nationale fiables et opérationnels.

Le présent document est soumis à validation avant lancement des travaux.


*Plan d'amendement des feedbacks - HEA-PLAN-AMEN-001 - Version 1.0 - 30 août 2026*
