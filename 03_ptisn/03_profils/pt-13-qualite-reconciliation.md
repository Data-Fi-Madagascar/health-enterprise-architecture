---
title: "Qualité et réconciliation"
id: ptisn-PT-13
domain: 03_profils
version: "1.0.0"
status: draft
last_reviewed: 2026-07-31
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "profils", "PT-13"]
related: ["CAP-INT-11", "ART-4", "ART-5", "ART-6", "CMP-05"]
---

# Profil technique national

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

## 1. Objet et périmètre

Le **profil PT-13 — Qualité et réconciliation** définit les services de validation, de qualité et de réconciliation des données du PTISN. Il garantit la cohérence entre sources, référentiels et projections analytiques.

Périmètre : validation des contrats, qualité des données, réconciliation, gestion des anomalies, publication d’indicateurs de qualité. Hors périmètre : le profilage sémantique (voir PT-07).

## 2. Capacité CNISN

- [CAP-INT-11: Qualité et réconciliation](../../referentiel/capacites/cap-int-11.md)

## 3. Chapitres ART applicables

- [ART-4: Référentiels de métadonnées de gestion](../../referentiel/chapitres/art-4.md)
- [ART-5: Cohérence et qualité des données](../../referentiel/chapitres/art-5.md)
- [ART-6: Analytique et restitution](../../referentiel/chapitres/art-6.md)

## 4. Acteurs (Actors)

- **Validateur de contrats (Contract Validator)** — exécute les tests de contrôle par interface (consomme PT-03).
- **Service de qualité (Data Quality Service)** — mesure et publie les indicateurs de qualité.
- **Service de réconciliation (Reconciliation Service)** — compare sources, référentiels et projections.
- **Gestionnaire d’anomalies (Anomaly Manager)** — traite et documente les écarts détectés.

*Référence — capacité CNISN mise en œuvre : [CAP-INT-11](../../referentiel/capacites/cap-int-11.md).
## 5. Transactions

| Transaction | Acteurs | R/O | Standard |
|----|----|----|----|
| T1 — Validation d’un contrat | Validateur → Registre (PT-03) | R | Tests de contrôle par interface |
| T2 — Réconciliation de données | Réconciliation → Sources/Référentiels | R | Comparaison documentée |
| T3 — Publication d’indicateurs de qualité | Qualité → Consommateur | O | Indicateurs de qualité |

R = requis ; O = optionnel (à définir si le dépôt ne précise pas).

*Référence — capacité CNISN mise en œuvre : [CAP-INT-11](../../referentiel/capacites/cap-int-11.md).
## 6. Content Modules

- **Rapport de test de contrat** : structure, terminologie, identifiants, métadonnées, cardinalités, valeurs obligatoires, compatibilité de version, droits d’émission, cohérence métier.
- **Rapport de réconciliation** : écarts entre système source/plateforme, deux référentiels, deux versions, journal/projection, opérationnel/analytique, agrégats de sources différentes.
- **Indicateurs de qualité** : mesures publiées et versionnées.

## 7. Options

- **O1 — Produit** : aucun produit unique retenu ; les règles de qualité restent explicites, portables, versionnées, testables, indépendantes d’un outil de visualisation.
- **O2 — Périmètre de réconciliation** : selon les paires de sources à comparer (source/plateforme, référentiels, versions, journal/projection, opérationnel/analytique, agrégats).

## 8. Service national

Services nationaux concernés :

- service de validation des contrats ;
- service de qualité ;
- service de réconciliation ;
- service de gestion des anomalies ;
- service de publication des indicateurs de qualité.

## 9. Formats et standards recommandés

Chaque interface doit disposer de tests de contrôle portant sur :

- structure ;
- terminologie ;
- identifiants ;
- métadonnées ;
- cardinalités ;
- valeurs obligatoires ;
- compatibilité de version ;
- droits d’émission ;
- cohérence métier.

*Référence — normes et standards CNISN : [01_cnisn/05_standards](../../01_cnisn/05_standards/index.md).
## 10. Exigences

Aucun produit unique n’est retenu. Les règles de qualité doivent rester :

- explicites ;
- portables ;
- versionnées ;
- testables ;
- indépendantes d’un outil de visualisation.

## 11. Déclaration de conformité (Integration Statement)

Conformité attestée par des tests de contrôle exécutés par interface, la publication d’indicateurs de qualité, et la gestion documentée des anomalies.

## 12. Articulation avec les autres profils

- [PT-03: catalogue des services et registre des contrats](../../referentiel/profils/pt-03.md)
- [PT-09: analytique et exposition de données](../../referentiel/profils/pt-09.md)
- [PT-08: échange de données agrégées](../../referentiel/profils/pt-08.md)

## 13. Limites et dépendances

La réconciliation dépend des référentiels (PT-04, PT-05, PT-06) et de la terminologie (PT-07). Aucun produit unique n’est imposé ; les règles de qualité sont portables et versionnées.

<!-- END:GENERATED -->
