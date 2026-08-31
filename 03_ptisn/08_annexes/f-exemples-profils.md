---

title: Exemples de profils d'initiative remplis
id: ptisn-exemples
domain: 08_annexes
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: ["ptisn", "exemples", "profils", "niveau-4"]
---

# Exemples de profils d'initiative remplis

## Pour qui lire ce document

**Niveau :** niveau 4 : Profils techniques d'implémentation de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

Ce document présente trois exemples concrets de profils d'initiative remplis selon le template standard du PTISN. Chaque exemple illustre la manière dont un projet réel est décrit, rattaché aux capacités, aux chapitres ART et aux composants du référentiel. Il s'agit de guides pratiques destinés aux équipes techniques chargées de rédiger les profils de leurs propres initiatives.

## Structure du template

Chaque profil suit une structure standardisée composée de dix rubriques. L'identification initiale renseigne le code de l'initiative, son titre, son type, sa portée et son statut. Le rattachement aux capacités CNISN et aux chapitres ART applicables permet de situer l'initiative dans le cadre national d'interopérabilité. La description de l'initiative précise son objectif, son contexte et ses parties prenantes. Les profils PTISN applicables identifient les patterns techniques requis. Les contrats d'interface spécifient les schémas, protocoles et formats d'échange. Les composants techniques décrivent l'infrastructure requise. Les indicateurs de bénéfice définissent les métriques de succès. Les risques et mitigations documentent les aléas identifiés et les mesures correctives. Enfin, le calendrier prévisionnel établit les jalons clés du projet.

## Exemple 1 : INIT-001 : Télésuivi des patients tuberculeux

### 1. Identifiant et titre

| Champ | Valeur |
|-------|--------|
| **Code** | INIT-001 |
| **Titre** | Télésuivi des patients tuberculeux |
| **Type** | Initiative de soins à distance |
| **Portée** | National (12 districts pilotes) |
| **Statut** | En conception |

### 2. Capacité(s) CNISN

| Capacité | Contribution |
|----------|--------------|
| **CAP-INT-03** | Échange et médiation inter-systèmes |
| **CAP-INT-05** | Données agrégées de santé publique |

### 3. Chapitres ART applicables

Les chapitres ART mobilisés par cette initiative couvrent les accords de partage entre structures sanitaires et la plateforme nationale (ART-0), l'intégration et l'ingestion des données terrain (ART-1), la médiation et la normalisation sémantique (ART-2), ainsi que la sécurité et la résidence des données (ART-7).

### 4. Description de l'initiative

**Objectif :** Améliorer l'observance du traitement tuberculose par un suivi quotidien des patients via SMS ou WhatsApp, avec alertes automatiques en cas de non-réponse. L'initiative vise à réduire significativement le nombre de patients perdus de vue et à rapprocher le taux d'observance national de la cible OMS de 90 %.

**Contexte :** En 2025, Madagascar comptait 240 000 cas de tuberculose, avec un taux d'observance national de 82 %. Douze districts pilotes ont été retenus pour la première phase de déploiement, couvrant des zones à forte densité de cas et disposant d'une connectivité réseau suffisante pour supporter les échanges numériques.

**Parties prenantes :**

| Rôle | Organisation |
|------|--------------|
| Maîtrise d'ouvrage | Programme National Lutte contre la Tuberculose (PNLT) |
| Maîtrise d'œuvre | DEPSI + opérateur mobile |
| Financement | OMS, Fonds Mondial |
| Bénéficiaires | Patients TB, agents communautaires, centres de diagnostique |

### 5. Profil(s) PTISN applicable(s)

| Profil | Usage |
|--------|-------|
| **PT-01** (X-Road) | Échange sécurisé avec le système d'identification patient national |
| **PT-04** (Identité) | Résolution d'identité du bénéficiaire pour le télésuivi |
| **PT-08** (Données agrégées) | Remontée des indicateurs d'observance au niveau district |

### 6. Contrats d'interface

| Contrat | Format | Direction |
|---------|--------|-----------|
| Enregistrement patient | HL7 FHIR Patient | Plateforme → Registre national |
| Message d'observance | JSON (propriétaire, normalisé via ART-2) | App terrain → Plateforme |
| Alerte agent | SMS / WhatsApp | Plateforme → Agent communautaire |
| Rapport agrégé | IHE mADX | Plateforme → DHIS2 |

### 7. Composants techniques

| Composant | Technologie | Rôle |
|-----------|-------------|------|
| Serveur d'échange | X-Road | Sécurisation des échanges inter-systèmes |
| Moteur de médiation | MuleSoft / WSO2 | Transformation des messages terrain |
| Base patients | PostgreSQL + HL7 FHIR | Stockage des identités patient |
| Service SMS | API opérateur mobile | Envoi/réception des messages |
| Tableau de bord | DHIS2 | Visualisation des indicateurs |

### 8. Indicateurs de bénéfice

| Indicateur | Baseline | Cible | Source |
|------------|----------|-------|--------|
| Taux d'observance TB | 82% | 90% | PNLT |
| Temps de détection des abandons | 14 jours | 2 jours | Plateforme |
| Taux de réponse des patients | N/A | 70% | App terrain |
| Nombre de cas perdus de vue | 43 000/an | 25 000/an | PNLT |

### 9. Risques et mitigations

| Risque | Impact | Probabilité | Mitigation |
|--------|--------|-------------|------------|
| Faible couverture réseau dans les zones rurales | Élevé | Moyenne | Mode déconnecté, synchronisation différée |
| Résistance des patients au suivi numérique | Moyen | Élevée | Formation des agents, consentement éclairé |
| Interopérabilité avec les systèmes existants | Élevé | Moyenne | Adhésion aux profils PT-01 et PT-04 |
| Protection des données de santé sensibles | Élevé | Faible | Chiffrement, contrôle d'accès par rôle |

### 10. Calendrier prévisionnel

| Jalon | Date | Livrable |
|-------|------|----------|
| Cadrage | T2 2026 | Note de cadrage validée |
| Conception | T3 2026 | Dossier de conception détaillée |
| Développement | T4 2026 : T1 2027 | Prototype fonctionnel |
| Pilote | T2 2027 | Déploiement 3 districts |
| Évaluation | T3 2027 | Rapport d'évaluation pilote |
| Généralisation | T4 2027 | Déploiement 12 districts |

## Exemple 2 : INIT-002 : Collecte des données communautaires (ACS)

### 1. Identifiant et titre

| Champ | Valeur |
|-------|--------|
| **Code** | INIT-002 |
| **Titre** | Collecte numérique des données communautaires |
| **Type** | Initiative de collecte de données terrain |
| **Portée** | National (8 000 ACS) |
| **Statut** | En déploiement (5 districts) |

### 2. Capacité(s) CNISN

| Capacité | Contribution |
|----------|--------------|
| **CAP-INT-02** | Collecte et transmission des données |
| **CAP-INT-05** | Données agrégées de santé publique |

### 3. Chapitres ART applicables

Les chapitres ART concernés sont l'intégration et l'ingestion des données communautaires (ART-1), la médiation et la normalisation sémantique (ART-2), l'authentification et l'autorisation des agents (ART-3), ainsi que la qualité et la validation des données terrain (ART-8).

### 4. Description de l'initiative

**Objectif :** Remplacer la collecte papier des 8 000 Agents Communautaires de Santé (ACS) par une application mobile de collecte, avec transmission sécurisée des données vers DHIS2. L'initiative vise à réduire drastiquement le délai de remontée des données et à améliorer leur complétude et leur fiabilité.

**Contexte :** Les 8 000 ACS couvrent 16 000 fokontany à travers le territoire national. La collecte actuelle repose sur des formulaires papier, entraînant des retards de deux à quatre semaines avant que les données ne soient exploitable au niveau district. Quatre flux de collecte sont définis : activités communautaires, alertes, suivi des ménages et sensibilisation.

**Parties prenantes :**

| Rôle | Organisation |
|------|--------------|
| Maîtrise d'ouvrage | Direction de la Promotion de la Santé Communautaire (DPSC) |
| Maîtrise d'œuvre | DEPSI + partenaires techniques |
| Financement | UNICEF, Banque Mondiale |
| Bénéficiaires | ACS, agents relais communautaires, districts sanitaires |

### 5. Profil(s) PTISN applicable(s)

| Profil | Usage |
|--------|-------|
| **PT-01** (X-Road) | Transmission sécurisée des données collectées |
| **PT-08** (Données agrégées) | Remontée des rapports d'activité mensuels |

### 6. Contrats d'interface

| Contrat | Format | Direction |
|---------|--------|-----------|
| Rapport d'activité ACS | JSON normalisé via ART-2 | App ACS → Serveur district |
| Alerte communautaire | FHIR Flag | App ACS → Plateforme alertes |
| Rapport agrégé mensuel | IHE mADX | Serveur district → DHIS2 |
| Validation des données | FHIR OperationOutcome | Serveur → App ACS (feedback) |

### 7. Composants techniques

| Composant | Technologie | Rôle |
|-----------|-------------|------|
| Application mobile ACS | KoBoToolbox / ODK | Collecte de données terrain |
| Serveur de médiation | Node.js + FHIR | Transformation et validation |
| Base communautaire | PostgreSQL | Stockage temporaire des rapports |
| Synchronisation | API REST sécurisée | Transmission vers DHIS2 |

### 8. Indicateurs de bénéfice

| Indicateur | Baseline | Cible | Source |
|------------|----------|-------|--------|
| Temps de remontée des données | 2-4 semaines | < 48 heures | DPSC |
| Taux de complétude des rapports | 65% | 90% | DHIS2 |
| Taux d'erreur de saisie | 15% | < 5% | Contrôle qualité |
| Nombre d'alertes communautaires traitées | 1 200/mois | 3 000/mois | PNLP, PNRH |

### 9. Risques et mitigations

| Risque | Impact | Probabilité | Mitigation |
|--------|--------|-------------|------------|
| Connectivité limitée en zone rurale | Élevé | Élevée | Mode hors-ligne, synchronisation différée |
| Niveau numérique des ACS | Moyen | Élevée | Formation renforcée, interface simplifiée |
| Maintenance des terminaux | Moyen | Moyenne | Partenariat avec opérateur mobile |
| Sécurité des données sensibles | Élevé | Faible | Chiffrement, contrôle d'accès |

### 10. Calendrier prévisionnel

| Jalon | Date | Livrable |
|-------|------|----------|
| Cadrage | T1 2026 | Note de cadrage validée |
| Pilote (5 districts) | T2 2026 | 2 000 ACS équipés |
| Évaluation pilote | T3 2026 | Rapport d'évaluation |
| Généralisation (22 districts) | T4 2026 : T2 2027 | 8 000 ACS équipés |
| Intégration DHIS2 | T3 2027 | Flux automatisé |

## Exemple 3 : INIT-003 : Traçabilité des médicaments (mTrack)

### 1. Identifiant et titre

| Champ | Valeur |
|-------|--------|
| **Code** | INIT-003 |
| **Titre** | Traçabilité des médicaments essentiels (mTrack) |
| **Type** | Initiative de gestion des stocks |
| **Portée** | National (22 districts, 1 800 formations sanitaires) |
| **Statut** | En conception |

### 2. Capacité(s) CNISN

| Capacité | Contribution |
|----------|--------------|
| **CAP-INT-04** | Gestion des stocks et chaîne d'approvisionnement |
| **CAP-INT-05** | Données agrégées de santé publique |

### 3. Chapitres ART applicables

Les chapitres ART impliqués couvrent les accords de partage entre formations sanitaires et le plateau technique (ART-0), l'intégration et l'ingestion des données de stock (ART-1), la médiation et la normalisation sémantique selon la codification OMS ATC (ART-2), les référentiels nationaux de produits de santé (ART-4), ainsi que la sécurité et la résidence des données (ART-7).

### 4. Description de l'initiative

**Objectif :** Assurer la traçabilité complète des médicaments essentiels de la réception à la dispensation, avec alertes automatiques de rupture de stock et de péremption. L'initiative vise à réduire les pertes estimées à 15 % des stocks et à garantir la disponibilité des traitements dans les 1 800 formations sanitaires du territoire.

**Contexte :** Le parc sanitaire national comprend 1 800 formations sanitaires (hôpitaux, centres de santé, cases de santé) desservant l'ensemble de la population. La liste nationale des médicaments essentiels compte plus de 400 produits. Les pertes actuelles, principalement imputables à la péremption et aux ruptures de stock, sont estimées à 15 % du volume total.

**Parties prenantes :**

| Rôle | Organisation |
|------|--------------|
| Maîtrise d'ouvrage | Direction de la Pharmacie et du Médicament (DPM) |
| Maîtrise d'œuvre | DEPSI + opérateur logistique |
| Financement | Fonds Mondial, USAID |
| Bénéficiaires | Pharmaciens, responsables de stock, décideurs |

### 5. Profil(s) PTISN applicable(s)

| Profil | Usage |
|--------|-------|
| **PT-01** (X-Road) | Échange sécurisé avec le système national d'approvisionnement |
| **PT-04** (Identité) | Authentification des utilisateurs (pharmaciens) |
| **PT-08** (Données agrégées) | Remontée des indicateurs de gestion des stocks |

### 6. Contrats d'interface

| Contrat | Format | Direction |
|---------|--------|-----------|
| Entrée de stock | FHIR MedicationDispense | App formation → Serveur district |
| Sortie de stock | FHIR MedicationDispense | App formation → Serveur district |
| Alerte rupture | FHIR Flag | Serveur district → App formation |
| Rapport de stock | IHE mADX | Serveur district → DPM/DHIS2 |
| Référence produit | FHIR Medication (ATC) | Référentiel national → App formation |

### 7. Composants techniques

| Composant | Technologie | Rôle |
|-----------|-------------|------|
| Application de gestion des stocks | OpenLMIS | Gestion des commandes et stocks |
| Moteur de médiation | MuleSoft | Transformation et validation |
| Référentiel produits | PostgreSQL + ATC | Codification des médicaments |
| Service d'alertes | Apache Kafka | Notifications temps réel |
| Tableau de bord | DHIS2 | Visualisation des indicateurs |

### 8. Indicateurs de bénéfice

| Indicateur | Baseline | Cible | Source |
|------------|----------|-------|--------|
| Taux de rupture de stock | 25% | < 10% | DPM |
| Pertes par péremption | 15% | < 5% | DPM |
| Temps de détection des ruptures | 7 jours | 24 heures | mTrack |
| Taux de couverture des stocks | 70% | 90% | DPM |

### 9. Risques et mitigations

| Risque | Impact | Probabilité | Mitigation |
|--------|--------|-------------|------------|
| Faible connectivité dans les centres de santé | Élevé | Élevée | Mode hors-ligne, synchronisation |
| Résistance au changement des pharmaciens | Moyen | Élevée | Formation, accompagnement |
| Intégration avec les systèmes existants | Élevé | Moyenne | Adhésion aux profils PT-01/PT-04 |
| Qualité des données de stock | Moyen | Moyenne | Contrôle qualité automatisé |

### 10. Calendrier prévisionnel

| Jalon | Date | Livrable |
|-------|------|----------|
| Cadrage | T2 2026 | Note de cadrage validée |
| Conception | T3 2026 | Dossier de conception détaillée |
| Développement | T4 2026 : T1 2027 | Prototype fonctionnel |
| Pilote (3 districts) | T2 2027 | 150 formations équipées |
| Évaluation pilote | T3 2027 | Rapport d'évaluation |
| Généralisation | T4 2027 | 1 800 formations équipées |

## Liens

- Profils techniques
- Référentiel : Profils
- PT-01 : Échange interinstitutionnel
- PT-04 : Résolution d'identité
- PT-08 : Données agrégées

## Références

- **matrice de lecture** : Matrice de lecture du PTISN (niveau 4) (`03_ptisn/reading-matrix.md`)
- **Profils techniques** : Partie III : Profils techniques nationaux (`03_ptisn/03_profils/pt-00-index.md`)
- **Référentiel : Profils** : Partie III : Profils techniques nationaux (`03_ptisn/03_profils/pt-00-index.md`)
- **PT-01 : Échange interinstitutionnel** : Profil technique national (`03_ptisn/03_profils/pt-01-echange-interinstitutionnel.md`)
- **PT-04 : Résolution d'identité** : Profil technique national (`03_ptisn/03_profils/pt-04-resolution-identite-beneficiaire.md`)
- **PT-08 : Données agrégées** : Profil technique national (`03_ptisn/03_profils/pt-08-echange-donnees-agregees.md`)
