---
title: "ART-7 — Sécurité, contrôle d'accès et résidence de la donnée"
id: art-7
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-7, niveau-3]
---

# ART-7 — Sécurité, contrôle d'accès et résidence de la donnée

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


ART-7 — Sécurité, contrôle d'accès et résidence de la donnée constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : [`art-7`](../../referentiel/chapitres/art-7.md).

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

**Contenu normatif.** L’architecture impose un modèle de sécurité **strict par défaut**. Le contrôle d’accès doit combiner le rôle de l’agent et ses attributs contextuels ou territoriaux. Tout accès, lecture ou écriture doit être chiffré et journalisé de manière immuable. Les données de santé des citoyens ont l’obligation légale de **résider physiquement sur le territoire national**.

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (terminaux mobiles volés sur le terrain, tentatives d’intrusions extérieures) : elle seule permet de garantir l’inviolabilité du secret médical et la souveraineté numérique de l’État sans rompre le pipeline.

- **Rattachement** : [CAP-15](../../referentiel/capabilites/cap-15.md) (cybersécurité et gouvernance de la sécurité).
- **Modèles cibles** : Zero-Trust, RBAC, ABAC, chiffrement (AES-256), AuditEvent FHIR.
- **Déduit selon** : [ENF-1](../../referentiel/exigences/enf-1.md) (sécurité locale).
- **Statut : Stable.**

*Rattachement : [ENF-1](../../referentiel/exigences/enf-1.md), [CAP-15](../../referentiel/capabilites/cap-15.md) · [fiche](../../referentiel/chapitres/art-7.md)*

<!-- END:GENERATED -->
## Liens

- [Index des chapitres](./index.md)
- [Exigences contextuelles — Partie III](../02_exigences-contextuelles.md)
