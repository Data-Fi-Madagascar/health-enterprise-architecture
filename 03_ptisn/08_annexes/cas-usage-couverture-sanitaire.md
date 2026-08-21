---
title: "Cas d'usage : Couverture sanitaire et protection financière"
id: ptisn-cas-usage-couverture
domain: 08_annexes
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: ["ptisn", "niveau-4", "cas-usage", "couverture", "protection-financiere", "exemption", "VS-03"]
---

# Cas d'usage : Couverture sanitaire et protection financière (VS-03)

## Pour qui lire ce document

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| Partenaires techniques et financiers | ◐ |

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

## Scénario : Cycle complet de protection financière

### Phase 1 : Identification du bénéficiaire (VS-03-01)

La première phase consiste à enregistrer le bénéficiaire et à lui attribuer un identifiant unique national. Le processus débute au niveau du Fokontany ou de la Commune, où la fiche bénéficiaire : comprenant le NIN, le nom, l'âge et la commune : est transmise à l'application terrain. Cette dernière soumet les informations au Pôle National d'Identité (INP) pour vérification d'unicité. Après validation, l'INP attribue ou confirme le NIN, et une carte bénéficiaire est délivrée au demandeur.

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

Les profils mobilisés lors de cette phase sont le PT-04 (résolution d'identité bénéficiaire via l'INP), le PT-02 (médiation assurant la conversion des données communautaires au format FHIR) et le PT-12 (traçabilité de l'enregistrement).

| Profil | Rôle |
|--------|------|
| **PT-04** | Résolution d'identité bénéficiaire (INP) |
| **PT-02** | Médiation (données communautaires → FHIR) |
| **PT-12** | Traçabilité de l'enregistrement |

### Phase 2 : Vérification des droits au point de service (VS-03-02/vs-03-04)

La phase de vérification des droits intervient au moment où le bénéficiaire se présente auprès d'un agent de santé. Ce dernier interroge le registre d'éligibilité pour confirmer que le patient bénéficie d'un droit à l'exemption : qu'il relève de la CSU, de la BPC, de l'AMM ou d'un autre mécanisme. Une fois le statut d'éligibilité confirmé, l'agent de santé dispense les soins sans paiement.

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

Les profils mobilisés sont le PT-04 (résolution d'identité pour la recherche patient), le PT-11 (consentement pour la vérification des droits), le PT-02 (médiation pour la vérification d'éligibilité) et le PT-12 (audit de la vérification en tant que traçabilité). Les données échangées comprennent le ressource FHIR `Coverage` (couverture sanitaire du patient), les ressources `EligibilityRequest` et `EligibilityResponse` (vérification en temps réel) et la ressource `Patient` (identité du bénéficiaire).

| Profil | Rôle |
|--------|------|
| **PT-04** | Résolution d'identité (recherche patient) |
| **PT-11** | Consentement pour la vérification des droits |
| **PT-02** | Médiation (vérification éligibilité) |
| **PT-12** | Audit de la vérification (traçabilité) |

### Phase 3 : Facturation et soumission (VS-03-05)

La phase de facturation consiste à documenter les soins dispensés et à soumettre la facture au mécanisme de financement. La formation sanitaire émet une facture structurée au format FHIR `Claim`, qui est transmise via la médiation (PT-02) au fonds de remboursement. La médiation assure la validation et la normalisation de la facture avant sa transmission. Le fonds de remboursement émet un accusé de réception, et la formation sanitaire reçoit une confirmation de prise en charge.

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

Les profils mobilisés sont le PT-01 (échange interinstitutionnel pour la transmission de la facture au fonds), le PT-02 (médiation pour la normalisation des factures) et le PT-12 (audit trail de la facturation). Les données échangées comprennent le `Claim` FHIR (facture détaillée), le `Coverage` (référence à la couverture) et l'`Account` (suivi financier).

| Profil | Rôle |
|--------|------|
| **PT-01** | Échange interinstitutionnel (facture → fonds) |
| **PT-02** | Médiation (normalisation factures) |
| **PT-12** | Audit trail de la facturation |

### Phase 4 : Remboursement (VS-03-06)

La phase de remboursement vise à indemniser la formation sanitaire dans les délais convenus. Le fonds de remboursement initie l'instruction de la facture, laquelle est transmise via la médiation pour vérification de conformité. Après validation, le paiement est validé et notifié à la formation sanitaire, qui reçoit la confirmation du virement.

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

### Phase 5 : Audit et contrôle (VS-03-07)

La phase d'audit et de contrôle a pour objectif de détecter les fraudes, d'ajuster les mécanismes de financement et d'améliorer l'équité du système. Les données de facturation agrégées sont extraites de l'entrepôt (CMP-03) et transmises au moteur analytique (CMP-04), qui réalise une analyse des anomalies et des patterns suspects. Les résultats alimentent un rapport d'audit transmis à l'inspection pour investigation.

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

Les profils mobilisés sont le PT-08 (échange de données agrégées pour l'analyse), le PT-09 (analytique et exposition des données), le PT-12 (audit trail complet) et le PT-10 (confiance pour l'accès restreint aux données financières).

| Profil | Rôle |
|--------|------|
| **PT-08** | Échange de données agrégées (analyse) |
| **PT-09** | Analytique et exposition des données |
| **PT-12** | Audit trail complet |
| **PT-10** | Confiance (accès restreint aux données financières) |

## Matrice de composition

| Étape | PT-01 | PT-02 | PT-04 | PT-08 | PT-09 | PT-10 | PT-11 | PT-12 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| Identification (VS-03-01) | : | ● | ● | : | : | : | : | ● |
| Vérification droits (VS-03-04) | : | ● | ● | : | : | ● | ● | ● |
| Facturation (VS-03-05) | ● | ● | : | : | : | : | : | ● |
| Remboursement (VS-03-06) | : | ● | : | : | : | : | : | ● |
| Audit (VS-03-07) | : | : | : | ● | ● | ● | : | ● |

## Exigences transversales

| Exigence | Source | Applicable à |
|----------|--------|--------------|
| PT-11 : Consentement | CAP-INT-09 | Vérification des droits |
| PT-10 : Confiance | CAP-INT-08 | Accès données financières |
| Loi 2014-038 | National | Cadre juridique exemption |

## Liens

- VS-03 : Protéger financièrement la population
- PT-01 : Échange interinstitutionnel
- PT-02 : Médiation intra-secteur
- PT-04 : Résolution identité bénéficiaire
- PT-10 : Confiance et autorisation
- PT-11 : Consentement
- PT-12 : Audit et traçabilité

## Références

- **VS-03 : Protéger financièrement la population** : Protéger financièrement la population face aux dépenses de santé (`00_caesn/01_value-streams/vs-03-financial-protection.md`)
- **PT-01 : Échange interinstitutionnel** : Profil technique national (`03_ptisn/03_profils/pt-01-echange-interinstitutionnel.md`)
- **PT-02 : Médiation intra-secteur** : Profil technique national (`03_ptisn/03_profils/pt-02-mediation-intra-secteur.md`)
- **PT-04 : Résolution identité bénéficiaire** : Profil technique national (`03_ptisn/03_profils/pt-04-resolution-identite-beneficiaire.md`)
- **PT-10 : Confiance et autorisation** : Profil technique national (`03_ptisn/03_profils/pt-10-confiance-authentification-autorisation.md`)
- **PT-11 : Consentement** : Profil technique national (`03_ptisn/03_profils/pt-11-consentement-bases-autorisation.md`)
- **PT-12 : Audit et traçabilité** : Profil technique national (`03_ptisn/03_profils/pt-12-audit-provenance-traçabilité.md`)
