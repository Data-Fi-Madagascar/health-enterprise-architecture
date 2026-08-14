---
title: "STD-0004 — Norme de données agrégées — mADX"
id: std-0004
domain: 09_standards
version: "1.0.0"
status: approved
last_reviewed: 2026-08-13
owner: Comité National d'Architecture Santé Numérique
tags: [standards, madx, donnees-agregees, obligatoire]
---

# STD-0004 — Norme de données agrégées — mADX

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

- **Type** : norme (obligatoire)
- **Statut** : approuvé
- **ADR de référence** : ADR-0002
- **Date d'entrée en vigueur** : 2026-08-13

## Contexte

La collecte de données sanitaires (DHIS2, programmes sectoriels) produit des rapports périodiques transmis de l'établissement au district, à la région, au national et à l'international. Le format d'échange doit être standardisé pour garantir l'interopérabilité et l'agrégation fiable.

## Énoncé

Toute transmission de données agrégées de santé publique **doit** :

1. **Utiliser le profil IHE mADX** (Mobile Aggregate Data Exchange) comme format standard
2. **Exposer des API REST conformes** aux spécifications mADX/FHIR
3. **Mapper les codes locaux** vers les classifications internationales (CIM-10, LOINC)
4. **Respecter la structure DHIS2** pour la compatibilité avec le système de collecte national
5. **Versionner les métadonnées** des rapports (période, indicateurs, dimensions)

## Champ d'application

Cette norme s'applique à :
- Tous les rapports périodiques de santé publique
- Le PT-08 (échange de données agrégées)
- Les échanges avec DHIS2, l'OMS et la Banque Mondiale

## Références au cadre

- **Principes** : PA-05 (Interopérabilité), PA-06 (Gouvernance des données)
- **ARTSN** : ART-5 (Analytique et pilotage), ART-2 (Médiation)
- **PTISN** : PT-08 (Données agrégées)
- **CNISN** : CAP-INT-05 (Données agrégées), CAP-INT-07 (Accès analytique)

## Contrôle et conformité

| Critère | Vérification |
|---------|--------------|
| Format | Données en mADX/FHIR |
| API | API REST mADX opérationnelle |
| Mapping | Codes mappés vers CIM-10/LOINC |
| DHIS2 | Compatibilité avec le schéma DHIS2 |
| Métadonnées | Versionnage des rapports |

## Dérogations

Les dérogations sont possibles pour :
- Les programmes utilisant encore des exports CSV (migration progressive vers mADX)
- Les échanges avec des systèmes internationaux non mADX (via médiation)

Toute dérogation doit être justifiée et approuvée par le Comité National.

## Références

- [Normes et standards](./index.md)
- [ADR-0002 — Adoption de mADX](../08_decisions/adr-0002-madx.md)
- [PT-08 — Données agrégées](../../03_ptisn/03_profils/pt-08-echange-donnees-agregees.md)
- [ARTSN — Chapitre ART-5](../../02_artsn/03_chapitres/art-5-coherence-qualite-donnees.md)
