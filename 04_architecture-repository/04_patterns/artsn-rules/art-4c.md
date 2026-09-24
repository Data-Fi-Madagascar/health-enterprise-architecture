---
domain: artsn-rules

id: ART-4C
type: chapitre
niveau: "3"
title: Éligibilité et couverture
status: candidate
maturity_condition: "Confirmation par une initiative VS-03"
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-4c-eligibilite-couverture.md
maps_to: ["CAP-07"]
implements: []
applies_to: ["ENF-2", "ENF-1"]
related: ["ART-4"]
tags: ["artsn", "niveau-3", "chapitre", "ART-4C"]
---
# Éligibilité et couverture

**Contenu normatif.** L’architecture doit maintenir un référentiel des droits ouverts structurant **disjoint de l’identité** et versionné dans le temps. Ce registre doit être accessible instantanément pour permettre le calcul automatique de la couverture financière au point de vente. Pattern cible : modélisation temporelle SCD type 2.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (comptoirs de pharmacies privées, caisses d’hôpitaux autonomes), cette discipline seule permet d’appliquer la gratuité légale en ligne de front sans imposer d’avance de frais aux ménages vulnérables et sans rompre le pipeline.

- **Rattachement** : [CAP-07: Protection financière, couverture santé universelle](../../02_architecture-elements/strategy/capabilities/cap-07.md) (protection financière, CSU).
- **Pattern cible** : modélisation temporelle SCD type 2.
- **Déduit selon** : [ENF-2: Intégrité des flux et traçabilité des valeurs](../../03_requirements/enf-2.md) (anti-fraude) et [ENF-1: Résilience à l'instabilité réseau](../../03_requirements/enf-1.md) (autonomie locale).
- **Statut : Proposition ouverte.**

## Profils PTISN qui implémentent ce chapitre

Les profils techniques nationaux ci-dessous déclarent implémenter ce chapitre ART dans leur champ `implements` (frontmatter du référentiel). Le profil constitue la spécification implémentable et testable ; le chapitre demeure le cadre normatif opposable.

- [PT-05 : Registre des professionnels](../../05_building-blocks/sbb/legacy-profiles/pt-05.md)

