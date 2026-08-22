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
**Contenu normatif.** Ce composant realise la gestion pharmaceutique au point de service (pharmacies hospitalieres, de district et communautaires) : catalogue des produits, stocks, dispensations, facturation et factures d'achat. Il assure la tracabilite du medicament du repertoire vers le beneficiaire et dialogue avec la chaine logistique (CMP-23/LMIS) pour le reapprovisionnement et les alertes de rupture. Il integre le volet pharmacovigilance en signalant les effets indesirables a la surveillance (PRC-05).
**Discipline de mise en oeuvre.** L'usage des referentiels de medicaments normalises (CMP-07) est obligatoire ; aucune denomination locale ne circule hors referentiel. Les mouvements de stock sont historises de facon immuable et les seuils de securite declares. La facturation au point de service respecte les regles d'exemption (PRC-08) lorsqu'elles s'appliquent.
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../fondations/f-1.md).
- **Processus soutenus** : [PRC-02: Prestation des soins cliniques](../processus/prc-02.md) (dispensation aux soins), [PRC-05: Alerte, investigation et riposte](../processus/prc-05.md) (pharmacovigilance et riposte).
- **Statut : Brouillon.**
