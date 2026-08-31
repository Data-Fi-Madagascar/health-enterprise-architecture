---
title: Aide à la décision clinique (CDS)
id: ptisn-PT-19
domain: 03_profils
version: "1.0.0"
status: draft
last_reviewed: 2026-08-27
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "profils", "PT-19"]
related: ["CAP-INT-05", "ART-12", "ART-2", "CMP-08"]
---

# Aide à la décision clinique (CDS)

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

## 1. Objet et périmètre

Le **profil PT-19 — Aide à la décision clinique (CDS)** expose l’aide à la décision clinique comme service de connaissance découplé des applications de point de service. La recommandation est adressée au professionnel ; elle ne décide pas à sa place.

Périmètre : publication et invocation d’artefacts de connaissance (guides de pratique, règles, ordonnances informatisées). Hors périmètre : les applications de point de service elles-mêmes.

## 2. Capacité CNISN

- [CAP-INT-05: Terminologie et codification](../../referentiel/capacites/cap-int-05.md)
- [CMP-08: Répertoire de données cliniques opérationnelles](../../referentiel/composants/cmp-08.md) (source de vérité clinique)

## 3. Chapitres ART applicables

- [ART-12: Aide à la décision clinique](../../referentiel/chapitres/art-12.md)
- [ART-2: normalisation sémantique](../../referentiel/chapitres/art-2.md)

## 4. Acteurs (Actors)

- **Éditeur de connaissance (Knowledge Author)** — publie et versionne les artefacts de connaissance.
- **Service CDS (Knowledge Service)** — expose les artefacts et répond aux invocations contextuelles.
- **Application de point de service (Point of Service / EHR)** — invoque le CDS et présente la recommandation au professionnel.

*Référence — capacité CNISN mise en œuvre : [CAP-INT-05](../../referentiel/capacites/cap-int-05.md).
## 5. Transactions

| Transaction | Acteurs | R/O | Standard |
|----|----|----|----|
| T1 — Publication d’artefact de connaissance | Éditeur → Service CDS | R | FHIR Clinical Reasoning (`PlanDefinition`, `ActivityDefinition`) |
| T2 — Invocation contextuelle (CDS Hooks) | Application → Service CDS | R | HL7 CDS Hooks |
| T3 — Récupération de règle (Clinical Reasoning) | Application → Service CDS | R | Module FHIR Clinical Reasoning |

R = requis ; O = optionnel (à définir si le dépôt ne précise pas).

*Référence — capacité CNISN mise en œuvre : [CAP-INT-05](../../referentiel/capacites/cap-int-05.md).
## 6. Content Modules

- **FHIR `PlanDefinition` / `ActivityDefinition`** : règles de décision, ordonnances informatisées, guides de pratique.
- **CDS Hooks** : ancrage contextuel de la recommandation dans l’application de point de service.
- **Liaison terminologique** : CIM-11 + LOINC (STD-0006), SNOMED CT (STD-0007).

## 7. Options

- **O1 — Mécanisme d’invocation** : CDS Hooks ou module FHIR Clinical Reasoning.
- **O2 — Produit** : aucun produit national retenu (statut : à instruire).

## 8. Service national

Le profil expose une aide à la décision clinique comme service de connaissance découplé des applications de point de service.

### Artefacts de connaissance

- guides de pratique, ensembles de règles et ordonnances informatisées, versionnés et publiés ;
- liaison aux terminologies nationales (STD-0006, STD-0007).

### Invocation

- ancrage contextuel via HL7 CDS Hooks ou module FHIR Clinical Reasoning ;
- la recommandation est adressée au professionnel ; elle ne décide pas à sa place.

## 9. Formats et standards recommandés

| Type d'artefact | Format recommandé |
|-----------------|-------------------|
| Règle de décision | HL7 FHIR Clinical Reasoning (`PlanDefinition`, `ActivityDefinition`) |
| Ancrage contextuel | HL7 CDS Hooks |
| Terminologie | CIM-11 + LOINC (STD-0006), SNOMED CT (STD-0007) |
| Invocation | FHIR R4 (STD-0001) |

*Référence — normes et standards CNISN : [01_cnisn/05_standards](../../01_cnisn/05_standards/index.md).
## 10. Exigences

Aucun produit national n’est encore retenu (**statut : à instruire**). Les artefacts doivent être versionnés, publiés, et liés aux terminologies nationales.

## 11. Déclaration de conformité (Integration Statement)

- artefacts de connaissance publiés et versionnés ;
- liaison terminologique vérifiée (STD-0007) ;
- séparation claire recommandation / décision professionnelle.

## 12. Articulation avec les autres profils

- [PT-07: terminologie et codification](../../referentiel/profils/pt-07.md)
- [PT-05: registre des professionnels](../../referentiel/profils/pt-05.md)
- [PT-10: confiance, authentification, autorisation](../../referentiel/profils/pt-10.md)

## 13. Limites et dépendances

Produit national à instruire. Dépendance : terminologie nationale (PT-07), répertoire de données cliniques (CMP-08), et composant d’invocation CDS Hooks / FHIR Clinical Reasoning.

<!-- END:GENERATED -->

## Références au cadre

- **ARTSN — lots consommateurs** : [L1 — Infrastructure & sécurité](../../02_artsn/07_lots/index.md), [L2 — Applications terrain](../../02_artsn/07_lots/index.md), [L4 — Analytique & pilotage](../../02_artsn/07_lots/index.md)
