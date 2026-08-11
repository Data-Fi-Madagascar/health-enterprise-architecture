---
title: "ART-9 — Garanties transactionnelles fortes"
id: art-9
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-9, niveau-3]
---

# ART-9 — Garanties transactionnelles fortes

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


ART-9 — Garanties transactionnelles fortes constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : [`art-9`](../../referentiel/chapitres/art-9.md).

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

**Contenu normatif.** Pour tout mouvement de valeur monétaire ou physique, l’architecture impose une contrainte de **grade comptable strict** basée sur un registre immuable, garantissant l’équilibre parfait des comptes (équation cible : *entrées − sorties = solde*). Toute écriture doit être associée à une signature non répudiable et un numéro de suivi de lot.

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (officines pharmaceutiques privées, gestionnaires de stocks régionaux, caisses de subventions) : elle seule permet d’empêcher les détournements de médicaments, de bloquer les marchés noirs et d’assurer la réconciliation à somme nulle de l’argent public, sans rompre le pipeline.

- **Rattachement** : recouvre partiellement [CAP-07](../../referentiel/capabilites/cap-07.md) (protection financière).
- **Équation cible** : entrées − sorties = solde.
- **Déduit selon** : [ENF-2](../../referentiel/exigences/enf-2.md) (grade comptable anti-fraude).
- **Statut : Proposition ouverte.**

*Rattachement : [ENF-2](../../referentiel/exigences/enf-2.md), [CAP-07](../../referentiel/capabilites/cap-07.md) · [fiche](../../referentiel/chapitres/art-9.md)*

<!-- END:GENERATED -->
## Liens

- [Index des chapitres](./index.md)
- [Exigences contextuelles — Partie III](../02_exigences-contextuelles.md)
