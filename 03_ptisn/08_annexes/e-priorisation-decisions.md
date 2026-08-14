---
title: "Priorisation et calendrier — 5 premières décisions PTISN"
id: ptisn-priorisation-decisions
domain: 03_ptisn
version: "0.1.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: [ptisn, decisions, priorisation, calendrier]
---

# Priorisation et calendrier — 5 premières décisions PTISN

## Pour qui lire ce document

**Niveau :** niveau 4 — Profils techniques d'implémentation de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

## Contexte

Le PTISN identifie **18 décisions à instruire** (Annexe B). Ces décisions conditionnent le déploiement des profils techniques et l'opérationnalisation du cadre d'interopérabilité. Leur priorisation est essentielle pour avancer de façon ordonnée.

## Critères de priorisation

| Critère | Poids |
|---------|-------|
| **Impact sur les initiatives en cours** | 30% |
| **Dépendance d'autres décisions** | 25% |
| **Faisabilité technique** | 20% |
| **Conformité aux obligations internationales** | 15% |
| **Disponibilité des ressources** | 10% |

## 5 premières décisions prioritaires

### Décision 1 : Modèle national d'identité santé du bénéficiaire

| Champ | Valeur |
|-------|--------|
| **Priorité** | 🔴 1 |
| **Impact** | Critique — bloque la continuité des soins et la protection financière |
| **Dépendances** | Aucune (décision fondatrice) |
| **Échéance** | T4 2026 |
| **Responsable** | DEPSI + Direction des Systèmes d'Information |
| **Livrable** | Note de cadrage validée par le Comité National |

**Pourquoi en priorité :**
- Conditionne PT-04 (résolution d'identité)
- Impacte tous les flux de valeur (VS-01, VS-03)
- Nécessaire pour le consentement (PT-11)

---

### Décision 2 : Version FHIR nationale de référence

| Champ | Valeur |
|-------|--------|
| **Priorité** | 🔴 2 |
| **Impact** | Élevé — standardise tous les échanges de données |
| **Dépendances** | Aucune |
| **Échéance** | T4 2026 |
| **Responsable** | DEPSI + Directions techniques |
| **Livrable** | ADR documentant le choix de la version FHIR |

**Pourquoi en priorité :**
- Standardise les contrats d'interface
- Conditionne l'homologation des solutions
- Aligné avec les standards internationaux (OMS, IHE)

---

### Décision 3 : Profil national de consentement

| Champ | Valeur |
|-------|--------|
| **Priorité** | 🔴 3 |
| **Impact** | Critique — bloque tout partage de données patients |
| **Dépendances** | Décision 1 (identité santé) |
| **Échéance** | T1 2027 |
| **Responsable** | DEPSI + Direction Juridique |
| **Livrable** | Profil PT-11 complété |

**Pourquoi en priorité :**
- Obligation légale (protection des données de santé)
- Bloque PT-01 (échange interinstitutionnel)
- Nécessaire pour la conformité au cadre juridique

---

### Décision 4 : Produit du service terminologique

| Champ | Valeur |
|-------|--------|
| **Priorité** | 🟡 4 |
| **Impact** | Élevé — conditionne la normalisation sémantique |
| **Dépendances** | Décision 2 (version FHIR) |
| **Échéance** | T1 2027 |
| **Responsable** | DEPSI + Directions cliniques |
| **Livrable** | Cahier des charges du service terminologique |

**Pourquoi en priorité :**
- Nécessaire pour ART-2 (médiation et normalisation)
- Conditionne l'interopérabilité sémantique
- Impacte le dictionnaire de données

---

### Décision 5 : Produit du catalogue des services

| Champ | Valeur |
|-------|--------|
| **Priorité** | 🟡 5 |
| **Impact** | Moyen — facilite la découverte et l'intégration |
| **Dépendances** | Décision 2 (version FHIR) |
| **Échéance** | T2 2027 |
| **Responsable** | DEPSI |
| **Livrable** | Spécification du catalogue de services |

**Pourquoi en priorité :**
- Supporte CAP-INT-06 (catalogue de services)
- Facilite l'intégration des nouvelles initiatives
- Améliore la visibilité de l'écosystème

## Calendrier prévisionnel

```
2026                    2027
T3      T4      T1      T2      T3      T4
│       │       │       │       │       │
├───────┼───────┼───────┼───────┼───────┤
│       │       │       │       │       │
│  D1───┼───────┤       │       │       │  Identité santé
│       │       │       │       │       │
│  D2───┼───────┤       │       │       │  Version FHIR
│       │       │       │       │       │
│       │  D3───┼───────┤       │       │  Consentement
│       │       │       │       │       │
│       │  D4───┼───────┤       │       │  Terminologie
│       │       │       │       │       │
│       │       │  D5───┼───────┤       │  Catalogue
│       │       │       │       │       │
└───────┴───────┴───────┴───────┴───────┘
```

## Prochaines étapes

1. **Valider la priorisation** avec les équipes techniques
2. **Lancer la Décision 1** (identité santé) — T3 2026
3. **Documenter via des ADR** chaque décision validée
4. **Communiquer** aux parties prenantes

## Liens

- [Annexe B — Décisions à instruire](./b-decisions-instruire.md)
- [PT-04 — Résolution d'identité](../../referentiel/profils/pt-04.md)
- [PT-11 — Consentement](../../referentiel/profils/pt-11.md)
- [CAESN — Décisions](../../00_caesn/08_decisions/index.md)
