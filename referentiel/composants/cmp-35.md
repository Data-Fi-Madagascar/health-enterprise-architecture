---
domain: composants
id: CMP-35
type: composant-securite
categorie: securite
niveau: "1"
title: Infrastructure de cles publiques (PKI)
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
implements: ["ART-7"]
uses: ["CMP-26", "CMP-27", "CMP-28", "CMP-29", "CMP-30", "CMP-31"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-35", "axe-securite"]
related: ["VS-04"]
---
# CMP-35 : Infrastructure de cles publiques (PKI)
**Contenu normatif.** Ce composant opere la PKI nationale du systeme de sante numerique : il emet, rotate et revoque les certificats des acteurs, structures et dispositifs, et fournit les services d'horodatage et de signature. Il est l'autorite de confiance a la base de l'authentification et du chiffrement.
**Discipline de mise en oeuvre.** Tout composant et toute liaison s'authentifie par certificat. La chaine de confiance est sous autorite nationale et ses racines sont protegees. La rotation des cles est planifiee et la revocation diffusee sans delai. Les operations de signature sont conformes aux normes en vigueur.
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../chapitres/art-7.md).
- **Statut : Brouillon.**
