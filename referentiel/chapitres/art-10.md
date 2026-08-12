---
id: art-10
type: chapitre
niveau: "3"
title: ART-10 — Logistique
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/03_chapitres/art-10-logistique.md
maps_to: ["cap-10", "cap-11"]
implements: []
applies_to: ["enf-2"]
related: []
tags: ["artsn", "niveau-3", "chapitre", "art-10"]
---
# ART-10 — Logistique

**Contenu normatif.** La continuité de la chaîne d'approvisionnement (médicaments, vaccins, intrants, équipements) conditionne l'exécution des flux de valeur de soins. L'architecture impose une traçabilité de bout en bout des mouvements de produits, de la centrale d'achat jusqu'au point de service : chaque mouvement (livraison, dispensation, transfert, destruction) est un événement immuable, horodaté, adossé aux référentiels de produits, et réconcilié selon les règles comptables de conservation de quantité (Entrées − Sorties = Solde).

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (centres de stockage isolés, ruptures de connectivité, circuits parallèles de distribution) : elle seule permet de garantir la disponibilité des intrants et la réconciliation à somme nulle des stocks sans rompre le pipeline.

- **Rattachement** : [CAP-10](../capabilites/cap-10.md) (chaîne d'approvisionnement), [CAP-11](../capabilites/cap-11.md) (infrastructures et équipements).
- **Modèles cibles** : événementisation des mouvements de stock, registres logistiques (ex. OpenLMIS), traçabilité par lot.
- **Déduit selon** : [ENF-2](../exigences/enf-2.md) (traçabilité des valeurs).
- **Statut : Provisoire.**