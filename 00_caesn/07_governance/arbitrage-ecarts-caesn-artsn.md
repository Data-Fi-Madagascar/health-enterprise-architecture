---
title: "Proposition d'arbitrage — 5 écarts CAESN ↔ ARTSN"
id: arbitrage-ecarts-caesn-artsn
domain: 07_governance
version: "1.0.0"
status: proposé
last_reviewed: 2026-08-13
owner: DEPSI
tags: [gouvernance, arbitrage, caesn, artsn, ecarts]
---

# Proposition d'arbitrage — 5 écarts CAESN ↔ ARTSN

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

Ce document présente les propositions d'arbitrage pour les 5 écarts identifiés entre le CAESN et l'ARTSN, documentés dans le point de vigilance.

---

## Écart 1 — CAP-04bis « Engagement patient et identitovigilance »

### Constat

L'ARTSN rattache ART-4a (résolution d'identité) et ART-4b (bases d'autorisation) à une capabilité **CAP-04bis « Engagement patient et identitovigilance »**. Le catalogue CAESN ne comporte pas cette capabilité : CAP-04 est « Santé communautaire ».

### Proposition d'arbitrage

**Option A (recommandée) : Créer une nouvelle capabilité CAP-17 « Engagement patient et identité numérique »**

| Justification |
|---------------|
| L'identité numérique du patient est un enjeu transversal qui dépasse la santé communautaire (CAP-04). Elle concerne la résolution d'identité, le rapprochement de dossiers, le consentement et l'identitovigilance. |
| Cette capabilité serait rattachée aux flux VS-01 (soins essentiels) et VS-03 (protection financière). |
| Elle s'inscrit dans la fondation F.1 (Identité et registres) de l'ARTSN. |

**Option B : Intégrer comme sous-composante de CAP-04**

| Justification |
|---------------|
| Évite la création d'une nouvelle capabilité. |
| Mais réduit la visibilité de l'enjeu identité numérique. |

### Recommandation

**Option A** — Créer CAP-17 « Engagement patient et identité numérique » avec les attributs suivants :

| Champ | Valeur |
|-------|--------|
| **Identifiant** | CAP-17 |
| **Titre** | Engagement patient et identité numérique |
| **Description** | Résolution d'identité, rapprochement de dossiers, gestion du consentement, identitovigilance, engagement du patient dans le système numérique |
| **Type** | Habilitante |
| **Flux concernés** | VS-01, VS-03 |
| **Maturité cible** | 3/5 à 2 ans |
| **Propriétaire** | DEPSI + Direction des Systèmes d'Information |

---

## Écart 2 — Capacité candidate « Coordination intersectorielle (One Health) »

### Constat

L'ARTSN rattache ART-0 (accords de partage) et ART-8d (chorégraphie inter-institutionnelle) à une capacité candidate « Coordination intersectorielle » (One Health), absente du catalogue CAP-01..16.

### Proposition d'arbitrage

**Option A (recommandée) : Créer une nouvelle capabilité CAP-18 « Coordination intersectorielle (One Health) »**

| Justification |
|---------------|
| La coordination entre santé humaine, animale et environnementale est un enjeu stratégique national (RSI, Tripartite Plus). |
| Elle nécessite des échanges inter-institutionnels spécifiques (ART-0, ART-8d). |
| Elle s'inscrit dans le flux VS-02 (prévention et surveillance). |

**Option B : Intégrer la responsabilité dans CAP-05 (Surveillance sanitaire)**

| Justification |
|---------------|
| Évite la création d'une nouvelle capabilité. |
| Mais CAP-05 est déjà large et ne couvre pas explicitement la coordination interministérielle. |

### Recommandation

**Option A** — Créer CAP-18 « Coordination intersectorielle (One Health) » avec les attributs suivants :

| Champ | Valeur |
|-------|--------|
| **Identifiant** | CAP-18 |
| **Titre** | Coordination intersectorielle (One Health) |
| **Description** | Échanges inter-institutionnels entre santé humaine, animale et environnementale ; coordination avec les ministères de l'Agriculture, de l'Environnement, de l'Intérieur |
| **Type** | Habilitante |
| **Flux concernés** | VS-02 |
| **Maturité cible** | 2/5 à 3 ans |
| **Propriétaire** | Secrétariat Général du Ministère + DEPSI |

---

## Écart 3 — Référentiel normatif « Tripartite Plus / RSI »

### Constat

La coordination intersectorielle s'appuie sur un référentiel normatif international : **Tripartite Plus OMS–WOAH–FAO–PNUE** et le **Règlement Sanitaire International (RSI)**. Ce référentiel n'est pas intégré au registre des normes du CAESN.

### Proposition d'arbitrage

**Option A (recommandée) : Inscrire le référentiel Tripartite Plus / RSI au registre des normes**

| Justification |
|---------------|
| Le RSI est une obligation internationale contraignante pour Madagascar. |
| Le Tripartite Plus est le cadre de coordination One Health reconnu par l'OMS. |
| Leur inscription au registre des normes permet de les rendre opposables lors des homologations. |

**Option B : Ne pas inscrire, garder comme référence externe**

| Justification |
|---------------|
| Évite une complexification du registre. |
| Mais réduit la visibilité et l'opposabilité de ces référentiels. |

### Recommandation

**Option A** — Inscrire au registre des normes avec les attributs suivants :

| Champ | Valeur |
|-------|--------|
| **Identifiant** | NORM-007 |
| **Titre** | Règlement Sanitaire International (RSI 2005) |
| **Type** | Norme internationale obligatoire |
| **Portée** | Surveillance, notification, riposte aux événements de santé publique |
| **Propriétaire** | Direction de la Surveillance Sanitaire |

| Champ | Valeur |
|-------|--------|
| **Identifiant** | NORM-008 |
| **Titre** | Tripartite Plus OMS–WOAH–FAO–PNUE |
| **Type** | Cadre normatif international |
| **Portée** | Coordination One Health (santé humaine, animale, environnementale) |
| **Propriétaire** | Secrétariat Général du Ministère |

---

## Écart 4 — Capacité candidate « Surveillance spatio-temporelle »

### Constat

ART-4d (référentiel géospatial et d'exploitation partagé) est rattaché à une capacité candidate « Surveillance spatio-temporelle » absente du catalogue, nécessaire au cloisonnement One Health.

### Proposition d'arbitrage

**Option A (recommandée) : Intégrer cette responsabilité dans CAP-05 (Surveillance sanitaire)**

| Justification |
|---------------|
| La surveillance spatio-temporelle est une composante de la surveillance sanitaire (CAP-05). |
| Évite la création d'une nouvelle capabilité trop spécifique. |
| ART-4d serait rattaché à CAP-05 avec une note de clarification. |

**Option B : Créer une nouvelle capabilité CAP-19 « Surveillance spatio-temporelle »**

| Justification |
|---------------|
| Donne une visibilité spécifique à l'enjeu géospatial. |
| Mais risque de fragmenter le catalogue des capabilités. |

### Recommandation

**Option A** — Intégrer dans CAP-05 avec les modifications suivantes :

| Modification |
|--------------|
| Élargir la description de CAP-05 pour inclure explicitement la dimension géospatiale |
| Ajouter ART-4d comme chapitre rattaché à CAP-05 |
| Préciser que la surveillance spatio-temporelle couvre : géolocalisation des formations sanitaires, suivi des épidémies par zone, cartographie des risques |

---

## Écart 5 — Compte des principes : 18 P-01..18 vs 12 PA + PD

### Constat

Le document source de l'ARTSN annonce **18 principes (P-01 à P-18)** ; le catalogue CAESN structure les principes en **12 transversaux (PA)** + **principes de domaine (PD) par flux**.

### Proposition d'arbitrage

**Option A (recommandée) : Conserver la nomenclature CAESN (12 PA + PD) et aligner l'ARTSN**

| Justification |
|---------------|
| La nomenclature CAESN (12 PA + PD) est plus structurée et plus lisible. |
| Elle permet de distinguer les principes transversaux des principes spécifiques à chaque flux de valeur. |
| L'ARTSN peut référencer les principes PA et PD sans nécessiter de renumérotation. |

**Option B : Adopter la nomenclature ARTSN (18 P-01..18)**

| Justification |
|---------------|
| Simplicité de numérotation. |
| Mais perd la distinction transversal/domaine. |

### Recommandation

**Option A** — Conserver la nomenclature CAESN avec les clarifications suivantes :

| Clarification |
|---------------|
| Documenter la correspondance entre P-01..18 (ARTSN) et PA-01..12 + PD (CAESN) |
| Créer un tableau de mapping dans l'annexe de l'ARTSN |
| Valider que les 18 principes de l'ARTSN couvrent bien les 12 PA + les PD du CAESN |

---

## Synthèse des arbitrages proposés

| Écart | Proposition | Impact |
|-------|-------------|--------|
| D-1 | Créer CAP-17 « Engagement patient et identité numérique » | Nouvelle capabilité habilitante |
| D-2 | Créer CAP-18 « Coordination intersectorielle (One Health) » | Nouvelle capabilité habilitante |
| D-3 | Inscrire Tripartite Plus / RSI au registre des normes | 2 nouvelles normes |
| D-4 | Intégrer dans CAP-05 (élargissement) | Modification de capabilité existante |
| D-5 | Conserver nomenclature CAESN (12 PA + PD) | Alignement de l'ARTSN |

## Prochaines étapes

1. **Validation par les directions métier** — Soumettre les propositions aux responsables de capabilités
2. **Arbitrage par le Comité National** — Formeliser les décisions via des ADR
3. **Mise à jour du CAESN** — Appliquer les modifications validées
4. **Mise à jour de l'ARTSN** — Aligner les chapitres sur les capabilités validées
5. **Communication** — Informer les parties prenantes des décisions prises

## Liens

- Point de vigilance CAESN
- CAESN — capabilités
- ARTSN — Annexe C
- CAESN — normes et standards
- CAESN — registre des ADR

## Références

- **matrice de lecture** — Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **CAESN** — Capabilités du système de santé (`00_caesn/03_capabilities/index.md`)
- **ARTSN** — Architecture de Référence Technique de la Santé Numérique (ARTSN) (`02_artsn/index.md`)
- **point de vigilance** — Point de vigilance CAESN — capacité et référentiel manquants pour la coordination intersectorielle (One Health) (`00_caesn/07_governance/point-de-vigilance-caesn.md`)
- **ART-4a (résolution d'identité)** — Résolution d'identité (`referentiel/chapitres/art-4a.md`)
- **ART-4b (bases d'autorisation)** — Bases d'autorisation (`referentiel/chapitres/art-4b.md`)
- **ART-0 (accords de partage)** — Accords de partage inter-institutionnels (`referentiel/chapitres/art-0.md`)
- **ART-8d (chorégraphie inter-institutionnelle)** — Chorégraphie inter-institutionnelle (`referentiel/chapitres/art-8d.md`)
- **ART-4d (référentiel géospatial et d'exploitation partagé)** — Référentiel géospatial et d'exploitation partagé (`referentiel/chapitres/art-4d.md`)
- **Point de vigilance CAESN** — Point de vigilance CAESN — capacité et référentiel manquants pour la coordination intersectorielle (One Health) (`00_caesn/07_governance/point-de-vigilance-caesn.md`)
- **CAESN — capabilités** — Capabilités du système de santé (`00_caesn/03_capabilities/index.md`)
- **ARTSN — Annexe C** — Annexe C — Renvoi CAESN et capacités candidates (`02_artsn/07_annexes/c-renvoi-capacites-candidates.md`)
- **CAESN — normes et standards** — Normes et standards d'architecture (`01_cnisn/05_standards/index.md`)
- **CAESN — registre des ADR** — Décisions d'architecture (ADR) (`01_cnisn/06_decisions/index.md`)
