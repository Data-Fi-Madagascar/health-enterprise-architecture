---

title: "Logistique"
id: artsn-ART-10
domain: 04_patterns
version: "1.0.0"
status: draft
last_reviewed: 2026-08-12
owner: DEPSI
tags: ["artsn", "chapitres", "ART-10", "niveau-3"]
related: ["CAP-INT-10"]
---
# Logistique

## Pour qui lire ce document

**Niveau :** niveau 3 : Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.


ART-10 : Logistique constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `ART-10`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Statut : candidate**

**Contenu normatif.** La continuité de la chaîne d'approvisionnement (médicaments, vaccins, intrants, équipements) conditionne l'exécution des flux de valeur de soins. L'architecture impose une traçabilité de bout en bout des mouvements de produits, de la centrale d'achat jusqu'au point de service : chaque mouvement (livraison, dispensation, transfert, destruction) est un événement immuable, horodaté, adossé aux référentiels de produits, et réconcilié selon les règles comptables de conservation de quantité (Entrées − Sorties = Solde).

**Discipline de mise en œuvre.** Dès qu'une source échappe à la gouvernance directe de l'initiative (centres de stockage isolés, ruptures de connectivité, circuits parallèles de distribution), cette discipline seule permet de garantir la disponibilité des intrants et la réconciliation à somme nulle des stocks sans rompre le pipeline.

- **Rattachement** : [CAP-10: Gestion des médicaments, vaccins, intrants et chaîne d'approvisionnement](../../referentiel/capabilites/cap-10.md) (chaîne d'approvisionnement), [CAP-11: Gestion des infrastructures, équipements et maintenance](../../referentiel/capabilites/cap-11.md) (infrastructures et équipements).
- **Modèles cibles** : événementisation des mouvements de stock, registres logistiques (ex. OpenLMIS), traçabilité par lot.
- **Déduit selon** : [ENF-2: Intégrité des flux et traçabilité des valeurs](../../referentiel/exigences/enf-2.md) (traçabilité des valeurs).
- **Statut : Provisoire.**

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`ART-10`** : Logistique (`referentiel/chapitres/art-10.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/04_patterns/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
