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

<!-- BEGIN:GENERATED mode=table source=04_architecture-repository/04_patterns/*.md,04_architecture-repository/04_patterns/**/*.md,04_architecture-repository/05_building-blocks/abb/*.md,04_architecture-repository/05_building-blocks/abb/**/*.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

| Code | Titre canonique | Rattachement | Statut | Fiche |
|---|---|---|---|---|
| ABB-AUDIT-PROVENANCE | Provenance, audit et traçabilité | CAP-03, CAP-08, CAP-12, CAP-13, CAP-15, ART-3, ART-7, ART-9, F-1, F-5, F-6 | candidate | ABB-AUDIT-PROVENANCE |
| ABB-CATALOGUE-CONTRATS | Catalogue des services et registre des contrats | CAP-12, CAP-14, CAP-16, ART-1, ART-2, F-3, F-4 | candidate | ABB-CATALOGUE-CONTRATS |
| ABB-CONFIANCE-AUTORISATION | Confiance, sécurité et autorisation | CAP-15, ART-0, ART-4B, ART-7, ART-9 | candidate | ABB-CONFIANCE-AUTORISATION |
| ABB-ECHANGE-LOGISTIQUE-LMIS | Échange logistique LMIS | CAP-06, CAP-10, CAP-11, ART-10 | candidate | ABB-ECHANGE-LOGISTIQUE-LMIS |
| ABB-ECHANGE-MEDIATION | Échange et médiation inter-systèmes | CAP-13, CAP-14, CAP-18, ART-1, ART-2, F-3 | candidate | ABB-ECHANGE-MEDIATION |
| ABB-EXPOSITION-DONNEES-ANALYTIQUES | Accès et exposition des données analytiques | CAP-05, CAP-13, ART-3, ART-5, ART-6, ART-7 | candidate | ABB-EXPOSITION-DONNEES-ANALYTIQUES |
| ABB-GESTION-CONSENTEMENT | Gestion des consentements et bases d'autorisation | CAP-15, CAP-17, ART-0, ART-4B, ART-7, ART-11 | candidate | ABB-GESTION-CONSENTEMENT |
| ABB-IDENTITE-BENEFICIAIRE | Résolution d'identité du bénéficiaire | CAP-01, CAP-02, CAP-04, CAP-07, CAP-14, CAP-17, ART-4, ART-4A, ART-7 | candidate | ABB-IDENTITE-BENEFICIAIRE |
| ABB-RECONCILIATION-DONNEES | Qualité et réconciliation des données | CAP-13, CAP-14, ART-4, ART-5, ART-6 | candidate | ABB-RECONCILIATION-DONNEES |
| ABB-REFERENTIEL-STRUCTURES-SERVICES | Référentiel des structures et services de santé | CAP-11, CAP-13, CAP-14, ART-4, ART-5, ART-6 | candidate | ABB-REFERENTIEL-STRUCTURES-SERVICES |
| ABB-REGISTRE-PROFESSIONNELS | Registre et résolution des professionnels de santé | CAP-09, CAP-14, ART-4, ART-4A, ART-7, ART-4C | candidate | ABB-REGISTRE-PROFESSIONNELS |
| ABB-SERVICE-TERMINOLOGIE | Service de terminologie et codification communes | CAP-13, CAP-14, ART-2, ART-4, ART-5 | candidate | ABB-SERVICE-TERMINOLOGIE |
| ART-0 | Accords de partage inter-institutionnels | ENF-4 | candidate | ART-0 |
| ART-1 | Intégration et ingestion | ENF-1, CAP-14 | stable | ART-1 |
| ART-2 | Médiation et normalisation | ENF-3, ENF-4, CAP-14 | stable | ART-2 |
| ART-3 | Historisation événementielle et profils de déploiement | ENF-1, CAP-13 | stable | ART-3 |
| ART-4 | Référentiels de métadonnées de gestion | ENF-4, CAP-14 | stable | ART-4 |
| ART-4A | Résolution d'identité | ENF-3, CAP-04 | draft | ART-4A |
| ART-4B | Bases d'autorisation | ENF-4, CAP-15 | draft | ART-4B |
| ART-4C | Éligibilité et couverture | ENF-2, ENF-1, CAP-07 | candidate | ART-4C |
| ART-4D | Référentiel géospatial et d'exploitation partagé | ENF-4 | candidate | ART-4D |
| ART-5 | Cohérence et qualité des données | ENF-5, CAP-13 | stable | ART-5 |
| ART-6 | Analytique et restitution | ENF-4, CAP-13, CAP-08 | draft | ART-6 |
| ART-7 | Sécurité, contrôle d'accès et résidence de la donnée | ENF-1, CAP-15 | stable | ART-7 |
| ART-8 | Orchestration de processus | CAP-13, CAP-14 | draft | ART-8 |
| ART-8A | Orchestration de processus borné | ENF-5, CAP-13, CAP-14 | draft | ART-8A |
| ART-8B | Modélisation de relations en graphe | ENF-4, CAP-13, CAP-14 | candidate | ART-8B |
| ART-8C | Agrégation par lot | ENF-1, ENF-2, CAP-13, CAP-14 | candidate | ART-8C |
| ART-8D | Chorégraphie inter-institutionnelle | ENF-4, CAP-13, CAP-14 | candidate | ART-8D |
| ART-9 | Garanties transactionnelles fortes | ENF-2, CAP-07 | candidate | ART-9 |
| ART-10 | Logistique | ENF-2, CAP-10, CAP-11 | candidate | ART-10 |
| ART-11 | Coordination intersectorielle | ENF-4, CAP-08, CAP-18, CAP-INT-14 | stable | ART-11 |
| ART-12 | Aide à la décision clinique | ART-6, CAP-13, CMP-08 | draft | ART-12 |
| CMP-01 | Tableaux de bord & Portails nationaux (performance, CSU, ressources, veille) | PRC-10, PRC-11, PRC-12, CAP-INT-07, CAP-INT-11, ART-6 | active | CMP-01 |
| CMP-02 | Centre de commande & Crises intersectorielles (alertes, crises, veille) | PRC-05, PRC-11, PRC-13, CAP-INT-07, ART-5, ART-0 | active | CMP-02 |
| CMP-03 | Entrepôt Lakehouse & Projections analytiques (pipeline ETL, Lakehouse, projections) | PRC-09, PRC-11, CAP-INT-07, CAP-INT-11, ART-6, ART-9 | active | CMP-03 |
| CMP-04 | Moteur analytique & IA (IA prédictive, routeur alertes, Grand Livre) | PRC-05, PRC-09, CAP-INT-07, CAP-INT-10, ART-5, ART-9 | active | CMP-04 |
| CMP-05 | Moteur de graphes & Référentiel spatio-temporel (Graph Store, Spatio ART-4D) | CAP-INT-03, CAP-INT-12, ART-8B, ART-4D | active | CMP-05 |
| CMP-06 | Intégration, Médiation, API Gateway, Broker & Registre schémas | PRC-13, CAP-INT-01, CAP-INT-03, ART-1, ART-2, F-3 | active | CMP-06 |
| CMP-07 | Orchestrateur de parcours & Gestionnaire de Sagas (ART-8A) | PRC-04, PRC-05, PRC-06, CAP-INT-08, ART-8A | active | CMP-07 |
| CMP-08 | Répertoire de données cliniques opérationnelles | PRC-04, PRC-05, CAP-INT-09, ART-4 | active | CMP-08 |
| CMP-09 | Référentiel des métadonnées d'exploitation (ART-4) | PRC-07, PRC-08, CAP-INT-09, ART-4 | active | CMP-09 |
| CMP-10 | Registre des terminologies | PRC-07, PRC-08, CAP-INT-09, ART-4 | active | CMP-10 |
| CMP-11 | Registre des clients / Index National des Patients (INP — ART-4A) | PRC-04, PRC-05, PRC-06, CAP-INT-09, ART-4A | active | CMP-11 |
| CMP-12 | Registre d'éligibilité et de couverture (CSU — ART-4C) | PRC-09, PRC-10, CAP-INT-09, ART-4C | active | CMP-12 |
| CMP-13 | Registre des personnels | PRC-04, PRC-05, CAP-INT-09, ART-4 | active | CMP-13 |
| CMP-14 | Registre des produits, intrants et indicateurs | PRC-05, PRC-06, CAP-INT-09, ART-4 | active | CMP-14 |
| CMP-15 | API Gateway | PRC-04, PRC-05, PRC-06, PRC-13, CAP-INT-10, ART-5 | active | CMP-15 |
| CMP-16 | Registre de schémas (F.3) | PRC-07, PRC-08, CAP-INT-10, ART-5 | active | CMP-16 |
| CMP-17 | Message broker asynchrone | PRC-04, PRC-05, PRC-06, CAP-INT-10, ART-5 | active | CMP-17 |
| CMP-18 | Compensateur / Regroupeur de flux (Netting — ART-8C) | PRC-04, PRC-05, PRC-06, CAP-INT-10, ART-8C | active | CMP-18 |
| CMP-19 | Dossiers & statistiques de sante (hopitaux) | PRC-01, PRC-02, PRC-03, PRC-06, CAP-INT-09, ENF-1, F-1 | active | CMP-19 |
| CMP-20 | Gestion des pharmacies (PMIS) | PRC-02, PRC-05, CAP-INT-09, ENF-1, F-1 | active | CMP-20 |
| CMP-21 | Sante communautaire mobile (offline) | PRC-01, PRC-02, PRC-03, CAP-INT-09, ENF-1, F-1 | active | CMP-21 |
| CMP-22 | Espace sante patient | PRC-01, PRC-07, PRC-08, CAP-INT-08, ENF-1, F-1 | active | CMP-22 |
| CMP-23 | Chaine logistique (LMIS) | PRC-05, PRC-10, CAP-INT-10, ENF-1, F-1 | active | CMP-23 |
| CMP-24 | Surveillance de la sante animale (zoonoses) | PRC-04, PRC-05, CAP-INT-14, ENF-1, F-1 | active | CMP-24 |
| CMP-25 | Enquetes & capteurs terrain | PRC-04, PRC-05, PRC-11, CAP-INT-09, ENF-1, F-1 | active | CMP-25 |
| CMP-26 | Noeud central (datacenters nationaux HDS) | ART-7 | active | CMP-26 |
| CMP-27 | Noeuds regionaux (clusters de district : Fog) | ART-7 | active | CMP-27 |
| CMP-28 | Noeuds locaux (equipements chiffres : Edge) | ART-7 | active | CMP-28 |
| CMP-29 | Liaisons dediees & VPN | ART-7 | active | CMP-29 |
| CMP-30 | Reseau prive MPLS | ART-7 | active | CMP-30 |
| CMP-31 | Reseaux mobiles prives (APN securises) | ART-7 | active | CMP-31 |
| CMP-32 | Gestion des identites | ART-7, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31 | active | CMP-32 |
| CMP-33 | Controle d'acces fin (RBAC/ABAC) | ART-7, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31 | active | CMP-33 |
| CMP-34 | Gestion des consentements | ART-7, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31 | active | CMP-34 |
| CMP-35 | Infrastructure de cles publiques (PKI) | ART-7, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31 | active | CMP-35 |
| CMP-36 | Passerelle de confiance mondiale OMS (GDHCN) | ART-7, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31 | active | CMP-36 |
| CMP-37 | Journal d'audit immuable | ART-7, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31 | active | CMP-37 |
| CMP-38 | Moteur de chiffrement | ART-7, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31 | active | CMP-38 |
| F-1 | Résilience face à la réalité géographique du pays | ENF-1, CAP-08 | stable | F-1 |
| F-2 | Préservation de la souveraineté intersectorielle | ENF-4 | stable | F-2 |
| F-3 | Éradication des silos technologiques | CAP-14 | stable | F-3 |
| F-4 | Homologation obligatoire | CAP-INT-12, CAP-16 | stable | F-4 |
| F-5 | Protection et minimisation | CAP-15 | draft | F-5 |
| F-6 | Observabilité | CAP-13 | draft | F-6 |
| PAT-ECHANGE-INTERNATIONAL-IPS | Pattern d'échange international IPS | CAP-15, CAP-18, ART-0, ART-1, ART-7 | candidate | PAT-ECHANGE-INTERNATIONAL-IPS |
| PAT-ECHANGE-MEDIATION | Pattern d'échange et médiation | CAP-13, CAP-14, CAP-18, ART-1, ART-2, F-3 | candidate | PAT-ECHANGE-MEDIATION |
| PAT-QUALITE-RECONCILIATION | Pattern qualité et réconciliation | CAP-13, CAP-14, ART-4, ART-5, ART-6 | candidate | PAT-QUALITE-RECONCILIATION |
| SRV-02 | Service de dossier patient | ART-2 | draft | SRV-02 |
| SRV-03 | Service de référentiels | ART-4 | draft | SRV-03 |
| SRV-04 | Service d'échange inter-systèmes | ART-9 | draft | SRV-04 |
| SRV-05 | Service logistique (LMIS) | ART-10 | draft | SRV-05 |
| SRV-06 | Service de pilotage et tableaux de bord | ART-3 | draft | SRV-06 |

<!-- END:GENERATED -->

## Lecture

La bibliothèque de référence constitue la base réutilisable des conceptions ARTSN et PTISN. Les équipes doivent privilégier ces patrons et blocs avant d'introduire un nouvel artefact, puis documenter l'écart si aucune réutilisation n'est possible.
