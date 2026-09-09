---
domain: chapitres

id: ART-8C
type: chapitre
niveau: "3"
title: Agrégation par lot
status: candidate
maturity_condition: "Confirmation par une initiative supplémentaire"
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-8c-agregation-par-lot.md
maps_to: ["CAP-13", "CAP-14"]
implements: []
applies_to: ["ENF-1", "ENF-2"]
related: ["ART-8"]
tags: ["artsn", "niveau-3", "chapitre", "ART-8C"]
---
# Agrégation par lot

**Contenu normatif.** L’architecture doit intégrer un moteur de traitement par lots capable de suspendre le flux transactionnel instantané pour regrouper les micro-agrégats individuels en un seul **agrégat consolidé de niveau supérieur** (pattern cible : *Netting*).

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (demandes massives de remboursements des pharmacies rurales, vagues de facturations d’hôpitaux), cette discipline seule permet de compiler les flux locaux et de générer une compensation globale unifiée sans saturer les réseaux d’échange centraux et sans rompre le pipeline.

- **Rattachement** : [CAP-13: Système d'information sanitaire, données et recherche](../capabilites/cap-13.md), [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../capabilites/cap-14.md).
- **Pattern cible** : Netting.
- **Déduit selon** : [ENF-1: Résilience à l'instabilité réseau](../exigences/enf-1.md) (réseau instable) et [ENF-2: Intégrité des flux et traçabilité des valeurs](../exigences/enf-2.md) (anti-fraude).
- **Statut : Proposition ouverte.**

## Profils PTISN qui implémentent ce chapitre

Les profils techniques nationaux ci-dessous déclarent implémenter ce chapitre ART dans leur champ `implements` (frontmatter du référentiel). Le profil constitue la spécification implémentable et testable ; le chapitre demeure le cadre normatif opposable.

- [PT-02 : Médiation intra-secteur](../profils/pt-02.md)

