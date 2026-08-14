---
title: "ART-3 — Historisation événementielle et profils de déploiement"
id: art-3
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-3, niveau-3]
---

# ART-3 — Historisation événementielle et profils de déploiement

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


ART-3 — Historisation événementielle et profils de déploiement constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : [`art-3`](../../referentiel/chapitres/art-3.md).

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

**Contenu normatif.** Le stockage de la donnée de santé doit être structuré sous forme de **journal d’événements ordonnés, non modifiables et cumulatifs**, agissant comme la source unique de vérité opérationnelle (event sourcing). L’architecture doit supporter trois profils d’intégration :

1. **Profil A** — historisation analytique en dérivation (*side-car*) ;
2. **Profil B** — système opérationnel natif ;
3. **Profil C** — fédération de réception tierce.

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (bases de données locales distribuées, serveurs de districts isolés) : elle seule permet de rejouer l’historique complet d’un dossier patient ou de reconstruire un nœud après un sinistre matériel sans rompre le pipeline.

- **Rattachement** : [CAP-13](../../referentiel/capabilites/cap-13.md) (gestion des données sanitaires).
- **Profils cibles** : Profil A, Profil B, Profil C.
- **Déduit selon** : [ENF-1](../../referentiel/exigences/enf-1.md) (mode déconnecté).
- **Statut : Stable.**

*Rattachement : [ENF-1](../../referentiel/exigences/enf-1.md), [CAP-13](../../referentiel/capabilites/cap-13.md) · [fiche](../../referentiel/chapitres/art-3.md)*

<!-- END:GENERATED -->
## Liens

- [Index des chapitres](./index.md)
- [Exigences contextuelles — Partie III](../02_exigences-contextuelles/index.md)
