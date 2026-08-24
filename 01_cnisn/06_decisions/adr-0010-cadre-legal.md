---

title: "ADR-0010 : Cadre légal et mandat d'opposabilité du CNASN"
id: adr-0010
domain: 06_decisions
version: "1.0.0"
status: candidate
date: 2026-08-20
owner: Ministère de la Santé Publique
tags: ["adr", "légal", "gouvernance", "e-santé"]
---

# ADR-0010 : Cadre légal et mandat d'opposabilité du CNASN

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ◐ |
| SIS / données / suivi-évaluation | ○ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

- **Statut** : proposé
- **Date** : 2026-08-20
- **Groupe concerné** : Ministère de la Santé, CNASN, UGD, CMIL

## Contexte

Le cadre HEA (CAESN, CNISN, ARTSN, PTISN) est aujourd'hui **consultatif**. Ses décisions (ADR, homologation, critères de conformité) ne disposent pas de base légale contraignante. Les pairs africains (Kenya Digital Health Act 2023, Afrique du Sud POPIA/National Health Act, Nigeria NDPR) ont doté leur architecture de santé numérique d'un mandat légal.

## Décision

Recommander l'adoption d'un **projet de loi e-santé** (modèle Kenya Digital Health Act 2023) qui :
1. confère au **CNASN** un mandat légal d'autorité d'architecture et d'homologation ;
2. rend **obligatoire** le respect des standards HEA pour tout système public ou utilisant les infrastructures nationales ;
3. fonde légalement la gestion du consentement et la résidence des données ;
4. instaure un **programme de conformité opérationnel** avec pouvoir de sanction.

En attendant l'adoption de la loi, le CNASN exerce son mandat par **accord interinstitutionnel** et conditionnalité des financements publics.

## Justification

Sans mandat légal, l'interopérabilité ne peut être imposée aux acteurs autonomes (établissements privés, partenaires), et la conformité reste théorique. La loi sécurise l'investissement et l'effort de standardisation.

## Conséquences

### Positives
- Homologation opposable et sanctionnable ;
- Base légale pour le consentement (PT-11) et la résidence (C7) ;
- Benchmarking GDHM crédible.

### Négatives
- Délais législatifs (12–24 mois) ;
- Nécessite un plaidoyer auprès du Ministère des Finances et du Parlement.

## Alternatives considérées

| Alternative | Raison du refus |
|-------------|-----------------|
| Maintien du cadre consultatif | Non-conformité durable, fragmentation persistante |
| Réglementation sectorielle isolée | Ne couvre pas l'interopérabilité inter-ministérielle (X-Road) |

## Références
- **ARTSN — lots consommateurs** : [L1 — Infrastructure & sécurité](../../02_artsn/07_lots/index.md)

- Fondement légal : `00_caesn/07_governance/fondement-legal.md`
- Programme de conformité : `01_cnisn/04_conformite/programme-conformite.md`
- Gouvernance CNISN : `01_cnisn/03_gouvernance/index.md`

- **matrice de lecture** : Matrice de lecture du CNISN (niveau 2) (`01_cnisn/reading-matrix.md`)
