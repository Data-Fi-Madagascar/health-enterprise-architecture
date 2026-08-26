---
title: "Feuille de route des lots du portefeuille (déploiement HEA)"
id: feuille-de-route-lots
domain: 06_portfolio
version: "1.0.0"
status: draft
last_reviewed: 2026-08-26
owner: "Direction du Numérique en Santé"
tags: ["portefeuille", "feuille-de-route", "lots", "deploiement", "implementation"]
---

# Feuille de route des lots du portefeuille (déploiement HEA)

## Rôle et source de vérité

Ce document est la **source de vérité** des lots de déploiement **L1–L7** au niveau du
[Cadre d'Architecture d'Entreprise (CAESN)](index.md) — niveau 1. Il définit le **périmètre,
la séquence et le financement** de chaque lot, exprimés dans le vocabulary de capacités du
CAESN (et non dans les composants techniques).

La **réalisation technique** de chaque lot (composants, patterns ARTSN, normes CNISN) est
détaillée dans la [vue de réalisation ARTSN](../../02_artsn/07_lots/index.md). Les lots opérationnalisent
les capacités du CAESN via les [work-packages `wp-01`…`wp-07`](../../referentiel/work-packages/wp-01.md).

> **Principe de cohérence** : le portefeuille (niveau 1) *définit* les lots ; l'ARTSN (niveau 3)
> *réalise* les lots. Les documents ARTSN référencent donc ce document vers le haut, ils ne
> sont pas la source de définition des lots.

## 1. Lots de déploiement

| Lot | Périmètre (capacités livrées) | Séquence | Objectif | Financement |
|-----|--------------------------------|----------|----------|-------------|
| **L1 — Infrastructure & sécurité** | CAP-INT-01, CMP-26, CMP-32, CMP-39, SRV-04 | T4 2026 – T2 2027 | Socle matériel, sécurité, référentiels de base et identité | [TCO L1](financement-tco.md#devis-indicatif-par-lot-ordre-de-grandeur) |
| **L2 — Applications terrain & collecte** | CAP-01, CMP-09, CMP-23, SRV-02, SRV-05 | T2 2027 – T4 2027 | Applications de collecte au plus près des formations sanitaires | [TCO L2](financement-tco.md#devis-indicatif-par-lot-ordre-de-grandeur) |
| **L3 — Médiation & registres** | CAP-INT-03, CMP-10, CMP-11, SRV-03, SRV-04 | T4 2027 – T2 2028 | Registres nationaux partagés et couche de médiation | [TCO L3](financement-tco.md#devis-indicatif-par-lot-ordre-de-grandeur) |
| **L4 — Analytique & pilotage** | CAP-03, ART-6, CMP-12, SRV-06 | T2 2028 – T4 2028 | Entrepôt analytique, IA prédictive et tableaux de bord décisionnels | [TCO L4](financement-tco.md#devis-indicatif-par-lot-ordre-de-grandeur) |
| **L5 — Extension & pérennisation** | CAP-INT-08, CAP-03, PT-14, PT-15 | T4 2028 – T2 2029 | Généralisation, formation, évaluation et pérennité | [TCO L5](financement-tco.md#devis-indicatif-par-lot-ordre-de-grandeur) |
| **L6 — Interopérabilité transfrontalière** | CAP-INT-08, ART-9, PT-14 | T2 2029 – T4 2029 | Adhésion GDHCN, confiance internationale et interopérabilité SADC/UA | [TCO L6](financement-tco.md#devis-indicatif-par-lot-ordre-de-grandeur) |
| **L7 — Coordination One Health** | CAP-03, CAP-INT-10, ART-8B, PT-15 | T2 2029 – T4 2029 | Échanges intersectoriels santé–animal–environnement | [TCO L7](financement-tco.md#devis-indicatif-par-lot-ordre-de-grandeur) |

## 2. Séquence et dépendances

Le déploiement respecte l'ordre *bottom-up* : chaque lot dépend du socle posé par le lot
précédent. Les lots L1 (infrastructure & sécurité) et L3 (médiation & registres) portent les
composants *partagés*, mutualisés et répartis en charge sur les lots consommateurs (voir la
[méthode TCO](financement-tco.md) pour la mutualisation).

## 3. Financement

Le coût total de possession par lot est défini dans la [méthode TCO et enveloppe de financement](financement-tco.md)
(portefeuille). Les montants y sont indicatifs et affinés en cadrage BRV.

## 4. Réalisation technique

Pour le détail des composants, patterns ARTSN et normes CNISN mis en œuvre par chaque lot,
voir la [vue de réalisation ARTSN](../../02_artsn/07_lots/index.md) et la
[matrice d'alignement PTISN](../../03_ptisn/04_matrice-alignement/index.md#4-alignement-avec-les-lots-de-deploiement-artsn).

## Références

- [Portefeuille d'initiatives orienté valeur](index.md)
- [Méthode TCO et enveloppe de financement](financement-tco.md)
- [Vue de réalisation ARTSN des lots](../../02_artsn/07_lots/index.md)
- [Work-packages `wp-01`…`wp-07`](../../referentiel/work-packages/wp-01.md)
- [Matrice d'alignement PTISN](../../03_ptisn/04_matrice-alignement/index.md)
