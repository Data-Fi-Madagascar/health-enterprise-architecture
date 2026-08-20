---
title: "ART-1 : Intégration et ingestion"
id: art-1
domain: 02_artsn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-1, niveau-3]
related: ['cap-int-03']
---

# ART-1 : Intégration et ingestion

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


ART-1 : Intégration et ingestion constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `art-1`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Contenu normatif.** Tout flux entrant doit transiter par un point d’accès central unique qui garantit l’authentification forte de la source, la validation d’intégrité, la limitation de débit (*rate limiting*) et la distribution asynchrone des messages selon un contrat de livraison au moins une fois (*at-least-once*). Le système doit supporter nativement trois topologies d’ingestion : **Point à point**, **Diffusion** (*fan-out*) et **Interrogation fédérée** (*pull*).

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (logiciels hospitaliers privés, applications mobiles terrain) : elle seule permet de protéger les serveurs centraux contre les saturations, les cyberattaques et les pertes de données induites par les micro-coupures réseau sans rompre le pipeline.

- **Rattachement** : CAP-14 (interopérabilité et infrastructure partagée).
- **Déduit selon** : ENF-1 (instabilité réseau).
- **Statut : Stable.**

*Rattachement : ENF-1, CAP-14 · fiche ART-1*

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`art-1`** : Intégration et ingestion (`referentiel/chapitres/art-1.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/03_chapitres/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
