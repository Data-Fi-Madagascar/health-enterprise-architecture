---
title: "Composition et fonctionnement du Comité National"
id: cnasen-composition
domain: 07_governance
version: "0.1.0"
status: draft
last_reviewed: 2026-08-13
owner: Secrétariat Général
tags: [gouvernance, cnasen, composition, fonctionnement]
---

# Composition et fonctionnement du Comité National d'Architecture Santé Numérique

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

## 1. Missions

Le Comité National d'Architecture Santé Numérique (CNASN) est l'instance collégiale responsable de :

| Mission | Description |
|---------|-------------|
| **Cohérence architecturale** | Garantir que toutes les solutions numériques s'inscrivent dans le cadre d'architecture |
| **Homologation** | Valider la conformité des solutions aux principes et standards |
| **Arbitrage** | Résoudre les conflits de standards ou de choix techniques |
| **Dérogations** | Statuer sur les demandes de dérogation aux normes |
| **Rationalisation** | Suivre et optimiser le paysage applicatif |

## 2. Composition

### 2.1 Membres permanents

| Rôle | Représentant | Institution |
|------|--------------|-------------|
| **Président** | Secrétaire Général (ou délégué) | Ministère de la Santé |
| **Vice-Président** | Directeur des Systèmes d'Information | Ministère de la Santé |
| **Secrétaire technique** | Chef de l'Unité de Coordination TIC | DEPSI |
| **Membres** | Directeurs techniques des programmes prioritaires | PNLP, PNVS, PNRH, etc. |
| **Membres** | Représentants des partenaires techniques | OMS, Banque Mondiale, UNICEF |
| **Membres** | Représentants des éditeurs de logiciels | Secteur privé |

### 2.2 Membres invités (selon l'ordre du jour)

| Rôle | Représentant |
|------|--------------|
| Représentant juridique | Direction Juridique |
| Représentant financier | Direction des Finances |
| Représentant des régions | Délégations régionales |
| Expert technique externe | Consultants spécialisés |

## 3. Fonctionnement

### 3.1 Réunions

| Type | Fréquence | Participants |
|------|-----------|--------------|
| **Réunion plénière** | Trimestrielle | Tous les membres |
| **Comité technique** | Mensuel | Membres techniques |
| **Comité des normes** | Bimensuel | Experts techniques |
| **Réunion extraordinaire** | Selon besoin | Selon l'ordre du jour |

### 3.2 Processus de décision

```
┌─────────────────────────────────────────────────────────────┐
│                    Processus de décision                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. Identification du besoin                                 │
│     ↓                                                        │
│  2. Proposition documentée (note, ADR)                       │
│     ↓                                                        │
│  3. Examen en Comité technique                               │
│     ↓                                                        │
│  4. Recommandation au CNASN                                  │
│     ↓                                                        │
│  5. Décision du CNASN (vote à la majorité)                   │
│     ↓                                                        │
│  6. Enregistrement (ADR, registre des normes)                │
│     ↓                                                        │
│  7. Communication et mise en œuvre                            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 Quorum et votes

| Règle | Valeur |
|-------|--------|
| **Quorum** | 2/3 des membres permanents |
| **Majorité** | Simple majorité des membres présents |
| **Arbitrage** | Le président a voix prépondérante en cas d'égalité |

## 4. Ordre du jour type

1. **Validation du compte-rendu** de la précédente réunion
2. **Suivi des décisions** en cours
3. **Examens des demandes d'homologation**
4. **Arbitrages techniques** (conflits de standards)
5. **Demandes de dérogation**
6. **Veille architecturale** (évolutions des standards)
7. **Questions diverses**

## 5. Documents de référence

| Document | Usage |
|----------|-------|
| **Registre des ADR** | Traçabilité des décisions d'architecture |
| **Registre des normes** | Normes et standards en vigueur |
| **Portefeuille d'initiatives** | Suivi des projets numériques |
| **Matrice de maturité** | Évaluation des capabilités |
| **Rapport semestriel** | Bilan d'activité du CNASN |

## 6. Indicateurs de performance

| Indicateur | Cible |
|------------|-------|
| Nombre de réunions par an | 4 (trimestrielles) |
| Délai de traitement des homologations | < 30 jours |
| Délai de traitement des dérogations | < 15 jours |
| Taux de conformité des nouvelles solutions | > 90% |
| Nombre d'ADR enregistrés par an | > 10 |

## Liens

- [Gouvernance du cadre](./index.md)
- [Bureau de Réalisation de la Valeur](./value-realization-office.md)
- [RACI de gouvernance](./raci.md)
- [Registre des ADR](../08_decisions/index.md)
- [Registre des normes](../09_standards/index.md)
