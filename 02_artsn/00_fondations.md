---
title: "Fondations de l'ARTSN"
id: artsn-fondations
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, fondations, catalogue, niveau-3]
---

# Fondations de l'ARTSN

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](./reading-matrix.md).


Les fondations invariantes constituent le **socle** sur lequel s'appuient tous les chapitres de l'ARTSN. Elles sont la partie la plus stable de l'architecture de référence. Chaque fondation vit dans le référentiel : `referentiel/fondations/f-X.md`.

## Catalogue des fondations

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

### F.1 — Résilience face à la réalité géographique du pays

**Contenu normatif.** Les contraintes d’infrastructure de Madagascar (zones rurales isolées, instabilité énergétique, connectivité asymétrique et intermittente au niveau des districts) imposent d’abandonner les mécanismes transactionnels centralisés synchrones. Pour garantir qu’aucun événement de santé ne soit perdu ou dupliqué lors d’une coupure réseau, l’État érige en obligations légales strictes :

1. **Immuabilité et idempotence à la source** : tout point de service doit déployer un journal d’événements immuable (*append-only*) où aucune modification ou suppression n’est permise, autorisant le rejeu complet des calculs.
2. **Déduplication par clé d’idempotence** générée localement, protégeant le système contre les renvois successifs d’un même paquet.

Cette discipline devient **existentielle** dès lors qu’une source échappe à la gouvernance directe de l’initiative (ruptures de connectivité, serveurs de districts ou tablettes isolés) : seule elle permet de garantir la traçabilité absolue et la transmission asynchrone résiliente sans rompre le pipeline.

**Statut : Stable.**

*Rattachement : [ENF-1](../referentiel/exigences/enf-1.md), [CAP-08](../referentiel/capabilites/cap-08.md) · [fiche](../referentiel/fondations/f-1.md)*

### F.2 — Préservation de la souveraineté intersectorielle

**Contenu normatif.** L’intégration des flux avec des ministères autonomes (Intérieur pour l’État Civil, Finances pour le tiers-payant, Élevage pour les zoonoses) exige des contrats d’interfaces techniques **d’égal à égal**. Le versionnement sémantique obligatoire des schémas protège chaque département contre les ruptures de service causées par les modifications applicatives de ses partenaires. Techniquement :

- tout événement échangé est adossé à un **schéma publié dans un registre commun** ;
- contrôle de compatibilité **ascendante et descendante** ;
- gestion explicite de la **dépréciation** des versions ;
- désignation d’un **propriétaire fonctionnel** par type d’événement.

Discipline **existentielle** pour absorber un changement de structure décidé unilatéralement par un tiers sans rompre le pipeline.

**Statut : Stable.**

*Rattachement : [ENF-4](../referentiel/exigences/enf-4.md) · [fiche](../referentiel/fondations/f-2.md)*

### F.3 — Éradication des silos technologiques

**Contenu normatif.** Pour mettre fin à la fragmentation historique du paysage numérique sanitaire (multiplicité de logiciels propriétaires incompatibles importés de manière non coordonnée), le Comité National impose un cadre d’homologation obligatoire : **aucun système ne peut interagir avec la plateforme sans prouver son rattachement explicite à une capacité d’État documentée**. Techniquement, toute solution applicative doit :

- **mapper ses flux de données sur les capacités officielles du CAESN** ;
- s’appuyer sur des **référentiels de référence validés** (type OpenHIE ou GovStack).

Discipline **existentielle** : elle seule permet au Comité National (CNASN) de bloquer à la périphérie les solutions non conformes et d’imposer un alignement architectural strict avant l’octroi des clés d’accès sur l’API Gateway.

**Statut : Stable.**

*Rattachement : [CAP-14](../referentiel/capabilites/cap-14.md) · [fiche](../referentiel/fondations/f-3.md)*

### F.4 — Homologation obligatoire

**Contenu normatif.** Le processus d’homologation obligatoire (introduit en F.3) s’applique à toute solution ; un constat d’homologation qui révélerait qu’un composant ne peut être rattaché à aucun chapitre existant déclenche une revue de l’ARTSN (voir [Gouvernance](06_gouvernance.md)).

**Statut : Stable.**

*Rattachement : [CAP-INT-12](../referentiel/capacites/cap-int-12.md), [CAP-16](../referentiel/capabilites/cap-16.md) · [fiche](../referentiel/fondations/f-4.md)*

### F.5 — Protection et minimisation

**Contenu normatif.** La protection des données de santé ne repose pas sur la captation massive mais sur la minimisation : l'architecture impose de ne collecter, traiter et conserver que les données strictement nécessaires à la finalité documentée. La résidence de la donnée sur le territoire national et la non-réplication hors du périmètre autorisé sont des obligations : chaque flux précise sa finalité, sa base légale et sa durée de conservation, et tout traitement excédant le besoin est proscrit.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (systèmes partenaires, prestataires, terrains) : elle seule permet de limiter l'exposition des données de santé en cas de fuite ou de compromission et de respecter la loi sans rompre le pipeline.

- **Rattachement** : [CAP-15](../referentiel/capabilites/cap-15.md) (cybersécurité, confidentialité, gouvernance des données personnelles).
- **Déduit selon** : [P-INT-16](../referentiel/principes/p-int-16.md) (résidence et non-réplication), [P-INT-17](../referentiel/principes/p-int-17.md) (minimisation).
- **Statut : Provisoire.**

*Rattachement : [CAP-15](../referentiel/capabilites/cap-15.md) · [fiche](../referentiel/fondations/f-5.md)*

### F.6 — Observabilité

**Contenu normatif.** La conduite du système sanitaire numérique exige une observabilité continue de bout en bout : événements, flux, traitements et accès doivent être tracés selon des niveaux différenciés (métadonnées de traçabilité, journaux d'audit immuables, indicateurs de fonctionnement). L'architecture impose que chaque composant expose des signaux de santé opérationnelle (disponibilité, latence, taux d'erreur, complétude des flux) exploitables par l'entrepôt national de données et les tableaux de bord.

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (systèmes partenaires, périphérie) : elle seule permet de détecter, diagnostiquer et corriger les défaillances d'un pipeline distribué et asynchrone sans rompre le pipeline.

- **Rattachement** : [CAP-13](../referentiel/capabilites/cap-13.md) (SIS, données, analytique).
- **Déduit selon** : [P-INT-18](../referentiel/principes/p-int-18.md) (traçabilité différenciée).
- **Statut : Provisoire.**

*Rattachement : [CAP-13](../referentiel/capabilites/cap-13.md) · [fiche](../referentiel/fondations/f-6.md)*

<!-- END:GENERATED -->
## Liens

- [Exigences contextuelles nationales](./02_exigences-contextuelles.md)
- [Chapitres et patterns de référence](./03_chapitres/index.md)
- [Cartographie cible](./04_cartographie-cible.md)
