---
domain: composants
id: CMP-33
type: composant-securite
categorie: securite
niveau: "1"
title: Controle d'acces fin (RBAC/ABAC)
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
implements: ["ART-7"]
uses: ["CMP-26", "CMP-27", "CMP-28", "CMP-29", "CMP-30", "CMP-31"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-33", "axe-securite"]
related: ["VS-04"]
---
# CMP-33 : Controle d'acces fin (RBAC/ABAC)
**Contenu normatif.** Ce composant applique le controle d'acces fin aux donnees et services, selon le role (RBAC), les attributs et le contexte (ABAC). Il decide, a chaque requete, si un acteur peut lire ou ecrire une ressource, en fonction de sa fonction, de la finalite et du niveau de sensibilite de la donnee.
**Discipline de mise en oeuvre.** L'acces aux donnees de sante est cloisonne par profil et finalite ; le moindre privilege est la regle. Toute decision d'acces (accord ou refus) est journalisee (CMP-37) pour audit. Les droits sont revus periodiquement. Les exceptions sont temporaires et tracees.
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../chapitres/art-7.md).
- **Statut : Brouillon.**
