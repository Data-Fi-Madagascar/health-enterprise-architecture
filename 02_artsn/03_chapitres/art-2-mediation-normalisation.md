---
title: "ART-2 — Médiation et normalisation"
id: art-2
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-2, niveau-3]
---

# ART-2 — Médiation et normalisation

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).


ART-2 — Médiation et normalisation constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : [`art-2`](../../referentiel/chapitres/art-2.md).

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

**Contenu normatif.** La plateforme doit intégrer un moteur de médiation capable de traduire, transformer et valider structurellement et sémantiquement les payloads hétérogènes du terrain en messages canoniques standardisés. Ce moteur doit obligatoirement s’adosser à des dictionnaires de référence nationaux et internationaux uniques : concepts cliniques, biologie/laboratoire, et classification des maladies.

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (multiplicité d’éditeurs de logiciels, silos applicatifs d’ONG) : elle seule permet de garantir que les données partagent le même sens médical et la même structure technique sans rompre le pipeline.

- **Rattachement** : [CAP-14](../../referentiel/capabilites/cap-14.md) (interopérabilité et infrastructure partagée).
- **Déduit selon** : [ENF-3](../../referentiel/exigences/enf-3.md) (fragmentation applicative) et [ENF-4](../../referentiel/exigences/enf-4.md) (One Health).
- **Statut : Stable.**

*Rattachement : [ENF-3](../../referentiel/exigences/enf-3.md), [ENF-4](../../referentiel/exigences/enf-4.md), [CAP-14](../../referentiel/capabilites/cap-14.md) · [fiche](../../referentiel/chapitres/art-2.md)*

<!-- END:GENERATED -->
## Liens

- [Index des chapitres](./index.md)
- [Exigences contextuelles — Partie III](../02_exigences-contextuelles/index.md)
