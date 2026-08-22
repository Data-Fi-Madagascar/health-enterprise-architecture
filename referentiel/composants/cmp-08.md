---
domain: composants
id: CMP-08
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Répertoire de données cliniques opérationnelles
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/composants.md
maps_to: ["CAP-INT-09"]
implements: ["ART-4"]
applies_to: ["PRC-04", "PRC-05"]
related: ["ENF-3", "CAP-09", "VS-02"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-08", "couche-4"]
---
# Répertoire de données cliniques opérationnelles

**Contenu normatif.** Ce composant centralise les données cliniques opérationnelles (dossiers patients, épisodes de soins, actes médicaux). Il assure la persistance et la cohérence des données cliniques en temps réel, et fournit les API de lecture/écriture pour les applications métier.

**Discipline de mise en œuvre.** Il constitue la source de vérité clinique pour les applications opérationnelles. Toute donnée clinique créée ou modifiée dans les applications de point de service y est persistée.

- **Rattachement** : [ART-4](../chapitres/art-4.md) (référentiel des métadonnées), [CAP-INT-09: Gestion des consentements et bases d’autorisation](../capacites/cap-int-09.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../processus/prc-05.md) (pharmacie).
- **Statut : Stable.**