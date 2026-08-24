---

title: Guide de lecture du CAESN (niveau 1)
id: caesn-reading-guide
domain: 00_caesn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: Bureau de Réalisation de la Valeur
tags: ["caesn", "lecture", "niveau-1", "guide"]
---

# Guide de lecture du CAESN (niveau 1)

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

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
| Capabilités | Catalogue CAP-01 à CAP-18, maturité | Tous |
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

1. Vue d'ensemble : Objet, portée, hiérarchie
2. Fondements : Ancrage stratégique
3. Modèle de valeur : Bénéficiaires et dimensions
4. Flux de valeur : Les 4 flux nationaux
5. Gouvernance : Instances et responsabilités
6. Portefeuille : Registre des initiatives

### 3.2 Direction métier / programme

**Objectif :** Comprendre comment une initiative s'inscrit dans le cadre.

1. Vue d'ensemble : Positionnement
2. Modèle de valeur : Valeur produite
3. Flux de valeur : Flux pertinent
4. Capabilités : Capacités couvertes
5. Portefeuille : Fiche d'initiative

### 3.3 Équipe technique / DEPSI

**Objectif :** Implémenter selon les principes et standards du cadre.

1. Vue d'ensemble : Lecture complète
2. Principes : Principes PA et PD
3. Capabilités : Catalogue complet
4. Données : Domaines de données
5. Application : Paysage applicatif
6. Normes : Standards à respecter
7. ARTSN (niveau 3) : Patterns techniques

### 3.4 Partenaire technique / financier

**Objectif :** Évaluer l'alignement d'une initiative avec le cadre.

1. Vue d'ensemble : Objet et portée
2. Modèle de valeur : Valeur attendue
3. Flux de valeur : Flux couverts
4. Capabilités : Maturité cible
5. Gouvernance : Processus de validation

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
| 2 : CNISN | Cadre National d'Interopérabilité | ../01_cnisn/index.md |
| 3 : ARTSN | Architecture de Référence Technique | ../02_artsn/index.md |
| 4 : PTISN | Profils techniques d'implémentation | ../03_ptisn/index.md |

---

## 7. Documents complémentaires

- Matrice de lecture : Vue croisée sections × lecteurs
- Glossaire : Définitions des termes
- Acronymes : Liste des acronymes
- Annexes : Supports complémentaires

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Fondements** : Fondements stratégiques et normatifs (`00_caesn/00_overview/foundations.md`)
- **Modèle de valeur** : Modèle national de valeur (`00_caesn/00_overview/value-model.md`)
- **Vue d'ensemble** : Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) (`00_caesn/00_overview/index.md`)
- **ARTSN (niveau 3)** : Architecture de Référence Technique de la Santé Numérique (ARTSN) (`02_artsn/index.md`)
- **../01_cnisn/index.md** : Cadre National d'Interopérabilité de la Santé Numérique (CNISN) (`01_cnisn/index.md`)
- **../02_artsn/index.md** : Architecture de Référence Technique de la Santé Numérique (ARTSN) (`02_artsn/index.md`)
- **../03_ptisn/index.md** : Profils techniques d'implémentation de la Santé Numérique (PTISN) (`03_ptisn/index.md`)
- **Matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Glossaire** : Glossaire (`00_caesn/10_annexes/glossary.md`)
- **Acronymes** : Acronymes et abréviations (`00_caesn/10_annexes/acronyms.md`)

## Documents de la section

- [caesn-reading-matrix: Matrice de lecture du CAESN (niveau 1)](reading-matrix.md)
- [fondements: Fondements stratégiques et normatifs](00_overview/foundations.md)
- [valeur: Modèle national de valeur](00_overview/value-model.md)
- [caesn: Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN)](00_overview/index.md)
- [verification-perennite-documents: Vérification de la pérennité : PDSS, SNSD, PSRSIS](00_overview/verification-perennite.md)
- [capabilities-business: Capabilités métier de santé](03_capabilities/business.md)
- [capabilities-digital: Capabilités numériques transversales et composants DPI-H](03_capabilities/digital.md)
- [capabilities-maturity: Évaluation de la maturité des capabilités](03_capabilities/maturity.md)
- [capabilities: Capabilités du système de santé](03_capabilities/index.md)
- [capabilities-enabling: Capabilités habilitantes du système](03_capabilities/enabling.md)
- [capabilities-runway: Capabilités critiques et architecture runway](03_capabilities/runway.md)
- [application-lifecycle: Cycle de vie applicatif et critères d'homologation](05_application/lifecycle.md)
- [application-principles: Principes de l'architecture applicative](05_application/principles.md)
- [application-urbanisation: Règles d'urbanisation applicative](05_application/urbanisation.md)
- [application-domains: Domaines applicatifs cibles par flux de valeur](05_application/application-domains.md)
- [application-constraints: Contraintes d'exploitation différenciées](05_application/constraints.md)
- [application-target-layers: Paysage applicatif cible](05_application/layers.md)
- [application-architecture: Architecture applicative et systèmes numériques](05_application/index.md)
- [application-shared-services: Services numériques partagés prioritaires](05_application/shared-services.md)
- [application-rationalization: Trajectoire de rationalisation du paysage applicatif](05_application/rationalization.md)
- [VS-03: VS-03 : Protéger financièrement la population face aux dépenses de santé](01_value-streams/vs-03-financial-protection.md)
- [VS-04: VS-04 : Piloter, coordonner et améliorer la performance du système de santé](01_value-streams/vs-04-system-steering.md)
- [VS-01: VS-01 : Accéder à des services de santé essentiels, intégrés, équitables et de qualité](01_value-streams/vs-01-access-care.md)
- [value-streams: Flux de valeur nationaux de santé](01_value-streams/index.md)
- [VS-02: VS-02 : Prévenir, détecter et répondre aux risques sanitaires](01_value-streams/vs-02-risk-protection.md)
- [evaluation-gdhm: Cartographie HEA → GDHM : Auto-évaluation de maturité numérique santé](10_annexes/evaluation-gdhm.md)
- [annexe-glossary: Glossaire](10_annexes/glossary.md)
- [annexe-acronyms: Acronymes et abréviations](10_annexes/acronyms.md)
- [annexes: Annexes](10_annexes/index.md)
- [annexe-comparaison-architectures-africaines: Comparaison des architectures de santé numérique africaines](10_annexes/comparaison-architectures-africaines.md)
- [data-referentials: Référentiels nationaux](04_data/referentials.md)
- [data-lifecycle: Cycle de vie des données](04_data/lifecycle.md)
- [data-principles: Principes de l'architecture des données](04_data/principles.md)
- [data-governance: Gouvernance, qualité et protection des données](04_data/governance.md)
- [data-architecture: Architecture des données et de l'information sanitaire](04_data/index.md)
- [data-domains: Domaines de données prioritaires](04_data/domains.md)
- [governance-vro: Bureau de Réalisation de la Valeur](07_governance/value-realization-office.md)
- [point-de-vigilance-caesn: Point de vigilance CAESN : capacité et référentiel manquants pour la coordination intersectorielle (One Health)](07_governance/point-de-vigilance-caesn.md)
- [processus-gouvernance: Guide du processus de gouvernance](07_governance/processus-gouvernance.md)
- [governance-raci: RACI de gouvernance et responsabilités](07_governance/raci.md)
- [homologation: Workflow d'homologation architecturale](07_governance/homologation.md)
- [governance: Gouvernance du cadre d'architecture](07_governance/index.md)
- [cnasen-composition: Composition et fonctionnement du Comité National](07_governance/cnasen-composition.md)
- [instances-sectorielles: Instances sectorielles et autorités spécialisées](07_governance/instances-sectorielles.md)
- [arbitrage-ecarts-caesn-artsn: Proposition d'arbitrage : 5 écarts CAESN ↔ ARTSN](07_governance/arbitrage-ecarts-caesn-artsn.md)
- [fondement-legal: Fondement légal et cadre législatif de la santé numérique](07_governance/fondement-legal.md)
- [prioritization: Critères et score de priorisation des initiatives](06_portfolio/prioritization.md)
- [portfolio-governance: Dépendances, revues et règles de gouvernance du portefeuille](06_portfolio/governance.md)
- [initiative-card: Fiche standard d'initiative orientée valeur](06_portfolio/initiative-card.md)
- [portfolio: Portefeuille d'initiatives orienté valeur](06_portfolio/index.md)
- [value-chain: Chaîne de valeur d'une initiative](06_portfolio/value-chain.md)
- [caesn-migration: Plan de migration : De l'existant au futur état](06_portfolio/migration-existant.md)
- [mapping-principes-caesn-artsn: Table de correspondance : Principes CAESN ↔ ARTSN](02_principles/mapping-caesn-artsn.md)
- [pa: Principes d'architecture transversaux](02_principles/transversal.md)
- [principles: Principes d'architecture](02_principles/index.md)
- [pd-VS-04: PD-VS-04 : Principes de domaine : piloter, coordonner et améliorer la performance](02_principles/domain/vs04.md)
- [pd-VS-01: PD-VS-01 : Principes de domaine : accéder à des services de santé essentiels](02_principles/domain/vs01.md)
- [pd-VS-02: PD-VS-02 : Principes de domaine : prévenir, détecter et répondre aux risques sanitaires](02_principles/domain/vs02.md)
- [principles-domain: Principes de domaine par flux de valeur](02_principles/domain/index.md)
- [pd-VS-03: PD-VS-03 : Principes de domaine : protéger financièrement la population](02_principles/domain/vs03.md)

<!-- liens-section-auto -->
