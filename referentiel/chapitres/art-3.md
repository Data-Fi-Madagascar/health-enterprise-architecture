---
id: art-3
type: chapitre
niveau: "4"
title: ART-3 — Historisation événementielle et profils de déploiement
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/03_chapitres/art-3-historisation-evenementielle.md
maps_to: ["cap-13"]
implements: []
applies_to: ["enf-1"]
related: []
tags: ['artsn', 'niveau-4', 'chapitre', 'art-3']
---
# ART-3 — Historisation événementielle et profils de déploiement

**Contenu normatif.** Le stockage de la donnée de santé doit être structuré sous forme de **journal d'événements ordonnés, non modifiables et cumulatifs**, agissant comme la source unique de vérité opérationnelle (event sourcing). L'architecture doit supporter trois profils d'intégration :

1. **Profil A** — historisation analytique en dérivation (*side-car*) ;
2. **Profil B** — système opérationnel natif ;
3. **Profil C** — fédération de réception tierce.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (bases de données locales distribuées, serveurs de districts isolés) : elle seule permet de rejouer l'historique complet d'un dossier patient ou de reconstruire un nœud après un sinistre matériel sans rompre le pipeline.

- **Rattachement** : [CAP-13](../capabilites/cap-13.md) (gestion des données sanitaires).
- **Profils cibles** : Profil A, Profil B, Profil C.
- **Déduit selon** : [ENF-1](../exigences/enf-1.md) (mode déconnecté).
- **Statut : Stable.**
