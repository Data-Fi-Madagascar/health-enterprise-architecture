---
domain: togaf
id: VIEW-TOGAF-ARCHITECTURE-LANDSCAPE
type: repository-view
niveau: "0"
title: "Vue TOGAF - Architecture Landscape"
status: draft
owner: DEPSI
version: "0.1"
tags: ["togaf", "architecture-landscape", "repository-view"]
---
# Vue TOGAF - Architecture Landscape

## Positionnement

Cette vue consolide les partitions d'architecture et les éléments stratégiques qui structurent le paysage cible HEA. Elle constitue le point d'entrée de lecture pour les revues de portée, d'alignement et de couverture des flux de valeur.

<!-- BEGIN:GENERATED mode=table source=04_architecture-repository/01_partitions/**/*.md,04_architecture-repository/02_architecture-elements/strategy/**/*.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

| Code | Titre canonique | Rattachement | Statut | Fiche |
|---|---|---|---|---|
| CAP-01 | Offre de soins et continuité des services | VS-01 | stable | CAP-01 |
| CAP-02 | Gestion du parcours patient, référence et contre-référence | VS-01, CAP-INT-03, CAP-INT-01, CAP-INT-13 | stable | CAP-02 |
| CAP-03 | Qualité, sécurité des soins et amélioration continue | VS-01, VS-04 | stable | CAP-03 |
| CAP-04 | Santé communautaire et engagement des communautés | VS-01, VS-02 | stable | CAP-04 |
| CAP-05 | Surveillance épidémiologique, alerte, investigation et riposte | VS-02 | stable | CAP-05 |
| CAP-06 | Vaccination, prévention et promotion de la santé | VS-02 | stable | CAP-06 |
| CAP-07 | Protection financière, couverture santé universelle | VS-03 | stable | CAP-07 |
| CAP-08 | Gouvernance institutionnelle, planification, coordination et redevabilité | VS-03, VS-04 | stable | CAP-08 |
| CAP-09 | Gestion des ressources humaines en santé | VS-01, VS-02, VS-04 | stable | CAP-09 |
| CAP-10 | Gestion des médicaments, vaccins, intrants et chaîne d'approvisionnement | VS-01, VS-02 | stable | CAP-10 |
| CAP-11 | Gestion des infrastructures, équipements et maintenance | VS-01, VS-02 | stable | CAP-11 |
| CAP-12 | Finances publiques, budget et allocation des ressources | VS-03, VS-04 | stable | CAP-12 |
| CAP-13 | Système d'information sanitaire, données et recherche | VS-01, VS-02, VS-03, VS-04 | stable | CAP-13 |
| CAP-14 | Interopérabilité, référentiels nationaux et infrastructure numérique partagée | VS-01, VS-02, VS-03, VS-04 | stable | CAP-14 |
| CAP-15 | Cybersécurité, confidentialité et gouvernance des données personnelles | VS-01, VS-02, VS-03, VS-04 | stable | CAP-15 |
| CAP-16 | Gestion du portefeuille d'initiatives numériques | VS-03, VS-04 | stable | CAP-16 |
| CAP-17 | Engagement patient et identité numérique | VS-01, VS-03, CAP-INT-01, CAP-INT-09 | stable | CAP-17 |
| CAP-18 | Coordination intersectorielle (One Health) | VS-02, CAP-INT-03, CAP-INT-14 | stable | CAP-18 |
| PART-ECHANGE-TRANSFRONTALIER | Partition échange transfrontalier | CAP-15, CAP-18, DO-29, DO-30, DO-31 | draft | PART-ECHANGE-TRANSFRONTALIER |
| PART-ONE-HEALTH | Partition One Health | CAP-18, VS-02, VS-04 | draft | PART-ONE-HEALTH |
| PART-TRANSVERSE-ANALYTICS-PILOTAGE | Partition transverse - Analytics et pilotage | PART-VS-01, PART-VS-02, PART-VS-03, PART-VS-04 | draft | PART-TRANSVERSE-ANALYTICS-PILOTAGE |
| PART-TRANSVERSE-DONNEES-REFERENTIELLES | Partition transverse - Données référentielles | PART-VS-01, PART-VS-02, PART-VS-03, PART-VS-04 | draft | PART-TRANSVERSE-DONNEES-REFERENTIELLES |
| PART-TRANSVERSE-IDENTITE | Partition transverse - Identité | PART-VS-01, PART-VS-02, PART-VS-03, PART-VS-04 | draft | PART-TRANSVERSE-IDENTITE |
| PART-TRANSVERSE-INTEROPERABILITE | Partition transverse - Interopérabilité | PART-VS-01, PART-VS-02, PART-VS-03, PART-VS-04 | draft | PART-TRANSVERSE-INTEROPERABILITE |
| PART-TRANSVERSE-SECURITE-CONFIANCE | Partition transverse - Sécurité et confiance | PART-VS-01, PART-VS-02, PART-VS-03, PART-VS-04 | draft | PART-TRANSVERSE-SECURITE-CONFIANCE |
| PART-VS-01 | Partition VS-01 | VS-01 | draft | PART-VS-01 |
| PART-VS-02 | Partition VS-02 | VS-02 | draft | PART-VS-02 |
| PART-VS-03 | Partition VS-03 | VS-03 | draft | PART-VS-03 |
| PART-VS-04 | Partition VS-04 | VS-04 | draft | PART-VS-04 |
| VS-01 | Accéder à des services de santé essentiels, intégrés, équitables et de qualité | CAP-01, CAP-02, CAP-03, CAP-04, CAP-09, CAP-10, CAP-11, CAP-13, CAP-14, CAP-15, CAP-17 | active | VS-01 |
| VS-01-01 | Reconnaissance du besoin et orientation | CAP-01, CAP-04 | draft | VS-01-01 |
| VS-01-02 | Accueil et enregistrement | CAP-01, CAP-14, CAP-15 | draft | VS-01-02 |
| VS-01-03 | Consultation et diagnostic | CAP-01, CAP-13 | draft | VS-01-03 |
| VS-01-04 | Traitement et prise en charge | CAP-01, CAP-10, CAP-11 | draft | VS-01-04 |
| VS-01-05 | Référence et contre-référence | CAP-02 | draft | VS-01-05 |
| VS-01-06 | Suivi et continuité des soins | CAP-01, CAP-02 | draft | VS-01-06 |
| VS-01-07 | Amélioration de la qualité | CAP-03, CAP-13 | draft | VS-01-07 |
| VS-02 | Prévenir, détecter et répondre aux risques sanitaires | CAP-04, CAP-05, CAP-06, CAP-09, CAP-10, CAP-11, CAP-13, CAP-14, CAP-15, CAP-17, CAP-18 | active | VS-02 |
| VS-02-01 | Identification des risques et promotion de la santé | CAP-06, CAP-04 | draft | VS-02-01 |
| VS-02-02 | Surveillance et détection | CAP-05, CAP-13 | draft | VS-02-02 |
| VS-02-03 | Notification et alerte | CAP-05, CAP-13 | draft | VS-02-03 |
| VS-02-04 | Vérification et investigation | CAP-05, CAP-13 | draft | VS-02-04 |
| VS-02-05 | Riposte | CAP-05, CAP-13, CAP-14 | draft | VS-02-05 |
| VS-02-06 | Suivi de situation et clôture | CAP-05, CAP-13 | draft | VS-02-06 |
| VS-02-07 | Capitalisation et amélioration | CAP-05, CAP-13 | draft | VS-02-07 |
| VS-03 | Protéger financièrement la population face aux dépenses de santé | CAP-07, CAP-08, CAP-12, CAP-13, CAP-14, CAP-15, CAP-16 | active | VS-03 |
| VS-03-01 | Identification et enregistrement des bénéficiaires | CAP-07, CAP-14, CAP-15 | draft | VS-03-01 |
| VS-03-02 | Définition des droits et du panier de soins | CAP-07 | draft | VS-03-02 |
| VS-03-03 | Mobilisation des financements | CAP-12, CAP-08 | draft | VS-03-03 |
| VS-03-04 | Prise en charge et exemption au point de service | CAP-07, CAP-15 | draft | VS-03-04 |
| VS-03-05 | Facturation et traitement des demandes de remboursement | CAP-07, CAP-13 | draft | VS-03-05 |
| VS-03-06 | Remboursement | CAP-07, CAP-12 | draft | VS-03-06 |
| VS-03-07 | Contrôle, audit et ajustement des mécanismes | CAP-08, CAP-13, CAP-16 | draft | VS-03-07 |
| VS-04 | Piloter, coordonner et améliorer la performance du système de santé | CAP-03, CAP-08, CAP-09, CAP-12, CAP-13, CAP-14, CAP-15, CAP-16 | active | VS-04 |
| VS-04-01 | Définition des priorités et planification | CAP-08, CAP-16 | draft | VS-04-01 |
| VS-04-02 | Budgétisation et allocation des ressources | CAP-12, CAP-08 | draft | VS-04-02 |
| VS-04-03 | Coordination des acteurs et alignement des partenaires | CAP-08, CAP-16 | draft | VS-04-03 |
| VS-04-04 | Suivi de l'exécution | CAP-13, CAP-08 | draft | VS-04-04 |
| VS-04-05 | Analyse de la performance et prise de décision | CAP-13, CAP-08 | draft | VS-04-05 |
| VS-04-06 | Redevabilité et communication publique | CAP-08, CAP-13 | draft | VS-04-06 |
| VS-04-07 | Amélioration continue | CAP-03, CAP-16, CAP-08 | draft | VS-04-07 |

<!-- END:GENERATED -->

## Lecture

Le paysage doit être lu comme une articulation entre partitions de gouvernance et éléments stratégiques. Une partition définit un périmètre de décision ; les flux, étapes et capabilités indiquent les objets qui portent effectivement la valeur ou la capacité métier.
