---
title: Guide de lecture du CAESN (niveau 1)
id: caesn-reading-guide
domain: 00_caesn
version: "1.0.0"
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

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

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
| Fondements | Ancrage stratégique et normatif | Tous |
| Modèle de valeur | Bénéficiaires, dimensions de valeur | Décideurs, directions métier |
| Flux de valeur | Les 4 flux de valeur nationaux (VS-01 à VS-04) | Décideurs, directions métier |
| Principes | Principes transversaux (PA) et de domaine (PD) | Architectes, DEPSI |
| Capabilités | Catalogue CAP-01 à CAP-16, maturité | Tous |
| Données | Principes DA, domaines de données | SIS, données |
| Application | Principes AA, paysage applicatif | Équipes techniques |
| Portefeuille | Registre des initiatives | Décideurs, directions métier |
| Gouvernance | Comité National, BRV | Décideurs |
| Décisions | Architecture Decision Records | Architectes |
| Normes | Standards et règles d'homologation | DEPSI, techniques |
| Annexes | Matrice de lecture, glossaire | Tous |

---

## 3. Parcours de lecture par profil

### 3.1 Décideur institutionnel

**Objectif :** Comprendre la vision stratégique et les enjeux de gouvernance.

1. Vue d'ensemble — Objet, portée, hiérarchie
2. Fondements — Ancrage stratégique
3. Modèle de valeur — Bénéficiaires et dimensions
4. Flux de valeur — Les 4 flux nationaux
5. Gouvernance — Instances et responsabilités
6. Portefeuille — Registre des initiatives

### 3.2 Direction métier / programme

**Objectif :** Comprendre comment une initiative s'inscrit dans le cadre.

1. Vue d'ensemble — Positionnement
2. Modèle de valeur — Valeur produite
3. Flux de valeur — Flux pertinent
4. Capabilités — Capacités couvertes
5. Portefeuille — Fiche d'initiative

### 3.3 Équipe technique / DEPSI

**Objectif :** Implémenter selon les principes et standards du cadre.

1. Vue d'ensemble — Lecture complète
2. Principes — Principes PA et PD
3. Capabilités — Catalogue complet
4. Données — Domaines de données
5. Application — Paysage applicatif
6. Normes — Standards à respecter
7. ARTSN (niveau 3) — Patterns techniques

### 3.4 Partenaire technique / financier

**Objectif :** Évaluer l'alignement d'une initiative avec le cadre.

1. Vue d'ensemble — Objet et portée
2. Modèle de valeur — Valeur attendue
3. Flux de valeur — Flux couverts
4. Capabilités — Maturité cible
5. Gouvernance — Processus de validation

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
| 2 — CNISN | Cadre National d'Interopérabilité | ../01_cnisn/index.md |
| 3 — ARTSN | Architecture de Référence Technique | ../02_artsn/index.md |
| 4 — PTISN | Profils techniques d'implémentation | ../03_ptisn/index.md |

---

## 7. Documents complémentaires

- Matrice de lecture — Vue croisée sections × lecteurs
- Glossaire — Définitions des termes
- Acronymes — Liste des acronymes
- Annexes — Supports complémentaires

## Références

- **matrice de lecture** — Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Fondements** — Fondements stratégiques et normatifs (`00_caesn/00_overview/foundations.md`)
- **Modèle de valeur** — Modèle national de valeur (`00_caesn/00_overview/value-model.md`)
- **Vue d'ensemble** — Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) (`00_caesn/00_overview/index.md`)
- **ARTSN (niveau 3)** — Architecture de Référence Technique de la Santé Numérique (ARTSN) (`02_artsn/index.md`)
- **../01_cnisn/index.md** — Cadre National d'Interopérabilité de la Santé Numérique (CNISN) (`01_cnisn/index.md`)
- **../02_artsn/index.md** — Architecture de Référence Technique de la Santé Numérique (ARTSN) (`02_artsn/index.md`)
- **../03_ptisn/index.md** — Profils techniques d'implémentation de la Santé Numérique (PTISN) (`03_ptisn/index.md`)
- **Matrice de lecture** — Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Glossaire** — Glossaire (`00_caesn/10_annexes/glossary.md`)
- **Acronymes** — Acronymes et abréviations (`00_caesn/10_annexes/acronyms.md`)
