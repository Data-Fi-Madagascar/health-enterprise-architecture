---
domain: legacy-components
id: CMP-12
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Registre d'éligibilité et de couverture (CSU — ART-4C)
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
maps_to: ["CAP-07"]
implements: ["ART-4C"]
applies_to: ["PRC-09", "PRC-10"]
related: ["CAP-07", "VS-03"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-12", "couche-4"]
realized_by: ["WP-03"]
---
# Registre d'éligibilité et de couverture (CSU — ART-4C)

**Contenu normatif.** Ce composant gère les données d'éligibilité et de couverture santé (CSU). Il assure la vérification en temps réel des droits des patients et fournit les services de contrôle d'éligibilité pour les applications métier.

**Discipline de mise en œuvre.** Il est l'autorité de vérification des droits. Toute opération de soins nécessitant une vérification de couverture transite par ce registre, ce qui garantit la conformité financière.

- **Rattachement** : [ART-4C](../../../04_patterns/artsn-rules/art-4c.md) (éligibilité/couverture), [CAP-07: Protection financière, couverture santé universelle](../../../02_architecture-elements/strategy/capabilities/cap-07.md). Aucun ABB distinct ne modélise encore le registre d'éligibilité : le rattachement direct à la capacité évite de le confondre avec le consentement ou l'identité.
- **Processus soutenus** : [PRC-09: Remboursement et régulation des mécanismes](../../../02_architecture-elements/business/processes/prc-09.md) (finance), [PRC-10: Planification et allocation des ressources](../../../02_architecture-elements/business/processes/prc-10.md) (planification).
- **Statut : Stable.**
