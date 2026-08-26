---
title: "Méthode TCO et enveloppe de financement du portefeuille"
id: financement-tco
domain: 06_portfolio
version: "1.1.0"
status: draft
last_reviewed: 2026-08-26
owner: Bureau de Réalisation de la Valeur
tags: ["portefeuille", "financement", "tco", "investissement", "adhmat", "budget"]
---

# Méthode TCO et enveloppe de financement du portefeuille

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ◐ |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## Objet et lacune comblée

Le [portefeuille](index.md) définit un registre national des initiatives dont le champ « coût total de possession » (TCO) est prévu mais non renseigné. L'évaluation **ADHMAT** (Africa CDC) de Madagascar recommande explicitement un *costed national implementation roadmap and financing plan*. Ce document comble le gap en fixant la méthode TCO, les hypothèses de coûts par lot et la gouvernance budgétaire associée.

## Méthode TCO

Le **coût total de possession** d'une initiative est estimé sur un **horizon de 5 à 7 ans** (durée de vie typique d'une infrastructure numérique de santé), selon la formule :

```
TCO = CapEx + Σ(OpEx_année) − Valeur_résiduelle, le tout actualisé (taux d'actualisation ~ 8–10 %)
```

| Composante | Nature | Périodicité | Contenu |
|------------|--------|-------------|---------|
| **CapEx** (investissement) | Unique | À l'amorçage | Serveurs, licences, connexions, hébergement souverain ([ART-7](../../referentiel/chapitres/art-7.md)), équipements |
| **OpEx** (exploitation) | Récurrente | Annuelle | Maintenance, connectivité, licences récurrentes ([STD-0007 SNOMED CT](../../01_cnisn/05_standards/std-0007-snomed-ct.md)), hébergement, support |
| **Hommes** | Récurrente | Annuelle | Formation, certification et rémunération du [workforce numérique](../03_capabilities/workforce-sante-numerique.md) |
| **Conduite de changement** | Mixte | Par phase | Gestion du changement, accompagnement métier, conduite de bénéfices, communication |
| **Conformité** | Récurrente | Annuelle | Audit, certification des profils, homologation (voir [loi e-santé](../07_governance/projet-loi-esante.md), Art. 17) |

Le TCO est renseigné **par lot** (L1–L7) et agrégé au niveau du portefeuille. Les coûts d'infrastructures *partagées* (L1, L3) sont mutualisés et répartis en charge sur les lots consommateurs pour éviter la double comptabilité.

## Hypothèses de coûts par lot (indicatif)

| Plateau / Lot | Postes de coût principaux | Part relative du TCO* | Hypothèse de mutualisation |
|---------------|---------------------------|------------------------|----------------------------|
| L1 — Infrastructure & sécurité | Hébergement souverain, X-Road, chiffrement ([STD-0002](../../01_cnisn/05_standards/std-0002-securite-chiffrement.md)) | Forte (socle) | Infra partagée, amortie sur tous les lots |
| L2 — Applications terrain | Dossier patient, terminologies, licences | Moyenne | Par formation sanitaire |
| L3 — Médiation & registres | Couche d'échange, registres, identité (PIXm/PDQm) | Forte | Infra partagée |
| L4 — Analytique & pilotage | Entrepôt, tableaux de bord, calcul/storage | Moyenne | Mutualisée (plateau analytique) |
| L5 — Extension & pérennisation | Consentement ([ADR-0005](../../01_cnisn/06_decisions/adr-0005-consentement.md)), formation, support | Moyenne | Par programme |
| L6 — Interopérabilité transfrontalière | Passerelle GDHCN, conformité | Faible | Mutualisée (un seul point d'entrée) |
| L7 — Coordination One Health | Graphe, crise, intégration intersectorielle | Faible | Mutualisée |

> *Part relative indicative (à affiner avec les ministères et partenaires) ; l'objectif est de hiérarchiser l'enveloppe, non de figer des montants. Les montants définitifs seront établis en cadrage [BRV](index.md) et soumis au CNASN.

## Devis indicatif par lot (ordre de grandeur)

Le tableau ci-dessous traduit les hypothèses en **enveloppes chiffrées d'ordre de grandeur** (MGA — milliards d'Ariary ; 1 USD ≈ 4 500 MGA), sur un horizon de 7 ans. Il sert au cadrage budgétaire et à la hiérarchisation de l'enveloppe ; il **ne fige aucun montant** et sera affiné en cadrage [BRV](index.md). Les lots à infrastructure *partagée* (L1, L3) portent le CapEx le plus élevé car mutualisé sur tous les lots.

| Lot | CapEx (Md MGA) | OpEx annuel (Md MGA) | TCO 7 ans (Md MGA) | ≈ USD (M) |
|-----|----------------|----------------------|--------------------|-----------|
| L1 — Infrastructure & sécurité | 18–25 | 2,5–3,5 | 35–48 | 7,8–10,7 |
| L2 — Applications terrain | 6–9 | 1,2–1,8 | 14–22 | 3,1–4,9 |
| L3 — Médiation & registres | 8–12 | 1,5–2,2 | 18–27 | 4,0–6,0 |
| L4 — Analytique & pilotage | 4–6 | 0,9–1,3 | 10–15 | 2,2–3,3 |
| L5 — Extension & pérennisation | 2–3 | 0,5–0,8 | 5,5–8,5 | 1,2–1,9 |
| L6 — Interopérabilité transfrontalière | 1–2 | 0,3–0,5 | 3–5,5 | 0,7–1,2 |
| L7 — Coordination One Health | 1–2 | 0,3–0,5 | 3–5,5 | 0,7–1,2 |
| **Total indicatif** | **40–59** | **7,2–10,6 / an** | **88–131** | **19,6–29,1** |

Ces estimations couvrent le coût de possession complet (CapEx + OpEx actualisés, hors valeur résiduelle) et intègrent les postes des référentiels de base (STD-0007 SNOMED CT, licences), du serveur de sécurité X-Road ([STD-0002](../../01_cnisn/05_standards/std-0002-securite-chiffrement.md)) et de la conduite de changement. Le décaissement reste conditionné aux jalons de lot et à la conformité HEA ([ADR-0010](../../01_cnisn/06_decisions/adr-0010-cadre-legal.md)).

## Sources de financement

- **Budget national** : enveloppe e-santé pluriannuelle, alignée sur la [Stratégie de Santé Numérique pour le Développement (SNSD)](../../00_caesn/00_overview/foundations.md) ; inscription dans la loi de finances.
- **Partenaires techniques et financiers** : cofinancements multilatéraux/bilatéraux (IDA, agences, fonds mondiaux) conditionnés à la **conformité HEA** (voir [ADR-0010](../../01_cnisn/06_decisions/adr-0010-cadre-legal.md) et [loi e-santé](../07_governance/projet-loi-esante.md), Art. 16).
- **Programmes verticaux** : coordonnés via le portefeuille pour mutualiser l'infrastructure et éviter la fragmentation (un socle partagé, plusieurs usages).
- **Modalités de décaissement** : décaissement par jalon de lot ARTSN (PL-1 → PL-2 → PL-3), conditionné à l'atteinte des critères de conformité et de maturité ([annexe A](../../02_artsn/08_annexes/a-table-de-maturite.md)).

## Gouvernance budgétaire

La budgetisation est pilotée selon un cycle clair pour garantir l'alignement investissement → valeur :

1. **Programmation** : le [Bureau de Réalisation de la Valeur (BRV)](index.md) établit le plan de financement par lot à partir du TCO et de la [feuille de route des lots du portefeuille](feuille-de-route-lots.md) (dont la [réalisation technique](../../02_artsn/07_lots/index.md) est détaillée en ARTSN).
2. **Arbitrage** : le CNASN homologue le plan (conformité) ; le comité de programmation arbitre la répartition (voir [gouvernance CAESN](../../00_caesn/07_governance/index.md)).
3. **Exécution** : décaissement par jalon, suivi de l'écart budget/réel par lot.
4. **Contrôle** : audit de conformité et certification des profils (PTISN) conditionnent les tranches suivantes.
5. **Révision** : mise à jour annuelle du TCO et de l'enveloppe selon la trajectoire [ADHMAT](../../02_artsn/08_annexes/h-benchmark-adhmat.md).

## Suivi et indicateurs

| Indicateur | Définition | Cible |
|------------|------------|-------|
| Coût par lot (TCO réel vs prévu) | Écart budget/réel | ≤ 10 % |
| TCO par citoyen couvert | Enveloppe / population desservie | Tendance à la baisse (mutualisation) |
| Part financée par partenaires vs État | Mix de financement | Équilibré et conforme |
| Lots conformes certifiés | Profils PTISN homologués | 100 % à PL-3 |

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Portefeuille** : Portefeuille d'initiatives orienté valeur (`index.md`)
- **Feuille de route des lots** : [Lots L1–L7 du portefeuille](feuille-de-route-lots.md) (réalisation technique : [vue ARTSN](../../02_artsn/07_lots/index.md))
- **Loi e-santé** : Avant-projet de loi e-santé (`../07_governance/projet-loi-esante.md`)
- **Workforce numérique** : Capacité numérique système (`../03_capabilities/workforce-sante-numerique.md`)
- **ADHMAT** : Africa CDC — *costed national implementation roadmap and financing plan* (annexe H : `../../02_artsn/08_annexes/h-benchmark-adhmat.md`)
