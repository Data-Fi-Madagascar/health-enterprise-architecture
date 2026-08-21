---
domain: exigences

id: ENF-4
type: exigence
niveau: "3"
title: Cloisonnement inter-institutionnel et étanchéité des données (One Health)
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/02_exigences-contextuelles/index.md
maps_to: []
implements: []
applies_to: []
related: ["ART-0", "ART-4B", "ART-4D", "F-2", "ART-2", "ART-6", "ART-8B", "ART-8D", "ART-4"]
tags: ["artsn", "niveau-3", "exigence", "ENF-4"]
---
# Cloisonnement inter-institutionnel et étanchéité des données (One Health)

**Contraintes contextuelles.** Le croisement de données massives entre le Ministère de la Santé (données cliniques), l’Agriculture et l’Élevage (zoonoses) et l’Environnement (climat, pollution) implique la manipulation de taxonomies, de secrets professionnels et de bases légales juridiquement et éthiquement étanches.

**Contenu normatif.** Le partage d’informations intersectoriel à des fins de recherche ou d’alerte épidémique précoce doit préserver la souveraineté de chaque institution, respecter le secret médical et protéger la vie privée des citoyens. Les pipelines de traitement analytique ont l’obligation d’opérer sur des données **définitivement dépouillées de tout identifiant direct** (Noms, INS). Les corrélations entre secteurs ne doivent s’effectuer qu’avec des dimensions de rapprochement **neutres et non nominatives** : l’espace géographique et le temps.

**Statut : Stable.** — appliqué par [ART-0 (accords de partage)](../chapitres/art-0.md), [ART-4b (bases d’autorisation)](../chapitres/art-4b.md), [ART-4d (référentiel géospatial)](../chapitres/art-4d.md).

## Justification

Le croisement de données massives entre Santé, Agriculture/Élevage et Environnement implique des taxonomies, des secrets professionnels et des bases légales juridiquement étanches. Cette exigence préserve la souveraineté de chaque institution et le secret médical en opérant sur des données définitivement dépouillées d’identifiants directs. Les corrélations intersectorielles ne s’appuient ainsi que sur des dimensions neutres et non nominatives : l’espace géographique et le temps.

## Capabilités concernées

- [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../capabilites/cap-14.md) — Interopérabilité, référentiels nationaux et infrastructure numérique partagée
- [CAP-18: Coordination intersectorielle (One Health)](../capabilites/cap-18.md) — Coordination intersectorielle (One Health)
- [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../capabilites/cap-15.md) — Cybersécurité, confidentialité et gouvernance des données personnelles

## Parties prenantes concernées

- [PP-03: Population](../parties-prenantes/pp-03.md) — Population
- [PP-07: District, région et Ministère](../parties-prenantes/pp-07.md) — District, région et Ministère
- [PP-08: Partenaires techniques et financiers](../parties-prenantes/pp-08.md) — Partenaires techniques et financiers
- [PP-10: Équipes techniques (DEPSI / SIS)](../parties-prenantes/pp-10.md) — Équipes techniques (DEPSI / SIS)

## Fondations et chapitres garants

- [ART-0: Accords de partage inter-institutionnels](../chapitres/art-0.md) — Accords de partage inter-institutionnels
- **ART-4b** — Bases d'autorisation
- **ART-4d** — Référentiel géospatial et d'exploitation partagé
- **F.2** — Préservation de la souveraineté intersectorielle
- [ART-2: Médiation et normalisation](../chapitres/art-2.md) — Médiation et normalisation
- [ART-6: Analytique et restitution](../chapitres/art-6.md) — Analytique et restitution
- **ART-8b** — Modélisation de relations en graphe
- **ART-8d** — Chorégraphie inter-institutionnelle
- [ART-4: Référentiels de métadonnées de gestion](../chapitres/art-4.md) — Référentiels de métadonnées de gestion
