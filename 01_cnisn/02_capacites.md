---
title: "Partie II — Capacités nationales requises"
id: cnisn-capacites
domain: 01_cnisn
version: "0.5"
status: draft
last_reviewed: 2026-07-31
owner: DEPSI
tags: ["cnisn", "niveau-2", "interopérabilité", "capacites"]
---

# Partie II — Capacités nationales requises

Les capacités suivantes opérationnalisent les principes du CNISN.

Elles ne nomment aucun produit ou standard.

Ce catalogue référence les 12 capacités. Le texte de référence de chaque capacité vit dans le référentiel : `referentiel/capacites/cap-int-XX.md`.

## Catalogue des capacités

Les 12 capacités sont regroupées en cinq familles de réponse, calquées sur les réponses architecturales de l'ART-SN (couches 3 à 5 et axes de la cartographie cible — voir [annexe B](08_annexes/b-articulation-art-sn.md)).

| Famille | Capacités |
|---|---|
| 1. Référentiels et identités | CAP-INT-01, CAP-INT-02, CAP-INT-04, CAP-INT-05 |
| 2. Échange, médiation et contractualisation | CAP-INT-03, CAP-INT-06 |
| 3. Données analytiques et exposition | CAP-INT-07 |
| 4. Confiance, sécurité et autorisation | CAP-INT-08, CAP-INT-09, CAP-INT-10 |
| 5. Qualité et conformité | CAP-INT-11, CAP-INT-12 |

Chaque entrée liste les principes associés via le référentiel.

## Famille 1 — Référentiels et identités

<!-- BEGIN:GENERATED source=referentiel/capacites/cap-int-01.md,referentiel/capacites/cap-int-02.md,referentiel/capacites/cap-int-04.md,referentiel/capacites/cap-int-05.md -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

### CAP-INT-01 — Résolution d’identité du bénéficiaire

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
- vérification auprès de l’autorité fondationnelle lorsque autorisée.

#### Principes associés

P-INT-01 à P-INT-04, P-INT-14 à P-INT-18.

*Rattachement : [P-INT-01](../referentiel/principes/p-int-01.md), [P-INT-02](../referentiel/principes/p-int-02.md), [P-INT-03](../referentiel/principes/p-int-03.md), [P-INT-04](../referentiel/principes/p-int-04.md), [P-INT-14](../referentiel/principes/p-int-14.md), [P-INT-15](../referentiel/principes/p-int-15.md), [P-INT-16](../referentiel/principes/p-int-16.md), [P-INT-17](../referentiel/principes/p-int-17.md), [P-INT-18](../referentiel/principes/p-int-18.md), [CAP-02](../referentiel/capabilites/cap-02.md), [CAP-14](../referentiel/capabilites/cap-14.md) · [fiche](../referentiel/capacites/cap-int-01.md)*

### CAP-INT-02 — Registre et résolution des professionnels de santé

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

P-INT-01 à P-INT-04, P-INT-14 et P-INT-15.

*Rattachement : [P-INT-01](../referentiel/principes/p-int-01.md), [P-INT-02](../referentiel/principes/p-int-02.md), [P-INT-03](../referentiel/principes/p-int-03.md), [P-INT-04](../referentiel/principes/p-int-04.md), [P-INT-14](../referentiel/principes/p-int-14.md), [P-INT-15](../referentiel/principes/p-int-15.md), [CAP-09](../referentiel/capabilites/cap-09.md), [CAP-14](../referentiel/capabilites/cap-14.md) · [fiche](../referentiel/capacites/cap-int-02.md)*

### CAP-INT-04 — Référentiel des structures et services de santé

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

P-INT-01 à P-INT-04.

*Rattachement : [P-INT-01](../referentiel/principes/p-int-01.md), [P-INT-02](../referentiel/principes/p-int-02.md), [P-INT-03](../referentiel/principes/p-int-03.md), [P-INT-04](../referentiel/principes/p-int-04.md), [CAP-11](../referentiel/capabilites/cap-11.md), [CAP-13](../referentiel/capabilites/cap-13.md), [CAP-14](../referentiel/capabilites/cap-14.md) · [fiche](../referentiel/capacites/cap-int-04.md)*

### CAP-INT-05 — Terminologie et codification communes

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

P-INT-01 à P-INT-06.

*Rattachement : [P-INT-01](../referentiel/principes/p-int-01.md), [P-INT-02](../referentiel/principes/p-int-02.md), [P-INT-03](../referentiel/principes/p-int-03.md), [P-INT-04](../referentiel/principes/p-int-04.md), [P-INT-05](../referentiel/principes/p-int-05.md), [P-INT-06](../referentiel/principes/p-int-06.md), [CAP-13](../referentiel/capabilites/cap-13.md), [CAP-14](../referentiel/capabilites/cap-14.md) · [fiche](../referentiel/capacites/cap-int-05.md)*

<!-- END:GENERATED -->

## Famille 2 — Échange, médiation et contractualisation

<!-- BEGIN:GENERATED source=referentiel/capacites/cap-int-03.md,referentiel/capacites/cap-int-06.md -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

### CAP-INT-03 — Échange et médiation inter-systèmes

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

P-INT-05 à P-INT-13, P-INT-18 à P-INT-25.

*Rattachement : [P-INT-05](../referentiel/principes/p-int-05.md), [P-INT-06](../referentiel/principes/p-int-06.md), [P-INT-07](../referentiel/principes/p-int-07.md), [P-INT-08](../referentiel/principes/p-int-08.md), [P-INT-09](../referentiel/principes/p-int-09.md), [P-INT-10](../referentiel/principes/p-int-10.md), [P-INT-11](../referentiel/principes/p-int-11.md), [P-INT-12](../referentiel/principes/p-int-12.md), [P-INT-13](../referentiel/principes/p-int-13.md), [P-INT-18](../referentiel/principes/p-int-18.md), [P-INT-19](../referentiel/principes/p-int-19.md), [P-INT-20](../referentiel/principes/p-int-20.md), [P-INT-21](../referentiel/principes/p-int-21.md), [P-INT-22](../referentiel/principes/p-int-22.md), [P-INT-23](../referentiel/principes/p-int-23.md), [P-INT-24](../referentiel/principes/p-int-24.md), [P-INT-25](../referentiel/principes/p-int-25.md), [CAP-13](../referentiel/capabilites/cap-13.md), [CAP-14](../referentiel/capabilites/cap-14.md) · [fiche](../referentiel/capacites/cap-int-03.md)*

### CAP-INT-06 — Catalogue des services et registre des contrats

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

P-INT-05 à P-INT-09, P-INT-23 à P-INT-25.

*Rattachement : [P-INT-05](../referentiel/principes/p-int-05.md), [P-INT-06](../referentiel/principes/p-int-06.md), [P-INT-07](../referentiel/principes/p-int-07.md), [P-INT-08](../referentiel/principes/p-int-08.md), [P-INT-09](../referentiel/principes/p-int-09.md), [P-INT-23](../referentiel/principes/p-int-23.md), [P-INT-24](../referentiel/principes/p-int-24.md), [P-INT-25](../referentiel/principes/p-int-25.md), [CAP-14](../referentiel/capabilites/cap-14.md), [CAP-16](../referentiel/capabilites/cap-16.md) · [fiche](../referentiel/capacites/cap-int-06.md)*

<!-- END:GENERATED -->

## Famille 3 — Données analytiques et exposition

<!-- BEGIN:GENERATED source=referentiel/capacites/cap-int-07.md -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

### CAP-INT-07 — Accès et exposition des données analytiques

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

La conception interne des entrepôts, projections et modèles analytiques relève de l’ART-SN et des architectures propres aux initiatives.

#### Principes associés

P-INT-05 à P-INT-09, P-INT-17 à P-INT-25.

*Rattachement : [P-INT-05](../referentiel/principes/p-int-05.md), [P-INT-06](../referentiel/principes/p-int-06.md), [P-INT-07](../referentiel/principes/p-int-07.md), [P-INT-08](../referentiel/principes/p-int-08.md), [P-INT-09](../referentiel/principes/p-int-09.md), [P-INT-17](../referentiel/principes/p-int-17.md), [P-INT-18](../referentiel/principes/p-int-18.md), [P-INT-19](../referentiel/principes/p-int-19.md), [P-INT-20](../referentiel/principes/p-int-20.md), [P-INT-21](../referentiel/principes/p-int-21.md), [P-INT-22](../referentiel/principes/p-int-22.md), [P-INT-23](../referentiel/principes/p-int-23.md), [P-INT-24](../referentiel/principes/p-int-24.md), [P-INT-25](../referentiel/principes/p-int-25.md), [CAP-05](../referentiel/capabilites/cap-05.md), [CAP-13](../referentiel/capabilites/cap-13.md) · [fiche](../referentiel/capacites/cap-int-07.md)*

<!-- END:GENERATED -->

## Famille 4 — Confiance, sécurité et autorisation

<!-- BEGIN:GENERATED source=referentiel/capacites/cap-int-08.md,referentiel/capacites/cap-int-09.md,referentiel/capacites/cap-int-10.md -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

### CAP-INT-08 — Confiance, sécurité et autorisation

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

P-INT-14 à P-INT-20.

*Rattachement : [P-INT-14](../referentiel/principes/p-int-14.md), [P-INT-15](../referentiel/principes/p-int-15.md), [P-INT-16](../referentiel/principes/p-int-16.md), [P-INT-17](../referentiel/principes/p-int-17.md), [P-INT-18](../referentiel/principes/p-int-18.md), [P-INT-19](../referentiel/principes/p-int-19.md), [P-INT-20](../referentiel/principes/p-int-20.md), [CAP-15](../referentiel/capabilites/cap-15.md) · [fiche](../referentiel/capacites/cap-int-08.md)*

### CAP-INT-09 — Gestion des consentements et bases d’autorisation

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

P-INT-14 à P-INT-17.

*Rattachement : [P-INT-14](../referentiel/principes/p-int-14.md), [P-INT-15](../referentiel/principes/p-int-15.md), [P-INT-16](../referentiel/principes/p-int-16.md), [P-INT-17](../referentiel/principes/p-int-17.md), [CAP-15](../referentiel/capabilites/cap-15.md) · [fiche](../referentiel/capacites/cap-int-09.md)*

### CAP-INT-10 — Provenance, audit et traçabilité

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

P-INT-07, P-INT-17, P-INT-18 et P-INT-23.

*Rattachement : [P-INT-07](../referentiel/principes/p-int-07.md), [P-INT-17](../referentiel/principes/p-int-17.md), [P-INT-18](../referentiel/principes/p-int-18.md), [P-INT-23](../referentiel/principes/p-int-23.md), [CAP-13](../referentiel/capabilites/cap-13.md), [CAP-15](../referentiel/capabilites/cap-15.md) · [fiche](../referentiel/capacites/cap-int-10.md)*

<!-- END:GENERATED -->

## Famille 5 — Qualité et conformité

<!-- BEGIN:GENERATED source=referentiel/capacites/cap-int-11.md,referentiel/capacites/cap-int-12.md -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

### CAP-INT-11 — Qualité et réconciliation

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

P-INT-01 à P-INT-09, P-INT-23 à P-INT-25.

*Rattachement : [P-INT-01](../referentiel/principes/p-int-01.md), [P-INT-02](../referentiel/principes/p-int-02.md), [P-INT-03](../referentiel/principes/p-int-03.md), [P-INT-04](../referentiel/principes/p-int-04.md), [P-INT-05](../referentiel/principes/p-int-05.md), [P-INT-06](../referentiel/principes/p-int-06.md), [P-INT-07](../referentiel/principes/p-int-07.md), [P-INT-08](../referentiel/principes/p-int-08.md), [P-INT-09](../referentiel/principes/p-int-09.md), [P-INT-23](../referentiel/principes/p-int-23.md), [P-INT-24](../referentiel/principes/p-int-24.md), [P-INT-25](../referentiel/principes/p-int-25.md), [CAP-13](../referentiel/capabilites/cap-13.md), [CAP-14](../referentiel/capabilites/cap-14.md) · [fiche](../referentiel/capacites/cap-int-11.md)*

### CAP-INT-12 — Conformité et tests d’interopérabilité

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

P-INT-19 à P-INT-25.

#### Réponse nationale

La conformité ne se traduit pas par un service exposé mais par un **processus d’homologation** : cadre CNISN Partie IV, fondation F.4 (rattachement aux capacités) et dispositif CNASN. Les tests associés (validation de contrats, jeux de données, remédiation) sont portés par les profils et outils PTISN.

*Rattachement : [P-INT-19](../referentiel/principes/p-int-19.md), [P-INT-20](../referentiel/principes/p-int-20.md), [P-INT-21](../referentiel/principes/p-int-21.md), [P-INT-22](../referentiel/principes/p-int-22.md), [P-INT-23](../referentiel/principes/p-int-23.md), [P-INT-24](../referentiel/principes/p-int-24.md), [P-INT-25](../referentiel/principes/p-int-25.md), [CAP-14](../referentiel/capabilites/cap-14.md), [CAP-16](../referentiel/capabilites/cap-16.md) · [fiche](../referentiel/capacites/cap-int-12.md)*

<!-- END:GENERATED -->
