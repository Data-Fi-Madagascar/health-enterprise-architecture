---

title: "Priorisation et calendrier : 5 premières décisions PTISN"
id: ptisn-priorisation-decisions
domain: 03_ptisn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: ["ptisn", "decisions", "priorisation", "calendrier"]
---

# Priorisation et calendrier : 5 premières décisions PTISN

## Pour qui lire ce document

**Niveau :** niveau 4 : Profils techniques d'implémentation de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## Contexte

Le PTISN identifie **18 décisions à instruire** (Annexe B). Ces décisions conditionnent le déploiement des profils techniques et l'opérationnalisation du cadre d'interopérabilité. Leur priorisation est essentielle pour avancer de façon ordonnée.

## Critères de priorisation

La priorisation repose sur cinq critères pondérés, appliqués à chacune des dix-huit décisions identifiées. L'impact sur les initiatives en cours pèse pour 30 %, reflétant l'urgence de lever les blocages opérationnels. La dépendance d'autres décisions pèse pour 25 %, car certaines validations sont préalables à d'autres. La faisabilité technique pèse pour 20 %, la conformité aux obligations internationales pour 15 % et la disponibilité des ressources pour 10 %.

| Critère | Poids |
|---------|-------|
| **Impact sur les initiatives en cours** | 30% |
| **Dépendance d'autres décisions** | 25% |
| **Faisabilité technique** | 20% |
| **Conformité aux obligations internationales** | 15% |
| **Disponibilité des ressources** | 10% |

## 5 premières décisions prioritaires

### Décision 1 : Modèle national d'identité santé du bénéficiaire

La première décision porte sur le modèle national d'identité santé du bénéficiaire. Elle est classée priorité 1 en raison de son impact critique : elle bloque la continuité des soins et la protection financière. Aucune dépendance ne la précède, car il s'agit d'une décision fondatrice. L'échéance est fixée au quatrième trimestre 2026, sous la responsabilité conjointe de la DEPSI et de la Direction des Systèmes d'Information. Le livrable attendu est une note de cadrage validée par le Comité National. Cette décision est prioritaire car elle conditionne le PT-04 (résolution d'identité), impacte tous les flux de valeur (VS-01, VS-03) et est nécessaire pour le consentement (PT-11).

| Champ | Valeur |
|-------|--------|
| **Priorité** | 🔴 1 |
| **Impact** | Critique : bloque la continuité des soins et la protection financière |
| **Dépendances** | Aucune (décision fondatrice) |
| **Échéance** | T4 2026 |
| **Responsable** | DEPSI + Direction des Systèmes d'Information |
| **Livrable** | Note de cadrage validée par le Comité National |

### Décision 2 : Version FHIR nationale de référence

La deuxième décision concerne la version FHIR nationale de référence. Elle est classée priorité 2 en raison de son impact élevé : elle standardise tous les échanges de données. Aucune dépendance ne la précède. L'échéance est fixée au quatrième trimestre 2026, sous la responsabilité conjointe de la DEPSI et des Directions techniques. Le livrable attendu est un Architecture Decision Record (ADR) documentant le choix de la version FHIR. Cette décision est prioritaire car elle standardise les contrats d'interface, conditionne l'homologation des solutions et s'aligne avec les standards internationaux de l'OMS et d'IHE.

| Champ | Valeur |
|-------|--------|
| **Priorité** | 🔴 2 |
| **Impact** | Élevé : standardise tous les échanges de données |
| **Dépendances** | Aucune |
| **Échéance** | T4 2026 |
| **Responsable** | DEPSI + Directions techniques |
| **Livrable** | ADR documentant le choix de la version FHIR |

### Décision 3 : Profil national de consentement

La troisième décision porte sur le profil national de consentement. Elle est classée priorité 3 en raison de son impact critique : elle bloque tout partage de données patients. Elle dépend de la Décision 1 (identité santé). L'échéance est fixée au premier trimestre 2027, sous la responsabilité conjointe de la DEPSI et de la Direction Juridique. Le livrable attendu est le profil PT-11 complété. Cette décision est prioritaire car elle constitue une obligation légale au titre de la protection des données de santé, bloque le PT-01 (échange interinstitutionnel) et est nécessaire pour la conformité au cadre juridique.

| Champ | Valeur |
|-------|--------|
| **Priorité** | 🔴 3 |
| **Impact** | Critique : bloque tout partage de données patients |
| **Dépendances** | Décision 1 (identité santé) |
| **Échéance** | T1 2027 |
| **Responsable** | DEPSI + Direction Juridique |
| **Livrable** | Profil PT-11 complété |

### Décision 4 : Produit du service terminologique

La quatrième décision concerne le produit du service terminologique. Elle est classée priorité 4 en raison de son impact élevé : elle conditionne la normalisation sémantique. Elle dépend de la Décision 2 (version FHIR). L'échéance est fixée au premier trimestre 2027, sous la responsabilité conjointe de la DEPSI et des Directions cliniques. Le livrable attendu est le cahier des charges du service terminologique. Cette décision est prioritaire car elle est nécessaire pour l'ART-2 (médiation et normalisation), conditionne l'interopérabilité sémantique et impacte le dictionnaire de données.

| Champ | Valeur |
|-------|--------|
| **Priorité** | 🟡 4 |
| **Impact** | Élevé : conditionne la normalisation sémantique |
| **Dépendances** | Décision 2 (version FHIR) |
| **Échéance** | T1 2027 |
| **Responsable** | DEPSI + Directions cliniques |
| **Livrable** | Cahier des charges du service terminologique |

### Décision 5 : Produit du catalogue des services

La cinquième décision porte sur le produit du catalogue des services. Elle est classée priorité 5 en raison de son impact moyen : elle facilite la découverte et l'intégration. Elle dépend de la Décision 2 (version FHIR). L'échéance est fixée au deuxième trimestre 2027, sous la responsabilité de la DEPSI. Le livrable attendu est la spécification du catalogue de services. Cette décision est prioritaire car elle supporte la CAP-INT-06 (catalogue de services), facilite l'intégration des nouvelles initiatives et améliore la visibilité de l'écosystème.

| Champ | Valeur |
|-------|--------|
| **Priorité** | 🟡 5 |
| **Impact** | Moyen : facilite la découverte et l'intégration |
| **Dépendances** | Décision 2 (version FHIR) |
| **Échéance** | T2 2027 |
| **Responsable** | DEPSI |
| **Livrable** | Spécification du catalogue de services |

## Calendrier prévisionnel

Le calendrier ci-dessous synthétise l'échelonnement des cinq premières décisions sur la période 2026–2027. La Décision 1 (identité santé) et la Décision 2 (version FHIR) sont lancées au quatrième trimestre 2026. La Décision 3 (consentement) et la Décision 4 (terminologie) sont programmées au premier trimestre 2027, tandis que la Décision 5 (catalogue des services) intervient au deuxième trimestre 2027.

```
2026                    2027
T3      T4      T1      T2      T3      T4
│       │       │       │       │       │
├───────┼───────┼───────┼───────┼───────┤
│       │       │       │       │       │
│  D1───┼───────┤       │       │       │  Identité santé
│       │       │       │       │       │
│  D2───┼───────┤       │       │       │  Version FHIR
│       │       │       │       │       │
│       │  D3───┼───────┤       │       │  Consentement
│       │       │       │       │       │
│       │  D4───┼───────┤       │       │  Terminologie
│       │       │       │       │       │
│       │       │  D5───┼───────┤       │  Catalogue
│       │       │       │       │       │
└───────┴───────┴───────┴───────┴───────┘
```

## Prochaines étapes

Les prochaines étapes consistent à valider la priorisation avec les équipes techniques, à lancer la Décision 1 (identité santé) au troisième trimestre 2026, à documenter via des ADR chaque décision validée et à communiquer aux parties prenantes.

1. **Valider la priorisation** avec les équipes techniques
2. **Lancer la Décision 1** (identité santé) : T3 2026
3. **Documenter via des ADR** chaque décision validée
4. **Communiquer** aux parties prenantes

## Liens

- Annexe B : Décisions à instruire
- PT-04 : Résolution d'identité
- PT-11 : Consentement
- CAESN : Décisions

## Références

- **matrice de lecture** : Matrice de lecture du PTISN (niveau 4) (`03_ptisn/reading-matrix.md`)
- **Annexe B : Décisions à instruire** : Annexe B : Décisions à instruire (`03_ptisn/08_annexes/b-decisions-instruire.md`)
- **PT-04 : Résolution d'identité** : Profil technique national (`referentiel/profils/pt-04.md`)
- **PT-11 : Consentement** : Profil technique national (`referentiel/profils/pt-11.md`)
- **CAESN : Décisions** : Décisions d'architecture (ADR) (`01_cnisn/06_decisions/index.md`)
