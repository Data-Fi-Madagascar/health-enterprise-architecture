---
id: ART-10
type: chapitre
niveau: "3"
title: Logistique
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/03_chapitres/art-10-logistique.md
maps_to: ["CAP-10", "CAP-11"]
implements: []
applies_to: ["ENF-2"]
related: []
tags: ["artsn", "niveau-3", "chapitre", "ART-10"]
---
# Logistique

**Contenu normatif.** La continuité de la chaîne d'approvisionnement (médicaments, vaccins, intrants, équipements) conditionne l'exécution des flux de valeur de soins. L'architecture impose une traçabilité de bout en bout des mouvements de produits, de la centrale d'achat jusqu'au point de service : chaque mouvement (livraison, dispensation, transfert, destruction) est un événement immuable, horodaté, adossé aux référentiels de produits, et réconcilié selon les règles comptables de conservation de quantité (Entrées − Sorties = Solde).

**Discipline de mise en œuvre.** Dès qu'une source échappe à la gouvernance directe de l'initiative (centres de stockage isolés, ruptures de connectivité, circuits parallèles de distribution), cette discipline seule permet de garantir la disponibilité des intrants et la réconciliation à somme nulle des stocks sans rompre le pipeline.

- **Rattachement** : [CAP-10: Gestion des médicaments, vaccins, intrants et chaîne d'approvisionnement](../capabilites/cap-10.md) (chaîne d'approvisionnement), [CAP-11: Gestion des infrastructures, équipements et maintenance](../capabilites/cap-11.md) (infrastructures et équipements).
- **Modèles cibles** : événementisation des mouvements de stock, registres logistiques (ex. OpenLMIS), traçabilité par lot.
- **Déduit selon** : [ENF-2: Intégrité des flux et traçabilité des valeurs](../exigences/enf-2.md) (traçabilité des valeurs).
- **Statut : Provisoire.**