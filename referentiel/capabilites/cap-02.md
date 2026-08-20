---

id: CAP-02
type: capabilite
niveau: "1"
title: Gestion du parcours patient, référence et contre-référence
status: draft
owner: Responsables de capabilités métier
version: "0.1"
source: 00_caesn/03_capabilities/business.md
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

Son absence fragilise la continuité des soins (VS-01) et provoque des ruptures de parcours.

## Scénarios couverts

| Scénario | Description | Profils consommés |
|----------|-------------|-------------------|
| **Référence (S-03)** | Orientation d'un patient d'un niveau de soins vers un autre (CSB → hôpital régional) | PT-01, PT-02 |
| **Contre-référence (S-04)** | Retour du patient vers l'établissement d'origine avec compte-rendu et recommandations | PT-01, PT-02 |
| **Évacuation sanitaire nationale (S-05)** | Transfert urgent entre établissements nationaux | PT-01, PT-02, PT-11 |
| **Évacuation sanitaire internationale (S-05)** | Transfert vers un centre spécialisé à l'étranger | PT-01, PT-02, PT-11, PT-14 |

## Flux de valeur

- [VS-01: Soins essentiels](../flux-valeur/vs-01.md)

## Rattachement ARTSN

- **ART-8** — Orchestration de processus
- **ART-3** — Historisation événementielle et profils de déploiement
- **PT-01** — Échange interinstitutionnel (X-Road)
- **PT-02** — Médiation intra-secteur

## Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 3/5 |

## Propriétaire

Responsables de capabilités métier
