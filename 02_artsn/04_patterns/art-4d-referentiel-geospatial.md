---

title: "Référentiel géospatial et d'exploitation partagé"
id: artsn-ART-4D
domain: 04_patterns
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: ["artsn", "chapitres", "ART-4D", "niveau-3"]
related: ["CAP-INT-04"]
---

# Référentiel géospatial et d'exploitation partagé

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


ART-4D : Référentiel géospatial et d'exploitation partagé constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `ART-4D`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Statut : candidate**

**Contenu normatif.** L’architecture doit fournir une **clé de rapprochement universelle** basée exclusivement sur des coordonnées spatiales ou codes de zones et des périodes de temps. Ce référentiel neutre est le **seul point de contact autorisé** pour croiser des bases de données sectorielles hétérogènes.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (bases de données météorologiques, registres de suivi des cheptels d’élevage), cette discipline seule permet de corréler des indicateurs environnementaux et cliniques sans jamais interconnecter les identités humaines, garantissant l’étanchéité One Health sans rompre le pipeline.

- **Rattachement** : capacité candidate « Surveillance spatio-temporelle ».
- **Déduit selon** : [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../../referentiel/exigences/enf-4.md) (cloisonnement inter-institutionnel).
- **Statut : Proposition ouverte.**

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`ART-4D`** : Référentiel géospatial et d'exploitation partagé (`referentiel/chapitres/art-4d.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/04_patterns/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
