---
domain: legacy-components
id: CMP-16
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Registre de schémas (F.3)
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
maps_to: ["ABB-AUDIT-PROVENANCE"]
implements: ["ART-5"]
applies_to: ["PRC-07", "PRC-08"]
related: ["ENF-4", "CAP-10", "VS-03"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-16", "couche-3"]
---
# Registre de schémas (F.3)

**Contenu normatif.** Ce composant gère les schémas de données et les contrats d'API. Il assure la validation des messages et la conformité des échanges, et fournit les services de découverte et de versioning des schémas.

**Discipline de mise en œuvre.** Il est l'autorité de validation des échanges. Toute donnée échangée doit être conforme aux schémas définis ici, ce qui garantit l'intégrité et la cohérence des données.

- **Rattachement** : [ART-5](../../../04_patterns/artsn-rules/art-5.md) (routeur d'escalade), [ABB-AUDIT-PROVENANCE: Provenance, audit et traçabilité](../abb-audit-provenance.md).
- **Processus soutenus** : [PRC-07: Identification et droits des bénéficiaires](../../../02_architecture-elements/business/processes/prc-07.md) (production données), [PRC-08: Financement et exemption au point de service](../../../02_architecture-elements/business/processes/prc-08.md) (qualité).
- **Statut : Stable.**