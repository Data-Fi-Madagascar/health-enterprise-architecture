---
id: p-int-20
type: principe
niveau: "2"
title: P-INT-20 — Portabilité et réversibilité
status: active
owner: DEPSI
version: "0.5"
source: 01_cnisn/01_principes.md
maps_to: ["cap-14"]
implements: []
applies_to: []
related: ["cap-int-03", "cap-int-07", "cap-int-08", "cap-int-12"]
tags: ["cnisn", "niveau-2", "principe"]
---

# P-INT-20 — Portabilité et réversibilité

Toute initiative doit prévoir la possibilité de :

- récupérer ses données ;
- récupérer ses configurations essentielles ;
- documenter ses contrats ;
- migrer vers une autre implémentation ;
- continuer à exploiter les données après changement de fournisseur ;
- éviter les formats propriétaires non documentés.

La stratégie de sortie doit être définie avant la mise en production des services critiques.
