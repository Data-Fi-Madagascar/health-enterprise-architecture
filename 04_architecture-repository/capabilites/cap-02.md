---
domain: capabilites

id: CAP-02
type: capabilite
niveau: "1"
title: Gestion du parcours patient, référence et contre-référence
status: stable
owner: Responsables de capabilités métier
version: "0.1"
envelope: 00_caesn/03_capabilities/business.md
maps_to: ["CAP-INT-03", "CAP-INT-01", "CAP-INT-13"]
implements: []
applies_to: ["VS-01"]
related: ["CAP-05", "CAP-10", "CAP-14", "CAP-17"]
tags: ["caesn", "niveau-1", "capabilite", "CAP-02"]
---
# Gestion du parcours patient, référence et contre-référence

## Rôle dans le système

La capabilité organise le parcours du patient entre les points de service : orientation vers le niveau adapté, référence vers une structure plus spécialisée et contre-référence vers la formation d'origine. Elle assure que l'information clinique suit le patient d'un niveau à l'autre, afin que la continuité des soins ne dépende pas d'un seul établissement. Sans elle, les ruptures de parcours (référence sans dossier, absence de retour d'information) fragmentent la prise en charge. Elle couvre :

- **Orientation et tri** : acheminement du patient vers le niveau de soins le plus adapté
- **Référence** : transfert vers une structure plus spécialisée avec transmission du dossier clinique
- **Contre-référence** : retour vers l'établissement d'origine avec compte-rendu et recommandations
- **Évacuation sanitaire** : transferts urgents nationaux et internationaux

Son absence fragilise la continuité des soins ([VS-01: Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../flux-valeur/vs-01.md)) et provoque des ruptures de parcours.

## Scénarios couverts

| Scénario | Description | Profils consommés |
|----------|-------------|-------------------|
| **Référence (DO-07)** | Orientation d'un patient d'un niveau de soins vers un autre (CSB → hôpital régional) | [PT-01: Profil technique national](../profils/pt-01.md), [PT-02: Profil technique national](../profils/pt-02.md) |
| **Contre-référence (DO-08)** | Retour du patient vers l'établissement d'origine avec compte-rendu et recommandations | [PT-01: Profil technique national](../profils/pt-01.md), [PT-02: Profil technique national](../profils/pt-02.md) |
| **Évacuation sanitaire nationale (DO-09)** | Transfert urgent entre établissements nationaux | [PT-01: Profil technique national](../profils/pt-01.md), [PT-02: Profil technique national](../profils/pt-02.md), [PT-11: Profil technique national](../profils/pt-11.md) |
| **Évacuation sanitaire internationale (DO-09)** | Transfert vers un centre spécialisé à l'étranger | [PT-01: Profil technique national](../profils/pt-01.md), [PT-02: Profil technique national](../profils/pt-02.md), [PT-11: Profil technique national](../profils/pt-11.md), [PT-14: Interopérabilité transfrontalière](../profils/pt-14.md) |

## Flux de valeur

- [VS-01: Soins essentiels](../flux-valeur/vs-01.md)

## Rattachement ARTSN

- [ART-8: Orchestration de processus](../chapitres/art-8.md)
- [ART-3: Historisation événementielle et profils de déploiement](../chapitres/art-3.md)
- [PT-01: Profil technique national](../profils/pt-01.md)
- [PT-02: Profil technique national](../profils/pt-02.md)

## Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 3/5 |

## Propriétaire

Responsables de capabilités métier
