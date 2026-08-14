---
title: "STD-0001 — Norme d'interopérabilité — HL7 FHIR R4"
id: std-0001
domain: 09_standards
version: "1.0.0"
status: approved
last_reviewed: 2026-08-13
owner: Comité National d'Architecture Santé Numérique
tags: [standards, interoperabilite, fhir, obligatoire]
---

# STD-0001 — Norme d'interopérabilité — HL7 FHIR R4

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ○ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

- **Type** : norme (obligatoire)
- **Statut** : approuvé
- **ADR de référence** : ADR-0003
- **Date d'entrée en vigueur** : 2026-08-13

## Contexte

L'interopérabilité sanitaire nécessite un standard de données commun pour l'échange, le stockage et l'exposition des informations de santé. Les systèmes existants utilisent des formats variés (HL7 v2, XML, CSV, JSON propriétaire) ce qui fragmente l'écosystème et complique les intégrations.

HL7 FHIR R4 (Fast Healthcare Interoperability Resources, Release 4) est le standard moderne pour les données de santé, reconnu par l'OMS, l'IHE et les principaux systèmes d'information sanitaire mondiaux.

## Énoncé

Toute solution numérique échangeant des données de santé dans le secteur santé de Madagascar **doit** :

1. **Utiliser HL7 FHIR R4** comme format d'échange pour les ressources cliniques et administratives
2. **Exposer des API REST conformes** aux spécifications FHIR R4
3. **Profiler les ressources** selon les profils nationaux définis dans l'ARTSN
4. **Versionner les API** selon les bonnes pratiques FHIR (URL de base + version)
5. **Documenter les API** selon le format OpenAPI 3.0

## Champ d'application

Cette norme s'applique à :
- Toutes les API échangeant des données de santé
- Tous les systèmes d'information sanitaire intégrés au SI national
- Tous les profils techniques du PTISN
- Toutes les solutions soumises à homologation

## Références au cadre

- **Principes** : PA-05 (Interopérabilité comme exigence), PA-02 (Neutralité technologique)
- **ARTSN** : ART-2 (Médiation et normalisation), F.2 (Normalisation), F.3 (Interopérabilité)
- **PTISN** : PT-04 (Identité), PT-08 (Données agrégées), TOUS les profils
- **Standards internationaux** : HL7 FHIR R4, IHE, OpenHIE, DPI-H

## Contrôle et conformité

Lors de l'homologation, le Comité National vérifiera :

| Critère | Vérification |
|---------|--------------|
| Format d'échange | Les données échangées sont en FHIR R4 |
| API REST | L'API respecte les spécifications FHIR R4 |
| Profilage | Les ressources utilisent les profils nationaux |
| Versioning | L'API est versionnée |
| Documentation | L'API est documentée en OpenAPI 3.0 |

## Dérogations

Les dérogations sont possibles pour :
- Les systèmes legacy en phase de migration (compatibilité HL7 v2 limitée dans le temps)
- Les échanges avec des systèmes externes non FHIR (via médiation obligatoire)

Toute dérogation doit être justifiée et approuvée par le Comité National.

## Références

- [Normes et standards](./index.md)
- [ADR-0003 — Utilisation de HL7 FHIR](../08_decisions/adr-0003-fhir.md)
- [ARTSN — Fondation F.2](../../referentiel/fondations/f-2.md)
- [ARTSN — Fondation F.3](../../referentiel/fondations/f-3.md)
