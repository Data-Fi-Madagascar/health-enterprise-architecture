---
domain: exigences

id: ENF-5
type: exigence
niveau: "3"
title: Coordination des processus complexes décentralisés et asynchrones
status: draft
owner: DEPSI
version: "0.1"
envelope: 02_artsn/02_exigences-contextuelles/index.md
maps_to: []
implements: []
applies_to: []
related: ["ART-8A", "ART-8", "ART-5", "PT-14"]
tags: ["artsn", "niveau-3", "exigence", "ENF-5"]
---
# Coordination des processus complexes décentralisés et asynchrones

**Contraintes contextuelles.** Les parcours de soins critiques (référence d'un CSB rural vers un hôpital de district, contre-référence ascendante vers un CHU central, ou évacuation sanitaire internationale) s'étendent sur des fenêtres temporelles de plusieurs jours et impliquent des structures sanitaires autonomes sans lien hiérarchique ou technique direct.

**Contenu normatif.** Le système national doit être capable de suivre et d'orchestrer l'état d'avancement d'un parcours de soins distribué à étapes multiples, de bout en bout. L'architecture doit tolérer les interruptions temporaires de transmission, tout en garantissant le déclenchement automatique d'alertes d'escalade ou d'annulations (compensations) fonctionnelles si un établissement de destination est saturé ou inaccessible.

**Statut : Stable.** — appliqué par [ART-8a (orchestration de processus borné)](../chapitres/art-8a.md), [ART-5 (qualité des données)](../chapitres/art-5.md), [PT-14 (interopérabilité transfrontalière)](../../03_ptisn/03_profils/pt-14-interopabilite-transfrontaliere.md).

## Justification

Les parcours de soins critiques s’étendent sur plusieurs jours et impliquent des structures autonomes sans lien hiérarchique ou technique direct. Cette exigence permet de suivre et d’orchestrer un parcours distribué de bout en bout tout en tolérant les interruptions de transmission. Elle garantit le déclenchement d’alertes d’escalade ou de compensations si une structure de destination est saturée ou inaccessible.

## Capabilités concernées

- [CAP-02: Gestion du parcours patient, référence et contre-référence](../capabilites/cap-02.md) — Gestion du parcours patient, référence et contre-référence
- [CAP-13: Système d'information sanitaire, données et recherche](../capabilites/cap-13.md) — Système d'information sanitaire, données et recherche
- [CAP-16: Gestion du portefeuille d'initiatives numériques](../capabilites/cap-16.md) — Gestion du portefeuille d'initiatives numériques

## Parties prenantes concernées

- [PP-01: Patient et usager](../parties-prenantes/pp-01.md) — Patient et usager
- [PP-05: Agent de santé](../parties-prenantes/pp-05.md) — Agent de santé
- [PP-06: Formation sanitaire](../parties-prenantes/pp-06.md) — Formation sanitaire

## Fondations et chapitres garants

- **ART-8a** — Orchestration de processus borné
- [ART-8: Orchestration de processus](../chapitres/art-8.md) — Orchestration de processus
- [ART-5: Cohérence et qualité des données](../chapitres/art-5.md) — Cohérence et qualité des données
- [PT-14: Interopérabilité transfrontalière](../profils/pt-14.md) — Interopérabilité transfrontalière
