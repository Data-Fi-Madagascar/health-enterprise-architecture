---
id: CMP-04
type: composant-applicatif
niveau: "1"
title: Moteur analytique & IA (IA prédictive, routeur alertes, Grand Livre)
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/04_cartographie-cible/index.md
maps_to: ["CAP-INT-07", "CAP-INT-10"]
implements: ["ART-5", "ART-9"]
applies_to: ["PRC-09", "PRC-05"]
related: ["ENF-2", "ENF-5", "CAP-13", "CAP-15", "VS-02", "VS-04"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-04", "couche-5"]
---
# Moteur analytique & IA

**Contenu normatif.** Ce composant exécute les modèles prédictifs (IA), le routeur d'escalade et d'alertes (ART-5) et la réconciliation analytique du Grand Livre (ART-9). Il consomme l'entrepôt Lakehouse (CMP-03) et alimente le centre de commande (CMP-02) ainsi que la facturation (CMP-10).

**Discipline de mise en œuvre.** Il sépare l'inférence analytique du stockage et garantit la traçabilité des modèles (versionnage, données d'entraînement) ainsi que l'audit des décisions automatisées (ENF-2, ENF-5).

- **Rattachement** : [ART-5](../chapitres/art-5.md) (alertes), [ART-9](../chapitres/art-9.md) (Grand Livre), [CAP-INT-07: Accès et exposition des données analytiques](../capacites/cap-int-07.md), [CAP-INT-10: Provenance, audit et traçabilité](../capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-09: Remboursement et régulation des mécanismes](../processus/prc-09.md) (remboursement), [PRC-05: Alerte, investigation et riposte](../processus/prc-05.md) (alerte/riposte).
- **Statut : Stable.**