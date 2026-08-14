---
title: "Cas d'usage — Couverture sanitaire et protection financière"
id: ptisn-cas-usage-couverture
domain: 03_ptisn
version: "0.1"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: ["ptisn", "niveau-4", "cas-usage", "couverture", "protection-financiere", "exemption", "vs-03"]
---

# Cas d'usage — Couverture sanitaire et protection financière (VS-03)

## Pour qui lire ce document

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| Partenaires techniques et financiers | ◐ |

---

## Objectif

Ce document montre comment les **profils techniques existants** composent pour couvrir le cycle complet de la couverture santé universelle : identification des bénéficiaires, vérification des droits, prise en charge sans paiement, facturation et remboursement.

## Principe architectural

La protection financière est un **cas d'usage métier** qui consomme plusieurs profils existants. Elle traverse le point de service (exemption), la médiation (facturation) et l'entrepôt (audit).

```
┌─────────────────────────────────────────────────────────────────────┐
│              PROTECTION FINANCIÈRE (VS-03)                         │
│  Bénéficiaire → Droits → Exemption → Facturation → Remboursement  │
└──────┬──────────┬──────────┬──────────┬──────────┬─────────────────┘
       │          │          │          │          │
       ▼          ▼          ▼          ▼          ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    PROFILS TECHNIQUES                              │
│  PT-04    │  PT-11  │  PT-01   │  PT-02  │  PT-12  │  PT-09     │
│  Identité │Consent. │ Échange  │Médiation│ Audit   │ Données    │
│           │         │          │         │         │ agrégées   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Scénario — Cycle complet de protection financière

### Phase 1 — Identification du bénéficiaire (EV-15)

**Objectif** : Enregistrer le bénéficiaire et lui attribuer un identifiant unique national.

```
Fokontany/Commune         Application terrain        INP (CMP-11)
        │                       │                        │
        │ Fiche bénéficiaire    │                        │
        │ (NIN, nom, âge,       │                        │
        │  commune)             │                        │
        │──────────────────────▶│  Vérification          │
        │                       │  unicité               │
        │                       │───────────────────────▶│
        │                       │                        │
        │                       │  NIN attribué/confirmé │
        │                       │◀───────────────────────│
        │                       │                        │
        │  Carte bénéficiaire   │                        │
        │◀──────────────────────│                        │
```

**Profils mobilisés** :

| Profil | Rôle |
|--------|------|
| **PT-04** | Résolution d'identité bénéficiaire (INP) |
| **PT-02** | Médiation (données communautaires → FHIR) |
| **PT-12** | Traçabilité de l'enregistrement |

---

### Phase 2 — Vérification des droits au point de service (EV-16/EV-18)

**Objectif** : Vérifier que le bénéficiaire a droit à l'exemption et appliquer la prise en charge sans paiement.

```
Agent de santé             Registre éligibilité (CMP-12)    Patient
        │                          │                           │
        │ Recherche bénéficiaire   │                           │
        │ (NIN ou recherche)        │                           │
        │─────────────────────────▶│                           │
        │                          │                           │
        │  Statut éligibilité       │                           │
        │  (CSU, BPC, AMM, autre)  │                           │
        │◀─────────────────────────│                           │
        │                          │                           │
        │  Confirmation            │                           │
        │  « Exemption applicable »│                           │
        │─────────────────────────────────────────────────────▶│
        │                          │                           │
        │  Soins dispensés         │                           │
        │  sans paiement           │                           │
```

**Profils mobilisés** :

| Profil | Rôle |
|--------|------|
| **PT-04** | Résolution d'identité (recherche patient) |
| **PT-11** | Consentement pour la vérification des droits |
| **PT-02** | Médiation (vérification éligibilité) |
| **PT-12** | Audit de la vérification (traçabilité) |

**Données échangées** :
- `Coverage` (FHIR) — couverture sanitaire du patient
- `EligibilityRequest/Response` — vérification en temps réel
- `Patient` — identité du bénéficiaire

---

### Phase 3 — Facturation et soumission (EV-19)

**Objectif** : Documenter les soins dispensés et soumettre la facture au mécanisme de financement.

```
Formation sanitaire        Médiation (PT-02)         Fonds de remboursement
        │                       │                          │
        │ Facture structurée     │                          │
        │ (Claim FHIR)           │                          │
        │──────────────────────▶│  Validation +             │
        │                       │  normalisation            │
        │                       │─────────────────────────▶│
        │                       │                          │
        │                       │  Accusé de réception      │
        │                       │◀─────────────────────────│
        │                       │                          │
        │  Confirmation          │                          │
        │◀──────────────────────│                          │
```

**Profils mobilisés** :

| Profil | Rôle |
|--------|------|
| **PT-01** | Échange interinstitutionnel (facture → fonds) |
| **PT-02** | Médiation (normalisation factures) |
| **PT-12** | Audit trail de la facturation |

**Données échangées** :
- `Claim` (FHIR) — facture détaillée
- `Coverage` — référence à la couverture
- `Account` — suivi financier

---

### Phase 4 — Remboursement (EV-20)

**Objectif** : Rembourser la formation sanitaire dans les délais convenus.

```
Fonds de remboursement     Médiation (PT-02)         Formation sanitaire
        │                       │                          │
        │ Instruction            │                          │
        │ de la facture          │                          │
        │──────────────────────▶│  Vérification             │
        │                       │  conformité               │
        │                       │─────────────────────────▶│
        │                       │                          │
        │  Paiement validé       │                          │
        │◀──────────────────────│◀─────────────────────────│
        │                       │                          │
        │  Notification paiement │                          │
        │──────────────────────▶│─────────────────────────▶│
```

---

### Phase 5 — Audit et contrôle (EV-21)

**Objectif** : Détecter les fraudes, ajuster les mécanismes, améliorer l'équité.

```
Entrepôt (CMP-03)         Moteur analytique (CMP-04)    Inspection
        │                       │                          │
        │ Données de             │                          │
        │ facturation            │                          │
        │ agrégées               │                          │
        │──────────────────────▶│  Analyse anomalies        │
        │                       │  (patterns suspects)     │
        │                       │─────────────────────────▶│
        │                       │                          │
        │  Rapport audit         │  Investigation           │
        │◀──────────────────────│◀─────────────────────────│
```

**Profils mobilisés** :

| Profil | Rôle |
|--------|------|
| **PT-08** | Échange de données agrégées (analyse) |
| **PT-09** | Analytique et exposition des données |
| **PT-12** | Audit trail complet |
| **PT-10** | Confiance (accès restreint aux données financières) |

---

## Matrice de composition

| Étape | PT-01 | PT-02 | PT-04 | PT-08 | PT-09 | PT-10 | PT-11 | PT-12 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| Identification (EV-15) | — | ● | ● | — | — | — | — | ● |
| Vérification droits (EV-18) | — | ● | ● | — | — | ● | ● | ● |
| Facturation (EV-19) | ● | ● | — | — | — | — | — | ● |
| Remboursement (EV-20) | — | ● | — | — | — | — | — | ● |
| Audit (EV-21) | — | — | — | ● | ● | ● | — | ● |

---

## Exigences transversales

| Exigence | Source | Applicable à |
|----------|--------|--------------|
| PT-11 — Consentement | CAP-INT-09 | Vérification des droits |
| PT-10 — Confiance | CAP-INT-08 | Accès données financières |
| Loi 2014-038 | National | Cadre juridique exemption |

---

## Liens

- [VS-03 — Protéger financièrement la population](../../00_caesn/01_value-streams/vs-03-financial-protection.md)
- [PT-01 — Échange interinstitutionnel](../03_profils/pt-01-echange-interinstitutionnel.md)
- [PT-02 — Médiation intra-secteur](../03_profils/pt-02-mediation-intra-secteur.md)
- [PT-04 — Résolution identité bénéficiaire](../03_profils/pt-04-resolution-identite-beneficiaire.md)
- [PT-10 — Confiance et autorisation](../03_profils/pt-10-confiance-authentification-autorisation.md)
- [PT-11 — Consentement](../03_profils/pt-11-consentement-bases-autorisation.md)
- [PT-12 — Audit et traçabilité](../03_profils/pt-12-audit-provenance-traçabilité.md)
