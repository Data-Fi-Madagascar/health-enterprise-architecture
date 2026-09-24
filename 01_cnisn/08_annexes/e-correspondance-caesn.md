---
title: "Annexe E : Correspondance CAESN–CNISN"
id: cnisn-annexe-e
domain: 08_annexes
version: "1.0.0"
status: draft
last_reviewed: 2026-08-11
owner: DEPSI
tags: ["cnisn", "niveau-2", "annexes"]
---

# Annexe E : Correspondance CAESN–CNISN

Cette annexe documente le rattachement des objets d'interopérabilité CNISN/TOGAF et des principes P-INT aux capabilités CAESN (CAP-01..18). Elle reflète les liens portés par le frontmatter des objets (champ `maps_to`).

## Correspondance objets CNISN/TOGAF -> capabilités CAESN

| Objet CNISN/TOGAF | Intitulé | Capabilités CAESN (CAP-XX) | Principes associés (P-INT) |
|---|---|---|---|
| ABB-IDENTITE-BENEFICIAIRE | Résolution d’identité du bénéficiaire | CAP-02, CAP-14, CAP-17 | P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-14, P-INT-15, P-INT-16, P-INT-17, P-INT-18 |
| ABB-REGISTRE-PROFESSIONNELS | Registre et résolution des professionnels de santé | CAP-09, CAP-14 | P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-14, P-INT-15 |
| ABB-ECHANGE-MEDIATION | Échange et médiation inter-systèmes | CAP-13, CAP-14, CAP-18 | P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-10, P-INT-11, P-INT-12, P-INT-13, P-INT-18, P-INT-19, P-INT-20, P-INT-21, P-INT-22, P-INT-23, P-INT-24, P-INT-25 |
| ABB-REFERENTIEL-STRUCTURES-SERVICES | Référentiel des structures et services de santé | CAP-11, CAP-13, CAP-14 | P-INT-01, P-INT-02, P-INT-03, P-INT-04 |
| ABB-SERVICE-TERMINOLOGIE | Terminologie et codification communes | CAP-13, CAP-14 | P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-05, P-INT-06 |
| ABB-CATALOGUE-CONTRATS | Catalogue des services et registre des contrats | CAP-14, CAP-16 | P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-23, P-INT-24, P-INT-25 |
| ABB-EXPOSITION-DONNEES-ANALYTIQUES | Accès et exposition des données analytiques | CAP-05, CAP-13 | P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-17, P-INT-18, P-INT-19, P-INT-20, P-INT-21, P-INT-22, P-INT-23, P-INT-24, P-INT-25 |
| ABB-CONFIANCE-AUTORISATION | Confiance, sécurité et autorisation | CAP-15 | P-INT-14, P-INT-15, P-INT-16, P-INT-17, P-INT-18, P-INT-19, P-INT-20 |
| ABB-GESTION-CONSENTEMENT | Gestion des consentements et bases d’autorisation | CAP-15, CAP-17 | P-INT-14, P-INT-15, P-INT-16, P-INT-17 |
| ABB-AUDIT-PROVENANCE | Provenance, audit et traçabilité | CAP-13, CAP-15 | P-INT-07, P-INT-17, P-INT-18, P-INT-23 |
| ABB-RECONCILIATION-DONNEES | Qualité et réconciliation | CAP-13, CAP-14 | P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-23, P-INT-24, P-INT-25 |
| COMP-HOMOLOGATION-INTEROPERABILITE | Conformité et tests d’interopérabilité | CAP-14, CAP-16 | P-INT-19, P-INT-20, P-INT-21, P-INT-22, P-INT-23, P-INT-24, P-INT-25 |
| PART-ECHANGE-TRANSFRONTALIER | Interopérabilité transfrontalière et confiance internationale | CAP-15 | P-INT-01, P-INT-05, P-INT-10, P-INT-14, P-INT-16, P-INT-17, P-INT-19 |
| PART-ONE-HEALTH | Échanges intersectoriels One Health | CAP-18 | P-INT-01, P-INT-05, P-INT-10, P-INT-14, P-INT-16, P-INT-22 |

## Correspondance principes CNISN → capabilités CAESN

| Principe CNISN | Intitulé | Capabilités CAESN (CAP-XX) | Objets CNISN/TOGAF |
|---|---|---|---|
| P-INT-01 | Autorité désignée | CAP-14 | ABB-IDENTITE-BENEFICIAIRE, ABB-REGISTRE-PROFESSIONNELS, ABB-REFERENTIEL-STRUCTURES-SERVICES, ABB-SERVICE-TERMINOLOGIE, ABB-RECONCILIATION-DONNEES |
| P-INT-02 | Résolution contre l’autorité | CAP-14 | ABB-IDENTITE-BENEFICIAIRE, ABB-REGISTRE-PROFESSIONNELS, ABB-REFERENTIEL-STRUCTURES-SERVICES, ABB-SERVICE-TERMINOLOGIE, ABB-RECONCILIATION-DONNEES |
| P-INT-03 | Copies locales non autoritatives | CAP-14 | ABB-IDENTITE-BENEFICIAIRE, ABB-REGISTRE-PROFESSIONNELS, ABB-REFERENTIEL-STRUCTURES-SERVICES, ABB-SERVICE-TERMINOLOGIE, ABB-RECONCILIATION-DONNEES |
| P-INT-04 | Historisation des références | CAP-14 | ABB-IDENTITE-BENEFICIAIRE, ABB-REGISTRE-PROFESSIONNELS, ABB-REFERENTIEL-STRUCTURES-SERVICES, ABB-SERVICE-TERMINOLOGIE, ABB-RECONCILIATION-DONNEES |
| P-INT-05 | Contrat explicite | CAP-14 | ABB-ECHANGE-MEDIATION, ABB-SERVICE-TERMINOLOGIE, ABB-CATALOGUE-CONTRATS, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-RECONCILIATION-DONNEES |
| P-INT-06 | Versionnement et compatibilité | CAP-14 | ABB-ECHANGE-MEDIATION, ABB-SERVICE-TERMINOLOGIE, ABB-CATALOGUE-CONTRATS, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-RECONCILIATION-DONNEES |
| P-INT-07 | Responsabilité de la donnée | CAP-13 | ABB-ECHANGE-MEDIATION, ABB-CATALOGUE-CONTRATS, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-AUDIT-PROVENANCE, ABB-RECONCILIATION-DONNEES |
| P-INT-08 | Publication au catalogue des services | CAP-14, CAP-16 | ABB-ECHANGE-MEDIATION, ABB-CATALOGUE-CONTRATS, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-RECONCILIATION-DONNEES |
| P-INT-09 | Publication des contrats | CAP-14, CAP-16 | ABB-ECHANGE-MEDIATION, ABB-CATALOGUE-CONTRATS, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-RECONCILIATION-DONNEES |
| P-INT-10 | Accord préalable | CAP-14 | ABB-ECHANGE-MEDIATION |
| P-INT-11 | Arbitrage des conflits d’autorité | CAP-14 | ABB-ECHANGE-MEDIATION |
| P-INT-12 | Dérogation explicite | CAP-14, CAP-16 | ABB-ECHANGE-MEDIATION |
| P-INT-13 | Dérogation d’urgence | CAP-14, CAP-16 | ABB-ECHANGE-MEDIATION |
| P-INT-14 | Base d’autorisation explicite | CAP-15 | ABB-IDENTITE-BENEFICIAIRE, ABB-REGISTRE-PROFESSIONNELS, ABB-CONFIANCE-AUTORISATION, ABB-GESTION-CONSENTEMENT |
| P-INT-15 | Limitation à la finalité | CAP-15 | ABB-IDENTITE-BENEFICIAIRE, ABB-REGISTRE-PROFESSIONNELS, ABB-CONFIANCE-AUTORISATION, ABB-GESTION-CONSENTEMENT |
| P-INT-16 | Résidence et non-réplication | CAP-14, CAP-15 | ABB-IDENTITE-BENEFICIAIRE, ABB-CONFIANCE-AUTORISATION, ABB-GESTION-CONSENTEMENT |
| P-INT-17 | Minimisation | CAP-15 | ABB-IDENTITE-BENEFICIAIRE, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-CONFIANCE-AUTORISATION, ABB-GESTION-CONSENTEMENT, ABB-AUDIT-PROVENANCE |
| P-INT-18 | Traçabilité différenciée | CAP-13, CAP-15 | ABB-IDENTITE-BENEFICIAIRE, ABB-ECHANGE-MEDIATION, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-CONFIANCE-AUTORISATION, ABB-AUDIT-PROVENANCE |
| P-INT-19 | Neutralité technologique | CAP-14 | ABB-ECHANGE-MEDIATION, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-CONFIANCE-AUTORISATION, COMP-HOMOLOGATION-INTEROPERABILITE |
| P-INT-20 | Portabilité et réversibilité | CAP-14 | ABB-ECHANGE-MEDIATION, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-CONFIANCE-AUTORISATION, COMP-HOMOLOGATION-INTEROPERABILITE |
| P-INT-21 | Progressivité | CAP-16 | ABB-ECHANGE-MEDIATION, ABB-EXPOSITION-DONNEES-ANALYTIQUES, COMP-HOMOLOGATION-INTEROPERABILITE |
| P-INT-22 | Fonctionnement en connectivité contrainte | CAP-14 | ABB-ECHANGE-MEDIATION, ABB-EXPOSITION-DONNEES-ANALYTIQUES, COMP-HOMOLOGATION-INTEROPERABILITE |
| P-INT-23 | Conformité fondée sur des preuves | CAP-16 | ABB-ECHANGE-MEDIATION, ABB-CATALOGUE-CONTRATS, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-AUDIT-PROVENANCE, ABB-RECONCILIATION-DONNEES, COMP-HOMOLOGATION-INTEROPERABILITE |
| P-INT-24 | Applicabilité déclarée | CAP-16 | ABB-ECHANGE-MEDIATION, ABB-CATALOGUE-CONTRATS, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-RECONCILIATION-DONNEES, COMP-HOMOLOGATION-INTEROPERABILITE |
| P-INT-25 | Réévaluation continue | CAP-16 | ABB-ECHANGE-MEDIATION, ABB-CATALOGUE-CONTRATS, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-RECONCILIATION-DONNEES, COMP-HOMOLOGATION-INTEROPERABILITE |

## Correspondance inverse : capabilités CAESN -> objets CNISN/TOGAF

| Capabilité CAESN | Intitulé | Objets CNISN/TOGAF |
|---|---|---|
| CAP-01 | Offre de soins et continuité des services | : |
| CAP-02 | Gestion du parcours patient, référence et contre-référence | ABB-IDENTITE-BENEFICIAIRE |
| CAP-03 | Qualité, sécurité des soins et amélioration continue | : |
| CAP-04 | Santé communautaire et engagement des communautés | : |
| CAP-05 | Surveillance épidémiologique, alerte, investigation et riposte | ABB-EXPOSITION-DONNEES-ANALYTIQUES |
| CAP-06 | Vaccination, prévention et promotion de la santé | : |
| CAP-07 | Protection financière, couverture santé universelle | : |
| CAP-08 | Gouvernance institutionnelle, planification, coordination et redevabilité | : |
| CAP-09 | Gestion des ressources humaines en santé | ABB-REGISTRE-PROFESSIONNELS |
| CAP-10 | Gestion des médicaments, vaccins, intrants et chaîne d'approvisionnement | : |
| CAP-11 | Gestion des infrastructures, équipements et maintenance | ABB-REFERENTIEL-STRUCTURES-SERVICES |
| CAP-12 | Finances publiques, budget et allocation des ressources | : |
| CAP-13 | Système d'information sanitaire, données et recherche | ABB-ECHANGE-MEDIATION, ABB-REFERENTIEL-STRUCTURES-SERVICES, ABB-SERVICE-TERMINOLOGIE, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-AUDIT-PROVENANCE, ABB-RECONCILIATION-DONNEES |
| CAP-14 | Interopérabilité, référentiels nationaux et infrastructure numérique partagée | ABB-IDENTITE-BENEFICIAIRE, ABB-REGISTRE-PROFESSIONNELS, ABB-ECHANGE-MEDIATION, ABB-REFERENTIEL-STRUCTURES-SERVICES, ABB-SERVICE-TERMINOLOGIE, ABB-CATALOGUE-CONTRATS, ABB-RECONCILIATION-DONNEES, COMP-HOMOLOGATION-INTEROPERABILITE |
| CAP-15 | Cybersécurité, confidentialité et gouvernance des données personnelles | ABB-CONFIANCE-AUTORISATION, ABB-GESTION-CONSENTEMENT, ABB-AUDIT-PROVENANCE |
| CAP-16 | Gestion du portefeuille d'initiatives numériques | ABB-CATALOGUE-CONTRATS, COMP-HOMOLOGATION-INTEROPERABILITE |
| CAP-17 | Engagement patient et identité numérique | ABB-IDENTITE-BENEFICIAIRE, ABB-GESTION-CONSENTEMENT |
| CAP-18 | Coordination intersectorielle (One Health) | ABB-ECHANGE-MEDIATION, PART-ONE-HEALTH |

*Rattachés au niveau 2 (CNISN) : 01_cnisn/02_capacites.md, 01_cnisn/01_principes.md.*

## Références

- [CAP-02](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-02.md)
- [CAP-14](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-14.md)
- [P-INT-01](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-01.md)
- [P-INT-02](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-02.md)
- [P-INT-03](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-03.md)
- [P-INT-04](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-04.md)
- [P-INT-14](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-14.md)
- [P-INT-15](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-15.md)
- [P-INT-16](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-16.md)
- [P-INT-17](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-17.md)
- [P-INT-18](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-18.md)
- [CAP-09](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-09.md)
- [CAP-13](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-13.md)
- [P-INT-05](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-05.md)
- [P-INT-06](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-06.md)
- [P-INT-07](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-07.md)
- [P-INT-08](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-08.md)
- [P-INT-09](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-09.md)
- [P-INT-10](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-10.md)
- [P-INT-11](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-11.md)
- [P-INT-12](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-12.md)
- [P-INT-13](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-13.md)
- [P-INT-19](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-19.md)
- [P-INT-20](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-20.md)
- [P-INT-21](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-21.md)
- [P-INT-22](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-22.md)
- [P-INT-23](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-23.md)
- [P-INT-24](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-24.md)
- [P-INT-25](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-25.md)
- [CAP-11](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-11.md)
- [CAP-16](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-16.md)
- [CAP-17](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-17.md)
- [CAP-18](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-18.md)
- [CAP-05](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-05.md)
- [CAP-15](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-15.md)
- [ABB-IDENTITE-BENEFICIAIRE](../../04_architecture-repository/05_building-blocks/abb/abb-identite-beneficiaire.md)
- [ABB-REGISTRE-PROFESSIONNELS](../../04_architecture-repository/05_building-blocks/abb/abb-registre-professionnels.md)
- [ABB-REFERENTIEL-STRUCTURES-SERVICES](../../04_architecture-repository/05_building-blocks/abb/abb-referentiel-structures-services.md)
- [ABB-SERVICE-TERMINOLOGIE](../../04_architecture-repository/05_building-blocks/abb/abb-service-terminologie.md)
- [ABB-RECONCILIATION-DONNEES](../../04_architecture-repository/05_building-blocks/abb/abb-reconciliation-donnees.md)
- [ABB-ECHANGE-MEDIATION](../../04_architecture-repository/05_building-blocks/abb/abb-echange-mediation.md)
- [ABB-CATALOGUE-CONTRATS](../../04_architecture-repository/05_building-blocks/abb/abb-catalogue-contrats.md)
- [ABB-EXPOSITION-DONNEES-ANALYTIQUES](../../04_architecture-repository/05_building-blocks/abb/abb-exposition-donnees-analytiques.md)
- [ABB-AUDIT-PROVENANCE](../../04_architecture-repository/05_building-blocks/abb/abb-audit-provenance.md)
- [ABB-CONFIANCE-AUTORISATION](../../04_architecture-repository/05_building-blocks/abb/abb-confiance-autorisation.md)
- [ABB-GESTION-CONSENTEMENT](../../04_architecture-repository/05_building-blocks/abb/abb-gestion-consentement.md)
- [COMP-HOMOLOGATION-INTEROPERABILITE](../../04_architecture-repository/06_governance/compliance/comp-homologation-interoperabilite.md)
- [PART-ECHANGE-TRANSFRONTALIER](../../04_architecture-repository/01_partitions/externes/part-echange-transfrontalier.md)
- [PART-ONE-HEALTH](../../04_architecture-repository/01_partitions/sectorielles/part-one-health.md)
- [01_cnisn/02_capacites.md](../02_capacites/index.md)
- [01_cnisn/01_principes.md](../01_principes/index.md)
