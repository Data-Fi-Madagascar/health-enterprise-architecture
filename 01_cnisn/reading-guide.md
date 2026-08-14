---
title: Guide de lecture du CNISN (niveau 2)
id: cnisn-reading-guide
domain: 01_cnisn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: [cnisn, lecture, niveau-2, guide]
---

# Guide de lecture du CNISN (niveau 2)

## Pour qui lire ce document

**Niveau :** niveau 2 — Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](reading-matrix.md).

---

## 1. Qu'est-ce que le CNISN ?

Le CNISN (Cadre National d'Interopérabilité de la Santé Numérique) est le **niveau 2** de la hiérarchie documentaire. Il définit les principes, capacités et règles de gouvernance applicables aux échanges de données et de services impliquant le secteur santé.

**Le CNISN fixe :**
- Les principes opposables
- Les responsabilités institutionnelles
- Les capacités nationales nécessaires
- Les règles applicables aux données et services partagés
- Les mécanismes de conformité

**Le CNISN ne sélectionne :**
- Aucun produit
- Aucun fournisseur
- Aucune technologie
- Aucune plateforme particulière

```
Niveau 1 (CAESN)  →  Valeur, capabilités, gouvernance
Niveau 2 (CNISN)  →  Principes d'interopérabilité  ← CE DOCUMENT
Niveau 3 (ARTSN)  →  Patterns architecturaux, standards
Niveau 4 (PTISN)  →  Services, profils, produits candidats
```

---

## 2. Structure du CNISN

Le CNISN est organisé en **8 parties** :

| Partie | Contenu | Qui la lit |
|--------|---------|------------|
| [Préambule](00_introduction/index.md) | Positionnement, portée, articulation | Tous |
| [Principes](01_principes/index.md) | 25 principes (catégories A-F) | DEPSI, architectes |
| [Capacités](02_capacites/index.md) | 12 capacités d'interopérabilité | DEPSI, équipes techniques |
| [Gouvernance](03_gouvernance/index.md) | Instances, processus, responsabilités | Décideurs, gouvernance |
| [Conformité](04_conformite/index.md) | Critères, tests, homologation | Équipes techniques |
| [Trajectoire](05_trajectoire/index.md) | Feuille de route, jalons | Décideurs, planificateurs |
| [Indicateurs](06_indicateurs/index.md) | Métriques, suivi | SIS, suivi-évaluation |
| [Conclusion](07_conclusion/index.md) | Synthèse | Tous |

---

## 3. Parcours de lecture par profil

### 3.1 Décideur institutionnel

**Objectif :** Comprendre les enjeux d'interopérabilité et les responsabilités.

1. [Préambule](00_introduction/index.md) — §1 Nature du cadre
2. [Gouvernance](03_gouvernance/index.md) — Instances et responsabilités
3. [Trajectoire](05_trajectoire/index.md) — Feuille de route
4. [Conclusion](07_conclusion/index.md)

### 3.2 Direction métier / programme

**Objectif :** Comprendre les règles applicables aux échanges de données.

1. [Préambule](00_introduction/index.md) — §4 Portée
2. [Principes](01_principes/index.md) — Catégories A et B
3. [Capacités](02_capacites/index.md) — Capacités pertinentes

### 3.3 Équipe technique / DEPSI

**Objectif :** Implémenter des échanges conformes au CNISN.

1. [Préambule](00_introduction/index.md) — Lecture complète
2. [Principes](01_principes/index.md) — Lecture complète (25 principes)
3. [Capacités](02_capacites/index.md) — 12 capacités
4. [Conformité](04_conformite/index.md) — Critères et tests
5. [ARTSN (niveau 3)](../02_artsn/index.md) — Patterns techniques
6. [PTISN (niveau 4)](../03_ptisn/index.md) — Standards et profils

### 3.4 Partenaire technique

**Objectif :** Évaluer la conformité d'une solution.

1. [Principes](01_principes/index.md) — Catégories D et E
2. [Capacités](02_capacites/index.md) — Capacités couvertes
3. [Conformité](04_conformite/index.md) — Preuves requises

---

## 4. Les 25 principes du CNISN

Les principes sont organisés en **6 catégories** :

| Catégorie | Principes | Objet |
|-----------|-----------|-------|
| **A** — Autorité et données de référence | P-INT-01 à P-INT-04 | Sources autoritatives, résolution, copies, historisation |
| **B** — Contractualisation | P-INT-05 à P-INT-09 | Contrats, versionnement, responsabilités, catalogues |
| **C** — Gouvernance interinstitutionnelle | P-INT-10 à P-INT-13 | Accords, arbitrage, dérogations |
| **D** — Sécurité et autorisation | P-INT-14 à P-INT-18 | Bases d'autorisation, finalité, résidence, minimisation |
| **E** — Neutralité et réversibilité | P-INT-19 à P-INT-22 | Neutralité technologique, portabilité, progressivité |
| **F** — Conformité | P-INT-23 à P-INT-25 | Preuves, applicabilité, réévaluation |

---

## 5. Les 12 capacités d'interopérabilité

| Capacité | Famille | Description |
|----------|---------|-------------|
| CAP-INT-01 | Référentiels et identités | Résolution d'identité du bénéficiaire |
| CAP-INT-02 | Référentiels et identités | Registre des professionnels de santé |
| CAP-INT-03 | Échange et médiation | Échange interinstitutionnel et médiation |
| CAP-INT-04 | Référentiels et identités | Référentiel des structures et services |
| CAP-INT-05 | Référentiels et identités | Terminologie et codification |
| CAP-INT-06 | Échange et médiation | Catalogue de services et registre de contrats |
| CAP-INT-07 | Données analytiques | Échange de données agrégées et analytique |
| CAP-INT-08 | Confiance et sécurité | Authentification et autorisation |
| CAP-INT-09 | Confiance et sécurité | Consentement et bases d'autorisation |
| CAP-INT-10 | Confiance et sécurité | Audit, provenance, traçabilité |
| CAP-INT-11 | Qualité et conformité | Qualité et réconciliation des données |
| CAP-INT-12 | Qualité et conformité | Conformité et homologation |

---

## 6. Liens vers les autres niveaux

| Niveau | Document | Lien |
|--------|----------|------|
| 1 — CAESN | Cadre d'Architecture d'Entreprise | [../00_caesn/00_overview/index.md](../00_caesn/00_overview/index.md) |
| 3 — ARTSN | Architecture de Référence Technique | [../02_artsn/index.md](../02_artsn/index.md) |
| 4 — PTISN | Profils techniques d'implémentation | [../03_ptisn/index.md](../03_ptisn/index.md) |

---

## 7. Documents complémentaires

- [Matrice de lecture](reading-matrix.md) — Vue croisée parties × lecteurs
- [Glossaire](glossary.md) — Définitions des termes d'interopérabilité
- [Acronymes](acronyms.md) — Liste des acronymes
- [Annexes](08_annexes/) — Articulation ARTSN, supports complémentaires
