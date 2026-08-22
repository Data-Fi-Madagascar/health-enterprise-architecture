---
domain: composants
id: CMP-17
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Message broker asynchrone
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/composants.md
maps_to: ["CAP-INT-10"]
implements: ["ART-5"]
uses: ["CMP-26", "CMP-27", "CMP-28", "CMP-29", "CMP-30", "CMP-31", "CMP-32", "CMP-33", "CMP-34", "CMP-35", "CMP-36", "CMP-37", "CMP-38"]
applies_to: ["PRC-04", "PRC-05", "PRC-06"]
related: ["ENF-3", "CAP-10", "VS-02"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-17", "couche-3"]
---
# Message broker asynchrone

**Contenu normatif.** Ce composant gère les échanges asynchrones entre les systèmes. Il assure la persistance tampon et la distribution des messages, et garantit la résilience et la fiabilité des communications inter-systèmes.

**Discipline de mise en œuvre.** Il est le mécanisme de déconnexion des systèmes. Il permet la communication même en cas de défaillance temporaire d'un composant, ce qui garantit la continuité des échanges.

- **Rattachement** : [ART-5](../chapitres/art-5.md) (routeur d'escalade), [CAP-INT-10: Provenance, audit et traçabilité](../capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../processus/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../processus/prc-06.md) (logistique).
- **Statut : Stable.**