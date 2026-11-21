---
domain: togaf
id: VIEW-TOGAF-REFERENCE-LIBRARY
type: repository-view
niveau: "0"
title: "Vue TOGAF - Reference Library"
status: draft
owner: DEPSI
version: "0.1"
tags: ["togaf", "reference-library", "repository-view"]
---
# Vue TOGAF - Reference Library

## Positionnement

Cette vue regroupe les patrons, fondations et blocs d'architecture réutilisables. Elle matérialise l'esprit HEART du dépôt : capitaliser les artefacts éprouvés, les rendre gouvernables et éviter la recréation de solutions locales incompatibles.

<!-- BEGIN:GENERATED mode=table source=04_architecture-repository/05_reference-library/patterns/*.md,04_architecture-repository/05_reference-library/patterns/**/*.md,04_architecture-repository/05_reference-library/building-blocks/abb/*.md,04_architecture-repository/05_reference-library/building-blocks/abb/**/*.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

| Code | Titre canonique | Rattachement | Statut | Fiche |
|---|---|---|---|---|
| ABB-AUDIT-PROVENANCE | Provenance, audit et traçabilité | CAP-03, CAP-08, CAP-12, CAP-13, CAP-15, ART-3, ART-7, ART-9, F-1, F-5, F-6, PART-TRANSVERSE-SECURITE-CONFIANCE, P-INT-07, P-INT-17, P-INT-18, P-INT-23 | candidate | ABB-AUDIT-PROVENANCE |
| ABB-CATALOGUE-CONTRATS | Catalogue des services et registre des contrats | CAP-12, CAP-14, CAP-16, ART-1, ART-2, F-3, F-4, AC-CATALOGUE-SERVICES, PART-TRANSVERSE-INTEROPERABILITE, P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-23, P-INT-24, P-INT-25 | candidate | ABB-CATALOGUE-CONTRATS |
| ABB-CONFIANCE-AUTORISATION | Confiance, sécurité et autorisation | CAP-15, ART-0, ART-4B, ART-7, ART-9, PART-TRANSVERSE-SECURITE-CONFIANCE, P-INT-14, P-INT-15, P-INT-16, P-INT-17, P-INT-18, P-INT-19, P-INT-20 | candidate | ABB-CONFIANCE-AUTORISATION |
| ABB-ECHANGE-LOGISTIQUE-LMIS | Échange logistique LMIS | CAP-06, CAP-10, CAP-11, ART-10, CMP-23, ENF-2, PART-TRANSVERSE-INTEROPERABILITE, P-INT-03, P-INT-07, P-INT-18 | candidate | ABB-ECHANGE-LOGISTIQUE-LMIS |
| ABB-ECHANGE-MEDIATION | Échange et médiation inter-systèmes | CAP-13, CAP-14, CAP-18, ART-1, ART-2, F-3, PAT-ECHANGE-MEDIATION, PART-TRANSVERSE-INTEROPERABILITE, PART-ONE-HEALTH, P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-10, P-INT-11, P-INT-12, P-INT-13, P-INT-18, P-INT-19, P-INT-20, P-INT-21, P-INT-22, P-INT-23, P-INT-24, P-INT-25 | candidate | ABB-ECHANGE-MEDIATION |
| ABB-ELIGIBILITE-COUVERTURE | Éligibilité et couverture sanitaire | CAP-07, ART-4C, ART-9, PART-VS-03, PRC-09, PRC-10, DO-14, DO-16, DO-17 | candidate | ABB-ELIGIBILITE-COUVERTURE |
| ABB-EXPOSITION-DONNEES-ANALYTIQUES | Accès et exposition des données analytiques | CAP-05, CAP-13, ART-3, ART-5, ART-6, ART-7, PART-TRANSVERSE-ANALYTICS-PILOTAGE, PART-ONE-HEALTH, P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-17, P-INT-18, P-INT-19, P-INT-20, P-INT-21, P-INT-22, P-INT-23, P-INT-24, P-INT-25 | candidate | ABB-EXPOSITION-DONNEES-ANALYTIQUES |
| ABB-GESTION-CONSENTEMENT | Gestion des consentements et bases d'autorisation | CAP-15, CAP-17, ART-0, ART-4B, ART-7, ART-11, PART-TRANSVERSE-SECURITE-CONFIANCE, P-INT-14, P-INT-15, P-INT-16, P-INT-17 | candidate | ABB-GESTION-CONSENTEMENT |
| ABB-IDENTITE-BENEFICIAIRE | Résolution d'identité du bénéficiaire | CAP-01, CAP-02, CAP-04, CAP-07, CAP-14, CAP-17, ART-4, ART-4A, ART-7, PART-TRANSVERSE-IDENTITE, P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-14, P-INT-15, P-INT-16, P-INT-17, P-INT-18 | candidate | ABB-IDENTITE-BENEFICIAIRE |
| ABB-RECONCILIATION-DONNEES | Qualité et réconciliation des données | CAP-13, CAP-14, ART-4, ART-5, ART-6, PAT-QUALITE-RECONCILIATION, PART-TRANSVERSE-INTEROPERABILITE, P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-23, P-INT-24, P-INT-25 | candidate | ABB-RECONCILIATION-DONNEES |
| ABB-REFERENTIEL-STRUCTURES-SERVICES | Référentiel des structures et services de santé | CAP-11, CAP-13, CAP-14, ART-4, ART-5, ART-6, RD-STRUCTURES-SERVICES, PART-TRANSVERSE-DONNEES-REFERENTIELLES, DO-23, DO-26, P-INT-01, P-INT-02, P-INT-03, P-INT-04 | candidate | ABB-REFERENTIEL-STRUCTURES-SERVICES |
| ABB-REGISTRE-PROFESSIONNELS | Registre et résolution des professionnels de santé | CAP-09, CAP-14, ART-4, ART-4A, ART-7, PART-TRANSVERSE-IDENTITE, P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-14, P-INT-15 | candidate | ABB-REGISTRE-PROFESSIONNELS |
| ABB-SERVICE-TERMINOLOGIE | Service de terminologie et codification communes | CAP-13, CAP-14, ART-2, ART-4, ART-5, TERM-CODIFICATION-COMMUNE, PART-TRANSVERSE-DONNEES-REFERENTIELLES, STD-0007, P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-05, P-INT-06 | candidate | ABB-SERVICE-TERMINOLOGIE |
| ART-0 | Accords de partage inter-institutionnels | ENF-4 | candidate | ART-0 |
| ART-1 | Intégration et ingestion | ENF-1, CAP-14 | stable | ART-1 |
| ART-2 | Médiation et normalisation | ENF-3, ENF-4, CAP-14 | stable | ART-2 |
| ART-3 | Historisation événementielle et profils de déploiement | ENF-1, CAP-13 | stable | ART-3 |
| ART-4 | Référentiels de métadonnées de gestion | ENF-4, CAP-14, ART-4A, ART-4B, ART-4C, ART-4D | stable | ART-4 |
| ART-4A | Résolution d'identité | ENF-3, CAP-04, ART-4 | draft | ART-4A |
| ART-4B | Bases d'autorisation | ENF-4, CAP-15, ART-4 | draft | ART-4B |
| ART-4C | Éligibilité et couverture | ENF-2, ENF-1, CAP-07, ART-4 | candidate | ART-4C |
| ART-4D | Référentiel géospatial et d'exploitation partagé | ENF-4, ART-4 | candidate | ART-4D |
| ART-5 | Cohérence et qualité des données | ENF-5, CAP-13 | stable | ART-5 |
| ART-6 | Analytique et restitution | ENF-4, CAP-13, CAP-08 | draft | ART-6 |
| ART-7 | Sécurité, contrôle d'accès et résidence de la donnée | ENF-1, CAP-15 | stable | ART-7 |
| ART-8 | Orchestration de processus | CAP-13, CAP-14, ART-8A, ART-8B, ART-8C, ART-8D | draft | ART-8 |
| ART-8A | Orchestration de processus borné | ENF-5, CAP-13, CAP-14, ART-8 | draft | ART-8A |
| ART-8B | Modélisation de relations en graphe | ENF-4, CAP-13, CAP-14, ART-8 | candidate | ART-8B |
| ART-8C | Agrégation par lot | ENF-1, ENF-2, CAP-13, CAP-14, ART-8 | candidate | ART-8C |
| ART-8D | Chorégraphie inter-institutionnelle | ENF-4, CAP-13, CAP-14, ART-8 | candidate | ART-8D |
| ART-9 | Garanties transactionnelles fortes | ENF-2, CAP-07 | candidate | ART-9 |
| ART-10 | Logistique | ENF-2, CAP-10, CAP-11 | candidate | ART-10 |
| ART-11 | Coordination intersectorielle | ENF-4, CAP-08, CAP-18, PART-ONE-HEALTH, ART-0, ART-4D, ART-8B, ART-8D | stable | ART-11 |
| ART-12 | Aide à la décision clinique | ART-6, CAP-13, CMP-08, ABB-SERVICE-TERMINOLOGIE, F-2 | draft | ART-12 |
| F-1 | Résilience face à la réalité géographique du pays | ENF-1, CAP-08 | stable | F-1 |
| F-2 | Préservation de la souveraineté intersectorielle | ENF-4 | stable | F-2 |
| F-3 | Éradication des silos technologiques | CAP-14 | stable | F-3 |
| F-4 | Homologation obligatoire | COMP-HOMOLOGATION-INTEROPERABILITE, CAP-16 | stable | F-4 |
| F-5 | Protection et minimisation | CAP-15, P-INT-16, P-INT-17 | draft | F-5 |
| F-6 | Observabilité | CAP-13, P-INT-18 | draft | F-6 |
| PAT-ECHANGE-INTERNATIONAL-IPS | Pattern d'échange international IPS | CAP-15, CAP-18, ART-0, ART-1, ART-7, PART-ECHANGE-TRANSFRONTALIER, DO-29, DO-31 | candidate | PAT-ECHANGE-INTERNATIONAL-IPS |
| PAT-ECHANGE-MEDIATION | Pattern d'échange et médiation | CAP-13, CAP-14, CAP-18, ART-1, ART-2, F-3, ABB-ECHANGE-MEDIATION | candidate | PAT-ECHANGE-MEDIATION |
| PAT-QUALITE-RECONCILIATION | Pattern qualité et réconciliation | CAP-13, CAP-14, ART-4, ART-5, ART-6, ABB-RECONCILIATION-DONNEES | candidate | PAT-QUALITE-RECONCILIATION |

<!-- END:GENERATED -->

## Lecture

La bibliothèque de référence constitue la base réutilisable des conceptions ARTSN et PTISN. Les équipes doivent privilégier ces patrons et blocs avant d'introduire un nouvel artefact, puis documenter l'écart si aucune réutilisation n'est possible.
