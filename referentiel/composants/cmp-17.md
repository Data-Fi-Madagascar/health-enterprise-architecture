---
id: cmp-17
type: composant-applicatif
niveau: "1"
title: CMP-17 — Message broker asynchrone
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/04_cartographie-cible.md
maps_to: ["cap-int-10"]
implements: ["art-5"]
applies_to: ["prc-04", "prc-05", "prc-06"]
related: ["enf-3", "cap-10", "vs-02"]
tags: ["artsn", "niveau-1", "composant-applicatif", "cmp-17", "couche-3"]
---
# CMP-17 — Message broker asynchrone

**Contenu normatif.** Gère les échanges asynchrones entre les systèmes. Assure la persistance tampon et la distribution des messages. Garantit la résilience et la fiabilité des communications inter-systèmes.

**Discipline existentielle.** Mécanisme de déconnexion des systèmes. Permet la communication même en cas de défaillance temporaire d'un composant. Garantit la continuité des échanges.

- **Rattachement** : [ART-5](../chapitres/art-5.md) (routeur d'escalade), [CAP-INT-10](../capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-04](../processus/prc-04.md) (soins), [PRC-05](../processus/prc-05.md) (pharmacie), [PRC-06](../processus/prc-06.md) (logistique).
- **Statut : Stable.**