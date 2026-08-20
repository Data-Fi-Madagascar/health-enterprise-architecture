---

title: Guide de lecture du CNISN (niveau 2)
id: cnisn-reading-guide
domain: 01_cnisn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-18
owner: DEPSI
tags: ["cnisn", "lecture", "niveau-2", "guide"]
---

# Guide de lecture du CNISN (niveau 2)

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## 1. Qu'est-ce que le CNISN ?

Le CNISN (Cadre National d'Interopérabilité de la Santé Numérique) constitue le deuxième niveau de la hiérarchie documentaire du secteur santé. Il définit les principes, capacités et règles de gouvernance qui s'appliquent aux échanges de données et de services impliquant le secteur santé à Madagascar.

Le CNISN fixe les principes opposables auxquels toute initiative doit se conformer, établit les responsabilités institutionnelles de chaque acteur, identifie les capacités nationales indispensables à l'interopérabilité, précise les règles applicables aux données et services partagés, et organise les mécanismes de conformité permettant de vérifier le respect de ces règles. Il reste volontairement neutre sur le plan technologique : il ne sélectionne aucun produit, fournisseur, technologie ni plateforme particulière.

```
Niveau 1 (CAESN)  →  Valeur, capabilités, gouvernance
Niveau 2 (CNISN)  →  Principes d'interopérabilité  ← CE DOCUMENT
Niveau 3 (ARTSN)  →  Patterns architecturaux, standards
Niveau 4 (PTISN)  →  Services, profils, produits candidats
```

## 2. Structure du CNISN

Le CNISN est organisé en huit parties qui couvrent l'ensemble du cycle de vie du cadre d'interopérabilité.

| Partie | Contenu | Qui la lit |
|--------|---------|------------|
| Préambule | Positionnement, portée, articulation | Tous |
| Principes | 25 principes (catégories A-F) | DEPSI, architectes |
| Capacités | 14 capacités d'interopérabilité | DEPSI, équipes techniques |
| Gouvernance | Instances, processus, responsabilités | Décideurs, gouvernance |
| Conformité | Critères, tests, homologation | Équipes techniques |
| Standards | Normes obligatoires et standards recommandés | Équipes techniques |
| Trajectoire | Feuille de route, jalons | Décideurs, planificateurs |
| Indicateurs | Métriques, suivi | SIS, suivi-évaluation |
| Conclusion | Synthèse | Tous |

## 3. Parcours de lecture par profil

### 3.1 Décideur institutionnel

Le décideur institutionnel cherche à comprendre les enjeux d'interopérabilité et les responsabilités qui en découlent. Il est invité à consulter le préambule pour le positionnement du cadre, la gouvernance pour les instances et responsabilités, la trajectoire pour la feuille de route, et la conclusion pour la synthèse.

### 3.2 Direction métier / programme

La direction métier ou le responsable de programme cherche à comprendre les règles applicables aux échanges de données dans son domaine. Elle doit lire le préambule pour la portée du cadre, les principes pour les catégories A et B, et les capacités pour les éléments pertinents à son domaine.

### 3.3 Équipe technique / DEPSI

L'équipe technique ou la DEPSI cherche à implémenter des échanges conformes au CNISN. Elle doit lire l'ensemble du préambule, les 25 principes, les 14 capacités, la conformité pour les critères et tests, puis se référer à l'ARTSN (niveau 3) pour les patterns techniques et au PTISN (niveau 4) pour les standards et profils.

### 3.4 Partenaire technique

Le partenaire technique cherche à évaluer la conformité d'une solution. Il doit consulter les principes (catégories D et E), les capacités couvertes par sa solution, et la conformité pour les preuves requises.

## 4. Les 25 principes du CNISN

Les principes sont organisés en six catégories qui couvrent l'ensemble des dimensions de l'interopérabilité.

| Catégorie | Principes | Objet |
|-----------|-----------|-------|
| **A** : Autorité et données de référence | P-INT-01 à P-INT-04 | Sources autoritatives, résolution, copies, historisation |
| **B** : Contractualisation | P-INT-05 à P-INT-09 | Contrats, versionnement, responsabilités, catalogues |
| **C** : Gouvernance interinstitutionnelle | P-INT-10 à P-INT-13 | Accords, arbitrage, dérogations |
| **D** : Sécurité et autorisation | P-INT-14 à P-INT-18 | Bases d'autorisation, finalité, résidence, minimisation |
| **E** : Neutralité et réversibilité | P-INT-19 à P-INT-22 | Neutralité technologique, portabilité, progressivité |
| **F** : Conformité | P-INT-23 à P-INT-25 | Preuves, applicabilité, réévaluation |

## 5. Les 14 capacités d'interopérabilité

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
| CAP-INT-13 | Transfrontalier | Interopérabilité transfrontalière |
| CAP-INT-14 | One Health | Échanges intersectoriels |

## 6. Liens vers les autres niveaux

| Niveau | Document | Lien |
|--------|----------|------|
| 1 : CAESN | Cadre d'Architecture d'Entreprise | ../00_caesn/00_overview/index.md |
| 3 : ARTSN | Architecture de Référence Technique | ../02_artsn/index.md |
| 4 : PTISN | Profils techniques d'implémentation | ../03_ptisn/index.md |

## 7. Documents complémentaires

Le guide de lecture s'accompagne de la matrice de lecture offrant une vue croisée des parties et des lecteurs, du glossaire définissant les termes d'interopérabilité, de la liste des acronymes, et des annexes contenant l'articulation avec l'ARTSN et les supports complémentaires.

## Références

- **matrice de lecture** : Matrice de lecture du CNISN (niveau 2) (`01_cnisn/reading-matrix.md`)
- **Préambule** : Préambule du CNISN (`01_cnisn/00_introduction/index.md`)
- **Principes** : Partie I : Principes nationaux d'interopérabilité de santé (`01_cnisn/01_principes/index.md`)
- **Capacités** : Partie II : Capacités nationales requises (`01_cnisn/02_capacites/index.md`)
- **Gouvernance** : Partie III : Gouvernance (`01_cnisn/03_gouvernance/index.md`)
- **Conformité** : Partie IV : Conformité (`01_cnisn/04_conformite/index.md`)
- **Standards** : Normes et standards d'architecture (`01_cnisn/05_standards/index.md`)
- **Trajectoire** : Partie V : Trajectoire de mise en œuvre (`01_cnisn/05_trajectoire/index.md`)
- **Indicateurs** : Partie VI : Indicateurs de suivi (`01_cnisn/06_indicateurs/index.md`)
- **Conclusion** : Conclusion du CNISN (`01_cnisn/07_conclusion/index.md`)
- **../00_caesn/00_overview/index.md** : Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) (`00_caesn/00_overview/index.md`)
- **../02_artsn/index.md** : Architecture de Référence Technique de la Santé Numérique (ARTSN) (`02_artsn/index.md`)
- **../03_ptisn/index.md** : Profils techniques d'implémentation de la Santé Numérique (PTISN) (`03_ptisn/index.md`)
