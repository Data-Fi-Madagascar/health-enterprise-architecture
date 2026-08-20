---
title: "Partie I : Principes nationaux d'interopérabilité de santé"
id: cnisn-principes
domain: 01_cnisn
version: "1.0.0"
status: draft
last_reviewed: 2026-07-31
owner: DEPSI
tags: ["cnisn", "niveau-2", "interopérabilité", "principes"]
---

# Partie I : Principes nationaux d'interopérabilité de santé

Ce catalogue référence les 25 principes du CNISN. Le texte de référence de chaque principe vit dans le référentiel : `referentiel/principes/p-int-XX.md`.

## Catégorie A : Autorité et données de référence
<!-- BEGIN:GENERATED source=referentiel/principes/p-int-01.md,referentiel/principes/p-int-02.md,referentiel/principes/p-int-03.md,referentiel/principes/p-int-04.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Autorité désignée

Toute donnée de référence partagée doit disposer :

- d’une autorité fonctionnelle désignée ;
- d’un mécanisme officiel de résolution ;
- d’une politique de gouvernance ;
- d’un identifiant stable ;
- d’une responsabilité de maintenance.

L’autorité peut être mise en œuvre par un référentiel :

- centralisé ;
- fédéré ;
- distribué.

Le principe d’autorité nationale ne signifie pas nécessairement qu’une seule base physique centralisée doit contenir toutes les données.

Il signifie qu’une règle non ambiguë doit déterminer :

- qui fait autorité ;
- quelle donnée fait foi ;
- comment elle est résolue ;
- comment un conflit est arbitré.

*Rattachement : CAP-14 · fiche P-INT-01*

### Résolution contre l’autorité

Tout système utilisant une donnée de référence partagée doit résoudre cette donnée contre l’autorité désignée.

Un système ne doit pas créer ou maintenir de manière indépendante une valeur concurrente prétendant faire autorité sur le même domaine.

Les domaines concernés comprennent notamment :

- les bénéficiaires ;
- les professionnels de santé ;
- les structures et services ;
- les terminologies ;
- les produits de santé ;
- les programmes ;
- les territoires ;
- les droits et couvertures.

*Rattachement : CAP-14 · fiche P-INT-02*

### Copies locales non autoritatives

Des copies locales, caches, répliques ou extraits hors ligne peuvent être utilisés lorsque les besoins de performance, de résilience ou de connectivité le justifient.

Ces copies doivent être :

- explicitement non autoritatives ;
- associées à une source ;
- datées ;
- versionnées ;
- synchronisées ;
- soumises à une politique d’expiration ;
- remplacées ou réconciliées lorsqu’une version plus récente est disponible.

Une copie locale ne doit pas devenir implicitement une nouvelle source faisant autorité.

*Rattachement : CAP-14 · fiche P-INT-03*

### Historisation des références

Toute donnée de référence susceptible d’évoluer doit être versionnée dans le temps.

Une mise à jour ne doit pas rendre impossible la compréhension d’une situation historique.

Les analyses et décisions historiques doivent pouvoir utiliser la version de référence applicable à la période concernée.

Les correspondances entre deux référentiels doivent également être :

- gouvernées ;
- versionnées ;
- datées ;
- réconciliées.

*Rattachement : CAP-14 · fiche P-INT-04*

<!-- END:GENERATED -->
## Catégorie B : Contractualisation des échanges et services
<!-- BEGIN:GENERATED source=referentiel/principes/p-int-05.md,referentiel/principes/p-int-06.md,referentiel/principes/p-int-07.md,referentiel/principes/p-int-08.md,referentiel/principes/p-int-09.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Contrat explicite

Tout échange entre deux systèmes doit être régi par un contrat explicite.

Le contrat doit préciser au minimum :

- le producteur ;
- le consommateur ;
- le propriétaire fonctionnel ;
- les données échangées ;
- la finalité ;
- les responsabilités ;
- la version ;
- les règles de sécurité ;
- les erreurs possibles ;
- les niveaux de service ;
- la politique d’évolution.

Aucune intégration durable ne doit dépendre uniquement :

- d’une connaissance informelle ;
- d’un accord verbal ;
- d’un format non documenté ;
- d’un accès direct non gouverné ;
- d’une dépendance à une personne déterminée.

*Rattachement : CAP-14 · fiche P-INT-05*

### Versionnement et compatibilité

Tout contrat d’échange doit être versionné.

Avant toute évolution, les règles suivantes doivent être documentées :

- compatibilité avec les producteurs existants ;
- compatibilité avec les consommateurs existants ;
- période de coexistence ;
- mécanisme de migration ;
- date de dépréciation ;
- date de retrait ;
- responsabilités de mise à niveau.

Aucune modification ne doit rompre silencieusement un système déjà intégré.

*Rattachement : CAP-14 · fiche P-INT-06*

### Responsabilité de la donnée

Pour chaque donnée ou événement échangé, les responsabilités suivantes doivent être explicites :

- source autoritative de l’état courant ;
- propriétaire fonctionnel ;
- responsable technique ;
- producteur ;
- consommateur ;
- responsable de la qualité ;
- responsable de la correction ;
- responsable de la conservation.

Aucun composant ne doit être déclaré « source unique de vérité » sans préciser la responsabilité exacte concernée.

Il convient de distinguer :

- l’état opérationnel courant ;
- l’historique capturé ;
- la preuve de réception ;
- les métadonnées ;
- la projection analytique ;
- la restitution.

*Rattachement : CAP-13 · fiche P-INT-07*

### Publication au catalogue des services

Tout service partagé ou exposé à plusieurs systèmes doit être enregistré dans le catalogue national ou sectoriel applicable.

L’enregistrement doit inclure :

- le nom du service ;
- la finalité ;
- le propriétaire ;
- le fournisseur ;
- les consommateurs ;
- la version ;
- les conditions d’accès ;
- le niveau de service ;
- le statut ;
- les environnements disponibles ;
- les contacts opérationnels.

Un service non enregistré ne doit pas être considéré comme un service national ou sectoriel officiel.

*Rattachement : CAP-14, CAP-16 · fiche P-INT-08*

### Publication des contrats

Tout contrat d’interface, d’événement, de notification ou de fichier doit être publié dans un registre gouverné.

Ce registre doit permettre de connaître :

- les versions actives ;
- les versions en transition ;
- les versions dépréciées ;
- les propriétaires ;
- les producteurs ;
- les consommateurs ;
- les règles de compatibilité ;
- les extensions nationales.

*Rattachement : CAP-14, CAP-16 · fiche P-INT-09*

<!-- END:GENERATED -->
## Catégorie C : Gouvernance interinstitutionnelle
<!-- BEGIN:GENERATED source=referentiel/principes/p-int-10.md,referentiel/principes/p-int-11.md,referentiel/principes/p-int-12.md,referentiel/principes/p-int-13.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Accord préalable

Toute intégration impliquant une source ou un consommateur relevant d’une autorité différente doit être couverte par un accord explicite.

L’accord doit être validé avant la mise en production de l’échange.

Il doit préciser :

- la finalité ;
- le périmètre ;
- les données ;
- les responsabilités ;
- les usages autorisés ;
- la résidence ;
- la conservation ;
- la sécurité ;
- les incidents ;
- l’arbitrage ;
- la sortie de l’accord.

Une intégration technique ne peut pas compenser l’absence d’un accord de gouvernance.

*Rattachement : CAP-14 · fiche P-INT-10*

### Arbitrage des conflits d’autorité

Toute divergence portant sur :

- l’autorité d’un référentiel ;
- la définition d’une donnée ;
- un contrat d’échange ;
- une règle d’accès ;
- une politique de résidence ;
- une définition d’indicateur ;

doit être arbitrée par l’instance compétente.

Elle ne doit pas être résolue durablement par un arrangement informel entre équipes techniques.

*Rattachement : CAP-14 · fiche P-INT-11*

### Dérogation explicite

Toute initiative s’écartant d’un principe du CNISN doit produire une dérogation explicite.

La dérogation doit préciser :

- le principe concerné ;
- la justification ;
- les risques ;
- les alternatives examinées ;
- les mesures compensatoires ;
- la durée ;
- les conditions de sortie ;
- le responsable.

Une dérogation non enregistrée constitue une non-conformité.

*Rattachement : CAP-14, CAP-16 · fiche P-INT-12*

### Dérogation d’urgence

Une procédure accélérée peut être utilisée lorsqu’une urgence sanitaire ou opérationnelle ne permet pas de suivre le processus normal.

La dérogation d’urgence doit être :

- autorisée par une personne ou instance habilitée ;
- limitée dans le temps ;
- limitée au périmètre strictement nécessaire ;
- assortie d’un niveau minimal de sécurité ;
- enregistrée ;
- réévaluée après l’urgence.

À l’issue de la période d’urgence, l’intégration doit être :

- retirée ;
- mise en conformité ;
- ou régularisée par une dérogation ordinaire.

*Rattachement : CAP-14, CAP-16 · fiche P-INT-13*

<!-- END:GENERATED -->
## Catégorie D : Sécurité, confiance et bases d’autorisation
<!-- BEGIN:GENERATED source=referentiel/principes/p-int-14.md,referentiel/principes/p-int-15.md,referentiel/principes/p-int-16.md,referentiel/principes/p-int-17.md,referentiel/principes/p-int-18.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Base d’autorisation explicite

Tout traitement ou accès à une donnée échangée doit reposer sur une base d’autorisation explicite et documentée.

Cette base peut notamment être :

- le consentement ;
- le mandat de soins ;
- le mandat de santé publique ;
- une obligation légale ;
- un intérêt vital ;
- un accord interinstitutionnel ;
- une autre base légale reconnue.

L’autorisation ne doit jamais être présumée uniquement parce qu’un système peut techniquement accéder à une donnée.

*Rattachement : CAP-15 · fiche P-INT-14*

### Limitation à la finalité

Une donnée obtenue pour une finalité ne doit pas être réutilisée pour une autre finalité sans :

- vérification de la base d’autorisation ;
- validation de la gouvernance ;
- mise à jour du contrat ;
- information ou consentement lorsque requis.

Les droits d’accès doivent être limités selon :

- le rôle ;
- la responsabilité ;
- le territoire ;
- le programme ;
- le contexte ;
- la finalité ;
- la durée.

*Rattachement : CAP-15 · fiche P-INT-15*

### Résidence et non-réplication

Toute contrainte de résidence doit être respectée.

Lorsqu’une donnée ne doit pas quitter son système ou son institution d’origine, l’architecture doit privilégier :

- l’interrogation fédérée ;
- l’agrégation à la source ;
- la transmission d’un résultat minimisé ;
- la pseudonymisation ;
- la transmission d’une preuve plutôt que de la donnée complète.

Une copie ne doit pas être créée uniquement parce qu’elle est techniquement possible.

*Rattachement : CAP-14, CAP-15 · fiche P-INT-16*

### Minimisation

Tout échange doit se limiter aux données nécessaires à la finalité déclarée.

Les contrats doivent distinguer :

- les données obligatoires ;
- les données optionnelles ;
- les données interdites ;
- les données sensibles ;
- les données directement identifiantes.

Les données personnelles ou cliniques ne doivent pas être ajoutées à un flux agrégé sans nécessité démontrée.

*Rattachement : CAP-15 · fiche P-INT-17*

### Traçabilité différenciée

Les initiatives doivent distinguer :

- les événements métier ;
- la provenance des données ;
- les événements d’audit ;
- les journaux techniques.

Ces traces peuvent être corrélées mais ne doivent pas être confondues.

Elles peuvent disposer :

- de formats distincts ;
- de stockages distincts ;
- de règles d’accès distinctes ;
- de durées de conservation distinctes.

*Rattachement : CAP-13, CAP-15 · fiche P-INT-18*

<!-- END:GENERATED -->
## Catégorie E : Neutralité, réversibilité et progressivité
<!-- BEGIN:GENERATED source=referentiel/principes/p-int-19.md,referentiel/principes/p-int-20.md,referentiel/principes/p-int-21.md,referentiel/principes/p-int-22.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Neutralité technologique

Le CNISN ne prescrit aucun produit, fournisseur ou technologie.

La conformité est évaluée à partir :

- des services fournis ;
- des contrats ;
- des garanties ;
- des preuves ;
- des résultats de tests.

L’utilisation d’un produit connu ou recommandé ne prouve pas automatiquement la conformité.

*Rattachement : CAP-14 · fiche P-INT-19*

### Portabilité et réversibilité

Toute initiative doit prévoir la possibilité de :

- récupérer ses données ;
- récupérer ses configurations essentielles ;
- documenter ses contrats ;
- migrer vers une autre implémentation ;
- continuer à exploiter les données après changement de fournisseur ;
- éviter les formats propriétaires non documentés.

La stratégie de sortie doit être définie avant la mise en production des services critiques.

*Rattachement : CAP-14 · fiche P-INT-20*

### Progressivité

La mise en œuvre doit être progressive.

Un périmètre limité doit précéder toute extension nationale lorsque :

- le service est nouveau ;
- le profil est provisoire ;
- le niveau de risque est élevé ;
- les capacités d’exploitation ne sont pas encore éprouvées.

Toute extension doit s’appuyer sur :

- les résultats du pilote ;
- les preuves de conformité ;
- les retours d’exploitation ;
- l’évaluation des bénéfices ;
- l’évaluation du coût total de possession.

*Rattachement : CAP-16 · fiche P-INT-21*

### Fonctionnement en connectivité contrainte

Les services nationaux doivent prendre en compte les conditions réelles de connectivité.

Lorsqu’un usage doit fonctionner hors ligne ou avec une connectivité intermittente, l’architecture doit définir :

- les copies locales autorisées ;
- les règles de synchronisation ;
- la résolution des conflits ;
- la date de validité des données ;
- la sécurité locale ;
- le traitement des opérations en attente ;
- les conditions d’expiration.

*Rattachement : CAP-14 · fiche P-INT-22*

<!-- END:GENERATED -->
## Catégorie F : Conformité et homologation
<!-- BEGIN:GENERATED source=referentiel/principes/p-int-23.md,referentiel/principes/p-int-24.md,referentiel/principes/p-int-25.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Conformité fondée sur des preuves

La conformité au CNISN ne peut pas être établie uniquement par une déclaration narrative.

Elle doit être démontrée par des preuves telles que :

- contrats publiés ;
- résultats de tests ;
- matrices de responsabilités ;
- preuves de sécurité ;
- mesures de performance ;
- preuves de versionnement ;
- rapports de réconciliation ;
- procédures de reprise ;
- décisions architecturales ;
- dérogations approuvées.

*Rattachement : CAP-16 · fiche P-INT-23*

### Applicabilité déclarée

Toute initiative doit déclarer :

- les principes qui lui sont applicables ;
- les capacités qu’elle fournit ou consomme ;
- les contrats ART applicables ;
- les profils techniques utilisés ;
- les écarts ;
- les preuves attendues.

L’absence d’applicabilité doit être justifiée lorsqu’un domaine semble directement concerné.

*Rattachement : CAP-16 · fiche P-INT-24*

### Réévaluation continue

La conformité doit être réévaluée lorsqu’intervient :

- une évolution majeure du système ;
- une nouvelle catégorie de données ;
- une nouvelle institution partenaire ;
- un changement de source autoritative ;
- une nouvelle version d’un contrat ;
- un incident majeur ;
- une modification de la base d’autorisation ;
- l’expiration d’une dérogation.

*Rattachement : CAP-16 · fiche P-INT-25*

<!-- END:GENERATED -->
