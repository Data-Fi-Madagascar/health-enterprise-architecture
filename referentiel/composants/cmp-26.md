---
domain: composants
id: CMP-26
type: composant-infrastructure
categorie: infrastructure
niveau: "1"
title: Noeud central (datacenters nationaux HDS)
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
implements: ["ART-7"]
uses: []
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-26", "couche-1"]
---
# CMP-26 : Noeud central (datacenters nationaux HDS)
**Contenu normatif.** Ce composant fournit l'infrastructure de calcul et de stockage centralisee hebergeant les donnees et services nationaux dans des datacenters conformes aux exigences d'hebergement de donnees de sante (HDS). Il est le socle physique des composants applicatifs (CMP-01..25), analytiques (CMP-03/CMP-04) et de securite (CMP-32..38). Il assure la haute disponibilite, la redondance geographique et la reprise d'activite.
**Discipline de mise en oeuvre.** Les donnees de sante y resident sous souverainete nationale, chiffrees au repos et en transit. La continuite de service est assuree par la redondance et des plans de reprise testes. L'acces au socle est limite aux composants authentifies (CMP-35). La capacite est dimensionnee pour absorber les pics (campagnes de vaccination, epidemics).
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../chapitres/art-7.md).
- **Statut : Brouillon.**
