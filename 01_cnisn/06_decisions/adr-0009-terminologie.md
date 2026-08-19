---
title: "ADR-0009 — Adoption d'un référentiel terminologique national (CIM-10 + LOINC)"
id: adr-0009
domain: 06_decisions
version: "1.0.0"
status: proposé
date: 2026-08-13
owner: DEPSI
tags: [adr, terminologie, cim-10, loinc, codage, sémantique]
---

# ADR-0009 — Adoption d'un référentiel terminologique national (CIM-10 + LOINC)

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle.

- **Statut** : proposé
- **Date** : 2026-08-13
- **Groupe concerné** : DEPSI, OMS, CNASN

## Contexte

La terminologie médicale est le socle de la sémantique commune du système d'information sanitaire. Sans référentiel terminologique unifié, il est impossible de :
- Croiser les données entre systèmes et programmes
- Calculer des indicateurs fiables
- Interopérer avec les systèmes internationaux
- Assurer la qualité des données cliniques

Actuellement, chaque programme utilise ses propres codages (codes locaux, codes OMS partiels, codage manuel). Les mappings entre systèmes sont inexistants ou incomplets, ce qui rend impossible l'agrégation fiable des données.

## Décision

Adopter un **référentiel terminologique national** basé sur :
- **CIM-10** (Classification Internationale des Maladies, 10e révision) pour les diagnostics
- **LOINC** (Logical Observation Identifiers Names and Codes) pour les observations et résultats
- **DCI** (Dénomination Commune Internationale) pour les médicaments
- **ATC** (Anatomical Therapeutic Chemical) pour la classification des médicaments

## Justification

Le référentiel terminologique répond aux exigences du cadre :

- **ART-2** : Médiation et normalisation sémantique
- **ART-5** : Qualité des données
- **CAP-INT-05** : Données agrégées de santé publique
- **CAP-INT-11** : Qualité et réconciliation des données
- **PT-07** : Mapping terminologique
- **VS-02** : Surveillance épidémique (codage standardisé)
- **VS-04** : Pilotage système (indicateurs fiables)

Le référentiel doit :
- Être maintenu par une instance nationale dédiée
- Être mis à jour annuellement (CIM-10) et trimestriellement (LOINC)
- Fournir des API de mapping (code local → code standard)
- Supporter les extensions nationales (codes spécifiques au Madagascar)

## Conséquences

### Positives
- Sémantique commune entre tous les systèmes
- Interopérabilité avec les standards internationaux (OMS, IHE)
- Qualité des données améliorée
- Capacité de pilotage fiable
- Préparation aux échanges transfrontaliers

### Négatives
- Coût de maintenance du référentiel (mappings, mises à jour)
- Nécessite un service de mapping pour les systèmes legacy
- Formation des développeurs et des cliniciens
- Résistance au changement (abandon des codes locaux)

## Alternatives considérées

| Alternative | Raison du refus |
|-------------|-----------------|
| Codes locaux uniquement | Pas d'interopérabilité, pas d'agrégation fiable |
| CIM-10 seul | Pas de codage pour les observations et résultats |
| SNOMED CT | Trop complexe pour le contexte malgache, coût de licence |
| OpenMRS concept dictionary | Limité aux programmes VIH/TB, pas national |

## Références

- PT-07 — Mapping terminologique
- ART-2 — Médiation et normalisation
- CAP-INT-05 — Données agrégées
- [CIM-10 — OMS](https://icd.who.int)
- [LOINC — Regenstrief Institute](https://loinc.org)

