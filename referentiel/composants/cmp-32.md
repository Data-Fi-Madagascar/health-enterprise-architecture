---
domain: composants
id: CMP-32
type: composant-securite
categorie: securite
niveau: "1"
title: Gestion des identites
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
implements: ["ART-7"]
uses: ["CMP-26", "CMP-27", "CMP-28", "CMP-29", "CMP-30", "CMP-31"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-32", "axe-securite"]
---
realized_by: ["WP-01"]
# CMP-32 : Gestion des identites
**Contenu normatif.** Ce composant de securite tient le systeme de gestion des identites et des acces (IAM) du systeme de sante numerique. Il enregistre et gere le cycle de vie des identites des acteurs (professionnels, patients via le registre), des structures et des dispositifs, et fournit l'authentification unique et la federation d'identites entre composants et partenaires.
**Discipline de mise en oeuvre.** Toute entite accedant au systeme dispose d'une identite verifiee et non reusee. L'identite du beneficiaire est resolue sans ambiguite via le registre d'identite (PT-04/CMP-34). Le cycle de vie (creation, suspension, suppression) est trace. La federation s'appuie sur des protocoles standards (OIDC/OAuth2, SAML) et des certificats (CMP-35).
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../chapitres/art-7.md).
- **Statut : Brouillon.**
