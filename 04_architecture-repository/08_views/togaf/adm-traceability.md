---
domain: togaf
id: VIEW-TOGAF-ADM-TRACEABILITY
type: repository-view
niveau: "0"
title: "Vue TOGAF - Traçabilité ADM"
status: draft
owner: DEPSI
version: "0.1"
tags: ["togaf", "adm-traceability", "repository-view"]
---
# Vue TOGAF - Traçabilité ADM

## Positionnement

Cette vue donne une lecture transversale du dépôt d'architecture selon les phases ADM. Elle aide à vérifier que les objets stratégiques, métier, données, applicatifs, technologiques, gouvernance et migration restent connectés dans une même chaîne de décision.

<!-- BEGIN:GENERATED mode=table source=04_architecture-repository/**/*.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

| Code | Titre canonique | Rattachement | Statut | Fiche |
|---|---|---|---|---|
| AA-01 | Les applications sont dérivées des flux de valeur et des capabilités | VS-01, VS-02, VS-03, VS-04 | draft | AA-01 |
| AA-02 | Les applications ne doivent pas dupliquer les référentiels nationaux | VS-01, VS-02, VS-03, VS-04 | draft | AA-02 |
| AA-03 | Les applications doivent être interopérables par conception | VS-01, VS-02, VS-03, VS-04 | draft | AA-03 |
| AA-04 | Les applications opérationnelles et analytiques doivent être séparées | VS-01, VS-02, VS-03, VS-04 | draft | AA-04 |
| AA-05 | Les applications doivent fonctionner dans les conditions réelles du terrain | VS-01, VS-02, VS-03, VS-04 | draft | AA-05 |
| AA-06 | Les plateformes partagées doivent être réutilisées avant de créer de nouveaux composants | VS-01, VS-02, VS-03, VS-04 | draft | AA-06 |
| AA-07 | Les applications doivent être soutenables | VS-01, VS-02, VS-03, VS-04 | draft | AA-07 |
| AA-08 | Les applications doivent être homologuées avant extension | VS-01, VS-02, VS-03, VS-04 | draft | AA-08 |
| AA-09 | Les applications obsolètes ou redondantes doivent être rationalisées | VS-01, VS-02, VS-03, VS-04 | draft | AA-09 |
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
| ACT-01 | Patient et usager (acteur) | PP-01, VS-01, CAP-17 | draft | ACT-01 |
| ACT-02 | Agent de santé de première ligne | PP-05, PRC-01, CAP-01 | draft | ACT-02 |
| ACT-03 | Formation sanitaire (établissement) | PP-06, CMP-01, CAP-01 | draft | ACT-03 |
| ACT-04 | Autorité district, région et Ministère | PP-07, CMP-39, VS-04 | draft | ACT-04 |
| ACT-05 | Partenaire technique et financier (acteur) | PP-08, VS-04, CAP-03 | draft | ACT-05 |
| ACT-06 | Équipe technique DEPSI / SIS | PP-10, CMP-32, ABB-IDENTITE-BENEFICIAIRE | draft | ACT-06 |
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
| BO-01 | BO-01 : Patient & identité | DO-01, DO-02, DO-03, DO-04, ART-2, ART-4, ART-7, PRC-01, PRC-06, PRC-07 | draft | BO-01 |
| BO-02 | BO-02 : Prestation & soins | DO-05, DO-06, DO-07, DO-08, DO-09, ART-2, ART-3, PRC-02, PRC-03 | draft | BO-02 |
| BO-03 | BO-03 : Dispensation & produits | DO-10, DO-11, DO-12, DO-13, ART-2, ART-4, ART-9, PRC-02, PRC-10 | draft | BO-03 |
| BO-04 | BO-04 : Financement & couverture | DO-14, DO-15, DO-16, DO-17, ART-2, ART-4, ART-9, PRC-08, PRC-09 | draft | BO-04 |
| BO-05 | BO-05 : Risque & surveillance | DO-18, DO-19, DO-20, DO-21, DO-22, ART-2, ART-3, PRC-04, PRC-05 | draft | BO-05 |
| BO-06 | BO-06 : Exploitation & gestion | DO-23, DO-24, DO-25, DO-26, DO-27, DO-28, ART-2, ART-4, PRC-10, PRC-11, PRC-12 | draft | BO-06 |
| BO-07 | BO-07 : Interopérabilité transfrontalière | DO-29, DO-30, DO-31, ART-2, ART-7, PRC-13 | draft | BO-07 |
| CAP-01 | Offre de soins et continuité des services | VS-01 | stable | CAP-01 |
| CAP-02 | Gestion du parcours patient, référence et contre-référence | VS-01, ABB-ECHANGE-MEDIATION, ABB-IDENTITE-BENEFICIAIRE, PART-ECHANGE-TRANSFRONTALIER, CAP-05, CAP-10, CAP-14, CAP-17 | stable | CAP-02 |
| CAP-03 | Qualité, sécurité des soins et amélioration continue | VS-01, VS-04 | stable | CAP-03 |
| CAP-04 | Santé communautaire et engagement des communautés | VS-01, VS-02 | stable | CAP-04 |
| CAP-05 | Surveillance épidémiologique, alerte, investigation et riposte | VS-02, CAP-18 | stable | CAP-05 |
| CAP-06 | Vaccination, prévention et promotion de la santé | VS-02 | stable | CAP-06 |
| CAP-07 | Protection financière, couverture santé universelle | VS-03 | stable | CAP-07 |
| CAP-08 | Gouvernance institutionnelle, planification, coordination et redevabilité | VS-03, VS-04 | stable | CAP-08 |
| CAP-09 | Gestion des ressources humaines en santé | VS-01, VS-02, VS-04, ABB-REGISTRE-PROFESSIONNELS, CAP-15, ART-6, PT-18 | stable | CAP-09 |
| CAP-10 | Gestion des médicaments, vaccins, intrants et chaîne d'approvisionnement | VS-01, VS-02 | stable | CAP-10 |
| CAP-11 | Gestion des infrastructures, équipements et maintenance | VS-01, VS-02 | stable | CAP-11 |
| CAP-12 | Finances publiques, budget et allocation des ressources | VS-03, VS-04 | stable | CAP-12 |
| CAP-13 | Système d'information sanitaire, données et recherche | VS-01, VS-02, VS-03, VS-04 | stable | CAP-13 |
| CAP-14 | Interopérabilité, référentiels nationaux et infrastructure numérique partagée | VS-01, VS-02, VS-03, VS-04 | stable | CAP-14 |
| CAP-15 | Cybersécurité, confidentialité et gouvernance des données personnelles | VS-01, VS-02, VS-03, VS-04 | stable | CAP-15 |
| CAP-16 | Gestion du portefeuille d'initiatives numériques | VS-03, VS-04 | stable | CAP-16 |
| CAP-17 | Engagement patient et identité numérique | VS-01, VS-03, ABB-IDENTITE-BENEFICIAIRE, ABB-GESTION-CONSENTEMENT, VS-02, PRC-01, PRC-04, PRC-07 | stable | CAP-17 |
| CAP-18 | Coordination intersectorielle (One Health) | VS-02, ABB-ECHANGE-MEDIATION, PART-ONE-HEALTH, PRC-04, PRC-05 | stable | CAP-18 |
| CMP-01 | Tableaux de bord & Portails nationaux (performance, CSU, ressources, veille) | PRC-10, PRC-11, PRC-12, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-RECONCILIATION-DONNEES, ART-6, ENF-5, CAP-13, CAP-16, VS-04 | active | CMP-01 |
| CMP-02 | Centre de commande & Crises intersectorielles (alertes, crises, veille) | PRC-05, PRC-11, PRC-13, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ART-5, ART-0, ENF-2, CAP-05, CAP-06, VS-02, VS-04 | active | CMP-02 |
| CMP-03 | Entrepôt Lakehouse & Projections analytiques (pipeline ETL, Lakehouse, projections) | PRC-09, PRC-11, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-RECONCILIATION-DONNEES, ART-6, ART-9, ENF-5, CAP-13, CAP-16, VS-04 | active | CMP-03 |
| CMP-04 | Moteur analytique & IA (IA prédictive, routeur alertes, Grand Livre) | PRC-05, PRC-09, ABB-EXPOSITION-DONNEES-ANALYTIQUES, ABB-AUDIT-PROVENANCE, ART-5, ART-9, ENF-2, ENF-5, CAP-13, CAP-15, VS-02, VS-04 | active | CMP-04 |
| CMP-05 | Moteur de graphes & Référentiel spatio-temporel (Graph Store, Spatio ART-4D) | ABB-ECHANGE-MEDIATION, COMP-HOMOLOGATION-INTEROPERABILITE, ART-8B, ART-4D, ENF-4, CAP-13, CAP-14, VS-04 | active | CMP-05 |
| CMP-06 | Intégration, Médiation, API Gateway, Broker & Registre schémas | PRC-13, ABB-IDENTITE-BENEFICIAIRE, ABB-ECHANGE-MEDIATION, ART-1, ART-2, F-3, ENF-1, ENF-3, CAP-13, CAP-14, CAP-15, VS-01, VS-02, VS-03, VS-04 | active | CMP-06 |
| CMP-07 | Orchestrateur de parcours & Gestionnaire de Sagas (ART-8A) | PRC-04, PRC-05, PRC-06, ABB-CONFIANCE-AUTORISATION, ART-8A, ENF-3, CAP-08, VS-02 | active | CMP-07 |
| CMP-08 | Répertoire de données cliniques opérationnelles | PRC-04, PRC-05, ABB-GESTION-CONSENTEMENT, ART-4, ENF-3, CAP-09, VS-02 | active | CMP-08 |
| CMP-09 | Référentiel des métadonnées d'exploitation (ART-4) | PRC-07, PRC-08, ABB-GESTION-CONSENTEMENT, ART-4, ENF-4, CAP-09, VS-03 | active | CMP-09 |
| CMP-10 | Registre des terminologies | PRC-07, PRC-08, ABB-SERVICE-TERMINOLOGIE, ART-4, ENF-4, CAP-09, VS-03 | active | CMP-10 |
| CMP-11 | Registre des clients / Index National des Patients (INP — ART-4A) | PRC-04, PRC-05, PRC-06, ABB-IDENTITE-BENEFICIAIRE, ART-4A, ENF-3, CAP-09, VS-02 | active | CMP-11 |
| CMP-12 | Registre d'éligibilité et de couverture (CSU — ART-4C) | PRC-09, PRC-10, CAP-07, ART-4C, VS-03 | active | CMP-12 |
| CMP-13 | Registre des personnels | PRC-04, PRC-05, ABB-GESTION-CONSENTEMENT, ART-4, ENF-3, CAP-09, VS-02 | active | CMP-13 |
| CMP-14 | Registre des produits, intrants et indicateurs | PRC-05, PRC-06, ABB-SERVICE-TERMINOLOGIE, ABB-ECHANGE-LOGISTIQUE-LMIS, ART-4, ENF-3, CAP-09, VS-02 | active | CMP-14 |
| CMP-15 | API Gateway | PRC-04, PRC-05, PRC-06, PRC-13, ABB-AUDIT-PROVENANCE, ART-5, ENF-3, CAP-10, VS-02 | active | CMP-15 |
| CMP-16 | Registre de schémas (F.3) | PRC-07, PRC-08, ABB-AUDIT-PROVENANCE, ART-5, ENF-4, CAP-10, VS-03 | active | CMP-16 |
| CMP-17 | Message broker asynchrone | PRC-04, PRC-05, PRC-06, ABB-AUDIT-PROVENANCE, ART-5, ENF-3, CAP-10, VS-02 | active | CMP-17 |
| CMP-18 | Compensateur / Regroupeur de flux (Netting — ART-8C) | PRC-04, PRC-05, PRC-06, ABB-AUDIT-PROVENANCE, ART-8C, ENF-3, CAP-10, VS-02 | active | CMP-18 |
| CMP-19 | Dossiers & statistiques de sante (hopitaux) | PRC-01, PRC-02, PRC-03, PRC-06, ABB-GESTION-CONSENTEMENT, ENF-1, F-1, VS-01, VS-04 | active | CMP-19 |
| CMP-20 | Gestion des pharmacies (PMIS) | PRC-02, PRC-05, ABB-GESTION-CONSENTEMENT, ENF-1, F-1, VS-01, VS-04 | active | CMP-20 |
| CMP-21 | Sante communautaire mobile (offline) | PRC-01, PRC-02, PRC-03, ABB-GESTION-CONSENTEMENT, ENF-1, F-1, VS-01, VS-02 | active | CMP-21 |
| CMP-22 | Espace sante patient | PRC-01, PRC-07, PRC-08, ABB-CONFIANCE-AUTORISATION, ENF-1, F-1, VS-01, VS-03 | active | CMP-22 |
| CMP-23 | Chaine logistique (LMIS) | PRC-05, PRC-10, ABB-ECHANGE-LOGISTIQUE-LMIS, ART-10, ENF-1, F-1, ABB-AUDIT-PROVENANCE, CAP-10, VS-01 | active | CMP-23 |
| CMP-24 | Surveillance de la sante animale (zoonoses) | PRC-04, PRC-05, PART-ONE-HEALTH, ENF-1, F-1, VS-02, VS-04 | active | CMP-24 |
| CMP-25 | Enquetes & capteurs terrain | PRC-04, PRC-05, PRC-11, ABB-GESTION-CONSENTEMENT, ENF-1, F-1, VS-02, VS-04 | active | CMP-25 |
| CMP-26 | Noeud central (datacenters nationaux HDS) | ART-7, VS-04 | active | CMP-26 |
| CMP-27 | Noeuds regionaux (clusters de district : Fog) | ART-7, VS-04 | active | CMP-27 |
| CMP-28 | Noeuds locaux (equipements chiffres : Edge) | ART-7, VS-04 | active | CMP-28 |
| CMP-29 | Liaisons dediees & VPN | ART-7, VS-04 | active | CMP-29 |
| CMP-30 | Reseau prive MPLS | ART-7, VS-04 | active | CMP-30 |
| CMP-31 | Reseaux mobiles prives (APN securises) | ART-7, VS-04 | active | CMP-31 |
| CMP-32 | Gestion des identites | ART-7, VS-04, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31 | active | CMP-32 |
| CMP-33 | Controle d'acces fin (RBAC/ABAC) | ART-7, VS-04, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31 | active | CMP-33 |
| CMP-34 | Gestion des consentements | ART-7, VS-04, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31 | active | CMP-34 |
| CMP-35 | Infrastructure de cles publiques (PKI) | ART-7, VS-04, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31 | active | CMP-35 |
| CMP-36 | Passerelle de confiance mondiale OMS (GDHCN) | ART-7, VS-02, VS-04, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31 | active | CMP-36 |
| CMP-37 | Journal d'audit immuable | ART-7, VS-04, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31 | active | CMP-37 |
| CMP-38 | Moteur de chiffrement | ART-7, VS-04, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31 | active | CMP-38 |
| CMP-39 | Registre des accords inter-institutions | ART-0, F-4, CMP-01, CMP-02, CMP-03, CMP-04, CMP-05, CMP-06, CMP-07, CMP-08, CMP-09, CMP-10, CMP-11, CMP-12, CMP-13, CMP-14, CMP-15, CMP-16, CMP-17, CMP-18, CMP-19, CMP-20, CMP-21, CMP-22, CMP-23, CMP-24, CMP-25, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31, CMP-32, CMP-33, CMP-34, CMP-35, CMP-36, CMP-37, CMP-38, CMP-39, CMP-40, CMP-41, CMP-42, CMP-43, CMP-44, CMP-45, CMP-46 | active | CMP-39 |
| CMP-40 | Charte nationale de protection | ART-0, F-4, CMP-01, CMP-02, CMP-03, CMP-04, CMP-05, CMP-06, CMP-07, CMP-08, CMP-09, CMP-10, CMP-11, CMP-12, CMP-13, CMP-14, CMP-15, CMP-16, CMP-17, CMP-18, CMP-19, CMP-20, CMP-21, CMP-22, CMP-23, CMP-24, CMP-25, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31, CMP-32, CMP-33, CMP-34, CMP-35, CMP-36, CMP-37, CMP-38, CMP-39, CMP-40, CMP-41, CMP-42, CMP-43, CMP-44, CMP-45, CMP-46 | active | CMP-40 |
| CMP-41 | Conventions internationales | ART-0, F-4, CMP-01, CMP-02, CMP-03, CMP-04, CMP-05, CMP-06, CMP-07, CMP-08, CMP-09, CMP-10, CMP-11, CMP-12, CMP-13, CMP-14, CMP-15, CMP-16, CMP-17, CMP-18, CMP-19, CMP-20, CMP-21, CMP-22, CMP-23, CMP-24, CMP-25, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31, CMP-32, CMP-33, CMP-34, CMP-35, CMP-36, CMP-37, CMP-38, CMP-39, CMP-40, CMP-41, CMP-42, CMP-43, CMP-44, CMP-45, CMP-46 | active | CMP-41 |
| CMP-42 | Comite national d'homologation | ART-0, F-4, CMP-01, CMP-02, CMP-03, CMP-04, CMP-05, CMP-06, CMP-07, CMP-08, CMP-09, CMP-10, CMP-11, CMP-12, CMP-13, CMP-14, CMP-15, CMP-16, CMP-17, CMP-18, CMP-19, CMP-20, CMP-21, CMP-22, CMP-23, CMP-24, CMP-25, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31, CMP-32, CMP-33, CMP-34, CMP-35, CMP-36, CMP-37, CMP-38, CMP-39, CMP-40, CMP-41, CMP-42, CMP-43, CMP-44, CMP-45, CMP-46 | active | CMP-42 |
| CMP-43 | Registre des initiatives | ART-0, F-4, CMP-01, CMP-02, CMP-03, CMP-04, CMP-05, CMP-06, CMP-07, CMP-08, CMP-09, CMP-10, CMP-11, CMP-12, CMP-13, CMP-14, CMP-15, CMP-16, CMP-17, CMP-18, CMP-19, CMP-20, CMP-21, CMP-22, CMP-23, CMP-24, CMP-25, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31, CMP-32, CMP-33, CMP-34, CMP-35, CMP-36, CMP-37, CMP-38, CMP-39, CMP-40, CMP-41, CMP-42, CMP-43, CMP-44, CMP-45, CMP-46 | active | CMP-43 |
| CMP-44 | Comite d'ethique | ART-0, F-4, CMP-01, CMP-02, CMP-03, CMP-04, CMP-05, CMP-06, CMP-07, CMP-08, CMP-09, CMP-10, CMP-11, CMP-12, CMP-13, CMP-14, CMP-15, CMP-16, CMP-17, CMP-18, CMP-19, CMP-20, CMP-21, CMP-22, CMP-23, CMP-24, CMP-25, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31, CMP-32, CMP-33, CMP-34, CMP-35, CMP-36, CMP-37, CMP-38, CMP-39, CMP-40, CMP-41, CMP-42, CMP-43, CMP-44, CMP-45, CMP-46 | active | CMP-44 |
| CMP-45 | Cellule d'audit | ART-0, F-4, CMP-01, CMP-02, CMP-03, CMP-04, CMP-05, CMP-06, CMP-07, CMP-08, CMP-09, CMP-10, CMP-11, CMP-12, CMP-13, CMP-14, CMP-15, CMP-16, CMP-17, CMP-18, CMP-19, CMP-20, CMP-21, CMP-22, CMP-23, CMP-24, CMP-25, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31, CMP-32, CMP-33, CMP-34, CMP-35, CMP-36, CMP-37, CMP-38, CMP-39, CMP-40, CMP-41, CMP-42, CMP-43, CMP-44, CMP-45, CMP-46 | active | CMP-45 |
| CMP-46 | Arbitrage et risques | ART-0, F-4, CMP-01, CMP-02, CMP-03, CMP-04, CMP-05, CMP-06, CMP-07, CMP-08, CMP-09, CMP-10, CMP-11, CMP-12, CMP-13, CMP-14, CMP-15, CMP-16, CMP-17, CMP-18, CMP-19, CMP-20, CMP-21, CMP-22, CMP-23, CMP-24, CMP-25, CMP-26, CMP-27, CMP-28, CMP-29, CMP-30, CMP-31, CMP-32, CMP-33, CMP-34, CMP-35, CMP-36, CMP-37, CMP-38, CMP-39, CMP-40, CMP-41, CMP-42, CMP-43, CMP-44, CMP-45, CMP-46 | active | CMP-46 |
| COMP-HOMOLOGATION-INTEROPERABILITE | Homologation d'interopérabilité | CAP-14, CAP-16, F-4, EVID-TESTS-INTEROPERABILITE, P-INT-23, P-INT-24, P-INT-25 | candidate | COMP-HOMOLOGATION-INTEROPERABILITE |
| DA-01 | Les données de santé sont un actif stratégique national | VS-01, VS-02, VS-03, VS-04 | draft | DA-01 |
| DA-02 | Une donnée doit être collectée une seule fois et réutilisée plusieurs fois | VS-01, VS-02, VS-03, VS-04 | draft | DA-02 |
| DA-03 | Les référentiels nationaux sont les sources de vérité | VS-01, VS-02, VS-03, VS-04 | draft | DA-03 |
| DA-04 | Les données opérationnelles et analytiques doivent être distinguées | VS-01, VS-02, VS-03, VS-04 | draft | DA-04 |
| DA-05 | La qualité des données est une responsabilité partagée | VS-01, VS-02, VS-03, VS-04 | draft | DA-05 |
| DA-06 | Les données doivent être utilisées pour des décisions réelles | VS-01, VS-02, VS-03, VS-04 | draft | DA-06 |
| DA-07 | Les données personnelles de santé doivent être protégées dès la conception | VS-01, VS-02, VS-03, VS-04 | draft | DA-07 |
| DA-08 | Les échanges de données doivent passer par des mécanismes gouvernés | VS-01, VS-02, VS-03, VS-04 | draft | DA-08 |
| DO-01 | DO-01 : Patient | ART-2, ART-4, ART-7, BO-01 | draft | DO-01 |
| DO-02 | DO-02 : Identifiant national d'identification | ART-2, ART-4, ART-7, BO-01 | draft | DO-02 |
| DO-03 | DO-03 : Dossier patient | ART-2, ART-4, ART-7, BO-01 | draft | DO-03 |
| DO-04 | DO-04 : Épisode de soins | ART-2, ART-4, ART-7, BO-01 | draft | DO-04 |
| DO-05 | DO-05 : Consultation | ART-2, ART-3, BO-02 | draft | DO-05 |
| DO-06 | DO-06 : Prescription | ART-2, ART-3, BO-02 | draft | DO-06 |
| DO-07 | DO-07 : Référence | ART-2, ART-3, BO-02 | draft | DO-07 |
| DO-08 | DO-08 : Contre-référence | ART-2, ART-3, BO-02 | draft | DO-08 |
| DO-09 | DO-09 : Évacuation sanitaire | ART-2, ART-3, BO-02 | draft | DO-09 |
| DO-10 | DO-10 : Dispensation | ART-2, ART-4, ART-9, BO-03 | draft | DO-10 |
| DO-11 | DO-11 : Produit de santé | ART-2, ART-4, ART-9, BO-03 | draft | DO-11 |
| DO-12 | DO-12 : Lot | ART-2, ART-4, ART-9, BO-03 | draft | DO-12 |
| DO-13 | DO-13 : Stock | ART-2, ART-4, ART-9, BO-03 | draft | DO-13 |
| DO-14 | DO-14 : Éligibilité | ART-2, ART-4, ART-9, BO-04 | draft | DO-14 |
| DO-15 | DO-15 : Couverture sanitaire | ART-2, ART-4, ART-9, BO-04 | draft | DO-15 |
| DO-16 | DO-16 : Facturation | ART-2, ART-4, ART-9, BO-04 | draft | DO-16 |
| DO-17 | DO-17 : Vérification d'éligibilité | ART-2, ART-4, ART-9, BO-04 | draft | DO-17 |
| DO-18 | DO-18 : Signal | ART-2, ART-3, BO-05 | draft | DO-18 |
| DO-19 | DO-19 : Foyer | ART-2, ART-3, BO-05 | draft | DO-19 |
| DO-20 | DO-20 : Investigation | ART-2, ART-3, BO-05 | draft | DO-20 |
| DO-21 | DO-21 : Notification sanitaire | ART-2, ART-3, BO-05 | draft | DO-21 |
| DO-22 | DO-22 : Alerte sanitaire | ART-2, ART-3, BO-05 | draft | DO-22 |
| DO-23 | DO-23 : Formation sanitaire | ART-2, ART-4, BO-06 | draft | DO-23 |
| DO-24 | DO-24 : Agent de santé | ART-2, ART-4, BO-06 | draft | DO-24 |
| DO-25 | DO-25 : Indicateur sanitaire | ART-2, ART-4, BO-06 | draft | DO-25 |
| DO-26 | DO-26 : Zone sanitaire | ART-2, ART-4, BO-06 | draft | DO-26 |
| DO-27 | DO-27 : Tâche | ART-2, ART-4, BO-06 | draft | DO-27 |
| DO-28 | DO-28 : Tableau de bord | ART-2, ART-4, BO-06 | draft | DO-28 |
| DO-29 | DO-29 : Résumé international du patient (IPS) | ART-2, ART-7, BO-07 | draft | DO-29 |
| DO-30 | DO-30 : Section du résumé patient | ART-2, ART-7, BO-07 | draft | DO-30 |
| DO-31 | DO-31 : Confiance internationale | ART-2, ART-7, BO-07 | draft | DO-31 |
| ENF-1 | Résilience à l'instabilité réseau | F-1, ART-1, ART-3, ART-7, ART-8C, ART-4C | draft | ENF-1 |
| ENF-2 | Intégrité des flux et traçabilité des valeurs | ART-9, ART-4C, ART-8C | draft | ENF-2 |
| ENF-3 | Unicité de l'identité et résilience face à la fragmentation applicative | ART-4A, ART-2 | draft | ENF-3 |
| ENF-4 | Cloisonnement inter-institutionnel et étanchéité des données (One Health) | ART-0, ART-4B, ART-4D, F-2, ART-2, ART-6, ART-8B, ART-8D, ART-4 | draft | ENF-4 |
| ENF-5 | Coordination des processus complexes décentralisés et asynchrones | ART-8A, ART-8, ART-5, PT-14 | draft | ENF-5 |
| EVID-TESTS-INTEROPERABILITE | Preuves de tests d'interopérabilité | CAP-16, F-4, COMP-HOMOLOGATION-INTEROPERABILITE | candidate | EVID-TESTS-INTEROPERABILITE |
| F-1 | Résilience face à la réalité géographique du pays | ENF-1, CAP-08 | stable | F-1 |
| F-2 | Préservation de la souveraineté intersectorielle | ENF-4 | stable | F-2 |
| F-3 | Éradication des silos technologiques | CAP-14 | stable | F-3 |
| F-4 | Homologation obligatoire | COMP-HOMOLOGATION-INTEROPERABILITE, CAP-16 | stable | F-4 |
| F-5 | Protection et minimisation | CAP-15, P-INT-16, P-INT-17 | draft | F-5 |
| F-6 | Observabilité | CAP-13, P-INT-18 | draft | F-6 |
| GAP-01 | Écart — Couverture terrain en zone isolée | PL-01, PL-02, LOC-04, CAP-01 | draft | GAP-01 |
| GAP-02 | Écart — Interopérabilité transfrontalière & One Health | PL-02, PL-03, ABB-CONFIANCE-AUTORISATION, PT-15 | draft | GAP-02 |
| GAP-03 | Écart — Cadre légal & gouvernance publié | PL-01, CMP-39, ABB-IDENTITE-BENEFICIAIRE | draft | GAP-03 |
| LOC-01 | Communauté / aire de santé | PP-04, CAP-01 | draft | LOC-01 |
| LOC-02 | Centre de santé de base (CSB) | PP-06, CMP-01 | draft | LOC-02 |
| LOC-03 | District sanitaire | PP-07, CMP-39 | draft | LOC-03 |
| LOC-04 | Région sanitaire | PP-07, VS-04 | draft | LOC-04 |
| LOC-05 | Établissement hospitalier de référence | PP-06, CAP-01 | draft | LOC-05 |
| LOC-06 | Siège central (DEPSI) | PP-10, CMP-32 | draft | LOC-06 |
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
| PA-01 | La valeur pour la population est la finalité de tout investissement numérique | VS-01, VS-02, VS-03, VS-04 | draft | PA-01 |
| PA-02 | Les flux de valeur précèdent les systèmes | VS-01, VS-02, VS-03, VS-04 | draft | PA-02 |
| PA-03 | Les bénéfices doivent être mesurés, pas seulement déclarés | VS-01, VS-02, VS-03, VS-04 | draft | PA-03 |
| PA-04 | Les données de santé sont un actif stratégique national | VS-01, VS-02, VS-03, VS-04 | draft | PA-04 |
| PA-05 | Une donnée doit être collectée une seule fois et réutilisée plusieurs fois | VS-01, VS-02, VS-03, VS-04 | draft | PA-05 |
| PA-06 | L'interopérabilité est une exigence non négociable | VS-01, VS-02, VS-03, VS-04 | draft | PA-06 |
| PA-07 | Les référentiels nationaux sont des biens communs indivisibles | VS-01, VS-02, VS-03, VS-04 | draft | PA-07 |
| PA-08 | Les systèmes doivent être soutenables sans dépendance externe permanente | VS-01, VS-02, VS-03, VS-04 | draft | PA-08 |
| PA-09 | L'architecture doit être adaptée aux réalités du terrain | VS-01, VS-02, VS-03, VS-04 | draft | PA-09 |
| PA-10 | La souveraineté nationale du système d'information sanitaire est non négociable | VS-01, VS-02, VS-03, VS-04 | draft | PA-10 |
| PA-11 | La protection des données personnelles est une condition de confiance | VS-01, VS-02, VS-03, VS-04 | draft | PA-11 |
| PA-12 | Toute initiative numérique doit être conforme au cadre national | VS-01, VS-02, VS-03, VS-04 | draft | PA-12 |
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
| PAT-ECHANGE-INTERNATIONAL-IPS | Pattern d'échange international IPS | CAP-15, CAP-18, ART-0, ART-1, ART-7, PART-ECHANGE-TRANSFRONTALIER, DO-29, DO-30, DO-31 | candidate | PAT-ECHANGE-INTERNATIONAL-IPS |
| PAT-ECHANGE-MEDIATION | Pattern d'échange et médiation | CAP-13, CAP-14, CAP-18, ART-1, ART-2, F-3, ABB-ECHANGE-MEDIATION | candidate | PAT-ECHANGE-MEDIATION |
| PAT-QUALITE-RECONCILIATION | Pattern qualité et réconciliation | CAP-13, CAP-14, ART-4, ART-5, ART-6, ABB-RECONCILIATION-DONNEES | candidate | PAT-QUALITE-RECONCILIATION |
| PD-VS01-01 | Le parcours du patient est l'unité de mesure de la performance | VS-01 | draft | PD-VS01-01 |
| PD-VS01-02 | Le dossier du patient suit le patient, pas l'institution | VS-01 | draft | PD-VS01-02 |
| PD-VS01-03 | La continuité des soins prime sur la logique des programmes | VS-01 | draft | PD-VS01-03 |
| PD-VS01-04 | Le patient et la communauté sont acteurs du parcours de santé | VS-01 | draft | PD-VS01-04 |
| PD-VS01-05 | L'accès numérique ne doit jamais devenir une barrière à l'accès aux soins | VS-01 | draft | PD-VS01-05 |
| PD-VS02-01 | La détection précoce prime sur la production tardive de rapports | VS-02 | draft | PD-VS02-01 |
| PD-VS02-02 | Toute alerte sanitaire doit être traçable de sa notification à sa clôture | VS-02 | draft | PD-VS02-02 |
| PD-VS02-03 | Les données communautaires et institutionnelles doivent converger | VS-02 | draft | PD-VS02-03 |
| PD-VS02-04 | La riposte doit être pilotée par des données exploitables en temps utile | VS-02 | draft | PD-VS02-04 |
| PD-VS02-05 | La surveillance sanitaire est une capabilité nationale permanente | VS-02 | draft | PD-VS02-05 |
| PD-VS03-01 | Les droits des bénéficiaires doivent être vérifiables au point de service | VS-03 | draft | PD-VS03-01 |
| PD-VS03-02 | La protection financière doit être liée au parcours réel de soins | VS-03 | draft | PD-VS03-02 |
| PD-VS03-03 | Les mécanismes d'exemption, de facturation et de remboursement doivent être traçables | VS-03 | draft | PD-VS03-03 |
| PD-VS03-04 | Aucun mécanisme numérique de financement ne doit créer une barrière supplémentaire à l'accès aux soins | VS-03 | draft | PD-VS03-04 |
| PD-VS03-05 | Le financement doit soutenir la qualité et la continuité des services | VS-03 | draft | PD-VS03-05 |
| PD-VS04-01 | La décision sanitaire doit s'appuyer sur des données fiables, traçables et réutilisables | VS-04 | draft | PD-VS04-01 |
| PD-VS04-02 | Le pilotage doit mesurer les résultats, pas seulement les activités | VS-04 | draft | PD-VS04-02 |
| PD-VS04-03 | Le portefeuille numérique doit être gouverné par la valeur produite | VS-04 | draft | PD-VS04-03 |
| PD-VS04-04 | Les partenaires contribuent au portefeuille national, ils ne le fragmentent pas | VS-04 | draft | PD-VS04-04 |
| PD-VS04-05 | L'amélioration continue doit être intégrée dans le système, pas ajoutée après coup | VS-04 | draft | PD-VS04-05 |
| PL-01 | Socle & confiance numérique | CAP-01, CAP-02, CAP-04, CAP-07, CAP-14, CAP-17, ABB-IDENTITE-BENEFICIAIRE, CMP-32, CMP-39, WP-01 | draft | PL-01 |
| PL-02 | Services de terrain & interopérabilité | CAP-13, CAP-14, CAP-18, CAP-01, ABB-ECHANGE-MEDIATION, SRV-02, SRV-03, CMP-10, WP-02, WP-03 | draft | PL-02 |
| PL-03 | Intelligence & ouverture | CAP-15, CAP-03, CAP-08, CAP-12, CAP-13, ABB-CONFIANCE-AUTORISATION, ABB-AUDIT-PROVENANCE, SRV-06, PT-14, WP-04, WP-05, WP-06, WP-07 | draft | PL-03 |
| PP-01 | Patient et usager | VS-01 | draft | PP-01 |
| PP-02 | Ménage et famille | VS-01, VS-03 | draft | PP-02 |
| PP-03 | Population | VS-02, VS-04 | draft | PP-03 |
| PP-04 | Communauté | VS-01, VS-02 | draft | PP-04 |
| PP-05 | Agent de santé | VS-01 | draft | PP-05 |
| PP-06 | Formation sanitaire | VS-01, VS-03 | draft | PP-06 |
| PP-07 | District, région et Ministère | VS-02, VS-04 | draft | PP-07 |
| PP-08 | Partenaires techniques et financiers | VS-02, VS-04 | draft | PP-08 |
| PP-09 | Décideurs institutionnels | VS-04 | draft | PP-09 |
| PP-10 | Équipes techniques (DEPSI / SIS) | VS-04 | draft | PP-10 |
| PRC-01 | Accès, orientation et admission du patient | CAP-01, CAP-02, CAP-04, CAP-11, CAP-13, CAP-14, CAP-15, VS-01-01, VS-01-02, VS-01, BO-01, DO-01, DO-03, DO-04, DO-05, CMP-19, CMP-21, CMP-22 | active | PRC-01 |
| PRC-02 | Prestation des soins cliniques | CAP-01, CAP-03, CAP-09, CAP-10, CAP-11, CAP-13, CAP-14, CAP-15, VS-01-03, VS-01-04, VS-01-05, VS-01, BO-02, BO-03, DO-05, DO-06, DO-07, DO-08, DO-10, CMP-19, CMP-20, CMP-21 | active | PRC-02 |
| PRC-03 | Continuité, suivi et qualité des soins | CAP-02, CAP-03, CAP-04, CAP-13, CAP-14, CAP-15, VS-01-06, VS-01-07, VS-01, BO-02, DO-03, DO-05, DO-10, CMP-19, CMP-21 | active | PRC-03 |
| PRC-04 | Veille, prévention et surveillance sanitaire | CAP-04, CAP-05, CAP-06, CAP-13, CAP-14, CAP-15, CAP-17, VS-02-01, VS-02-02, VS-02, BO-05, DO-18, DO-19, DO-21, DO-25, DO-26, CMP-07, CMP-08, CMP-11, CMP-13, CMP-15, CMP-17, CMP-18, CMP-24, CMP-25 | active | PRC-04 |
| PRC-05 | Alerte, investigation et riposte | CAP-04, CAP-05, CAP-13, CAP-14, CAP-15, CAP-17, CAP-18, VS-02-03, VS-02-04, VS-02-05, VS-02, BO-05, DO-18, DO-19, DO-20, DO-21, DO-22, CMP-02, CMP-04, CMP-07, CMP-08, CMP-11, CMP-13, CMP-14, CMP-15, CMP-17, CMP-18, CMP-20, CMP-23, CMP-24, CMP-25 | active | PRC-05 |
| PRC-06 | Clôture et capitalisation des épisodes | CAP-03, CAP-13, CAP-14, CAP-15, VS-02-06, VS-02-07, VS-02, BO-01, DO-01, DO-04, DO-25, CMP-07, CMP-11, CMP-14, CMP-15, CMP-17, CMP-18, CMP-19 | active | PRC-06 |
| PRC-07 | Identification et droits des bénéficiaires | CAP-07, CAP-08, CAP-13, CAP-14, CAP-15, CAP-17, VS-03-01, VS-03-02, VS-03, BO-01, DO-01, DO-02, DO-14, DO-15, CMP-09, CMP-10, CMP-16, CMP-22 | active | PRC-07 |
| PRC-08 | Financement et exemption au point de service | CAP-07, CAP-08, CAP-12, CAP-13, CAP-15, CAP-16, VS-03-03, VS-03-04, VS-03, BO-04, DO-14, DO-15, DO-16, CMP-09, CMP-10, CMP-16, CMP-22 | active | PRC-08 |
| PRC-09 | Remboursement et régulation des mécanismes | CAP-07, CAP-12, CAP-13, CAP-14, CAP-15, VS-03-05, VS-03-06, VS-03-07, VS-03, BO-04, DO-16, DO-17, CMP-03, CMP-04, CMP-12 | active | PRC-09 |
| PRC-10 | Planification et allocation des ressources | CAP-08, CAP-09, CAP-12, CAP-13, CAP-15, CAP-16, VS-04-01, VS-04-02, VS-04-03, VS-04, BO-03, BO-06, DO-25, DO-26, DO-27, CMP-01, CMP-12, CMP-23 | active | PRC-10 |
| PRC-11 | Suivi et pilotage de la performance | CAP-03, CAP-08, CAP-13, CAP-14, CAP-15, CAP-16, VS-04-04, VS-04-05, VS-04, BO-06, DO-25, DO-28, CMP-01, CMP-02, CMP-03, CMP-25 | active | PRC-11 |
| PRC-12 | Redevabilité et amélioration continue | CAP-03, CAP-08, CAP-13, CAP-14, CAP-15, CAP-16, VS-04-06, VS-04-07, VS-04, BO-06, DO-25, DO-28, CMP-01 | active | PRC-12 |
| PRC-13 | Échange et coordination transfrontaliers | PART-ECHANGE-TRANSFRONTALIER, CAP-15, CAP-17, VS-02, BO-07, DO-29, DO-30, DO-31, CMP-02, CMP-06, CMP-15 | active | PRC-13 |
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
| ROL-01 | Clinicien / prestataire de soins | PRC-01, ACT-02, CAP-01 | draft | ROL-01 |
| ROL-02 | Gestionnaire de parcours / référence | PRC-02, ACT-02, CAP-02 | draft | ROL-02 |
| ROL-03 | Gestionnaire de données / registre | PRC-09, ACT-06, ABB-REFERENTIEL-STRUCTURES-SERVICES | draft | ROL-03 |
| ROL-04 | Gestionnaire logistique | PRC-08, ACT-03, ABB-AUDIT-PROVENANCE | draft | ROL-04 |
| ROL-05 | Contrôleur / auditeur | PRC-13, ACT-04, CMP-39 | draft | ROL-05 |
| SRV-01 | Service d'identité du bénéficiaire | CAP-17, ART-2, PP-01, BO-01, CMP-08 | draft | SRV-01 |
| SRV-02 | Service de dossier patient | CAP-01, ART-2, PP-05, BO-01, DO-01, CMP-09 | draft | SRV-02 |
| SRV-03 | Service de référentiels | ABB-SERVICE-TERMINOLOGIE, ART-4, PP-06, TERM-CODIFICATION-COMMUNE, DO-11, DO-23, DO-25, CMP-10 | draft | SRV-03 |
| SRV-04 | Service d'échange inter-systèmes | ABB-ECHANGE-MEDIATION, ART-1, ART-2, ART-7, PP-10, DO-03, CMP-06 | draft | SRV-04 |
| SRV-05 | Service logistique (LMIS) | ABB-ECHANGE-LOGISTIQUE-LMIS, ART-10, PP-06, ABB-AUDIT-PROVENANCE, DO-11, DO-12, DO-13, CMP-23 | draft | SRV-05 |
| SRV-06 | Service de pilotage et tableaux de bord | ABB-EXPOSITION-DONNEES-ANALYTIQUES, ART-3, ART-6, PP-07, CAP-03, DO-25, DO-28, CMP-03, CMP-04 | draft | SRV-06 |
| TERM-CODIFICATION-COMMUNE | Terminologie et codification communes | CAP-13, CAP-14, ART-2, ART-4, ART-5, ABB-SERVICE-TERMINOLOGIE, STD-0007 | candidate | TERM-CODIFICATION-COMMUNE |
| VAL-01 | Soins accessibles, continus, sûrs et de qualité | — | active | VAL-01 |
| VAL-02 | Protection contre les maladies, épidémies et urgences sanitaires | — | active | VAL-02 |
| VAL-03 | Protection financière contre les dépenses de santé | — | active | VAL-03 |
| VAL-04 | Système de santé planifié, coordonné et continuellement amélioré | — | active | VAL-04 |
| VS-01 | Accéder à des services de santé essentiels, intégrés, équitables et de qualité | CAP-01, CAP-02, CAP-03, CAP-04, CAP-09, CAP-10, CAP-11, CAP-13, CAP-14, CAP-15, CAP-17, PRC-01, PRC-02, PRC-03 | active | VS-01 |
| VS-01-01 | Reconnaissance du besoin et orientation | CAP-01, CAP-04, VS-01 | draft | VS-01-01 |
| VS-01-02 | Accueil et enregistrement | CAP-01, CAP-14, CAP-15, VS-01 | draft | VS-01-02 |
| VS-01-03 | Consultation et diagnostic | CAP-01, CAP-13, VS-01 | draft | VS-01-03 |
| VS-01-04 | Traitement et prise en charge | CAP-01, CAP-10, CAP-11, VS-01 | draft | VS-01-04 |
| VS-01-05 | Référence et contre-référence | CAP-02, VS-01 | draft | VS-01-05 |
| VS-01-06 | Suivi et continuité des soins | CAP-01, CAP-02, VS-01 | draft | VS-01-06 |
| VS-01-07 | Amélioration de la qualité | CAP-03, CAP-13, VS-01 | draft | VS-01-07 |
| VS-02 | Prévenir, détecter et répondre aux risques sanitaires | CAP-04, CAP-05, CAP-06, CAP-09, CAP-10, CAP-11, CAP-13, CAP-14, CAP-15, CAP-17, CAP-18, PRC-04, PRC-05, PRC-06 | active | VS-02 |
| VS-02-01 | Identification des risques et promotion de la santé | CAP-06, CAP-04, VS-02 | draft | VS-02-01 |
| VS-02-02 | Surveillance et détection | CAP-05, CAP-13, VS-02 | draft | VS-02-02 |
| VS-02-03 | Notification et alerte | CAP-05, CAP-13, VS-02 | draft | VS-02-03 |
| VS-02-04 | Vérification et investigation | CAP-05, CAP-13, VS-02 | draft | VS-02-04 |
| VS-02-05 | Riposte | CAP-05, CAP-13, CAP-14, VS-02 | draft | VS-02-05 |
| VS-02-06 | Suivi de situation et clôture | CAP-05, CAP-13, VS-02 | draft | VS-02-06 |
| VS-02-07 | Capitalisation et amélioration | CAP-05, CAP-13, VS-02 | draft | VS-02-07 |
| VS-03 | Protéger financièrement la population face aux dépenses de santé | CAP-07, CAP-08, CAP-12, CAP-13, CAP-14, CAP-15, CAP-16, PRC-07, PRC-08, PRC-09 | active | VS-03 |
| VS-03-01 | Identification et enregistrement des bénéficiaires | CAP-07, CAP-14, CAP-15, VS-03 | draft | VS-03-01 |
| VS-03-02 | Définition des droits et du panier de soins | CAP-07, VS-03 | draft | VS-03-02 |
| VS-03-03 | Mobilisation des financements | CAP-12, CAP-08, VS-03 | draft | VS-03-03 |
| VS-03-04 | Prise en charge et exemption au point de service | CAP-07, CAP-15, VS-03 | draft | VS-03-04 |
| VS-03-05 | Facturation et traitement des demandes de remboursement | CAP-07, CAP-13, VS-03 | draft | VS-03-05 |
| VS-03-06 | Remboursement | CAP-07, CAP-12, VS-03 | draft | VS-03-06 |
| VS-03-07 | Contrôle, audit et ajustement des mécanismes | CAP-08, CAP-13, CAP-16, VS-03 | draft | VS-03-07 |
| VS-04 | Piloter, coordonner et améliorer la performance du système de santé | CAP-03, CAP-08, CAP-09, CAP-12, CAP-13, CAP-14, CAP-15, CAP-16, PRC-10, PRC-11, PRC-12 | active | VS-04 |
| VS-04-01 | Définition des priorités et planification | CAP-08, CAP-16, VS-04 | draft | VS-04-01 |
| VS-04-02 | Budgétisation et allocation des ressources | CAP-12, CAP-08, VS-04 | draft | VS-04-02 |
| VS-04-03 | Coordination des acteurs et alignement des partenaires | CAP-08, CAP-16, VS-04 | draft | VS-04-03 |
| VS-04-04 | Suivi de l'exécution | CAP-13, CAP-08, VS-04 | draft | VS-04-04 |
| VS-04-05 | Analyse de la performance et prise de décision | CAP-13, CAP-08, VS-04 | draft | VS-04-05 |
| VS-04-06 | Redevabilité et communication publique | CAP-08, CAP-13, VS-04 | draft | VS-04-06 |
| VS-04-07 | Amélioration continue | CAP-03, CAP-16, CAP-08, VS-04 | draft | VS-04-07 |
| WP-01 | Infrastructure & sécurité | CAP-01, CAP-02, CAP-04, CAP-07, CAP-14, CAP-17, CMP-26, CMP-32, CMP-39, ABB-IDENTITE-BENEFICIAIRE, SRV-04, PL-01 | draft | WP-01 |
| WP-02 | Applications terrain & collecte | CMP-09, CMP-23, SRV-02, SRV-05, CAP-01, PL-02 | draft | WP-02 |
| WP-03 | Médiation & registres partagés | CAP-13, CAP-14, CAP-18, CMP-10, CMP-11, CMP-12, SRV-03, SRV-04, ABB-ECHANGE-MEDIATION, ABB-SERVICE-TERMINOLOGIE, ABB-IDENTITE-BENEFICIAIRE, PL-02 | draft | WP-03 |
| WP-04 | Analytique & pilotage | CMP-02, CMP-03, CMP-04, SRV-06, ABB-EXPOSITION-DONNEES-ANALYTIQUES, CAP-03, ART-6, PL-03 | draft | WP-04 |
| WP-05 | Extension & pérennisation | CAP-15, SRV-06, CAP-03, ABB-CONFIANCE-AUTORISATION, PT-14, PT-15, PL-03 | draft | WP-05 |
| WP-06 | Interopérabilité transfrontalière | CAP-15, SRV-04, ABB-CONFIANCE-AUTORISATION, ART-9, PT-14, PL-03 | draft | WP-06 |
| WP-07 | Coordination One Health | CMP-02, ART-8B, CAP-03, PT-15, PL-03 | draft | WP-07 |

<!-- END:GENERATED -->

## Lecture

La traçabilité ADM doit être utilisée comme contrôle de cohérence global. Elle ne remplace pas les vues spécialisées, mais permet d'identifier rapidement les objets sans rattachement ou les périmètres dont la phase ADM doit être précisée.
