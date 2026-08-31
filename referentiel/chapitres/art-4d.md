---
domain: chapitres

id: ART-4D
type: chapitre
niveau: "3"
title: Référentiel géospatial et d'exploitation partagé
status: candidate
maturity_condition: "Confirmation par une initiative intersectorielle"
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-4d-referentiel-geospatial.md
maps_to: []
implements: []
applies_to: ["ENF-4"]
related: ["ART-4"]
tags: ["artsn", "niveau-3", "chapitre", "ART-4D"]
---
# Référentiel géospatial et d’exploitation partagé

**Contenu normatif.** L’architecture doit fournir une **clé de rapprochement universelle** basée exclusivement sur des coordonnées spatiales ou codes de zones et des périodes de temps. Ce référentiel neutre est le **seul point de contact autorisé** pour croiser des bases de données sectorielles hétérogènes.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (bases de données météorologiques, registres de suivi des cheptels d’élevage), cette discipline seule permet de corréler des indicateurs environnementaux et cliniques sans jamais interconnecter les identités humaines, garantissant l’étanchéité One Health sans rompre le pipeline.

- **Rattachement** : capacité candidate « Surveillance spatio-temporelle ».
- **Déduit selon** : [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../exigences/enf-4.md) (cloisonnement inter-institutionnel).
- **Statut : Proposition ouverte.**

## Profils PTISN qui implémentent ce chapitre

Les profils techniques nationaux ci-dessous déclarent implémenter ce chapitre ART dans leur champ `implements` (frontmatter du référentiel). Le profil constitue la spécification implémentable et testable ; le chapitre demeure le cadre normatif opposable.

- [PT-15 : Surveillance One Health](../profils/pt-15.md)

