---

title: "Table de correspondance : Principes CAESN ↔ ARTSN"
id: mapping-principes-caesn-artsn
domain: 02_principles
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: ["principes", "caesn", "artsn", "mapping", "correspondance"]
---

# Table de correspondance : Principes CAESN ↔ ARTSN

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## Contexte

L'ARTSN (document source) référence **18 principes (P-01 à P-18)** tandis que le CAESN structure les principes en **12 principes architecturaux transversaux (PA-01 à PA-12)** plus des **principes de domaine (PD)** par flux de valeur.

Cette table établit la correspondance entre les deux nomenclatures pour assurer la cohérence entre les niveaux.

## Correspondance PA ↔ P

| PA CAESN | Titre PA | P ARTSN | Titre P |
|----------|----------|---------|---------|
| PA-01 | Primauté de la valeur pour le bénéficiaire | P-01 | Orientation bénéficiaire |
| PA-02 | Neutralité technologique | P-02 | Neutralité technologique |
| PA-03 | Sécurité par conception | P-03 | Sécurité dès la conception |
| PA-04 | Protection de la vie privée | P-04 | Protection de la vie privée |
| PA-05 | Interopérabilité comme exigence | P-05 | Interopérabilité |
| PA-06 | Gouvernance des données | P-06 | Gouvernance des données |
| PA-07 | Soutenabilité financière | P-07 | Soutenabilité |
| PA-08 | Pérennité et évolutivité | P-08 | Pérennité |
| PA-09 | Transparence et redevabilité | P-09 | Transparence |
| PA-10 | Inclusivité et accessibilité | P-10 | Inclusivité |
| PA-11 | Souveraineté numérique | P-11 | Souveraineté numérique |
| PA-12 | Architecture runway | P-12 | Architecture runway |

## Principes de domaine (PD) : uniques au CAESN

Les principes de domaine sont spécifiques aux flux de valeur et ne figurent pas dans la nomenclature ARTSN (qui les intègre implicitement via les chapitres ART).

| Flux | Principe | Titre |
|------|----------|-------|
| VS-01 | PD-VS01-01 | Continuité des soins |
| VS-01 | PD-VS01-02 | Qualité des soins |
| VS-01 | PD-VS01-03 | Droits du patient |
| VS-02 | PD-VS02-01 | Rapidité de détection |
| VS-02 | PD-VS02-02 | Couverture de surveillance |
| VS-02 | PD-VS02-03 | Coordination intersectorielle |
| VS-03 | PD-VS03-01 | Protection financière |
| VS-03 | PD-VS03-02 | Équité d'accès |
| VS-03 | PD-VS03-03 | Pérennité du financement |
| VS-04 | PD-VS04-01 | Evidence-based policy |
| VS-04 | PD-VS04-02 | Redevabilité |

## Principes ARTSN sans équivalent PA direct

Les principes P-13 à P-18 de l'ARTSN sont des déclinaisons techniques des PA, pas de nouveaux principes transversaux :

| P ARTSN | Rattachement PA | Titre |
|---------|-----------------|-------|
| P-13 | PA-05, PA-06 | Standardisation des données |
| P-14 | PA-03, PA-04 | Contrôle d'accès |
| P-15 | PA-03 | Journalisation et audit |
| P-16 | PA-04 | Minimisation des données |
| P-17 | PA-11 | Résidence des données |
| P-18 | PA-03, PA-15 | Traçabilité |

## Conclusion

La nomenclature CAESN (12 PA + PD) est la référence. L'ARTSN peut référencer les principes PA et PD sans renumérotation. Le tableau ci-dessus sert de base à l'Annexe de l'ARTSN.

## Liens

- CAESN : Principes architecturaux
- ARTSN : Fondations
- Point de vigilance CAESN

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **CAESN : Principes architecturaux** : Principes d'architecture (`00_caesn/02_principles/index.md`)
- **ARTSN : Fondations** : Fondations de l'ARTSN (`02_artsn/00_fondations/index.md`)
- **Point de vigilance CAESN** : Point de vigilance CAESN : capacité et référentiel manquants pour la coordination intersectorielle (One Health) (`00_caesn/07_governance/point-de-vigilance-caesn.md`)
