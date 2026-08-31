---
domain: nomenclatures
id: FOSA-STATUS
type: nomenclature
niveau: "3"
title: "Statut opérationnel d'une formation sanitaire"
status: active
owner: DEPSI
version: "1.0.0"
envelope: 02_artsn/03_objets-de-donnees/nomenclatures/fosa-status.md
artRef: ["ART-4", "ART-5"]
maps_to: ["CAP-INT-04"]
implements: ["IHE mCSD"]
related: ["DO-04", "DO-05", "PT-06"]
tags: ["nomenclature", "fosa", "mCSD", "etablissement"]
fhir_resource: "CodeSystem"
fhir_url: "https://healmadagascar.mg/fhir/CodeSystem/hea-fosa-status"
---

# FOSA-STATUS : Statut opérationnel d'une formation sanitaire

Nomenclature nationale des statuts opérationnels des formations sanitaires (FOSA - Health Facility) conformément au standard IHE mCSD (Master Client Directory).

## Contexte

Cette nomenclature est utilisée par le **référentiel national des formations sanitaires** (PT-06) pour typer le statut opérationnel de chaque structure de santé. Elle est consommée par :

- Le service mCSD (IHE mCSD ITI-90/91) pour la recherche et la mise à jour des formations sanitaires
- Le module de géosanitaire pour la cartographie des structures actives
- Le système DHIS2 pour le reporting sanitaire national

## Définition des concepts

| Code | Libellé | Description | Statut |
|------|---------|-------------|--------|
| `actif` | Actif | Formation sanitaire opérationnelle, desservant la population cible | active |
| `inactif` | Inactif | Formation sanitaire temporairement hors service (maintenance, rénovation) | active |
| `temporaire` | Temporaire | Structure mise en place pour une réponse exceptionnelle (épidémie, catastrophe) | active |
| `ferme` | Fermé | Formation sanitaire définitivement fermée ou détruite | active |
| `projet` | Projet | Formation sanitaire en cours de construction ou de mise en service | active |

## Contraintes d'intégrité

- **Unicité** : Chaque code est unique au sein de cette nomenclature
- **Stabilité** : Les codes ne doivent pas être modifiés après publication (version majeure)
- **Traçabilité** : Chaque changement de statut doit être horodaté et identifié
- **Complétude** : Tout statut possible doit être couvert par cette nomenclature

## Mapping FHIR

La nomenclature est implémentée comme un **CodeSystem FHIR R4** avec les propriétés :

- `code` : identifiant du concept (string)
- `display` : libellé court (string)
- `definition` : description textuelle (string)
- `status` : statut du concept dans le code system (active | deprecated | retired)

## Mapping IHE mCSD

Dans le cadre IHE mCSD (ITI-90), le statut est utilisé dans :

- `Organization.type` avec le code `fosa-status`
- `Organization.active` (boolean) mapping vers `actif`/`inactif`

## Références

- **ART-4** : Référentiels de métadonnées de gestion
- **ART-5** : Cohérence et qualité des données
- **CAP-INT-04** : Référentiel des structures et services de santé
- **PT-06** : Référentiel des structures et services de santé (mCSD)
- **IHE mCSD** : Master Client Directory
- **DO-04** : Formation sanitaire
- **DO-05** : Service de santé
