---
title: Guide de lecture du PTISN (niveau 4)
id: ptisn-reading-guide
domain: 03_ptisn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-13
owner: Équipes techniques des initiatives
tags: [ptisn, lecture, niveau-4, guide]
---

# Guide de lecture du PTISN (niveau 4)

## Pour qui lire ce document

**Niveau :** niveau 4 — Profils techniques d'implémentation de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](reading-matrix.md).

---

## 1. Qu'est-ce que le PTISN ?

Le PTISN (Profils techniques d'implémentation de la Santé Numérique) est le **niveau 4** de la hiérarchie documentaire du secteur santé numérique de Madagascar. Il traduit les capacités et principes des niveaux supérieurs en **spécifications techniques concrètes** pour chaque initiative numérique.

```
Niveau 1 (CAESN)  →  Valeur, capabilités, gouvernance
Niveau 2 (CNISN)  →  Principes d'interopérabilité, capacités requises
Niveau 3 (ARTSN)  →  Patterns architecturaux, standards techniques
Niveau 4 (PTISN)  →  Services, profils, standards, produits candidats
```

**Le PTISN est le seul niveau qui peut nommer explicitement des standards, profils et produits.**

---

## 2. Structure du PTISN

Le PTISN est organisé en **8 parties** + annexes :

| Partie | Contenu | Qui la lit |
|--------|---------|------------|
| [Préambule](00_introduction/index.md) | Positionnement, fonction, hiérarchie | Tous |
| [Règles d'utilisation](01_regles-utilisation/index.md) | Types de décisions, statuts, versionnement | Équipes techniques, DEPSI |
| [Topologie nationale cible](02_topologie-nationale-cible/index.md) | Architecture cible, couches, responsabilités | Architectes, intégrateurs |
| [Profils techniques](03_profils/) | 13 profils PT-01 à PT-13 | Développeurs, fournisseurs |
| [Matrice d'alignement](04_matrice-alignement/index.md) | Mapping capacités CNISN ↔ profils ↔ ART | DEPSI, validateurs |
| [Profil d'initiative](05_profil-initiative/index.md) | Template pour chaque initiative | Équipes projet |
| [Gouvernance](06_gouvernance/index.md) | Processus d'adoption, critères, homologation | Décideurs, gouvernance |
| [Conclusion](07_conclusion/index.md) | Synthèse, principles | Tous |

---

## 3. Parcours de lecture par profil

### 3.1 Décideur institutionnel

**Objectif :** Comprendre le rôle du PTISN dans la hiérarchie et les enjeux de gouvernance.

1. [Préambule](00_introduction/index.md) — §1 Fonction du PTISN
2. [Gouvernance](06_gouvernance/index.md) — §1 Instance porteuse, §4 Homologation
3. [Conclusion](07_conclusion/index.md)

### 3.2 Direction métier / programme

**Objectif :** Comprendre comment une initiative s'inscrit dans le cadre technique.

1. [Préambule](00_introduction/index.md) — §2 Position hiérarchique
2. [Règles d'utilisation](01_regles-utilisation/index.md) — §4 Applicabilité
3. [Profil d'initiative](05_profil-initiative/index.md) — Template à produire

### 3.3 Équipe technique / développeur

**Objectif :** Implémenter une initiative conforme aux standards nationaux.

1. [Préambule](00_introduction/index.md) — Lecture complète
2. [Règles d'utilisation](01_regles-utilisation/index.md) — Lecture complète
3. [Topologie nationale cible](02_topologie-nationale-cible/index.md) — Comprendre l'architecture cible
4. [Profils techniques](03_profils/) — Consulter les profils applicables (PT-XX)
5. [Matrice d'alignement](04_matrice-alignement/index.md) — Vérifier l'alignement
6. [Profil d'initiative](05_profil-initiative/index.md) — Produire sa fiche

### 3.4 Architecte / intégrateur

**Objectif :** Évaluer et sélectionner les standards et profils pour une initiative.

1. [Topologie nationale cible](02_topologie-nationale-cible/index.md)
2. [Profils techniques](03_profils/) — Tous les profils
3. [Matrice d'alignement](04_matrice-alignement/index.md)
4. [Gouvernance](06_gouvernance/index.md) — §2 Processus d'adoption, §3 Critères

### 3.5 Partenaire technique / fournisseur

**Objectif :** Évaluer la conformité d'un produit ou service.

1. [Règles d'utilisation](01_regles-utilisation/index.md) — §2 Statuts, §3 Versionnement
2. [Profils techniques](03_profils/) — Profils pertinents
3. [Gouvernance](06_gouvernance/index.md) — §4 Homologation d'un produit

---

## 4. Catalogue des profils techniques

Les 13 profils couvrent l'ensemble des capacités d'interopérabilité du CNISN :

| Profil | Capacité CNISN | Description |
|--------|----------------|-------------|
| [PT-01](03_profils/pt-01-echange-interinstitutionnel.md) | CAP-INT-03 | Échange interinstitutionnel (X-Road) |
| [PT-02](03_profils/pt-02-mediation-intra-secteur.md) | CAP-INT-03 | Médiation intra-secteur |
| [PT-03](03_profils/pt-03-catalogue-services-registre-contrats.md) | CAP-INT-06 | Catalogue de services et registre de contrats |
| [PT-04](03_profils/pt-04-resolution-identite-beneficiaire.md) | CAP-INT-01 | Résolution d'identité bénéficiaire |
| [PT-05](03_profils/pt-05-registre-professionnels.md) | CAP-INT-02 | Registre des professionnels |
| [PT-06](03_profils/pt-06-referentiel-structures-services.md) | CAP-INT-04 | Référentiel des structures et services |
| [PT-07](03_profils/pt-07-terminologie-codification.md) | CAP-INT-05 | Terminologie et codification |
| [PT-08](03_profils/pt-08-echange-donnees-agregees.md) | CAP-INT-07 | Échange de données agrégées |
| [PT-09](03_profils/pt-09-analytique-exposition-donnees.md) | CAP-INT-07 | Analytique et exposition de données |
| [PT-10](03_profils/pt-10-confiance-authentification-autorisation.md) | CAP-INT-08 | Confiance, authentification, autorisation |
| [PT-11](03_profils/pt-11-consentement-bases-autorisation.md) | CAP-INT-09 | Consentement et bases d'autorisation |
| [PT-12](03_profils/pt-12-audit-provenance-traçabilité.md) | CAP-INT-10 | Audit, provenance, traçabilité |
| [PT-13](03_profils/pt-13-qualite-reconciliation.md) | CAP-INT-11 | Qualité et réconciliation des données |

---

## 5. Statuts des décisions techniques

Chaque standard, profil ou produit porteur l'un des statuts suivants :

| Statut | Quand consulter |
|--------|-----------------|
| **À instruire** | Besoin identifié, pas encore de solution |
| **Candidat** | En évaluation |
| **Recommandé** | Nouvelles initiatives — privilégier |
| **Retenu pour pilote** | Expérimentation en cours |
| **Retenu nationalement** | Choix validé pour le pays |
| **Homologué** | Conformité démontrée |
| **Déprécié** | Compatibilité temporaire |
| **Retiré** | Ne plus utiliser |

---

## 6. Liens vers les autres niveaux

| Niveau | Document | Lien |
|--------|----------|------|
| 1 — CAESN | Cadre d'Architecture d'Entreprise | [../00_caesn/00_overview/index.md](../00_caesn/00_overview/index.md) |
| 2 — CNISN | Cadre National d'Interopérabilité | [../01_cnisn/index.md](../01_cnisn/index.md) |
| 3 — ARTSN | Architecture de Référence Technique | [../02_artsn/index.md](../02_artsn/index.md) |
| — | Portefeuille national d'initiatives | [../00_caesn/06_portfolio/index.md](../00_caesn/06_portfolio/index.md) |
| — | Référentiel des profils | [../referentiel/profils/](../referentiel/profils/) |

---

## 7. Documents complémentaires

- [Matrice de lecture](reading-matrix.md) — Vue croisée profils × lecteurs
- [Glossaire du PTISN](glossary.md) — Définitions des termes techniques
- [Acronymes du PTISN](acronyms.md) — Liste des acronymes
- [Annexes](08_annexes/) — Supports complémentaires
