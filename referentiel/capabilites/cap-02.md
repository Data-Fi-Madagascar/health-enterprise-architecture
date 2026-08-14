---
id: cap-02
type: capabilite
niveau: "1"
title: CAP-02 — Gestion du parcours patient, référence et contre-référence
status: draft
owner: Responsables de capabilités métier
version: "0.1"
source: 00_caesn/03_capabilities/business.md
maps_to: ["cap-int-03", "cap-int-01", "cap-int-13"]
implements: []
applies_to: ["vs-01"]
related: ["cap-05", "cap-10", "cap-14", "cap-17"]
tags: ['caesn', 'niveau-1', 'capabilite', 'cap-02']
---
# CAP-02 — Gestion du parcours patient, référence et contre-référence

## Rôle dans le système

La capabilité organise le parcours du patient entre les points de service : orientation vers le niveau adapté, référence vers une structure plus spécialisée et contre-référence vers la formation d'origine. Elle assure que l'information clinique suit le patient d'un niveau à l'autre, afin que la continuité des soins ne dépende pas d'un seul établissement. Sans elle, les ruptures de parcours (référence sans dossier, absence de retour d'information) fragmentent la prise en charge.

## Scénarios couverts

| Scénario | Description | Profils consommés |
|----------|-------------|-------------------|
| **Référence (S-03)** | Orientation d'un patient d'un niveau de soins vers un autre (CSB → hôpital régional) | PT-01, PT-02 |
| **Contre-référence (S-04)** | Retour du patient vers l'établissement d'origine avec compte-rendu et recommandations | PT-01, PT-02 |
| **Évacuation sanitaire nationale (S-05)** | Transfert urgent entre établissements nationaux | PT-01, PT-02, PT-11 |
| **Évacuation sanitaire internationale (S-05)** | Transfert vers un centre spécialisé à l'étranger | PT-01, PT-02, PT-11, PT-14 |

## Flux de valeur

- [VS-01](../flux-valeur/vs-01.md)
