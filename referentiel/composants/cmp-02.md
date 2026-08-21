---
domain: composants
id: CMP-02
type: composant-applicatif
niveau: "1"
title: Centre de commande & Crises intersectorielles (alertes, crises, veille)
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/index.md
maps_to: ["CAP-INT-07"]
implements: ["ART-5", "ART-0"]
applies_to: ["PRC-05", "PRC-11"]
related: ["ENF-2", "CAP-05", "CAP-06", "VS-02", "VS-04"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-02", "couche-6"]
---
# Centre de commande & Crises intersectorielles

**Contenu normatif.** Ce composant constitue le centre unique de supervision des alertes épidémiques et de coordination des crises intersectorielles (santé, élevage, environnement). Il agrège les signaux de la surveillance ([CMP-14: Registre des produits, intrants et indicateurs](cmp-14.md)), du moteur d'alertes ([CMP-04: Moteur analytique & IA (IA prédictive, routeur alertes, Grand Livre)](cmp-04.md)) et des registres de gouvernance ([CMP-17: Message broker asynchrone](cmp-17.md)), et fournit une vue en temps réel pour la prise de décision multi-ministérielle.

**Discipline de mise en œuvre.** Il est le point de convergence obligatoire de toute riposte coordonnée ; sans lui, les secteurs agissent en silos et la riposte reste fragmentée.

- **Rattachement** : [ART-5](../chapitres/art-5.md) (routeur alertes), [ART-0](../chapitres/art-0.md) (accords partage), [CAP-INT-07: Accès et exposition des données analytiques](../capacites/cap-int-07.md).
- **Processus soutenus** : [PRC-05: Alerte, investigation et riposte](../processus/prc-05.md) (alerte/investigation/riposte), [PRC-11: Suivi et pilotage de la performance](../processus/prc-11.md) (pilotage performance).
- **Statut : Stable.**
