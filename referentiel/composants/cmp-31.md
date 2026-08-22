---
domain: composants
id: CMP-31
type: composant-infrastructure
categorie: infrastructure
niveau: "1"
title: Reseaux mobiles prives (APN securises)
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/composants.md
implements: ["ART-7"]
uses: []
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-31", "couche-1"]
---
# CMP-31 : Reseaux mobiles prives (APN securises)
**Contenu normatif.** Ce composant fournit des APN (Access Point Name) securises sur les reseaux mobiles des operateurs pour les terminaux de terrain (CMP-21, agents communautaires, vehicules). Il garantit un transit prive des donnees de sante hors de l'internet ouvert.
**Discipline de mise en oeuvre.** Les terminaux mobiles n'emettent les donnees de sante que via l'APN prive, chiffre de bout en bout. L'acces a l'APN est controle et les cartes SIM identifiees. Les volumes et flux sont supervises pour detecter les anomalies.
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../chapitres/art-7.md).
- **Statut : Brouillon.**
