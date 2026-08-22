---

title: "Historisation événementielle et profils de déploiement"
id: artsn-ART-3
domain: 03_chapitres
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: ["artsn", "chapitres", "ART-3", "niveau-3"]
related: ["CAP-INT-03"]
---

# Historisation événementielle et profils de déploiement

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


ART-3 : Historisation événementielle et profils de déploiement constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `ART-3`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Contenu normatif.** Le stockage de la donnée de santé doit être structuré sous forme de **journal d’événements ordonnés, non modifiables et cumulatifs**, agissant comme la source unique de vérité opérationnelle (event sourcing). L’architecture doit supporter trois profils d’intégration :

1. **Profil A** — historisation analytique en dérivation (*side-car*) ;
2. **Profil B** — système opérationnel natif ;
3. **Profil C** — fédération de réception tierce.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (bases de données locales distribuées, serveurs de districts isolés), cette discipline seule permet de rejouer l’historique complet d’un dossier patient ou de reconstruire un nœud après un sinistre matériel sans rompre le pipeline.

- **Rattachement** : [CAP-13: Système d'information sanitaire, données et recherche](../../referentiel/capabilites/cap-13.md) (gestion des données sanitaires).
- **Profils cibles** : Profil A, Profil B, Profil C.
- **Déduit selon** : [ENF-1: Résilience à l'instabilité réseau](../../referentiel/exigences/enf-1.md) (mode déconnecté).
- **Statut : Stable.**

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`ART-3`** : Historisation événementielle et profils de déploiement (`referentiel/chapitres/art-3.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/03_chapitres/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
