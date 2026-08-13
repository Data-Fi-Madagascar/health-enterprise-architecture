---
id: cmp-07
type: composant-applicatif
niveau: "1"
title: CMP-07 — Orchestrateur de parcours & Gestionnaire de Sagas (ART-8a)
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/04_cartographie-cible.md
maps_to: ["cap-int-08"]
implements: ["art-8a"]
applies_to: ["prc-04", "prc-05", "prc-06"]
related: ["enf-3", "cap-08", "vs-02"]
tags: ["artsn", "niveau-1", "composant-applicatif", "cmp-07", "couche-4"]
---
# CMP-07 — Orchestrateur de parcours & Gestionnaire de Sagas (ART-8a)

**Contenu normatif.** Orchestre les flux inter-systèmes en gérant les transactions distribuées (Sagas) et les compensations. Garantit la cohérence des parcours patient跨机构跨系统跨部门. Assure la résilience des workflows cliniques critiques.

**Discipline existentielle.** Point de coordination central pour tous les flux transactionnels : toute opération multi-systèmes transite par cet orchestrateur. Garantit l'atomicité logique des parcours complexes.

- **Rattachement** : [ART-8a](../chapitres/art-8a.md) (orchestrateur de parcours), [CAP-INT-08](../capacites/cap-int-08.md).
- **Processus soutenus** : [PRC-04](../processus/prc-04.md) (soins), [PRC-05](../processus/prc-05.md) (pharmacie), [PRC-06](../processus/prc-06.md) (logistique).
- **Statut : Stable.**