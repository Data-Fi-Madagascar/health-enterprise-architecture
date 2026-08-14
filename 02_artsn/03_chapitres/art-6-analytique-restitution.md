---
title: "ART-6 — Analytique et restitution"
id: art-6
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-6, niveau-3]
---

# ART-6 — Analytique et restitution

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


ART-6 — Analytique et restitution constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : [`art-6`](../../referentiel/chapitres/art-6.md).

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

**Contenu normatif.** L’architecture doit imposer une **séparation étanche entre le stockage opérationnel et le stockage analytique** (CQRS). L’entrepôt analytique doit être alimenté par des pipelines automatisés intégrant un moteur de masquage irréversible, et doit supporter nativement quatre types de requêtes : projections tabulaires, parcours de graphes, réconciliation comptable et fusion de signaux géospatiaux.

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (requêtes lourdes des décideurs, extractions massives pour la recherche) : elle seule permet de garantir des performances de restitution constantes et une sécurité réglementaire absolue sans surcharger les serveurs de soins et sans rompre le pipeline.

- **Rattachement** : [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-08](../../referentiel/capabilites/cap-08.md) (analytics & décisionnel).
- **Infrastructure cible** : Data Lakehouse.
- **Pattern cible** : modèle de séparation CQRS.
- **Déduit selon** : [ENF-4](../../referentiel/exigences/enf-4.md) (protection One Health).
- **Statut : Provisoire.**

*Rattachement : [ENF-4](../../referentiel/exigences/enf-4.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-08](../../referentiel/capabilites/cap-08.md) · [fiche](../../referentiel/chapitres/art-6.md)*

<!-- END:GENERATED -->
## Liens

- [Index des chapitres](./index.md)
- [Exigences contextuelles — Partie III](../02_exigences-contextuelles/index.md)
