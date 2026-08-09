---
title: ART-8d — Chorégraphie inter-institutionnelle
id: art-8d-choregraphie-interinstitutionnelle
domain: 02_artsn
version: "0.1.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-8d, choregraphie, pubsub, niveau-3]
---

# ART-8d — Chorégraphie inter-institutionnelle

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

**Contenu normatif.** Lorsque l'intégration implique plusieurs ministères co-égaux, l'architecture **proscrit l'orchestration centralisée** et impose un modèle de coordination par messagerie décentralisée. Les systèmes partenaires doivent s'abonner de manière autonome à des files d'événements publics sans qu'aucun nœud n'ait d'autorité informatique sur le système de l'autre (pattern cible : Publication/Abonnement, Pub/Sub).

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (systèmes d'information autonomes des ministères de l'Agriculture ou de l'Environnement) : elle seule permet de déclencher des actions conjointes et simultanées lors d'un signal épidémique tout en préservant l'indépendance informatique et la souveraineté de chaque institution, sans rompre le pipeline.

- **Rattachement** : [CAP-13](../../00_caesn/03_capabilities/index.md), [CAP-14](../../00_caesn/03_capabilities/index.md).
- **Pattern cible** : Publication / Abonnement (Pub/Sub).
- **Déduit selon** : [ENF-4](../02_exigences-contextuelles.md#enf-4--cloisonnement-inter-institutionnel-et-étanchéité-des-données-one-health) (souveraineté intersectorielle).
- **Statut : Proposition ouverte.**

## Liens

- [Index des chapitres](./index.md)
- [ART-8 — Orchestration de processus borné](./art-8-orchestration-processus-borne.md)
- [VS-02 — Risques sanitaires](../01_flux-de-valeur.md#vs-02--prévenir-détecter-et-répondre-aux-risques-sanitaires)
