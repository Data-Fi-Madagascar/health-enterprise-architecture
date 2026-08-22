---

title: "Résolution d'identité"
id: artsn-ART-4A
domain: 03_chapitres
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: ["artsn", "chapitres", "ART-4A", "niveau-3"]
related: ["CAP-INT-01"]
---

# Résolution d'identité

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


ART-4a : Résolution d'identité constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `ART-4A`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Contenu normatif.** La plateforme doit intégrer un index centralisé chargé d’exécuter des algorithmes de **rapprochement démographique** sur les attributs transmis par le terrain. Ce système doit réconcilier les fiches incomplètes avec le flux civil pour consolider un enregistrement unique (*Golden Record*) et attribuer le **matricule national** (Identifiant National de Santé, INS).

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (erreurs de saisie manuelle, variations phonétiques des patronymes, logiciels distants en silos), cette discipline seule permet d’éviter l’attribution de données cliniques au mauvais patient et de bloquer les accidents médicaux sans rompre le pipeline.

- **Rattachement** : [CAP-04bis](../07_annexes/c-renvoi-capacites-candidates.md) (engagement patient et identitovigilance).
- **Concepts cibles** : Golden Record, Identifiant National de Santé (INS).
- **Déduit selon** : [ENF-3: Unicité de l'identité et résilience face à la fragmentation applicative](../../referentiel/exigences/enf-3.md) (unicité de l’identité).
- **Statut : Provisoire.**

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`ART-4A`** : Résolution d'identité (`referentiel/chapitres/art-4a.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/03_chapitres/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
