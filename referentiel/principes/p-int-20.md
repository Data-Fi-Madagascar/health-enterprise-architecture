---
id: P-INT-20
type: principe
niveau: "2"
title: Portabilité et réversibilité
status: active
owner: DEPSI
version: "0.5"
envelope: 01_cnisn/01_principes/index.md
maps_to: ["CAP-14"]
implements: []
applies_to: []
related: ["CAP-INT-03", "CAP-INT-07", "CAP-INT-08", "CAP-INT-12"]
tags: ["cnisn", "niveau-2", "principe"]
---

# Portabilité et réversibilité

Toute initiative doit prévoir la possibilité de :

- récupérer ses données ;
- récupérer ses configurations essentielles ;
- documenter ses contrats ;
- migrer vers une autre implémentation ;
- continuer à exploiter les données après changement de fournisseur ;
- éviter les formats propriétaires non documentés.

La stratégie de sortie doit être définie avant la mise en production des services critiques.
