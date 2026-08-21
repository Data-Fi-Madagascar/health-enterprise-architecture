---
domain: composants
id: CMP-06
type: composant-applicatif
niveau: "1"
title: Intégration, Médiation, API Gateway, Broker & Registre schémas
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/composants.md
maps_to: ["CAP-INT-01", "CAP-INT-03"]
implements: ["ART-1", "ART-2", "F-3"]
applies_to: []
related: ["ENF-1", "ENF-3", "CAP-13", "CAP-14", "CAP-15", "VS-01", "VS-02", "VS-03", "VS-04"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-06", "couche-4"]
---
# Intégration, Médiation, API Gateway, Broker & Registre schémas

**Contenu normatif.** Ce composant constitue le point d'entrée unique de la plateforme : API Gateway (contrats, throttling, authentification), message broker asynchrone (files d'attente, durabilité), registre de schémas (F.3 — versioning, compatibilité ascendante/descendante) et moteur de médiation sémantique ([ART-2](../chapitres/art-2.md) transformation, normalisation, enrichissement).

**Discipline de mise en œuvre.** Il forme la bordure de la plateforme ; tout flux entrant ou sortant le traverse. Il garantit l'éradication des silos (F.3) et la conformité aux contrats ([ENF-1: Résilience à l'instabilité réseau](../exigences/enf-1.md), [ENF-3: Unicité de l'identité et résilience face à la fragmentation applicative](../exigences/enf-3.md)).

- **Rattachement** : [ART-1](../chapitres/art-1.md) (ingestion), [ART-2](../chapitres/art-2.md) (médiation), [F.3](../fondations/f-3.md) (schémas), [CAP-INT-01: Résolution d’identité du bénéficiaire](../capacites/cap-int-01.md), [CAP-INT-03: Échange et médiation inter-systèmes](../capacites/cap-int-03.md).
- **Statut : Stable.**
