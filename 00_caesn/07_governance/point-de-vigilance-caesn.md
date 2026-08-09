---
title: Point de vigilance CAESN — capacité et référentiel manquants pour la coordination intersectorielle (One Health)
id: point-de-vigilance-caesn
domain: 07_governance
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: Comité National d'Architecture Santé Numérique
tags: [gouvernance, vigilance, one-health, capabilites, identitovigilance]
---

# Point de vigilance CAESN — capacité et référentiel manquants pour la coordination intersectorielle (One Health)

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

Cette note est destinée à l'instance de gouvernance du [CAESN](./index.md). Elle documente les écarts constatés lors du peuplement de l'[ARTSN](../../02_artsn/index.md) entre la doctrine exprimée par le document source *[Draft] TECHNICAL-Reference-Architecture-1.pdf* et le catalogue en vigueur du CAESN. Aucun élément du catalogue n'est modifié par cette note : elle porte une **décision à instruire**.

## Contexte

Le document source de l'ARTSN décrit le CAESN comme comportant **18 principes (P-01 à P-18)** et **17 capacités** (dont « CAP-04bis — Engagement patient et identitovigilance »). Le CAESN en vigueur dans ce dépôt recense pour l'instant :

- **12 principes transversaux** (PA-01 à PA-12) + **principes de domaine** (PD-VS01 à PD-VS04) ;
- **16 capabilités** CAP-01 à CAP-16, dans lesquelles CAP-04 est « Santé communautaire et engagement des communautés ».

## Écarts identifiés

### Écart 1 — CAP-04bis « Engagement patient et identitovigilance »

L'ARTSN rattache [ART-4a (résolution d'identité)](../../02_artsn/03_chapitres/art-4a-resolution-identite.md) et [ART-4b (bases d'autorisation)](../../02_artsn/03_chapitres/art-4b-bases-autorisation.md) à une capabilité **CAP-04bis « Engagement patient et identitovigilance »**. Le catalogue CAESN ne comporte pas cette capabilité : CAP-04 est « Santé communautaire », et aucune capabilité ne couvre explicitement l'identitovigilance probabilitique ni l'engagement du patient dans le système numérique.

**Impact pour l'ARTSN** : l'Architecture de référence technique suppose une capabilité absente du CAESN. La promotion des chapitres 4a/4b vers un statut Stable exige au préalable l'arbitrage de cette capabilité.

## Écart 2 — Capacité candidate « Coordination intersectorielle »

L'ARTSN rattache [ART-0 (accords de partage inter-institutionnels)](../../02_artsn/03_chapitres/art-0-accords-partage.md) et [ART-8d (chorégraphie inter-institutionnelle)](../../02_artsn/03_chapitres/art-8d-choregraphie-interinstitutionnelle.md) à une **capacité candidate « Coordination intersectorielle »** (One Health), absente du catalogue CAP-01..16.

### Écart 3 — Référentiel normatif « Tripartite Plus » (OMS-WOAH-FAO-PNUE, RSI)

La coordination intersectorielle s'appuie sur un référentiel normatif international : **Tripartite Plus OMS–WOAH–FAO–PNUE** et le **Règlement Sanitaire International (RSI)**. Ce référentiel n'est pas intégré au [registre des normes](../09_standards/index.md) du CAESN, alors qu'il conditionne la surveillance épidémique conjointe (ENF-4).

### Écart 4 — Capacité candidate « Surveillance spatio-temporelle »

[ART-4d (référentiel géospatial et d'exploitation partagé)](../../02_artsn/03_chapitres/art-4d-referentiel-geospatial.md) est rattaché à une capacité candidate « Surveillance spatio-temporelle » absente du catalogue, nécessaire au cloisonnement One Health.

### Écart 5 — Compte des principes : 18 dans le document source vs PA+PD dans le catalogue

Le document source annonce **18 principes (P-01 à P-18)** ; le catalogue en vigueur structure les principes en **12 transversaux (PA)** + **principes de domaine (PD) par flux**. L'écart peut être une différence de numérotation (vote de la nomenclature) ou un périmètre réel à trancher : faut-il ajouter des principes transversaux, ou aligner la nomenclature du document source sur le CAESN ?

## Décisions à instruire

| # | Décision attendue de l'instance de gouvernance |
|---|------------------------------------------------|
| D-1 | Créer ou non la capabilité **CAP-04bis « Engagement patient et identitovigilance »** (ou la rattacher à une sous-composante de CAP-04) |
| D-2 | Créer la capabilité **« Coordination intersectorielle (One Health) »** ou intégrer sa responsabilité dans CAP-05 |
| D-3 | Inscrire le référentiel **Tripartite Plus / RSI** au registre des normes |
| D-4 | Créer la capacité **« Surveillance spatio-temporelle »** et préciser son propriétaire |
| D-5 | Arbitrer la nomenclature des principes (18 P-01..18 vs 12 PA + PD) |

## Suivi

Cette note est consignée dans le dossier [gouvernance](./index.md) et référencée par l'[Annexe C de l'ARTSN](../../02_artsn/07_annexes/c-renvoi-capacites-candidates.md). Son statut reste **draft** tant que l'instance de gouvernance n'a pas statué.

Lorsqu'une décision D-1 à D-5 entre en instruction, elle fait l'objet d'un [ADR (Architecture Decision Record)](../08_decisions/index.md) au statut `proposé`, puis `accepté` ou `appliqué` après arbitrage du Comité National d'Architecture Santé Numérique. Chaque ADR référencera cette note comme source de l'écart constaté.

## Liens

- [CAESN — capabilités](../03_capabilities/index.md)
- [CAESN — normes et standards](../09_standards/index.md)
- [CAESN — registre des ADR](../08_decisions/index.md)
- [ARTSN — Annexe C (renvoi CAESN)](../../02_artsn/07_annexes/c-renvoi-capacites-candidates.md)
- [ARTSN — chapitres ART-0, 4a, 4b, 4d, 8d](../../02_artsn/03_chapitres/index.md)