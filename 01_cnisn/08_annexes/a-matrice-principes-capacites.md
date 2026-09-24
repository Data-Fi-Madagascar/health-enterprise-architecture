---
title: "Annexe A : Matrice principes-objets d'interopérabilité"
id: cnisn-annexe-a
domain: 08_annexes
version: "1.0.0"
status: draft
last_reviewed: 2026-07-31
owner: DEPSI
tags: ["cnisn", "niveau-2", "annexes"]
---

# Annexe A : Matrice principes-objets d'interopérabilité

Tableau généré depuis le référentiel : les objets d'interopérabilité requis et les 25 principes du CNISN, avec leur rattachement. La dérive de libellés est éliminée : le titre provient de l'objet.

## Matrice

<!-- BEGIN:GENERATED mode=table source=04_architecture-repository/01_partitions/transverses/*.md,04_architecture-repository/01_partitions/externes/*.md,04_architecture-repository/01_partitions/sectorielles/*.md,04_architecture-repository/02_architecture-elements/data/reference-data/*.md,04_architecture-repository/02_architecture-elements/data/terminologies/*.md,04_architecture-repository/03_requirements/req-tf-*.md,04_architecture-repository/03_requirements/req-oh-*.md,04_architecture-repository/04_patterns/pat-*.md,04_architecture-repository/05_building-blocks/abb/abb-*.md,04_architecture-repository/06_governance/architecture-contracts/*.md,04_architecture-repository/06_governance/compliance/*.md,04_architecture-repository/06_governance/evidence/*.md,04_architecture-repository/02_architecture-elements/motivation/principles/p-int-*.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

| Code | Titre canonique | Rattachement | Statut | Fiche |
|---|---|---|---|---|
| ABB-AUDIT-PROVENANCE | Provenance, audit et traçabilité | CAP-03, CAP-08, CAP-12, CAP-13, CAP-15, ART-3, ART-7, ART-9, F-1, F-5, F-6, PART-TRANSVERSE-SECURITE-CONFIANCE, P-INT-07, P-INT-17, P-INT-18, P-INT-23 | candidate | ABB-AUDIT-PROVENANCE |
| ABB-CATALOGUE-CONTRATS | Catalogue des services et registre des contrats | CAP-12, CAP-14, CAP-16, ART-1, ART-2, F-3, F-4, AC-CATALOGUE-SERVICES, PART-TRANSVERSE-INTEROPERABILITE, P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-23, P-INT-24, P-INT-25 | candidate | ABB-CATALOGUE-CONTRATS |
| ABB-CONFIANCE-AUTORISATION | Confiance, sécurité et autorisation | CAP-15, ART-0, ART-4B, ART-7, ART-9, PART-TRANSVERSE-SECURITE-CONFIANCE, P-INT-14, P-INT-15, P-INT-16, P-INT-17, P-INT-18, P-INT-19, P-INT-20 | candidate | ABB-CONFIANCE-AUTORISATION |
| ABB-ECHANGE-LOGISTIQUE-LMIS | Échange logistique LMIS | CAP-06, CAP-10, CAP-11, ART-10, CMP-23, ENF-2, PART-TRANSVERSE-INTEROPERABILITE, P-INT-03, P-INT-07, P-INT-18 | candidate | ABB-ECHANGE-LOGISTIQUE-LMIS |
| ABB-ECHANGE-MEDIATION | Échange et médiation inter-systèmes | CAP-13, CAP-14, CAP-18, ART-1, ART-2, F-3, PAT-ECHANGE-MEDIATION, PART-TRANSVERSE-INTEROPERABILITE, P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-10, P-INT-11, P-INT-12, P-INT-13, P-INT-18, P-INT-19, P-INT-20, P-INT-21, P-INT-22, P-INT-23, P-INT-24, P-INT-25 | candidate | ABB-ECHANGE-MEDIATION |
| ABB-EXPOSITION-DONNEES-ANALYTIQUES | Accès et exposition des données analytiques | CAP-05, CAP-13, ART-3, ART-5, ART-6, ART-7, PART-TRANSVERSE-ANALYTICS-PILOTAGE, P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-17, P-INT-18, P-INT-19, P-INT-20, P-INT-21, P-INT-22, P-INT-23, P-INT-24, P-INT-25 | candidate | ABB-EXPOSITION-DONNEES-ANALYTIQUES |
| ABB-GESTION-CONSENTEMENT | Gestion des consentements et bases d'autorisation | CAP-15, CAP-17, ART-0, ART-4B, ART-7, ART-11, PART-TRANSVERSE-SECURITE-CONFIANCE, P-INT-14, P-INT-15, P-INT-16, P-INT-17 | candidate | ABB-GESTION-CONSENTEMENT |
| ABB-IDENTITE-BENEFICIAIRE | Résolution d'identité du bénéficiaire | CAP-01, CAP-02, CAP-04, CAP-07, CAP-14, CAP-17, ART-4, ART-4A, ART-7, PART-TRANSVERSE-IDENTITE, P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-14, P-INT-15, P-INT-16, P-INT-17, P-INT-18 | candidate | ABB-IDENTITE-BENEFICIAIRE |
| ABB-RECONCILIATION-DONNEES | Qualité et réconciliation des données | CAP-13, CAP-14, ART-4, ART-5, ART-6, PAT-QUALITE-RECONCILIATION, PART-TRANSVERSE-INTEROPERABILITE, P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-23, P-INT-24, P-INT-25 | candidate | ABB-RECONCILIATION-DONNEES |
| ABB-REFERENTIEL-STRUCTURES-SERVICES | Référentiel des structures et services de santé | CAP-11, CAP-13, CAP-14, ART-4, ART-5, ART-6, RD-STRUCTURES-SERVICES, PART-TRANSVERSE-DONNEES-REFERENTIELLES, DO-23, P-INT-01, P-INT-02, P-INT-03, P-INT-04 | candidate | ABB-REFERENTIEL-STRUCTURES-SERVICES |
| ABB-REGISTRE-PROFESSIONNELS | Registre et résolution des professionnels de santé | CAP-09, CAP-14, ART-4, ART-4A, ART-7, ART-4C, PART-TRANSVERSE-IDENTITE, P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-14, P-INT-15 | candidate | ABB-REGISTRE-PROFESSIONNELS |
| ABB-SERVICE-TERMINOLOGIE | Service de terminologie et codification communes | CAP-13, CAP-14, ART-2, ART-4, ART-5, TERM-CODIFICATION-COMMUNE, PART-TRANSVERSE-DONNEES-REFERENTIELLES, STD-0007, P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-05, P-INT-06 | candidate | ABB-SERVICE-TERMINOLOGIE |
| AC-CATALOGUE-SERVICES | Contrat d'architecture du catalogue de services | CAP-12, CAP-14, CAP-16, ART-1, ART-2, F-3, F-4, ABB-CATALOGUE-CONTRATS | candidate | AC-CATALOGUE-SERVICES |
| COMP-HOMOLOGATION-INTEROPERABILITE | Homologation d'interopérabilité | CAP-14, CAP-16, F-4, EVID-TESTS-INTEROPERABILITE, P-INT-23, P-INT-24, P-INT-25 | candidate | COMP-HOMOLOGATION-INTEROPERABILITE |
| EVID-TESTS-INTEROPERABILITE | Preuves de tests d'interopérabilité | CAP-16, F-4, COMP-HOMOLOGATION-INTEROPERABILITE | candidate | EVID-TESTS-INTEROPERABILITE |
| P-INT-01 | Autorité désignée | CAP-14, ABB-IDENTITE-BENEFICIAIRE, ABB-REGISTRE-PROFESSIONNELS, ABB-REFERENTIEL-STRUCTURES-SERVICES, ABB-SERVICE-TERMINOLOGIE, ABB-RECONCILIATION-DONNEES | active | P-INT-01 |
| P-INT-02 | Résolution contre l’autorité | CAP-14, ABB-IDENTITE-BENEFICIAIRE, ABB-REGISTRE-PROFESSIONNELS, ABB-REFERENTIEL-STRUCTURES-SERVICES, ABB-SERVICE-TERMINOLOGIE, ABB-RECONCILIATION-DONNEES | active | P-INT-02 |
| P-INT-03 | Copies locales non autoritatives | CAP-14, ABB-IDENTITE-BENEFICIAIRE, ABB-REGISTRE-PROFESSIONNELS, ABB-REFERENTIEL-STRUCTURES-SERVICES, ABB-SERVICE-TERMINOLOGIE, ABB-RECONCILIATION-DONNEES | active | P-INT-03 |
| P-INT-04 | Historisation des références | CAP-14, ABB-IDENTITE-BENEFICIAIRE, ABB-REGISTRE-PROFESSIONNELS, ABB-REFERENTIEL-STRUCTURES-SERVICES, ABB-SERVICE-TERMINOLOGIE, ABB-RECONCILIATION-DONNEES | active | P-INT-04 |
| P-INT-05 | Contrat explicite | CAP-14, ABB-ECHANGE-MEDIATION, ABB-SERVICE-TERMINOLOGIE, ABB-CATALOGUE-CONTRATS, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-RECONCILIATION-DONNEES | active | P-INT-05 |
| P-INT-06 | Versionnement et compatibilité | CAP-14, ABB-ECHANGE-MEDIATION, ABB-SERVICE-TERMINOLOGIE, ABB-CATALOGUE-CONTRATS, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-RECONCILIATION-DONNEES | active | P-INT-06 |
| P-INT-07 | Responsabilité de la donnée | CAP-13, ABB-ECHANGE-MEDIATION, ABB-CATALOGUE-CONTRATS, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-AUDIT-PROVENANCE, ABB-RECONCILIATION-DONNEES | active | P-INT-07 |
| P-INT-08 | Publication au catalogue des services | CAP-14, CAP-16, ABB-ECHANGE-MEDIATION, ABB-CATALOGUE-CONTRATS, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-RECONCILIATION-DONNEES | active | P-INT-08 |
| P-INT-09 | Publication des contrats | CAP-14, CAP-16, ABB-ECHANGE-MEDIATION, ABB-CATALOGUE-CONTRATS, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-RECONCILIATION-DONNEES | active | P-INT-09 |
| P-INT-10 | Accord préalable | CAP-14, ABB-ECHANGE-MEDIATION | active | P-INT-10 |
| P-INT-11 | Arbitrage des conflits d’autorité | CAP-14, ABB-ECHANGE-MEDIATION | active | P-INT-11 |
| P-INT-12 | Dérogation explicite | CAP-14, CAP-16, ABB-ECHANGE-MEDIATION | active | P-INT-12 |
| P-INT-13 | Dérogation d’urgence | CAP-14, CAP-16, ABB-ECHANGE-MEDIATION | active | P-INT-13 |
| P-INT-14 | Base d’autorisation explicite | CAP-15, ABB-IDENTITE-BENEFICIAIRE, ABB-REGISTRE-PROFESSIONNELS, ABB-CONFIANCE-AUTORISATION, ABB-GESTION-CONSENTEMENT | active | P-INT-14 |
| P-INT-15 | Limitation à la finalité | CAP-15, ABB-IDENTITE-BENEFICIAIRE, ABB-REGISTRE-PROFESSIONNELS, ABB-CONFIANCE-AUTORISATION, ABB-GESTION-CONSENTEMENT | active | P-INT-15 |
| P-INT-16 | Résidence et non-réplication | CAP-14, CAP-15, ABB-IDENTITE-BENEFICIAIRE, ABB-CONFIANCE-AUTORISATION, ABB-GESTION-CONSENTEMENT | active | P-INT-16 |
| P-INT-17 | Minimisation | CAP-15, ABB-IDENTITE-BENEFICIAIRE, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-CONFIANCE-AUTORISATION, ABB-GESTION-CONSENTEMENT, ABB-AUDIT-PROVENANCE | active | P-INT-17 |
| P-INT-18 | Traçabilité différenciée | CAP-13, CAP-15, ABB-IDENTITE-BENEFICIAIRE, ABB-ECHANGE-MEDIATION, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-CONFIANCE-AUTORISATION, ABB-AUDIT-PROVENANCE | active | P-INT-18 |
| P-INT-19 | Neutralité technologique | CAP-14, ABB-ECHANGE-MEDIATION, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-CONFIANCE-AUTORISATION, COMP-HOMOLOGATION-INTEROPERABILITE | active | P-INT-19 |
| P-INT-20 | Portabilité et réversibilité | CAP-14, ABB-ECHANGE-MEDIATION, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-CONFIANCE-AUTORISATION, COMP-HOMOLOGATION-INTEROPERABILITE | active | P-INT-20 |
| P-INT-21 | Progressivité | CAP-16, ABB-ECHANGE-MEDIATION, ABB-EXPOSITION-DONNEES-ANALYTIQUES, COMP-HOMOLOGATION-INTEROPERABILITE | active | P-INT-21 |
| P-INT-22 | Fonctionnement en connectivité contrainte | CAP-14, ABB-ECHANGE-MEDIATION, ABB-EXPOSITION-DONNEES-ANALYTIQUES, COMP-HOMOLOGATION-INTEROPERABILITE | active | P-INT-22 |
| P-INT-23 | Conformité fondée sur des preuves | CAP-16, ABB-ECHANGE-MEDIATION, ABB-CATALOGUE-CONTRATS, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-AUDIT-PROVENANCE, ABB-RECONCILIATION-DONNEES, COMP-HOMOLOGATION-INTEROPERABILITE | active | P-INT-23 |
| P-INT-24 | Applicabilité déclarée | CAP-16, ABB-ECHANGE-MEDIATION, ABB-CATALOGUE-CONTRATS, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-RECONCILIATION-DONNEES, COMP-HOMOLOGATION-INTEROPERABILITE | active | P-INT-24 |
| P-INT-25 | Réévaluation continue | CAP-16, ABB-ECHANGE-MEDIATION, ABB-CATALOGUE-CONTRATS, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-RECONCILIATION-DONNEES, COMP-HOMOLOGATION-INTEROPERABILITE | active | P-INT-25 |
| PART-ECHANGE-TRANSFRONTALIER | Partition échange transfrontalier | CAP-15, CAP-18, DO-29, DO-30, DO-31 | draft | PART-ECHANGE-TRANSFRONTALIER |
| PART-ONE-HEALTH | Partition One Health | CAP-18, VS-02, VS-04 | draft | PART-ONE-HEALTH |
| PART-TRANSVERSE-ANALYTICS-PILOTAGE | Partition transverse - Analytics et pilotage | PART-VS-01, PART-VS-02, PART-VS-03, PART-VS-04 | draft | PART-TRANSVERSE-ANALYTICS-PILOTAGE |
| PART-TRANSVERSE-DONNEES-REFERENTIELLES | Partition transverse - Données référentielles | PART-VS-01, PART-VS-02, PART-VS-03, PART-VS-04 | draft | PART-TRANSVERSE-DONNEES-REFERENTIELLES |
| PART-TRANSVERSE-IDENTITE | Partition transverse - Identité | PART-VS-01, PART-VS-02, PART-VS-03, PART-VS-04 | draft | PART-TRANSVERSE-IDENTITE |
| PART-TRANSVERSE-INTEROPERABILITE | Partition transverse - Interopérabilité | PART-VS-01, PART-VS-02, PART-VS-03, PART-VS-04 | draft | PART-TRANSVERSE-INTEROPERABILITE |
| PART-TRANSVERSE-SECURITE-CONFIANCE | Partition transverse - Sécurité et confiance | PART-VS-01, PART-VS-02, PART-VS-03, PART-VS-04 | draft | PART-TRANSVERSE-SECURITE-CONFIANCE |
| PAT-ECHANGE-INTERNATIONAL-IPS | Pattern d'échange international IPS | CAP-15, CAP-18, ART-0, ART-1, ART-7, PART-ECHANGE-TRANSFRONTALIER, DO-29, DO-30, DO-31 | candidate | PAT-ECHANGE-INTERNATIONAL-IPS |
| PAT-ECHANGE-MEDIATION | Pattern d'échange et médiation | CAP-13, CAP-14, CAP-18, ART-1, ART-2, F-3, ABB-ECHANGE-MEDIATION | candidate | PAT-ECHANGE-MEDIATION |
| PAT-QUALITE-RECONCILIATION | Pattern qualité et réconciliation | CAP-13, CAP-14, ART-4, ART-5, ART-6, ABB-RECONCILIATION-DONNEES | candidate | PAT-QUALITE-RECONCILIATION |
| RD-DONNEES-ENVIRONNEMENTALES-CLIMAT | Données environnementales et de résilience climatique | CAP-04, CAP-05, CAP-18, ART-4D, ART-11, PART-ONE-HEALTH, ENF-4 | candidate | RD-DONNEES-ENVIRONNEMENTALES-CLIMAT |
| RD-STRUCTURES-SERVICES | Données de référence des structures et services | CAP-11, CAP-13, CAP-14, ART-4, ART-5, ART-6, ABB-REFERENTIEL-STRUCTURES-SERVICES, DO-23 | candidate | RD-STRUCTURES-SERVICES |
| REQ-OH-01 | Tout échange intersectoriel doit être couvert par un accord explicite entre ministères. | CAP-18, ART-0, ART-11, PART-ONE-HEALTH, ENF-4 | candidate | REQ-OH-01 |
| REQ-OH-02 | Les identités humaines ne doivent jamais être croisées avec les identités animales. | CAP-18, ART-0, ART-11, PART-ONE-HEALTH, ENF-4 | candidate | REQ-OH-02 |
| REQ-OH-03 | Les données agrégées croisées doivent être irréversiblement anonymisées. | CAP-18, ART-0, ART-11, PART-ONE-HEALTH, ENF-4 | candidate | REQ-OH-03 |
| REQ-OH-04 | Chaque secteur conserve la souveraineté sur ses données source. | CAP-18, ART-0, ART-11, PART-ONE-HEALTH, ENF-4 | candidate | REQ-OH-04 |
| REQ-OH-05 | Les dimensions d'agrégation communes doivent être normalisées. | CAP-18, ART-0, ART-11, PART-ONE-HEALTH, ENF-4 | candidate | REQ-OH-05 |
| REQ-OH-06 | Tous les échanges intersectoriels doivent être journalisés et auditables. | CAP-18, ART-0, ART-11, PART-ONE-HEALTH, ENF-4 | candidate | REQ-OH-06 |
| REQ-OH-07 | Le cadre Tripartite Plus doit être respecté pour les flux internationaux. | CAP-18, ART-0, ART-11, PART-ONE-HEALTH, ENF-4 | candidate | REQ-OH-07 |
| REQ-TF-01 | Tout flux transfrontalier doit être couvert par un accord explicite. | CAP-15, CAP-18, ART-0, ART-7, PART-ECHANGE-TRANSFRONTALIER | candidate | REQ-TF-01 |
| REQ-TF-02 | Le consentement du patient doit être obtenu pour tout échange sortant sauf obligation légale. | CAP-15, CAP-18, ART-0, ART-7, PART-ECHANGE-TRANSFRONTALIER | candidate | REQ-TF-02 |
| REQ-TF-03 | Seules les données minimisées nécessaires à la finalité peuvent être exportées. | CAP-15, CAP-18, ART-0, ART-7, PART-ECHANGE-TRANSFRONTALIER | candidate | REQ-TF-03 |
| REQ-TF-04 | Tous les flux transfrontaliers doivent être journalisés et auditables. | CAP-15, CAP-18, ART-0, ART-7, PART-ECHANGE-TRANSFRONTALIER | candidate | REQ-TF-04 |
| REQ-TF-05 | Le GDHCN doit être le référentiel de confiance pour les échanges internationaux. | CAP-15, CAP-18, ART-0, ART-7, PART-ECHANGE-TRANSFRONTALIER | candidate | REQ-TF-05 |
| REQ-TF-06 | Les données souveraines ne quittent pas le territoire sauf dérogation. | CAP-15, CAP-18, ART-0, ART-7, PART-ECHANGE-TRANSFRONTALIER | candidate | REQ-TF-06 |
| REQ-TF-07 | Les systèmes partenaires étrangers doivent démontrer leur conformité avant tout accès. | CAP-15, CAP-18, ART-0, ART-7, PART-ECHANGE-TRANSFRONTALIER | candidate | REQ-TF-07 |
| REQ-TF-08 | Tout résumé patient échangé doit être conforme au profil HL7 FHIR IPS et contenir les sections minimales requises. | CAP-15, CAP-18, ART-0, ART-7, PART-ECHANGE-TRANSFRONTALIER | candidate | REQ-TF-08 |
| TERM-CODIFICATION-COMMUNE | Terminologie et codification communes | CAP-13, CAP-14, ART-2, ART-4, ART-5, ABB-SERVICE-TERMINOLOGIE, STD-0007 | candidate | TERM-CODIFICATION-COMMUNE |

<!-- END:GENERATED -->
---
