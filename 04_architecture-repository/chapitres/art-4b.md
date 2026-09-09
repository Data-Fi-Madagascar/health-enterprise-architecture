---
domain: chapitres

id: ART-4B
type: chapitre
niveau: "3"
title: Bases d'autorisation
status: draft
maturity_condition: "Confirmation par une seconde initiative"
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-4b-bases-autorisation.md
maps_to: ["CAP-15"]
implements: []
applies_to: ["ENF-4"]
related: ["ART-4"]
tags: ["artsn", "niveau-3", "chapitre", "ART-4B"]
---
# Bases d’autorisation

**Contenu normatif.** Tout traitement, lecture ou transfert d’une donnée individuelle doit valider **dynamiquement sa légitimité face à un registre centralisé** évaluant les fondements juridiques d’accès. Les fondements cibles sont : consentement ou opposition explicite, mandat de santé publique, ou accord interinstitutionnel ([ART-0](art-0.md)).

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (demandes d’extraction d’instituts de recherche, requêtes de ministères tiers), cette discipline seule permet de garantir techniquement le respect absolu du secret médical et des droits du citoyen sans rompre le pipeline.

- **Rattachement** : [CAP-04bis](../../02_artsn/08_annexes/c-renvoi-capacites-candidates.md), [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../capabilites/cap-15.md) (cybersécurité).
- **Fondements cibles** : consentement ou opposition explicite, mandat de santé publique, accord interinstitutionnel ([ART-0: Accords de partage inter-institutionnels](art-0.md)).
- **Déduit selon** : [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../exigences/enf-4.md) (protection One Health).
- **Statut : Provisoire.**

## Profils PTISN qui implémentent ce chapitre

Les profils techniques nationaux ci-dessous déclarent implémenter ce chapitre ART dans leur champ `implements` (frontmatter du référentiel). Le profil constitue la spécification implémentable et testable ; le chapitre demeure le cadre normatif opposable.

- [PT-04 : Résolution d’identité du bénéficiaire](../profils/pt-04.md)
- [PT-10 : Confiance, authentification et autorisation](../profils/pt-10.md)
- [PT-11 : Consentement et bases d’autorisation](../profils/pt-11.md)

