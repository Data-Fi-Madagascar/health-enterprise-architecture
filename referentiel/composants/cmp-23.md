---
domain: composants
id: CMP-23
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Chaine logistique (LMIS)
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/composants.md
implements: ["ENF-1", "F-1"]
applies_to: ["PRC-05", "PRC-10"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-23", "couche-2"]
---
# CMP-23 : Chaine logistique (LMIS)
**Contenu normatif.** Ce composant pilote la logistique medicale : prevision, approvisionnement, stockage et distribution des intrants (medicaments, consommables, vaccins). Il interconnecte les pharmacies, les districts et le noeud central.
**Discipline de mise en oeuvre.** Il assure la tracabilite de bout en bout et l'alerte en cas de rupture. Les seuils de reapprovisionnement sont calcules a partir des donnees d'activite.
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../fondations/f-1.md).
- **Processus soutenus** : [PRC-05: Alerte, investigation et riposte](../processus/prc-05.md) (approvisionnement et riposte), [PRC-10: Planification et allocation des ressources](../processus/prc-10.md) (planification des ressources).
- **Statut : Brouillon.**
