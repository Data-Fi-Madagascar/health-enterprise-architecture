---
id: CMP-03
type: composant-applicatif
niveau: "1"
title: Entrepôt Lakehouse & Projections analytiques (pipeline ETL, Lakehouse, projections)
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/04_cartographie-cible/index.md
maps_to: ["CAP-INT-07", "CAP-INT-11"]
implements: ["ART-6", "ART-9"]
applies_to: ["PRC-09", "PRC-11"]
related: ["ENF-5", "CAP-13", "CAP-16", "VS-04"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-03", "couche-5"]
---
# Entrepôt Lakehouse & Projections analytiques

**Contenu normatif.** Ce composant assure le stockage analytique central (Lakehouse) en recevant les flux ETL depuis la Couche 4. Il exécute les projections tabulaires, la réconciliation du Grand Livre (ART-9) et alimente les tableaux de bord (CMP-01). La séparation stricte CQRS (ART-6) interdit tout traitement transactionnel.

**Discipline de mise en œuvre.** Il garantit l'intégrité analytique (ENF-5) et l'irréversibilité du masquage des identités. Toute analyse officielle passe par cet entrepôt.

- **Rattachement** : [ART-6](../chapitres/art-6.md) (CQRS), [ART-9](../chapitres/art-9.md) (Grand Livre), [CAP-INT-07: Accès et exposition des données analytiques](../capacites/cap-int-07.md), [CAP-INT-11: Qualité et réconciliation](../capacites/cap-int-11.md).
- **Processus soutenus** : [PRC-09: Remboursement et régulation des mécanismes](../processus/prc-09.md) (remboursement), [PRC-11: Suivi et pilotage de la performance](../processus/prc-11.md) (pilotage).
- **Statut : Stable.**