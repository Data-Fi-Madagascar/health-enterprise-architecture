---

title: Guide de lecture de l'ARTSN (niveau 3)
id: artsn-reading-guide
domain: 02_artsn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: ["artsn", "lecture", "niveau-3", "guide"]
---

# Guide de lecture de l'ARTSN (niveau 3)

## Pour qui lire ce document

**Niveau :** niveau 3 : Architecture de Référence Technique de la Santé Numérique.

Ce document s'adresse prioritairement aux décideurs institutionnels, aux équipes DEPSI et techniques, et aux partenaires techniques et financiers. Les directions métier et programmes ainsi que les équipes SIS, données et suivi-évaluation y trouveront un complément utile. Pour une vue d'ensemble des niveaux de pertinence, consultez la matrice de lecture.

## 1. Qu'est-ce que l'ARTSN ?

L'ARTSN (Architecture de Référence Technique de la Santé Numérique) est le **niveau 3** de la hiérarchie documentaire. Elle traduit les principes architecturaux du CAESN en **familles de patterns validées**, **standards techniques**, **contrats d'interfaces** et **règles d'homologation**.

**L'ARTSN précise le niveau technique** mais ne sélectionne pas de produits ni de configurations (ceci relève du PTISN).

```
Niveau 1 (CAESN)  →  Valeur, capabilités, gouvernance
Niveau 2 (CNISN)  →  Principes d'interopérabilité
Niveau 3 (ARTSN)  →  Patterns architecturaux, standards  ← CE DOCUMENT
Niveau 4 (PTISN)  →  Services, profils, produits candidats
```

## 2. Structure de l'ARTSN

L'ARTSN est organisée en **6 parties** + annexes. Le tableau suivant présente chaque partie, son contenu et les profils de lecteurs concernés : la Fondations recense les 6 fondations invariantes F.1 à F.6 lues par tous les profils ; les Flux de valeur déclinent VS-01 à VS-04 en exigences techniques, principalement pour architectes et intégrateurs ; les Exigences contextuelles couvrent ENF-1 à ENF-5 pour les équipes DEPSI et architectes ; les Chapitres et patterns articulent ART-0 à ART-11 sous forme de règles d'or et contrats pour développeurs et intégrateurs ; la Cartographie cible présente 6 couches et 2 axes verticaux, principalement pour architectes ; le Dictionnaire de données assure la sémantique universelle interministérielle pour les équipes données ; et la Gouvernance organise le cycle de vie, le versionnement et la revue pour décideurs et gouvernance.

## 3. Parcours de lecture par profil

### 3.1 Décideur institutionnel

**Objectif :** Comprendre l'architecture technique cible et les enjeux d'homologation.

Le décideur institutionnel commence par la Vue d'ensemble pour saisir le rôle et le positionnement de l'ARTSN, poursuit avec les Fondations afin de comprendre les 6 obligations fondamentales, consulte la Gouvernance pour appréhender le processus de décision, et termine par la Table de maturité qui présente les statuts des chapitres.

### 3.2 Architecte / intégrateur

**Objectif :** Concevoir une solution conforme à l'architecture de référence.

L'architecte ou l'intégrateur parcourt d'abord les Fondations pour identifier les contraintes invariantes, consulte la Cartographie cible pour disposer de la vue en couches, explore les Chapitres et patterns pour les patterns applicables, se réfère aux Exigences contextuelles pour les contraintes nationales, et achève par les Flux de valeur pour les exigences spécifiques par flux.

### 3.3 Développeur / intégrateur

**Objectif :** Implémenter les interfaces selon les patterns validés.

Le développeur ou l'intégrateur commence par les Fondations, en ciblant spécifiquement la section Résilience et la section Souveraineté, poursuit avec les Chapitres et patterns de ART-0 à ART-11, consulte le Dictionnaire de données pour la sémantique, et se réfère au PTISN (niveau 4) pour les standards et profils d'implémentation.

### 3.4 Partenaire technique / fournisseur

**Objectif :** Évaluer la conformité d'un produit ou service.

Le partenaire technique ou fournisseur examine les Fondations, en ciblant la section Éradication des silos et la section Homologation, analyse les Chapitres et patterns pour les contrats applicables, se réfère à la Gouvernance pour les critères d'homologation, et termine par la Table de maturité pour les conditions de promotion des chapitres.

## 4. Les 6 fondations invariantes

Le tableau suivant résume les fondations de l'ARTSN. F.1 Résilience géographique, F.2 Souveraineté intersectorielle, F.3 Éradication des silos et F.4 Homologation obligatoire portent un statut Stable, tandis que F.5 Protection et minimisation et F.6 Observabilité restent à ce stade au statut Provisoire.

## 5. Les chapitres et patterns de référence

Le tableau suivant recense les chapitres ART de ART-0 à ART-11 avec les patterns couverts : ART-0 couvre les accords de partage et contrats interinstitutionnels ; ART-1 traite de l'intégration et ingestion via connecteurs et adapters ; ART-2 aborde la médiation et normalisation avec médiateur et transformation ; ART-3 couvre l'historisation événementielle par event sourcing et CQRS ; ART-4 porte sur les référentiels de métadonnées sous forme de registres et catalogues ; ART-4A concerne la résolution d'identité via Client Registry et PIX ; ART-4B traite des bases d'autorisation par consentement et RBAC ; ART-4C couvre l'éligibilité et couverture par Benefits Registry ; ART-4D porte sur le référentiel géospatial par Facility Registry ; ART-5 aborde la cohérence et qualité par réconciliation et validation ; ART-6 traite de l'analytique et restitution avec tableaux de bord et indicateurs ; ART-7 porte sur la sécurité et contrôle d'accès par authentification et autorisation ; ART-8 couvre l'orchestration de processus par workflow et BPM ; ART-8A concerne l'orchestration bornée pour processus limités ; ART-8B traite de la modélisation en graphe pour flux relationnels ; ART-8C couvre l'agrégation par lot ; ART-8D porte sur la chorégraphie inter-institutionnelle pour l'échange décentralisé ; ART-9 aborde les garanties transactionnelles par ACID et sagas ; ART-10 traite de la logistique et supply chain ; ART-11 porte sur la coordination intersectorielle dans le cadre du One Health.

## 6. Liens vers les autres niveaux

La CNISN (niveau 2) définit le Cadre National d'Interopérabilité. Le CAESN (niveau 1) établit le Cadre d'Architecture d'Entreprise. Le PTISN (niveau 4) fournit les profils techniques d'implémentation.

## 7. Documents complémentaires

La Matrice de lecture propose une vue croisée parties et lecteurs. Le Glossaire fournit les définitions des termes techniques. Les Acronymes listent l'ensemble des acronymes. Les Annexes comprennent la table de maturité, le glossaire des patterns et le renvoi au CAESN.

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **Fondations** : Fondations de l'ARTSN (`02_artsn/00_fondations/index.md`)
- **Flux de valeur** : Flux de valeur (`02_artsn/01_flux-de-valeur/index.md`)
- **Exigences contextuelles** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
- **Cartographie cible** : Cartographie conceptuelle cible (`02_artsn/05_cartographie/index.md`)
- **Dictionnaire de données** : Dictionnaire de données fonctionnelles (`02_artsn/03_objets-de-donnees/index.md`)
- **Gouvernance** : Gouvernance de l'ARTSN (`02_artsn/06_gouvernance/index.md`)
- **Vue d'ensemble** : Architecture de Référence Technique de la Santé Numérique (ARTSN) (`02_artsn/index.md`)
- **Table de maturité** : Annexe A : Table de maturité par chapitre (`02_artsn/08_annexes/a-table-de-maturite.md`)
- **PTISN (niveau 4)** : Profils techniques d'implémentation de la Santé Numérique (PTISN) (`03_ptisn/index.md`)
- **CNISN (niveau 2)** : Cadre National d'Interopérabilité de la Santé Numérique (CNISN) (`01_cnisn/index.md`)
- **CAESN (niveau 1)** : Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) (`00_caesn/00_overview/index.md`)
- **Matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **Glossaire** : Glossaire de l'ARTSN (niveau 3) (`02_artsn/glossary.md`)
- **Acronymes** : Acronymes et abréviations de l'ARTSN (niveau 3) (`02_artsn/acronyms.md`)

## Documents de la section

- [artsn-glossary: Glossaire de l'ARTSN (niveau 3)](glossary.md)
- [artsn-reading-matrix: Matrice de lecture de l'ARTSN (niveau 3)](reading-matrix.md)
- [artsn-acronyms: Acronymes et abréviations de l'ARTSN (niveau 3)](acronyms.md)
- [artsn: Architecture de Référence Technique de la Santé Numérique (ARTSN)](index.md)
- [artsn-annexe-a-maturite: Annexe A : Table de maturité par chapitre](08_annexes/a-table-de-maturite.md)
- [artsn-annexe-c-renvoi: Annexe C : Renvoi CAESN et capacités candidates](08_annexes/c-renvoi-capacites-candidates.md)
- [artsn-annexe-b-glossaire-patterns: Annexe B : Glossaire des patterns cités](08_annexes/b-glossaire-patterns.md)
- [artsn-annexes: Annexes de l'ARTSN](08_annexes/index.md)
- [artsn-protocole-test: Annexe D : Protocole de test d'interopérabilité](08_annexes/d-protocole-test-interopabilite.md)
- [artsn-sla-performance: Annexe E : SLA et métriques de performance par profil](08_annexes/e-sla-performance.md)
- [artsn-cartographie-cible: Cartographie conceptuelle cible](05_cartographie/index.md)
- [ART-8D: ART-8D : Chorégraphie inter-institutionnelle](04_patterns/art-8d-choregraphie-interinstitutionnelle.md)
- [ART-8: ART-8 : Orchestration de processus](04_patterns/art-8-orchestration-processus-borne.md)
- [ART-4D: ART-4D : Référentiel géospatial et d'exploitation partagé](04_patterns/art-4d-referentiel-geospatial.md)
- [ART-7: ART-7 : Sécurité, contrôle d'accès et résidence de la donnée](04_patterns/art-7-securite-controle-acces.md)
- [ART-3: ART-3 : Historisation événementielle et profils de déploiement](04_patterns/art-3-historisation-evenementielle.md)
- [ART-10: ART-10 : Logistique](04_patterns/art-10-logistique.md)
- [ART-8B: ART-8B : Modélisation de relations en graphe](04_patterns/art-8b-modelisation-graphe.md)
- [ART-4C: ART-4C : Éligibilité et couverture](04_patterns/art-4c-eligibilite-couverture.md)
- [ART-5: ART-5 : Cohérence et qualité des données](04_patterns/art-5-coherence-qualite-donnees.md)
- [ART-0: ART-0 : Accords de partage inter-institutionnels](04_patterns/art-0-accords-partage.md)
- [ART-4B: ART-4B : Bases d'autorisation](04_patterns/art-4b-bases-autorisation.md)
- [ART-11: ART-11 : Coordination intersectorielle](04_patterns/art-11-coordination-intersectorielle.md)
- [ART-8C: ART-8C : Agrégation par lot](04_patterns/art-8c-agregation-par-lot.md)
- [ART-2: ART-2 : Médiation et normalisation](04_patterns/art-2-mediation-normalisation.md)
- [ART-4: ART-4 : Référentiels de métadonnées de gestion](04_patterns/art-4-referentiels-metadonnees.md)
- [artsn-chapitres: Chapitres et patterns de référence](04_patterns/index.md)
- [ART-6: ART-6 : Analytique et restitution](04_patterns/art-6-analytique-restitution.md)
- [ART-1: ART-1 : Intégration et ingestion](04_patterns/art-1-integration-ingestion.md)
- [ART-8A: ART-8A : Orchestration de processus borné](04_patterns/art-8a-orchestration-processus-borne.md)
- [ART-9: ART-9 : Garanties transactionnelles fortes](04_patterns/art-9-garanties-transactionnelles.md)
- [ART-4A: ART-4A : Résolution d'identité](04_patterns/art-4a-resolution-identite.md)
- [artsn-dictionnaire-donnees: Dictionnaire de données fonctionnelles](03_objets-de-donnees/index.md)
- [artsn-exigences-contextuelles: Exigences contextuelles nationales](02_exigences-contextuelles/index.md)
- [artsn-fondations: Fondations de l'ARTSN](00_fondations/index.md)
- [roadmap-deploiement-artsn: Réalisation technique ARTSN des lots du portefeuille](07_lots/index.md)
- [artsn-flux-de-valeur: Flux de valeur](01_flux-de-valeur/index.md)
- [artsn-gouvernance: Gouvernance de l'ARTSN](06_gouvernance/index.md)
- [conformite: Tableau de bord de conformité architecturale](06_gouvernance/conformite.md)
- [depreciation: Processus de dépréciation des composants](06_gouvernance/depreciation.md)
- [veille-architecturale: Veille architecturale](06_gouvernance/veille-architecturale.md)

<!-- liens-section-auto -->
