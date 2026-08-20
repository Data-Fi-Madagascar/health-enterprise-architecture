---

id: ENF-1
type: exigence
niveau: "3"
title: Résilience à l'instabilité réseau
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/02_exigences-contextuelles/index.md
maps_to: []
implements: []
applies_to: []
related: ["F-1", "ART-1", "ART-3", "ART-7", "ART-8C", "ART-4C"]
tags: ["artsn", "niveau-3", "exigence", "ENF-1"]
---
# Résilience à l’instabilité réseau

**Contenu normatif.** La connectivité internet et la couverture mobile (3G/4G/Fibre) sont hautement asymétriques, intermittentes, voire inexistantes dans la majorité des districts ruraux et des Centres de Santé de Base (CSB). L’indisponibilité, la coupure ou la dégradation du réseau ne doit en aucun cas bloquer, ralentir ou altérer l’acte clinique, la dispensation pharmaceutique au comptoir ou la saisie logistique. Tout logiciel et base de données utilisés sur le point de service ont l’obligation structurelle de **capturer, valider et persister les transactions de manière 100 % locale et autonome**, puis de gérer des mécanismes de **synchronisation asynchrone** pour différer la transmission centrale dès le retour de la connectivité.

**Statut : Stable.** — appliqué par [F.1](../fondations/f-1.md), [ART-1](../chapitres/art-1.md), [Couche 2 (point de service)](../../02_artsn/04_cartographie-cible/index.md#couche-2--point-de-service).

## Justification

La connectivité internet et mobile reste asymétrique, intermittente ou absente dans la majorité des districts ruraux et des CSB, rendant les architectures transactionnelles centralisées synchrones inadaptées. Cette exigence protège l’acte clinique, la dispensation et la saisie logistique contre toute coupure réseau en imposant la capture locale autonome et la synchronisation différée. Elle évite la perte ou la duplication d’événements de santé lors des micro-coupures.

## Capabilités concernées

- **CAP-13** — Système d'information sanitaire, données et recherche
- **CAP-14** — Interopérabilité, référentiels nationaux et infrastructure numérique partagée
- **CAP-15** — Cybersécurité, confidentialité et gouvernance des données personnelles

## Parties prenantes concernées

- **PP-05** — Agent de santé
- **PP-06** — Formation sanitaire
- **PP-10** — Équipes techniques (DEPSI / SIS)

## Fondations et chapitres garants

- **F.1** — Résilience face à la réalité géographique du pays
- **ART-1** — Intégration et ingestion
- **ART-3** — Historisation événementielle et profils de déploiement
- **ART-7** — Sécurité, contrôle d'accès et résidence de la donnée
- **ART-8c** — Agrégation par lot
- **ART-4c** — Éligibilité et couverture
