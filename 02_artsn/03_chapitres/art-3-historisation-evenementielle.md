---
title: ART-3 — Historisation événementielle et profils de déploiement
id: art-3-historisation-evenementielle
domain: 02_artsn
version: "0.1.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-3, event-sourcing, niveau-3]
---

# ART-3 — Historisation événementielle et profils de déploiement

**Contenu normatif.** Le stockage de la donnée de santé doit être structuré sous forme de **journal d'événements ordonnés, non modifiables et cumulatifs**, agissant comme la source unique de vérité opérationnelle (event sourcing). L'architecture doit supporter trois profils d'intégration :

1. **Profil A** — historisation analytique en dérivation (*side-car*) ;
2. **Profil B** — système opérationnel natif ;
3. **Profil C** — fédération de réception tierce.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (bases de données locales distribuées, serveurs de districts isolés) : elle seule permet de rejouer l'historique complet d'un dossier patient ou de reconstruire un nœud après un sinistre matériel sans rompre le pipeline.

- **Rattachement** : [CAP-13](../../00_caesn/03_capabilities/index.md) (gestion des données sanitaires).
- **Profils cibles** : Profil A, Profil B, Profil C.
- **Déduit selon** : [ENF-1](../02_exigences-contextuelles.md#enf-1--résilience-à-l-instabilité-réseau) (mode déconnecté).
- **Statut : Stable.**

## Liens

- [Index des chapitres](./index.md)
- [Exigences contextuelles — ENF-1](../02_exigences-contextuelles.md)
- [Couche 2 — Point de service](../04_cartographie-cible.md)
