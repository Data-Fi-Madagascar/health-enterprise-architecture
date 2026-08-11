---
id: art-7
type: chapitre
niveau: "3"
title: ART-7 — Sécurité, contrôle d'accès et résidence de la donnée
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/03_chapitres/art-7-securite-controle-acces.md
maps_to: ["cap-15"]
implements: []
applies_to: ["enf-1"]
related: []
tags: ['artsn', 'niveau-3', 'chapitre', 'art-7']
---
# ART-7 — Sécurité, contrôle d’accès et résidence de la donnée

**Contenu normatif.** L’architecture impose un modèle de sécurité **strict par défaut**. Le contrôle d’accès doit combiner le rôle de l’agent et ses attributs contextuels ou territoriaux. Tout accès, lecture ou écriture doit être chiffré et journalisé de manière immuable. Les données de santé des citoyens ont l’obligation légale de **résider physiquement sur le territoire national**.

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (terminaux mobiles volés sur le terrain, tentatives d’intrusions extérieures) : elle seule permet de garantir l’inviolabilité du secret médical et la souveraineté numérique de l’État sans rompre le pipeline.

- **Rattachement** : [CAP-15](../capabilites/cap-15.md) (cybersécurité et gouvernance de la sécurité).
- **Modèles cibles** : Zero-Trust, RBAC, ABAC, chiffrement (AES-256), AuditEvent FHIR.
- **Déduit selon** : [ENF-1](../exigences/enf-1.md) (sécurité locale).
- **Statut : Stable.**
