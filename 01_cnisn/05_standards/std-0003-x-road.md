---
title: "STD-0003 : Norme d'échange interinstitutionnel : X-Road"
id: std-0003
domain: 05_standards
version: "1.0.0"
status: approved
last_reviewed: 2026-08-13
owner: Comité National d'Architecture Santé Numérique
tags: [standards, x-road, interinstitutionnel, obligatoire]
---

# STD-0003 : Norme d'échange interinstitutionnel : X-Road

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ○ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

- **Type** : norme (obligatoire)
- **Statut** : approuvé
- **ADR de référence** : ADR-0001
- **Date d'entrée en vigueur** : 2026-08-13

## Contexte

Le secteur santé doit échanger des données avec les systèmes interministériels (état civil, protection sociale, finances publiques). Ces échanges nécessitent une infrastructure de confiance commune garantissant la sécurité, la traçabilité et l'authentification mutuelle entre organisations.

## Énoncé

Tout échange de données entre le secteur santé et les autres secteurs de l'État **doit** :

1. **Utiliser X-Road** comme plateforme d'échange sécurisé
2. **Déployer un serveur de sécurité sectoriel** (Point de raccordement santé)
3. **Authentifier mutuellement** les organisations via des certificats numériques
4. **Chiffrer tous les échanges** en transit (TLS 1.2+)
5. **Journaliser toutes les transactions** pour traçabilité et audit

## Champ d'application

Cette norme s'applique à :
- Tous les échanges entre systèmes santé et systèmes interministériels
- Le PT-01 (échange interinstitutionnel)
- Toute solution nécessitant un échange avec l'état civil, la protection sociale ou les finances publiques

## Références au cadre

- **Principes** : PA-05 (Interopérabilité), PA-03 (Sécurité)
- **ARTSN** : ART-0 (Accords de partage), ART-7 (Sécurité)
- **PTISN** : PT-01 (Échange interinstitutionnel)
- **CNISN** : P-INT-01 à P-INT-04 (Autorité des données), P-INT-18 (Traçabilité)

## Contrôle et conformité

Lors de l'homologation, le Comité National vérifiera :

| Critère | Vérification |
|---------|--------------|
| Plateforme | X-Road déployé et configuré |
| Serveur de sécurité | Point de raccordement santé opérationnel |
| Authentification | Certificats numériques valides |
| Chiffrement | TLS 1.2+ configuré |
| Journalisation | Logs de transactions activés |

## Dérogations

Les dérogations sont possibles pour :
- Les systèmes legacy en phase de migration (API REST directe avec journalisation compensatoire)
- Les échanges urgentes en attendant le déploiement du serveur de sécurité

Toute dérogation doit être justifiée et approuvée par le Comité National.

## Références

- Normes et standards
- ADR-0001 : Adoption de X-Road
- PT-01 : Échange interinstitutionnel
- ARTSN : Chapitre ART-0

- **matrice de lecture** : Matrice de lecture du CNISN (niveau 2) (`01_cnisn/reading-matrix.md`)
