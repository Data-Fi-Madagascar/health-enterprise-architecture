---
domain: capabilities

id: CAP-13
type: capabilite
niveau: "1"
title: Système d'information sanitaire, données et recherche
status: stable
owner: Responsables de capabilités habilitantes
version: "0.0.1"
envelope: 00_caesn/03_capabilities/enabling.md
maps_to: []
implements: []
applies_to: ["VS-01", "VS-02", "VS-03", "VS-04"]
related: []
tags: ["caesn", "niveau-1", "capabilite", "CAP-13"]
---
# Système d’information sanitaire, données et recherche

## Rôle dans le système

La capabilité transforme les données du système de santé en information utile : production, gestion, intégration, analyse et utilisation pour la décision, la recherche, le pilotage et la redevabilité. Elle est transversale à tous les flux de valeur, car aucun flux ne peut être mesuré, amélioré ou gouverné sans données fiables. Elle couvre :

- **Production et collecte** : génération et capture des données de santé aux points de service
- **Intégration et ingestion** : centralisation, validation d'intégrité et routage asynchrone des flux
- **Historisation événementielle** : journal d'événements immuable, source unique de vérité
- **Qualité et cohérence** : audit continu, traçabilité et fiabilité des données
- **Analyse et recherche** : entrepôt analytique, projections et exploitation pour la décision

Ces quatre capabilités ([CAP-13: Système d'information sanitaire, données et recherche](cap-13.md), [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](cap-14.md), [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](cap-15.md), [CAP-16: Gestion du portefeuille d'initiatives numériques](cap-16.md)) constituent le **socle commun (architecture runway)** dont l'absence bloque de nombreuses initiatives.

## Flux de valeur

- [VS-01: Soins essentiels](../value-streams/vs-01.md)
- [VS-02: Prévention et surveillance](../value-streams/vs-02.md)
- [VS-03: Protection financière](../value-streams/vs-03.md)
- [VS-04: Pilotage du système](../value-streams/vs-04.md)

## Rattachement ARTSN

- [ART-1: Intégration et ingestion](../../../04_patterns/artsn-rules/art-1.md)
- [ART-3: Historisation événementielle et profils de déploiement](../../../04_patterns/artsn-rules/art-3.md)
- [ART-5: Cohérence et qualité des données](../../../04_patterns/artsn-rules/art-5.md)

## Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 4/5 |

## Propriétaire

Responsables de capabilités habilitantes
