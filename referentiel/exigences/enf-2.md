---

id: ENF-2
type: exigence
niveau: "3"
title: Intégrité des flux et traçabilité des valeurs
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/02_exigences-contextuelles/index.md
maps_to: []
implements: []
applies_to: []
related: ["ART-9", "ART-4C", "ART-8C"]
tags: ["artsn", "niveau-3", "exigence", "ENF-2"]
---
# Intégrité des flux et traçabilité des valeurs

**Contenu normatif.** Le déploiement national de la gratuité ciblée, des subventions de l’État et des mécanismes de la Couverture Santé Universelle (CSU) présente un risque systémique élevé de fraude, de double facturation, de falsification d’ordonnances et de détournement de stocks. L’architecture doit interdire toute modification, suppression ou altération rétroactive des transactions logistiques et financières validées. Tout mouvement de valeur (Ariary ou unités physiques de médicaments) doit obéir à des règles strictes de **double écriture comptable** et de **conservation de quantité** (Entrées − Sorties = Solde), garantissant une réconciliation exacte à somme nulle.

**Statut : Stable.** — appliqué par [ART-9 (garanties transactionnelles)](../chapitres/art-9.md), [ART-4c (éligibilité)](../chapitres/art-4c.md), [ART-8c (agrégation par lot)](../chapitres/art-8c.md).

## Justification

Le déploiement national de la gratuité ciblée, des subventions et de la CSU crée un risque systémique de fraude, de double facturation et de détournement de stocks. Cette exigence interdit toute altération rétroactive des transactions et impose la double écriture comptable pour garantir une réconciliation à somme nulle. Elle protège l’argent public et la confiance des ménages dans les mécanismes de protection financière.

## Capabilités concernées

- **CAP-07** — Protection financière, couverture santé universelle
- **CAP-10** — Gestion des médicaments, vaccins, intrants et chaîne d'approvisionnement
- **CAP-12** — Finances publiques, budget et allocation des ressources
- **CAP-13** — Système d'information sanitaire, données et recherche

## Parties prenantes concernées

- **PP-02** — Ménage et famille
- **PP-06** — Formation sanitaire
- **PP-08** — Partenaires techniques et financiers

## Fondations et chapitres garants

- **ART-9** — Garanties transactionnelles fortes
- **ART-4c** — Éligibilité et couverture
- **ART-8c** — Agrégation par lot
