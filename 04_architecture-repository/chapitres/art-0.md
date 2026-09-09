---
domain: chapitres

id: ART-0
type: chapitre
niveau: "3"
title: Accords de partage inter-institutionnels
status: candidate
maturity_condition: "Confirmation par une initiative impliquant une source hors gouvernance sanitaire"
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-0-accords-partage.md
maps_to: []
implements: []
applies_to: ["ENF-4"]
related: []
tags: ["artsn", "niveau-3", "chapitre", "ART-0"]
---
# Accords de partage inter-institutionnels

**Contenu normatif.** Avant toute interconnexion technique, échange ou ingestion de données provenant d’une entité extérieure à la gouvernance directe de la santé, un accord formel (*Data Sharing Agreement*) doit obligatoirement fixer le périmètre de partage, les clauses de réciprocité, les obligations de notification en cas de faille, et sécuriser la souveraineté et la résidence physique de la donnée de santé sur le territoire national.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (ministères partenaires, secteurs tiers), cette discipline seule permet de fixer les frontières de la responsabilité juridique et de configurer dynamiquement les filtres de sécurité automatiques sans rompre le pipeline.

- **Rattachement** : capacité candidate « Coordination intersectorielle ».
- **Déduit selon** : [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../exigences/enf-4.md) (cloisonnement One Health).
- **Statut : Proposition ouverte.**

## Profils PTISN qui implémentent ce chapitre

Les profils techniques nationaux ci-dessous déclarent implémenter ce chapitre ART dans leur champ `implements` (frontmatter du référentiel). Le profil constitue la spécification implémentable et testable ; le chapitre demeure le cadre normatif opposable.

- [PT-01 : Échange interinstitutionnel](../profils/pt-01.md)
- [PT-10 : Confiance, authentification et autorisation](../profils/pt-10.md)
- [PT-11 : Consentement et bases d’autorisation](../profils/pt-11.md)
- [PT-14 : Interopérabilité transfrontalière](../profils/pt-14.md)
- [PT-15 : Surveillance One Health](../profils/pt-15.md)

