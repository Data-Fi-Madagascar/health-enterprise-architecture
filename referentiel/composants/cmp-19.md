---
domain: composants
id: CMP-19
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Dossiers & statistiques de sante (hopitaux)
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/composants.md
implements: ["ENF-1", "F-1"]
applies_to: ["PRC-01", "PRC-02", "PRC-03", "PRC-06"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-19", "couche-2"]
---
# CMP-19 : Dossiers & statistiques de sante (hopitaux)
**Contenu normatif.** Ce composant tient le dossier patient et les statistiques de sante au niveau de l'hopital (Couche 2, soins curatifs). Il consolide les donnees cliniques, les indicateurs d'activite et les rapports hospitaliers, et alimente les registres et l'entrepot national. Il fonctionne en mode degrade (connectivite intermittente) et se synchronise avec les composants centraux.
**Discipline de mise en oeuvre.** Il garantit l'exhaustivite et l'exactitude des statistiques hospitalieres, fondement de la planification. Toute donnee saisie reste reconciliable avec sa source clinique.
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../fondations/f-1.md).
- **Processus soutenus** : [PRC-01: Acces, orientation et admission du patient](../processus/prc-01.md) (acces et admission), [PRC-02: Prestation des soins cliniques](../processus/prc-02.md) (prestation des soins), [PRC-03: Continuite, suivi et qualite des soins](../processus/prc-03.md) (suivi et qualite), [PRC-06: Cloture et capitalisation des episodes](../processus/prc-06.md) (cloture et capitalisation).
- **Statut : Brouillon.**
