---
domain: sbb
id: CMP-18
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Compensateur / Regroupeur de flux (Netting — ART-8C)
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
maps_to: ["ABB-AUDIT-PROVENANCE"]
implements: ["ART-8C"]
applies_to: ["PRC-04", "PRC-05", "PRC-06"]
accesses: []
related: ["ENF-3", "CAP-10", "VS-02"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-18", "couche-3"]
---
# Compensateur / Regroupeur de flux (Netting — ART-8C)

**Contenu normatif.** Ce composant gère les compensations et le regroupement des flux. Il assure la cohérence des transactions distribuées et la résolution des anomalies, et garantit l'intégrité des échanges complexes.

**Discipline de mise en œuvre.** Il est le mécanisme de résolution des anomalies. Il permet la compensation automatique des erreurs et la cohérence des transactions, ce qui garantit la fiabilité des échanges critiques.

- **Rattachement** : [ART-8C](../../patterns/artsn-rules/art-8c.md) (Netting), [ABB-AUDIT-PROVENANCE: Provenance, audit et traçabilité](../abb/abb-audit-provenance.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../../03_business-architecture/business/processes/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../../03_business-architecture/business/processes/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../../../03_business-architecture/business/processes/prc-06.md) (logistique).
- **Données portées** : aucune. Composant transversal : compensation et regroupement des flux. Le rattachement aux données est porté par les composants qui lui confient les flux.
- **Statut : Stable.**