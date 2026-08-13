---
id: cmp-15
type: composant-applicatif
niveau: "1"
title: CMP-15 — API Gateway
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/04_cartographie-cible.md
maps_to: ["cap-int-10"]
implements: ["art-5"]
applies_to: ["prc-04", "prc-05", "prc-06"]
related: ["enf-3", "cap-10", "vs-02"]
tags: ["artsn", "niveau-1", "composant-applicatif", "cmp-15", "couche-3"]
---
# CMP-15 — API Gateway

**Contenu normatif.** Point d'entrée unique pour toutes les requêtes API. Assure la gestion des flux, l'authentification, la limitation de débit et la routage. Garantit la sécurité et la performance des échanges inter-systèmes.

**Discipline existentielle.** Gardien de la plateforme. Toute requête externe ou inter-systèmes transite par cet point. Garantit la sécurité, la disponibilité et la conformité des échanges.

- **Rattachement** : [ART-5](../chapitres/art-5.md) (routeur d'escalade), [CAP-INT-10](../capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-04](../processus/prc-04.md) (soins), [PRC-05](../processus/prc-05.md) (pharmacie), [PRC-06](../processus/prc-06.md) (logistique).
- **Statut : Stable.**