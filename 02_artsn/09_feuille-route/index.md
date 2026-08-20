---
title: "Feuille de route de déploiement progressif de l'ARTSN"
domain: 02_artsn
id: roadmap-deploiement-artsn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: "Direction du Numérique en Santé"
tags:
  - artsn
  - feuille-de-route
  - deploiement
  - planification
  - implementation
---

# Feuille de route de déploiement progressif de l'ARTSN

## Objectif

Documenter la séquence de déploiement des composants de l'Architecture de Référence Technique de la Santé Numérique (ARTSN) selon un planning réaliste et prioritaire, en alignement avec le Cadre d'Architecture d'Entreprise (CAESN) et les besoins des initiatives du catalogue PTISN.

## Architecture cible : Rappel

L'ARTSN est structurée en **6 couches horizontales** (Couche 1 à 6) traversées par **2 axes verticaux** (Sécurité, Gouvernance de données). Le déploiement respecte l'ordre bottom-up : chaque couche dépend de celle qui la sous-tend.

| Couche | Intitulé | Composants clés |
|--------|----------|-----------------|
| 6 | Pilotage & gouvernance intersectorielle | Tableaux de bord nationaux, centre de commande alertes |
| 5 | Projections analytiques & modèles | Entrepôt Lakehouse, IA prédictive, moteur de graphes |
| 4 | Interopérabilité & services partagés | Médiation (ART-2), registres (patient, personnels, produits, terminologies, éligibilité), orchestrateur (ART-8a) |
| 3 | Échange, transport & ingestion | API Gateway, message broker, registre de schémas (F.3), serveur de sécurité X-Road santé (connecté à l'infrastructure UGD existante) |
| 2 | Point de service | Applications terrain (dossiers, pharmacie, LMIS, santé communautaire, enquêtes) |
| 1 | Infrastructure | Data centers nationaux, nœuds régionaux, nœuds locaux, VPN, liaisons sécurisées |
| Axe 1 | Sécurité & confiance numérique | Identités, RBAC/ABAC, consentement, PKI, chiffrement, audit |
| Axe 2 | Gouvernance de données | Accords inter-institutions, charte protection, comité homologation |

## 1. Phases de déploiement

### Phase 1 : Infrastructure & sécurité (T4 2026 – T2 2027) : 9 mois

**Priorité absolue.** Pas de système sans socle matériel ni sécurité. Cette phase pose les fondations physiques et transversales de toute la plateforme.

| Composant | Couches | Responsables | Livrables | Critère de succès |
|-----------|---------|--------------|-----------|-------------------|
| **Data center national** | Couche 1 | DNS, STEG | 2 sites certifiés HDS (Antananarivo + backup) | Disponibilité 99,5% |
| **Nœuds régionaux** | Couche 1 | DNS, régions | 6 clusters régionaux (Fog) opérationnels | 6 régions couvertes |
| **VPN & liaisons** | Couche 1 | DNS, telecoms | Réseau MPLS + APN sécurisés | Connectivité 95% des districts |
| **Identité santé** | Axe 1 | DNS, ANM | Registre des identifiants (INP), module authentification | 100% agents identifiés |
| **Sécurité** | Axe 1 | DNS, CNRAC | Politique chiffrement RBAC/ABAC, PKI, audit | Conformité NIST 800-53 |
| **Gouvernance de données** | Axe 2 | DNS, Ministère | Charte protection, registre accords, comité homologation | Cadre réglementaire publié |
| **Référentiels de base** | Couche 4 | DNS | Registre terminologies (CIM-10, SNOMED CT, LOINC), registre personnels, registre produits | 500 termes mappés, 100% agents référencés |
| **Serveur de sécurité X-Road** | Couche 3 | DNS, UGD | Security Server santé connecté au backbone X-Road UGD existant | Serveur opérationnel, prêt pour échanges inter-institutionnels |

**Note** : L'infrastructure X-Road est déjà opérationnelle via l'UGD (Unité de Gouvernance Digitale). La phase 1 déploie uniquement le serveur de sécurité (Security Server) côté santé pour s'y connecter.

**Livrable clé** : Infrastructure opérationnelle + cadre de sécurité + référentiels de base.

### Phase 2 : Applications terrain & collecte (T2 2027 – T4 2027) : 6 mois

**Couche 2 : Point de service.** Déployer les applications de terrain qui captent les données au plus près des formations sanitaires, y compris en mode hors-ligne.

| Composant | Couches | Responsables | Livrables | Critère de succès |
|-----------|---------|--------------|-----------|-------------------|
| **Dossiers patients** | Couche 2 | DNS, hôpitaux | Application dossiers (HOS) déployée dans 22 RIS | 22 hôpitaux connectés |
| **Gestion pharmacies** | Couche 2 | DNS, PMI | Application PMIS (gestion stocks) | 100 pharmacies couvertes |
| **Santé communautaire** | Couche 2 | DNS,communes | Application mobile offline (CSS) | 500 agents communautaires équipés |
| **Chaîne logistique** | Couche 2 | DNS, logistique | Application LMIS (suivi intrants) | 80% intrants tracés |
| **Équipes mobiles** | Couche 2 | DNS, enquêtes | Tablettes enquêtes + capteurs terrain | 50 enquêtes déployées |
| **API Gateway** | Couche 3 | DNS | Point d'entrée unique, throttling, authentification | Toutes les app terrain connectées |
| **Message broker** | Couche 3 | DNS | Files d'attente asynchrones, persistance | 1 000 messages/jour traités |

**Livrable clé** : 5 applications terrain opérationnelles + couche transport asynchrone.

### Phase 3 : Médiation & registres partagés (T4 2027 – T2 2028) : 6 mois

**Couche 4 : Interopérabilité.** Centraliser les registres nationaux et orchestrer les parcours cliniques transversaux.

| Composant | Couches | Responsables | Livrables | Critère de succès |
|-----------|---------|--------------|-----------|-------------------|
| **Moteur de médiation** | Couche 4 | DNS | Moteur ART-2 (transformation, normalisation, enrichissement) | 80% messages transformés |
| **Orchestrateur de parcours** | Couche 4 | DNS | Gestionnaire de Sagas (ART-8a) | Parcours multi-systèmes opérationnels |
| **Registre patients** | Couche 4 | DNS | Index National des Patients (INP : ART-4a) | 500 000 patients dédupliqués |
| **Registre éligibilité** | Couche 4 | DNS | CSU vérification en temps réel (ART-4c) | 100% soins vérifiés |
| **Registre de schémas** | Couche 3 | DNS | Versioning schémas, validation FHIR | 100% messages validés |
| **Serveur de sécurité X-Road santé** | Couche 3 | DNS, UGD | Serveur de sécurité (Security Server) connecté au backbone X-Road UGD existant, connecteurs inter-institutionnels (État civil, Protection sociale, Finances) | Serveur opérationnel, 5 échanges inter-institutionnels/jour |
| **Consentement** | Axe 1 | DNS, CNRAC | Gestion du consentement numérique | Conformité Loi 2014-038 |

**Livrable clé** : Médiation opérationnelle + 3 registres nationaux + premiers échanges inter-institutionnels.

### Phase 4 : Analytique & pilotage (T2 2028 – T4 2028) : 6 mois

**Couche 5-6 : Projections analytiques & pilotage.** Construire la capacité analytique et les tableaux de bord décisionnels.

| Composant | Couches | Responsables | Livrables | Critère de succès |
|-----------|---------|--------------|-----------|-------------------|
| **Entrepôt Lakehouse** | Couche 5 | DNS | Architecture CQRS (ART-6), 3 pipelines ETL | Données consolidées disponibles |
| **Moteur de graphes** | Couche 5 | DNS, INS | Graphe de connaissances (ART-8b), modèle RDF | Requêtes SPARQL fonctionnelles |
| **IA prédictive** | Couche 5 | DNS | 3 modèles (TB, palu, prédiction hospitalière) | Précision > 80% |
| **Tableaux de bord** | Couche 6 | DNS | Dashboards nationaux (performance, CSU, ressources) | Indicateurs publiés mensuellement |
| **Centre de commande** | Couche 6 | DNS | Alertes épidémiques temps réel (ART-5) | 100% alertes traitées |
| **Grand Livre** | Couche 5 | DNS | Réconciliation analytique (ART-9) | 99% données réconciliées |

**Livrable clé** : Entrepôt analytique + 3 modèles IA + tableaux de bord décisionnels.

### Phase 5 : Extension & pérennisation (T4 2028 – T2 2029) : 6 mois

**Intégration complète et stabilisation.** Connecter les régions restantes, former, évaluer et assurer la pérennité.

| Composant | Couches | Responsables | Livrables | Critère de succès |
|-----------|---------|--------------|-----------|-------------------|
| **Intégration RIS/RPS** | Couche 2-3 | DNS, Ministères | Connexion 22 RIS + 6 RPS | 100% régions connectées |
| **DPI régional** | Couche 4 | DNS, Régions | DPI déployé dans 6 régions pilotes | 10 000 dossiers créés |
| **Interopérabilité externe** | Couche 3 | DNS | Adhésion GDHCN, point de confiance nationale (Trust Anchor), accords bilatéraux SADC/UA, PT-14 déployé, service IPS (résumé patient) opérationnel, premier flux OMS AFRO testé | GDHCN opérationnel, 1 accord bilatéral signé, PT-14 opérationnel, IPS interopérable |
| **Supervision** | Toutes | DNS | Monitoring centralisé, alertes | Disponibilité > 99,5% |
| **Formation** | Toutes | DNS, INS | 500 professionnels formés | 90% taux de réussite |
| **Évaluation** | Toutes | DNS, INS | Bilan annuel, recommandations | Rapport publié |
| **Migration données** | Couche 2-4 | DNS | Migration legacy → nouvelle architecture | 0 perte de données |

**Livrable clé** : 22 régions connectées + DPI + formation + évaluation complète.

### Phase 6 : Coordination One Health (T2 2029 – T4 2029) : 6 mois

**Dimension intersectorielle.** Déployer les échanges de données entre santé humaine, animale et environnement pour la surveillance et la riposte coordonnée.

| Composant | Couches | Responsables | Livrables | Critère de succès |
|-----------|---------|--------------|-----------|-------------------|
| **Accords interministériels** | Axe 2 | DNS, MSP, MINAE, MEEF | Accords de partage de données signés (MSP–MINAE–MEEF) | 3 accords signés |
| **Médiation intersectorielle** | Couche 4 | DNS | Moteur de transformation CIM-10 ↔ OIE ↔ GBIF | 80% messages intersectoriels transformés |
| **Centre de commande One Health** | Couche 6 | DNS | CMP-02 activé pour alertes intersectorielles | Alertes multi-ministères opérationnelles |
| **Corrélation signaux faibles** | Couche 5 | DNS, INS | Moteur de corrélation (ART-8b) pour clusters intersectoriels | Détection cluster < 24h |
| **PT-15 déployé** | Toutes | DNS | Profil Surveillance One Health opérationnel en pilote (1 région) | 1 région pilote active |
| **Tripartite Plus** | Toutes | DNS, MINAE | Flux avec OMS–WOAH–FAO–PNUE opérationnels | 1 flux international One Health actif |

**Livrable clé** : Accords interministériels + médiation intersectorielle + centre de commande One Health.

## 2. Jalons critiques

| Jalon | Phase | Date | Responsable | Risque si retard |
|-------|-------|------|-------------|------------------|
| **J1** : Décret CNASN + charte gouvernance | P1 | T4 2026 | Ministère | Blocage gouvernance |
| **J2** : Data center national opérationnel | P1 | T1 2027 | DNS, STEG | Pas d'hébergement |
| **J3** : Identité santé + sécurité | P1 | T2 2027 | DNS, ANM, CNRAC | Pas de confiance numérique |
| **J4** : Serveur X-Road santé opérationnel | P1 | T1 2027 | DNS, UGD | Pas d'échanges inter-institutionnels |
| **J5** : 22 hôpitaux connectés | P2 | T4 2027 | DNS, RIS | Pas de données terrain |
| **J6** : Médiation + 3 registres | P3 | T2 2028 | DNS | Pas d'interopérabilité |
| **J7** : 22 RIS + 6 RPS connectés | P5 | T4 2028 | DNS, Ministères | Données incomplètes |
| **J8** : Audit indépendant | P5 | T2 2029 | INS | Pas de validation |
| **J9** : Accords interministériels One Health | P6 | T2 2029 | DNS, MSP, MINAE, MEEF | Pas de coordination intersectorielle |
| **J10** : PT-15 opérationnel | P6 | T4 2029 | DNS | Pas de surveillance One Health |
| **J11** : PT-14 opérationnel (transfrontalier) | P5 | T2 2029 | DNS | Pas d'interopérabilité SADC/UA |

## 3. Risques et mitigations

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| **Retard budget** | Élevée | Critique | Phasage, bailleurs internationaux, FSP |
| **Résistance changement** | Moyenne | Élevée | Formation, communication, champions régionaux |
| **Défaillance infrastructure** | Moyenne | Critique | Redondance 2 sites, backup offline |
| **Problèmes intégration** | Moyenne | Élevée | Tests unitaires, prototypage, sandbox |
| **Départs équipe** | Moyenne | Élevée | Documentation, transfert compétences |
| **Obsolescence technique** | Faible | Élevée | Veille technologique, mises à jour annuelles |

## 4. Gouvernance du déploiement

| Instance | Rôle | Fréquence |
|----------|------|-----------|
| **Comité de pilotage** | Stratégie, budget, arbitrage | Trimestrielle |
| **Comité technique** | Architecture, sécurité, intégration | Mensuelle |
| **Cellule de projet** | Suivi des lots, blocages | Hebdomadaire |
| **Réseau des régions** | Retour terrain, besoins | Bimensuelle |

## 5. Budget estimé

| Phase | Montant estimé (MGA) | Sources |
|-------|----------------------|---------|
| Phase 1 : Infrastructure & sécurité | 25 milliards | État, BM, UE, BAD |
| Phase 2 : Applications terrain | 20 milliards | BM, UE, coopération bilatérale |
| Phase 3 : Médiation & registres | 18 milliards | BM, BAD, UE |
| Phase 4 : Analytique & pilotage | 20 milliards | UE, AfDB, État |
| Phase 5 : Extension & pérennisation | 15 milliards | État, fonds propres |
| **Total** | **98 milliards** | |

## 6. Indicateurs de suivi

| Indicateur | P1 (9 mois) | P2 (15 mois) | P3 (21 mois) | P4 (27 mois) | P5 (33 mois) |
|------------|-------------|--------------|--------------|--------------|--------------|
| Data centers opérationnels | 2 | 2 | 2 | 2 | 2 |
| Régions avec nœud régional | 6 | 6 | 6 | 6 | 6 |
| Applications terrain déployées | 0 | 5 | 5 | 5 | 5 |
| Registres nationaux opérationnels | 3 (base) | 3 | 6 | 6 | 6 |
| Serveur X-Road santé | ✅ | ✅ | ✅ | ✅ | ✅ |
| Échanges/jour (total) | 0 | 1 000 | 10 000 | 50 000 | 100 000 |
| Échanges inter-institutionnels/jour | 0 (config) | 0 (config) | 5 | 20 | 50 |
| Régions connectées (RIS/RPS) | 6 | 6 | 6 | 15 | 22 |
| Professionnels formés | 0 | 50 | 200 | 350 | 500 |
| Disponibilité plateforme | 99% | 99% | 99,5% | 99,5% | 99,9% |

## 7. Dépendances externes

| Dépendance | Acteur | Phase | Statut | Action requise |
|------------|--------|-------|--------|----------------|
| **Décret CNASN** | Ministère de la Santé | P1 | En attente | Solliciter publication T4 2026 |
| **Budget infrastructure** | Ministère des Finances | P1 | Préparation | Dépôt dossier Q4 2026 |
| **Accord BM** | Banque Mondiale | P1-P2 | Finalisation | Signature T1 2027 |
| **Accord UE** | Délégation UE | P2-P3 | Négociation | Signature T2 2027 |
| **Norme FHIR R4** | HL7 International | P3 | Validée | Adoption nationale |
| **SNOMED CT** | SNOMED International | P1 | Licence | Obtention licence nationale |
| **X-Road backbone** | UGD | P1 | ✅ Opérationnel | Déployer le serveur de sécurité santé (Security Server) et connecter au backbone UGD |
| **Accords inter-institutions** | État civil, Finances, Éducation | P3 | En attente | Négociation P2 |

## 8. Prochaines étapes

À l'horizon immédiate d'août à septembre 2026, la priorité consiste à présenter la feuille de route au Comité de pilotage, à valider le budget prévisionnel de la Phase 1 d'infrastructure, à lancer l'appel d'offres pour le data center national et à coordonner avec l'UGD le déploiement du serveur de sécurité X-Road santé. Sur la période court terme d'octobre à décembre 2026, l'équipe projet de huit personnes sera recrutée, l'environnement de développement sera déployé et la construction des nœuds régionaux sera amorcée. En milieu de parcours, au cours de l'année 2027, les jalons J1, J2 et J3 devront être atteints, les applications terrain de la Phase 2 lancées et les résultats de la Phase 1 évalués.

**Prochaine révision** : Septembre 2026
