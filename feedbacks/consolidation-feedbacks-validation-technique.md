# Consolidation des feedbacks de validation technique HEA

> **Référence** : HEA-CONSOLIDATION-001
> **Date** : 30 août 2026
> **Version** : 2.0
> **Objet** : Synthèse consolidée de l'ensemble des observations issues de la validation technique des documents HEA (CAESN, CNISN, ARTSN)
> **Sources** : Matrices de validation des groupes G1, G2, G3, G4


## 1. Contexte

L'atelier de validation technique HEA a réuni quatre groupes d'experts (G1, G2, G3, G4) pour examiner les documents de la hiérarchie architecturale :

- **CAESN** (Cadre d'Architecture d'Entreprise de la Santé Numérique) - Niveau 1
- **CNISN** (Cadre National d'Interopérabilité de la Santé Numérique) - Niveau 2
- **ARTSN** (Architecture de Référence Technique de la Santé Numérique) - Niveau 3

Chaque groupe a rempli une matrice de validation technique standardisée avec les colonnes : ID, Document, Jour, Section/Domaine, Observation/Commentaire, Type d'écart, Proposition d'amendement, Décision, Responsable, Échéance, Statut, Point à arbitrer, Commentaire final.


## 2. Synthèse quantitative

### 2.1 Volume d'observations par groupe et par document

| Groupe | CAESN | CNISN | ARTSN | **Total** |
|--------|-------|-------|-------|-----------|
| G1 | 27 | 52 | 6 | **85** |
| G2 | 62 | 32 | 0 | **94** |
| G3 | 88 | 34 | 6 | **128** |
| G4 | 31 | 18 | 0 | **49** |
| **Total** | **208** | **136** | **12** | **356** |

### 2.2 Répartition par type d'écart

| Type d'écart | CAESN | CNISN | ARTSN | Total |
|-------------|-------|-------|-------|-------|
| Observation rédactionnelle | ~120 | ~70 | ~8 | ~198 |
| Lacune | ~35 | ~45 | ~2 | ~82 |
| Incohérence | ~15 | ~8 | ~3 | ~26 |
| Exigence à préciser | ~20 | ~8 | ~2 | ~30 |
| Ambiguïté | ~10 | ~3 | ~0 | ~13 |
| Autre | ~8 | ~2 | ~0 | ~10 |
| Non renseigné | ~0 | ~0 | ~0 | ~0 |
| **Total** | **208** | **136** | **12** | **356** |

### 2.3 Répartition par décision

| Décision | CAESN | CNISN | Total |
|----------|-------|-------|-------|
| Validé | ~8 | ~3 | ~11 |
| Validé sous réserve d'amendement | ~12 | ~6 | ~18 |
| À revoir | ~130 | ~100 | ~230 |
| Amendement requis | ~30 | ~12 | ~42 |
| À arbitrer | ~15 | ~10 | ~25 |
| Non renseigné | ~13 | ~5 | ~18 |
| **Total** | **208** | **136** | **344** |

### 2.4 Taux de convergence inter-groupes

Un même sujet a été soulevé par **≥2 groupes** dans environ **30% des cas**, concentré sur :
- Terminologie et références (CIM-10, anglicismes)
- Annexes manquantes
- Glossaire/lexique absent
- Gouvernance et responsabilités


## 3. Observations par document

### 3.1 CAESN (208 observations)

**Sources** : G1 (27), G2 (62), G3 (88), G4 (31)

**Domaines principaux d'observation** :
- Rédaction et mise en forme (~45)
- Flux de valeur et indicateurs (~30)
- Portée et applicabilité (~20)
- Gouvernance et responsabilités (~25)
- Données et référentiels (~25)
- Portefeuille d'initiatives (~20)
- Capabilités et architecture runway (~15)
- Principes d'architecture (~15)
- Annexes et structure (~13)

**Observations convergentes majeures** :
1. PDSS 2020-2024 → 2026-2030 (G1, G2, G3, G4)
2. "Malgache" → "malagasy" (G1, G3)
3. Matrice RACI absente (G1, G2, G3)
4. Responsabilités acteurs insuffisantes (G1, G2, G3)
5. Annexes vides (G1, G2, G3)
6. "Architecture runway" non définie (G1, G2)
7. Capabilité : incohérence glossaire/corps (G1, G2)
8. Terminologie VS : réhabilitation, intrants (G2, G4)
9. VS indicateurs manquants (G2, G4)
10. Scoring d'évaluation absent (G2)

### 3.2 CNISN (136 observations)

**Sources** : G1 (52), G2 (32), G3 (34), G4 (18)

**Domaines principaux d'observation** :
- Rédaction et mise en forme (~25)
- Terminologie et traduction (~20)
- Principes et exigences (~20)
- Gouvernance et conformité (~25)
- Portée et articulation (~15)
- Trajectoire de mise en œuvre (~15)
- Types d'interopérabilité (~8)
- Indicateurs et suivi (~8)

**Observations convergentes majeures** :
1. CIM-10 → CIM-11 (G1, G3, G4)
2. Glossaire/lexique absent (G1, G2, G3)
3. Annexes B-G inexistantes (G1, G3, G4)
4. "through" → "à travers" (G1, G2, G3)
5. "Malagasy" à enlever (G1)
6. CNASN → CAESN (G1, G3)
7. Gestion de version absente (G1, G2)
8. Portée trop restrictif MSANP (G4)
9. CSU/RSU/Min.Population (G3, G4)
10. Grille d'évaluation/conformité (G2, G4)

### 3.3 ARTSN (12 observations)

**Sources** : G1 (6), G3 (6)

**Observations** : principalement rédactionnelles (gestion de version, redondances, figures sans légende, F.4 manquant).


## 4. Points d'arbitrage identifiés

### CAESN
1. PDSS 2020-2024 → 2026-2030 (validé, immédiat)
2. Rôle du Comité National d'Architecture vs Bureau de Réalisation de la Valeur
3. Portée : « systèmes d'information sanitaire » vs périmètre actuel
4. Statut du document : draft vs cadre de référence

### CNISN
1. Annexes B-G : créer ou retirer ?
2. 5 types ou 4 types d'interopérabilité ?
3. Clause de proportionnalité décentralisée
4. Articulation CSU/RSU/Min.Population
5. Responsables référentiels : qui désigner ?
6. Pérennité comme caractéristique de l'information
7. Système de notation et grille d'évaluation


## 5. Processus de révision recommandé

### CAESN - 8 phases
1. Corrections immédiates (PDSS, "Malgache", acronymes)
2. Rédaction du glossaire
3. Complétion des annexes
4. Harmonisation terminologique
5. Structure de gouvernance (RACI, rôles)
6. Flux de valeur et indicateurs
7. Portefeuille et scoring
8. Relecture et validation finale

### CNISN - 8 phases
1. Corrections immédiates (CIM-11, "through", CNASN, "Malagasy", gestion de version)
2. Rédaction du glossaire/lexique
3. Décision sur les annexes B-G
4. Harmonisation terminologique
5. Élargissement de la portée
6. Intégration des exigences techniques
7. Structure de conformité (critères, scoring, matrice des pouvoirs)
8. Relecture et validation finale


*Consolidation des feedbacks - HEA-CONSOLIDATION-001 - Version 2.0 - 30 août 2026*
