---

id: ART-1
type: chapitre
niveau: "3"
title: Intégration et ingestion
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/03_chapitres/art-1-integration-ingestion.md
maps_to: ["CAP-14"]
implements: []
applies_to: ["ENF-1"]
related: []
tags: ["artsn", "niveau-3", "chapitre", "ART-1"]
---
# Intégration et ingestion

**Contenu normatif.** Tout flux entrant doit transiter par un point d’accès central unique qui garantit l’authentification forte de la source, la validation d’intégrité, la limitation de débit (*rate limiting*) et la distribution asynchrone des messages selon un contrat de livraison au moins une fois (*at-least-once*). Le système doit supporter nativement trois topologies d’ingestion : **Point à point**, **Diffusion** (*fan-out*) et **Interrogation fédérée** (*pull*).

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (logiciels hospitaliers privés, applications mobiles terrain), cette discipline seule permet de protéger les serveurs centraux contre les saturations, les cyberattaques et les pertes de données induites par les micro-coupures réseau sans rompre le pipeline.

- **Rattachement** : [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../capabilites/cap-14.md) (interopérabilité et infrastructure partagée).
- **Déduit selon** : [ENF-1: Résilience à l'instabilité réseau](../exigences/enf-1.md) (instabilité réseau).
- **Statut : Stable.**
