---
title: PT-10 : Profil technique national
id: ptisn-pt-10-confiance-authentification-autorisation
domain: 03_ptisn
version: "1.0.0"
status: draft
last_reviewed: 2026-07-31
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "profils", "pt-10"]
---

# PT-10 : Profil technique national

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

## 1. Capacité CNISN

**CAP-INT-08 : Confiance, sécurité et autorisation**

## 2. Chapitres ART applicables

- ART-0 ;
- ART-4b ;
- ART-7 ;
- ART-9 lorsque applicable.

## 3. Services nationaux

- fournisseur d’identité sectoriel ou fédéré ;
- authentification des utilisateurs ;
- identité des systèmes ;
- service d’autorisation ;
- gestion des politiques ;
- gestion des comptes techniques ;
- fédération avec les identités pangouvernementales ;
- gestion des certificats et secrets.

## 4. Profils recommandés

| Besoin | Profil ou standard |
|----|----|
| Autorisation des API REST/FHIR | OAuth 2.0 / OpenID Connect selon le contexte |
| Profil IHE d’autorisation REST | IHE IUA |
| Authentification des nœuds et audit | IHE ATNA lorsque applicable |
| Confiance interinstitutionnelle | Mécanismes de la plateforme nationale d’échange |
| Authentification renforcée | Profil national à définir |
| Autorisation par attributs | Politique ABAC nationale à définir |

IHE IUA fournit un cadre d’autorisation fondé sur des jetons pour les services HTTP REST, notamment FHIR. ATNA porte des exigences relatives à l’authentification des nœuds et à l’audit des événements de sécurité.

## 5. Principe de séparation

```plantuml
@startuml
skinparam activity {
  BackgroundColor #E8F4FD
  BorderColor #2196F3
}

|Authentification|
start
:Qui est l'utilisateur ou le système?;

|Contexte professionnel|
:Quelle est sa fonction et son affectation?;

|Base d'autorisation|
:Pourquoi l'accès est-il permis?;

|Décision|
:Quelles actions sont autorisées?;

stop

@enduml
```

## 6. Exigences minimales

- moindre privilège ;
- authentification adaptée au risque ;
- séparation des comptes utilisateurs et techniques ;
- révocation ;
- rotation des secrets ;
- contrôle territorial ;
- contrôle programmatique ;
- journalisation ;
- durée limitée des jetons ;
- vérification du contexte professionnel ;
- décision explicite.

## 7. Rôles et matrice RBAC

### 7.1 Rôles du système de santé national

| Code | Rôle | Description | Niveau hiérarchique |
|------|------|-------------|---------------------|
| **R-AS** | Agent de santé | Prestataire de soins au niveau communautaire ou centre de santé (infirmier, ACS, matrone) | Opérationnel |
| **R-MED** | Médecin | Prestataire de soins qualifié, prescripteur, spécialiste | Opérationnel |
| **R-PH** | Pharmacien | Dispensateur de produits de santé, responsable de stock | Opérationnel |
| **R-ENC** | Enquêteur | Membre d'une équipe d'investigation épidémiologique | Opérationnel |
| **R-CDIR** | Directeur de formation sanitaire | Responsable de l'établissement de soins | Tactique |
| **R-DDIST** | Directeur de district sanitaire | Coordinateur des services de santé au niveau district | Tactique |
| **R-DREG** | Directeur régional | Coordinateur des districts au niveau région | Tactique |
| **R-PROG** | Responsable de programme | Gestionnaire de programme thématique (BPC, vaccination, PAL) | Tactique |
| **R-INS** | Inspecteur | Contrôle et audit des formations sanitaires | Tactique |
| **R-DMIN** | Administrateur système | Gestionnaire technique des plateformes numériques | Technique |
| **R-API** | Compte technique (API) | Système interagissant automatiquement avec les plateformes | Technique |
| **R-MINS** | Direction ministérielle | Décideur politique, pilotage stratégique | Stratégique |
| **R-INTER** | Partenaire international | Organisme international (OMS, UNICEF, banque mondiale) | Stratégique |

### 7.2 Matrice RBAC : Accès aux données par rôle

Légende : **C** = Créer · **R** = Lire · **U** = Modifier · **D** = Supprimer · **×** = Accès interdit

| Ressource / Donnée | R-AS | R-MED | R-PH | R-ENC | R-CDIR | R-DDIST | R-DREG | R-PROG | R-INS | R-DMIN | R-API | R-MINS | R-INTER |
|---------------------|------|-------|------|-------|--------|---------|--------|--------|-------|--------|-------|--------|---------|
| **Dossier patient** | R | CRUD | R | R | R | R | R | R | R | R | R* | : | : |
| **Prescription** | R | CRUD | R | : | R | R | R | R | R | : | R* | : | : |
| **Dispensation** | R | R | CRUD | : | R | R | R | R | R | : | R* | : | : |
| **Référence / évacuation** | CR | CRUD | R | R | R | R | R | R | R | R | R* | : | : |
| **Signal épidémique** | CR | R | : | CRUD | R | R | R | R | R | R | R* | R | R |
| **Alerte sanitaire** | : | : | : | : | R | CRUD | R | R | R | R | R* | R | R |
| **Investigation** | : | R | : | CRUD | R | R | R | R | R | R | R* | R | R |
| **Éligibilité / couverture** | R | R | R | : | R | R | R | R | R | : | R* | : | : |
| **Facturation** | : | R | R | : | R | R | R | R | R | : | R* | : | : |
| **Stock / produits** | R | R | CRUD | : | R | R | R | R | R | : | R* | : | : |
| **Indicateurs / dashboards** | : | R | : | : | R | R | R | CRUD | R | R | R* | R | R |
| **Tâche d'investigation** | R | R | : | CRUD | R | R | R | R | R | : | R* | : | : |
| **Référentiels (normes, codes)** | R | R | R | R | R | R | R | R | R | R | R* | R | R |
| **Configuration système** | : | : | : | : | : | : | : | : | : | R | CRUD | : | : |

*R* : accès programme-spécifique (restreint aux données du programme assigné)

### 7.3 Politiques d'autorisation

| Code | Politique | Description |
|------|-----------|-------------|
| **POL-01** | Moindre privilège | Chaque rôle ne reçoit que les permissions strictement nécessaires à sa fonction |
| **POL-02** | Séparation des rôles | Un même utilisateur ne peut pas cumuler les rôles de prescripteur et de dispensateur pour un même patient |
| **POL-03** | Contrôle territorial | L'accès aux données est limité à la zone sanitaire d'affectation sauf autorisation explicite |
| **POL-04** | Finalité de l'accès | Chaque accès doit être justifié par une finalité (soins, surveillance, pilotage, audit) |
| **POL-05** | Durée limitée | Les jetons d'accès ont une durée maximale de 8 heures renouvelable |
| **POL-06** | Révocation temps réel | Un accès peut être révoqué instantanément en cas de compromission ou de changement d'affectation |
| **POL-07** | Traçabilité complète | Chaque accès (lecture, écriture, modification) est journalisé avec identifiant, horodatage, action, ressource |
| **POL-08** | Consentement patient | L'accès aux données cliniques sensibles nécessite le consentement du patient sauf urgence vitale |
| **POL-09** | Données minimales | En contexte transfrontalier, seules les données strictement nécessaires sont transmises (principe de minimisation) |
| **POL-10** | Comptes techniques | Les systèmes (API) sont soumis aux mêmes politiques que les utilisateurs humains, avec des jetons de service signés |

### 7.4 Matrice RBAC : Accès aux fonctions par rôle

| Fonction | R-AS | R-MED | R-PH | R-ENC | R-CDIR | R-DDIST | R-DREG | R-PROG | R-INS | R-DMIN | R-API | R-MINS |
|----------|------|-------|------|-------|--------|---------|--------|--------|-------|--------|-------|--------|
| Consulter un dossier patient | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | : |
| Écrire une prescription | : | ● | : | : | : | : | : | : | : | : | : | : |
| Dispenser un produit | : | : | ● | : | : | : | : | : | : | : | : | : |
| Émettre une référence | ● | ● | : | : | ● | ● | ● | : | : | : | : | : |
| Déclarer un signal | ● | ● | : | ● | ● | ● | ● | ● | ● | : | : | : |
| Déclencher une alerte | : | : | : | : | ● | ● | ● | ● | : | ● | : | : |
| Mener une investigation | : | ● | : | ● | ● | ● | ● | ● | ● | : | : | : |
| Vérifier l'éligibilité | ● | ● | ● | : | ● | ● | ● | ● | ● | : | ● | : |
| Consulter un dashboard | : | ● | : | : | ● | ● | ● | ● | ● | ● | ● | ● |
| Gérer les stocks | : | : | ● | : | ● | ● | ● | ● | : | : | ● | : |
| Configurer le système | : | : | : | : | : | : | : | : | : | ● | ● | : |
| Administrer les comptes | : | : | : | : | : | : | : | : | : | ● | : | : |

### 7.5 Escalade en cas d'urgence vitale

En cas d'urgence vitale documentée (code U3 ou U4), les restrictions RBAC sont temporairement levées :

| Condition | Dérogation | Traçabilité |
|-----------|------------|-------------|
| Urgence vitale (U3/U4) confirmée par un médecin | Accès complet au dossier patient pour tout prestataire impliqué | Journalisation renforcée avec motif médical, validation hiérarchique dans les 24h |
| Alerte épidémique de niveau 4 | Accès en lecture aux données de surveillance pour tous les acteurs de la riposte | Journalisation automatique, révocation à la fin de l'épisode |
| Catastrophe naturelle ou sanitaire | Mode dégradé : accès hors-ligne avec synchronisation différée | Piste d'audit complète après resynchronisation |

------------------------------------------------------------------------

*Rattachement : CMP-15, CAP-INT-08, ART-0, ART-4B, ART-7, ART-9 · fiche PT-10*

<!-- END:GENERATED -->
