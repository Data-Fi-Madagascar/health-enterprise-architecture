---

title: "Chorégraphie inter-institutionnelle"
id: artsn-ART-8D
domain: 02_artsn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: ["artsn", "chapitres", "ART-8D", "niveau-3"]
related: ["CAP-INT-03"]
---

# Chorégraphie inter-institutionnelle

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


ART-8d : Chorégraphie inter-institutionnelle constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `ART-8D`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Contenu normatif.** Lorsque l’intégration implique plusieurs ministères co-égaux, l’architecture **proscrit l’orchestration centralisée** et impose un modèle de coordination par messagerie décentralisée. Les systèmes partenaires doivent s’abonner de manière autonome à des files d’événements publics sans qu’aucun nœud n’ait d’autorité informatique sur le système de l’autre (pattern cible : Publication/Abonnement, Pub/Sub).

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (systèmes d’information autonomes des ministères de l’Agriculture ou de l’Environnement), cette discipline seule permet de déclencher des actions conjointes et simultanées lors d’un signal épidémique tout en préservant l’indépendance informatique et la souveraineté de chaque institution, sans rompre le pipeline.

- **Rattachement** : [CAP-13: Système d'information sanitaire, données et recherche](../../referentiel/capabilites/cap-13.md), [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../../referentiel/capabilites/cap-14.md).
- **Pattern cible** : Publication / Abonnement (Pub/Sub).
- **Déduit selon** : [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../../referentiel/exigences/enf-4.md) (souveraineté intersectorielle).
- **Statut : Proposition ouverte.**

*Rattachement : ENF-4, CAP-13, CAP-14 · fiche ART-8D*

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`ART-8D`** : Chorégraphie inter-institutionnelle (`referentiel/chapitres/art-8d.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/03_chapitres/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
