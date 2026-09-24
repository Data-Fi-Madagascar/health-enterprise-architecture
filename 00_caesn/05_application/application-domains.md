---

title: Domaines applicatifs cibles par flux de valeur
id: application-domains
domain: 05_application
version: "1.0.0"
status: draft
last_reviewed: 2026-07-03
owner: Direction des Systèmes d'Information
tags: ["applications", "domaines", "flux"]
---

# Domaines applicatifs cibles par flux de valeur

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

Le cadre retient les domaines applicatifs suivants, qui décrivent des familles de systèmes sans imposer un logiciel particulier.

| Flux de valeur | Domaine applicatif | Services numériques | Capabilités |
|----------------|--------------------|---------------------|-------------|
| VS-01 | Dossier patient et parcours de soins | Identification patient, dossier de soins, historique, consultation, référence, contre-référence, suivi | CAP-01, 02, 03, 14, 15 |
| VS-01 | Système d'information hospitalier et formation sanitaire | Admissions, consultations, actes, services, statistiques opérationnelles | CAP-01, 03, 13 |
| VS-01 / VS-02 | Santé communautaire | Suivi communautaire, sensibilisation, remontée d'alertes, visites à domicile, suivi des ménages, supervision | CAP-04, 05, 06 |
| VS-02 | Surveillance épidémiologique et riposte | Notification des cas, alertes, investigation, confirmation, riposte, clôture | CAP-05, 06, 13, 14 |
| VS-02 | Vaccination, prévention et promotion de la santé | Registre vaccinal, suivi des campagnes, rappels, couverture, chaîne du froid | CAP-06, 10, 13 |
| VS-03 | Couverture santé universelle et gestion des bénéficiaires | Enregistrement des bénéficiaires, vérification des droits, exemptions, panier de soins, éligibilité | CAP-07, 14, 15 |
| VS-03 | Facturation, remboursement et achat stratégique | Facturation des prestations, validation, remboursement, contrôle, audit, suivi des coûts | CAP-07, 08, 12, 13 |
| VS-01 / VS-02 / VS-04 | Logistique et chaîne d'approvisionnement | Gestion des stocks, commandes, distribution, ruptures, traçabilité, chaîne du froid | CAP-10, 13, 14 |
| VS-04 | Ressources humaines en santé | Référentiel agents, affectation, disponibilité, formation, supervision, compétences | CAP-09, 13, 14 |
| VS-04 | Entrepôt national de données et tableaux de bord | Consolidation, analyse, indicateurs, visualisation, revues de performance | CAP-13, 08, 16 |
| VS-04 | Gestion du portefeuille numérique | Registre des initiatives, suivi des financements, alignement stratégique, maturité des capabilités, bénéfices | CAP-16, 08, 13 |
| Tous les VS | Référentiels nationaux et services partagés | FOSA, géographie, indicateurs, agents, produits, bénéficiaires, terminologies, identité, accès, consentement | CAP-13, 14, 15 |

## Composants applicatifs cibles

<!-- BEGIN:GENERATED source=04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-01.md,04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-02.md,04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-03.md,04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-04.md,04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-05.md,04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-06.md,04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-07.md,04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-08.md,04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-09.md,04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-10.md,04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-11.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Tableaux de bord & Portails nationaux

**Contenu normatif.** Ce composant agrège les projections analytiques (Couche 5) et expose des tableaux de bord unifiés pour le pilotage national : performance sanitaire, suivi CSU, gestion des ressources et veille environnementale. L'accès y est cloisonné par profil (décideurs, SIS, partenaires). Il interopère avec l'entrepôt Lakehouse ([CMP-03: Entrepôt Lakehouse & Projections analytiques (pipeline ETL, Lakehouse, projections)](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-03.md)) et le moteur analytique ([CMP-04: Moteur analytique & IA (IA prédictive, routeur alertes, Grand Livre)](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-04.md)).

**Discipline de mise en œuvre.** Il constitue la seule source de vérité décisionnelle pour l'État ; tout indicateur officiel y transite. Il garantit l'unicité des métriques et la traçabilité des calculs.

- **Rattachement** : [ART-6](../../04_architecture-repository/04_patterns/artsn-rules/art-6.md) (projections analytiques), [ABB-EXPOSITION-DONNEES-ANALYTIQUES: Accès et exposition des données analytiques](../../04_architecture-repository/05_building-blocks/abb/abb-exposition-donnees-analytiques.md), [ABB-RECONCILIATION-DONNEES: Qualité et réconciliation](../../04_architecture-repository/05_building-blocks/abb/abb-reconciliation-donnees.md).
- **Processus soutenus** : [PRC-10: Planification et allocation des ressources](../../04_architecture-repository/02_architecture-elements/business/processes/prc-10.md) (planification), [PRC-11: Suivi et pilotage de la performance](../../04_architecture-repository/02_architecture-elements/business/processes/prc-11.md) (pilotage performance), [PRC-12: Redevabilité et amélioration continue](../../04_architecture-repository/02_architecture-elements/business/processes/prc-12.md) (redevabilité).
- **Statut : Stable.**

### Centre de commande & Crises intersectorielles

**Contenu normatif.** Ce composant constitue le centre unique de supervision des alertes épidémiques et de coordination des crises intersectorielles (santé, élevage, environnement). Il agrège les signaux de la surveillance ([CMP-14: Registre des produits, intrants et indicateurs](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-14.md)), du moteur d'alertes ([CMP-04: Moteur analytique & IA (IA prédictive, routeur alertes, Grand Livre)](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-04.md)) et des registres de gouvernance ([CMP-17: Message broker asynchrone](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-17.md)), et fournit une vue en temps réel pour la prise de décision multi-ministérielle.

**Discipline de mise en œuvre.** Il est le point de convergence obligatoire de toute riposte coordonnée ; sans lui, les secteurs agissent en silos et la riposte reste fragmentée.

- **Rattachement** : [ART-5](../../04_architecture-repository/04_patterns/artsn-rules/art-5.md) (routeur alertes), [ART-0](../../04_architecture-repository/04_patterns/artsn-rules/art-0.md) (accords partage), [ABB-EXPOSITION-DONNEES-ANALYTIQUES: Accès et exposition des données analytiques](../../04_architecture-repository/05_building-blocks/abb/abb-exposition-donnees-analytiques.md).
- **Processus soutenus** : [PRC-05: Alerte, investigation et riposte](../../04_architecture-repository/02_architecture-elements/business/processes/prc-05.md) (alerte/investigation/riposte), [PRC-11: Suivi et pilotage de la performance](../../04_architecture-repository/02_architecture-elements/business/processes/prc-11.md) (pilotage performance).
- **Statut : Stable.**

### Entrepôt Lakehouse & Projections analytiques

**Contenu normatif.** Ce composant assure le stockage analytique central (Lakehouse) en recevant les flux ETL depuis la Couche 4. Il exécute les projections tabulaires, la réconciliation du Grand Livre ([ART-9: Garanties transactionnelles fortes](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md)) et alimente les tableaux de bord ([CMP-01: Tableaux de bord & Portails nationaux (performance, CSU, ressources, veille)](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-01.md)). La séparation stricte CQRS ([ART-6: Analytique et restitution](../../04_architecture-repository/04_patterns/artsn-rules/art-6.md)) interdit tout traitement transactionnel.

**Discipline de mise en œuvre.** Il garantit l'intégrité analytique ([ENF-5: Coordination des processus complexes décentralisés et asynchrones](../../04_architecture-repository/03_requirements/enf-5.md)) et l'irréversibilité du masquage des identités. Toute analyse officielle passe par cet entrepôt.

- **Rattachement** : [ART-6](../../04_architecture-repository/04_patterns/artsn-rules/art-6.md) (CQRS), [ART-9](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md) (Grand Livre), [ABB-EXPOSITION-DONNEES-ANALYTIQUES: Accès et exposition des données analytiques](../../04_architecture-repository/05_building-blocks/abb/abb-exposition-donnees-analytiques.md), [ABB-RECONCILIATION-DONNEES: Qualité et réconciliation](../../04_architecture-repository/05_building-blocks/abb/abb-reconciliation-donnees.md).
- **Processus soutenus** : [PRC-09: Remboursement et régulation des mécanismes](../../04_architecture-repository/02_architecture-elements/business/processes/prc-09.md) (remboursement), [PRC-11: Suivi et pilotage de la performance](../../04_architecture-repository/02_architecture-elements/business/processes/prc-11.md) (pilotage).
- **Statut : Stable.**

### Moteur analytique & IA

**Contenu normatif.** Ce composant exécute les modèles prédictifs (IA), le routeur d'escalade et d'alertes ([ART-5: Cohérence et qualité des données](../../04_architecture-repository/04_patterns/artsn-rules/art-5.md)) et la réconciliation analytique du Grand Livre ([ART-9: Garanties transactionnelles fortes](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md)). Il consomme l'entrepôt Lakehouse ([CMP-03: Entrepôt Lakehouse & Projections analytiques (pipeline ETL, Lakehouse, projections)](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-03.md)) et alimente le centre de commande ([CMP-02: Centre de commande & Crises intersectorielles (alertes, crises, veille)](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-02.md)) ainsi que la facturation ([CMP-10: Registre des terminologies](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-10.md)).

**Discipline de mise en œuvre.** Il sépare l'inférence analytique du stockage et garantit la traçabilité des modèles (versionnage, données d'entraînement) ainsi que l'audit des décisions automatisées ([ENF-2: Intégrité des flux et traçabilité des valeurs](../../04_architecture-repository/03_requirements/enf-2.md), [ENF-5: Coordination des processus complexes décentralisés et asynchrones](../../04_architecture-repository/03_requirements/enf-5.md)).

- **Rattachement** : [ART-5](../../04_architecture-repository/04_patterns/artsn-rules/art-5.md) (alertes), [ART-9](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md) (Grand Livre), [ABB-EXPOSITION-DONNEES-ANALYTIQUES: Accès et exposition des données analytiques](../../04_architecture-repository/05_building-blocks/abb/abb-exposition-donnees-analytiques.md), [ABB-AUDIT-PROVENANCE: Provenance, audit et traçabilité](../../04_architecture-repository/05_building-blocks/abb/abb-audit-provenance.md).
- **Processus soutenus** : [PRC-09: Remboursement et régulation des mécanismes](../../04_architecture-repository/02_architecture-elements/business/processes/prc-09.md) (remboursement), [PRC-05: Alerte, investigation et riposte](../../04_architecture-repository/02_architecture-elements/business/processes/prc-05.md) (alerte/riposte).
- **Statut : Stable.**

### Moteur de graphes & Référentiel spatio-temporel

**Contenu normatif.** Ce composant gère le graphe de relations entre entités (patients, structures, personnels, produits) et le référentiel spatio-temporel unifié (ART-4D). Il sert les requêtes de parcours, la détection de clusters épidémiques et l'analyse de réseaux.

**Discipline de mise en œuvre.** Il garantit la cohérence topologique du graphe national et la résilience spatiale ([ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../../04_architecture-repository/03_requirements/enf-4.md)). Toute requête de navigation relationnelle passe par ce composant.

- **Rattachement** : [ART-8B](../../04_architecture-repository/04_patterns/artsn-rules/art-8b.md) (graphe), [ART-4D](../../04_architecture-repository/04_patterns/artsn-rules/art-4d.md) (spatio-temporel), [ABB-ECHANGE-MEDIATION: Échange et médiation inter-systèmes](../../04_architecture-repository/05_building-blocks/abb/abb-echange-mediation.md), [COMP-HOMOLOGATION-INTEROPERABILITE: Conformité et tests d’interopérabilité](../../04_architecture-repository/06_governance/compliance/comp-homologation-interoperabilite.md).
- **Statut : Stable.**

### Intégration, Médiation, API Gateway, Broker & Registre schémas

**Contenu normatif.** Ce composant constitue le point d'entrée unique de la plateforme : API Gateway (contrats, throttling, authentification), message broker asynchrone (files d'attente, durabilité), registre de schémas (F.3 — versioning, compatibilité ascendante/descendante) et moteur de médiation sémantique ([ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md) transformation, normalisation, enrichissement).

**Discipline de mise en œuvre.** Il forme la bordure de la plateforme ; tout flux entrant ou sortant le traverse. Il garantit l'éradication des silos (F.3) et la conformité aux contrats ([ENF-1: Résilience à l'instabilité réseau](../../04_architecture-repository/03_requirements/enf-1.md), [ENF-3: Unicité de l'identité et résilience face à la fragmentation applicative](../../04_architecture-repository/03_requirements/enf-3.md)).

- **Rattachement** : [ART-1](../../04_architecture-repository/04_patterns/artsn-rules/art-1.md) (ingestion), [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md) (médiation), [F.3](../../04_architecture-repository/04_patterns/foundations/f-3.md) (schémas), [ABB-IDENTITE-BENEFICIAIRE: Résolution d’identité du bénéficiaire](../../04_architecture-repository/05_building-blocks/abb/abb-identite-beneficiaire.md), [ABB-ECHANGE-MEDIATION: Échange et médiation inter-systèmes](../../04_architecture-repository/05_building-blocks/abb/abb-echange-mediation.md).
- **Statut : Stable.**

### Orchestrateur de parcours & Gestionnaire de Sagas (ART-8A)

**Contenu normatif.** Ce composant orchestre les flux inter-systèmes en gérant les transactions distribuées (Sagas) et les compensations. Il garantit la cohérence des parcours patient à travers les institutions, les systèmes et les départements. Il assure la résilience des workflows cliniques critiques.

**Discipline de mise en œuvre.** Il est le point de coordination central de tous les flux transactionnels : toute opération multi-systèmes transite par cet orchestrateur. Il garantit l'atomicité logique des parcours complexes.

- **Rattachement** : [ART-8A](../../04_architecture-repository/04_patterns/artsn-rules/art-8a.md) (orchestrateur de parcours), [ABB-CONFIANCE-AUTORISATION: Confiance, sécurité et autorisation](../../04_architecture-repository/05_building-blocks/abb/abb-confiance-autorisation.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../04_architecture-repository/02_architecture-elements/business/processes/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../04_architecture-repository/02_architecture-elements/business/processes/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../../04_architecture-repository/02_architecture-elements/business/processes/prc-06.md) (logistique).
- **Statut : Stable.**

### Répertoire de données cliniques opérationnelles

**Contenu normatif.** Ce composant centralise les données cliniques opérationnelles (dossiers patients, épisodes de soins, actes médicaux). Il assure la persistance et la cohérence des données cliniques en temps réel, et fournit les API de lecture/écriture pour les applications métier.

**Discipline de mise en œuvre.** Il constitue la source de vérité clinique pour les applications opérationnelles. Toute donnée clinique créée ou modifiée dans les applications de point de service y est persistée.

- **Rattachement** : [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md) (référentiel des métadonnées), [ABB-GESTION-CONSENTEMENT: Gestion des consentements et bases d’autorisation](../../04_architecture-repository/05_building-blocks/abb/abb-gestion-consentement.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../04_architecture-repository/02_architecture-elements/business/processes/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../04_architecture-repository/02_architecture-elements/business/processes/prc-05.md) (pharmacie).
- **Statut : Stable.**

### Référentiel des métadonnées d'exploitation ([ART-4: Référentiels de métadonnées de gestion](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md))

**Contenu normatif.** Ce composant définit et gère les métadonnées d'exploitation : nomenclatures, codifications et standards de données. Il assure l'interopérabilité sémantique entre les systèmes et garantit l'utilisation cohérente des terminologies et classifications.

**Discipline de mise en œuvre.** Il est l'autorité sémantique de la plateforme. Toute définition de donnée clinique ou administrative passe par ce référentiel, ce qui garantit l'unicité des définitions à l'échelle nationale.

- **Rattachement** : [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md) (référentiel des métadonnées), [ABB-GESTION-CONSENTEMENT: Gestion des consentements et bases d’autorisation](../../04_architecture-repository/05_building-blocks/abb/abb-gestion-consentement.md).
- **Processus soutenus** : [PRC-07: Identification et droits des bénéficiaires](../../04_architecture-repository/02_architecture-elements/business/processes/prc-07.md) (production données), [PRC-08: Financement et exemption au point de service](../../04_architecture-repository/02_architecture-elements/business/processes/prc-08.md) (qualité).
- **Statut : Stable.**

### Registre des terminologies

**Contenu normatif.** Ce composant gère les terminologies médicales et de référence (CIM-11, SNOMED CT, LOINC, ATC, etc.). Il assure le mapping sémantique entre les systèmes et fournit les services de traduction et de validation des codages.

**Discipline de mise en œuvre.** Il sert de pont sémantique entre les systèmes hétérogènes. Il garantit que les données codées dans un système sont interprétables et exploitables par un autre.

- **Rattachement** : [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md) (référentiel des métadonnées), [ABB-GESTION-CONSENTEMENT: Gestion des consentements et bases d’autorisation](../../04_architecture-repository/05_building-blocks/abb/abb-gestion-consentement.md).
- **Processus soutenus** : [PRC-07: Identification et droits des bénéficiaires](../../04_architecture-repository/02_architecture-elements/business/processes/prc-07.md) (production données), [PRC-08: Financement et exemption au point de service](../../04_architecture-repository/02_architecture-elements/business/processes/prc-08.md) (qualité).
- **Statut : Stable.**

### Registre des clients / Index National des Patients (INP — ART-4A)

**Contenu normatif.** Ce composant gère l'identité unique des patients à l'échelle nationale. Il assure la déduplication et le matching des identités, et fournit les services de recherche et d'identification des patients.

**Discipline de mise en œuvre.** Il constitue l'identité nationale de référence pour tous les systèmes de santé. Toute identification patient transite par cet index, ce qui garantit l'unicité et la cohérence des identités.

- **Rattachement** : [ART-4A](../../04_architecture-repository/04_patterns/artsn-rules/art-4a.md) (INP), [ABB-GESTION-CONSENTEMENT: Gestion des consentements et bases d’autorisation](../../04_architecture-repository/05_building-blocks/abb/abb-gestion-consentement.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../04_architecture-repository/02_architecture-elements/business/processes/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../04_architecture-repository/02_architecture-elements/business/processes/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../../04_architecture-repository/02_architecture-elements/business/processes/prc-06.md) (logistique).
- **Statut : Stable.**

<!-- END:GENERATED -->
## Liens

- Paysage applicatif cible
- Services numériques partagés
- Flux de valeur

## Références

- [matrice de lecture](../reading-matrix.md)
- [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md)
- [PRC-01](../../04_architecture-repository/02_architecture-elements/business/processes/prc-01.md)
- [PRC-02](../../04_architecture-repository/02_architecture-elements/business/processes/prc-02.md)
- [PRC-03](../../04_architecture-repository/02_architecture-elements/business/processes/prc-03.md)
- [ABB-IDENTITE-BENEFICIAIRE](../../04_architecture-repository/05_building-blocks/abb/abb-identite-beneficiaire.md)
- [ABB-ECHANGE-MEDIATION](../../04_architecture-repository/05_building-blocks/abb/abb-echange-mediation.md)
- [ART-4A](../../04_architecture-repository/04_patterns/artsn-rules/art-4a.md)
- [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md)
- [fiche](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-01.md)
- [ART-1](../../04_architecture-repository/04_patterns/artsn-rules/art-1.md)
- [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md)
- [PRC-04](../../04_architecture-repository/02_architecture-elements/business/processes/prc-04.md)
- [ART-8D](../../04_architecture-repository/04_patterns/artsn-rules/art-8d.md)
- [PRC-05](../../04_architecture-repository/02_architecture-elements/business/processes/prc-05.md)
- [PRC-06](../../04_architecture-repository/02_architecture-elements/business/processes/prc-06.md)
- [ABB-EXPOSITION-DONNEES-ANALYTIQUES](../../04_architecture-repository/05_building-blocks/abb/abb-exposition-donnees-analytiques.md)
- [ART-0](../../04_architecture-repository/04_patterns/artsn-rules/art-0.md)
- [ABB-SERVICE-TERMINOLOGIE](../../04_architecture-repository/05_building-blocks/abb/abb-service-terminologie.md)
- [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md)
- [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md)
- [PRC-07](../../04_architecture-repository/02_architecture-elements/business/processes/prc-07.md)
- [PRC-08](../../04_architecture-repository/02_architecture-elements/business/processes/prc-08.md)
- [ABB-GESTION-CONSENTEMENT](../../04_architecture-repository/05_building-blocks/abb/abb-gestion-consentement.md)
- [ART-4C](../../04_architecture-repository/04_patterns/artsn-rules/art-4c.md)
- [PRC-09](../../04_architecture-repository/02_architecture-elements/business/processes/prc-09.md)
- [ABB-AUDIT-PROVENANCE](../../04_architecture-repository/05_building-blocks/abb/abb-audit-provenance.md)
- [ART-8C](../../04_architecture-repository/04_patterns/artsn-rules/art-8c.md)
- [ART-9](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md)
- [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)
- [ART-10](../../04_architecture-repository/04_patterns/artsn-rules/art-10.md)
- [PRC-10](../../04_architecture-repository/02_architecture-elements/business/processes/prc-10.md)
- [PRC-11](../../04_architecture-repository/02_architecture-elements/business/processes/prc-11.md)
- [ABB-REGISTRE-PROFESSIONNELS](../../04_architecture-repository/05_building-blocks/abb/abb-registre-professionnels.md)
- [PRC-12](../../04_architecture-repository/02_architecture-elements/business/processes/prc-12.md)
- [ABB-RECONCILIATION-DONNEES](../../04_architecture-repository/05_building-blocks/abb/abb-reconciliation-donnees.md)
- [ART-6](../../04_architecture-repository/04_patterns/artsn-rules/art-6.md)
- [ABB-CATALOGUE-CONTRATS](../../04_architecture-repository/05_building-blocks/abb/abb-catalogue-contrats.md)
- [COMP-HOMOLOGATION-INTEROPERABILITE](../../04_architecture-repository/06_governance/compliance/comp-homologation-interoperabilite.md)
- [Paysage applicatif cible](layers.md)
- [Services numériques partagés](shared-services.md)
- [Flux de valeur](../01_value-streams/index.md)
