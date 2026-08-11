---
title: "ART-8 — Orchestration de processus"
id: art-8
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-8, niveau-3]
---

# ART-8 — Orchestration de processus

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).


ART-8 — Orchestration de processus constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : [`art-8`](../../referentiel/chapitres/art-8.md).

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

**Contenu normatif.** Pour tout processus métier distribué, asynchrone et à étapes multiples, l’architecture impose l’utilisation d’un **gestionnaire de transactions longues**. Ce composant doit suivre l’état du parcours, maintenir la cohérence sans verrouiller les bases distantes, et déclencher obligatoirement des transactions d’annulation ou de correction en cas d’échec d’une étape.

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (établissements hospitaliers autonomes, cliniques privées, rupture de liaison réseau d’un des nœuds) : elle seule permet d’assurer la continuité et la traçabilité complète du parcours patient sans bloquer les systèmes locaux et sans rompre le pipeline.

- **Rattachement** : [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md).
- **Pattern cible** : Saga / Process Manager (transactions de compensation).

Ce chapitre se décline en quatre sous-chapitres :
- [ART-8a — Orchestration de processus borné](../../referentiel/chapitres/art-8a.md)
- [ART-8b — Modélisation de relations en graphe](../../referentiel/chapitres/art-8b.md)
- [ART-8c — Agrégation par lot](../../referentiel/chapitres/art-8c.md)
- [ART-8d — Chorégraphie inter-institutionnelle](../../referentiel/chapitres/art-8d.md)

*Rattachement : [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md) · [fiche](../../referentiel/chapitres/art-8.md)*

<!-- END:GENERATED -->
## Liens

- [Index des chapitres](./index.md)
- [Exigences contextuelles — Partie III](../02_exigences-contextuelles.md)
