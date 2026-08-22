---

title: "Analytique et restitution"
id: artsn-ART-6
domain: 03_chapitres
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: ["artsn", "chapitres", "ART-6", "niveau-3"]
related: ["CAP-INT-07"]
---

# Analytique et restitution

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


ART-6 : Analytique et restitution constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `ART-6`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Contenu normatif.** L’architecture doit imposer une **séparation étanche entre le stockage opérationnel et le stockage analytique** (CQRS). L’entrepôt analytique doit être alimenté par des pipelines automatisés intégrant un moteur de masquage irréversible, et doit supporter nativement quatre types de requêtes : projections tabulaires, parcours de graphes, réconciliation comptable et fusion de signaux géospatiaux.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (requêtes lourdes des décideurs, extractions massives pour la recherche), cette discipline seule permet de garantir des performances de restitution constantes et une sécurité réglementaire absolue sans surcharger les serveurs de soins et sans rompre le pipeline.

- **Rattachement** : [CAP-13: Système d'information sanitaire, données et recherche](../../referentiel/capabilites/cap-13.md), [CAP-08: Gouvernance institutionnelle, planification, coordination et redevabilité](../../referentiel/capabilites/cap-08.md) (analytics & décisionnel).
- **Infrastructure cible** : Data Lakehouse.
- **Pattern cible** : modèle de séparation CQRS.
- **Déduit selon** : [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../../referentiel/exigences/enf-4.md) (protection One Health).
- **Statut : Provisoire.**

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`ART-6`** : Analytique et restitution (`referentiel/chapitres/art-6.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/03_chapitres/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
