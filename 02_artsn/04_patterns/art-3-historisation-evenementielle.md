---

title: "Historisation événementielle et profils de déploiement"
id: artsn-ART-3
domain: 04_patterns
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
- **Normes CNISN** : [STD-0003: X-Road](../../01_cnisn/05_standards/std-0003-x-road.md) (transport inter-institutionnel, [ADR-0001](../../01_cnisn/06_decisions/adr-0001-x-road.md)), [STD-0002: Sécurité et chiffrement](../../01_cnisn/05_standards/std-0002-securite-chiffrement.md).
- **Objets de données** : [BO-01 Patient & identité](../../00_caesn/04_data/objets.md), [BO-02 Prestation & soins](../../00_caesn/04_data/objets.md), [BO-05 Risque & surveillance](../../00_caesn/04_data/objets.md), [BO-06 Exploitation & gestion](../../00_caesn/04_data/objets.md) (objets métier CAESN) ; voir aussi le [dictionnaire des objets de données ARTSN](../03_objets-de-donnees/index.md).
- **Profils cibles** : Profil A, Profil B, Profil C.
- **Déduit selon** : [ENF-1: Résilience à l'instabilité réseau](../../referentiel/exigences/enf-1.md) (mode déconnecté).
- **Statut : Stable.**

## Profils PTISN qui implémentent ce chapitre

Les profils techniques nationaux ci-dessous déclarent implémenter ce chapitre ART dans leur champ `implements` (frontmatter du référentiel). Le profil constitue la spécification implémentable et testable ; le chapitre demeure le cadre normatif opposable.

- [PT-09 : Analytique et exposition de données](../../referentiel/profils/pt-09.md)
- [PT-12 : Audit, provenance et traçabilité](../../referentiel/profils/pt-12.md)

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`ART-3`** : Historisation événementielle et profils de déploiement (`referentiel/chapitres/art-3.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/04_patterns/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
