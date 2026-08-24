---
domain: chapitres

id: ART-4A
type: chapitre
niveau: "3"
title: Résolution d'identité
status: draft
maturity_condition: "Confirmation par une seconde initiative"
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-4a-resolution-identite.md
maps_to: ["CAP-04"]
implements: []
applies_to: ["ENF-3"]
related: ["ART-4"]
tags: ["artsn", "niveau-3", "chapitre", "ART-4A"]
---
# Résolution d’identité

**Contenu normatif.** La plateforme doit intégrer un index centralisé chargé d’exécuter des algorithmes de **rapprochement démographique** sur les attributs transmis par le terrain. Ce système doit réconcilier les fiches incomplètes avec le flux civil pour consolider un enregistrement unique (*Golden Record*) et attribuer le **matricule national** (Identifiant National de Santé, INS).

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (erreurs de saisie manuelle, variations phonétiques des patronymes, logiciels distants en silos), cette discipline seule permet d’éviter l’attribution de données cliniques au mauvais patient et de bloquer les accidents médicaux sans rompre le pipeline.

- **Rattachement** : [CAP-04bis](../../02_artsn/08_annexes/c-renvoi-capacites-candidates.md) (engagement patient et identitovigilance).
- **Concepts cibles** : Golden Record, Identifiant National de Santé (INS).
- **Déduit selon** : [ENF-3: Unicité de l'identité et résilience face à la fragmentation applicative](../exigences/enf-3.md) (unicité de l’identité).
- **Statut : Provisoire.**
