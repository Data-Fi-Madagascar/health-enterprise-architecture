---

id: ENF-3
type: exigence
niveau: "3"
title: Unicité de l'identité et résilience face à la fragmentation applicative
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/02_exigences-contextuelles/index.md
maps_to: []
implements: []
applies_to: []
related: ["ART-4A", "ART-2"]
tags: ["artsn", "niveau-3", "exigence", "ENF-3"]
---
# Unicité de l’identité et résilience face à la fragmentation applicative

**Contraintes contextuelles.** Le paysage numérique historique est caractérisé par une dispersion de solutions logicielles et de bases de données isolées. Un même citoyen possède des fiches cliniques, des dossiers et des identifiants locaux différents selon les hôpitaux ou les programmes verticaux (Malariologie, Tuberculose, Vaccination), ce qui menace la sécurité des soins et empêche le suivi médical longitudinal.

**Contenu normatif.** Le système national doit posséder la capacité de rapprocher, consolider et unifier des identités de patients incertains, phonétiquement variables ou incomplètes. Cette brique d’**identitovigilance** doit générer un enregistrement pivot unique et souverain pour le citoyen, sans forcer le remplacement immédiat ou la refonte structurelle des bases locales des hôpitaux.

**Statut : Stable.** — appliqué par [ART-4a (résolution d’identité)](../chapitres/art-4a.md), [ART-2 (médiation)](../chapitres/art-2.md).

## Justification

Le paysage numérique historique est marqué par une dispersion de solutions et de bases isolées, où un même citoyen cumule des fiches et identifiants différents selon les structures ou programmes. Cette fragmentation menace la sécurité des soins et empêche le suivi médical longitudinal. L’exigence d’unicité permet de consolider une identité pivot souveraine sans forcer la refonte immédiate des systèmes locaux.

## Capabilités concernées

- [CAP-17: Engagement patient et identité numérique](../capabilites/cap-17.md) — Engagement patient et identité numérique
- [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../capabilites/cap-14.md) — Interopérabilité, référentiels nationaux et infrastructure numérique partagée
- [CAP-13: Système d'information sanitaire, données et recherche](../capabilites/cap-13.md) — Système d'information sanitaire, données et recherche

## Parties prenantes concernées

- [PP-01: Patient et usager](../parties-prenantes/pp-01.md) — Patient et usager
- [PP-06: Formation sanitaire](../parties-prenantes/pp-06.md) — Formation sanitaire
- [PP-10: Équipes techniques (DEPSI / SIS)](../parties-prenantes/pp-10.md) — Équipes techniques (DEPSI / SIS)

## Fondations et chapitres garants

- **ART-4a** — Résolution d'identité
- [ART-2: Médiation et normalisation](../chapitres/art-2.md) — Médiation et normalisation
