---
title: Profil technique national
id: ptisn-PT-08
domain: 03_profils
version: "1.0.0"
status: draft
last_reviewed: 2026-07-31
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "profils", "PT-08"]
---

# Profil technique national

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

## 1. Capacités CNISN

- [CAP-INT-03: Échange et médiation inter-systèmes](../../referentiel/capacites/cap-int-03.md)
- contribution à [CAP-INT-07: Accès et exposition des données analytiques](../../referentiel/capacites/cap-int-07.md)

## 2. Chapitres ART applicables

- [ART-1: Intégration et ingestion](../../referentiel/chapitres/art-1.md) ;
- [ART-2: Médiation et normalisation](../../referentiel/chapitres/art-2.md) ;
- [ART-5: Cohérence et qualité des données](../../referentiel/chapitres/art-5.md) ;
- [ART-6: Analytique et restitution](../../referentiel/chapitres/art-6.md).

## 3. Service national

**Service d’échange de rapports et indicateurs sanitaires agrégés**

## 4. Cas d’usage

- rapports mensuels d’activité ;
- rapports hebdomadaires ;
- rapports trimestriels ;
- indicateurs de programme ;
- remontée communautaire ;
- reporting international ;
- transmission établissement-district ;
- échange entre systèmes de collecte et entrepôt national.

## 5. Profil cible

**IHE mADX — Mobile Aggregate Data Exchange**

mADX est conçu pour l’échange interopérable de données agrégées de santé publique, notamment les rapports périodiques produits par les établissements et transmis à une juridiction administrative. Il est présenté comme fonctionnellement équivalent à ADX pour ces usages, tout en reposant sur FHIR.

## 6. Positionnement

| Profil                 | Position                                           |
|------------------------|----------------------------------------------------|
| mADX                   | Profil cible pour les nouvelles interfaces         |
| ADX                    | Compatibilité avec les implémentations existantes  |
| Export CSV non profilé | Transitoire, non recommandé comme contrat national |
| API propriétaire       | Doit être médiée vers le profil national           |

## 7. Relation avec la terminologie

mADX est un profil d’échange de données agrégées.

Il ne remplace pas le service terminologique.

Les codes et dimensions utilisés dans un rapport agrégé doivent être résolus par :

- le service terminologique ;
- le référentiel des structures ;
- les définitions d’indicateurs ;
- les périodes et dimensions publiées.

## 8. Relation avec la plateforme RMA

La plateforme nationale de traçabilité RMA constitue une première initiative d’application des contrats ART relatifs :

- à l’ingestion ;
- à l’historisation ;
- à la qualité ;
- à la réconciliation ;
- à l’analytique.

Le profil mADX doit être évalué comme contrat cible d’entrée et de sortie pour les données agrégées, indépendamment du format interne du système opérationnel.

------------------------------------------------------------------------

<!-- END:GENERATED -->
