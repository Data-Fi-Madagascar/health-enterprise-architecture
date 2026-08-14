---
id: cmp-08
type: composant-applicatif
niveau: "1"
title: CMP-08 — Répertoire de données cliniques opérationnelles
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/04_cartographie-cible/index.md
maps_to: ["cap-int-09"]
implements: ["art-4"]
applies_to: ["prc-04", "prc-05"]
related: ["enf-3", "cap-09", "vs-02"]
tags: ["artsn", "niveau-1", "composant-applicatif", "cmp-08", "couche-4"]
---
# CMP-08 — Répertoire de données cliniques opérationnelles

**Contenu normatif.** Centralise les données cliniques opérationnelles (dossiers patients, épisodes de soins, actes médicaux). Assure la persistance et la cohérence des données cliniques temps réel. Fournit les APIs de lecture/écriture pour les applications métier.

**Discipline existentielle.** Source de vérité clinique pour les applications opérationnelles. Toute donnée clinique créée ou modifiée dans les applications de point de service est persistée ici.

- **Rattachement** : [ART-4](../chapitres/art-4.md) (référentiel des métadonnées), [CAP-INT-09](../capacites/cap-int-09.md).
- **Processus soutenus** : [PRC-04](../processus/prc-04.md) (soins), [PRC-05](../processus/prc-05.md) (pharmacie).
- **Statut : Stable.**