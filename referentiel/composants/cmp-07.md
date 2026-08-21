---
domain: composants
id: CMP-07
type: composant-applicatif
niveau: "1"
title: Orchestrateur de parcours & Gestionnaire de Sagas (ART-8a)
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/composants.md
maps_to: ["CAP-INT-08"]
implements: ["ART-8A"]
applies_to: ["PRC-04", "PRC-05", "PRC-06"]
related: ["ENF-3", "CAP-08", "VS-02"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-07", "couche-4"]
---
# Orchestrateur de parcours & Gestionnaire de Sagas (ART-8a)

**Contenu normatif.** Ce composant orchestre les flux inter-systèmes en gérant les transactions distribuées (Sagas) et les compensations. Il garantit la cohérence des parcours patient à travers les institutions, les systèmes et les départements. Il assure la résilience des workflows cliniques critiques.

**Discipline de mise en œuvre.** Il est le point de coordination central de tous les flux transactionnels : toute opération multi-systèmes transite par cet orchestrateur. Il garantit l'atomicité logique des parcours complexes.

- **Rattachement** : [ART-8a](../chapitres/art-8a.md) (orchestrateur de parcours), [CAP-INT-08: Confiance, sécurité et autorisation](../capacites/cap-int-08.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../processus/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../processus/prc-06.md) (logistique).
- **Statut : Stable.**