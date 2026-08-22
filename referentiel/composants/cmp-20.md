---
domain: composants
id: CMP-20
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Gestion des pharmacies (PMIS)
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/composants.md
implements: ["ENF-1", "F-1"]
applies_to: ["PRC-02", "PRC-05"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-20", "couche-2"]
---
# CMP-20 : Gestion des pharmacies (PMIS)
**Contenu normatif.** Ce composant gere le catalogue pharmaceutique, les stocks, les dispensations et la facturation aux points de service (pharmacies hospitalieres et de district). Il assure la tragabilite des medicaments et l'interface avec la chaine logistique (LMIS).
**Discipline de mise en oeuvre.** Il impose l'usage des referentiels de medicaments normalises et empeche les ruptures de stock non signalees. Les mouvements sont historises de facon immuable.
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../fondations/f-1.md).
- **Processus soutenus** : [PRC-02: Prestation des soins cliniques](../processus/prc-02.md) (dispensation aux soins), [PRC-05: Alerte, investigation et riposte](../processus/prc-05.md) (pharmacovigilance et riposte).
- **Statut : Brouillon.**
