---
title: "Cas d'usage — Remontée de données et pilotage du système"
id: ptisn-cas-usage-pilotage
domain: 03_ptisn
version: "0.1"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: ["ptisn", "niveau-4", "cas-usage", "pilotage", "rapports", "performance", "vs-04"]
---

# Cas d'usage — Remontée de données et pilotage du système (VS-04)

## Pour qui lire ce document

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| Partenaires techniques et financiers | ◐ |

---

## Objectif

Ce document montre comment les **profils techniques existants** composent pour couvrir le cycle complet de pilotage du système de santé : collecte de données, agrégation, analyse, tableaux de bord, prise de décision et redevabilité.

## Principe architectural

Le pilotage est un **cas d'usage transversal** qui consomme les profils de données agrégées, d'analytique, de confiance et d'audit. Il irrigue tous les autres flux de valeur.

```
┌─────────────────────────────────────────────────────────────────────┐
│              PILOTAGE DU SYSTÈME (VS-04)                           │
│  Collecte → Agrégation → Analyse → Décision → Redevabilité        │
└──────┬──────────┬──────────┬──────────┬──────────┬─────────────────┘
       │          │          │          │          │
       ▼          ▼          ▼          ▼          ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    PROFILS TECHNIQUES                              │
│  PT-08    │  PT-09   │  PT-13  │  PT-01  │  PT-12  │  PT-10     │
│  Données  │Analytique│ Qualité │ Échange │ Audit   │ Confiance  │
│  agrégées │          │         │         │         │            │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Scénario — Cycle complet de pilotage

### Phase 1 — Collecte de données opérationnelles (VS-01/02/03 → VS-04)

**Objectif** : Alimenter le système analytique avec les données provenant de tous les points de service.

```
Formations sanitaires    RIS (district)    Médiation (PT-02)    Entrepôt (CMP-03)
        │                     │                   │                     │
        │ Données cliniques   │                   │                     │
        │ terrain             │                   │                     │
        │────────────────────▶│  Consolidation    │                     │
        │                     │  district         │                     │
        │                     │──────────────────▶│  ETL national       │
        │                     │                   │────────────────────▶│
        │                     │                   │                     │
Programmes (BPC,     Médiation (PT-02)  Entrepôt (CMP-03)
 vaccination, etc.)        │                   │
        │                  │                   │
        │ Données agrégées │                   │
        │ (mADX)           │                   │
        │─────────────────▶│──────────────────▶│
```

**Profils mobilisés** :

| Profil | Rôle |
|--------|------|
| **PT-08** | Échange de données agrégées (mADX) |
| **PT-02** | Médiation sémantique (formatage) |
| **PT-13** | Qualité et réconciliation des données |

---

### Phase 2 — Agrégation et analyse (EV-25/EV-26)

**Objectif** : Consolider les données, calculer les indicateurs, alimenter les tableaux de bord.

```
Entrepôt (CMP-03)     Moteur analytique (CMP-04)    Tableaux de bord (CMP-01)
        │                     │                            │
        │ Données              │                            │
        │ consolidées          │                            │
        │────────────────────▶│  Calcul indicateurs        │
        │                     │  (3 modèles IA)            │
        │                     │───────────────────────────▶│
        │                     │                            │
        │  Résultats          │  Dashboard national        │
        │◀────────────────────│◀───────────────────────────│
```

**Profils mobilisés** :

| Profil | Rôle |
|--------|------|
| **PT-09** | Analytique et exposition des données |
| **PT-13** | Qualité et réconciliation |
| **PT-08** | Échange de données agrégées |
| **PT-12** | Audit des processus analytiques |

**Données échangées** :
- `Indicator` (FHIR) — indicateurs calculés
- `Dashboard` — tableaux de bord décisionnels
- `Report` — rapports DHIS2

---

### Phase 3 — Tableaux de bord et alertes (CMP-01/CMP-02)

**Objectif** : Exposer les données de performance aux décideurs et déclencher des alertes en cas de dérive.

```
Moteur analytique (CMP-04)    Centre de commande (CMP-02)
        │                            │
        │ Indicateur                 │
        │ < seuil                    │
        │───────────────────────────▶│
        │                            │  Alerte dérive
        │                            │──────────────────▶ Direction
        │                            │                   technique
        │                            │
        │  Validation alerte         │
        │◀───────────────────────────│
```

**Profils mobilisés** :

| Profil | Rôle |
|--------|------|
| **PT-10** | Confiance (RBAC tableaux de bord) |
| **PT-12** | Audit des consultations de dashboards |

---

### Phase 4 — Rapports et redevabilité (EV-27)

**Objectif** : Produire les rapports publics et alimenter les instances de redevabilité (Parlement, partenaires).

```
Entrepôt (CMP-03)     Moteur analytique (CMP-04)    Rapports publics
        │                     │                            │
        │ Données annuelles   │                            │
        │ consolidées         │                            │
        │────────────────────▶│  Production rapports       │
        │                     │  annuels de performance    │
        │                     │───────────────────────────▶│
        │                     │                            │
        │                     │  Rapport validé            │
        │                     │◀───────────────────────────│
        │                     │                            │
        │                     │  Publication               │
        │                     │───────────────────────────▶ Parlement
        │                     │                           Partenaires
        │                     │                           Société civile
```

**Profils mobilisés** :

| Profil | Rôle |
|--------|------|
| **PT-09** | Analytique et restitution |
| **PT-12** | Audit trail (traçabilité rapports) |
| **PT-01** | Échange interinstitutionnel (transmission rapports) |

---

### Phase 5 — Amélioration continue (EV-28)

**Objectif** : Utiliser les leçons tirées pour améliorer l'architecture et les processus.

```
Comité de pilotage     Bureau de réalisation     Équipe architecture
        │                     │                          │
        │ Recommandations      │                          │
        │ d'amélioration       │                          │
        │────────────────────▶│  Traduction en            │
        │                     │  modifications ARTSN      │
        │                     │─────────────────────────▶│
        │                     │                          │
        │                     │  Mise à jour              │
        │                     │  référentiel              │
        │                     │◀─────────────────────────│
```

---

## Matrice de composition

| Étape | PT-01 | PT-02 | PT-08 | PT-09 | PT-10 | PT-12 | PT-13 |
|-------|-------|-------|-------|-------|-------|-------|-------|
| Collecte (VS → VS-04) | — | ● | ● | — | — | ● | ● |
| Agrégation/Analyse (EV-25/26) | — | — | ● | ● | — | ● | ● |
| Alertes (CMP-02) | — | — | — | ● | ● | ● | — |
| Rapports (EV-27) | ● | — | — | ● | — | ● | — |
| Amélioration (EV-28) | — | — | — | ○ | — | ● | — |

---

## Exigences transversales

| Exigence | Source | Applicable à |
|----------|--------|--------------|
| ART-5 — Qualité des données | ART-5 | Toutes les phases |
| PT-10 — Confiance | CAP-INT-08 | Accès tableaux de bord sensibles |
| PT-13 — Qualité et réconciliation | CAP-INT-11 | Agrégation multi-sources |

---

## Liens

- [VS-04 — Piloter, coordonner et améliorer la performance](../../00_caesn/01_value-streams/vs-04-system-steering.md)
- [PT-08 — Échange données agrégées](../03_profils/pt-08-echange-donnees-agregees.md)
- [PT-09 — Analytique exposition données](../03_profils/pt-09-analytique-exposition-donnees.md)
- [PT-10 — Confiance et autorisation](../03_profils/pt-10-confiance-authentification-autorisation.md)
- [PT-12 — Audit et traçabilité](../03_profils/pt-12-audit-provenance-traçabilité.md)
- [PT-13 — Qualité et réconciliation](../03_profils/pt-13-qualite-reconciliation.md)
