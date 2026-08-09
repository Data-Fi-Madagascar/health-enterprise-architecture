---
title: ART-2 — Médiation et normalisation
id: art-2-mediation-normalisation
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-2, mediation, normalisation, niveau-3]
---

# ART-2 — Médiation et normalisation

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

**Contenu normatif.** La plateforme doit intégrer un moteur de médiation capable de traduire, transformer et valider structurellement et sémantiquement les payloads hétérogènes du terrain en messages canoniques standardisés. Ce moteur doit obligatoirement s'adosser à des dictionnaires de référence nationaux et internationaux uniques : concepts cliniques, biologie/laboratoire, et classification des maladies.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (multiplicité d'éditeurs de logiciels, silos applicatifs d'ONG) : elle seule permet de garantir que les données partagent le même sens médical et la même structure technique sans rompre le pipeline.

- **Rattachement** : [CAP-14](../../00_caesn/03_capabilities/index.md) (interopérabilité et infrastructure partagée).
- **Déduit selon** : [ENF-3](../02_exigences-contextuelles.md#enf-3--unicité-de-l-identité-et-résilience-face-à-la-fragmentation-applicative) (fragmentation applicative) et [ENF-4](../02_exigences-contextuelles.md#enf-4--cloisonnement-inter-institutionnel-et-étanchéité-des-données-one-health) (One Health).
- **Statut : Stable.**

## Liens

- [Index des chapitres](./index.md)
- [Exigences contextuelles — ENF-3](../02_exigences-contextuelles.md)
- [Couche 4 — Interopérabilité et services partagés](../04_cartographie-cible.md)
