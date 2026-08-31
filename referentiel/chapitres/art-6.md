---
domain: chapitres

id: ART-6
type: chapitre
niveau: "3"
title: Analytique et restitution
status: draft
maturity_condition: "Confirmation par une initiative combinant plusieurs familles de projection"
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-6-analytique-restitution.md
maps_to: ["CAP-13", "CAP-08"]
implements: []
applies_to: ["ENF-4"]
related: []
tags: ["artsn", "niveau-3", "chapitre", "ART-6"]
realized_by: ["WP-04"]
---
# Analytique et restitution

**Contenu normatif.** L’architecture doit imposer une **séparation étanche entre le stockage opérationnel et le stockage analytique** (CQRS). L’entrepôt analytique doit être alimenté par des pipelines automatisés intégrant un moteur de masquage irréversible, et doit supporter nativement quatre types de requêtes : projections tabulaires, parcours de graphes, réconciliation comptable et fusion de signaux géospatiaux.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (requêtes lourdes des décideurs, extractions massives pour la recherche), cette discipline seule permet de garantir des performances de restitution constantes et une sécurité réglementaire absolue sans surcharger les serveurs de soins et sans rompre le pipeline.

- **Rattachement** : [CAP-13: Système d'information sanitaire, données et recherche](../capabilites/cap-13.md), [CAP-08: Gouvernance institutionnelle, planification, coordination et redevabilité](../capabilites/cap-08.md) (analytics & décisionnel).
- **Infrastructure cible** : Data Lakehouse.
- **Pattern cible** : modèle de séparation CQRS.
- **Déduit selon** : [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../exigences/enf-4.md) (protection One Health).
- **Statut : Provisoire.**
