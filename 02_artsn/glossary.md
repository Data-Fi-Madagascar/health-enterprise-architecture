---
title: Glossaire de l'ARTSN (niveau 3)
id: artsn-glossary
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-09
owner: DEPSI
tags: [artsn, glossaire, terminologie, niveau-3]
---

# Glossaire de l'ARTSN (niveau 3)

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](./reading-matrix.md).

Termes techniques propres à l'ARTSN. Les définitions des patterns mobilisés par les chapitres (event sourcing, CQRS, médiateur, SCD, golden record…) sont détaillées dans l'[Annexe B — Glossaire des patterns](./07_annexes/b-glossaire-patterns.md) ; les termes transverses de l'architecture sont dans le [glossaire du CAESN](../00_caesn/10_annexes/glossary.md).

**Chapitre (ART-)** — Unité normative de la Partie IV de l'ARTSN définissant une règle d'or ou un contrat technique d'interface obligatoire. Les chapitres portent un statut Stable, Provisoire ou Proposition ouverte selon la [table de maturité](./07_annexes/a-table-de-maturite.md).

**Configurations et paramétrages** — Rapport des choix d'implémentation (valeurs, règles, réglages) qui transposent un standard technique dans une solution logicielle donnée, sur un périmètre et un environnement précis.

**Contrat d'interface** — Spécification technique opposable d'un échange entre composants : format, schéma, version du standard, invariants de sécurité et de résidence de la donnée. Le respect du contrat conditionne l'[homologation](../00_caesn/10_annexes/glossary.md).

**Couche applicative** — Niveau logique de la [cartographie cible](./04_cartographie-cible.md) organisant les composants (infrastructure, données, services partagés, applications métier, intégration, présentation) selon des responsabilités séparées.

**Homologation technique** — Contrôle par lequel une solution est vérifiée pour conformité aux standards techniques et aux exigences de sécurité de l'ARTSN avant mise en production, indépendamment des règles d'homologation fonctionnelle du niveau 1.

**Modèle d'hébergement** — Choix d'hébergement (sur site national, cloud souverain, hybride) conforme à l'exigence de [résidence de la donnée](./03_chapitres/art-7-securite-controle-acces.md) et aux fondations du niveau.

**Norme et standard technique** — Spécification technique normative (formats, protocoles, API) retenue par l'ARTSN et opposable lors d'une homologation ; déclinée depuis les standards du [niveau 1](../00_caesn/09_standards/index.md).

**Pattern technique** — Solution réutilisable à niveau de conception d'un problème récurrent d'intégration, de données, de sécurité ou de processus (voir l'[Annexe B](./07_annexes/b-glossaire-patterns.md)).

## Liens

- [Index de l'ARTSN](./index.md)
- [Matrice de lecture de l'ARTSN](./reading-matrix.md)
- [Acronymes de l'ARTSN](./acronyms.md)
- [Annexe B — Glossaire des patterns](./07_annexes/b-glossaire-patterns.md)
- [Glossaire du CAESN (niveau 1)](../00_caesn/10_annexes/glossary.md)