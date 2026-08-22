---
domain: chapitres

id: ART-7
type: chapitre
niveau: "3"
title: Sécurité, contrôle d'accès et résidence de la donnée
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-7-securite-controle-acces.md
maps_to: ["CAP-15"]
implements: []
applies_to: ["ENF-1"]
related: []
tags: ["artsn", "niveau-3", "chapitre", "ART-7"]
---
# Sécurité, contrôle d’accès et résidence de la donnée

**Contenu normatif.** L’architecture impose un modèle de sécurité **strict par défaut**. Le contrôle d’accès doit combiner le rôle de l’agent et ses attributs contextuels ou territoriaux. Tout accès, lecture ou écriture doit être chiffré et journalisé de manière immuable. Les données de santé des citoyens ont l’obligation légale de **résider physiquement sur le territoire national**.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (terminaux mobiles volés sur le terrain, tentatives d’intrusions extérieures), cette discipline seule permet de garantir l’inviolabilité du secret médical et la souveraineté numérique de l’État sans rompre le pipeline.

- **Rattachement** : [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../capabilites/cap-15.md) (cybersécurité et gouvernance de la sécurité).
- **Modèles cibles** : Zero-Trust, RBAC, ABAC, chiffrement (AES-256), AuditEvent FHIR.
- **Déduit selon** : [ENF-1: Résilience à l'instabilité réseau](../exigences/enf-1.md) (sécurité locale).
- **Statut : Stable.**
