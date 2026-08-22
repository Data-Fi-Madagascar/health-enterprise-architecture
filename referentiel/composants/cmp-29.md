---
domain: composants
id: CMP-29
type: composant-infrastructure
categorie: infrastructure
niveau: "1"
title: Liaisons dediees & VPN
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/composants.md
implements: ["ART-7"]
uses: []
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-29", "couche-1"]
---
# CMP-29 : Liaisons dediees & VPN
**Contenu normatif.** Ce composant etablit les liaisons dediees et les tunnels VPN securises entre les structures, les noeuds et les partenaires. Il fournit la connectivite de confiance necessaire aux echanges inter-structures et aux acces distants administrateurs.
**Discipline de mise en oeuvre.** Tout transit inter-structure emprunte un canal authentifie et chiffre ; les cles sont gerees via la PKI (CMP-35). Les acces distants sont controles et journalises. La segmentation isole les flux de gestion des flux metiers.
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../chapitres/art-7.md).
- **Statut : Brouillon.**
