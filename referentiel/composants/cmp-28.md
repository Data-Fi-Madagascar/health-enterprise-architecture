---
domain: composants
id: CMP-28
type: composant-infrastructure
categorie: infrastructure
niveau: "1"
title: Noeuds locaux (equipements chiffres : Edge)
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/composants.md
implements: ["ART-7"]
uses: []
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-28", "couche-1"]
---
# CMP-28 : Noeuds locaux (equipements chiffres : Edge)
**Contenu normatif.** Ce composant regroupe les equipements de bord (Edge) des structures de soins : terminaux, passerelles de collecte, boitiers de pre-traitement et concentrateurs. Il assure la collecte locale des donnees, leur pre-traitement et leur mise en file d'attente chiffree en attente de synchronisation. Il interconnecte les dispositifs au noeud regional (CMP-27).
**Discipline de mise en oeuvre.** Les equipements sont durcis, chiffres et authentifies au reseau via certificat (CMP-35). Ils fonctionnent hors ligne et se synchronisent a l'amont sans perte. Le cycle de vie des equipements (deploiement, rotation, retrait) est trace pour eviter toute compromission au bord du reseau.
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../chapitres/art-7.md).
- **Statut : Brouillon.**
