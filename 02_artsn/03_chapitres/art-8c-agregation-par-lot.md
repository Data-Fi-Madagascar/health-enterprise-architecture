---
title: "ART-8c — Agrégation par lot"
id: art-8c
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-8c, niveau-3]
---

# ART-8c — Agrégation par lot

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


ART-8c — Agrégation par lot constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : [`art-8c`](../../referentiel/chapitres/art-8c.md).

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

**Contenu normatif.** L’architecture doit intégrer un moteur de traitement par lots capable de suspendre le flux transactionnel instantané pour regrouper les micro-agrégats individuels en un seul **agrégat consolidé de niveau supérieur** (pattern cible : *Netting*).

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (demandes massives de remboursements des pharmacies rurales, vagues de facturations d’hôpitaux) : elle seule permet de compiler les flux locaux et de générer une compensation globale unifiée sans saturer les réseaux d’échange centraux et sans rompre le pipeline.

- **Rattachement** : [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md).
- **Pattern cible** : Netting.
- **Déduit selon** : [ENF-1](../../referentiel/exigences/enf-1.md) (réseau instable) et [ENF-2](../../referentiel/exigences/enf-2.md) (anti-fraude).
- **Statut : Proposition ouverte.**

*Rattachement : [ENF-1](../../referentiel/exigences/enf-1.md), [ENF-2](../../referentiel/exigences/enf-2.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md) · [fiche](../../referentiel/chapitres/art-8c.md)*

<!-- END:GENERATED -->
## Liens

- [Index des chapitres](./index.md)
- [Exigences contextuelles — Partie III](../02_exigences-contextuelles.md)
