---
domain: chapitres

id: ART-8B
type: chapitre
niveau: "3"
title: Modélisation de relations en graphe
status: candidate
maturity_condition: "Confirmation par une initiative supplémentaire"
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-8b-modelisation-graphe.md
maps_to: ["CAP-13", "CAP-14"]
implements: []
applies_to: ["ENF-4"]
related: ["ART-8"]
tags: ["artsn", "niveau-3", "chapitre", "ART-8B"]
realized_by: ["WP-07"]
---
# Modélisation de relations en graphe

**Contenu normatif.** Pour la surveillance et la cartographie de structures relationnelles ouvertes, récursives et sans limites définies, l’architecture impose l’utilisation d’un **stockage non-relationnel** (*Graph Store*). Les entités et leurs interactions doivent y être traitées comme des nœuds et des arcs qualifiés.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (réseaux de contacts épidémiques, propagation de foyers de zoonoses), cette discipline seule permet de calculer instantanément les chaînes de transmission et d’identifier les super-propagateurs sans rompre le pipeline.

- **Rattachement** : [CAP-13: Système d'information sanitaire, données et recherche](../capabilites/cap-13.md), [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../capabilites/cap-14.md).
- **Infrastructure cible** : Graph Store.
- **Déduit selon** : [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../exigences/enf-4.md) (cloisonnement One Health).
- **Statut : Proposition ouverte.**

## Profils PTISN qui implémentent ce chapitre

Les profils techniques nationaux ci-dessous déclarent implémenter ce chapitre ART dans leur champ `implements` (frontmatter du référentiel). Le profil constitue la spécification implémentable et testable ; le chapitre demeure le cadre normatif opposable.

- [PT-15 : Surveillance One Health](../profils/pt-15.md)

