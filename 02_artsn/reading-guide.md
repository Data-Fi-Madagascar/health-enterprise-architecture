---
title: Guide de lecture de l'ARTSN (niveau 3)
id: artsn-reading-guide
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: [artsn, lecture, niveau-3, guide]
---

# Guide de lecture de l'ARTSN (niveau 3)

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](reading-matrix.md).

---

## 1. Qu'est-ce que l'ARTSN ?

L'ARTSN (Architecture de Référence Technique de la Santé Numérique) est le **niveau 3** de la hiérarchie documentaire. Elle traduit les principes architecturaux du CAESN en **familles de patterns validées**, **standards techniques**, **contrats d'interfaces** et **règles d'homologation**.

**L'ARTSN précise le niveau technique** mais ne sélectionne pas de produits ni de configurations (ceci relève du PTISN).

```
Niveau 1 (CAESN)  →  Valeur, capabilités, gouvernance
Niveau 2 (CNISN)  →  Principes d'interopérabilité
Niveau 3 (ARTSN)  →  Patterns architecturaux, standards  ← CE DOCUMENT
Niveau 4 (PTISN)  →  Services, profils, produits candidats
```

---

## 2. Structure de l'ARTSN

L'ARTSN est organisée en **6 parties** + annexes :

| Partie | Contenu | Qui la lit |
|--------|---------|------------|
| [Fondations](00_fondations/index.md) | 6 fondations invariantes (F.1-F.6) | Tous |
| [Flux de valeur](01_flux-de-valeur/index.md) | VS-01 à VS-04 déclinés en exigences techniques | Architectes, intégrateurs |
| [Exigences contextuelles](02_exigences-contextuelles/index.md) | ENF-1 à ENF-5 | DEPSI, architectes |
| [Chapitres et patterns](03_chapitres/) | ART-0 à ART-11 (règles d'or et contrats) | Développeurs, intégrateurs |
| [Cartographie cible](04_cartographie-cible/index.md) | 6 couches + 2 axes verticaux | Architectes |
| [Dictionnaire de données](05_dictionnaire/index.md) | Sémantique universelle interministérielle | SIS, données |
| [Gouvernance](06_gouvernance/index.md) | Cycle de vie, versionnement, revue | Décideurs, gouvernance |

---

## 3. Parcours de lecture par profil

### 3.1 Décideur institutionnel

**Objectif :** Comprendre l'architecture technique cible et les enjeux d'homologation.

1. [Vue d'ensemble](index.md) — Rôle et positionnement
2. [Fondations](00_fondations/index.md) — Les 6 obligations fondamentales
3. [Gouvernance](06_gouvernance/index.md) — Processus de décision
4. [Table de maturité](07_annexes/a-table-de-maturite.md) — Statuts des chapitres

### 3.2 Architecte / intégrateur

**Objectif :** Concevoir une solution conforme à l'architecture de référence.

1. [Fondations](00_fondations/index.md) — Contraintes invariantes
2. [Cartographie cible](04_cartographie-cible/index.md) — Vue en couches
3. [Chapitres et patterns](03_chapitres/) — Patterns applicables
4. [Exigences contextuelles](02_exigences-contextuelles/index.md) — Contraintes nationales
5. [Flux de valeur](01_flux-de-valeur/index.md) — Exigences par flux

### 3.3 Développeur / intégrateur

**Objectif :** Implémenter les interfaces selon les patterns validés.

1. [Fondations](00_fondations/index.md) — §1 Résilience, §2 Souveraineté
2. [Chapitres et patterns](03_chapitres/) — ART-0 à ART-11
3. [Dictionnaire de données](05_dictionnaire/index.md) — Sémantique
4. [PTISN (niveau 4)](../03_ptisn/index.md) — Standards et profils

### 3.4 Partenaire technique / fournisseur

**Objectif :** Évaluer la conformité d'un produit ou service.

1. [Fondations](00_fondations/index.md) — §3 Éradication des silos, §4 Homologation
2. [Chapitres et patterns](03_chapitres/) — Contrats applicables
3. [Gouvernance](06_gouvernance/index.md) — Critères d'homologation
4. [Table de maturité](07_annexes/a-table-de-maturite.md) — Conditions de promotion

---

## 4. Les 6 fondations invariantes

| Fondation | Statut | Objet |
|-----------|--------|-------|
| F.1 — Résilience géographique | Stable | Immuabilité, idempotence, déduplication |
| F.2 — Souveraineté intersectorielle | Stable | Contrats d'égal à égal, versionnement sémantique |
| F.3 — Éradication des silos | Stable | Homologation obligatoire, alignement CAESN |
| F.4 — Homologation obligatoire | Stable | Processus de validation des solutions |
| F.5 — Protection et minimisation | Provisoire | Minimisation des données, résidence |
| F.6 — Observabilité | Provisoire | Traçabilité de bout en bout |

---

## 5. Les chapitres et patterns de référence

| Chapitre | Nom | Patterns couverts |
|----------|-----|-------------------|
| ART-0 | Accords de partage | Contrats interinstitutionnels |
| ART-1 | Intégration et ingestion | Connecteurs, adapters |
| ART-2 | Médiation et normalisation | Médiateur, transformation |
| ART-3 | Historisation événementielle | Event sourcing, CQRS |
| ART-4 | Référentiels de métadonnées | Registres, catalogues |
| ART-4a | Résolution d'identité | Client Registry, PIX |
| ART-4b | Bases d'autorisation | Consentement, RBAC |
| ART-4c | Éligibilité et couverture | Benefits Registry |
| ART-4d | Référentiel géospatial | Facility Registry |
| ART-5 | Cohérence et qualité | Réconciliation, validation |
| ART-6 | Analytique et restitution | Tableaux de bord, indicateurs |
| ART-7 | Sécurité et contrôle d'accès | Authentification, autorisation |
| ART-8 | Orchestration de processus | Workflow, BPM |
| ART-8a | Orchestration bornée | Processus limités |
| ART-8b | Modélisation en graphe | Flux relationnels |
| ART-8c | Agrégation par lot | Batch processing |
| ART-8d | Chorégraphie inter-institutionnelle | Échange décentralisé |
| ART-9 | Garanties transactionnelles | ACID, sagas |
| ART-10 | Logistique | Supply chain |
| ART-11 | Coordination intersectorielle | One Health |

---

## 6. Liens vers les autres niveaux

| Niveau | Document | Lien |
|--------|----------|------|
| 1 — CAESN | Cadre d'Architecture d'Entreprise | [../00_caesn/00_overview/index.md](../00_caesn/00_overview/index.md) |
| 2 — CNISN | Cadre National d'Interopérabilité | [../01_cnisn/index.md](../01_cnisn/index.md) |
| 4 — PTISN | Profils techniques d'implémentation | [../03_ptisn/index.md](../03_ptisn/index.md) |

---

## 7. Documents complémentaires

- [Matrice de lecture](reading-matrix.md) — Vue croisée parties × lecteurs
- [Glossaire](glossary.md) — Définitions des termes techniques
- [Acronymes](acronyms.md) — Liste des acronymes
- [Annexes](07_annexes/) — Table de maturité, glossaire des patterns, renvoi CAESN
