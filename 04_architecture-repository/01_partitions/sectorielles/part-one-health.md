---
domain: sectorielles
id: PART-ONE-HEALTH
type: architecture-partition
niveau: "2"
title: Partition One Health
status: draft
owner: DEPSI
version: "0.1"
legacy_id: ["CAP-INT-14", "CAP-INT-16"]
partition_kind: sectorielle
togaf_repository_section: architecture-landscape
togaf_adm_phase: B
architecture_level: segment
architecture_domain: business
architecture_scope: one-health
architecture_state: target
applies_to: ["CAP-08", "CAP-18", "VS-02", "VS-04"]
related: []
tags: ["togaf", "partition", "sectorielle"]
---
# Partition One Health

## Finalité

Cette partition sectorielle cadre les dépendances d'architecture nécessaires à la coordination One Health entre santé humaine, santé animale, environnement et partenaires institutionnels.

## Périmètre

- Capabilités couvertes : [CAP-08 : Gouvernance institutionnelle, planification, coordination et redevabilité](../../02_architecture-elements/strategy/capabilities/cap-08.md), [CAP-18 : Coordination intersectorielle One Health](../../02_architecture-elements/strategy/capabilities/cap-18.md)
- Flux de valeur couverts : [VS-02](../../02_architecture-elements/strategy/value-streams/vs-02.md), [VS-04](../../02_architecture-elements/strategy/value-streams/vs-04.md)
- Niveau TOGAF : segment
- Etat d'architecture : cible

La surveillance et la riposte intersectorielles mobilisent CAP-18 dans VS-02. Le pilotage, la coordination des institutions et la redevabilité mobilisent CAP-08 dans VS-04, notamment par le centre de commande CMP-02. Ces deux responsabilités s'inscrivent dans les flux nationaux existants ; elles ne justifient pas la création d'un nouveau flux One Health, selon [ADR-0012](../../../01_cnisn/06_decisions/adr-0012-one-health-pilotage.md).

Le profil [PT-15](../../05_building-blocks/sbb/legacy-profiles/pt-15.md) réutilise [ABB-ECHANGE-MEDIATION](../../05_building-blocks/abb/abb-echange-mediation.md) pour les échanges intersectoriels et [ABB-EXPOSITION-DONNEES-ANALYTIQUES](../../05_building-blocks/abb/abb-exposition-donnees-analytiques.md) pour l'accès gouverné aux indicateurs. Ces blocs conservent leur portée transverse et participent également à cette partition sectorielle.

## Règle de cohérence

Toute évolution de cette partition doit préserver la séparation des autorités de données et l'interopérabilité contrôlée entre institutions, sans créer de référentiel maître intersectoriel non gouverné.
