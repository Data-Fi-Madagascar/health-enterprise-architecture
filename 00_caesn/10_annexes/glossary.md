---
title: Glossaire
id: annexe-glossary
domain: 10_annexes
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: Bureau de Réalisation de la Valeur
tags: [glossaire, terminologie]
---

# Glossaire

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## Termes d'architecture d'entreprise

**Architecture d'entreprise** — Discipline de management qui décrit de façon structurée et cohérente l'ensemble d'une organisation : sa stratégie, ses processus métier, ses systèmes d'information, ses données et son infrastructure technologique. Elle permet d'aligner les investissements sur les priorités stratégiques et d'assurer la cohérence de l'ensemble.

**Architecture runway** — Ensemble des capabilités fondamentales qui doivent être développées en priorité car leur absence bloque le développement de toutes les autres. Dans le présent cadre, il s'agit de CAP-13, CAP-14, CAP-15 et CAP-16.

**Bureau de Réalisation de la Valeur** — Instance institutionnelle chargée de vérifier que les initiatives financées produisent réellement les bénéfices attendus, d'arbitrer les décisions de portefeuille et de rendre compte aux instances de gouvernance nationale. Traduction française de *Value Realization Office*.

**Capabilité** — Ce que le système de santé doit être en mesure de faire de façon durable pour exécuter ses flux de valeur. Une capabilité repose sur la combinaison de compétences humaines, de processus organisationnels, de données et de technologies.

**Chaîne de valeur d'une initiative** — Représentation explicite du lien causal entre l'*output* technique d'une initiative, le résultat intermédiaire qu'elle génère dans le fonctionnement du système, et la valeur finale pour le bénéficiaire. Appelée *Benefit Dependency Network* dans la terminologie internationale de l'architecture d'entreprise.

**Comité National d'Architecture Santé Numérique** — Instance collégiale qui garantit la cohérence architecturale du système d'information sanitaire, homologue les solutions, arbitre les standards, statue sur les dérogations et suit la rationalisation du paysage applicatif. Présidée par le Secrétaire Général du Ministère ou son représentant.

**Coût total de possession** — Coût complet d'un système ou d'une initiative sur l'ensemble de sa durée de vie : investissement initial, déploiement, exploitation, maintenance, formation des utilisateurs et support technique. En anglais : *Total Cost of Ownership* (TCO).

**Delta de maturité** — Écart entre le niveau de maturité actuel d'une capabilité et le niveau cible défini pour une échéance. C'est cet écart qui doit guider la priorisation des investissements.

**Flux de valeur** — Séquence complète des activités qui permettent de produire un résultat de valeur pour un bénéficiaire identifié, depuis le déclenchement du besoin jusqu'à la livraison du résultat. Appelé *value stream* dans la terminologie internationale.

**Interopérabilité** — Capabilité de systèmes informatiques distincts à échanger des données et à les utiliser mutuellement, de façon automatisée et fiable, sans transformation manuelle.

**Niveau de maturité** — Mesure du degré de développement d'une capabilité, selon une échelle de 1 (initial) à 5 (optimisé).

**Portefeuille d'initiatives** — Ensemble structuré des projets et programmes numériques en cours ou planifiés dans le secteur santé, géré collectivement en fonction de leur contribution à la valeur nationale.

**Référentiel national** — Base de données de référence partagée par l'ensemble des systèmes d'information sanitaire, garantissant que tous les systèmes utilisent les mêmes identifiants, définitions et codifications. Les référentiels nationaux sont des biens communs qui ne peuvent être fragmentés par des solutions propriétaires.

**Soutenabilité** — Capabilité d'un système ou d'une initiative à continuer de fonctionner et de produire de la valeur après la fin du financement initial, grâce à des ressources nationales propres.

**Value-Driven Enterprise Architecture** — Approche de l'architecture d'entreprise qui part des résultats attendus pour les bénéficiaires et remonte vers les capabilités et les technologies nécessaires pour les produire, plutôt que de partir des technologies disponibles. Approche retenue par le présent cadre.

## Termes de données et d'information

**Concept de données** — Unité atomique du dictionnaire de données, identifiant un objet d'information du système de santé (ex. : Patient, Établissement, Consultation). Chaque concept possède 7 attributs : nom, description, type, source, propriétaire, cycle de vie et référentiel source.

**Cycle de vie des données** — Ensemble des phases par lesquelles transitent les données, depuis leur création ou collecte jusqu'à leur archivage ou suppression, en passant par leur stockage, traitement, partage et utilisation.

**Dictionnaire de données** — Référentiel centralisé des concepts de données du système de santé, organisés par domaines (Patient, Professions, Structures, Produits, Événements, Géographie, Santé publique). 40 concepts définis au niveau sémantique, avec mapping technique vers FHIR.

**Domaine de données** — Catégorie regroupant les concepts de données par affinité métier. Le dictionnaire ARTSN en définit 7 : Patient, Professions et acteurs, Structures et services, Produits de santé, Événements et actes, Géographie, Santé publique et pilotage.

**Données opérationnelles** — Données produites et utilisées dans l'exécution quotidienne des services (dossier patient, consultation, référence, alerte, stock, droit, affectation). Disponibles au point de service, y compris à connectivité limitée.

**Données analytiques** — Données utilisées pour le pilotage, la planification, l'évaluation, la recherche et la redevabilité. Consolidées depuis plusieurs sources.

**Gouvernance des données** — Ensemble des processus, rôles et règles qui garantissent que les données sont gérées comme un actif stratégique, avec des propriétaires clairement identifiés, des règles de qualité et d'accès, et des mécanismes de traçabilité.

**Qualité des données** — Degré auquel les données répondent aux besoins de leurs utilisateurs, mesuré par des critères d'exactitude, de complétude, de cohérence, de opportunité et de pertinence.

**Cycle de vie des données** — Ensemble des phases par lesquelles transitent les données, depuis leur création ou collecte jusqu'à leur archivage ou suppression, en passant par leur stockage, traitement, partage et utilisation.

**Référentiel des formations sanitaires** — Base de données de référence identifiant de manière unique toutes les structures de santé (publics, privés, confessionnels, communautaires) du territoire national.

**Référentiel géographique sanitaire** — Base de données harmonisant les régions, districts, communes, fokontany et bassins de couverture pour l'organisation spatiale des services de santé.

**Référentiel des indicateurs sanitaires** — Base de données garantissant une définition unique, stable et partagée des indicateurs de performance et de résultat du système de santé.

**Référentiel des agents de santé** — Base de données identifiant les agents, leurs rôles, affectations, qualifications et formations.

**Référentiel des produits de santé** — Base de données harmonisant la désignation, la codification et le suivi des médicaments, vaccins et intrants.

**Référentiel des bénéficiaires / patients** — Base de données soutenant la continuité des soins, la protection financière et le suivi des droits des patients.

## Termes de gouvernance

**Architecture Decision Record (ADR)** — Document formalisant une décision architecturale importante : contexte, options considérées, décision retenue, conséquences. Chaque ADR reçoit un numéro unique (ADR-0001, ADR-0002…) et un statut (proposé, accepté, refusé, déprécié). Voir le registre des décisions.

**Autorité des données** — Institution ou rôle responsable de la définition des règles de gouvernance des données, de leur application et du contrôle de conformité.

**Autorité cybersécurité** — Instance responsable de la définition et de l'application des règles de sécurité informatique au sein du secteur santé.

**Instance sectorielle** — Organisme de coordination et de décision au niveau du secteur santé, regroupant les parties prenantes clés pour l'élaboration et le suivi des politiques numériques.

**Partie prenante** — Toute personne, organisation ou groupe ayant un intérêt ou une influence sur le système d'information sanitaire, qu'il soit direct (utilisateur, décideur) ou indirect (bénéficiaire, partenaire).

**RACI** — Matrice de responsabilité définissant les rôles de chaque partie prenante pour chaque activité : Responsible (exécutant), Accountable (décideur), Consulted (consulté), Informed (informé).

**Demande de modification architecturale (MOD-XXXX)** — Formulaire structuré permettant de soumettre toute modification au CAESN, à l'ARTSN ou au référentiel PTISN. Assure un traitement traçable et documenté des changements via le processus de gouvernance.

**Dépréciation** — Processus par lequel un composant, un standard ou un service est progressivement retiré du référentiel, avec un préavis de 15 mois permettant aux systèmes existants de migrer vers une alternative.

**Feuille de route** — Planification temporelle des phases de déploiement de l'architecture, identifiant les jalons, les prérequis et les budgets associés. L'ARTSN définit 6 phases de T4 2026 à T1 2028 (98 MGA).

**Homologation** — Processus par lequel le Comité National d'Architecture Santé Numérique vérifie qu'une solution numérique respecte les principes du cadre et les standards définis dans l'Architecture de Référence Technique, avant d'autoriser son déploiement dans le secteur santé.

**Niveau de service (SLA)** — Engagement contractuel définissant les performances minimales d'un service (disponibilité, temps de réponse, taux d'erreur). Trois niveaux : critique (99,95 %), important (99,9 %), standard (99,5 %).

**Plan de migration** — Stratégie de transition depuis les systèmes existants vers l'architecture cible, définissant les phases, les risques et les indicateurs de suivi. Cinq phases de T4 2026 à T2 2028 pour 7 systèmes existants.

**RBAC** — *Role-Based Access Control*. Modèle de contrôle d'accès basé sur les rôles. L'ARTSN définit 13 rôles (R-AS à R-INTER) organisés en 3 niveaux hiérarchiques (opérationnel, tactique, stratégique) et10 politiques d'autorisation (POL-01 à POL-10).

**Test d'interopérabilité** — Protocole de validation en 4 niveaux : N1 (conformité d'un profil), N2 (composabilité entre deux profils), N3 (scénario bout-en-bout), N4 (tests de charge). Chaque niveau a des exigences spécifiques avant mise en production.

## Termes de standards et normes

**DPI-H** — *Digital Public Infrastructure for Health*. Cadre normatif de l'OMS définissant les six composantes d'infrastructure numérique que tout système de santé national doit développer comme biens communs : identité, échange de données, registre des formations sanitaires, terminologie, analyse, et confiance et sécurité.

**GovStack Building Blocks** — Référentiel international définissant les composantes numériques transversales à l'ensemble de l'administration publique : identité civile, paiements, échanges inter-administrations, consentement, entre autres.

**OpenHIE** — *Open Health Information Exchange*. Architecture de référence internationale définissant comment organiser les composantes d'un système d'information sanitaire en couches interopérables : couche de médiation, couche de référence (registres et terminologies) et couche de points de service.

**HL7 FHIR** — *Fast Healthcare Interoperability Resources*. Standard moderne pour l'échange de données de santé, basé sur des ressources modulaires et une API REST.

**IHE** — *Integrating the Healthcare Enterprise*. Organisation internationale développant des profils d'intégration pour améliorer l'interopérabilité des systèmes de santé.

**CIM-10** — *Classification Internationale des Maladies, 10e révision*. Classification OMS des maladies et problèmes de santé connexes, utilisée pour le codage des diagnostics.

**SNOMED CT** — *Systematized Nomenclature of Medicine — Clinical Terms*. Terminologie clinique standardisée couvrant l'ensemble du domaine de la santé.

**LOINC** — *Logical Observation Identifiers Names and Codes*. Standard pour l'identification des mesures cliniques et des résultats de laboratoire.

**ATC** — *Anatomical Therapeutic Chemical*. Classification OMS des médicaments.

## Termes techniques

**API** — *Application Programming Interface*. Interface de programmation permettant à deux systèmes de communiquer entre eux.

**Chiffrement** — Processus de transformation des données pour les rendre illisibles à toute personne non autorisée.

**Connectivité limitée** — Environnement réseau avec débit faible, latence élevée ou discontinu, nécessitant des solutions adaptées (mode hors-ligne, synchronisation différée).

**Mode hors-ligne** — Capabilité d'un système à fonctionner sans connexion réseau, en stockant les données localement et en les synchronisant lorsque la connexion est rétablie.

**Synchronisation différée** — Mécanisme de transmission des données collectées en mode hors-ligne lors de la prochaine connexion disponible.

## Liens

- Annexes
- Matrice de lecture
- Acronymes

## Références

- **matrice de lecture** — Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **registre des décisions** — Registre des décisions d'architecture (ADR) (`01_cnisn/06_decisions/registre-decisions.md`)
- **Annexes** — Annexes (`00_caesn/10_annexes/index.md`)
- **Matrice de lecture** — Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Acronymes** — Acronymes et abréviations (`00_caesn/10_annexes/acronyms.md`)
