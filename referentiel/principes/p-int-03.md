---
domain: principes
id: P-INT-03
type: principe
niveau: "2"
title: Copies locales non autoritatives
status: active
owner: DEPSI
version: "0.5"
envelope: 01_cnisn/01_principes/index.md
maps_to: ["CAP-14"]
implements: []
applies_to: []
related: ["CAP-INT-01", "CAP-INT-02", "CAP-INT-04", "CAP-INT-05", "CAP-INT-11"]
tags: ["cnisn", "niveau-2", "principe"]
---

# Copies locales non autoritatives

Des copies locales, caches, répliques ou extraits hors ligne peuvent être utilisés lorsque les besoins de performance, de résilience ou de connectivité le justifient.

Ces copies doivent être :

- explicitement non autoritatives ;
- associées à une source ;
- datées ;
- versionnées ;
- synchronisées ;
- soumises à une politique d’expiration ;
- remplacées ou réconciliées lorsqu’une version plus récente est disponible.

Une copie locale ne doit pas devenir implicitement une nouvelle source faisant autorité.
