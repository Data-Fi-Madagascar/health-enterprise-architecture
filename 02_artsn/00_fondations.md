---
title: Fondations invariantes
id: artsn-fondations
domain: 02_artsn
version: "0.1.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, fondations, invariants, niveau-3]
---

# Fondations invariantes

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](reading-matrix.md).

Les fondations invariantes constituent le **socle** sur lequel s'appuient tous les chapitres de l'ARTSN. Elles sont la partie la plus stable de l'architecture de référence et ne devraient être révisées qu'exceptionnellement. Elles émanent de la doctrine souveraine d'urbanisation de l'État de Madagascar et s'alignent sur les directives stratégiques du [CAESN](../00_caesn/00_overview/index.md). Sur le plan international, elles traduisent les meilleures pratiques portées par OpenHIE (interopérabilité des systèmes de santé) et GovStack (sous l'égide de l'UIT).

Dans la hiérarchie des normes du Système National d'Information de Santé (SNIS), la Partie I fait office de **bloc de constitutionnalité technique** : ces règles s'imposent de manière absolue, universelle et transversale à l'ensemble des couches de la plateforme, ainsi qu'à tout système périphérique, ministériel ou international tiers qui ambitionne de s'y connecter.

## F.1 — Résilience face à la réalité géographique du pays

**Contenu normatif.** Les contraintes d'infrastructure de Madagascar (zones rurales isolées, instabilité énergétique, connectivité asymétrique et intermittente au niveau des districts) imposent d'abandonner les mécanismes transactionnels centralisés synchrones. Pour garantir qu'aucun événement de santé ne soit perdu ou dupliqué lors d'une coupure réseau, l'État érige en obligations légales strictes :

1. **Immuabilité et idempotence à la source** : tout point de service doit déployer un journal d'événements immuable (*append-only*) où aucune modification ou suppression n'est permise, autorisant le rejeu complet des calculs.
2. **Déduplication par clé d'idempotence** générée localement, protégeant le système contre les renvois successifs d'un même paquet.

Cette discipline devient **existentielle** dès lors qu'une source échappe à la gouvernance directe de l'initiative (ruptures de connectivité, serveurs de districts ou tablettes isolés) : seule elle permet de garantir la traçabilité absolue et la transmission asynchrone résiliente sans rompre le pipeline.

**Statut : Stable.**

## F.2 — Préservation de la souveraineté intersectorielle

**Contenu normatif.** L'intégration des flux avec des ministères autonomes (Intérieur pour l'État Civil, Finances pour le tiers-payant, Élevage pour les zoonoses) exige des contrats d'interfaces techniques **d'égal à égal**. Le versionnement sémantique obligatoire des schémas protège chaque département contre les ruptures de service causées par les modifications applicatives de ses partenaires. Techniquement :

- tout événement échangé est adossé à un **schéma publié dans un registre commun** ;
- contrôle de compatibilité **ascendante et descendante** ;
- gestion explicite de la **dépréciation** des versions ;
- désignation d'un **propriétaire fonctionnel** par type d'événement.

Discipline **existentielle** pour absorber un changement de structure décidé unilatéralement par un tiers sans rompre le pipeline.

**Statut : Stable.**

## F.3 — Éradication des silos technologiques

**Contenu normatif.** Pour mettre fin à la fragmentation historique du paysage numérique sanitaire (multiplicité de logiciels propriétaires incompatibles importés de manière non coordonnée), le Comité National impose un cadre d'homologation obligatoire : **aucun système ne peut interagir avec la plateforme sans prouver son rattachement explicite à une capacité d'État documentée**. Techniquement, toute solution applicative doit :

- **mapper ses flux de données sur les capacités officielles du CAESN** ;
- s'appuyer sur des **référentiels de référence validés** (type OpenHIE ou GovStack).

Discipline **existentielle** : elle seule permet au Comité National (CNASN) de bloquer à la périphérie les solutions non conformes et d'imposer un alignement architectural strict avant l'octroi des clés d'accès sur l'API Gateway.

**Statut : Stable.**

## F.4 — Homologation obligatoire

**Contenu normatif.** Le processus d'homologation obligatoire (introduit en F.3) s'applique à toute solution ; un constat d'homologation qui révélerait qu'un composant ne peut être rattaché à aucun chapitre existant déclenche une revue de l'ARTSN (voir [Gouvernance](./06_gouvernance.md)).

**Statut : Stable.**

## Liens

- [Flux de valeur](./01_flux-de-valeur.md)
- [Exigences contextuelles nationales](./02_exigences-contextuelles.md)
- [Chapitres et patterns de référence](./03_chapitres/index.md)
- [CAESN — principes](../00_caesn/02_principles/index.md)
