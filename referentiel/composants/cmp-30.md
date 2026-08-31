---
domain: composants
id: CMP-30
type: composant-infrastructure
categorie: infrastructure
niveau: "1"
title: Reseau prive MPLS
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
implements: ["ART-7"]
uses: []
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-30", "couche-1"]
related: ["VS-04"]
---
# CMP-30 : Reseau prive MPLS
**Contenu normatif.** Ce composant opere le reseau prive MPLS reliant les sites du systeme de sante, isole de l'internet public pour les flux sensibles. Il offre un transport garantie, avec qualite de service, entre le noeud central, les noeuds regionaux et les structures connectees.
**Discipline de mise en oeuvre.** Le routage sensible est separe du trafic grand public. La qualite de service priorise les flux critiques (alertes, dossiers urgents). La supervision mesure la disponibilite et declenche les bascules vers les liaisons de secours (CMP-29).
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../chapitres/art-7.md).
- **Statut : Brouillon.**
