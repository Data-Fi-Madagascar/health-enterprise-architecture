---
title: "Aide à la décision clinique"
id: artsn-ART-12
domain: 04_patterns
version: "1.0.0"
status: draft
last_reviewed: 2026-08-27
owner: DEPSI
tags: ["artsn", "chapitres", "ART-12", "niveau-3"]
related: []
---

# Aide à la décision clinique

ART-12 : Aide à la décision clinique constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `ART-12`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Contenu normatif.** Toute assistance à la décision clinique (CDS) déployée dans le secteur santé de Madagascar **doit** s'appuyer sur des artefacts de connaissance explicites, versionnés et liés à la terminologie nationale, plutôt que sur des règles métier encapsulées dans le code applicatif. L'aide à la décision est une recommandation adressée au professionnel ; elle ne substitue pas à son jugement et ne prend pas de décision à sa place.

**Discipline de mise en œuvre.** Dès qu'une règle de décision (protocole, alerte, rappel) peut impacter la prise en charge, elle doit être exprimée comme un artefact de connaissance (guide de pratique, ensemble de règles, ordonnance informatisée) profilé selon l'ARTSN et lié aux terminologies (STD-0006, STD-0007). Cela garantit l'auditabilité, la réutilisabilité inter-initatives et la mise à jour centralisée sans re-déploiement des applications de point de service.

- **Rattachement** : [CMP-08: Répertoire de données cliniques opérationnelles](../../referentiel/composants/cmp-08.md) (source de vérité clinique).
- **Terminologie** : [CAP-INT-05: Terminologie et codification](../../referentiel/capacites/cap-int-05.md), [STD-0007: SNOMED CT](../../01_cnisn/05_standards/std-0007-snomed-ct.md).
- **Référentiel cible** : HL7 CDS Hooks, FHIR Clinical Reasoning Module, guides de pratique profilés.
- **Déduit selon** : [ART-6: Analytique et restitution](../../referentiel/chapitres/art-6.md) (restitution de la connaissance), [CAP-13: Système d'information sanitaire, données et recherche](../../referentiel/capabilites/cap-13.md).
- **Statut : Proposition ouverte.**

## Profils PTISN qui implémentent ce chapitre

Les profils techniques nationaux ci-dessous déclarent implémenter ce chapitre ART dans leur champ `implements` (frontmatter du référentiel). Le profil constitue la spécification implémentable et testable ; le chapitre demeure le cadre normatif opposable.

- [PT-19 : Aide à la décision clinique (CDS)](../../referentiel/profils/pt-19.md)

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`ART-12`** : Aide à la décision clinique (`referentiel/chapitres/art-12.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/04_patterns/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
