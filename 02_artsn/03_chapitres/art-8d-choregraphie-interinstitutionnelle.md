---
title: "ART-8d — Chorégraphie inter-institutionnelle"
id: art-8d
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-8d, niveau-3]
---

# ART-8d — Chorégraphie inter-institutionnelle

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).


ART-8d — Chorégraphie inter-institutionnelle constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : [`art-8d`](../../referentiel/chapitres/art-8d.md).

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

**Contenu normatif.** Lorsque l’intégration implique plusieurs ministères co-égaux, l’architecture **proscrit l’orchestration centralisée** et impose un modèle de coordination par messagerie décentralisée. Les systèmes partenaires doivent s’abonner de manière autonome à des files d’événements publics sans qu’aucun nœud n’ait d’autorité informatique sur le système de l’autre (pattern cible : Publication/Abonnement, Pub/Sub).

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (systèmes d’information autonomes des ministères de l’Agriculture ou de l’Environnement) : elle seule permet de déclencher des actions conjointes et simultanées lors d’un signal épidémique tout en préservant l’indépendance informatique et la souveraineté de chaque institution, sans rompre le pipeline.

- **Rattachement** : [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md).
- **Pattern cible** : Publication / Abonnement (Pub/Sub).
- **Déduit selon** : [ENF-4](../../referentiel/exigences/enf-4.md) (souveraineté intersectorielle).
- **Statut : Proposition ouverte.**

*Rattachement : [ENF-4](../../referentiel/exigences/enf-4.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md) · [fiche](../../referentiel/chapitres/art-8d.md)*

<!-- END:GENERATED -->
## Liens

- [Index des chapitres](./index.md)
- [Exigences contextuelles — Partie III](../02_exigences-contextuelles/index.md)
