---

title: "ART-9 : Garanties transactionnelles fortes"
id: ART-9
domain: 02_artsn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: ["artsn", "chapitres", "ART-9", "niveau-3"]
related: ["CAP-INT-07"]
---

# ART-9 : Garanties transactionnelles fortes

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


ART-9 : Garanties transactionnelles fortes constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `ART-9`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Contenu normatif.** Pour tout mouvement de valeur monétaire ou physique, l’architecture impose une contrainte de **grade comptable strict** basée sur un registre immuable, garantissant l’équilibre parfait des comptes (équation cible : *entrées − sorties = solde*). Toute écriture doit être associée à une signature non répudiable et un numéro de suivi de lot.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (officines pharmaceutiques privées, gestionnaires de stocks régionaux, caisses de subventions), cette discipline seule permet d’empêcher les détournements de médicaments, de bloquer les marchés noirs et d’assurer la réconciliation à somme nulle de l’argent public, sans rompre le pipeline.

- **Rattachement** : recouvre partiellement [CAP-07: Protection financière, couverture santé universelle](../../referentiel/capabilites/cap-07.md) (protection financière).
- **Équation cible** : entrées − sorties = solde.
- **Déduit selon** : [ENF-2: Intégrité des flux et traçabilité des valeurs](../../referentiel/exigences/enf-2.md) (grade comptable anti-fraude).
- **Statut : Proposition ouverte.**

*Rattachement : ENF-2, CAP-07 · fiche ART-9*

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`ART-9`** : Garanties transactionnelles fortes (`referentiel/chapitres/art-9.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/03_chapitres/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
