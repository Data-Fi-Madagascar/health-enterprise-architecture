---
domain: composants
id: CMP-36
type: composant-securite
categorie: securite
niveau: "1"
title: Passerelle de confiance mondiale OMS (GDHCN)
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
implements: ["ART-7"]
uses: ["CMP-26", "CMP-27", "CMP-28", "CMP-29", "CMP-30", "CMP-31"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-36", "axe-securite"]
---
# CMP-36 : Passerelle de confiance mondiale OMS (GDHCN)
**Contenu normatif.** Ce composant interconnecte le systeme avec la Gateway de confiance mondiale de l'OMS (GDHCN) pour la verification internationale des certificats de vaccination et de sante. Il publie les certificats nationaux signes et consomme ceux des etats partenaires, dans le respect des protocoles GDHCN.
**Discipline de mise en oeuvre.** Les echanges internationaux n'exposent que les donnees necessaires, signees et chiffrees, conformement aux conventions (CMP-41). La confiance repose sur la PKI nationale (CMP-35). Les acces sont traces et les anomalies remontees a la surveillance (CMP-37).
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../chapitres/art-7.md).
- **Statut : Brouillon.**
