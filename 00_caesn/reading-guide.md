---
title: Guide de lecture du CAESN (niveau 1)
id: caesn-reading-guide
domain: 00_caesn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-13
owner: Bureau de Réalisation de la Valeur
tags: [caesn, lecture, niveau-1, guide]
---

# Guide de lecture du CAESN (niveau 1)

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ◐ |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](reading-matrix.md).

---

## 1. Qu'est-ce que le CAESN ?

Le CAESN (Cadre d'Architecture d'Entreprise de la Santé Numérique) est le **niveau 1** de la hiérarchie documentaire du secteur santé numérique de Madagascar. Il définit les principes, méthodes et mécanismes de gouvernance pour toute initiative numérique du secteur santé.

**Le CAESN est le document fondateur** qui fixe :
1. La **valeur** que le système de santé doit produire pour la population
2. Les **capabilités** nécessaires pour produire cette valeur
3. Les **règles de gouvernance** pour les investissements numériques

```
Niveau 1 (CAESN)  →  Valeur, capabilités, gouvernance  ← CE DOCUMENT
Niveau 2 (CNISN)  →  Principes d'interopérabilité
Niveau 3 (ARTSN)  →  Patterns architecturaux, standards
Niveau 4 (PTISN)  →  Services, profils, produits candidats
```

---

## 2. Structure du CAESN

Le CAESN est organisé en **11 domaines** :

| Domaine | Contenu | Qui le lit |
|---------|---------|------------|
| [Fondements](00_overview/foundations.md) | Ancrage stratégique et normatif | Tous |
| [Modèle de valeur](00_overview/value-model.md) | Bénéficiaires, dimensions de valeur | Décideurs, directions métier |
| [Flux de valeur](01_value-streams/) | Les 4 flux de valeur nationaux (VS-01 à VS-04) | Décideurs, directions métier |
| [Principes](02_principles/) | Principes transversaux (PA) et de domaine (PD) | Architectes, DEPSI |
| [Capabilités](03_capabilities/) | Catalogue CAP-01 à CAP-16, maturité | Tous |
| [Données](04_data/) | Principes DA, domaines de données | SIS, données |
| [Application](05_application/) | Principes AA, paysage applicatif | Équipes techniques |
| [Portefeuille](06_portfolio/) | Registre des initiatives | Décideurs, directions métier |
| [Gouvernance](07_governance/) | Comité National, BRV | Décideurs |
| [Décisions](08_decisions/) | Architecture Decision Records | Architectes |
| [Normes](09_standards/) | Standards et règles d'homologation | DEPSI, techniques |
| [Annexes](10_annexes/) | Matrice de lecture, glossaire | Tous |

---

## 3. Parcours de lecture par profil

### 3.1 Décideur institutionnel

**Objectif :** Comprendre la vision stratégique et les enjeux de gouvernance.

1. [Vue d'ensemble](00_overview/index.md) — Objet, portée, hiérarchie
2. [Fondements](00_overview/foundations.md) — Ancrage stratégique
3. [Modèle de valeur](00_overview/value-model.md) — Bénéficiaires et dimensions
4. [Flux de valeur](01_value-streams/) — Les 4 flux nationaux
5. [Gouvernance](07_governance/) — Instances et responsabilités
6. [Portefeuille](06_portfolio/) — Registre des initiatives

### 3.2 Direction métier / programme

**Objectif :** Comprendre comment une initiative s'inscrit dans le cadre.

1. [Vue d'ensemble](00_overview/index.md) — Positionnement
2. [Modèle de valeur](00_overview/value-model.md) — Valeur produite
3. [Flux de valeur](01_value-streams/) — Flux pertinent
4. [Capabilités](03_capabilities/) — Capacités couvertes
5. [Portefeuille](06_portfolio/) — Fiche d'initiative

### 3.3 Équipe technique / DEPSI

**Objectif :** Implémenter selon les principes et standards du cadre.

1. [Vue d'ensemble](00_overview/index.md) — Lecture complète
2. [Principes](02_principles/) — Principes PA et PD
3. [Capabilités](03_capabilities/) — Catalogue complet
4. [Données](04_data/) — Domaines de données
5. [Application](05_application/) — Paysage applicatif
6. [Normes](09_standards/) — Standards à respecter
7. [ARTSN (niveau 3)](../02_artsn/index.md) — Patterns techniques

### 3.4 Partenaire technique / financier

**Objectif :** Évaluer l'alignement d'une initiative avec le cadre.

1. [Vue d'ensemble](00_overview/index.md) — Objet et portée
2. [Modèle de valeur](00_overview/value-model.md) — Valeur attendue
3. [Flux de valeur](01_value-streams/) — Flux couverts
4. [Capabilités](03_capabilities/) — Maturité cible
5. [Gouvernance](07_governance/) — Processus de validation

---

## 4. Catalogue des capabilités

Les 16 capabilités couvrent l'ensemble du système de santé :

| Capacité | Description |
|----------|-------------|
| CAP-01 | Accès aux soins |
| CAP-02 | Orientation et tri |
| CAP-03 | Coordination des soins |
| CAP-04 | Prévention et promotion |
| CAP-05 | Surveillance sanitaire |
| CAP-06 | Riposte sanitaire |
| CAP-07 | Protection financière |
| CAP-08 | Gestion des ressources |
| CAP-09 | Qualité des données |
| CAP-10 | Partage des données |
| CAP-11 | Sécurité et confidentialité |
| CAP-12 | Identification des bénéficiaires |
| CAP-13 | Identification des structures |
| CAP-14 | Identification des professionnels |
| CAP-15 | Référentiels partagés |
| CAP-16 | Services analytiques |

---

## 5. Flux de valeur nationaux

| Flux | Nom | Objectif |
|------|-----|----------|
| VS-01 | Accès aux soins | Assurer l'entrée et la continuité des soins |
| VS-02 | Protection contre les risques | Prévenir, détecter et répondre aux risques sanitaires |
| VS-03 | Protection financière | Garantir l'accès aux soins sans obstacle financier |
| VS-04 | Pilotage du système | Diriger et améliorer le système de santé |

---

## 6. Liens vers les autres niveaux

| Niveau | Document | Lien |
|--------|----------|------|
| 2 — CNISN | Cadre National d'Interopérabilité | [../01_cnisn/index.md](../01_cnisn/index.md) |
| 3 — ARTSN | Architecture de Référence Technique | [../02_artsn/index.md](../02_artsn/index.md) |
| 4 — PTISN | Profils techniques d'implémentation | [../03_ptisn/index.md](../03_ptisn/index.md) |

---

## 7. Documents complémentaires

- [Matrice de lecture](reading-matrix.md) — Vue croisée sections × lecteurs
- [Glossaire](10_annexes/glossary.md) — Définitions des termes
- [Acronymes](10_annexes/acronyms.md) — Liste des acronymes
- [Annexes](10_annexes/) — Supports complémentaires
