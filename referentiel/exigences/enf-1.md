---
id: enf-1
type: exigence
niveau: "3"
title: ENF-1 — Résilience à l'instabilité réseau
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/02_exigences-contextuelles.md
maps_to: []
implements: []
applies_to: []
related: ["f-1", "art-1", "art-3", "art-7", "art-8c", "art-4c"]
tags: ['artsn', 'niveau-3', 'exigence', 'enf-1']
---
# ENF-1 — Résilience à l’instabilité réseau

**Contenu normatif.** La connectivité internet et la couverture mobile (3G/4G/Fibre) sont hautement asymétriques, intermittentes, voire inexistantes dans la majorité des districts ruraux et des Centres de Santé de Base (CSB). L’indisponibilité, la coupure ou la dégradation du réseau ne doit en aucun cas bloquer, ralentir ou altérer l’acte clinique, la dispensation pharmaceutique au comptoir ou la saisie logistique. Tout logiciel et base de données utilisés sur le point de service a l’obligation structurelle de **capturer, valider et persister les transactions de manière 100% locale et autonome**, puis de gérer des mécanismes de **synchronisation asynchrone** pour différer la transmission centrale dès le retour de la connectivité.

**Statut : Stable.** — appliqué par [F.1](../fondations/f-1.md), [ART-1](../chapitres/art-1.md), [Couche 2 (point de service)](../../02_artsn/04_cartographie-cible/index.md#couche-2--point-de-service).
