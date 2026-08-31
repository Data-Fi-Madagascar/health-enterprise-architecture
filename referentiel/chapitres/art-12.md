---
domain: chapitres
id: ART-12
type: chapitre
niveau: "3"
title: Aide à la décision clinique
status: draft
maturity_condition: "Proposition ouverte : à confirmer par une initiative de soins utilisant des artefacts de connaissance profilés"
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-12-aide-decision-clinique.md
maps_to: ["CMP-08"]
implements: []
applies_to: ["ART-6", "CAP-13"]
related: ["CAP-INT-05", "F-2"]
tags: ["artsn", "niveau-3", "chapitre", "ART-12"]
---

# Aide à la décision clinique

**Contenu normatif.** Toute assistance à la décision clinique (CDS) déployée dans le secteur santé de Madagascar **doit** s'appuyer sur des artefacts de connaissance explicites, versionnés et liés à la terminologie nationale, plutôt que sur des règles métier encapsulées dans le code applicatif. L'aide à la décision est une recommandation adressée au professionnel ; elle ne substitue pas à son jugement et ne prend pas de décision à sa place.

**Discipline de mise en œuvre.** Dès qu'une règle de décision (protocole, alerte, rappel) peut impacter la prise en charge, elle doit être exprimée comme un artefact de connaissance (guide de pratique, ensemble de règles, ordonnance informatisée) profilé selon l'ARTSN et lié aux terminologies (STD-0006, STD-0007). Cela garantit l'auditabilité, la réutilisabilité inter-initatives et la mise à jour centralisée sans re-déploiement des applications de point de service.

- **Rattachement** : [CMP-08: Répertoire de données cliniques opérationnelles](../composants/cmp-08.md) (source de vérité clinique).
- **Terminologie** : [CAP-INT-05: Terminologie et codification](../capacites/cap-int-05.md), [STD-0007: SNOMED CT](../../01_cnisn/05_standards/std-0007-snomed-ct.md).
- **Référentiel cible** : HL7 CDS Hooks, FHIR Clinical Reasoning Module, guides de pratique profilés.
- **Déduit selon** : [ART-6: Analytique et restitution](../chapitres/art-6.md) (restitution de la connaissance), [CAP-13: Système d'information sanitaire, données et recherche](../capabilites/cap-13.md).
- **Statut : Proposition ouverte.**
