---
id: cmp-05
type: composant-applicatif
niveau: "1"
title: CMP-05 — Moteur de graphes & Référentiel spatio-temporel (Graph Store, Spatio ART-4d)
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/04_cartographie-cible/index.md
maps_to: ["cap-int-03", "cap-int-12"]
implements: ["art-8b", "art-4d"]
applies_to: []
related: ["enf-4", "cap-13", "cap-14", "vs-04"]
tags: ["artsn", "niveau-1", "composant-applicatif", "cmp-05", "couche-5"]
---
# CMP-05 — Moteur de graphes & Référentiel spatio-temporel

**Contenu normatif.** Gère le graphe de relations entre entités (patients, structures, personnels, produits) et le référentiel spatio-temporel unifié (ART-4d). Sert les requêtes de parcours, la détection de clusters épidémiques et l'analyse de réseaux.

**Discipline existentielle.** Garantit la cohérence topologique du graphe national et la résilience spatiale (ENF-4). Toute requête de navigation relationnelle passe par ce composant.

- **Rattachement** : [ART-8b](../chapitres/art-8b.md) (graphe), [ART-4d](../chapitres/art-4d.md) (spatio-temporel), [CAP-INT-03](../capacites/cap-int-03.md), [CAP-INT-12](../capacites/cap-int-12.md).
- **Statut : Stable.**