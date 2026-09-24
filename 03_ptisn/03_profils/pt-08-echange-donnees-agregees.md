---
title: "Échange de données agrégées"
id: ptisn-PT-08
domain: 03_profils
version: "1.0.0"
status: draft
last_reviewed: 2026-07-31
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "profils", "PT-08"]
related: ["ABB-ECHANGE-MEDIATION", "ABB-EXPOSITION-DONNEES-ANALYTIQUES", "ART-1", "ART-2", "ART-5", "ART-6", "CMP-03", "CMP-06"]
---

# Profil technique national

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

## 1. Objet et périmètre

Le **profil PT-08 — Échange de données agrégées** définit le service d’échange de rapports et indicateurs sanitaires agrégés. Il couvre la remontée des données agrégées des systèmes de collecte vers l’entrepôt national.

Périmètre : rapports périodiques d’activité et indicateurs de programme. Hors périmètre : les données individuelles (voir PT-04, PT-09) et la normalisation sémantique (voir PT-07).

## 2. Objet CNISN/TOGAF de référence

- [ABB-ECHANGE-MEDIATION: Échange et médiation inter-systèmes](../../04_architecture-repository/05_building-blocks/abb/abb-echange-mediation.md)
- contribution à [ABB-EXPOSITION-DONNEES-ANALYTIQUES: Accès et exposition des données analytiques](../../04_architecture-repository/05_building-blocks/abb/abb-exposition-donnees-analytiques.md)

## 3. Chapitres ART applicables

- [ART-1: Intégration et ingestion](../../04_architecture-repository/04_patterns/artsn-rules/art-1.md)
- [ART-2: Médiation et normalisation](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md)
- [ART-5: Cohérence et qualité des données](../../04_architecture-repository/04_patterns/artsn-rules/art-5.md)
- [ART-6: Analytique et restitution](../../04_architecture-repository/04_patterns/artsn-rules/art-6.md)

## 4. Acteurs (Actors)

- **Déclarant (Aggregate Data Reporter)** — établissement ou système de collecte soumettant un rapport périodique.
- **Récepteur de données agrégées (Aggregate Data Receiver)** — entrepôt national recevant et accusant réception des rapports.

*Référence - objet CNISN/TOGAF mis en œuvre : [ABB-ECHANGE-MEDIATION](../../04_architecture-repository/05_building-blocks/abb/abb-echange-mediation.md).
## 5. Transactions

| Transaction | Acteurs | R/O | Standard |
|----|----|----|----|
| T1 — Soumission de rapport agrégé | Déclarant → Récepteur | R | IHE mADX (ITI-73) |
| T2 — Accusé de réception | Récepteur → Déclarant | R | IHE mADX (ITI-73 response) |
| T3 — Compatibilité ADX (v2) | Déclarant → Récepteur | O | IHE ADX |

R = requis ; O = optionnel.

*Référence - objet CNISN/TOGAF mis en œuvre : [ABB-ECHANGE-MEDIATION](../../04_architecture-repository/05_building-blocks/abb/abb-echange-mediation.md).
## 6. Content Modules

- **HL7 FHIR MeasureReport** : rapport d’indicateurs agrégés.
- **HL7 FHIR Group / période / dimensions** : découpage du rapport (structure, programme, période).
- Dimensions résolues via PT-06 (structures) et PT-07 (terminologie).

## 7. Options

- **O1 — Profil cible** : mADX pour les nouvelles interfaces.
- **O2 — Compatibilité** : ADX pour les implémentations existantes.
- **O3 — Export CSV non profilé** : transitoire, non recommandé comme contrat national.
- **O4 — API propriétaire** : doit être médiée vers le profil national (PT-02).

## 8. Service national

**Service d’échange de rapports et indicateurs sanitaires agrégés** — positionnement :

| Profil                 | Position                                           |
|------------------------|----------------------------------------------------|
| mADX                   | Profil cible pour les nouvelles interfaces         |
| ADX                    | Compatibilité avec les implémentations existantes  |
| Export CSV non profilé | Transitoire, non recommandé comme contrat national |
| API propriétaire       | Doit être médiée vers le profil national           |

## 9. Formats et standards recommandés

**IHE mADX — Mobile Aggregate Data Exchange** : profil d’échange de données agrégées de santé publique, notamment les rapports périodiques produits par les établissements et transmis à une juridiction administrative. Fonctionnellement équivalent à ADX pour ces usages, tout en reposant sur FHIR.

*Référence — normes et standards CNISN : [01_cnisn/05_standards](../../01_cnisn/05_standards/index.md).
## 10. Exigences

Les codes et dimensions utilisés dans un rapport agrégé doivent être résolus par le service terminologique (PT-07), le référentiel des structures (PT-06), les définitions d’indicateurs, et les périodes/dimensions publiées. mADX ne remplace pas le service terminologique.

## 11. Déclaration de conformité (Integration Statement)

La plateforme nationale de traçabilité RMA constitue une première initiative d’application des contrats ART relatifs à l’ingestion, l’historisation, la qualité, la réconciliation et l’analytique. Le profil mADX doit être évalué comme contrat cible d’entrée et de sortie pour les données agrégées, indépendamment du format interne du système opérationnel.

## 12. Articulation avec les autres profils

- [PT-07: terminologie et codification](../../04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-07.md)
- [PT-06: référentiel des structures](../../04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-06.md)
- [PT-09: analytique et exposition de données](../../04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-09.md)
- [PT-01: échange interinstitutionnel](../../04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-01.md)

## 13. Limites et dépendances

mADX est un profil d’échange de données agrégées ; il ne remplace pas le service terminologique. Dépendance : entrepôt national et plateforme RMA pour la validation des contrats d’ingestion et d’analytique.

<!-- END:GENERATED -->

## Références au cadre

- **ARTSN — lots consommateurs** : [L3 — Médiation & registres](../../02_artsn/07_lots/index.md)
