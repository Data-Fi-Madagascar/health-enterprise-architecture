---
domain: composants
id: CMP-16
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Registre de schémas (F.3)
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
maps_to: ["CAP-INT-10"]
implements: ["ART-5"]
applies_to: ["PRC-07", "PRC-08"]
related: ["ENF-4", "CAP-10", "VS-03"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-16", "couche-3"]
---
# Registre de schémas (F.3)

**Contenu normatif.** Ce composant gère les schémas de données et les contrats d'API. Il assure la validation des messages et la conformité des échanges, et fournit les services de découverte et de versioning des schémas.

**Discipline de mise en œuvre.** Il est l'autorité de validation des échanges. Toute donnée échangée doit être conforme aux schémas définis ici, ce qui garantit l'intégrité et la cohérence des données.

- **Rattachement** : [ART-5](../chapitres/art-5.md) (routeur d'escalade), [CAP-INT-10: Provenance, audit et traçabilité](../capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-07: Identification et droits des bénéficiaires](../processus/prc-07.md) (production données), [PRC-08: Financement et exemption au point de service](../processus/prc-08.md) (qualité).
- **Statut : Stable.**