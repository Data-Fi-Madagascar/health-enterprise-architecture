---

domain: composants
id: CMP-27
type: composant-infrastructure
categorie: infrastructure
niveau: "1"
title: "Noeuds regionaux (clusters de district : Fog)"
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
implements: ["ART-7"]
uses: []
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-27", "couche-1"]
related: ["VS-04"]
---

# CMP-27 : Noeuds regionaux (clusters de district : Fog)
**Contenu normatif.** Ce composant deploie des clusters de calcul et de stockage au niveau regional et de district (Fog computing) pour rapprocher les services des points de service et amortir la latence ou l'absence de reseau. Il heberge les instances locales des applicatifs (CMP-19..25) et assure la synchronisation differentielle avec le noeud central (CMP-26).
**Discipline de mise en oeuvre.** La continuite de service en connectivite degradee est une exigence : les ecritures locales sont conservees et reconciliees a l'amont. Les donnees y sont chiffrees et les noeuds authentifies. La topologie est documentee et les seuils de retention definis pour respecter la politique de conservation.
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../chapitres/art-7.md).
- **Statut : Brouillon.**
