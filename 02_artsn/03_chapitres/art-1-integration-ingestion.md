---
title: ART-1 — Intégration et ingestion
id: art-1-integration-ingestion
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-1, ingestion, niveau-3]
---

# ART-1 — Intégration et ingestion

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

**Contenu normatif.** Tout flux entrant doit transiter par un point d'accès central unique qui garantit l'authentification forte de la source, la validation d'intégrité, la limitation de débit (*rate limiting*) et la distribution asynchrone des messages selon un contrat de livraison au moins une fois (*at-least-once*). Le système doit supporter nativement trois topologies d'ingestion : **Point à point**, **Diffusion** (*fan-out*) et **Interrogation fédérée** (*pull*).

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (logiciels hospitaliers privés, applications mobiles terrain) : elle seule permet de protéger les serveurs centraux contre les saturations, les cyberattaques et les pertes de données induites par les micro-coupures réseau sans rompre le pipeline.

- **Rattachement** : [CAP-14](../../00_caesn/03_capabilities/index.md) (interopérabilité et infrastructure partagée).
- **Déduit selon** : [ENF-1](../02_exigences-contextuelles.md#enf-1--résilience-à-l-instabilité-réseau) (instabilité réseau).
- **Statut : Stable.**

## Liens

- [Index des chapitres](./index.md)
- [Exigences contextuelles — ENF-1](../02_exigences-contextuelles.md)
- [Couche 3 — Échange, transport et ingestion](../04_cartographie-cible.md)
