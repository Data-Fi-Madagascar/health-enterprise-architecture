---
domain: capabilites

id: CAP-05
type: capabilite
niveau: "1"
title: Surveillance épidémiologique, alerte, investigation et riposte
status: draft
owner: Responsables de capabilités métier
version: "0.1.0"
envelope: 00_caesn/03_capabilities/business.md
maps_to: []
implements: []
applies_to: ["VS-02"]
related: ["CAP-18"]
tags: ["caesn", "niveau-1", "capabilite", "CAP-05", "surveillance", "geospatial"]
---
# Surveillance épidémiologique, alerte, investigation et riposte

## Rôle dans le système

La capabilité couvre l'ensemble du cycle de gestion des risques sanitaires : détection des signaux, notification des cas, vérification, investigation, déclenchement de la riposte et retour d'expérience. Elle relie les formations sanitaires, les districts et le niveau central pour qu'une épidémie ou une urgence soit identifiée et traitée sans délai.

Elle couvre :
- **Détection et alerte** : surveillance sentinelle, notification des cas et signalement précoce des événements
- **Investigation** : vérification terrain, recherche des contacts et confirmation étiologique
- **Riposte** : coordination de la réponse, mesures de contrôle et retour d'expérience
- **Surveillance multisource** : agrégation des données laboratoires, cliniques et communautaires

La capabilité inclut désormais la **dimension géospatiale** :
- **Géolocalisation des formations sanitaires** : positionnement GPS de toutes les structures de soins
- **Cartographie des risques** : visualisation spatiale des foyers épidémiques et des zones à risque
- **Suivi temporel** : analyse des tendances épidémiques par zone géographique
- **Cloisonnement One Health** : surveillance conjointe santé humaine/animale/environnement par zone

Son absence fragilise la surveillance sanitaire ([VS-02: Prévenir, détecter et répondre aux risques sanitaires](../flux-valeur/vs-02.md)).

## Flux de valeur

- [VS-02: Prévention et surveillance](../flux-valeur/vs-02.md)

## Rattachement ARTSN

- [F-1: Résilience face à la réalité géographique du pays](../fondations/f-1.md)
- [ART-4D: Référentiel géospatial et d'exploitation partagé](../chapitres/art-4d.md)
- [PT-05: Profil technique national](../profils/pt-05.md)
- [PT-15: Surveillance One Health](../profils/pt-15.md)

## Maturité

| Niveau actuel | Niveau cible (2 ans) |
|---------------|----------------------|
| 2/5 | 3/5 |

## Propriétaire

Responsables de capabilités métier
