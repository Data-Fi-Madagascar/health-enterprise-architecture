---
id: p-int-03
type: principe
niveau: "2"
title: P-INT-03 — Copies locales non autoritatives
status: active
owner: DEPSI
version: "0.5"
source: 01_cnisn/01_principes/index.md
maps_to: ["cap-14"]
implements: []
applies_to: []
related: ["cap-int-01", "cap-int-02", "cap-int-04", "cap-int-05", "cap-int-11"]
tags: ["cnisn", "niveau-2", "principe"]
---

# P-INT-03 — Copies locales non autoritatives

Des copies locales, caches, répliques ou extraits hors ligne peuvent être utilisés lorsque les besoins de performance, de résilience ou de connectivité le justifient.

Ces copies doivent être :

- explicitement non autoritatives ;
- associées à une source ;
- datées ;
- versionnées ;
- synchronisées ;
- soumises à une politique d’expiration ;
- remplacées ou réconciliées lorsqu’une version plus récente est disponible.

Une copie locale ne doit pas devenir implicitement une nouvelle source faisant autorité.
