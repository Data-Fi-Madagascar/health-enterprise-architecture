---
domain: capabilites

id: CAP-17
type: capabilite
niveau: "1"
title: Engagement patient et identité numérique
status: stable
owner: Responsables de capabilités habilitantes
version: "0.1.0"
envelope: 00_caesn/03_capabilities/enabling.md
maps_to: ["CAP-INT-01", "CAP-INT-09"]
implements: []
applies_to: ["VS-01", "VS-03"]
related: ["VS-01", "VS-02", "PRC-01", "PRC-04", "PRC-07"]
tags: ["caesn", "niveau-1", "capabilite", "CAP-17", "identite", "consentement"]
realized_by: ["SRV-01"]
---
# Engagement patient et identité numérique

## Rôle dans le système

La capabilité garantit l'existence d'une identité unique, sécurisée et partagée pour chaque patient à travers le système d'information sanitaire national. Elle couvre :

- **Résolution d'identité** : recherche démographique, rapprochement de dossiers, détection des doublons
- **Gestion du consentement** : recueil, stockage et vérification du consentement du patient pour le partage de ses données
- **Identitovigilance** : surveillance et correction des erreurs d'identité, protection contre les usurpations
- **Engagement du patient** : accès du patient à ses données, participation active à la gestion de sa santé

Cette capabilité est **habilitante** : son absence bloque la continuité des soins ([VS-01: Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../flux-valeur/vs-01.md)) et la protection financière ([VS-03: Protéger financièrement la population face aux dépenses de santé](../flux-valeur/vs-03.md)).

## Flux de valeur

- [VS-01: Soins essentiels](../flux-valeur/vs-01.md)
- [VS-03: Protection financière](../flux-valeur/vs-03.md)

## Rattachement ARTSN

- [F-1: Résilience face à la réalité géographique du pays](../fondations/f-1.md)
- [ART-4A: Résolution d'identité](../chapitres/art-4a.md)
- [ART-4B: Bases d'autorisation](../chapitres/art-4b.md)
- [PT-04: Profil technique national](../profils/pt-04.md)

## Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 1/5 | 3/5 |

## Propriétaire

DEPSI + Direction des Systèmes d'Information
