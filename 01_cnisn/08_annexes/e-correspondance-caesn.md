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

Cette annexe documente le rattachement des objets CNISN (capacités CAP-INT et principes P-INT) aux capabilités CAESN (CAP-01…16). Elle reflète les liens portés par le frontmatter des objets (champ `maps_to`).

## Correspondance capacités CNISN → capabilités CAESN

| Capacité CNISN | Intitulé | Capabilités CAESN (CAP-XX) | Principes associés (P-INT) |
|---|---|---|---|
| CAP-INT-01 | Résolution d’identité du bénéficiaire | CAP-02, CAP-14 | P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-14, P-INT-15, P-INT-16, P-INT-17, P-INT-18 |
| CAP-INT-02 | Registre et résolution des professionnels de santé | CAP-09, CAP-14 | P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-14, P-INT-15 |
| CAP-INT-03 | Échange et médiation inter-systèmes | CAP-13, CAP-14 | P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-10, P-INT-11, P-INT-12, P-INT-13, P-INT-18, P-INT-19, P-INT-20, P-INT-21, P-INT-22, P-INT-23, P-INT-24, P-INT-25 |
| CAP-INT-04 | Référentiel des structures et services de santé | CAP-11, CAP-13, CAP-14 | P-INT-01, P-INT-02, P-INT-03, P-INT-04 |
| CAP-INT-05 | Terminologie et codification communes | CAP-13, CAP-14 | P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-05, P-INT-06 |
| CAP-INT-06 | Catalogue des services et registre des contrats | CAP-14, CAP-16 | P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-23, P-INT-24, P-INT-25 |
| CAP-INT-07 | Accès et exposition des données analytiques | CAP-05, CAP-13 | P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-17, P-INT-18, P-INT-19, P-INT-20, P-INT-21, P-INT-22, P-INT-23, P-INT-24, P-INT-25 |
| CAP-INT-08 | Confiance, sécurité et autorisation | CAP-15 | P-INT-14, P-INT-15, P-INT-16, P-INT-17, P-INT-18, P-INT-19, P-INT-20 |
| CAP-INT-09 | Gestion des consentements et bases d’autorisation | CAP-15 | P-INT-14, P-INT-15, P-INT-16, P-INT-17 |
| CAP-INT-10 | Provenance, audit et traçabilité | CAP-13, CAP-15 | P-INT-07, P-INT-17, P-INT-18, P-INT-23 |
| CAP-INT-11 | Qualité et réconciliation | CAP-13, CAP-14 | P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-23, P-INT-24, P-INT-25 |
| CAP-INT-12 | Conformité et tests d’interopérabilité | CAP-14, CAP-16 | P-INT-19, P-INT-20, P-INT-21, P-INT-22, P-INT-23, P-INT-24, P-INT-25 |

## Correspondance principes CNISN → capabilités CAESN

| Principe CNISN | Intitulé | Capabilités CAESN (CAP-XX) | Capacités CNISN (CAP-INT) |
|---|---|---|---|
| P-INT-01 | Autorité désignée | CAP-14 | CAP-INT-01, CAP-INT-02, CAP-INT-04, CAP-INT-05, CAP-INT-11 |
| P-INT-02 | Résolution contre l’autorité | CAP-14 | CAP-INT-01, CAP-INT-02, CAP-INT-04, CAP-INT-05, CAP-INT-11 |
| P-INT-03 | Copies locales non autoritatives | CAP-14 | CAP-INT-01, CAP-INT-02, CAP-INT-04, CAP-INT-05, CAP-INT-11 |
| P-INT-04 | Historisation des références | CAP-14 | CAP-INT-01, CAP-INT-02, CAP-INT-04, CAP-INT-05, CAP-INT-11 |
| P-INT-05 | Contrat explicite | CAP-14 | CAP-INT-03, CAP-INT-05, CAP-INT-06, CAP-INT-07, CAP-INT-11 |
| P-INT-06 | Versionnement et compatibilité | CAP-14 | CAP-INT-03, CAP-INT-05, CAP-INT-06, CAP-INT-07, CAP-INT-11 |
| P-INT-07 | Responsabilité de la donnée | CAP-13 | CAP-INT-03, CAP-INT-06, CAP-INT-07, CAP-INT-10, CAP-INT-11 |
| P-INT-08 | Publication au catalogue des services | CAP-14, CAP-16 | CAP-INT-03, CAP-INT-06, CAP-INT-07, CAP-INT-11 |
| P-INT-09 | Publication des contrats | CAP-14, CAP-16 | CAP-INT-03, CAP-INT-06, CAP-INT-07, CAP-INT-11 |
| P-INT-10 | Accord préalable | CAP-14 | CAP-INT-03 |
| P-INT-11 | Arbitrage des conflits d’autorité | CAP-14 | CAP-INT-03 |
| P-INT-12 | Dérogation explicite | CAP-14, CAP-16 | CAP-INT-03 |
| P-INT-13 | Dérogation d’urgence | CAP-14, CAP-16 | CAP-INT-03 |
| P-INT-14 | Base d’autorisation explicite | CAP-15 | CAP-INT-01, CAP-INT-02, CAP-INT-08, CAP-INT-09 |
| P-INT-15 | Limitation à la finalité | CAP-15 | CAP-INT-01, CAP-INT-02, CAP-INT-08, CAP-INT-09 |
| P-INT-16 | Résidence et non-réplication | CAP-14, CAP-15 | CAP-INT-01, CAP-INT-08, CAP-INT-09 |
| P-INT-17 | Minimisation | CAP-15 | CAP-INT-01, CAP-INT-07, CAP-INT-08, CAP-INT-09, CAP-INT-10 |
| P-INT-18 | Traçabilité différenciée | CAP-13, CAP-15 | CAP-INT-01, CAP-INT-03, CAP-INT-07, CAP-INT-08, CAP-INT-10 |
| P-INT-19 | Neutralité technologique | CAP-14 | CAP-INT-03, CAP-INT-07, CAP-INT-08, CAP-INT-12 |
| P-INT-20 | Portabilité et réversibilité | CAP-14 | CAP-INT-03, CAP-INT-07, CAP-INT-08, CAP-INT-12 |
| P-INT-21 | Progressivité | CAP-16 | CAP-INT-03, CAP-INT-07, CAP-INT-12 |
| P-INT-22 | Fonctionnement en connectivité contrainte | CAP-14 | CAP-INT-03, CAP-INT-07, CAP-INT-12 |
| P-INT-23 | Conformité fondée sur des preuves | CAP-16 | CAP-INT-03, CAP-INT-06, CAP-INT-07, CAP-INT-10, CAP-INT-11, CAP-INT-12 |
| P-INT-24 | Applicabilité déclarée | CAP-16 | CAP-INT-03, CAP-INT-06, CAP-INT-07, CAP-INT-11, CAP-INT-12 |
| P-INT-25 | Réévaluation continue | CAP-16 | CAP-INT-03, CAP-INT-06, CAP-INT-07, CAP-INT-11, CAP-INT-12 |

## Correspondance inverse : capabilités CAESN → capacités CNISN

| Capabilité CAESN | Intitulé | Capacités CNISN (CAP-INT) |
|---|---|---|
| CAP-01 | Offre de soins et continuité des services | : |
| CAP-02 | Gestion du parcours patient, référence et contre-référence | CAP-INT-01 |
| CAP-03 | Qualité, sécurité des soins et amélioration continue | : |
| CAP-04 | Santé communautaire et engagement des communautés | : |
| CAP-05 | Surveillance épidémiologique, alerte, investigation et riposte | CAP-INT-07 |
| CAP-06 | Vaccination, prévention et promotion de la santé | : |
| CAP-07 | Protection financière, couverture santé universelle | : |
| CAP-08 | Gouvernance institutionnelle, planification, coordination et redevabilité | : |
| CAP-09 | Gestion des ressources humaines en santé | CAP-INT-02 |
| CAP-10 | Gestion des médicaments, vaccins, intrants et chaîne d'approvisionnement | : |
| CAP-11 | Gestion des infrastructures, équipements et maintenance | CAP-INT-04 |
| CAP-12 | Finances publiques, budget et allocation des ressources | : |
| CAP-13 | Système d'information sanitaire, données et recherche | CAP-INT-03, CAP-INT-04, CAP-INT-05, CAP-INT-07, CAP-INT-10, CAP-INT-11 |
| CAP-14 | Interopérabilité, référentiels nationaux et infrastructure numérique partagée | CAP-INT-01, CAP-INT-02, CAP-INT-03, CAP-INT-04, CAP-INT-05, CAP-INT-06, CAP-INT-11, CAP-INT-12 |
| CAP-15 | Cybersécurité, confidentialité et gouvernance des données personnelles | CAP-INT-08, CAP-INT-09, CAP-INT-10 |
| CAP-16 | Gestion du portefeuille d'initiatives numériques | CAP-INT-06, CAP-INT-12 |

---

*Rattachées au niveau 2 (CNISN) : 01_cnisn/02_capacites.md, 01_cnisn/01_principes.md.*

## Références

- **CAP-02** : Gestion du parcours patient, référence et contre-référence (`referentiel/capabilites/cap-02.md`)
- **CAP-14** : Interopérabilité, référentiels nationaux et infrastructure numérique partagée (`referentiel/capabilites/cap-14.md`)
- **P-INT-01** : P-INT-01 : Autorité désignée (`referentiel/principes/p-int-01.md`)
- **P-INT-02** : P-INT-02 : Résolution contre l’autorité (`referentiel/principes/p-int-02.md`)
- **P-INT-03** : P-INT-03 : Copies locales non autoritatives (`referentiel/principes/p-int-03.md`)
- **P-INT-04** : P-INT-04 : Historisation des références (`referentiel/principes/p-int-04.md`)
- **P-INT-14** : P-INT-14 : Base d’autorisation explicite (`referentiel/principes/p-int-14.md`)
- **P-INT-15** : P-INT-15 : Limitation à la finalité (`referentiel/principes/p-int-15.md`)
- **P-INT-16** : P-INT-16 : Résidence et non-réplication (`referentiel/principes/p-int-16.md`)
- **P-INT-17** : P-INT-17 : Minimisation (`referentiel/principes/p-int-17.md`)
- **P-INT-18** : P-INT-18 : Traçabilité différenciée (`referentiel/principes/p-int-18.md`)
- **CAP-09** : Gestion des ressources humaines en santé (`referentiel/capabilites/cap-09.md`)
- **CAP-13** : Système d'information sanitaire, données et recherche (`referentiel/capabilites/cap-13.md`)
- **P-INT-05** : P-INT-05 : Contrat explicite (`referentiel/principes/p-int-05.md`)
- **P-INT-06** : P-INT-06 : Versionnement et compatibilité (`referentiel/principes/p-int-06.md`)
- **P-INT-07** : P-INT-07 : Responsabilité de la donnée (`referentiel/principes/p-int-07.md`)
- **P-INT-08** : P-INT-08 : Publication au catalogue des services (`referentiel/principes/p-int-08.md`)
- **P-INT-09** : P-INT-09 : Publication des contrats (`referentiel/principes/p-int-09.md`)
- **P-INT-10** : P-INT-10 : Accord préalable (`referentiel/principes/p-int-10.md`)
- **P-INT-11** : P-INT-11 : Arbitrage des conflits d’autorité (`referentiel/principes/p-int-11.md`)
- **P-INT-12** : P-INT-12 : Dérogation explicite (`referentiel/principes/p-int-12.md`)
- **P-INT-13** : P-INT-13 : Dérogation d’urgence (`referentiel/principes/p-int-13.md`)
- **P-INT-19** : P-INT-19 : Neutralité technologique (`referentiel/principes/p-int-19.md`)
- **P-INT-20** : P-INT-20 : Portabilité et réversibilité (`referentiel/principes/p-int-20.md`)
- **P-INT-21** : P-INT-21 : Progressivité (`referentiel/principes/p-int-21.md`)
- **P-INT-22** : P-INT-22 : Fonctionnement en connectivité contrainte (`referentiel/principes/p-int-22.md`)
- **P-INT-23** : P-INT-23 : Conformité fondée sur des preuves (`referentiel/principes/p-int-23.md`)
- **P-INT-24** : P-INT-24 : Applicabilité déclarée (`referentiel/principes/p-int-24.md`)
- **P-INT-25** : P-INT-25 : Réévaluation continue (`referentiel/principes/p-int-25.md`)
- **CAP-11** : Gestion des infrastructures, équipements et maintenance (`referentiel/capabilites/cap-11.md`)
- **CAP-16** : Gestion du portefeuille d'initiatives numériques (`referentiel/capabilites/cap-16.md`)
- **CAP-05** : Surveillance épidémiologique, alerte, investigation et riposte (`referentiel/capabilites/cap-05.md`)
- **CAP-15** : Cybersécurité, confidentialité et gouvernance des données personnelles (`referentiel/capabilites/cap-15.md`)
- **CAP-INT-01** : CAP-INT-01 : Résolution d’identité du bénéficiaire (`referentiel/capacites/cap-int-01.md`)
- **CAP-INT-02** : CAP-INT-02 : Registre et résolution des professionnels de santé (`referentiel/capacites/cap-int-02.md`)
- **CAP-INT-04** : CAP-INT-04 : Référentiel des structures et services de santé (`referentiel/capacites/cap-int-04.md`)
- **CAP-INT-05** : CAP-INT-05 : Terminologie et codification communes (`referentiel/capacites/cap-int-05.md`)
- **CAP-INT-11** : CAP-INT-11 : Qualité et réconciliation (`referentiel/capacites/cap-int-11.md`)
- **CAP-INT-03** : CAP-INT-03 : Échange et médiation inter-systèmes (`referentiel/capacites/cap-int-03.md`)
- **CAP-INT-06** : CAP-INT-06 : Catalogue des services et registre des contrats (`referentiel/capacites/cap-int-06.md`)
- **CAP-INT-07** : CAP-INT-07 : Accès et exposition des données analytiques (`referentiel/capacites/cap-int-07.md`)
- **CAP-INT-10** : CAP-INT-10 : Provenance, audit et traçabilité (`referentiel/capacites/cap-int-10.md`)
- **CAP-INT-08** : CAP-INT-08 : Confiance, sécurité et autorisation (`referentiel/capacites/cap-int-08.md`)
- **CAP-INT-09** : CAP-INT-09 : Gestion des consentements et bases d’autorisation (`referentiel/capacites/cap-int-09.md`)
- **CAP-INT-12** : CAP-INT-12 : Conformité et tests d’interopérabilité (`referentiel/capacites/cap-int-12.md`)
- **01_cnisn/02_capacites.md** : Partie II : Capacités nationales requises (`01_cnisn/02_capacites/index.md`)
- **01_cnisn/01_principes.md** : Partie I : Principes nationaux d'interopérabilité de santé (`01_cnisn/01_principes/index.md`)
