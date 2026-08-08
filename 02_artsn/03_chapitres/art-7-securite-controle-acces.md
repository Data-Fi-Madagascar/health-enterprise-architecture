---
title: ART-7 — Sécurité, contrôle d'accès et résidence de la donnée
id: art-7-securite-controle-acces
domain: 02_artsn
version: "0.1.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-7, securite, residence, niveau-3]
---

# ART-7 — Sécurité, contrôle d'accès et résidence de la donnée

**Contenu normatif.** L'architecture impose un modèle de sécurité **strict par défaut**. Le contrôle d'accès doit combiner le rôle de l'agent et ses attributs contextuels ou territoriaux. Tout accès, lecture ou écriture doit être chiffré et journalisé de manière immuable. Les données de santé des citoyens ont l'obligation légale de **résider physiquement sur le territoire national**.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (terminaux mobiles volés sur le terrain, tentatives d'intrusions extérieures) : elle seule permet de garantir l'inviolabilité du secret médical et la souveraineté numérique de l'État sans rompre le pipeline.

- **Rattachement** : [CAP-15](../../00_caesn/03_capabilities/index.md) (cybersécurité et gouvernance de la sécurité).
- **Modèles cibles** : Zero-Trust, RBAC, ABAC, chiffrement (AES-256), AuditEvent FHIR.
- **Déduit selon** : [ENF-1](../02_exigences-contextuelles.md#enf-1--résilience-à-l-instabilité-réseau) (sécurité locale).
- **Statut : Stable.**

## Liens

- [Index des chapitres](./index.md)
- [Couche 1 — Infrastructure](../04_cartographie-cible.md)
- [Axe vertical 1 — Sécurité et confiance numérique](../04_cartographie-cible.md)
