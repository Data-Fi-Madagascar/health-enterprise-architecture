---
title: Composants de la cartographie cible
id: artsn-cartographie-composants
domain: 05_cartographie
version: "1.0.0"
status: draft
last_reviewed: 2026-08-21
owner: DEPSI
tags: ["artsn", "composants", "niveau-3"]
related: ["CAP-INT-10", "ART-8C", "PRC-04", "PRC-05", "PRC-06"]
---

# Composants de la cartographie cible

Ce document agrege les monographies des composants reference par la cartographie conceptuelle cible. Les composants sont regroupes par sous-couche ArchiMate : applicatif (couches 2 a 6), infrastructure (couche 1), securite et gouvernance.

## Composants applicatifs (couches 2 a 6)

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/composants/cmp-01.md,referentiel/composants/cmp-02.md,referentiel/composants/cmp-03.md,referentiel/composants/cmp-04.md,referentiel/composants/cmp-05.md,referentiel/composants/cmp-06.md,referentiel/composants/cmp-07.md,referentiel/composants/cmp-08.md,referentiel/composants/cmp-09.md,referentiel/composants/cmp-10.md,referentiel/composants/cmp-11.md,referentiel/composants/cmp-12.md,referentiel/composants/cmp-13.md,referentiel/composants/cmp-14.md,referentiel/composants/cmp-15.md,referentiel/composants/cmp-16.md,referentiel/composants/cmp-17.md,referentiel/composants/cmp-18.md,referentiel/composants/cmp-19.md,referentiel/composants/cmp-20.md,referentiel/composants/cmp-21.md,referentiel/composants/cmp-22.md,referentiel/composants/cmp-23.md,referentiel/composants/cmp-24.md,referentiel/composants/cmp-25.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Tableaux de bord & Portails nationaux

**Contenu normatif.** Ce composant agrège les projections analytiques (Couche 5) et expose des tableaux de bord unifiés pour le pilotage national : performance sanitaire, suivi CSU, gestion des ressources et veille environnementale. L'accès y est cloisonné par profil (décideurs, SIS, partenaires). Il interopère avec l'entrepôt Lakehouse ([CMP-03: Entrepôt Lakehouse & Projections analytiques (pipeline ETL, Lakehouse, projections)](../../referentiel/composants/cmp-03.md)) et le moteur analytique ([CMP-04: Moteur analytique & IA (IA prédictive, routeur alertes, Grand Livre)](../../referentiel/composants/cmp-04.md)).

**Discipline de mise en œuvre.** Il constitue la seule source de vérité décisionnelle pour l'État ; tout indicateur officiel y transite. Il garantit l'unicité des métriques et la traçabilité des calculs.

- **Rattachement** : [ART-6](../../referentiel/chapitres/art-6.md) (projections analytiques), [CAP-INT-07: Accès et exposition des données analytiques](../../referentiel/capacites/cap-int-07.md), [CAP-INT-11: Qualité et réconciliation](../../referentiel/capacites/cap-int-11.md).
- **Processus soutenus** : [PRC-10: Planification et allocation des ressources](../../referentiel/processus/prc-10.md) (planification), [PRC-11: Suivi et pilotage de la performance](../../referentiel/processus/prc-11.md) (pilotage performance), [PRC-12: Redevabilité et amélioration continue](../../referentiel/processus/prc-12.md) (redevabilité).
- **Statut : Stable.**

### Centre de commande & Crises intersectorielles

**Contenu normatif.** Ce composant constitue le centre unique de supervision des alertes épidémiques et de coordination des crises intersectorielles (santé, élevage, environnement). Il agrège les signaux de la surveillance ([CMP-14: Registre des produits, intrants et indicateurs](../../referentiel/composants/cmp-14.md)), du moteur d'alertes ([CMP-04: Moteur analytique & IA (IA prédictive, routeur alertes, Grand Livre)](../../referentiel/composants/cmp-04.md)) et des registres de gouvernance ([CMP-17: Message broker asynchrone](../../referentiel/composants/cmp-17.md)), et fournit une vue en temps réel pour la prise de décision multi-ministérielle.

**Discipline de mise en œuvre.** Il est le point de convergence obligatoire de toute riposte coordonnée ; sans lui, les secteurs agissent en silos et la riposte reste fragmentée.

- **Rattachement** : [ART-5](../../referentiel/chapitres/art-5.md) (routeur alertes), [ART-0](../../referentiel/chapitres/art-0.md) (accords partage), [CAP-INT-07: Accès et exposition des données analytiques](../../referentiel/capacites/cap-int-07.md).
- **Processus soutenus** : [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (alerte/investigation/riposte), [PRC-11: Suivi et pilotage de la performance](../../referentiel/processus/prc-11.md) (pilotage performance).
- **Statut : Stable.**

### Entrepôt Lakehouse & Projections analytiques

**Contenu normatif.** Ce composant assure le stockage analytique central (Lakehouse) en recevant les flux ETL depuis la Couche 4. Il exécute les projections tabulaires, la réconciliation du Grand Livre ([ART-9: Garanties transactionnelles fortes](../../referentiel/chapitres/art-9.md)) et alimente les tableaux de bord ([CMP-01: Tableaux de bord & Portails nationaux (performance, CSU, ressources, veille)](../../referentiel/composants/cmp-01.md)). La séparation stricte CQRS ([ART-6: Analytique et restitution](../../referentiel/chapitres/art-6.md)) interdit tout traitement transactionnel.

**Discipline de mise en œuvre.** Il garantit l'intégrité analytique ([ENF-5: Coordination des processus complexes décentralisés et asynchrones](../../referentiel/exigences/enf-5.md)) et l'irréversibilité du masquage des identités. Toute analyse officielle passe par cet entrepôt.

- **Rattachement** : [ART-6](../../referentiel/chapitres/art-6.md) (CQRS), [ART-9](../../referentiel/chapitres/art-9.md) (Grand Livre), [CAP-INT-07: Accès et exposition des données analytiques](../../referentiel/capacites/cap-int-07.md), [CAP-INT-11: Qualité et réconciliation](../../referentiel/capacites/cap-int-11.md).
- **Processus soutenus** : [PRC-09: Remboursement et régulation des mécanismes](../../referentiel/processus/prc-09.md) (remboursement), [PRC-11: Suivi et pilotage de la performance](../../referentiel/processus/prc-11.md) (pilotage).
- **Statut : Stable.**

### Moteur analytique & IA

**Contenu normatif.** Ce composant exécute les modèles prédictifs (IA), le routeur d'escalade et d'alertes ([ART-5: Cohérence et qualité des données](../../referentiel/chapitres/art-5.md)) et la réconciliation analytique du Grand Livre ([ART-9: Garanties transactionnelles fortes](../../referentiel/chapitres/art-9.md)). Il consomme l'entrepôt Lakehouse ([CMP-03: Entrepôt Lakehouse & Projections analytiques (pipeline ETL, Lakehouse, projections)](../../referentiel/composants/cmp-03.md)) et alimente le centre de commande ([CMP-02: Centre de commande & Crises intersectorielles (alertes, crises, veille)](../../referentiel/composants/cmp-02.md)) ainsi que la facturation ([CMP-10: Registre des terminologies](../../referentiel/composants/cmp-10.md)).

**Discipline de mise en œuvre.** Il sépare l'inférence analytique du stockage et garantit la traçabilité des modèles (versionnage, données d'entraînement) ainsi que l'audit des décisions automatisées ([ENF-2: Intégrité des flux et traçabilité des valeurs](../../referentiel/exigences/enf-2.md), [ENF-5: Coordination des processus complexes décentralisés et asynchrones](../../referentiel/exigences/enf-5.md)).

- **Rattachement** : [ART-5](../../referentiel/chapitres/art-5.md) (alertes), [ART-9](../../referentiel/chapitres/art-9.md) (Grand Livre), [CAP-INT-07: Accès et exposition des données analytiques](../../referentiel/capacites/cap-int-07.md), [CAP-INT-10: Provenance, audit et traçabilité](../../referentiel/capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-09: Remboursement et régulation des mécanismes](../../referentiel/processus/prc-09.md) (remboursement), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (alerte/riposte).
- **Statut : Stable.**

### Moteur de graphes & Référentiel spatio-temporel

**Contenu normatif.** Ce composant gère le graphe de relations entre entités (patients, structures, personnels, produits) et le référentiel spatio-temporel unifié (ART-4D). Il sert les requêtes de parcours, la détection de clusters épidémiques et l'analyse de réseaux.

**Discipline de mise en œuvre.** Il garantit la cohérence topologique du graphe national et la résilience spatiale ([ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../../referentiel/exigences/enf-4.md)). Toute requête de navigation relationnelle passe par ce composant.

- **Rattachement** : [ART-8B](../../referentiel/chapitres/art-8b.md) (graphe), [ART-4D](../../referentiel/chapitres/art-4d.md) (spatio-temporel), [CAP-INT-03: Échange et médiation inter-systèmes](../../referentiel/capacites/cap-int-03.md), [CAP-INT-12: Conformité et tests d’interopérabilité](../../referentiel/capacites/cap-int-12.md).
- **Statut : Stable.**

### Intégration, Médiation, API Gateway, Broker & Registre schémas

**Contenu normatif.** Ce composant constitue le point d'entrée unique de la plateforme : API Gateway (contrats, throttling, authentification), message broker asynchrone (files d'attente, durabilité), registre de schémas (F.3 — versioning, compatibilité ascendante/descendante) et moteur de médiation sémantique ([ART-2](../../referentiel/chapitres/art-2.md) transformation, normalisation, enrichissement).

**Discipline de mise en œuvre.** Il forme la bordure de la plateforme ; tout flux entrant ou sortant le traverse. Il garantit l'éradication des silos (F.3) et la conformité aux contrats ([ENF-1: Résilience à l'instabilité réseau](../../referentiel/exigences/enf-1.md), [ENF-3: Unicité de l'identité et résilience face à la fragmentation applicative](../../referentiel/exigences/enf-3.md)).

- **Rattachement** : [ART-1](../../referentiel/chapitres/art-1.md) (ingestion), [ART-2](../../referentiel/chapitres/art-2.md) (médiation), [F.3](../../referentiel/fondations/f-3.md) (schémas), [CAP-INT-01: Résolution d’identité du bénéficiaire](../../referentiel/capacites/cap-int-01.md), [CAP-INT-03: Échange et médiation inter-systèmes](../../referentiel/capacites/cap-int-03.md).
- **Statut : Stable.**

### Orchestrateur de parcours & Gestionnaire de Sagas (ART-8A)

**Contenu normatif.** Ce composant orchestre les flux inter-systèmes en gérant les transactions distribuées (Sagas) et les compensations. Il garantit la cohérence des parcours patient à travers les institutions, les systèmes et les départements. Il assure la résilience des workflows cliniques critiques.

**Discipline de mise en œuvre.** Il est le point de coordination central de tous les flux transactionnels : toute opération multi-systèmes transite par cet orchestrateur. Il garantit l'atomicité logique des parcours complexes.

- **Rattachement** : [ART-8A](../../referentiel/chapitres/art-8a.md) (orchestrateur de parcours), [CAP-INT-08: Confiance, sécurité et autorisation](../../referentiel/capacites/cap-int-08.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../referentiel/processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../../referentiel/processus/prc-06.md) (logistique).
- **Statut : Stable.**

### Répertoire de données cliniques opérationnelles

**Contenu normatif.** Ce composant centralise les données cliniques opérationnelles (dossiers patients, épisodes de soins, actes médicaux). Il assure la persistance et la cohérence des données cliniques en temps réel, et fournit les API de lecture/écriture pour les applications métier.

**Discipline de mise en œuvre.** Il constitue la source de vérité clinique pour les applications opérationnelles. Toute donnée clinique créée ou modifiée dans les applications de point de service y est persistée.

- **Rattachement** : [ART-4](../../referentiel/chapitres/art-4.md) (référentiel des métadonnées), [CAP-INT-09: Gestion des consentements et bases d’autorisation](../../referentiel/capacites/cap-int-09.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../referentiel/processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (pharmacie).
- **Statut : Stable.**

### Référentiel des métadonnées d'exploitation ([ART-4: Référentiels de métadonnées de gestion](../../referentiel/chapitres/art-4.md))

**Contenu normatif.** Ce composant définit et gère les métadonnées d'exploitation : nomenclatures, codifications et standards de données. Il assure l'interopérabilité sémantique entre les systèmes et garantit l'utilisation cohérente des terminologies et classifications.

**Discipline de mise en œuvre.** Il est l'autorité sémantique de la plateforme. Toute définition de donnée clinique ou administrative passe par ce référentiel, ce qui garantit l'unicité des définitions à l'échelle nationale.

- **Rattachement** : [ART-4](../../referentiel/chapitres/art-4.md) (référentiel des métadonnées), [CAP-INT-09: Gestion des consentements et bases d’autorisation](../../referentiel/capacites/cap-int-09.md).
- **Processus soutenus** : [PRC-07: Identification et droits des bénéficiaires](../../referentiel/processus/prc-07.md) (production données), [PRC-08: Financement et exemption au point de service](../../referentiel/processus/prc-08.md) (qualité).
- **Statut : Stable.**

### Registre des terminologies

**Contenu normatif.** Ce composant gère les terminologies médicales et de référence (CIM-11, SNOMED CT, LOINC, ATC, etc.). Il assure le mapping sémantique entre les systèmes et fournit les services de traduction et de validation des codages.

**Discipline de mise en œuvre.** Il sert de pont sémantique entre les systèmes hétérogènes. Il garantit que les données codées dans un système sont interprétables et exploitables par un autre.

- **Rattachement** : [ART-4](../../referentiel/chapitres/art-4.md) (référentiel des métadonnées), [CAP-INT-09: Gestion des consentements et bases d’autorisation](../../referentiel/capacites/cap-int-09.md).
- **Processus soutenus** : [PRC-07: Identification et droits des bénéficiaires](../../referentiel/processus/prc-07.md) (production données), [PRC-08: Financement et exemption au point de service](../../referentiel/processus/prc-08.md) (qualité).
- **Statut : Stable.**

### Registre des clients / Index National des Patients (INP — ART-4A)

**Contenu normatif.** Ce composant gère l'identité unique des patients à l'échelle nationale. Il assure la déduplication et le matching des identités, et fournit les services de recherche et d'identification des patients.

**Discipline de mise en œuvre.** Il constitue l'identité nationale de référence pour tous les systèmes de santé. Toute identification patient transite par cet index, ce qui garantit l'unicité et la cohérence des identités.

- **Rattachement** : [ART-4A](../../referentiel/chapitres/art-4a.md) (INP), [CAP-INT-09: Gestion des consentements et bases d’autorisation](../../referentiel/capacites/cap-int-09.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../referentiel/processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../../referentiel/processus/prc-06.md) (logistique).
- **Statut : Stable.**

### Registre d'éligibilité et de couverture (CSU — ART-4C)

**Contenu normatif.** Ce composant gère les données d'éligibilité et de couverture santé (CSU). Il assure la vérification en temps réel des droits des patients et fournit les services de contrôle d'éligibilité pour les applications métier.

**Discipline de mise en œuvre.** Il est l'autorité de vérification des droits. Toute opération de soins nécessitant une vérification de couverture transite par ce registre, ce qui garantit la conformité financière.

- **Rattachement** : [ART-4C](../../referentiel/chapitres/art-4c.md) (éligibilité/couverture), [CAP-INT-09: Gestion des consentements et bases d’autorisation](../../referentiel/capacites/cap-int-09.md).
- **Processus soutenus** : [PRC-09: Remboursement et régulation des mécanismes](../../referentiel/processus/prc-09.md) (finance), [PRC-10: Planification et allocation des ressources](../../referentiel/processus/prc-10.md) (planification).
- **Statut : Stable.**

### Registre des personnels

**Contenu normatif.** Ce composant gère les données des personnels de santé (identités, qualifications, affectations). Il assure la traçabilité des interventions et des responsabilités, et fournit les services de recherche et d'identification des personnels.

**Discipline de mise en œuvre.** Il constitue le référentiel de référence pour l'identification des intervenants. Toute intervention médicale enregistre l'identité du personnel via ce registre, ce qui garantit la traçabilité et la responsabilité.

- **Rattachement** : [ART-4](../../referentiel/chapitres/art-4.md) (référentiel des métadonnées), [CAP-INT-09: Gestion des consentements et bases d’autorisation](../../referentiel/capacites/cap-int-09.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../referentiel/processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (pharmacie).
- **Statut : Stable.**

### Registre des produits, intrants et indicateurs

**Contenu normatif.** Ce composant gère les référentiels de produits, d'intrants et d'indicateurs. Il assure la cohérence des nomenclatures de produits et la standardisation des indicateurs, et fournit les services de recherche et de validation.

**Discipline de mise en œuvre.** Il est l'autorité de référence pour les produits et indicateurs. Toute définition de produit ou d'indicateur passe par ce registre, ce qui garantit l'unicité et la cohérence des référentiels.

- **Rattachement** : [ART-4](../../referentiel/chapitres/art-4.md) (référentiel des métadonnées), [CAP-INT-09: Gestion des consentements et bases d’autorisation](../../referentiel/capacites/cap-int-09.md).
- **Processus soutenus** : [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../../referentiel/processus/prc-06.md) (logistique).
- **Statut : Stable.**

### API Gateway

**Contenu normatif.** Ce composant constitue le point d'entrée unique pour toutes les requêtes API. Il assure la gestion des flux, l'authentification, la limitation de débit et le routage, et garantit la sécurité et la performance des échanges inter-systèmes.

**Discipline de mise en œuvre.** Il est le gardien de la plateforme. Toute requête externe ou inter-systèmes transite par ce point, ce qui garantit la sécurité, la disponibilité et la conformité des échanges.

- **Rattachement** : [ART-5](../../referentiel/chapitres/art-5.md) (routeur d'escalade), [CAP-INT-10: Provenance, audit et traçabilité](../../referentiel/capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../referentiel/processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../../referentiel/processus/prc-06.md) (logistique).
- **Statut : Stable.**

### Registre de schémas (F.3)

**Contenu normatif.** Ce composant gère les schémas de données et les contrats d'API. Il assure la validation des messages et la conformité des échanges, et fournit les services de découverte et de versioning des schémas.

**Discipline de mise en œuvre.** Il est l'autorité de validation des échanges. Toute donnée échangée doit être conforme aux schémas définis ici, ce qui garantit l'intégrité et la cohérence des données.

- **Rattachement** : [ART-5](../../referentiel/chapitres/art-5.md) (routeur d'escalade), [CAP-INT-10: Provenance, audit et traçabilité](../../referentiel/capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-07: Identification et droits des bénéficiaires](../../referentiel/processus/prc-07.md) (production données), [PRC-08: Financement et exemption au point de service](../../referentiel/processus/prc-08.md) (qualité).
- **Statut : Stable.**

### Message broker asynchrone

**Contenu normatif.** Ce composant gère les échanges asynchrones entre les systèmes. Il assure la persistance tampon et la distribution des messages, et garantit la résilience et la fiabilité des communications inter-systèmes.

**Discipline de mise en œuvre.** Il est le mécanisme de déconnexion des systèmes. Il permet la communication même en cas de défaillance temporaire d'un composant, ce qui garantit la continuité des échanges.

- **Rattachement** : [ART-5](../../referentiel/chapitres/art-5.md) (routeur d'escalade), [CAP-INT-10: Provenance, audit et traçabilité](../../referentiel/capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../referentiel/processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../../referentiel/processus/prc-06.md) (logistique).
- **Statut : Stable.**

### Compensateur / Regroupeur de flux (Netting — ART-8C)

**Contenu normatif.** Ce composant gère les compensations et le regroupement des flux. Il assure la cohérence des transactions distribuées et la résolution des anomalies, et garantit l'intégrité des échanges complexes.

**Discipline de mise en œuvre.** Il est le mécanisme de résolution des anomalies. Il permet la compensation automatique des erreurs et la cohérence des transactions, ce qui garantit la fiabilité des échanges critiques.

- **Rattachement** : [ART-8C](../../referentiel/chapitres/art-8c.md) (Netting), [CAP-INT-10: Provenance, audit et traçabilité](../../referentiel/capacites/cap-int-10.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../referentiel/processus/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (pharmacie), [PRC-06: Clôture et capitalisation des épisodes](../../referentiel/processus/prc-06.md) (logistique).
- **Statut : Stable.**

### CMP-19 : Dossiers & statistiques de sante (hopitaux)
**Contenu normatif.** Ce composant constitue le systeme d'information hospitalier de base au niveau de l'etablissement (Couche 2 du modele ARTSN). Il tient le dossier patient informatise, les admissions, les consultations, les hospitalisations, les actes cliniques et les comptes rendus, et produit les statistiques d'activite hospitaliere (RNAM, indicateurs CSU). Il alimente en amont les registres et l'entrepot national (CMP-03) ainsi que les tableaux de bord (CMP-01). Concu pour un environnement a connectivite intermittente, il fonctionne en mode degrade et se reconcilie avec les composants centraux au retour de couverture.
**Discipline de mise en oeuvre.** L'exhaustivite et l'exactitude des statistiques hospitalieres sont une discipline de premier ordre : tout episode de soin ouvert doit etre cloture et compte-rendu. Les donnees saisies restent reconciliables avec leur source clinique et horodatees. Le composant respecte les referentiels de terminologie (PT-07/CMP-07) et le format de messagerie HL7 FHIR pour l'echange avec le noeud regional (CMP-27).
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../../referentiel/exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../../referentiel/fondations/f-1.md).
- **Processus soutenus** : [PRC-01: Acces, orientation et admission du patient](../../referentiel/processus/prc-01.md) (acces et admission), [PRC-02: Prestation des soins cliniques](../../referentiel/processus/prc-02.md) (prestation des soins), [PRC-03: Continuite, suivi et qualite des soins](../../referentiel/processus/prc-03.md) (suivi et qualite), [PRC-06: Cloture et capitalisation des episodes](../../referentiel/processus/prc-06.md) (cloture et capitalisation).
- **Statut : Brouillon.**

### CMP-20 : Gestion des pharmacies (PMIS)
**Contenu normatif.** Ce composant realise la gestion pharmaceutique au point de service (pharmacies hospitalieres, de district et communautaires) : catalogue des produits, stocks, dispensations, facturation et factures d'achat. Il assure la tracabilite du medicament du repertoire vers le beneficiaire et dialogue avec la chaine logistique (CMP-23/LMIS) pour le reapprovisionnement et les alertes de rupture. Il integre le volet pharmacovigilance en signalant les effets indesirables a la surveillance (PRC-05).
**Discipline de mise en oeuvre.** L'usage des referentiels de medicaments normalises (CMP-07) est obligatoire ; aucune denomination locale ne circule hors referentiel. Les mouvements de stock sont historises de facon immuable et les seuils de securite declares. La facturation au point de service respecte les regles d'exemption (PRC-08) lorsqu'elles s'appliquent.
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../../referentiel/exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../../referentiel/fondations/f-1.md).
- **Processus soutenus** : [PRC-02: Prestation des soins cliniques](../../referentiel/processus/prc-02.md) (dispensation aux soins), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (pharmacovigilance et riposte).
- **Statut : Brouillon.**

### CMP-21 : Sante communautaire mobile (offline)
**Contenu normatif.** Ce composant equipe les agents de sante de proximite (agents communautaires, sages-femmes, relais) sur terminaux mobiles fonctionnant hors ligne. Il capture les donnees communautaires : vaccinations, consultations, references vers le niveau superieur, releves de terrain et enquetes, et assure la remontee d'information vers la structure de reference. Il s'appuie sur le resolveur d'identite local (CMP-32) pour rattacher le beneficiaire sans ambiguite, meme hors reseau.
**Discipline de mise en oeuvre.** La perte de connectivite ne doit entrainer aucune perte de donnee : une file d'attente locale chiffree conserve les ecritures en attente et la synchronisation differentielle se declenche au retour de couverture. Les terminaux sont authentifies et leurs donnees signees. Le composant reste conforme a l'exigence de resilience au reseau (ENF-1).
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../../referentiel/exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../../referentiel/fondations/f-1.md).
- **Processus soutenus** : [PRC-01: Acces, orientation et admission du patient](../../referentiel/processus/prc-01.md) (acces au beneficiaire), [PRC-02: Prestation des soins cliniques](../../referentiel/processus/prc-02.md) (soins de proximite), [PRC-03: Continuite, suivi et qualite des soins](../../referentiel/processus/prc-03.md) (suivi communautaire).
- **Statut : Brouillon.**

### CMP-22 : Espace sante patient
**Contenu normatif.** Ce composant est le portail oriente beneficiaire du systeme de sante numerique. Il expose au citoyen son dossier, ses rendez-vous, ses droits, son historique de soins et ses documents (resultats d'examens, certificats). Il permet la prise de rendez-vous, l'acces aux services administratifs et la consultation des donnees partagees selon le consentement du beneficiaire. Il materialise l'engagement du patient et l'ouverture du systeme a la partie prenante citoyen.
**Discipline de mise en oeuvre.** L'acces est strictement controle par authentification forte et consentement (CMP-34) ; aucune donnee a caractere personnel n'est exposee sans autorisation explicite. Les traces d'acces sont journalisees (CMP-37). Le portail ne detient pas les donnees sources : il les presente en lecture via les composants detenteurs, garantissant une source unique de verite.
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../../referentiel/exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../../referentiel/fondations/f-1.md).
- **Processus soutenus** : [PRC-01: Acces, orientation et admission du patient](../../referentiel/processus/prc-01.md) (acces aux services), [PRC-07: Identification et droits des beneficiaires](../../referentiel/processus/prc-07.md) (identification et droits), [PRC-08: Financement et exemption au point de service](../../referentiel/processus/prc-08.md) (financement et exemption).
- **Statut : Brouillon.**

### CMP-23 : Chaine logistique (LMIS)
**Contenu normatif.** Ce composant pilote la logistique medicale de bout en bout : prevision des besoins, approvisionnement, stockage, distribution et dispensation des intrants (medicaments, consommables, vaccins, reactifs). Il interconnecte les pharmacies (CMP-20), les districts, les regions et le noeud central, et calcule les seuils de reapprovisionnement a partir des donnees d'activite clinique. Il emet les alertes de rupture et orchestre les flux physiques et informationnels.
**Discipline de mise en oeuvre.** La tracabilite de bout en bout est obligatoire (lot, periode de validite, lieu). Les seuils de securite sont parametres par type d'intrant et de structure. Les donnees d'activite issues des etablissements (CMP-19) alimentent la prevision. Tout mouvement est historise de facon immuable et reconcilie avec la comptabilite.
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../../referentiel/exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../../referentiel/fondations/f-1.md).
- **Processus soutenus** : [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (approvisionnement et riposte), [PRC-10: Planification et allocation des ressources](../../referentiel/processus/prc-10.md) (planification des ressources).
- **Statut : Brouillon.**

### CMP-24 : Surveillance de la sante animale (zoonoses)
**Contenu normatif.** Ce composant assure la surveillance sanitaire animale et la detection precoce des zoonoses dans une logique One Health. Il collecte les evenements chez les animaux (foyers, signaux cliniques, mouvements de cheptels), les croise avec la surveillance humaine (CMP-25, PRC-04) et declenche les alertes inter-sectorielles. Il s'appuie sur les referentiels de terminologie animal/humain et les registres des structures veterinaires.
**Discipline de mise en oeuvre.** L'interoperabilite avec la surveillance humaine est obligatoire : un meme evenement peut avoir une composante animale et humaine. Les signalements respectent les formats de messagerie d'alerte (ART-8) et sont horodates. Les donnees zoologiques et humaines sont cloisonnees par finalite et ne sont jointes qu'au sein des pipelines d'analyse autorises (CMP-03/CMP-04).
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../../referentiel/exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../../referentiel/fondations/f-1.md).
- **Processus soutenus** : [PRC-04: Veille, prevention et surveillance sanitaire](../../referentiel/processus/prc-04.md) (veille et prevention), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (alerte et riposte).
- **Statut : Brouillon.**

### CMP-25 : Enquetes & capteurs terrain
**Contenu normatif.** Ce composant gere les enquetes de terrain (enquetes sante, collectes ciblees) et les flux de capteurs environnementaux et de sante publique (meteo, qualite de l'air, eau, capteurs de surveillance). Il ingest les donnees, en verifie la provenance et l'horodatage, et les met a disposition de la veille (PRC-04) et du pilotage de la performance (PRC-11). Il alimente egalement les tableaux de bord (CMP-01).
**Discipline de mise en oeuvre.** La qualite et la provenance des donnees capteurs sont garanties (signature a la source, horodatage fiable). Les resultats sont reconcilies avant publication afin d'eviter les doubles comptes. Les protocoles d'enquete sont versionnes et tracables. Les flux exterieurs (partenaires, capteurs tiers) sont admis selon des accords references (CMP-39).
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../../referentiel/exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../../referentiel/fondations/f-1.md).
- **Processus soutenus** : [PRC-04: Veille, prevention et surveillance sanitaire](../../referentiel/processus/prc-04.md) (veille terrain), [PRC-05: Alerte, investigation et riposte](../../referentiel/processus/prc-05.md) (alerte), [PRC-11: Suivi et pilotage de la performance](../../referentiel/processus/prc-11.md) (pilotage de la performance).
- **Statut : Brouillon.**

<!-- END:GENERATED -->

## Infrastructure (couche 1)

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/composants/cmp-26.md,referentiel/composants/cmp-27.md,referentiel/composants/cmp-28.md,referentiel/composants/cmp-29.md,referentiel/composants/cmp-30.md,referentiel/composants/cmp-31.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### CMP-26 : Noeud central (datacenters nationaux HDS)
**Contenu normatif.** Ce composant fournit l'infrastructure de calcul et de stockage centralisee hebergeant les donnees et services nationaux dans des datacenters conformes aux exigences d'hebergement de donnees de sante (HDS). Il est le socle physique des composants applicatifs (CMP-01..25), analytiques (CMP-03/CMP-04) et de securite (CMP-32..38). Il assure la haute disponibilite, la redondance geographique et la reprise d'activite.
**Discipline de mise en oeuvre.** Les donnees de sante y resident sous souverainete nationale, chiffrees au repos et en transit. La continuite de service est assuree par la redondance et des plans de reprise testes. L'acces au socle est limite aux composants authentifies (CMP-35). La capacite est dimensionnee pour absorber les pics (campagnes de vaccination, epidemics).
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../../referentiel/chapitres/art-7.md).
- **Statut : Brouillon.**

### CMP-27 : Noeuds regionaux (clusters de district : Fog)
**Contenu normatif.** Ce composant deploie des clusters de calcul et de stockage au niveau regional et de district (Fog computing) pour rapprocher les services des points de service et amortir la latence ou l'absence de reseau. Il heberge les instances locales des applicatifs (CMP-19..25) et assure la synchronisation differentielle avec le noeud central (CMP-26).
**Discipline de mise en oeuvre.** La continuite de service en connectivite degradee est une exigence : les ecritures locales sont conservees et reconciliees a l'amont. Les donnees y sont chiffrees et les noeuds authentifies. La topologie est documentee et les seuils de retention definis pour respecter la politique de conservation.
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../../referentiel/chapitres/art-7.md).
- **Statut : Brouillon.**

### CMP-28 : Noeuds locaux (equipements chiffres : Edge)
**Contenu normatif.** Ce composant regroupe les equipements de bord (Edge) des structures de soins : terminaux, passerelles de collecte, boitiers de pre-traitement et concentrateurs. Il assure la collecte locale des donnees, leur pre-traitement et leur mise en file d'attente chiffree en attente de synchronisation. Il interconnecte les dispositifs au noeud regional (CMP-27).
**Discipline de mise en oeuvre.** Les equipements sont durcis, chiffres et authentifies au reseau via certificat (CMP-35). Ils fonctionnent hors ligne et se synchronisent a l'amont sans perte. Le cycle de vie des equipements (deploiement, rotation, retrait) est trace pour eviter toute compromission au bord du reseau.
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../../referentiel/chapitres/art-7.md).
- **Statut : Brouillon.**

### CMP-29 : Liaisons dediees & VPN
**Contenu normatif.** Ce composant etablit les liaisons dediees et les tunnels VPN securises entre les structures, les noeuds et les partenaires. Il fournit la connectivite de confiance necessaire aux echanges inter-structures et aux acces distants administrateurs.
**Discipline de mise en oeuvre.** Tout transit inter-structure emprunte un canal authentifie et chiffre ; les cles sont gerees via la PKI (CMP-35). Les acces distants sont controles et journalises. La segmentation isole les flux de gestion des flux metiers.
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../../referentiel/chapitres/art-7.md).
- **Statut : Brouillon.**

### CMP-30 : Reseau prive MPLS
**Contenu normatif.** Ce composant opere le reseau prive MPLS reliant les sites du systeme de sante, isole de l'internet public pour les flux sensibles. Il offre un transport garantie, avec qualite de service, entre le noeud central, les noeuds regionaux et les structures connectees.
**Discipline de mise en oeuvre.** Le routage sensible est separe du trafic grand public. La qualite de service priorise les flux critiques (alertes, dossiers urgents). La supervision mesure la disponibilite et declenche les bascules vers les liaisons de secours (CMP-29).
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../../referentiel/chapitres/art-7.md).
- **Statut : Brouillon.**

### CMP-31 : Reseaux mobiles prives (APN securises)
**Contenu normatif.** Ce composant fournit des APN (Access Point Name) securises sur les reseaux mobiles des operateurs pour les terminaux de terrain (CMP-21, agents communautaires, vehicules). Il garantit un transit prive des donnees de sante hors de l'internet ouvert.
**Discipline de mise en oeuvre.** Les terminaux mobiles n'emettent les donnees de sante que via l'APN prive, chiffre de bout en bout. L'acces a l'APN est controle et les cartes SIM identifiees. Les volumes et flux sont supervises pour detecter les anomalies.
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../../referentiel/chapitres/art-7.md).
- **Statut : Brouillon.**

<!-- END:GENERATED -->

## Securite et confiance

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/composants/cmp-32.md,referentiel/composants/cmp-33.md,referentiel/composants/cmp-34.md,referentiel/composants/cmp-35.md,referentiel/composants/cmp-36.md,referentiel/composants/cmp-37.md,referentiel/composants/cmp-38.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### CMP-32 : Gestion des identites
**Contenu normatif.** Ce composant de securite tient le systeme de gestion des identites et des acces (IAM) du systeme de sante numerique. Il enregistre et gere le cycle de vie des identites des acteurs (professionnels, patients via le registre), des structures et des dispositifs, et fournit l'authentification unique et la federation d'identites entre composants et partenaires.
**Discipline de mise en oeuvre.** Toute entite accedant au systeme dispose d'une identite verifiee et non reusee. L'identite du beneficiaire est resolue sans ambiguite via le registre d'identite (PT-04/CMP-34). Le cycle de vie (creation, suspension, suppression) est trace. La federation s'appuie sur des protocoles standards (OIDC/OAuth2, SAML) et des certificats (CMP-35).
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../../referentiel/chapitres/art-7.md).
- **Statut : Brouillon.**

### CMP-33 : Controle d'acces fin (RBAC/ABAC)
**Contenu normatif.** Ce composant applique le controle d'acces fin aux donnees et services, selon le role (RBAC), les attributs et le contexte (ABAC). Il decide, a chaque requete, si un acteur peut lire ou ecrire une ressource, en fonction de sa fonction, de la finalite et du niveau de sensibilite de la donnee.
**Discipline de mise en oeuvre.** L'acces aux donnees de sante est cloisonne par profil et finalite ; le moindre privilege est la regle. Toute decision d'acces (accord ou refus) est journalisee (CMP-37) pour audit. Les droits sont revus periodiquement. Les exceptions sont temporaires et tracees.
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../../referentiel/chapitres/art-7.md).
- **Statut : Brouillon.**

### CMP-34 : Gestion des consentements
**Contenu normatif.** Ce composant gere le consentement des beneficiaires a l'echange et a l'utilisation de leurs donnees, par finalite, par partenaire et dans le temps. Il tient le registre de consentements et l'applique a chaque flux sortant ou acces patient (CMP-22).
**Discipline de mise en oeuvre.** Aucune donnee a caractere personnel n'est partagee sans consentement enregistre, verifiable et dans le champ autorise. Le retrait de consentement est effectif immediatement et applique aux nouveaux echanges. Les consentements sont horodates et non modifiables (journal immutable, CMP-37).
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../../referentiel/chapitres/art-7.md).
- **Statut : Brouillon.**

### CMP-35 : Infrastructure de cles publiques (PKI)
**Contenu normatif.** Ce composant opere la PKI nationale du systeme de sante numerique : il emet, rotate et revoque les certificats des acteurs, structures et dispositifs, et fournit les services d'horodatage et de signature. Il est l'autorite de confiance a la base de l'authentification et du chiffrement.
**Discipline de mise en oeuvre.** Tout composant et toute liaison s'authentifie par certificat. La chaine de confiance est sous autorite nationale et ses racines sont protegees. La rotation des cles est planifiee et la revocation diffusee sans delai. Les operations de signature sont conformes aux normes en vigueur.
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../../referentiel/chapitres/art-7.md).
- **Statut : Brouillon.**

### CMP-36 : Passerelle de confiance mondiale OMS (GDHCN)
**Contenu normatif.** Ce composant interconnecte le systeme avec la Gateway de confiance mondiale de l'OMS (GDHCN) pour la verification internationale des certificats de vaccination et de sante. Il publie les certificats nationaux signes et consomme ceux des etats partenaires, dans le respect des protocoles GDHCN.
**Discipline de mise en oeuvre.** Les echanges internationaux n'exposent que les donnees necessaires, signees et chiffrees, conformement aux conventions (CMP-41). La confiance repose sur la PKI nationale (CMP-35). Les acces sont traces et les anomalies remontees a la surveillance (CMP-37).
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../../referentiel/chapitres/art-7.md).
- **Statut : Brouillon.**

### CMP-37 : Journal d'audit immuable
**Contenu normatif.** Ce composant enregistre de facon immuable tous les evenements de securite et d'acces du systeme : authentifications, decisions d'acces (CMP-33), consultations de donnees, modifications, echecs. Il constitue la piste d'audit unique et fiable pour la tracabilite et l'investigation.
**Discipline de mise en oeuvre.** Les journaux sont horodates, signes et non alterables (ajout seul). Ils sont conserves selon la politique de retention et indexes pour la recherche. L'acces a la piste d'audit est lui-meme controle et separe des producteurs de logs.
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../../referentiel/chapitres/art-7.md).
- **Statut : Brouillon.**

### CMP-38 : Moteur de chiffrement
**Contenu normatif.** Ce composant centralise les services de chiffrement (au repos et en transit) et la gestion des cles cryptographiques pour l'ensemble du socle. Il fournit les primitives utilisees par le stockage (CMP-26..28), les liaisons (CMP-29..31) et la securite (CMP-32..37).
**Discipline de mise en oeuvre.** Toutes les donnees de sante sont chiffrees par defaut. Les cles sont separees des donnees chiffrees et protegees par la PKI (CMP-35). Les algorithmes sont conformes aux recommandations et mis a jour sans rupture de service. La perte de cles est prevenue par une copie securisee.
- **Rattachement** : [ART-7: Securite, controle d'acces et residence de la donnee](../../referentiel/chapitres/art-7.md).
- **Statut : Brouillon.**

<!-- END:GENERATED -->

## Gouvernance

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/composants/cmp-39.md,referentiel/composants/cmp-40.md,referentiel/composants/cmp-41.md,referentiel/composants/cmp-42.md,referentiel/composants/cmp-43.md,referentiel/composants/cmp-44.md,referentiel/composants/cmp-45.md,referentiel/composants/cmp-46.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### CMP-39 : Registre des accords inter-institutions
**Contenu normatif.** Ce registre de gouvernance tient a jour les accords de partage de donnees entre institutions (ministeres, structures de sante, partenaires, secteur prive). Il documente le cadre juridique, les parties, le perimetre et les finalites de chaque echange inter-institutionnel.
**Discipline de mise en oeuvre.** Aucun echange inter-institutionnel n'a lieu sans accord reference et actif. Le registre est la source de verite des engagements et est consulte par la passerelle d'echange (PT-01). Les accords expires suspendent automatiquement les flux correspondants.
- **Rattachement** : [ART-0: Accords de partage inter-institutionnels](../../referentiel/chapitres/art-0.md), [F-4: Homologation obligatoire](../../referentiel/fondations/f-4.md).
- **Statut : Brouillon.**

### CMP-40 : Charte nationale de protection
**Contenu normatif.** Ce registre porte la charte nationale de protection des donnees de sante et les regles d'usage obligatoires pour tous les acteurs du systeme. Il fixe les principes de minimisation, de finalite, de conservation et de responsabilite applicables aux traitements.
**Discipline de mise en oeuvre.** Tout composant et tout traitement se conforme a la charte ; les derogations sont tracees, justifiees et temporaires. La conformite est verifiee a l'homologation (CMP-42) et auditee (CMP-45). Les manquements sont remontes a l'arbitrage (CMP-46).
- **Rattachement** : [ART-0: Accords de partage inter-institutionnels](../../referentiel/chapitres/art-0.md), [F-4: Homologation obligatoire](../../referentiel/fondations/f-4.md).
- **Statut : Brouillon.**

### CMP-41 : Conventions internationales
**Contenu normatif.** Ce registre reference les conventions internationales et les engagements multilateraux lies aux echanges de donnees de sante (OMS/GDHCN, partenaires techniques, etats voisins). Il encadre les flux transfrontaliers et les obligations de l'Etat.
**Discipline de mise en oeuvre.** Les echanges transfrontaliers respectent les conventions referencees et les exigences de souverainete et de protection (CMP-40). Toute nouvelle convention est evaluee et enregistree avant activation. Les conflits de normes sont arbitres (CMP-46).
- **Rattachement** : [ART-0: Accords de partage inter-institutionnels](../../referentiel/chapitres/art-0.md), [F-4: Homologation obligatoire](../../referentiel/fondations/f-4.md).
- **Statut : Brouillon.**

### CMP-42 : Comite national d'homologation
**Contenu normatif.** Ce registre trace les decisions du comite national d'homologation des composants et services numeriques de sante. Il consigne l'etat d'homologation, les conditions et les restrictions de mise en production de chaque element de l'architecture.
**Discipline de mise en oeuvre.** Aucun composant n'entre en production sans homologation referencee. Le registre est consulte par le deploiement et la surveillance. Les conditions d'homologation sont suivies et leur non-respect suspend le service. La periodicite de re-homologation est definie.
- **Rattachement** : [ART-0: Accords de partage inter-institutionnels](../../referentiel/chapitres/art-0.md), [F-4: Homologation obligatoire](../../referentiel/fondations/f-4.md).
- **Statut : Brouillon.**

### CMP-43 : Registre des initiatives
**Contenu normatif.** Ce registre reference les initiatives et projets numeriques de sante (existants, en cours, planifies) pour garantir la coherence de l'ecosysteme. Il documente objectif, porteur, perimetre et alignement au CAESN de chaque initiative.
**Discipline de mise en oeuvre.** Toute nouvelle initiative est enregistree et evaluee contre l'architecture de reference (ARTSN/CNISN) avant lancement. Les doublons ou les derivations non alignees sont signales au comite d'arbitrage (CMP-46). Le registre alimente le portefeuille de l'Etat.
- **Rattachement** : [ART-0: Accords de partage inter-institutionnels](../../referentiel/chapitres/art-0.md), [F-4: Homologation obligatoire](../../referentiel/fondations/f-4.md).
- **Statut : Brouillon.**

### CMP-44 : Comite d'ethique
**Contenu normatif.** Ce registre porte les avis du comite d'ethique sur les usages des donnees et les traitements sensibles (IA, profilage, recherche, partages). Il documente les saisines, les avis et les suites donnees.
**Discipline de mise en oeuvre.** Les traitements a risque ethique sollicitent un avis avant mise en oeuvre. Les avis sont conserves, opposables et relies aux composants concernes. Les derives ethiques sont remontees a l'arbitrage (CMP-46) et a l'audit (CMP-45).
- **Rattachement** : [ART-0: Accords de partage inter-institutionnels](../../referentiel/chapitres/art-0.md), [F-4: Homologation obligatoire](../../referentiel/fondations/f-4.md).
- **Statut : Brouillon.**

### CMP-45 : Cellule d'audit
**Contenu normatif.** Ce registre consigne les audits de conformite, de securite et de qualite des composants et de l'architecture dans son ensemble. Il tient le plan d'audit, les rapports et le suivi des recommandations.
**Discipline de mise en oeuvre.** Les audits sont planifies sur la base des risques et de l'homologation. Leurs recommandations sont suivies jusqu'a cloture et les ecarts remontes a l'arbitrage (CMP-46). Les conclusions alimentent la revue de l'architecture et le portefeuille.
- **Rattachement** : [ART-0: Accords de partage inter-institutionnels](../../referentiel/chapitres/art-0.md), [F-4: Homologation obligatoire](../../referentiel/fondations/f-4.md).
- **Statut : Brouillon.**

### CMP-46 : Arbitrage et risques
**Contenu normatif.** Ce registre documente l'arbitrage des risques et les decisions de gouvernance transverses du systeme de sante numerique : priorisation, resolution de conflits, gestion des risques et des crises. Il est l'instance de decision finale sur l'architecture.
**Discipline de mise en oeuvre.** Les decisions d'arbitrage sont tracees, motivees et publiees aux instances concernees. Elles alimentent le portefeuille d'initiatives (CMP-43) et la feuille de route. Les risques identifies sont suivis et reevalues periodiquement.
- **Rattachement** : [ART-0: Accords de partage inter-institutionnels](../../referentiel/chapitres/art-0.md), [F-4: Homologation obligatoire](../../referentiel/fondations/f-4.md).
- **Statut : Brouillon.**

<!-- END:GENERATED -->
