---
domain: togaf
id: VIEW-TOGAF-GAP-CLOSURE-ROADMAP
type: repository-view
niveau: "0"
title: "Vue TOGAF - Feuille de route de fermeture des gaps"
status: draft
owner: DEPSI
version: "0.1"
tags: ["togaf", "gap", "migration", "governance", "repository-view"]
---
# Vue TOGAF - Feuille de route de fermeture des gaps

## Positionnement

Cette vue relie chaque écart de migration à son état opérationnel, sa transition, son plateau cible, ses responsables, ses critères et ses preuves attendues. Elle est entièrement dérivée des objets canoniques et ne constitue pas une seconde source de vérité.

## Trajectoires de fermeture

Chaque ligne se lit comme une chaîne de gouvernance allant de l'état source au plateau cible, avec les paquets de travail chargés de la remédiation et les preuves candidates nécessaires à la clôture.

<!-- BEGIN:GENERATED mode=gap-closure-roadmap -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

| Gap | État | Transition | Plateau cible | Responsable | Work packages | Objets impactés | Critères de clôture | Preuves |
|---|---|---|---|---|---|---|---|---|
| [GAP-01](../../07_migration/gaps/gap-01.md) — Écart — Couverture terrain en zone isolée | planned | [PL-01](../../07_migration/plateaux/pl-01.md) → [GAP-01](../../07_migration/gaps/gap-01.md) → [PL-02](../../07_migration/plateaux/pl-02.md) | [PL-02](../../07_migration/plateaux/pl-02.md) | Direction du Numérique en Santé | [WP-02](../../07_migration/work-packages/wp-02.md) | [CAP-01](../../02_architecture-elements/strategy/capabilities/cap-01.md), [LOC-04](../../02_architecture-elements/business/locations/loc-04.md) | Fonctionnement hors ligne qualifié sur un terrain représentatif de LOC-04<br>Reprise de synchronisation qualifiée<br>Absence de perte critique démontrée | [EVID-GAP-01-QUALIFICATION-OFFLINE](../../06_governance/evidence/evid-gap-01-qualification-offline.md) |
| [GAP-02](../../07_migration/gaps/gap-02.md) — Écart — Interopérabilité transfrontalière & One Health | planned | [PL-02](../../07_migration/plateaux/pl-02.md) → [GAP-02](../../07_migration/gaps/gap-02.md) → [PL-03](../../07_migration/plateaux/pl-03.md) | [PL-03](../../07_migration/plateaux/pl-03.md) | Direction du Numérique en Santé | [WP-06](../../07_migration/work-packages/wp-06.md), [WP-07](../../07_migration/work-packages/wp-07.md) | [ABB-CONFIANCE-AUTORISATION](../../05_building-blocks/abb/abb-confiance-autorisation.md), [ABB-ECHANGE-MEDIATION](../../05_building-blocks/abb/abb-echange-mediation.md), [ABB-EXPOSITION-DONNEES-ANALYTIQUES](../../05_building-blocks/abb/abb-exposition-donnees-analytiques.md), [PT-14](../../05_building-blocks/sbb/legacy-profiles/pt-14.md), [PT-15](../../05_building-blocks/sbb/legacy-profiles/pt-15.md) | Accord de gouvernance disponible pour le périmètre transfrontalier<br>Accord de gouvernance disponible pour le périmètre One Health<br>Contrats d'échange applicables identifiés<br>Échange transfrontalier testé<br>Échange One Health testé<br>Responsabilités et remédiations documentées | [EVID-GAP-02-INTEROPERABILITE-ETENDUE](../../06_governance/evidence/evid-gap-02-interoperabilite-etendue.md) |
| [GAP-03](../../07_migration/gaps/gap-03.md) — Écart — Cadre légal & gouvernance publié | planned | État initial → [GAP-03](../../07_migration/gaps/gap-03.md) → [PL-01](../../07_migration/plateaux/pl-01.md) | [PL-01](../../07_migration/plateaux/pl-01.md) | Direction du Numérique en Santé | [WP-01](../../07_migration/work-packages/wp-01.md) | [ABB-IDENTITE-BENEFICIAIRE](../../05_building-blocks/abb/abb-identite-beneficiaire.md), ADR-0010, [CMP-39](../../06_governance/registers/cmp-39.md) | Cadre CNASN approuvé et publié<br>Charte de protection approuvée et publiée<br>Références officielles enregistrées<br>Pièces utilisables dans le processus d'homologation | [EVID-GAP-03-CADRE-LEGAL](../../06_governance/evidence/evid-gap-03-cadre-legal.md) |

<!-- END:GENERATED -->

## Usage

Cette vue sert aux revues des phases TOGAF E, F et G. Toute correction doit être portée dans les fiches canoniques `GAP-*`, `WP-*`, `PL-*` ou `EVID-*`, puis régénérée.
