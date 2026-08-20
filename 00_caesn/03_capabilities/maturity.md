---
title: Évaluation de la maturité des capabilités
id: capabilities-maturity
domain: 03_capabilities
version: "1.0.0"
status: draft
last_reviewed: 2026-07-03
owner: Bureau de Réalisation de la Valeur
tags: [capabilités, maturité, priorisation]
---

# Évaluation de la maturité des capabilités

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## Échelle de maturité

Chaque capabilité est évaluée sur une échelle à cinq niveaux. L'évaluation mesure l'écart entre l'état actuel et le niveau cible nécessaire pour produire la valeur attendue.

| Niveau | Désignation | Description |
|--------|-------------|-------------|
| 1 | Initial | Capabilité inexistante ou mise en œuvre de façon ad hoc, sans processus défini ni documentation. |
| 2 | Émergent | Capabilité partiellement en place sur certains sites ou programmes, sans standardisation ni cohérence nationale. |
| 3 | Défini | Capabilité standardisée, documentée et déployée de façon partielle mais structurée. |
| 4 | Géré | Capabilité mesurée, pilotée par des indicateurs et pleinement intégrée aux processus du système. |
| 5 | Optimisé | Capabilité en amélioration continue, référence comparable aux meilleures pratiques régionales. |

Le **delta de maturité** (écart entre niveau actuel et niveau cible) constitue un critère central de priorisation des investissements.

## Priorisation des capabilités

Une capabilité est prioritaire lorsque :

- son delta de maturité est élevé ;
- elle sert plusieurs flux de valeur ;
- elle conditionne le fonctionnement d'autres capabilités ;
- elle réduit un risque majeur de fragmentation, non-adoption, dépendance ou non-soutenabilité ;
- elle contribue directement à un bénéfice mesurable pour les bénéficiaires.

## Tableau de maturité et de priorisation

Les niveaux ci-dessous sont une estimation de cadrage, à valider avec les directions métier et techniques.

| Code | Capabilité | Type | Niveau actuel | Cible 6 mois | Cible 12 mois | Delta | Priorité |
|------|------------|------|---------------|--------------|---------------|-------|----------|
| CAP-01 | Offre de soins et continuité | Métier | 2 | 3 | 4 | +2 | Haute |
| CAP-02 | Parcours patient et référence | Métier | 1 | 2 | 3 | +2 | Haute |
| CAP-03 | Qualité et sécurité des soins | Métier | 1 | 2 | 4 | +3 | Critique |
| CAP-04 | Santé communautaire | Métier | 2 | 3 | 4 | +2 | Haute |
| CAP-05 | Surveillance, alerte, riposte | Métier | 2 | 3 | 4 | +2 | Haute |
| CAP-06 | Vaccination et prévention | Métier | 3 | 4 | 5 | +2 | Moyenne |
| CAP-07 | Protection financière et CSU | Métier | 1 | 2 | 3 | +2 | Haute |
| CAP-08 | Gouvernance et redevabilité | Métier | 2 | 3 | 4 | +2 | Haute |
| CAP-09 | Ressources humaines en santé | Habilitante | 2 | 3 | 4 | +2 | Haute |
| CAP-10 | Chaîne d'approvisionnement | Habilitante | 2 | 3 | 4 | +2 | Haute |
| CAP-11 | Infrastructures et équipements | Habilitante | 2 | 2 | 3 | +1 | Normale |
| CAP-12 | Finances publiques et budget | Habilitante | 2 | 3 | 3 | +1 | Normale |
| CAP-13 | Système d'information sanitaire | Habilitante | 2 | 3 | 5 | +3 | Critique |
| CAP-14 | Interopérabilité et référentiels | Habilitante | 1 | 2 | 4 | +3 | Critique |
| CAP-15 | Cybersécurité et données | Habilitante | 1 | 2 | 3 | +2 | Haute |
| CAP-16 | Gestion du portefeuille numérique | Habilitante | 1 | 2 | 4 | +3 | Critique |
| CAP-17 | Engagement patient et identité numérique | Habilitante | 1 | 2 | 3 | +2 | Haute |
| CAP-18 | Coordination intersectorielle (One Health) | Habilitante | 1 | 2 | 2 | +1 | Normale |

### Résumé par priorité

| Priorité | Nombre | Capabilités |
|----------|--------|-------------|
| **Critique** | 4 | CAP-03, CAP-13, CAP-14, CAP-16 |
| **Haute** | 10 | CAP-01, CAP-02, CAP-04, CAP-05, CAP-07, CAP-08, CAP-09, CAP-10, CAP-15, CAP-17 |
| **Moyenne** | 2 | CAP-06, CAP-18 |
| **Normale** | 2 | CAP-11, CAP-12 |

### Maturité moyenne

| Indicateur | Valeur |
|------------|--------|
| **Maturité moyenne actuelle** | 1.6/5 |
| **Maturité moyenne cible (12 mois)** | 3.6/5 |
| **Delta moyen** | +2.0 |
| **Capabilités runway (CAP-13, 14, 15, 16)** | 1.5/5 → 4.0/5 |

## Liens

- Capabilités
- Runway
- Portefeuille

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Capabilités** : Capabilités du système de santé (`00_caesn/03_capabilities/index.md`)
- **Runway** : Capabilités critiques et architecture runway (`00_caesn/03_capabilities/runway.md`)
- **Portefeuille** : Portefeuille d'initiatives orienté valeur (`00_caesn/06_portfolio/index.md`)
