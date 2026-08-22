---
title: "Partie II : Capacités nationales requises"
id: cnisn-capacites
domain: 02_capacites
version: "1.0.0"
status: draft
last_reviewed: 2026-07-31
owner: DEPSI
tags: ["cnisn", "niveau-2", "interopérabilité", "capacites"]
---

# Partie II : Capacités nationales requises

Les capacités suivantes opérationnalisent les principes du CNISN.

Elles ne nomment aucun produit ou standard.

Ce catalogue référence les 14 capacités. Le texte de référence de chaque capacité vit dans le référentiel : `referentiel/capacites/cap-int-XX.md`.

## Catalogue des capacités

Les 14 capacités sont regroupées en sept familles de réponse, calquées sur les réponses architecturales de l'ARTSN (couches 3 à 6, axes et extensions transfrontalière et intersectorielle de la cartographie cible : voir annexe B).

| Famille | Capacités |
|---|---|
| 1. Référentiels et identités | CAP-INT-01, CAP-INT-02, CAP-INT-04, CAP-INT-05 |
| 2. Échange, médiation et contractualisation | CAP-INT-03, CAP-INT-06 |
| 3. Données analytiques et exposition | CAP-INT-07 |
| 4. Confiance, sécurité et autorisation | CAP-INT-08, CAP-INT-09, CAP-INT-10 |
| 5. Qualité et conformité | CAP-INT-11, CAP-INT-12 |
| 6. Interopérabilité transfrontalière | CAP-INT-13 |
| 7. Échanges intersectoriels One Health | CAP-INT-14 |

Chaque entrée liste les principes associés via le référentiel.

## Famille 1 : Référentiels et identités

<!-- BEGIN:GENERATED source=referentiel/capacites/cap-int-01.md,referentiel/capacites/cap-int-02.md,referentiel/capacites/cap-int-04.md,referentiel/capacites/cap-int-05.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Résolution d’identité du bénéficiaire

#### Finalité

Permettre aux systèmes autorisés de relier plusieurs représentations d’un même bénéficiaire sans confondre :

- identité fondationnelle ;
- identité fonctionnelle santé ;
- identifiants locaux ;
- identifiants temporaires ;
- identifiants de dossiers.

#### Services attendus

- recherche démographique ;
- résolution d’identifiants ;
- rapprochement ;
- détection de doublons ;
- fusion contrôlée ;
- séparation après erreur ;
- gestion des identités temporaires ;
- conservation de la provenance ;
- vérification auprès de l’autorité fondationnelle lorsque l’accès est autorisé.

#### Principes associés

- [P-INT-01: Autorité désignée](../../referentiel/principes/p-int-01.md)
- [P-INT-02: Résolution contre l’autorité](../../referentiel/principes/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../../referentiel/principes/p-int-03.md)
- [P-INT-04: Historisation des références](../../referentiel/principes/p-int-04.md)
- [P-INT-14: Base d’autorisation explicite](../../referentiel/principes/p-int-14.md)
- [P-INT-15: Limitation à la finalité](../../referentiel/principes/p-int-15.md)
- [P-INT-16: Résidence et non-réplication](../../referentiel/principes/p-int-16.md)
- [P-INT-17: Minimisation](../../referentiel/principes/p-int-17.md)
- [P-INT-18: Traçabilité différenciée](../../referentiel/principes/p-int-18.md)

### Registre et résolution des professionnels de santé

#### Finalité

Permettre de déterminer l’identité professionnelle, la qualification, le statut et l’affectation d’un professionnel ou travailleur de santé.

#### Services attendus

- recherche d’un professionnel ;
- vérification de la profession ;
- vérification de la qualification ;
- vérification de la licence ;
- vérification du statut d’exercice ;
- consultation de l’affectation ;
- consultation des habilitations ;
- historisation des changements.

#### Principe de séparation

Cette capacité est distincte :

- de l’authentification ;
- du registre des bénéficiaires ;
- de l’identité fondationnelle ;
- de la décision d’autorisation.

#### Principes associés

- [P-INT-01: Autorité désignée](../../referentiel/principes/p-int-01.md)
- [P-INT-02: Résolution contre l’autorité](../../referentiel/principes/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../../referentiel/principes/p-int-03.md)
- [P-INT-04: Historisation des références](../../referentiel/principes/p-int-04.md)
- [P-INT-14: Base d’autorisation explicite](../../referentiel/principes/p-int-14.md)
- [P-INT-15: Limitation à la finalité](../../referentiel/principes/p-int-15.md)

### Référentiel des structures et services de santé

#### Finalité

Fournir une autorité commune sur :

- les formations sanitaires ;
- les structures communautaires ;
- les laboratoires ;
- les services de santé ;
- les rattachements ;
- les localisations ;
- les périodes d’activité.

#### Services attendus

- recherche ;
- consultation ;
- résolution d’identifiants ;
- historique ;
- synchronisation ;
- publication ;
- gestion des correspondances ;
- vérification de validité.

#### Principes associés

- [P-INT-01: Autorité désignée](../../referentiel/principes/p-int-01.md)
- [P-INT-02: Résolution contre l’autorité](../../referentiel/principes/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../../referentiel/principes/p-int-03.md)
- [P-INT-04: Historisation des références](../../referentiel/principes/p-int-04.md)

### Terminologie et codification communes

#### Finalité

Permettre aux systèmes de partager des définitions et codifications cohérentes.

#### Services attendus

- consultation de systèmes de codes ;
- consultation d’ensembles de valeurs ;
- validation de codes ;
- expansion ;
- recherche de concepts ;
- traduction ;
- publication de correspondances ;
- gestion des versions ;
- dépréciation.

#### Principes associés

- [P-INT-01: Autorité désignée](../../referentiel/principes/p-int-01.md)
- [P-INT-02: Résolution contre l’autorité](../../referentiel/principes/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../../referentiel/principes/p-int-03.md)
- [P-INT-04: Historisation des références](../../referentiel/principes/p-int-04.md)
- [P-INT-05: Contrat explicite](../../referentiel/principes/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../referentiel/principes/p-int-06.md)

<!-- END:GENERATED -->

## Famille 2 : Échange, médiation et contractualisation

<!-- BEGIN:GENERATED source=referentiel/capacites/cap-int-03.md,referentiel/capacites/cap-int-06.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Échange et médiation inter-systèmes

#### Finalité

Permettre aux systèmes de transmettre, recevoir, transformer et acheminer des données ou commandes de manière gouvernée.

#### Services attendus

- réception ;
- publication ;
- interrogation ;
- notification ;
- synchronisation ;
- routage ;
- transformation ;
- validation ;
- gestion des erreurs ;
- corrélation ;
- réconciliation ;
- intégration sortante.

#### Principes associés

- [P-INT-05: Contrat explicite](../../referentiel/principes/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../referentiel/principes/p-int-06.md)
- [P-INT-07: Responsabilité de la donnée](../../referentiel/principes/p-int-07.md)
- [P-INT-08: Publication au catalogue des services](../../referentiel/principes/p-int-08.md)
- [P-INT-09: Publication des contrats](../../referentiel/principes/p-int-09.md)
- [P-INT-10: Accord préalable](../../referentiel/principes/p-int-10.md)
- [P-INT-11: Arbitrage des conflits d’autorité](../../referentiel/principes/p-int-11.md)
- [P-INT-12: Dérogation explicite](../../referentiel/principes/p-int-12.md)
- [P-INT-13: Dérogation d’urgence](../../referentiel/principes/p-int-13.md)
- [P-INT-18: Traçabilité différenciée](../../referentiel/principes/p-int-18.md)
- [P-INT-19: Neutralité technologique](../../referentiel/principes/p-int-19.md)
- [P-INT-20: Portabilité et réversibilité](../../referentiel/principes/p-int-20.md)
- [P-INT-21: Progressivité](../../referentiel/principes/p-int-21.md)
- [P-INT-22: Fonctionnement en connectivité contrainte](../../referentiel/principes/p-int-22.md)
- [P-INT-23: Conformité fondée sur des preuves](../../referentiel/principes/p-int-23.md)
- [P-INT-24: Applicabilité déclarée](../../referentiel/principes/p-int-24.md)
- [P-INT-25: Réévaluation continue](../../referentiel/principes/p-int-25.md)

### Catalogue des services et registre des contrats

#### Finalité

Rendre visibles, gouvernables et réutilisables les services et interfaces du secteur.

#### Services attendus

#### Catalogue des services

- enregistrement des services ;
- publication des propriétaires ;
- publication des consommateurs ;
- publication des niveaux de service ;
- publication des conditions d’accès ;
- publication du statut.

#### Registre des contrats

- publication des interfaces ;
- publication des événements ;
- publication des schémas ;
- versionnement ;
- compatibilité ;
- dépréciation ;
- gestion des extensions nationales.

#### Principes associés

- [P-INT-05: Contrat explicite](../../referentiel/principes/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../referentiel/principes/p-int-06.md)
- [P-INT-07: Responsabilité de la donnée](../../referentiel/principes/p-int-07.md)
- [P-INT-08: Publication au catalogue des services](../../referentiel/principes/p-int-08.md)
- [P-INT-09: Publication des contrats](../../referentiel/principes/p-int-09.md)
- [P-INT-23: Conformité fondée sur des preuves](../../referentiel/principes/p-int-23.md)
- [P-INT-24: Applicabilité déclarée](../../referentiel/principes/p-int-24.md)
- [P-INT-25: Réévaluation continue](../../referentiel/principes/p-int-25.md)

<!-- END:GENERATED -->

## Famille 3 : Données analytiques et exposition

<!-- BEGIN:GENERATED source=referentiel/capacites/cap-int-07.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Accès et exposition des données analytiques

#### Finalité

Permettre l’accès gouverné aux données et indicateurs destinés à la décision, sans imposer une charge excessive aux systèmes opérationnels.

#### Services attendus

- publication d’indicateurs ;
- consultation de données agrégées ;
- publication de métadonnées analytiques ;
- accès aux modèles validés ;
- exposition de données historiques ;
- publication de la qualité ;
- export contrôlé ;
- catalogue des données disponibles.

#### Limite de portée

Cette capacité concerne l’exposition et l’accès interopérables.

La conception interne des entrepôts, projections et modèles analytiques relève de l’ARTSN et des architectures propres aux initiatives.

#### Principes associés

- [P-INT-05: Contrat explicite](../../referentiel/principes/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../referentiel/principes/p-int-06.md)
- [P-INT-07: Responsabilité de la donnée](../../referentiel/principes/p-int-07.md)
- [P-INT-08: Publication au catalogue des services](../../referentiel/principes/p-int-08.md)
- [P-INT-09: Publication des contrats](../../referentiel/principes/p-int-09.md)
- [P-INT-17: Minimisation](../../referentiel/principes/p-int-17.md)
- [P-INT-18: Traçabilité différenciée](../../referentiel/principes/p-int-18.md)
- [P-INT-19: Neutralité technologique](../../referentiel/principes/p-int-19.md)
- [P-INT-20: Portabilité et réversibilité](../../referentiel/principes/p-int-20.md)
- [P-INT-21: Progressivité](../../referentiel/principes/p-int-21.md)
- [P-INT-22: Fonctionnement en connectivité contrainte](../../referentiel/principes/p-int-22.md)
- [P-INT-23: Conformité fondée sur des preuves](../../referentiel/principes/p-int-23.md)
- [P-INT-24: Applicabilité déclarée](../../referentiel/principes/p-int-24.md)
- [P-INT-25: Réévaluation continue](../../referentiel/principes/p-int-25.md)

<!-- END:GENERATED -->

## Famille 4 : Confiance, sécurité et autorisation

<!-- BEGIN:GENERATED source=referentiel/capacites/cap-int-08.md,referentiel/capacites/cap-int-09.md,referentiel/capacites/cap-int-10.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Confiance, sécurité et autorisation

#### Finalité

Fournir les mécanismes nécessaires à l’identification, l’authentification, l’autorisation et la protection des échanges.

#### Services attendus

- authentification des utilisateurs ;
- authentification des systèmes ;
- identité des organisations ;
- gestion des rôles ;
- gestion des attributs ;
- décision d’autorisation ;
- gestion des comptes techniques ;
- révocation ;
- gestion des secrets et certificats ;
- journalisation ;
- gestion des incidents.

#### Principes associés

- [P-INT-14: Base d’autorisation explicite](../../referentiel/principes/p-int-14.md)
- [P-INT-15: Limitation à la finalité](../../referentiel/principes/p-int-15.md)
- [P-INT-16: Résidence et non-réplication](../../referentiel/principes/p-int-16.md)
- [P-INT-17: Minimisation](../../referentiel/principes/p-int-17.md)
- [P-INT-18: Traçabilité différenciée](../../referentiel/principes/p-int-18.md)
- [P-INT-19: Neutralité technologique](../../referentiel/principes/p-int-19.md)
- [P-INT-20: Portabilité et réversibilité](../../referentiel/principes/p-int-20.md)

### Gestion des consentements et bases d’autorisation

#### Finalité

Permettre de déterminer et de prouver la base autorisant un traitement ou un accès.

#### Services attendus

- enregistrement d’une base d’autorisation ;
- consultation ;
- vérification ;
- gestion des finalités ;
- gestion des périodes ;
- retrait lorsque applicable ;
- preuve ;
- application des politiques ;
- traçabilité des décisions.

#### Principe

Le consentement est une base possible parmi plusieurs bases légales ou fonctionnelles.

#### Principes associés

- [P-INT-14: Base d’autorisation explicite](../../referentiel/principes/p-int-14.md)
- [P-INT-15: Limitation à la finalité](../../referentiel/principes/p-int-15.md)
- [P-INT-16: Résidence et non-réplication](../../referentiel/principes/p-int-16.md)
- [P-INT-17: Minimisation](../../referentiel/principes/p-int-17.md)

### Provenance, audit et traçabilité

#### Finalité

Permettre de comprendre :

- l’origine d’une donnée ;
- les transformations appliquées ;
- les accès effectués ;
- les décisions prises ;
- les opérations techniques liées.

#### Services attendus

- conservation de la provenance ;
- audit des accès ;
- audit des exports ;
- audit des opérations administratives ;
- corrélation de bout en bout ;
- consultation autorisée des traces ;
- politiques de conservation différenciées.

#### Principes associés

- [P-INT-07: Responsabilité de la donnée](../../referentiel/principes/p-int-07.md)
- [P-INT-17: Minimisation](../../referentiel/principes/p-int-17.md)
- [P-INT-18: Traçabilité différenciée](../../referentiel/principes/p-int-18.md)
- [P-INT-23: Conformité fondée sur des preuves](../../referentiel/principes/p-int-23.md)

<!-- END:GENERATED -->

## Famille 5 : Qualité et conformité

<!-- BEGIN:GENERATED source=referentiel/capacites/cap-int-11.md,referentiel/capacites/cap-int-12.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Qualité et réconciliation

#### Finalité

Permettre de détecter et traiter les divergences entre systèmes, référentiels et projections.

#### Services attendus

- validation de contrats ;
- contrôle des métadonnées ;
- détection des messages manquants ;
- comparaison de versions ;
- comparaison de valeurs ;
- détection des doublons ;
- suivi des anomalies ;
- déclenchement de corrections ;
- publication d’indicateurs de qualité.

#### Principes associés

- [P-INT-01: Autorité désignée](../../referentiel/principes/p-int-01.md)
- [P-INT-02: Résolution contre l’autorité](../../referentiel/principes/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../../referentiel/principes/p-int-03.md)
- [P-INT-04: Historisation des références](../../referentiel/principes/p-int-04.md)
- [P-INT-05: Contrat explicite](../../referentiel/principes/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../referentiel/principes/p-int-06.md)
- [P-INT-07: Responsabilité de la donnée](../../referentiel/principes/p-int-07.md)
- [P-INT-08: Publication au catalogue des services](../../referentiel/principes/p-int-08.md)
- [P-INT-09: Publication des contrats](../../referentiel/principes/p-int-09.md)
- [P-INT-23: Conformité fondée sur des preuves](../../referentiel/principes/p-int-23.md)
- [P-INT-24: Applicabilité déclarée](../../referentiel/principes/p-int-24.md)
- [P-INT-25: Réévaluation continue](../../referentiel/principes/p-int-25.md)

### Conformité et tests d’interopérabilité

#### Finalité

Permettre de vérifier objectivement qu’un système respecte les contrats et profils applicables.

#### Services attendus

- validation des contrats ;
- tests automatisés ;
- tests de sécurité ;
- tests de compatibilité ;
- tests de performance ;
- jeux de données de référence ;
- publication des résultats ;
- déclaration de conformité ;
- gestion des dérogations ;
- suivi de remédiation.

#### Principes associés

- [P-INT-19: Neutralité technologique](../../referentiel/principes/p-int-19.md)
- [P-INT-20: Portabilité et réversibilité](../../referentiel/principes/p-int-20.md)
- [P-INT-21: Progressivité](../../referentiel/principes/p-int-21.md)
- [P-INT-22: Fonctionnement en connectivité contrainte](../../referentiel/principes/p-int-22.md)
- [P-INT-23: Conformité fondée sur des preuves](../../referentiel/principes/p-int-23.md)
- [P-INT-24: Applicabilité déclarée](../../referentiel/principes/p-int-24.md)
- [P-INT-25: Réévaluation continue](../../referentiel/principes/p-int-25.md)

#### Réponse nationale

La conformité ne se traduit pas par un service exposé mais par un **processus d’homologation** : cadre CNISN Partie IV, fondation F.4 (rattachement aux capacités) et dispositif CNASN. Les tests associés (validation de contrats, jeux de données, remédiation) sont portés par les profils et outils PTISN.

<!-- END:GENERATED -->

## Famille 6 : Interopérabilité transfrontalière

<!-- BEGIN:GENERATED source=referentiel/capacites/cap-int-13.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Interopérabilité transfrontalière et confiance internationale

#### Finalité

Permettre les échanges de données et de services de santé au-delà des frontières nationales tout en garantissant la confiance mutuelle, la souveraineté des données et la conformité aux cadres internationaux.

#### Contexte

Madagascar est membre de l'Union Africaine (UA), de la Commission Économique des Nations Unies pour l'Afrique (CEUA) et candidat à l'adhésion à la Communauté de Développement de l'Afrique Australe (SADC) et à l'Organisation Internationale de la Francophonie (OIF). Les flux de données de santé transfrontaliers concernent notamment :

- la surveillance épidémique régionale (OMS AFRO, CDC Africa) ;
- les déplacements de patients entre pays de la SADC ;
- les programmes de santé multilatéraux (OMS, UNICEF, Gavi) ;
- la recherche clinique internationale ;
- les échanges d'actes médicaux pour patients transfrontaliers ;
- la logistique pharmaceutique transfrontalière.

#### Services attendus

#### Gouvernance des échanges transfrontaliers

- identification des flux autorisés vers/lors de l'international ;
- définition des données échangeables vs. les données souveraines ;
- enregistrement des accords de confiance mutuelle ;
- gestion des autorisations d'accès pour les acteurs internationaux ;
- arbitrage des conflits de juridiction.

#### Confiance mutuelle et certification

- adhésion et conformité au GDHCN (Global Digital Health Certification Network) ;
- gestion des certificats de confiance mutuelle ;
- vérification de la conformité des systèmes partenaires étrangers ;
- publication de la politique de confiance nationale ;
- révocation en cas d'incident.

#### Identification transfrontalière

- résolution d'identité pour patients étrangers sur le territoire national ;
- mapping des identifiants nationaux vers les standards internationaux (OID, HL7) ;
- gestion des identifiants temporaires pour patients de passage ;
- prévention des confusions d'identité transfrontalières.

#### Consentement et autorisation pour échanges internationaux

- gestion du consentement spécifique aux échanges internationaux ;
- vérification de la base légale pour chaque flux sortant ;
- minimisation stricte des données exportées ;
- pseudonymisation pour les flux de recherche.

#### Résidence et souveraineté

- contrôle de sortie des données sensibles ;
- journalisation de tous les flux transfrontaliers ;
- audit des accès internationaux ;
- alertes en cas d'export non autorisé ;
- rapport périodique aux autorités compétentes.

#### Échange de résumé patient (IPS)

- production et réception de résumés internationaux du patient (HL7 FHIR IPS) ;
- mapping des données nationales vers les sections IPS (allergies, médicaments, problèmes, identité) ;
- validation de conformité des IPS émis et reçus ;
- minimisation stricte : seules les sections nécessaires à la finalité clinique sont incluses ;
- conservation des IPS échangés selon la politique de rétention nationale.

#### Exigences de conformité

| Exigence | Description |
|----------|-------------|
| **EXG-TF-01** | Tout flux transfrontalier doit être couvert par un accord explicite ([P-INT-10: Accord préalable](../../referentiel/principes/p-int-10.md)) |
| **EXG-TF-02** | Le consentement du patient doit être obtenu pour tout échange sortant sauf obligation légale |
| **EXG-TF-03** | Seules les données minimisées nécessaires à la finalité peuvent être exportées |
| **EXG-TF-04** | Tous les flux transfrontaliers doivent être journalisés et auditable |
| **EXG-TF-05** | Le GDHCN doit être le référentiel de confiance pour les échanges internationaux |
| **EXG-TF-06** | Les données souveraines (identité nationale complète, données génomiques) ne quittent pas le territoire sauf dérogation |
| **EXG-TF-07** | Les systèmes partenaires étrangers doivent démontrer leur conformité avant tout accès |
| **EXG-TF-08** | Tout résumé patient échangé (IPS) doit être conforme au profil HL7 FHIR IPS et contenir au minimum les sections ALGY, MDCA, PROB, IDOI |

#### Principes associés

- [P-INT-01: Autorité désignée](../../referentiel/principes/p-int-01.md) (Autorité désignée) : l'autorité nationale reste l'autorité pour les données malgaches, même lors d'échanges ;
- [P-INT-05: Contrat explicite](../../referentiel/principes/p-int-05.md) (Contrat explicite) : tout flux transfrontalier nécessite un accord bilatéral ou multilatéral ;
- [P-INT-10: Accord préalable](../../referentiel/principes/p-int-10.md) (Accord préalable) : accord obligatoire avant tout échange avec une institution étrangère ;
- [P-INT-14: Base d’autorisation explicite](../../referentiel/principes/p-int-14.md) (Base d'autorisation explicite) : base légale documentée pour chaque type de flux sortant ;
- [P-INT-16: Résidence et non-réplication](../../referentiel/principes/p-int-16.md) (Résidence) : les contraintes de résidence s'appliquent aux flux transfrontaliers ;
- [P-INT-17: Minimisation](../../referentiel/principes/p-int-17.md) (Minimisation) : minimisation renforcée pour les échanges internationaux ;
- [P-INT-19: Neutralité technologique](../../referentiel/principes/p-int-19.md) (Neutralité technologique) : le GDHCN est un cadre de confiance, pas un produit.

#### Rattachement

- [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../../referentiel/capabilites/cap-15.md) (Sécurité, contrôle d'accès et résidence)
- [CAP-18: Coordination intersectorielle (One Health)](../../referentiel/capabilites/cap-18.md) (Coordination intersectorielle — One Health)
- [ART-7](../../referentiel/chapitres/art-7.md) (Sécurité, contrôle d'accès et résidence)
- [ART-0](../../referentiel/chapitres/art-0.md) (Accords de partage inter-institutionnels)
- [PT-14](../../03_ptisn/03_profils/pt-14-interopabilite-transfrontaliere.md) (Profil technique transfrontalier — IPS)

<!-- END:GENERATED -->

## Famille 7 : Échanges intersectoriels One Health

<!-- BEGIN:GENERATED source=referentiel/capacites/cap-int-14.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Échanges intersectoriels One Health

#### Finalité

Permettre les échanges de données entre le secteur santé et les autres secteurs de l'État (agriculture/élevage, environnement, intérieur, météorologie) dans le cadre de l'approche One Health, tout en préservant l'étanchéité juridique et éthique des bases de chaque institution.

#### Contexte

L'approche One Health reconnaît l'interdépendance entre la santé humaine, la santé animale et l'environnement. À Madagascar, les enjeux incluent :

- **Zoonoses** : peste, rage, fièvre hémorragique de Rift Valley, brucellose, tuberculose bovine
- **Surveillance environnementale** : déforestation, climat, pollution, eau
- **Sécurité alimentaire** : contamination alimentaire, résistance aux antimicrobiens
- **Épidémies émergentes** : détection précoce à l'interface homme-animal-environnement

Les secteurs concernés :

| Secteur | Ministère | Données produites |
|---------|-----------|-------------------|
| Santé humaine | MSP | Cas cliniques, laboratoire, mortalité |
| Élevage | MINAE | Cheptels, maladies animales, vaccinations animales |
| Environnement | MEEF | Climat, pollution, biodiversité, eau |
| Intérieur | MINUST | Administrations territoriales, populations |
| Météo | DGM | Données climatiques, prévisions |
| Agriculture | MINAE | Productions agricoles, intrants |

#### Services attendus

#### Gouvernance des échanges intersectoriels

- enregistrement des accords de partage entre ministères ;
- définition des flux autorisés par secteur et par finalité ;
- gestion des bases légales par secteur (secret médical, secret professionnel vétérinal, secret environnemental) ;
- arbitrage des conflits d'autorité entre secteurs ;
- suivi de la conformité des échanges.

#### Médiation intersectorielle

- transformation sémantique entre taxonomies sectorielles (CIM-10 pour santé humaine, OIE pour animaux, classification environnementale) ;
- normalisation des dimensions communes (espace, temps, géographie) ;
- corrélation des signaux faibles entre secteurs ;
- détection de clusters intersectoriels.

#### Cloisonnement et étanchéité

- séparation stricte des identités entre secteurs (pas de croisement d'identités humaines et animales) ;
- agrégation croisée sans désanonymisation ;
- journalisation distincte par secteur ;
- contrôle d'accès différencié par rôle sectoriel.

#### Alertes et coordination

- déclenchement d'alertes intersectorielles ;
- notification aux autorités compétentes de chaque secteur ;
- coordination des plans de riposte ;
- retour d'expérience post-crise.

#### Exigences de conformité

| Exigence | Description |
|----------|-------------|
| **EXG-OH-01** | Tout échange intersectoriel doit être couvert par un accord explicite entre ministères ([P-INT-10: Accord préalable](../../referentiel/principes/p-int-10.md)) |
| **EXG-OH-02** | Les identités humaines ne doivent jamais être croisées avec les identités animales |
| **EXG-OH-03** | Les données agrégées croisées doivent être irréversiblement désanonymisées |
| **EXG-OH-04** | Chaque secteur conserve la souveraineté sur ses données source |
| **EXG-OH-05** | Les dimensions d'agrégation communes (espace, temps, géographie) doivent être normalisées |
| **EXG-OH-06** | Tous les échanges intersectoriels doivent être journalisés et auditables |
| **EXG-OH-07** | Le cadre Tripartite Plus (OMS–WOAH–FAO–PNUE) doit être respecté pour les flux internationaux |

#### Principes associés

- [P-INT-01: Autorité désignée](../../referentiel/principes/p-int-01.md) (Autorité désignée) : chaque secteur reste l'autorité de ses données ;
- [P-INT-05: Contrat explicite](../../referentiel/principes/p-int-05.md) (Contrat explicite) : tout flux intersectoriel nécessite un accord ;
- [P-INT-10: Accord préalable](../../referentiel/principes/p-int-10.md) (Accord préalable) : accord obligatoire entre ministères ;
- [P-INT-14: Base d’autorisation explicite](../../referentiel/principes/p-int-14.md) (Base d'autorisation explicite) : base légale documentée par secteur ;
- [P-INT-16: Résidence et non-réplication](../../referentiel/principes/p-int-16.md) (Résidence) : les données restent dans leur secteur d'origine ;
- [P-INT-22: Fonctionnement en connectivité contrainte](../../referentiel/principes/p-int-22.md) (Connectivité contrainte) : les secteurs ont des niveaux de connectivité variables.

#### Rattachement

- [CAP-18: Coordination intersectorielle (One Health)](../../referentiel/capabilites/cap-18.md) (Coordination intersectorielle — One Health)
- [CAP-05: Surveillance épidémiologique, alerte, investigation et riposte](../../referentiel/capabilites/cap-05.md) (Surveillance épidémiologique)
- [ART-11](../../referentiel/chapitres/art-11.md) (Coordination intersectorielle)
- [ART-0](../../referentiel/chapitres/art-0.md) (Accords de partage inter-institutionnels)
- [ART-4D](../../referentiel/chapitres/art-4d.md) (Référentiel géospatial)
- [F.2](../../referentiel/fondations/f-2.md) (Souveraineté intersectorielle)
- [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../../referentiel/exigences/enf-4.md) (Cloisonnement inter-institutionnel One Health)

<!-- END:GENERATED -->

## Références

- **annexe B** : Annexe B : Articulation avec l'ARTSN (`01_cnisn/08_annexes/b-articulation-art-sn.md`)
