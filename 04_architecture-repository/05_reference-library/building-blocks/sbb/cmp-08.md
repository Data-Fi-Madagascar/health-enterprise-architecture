---
domain: sbb
id: CMP-08
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Répertoire de données cliniques opérationnelles
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
maps_to: ["ABB-GESTION-CONSENTEMENT"]
implements: ["ART-4"]
applies_to: ["PRC-04", "PRC-05"]
accesses: ["DO-03", "DO-05"]
related: ["ENF-3", "CAP-09", "VS-02"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-08", "couche-4"]
---
# Répertoire de données cliniques opérationnelles

**Contenu normatif.** Ce composant centralise les données cliniques opérationnelles (dossiers patients, épisodes de soins, actes médicaux). Il assure la persistance et la cohérence des données cliniques en temps réel, et fournit les API de lecture/écriture pour les applications métier.

**Discipline de mise en œuvre.** Il constitue la source de vérité clinique pour les applications opérationnelles. Toute donnée clinique créée ou modifiée dans les applications de point de service y est persistée.

- **Rattachement** : [ART-4](../../patterns/artsn-rules/art-4.md) (référentiel des métadonnées), [ABB-GESTION-CONSENTEMENT: Gestion des consentements et bases d’autorisation](../abb/abb-gestion-consentement.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../../03_business-architecture/business/processes/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../../03_business-architecture/business/processes/prc-05.md) (pharmacie).
- **Données portées** : [DO-03 : Dossier et épisode de soins](../../../04_data-architecture/data-objects/do-03.md), [DO-05 : Consultation](../../../04_data-architecture/data-objects/do-05.md)
- **Statut : Stable.**