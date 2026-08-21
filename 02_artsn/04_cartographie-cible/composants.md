---
title: Composants de la cartographie cible
id: artsn-cartographie-composants
domain: 04_cartographie-cible
version: "1.0.0"
status: draft
last_reviewed: 2026-08-21
owner: DEPSI
tags: ["artsn", "composants", "niveau-3"]
---

# Composants de la cartographie cible

Ce document agrege les monographies des composants reference par la cartographie conceptuelle cible.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Tableaux de bord & Portails nationaux

**Contenu normatif.** Ce composant agrège les projections analytiques (Couche 5) et expose des tableaux de bord unifiés pour le pilotage national : performance sanitaire, suivi CSU, gestion des ressources et veille environnementale. L'accès y est cloisonné par profil (décideurs, SIS, partenaires). Il interopère avec l'entrepôt Lakehouse ([CMP-03: Entrepôt Lakehouse & Projections analytiques (pipeline ETL, Lakehouse, projections)](../../referentiel/composants/cmp-03.md)) et le moteur analytique ([CMP-04: Moteur analytique & IA (IA prédictive, routeur alertes, Grand Livre)](../../referentiel/composants/cmp-04.md)).

**Discipline de mise en œuvre.** Il constitue la seule source de vérité décisionnelle pour l'État ; tout indicateur officiel y transite. Il garantit l'unicité des métriques et la traçabilité des calculs.

- **Rattachement** : [ART-6](../../referentiel/chapitres/art-6.md) (projections analytiques), [CAP-INT-07: Accès et exposition des données analytiques](../../referentiel/capacites/cap-int-07.md), [CAP-INT-11: Qualité et réconciliation](../../referentiel/capacites/cap-int-11.md).
- **Processus soutenus** : [PRC-10: Planification et allocation des ressources](../../referentiel/processus/prc-10.md) (planification), [PRC-11: Suivi et pilotage de la performance](../../referentiel/processus/prc-11.md) (pilotage performance), [PRC-12: Redevabilité et amélioration continue](../../referentiel/processus/prc-12.md) (redevabilité).
- **Statut : Stable.**

*Rattachement : PRC-10, PRC-11, PRC-12, CAP-INT-07, CAP-INT-11, ART-6 · fiche CMP-01*

### Centre de commande & Crises intersectorielles

**Contenu normatif.** Ce composant constitue le centre unique de supervision des alertes épidémiques et de coordination des crises intersectorielles (santé, élevage, environnement). Il agrège les signaux de la surveillance ([CMP-14: Registre des produits, intrants et indicateurs](../../referentiel/composants/cmp-14.md)), du moteur d'alertes ([CMP-04: Moteur analytique & IA (IA prédictive, routeur alertes, Grand Livre)](../../referentiel/composants/cmp-04.md)) et des registres de gouvernance ([CMP-17: Message broker asynchrone](../../referentiel/composants/cmp-17.md)), et fournit une vue en temps réel pour la prise de décision multi-ministérielle.

**Discipline de mise en œuvre.** Il est le point de convergence obligatoire de toute riposte coordonnée ; sans lui, les secteurs agissent en silos et la riposte reste fragmentée.

- **Rattachement** : [ART-5](../../referentiel/chapitres/art-5.md) (routeur alertes), [ART-0](../../referentiel/chapitres/art-0.md) (accords partage), [CAP-INT-07: Accès et exposition des données analytiques](../../referentiel/capacites/cap-int-07.md).
- **Processus soutenus** : [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (alerte/investigation/riposte), [PRC-11: Suivi et pilotage de la performance](../../referentiel/processus/prc-11.md) (pilotage performance).
- **Statut : Stable.**

*Rattachement : PRC-05, PRC-11, CAP-INT-07, ART-5, ART-0 · fiche CMP-02*

### Entrepôt Lakehouse & Projections analytiques

**Contenu normatif.** Ce composant assure le stockage analytique central (Lakehouse) en recevant les flux ETL depuis la Couche 4. Il exécute les projections tabulaires, la réconciliation du Grand Livre ([ART-9: Garanties transactionnelles fortes](../../referentiel/chapitres/art-9.md)) et alimente les tableaux de bord ([CMP-01: Tableaux de bord & Portails nationaux (performance, CSU, ressources, veille)](../../referentiel/composants/cmp-01.md)). La séparation stricte CQRS ([ART-6: Analytique et restitution](../../referentiel/chapitres/art-6.md)) interdit tout traitement transactionnel.

**Discipline de mise en œuvre.** Il garantit l'intégrité analytique ([ENF-5: Coordination des processus complexes décentralisés et asynchrones](../../referentiel/exigences/enf-5.md)) et l'irréversibilité du masquage des identités. Toute analyse officielle passe par cet entrepôt.

- **Rattachement** : [ART-6](../../referentiel/chapitres/art-6.md) (CQRS), [ART-9](../../referentiel/chapitres/art-9.md) (Grand Livre), [CAP-INT-07: Accès et exposition des données analytiques](../../referentiel/capacites/cap-int-07.md), [CAP-INT-11: Qualité et réconciliation](../../referentiel/capacites/cap-int-11.md).
- **Processus soutenus** : [PRC-09: Remboursement et régulation des mécanismes](../../referentiel/processus/prc-09.md) (remboursement), [PRC-11: Suivi et pilotage de la performance](../../referentiel/processus/prc-11.md) (pilotage).
- **Statut : Stable.**

*Rattachement : PRC-09, PRC-11, CAP-INT-07, CAP-INT-11, ART-6, ART-9 · fiche CMP-03*

### Moteur analytique & IA

**Contenu normatif.** Ce composant exécute les modèles prédictifs (IA), le routeur d'escalade et d'alertes ([ART-5: Cohérence et qualité des données](../../referentiel/chapitres/art-5.md)) et la réconciliation analytique du Grand Livre ([ART-9: Garanties transactionnelles fortes](../../referentiel/chapitres/art-9.md)). Il consomme l'entrepôt Lakehouse ([CMP-03: Entrepôt Lakehouse & Projections analytiques (pipeline ETL, Lakehouse, projections)](../../referentiel/composants/cmp-03.md)) et alimente le centre de commande ([CMP-02: Centre de commande & Crises intersectorielles (alertes, crises, veille)](../../referentiel/composants/cmp-02.md)) ainsi que la facturation ([CMP-10: Registre des terminologies](../../referentiel/composants/cmp-10.md)).

**Discipline de mise en œuvre.** Il sépare l'inférence analytique du stockage et garantit la traçabilité des modèles (versionnage, données d'entraînement) ainsi que l'audit des décisions automatisées ([ENF-2: Intégrité des flux et traçabilité des valeurs](../../referentiel/exigences/enf-2.md), [ENF-5: Coordination des processus complexes décentralisés et asynchrones](../../referentiel/exigences/enf-5.md)).

- **Rattachement** : [ART-5](../../referentiel/chapitres/art-5.md) (alertes), [ART-9](../../referentiel/chapitres/art-9.md) (Grand Livre), [CAP-INT-07: Accès et exposition des données analytiques](../../referentiel/capacites/cap-int-07.md), [CAP-INT-10: Provenance, audit et traçabilité](../../referentiel/capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-09: Remboursement et régulation des mécanismes](../../referentiel/processus/prc-09.md) (remboursement), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (alerte/riposte).
- **Statut : Stable.**

*Rattachement : PRC-09, PRC-05, CAP-INT-07, CAP-INT-10, ART-5, ART-9 · fiche CMP-04*

### Moteur de graphes & Référentiel spatio-temporel

**Contenu normatif.** Ce composant gère le graphe de relations entre entités (patients, structures, personnels, produits) et le référentiel spatio-temporel unifié (ART-4d). Il sert les requêtes de parcours, la détection de clusters épidémiques et l'analyse de réseaux.

**Discipline de mise en œuvre.** Il garantit la cohérence topologique du graphe national et la résilience spatiale ([ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../../referentiel/exigences/enf-4.md)). Toute requête de navigation relationnelle passe par ce composant.

- **Rattachement** : [ART-8b](../../referentiel/chapitres/art-8b.md) (graphe), [ART-4d](../../referentiel/chapitres/art-4d.md) (spatio-temporel), [CAP-INT-03: Échange et médiation inter-systèmes](../../referentiel/capacites/cap-int-03.md), [CAP-INT-12: Conformité et tests d’interopérabilité](../../referentiel/capacites/cap-int-12.md).
- **Statut : Stable.**

*Rattachement : CAP-INT-03, CAP-INT-12, ART-8B, ART-4D · fiche CMP-05*

### Intégration, Médiation, API Gateway, Broker & Registre schémas

**Contenu normatif.** Ce composant constitue le point d'entrée unique de la plateforme : API Gateway (contrats, throttling, authentification), message broker asynchrone (files d'attente, durabilité), registre de schémas (F.3 — versioning, compatibilité ascendante/descendante) et moteur de médiation sémantique ([ART-2](../../referentiel/chapitres/art-2.md) transformation, normalisation, enrichissement).

**Discipline de mise en œuvre.** Il forme la bordure de la plateforme ; tout flux entrant ou sortant le traverse. Il garantit l'éradication des silos (F.3) et la conformité aux contrats ([ENF-1: Résilience à l'instabilité réseau](../../referentiel/exigences/enf-1.md), [ENF-3: Unicité de l'identité et résilience face à la fragmentation applicative](../../referentiel/exigences/enf-3.md)).

- **Rattachement** : [ART-1](../../referentiel/chapitres/art-1.md) (ingestion), [ART-2](../../referentiel/chapitres/art-2.md) (médiation), [F.3](../../referentiel/fondations/f-3.md) (schémas), [CAP-INT-01: Résolution d’identité du bénéficiaire](../../referentiel/capacites/cap-int-01.md), [CAP-INT-03: Échange et médiation inter-systèmes](../../referentiel/capacites/cap-int-03.md).
- **Statut : Stable.**

*Rattachement : CAP-INT-01, CAP-INT-03, ART-1, ART-2, F-3 · fiche CMP-06*

### Orchestrateur de parcours & Gestionnaire de Sagas (ART-8a)

**Contenu normatif.** Ce composant orchestre les flux inter-systèmes en gérant les transactions distribuées (Sagas) et les compensations. Il garantit la cohérence des parcours patient à travers les institutions, les systèmes et les départements. Il assure la résilience des workflows cliniques critiques.

**Discipline de mise en œuvre.** Il est le point de coordination central de tous les flux transactionnels : toute opération multi-systèmes transite par cet orchestrateur. Il garantit l'atomicité logique des parcours complexes.

- **Rattachement** : [ART-8a](../../referentiel/chapitres/art-8a.md) (orchestrateur de parcours), [CAP-INT-08: Confiance, sécurité et autorisation](../../referentiel/capacites/cap-int-08.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../referentiel/processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../../referentiel/processus/prc-06.md) (logistique).
- **Statut : Stable.**

*Rattachement : PRC-04, PRC-05, PRC-06, CAP-INT-08, ART-8A · fiche CMP-07*

### Répertoire de données cliniques opérationnelles

**Contenu normatif.** Ce composant centralise les données cliniques opérationnelles (dossiers patients, épisodes de soins, actes médicaux). Il assure la persistance et la cohérence des données cliniques en temps réel, et fournit les API de lecture/écriture pour les applications métier.

**Discipline de mise en œuvre.** Il constitue la source de vérité clinique pour les applications opérationnelles. Toute donnée clinique créée ou modifiée dans les applications de point de service y est persistée.

- **Rattachement** : [ART-4](../../referentiel/chapitres/art-4.md) (référentiel des métadonnées), [CAP-INT-09: Gestion des consentements et bases d’autorisation](../../referentiel/capacites/cap-int-09.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../referentiel/processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (pharmacie).
- **Statut : Stable.**

*Rattachement : PRC-04, PRC-05, CAP-INT-09, ART-4 · fiche CMP-08*

### Référentiel des métadonnées d'exploitation ([ART-4: Référentiels de métadonnées de gestion](../../referentiel/chapitres/art-4.md))

**Contenu normatif.** Ce composant définit et gère les métadonnées d'exploitation : nomenclatures, codifications et standards de données. Il assure l'interopérabilité sémantique entre les systèmes et garantit l'utilisation cohérente des terminologies et classifications.

**Discipline de mise en œuvre.** Il est l'autorité sémantique de la plateforme. Toute définition de donnée clinique ou administrative passe par ce référentiel, ce qui garantit l'unicité des définitions à l'échelle nationale.

- **Rattachement** : [ART-4](../../referentiel/chapitres/art-4.md) (référentiel des métadonnées), [CAP-INT-09: Gestion des consentements et bases d’autorisation](../../referentiel/capacites/cap-int-09.md).
- **Processus soutenus** : [PRC-07: Identification et droits des bénéficiaires](../../referentiel/processus/prc-07.md) (production données), [PRC-08: Financement et exemption au point de service](../../referentiel/processus/prc-08.md) (qualité).
- **Statut : Stable.**

*Rattachement : PRC-07, PRC-08, CAP-INT-09, ART-4 · fiche CMP-09*

### Registre des terminologies

**Contenu normatif.** Ce composant gère les terminologies médicales et de référence (CIM-10, SNOMED CT, LOINC, ATC, etc.). Il assure le mapping sémantique entre les systèmes et fournit les services de traduction et de validation des codages.

**Discipline de mise en œuvre.** Il sert de pont sémantique entre les systèmes hétérogènes. Il garantit que les données codées dans un système sont interprétables et exploitables par un autre.

- **Rattachement** : [ART-4](../../referentiel/chapitres/art-4.md) (référentiel des métadonnées), [CAP-INT-09: Gestion des consentements et bases d’autorisation](../../referentiel/capacites/cap-int-09.md).
- **Processus soutenus** : [PRC-07: Identification et droits des bénéficiaires](../../referentiel/processus/prc-07.md) (production données), [PRC-08: Financement et exemption au point de service](../../referentiel/processus/prc-08.md) (qualité).
- **Statut : Stable.**

*Rattachement : PRC-07, PRC-08, CAP-INT-09, ART-4 · fiche CMP-10*

### Registre des clients / Index National des Patients (INP — ART-4a)

**Contenu normatif.** Ce composant gère l'identité unique des patients à l'échelle nationale. Il assure la déduplication et le matching des identités, et fournit les services de recherche et d'identification des patients.

**Discipline de mise en œuvre.** Il constitue l'identité nationale de référence pour tous les systèmes de santé. Toute identification patient transite par cet index, ce qui garantit l'unicité et la cohérence des identités.

- **Rattachement** : [ART-4a](../../referentiel/chapitres/art-4a.md) (INP), [CAP-INT-09: Gestion des consentements et bases d’autorisation](../../referentiel/capacites/cap-int-09.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../referentiel/processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../../referentiel/processus/prc-06.md) (logistique).
- **Statut : Stable.**

*Rattachement : PRC-04, PRC-05, PRC-06, CAP-INT-09, ART-4A · fiche CMP-11*

### Registre d'éligibilité et de couverture (CSU — ART-4c)

**Contenu normatif.** Ce composant gère les données d'éligibilité et de couverture santé (CSU). Il assure la vérification en temps réel des droits des patients et fournit les services de contrôle d'éligibilité pour les applications métier.

**Discipline de mise en œuvre.** Il est l'autorité de vérification des droits. Toute opération de soins nécessitant une vérification de couverture transite par ce registre, ce qui garantit la conformité financière.

- **Rattachement** : [ART-4c](../../referentiel/chapitres/art-4c.md) (éligibilité/couverture), [CAP-INT-09: Gestion des consentements et bases d’autorisation](../../referentiel/capacites/cap-int-09.md).
- **Processus soutenus** : [PRC-09: Remboursement et régulation des mécanismes](../../referentiel/processus/prc-09.md) (finance), [PRC-10: Planification et allocation des ressources](../../referentiel/processus/prc-10.md) (planification).
- **Statut : Stable.**

*Rattachement : PRC-09, PRC-10, CAP-INT-09, ART-4C · fiche CMP-12*

### Registre des personnels

**Contenu normatif.** Ce composant gère les données des personnels de santé (identités, qualifications, affectations). Il assure la traçabilité des interventions et des responsabilités, et fournit les services de recherche et d'identification des personnels.

**Discipline de mise en œuvre.** Il constitue le référentiel de référence pour l'identification des intervenants. Toute intervention médicale enregistre l'identité du personnel via ce registre, ce qui garantit la traçabilité et la responsabilité.

- **Rattachement** : [ART-4](../../referentiel/chapitres/art-4.md) (référentiel des métadonnées), [CAP-INT-09: Gestion des consentements et bases d’autorisation](../../referentiel/capacites/cap-int-09.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../referentiel/processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (pharmacie).
- **Statut : Stable.**

*Rattachement : PRC-04, PRC-05, CAP-INT-09, ART-4 · fiche CMP-13*

### Registre des produits, intrants et indicateurs

**Contenu normatif.** Ce composant gère les référentiels de produits, d'intrants et d'indicateurs. Il assure la cohérence des nomenclatures de produits et la standardisation des indicateurs, et fournit les services de recherche et de validation.

**Discipline de mise en œuvre.** Il est l'autorité de référence pour les produits et indicateurs. Toute définition de produit ou d'indicateur passe par ce registre, ce qui garantit l'unicité et la cohérence des référentiels.

- **Rattachement** : [ART-4](../../referentiel/chapitres/art-4.md) (référentiel des métadonnées), [CAP-INT-09: Gestion des consentements et bases d’autorisation](../../referentiel/capacites/cap-int-09.md).
- **Processus soutenus** : [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../../referentiel/processus/prc-06.md) (logistique).
- **Statut : Stable.**

*Rattachement : PRC-05, PRC-06, CAP-INT-09, ART-4 · fiche CMP-14*

### API Gateway

**Contenu normatif.** Ce composant constitue le point d'entrée unique pour toutes les requêtes API. Il assure la gestion des flux, l'authentification, la limitation de débit et le routage, et garantit la sécurité et la performance des échanges inter-systèmes.

**Discipline de mise en œuvre.** Il est le gardien de la plateforme. Toute requête externe ou inter-systèmes transite par ce point, ce qui garantit la sécurité, la disponibilité et la conformité des échanges.

- **Rattachement** : [ART-5](../../referentiel/chapitres/art-5.md) (routeur d'escalade), [CAP-INT-10: Provenance, audit et traçabilité](../../referentiel/capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../referentiel/processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../../referentiel/processus/prc-06.md) (logistique).
- **Statut : Stable.**

*Rattachement : PRC-04, PRC-05, PRC-06, CAP-INT-10, ART-5 · fiche CMP-15*

### Registre de schémas (F.3)

**Contenu normatif.** Ce composant gère les schémas de données et les contrats d'API. Il assure la validation des messages et la conformité des échanges, et fournit les services de découverte et de versioning des schémas.

**Discipline de mise en œuvre.** Il est l'autorité de validation des échanges. Toute donnée échangée doit être conforme aux schémas définis ici, ce qui garantit l'intégrité et la cohérence des données.

- **Rattachement** : [ART-5](../../referentiel/chapitres/art-5.md) (routeur d'escalade), [CAP-INT-10: Provenance, audit et traçabilité](../../referentiel/capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-07: Identification et droits des bénéficiaires](../../referentiel/processus/prc-07.md) (production données), [PRC-08: Financement et exemption au point de service](../../referentiel/processus/prc-08.md) (qualité).
- **Statut : Stable.**

*Rattachement : PRC-07, PRC-08, CAP-INT-10, ART-5 · fiche CMP-16*

### Message broker asynchrone

**Contenu normatif.** Ce composant gère les échanges asynchrones entre les systèmes. Il assure la persistance tampon et la distribution des messages, et garantit la résilience et la fiabilité des communications inter-systèmes.

**Discipline de mise en œuvre.** Il est le mécanisme de déconnexion des systèmes. Il permet la communication même en cas de défaillance temporaire d'un composant, ce qui garantit la continuité des échanges.

- **Rattachement** : [ART-5](../../referentiel/chapitres/art-5.md) (routeur d'escalade), [CAP-INT-10: Provenance, audit et traçabilité](../../referentiel/capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../referentiel/processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../../referentiel/processus/prc-06.md) (logistique).
- **Statut : Stable.**

*Rattachement : PRC-04, PRC-05, PRC-06, CAP-INT-10, ART-5 · fiche CMP-17*

### Compensateur / Regroupeur de flux (Netting — ART-8c)

**Contenu normatif.** Ce composant gère les compensations et le regroupement des flux. Il assure la cohérence des transactions distribuées et la résolution des anomalies, et garantit l'intégrité des échanges complexes.

**Discipline de mise en œuvre.** Il est le mécanisme de résolution des anomalies. Il permet la compensation automatique des erreurs et la cohérence des transactions, ce qui garantit la fiabilité des échanges critiques.

- **Rattachement** : [ART-8c](../../referentiel/chapitres/art-8c.md) (Netting), [CAP-INT-10: Provenance, audit et traçabilité](../../referentiel/capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../referentiel/processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../../referentiel/processus/prc-06.md) (logistique).
- **Statut : Stable.**

*Rattachement : PRC-04, PRC-05, PRC-06, CAP-INT-10, ART-8C · fiche CMP-18*

### CMP-19 : Dossiers & statistiques de sante (hopitaux)

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ENF-1, F.1 · fiche CMP-19*

### CMP-20 : Gestion des pharmacies (PMIS)

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ENF-1, F.1 · fiche CMP-20*

### CMP-21 : Sante communautaire mobile (offline)

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ENF-1, F.1 · fiche CMP-21*

### CMP-22 : Espace sante patient

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ENF-1, F.1 · fiche CMP-22*

### CMP-23 : Chaine logistique (LMIS)

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ENF-1, F.1 · fiche CMP-23*

### CMP-24 : Surveillance de la sante animale (zoonoses)

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ENF-1, F.1 · fiche CMP-24*

### CMP-25 : Enquetes & capteurs terrain

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ENF-1, F.1 · fiche CMP-25*

### CMP-26 : Noeud central (datacenters nationaux HDS)

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-7 · fiche CMP-26*

### CMP-27 : Noeuds regionaux (clusters de district : Fog)

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-7 · fiche CMP-27*

### CMP-28 : Noeuds locaux (equipements chiffres : Edge)

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-7 · fiche CMP-28*

### CMP-29 : Liaisons dediees & VPN

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-7 · fiche CMP-29*

### CMP-30 : Reseau prive MPLS

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-7 · fiche CMP-30*

### CMP-31 : Reseaux mobiles prives (APN securises)

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-7 · fiche CMP-31*

### CMP-32 : Gestion des identites

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-7 · fiche CMP-32*

### CMP-33 : Controle d'acces fin (RBAC/ABAC)

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-7 · fiche CMP-33*

### CMP-34 : Gestion des consentements

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-7 · fiche CMP-34*

### CMP-35 : Infrastructure de cles publiques (PKI)

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-7 · fiche CMP-35*

### CMP-36 : Passerelle de confiance mondiale OMS (GDHCN)

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-7 · fiche CMP-36*

### CMP-37 : Journal d'audit immuable

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-7 · fiche CMP-37*

### CMP-38 : Moteur de chiffrement

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-7 · fiche CMP-38*

### CMP-39 : Registre des accords inter-institutions

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-0, F.4 · fiche CMP-39*

### CMP-40 : Charte nationale de protection

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-0, F.4 · fiche CMP-40*

### CMP-41 : Conventions internationales

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-0, F.4 · fiche CMP-41*

### CMP-42 : Comite national d'homologation

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-0, F.4 · fiche CMP-42*

### CMP-43 : Registre des initiatives

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-0, F.4 · fiche CMP-43*

### CMP-44 : Comite d'ethique

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-0, F.4 · fiche CMP-44*

### CMP-45 : Cellule d'audit

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-0, F.4 · fiche CMP-45*

### CMP-46 : Arbitrage et risques

#### Contenu normatif.

(A completer : decrire le contenu normatif et la discipline de mise en oeuvre de ce composant.)

*Rattachement : ART-0, F.4 · fiche CMP-46*

<!-- END:GENERATED -->
