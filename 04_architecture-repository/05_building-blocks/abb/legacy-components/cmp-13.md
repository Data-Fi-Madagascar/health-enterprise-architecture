---
domain: legacy-components
id: CMP-13
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Registre des personnels
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
maps_to: ["ABB-GESTION-CONSENTEMENT"]
implements: ["ART-4"]
applies_to: ["PRC-04", "PRC-05"]
related: ["ENF-3", "CAP-09", "VS-02"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-13", "couche-4"]
---
# Registre des personnels

**Contenu normatif.** Ce composant gère les données des personnels de santé (identités, qualifications, affectations). Il assure la traçabilité des interventions et des responsabilités, et fournit les services de recherche et d'identification des personnels.

**Discipline de mise en œuvre.** Il constitue le référentiel de référence pour l'identification des intervenants. Toute intervention médicale enregistre l'identité du personnel via ce registre, ce qui garantit la traçabilité et la responsabilité.

- **Rattachement** : [ART-4](../../../04_patterns/artsn-rules/art-4.md) (référentiel des métadonnées), [ABB-GESTION-CONSENTEMENT: Gestion des consentements et bases d’autorisation](../abb-gestion-consentement.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../../02_architecture-elements/business/processes/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../../02_architecture-elements/business/processes/prc-05.md) (pharmacie).
- **Statut : Stable.**