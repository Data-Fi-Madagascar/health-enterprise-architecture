---
id: cap-17
type: capabilite
niveau: "1"
title: CAP-17 — Engagement patient et identité numérique
status: draft
owner: Responsables de capabilités habilitantes
version: "0.1.0"
source: 00_caesn/03_capabilities/enabling.md
maps_to: ["cap-int-01", "cap-int-09"]
implements: []
applies_to: ["vs-01", "vs-03"]
related: ["cap-04"]
tags: ['caesn', 'niveau-1', 'capabilite', 'cap-17', 'identite', 'consentement']
---
# CAP-17 — Engagement patient et identité numérique

## Rôle dans le système

La capabilité garantit l'existence d'une identité unique, sécurisée et partagée pour chaque patient à travers le système d'information sanitaire national. Elle couvre :

- **Résolution d'identité** : recherche démographique, rapprochement de dossiers, détection des doublons
- **Gestion du consentement** : recueil, stockage et vérification du consentement du patient pour le partage de ses données
- **Identitovigilance** : surveillance et correction des erreurs d'identité, protection contre les usurpations
- **Engagement du patient** : accès du patient à ses données, participation active à la gestion de sa santé

Cette capabilité est **habilitante** : son absence bloque la continuité des soins (VS-01) et la protection financière (VS-03).

## Flux de valeur

- [VS-01](../flux-valeur/vs-01.md) — Soins essentiels
- [VS-03](../flux-valeur/vs-03.md) — Protection financière

## Rattachement ARTSN

- **F.1** — Fondation Identité et registres
- **ART-4a** — Résolution d'identité
- **ART-4b** — Bases d'autorisation
- **PT-04** — Profil technique identité nationale

## Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 1/5 | 3/5 |

## Propriétaire

DEPSI + Direction des Systèmes d'Information
