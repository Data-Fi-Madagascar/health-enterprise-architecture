---
domain: composants
id: CMP-37
type: composant-securite
categorie: securite
niveau: "1"
title: Journal d'audit immuable
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/composants.md
implements: ["ART-7"]
uses: ["CMP-26", "CMP-27", "CMP-28", "CMP-29", "CMP-30", "CMP-31"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-37", "axe-securite"]
---
# CMP-37 : Journal d'audit immuable
**Contenu normatif.** Ce composant enregistre de facon immuable tous les evenements de securite et d'acces du systeme : authentifications, decisions d'acces (CMP-33), consultations de donnees, modifications, echecs. Il constitue la piste d'audit unique et fiable pour la tracabilite et l'investigation.
**Discipline de mise en oeuvre.** Les journaux sont horodates, signes et non alterables (ajout seul). Ils sont conserves selon la politique de retention et indexes pour la recherche. L'acces a la piste d'audit est lui-meme controle et separe des producteurs de logs.
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../chapitres/art-7.md).
- **Statut : Brouillon.**
