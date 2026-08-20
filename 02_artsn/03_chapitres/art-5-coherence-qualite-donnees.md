---
title: "ART-5 : Cohérence et qualité des données"
id: art-5
domain: 02_artsn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-5, niveau-3]
related: ['cap-int-03']
---

# ART-5 : Cohérence et qualité des données

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


ART-5 : Cohérence et qualité des données constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `art-5`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Contenu normatif.** Tout flux ingéré doit être audité en continu face aux dimensions de qualité des données. En cas de détection d’anomalie, le système a l’obligation de router l’événement vers l’une des **branches d’escalade humaine** définies réglementairement. Les circuits cibles sont : sécurité clinique, alerte épidémiologique, fraude financière, risque intersectoriel.

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (données corrompues du terrain, anomalies massives de facturation) : elle seule permet d’aiguiller le problème vers la bonne cellule humaine de décision stratégique sans rompre le pipeline.

- **Rattachement** : CAP-13 (gestion des données sanitaires).
- **Référentiel cible** : DAMA/DMBOK.
- **Circuits cibles** : sécurité clinique, alerte épidémiologique, fraude financière, risque intersectoriel.
- **Déduit selon** : ENF-5 (coordination des processus).
- **Statut : Stable** (pour les métriques) / **Proposition ouverte** (pour la gouvernance des 4 branches).

*Rattachement : ENF-5, CAP-13 · fiche ART-5*

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`art-5`** : Cohérence et qualité des données (`referentiel/chapitres/art-5.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/03_chapitres/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
