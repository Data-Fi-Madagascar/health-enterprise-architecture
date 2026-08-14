---
id: cmp-06
type: composant-applicatif
niveau: "1"
title: CMP-06 — Intégration, Médiation, API Gateway, Broker & Registre schémas
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/04_cartographie-cible/index.md
maps_to: ["cap-int-01", "cap-int-03"]
implements: ["art-1", "art-2", "f-3"]
applies_to: []
related: ["enf-1", "enf-3", "cap-13", "cap-14", "cap-15", "vs-01", "vs-02", "vs-03", "vs-04"]
tags: ["artsn", "niveau-1", "composant-applicatif", "cmp-06", "couche-4"]
---
# CMP-06 — Intégration, Médiation, API Gateway, Broker & Registre schémas

**Contenu normatif.** Point d'entrée unique de la plateforme : API Gateway (contrats, throttling, authentification), message broker asynchrone (files d'attente, durabilité), registre de schémas (F.3 — versioning, compatibilité ascendante/descendante), moteur de médiation sémantique (ART-2 — transformation, normalisation, enrichissement).

**Discipline existentielle.** Bordure de la plateforme ; tout flux entrant/sortant traverse ce composant. Garantit l'éradication des silos (F.3) et la conformité aux contrats (ENF-1, ENF-3).

- **Rattachement** : [ART-1](../chapitres/art-1.md) (ingestion), [ART-2](../chapitres/art-2.md) (médiation), [F.3](../fondations/f-3.md) (schémas), [CAP-INT-01](../capacites/cap-int-01.md), [CAP-INT-03](../capacites/cap-int-03.md).
- **Statut : Stable.**