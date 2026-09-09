---
domain: composants
id: CMP-34
type: composant-securite
categorie: securite
niveau: "1"
title: Gestion des consentements
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
implements: ["ART-7"]
uses: ["CMP-26", "CMP-27", "CMP-28", "CMP-29", "CMP-30", "CMP-31"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-34", "axe-securite"]
related: ["VS-04"]
---
# CMP-34 : Gestion des consentements
**Contenu normatif.** Ce composant gere le consentement des beneficiaires a l'echange et a l'utilisation de leurs donnees, par finalite, par partenaire et dans le temps. Il tient le registre de consentements et l'applique a chaque flux sortant ou acces patient (CMP-22).
**Discipline de mise en oeuvre.** Aucune donnee a caractere personnel n'est partagee sans consentement enregistre, verifiable et dans le champ autorise. Le retrait de consentement est effectif immediatement et applique aux nouveaux echanges. Les consentements sont horodates et non modifiables (journal immutable, CMP-37).
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../chapitres/art-7.md).
- **Statut : Brouillon.**
