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
| ACT-01 | Patient et usager (acteur) | — | draft | ACT-01 |
| ACT-02 | Agent de santé de première ligne | — | draft | ACT-02 |
| ACT-03 | Formation sanitaire (établissement) | — | draft | ACT-03 |
| ACT-04 | Autorité district, région et Ministère | — | draft | ACT-04 |
| ACT-05 | Partenaire technique et financier (acteur) | — | draft | ACT-05 |
| ACT-06 | Équipe technique DEPSI / SIS | — | draft | ACT-06 |
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
| BO-01 | BO-01 : Patient & identité | — | draft | BO-01 |
| BO-02 | BO-02 : Prestation & soins | — | draft | BO-02 |
| BO-03 | BO-03 : Dispensation & produits | — | draft | BO-03 |
| BO-04 | BO-04 : Financement & couverture | — | draft | BO-04 |
| BO-05 | BO-05 : Risque & surveillance | — | draft | BO-05 |
| BO-06 | BO-06 : Exploitation & gestion | — | draft | BO-06 |
| BO-07 | BO-07 : Interopérabilité transfrontalière | — | draft | BO-07 |
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
| CAP-INT-01 | Résolution d’identité du bénéficiaire | P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-14, P-INT-15, P-INT-16, P-INT-17, P-INT-18, CAP-01, CAP-02, CAP-04, CAP-07, CAP-14, CAP-17 | candidate | CAP-INT-01 |
| CAP-INT-02 | Registre et résolution des professionnels de santé | P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-14, P-INT-15, CAP-09, CAP-14 | candidate | CAP-INT-02 |
| CAP-INT-03 | Échange et médiation inter-systèmes | P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-10, P-INT-11, P-INT-12, P-INT-13, P-INT-18, P-INT-19, P-INT-20, P-INT-21, P-INT-22, P-INT-23, P-INT-24, P-INT-25, CAP-13, CAP-14, CAP-18 | candidate | CAP-INT-03 |
| CAP-INT-04 | Référentiel des structures et services de santé | P-INT-01, P-INT-02, P-INT-03, P-INT-04, CAP-11, CAP-13, CAP-14 | candidate | CAP-INT-04 |
| CAP-INT-05 | Terminologie et codification communes | P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-05, P-INT-06, CAP-13, CAP-14 | candidate | CAP-INT-05 |
| CAP-INT-06 | Catalogue des services et registre des contrats | P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-23, P-INT-24, P-INT-25, CAP-12, CAP-14, CAP-16 | candidate | CAP-INT-06 |
| CAP-INT-07 | Accès et exposition des données analytiques | P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-17, P-INT-18, P-INT-19, P-INT-20, P-INT-21, P-INT-22, P-INT-23, P-INT-24, P-INT-25, CAP-05, CAP-13 | candidate | CAP-INT-07 |
| CAP-INT-08 | Confiance, sécurité et autorisation | P-INT-14, P-INT-15, P-INT-16, P-INT-17, P-INT-18, P-INT-19, P-INT-20, CAP-15 | candidate | CAP-INT-08 |
| CAP-INT-09 | Gestion des consentements et bases d’autorisation | P-INT-14, P-INT-15, P-INT-16, P-INT-17, CAP-15, CAP-17 | candidate | CAP-INT-09 |
| CAP-INT-10 | Provenance, audit et traçabilité | P-INT-07, P-INT-17, P-INT-18, P-INT-23, CAP-03, CAP-08, CAP-12, CAP-13, CAP-15 | candidate | CAP-INT-10 |
| CAP-INT-11 | Qualité et réconciliation | P-INT-01, P-INT-02, P-INT-03, P-INT-04, P-INT-05, P-INT-06, P-INT-07, P-INT-08, P-INT-09, P-INT-23, P-INT-24, P-INT-25, CAP-13, CAP-14 | candidate | CAP-INT-11 |
| CAP-INT-12 | Conformité et tests d’interopérabilité | P-INT-19, P-INT-20, P-INT-21, P-INT-22, P-INT-23, P-INT-24, P-INT-25, CAP-14, CAP-16 | candidate | CAP-INT-12 |
| CAP-INT-13 | Interopérabilité transfrontalière et confiance internationale | P-INT-01, P-INT-05, P-INT-10, P-INT-14, P-INT-16, P-INT-17, P-INT-19, CAP-15 | candidate | CAP-INT-13 |
| CAP-INT-14 | Échanges intersectoriels One Health | P-INT-01, P-INT-05, P-INT-10, P-INT-14, P-INT-16, P-INT-22, CAP-18 | candidate | CAP-INT-14 |
| CAP-INT-15 | Échange et traçabilité de la chaîne d'approvisionnement sanitaire | CAP-06, CAP-10, CAP-11, CMP-23 | candidate | CAP-INT-15 |
| CAP-INT-16 | Données environnementales et de résilience climatique | CAP-04, CAP-05, CAP-18, CMP-05, ART-4D | candidate | CAP-INT-16 |
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
| CMP-39 | Registre des accords inter-institutions | ART-0, F-4 | active | CMP-39 |
| CMP-40 | Charte nationale de protection | ART-0, F-4 | active | CMP-40 |
| CMP-41 | Conventions internationales | ART-0, F-4 | active | CMP-41 |
| CMP-42 | Comite national d'homologation | ART-0, F-4 | active | CMP-42 |
| CMP-43 | Registre des initiatives | ART-0, F-4 | active | CMP-43 |
| CMP-44 | Comite d'ethique | ART-0, F-4 | active | CMP-44 |
| CMP-45 | Cellule d'audit | ART-0, F-4 | active | CMP-45 |
| CMP-46 | Arbitrage et risques | ART-0, F-4 | active | CMP-46 |
| DA-01 | Les données de santé sont un actif stratégique national | VS-01, VS-02, VS-03, VS-04 | draft | DA-01 |
| DA-02 | Une donnée doit être collectée une seule fois et réutilisée plusieurs fois | VS-01, VS-02, VS-03, VS-04 | draft | DA-02 |
| DA-03 | Les référentiels nationaux sont les sources de vérité | VS-01, VS-02, VS-03, VS-04 | draft | DA-03 |
| DA-04 | Les données opérationnelles et analytiques doivent être distinguées | VS-01, VS-02, VS-03, VS-04 | draft | DA-04 |
| DA-05 | La qualité des données est une responsabilité partagée | VS-01, VS-02, VS-03, VS-04 | draft | DA-05 |
| DA-06 | Les données doivent être utilisées pour des décisions réelles | VS-01, VS-02, VS-03, VS-04 | draft | DA-06 |
| DA-07 | Les données personnelles de santé doivent être protégées dès la conception | VS-01, VS-02, VS-03, VS-04 | draft | DA-07 |
| DA-08 | Les échanges de données doivent passer par des mécanismes gouvernés | VS-01, VS-02, VS-03, VS-04 | draft | DA-08 |
| DO-01 | DO-01 : Patient | — | draft | DO-01 |
| DO-02 | DO-02 : Identifiant national d'identification | — | draft | DO-02 |
| DO-03 | DO-03 : Dossier patient | — | draft | DO-03 |
| DO-04 | DO-04 : Épisode de soins | — | draft | DO-04 |
| DO-05 | DO-05 : Consultation | — | draft | DO-05 |
| DO-06 | DO-06 : Prescription | — | draft | DO-06 |
| DO-07 | DO-07 : Référence | — | draft | DO-07 |
| DO-08 | DO-08 : Contre-référence | — | draft | DO-08 |
| DO-09 | DO-09 : Évacuation sanitaire | — | draft | DO-09 |
| DO-10 | DO-10 : Dispensation | — | draft | DO-10 |
| DO-11 | DO-11 : Produit de santé | — | draft | DO-11 |
| DO-12 | DO-12 : Lot | — | draft | DO-12 |
| DO-13 | DO-13 : Stock | — | draft | DO-13 |
| DO-14 | DO-14 : Éligibilité | — | draft | DO-14 |
| DO-15 | DO-15 : Couverture sanitaire | — | draft | DO-15 |
| DO-16 | DO-16 : Facturation | — | draft | DO-16 |
| DO-17 | DO-17 : Vérification d'éligibilité | — | draft | DO-17 |
| DO-18 | DO-18 : Signal | — | draft | DO-18 |
| DO-19 | DO-19 : Foyer | — | draft | DO-19 |
| DO-20 | DO-20 : Investigation | — | draft | DO-20 |
| DO-21 | DO-21 : Notification sanitaire | — | draft | DO-21 |
| DO-22 | DO-22 : Alerte sanitaire | — | draft | DO-22 |
| DO-23 | DO-23 : Formation sanitaire | — | draft | DO-23 |
| DO-24 | DO-24 : Agent de santé | — | draft | DO-24 |
| DO-25 | DO-25 : Indicateur sanitaire | — | draft | DO-25 |
| DO-26 | DO-26 : Zone sanitaire | — | draft | DO-26 |
| DO-27 | DO-27 : Tâche | — | draft | DO-27 |
| DO-28 | DO-28 : Tableau de bord | — | draft | DO-28 |
| DO-29 | DO-29 : Résumé international du patient (IPS) | — | draft | DO-29 |
| DO-30 | DO-30 : Section du résumé patient | — | draft | DO-30 |
| DO-31 | DO-31 : Confiance internationale | — | draft | DO-31 |
| ENF-1 | Résilience à l'instabilité réseau | — | draft | ENF-1 |
| ENF-2 | Intégrité des flux et traçabilité des valeurs | — | draft | ENF-2 |
| ENF-3 | Unicité de l'identité et résilience face à la fragmentation applicative | — | draft | ENF-3 |
| ENF-4 | Cloisonnement inter-institutionnel et étanchéité des données (One Health) | — | draft | ENF-4 |
| ENF-5 | Coordination des processus complexes décentralisés et asynchrones | — | draft | ENF-5 |
| F-1 | Résilience face à la réalité géographique du pays | ENF-1, CAP-08 | stable | F-1 |
| F-2 | Préservation de la souveraineté intersectorielle | ENF-4 | stable | F-2 |
| F-3 | Éradication des silos technologiques | CAP-14 | stable | F-3 |
| F-4 | Homologation obligatoire | CAP-INT-12, CAP-16 | stable | F-4 |
| F-5 | Protection et minimisation | CAP-15 | draft | F-5 |
| F-6 | Observabilité | CAP-13 | draft | F-6 |
| GAP-01 | Écart — Couverture terrain en zone isolée | — | draft | GAP-01 |
| GAP-02 | Écart — Interopérabilité transfrontalière & One Health | — | draft | GAP-02 |
| GAP-03 | Écart — Cadre légal & gouvernance publié | — | draft | GAP-03 |
| LOC-01 | Communauté / aire de santé | — | draft | LOC-01 |
| LOC-02 | Centre de santé de base (CSB) | — | draft | LOC-02 |
| LOC-03 | District sanitaire | — | draft | LOC-03 |
| LOC-04 | Région sanitaire | — | draft | LOC-04 |
| LOC-05 | Établissement hospitalier de référence | — | draft | LOC-05 |
| LOC-06 | Siège central (DEPSI) | — | draft | LOC-06 |
| P-INT-01 | Autorité désignée | CAP-14 | active | P-INT-01 |
| P-INT-02 | Résolution contre l’autorité | CAP-14 | active | P-INT-02 |
| P-INT-03 | Copies locales non autoritatives | CAP-14 | active | P-INT-03 |
| P-INT-04 | Historisation des références | CAP-14 | active | P-INT-04 |
| P-INT-05 | Contrat explicite | CAP-14 | active | P-INT-05 |
| P-INT-06 | Versionnement et compatibilité | CAP-14 | active | P-INT-06 |
| P-INT-07 | Responsabilité de la donnée | CAP-13 | active | P-INT-07 |
| P-INT-08 | Publication au catalogue des services | CAP-14, CAP-16 | active | P-INT-08 |
| P-INT-09 | Publication des contrats | CAP-14, CAP-16 | active | P-INT-09 |
| P-INT-10 | Accord préalable | CAP-14 | active | P-INT-10 |
| P-INT-11 | Arbitrage des conflits d’autorité | CAP-14 | active | P-INT-11 |
| P-INT-12 | Dérogation explicite | CAP-14, CAP-16 | active | P-INT-12 |
| P-INT-13 | Dérogation d’urgence | CAP-14, CAP-16 | active | P-INT-13 |
| P-INT-14 | Base d’autorisation explicite | CAP-15 | active | P-INT-14 |
| P-INT-15 | Limitation à la finalité | CAP-15 | active | P-INT-15 |
| P-INT-16 | Résidence et non-réplication | CAP-14, CAP-15 | active | P-INT-16 |
| P-INT-17 | Minimisation | CAP-15 | active | P-INT-17 |
| P-INT-18 | Traçabilité différenciée | CAP-13, CAP-15 | active | P-INT-18 |
| P-INT-19 | Neutralité technologique | CAP-14 | active | P-INT-19 |
| P-INT-20 | Portabilité et réversibilité | CAP-14 | active | P-INT-20 |
| P-INT-21 | Progressivité | CAP-16 | active | P-INT-21 |
| P-INT-22 | Fonctionnement en connectivité contrainte | CAP-14 | active | P-INT-22 |
| P-INT-23 | Conformité fondée sur des preuves | CAP-16 | active | P-INT-23 |
| P-INT-24 | Applicabilité déclarée | CAP-16 | active | P-INT-24 |
| P-INT-25 | Réévaluation continue | CAP-16 | active | P-INT-25 |
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
| PL-01 | Socle & confiance numérique | — | draft | PL-01 |
| PL-02 | Services de terrain & interopérabilité | — | draft | PL-02 |
| PL-03 | Intelligence & ouverture | — | draft | PL-03 |
| PP-01 | Patient et usager | — | draft | PP-01 |
| PP-02 | Ménage et famille | — | draft | PP-02 |
| PP-03 | Population | — | draft | PP-03 |
| PP-04 | Communauté | — | draft | PP-04 |
| PP-05 | Agent de santé | — | draft | PP-05 |
| PP-06 | Formation sanitaire | — | draft | PP-06 |
| PP-07 | District, région et Ministère | — | draft | PP-07 |
| PP-08 | Partenaires techniques et financiers | — | draft | PP-08 |
| PP-09 | Décideurs institutionnels | — | draft | PP-09 |
| PP-10 | Équipes techniques (DEPSI / SIS) | — | draft | PP-10 |
| PRC-01 | Accès, orientation et admission du patient | CAP-01, CAP-02, CAP-04, CAP-11, CAP-13, CAP-14, CAP-15, CMP-19, CMP-21, CMP-22 | active | PRC-01 |
| PRC-02 | Prestation des soins cliniques | CAP-01, CAP-03, CAP-09, CAP-10, CAP-11, CAP-13, CAP-14, CAP-15, CMP-19, CMP-20, CMP-21 | active | PRC-02 |
| PRC-03 | Continuité, suivi et qualité des soins | CAP-02, CAP-03, CAP-04, CAP-13, CAP-14, CAP-15, CMP-19, CMP-21 | active | PRC-03 |
| PRC-04 | Veille, prévention et surveillance sanitaire | CAP-04, CAP-05, CAP-06, CAP-13, CAP-14, CAP-15, CAP-17, CMP-07, CMP-08, CMP-11, CMP-13, CMP-15, CMP-17, CMP-18, CMP-24, CMP-25 | active | PRC-04 |
| PRC-05 | Alerte, investigation et riposte | CAP-04, CAP-05, CAP-13, CAP-14, CAP-15, CAP-17, CAP-18, CMP-02, CMP-04, CMP-07, CMP-08, CMP-11, CMP-13, CMP-14, CMP-15, CMP-17, CMP-18, CMP-20, CMP-23, CMP-24, CMP-25 | active | PRC-05 |
| PRC-06 | Clôture et capitalisation des épisodes | CAP-03, CAP-13, CAP-14, CAP-15, CMP-07, CMP-11, CMP-14, CMP-15, CMP-17, CMP-18, CMP-19 | active | PRC-06 |
| PRC-07 | Identification et droits des bénéficiaires | CAP-07, CAP-08, CAP-13, CAP-14, CAP-15, CAP-17, CMP-09, CMP-10, CMP-16, CMP-22 | active | PRC-07 |
| PRC-08 | Financement et exemption au point de service | CAP-07, CAP-08, CAP-12, CAP-13, CAP-15, CAP-16, CMP-09, CMP-10, CMP-16, CMP-22 | active | PRC-08 |
| PRC-09 | Remboursement et régulation des mécanismes | CAP-07, CAP-12, CAP-13, CAP-14, CAP-15, CMP-03, CMP-04, CMP-12 | active | PRC-09 |
| PRC-10 | Planification et allocation des ressources | CAP-08, CAP-09, CAP-12, CAP-13, CAP-15, CAP-16, CMP-01, CMP-12, CMP-23 | active | PRC-10 |
| PRC-11 | Suivi et pilotage de la performance | CAP-03, CAP-08, CAP-13, CAP-14, CAP-15, CAP-16, CMP-01, CMP-02, CMP-03, CMP-25 | active | PRC-11 |
| PRC-12 | Redevabilité et amélioration continue | CAP-03, CAP-08, CAP-13, CAP-14, CAP-15, CAP-16, CMP-01 | active | PRC-12 |
| PRC-13 | Échange et coordination transfrontaliers | CAP-INT-13, CAP-15, CAP-17, CMP-02, CMP-06, CMP-15 | active | PRC-13 |
| PT-01 | Échange interinstitutionnel | CMP-06, CAP-INT-03, CAP-INT-12, ART-0, ART-1, ART-7, ART-11 | active | PT-01 |
| PT-02 | Médiation intra-secteur | CMP-06, CAP-INT-03, ART-1, ART-2, ART-5, ART-7, ART-8, ART-8C, ART-8D | active | PT-02 |
| PT-03 | Catalogue des services et registre des contrats | CMP-16, CAP-INT-06, F-3, F-4, ART-1, ART-2 | active | PT-03 |
| PT-04 | Résolution d’identité du bénéficiaire | CMP-11, CAP-INT-01, ART-4, ART-4A, ART-4B, ART-7 | active | PT-04 |
| PT-05 | Registre des professionnels | CMP-13, CAP-INT-02, ART-4, ART-4A, ART-7, ART-4C | active | PT-05 |
| PT-06 | Référentiel des structures et services de santé | CMP-08, CAP-INT-04, ART-4, ART-5, ART-6 | active | PT-06 |
| PT-07 | Terminologie et codification | CMP-10, CAP-INT-05, ART-2, ART-4, ART-5 | active | PT-07 |
| PT-08 | Échange de données agrégées | CMP-03, CMP-06, CAP-INT-03, CAP-INT-07, ART-1, ART-2, ART-5, ART-6 | active | PT-08 |
| PT-09 | Analytique et exposition de données | CMP-03, CMP-04, CAP-INT-07, ART-3, ART-5, ART-6, ART-7 | active | PT-09 |
| PT-10 | Confiance, authentification et autorisation | CMP-15, CAP-INT-08, ART-0, ART-4B, ART-7, ART-9 | active | PT-10 |
| PT-11 | Consentement et bases d’autorisation | CMP-12, CAP-INT-09, ART-0, ART-4B, ART-7, ART-11 | active | PT-11 |
| PT-12 | Audit, provenance et traçabilité | CMP-17, CAP-INT-10, F-1, F-5, F-6, ART-3, ART-7 | active | PT-12 |
| PT-13 | Qualité et réconciliation | CMP-05, CAP-INT-11, ART-4, ART-5, ART-6 | active | PT-13 |
| PT-14 | Interopérabilité transfrontalière | CAP-INT-13, CAP-15, CAP-17, CMP-06, CMP-15, ART-7, ART-0, ART-1 | active | PT-14 |
| PT-15 | Surveillance One Health | CAP-INT-14, CAP-INT-16, CAP-18, CAP-05, CMP-02, CMP-04, CMP-06, ART-11, ART-0, ART-4D, ART-8B | active | PT-15 |
| PT-16 | Orchestration de processus bornés | CMP-07, CMP-06, CAP-INT-03, ART-8A, ART-7 | active | PT-16 |
| PT-17 | Logistique & chaîne d'approvisionnement (LMIS) | CMP-23, CAP-INT-10, CAP-INT-15, ART-10 | active | PT-17 |
| PT-18 | Échange de réclamations et paiements | CAP-INT-07, ART-2, ART-9 | active | PT-18 |
| PT-19 | Aide à la décision clinique (CDS) | CMP-08, CAP-INT-05, ART-12, ART-2 | active | PT-19 |
| ROL-01 | Clinicien / prestataire de soins | — | draft | ROL-01 |
| ROL-02 | Gestionnaire de parcours / référence | — | draft | ROL-02 |
| ROL-03 | Gestionnaire de données / registre | — | draft | ROL-03 |
| ROL-04 | Gestionnaire logistique | — | draft | ROL-04 |
| ROL-05 | Contrôleur / auditeur | — | draft | ROL-05 |
| SRV-01 | Service d'identité du bénéficiaire | ART-2 | draft | SRV-01 |
| SRV-02 | Service de dossier patient | ART-2 | draft | SRV-02 |
| SRV-03 | Service de référentiels | ART-4 | draft | SRV-03 |
| SRV-04 | Service d'échange inter-systèmes | ART-9 | draft | SRV-04 |
| SRV-05 | Service logistique (LMIS) | ART-10 | draft | SRV-05 |
| SRV-06 | Service de pilotage et tableaux de bord | ART-3 | draft | SRV-06 |
| VAL-01 | Soins accessibles, continus, sûrs et de qualité | — | active | VAL-01 |
| VAL-02 | Protection contre les maladies, épidémies et urgences sanitaires | — | active | VAL-02 |
| VAL-03 | Protection financière contre les dépenses de santé | — | active | VAL-03 |
| VAL-04 | Système de santé planifié, coordonné et continuellement amélioré | — | active | VAL-04 |
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
| WP-01 | Infrastructure & sécurité | — | draft | WP-01 |
| WP-02 | Applications terrain & collecte | — | draft | WP-02 |
| WP-03 | Médiation & registres partagés | — | draft | WP-03 |
| WP-04 | Analytique & pilotage | — | draft | WP-04 |
| WP-05 | Extension & pérennisation | — | draft | WP-05 |
| WP-06 | Interopérabilité transfrontalière | — | draft | WP-06 |
| WP-07 | Coordination One Health | — | draft | WP-07 |

<!-- END:GENERATED -->

## Lecture

La traçabilité ADM doit être utilisée comme contrôle de cohérence global. Elle ne remplace pas les vues spécialisées, mais permet d'identifier rapidement les objets sans rattachement ou les périmètres dont la phase ADM doit être précisée.
