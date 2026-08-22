---

title: "Agrégation par lot"
id: artsn-ART-8C
domain: 04_patterns
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: ["artsn", "chapitres", "ART-8C", "niveau-3"]
related: ["CAP-INT-03"]
---

# Agrégation par lot

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


ART-8C : Agrégation par lot constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `ART-8C`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Statut : candidate**

**Contenu normatif.** L’architecture doit intégrer un moteur de traitement par lots capable de suspendre le flux transactionnel instantané pour regrouper les micro-agrégats individuels en un seul **agrégat consolidé de niveau supérieur** (pattern cible : *Netting*).

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (demandes massives de remboursements des pharmacies rurales, vagues de facturations d’hôpitaux), cette discipline seule permet de compiler les flux locaux et de générer une compensation globale unifiée sans saturer les réseaux d’échange centraux et sans rompre le pipeline.

- **Rattachement** : [CAP-13: Système d'information sanitaire, données et recherche](../../referentiel/capabilites/cap-13.md), [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../../referentiel/capabilites/cap-14.md).
- **Pattern cible** : Netting.
- **Déduit selon** : [ENF-1: Résilience à l'instabilité réseau](../../referentiel/exigences/enf-1.md) (réseau instable) et [ENF-2: Intégrité des flux et traçabilité des valeurs](../../referentiel/exigences/enf-2.md) (anti-fraude).
- **Statut : Proposition ouverte.**

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`ART-8C`** : Agrégation par lot (`referentiel/chapitres/art-8c.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/04_patterns/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
