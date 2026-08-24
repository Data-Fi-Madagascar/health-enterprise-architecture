---
domain: chapitres

id: ART-8D
type: chapitre
niveau: "3"
title: Chorégraphie inter-institutionnelle
status: candidate
maturity_condition: "Confirmation par une initiative intersectorielle"
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-8d-choregraphie-interinstitutionnelle.md
maps_to: ["CAP-13", "CAP-14"]
implements: []
applies_to: ["ENF-4"]
related: ["ART-8"]
tags: ["artsn", "niveau-3", "chapitre", "ART-8D"]
---
# Chorégraphie inter-institutionnelle

**Contenu normatif.** Lorsque l’intégration implique plusieurs ministères co-égaux, l’architecture **proscrit l’orchestration centralisée** et impose un modèle de coordination par messagerie décentralisée. Les systèmes partenaires doivent s’abonner de manière autonome à des files d’événements publics sans qu’aucun nœud n’ait d’autorité informatique sur le système de l’autre (pattern cible : Publication/Abonnement, Pub/Sub).

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (systèmes d’information autonomes des ministères de l’Agriculture ou de l’Environnement), cette discipline seule permet de déclencher des actions conjointes et simultanées lors d’un signal épidémique tout en préservant l’indépendance informatique et la souveraineté de chaque institution, sans rompre le pipeline.

- **Rattachement** : [CAP-13: Système d'information sanitaire, données et recherche](../capabilites/cap-13.md), [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../capabilites/cap-14.md).
- **Pattern cible** : Publication / Abonnement (Pub/Sub).
- **Déduit selon** : [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../exigences/enf-4.md) (souveraineté intersectorielle).
- **Statut : Proposition ouverte.**
