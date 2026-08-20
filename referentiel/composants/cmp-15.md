---
id: CMP-15
type: composant-applicatif
niveau: "1"
title: API Gateway
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/index.md
maps_to: ["CAP-INT-10"]
implements: ["ART-5"]
applies_to: ["PRC-04", "PRC-05", "PRC-06"]
related: ["ENF-3", "CAP-10", "VS-02"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-15", "couche-3"]
---
# API Gateway

**Contenu normatif.** Ce composant constitue le point d'entrée unique pour toutes les requêtes API. Il assure la gestion des flux, l'authentification, la limitation de débit et le routage, et garantit la sécurité et la performance des échanges inter-systèmes.

**Discipline de mise en œuvre.** Il est le gardien de la plateforme. Toute requête externe ou inter-systèmes transite par ce point, ce qui garantit la sécurité, la disponibilité et la conformité des échanges.

- **Rattachement** : [ART-5](../chapitres/art-5.md) (routeur d'escalade), [CAP-INT-10: Provenance, audit et traçabilité](../capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../processus/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../processus/prc-06.md) (logistique).
- **Statut : Stable.**