---
title: "Partie II : Objets d'interopérabilité requis"
id: cnisn-capacites
domain: 02_capacites
version: "1.0.0"
status: draft
last_reviewed: 2026-07-31
owner: DEPSI
tags: ["cnisn", "niveau-2", "interopérabilité", "objets-interoperabilite"]
related: ["CAP-10", "CAP-11", "CMP-23", "ABB-ECHANGE-MEDIATION", "COMP-HOMOLOGATION-INTEROPERABILITE"]
---

# Partie II : Objets d'interopérabilité requis

Les objets suivants opérationnalisent les principes du CNISN en décrivant les blocs d'architecture, patterns, exigences, contrats, preuves et données de référence nécessaires à l'interopérabilité nationale.

Ce chapitre ne définit pas de nouvelles capacités nationales : les capacités canoniques restent les `CAP-*` du CAESN.

Le texte de référence de chaque objet vit dans le référentiel cible sous `04_architecture-repository/`. Les anciennes fiches CNISN sont conservées temporairement comme sources legacy et ne sont plus rendues comme objets actifs dans ce chapitre.

## Catalogue des objets d'interopérabilité

Les objets d'interopérabilité requis sont regroupés en huit familles de réponse, calquées sur les réponses architecturales de l'ARTSN (couches 3 à 6, axes et extensions transfrontalière et intersectorielle de la cartographie cible : voir annexe B).

| Famille | Objets d'interopérabilité requis |
|---|---|
| 1. Référentiels et identités | ABB-IDENTITE-BENEFICIAIRE, ABB-REGISTRE-PROFESSIONNELS, ABB-REFERENTIEL-STRUCTURES-SERVICES, RD-STRUCTURES-SERVICES, ABB-SERVICE-TERMINOLOGIE, TERM-CODIFICATION-COMMUNE |
| 2. Échange, médiation et contractualisation | ABB-ECHANGE-MEDIATION, PAT-ECHANGE-MEDIATION, ABB-CATALOGUE-CONTRATS, AC-CATALOGUE-SERVICES |
| 3. Données analytiques et exposition | ABB-EXPOSITION-DONNEES-ANALYTIQUES |
| 4. Confiance, sécurité et autorisation | ABB-CONFIANCE-AUTORISATION, ABB-GESTION-CONSENTEMENT, ABB-AUDIT-PROVENANCE |
| 5. Qualité et conformité | ABB-RECONCILIATION-DONNEES, PAT-QUALITE-RECONCILIATION, COMP-HOMOLOGATION-INTEROPERABILITE, EVID-TESTS-INTEROPERABILITE |
| 6. Interopérabilité transfrontalière | PART-ECHANGE-TRANSFRONTALIER, PAT-ECHANGE-INTERNATIONAL-IPS, REQ-TF-01 à REQ-TF-08 |
| 7. Échanges intersectoriels One Health | PART-ONE-HEALTH, REQ-OH-01 à REQ-OH-07 |
| 8. Logistique et chaîne d'approvisionnement | ABB-ECHANGE-LOGISTIQUE-LMIS, RD-DONNEES-ENVIRONNEMENTALES-CLIMAT |

Chaque entrée liste les principes associés via le référentiel et conserve la traçabilité par `legacy_id` dans sa fiche source.

## Famille 1 : Référentiels et identités

<!-- BEGIN:GENERATED source=04_architecture-repository/05_building-blocks/abb/abb-identite-beneficiaire.md,04_architecture-repository/05_building-blocks/abb/abb-registre-professionnels.md,04_architecture-repository/05_building-blocks/abb/abb-referentiel-structures-services.md,04_architecture-repository/02_architecture-elements/data/reference-data/rd-structures-services.md,04_architecture-repository/05_building-blocks/abb/abb-service-terminologie.md,04_architecture-repository/02_architecture-elements/data/terminologies/term-codification-commune.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Statut : candidate**

### Résolution d'identité du bénéficiaire

#### Finalité

Permettre aux systèmes autorisés de relier plusieurs représentations d'un même bénéficiaire sans confondre :

- identité fondationnelle ;
- identité fonctionnelle santé ;
- identifiants locaux ;
- identifiants temporaires ;
- identifiants de dossiers.

#### Services attendus

- recherche démographique ;
- résolution d'identifiants ;
- rapprochement ;
- détection de doublons ;
- fusion contrôlée ;
- séparation après erreur ;
- gestion des identités temporaires ;
- conservation de la provenance ;
- vérification auprès de l'autorité fondationnelle lorsque l'accès est autorisé.

#### Principes associés

- [P-INT-01: Autorité désignée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-01.md)
- [P-INT-02: Résolution contre l'autorité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-03.md)
- [P-INT-04: Historisation des références](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-04.md)
- [P-INT-14: Base d'autorisation explicite](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-14.md)
- [P-INT-15: Limitation à la finalité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-15.md)
- [P-INT-16: Résidence et non-réplication](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-16.md)
- [P-INT-17: Minimisation](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-17.md)
- [P-INT-18: Traçabilité différenciée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-18.md)

#### Rattachement

- [Partition transverse - Identité](../../04_architecture-repository/01_partitions/transverses/part-transverse-identite.md)
- [ART-4A: Résolution d'identité](../../04_architecture-repository/04_patterns/artsn-rules/art-4a.md)

**Statut : candidate**

### Référentiel des structures et services de santé

#### Finalité

Fournir une autorité commune sur :

- les formations sanitaires ;
- les structures communautaires ;
- les laboratoires ;
- les services de santé ;
- les rattachements ;
- les localisations ;
- les périodes d'activité.

#### Services attendus

- recherche ;
- consultation ;
- résolution d'identifiants ;
- historique ;
- synchronisation ;
- publication ;
- gestion des correspondances ;
- vérification de validité.

#### Principes associés

- [P-INT-01: Autorité désignée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-01.md)
- [P-INT-02: Résolution contre l'autorité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-03.md)
- [P-INT-04: Historisation des références](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-04.md)

#### Rattachement

- [Données de référence des structures et services](../../04_architecture-repository/02_architecture-elements/data/reference-data/rd-structures-services.md)
- [Partition transverse - Données référentielles](../../04_architecture-repository/01_partitions/transverses/part-transverse-donnees-referentielles.md)

**Statut : candidate**

### Registre et résolution des professionnels de santé

#### Finalité

Permettre de déterminer l'identité professionnelle, la qualification, le statut et l'affectation d'un professionnel ou travailleur de santé.

#### Services attendus

- recherche d'un professionnel ;
- vérification de la profession ;
- vérification de la qualification ;
- vérification de la licence ;
- vérification du statut d'exercice ;
- consultation de l'affectation ;
- consultation des habilitations ;
- historisation des changements.

#### Principe de séparation

Ce bloc d'architecture est distinct :

- de l'authentification ;
- du registre des bénéficiaires ;
- de l'identité fondationnelle ;
- de la décision d'autorisation.

#### Principes associés

- [P-INT-01: Autorité désignée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-01.md)
- [P-INT-02: Résolution contre l'autorité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-03.md)
- [P-INT-04: Historisation des références](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-04.md)
- [P-INT-14: Base d'autorisation explicite](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-14.md)
- [P-INT-15: Limitation à la finalité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-15.md)

#### Articulation avec la paie et les habilitations

- La résolution des professionnels alimente la [CAP-09: Gestion des ressources humaines en santé](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-09.md) et les habilitations rattachées à la [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-15.md) ; elle ne gère pas la rémunération.
- Échange financier associé : [PT-18: Échange de réclamations et paiements](../../03_ptisn/03_profils/pt-18-echange-reclamations-paiements.md).

**Statut : candidate**

### Service de terminologie et codification communes

#### Finalité

Permettre aux systèmes de partager des définitions et codifications cohérentes.

#### Services attendus

- consultation de systèmes de codes ;
- consultation d'ensembles de valeurs ;
- validation de codes ;
- expansion ;
- recherche de concepts ;
- traduction ;
- publication de correspondances ;
- gestion des versions ;
- dépréciation.

#### Principes associés

- [P-INT-01: Autorité désignée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-01.md)
- [P-INT-02: Résolution contre l'autorité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-03.md)
- [P-INT-04: Historisation des références](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-04.md)
- [P-INT-05: Contrat explicite](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-06.md)

#### Rattachement

- [Terminologie de codification commune](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-codification-commune.md)
- [STD-0007: SNOMED CT](../05_standards/std-0007-snomed-ct.md)

**Statut : candidate**

### Données de référence des structures et services

#### Finalité

Fournir une autorité commune sur :

- les formations sanitaires ;
- les structures communautaires ;
- les laboratoires ;
- les services de santé ;
- les rattachements ;
- les localisations ;
- les périodes d'activité.

#### Services attendus

- recherche ;
- consultation ;
- résolution d'identifiants ;
- historique ;
- synchronisation ;
- publication ;
- gestion des correspondances ;
- vérification de validité.

#### Principes associés

- [P-INT-01: Autorité désignée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-01.md)
- [P-INT-02: Résolution contre l'autorité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-03.md)
- [P-INT-04: Historisation des références](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-04.md)

#### Rattachement

- [ABB référentiel des structures et services](../../04_architecture-repository/05_building-blocks/abb/abb-referentiel-structures-services.md)
- [DO-23](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-23.md)

**Statut : candidate**

### Terminologie et codification communes

#### Finalité

Permettre aux systèmes de partager des définitions et codifications cohérentes.

#### Services attendus

- consultation de systèmes de codes ;
- consultation d'ensembles de valeurs ;
- validation de codes ;
- expansion ;
- recherche de concepts ;
- traduction ;
- publication de correspondances ;
- gestion des versions ;
- dépréciation.

#### Principes associés

- [P-INT-01: Autorité désignée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-01.md)
- [P-INT-02: Résolution contre l'autorité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-03.md)
- [P-INT-04: Historisation des références](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-04.md)
- [P-INT-05: Contrat explicite](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-06.md)

#### Rattachement

- [ABB service de terminologie](../../04_architecture-repository/05_building-blocks/abb/abb-service-terminologie.md)
- [STD-0007: SNOMED CT](../05_standards/std-0007-snomed-ct.md)

<!-- END:GENERATED -->

## Famille 2 : Échange, médiation et contractualisation

<!-- BEGIN:GENERATED source=04_architecture-repository/05_building-blocks/abb/abb-echange-mediation.md,04_architecture-repository/04_patterns/pat-echange-mediation.md,04_architecture-repository/05_building-blocks/abb/abb-catalogue-contrats.md,04_architecture-repository/06_governance/architecture-contracts/ac-catalogue-services.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Statut : candidate**

### Catalogue des services et registre des contrats

#### Finalité

Rendre visibles, gouvernables et réutilisables les services et interfaces du secteur.

#### Services attendus

#### Catalogue des services

- enregistrement des services ;
- publication des propriétaires ;
- publication des consommateurs ;
- publication des niveaux de service ;
- publication des conditions d'accès ;
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

- [P-INT-05: Contrat explicite](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-06.md)
- [P-INT-07: Responsabilité de la donnée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-07.md)
- [P-INT-08: Publication au catalogue des services](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-08.md)
- [P-INT-09: Publication des contrats](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-09.md)
- [P-INT-23: Conformité fondée sur des preuves](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-23.md)
- [P-INT-24: Applicabilité déclarée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-24.md)
- [P-INT-25: Réévaluation continue](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-25.md)

#### Rattachement

- [Contrat d'architecture du catalogue de services](../../04_architecture-repository/06_governance/architecture-contracts/ac-catalogue-services.md)
- [Partition transverse - Interopérabilité](../../04_architecture-repository/01_partitions/transverses/part-transverse-interoperabilite.md)

**Statut : candidate**

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

- [P-INT-05: Contrat explicite](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-06.md)
- [P-INT-07: Responsabilité de la donnée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-07.md)
- [P-INT-08: Publication au catalogue des services](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-08.md)
- [P-INT-09: Publication des contrats](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-09.md)
- [P-INT-10: Accord préalable](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-10.md)
- [P-INT-11: Arbitrage des conflits d'autorité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-11.md)
- [P-INT-12: Dérogation explicite](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-12.md)
- [P-INT-13: Dérogation d'urgence](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-13.md)
- [P-INT-18: Traçabilité différenciée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-18.md)
- [P-INT-19: Neutralité technologique](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-19.md)
- [P-INT-20: Portabilité et réversibilité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-20.md)
- [P-INT-21: Progressivité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-21.md)
- [P-INT-22: Fonctionnement en connectivité contrainte](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-22.md)
- [P-INT-23: Conformité fondée sur des preuves](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-23.md)
- [P-INT-24: Applicabilité déclarée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-24.md)
- [P-INT-25: Réévaluation continue](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-25.md)

#### Rattachement

- [Pattern d'échange et médiation](../../04_architecture-repository/04_patterns/pat-echange-mediation.md)
- [Partition transverse - Interopérabilité](../../04_architecture-repository/01_partitions/transverses/part-transverse-interoperabilite.md)

**Statut : candidate**

### Contrat d'architecture du catalogue de services

#### Finalité

Rendre visibles, gouvernables et réutilisables les services et interfaces du secteur.

#### Clauses attendues

#### Catalogue des services

- enregistrement des services ;
- publication des propriétaires ;
- publication des consommateurs ;
- publication des niveaux de service ;
- publication des conditions d'accès ;
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

- [P-INT-05: Contrat explicite](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-06.md)
- [P-INT-08: Publication au catalogue des services](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-08.md)
- [P-INT-09: Publication des contrats](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-09.md)

#### Rattachement

- [ABB catalogue des services et registre des contrats](../../04_architecture-repository/05_building-blocks/abb/abb-catalogue-contrats.md)

**Statut : candidate**

### Pattern d'échange et médiation

#### Finalité

Structurer la transmission, la réception, la transformation et l'acheminement de données ou commandes entre systèmes de manière gouvernée.

#### Mécanismes attendus

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

- [P-INT-05: Contrat explicite](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-06.md)
- [P-INT-07: Responsabilité de la donnée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-07.md)
- [P-INT-08: Publication au catalogue des services](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-08.md)
- [P-INT-09: Publication des contrats](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-09.md)
- [P-INT-10: Accord préalable](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-10.md)
- [P-INT-18: Traçabilité différenciée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-18.md)

#### Rattachement

- [ABB échange et médiation](../../04_architecture-repository/05_building-blocks/abb/abb-echange-mediation.md)
- [Partition transverse - Interopérabilité](../../04_architecture-repository/01_partitions/transverses/part-transverse-interoperabilite.md)

<!-- END:GENERATED -->

## Famille 3 : Données analytiques et exposition

<!-- BEGIN:GENERATED source=04_architecture-repository/05_building-blocks/abb/abb-exposition-donnees-analytiques.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Statut : candidate**

### Accès et exposition des données analytiques

#### Finalité

Permettre l'accès gouverné aux données et indicateurs destinés à la décision, sans imposer une charge excessive aux systèmes opérationnels.

#### Services attendus

- publication d'indicateurs ;
- consultation de données agrégées ;
- publication de métadonnées analytiques ;
- accès aux modèles validés ;
- exposition de données historiques ;
- publication de la qualité ;
- export contrôlé ;
- catalogue des données disponibles.

#### Limite de portée

Cet ABB concerne l'exposition et l'accès interopérables.

La conception interne des entrepôts, projections et modèles analytiques relève de l'ARTSN et des architectures propres aux initiatives.

#### Principes associés

- [P-INT-05: Contrat explicite](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-06.md)
- [P-INT-07: Responsabilité de la donnée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-07.md)
- [P-INT-08: Publication au catalogue des services](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-08.md)
- [P-INT-09: Publication des contrats](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-09.md)
- [P-INT-17: Minimisation](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-17.md)
- [P-INT-18: Traçabilité différenciée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-18.md)
- [P-INT-19: Neutralité technologique](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-19.md)
- [P-INT-20: Portabilité et réversibilité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-20.md)
- [P-INT-21: Progressivité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-21.md)
- [P-INT-22: Fonctionnement en connectivité contrainte](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-22.md)
- [P-INT-23: Conformité fondée sur des preuves](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-23.md)
- [P-INT-24: Applicabilité déclarée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-24.md)
- [P-INT-25: Réévaluation continue](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-25.md)

#### Rattachement

- [Partition transverse - Analytics et pilotage](../../04_architecture-repository/01_partitions/transverses/part-transverse-analytics-pilotage.md)
- [ART-6: Analytique et restitution](../../04_architecture-repository/04_patterns/artsn-rules/art-6.md)

<!-- END:GENERATED -->

## Famille 4 : Confiance, sécurité et autorisation

<!-- BEGIN:GENERATED source=04_architecture-repository/05_building-blocks/abb/abb-confiance-autorisation.md,04_architecture-repository/05_building-blocks/abb/abb-gestion-consentement.md,04_architecture-repository/05_building-blocks/abb/abb-audit-provenance.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Statut : candidate**

### Provenance, audit et traçabilité

#### Finalité

Permettre de comprendre :

- l'origine d'une donnée ;
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

- [P-INT-07: Responsabilité de la donnée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-07.md)
- [P-INT-17: Minimisation](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-17.md)
- [P-INT-18: Traçabilité différenciée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-18.md)
- [P-INT-23: Conformité fondée sur des preuves](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-23.md)

#### Rattachement

- [Partition transverse - Sécurité et confiance](../../04_architecture-repository/01_partitions/transverses/part-transverse-securite-confiance.md)
- [ART-9: Garanties transactionnelles fortes](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md)

**Statut : candidate**

### Confiance, sécurité et autorisation

#### Finalité

Fournir les mécanismes nécessaires à l'identification, l'authentification, l'autorisation et la protection des échanges.

#### Services attendus

- authentification des utilisateurs ;
- authentification des systèmes ;
- identité des organisations ;
- gestion des rôles ;
- gestion des attributs ;
- décision d'autorisation ;
- gestion des comptes techniques ;
- révocation ;
- gestion des secrets et certificats ;
- journalisation ;
- gestion des incidents.

#### Principes associés

- [P-INT-14: Base d'autorisation explicite](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-14.md)
- [P-INT-15: Limitation à la finalité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-15.md)
- [P-INT-16: Résidence et non-réplication](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-16.md)
- [P-INT-17: Minimisation](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-17.md)
- [P-INT-18: Traçabilité différenciée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-18.md)
- [P-INT-19: Neutralité technologique](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-19.md)
- [P-INT-20: Portabilité et réversibilité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-20.md)

#### Rattachement

- [Partition transverse - Sécurité et confiance](../../04_architecture-repository/01_partitions/transverses/part-transverse-securite-confiance.md)
- [ART-7: Sécurité, contrôle d'accès et résidence de la donnée](../../04_architecture-repository/04_patterns/artsn-rules/art-7.md)

**Statut : candidate**

### Gestion des consentements et bases d'autorisation

#### Finalité

Permettre de déterminer et de prouver la base autorisant un traitement ou un accès.

#### Services attendus

- enregistrement d'une base d'autorisation ;
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

- [P-INT-14: Base d'autorisation explicite](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-14.md)
- [P-INT-15: Limitation à la finalité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-15.md)
- [P-INT-16: Résidence et non-réplication](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-16.md)
- [P-INT-17: Minimisation](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-17.md)

#### Rattachement

- [Partition transverse - Sécurité et confiance](../../04_architecture-repository/01_partitions/transverses/part-transverse-securite-confiance.md)
- [ART-4B: Bases d'autorisation](../../04_architecture-repository/04_patterns/artsn-rules/art-4b.md)

<!-- END:GENERATED -->

## Famille 5 : Qualité et conformité

<!-- BEGIN:GENERATED source=04_architecture-repository/05_building-blocks/abb/abb-reconciliation-donnees.md,04_architecture-repository/04_patterns/pat-qualite-reconciliation.md,04_architecture-repository/06_governance/compliance/comp-homologation-interoperabilite.md,04_architecture-repository/06_governance/evidence/evid-tests-interoperabilite.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Statut : candidate**

### Qualité et réconciliation des données

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
- publication d'indicateurs de qualité.

#### Principes associés

- [P-INT-01: Autorité désignée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-01.md)
- [P-INT-02: Résolution contre l'autorité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-03.md)
- [P-INT-04: Historisation des références](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-04.md)
- [P-INT-05: Contrat explicite](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-06.md)
- [P-INT-07: Responsabilité de la donnée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-07.md)
- [P-INT-08: Publication au catalogue des services](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-08.md)
- [P-INT-09: Publication des contrats](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-09.md)
- [P-INT-23: Conformité fondée sur des preuves](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-23.md)
- [P-INT-24: Applicabilité déclarée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-24.md)
- [P-INT-25: Réévaluation continue](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-25.md)

#### Rattachement

- [Pattern qualité et réconciliation](../../04_architecture-repository/04_patterns/pat-qualite-reconciliation.md)
- [Partition transverse - Interopérabilité](../../04_architecture-repository/01_partitions/transverses/part-transverse-interoperabilite.md)

**Statut : candidate**

### Homologation d'interopérabilité

#### Finalité

Permettre de vérifier objectivement qu'un système respecte les contrats et profils applicables.

#### Contrôles attendus

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

- [P-INT-19: Neutralité technologique](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-19.md)
- [P-INT-20: Portabilité et réversibilité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-20.md)
- [P-INT-21: Progressivité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-21.md)
- [P-INT-22: Fonctionnement en connectivité contrainte](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-22.md)
- [P-INT-23: Conformité fondée sur des preuves](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-23.md)
- [P-INT-24: Applicabilité déclarée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-24.md)
- [P-INT-25: Réévaluation continue](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-25.md)

#### Réponse nationale

La conformité ne se traduit pas par un service exposé mais par un processus d'homologation : cadre CNISN Partie IV, fondation F.4 et dispositif CNASN. Les tests associés sont portés par les profils et outils PTISN.

**Statut : candidate**

### Preuves de tests d'interopérabilité

#### Finalité

Conserver les éléments probants qui démontrent qu'un système respecte les contrats et profils applicables.

#### Preuves attendues

- résultats de validation des contrats ;
- rapports de tests automatisés ;
- rapports de tests de sécurité ;
- rapports de compatibilité ;
- résultats de performance ;
- jeux de données de référence utilisés ;
- déclaration de conformité ;
- suivi de remédiation.

#### Rattachement

- [Règle de conformité d'homologation](../../04_architecture-repository/06_governance/compliance/comp-homologation-interoperabilite.md)

**Statut : candidate**

### Pattern qualité et réconciliation

#### Finalité

Organiser la détection et le traitement des divergences entre systèmes, référentiels et projections.

#### Mécanismes attendus

- validation de contrats ;
- contrôle des métadonnées ;
- détection des messages manquants ;
- comparaison de versions ;
- comparaison de valeurs ;
- détection des doublons ;
- suivi des anomalies ;
- déclenchement de corrections ;
- publication d'indicateurs de qualité.

#### Principes associés

- [P-INT-01: Autorité désignée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-01.md)
- [P-INT-02: Résolution contre l'autorité](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-03.md)
- [P-INT-04: Historisation des références](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-04.md)
- [P-INT-23: Conformité fondée sur des preuves](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-23.md)
- [P-INT-24: Applicabilité déclarée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-24.md)
- [P-INT-25: Réévaluation continue](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-25.md)

#### Rattachement

- [ABB qualité et réconciliation](../../04_architecture-repository/05_building-blocks/abb/abb-reconciliation-donnees.md)

<!-- END:GENERATED -->

## Famille 6 : Interopérabilité transfrontalière

<!-- BEGIN:GENERATED source=04_architecture-repository/04_patterns/pat-echange-international-ips.md,04_architecture-repository/03_requirements/req-tf-01.md,04_architecture-repository/03_requirements/req-tf-02.md,04_architecture-repository/03_requirements/req-tf-03.md,04_architecture-repository/03_requirements/req-tf-04.md,04_architecture-repository/03_requirements/req-tf-05.md,04_architecture-repository/03_requirements/req-tf-06.md,04_architecture-repository/03_requirements/req-tf-07.md,04_architecture-repository/03_requirements/req-tf-08.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Statut : candidate**

### Pattern d'échange international IPS

#### Finalité

Encadrer les échanges de données et de services de santé au-delà des frontières nationales tout en garantissant la confiance mutuelle, la souveraineté des données et la conformité aux cadres internationaux.

#### Mécanismes attendus

#### Gouvernance des échanges transfrontaliers

- identification des flux autorisés vers ou depuis l'international ;
- définition des données échangeables et des données souveraines ;
- enregistrement des accords de confiance mutuelle ;
- gestion des autorisations d'accès pour les acteurs internationaux ;
- arbitrage des conflits de juridiction.

#### Confiance mutuelle et certification

- adhésion et conformité au GDHCN (Global Digital Health Certification Network) ;
- gestion des certificats de confiance mutuelle ;
- vérification de la conformité des systèmes partenaires étrangers ;
- publication de la politique de confiance nationale ;
- révocation en cas d'incident.

#### Échange de résumé patient

- production et réception de résumés internationaux du patient (HL7 FHIR IPS) ;
- mapping des données nationales vers les sections IPS ;
- validation de conformité des IPS émis et reçus ;
- minimisation stricte des sections incluses ;
- conservation des IPS échangés selon la politique de rétention nationale.

#### Rattachement

- [Partition échange transfrontalier](../../04_architecture-repository/01_partitions/externes/part-echange-transfrontalier.md)
- [ART-7: Sécurité, contrôle d'accès et résidence de la donnée](../../04_architecture-repository/04_patterns/artsn-rules/art-7.md)

**Statut : candidate**

### Tout flux transfrontalier doit être couvert par un accord explicite.

#### Énoncé

Tout flux transfrontalier doit être couvert par un accord explicite.

#### Rattachement

- [Partition échange transfrontalier](../../04_architecture-repository/01_partitions/externes/part-echange-transfrontalier.md)

**Statut : candidate**

### Le consentement du patient doit être obtenu pour tout échange sortant sauf obligation légale.

#### Énoncé

Le consentement du patient doit être obtenu pour tout échange sortant sauf obligation légale.

#### Rattachement

- [Partition échange transfrontalier](../../04_architecture-repository/01_partitions/externes/part-echange-transfrontalier.md)

**Statut : candidate**

### Seules les données minimisées nécessaires à la finalité peuvent être exportées.

#### Énoncé

Seules les données minimisées nécessaires à la finalité peuvent être exportées.

#### Rattachement

- [Partition échange transfrontalier](../../04_architecture-repository/01_partitions/externes/part-echange-transfrontalier.md)

**Statut : candidate**

### Tous les flux transfrontaliers doivent être journalisés et auditables.

#### Énoncé

Tous les flux transfrontaliers doivent être journalisés et auditables.

#### Rattachement

- [Partition échange transfrontalier](../../04_architecture-repository/01_partitions/externes/part-echange-transfrontalier.md)

**Statut : candidate**

### Le GDHCN doit être le référentiel de confiance pour les échanges internationaux.

#### Énoncé

Le GDHCN doit être le référentiel de confiance pour les échanges internationaux.

#### Rattachement

- [Partition échange transfrontalier](../../04_architecture-repository/01_partitions/externes/part-echange-transfrontalier.md)

**Statut : candidate**

### Les données souveraines ne quittent pas le territoire sauf dérogation.

#### Énoncé

Les données souveraines ne quittent pas le territoire sauf dérogation.

#### Rattachement

- [Partition échange transfrontalier](../../04_architecture-repository/01_partitions/externes/part-echange-transfrontalier.md)

**Statut : candidate**

### Les systèmes partenaires étrangers doivent démontrer leur conformité avant tout accès.

#### Énoncé

Les systèmes partenaires étrangers doivent démontrer leur conformité avant tout accès.

#### Rattachement

- [Partition échange transfrontalier](../../04_architecture-repository/01_partitions/externes/part-echange-transfrontalier.md)

**Statut : candidate**

### Tout résumé patient échangé doit être conforme au profil HL7 FHIR IPS et contenir les sections minimales requises.

#### Énoncé

Tout résumé patient échangé doit être conforme au profil HL7 FHIR IPS et contenir les sections minimales requises.

#### Rattachement

- [Partition échange transfrontalier](../../04_architecture-repository/01_partitions/externes/part-echange-transfrontalier.md)

<!-- END:GENERATED -->

## Famille 7 : Échanges intersectoriels One Health

<!-- BEGIN:GENERATED source=04_architecture-repository/03_requirements/req-oh-01.md,04_architecture-repository/03_requirements/req-oh-02.md,04_architecture-repository/03_requirements/req-oh-03.md,04_architecture-repository/03_requirements/req-oh-04.md,04_architecture-repository/03_requirements/req-oh-05.md,04_architecture-repository/03_requirements/req-oh-06.md,04_architecture-repository/03_requirements/req-oh-07.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Statut : candidate**

### Tout échange intersectoriel doit être couvert par un accord explicite entre ministères.

#### Énoncé

Tout échange intersectoriel doit être couvert par un accord explicite entre ministères.

#### Rattachement

- [Partition One Health](../../04_architecture-repository/01_partitions/sectorielles/part-one-health.md)
- [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données](../../04_architecture-repository/03_requirements/enf-4.md)

**Statut : candidate**

### Les identités humaines ne doivent jamais être croisées avec les identités animales.

#### Énoncé

Les identités humaines ne doivent jamais être croisées avec les identités animales.

#### Rattachement

- [Partition One Health](../../04_architecture-repository/01_partitions/sectorielles/part-one-health.md)
- [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données](../../04_architecture-repository/03_requirements/enf-4.md)

**Statut : candidate**

### Les données agrégées croisées doivent être irréversiblement désanonymisées.

#### Énoncé

Les données agrégées croisées doivent être irréversiblement désanonymisées.

#### Rattachement

- [Partition One Health](../../04_architecture-repository/01_partitions/sectorielles/part-one-health.md)
- [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données](../../04_architecture-repository/03_requirements/enf-4.md)

**Statut : candidate**

### Chaque secteur conserve la souveraineté sur ses données source.

#### Énoncé

Chaque secteur conserve la souveraineté sur ses données source.

#### Rattachement

- [Partition One Health](../../04_architecture-repository/01_partitions/sectorielles/part-one-health.md)
- [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données](../../04_architecture-repository/03_requirements/enf-4.md)

**Statut : candidate**

### Les dimensions d'agrégation communes doivent être normalisées.

#### Énoncé

Les dimensions d'agrégation communes doivent être normalisées.

#### Rattachement

- [Partition One Health](../../04_architecture-repository/01_partitions/sectorielles/part-one-health.md)
- [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données](../../04_architecture-repository/03_requirements/enf-4.md)

**Statut : candidate**

### Tous les échanges intersectoriels doivent être journalisés et auditables.

#### Énoncé

Tous les échanges intersectoriels doivent être journalisés et auditables.

#### Rattachement

- [Partition One Health](../../04_architecture-repository/01_partitions/sectorielles/part-one-health.md)
- [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données](../../04_architecture-repository/03_requirements/enf-4.md)

**Statut : candidate**

### Le cadre Tripartite Plus doit être respecté pour les flux internationaux.

#### Énoncé

Le cadre Tripartite Plus doit être respecté pour les flux internationaux.

#### Rattachement

- [Partition One Health](../../04_architecture-repository/01_partitions/sectorielles/part-one-health.md)
- [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données](../../04_architecture-repository/03_requirements/enf-4.md)

<!-- END:GENERATED -->

<!-- BEGIN:GENERATED source=04_architecture-repository/05_building-blocks/abb/abb-echange-logistique-lmis.md,04_architecture-repository/02_architecture-elements/data/reference-data/rd-donnees-environnementales-climat.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Statut : candidate**

### Échange logistique LMIS

#### Finalité

Permettre l'interopérabilité des données de la chaîne d'approvisionnement sanitaire (médicaments, vaccins, intrants, équipements) : catalogue produit partagé, niveaux de stock, lots et traçabilité des mouvements, afin d'éviter les ruptures et les péremptions.

#### Services attendus

- catalogue produit normalisé (désignation, code, unité, seuils) ;
- remontée des niveaux de stock par établissement ;
- traçabilité des lots et des mouvements (réception, transfert, distribution) ;
- alerte de rupture et de péremption ;
- corrélation stock vers consommation vers épidémiologie.

#### Principe de séparation

Ce bloc normalise l'échange et la traçabilité inter-initiatives. Il ne remplace pas le système métier de gestion des stocks.

#### Principes associés

- [P-INT-03: Copies locales non autoritatives](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-03.md)
- [P-INT-07: Responsabilité de la donnée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-07.md)
- [P-INT-18: Traçabilité différenciée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-18.md)

#### Rattachement

- [CMP-23: Chaîne logistique LMIS](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-23.md)
- [ART-10: Logistique](../../04_architecture-repository/04_patterns/artsn-rules/art-10.md)

**Statut : candidate**

### Données environnementales et de résilience climatique

#### Finalité

Permettre l'interopérabilité des données environnementales et climatiques utiles à la santé publique (climat, qualité de l'air ou de l'eau, biodiversité, événements extrêmes) avec les secteurs environnement, agriculture, météorologie et intérieur, dans le cadre One Health.

#### Services attendus

- référentiel spatio-temporel partagé (espace, temps, géographie) ;
- échange des indicateurs environnementaux et climatiques normalisés ;
- corrélation des signaux environnementaux et épidémiologiques ;
- alertes conjointes santé, environnement et climat.

#### Principe de séparation

Cet élément de données de référence porte spécifiquement la dimension environnementale et climatique normalisée. Il complète la coordination intersectorielle One Health sans créer de référentiel maître intersectoriel non gouverné.

#### Principes associés

- [P-INT-01: Autorité désignée](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-01.md)
- [P-INT-10: Accord préalable](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-10.md)
- [P-INT-16: Résidence et non-réplication](../../04_architecture-repository/02_architecture-elements/motivation/principles/p-int-16.md)

#### Rattachement

- [Partition One Health](../../04_architecture-repository/01_partitions/sectorielles/part-one-health.md)
- [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données](../../04_architecture-repository/03_requirements/enf-4.md)
- [ART-4D: Référentiel géospatial et d'exploitation partagé](../../04_architecture-repository/04_patterns/artsn-rules/art-4d.md)

<!-- END:GENERATED -->

## Références

- **annexe B** : Annexe B : Articulation avec l'ARTSN (`01_cnisn/08_annexes/b-articulation-art-sn.md`)
