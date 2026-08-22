---
domain: chapitres

id: ART-9
type: chapitre
niveau: "3"
title: Garanties transactionnelles fortes
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-9-garanties-transactionnelles.md
maps_to: ["CAP-07"]
implements: []
applies_to: ["ENF-2"]
related: []
tags: ["artsn", "niveau-3", "chapitre", "ART-9"]
---
# Garanties transactionnelles fortes

**Contenu normatif.** Pour tout mouvement de valeur monétaire ou physique, l’architecture impose une contrainte de **grade comptable strict** basée sur un registre immuable, garantissant l’équilibre parfait des comptes (équation cible : *entrées − sorties = solde*). Toute écriture doit être associée à une signature non répudiable et un numéro de suivi de lot.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (officines pharmaceutiques privées, gestionnaires de stocks régionaux, caisses de subventions), cette discipline seule permet d’empêcher les détournements de médicaments, de bloquer les marchés noirs et d’assurer la réconciliation à somme nulle de l’argent public, sans rompre le pipeline.

- **Rattachement** : recouvre partiellement [CAP-07: Protection financière, couverture santé universelle](../capabilites/cap-07.md) (protection financière).
- **Équation cible** : entrées − sorties = solde.
- **Déduit selon** : [ENF-2: Intégrité des flux et traçabilité des valeurs](../exigences/enf-2.md) (grade comptable anti-fraude).
- **Statut : Proposition ouverte.**
