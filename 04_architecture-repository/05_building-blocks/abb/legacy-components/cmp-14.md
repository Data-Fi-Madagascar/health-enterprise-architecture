---
domain: legacy-components
id: CMP-14
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Registre des produits, intrants et indicateurs
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
maps_to: ["ABB-SERVICE-TERMINOLOGIE", "ABB-ECHANGE-LOGISTIQUE-LMIS"]
implements: ["ART-4"]
applies_to: ["PRC-05", "PRC-06"]
related: ["ENF-3", "CAP-09", "VS-02"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-14", "couche-4"]
---
# Registre des produits, intrants et indicateurs

**Contenu normatif.** Ce composant gère les référentiels de produits, d'intrants et d'indicateurs. Il assure la cohérence des nomenclatures de produits et la standardisation des indicateurs, et fournit les services de recherche et de validation.

**Discipline de mise en œuvre.** Il est l'autorité de référence pour les produits et indicateurs. Toute définition de produit ou d'indicateur passe par ce registre, ce qui garantit l'unicité et la cohérence des référentiels.

- **Rattachement** : [ART-4](../../../04_patterns/artsn-rules/art-4.md) (référentiel des métadonnées), [ABB-SERVICE-TERMINOLOGIE: Service de terminologie et codification communes](../abb-service-terminologie.md) pour les nomenclatures, et [ABB-ECHANGE-LOGISTIQUE-LMIS: Échange logistique LMIS](../abb-echange-logistique-lmis.md) pour le catalogue partagé des produits et intrants.
- **Processus soutenus** : [PRC-05: Alerte, investigation et riposte](../../../02_architecture-elements/business/processes/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../../../02_architecture-elements/business/processes/prc-06.md) (logistique).
- **Statut : Stable.**
