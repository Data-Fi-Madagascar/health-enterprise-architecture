---
domain: composants
id: CMP-10
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Registre des terminologies
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/composants.md
maps_to: ["CAP-INT-09"]
implements: ["ART-4"]
uses: ["CMP-26", "CMP-27", "CMP-28", "CMP-29", "CMP-30", "CMP-31", "CMP-32", "CMP-33", "CMP-34", "CMP-35", "CMP-36", "CMP-37", "CMP-38"]
applies_to: ["PRC-07", "PRC-08"]
related: ["ENF-4", "CAP-09", "VS-03"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-10", "couche-4"]
---
# Registre des terminologies

**Contenu normatif.** Ce composant gère les terminologies médicales et de référence (CIM-10, SNOMED CT, LOINC, ATC, etc.). Il assure le mapping sémantique entre les systèmes et fournit les services de traduction et de validation des codages.

**Discipline de mise en œuvre.** Il sert de pont sémantique entre les systèmes hétérogènes. Il garantit que les données codées dans un système sont interprétables et exploitables par un autre.

- **Rattachement** : [ART-4](../chapitres/art-4.md) (référentiel des métadonnées), [CAP-INT-09: Gestion des consentements et bases d’autorisation](../capacites/cap-int-09.md).
- **Processus soutenus** : [PRC-07: Identification et droits des bénéficiaires](../processus/prc-07.md) (production données), [PRC-08: Financement et exemption au point de service](../processus/prc-08.md) (qualité).
- **Statut : Stable.**