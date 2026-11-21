---

title: "Feuille de route technique de l'ARTSN"
id: artsn-feuille-de-route
domain: 10_feuille-de-route
version: "1.0.0"
status: draft
last_reviewed: 2026-11-21
owner: DEPSI
tags: ["artsn", "migration", "plateaux", "ecarts", "niveau-3"]
---

# Feuille de route technique de l'ARTSN

## Pour qui lire ce document

**Niveau :** niveau 3 : Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## Objet

La feuille de route technique de l'ARTSN décrit le chemin de migration de l'existant vers l'architecture cible. Elle procède en deux séries complémentaires : des plateaux, qui désignent des états cibles successifs du système, et des écarts, qui désignent les risques connus au sein de ces états cibles et qui ne sont pas levés par le seul fait d'atteindre le plateau correspondant.

Cette distinction est la raison d'être de cette section. Un plateau décrit un état atteignable, donc un engagement de livraison ; un écart décrit une fragilité qui survit à l'atteinte de cet état. Le gap de couverture terrain en zone isolée, par exemple, ne disparaît pas lorsque le socle technique du plateau 1 est opérationnel : il conditionne la conception même des applications de terrain du plateau 2. Confondre les deux reviendrait à croire qu'un palier de livraison épuise les risques attachés aux paliers suivants.

## Plateaux

| Plateau | État cible | Contenu dominant |
|---------|------------|------------------|
| PL-01 | Socle et confiance numérique | Infrastructure opérationnelle, sécurité de confiance, gouvernance des données publiée, référentiels de base disponibles |
| PL-02 | Services de terrain et interopérabilité | Applications de terrain déployées, médiation opérationnelle, registres nationaux actifs, premiers échanges interinstitutionnels |
| PL-03 | Intelligence et ouverture | Entrepôt analytique, tableaux de bord, extension nationale, interopérabilité transfrontalière et coordination One Health |

## Écarts

| Écart | Position | Portée |
|-------|----------|--------|
| GAP-01 | Entre le plateau 1 et le plateau 2 | Les applications de terrain du lot L2 doivent fonctionner en connectivité contrainte avant la généralisation du socle régional du lot L1, sous peine d'exclure les zones les plus isolées |
| GAP-02 | Entre le plateau 2 et le plateau 3 | L'ouverture internationale (GDHCN) et la coordination intersectorielle One Health ne sont couvertes qu'au dernier plateau, ce qui retarde la part de valeur liée aux échanges régionaux et à la surveillance multi-ministères |
| GAP-03 | Entre l'état initial et le plateau 1 | Le décret CNASN et la charte de protection doivent être publiés pour valider juridiquement le socle, faute de quoi le déploiement évolue en zone de risque réglementaire |

## Liens

La mise en œuvre des lots techniques est décrite dans la feuille de route des lots du portefeuille, et la relation entre chaque lot et les chapitres ART qu'il réalise est établie dans la section des chapitres et patterns de référence.

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **Feuille de route des lots** : Réalisation technique ARTSN des lots du portefeuille (`02_artsn/08_lots/index.md`)
- **Chapitres et patterns de référence** : Chapitres et patterns de référence (`02_artsn/04_patterns/index.md`)

## Documents de la section

- [PL-01: Plateau 1 — Socle & confiance numérique](pl-01-plateau-1-socle-confiance-num-rique.md)
- [PL-02: Plateau 2 — Services de terrain & interopérabilité](pl-02-plateau-2-services-de-terrain-interop-rabilit.md)
- [PL-03: Plateau 3 — Intelligence & ouverture](pl-03-plateau-3-intelligence-ouverture.md)
- [GAP-01: Écart — Couverture terrain en zone isolée](gap-01-cart-couverture-terrain-en-zone-isol-e.md)
- [GAP-02: Écart — Interopérabilité transfrontalière & One Health](gap-02-cart-interop-rabilit-transfrontali-re-one-health.md)
- [GAP-03: Écart — Cadre légal & gouvernance publié](gap-03-cart-cadre-l-gal-gouvernance-publi.md)

<!-- liens-section-auto -->
