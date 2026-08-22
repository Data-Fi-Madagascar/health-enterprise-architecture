---
domain: composants
id: CMP-04
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Moteur analytique & IA (IA prédictive, routeur alertes, Grand Livre)
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/composants.md
maps_to: ["CAP-INT-07", "CAP-INT-10"]
implements: ["ART-5", "ART-9"]
applies_to: ["PRC-05", "PRC-09"]
related: ["ENF-2", "ENF-5", "CAP-13", "CAP-15", "VS-02", "VS-04"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-04", "couche-5"]
---
# Moteur analytique & IA

**Contenu normatif.** Ce composant exécute les modèles prédictifs (IA), le routeur d'escalade et d'alertes ([ART-5: Cohérence et qualité des données](../chapitres/art-5.md)) et la réconciliation analytique du Grand Livre ([ART-9: Garanties transactionnelles fortes](../chapitres/art-9.md)). Il consomme l'entrepôt Lakehouse ([CMP-03: Entrepôt Lakehouse & Projections analytiques (pipeline ETL, Lakehouse, projections)](cmp-03.md)) et alimente le centre de commande ([CMP-02: Centre de commande & Crises intersectorielles (alertes, crises, veille)](cmp-02.md)) ainsi que la facturation ([CMP-10: Registre des terminologies](cmp-10.md)).

**Discipline de mise en œuvre.** Il sépare l'inférence analytique du stockage et garantit la traçabilité des modèles (versionnage, données d'entraînement) ainsi que l'audit des décisions automatisées ([ENF-2: Intégrité des flux et traçabilité des valeurs](../exigences/enf-2.md), [ENF-5: Coordination des processus complexes décentralisés et asynchrones](../exigences/enf-5.md)).

- **Rattachement** : [ART-5](../chapitres/art-5.md) (alertes), [ART-9](../chapitres/art-9.md) (Grand Livre), [CAP-INT-07: Accès et exposition des données analytiques](../capacites/cap-int-07.md), [CAP-INT-10: Provenance, audit et traçabilité](../capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-09: Remboursement et régulation des mécanismes](../processus/prc-09.md) (remboursement), [PRC-05: Alerte, investigation et riposte](../processus/prc-05.md) (alerte/riposte).
- **Statut : Stable.**
