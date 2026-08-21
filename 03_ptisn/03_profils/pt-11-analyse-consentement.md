---

title: "Analyse PT-11 : Profil technique du consentement"
id: ptisn-PT-11-analyse
domain: 03_profils
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: ["ptisn", "PT-11", "consentement", "analyse"]
---

# Analyse PT-11 : Profil technique du consentement

## Pour qui lire ce document

**Niveau :** niveau 4 : Profils techniques d'implémentation de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## 1. Contexte

Le PT-11 (Consentement et bases d'autorisation) est identifié comme **critique** dans l'analyse de contenu :

> **C7** : PT-11 Consentement vide : aucun standard technique choisi, toute initiative de partage patients bloquée.

Cette analyse vise à :
1. Évaluer les options techniques disponibles
2. Proposer un profil national de consentement
3. Définir les travaux nécessaires à sa mise en œuvre

## 2. Cadre juridique

### 2.1 Bases légales du traitement des données de santé

| Base légale | Description | Cas d'usage |
|-------------|-------------|-------------|
| **Consentement** | Autorisation explicite du patient | Partage de données non urgent |
| **Mandat de soins** | Autorisation implicite dans le cadre des soins | Consultation, prescription, suivi |
| **Mandat de santé publique** | Obligation de notification | Surveillance épidémique, déclaration obligatoire |
| **Obligation légale** | Exigence réglementaire | Déclarations obligatoires, statistiques |
| **Intérêt vital** | Urgence médicale | Soins d'urgence sans consentement possible |
| **Accord interinstitutionnel** | Protocole entre organisations | Échange de données entre ministères |

### 2.2 Principes directeurs

1. **Minimisation** : collecter uniquement les données nécessaires
2. **Finalité** : utilisation limitée à la finalité déclarée
3. **Durée** : conservation limitée dans le temps
4. **Droit d'accès** : le patient peut consulter et modifier ses choix
5. **Droit de retrait** : le patient peut retirer son consentement
6. **Traçabilité** : enregistrer toutes les décisions de consentement

## 3. Options techniques

### 3.1 Option A : FHIR Consent

| Champ | Valeur |
|-------|--------|
| **Standard** | HL7 FHIR R4 : Resource Consent |
| **Avantages** | Standard international, intégré à l'écosystème FHIR, largement documenté |
| **Inconvénients** | Complexité du modèle, nécessite un profiling national |
| **Maturité** | Élevée (utilisé dans plusieurs pays) |

### 3.2 Option B : IHE BPPC (Basic Patient Privacy Consents)

| Champ | Valeur |
|-------|--------|
| **Standard** | IHE Basic Patient Privacy Consents |
| **Avantages** | Profil IHE reconnu, orienté document |
| **Inconvénients** | Moins flexible que FHIR, orienté document papier |
| **Maturité** | Moyenne |

### 3.3 Option C : Solution nationale sur mesure

| Champ | Valeur |
|-------|--------|
| **Standard** | Développement national |
| **Avantages** | Adapté au contexte local |
| **Inconvénients** | Pas d'interopérabilité, coût de développement |
| **Maturité** | Faible |

### 3.4 Recommandation

**Option A : FHIR Consent** avec les éléments suivants :

| Élément | Valeur |
|---------|--------|
| **Ressource principale** | FHIR Consent |
| **Profils nationaux** | 3 profils (consentement général, santé publique, urgence) |
| **Intégration** | Articulation avec PT-04 (identité) et PT-06 (autorisation) |
| **Stockage** | Service national de consentement |

## 4. Architecture proposée

```
┌─────────────────────────────────────────────────────────────┐
│              Architecture PT-11 Consentement                 │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │           Point de service patient                   │    │
│  │    (Application mobile, portail web, guichet)        │    │
│  └──────────────────────┬──────────────────────────────┘    │
│                         │                                    │
│                         ▼                                    │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Service national de consentement             │    │
│  │  - Enregistrement du consentement                    │    │
│  │  - Consultation et modification                      │    │
│  │  - Vérification au moment de l'accès                 │    │
│  │  - Traçabilité des décisions                         │    │
│  └──────────────────────┬──────────────────────────────┘    │
│                         │                                    │
│          ┌──────────────┼──────────────┐                    │
│          │              │              │                    │
│          ▼              ▼              ▼                    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                │
│  │ PT-04    │  │ PT-06    │  │ PT-12    │                │
│  │ Identité │  │ Autoris. │  │ Audit    │                │
│  └──────────┘  └──────────┘  └──────────┘                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## 5. Services à implémenter

| Service | Description | Priorité |
|---------|-------------|----------|
| **Enregistrement** | Capture du consentement patient | 🔴 Haute |
| **Consultation** | Accès aux choix de consentement | 🔴 Haute |
| **Modification** | Mise à jour des choix | 🔴 Haute |
| **Retrait** | Retrait du consentement | 🔴 Haute |
| **Vérification** | Contrôle au moment de l'accès | 🔴 Haute |
| **Traçabilité** | Journalisation des accès | 🟡 Moyenne |
| **Politiques** | Gestion des règles de consentement | 🟡 Moyenne |
| **Reporting** | Statistiques d'utilisation | 🟢 Basse |

## 6. Travaux à mener

| # | Travail | Responsable | Échéance |
|---|---------|-------------|----------|
| 1 | Analyse du cadre juridique national | Direction Juridique | T4 2026 |
| 2 | Classification des cas d'usage | DEPSI | T4 2026 |
| 3 | Définition des politiques de consentement | DEPSI + Juridique | T1 2027 |
| 4 | Évaluation des standards disponibles | DEPSI | T4 2026 |
| 5 | Articulation avec le registre patient (PT-04) | DEPSI | T1 2027 |
| 6 | Articulation avec le fournisseur d'identité | DEPSI | T1 2027 |
| 7 | Articulation avec les mandats de santé publique | DEPSI + Programmes | T2 2027 |
| 8 | Développement du prototype | DEPSI | T2 2027 |
| 9 | Tests et validation | DEPSI | T3 2027 |
| 10 | Déploiement pilote | DEPSI | T4 2027 |

## 7. Risques et mitigations

| Risque | Impact | Probabilité | Mitigation |
|--------|--------|-------------|------------|
| Cadre juridique flou | Élevé | Moyenne | Analyse juridique approfondie |
| Complexité technique | Élevé | Moyenne | Utilisation de FHIR (standard) |
| Résistance au changement | Moyen | Élevée | Formation, accompagnement |
| Interopérabilité limitée | Élevé | Faible | Adhésion aux profils FHIR |

## 8. Calendrier prévisionnel

```
2026                    2027
T3      T4      T1      T2      T3      T4
│       │       │       │       │       │
├───────┼───────┼───────┼───────┼───────┤
│       │       │       │       │       │
│  Analyse juridique    │       │       │
│  ─────────────►      │       │       │
│       │       │       │       │       │
│       Définition      │       │       │
│       politiques ─────►      │       │
│       │       │       │       │       │
│       Prototype ──────►      │       │
│       │       │       │       │       │
│       Tests ─────────►       │       │
│       │       │       │       │       │
│       Pilote ────────────────►       │
│       │       │       │       │       │
└───────┴───────┴───────┴───────┴───────┘
```

## Liens

- PT-11 : Profil technique
- CAP-INT-09 : Gestion des consentements
- ART-4b : Bases d'autorisation
- PT-04 : Résolution d'identité
- PT-06 : Authentification

## Références

- **matrice de lecture** : Matrice de lecture du PTISN (niveau 4) (`03_ptisn/reading-matrix.md`)
- **PT-11 : Profil technique** : Profil technique national (`referentiel/profils/pt-11.md`)
- **CAP-INT-09 : Gestion des consentements** : CAP-INT-09 : Gestion des consentements et bases d’autorisation (`referentiel/capacites/cap-int-09.md`)
- **ART-4b : Bases d'autorisation** : Bases d'autorisation (`referentiel/chapitres/art-4b.md`)
- **PT-04 : Résolution d'identité** : Profil technique national (`referentiel/profils/pt-04.md`)
- **PT-06 : Authentification** : Profil technique national (`referentiel/profils/pt-06.md`)
