---
domain: chapitres

id: ART-4
type: chapitre
niveau: "3"
title: Référentiels de métadonnées de gestion
status: stable
maturity_condition: "Reconfirmation par une initiative supplémentaire"
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-4-referentiels-metadonnees.md
maps_to: ["CAP-14"]
implements: []
applies_to: ["ENF-4"]
related: ["ART-4A", "ART-4B", "ART-4C", "ART-4D"]
tags: ["artsn", "niveau-3", "chapitre", "ART-4"]
---
# Référentiels de métadonnées de gestion

**Contenu normatif.** La maintenance et le stockage des structures de gestion (établissements, programmes sanitaires, indicateurs) doivent obligatoirement utiliser une **modélisation temporelle**. Tout changement ou divergence de hiérarchie organisationnelle doit être historisé et versionné, selon le pattern cible *Slowly Changing Dimension* (SCD) **type 2**.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (évolutions administratives, réorganisations territoriales), cette discipline seule permet de garantir qu’une analyse ou un rapport statistique passé pointe vers l’arborescence exacte en vigueur au moment précis de l’événement sans rompre le pipeline.

- **Rattachement** : [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../capabilites/cap-14.md) (interopérabilité et infrastructure partagée).
- **Pattern cible** : SCD type 2.
- **Déduit selon** : [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../exigences/enf-4.md) (cloisonnement inter-institutionnel).
- **Statut : Stable.**

Ce chapitre se décline en quatre sous-chapitres :
- [ART-4A: Résolution d’identité](art-4a.md)
- [ART-4B: Bases d’autorisation](art-4b.md)
- [ART-4C: Éligibilité et couverture](art-4c.md)
- [ART-4D: Référentiel géospatial et d’exploitation partagé](art-4d.md)
