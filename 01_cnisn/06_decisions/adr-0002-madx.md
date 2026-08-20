---

title: "ADR-0002 : Adoption du profil IHE mADX pour l'échange de données agrégées"
id: adr-0002
domain: 06_decisions
version: "1.0.0"
status: accepté
date: 2026-07-01
owner: DEPSI
tags: ["adr", "interopérabilité", "madx", "données-agrégées"]
---

# ADR-0002 : Adoption du profil IHE mADX pour l'échange de données agrégées

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

- **Statut** : accepté
- **Date** : 2026-07-01
- **Groupe concerné** : DEPSI, directions métier, partenaires techniques

## Contexte

Les systèmes de collecte de données sanitaires (DHIS2, programmes sectoriels) produisent des rapports périodiques qui doivent être transmis à différents niveaux : établissement → district → région → national → international.

Le profil IHE ADX (Aggregate Data Exchange) existe déjà mais repose sur un format XML propriétaire. Le profil mADX (Mobile ADX) est sa version moderne basée sur FHIR, conçue pour les environnements à connectivité limitée.

## Décision

Adopter le **profil IHE mADX** comme standard national pour l'échange de données agrégées de santé publique, en conservant la compatibilité avec les implémentations ADX existantes.

## Justification

mADX répond aux exigences du CNISN et de l'ARTSN :

- **CAP-INT-05** : Données agrégées de santé publique
- **CAP-INT-07** : Accès et exposition des données analytiques
- **ART-2** : Médiation et normalisation sémantique
- **ART-5** : Analytique et pilotage

Il est compatible avec DHIS2, le système de collecte national déjà déployé, et permet l'échange interopérable avec les standards internationaux (OMS, Banque Mondiale).

## Conséquences

### Positives
- Standard international reconnu par l'IHE et l'OMS
- Compatible avec les implémentations ADX existantes
- Conçu pour les environnements à connectivité limitée
- Base FHIR pour l'interopérabilité future

### Négatives
- Nécessite la normalisation des codes et dimensions via le service terminologique
- Migration des flux ADX existants vers mADX
- Formation des développeurs aux profils IHE

## Alternatives considérées

| Alternative | Raison du refus |
|-------------|-----------------|
| ADX classique | Format XML propriétaire, moins adapté aux environnements mobiles |
| Export CSV non profilé | Pas de standardisation, risques d'erreur |
| API propriétaire | Pas d'interopérabilité, dépendance éditeur |

## Références

- PT-08 : Profil technique national
- ARTSN : Chapitre ART-5
- CNISN : CAP-INT-05

- **matrice de lecture** : Matrice de lecture du CNISN (niveau 2) (`01_cnisn/reading-matrix.md`)
