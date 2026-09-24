---
domain: togaf
id: VIEW-TOGAF-SOLUTIONS-LANDSCAPE
type: repository-view
niveau: "0"
title: "Vue TOGAF - Solutions Landscape"
status: draft
owner: DEPSI
version: "0.1"
tags: ["togaf", "solutions-landscape", "repository-view"]
---
# Vue TOGAF - Solutions Landscape

## Positionnement

Cette vue expose les blocs de solution et les contrats techniques qui matérialisent l'architecture cible dans les profils PTISN. Elle permet de distinguer les solutions réutilisables, les profils de mise en oeuvre et les schémas d'interface associés.

<!-- BEGIN:GENERATED mode=table source=04_architecture-repository/05_building-blocks/sbb/**/*.md,03_ptisn/schemas/**/*.json -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

| Code | Titre canonique | Rattachement | Statut | Fiche |
|---|---|---|---|---|
| PT-01 | Échange interinstitutionnel | CMP-06, ABB-ECHANGE-MEDIATION, COMP-HOMOLOGATION-INTEROPERABILITE, CAP-13, CAP-14, CAP-18, CAP-16, ART-0, ART-1, ART-7, ART-11 | active | PT-01 |
| PT-02 | Médiation intra-secteur | CMP-06, ABB-ECHANGE-MEDIATION, CAP-13, CAP-14, CAP-18, ART-1, ART-2, ART-5, ART-7, ART-8, ART-8C, ART-8D | active | PT-02 |
| PT-03 | Catalogue des services et registre des contrats | CMP-16, ABB-CATALOGUE-CONTRATS, CAP-12, CAP-14, CAP-16, F-3, F-4, ART-1, ART-2 | active | PT-03 |
| PT-04 | Résolution d’identité du bénéficiaire | CMP-11, ABB-IDENTITE-BENEFICIAIRE, CAP-01, CAP-02, CAP-04, CAP-07, CAP-14, CAP-17, ART-4, ART-4A, ART-4B, ART-7 | active | PT-04 |
| PT-05 | Registre des professionnels | CMP-13, ABB-REGISTRE-PROFESSIONNELS, CAP-09, CAP-14, ART-4, ART-4A, ART-7, ART-4C | active | PT-05 |
| PT-06 | Référentiel des structures et services de santé | CMP-08, ABB-REFERENTIEL-STRUCTURES-SERVICES, CAP-11, CAP-13, CAP-14, ART-4, ART-5, ART-6 | active | PT-06 |
| PT-07 | Terminologie et codification | CMP-10, ABB-SERVICE-TERMINOLOGIE, CAP-13, CAP-14, ART-2, ART-4, ART-5 | active | PT-07 |
| PT-08 | Échange de données agrégées | CMP-03, CMP-06, ABB-ECHANGE-MEDIATION, ABB-EXPOSITION-DONNEES-ANALYTIQUES, CAP-13, CAP-14, CAP-18, CAP-05, ART-1, ART-2, ART-5, ART-6 | active | PT-08 |
| PT-09 | Analytique et exposition de données | CMP-03, CMP-04, ABB-EXPOSITION-DONNEES-ANALYTIQUES, CAP-05, CAP-13, ART-3, ART-5, ART-6, ART-7 | active | PT-09 |
| PT-10 | Confiance, authentification et autorisation | CMP-15, ABB-CONFIANCE-AUTORISATION, CAP-15, ART-0, ART-4B, ART-7, ART-9 | active | PT-10 |
| PT-11 | Consentement et bases d’autorisation | CMP-12, ABB-GESTION-CONSENTEMENT, CAP-15, CAP-17, ART-0, ART-4B, ART-7, ART-11 | active | PT-11 |
| PT-12 | Audit, provenance et traçabilité | CMP-17, ABB-AUDIT-PROVENANCE, CAP-03, CAP-08, CAP-12, CAP-13, CAP-15, F-1, F-5, F-6, ART-3, ART-7 | active | PT-12 |
| PT-13 | Qualité et réconciliation | CMP-05, ABB-RECONCILIATION-DONNEES, CAP-13, CAP-14, ART-4, ART-5, ART-6 | active | PT-13 |
| PT-14 | Interopérabilité transfrontalière | PART-ECHANGE-TRANSFRONTALIER, CAP-15, CAP-17, CMP-06, CMP-15, CAP-18, ART-7, ART-0, ART-1 | active | PT-14 |
| PT-15 | Surveillance One Health | PART-ONE-HEALTH, RD-DONNEES-ENVIRONNEMENTALES-CLIMAT, CAP-18, CAP-05, CMP-02, CMP-04, CMP-06, CAP-04, ART-11, ART-0, ART-4D, ART-8B | active | PT-15 |
| PT-16 | Orchestration de processus bornés | CMP-07, CMP-06, ABB-ECHANGE-MEDIATION, CAP-13, CAP-14, CAP-18, ART-8A, ART-7, PT-02 | active | PT-16 |
| PT-17 | Logistique & chaîne d'approvisionnement (LMIS) | CMP-23, ABB-AUDIT-PROVENANCE, ABB-ECHANGE-LOGISTIQUE-LMIS, CAP-03, CAP-08, CAP-12, CAP-13, CAP-15, CAP-06, CAP-10, CAP-11, ART-10, PT-13 | active | PT-17 |
| PT-18 | Échange de réclamations et paiements | ABB-EXPOSITION-DONNEES-ANALYTIQUES, CAP-05, CAP-13, ART-2, ART-9 | active | PT-18 |
| PT-19 | Aide à la décision clinique (CDS) | CMP-08, ABB-SERVICE-TERMINOLOGIE, CAP-13, CAP-14, ART-12, ART-2 | active | PT-19 |

<!-- END:GENERATED -->

## Lecture

Le paysage des solutions doit rester aligné avec les blocs d'architecture et les exigences. Lorsqu'un profil ou un schéma évolue, son rattachement aux capacités, standards et objets de données doit rester vérifiable.

## Contrats techniques associés

Les schémas JSON et OpenAPI sous `03_ptisn/schemas/` restent des artefacts techniques générés et validés par les compilateurs dédiés. Ils ne sont pas reclassés comme objets du dépôt d'architecture ; leur traçabilité passe par les profils PTISN listés dans cette vue.
