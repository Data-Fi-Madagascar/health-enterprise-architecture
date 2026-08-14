---
title: "Cas d'usage — Référence, contre-référence et évacuation sanitaire"
id: ptisn-cas-usage-reference
domain: 03_ptisn
version: "0.1"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: ["ptisn", "niveau-4", "cas-usage", "reference", "contre-reference", "evacuation"]
---

# Cas d'usage — Référence, contre-référence et évacuation sanitaire

## Pour qui lire ce document

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| Partenaires techniques et financiers | ◐ |

---

## Objectif

Ce document montre comment les **profils techniques existants** (PTISN) composent pour couvrir les 3 scénarios critiques du parcours patient inter-établissement. Il ne s'agit pas d'un profil technique, mais d'une **illustration d'assemblage** de briques techniques déjà définies.

## Principe architectural

Les scénarios métier (référence, contre-référence, évacuation) ne sont **pas** des profils techniques. Ce sont des **cas d'usage** qui consomment plusieurs profils existants :

```
┌─────────────────────────────────────────────────────────────┐
│                   CAS D'USAGE MÉTIER                       │
│  Référence │ Contre-référence │ Évacuation sanitaire       │
└──────┬──────────┬──────────────────┬────────────────────────┘
       │          │                  │
       ▼          ▼                  ▼
┌─────────────────────────────────────────────────────────────┐
│                   PROFILS TECHNIQUES                       │
│  PT-01/PT-02  │  PT-11   │  PT-14  │  PT-07  │  PT-12    │
│  Échange +    │ Consent. │ Trans-  │ Termin. │  Audit    │
│  Médiation    │          │ frontal.│         │           │
└─────────────────────────────────────────────────────────────┘
```

---

## Scénario 1 — Référence (S-03)

**Définition** : Orientation d'un patient d'un niveau de soins vers un autre (ex. : CSB → hôpital régional).

### Flux technique

```
CSB rural                    Médiation nationale              Hôpital régional
    │                              │                               │
    │  ServiceRequest (referral)   │                               │
    │─────────────────────────────▶│  Validation + routage         │
    │                              │──────────────────────────────▶│
    │                              │                               │
    │                              │  Acceptation                  │
    │◀─────────────────────────────│◀──────────────────────────────│
    │                              │                               │
    │  IPS (données cliniques)     │                               │
    │─────────────────────────────▶│  Transmission                 │
    │                              │──────────────────────────────▶│
```

### Profils consommés

| Profil | Rôle dans le scénario |
|--------|----------------------|
| **PT-01** | Transport des messages (X-Road / API Gateway) |
| **PT-02** | Médiation sémantique (transformation des données CSB → FHIR) |
| **PT-04** | Résolution d'identité patient (vérifier/créer l'identité dans l'INP) |
| **PT-07** | Mapping terminologique (codes CSB → CIM-10 / LOINC) |
| **PT-12** | Traçabilité de l'événement de référence |

### Données échangées

- `ServiceRequest` (type: referral) — demande de référence
- `Patient` — identité du patient (via INP)
- `AllergyIntolerance`, `MedicationStatement`, `Condition` — données cliniques minimales
- `DocumentReference` — compte-rendu si disponible

---

## Scénario 2 — Contre-référence (S-04)

**Définition** : Retour du patient vers l'établissement d'origine après prise en charge spécialisée, avec compte-rendu et recommandations.

### Flux technique

```
Hôpital régional              Médiation nationale              CSB rural
    │                              │                               │
    │  ServiceRequest (referral)   │                               │
    │  + DocumentReference (CR)    │                               │
    │─────────────────────────────▶│  Validation + routage         │
    │                              │──────────────────────────────▶│
    │                              │                               │
    │                              │  Acceptation + plan de suivi  │
    │◀─────────────────────────────│◀──────────────────────────────│
    │                              │                               │
    │  MedicationRequest (suite)   │                               │
    │─────────────────────────────▶│  Transmission                 │
    │                              │──────────────────────────────▶│
```

### Profils consommés

| Profil | Rôle dans le scénario |
|--------|----------------------|
| **PT-01** | Transport des messages |
| **PT-02** | Médiation sémantique |
| **PT-04** | Résolution d'identité |
| **PT-11** | Consentement pour le retour d'information |
| **PT-12** | Traçabilité |

### Données échangées

- `ServiceRequest` (type: referral) — demande de contre-référence
- `DocumentReference` — compte-rendu de la prise en charge spécialisée
- `MedicationRequest` — traitements à poursuivre
- `CarePlan` — plan de suivi recommandé

---

## Scénario 3 — Évacuation sanitaire (S-05)

### 3a. Évacuation nationale (EVA-N1/N2)

**Définition** : Transfert urgent d'un patient entre établissements nationaux avec transport sanitaire spécialisé.

### Flux technique

```
CSB/Hôpital régional    Médiation    Centre de commande    Hôpital destination
         │                   │               │                      │
         │ ServiceRequest    │               │                      │
         │ (transfer + URGENCE)             │                      │
         │──────────────────▶│  Routage +    │                      │
         │                   │  acceptation  │                      │
         │                   │──────────────▶│─────────────────────▶│
         │                   │               │                      │
         │                   │  Acceptation  │                      │
         │◀──────────────────│◀──────────────│◀─────────────────────│
         │                   │               │                      │
         │ Transport         │  Géolocalisation temps réel          │
         │ (FHIR Transport)  │──────────────▶│                      │
         │                   │               │                      │
         │                   │  Arrivée + IPS complet               │
         │                   │──────────────▶│─────────────────────▶│
```

### Profils consommés

| Profil | Rôle dans le scénario |
|--------|----------------------|
| **PT-01** | Transport des messages |
| **PT-02** | Médiation sémantique |
| **PT-04** | Résolution d'identité |
| **PT-11** | Consentement pour le transfert |
| **PT-12** | Traçabilité (audit trail complet) |

### 3b. Évacuation internationale (EVA-I1/I2)

**Définition** : Transfert urgent vers un centre spécialisé à l'étranger.

### Flux technique additionnel

```
Hôpital Madagascar          Médiation          Pays de destination
         │                      │                      │
         │ ServiceRequest       │                      │
         │ + IPS                │                      │
         │ + autorisation sortie│                      │
         │─────────────────────▶│  Vérification GDHCN  │
         │                      │  + accord bilatéral  │
         │                      │─────────────────────▶│
         │                      │                      │
         │                      │  Acceptation         │
         │◀─────────────────────│◀─────────────────────│
         │                      │                      │
         │ Transport            │  Suivi temps réel    │
         │─────────────────────▶│─────────────────────▶│
```

### Profils supplémentaires pour l'international

| Profil | Rôle dans le scénario |
|--------|----------------------|
| **PT-14** | Confiance transfrontalière (GDHCN), IPS, accords bilatéraux |

### Données échangées (internationale)

- `ServiceRequest` (type: transfer) — demande d'évacuation
- `IPS Composition` — résumé patient complet (ALGY, MDCA, PROB, IDOI, VITAL)
- `DocumentReference` — autorisation de sortie du territoire
- `Coverage` — couverture financière

---

## Matrice de composition

| Scénario | PT-01 | PT-02 | PT-04 | PT-07 | PT-11 | PT-12 | PT-14 |
|----------|-------|-------|-------|-------|-------|-------|-------|
| Référence (S-03) | ● | ● | ● | ● | ○ | ● | — |
| Contre-référence (S-04) | ● | ● | ● | ○ | ● | ● | — |
| Évacuation nationale (S-05 N) | ● | ● | ● | ○ | ● | ● | — |
| Évacuation internationale (S-05 I) | ● | ● | ● | ○ | ● | ● | ● |

Légende : ● requis · ○ optionnel · — non applicable

---

## Exigences transversales

| Exigence | Source | Applicable à |
|----------|--------|--------------|
| ENF-5 — Coordination processus complexes | ART-8a | Les 3 scénarios |
| EXG-TF-01 à TF-08 | CAP-INT-13 | Évacuation internationale |
| Consentement (PT-11) | CAP-INT-09 | Tous les scénarios |

---

## Liens

- [S-03 — Référence](../../02_artsn/05_dictionnaire/index.md)
- [S-04 — Contre-référence](../../02_artsn/05_dictionnaire/index.md)
- [S-05 — Évacuation sanitaire](../../02_artsn/05_dictionnaire/index.md)
- [PT-01 — Échange interinstitutionnel](../03_profils/pt-01-echange-interinstitutionnel.md)
- [PT-02 — Médiation intra-secteur](../03_profils/pt-02-mediation-intra-secteur.md)
- [PT-11 — Consentement](../03_profils/pt-11-consentement-bases-autorisation.md)
- [PT-14 — Interopérabilité transfrontalière](../03_profils/pt-14-interopabilite-transfrontaliere.md)
- [ENF-5 — Coordination processus complexes](../../referentiel/exigences/enf-5.md)
