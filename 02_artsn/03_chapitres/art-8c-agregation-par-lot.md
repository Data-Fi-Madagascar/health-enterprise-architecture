---
title: "ART-8c : Agrégation par lot"
id: art-8c
domain: 02_artsn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-8c, niveau-3]
related: ['cap-int-03']
---

# ART-8c : Agrégation par lot

## Pour qui lire ce document

**Niveau :** niveau 3 : Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.


ART-8c : Agrégation par lot constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `art-8c`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Contenu normatif.** L’architecture doit intégrer un moteur de traitement par lots capable de suspendre le flux transactionnel instantané pour regrouper les micro-agrégats individuels en un seul **agrégat consolidé de niveau supérieur** (pattern cible : *Netting*).

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (demandes massives de remboursements des pharmacies rurales, vagues de facturations d’hôpitaux) : elle seule permet de compiler les flux locaux et de générer une compensation globale unifiée sans saturer les réseaux d’échange centraux et sans rompre le pipeline.

- **Rattachement** : CAP-13, CAP-14.
- **Pattern cible** : Netting.
- **Déduit selon** : ENF-1 (réseau instable) et ENF-2 (anti-fraude).
- **Statut : Proposition ouverte.**

*Rattachement : ENF-1, ENF-2, CAP-13, CAP-14 · fiche ART-8C*

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`art-8c`** : Agrégation par lot (`referentiel/chapitres/art-8c.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/03_chapitres/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
