---


title: "Annexe A : Table de maturité par chapitre"
id: artsn-annexe-a-maturite
domain: 08_annexes
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: ["artsn", "annexes", "maturite", "statuts", "niveau-3"]
---


# Annexe A : Table de maturité par chapitre

## Pour qui lire ce document

**Niveau :** niveau 3 : Architecture de Référence Technique de la Santé Numérique.

La lecture de ce document est **ponctuelle** pour les décideurs institutionnels, **complémentaire** pour les directions métier et programmes ainsi que pour les équipes SIS, données et suivi-évaluation et les partenaires techniques et financiers, et **prioritaire** pour l'équipe DEPSI et ses équipes techniques. Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

La table de maturité fixe le statut de chaque chapitre et la condition de passage au statut supérieur. Elle est mise à jour par l'instance de gouvernance lors de chaque revue du document.

<!-- BEGIN:GENERATED mode=maturity source=referentiel/chapitres/*.md,referentiel/fondations/*.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

| Code | Titre canonique | Statut | Condition de passage au statut supérieur | Fiche |
|---|---|---|---|---|
| ART-0 | Accords de partage inter-institutionnels | candidate | Confirmation par une initiative impliquant une source hors gouvernance sanitaire | [ART-0](../../referentiel/chapitres/art-0.md) |
| ART-1 | Intégration et ingestion | stable | — | [ART-1](../../referentiel/chapitres/art-1.md) |
| ART-2 | Médiation et normalisation | stable | Stable pour registre structurel/sémantique/géospatial/tarifaire ; Proposition ouverte pour registre intersectoriel. Condition : confirmation du registre intersectoriel par une initiative concernée. | [ART-2](../../referentiel/chapitres/art-2.md) |
| ART-3 | Historisation événementielle et profils de déploiement | stable | — | [ART-3](../../referentiel/chapitres/art-3.md) |
| ART-4 | Référentiels de métadonnées de gestion | stable | Reconfirmation par une initiative supplémentaire | [ART-4](../../referentiel/chapitres/art-4.md) |
| ART-4A | Résolution d'identité | draft | Confirmation par une seconde initiative | [ART-4A](../../referentiel/chapitres/art-4a.md) |
| ART-4B | Bases d'autorisation | draft | Confirmation par une seconde initiative | [ART-4B](../../referentiel/chapitres/art-4b.md) |
| ART-4C | Éligibilité et couverture | candidate | Confirmation par une initiative VS-03 | [ART-4C](../../referentiel/chapitres/art-4c.md) |
| ART-4D | Référentiel géospatial et d'exploitation partagé | candidate | Confirmation par une initiative intersectorielle | [ART-4D](../../referentiel/chapitres/art-4d.md) |
| ART-5 | Cohérence et qualité des données | stable | Stable pour principe ; Proposition ouverte pour branches d'escalade. Condition : instruction détaillée de chaque branche par domaine | [ART-5](../../referentiel/chapitres/art-5.md) |
| ART-6 | Analytique et restitution | draft | Confirmation par une initiative combinant plusieurs familles de projection | [ART-6](../../referentiel/chapitres/art-6.md) |
| ART-7 | Sécurité, contrôle d'accès et résidence de la donnée | stable | — | [ART-7](../../referentiel/chapitres/art-7.md) |
| ART-8 | Orchestration de processus | draft | — | [ART-8](../../referentiel/chapitres/art-8.md) |
| ART-8A | Orchestration de processus borné | draft | Confirmation par une seconde initiative | [ART-8A](../../referentiel/chapitres/art-8a.md) |
| ART-8B | Modélisation de relations en graphe | candidate | Confirmation par une initiative supplémentaire | [ART-8B](../../referentiel/chapitres/art-8b.md) |
| ART-8C | Agrégation par lot | candidate | Confirmation par une initiative supplémentaire | [ART-8C](../../referentiel/chapitres/art-8c.md) |
| ART-8D | Chorégraphie inter-institutionnelle | candidate | Confirmation par une initiative intersectorielle | [ART-8D](../../referentiel/chapitres/art-8d.md) |
| ART-9 | Garanties transactionnelles fortes | candidate | Confirmation par une seconde initiative à garanties transactionnelles fortes | [ART-9](../../referentiel/chapitres/art-9.md) |
| ART-10 | Logistique | candidate | Confirmation par une initiative LMIS/logistique déployant la traçabilité de bout en bout des mouvements de stock | [ART-10](../../referentiel/chapitres/art-10.md) |
| ART-11 | Coordination intersectorielle | stable | — | [ART-11](../../referentiel/chapitres/art-11.md) |
| F-1 | Résilience face à la réalité géographique du pays | stable | — | [F-1](../../referentiel/fondations/f-1.md) |
| F-2 | Préservation de la souveraineté intersectorielle | stable | — | [F-2](../../referentiel/fondations/f-2.md) |
| F-3 | Éradication des silos technologiques | stable | — | [F-3](../../referentiel/fondations/f-3.md) |
| F-4 | Homologation obligatoire | stable | — | [F-4](../../referentiel/fondations/f-4.md) |
| F-5 | Protection et minimisation | draft | — | [F-5](../../referentiel/fondations/f-5.md) |
| F-6 | Observabilité | draft | — | [F-6](../../referentiel/fondations/f-6.md) |

<!-- END:GENERATED -->

## Domaines partiellement couverts par cette version

La logistique des médicaments et intrants (CAP-10) dispose d'un chapitre candidat (ART-10) qui définit les exigences de traçabilité de bout en bout des mouvements de stock et de réconciliation à somme nulle. Ce chapitre reste au statut **Proposition ouverte** en attente de confirmation par une initiative LMIS concrète. En complément, la réconciliation physique-numérique (ART-5) et la généralisation d'ART-9 au-delà du seul registre financier constituent des leviers complémentaires pour couvrir la chaîne logistique.

## Liens

Les liens utiles pour approfondir ce document sont les suivants : les chapitres et patterns de référence sont disponibles dans l'index des Chapitres et patterns de référence, et la structure de gouvernance est décrite dans la Gouvernance de l'ARTSN.

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **CAP-10** : Capabilités du système de santé (`00_caesn/03_capabilities/index.md`)
- **ART-10** : Logistique (`referentiel/chapitres/art-10.md`)
- **ART-5** : Cohérence et qualité des données (`referentiel/chapitres/art-5.md`)
- **ART-9** : Garanties transactionnelles fortes (`referentiel/chapitres/art-9.md`)
- **Chapitres et patterns de référence** : Chapitres et patterns de référence (`02_artsn/04_patterns/index.md`)
- **Gouvernance de l'ARTSN** : Gouvernance de l'ARTSN (`02_artsn/06_gouvernance/index.md`)
- **ADHMAT** : Évaluation de maturité ADHMAT (Africa CDC) — benchmark externe de réévaluation du HEA (`../../00_caesn/00_overview/foundations.md`)
