---
title: Exemples de profils d'initiative remplis
id: ptisn-exemples
domain: 03_ptisn
version: "0.1.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: [ptisn, exemples, profils, niveau-4]
---

# Exemples de profils d'initiative remplis

## Pour qui lire ce document

**Niveau :** niveau 4 — Profils Techniques d'Implémentation par Initiative.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

Ce document présente **3 exemples concrets** de profils d'initiative remplis selon le template standard du PTISN. Chaque exemple illustre comment un projet réel est décrit, rattaché aux capabilités, aux chapitres ART et aux composants du référentiel.

## Structure du template

Chaque profil suit la structure standardisée :

1. **Identifiant et titre** — Code de l'initiative (ex. : INIT-001)
2. **Capacité(s) CNISN** — Rattachement aux capacités d'interopérabilité
3. **Chapitres ART applicables** — Patterns architecturaux mobilisés
4. **Description de l'initiative** — Objectif, contexte, parties prenantes
5. **Profil(s) PTISN applicable(s)** — Profils techniques requis
6. **Contrats d'interface** — Schémas, protocoles, formats d'échange
7. **Composants techniques** — Infrastructure requise
8. **Indicateurs de bénéfice** — Métriques de succès
9. **Risques et mitigations** — Risques identifiés et mesures correctives
10. **Calendrier prévisionnel** — Jalons clés

---

## Exemple 1 : INIT-001 — Télésuivi des patients tuberculeux

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

- **ART-0** — Accords de partage entre structures sanitaires et plateforme nationale
- **ART-1** — Intégration et ingestion des données terrain
- **ART-2** — Médiation et normalisation sémantique
- **ART-7** — Sécurité et résidence des données

### 4. Description de l'initiative

**Objectif :** Améliorer l'observance du traitement tuberculose par un suivi quotidien des patients via SMS/WhatsApp, avec alertes automatiques en cas de non-réponse.

**Contexte :**
- 240 000 cas de TB en 2025
- Taux d'observance national : 82% (cible OMS : 90%)
- 12 districts pilotes retenus

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
| Développement | T4 2026 — T1 2027 | Prototype fonctionnel |
| Pilote | T2 2027 | Déploiement 3 districts |
| Évaluation | T3 2027 | Rapport d'évaluation pilote |
| Généralisation | T4 2027 | Déploiement 12 districts |

---

## Exemple 2 : INIT-002 — Collecte des données communautaires (ACS)

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

- **ART-1** — Intégration et ingestion des données communautaires
- **ART-2** — Médiation et normalisation sémantique
- **ART-3** — Authentification et autorisation des agents
- **ART-8** — Qualité et validation des données terrain

### 4. Description de l'initiative

**Objectif :** Remplacer la collecte papier des 8 000 Agents Communautaires de Santé (ACS) par une application mobile de collecte, avec transmission sécurisée des données vers DHIS2.

**Contexte :**
- 8 000 ACS couvrant 16 000 fokontany
- Collecte actuelle sur formulaires papier (retard de 2-4 semaines)
- 4 flux de collecte : activités communautaires, alertes, suivi des ménages, sensibilisation

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
| Généralisation (22 districts) | T4 2026 — T2 2027 | 8 000 ACS équipés |
| Intégration DHIS2 | T3 2027 | Flux automatisé |

---

## Exemple 3 : INIT-003 — Traçabilité des médicaments (mTrack)

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

- **ART-0** — Accords de partage entre formations sanitaires et plateau technique
- **ART-1** — Intégration et ingestion des données de stock
- **ART-2** — Médiation et normalisation sémantique (codification OMS ATC)
- **ART-4** — Référentiels nationaux (produits de santé)
- **ART-7** — Sécurité et résidence

### 4. Description de l'initiative

**Objectif :** Assurer la traçabilité complète des médicaments essentiels de la réception à la dispensation, avec alertes automatiques de rupture de stock et de péremption.

**Contexte :**
- 1 800 formations sanitaires (hôpitaux, centres de santé, case de santé)
- 400+ médicaments essentiels dans la liste nationale
- Pertes estimées à 15% des stocks (péremption, ruptures)

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
| Développement | T4 2026 — T1 2027 | Prototype fonctionnel |
| Pilote (3 districts) | T2 2027 | 150 formations équipées |
| Évaluation pilote | T3 2027 | Rapport d'évaluation |
| Généralisation | T4 2027 | 1 800 formations équipées |

---

## Liens

- [Profils techniques](../03_profils/pt-00-index.md)
- [Référentiel — Profils](../03_profils/pt-00-index.md)
- [PT-01 — Échange interinstitutionnel](../03_profils/pt-01-echange-interinstitutionnel.md)
- [PT-04 — Résolution d'identité](../03_profils/pt-04-resolution-identite-beneficiaire.md)
- [PT-08 — Données agrégées](../03_profils/pt-08-echange-donnees-agregees.md)
