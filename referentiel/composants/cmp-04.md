---
id: cmp-04
type: composant-applicatif
niveau: "1"
title: CMP-04 — Moteur analytique & IA (IA prédictive, routeur alertes, Grand Livre)
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/04_cartographie-cible.md
maps_to: ["cap-int-07", "cap-int-10"]
implements: ["art-5", "art-9"]
applies_to: ["prc-09", "prc-05"]
related: ["enf-2", "enf-5", "cap-13", "cap-15", "vs-02", "vs-04"]
tags: ["artsn", "niveau-1", "composant-applicatif", "cmp-04", "couche-5"]
---
# CMP-04 — Moteur analytique & IA

**Contenu normatif.** Exécute les modèles prédictifs (IA), le routeur d'escalade/d'alertes (ART-5) et la réconciliation analytique du Grand Livre (ART-9). Consomme l'entrepôt Lakehouse (CMP-03) et alimente le centre de commande (CMP-02) et la facturation (CMP-10).

**Discipline existentielle.** Sépare l'inférence analytique du stockage ; garantit la traçabilité des modèles (versionnage, données d'entraînement) et l'audit des décisions automatisées (ENF-2, ENF-5).

- **Rattachement** : [ART-5](../chapitres/art-5.md) (alertes), [ART-9](../chapitres/art-9.md) (Grand Livre), [CAP-INT-07](../capacites/cap-int-07.md), [CAP-INT-10](../capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-09](../processus/prc-09.md) (remboursement), [PRC-05](../processus/prc-05.md) (alerte/riposte).
- **Statut : Stable.**