---

title: "Intégration et ingestion"
id: artsn-ART-1
domain: 04_patterns
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: ["artsn", "chapitres", "ART-1", "niveau-3"]
related: ["CAP-INT-03"]
---

# Intégration et ingestion

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


ART-1 : Intégration et ingestion constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `ART-1`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Contenu normatif.** Tout flux entrant doit transiter par un point d’accès central unique qui garantit l’authentification forte de la source, la validation d’intégrité, la limitation de débit (*rate limiting*) et la distribution asynchrone des messages selon un contrat de livraison au moins une fois (*at-least-once*). Le système doit supporter nativement trois topologies d’ingestion : **Point à point**, **Diffusion** (*fan-out*) et **Interrogation fédérée** (*pull*).

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (logiciels hospitaliers privés, applications mobiles terrain), cette discipline seule permet de protéger les serveurs centraux contre les saturations, les cyberattaques et les pertes de données induites par les micro-coupures réseau sans rompre le pipeline.

- **Rattachement** : [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../../referentiel/capabilites/cap-14.md) (interopérabilité et infrastructure partagée).
- **Déduit selon** : [ENF-1: Résilience à l'instabilité réseau](../../referentiel/exigences/enf-1.md) (instabilité réseau).
- **Statut : Stable.**

## Profils PTISN qui implémentent ce chapitre

Les profils techniques nationaux ci-dessous déclarent implémenter ce chapitre ART dans leur champ `implements` (frontmatter du référentiel). Le profil constitue la spécification implémentable et testable ; le chapitre demeure le cadre normatif opposable.

- [PT-01 : Échange interinstitutionnel](../../referentiel/profils/pt-01.md)
- [PT-02 : Médiation intra-secteur](../../referentiel/profils/pt-02.md)
- [PT-03 : Catalogue des services et registre des contrats](../../referentiel/profils/pt-03.md)
- [PT-08 : Échange de données agrégées](../../referentiel/profils/pt-08.md)
- [PT-14 : Interopérabilité transfrontalière](../../referentiel/profils/pt-14.md)

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`ART-1`** : Intégration et ingestion (`referentiel/chapitres/art-1.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/04_patterns/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
