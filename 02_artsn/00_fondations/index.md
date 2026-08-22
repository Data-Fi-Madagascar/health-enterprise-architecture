---

title: "Fondations de l'ARTSN"
id: artsn-fondations
domain: 00_fondations
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: ["artsn", "fondations", "catalogue", "niveau-3"]
---

# Fondations de l'ARTSN

## Pour qui lire ce document

**Niveau :** niveau 3 : Architecture de Référence Technique de la Santé Numérique.

Ce document s'adresse prioritairement aux décideurs institutionnels et aux équipes DEPSI/techniques, qui doivent en assurer la compréhension et l'application. Les directions métier, les programmes, les responsables SIS/données/suivi-évaluation, ainsi que les partenaires techniques et financiers y trouvent un complément utile à leur compréhension de l'architecture. La vue d'ensemble de ces priorités de lecture est disponible dans la matrice de lecture. Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle.

Les fondations invariantes constituent le **socle** sur lequel s'appuient tous les chapitres de l'ARTSN. Elles sont la partie la plus stable de l'architecture de référence. Chaque fondation vit dans le référentiel : `referentiel/fondations/f-X.md`.

## Catalogue des fondations

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Résilience face à la réalité géographique du pays

**Contenu normatif.** Les contraintes d’infrastructure de Madagascar (zones rurales isolées, instabilité énergétique, connectivité asymétrique et intermittente au niveau des districts) imposent d’abandonner les mécanismes transactionnels centralisés synchrones. Pour garantir qu’aucun événement de santé ne soit perdu ou dupliqué lors d’une coupure réseau, l’État érige en obligations légales strictes :

1. **Immuabilité et idempotence à la source** : tout point de service doit déployer un journal d’événements immuable (*append-only*) où aucune modification ou suppression n’est permise, autorisant le rejeu complet des calculs.
2. **Déduplication par clé d’idempotence** générée localement, protégeant le système contre les renvois successifs d’un même paquet.

Cette discipline de **mise en œuvre** s’impose dès lors qu’une source échappe à la gouvernance directe de l’initiative (ruptures de connectivité, serveurs de districts ou tablettes isolés) : seule elle permet de garantir la traçabilité absolue et la transmission asynchrone résiliente sans rompre le pipeline.

**Statut : Stable.**

### Préservation de la souveraineté intersectorielle

**Contenu normatif.** L’intégration des flux avec des ministères autonomes (Intérieur pour l’État Civil, Finances pour le tiers-payant, Élevage pour les zoonoses) exige des contrats d’interfaces techniques **d’égal à égal**. Le versionnement sémantique obligatoire des schémas protège chaque département contre les ruptures de service causées par les modifications applicatives de ses partenaires. Techniquement :

- tout événement échangé est adossé à un **schéma publié dans un registre commun** ;
- contrôle de compatibilité **ascendante et descendante** ;
- gestion explicite de la **dépréciation** des versions ;
- désignation d’un **propriétaire fonctionnel** par type d’événement.

Discipline de **mise en œuvre** pour absorber un changement de structure décidé unilatéralement par un tiers sans rompre le pipeline.

**Statut : Stable.**

### Éradication des silos technologiques

**Contenu normatif.** Pour mettre fin à la fragmentation historique du paysage numérique sanitaire (multiplicité de logiciels propriétaires incompatibles importés de manière non coordonnée), le Comité National impose un cadre d’homologation obligatoire : **aucun système ne peut interagir avec la plateforme sans prouver son rattachement explicite à une capacité d’État documentée**. Techniquement, toute solution applicative doit :

- **mapper ses flux de données sur les capacités officielles du CAESN** ;
- s’appuyer sur des **référentiels de référence validés** (type OpenHIE ou GovStack).

Discipline de **mise en œuvre** : elle seule permet au Comité National (CNASN) de bloquer à la périphérie les solutions non conformes et d’imposer un alignement architectural strict avant l’octroi des clés d’accès sur l’API Gateway.

**Statut : Stable.**

### Homologation obligatoire

**Contenu normatif.** Le processus d’homologation obligatoire (introduit en F.3) s’applique à toute solution ; un constat d’homologation qui révélerait qu’un composant ne peut être rattaché à aucun chapitre existant déclenche une revue de l’ARTSN (voir [Gouvernance](../06_gouvernance/index.md)).

**Statut : Stable.**

### Protection et minimisation

**Contenu normatif.** La protection des données de santé ne repose pas sur la captation massive mais sur la minimisation : l'architecture impose de ne collecter, traiter et conserver que les données strictement nécessaires à la finalité documentée. La résidence de la donnée sur le territoire national et la non-réplication hors du périmètre autorisé sont des obligations : chaque flux précise sa finalité, sa base légale et sa durée de conservation, et tout traitement excédant le besoin est proscrit.

**Discipline de mise en œuvre.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (systèmes partenaires, prestataires, terrains) : elle seule permet de limiter l'exposition des données de santé en cas de fuite ou de compromission et de respecter la loi sans rompre le pipeline.

- **Rattachement** : [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../../referentiel/capabilites/cap-15.md) (cybersécurité, confidentialité, gouvernance des données personnelles).
- **Déduit selon** : [P-INT-16: Résidence et non-réplication](../../referentiel/principes/p-int-16.md) (résidence et non-réplication), [P-INT-17: Minimisation](../../referentiel/principes/p-int-17.md) (minimisation).
- **Statut : Provisoire.**

### Observabilité

**Contenu normatif.** La conduite du système sanitaire numérique exige une observabilité continue de bout en bout : événements, flux, traitements et accès doivent être tracés selon des niveaux différenciés (métadonnées de traçabilité, journaux d'audit immuables, indicateurs de fonctionnement). L'architecture impose que chaque composant expose des signaux de santé opérationnelle (disponibilité, latence, taux d'erreur, complétude des flux) exploitables par l'entrepôt national de données et les tableaux de bord.

**Discipline de mise en œuvre.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (systèmes partenaires, périphérie) : elle seule permet de détecter, diagnostiquer et corriger les défaillances d'un pipeline distribué et asynchrone sans rompre le pipeline.

- **Rattachement** : [CAP-13: Système d'information sanitaire, données et recherche](../../referentiel/capabilites/cap-13.md) (SIS, données, analytique).
- **Déduit selon** : [P-INT-18: Traçabilité différenciée](../../referentiel/principes/p-int-18.md) (traçabilité différenciée).
- **Statut : Provisoire.**

<!-- END:GENERATED -->

## Liens

Pour approfondir les fondations de l'ARTSN, les lecteurs peuvent consulter les exigences contextuelles nationales, les chapitres et patterns de référence ainsi que la cartographie cible.

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **exigences contextuelles nationales** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
- **chapitres et patterns de référence** : Chapitres et patterns de référence (`02_artsn/03_chapitres/index.md`)
- **cartographie cible** : Cartographie conceptuelle cible (`02_artsn/04_cartographie-cible/index.md`)
