---

title: "Veille architecturale"
id: veille-architecturale
domain: 02_artsn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: ["artsn", "gouvernance", "veille", "standards", "tendances", "niveau-3"]
---

# Veille architecturale

## Pour qui lire ce document

**Niveau :** niveau 3 : Architecture de Référence Technique de la Santé Numérique.

Ce document s'adresse prioritairement aux équipes DEPSI et techniques ainsi qu'aux partenaires techniques et financiers. Les directions métier et programmes, ainsi que les équipes SIS, données et suivi-évaluation, trouveront une lecture complémentaire utile. Les décideurs institutionnels peuvent y recourir ponctuellement.

## Objet

Ce document définit le processus de veille architecturale pour maintenir l'ARTSN alignée sur les standards en vigueur, les évolutions technologiques et les besoins métier émergents. La veille alimente le processus de décision du CNASN et garantit la pertinence continue du cadre.

## 1. Périmètre de la veille

### 1.1 Domaines de veille

| Domaine | Sujet | Priorité |
|---------|-------|----------|
| **Standards de données** | HL7 FHIR, IHE, CIM-10, LOINC, SNOMED CT | Haute |
| **Interopérabilité** | X-Road, mADX, GDHCN, API REST | Haute |
| **Sécurité** | OAuth 2.0, OpenID Connect, chiffrement, zero-trust | Haute |
| **Souveraineté** | RGPD-like, protection des données, hébergement | Haute |
| **Tendances technologiques** | IA en santé, IoT médical, blockchain, FHIR R6 | Moyenne |
| **Réglementation** | Lois nationales, accords SADC, politiques OMS | Haute |
| **Concurrence** | Architectures similaires (Sénégal, Rwanda, Tunisie) | Basse |

### 1.2 Sources de veille

| Source | Type | Fréquence | Responsable |
|--------|------|-----------|-------------|
| **HL7 International** | Standard FHIR, IG, ballotages | Continue | DEPSI |
| **IHE International** | Profils d'intégration | Trimestriel | DEPSI |
| **OMS / OMS-AFRO** | Politiques santé, standards numériques | Mensuel | DEPSI |
| **Banque Mondiale** | Projets eHealth, financements | Trimestriel | BRV |
| **SADC / AMSP** | Interopérabilité régionale | Trimestriel | DEPSI |
| **OMS GDHCN** | Confiance numérique | Mensuel | DEPSI |
| **DHIS2 Community** | Évolutions DHIS2, mADX | Mensuel | DEPSI |
| **OpenHIE** | Patterns d'interopérabilité | Trimestriel | DEPSI |
| **GovStack** | Standards gouvernementaux | Semestriel | DEPSI |
| **Articles scientifiques** | Recherche en eHealth | Trimestriel | DEPSI |
| **Pays similaires** | Retours d'expérience | Semestriel | DEPSI |

## 2. Processus de veille

### 2.1 Collecte

Le chargé de veille consulte les sources identifiées de manière continue, enregistre les veilles dans la fiche à chaque découverte et les classifie par domaine et priorité.

| Étape | Action | Responsable | Fréquence |
|-------|--------|-------------|-----------|
| 2.1.1 | Consulter les sources identifiées | Chargé de veille | Continue |
| 2.1.2 | Enregistrer les veilles dans la fiche | Chargé de veille | À chaque découverte |
| 2.1.3 | Classifier par domaine et priorité | Chargé de veille | À chaque découverte |

### 2.2 Analyse

Le comité technique évalue l'impact sur l'ARTSN, identifie les actions requises et le CNASN priorise ces actions, le tout de manière trimestrielle.

| Étape | Action | Responsable | Fréquence |
|-------|--------|-------------|-----------|
| 2.2.1 | Évaluer l'impact sur l'ARTSN | Comité technique | Trimestriel |
| 2.2.2 | Identifier les actions requises | Comité technique | Trimestriel |
| 2.2.3 | Prioriser les actions | CNASN | Trimestriel |

### 2.3 Intégration

Le chargé de veille soumet les modifications au CNASN selon la priorité établie, la DEPSI met à jour l'ARTSN après décision et le CNASN communique les changements après publication.

| Étape | Action | Responsable | Fréquence |
|-------|--------|-------------|-----------|
| 2.3.1 | Soumettre les modifications au CNASN | Chargé de veille | Selon priorité |
| 2.3.2 | Mettre à jour l'ARTSN si nécessaire | DEPSI | Après décision |
| 2.3.3 | Communiquer les changements | CNASN | Après publication |

## 3. Fiche de veille

### 3.1 Template

| Champ | Description |
|-------|-------------|
| **ID** | VEE-XXXX (numéro séquentiel) |
| **Date** | Date de découverte |
| **Source** | Source de l'information |
| **Domaine** | Standards, interopérabilité, sécurité, souveraineté, tendances, réglementation |
| **Titre** | Résumé en une phrase |
| **Description** | Détail de l'évolution détectée |
| **Impact ARTSN** | Nul / Faible / Moyen / Élevé / Critique |
| **Composant impacté** | Chapitre, profil, fondation concerné(s) |
| **Action recommandée** | Aucune / Veille / Modification / Nouvelle ADR |
| **Statut** | Nouveau / En analyse / Traité / Archivé |

### 3.2 Exemples de fiches

| ID | Date | Source | Titre | Impact | Action |
|----|------|--------|-------|--------|--------|
| VEE-0001 | 2026-08-13 | HL7 | Publication FHIR R6 (draft) | Élevé | Veille : analyse impact |
| VEE-0002 | 2026-08-13 | IHE | Nouveau profil mCSD pour le community health | Moyen | Veille : à évaluer |
| VEE-0003 | 2026-08-13 | OMS | Mise à jour GDHCN v2.0 | Élevé | Modification PT-14 |

## 4. Revue trimestrielle

### 4.1 Ordre du jour type

L'ordre du jour de la revue trimestrielle comprend le bilan des veilles (nombre de fiches, répartition par domaine), l'analyse de l'impact sur l'ARTSN (modifications à programmer), l'examen des standards émergents (technologies à surveiller), les retours d'expérience de pays similaires pertinents, et la définition du plan d'action avec les priorités du trimestre suivant.

### 4.2 Participants

| Rôle | Participation |
|------|---------------|
| Chargé de veille | Présentation |
| Comité technique | Analyse |
| CNASN | Décision |
| DEPSI | Compte-rendu |

### 4.3 Livrables

| Livrable | Description |
|----------|-------------|
| **Rapport de veille trimestriel** | Synthèse des veilles et impacts |
| **Plan d'action** | Modifications à programmer |
| **Mise à jour des fiches** | Statuts et actions |

## 5. Intégration avec les autres processus

La veille architecturale s'intègre aux processus de décision d'architecture (ADR) en alimentant les propositions d'ADR, à l'homologation en informant les critères de conformité, au processus de dépréciation en détectant les standards abandonnés, et à la roadmap en influençant la priorisation.

| Processus | Lien avec la veille |
|-----------|---------------------|
| **Décisions d'architecture (ADR)** | La veille alimente les propositions d'ADR |
| **Homologation** | La veille informe les critères de conformité |
| **Dépréciation** | La veille détecte les standards abandonnés |
| **Roadmap** | La veille influence la priorisation |

## Liens

Voir les documents suivants : Gouvernance ARTSN, Processus de dépréciation, Registre des décisions, et Feuille de route.

## Références

- **Gouvernance ARTSN** : Gouvernance de l'ARTSN (`02_artsn/06_gouvernance/index.md`)
- **Processus de dépréciation** : Processus de dépréciation des composants (`02_artsn/06_gouvernance/depreciation.md`)
- **Registre des décisions** : Registre des décisions d'architecture (ADR) (`01_cnisn/06_decisions/registre-decisions.md`)
- **Feuille de route** : Feuille de route de déploiement progressif de l'ARTSN (`02_artsn/09_feuille-route/index.md`)
