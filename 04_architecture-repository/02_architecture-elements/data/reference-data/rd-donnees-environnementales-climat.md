---
domain: reference-data
id: RD-DONNEES-ENVIRONNEMENTALES-CLIMAT
type: reference-data
niveau: "2"
title: Données environnementales et de résilience climatique
status: candidate
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-16
envelope: 01_cnisn/02_capacites/index.md
togaf_repository_section: architecture-landscape
togaf_adm_phase: C
architecture_level: segment
architecture_domain: data
architecture_scope: one-health
architecture_state: target
maps_to: ["CAP-04", "CAP-05", "CAP-18"]
implements: ["ART-4D", "ART-11"]
related: ["PART-ONE-HEALTH", "ENF-4", "ART-4D"]
tags: ["cnisn", "reference-data", "environnement", "climat", "one-health"]
---
# Données environnementales et de résilience climatique

## Finalité

Permettre l'interopérabilité des données environnementales et climatiques utiles à la santé publique (climat, qualité de l'air ou de l'eau, biodiversité, événements extrêmes) avec les secteurs environnement, agriculture, météorologie et intérieur, dans le cadre One Health.

## Services attendus

- référentiel spatio-temporel partagé (espace, temps, géographie) ;
- échange des indicateurs environnementaux et climatiques normalisés ;
- corrélation des signaux environnementaux et épidémiologiques ;
- alertes conjointes santé, environnement et climat.

## Principe de séparation

Cet élément de données de référence porte spécifiquement la dimension environnementale et climatique normalisée. Il complète la coordination intersectorielle One Health sans créer de référentiel maître intersectoriel non gouverné.

## Principes associés

- [P-INT-01: Autorité désignée](../../motivation/principles/p-int-01.md)
- [P-INT-10: Accord préalable](../../motivation/principles/p-int-10.md)
- [P-INT-16: Résidence et non-réplication](../../motivation/principles/p-int-16.md)

## Rattachement

- [Partition One Health](../../../01_partitions/sectorielles/part-one-health.md)
- [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données](../../../03_requirements/enf-4.md)
- [ART-4D: Référentiel géospatial et d'exploitation partagé](../../../04_patterns/artsn-rules/art-4d.md)
