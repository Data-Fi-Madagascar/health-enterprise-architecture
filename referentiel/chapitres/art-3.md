---
domain: chapitres

id: ART-3
type: chapitre
niveau: "3"
title: Historisation événementielle et profils de déploiement
status: stable
maturity_condition: "—"
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-3-historisation-evenementielle.md
maps_to: ["CAP-13"]
implements: []
applies_to: ["ENF-1"]
related: []
tags: ["artsn", "niveau-3", "chapitre", "ART-3"]
---
# Historisation événementielle et profils de déploiement

**Contenu normatif.** Le stockage de la donnée de santé doit être structuré sous forme de **journal d’événements ordonnés, non modifiables et cumulatifs**, agissant comme la source unique de vérité opérationnelle (event sourcing). L’architecture doit supporter trois profils d’intégration :

1. **Profil A** — historisation analytique en dérivation (*side-car*) ;
2. **Profil B** — système opérationnel natif ;
3. **Profil C** — fédération de réception tierce.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (bases de données locales distribuées, serveurs de districts isolés), cette discipline seule permet de rejouer l’historique complet d’un dossier patient ou de reconstruire un nœud après un sinistre matériel sans rompre le pipeline.

- **Rattachement** : [CAP-13: Système d'information sanitaire, données et recherche](../capabilites/cap-13.md) (gestion des données sanitaires).
- **Normes CNISN** : [STD-0003: X-Road](../../01_cnisn/05_standards/std-0003-x-road.md) (transport inter-institutionnel, [ADR-0001](../../01_cnisn/06_decisions/adr-0001-x-road.md)), [STD-0002: Sécurité et chiffrement](../../01_cnisn/05_standards/std-0002-securite-chiffrement.md).
- **Profils cibles** : Profil A, Profil B, Profil C.
- **Déduit selon** : [ENF-1: Résilience à l'instabilité réseau](../exigences/enf-1.md) (mode déconnecté).
- **Statut : Stable.**
