---
id: P-INT-16
type: principe
niveau: "2"
title: Résidence et non-réplication
status: active
owner: DEPSI
version: "0.5"
envelope: 01_cnisn/01_principes/index.md
maps_to: ["CAP-14", "CAP-15"]
implements: []
applies_to: []
related: ["CAP-INT-01", "CAP-INT-08", "CAP-INT-09"]
tags: ["cnisn", "niveau-2", "principe"]
---

# Résidence et non-réplication

Toute contrainte de résidence doit être respectée.

Lorsqu’une donnée ne doit pas quitter son système ou son institution d’origine, l’architecture doit privilégier :

- l’interrogation fédérée ;
- l’agrégation à la source ;
- la transmission d’un résultat minimisé ;
- la pseudonymisation ;
- la transmission d’une preuve plutôt que de la donnée complète.

Une copie ne doit pas être créée uniquement parce qu’elle est techniquement possible.
