---
title: "Annexe H : Benchmark de maturité ADHMAT et trajectoire du SNS numérique"
id: adhmat-benchmark
domain: 08_annexes
version: "1.0.0"
status: draft
last_reviewed: 2026-08-26
owner: DEPSI
tags: ["artsn", "annexes", "adhmat", "maturite", "africa-cdc", "benchmark"]
---

# Annexe H : Benchmark de maturité ADHMAT et trajectoire du SNS numérique

L'**ADHMAT** (*African Digital Health Maturity Assessment Tool*) est l'outil d'évaluation de maturité du système de santé numérique porté par l'Africa CDC (avec l'OMS et la Banque mondiale). Il structure la maturité en **7 domaines** et produit un score global indicatif permettant de situer un pays et de planifier sa trajectoire d'investissement.

Cette annexe répond à la question : *où Madagascar se situe-t-il sur le modèle ADHMAT, quels gaps l'HEA comble, et quelle trajectoire de score est attendue le long des plateaux/lots ARTSN ?* Elle prolonge l'annexe G (source internationale OMS/ITU) en descendant au niveau de l'évaluation de maturité continentale.

> **Nature de l'évaluation.** Le score ci-dessous est une **auto-évaluation indicative** alignée sur le modèle à 7 domaines ADHMAT, réalisée dans le cadre de l'élaboration de l'HEA. Elle ne constitue pas la soumission officielle Africa CDC ; elle sert de référence de cohérence pour la feuille de route ARTSN.

## 1. Évaluation ADHMAT — 7 domaines (Madagascar, indicative)

| # | Domaine ADHMAT | Score indicatif | Niveau | Forces / faiblesses principales |
|---|----------------|-----------------|--------|----------------------------------|
| 1 | Gouvernance | 70 % | Défini | CNASN désigné, instances sectorielles en place ; manque de pouvoir d'homologation opposable |
| 2 | Stratégie & investissement | 65 % | Défini | Feuille de route ARTSN (L1–L7) et enveloppe TCO posées ; financement non encore arbitré |
| 3 | Législation & politique | 40 % | Initial | Absence de loi e-santé opposable ; cadre consensuel en cours ([ADR-0010](../../01_cnisn/06_decisions/adr-0010-cadre-legal.md), [avant-projet de loi](../../00_caesn/07_governance/projet-loi-esante.md)) |
| 4 | Workforce | 45 % | Initial | Compétences SIS présentes, mais capacité numérique système non structurée ([workforce numérique](../../00_caesn/03_capabilities/workforce-sante-numerique.md)) |
| 5 | Standards & interopérabilité | 60 % | Défini | CNISN publié (normes + ADR) ; déploiement X-Road/PIXm encore limité |
| 6 | Infrastructure | 35 % | Initial | Hébergement souverain non confirmé ; cloud souverain en cours de cadrage ([ART-7](../../referentiel/chapitres/art-7.md)) |
| 7 | Services numériques | 75 % | Géré | Dossiers, HMIS et analytique relativement matures ; continuité inter-structure fragile |

**Score global indicatif : ~55,6 %** (moyenne des 7 domaines) — profil « analytique fort, socle infra/workforce/législation faible ».

## 2. Gaps ADHMAT et réponse de l'HEA

Chaque domaine faible fait l'objet d'une réponse directe dans le document HEA :

| Domaine faible | Gap ADHMAT | Réponse dans l'HEA |
|----------------|------------|--------------------|
| Législation & politique (40 %) | Pas de base légale opposable | [ADR-0010](../../01_cnisn/06_decisions/adr-0010-cadre-legal.md) + [avant-projet de loi e-santé](../../00_caesn/07_governance/projet-loi-esante.md) ; [fondement légal CAESN](../../00_caesn/07_governance/fondement-legal.md) |
| Workforce (45 %) | Capacité numérique non structurée | Nouveau document [workforce numérique](../../00_caesn/03_capabilities/workforce-sante-numerique.md) ; référencé par [instances sectorielles](../../00_caesn/07_governance/instances-sectorielles.md) |
| Infrastructure (35 %) | Hébergement souverain non confirmé | Sous-section « Hébergement souverain et cloud souverain » de [ART-7](../../referentiel/chapitres/art-7.md) (réf [STD-0002](../../01_cnisn/05_standards/std-0002-securite-chiffrement.md)) ; [plateforme PHC](../../00_caesn/07_governance/instances-sectorielles.md) |
| Gouvernance (70 %) | Pouvoir d'homologation à confirmer | [Table de maturité](a-table-de-maturite.md) utilise ADHMAT comme grille de M&E ; CNASN (PA-05) |
| Stratégie & investissement (65 %) | Financement non arbitré | [Méthode TCO et enveloppe L1–L7](../../00_caesn/06_portfolio/financement-tco.md) |

## 3. Trajectoire de score attendue (par plateau / lot)

La feuille de route ARTSN ([lots L1–L7](../07_lots/index.md)) est ordonnée pour lever les domaines faibles en priorité, puis consolider les domaines forts :

| Phase / plateau | Lots | Domaines ADHMAT levés | Score global attendu |
|-----------------|------|------------------------|----------------------|
| PL-1 (socle légal & capacités) | L1, L2 | Législation & politique, Workforce, Gouvernance | ~62 % |
| PL-2 (interop & infra souveraine) | L3, L4, L5 | Standards & interopérabilité, Infrastructure | ~70 % |
| PL-3 (services & intégration) | L6, L7 | Services numériques, intégration GDHCN | ~75–80 % |

Cible à 3 ans : **passage du niveau « Initial/Défini » (~55 %) au niveau « Géré/Optimisé » (~75–80 %)**, soit un gain d'environ 20 à 25 points, principalement tiré par la consolidation de l'infrastructure souveraine et de la base légale.

## 4. Suivi

L'évaluation doit être réitérée à chaque changement de plateau (voir [gaps](../07_lots/index.md) et [table de maturité](a-table-de-maturite.md)) pour mesurer le gain effectif et ajuster la feuille de route. L'outil ADHMAT (Africa CDC) reste la référence de mesure officielle.

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **Feuille de route ARTSN** : Feuille de route de déploiement (`../07_lots/index.md`)
- **Table de maturité** : Annexe A (`a-table-de-maturite.md`)
- **Avant-projet de loi e-santé** : (`../../00_caesn/07_governance/projet-loi-esante.md`)
- **Workforce numérique** : (`../../00_caesn/03_capabilities/workforce-sante-numerique.md`)
- **Méthode TCO** : (`../../00_caesn/06_portfolio/financement-tco.md`)
- **ADHMAT** : African Digital Health Maturity Assessment Tool — Africa CDC (`https://africacdc.org/`)
