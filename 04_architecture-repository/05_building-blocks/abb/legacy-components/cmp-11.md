---
domain: legacy-components
id: CMP-11
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Registre des clients / Index National des Patients (INP — ART-4A)
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
maps_to: ["ABB-IDENTITE-BENEFICIAIRE"]
implements: ["ART-4A"]
applies_to: ["PRC-04", "PRC-05", "PRC-06"]
related: ["ENF-3", "CAP-09", "VS-02"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-11", "couche-4"]
realized_by: ["WP-03"]
---
# Registre des clients / Index National des Patients (INP — ART-4A)

**Contenu normatif.** Ce composant gère l'identité unique des patients à l'échelle nationale. Il assure la déduplication et le matching des identités, et fournit les services de recherche et d'identification des patients.

**Discipline de mise en œuvre.** Il constitue l'identité nationale de référence pour tous les systèmes de santé. Toute identification patient transite par cet index, ce qui garantit l'unicité et la cohérence des identités.

- **Rattachement** : [ART-4A](../../../04_patterns/artsn-rules/art-4a.md) (INP), [ABB-IDENTITE-BENEFICIAIRE: Résolution d'identité du bénéficiaire](../abb-identite-beneficiaire.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../../02_architecture-elements/business/processes/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../../02_architecture-elements/business/processes/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../../../02_architecture-elements/business/processes/prc-06.md) (logistique).
- **Statut : Stable.**
