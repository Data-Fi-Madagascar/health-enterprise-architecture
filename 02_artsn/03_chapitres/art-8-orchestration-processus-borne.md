---

title: "Orchestration de processus"
id: artsn-ART-8
domain: 03_chapitres
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: ["artsn", "chapitres", "ART-8", "niveau-3"]
related: ["CAP-INT-03"]
---

# Orchestration de processus

## Pour qui lire ce document

**Niveau :** niveau 3 : Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.


ART-8 : Orchestration de processus constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `ART-8`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Contenu normatif.** Pour tout processus métier distribué, asynchrone et à étapes multiples, l’architecture impose l’utilisation d’un **gestionnaire de transactions longues**. Ce composant doit suivre l’état du parcours, maintenir la cohérence sans verrouiller les bases distantes, et déclencher obligatoirement des transactions d’annulation ou de correction en cas d’échec d’une étape.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (établissements hospitaliers autonomes, cliniques privées, rupture de liaison réseau d’un des nœuds), cette discipline seule permet d’assurer la continuité et la traçabilité complète du parcours patient sans bloquer les systèmes locaux et sans rompre le pipeline.

- **Rattachement** : [CAP-13: Système d'information sanitaire, données et recherche](../../referentiel/capabilites/cap-13.md), [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../../referentiel/capabilites/cap-14.md).
- **Pattern cible** : Saga / Process Manager (transactions de compensation).

Ce chapitre se décline en quatre sous-chapitres :
- [ART-8A: Orchestration de processus borné](../../referentiel/chapitres/art-8a.md)
- [ART-8B: Modélisation de relations en graphe](../../referentiel/chapitres/art-8b.md)
- [ART-8C: Agrégation par lot](../../referentiel/chapitres/art-8c.md)
- [ART-8D: Chorégraphie inter-institutionnelle](../../referentiel/chapitres/art-8d.md)

*Rattachement : CAP-13, CAP-14 · fiche ART-8*

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`ART-8`** : Orchestration de processus (`referentiel/chapitres/art-8.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/03_chapitres/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
