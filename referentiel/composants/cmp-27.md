---
domain: composants
id: CMP-27
type: composant-infrastructure
categorie: infrastructure
niveau: "1"
title: Noeuds regionaux (clusters de district : Fog)
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/composants.md
implements: ["ART-7"]
uses: []
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-27", "couche-1"]
---
# CMP-27 : Noeuds regionaux (clusters de district : Fog)
**Contenu normatif.** Ce composant deploie des clusters de calcul et de stockage au niveau regional/district (Fog computing) pour rapprocher les services des points de service et amortir la latence reseau.
**Discipline de mise en oeuvre.** Il assure la continuite de service en connectivite degradee et se synchronise avec le noeud central. Les donnees y sont chiffrees et reconciliables.
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../chapitres/art-7.md).
- **Statut : Brouillon.**
