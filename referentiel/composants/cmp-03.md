---
id: cmp-03
type: composant-applicatif
niveau: "1"
title: CMP-03 — Entrepôt Lakehouse & Projections analytiques (pipeline ETL, Lakehouse, projections)
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/04_cartographie-cible.md
maps_to: ["cap-int-07", "cap-int-11"]
implements: ["art-6", "art-9"]
applies_to: ["prc-09", "prc-11"]
related: ["enf-5", "cap-13", "cap-16", "vs-04"]
tags: ["artsn", "niveau-1", "composant-applicatif", "cmp-03", "couche-5"]
---
# CMP-03 — Entrepôt Lakehouse & Projections analytiques

**Contenu normatif.** Stockage analytique central (Lakehouse) recevant les flux ETL depuis la Couche 4. Exécute les projections tabulaires, la réconciliation du Grand Livre (ART-9) et alimente les tableaux de bord (CMP-01). Séparation stricte CQRS (ART-6) : aucun traitement transactionnel.

**Discipline existentielle.** Garantit l'intégrité analytique (ENF-5) et l'irréversibilité du masquage des identités. Toute analyse officielle passe par cet entrepôt.

- **Rattachement** : [ART-6](../chapitres/art-6.md) (CQRS), [ART-9](../chapitres/art-9.md) (Grand Livre), [CAP-INT-07](../capacites/cap-int-07.md), [CAP-INT-11](../capacites/cap-int-11.md).
- **Processus soutenus** : [PRC-09](../processus/prc-09.md) (remboursement), [PRC-11](../processus/prc-11.md) (pilotage).
- **Statut : Stable.**