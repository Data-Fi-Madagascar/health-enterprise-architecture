---
domain: composants
id: CMP-38
type: composant-securite
categorie: securite
niveau: "1"
title: Moteur de chiffrement
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/composants.md
implements: ["ART-7"]
uses: ["CMP-26", "CMP-27", "CMP-28", "CMP-29", "CMP-30", "CMP-31"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-38", "axe-securite"]
---
# CMP-38 : Moteur de chiffrement
**Contenu normatif.** Ce composant centralise les services de chiffrement (au repos et en transit) et la gestion des cles cryptographiques pour l'ensemble du socle. Il fournit les primitives utilisees par le stockage (CMP-26..28), les liaisons (CMP-29..31) et la securite (CMP-32..37).
**Discipline de mise en oeuvre.** Toutes les donnees de sante sont chiffrees par defaut. Les cles sont separees des donnees chiffrees et protegees par la PKI (CMP-35). Les algorithmes sont conformes aux recommandations et mis a jour sans rupture de service. La perte de cles est prevenue par une copie securisee.
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../chapitres/art-7.md).
- **Statut : Brouillon.**
