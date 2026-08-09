---
title: ART-5 — Cohérence et qualité des données
id: art-5-coherence-qualite-donnees
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-5, qualite-donnees, niveau-3]
---

# ART-5 — Cohérence et qualité des données

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

**Contenu normatif.** Tout flux ingéré doit être audité en continu face aux dimensions de qualité des données. En cas de détection d'anomalie, le système a l'obligation de router l'événement vers l'une des **branches d'escalade humaine** définies réglementairement. Les circuits cibles sont : sécurité clinique, alerte épidémiologique, fraude financière, risque intersectoriel.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (données corrompues du terrain, anomalies massives de facturation) : elle seule permet d'aiguiller le problème vers la bonne cellule humaine de décision stratégique sans rompre le pipeline.

- **Rattachement** : [CAP-13](../../00_caesn/03_capabilities/index.md) (gestion des données sanitaires).
- **Référentiel cible** : DAMA/DMBOK.
- **Circuits cibles** : sécurité clinique, alerte épidémiologique, fraude financière, risque intersectoriel.
- **Déduit selon** : [ENF-5](../02_exigences-contextuelles.md#enf-5--coordination-des-processus-complexes-décentralisés-et-asynchrones) (coordination des processus).
- **Statut : Stable** (pour les métriques) / **Proposition ouverte** (pour la gouvernance des 4 branches).

## Liens

- [Index des chapitres](./index.md)
- [Exigences contextuelles — ENF-5](../02_exigences-contextuelles.md)
- [Couche 5 — Projections analytiques et modèles](../04_cartographie-cible.md)
