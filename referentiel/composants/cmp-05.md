---
domain: composants
id: CMP-05
type: composant-applicatif
niveau: "1"
title: Moteur de graphes & Référentiel spatio-temporel (Graph Store, Spatio ART-4d)
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/index.md
maps_to: ["CAP-INT-03", "CAP-INT-12"]
implements: ["ART-8B", "ART-4D"]
applies_to: []
related: ["ENF-4", "CAP-13", "CAP-14", "VS-04"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-05", "couche-5"]
---
# Moteur de graphes & Référentiel spatio-temporel

**Contenu normatif.** Ce composant gère le graphe de relations entre entités (patients, structures, personnels, produits) et le référentiel spatio-temporel unifié (ART-4d). Il sert les requêtes de parcours, la détection de clusters épidémiques et l'analyse de réseaux.

**Discipline de mise en œuvre.** Il garantit la cohérence topologique du graphe national et la résilience spatiale ([ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../exigences/enf-4.md)). Toute requête de navigation relationnelle passe par ce composant.

- **Rattachement** : [ART-8b](../chapitres/art-8b.md) (graphe), [ART-4d](../chapitres/art-4d.md) (spatio-temporel), [CAP-INT-03: Échange et médiation inter-systèmes](../capacites/cap-int-03.md), [CAP-INT-12: Conformité et tests d’interopérabilité](../capacites/cap-int-12.md).
- **Statut : Stable.**
