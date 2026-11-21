---
domain: sbb
id: CMP-05
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Moteur de graphes & Référentiel spatio-temporel (Graph Store, Spatio ART-4D)
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
maps_to: ["ABB-ECHANGE-MEDIATION", "COMP-HOMOLOGATION-INTEROPERABILITE"]
implements: ["ART-8B", "ART-4D"]
applies_to: []
accesses: ["DO-01", "DO-11", "DO-23", "DO-24", "DO-26"]
related: ["ENF-4", "CAP-13", "CAP-14", "VS-04"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-05", "couche-5"]
---
# Moteur de graphes & Référentiel spatio-temporel

**Contenu normatif.** Ce composant gère le graphe de relations entre entités (patients, structures, personnels, produits) et le référentiel spatio-temporel unifié (ART-4D). Il sert les requêtes de parcours, la détection de clusters épidémiques et l'analyse de réseaux.

**Discipline de mise en œuvre.** Il garantit la cohérence topologique du graphe national et la résilience spatiale ([ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../../../02_requirements/enf-4.md)). Toute requête de navigation relationnelle passe par ce composant.

- **Rattachement** : [ART-8B](../../patterns/artsn-rules/art-8b.md) (graphe), [ART-4D](../../patterns/artsn-rules/art-4d.md) (spatio-temporel), [ABB-ECHANGE-MEDIATION: Échange et médiation inter-systèmes](../abb/abb-echange-mediation.md), [COMP-HOMOLOGATION-INTEROPERABILITE: Conformité et tests d’interopérabilité](../../../06_governance/compliance/comp-homologation-interoperabilite.md).
- **Données portées** : [DO-01 : Patient](../../../04_data-architecture/data-objects/do-01.md), [DO-11 : Produit de santé](../../../04_data-architecture/data-objects/do-11.md), [DO-23 : Formation sanitaire](../../../04_data-architecture/data-objects/do-23.md), [DO-24 : Agent de santé](../../../04_data-architecture/data-objects/do-24.md), [DO-26 : Zone sanitaire](../../../04_data-architecture/data-objects/do-26.md)
- **Statut : Stable.**
