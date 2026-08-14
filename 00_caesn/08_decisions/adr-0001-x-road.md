---
title: "ADR-0001 — Adoption de X-Road comme plateforme d'échange interinstitutionnel"
id: adr-0001
domain: 08_decisions
version: "0.1.0"
status: accepté
date: 2026-07-01
owner: DEPSI
tags: [adr, interopérabilité, x-road, plateforme]
---

# ADR-0001 — Adoption de X-Road comme plateforme d'échange interinstitutionnel

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ○ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

- **Statut** : accepté
- **Date** : 2026-07-01
- **Groupe concerné** : DEPSI, UGD, Ministère de la Santé

## Contexte

Le système d'information sanitaire national doit échanger des données avec de multiples systèmes interministériels : état civil, registre de la population, protection sociale, finances publiques, éducation et collectivités territoriales. 

Le CNISN (Cadre National d'Interopérabilité de la Santé Numérique) exige un mécanisme d'échange sécurisé entre organisations membres, conforme au CNI (Cadre National d'Interopérabilité).

## Décision

Adopter **X-Road** comme plateforme d'échange interinstitutionnel pour les échanges entre le secteur santé et les autres secteurs de l'État.

## Justification

X-Road répond aux exigences du CNISN :

- **P-INT-01 à P-INT-04** : Autorité des données et gouvernance inter-organisations
- **P-INT-18** : Traçabilité des échanges
- **P-INT-19** : Neutralité technologique (open source)
- **P-INT-22** : Connectivité contrainte (infrastructure légère)

Il est déjà déployé dans plusieurs pays similaires (Estonie, Finlande, Islande) et constitue un standard reconnu pour l'interopérabilité interministérielle.

## Conséquences

### Positives
- Sécurisation des échanges inter-systèmes par chiffrement et signature
- Infrastructure de confiance commune entre organisations membres
- Traçabilité complète des transactions
- Conformité au CNI national

### Négatives
- Nécessite un serveur de sécurité sectoriel (Point de raccordement santé)
- Ne constitue pas à lui seul un service de normalisation sémantique
- Nécessite une autorité de gouvernance nationale

## Alternatives considérées

| Alternative | Raison du refus |
|-------------|-----------------|
| API REST propriétaires | Pas de standardisation, traçabilité insuffisante |
| HL7 FHIR seul | Standard de données, pas de infrastructure d'échange |
| Service middleware propriétaire | Dépendance éditeur, coût élevé |

## Références

- [PT-01 — Profil technique national](../../03_ptisn/03_profils/pt-01-echange-interinstitutionnel.md)
- [CNISN — Principes d'interopérabilité](../../01_cnisn/01_principes/index.md)
- [ARTSN — Chapitre ART-0](../../02_artsn/03_chapitres/art-0-accords-partage.md)
