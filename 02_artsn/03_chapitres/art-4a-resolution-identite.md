---
title: "ART-4a — Résolution d'identité"
id: art-4a
domain: 02_artsn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-4a, niveau-3]
related: ['cap-int-01']
---

# ART-4a — Résolution d'identité

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.


ART-4a — Résolution d'identité constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `art-4a`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

**Contenu normatif.** La plateforme doit intégrer un index centralisé chargé d’exécuter des algorithmes de **rapprochement démographique** sur les attributs transmis par le terrain. Ce système a l’obligation de réconcilier les fiches incomplètes avec le flux civil pour consolider un enregistrement unique (*Golden Record*) et attribuer le **matricule national** (Identifiant National de Santé, INS).

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (erreurs de saisies manuelles, variations phonétiques des patronymes, logiciels distants en silos) : elle seule permet d’éviter l’attribution de données cliniques au mauvais patient et de bloquer les accidents médicaux sans rompre le pipeline.

- **Rattachement** : CAP-04bis (engagement patient et identitovigilance).
- **Concepts cibles** : Golden Record, Identifiant National de Santé (INS).
- **Déduit selon** : ENF-3 (unicité de l’identité).
- **Statut : Provisoire.**

*Rattachement : ENF-3, CAP-04 · fiche ART-4A*

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles — Partie III

## Références

- **matrice de lecture** — Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`art-4a`** — Résolution d'identité (`referentiel/chapitres/art-4a.md`)
- **Index des chapitres** — Chapitres et patterns de référence (`02_artsn/03_chapitres/index.md`)
- **Exigences contextuelles — Partie III** — Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
