---
title: "Exigences contextuelles nationales"
id: artsn-exigences-contextuelles
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, exigences, contexte, niveau-3]
---

# Exigences contextuelles nationales

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](./reading-matrix.md).


Les exigences contextuelles traduisent les contraintes nationales (géographie, réseau, interopérabilité inter-institutionnelle) en obligations qui s'imposent à tout chapitre et à toute solution. Chaque exigence vit dans le référentiel : `referentiel/exigences/enf-X.md`.

## Catalogue des exigences

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

### ENF-1 — Résilience à l’instabilité réseau

**Contenu normatif.** La connectivité internet et la couverture mobile (3G/4G/Fibre) sont hautement asymétriques, intermittentes, voire inexistantes dans la majorité des districts ruraux et des Centres de Santé de Base (CSB). L’indisponibilité, la coupure ou la dégradation du réseau ne doit en aucun cas bloquer, ralentir ou altérer l’acte clinique, la dispensation pharmaceutique au comptoir ou la saisie logistique. Tout logiciel et base de données utilisés sur le point de service a l’obligation structurelle de **capturer, valider et persister les transactions de manière 100% locale et autonome**, puis de gérer des mécanismes de **synchronisation asynchrone** pour différer la transmission centrale dès le retour de la connectivité.

**Statut : Stable.** — appliqué par [F.1](../referentiel/fondations/f-1.md), [ART-1](../referentiel/chapitres/art-1.md), [Couche 2 (point de service)](04_cartographie-cible.md#couche-2--point-de-service).

*Rattachement : — · [fiche](../referentiel/exigences/enf-1.md)*

### ENF-2 — Intégrité des flux et traçabilité des valeurs

**Contenu normatif.** Le déploiement national de la gratuité ciblée, des subventions de l’État et des mécanismes de la Couverture Santé Universelle (CSU) présente un risque systémique élevé de fraude, de double facturation, de falsification d’ordonnances et de détournement de stocks. L’architecture doit interdire toute modification, suppression ou altération rétroactive des transactions logistiques et financières validées. Tout mouvement de valeur (Ariary ou unités physiques de médicaments) doit obéir à des règles strictes de **double écriture comptable** et de **conservation de quantité** (Entrées − Sorties = Solde), garantissant une réconciliation exacte à somme nulle.

**Statut : Stable.** — appliqué par [ART-9 (garanties transactionnelles)](../referentiel/chapitres/art-9.md), [ART-4c (éligibilité)](../referentiel/chapitres/art-4c.md), [ART-8c (agrégation par lot)](../referentiel/chapitres/art-8c.md).

*Rattachement : — · [fiche](../referentiel/exigences/enf-2.md)*

### ENF-3 — Unicité de l’identité et résilience face à la fragmentation applicative

**Contraintes contextuelles.** Le paysage numérique historique est caractérisé par une dispersion de solutions logicielles et de bases de données isolées. Un même citoyen possède des fiches cliniques, des dossiers et des identifiants locaux différents selon les hôpitaux ou les programmes verticaux (Malariologie, Tuberculose, Vaccination), ce qui menace la sécurité des soins et empêche le suivi médical longitudinal.

**Contenu normatif.** Le système national doit posséder la capacité de rapprocher, consolider et unifier des identités de patients incertains, phonétiquement variables ou incomplètes. Cette brique d’**identitovigilance** doit générer un enregistrement pivot unique et souverain pour le citoyen, sans forcer le remplacement immédiat ou la refonte structurelle des bases locales des hôpitaux.

**Statut : Stable.** — appliqué par [ART-4a (résolution d’identité)](../referentiel/chapitres/art-4a.md), [ART-2 (médiation)](../referentiel/chapitres/art-2.md).

*Rattachement : — · [fiche](../referentiel/exigences/enf-3.md)*

### ENF-4 — Cloisonnement inter-institutionnel et étanchéité des données (One Health)

**Contraintes contextuelles.** Le croisement de données massives entre le Ministère de la Santé (données cliniques), l’Agriculture et l’Élevage (zoonoses) et l’Environnement (climat, pollution) implique la manipulation de taxonomies, de secrets professionnels et de bases légales juridiquement et éthiquement étanches.

**Contenu normatif.** Le partage d’informations intersectoriel à des fins de recherche ou d’alerte épidémique précoce doit préserver la souveraineté de chaque institution, respecter le secret médical et protéger la vie privée des citoyens. Les pipelines de traitement analytique ont l’obligation d’opérer sur des données **définitivement dépouillées de tout identifiant direct** (Noms, INS). Les corrélations entre secteurs ne doivent s’effectuer qu’avec des dimensions de rapprochement **neutres et non nominatives** : l’espace géographique et le temps.

**Statut : Stable.** — appliqué par [ART-0 (accords de partage)](../referentiel/chapitres/art-0.md), [ART-4b (bases d’autorisation)](../referentiel/chapitres/art-4b.md), [ART-4d (référentiel géospatial)](../referentiel/chapitres/art-4d.md).

*Rattachement : — · [fiche](../referentiel/exigences/enf-4.md)*

### ENF-5 — Coordination des processus complexes décentralisés et asynchrones

**Contraintes contextuelles.** Les parcours de soins critiques (référence d’un CSB rural vers un hôpital de district, contre-référence ascendante vers un CHU central, ou évacuation sanitaire internationale) s’étendent sur des fenêtres temporelles de plusieurs jours et impliquent des structures sanitaires autonomes sans lien hiérarchique ou technique direct.

**Contenu normatif.** Le système national doit être capable de suivre et d’orchestrer l’état d’avancement d’un parcours de soins distribué à étapes multiples, de bout en bout. L’architecture doit tolérer les interruptions temporaires de transmission, tout en garantissant le déclenchement automatique d’alertes d’escalade ou d’annulations (compensations) fonctionnelles si un établissement de destination est saturé ou inaccessible.

**Statut : Stable.** — appliqué par [ART-8a (orchestration de processus borné)](../referentiel/chapitres/art-8a.md), [ART-5 (qualité des données)](../referentiel/chapitres/art-5.md).

*Rattachement : — · [fiche](../referentiel/exigences/enf-5.md)*

<!-- END:GENERATED -->
## Liens

- [Fondations](./00_fondations.md)
- [Chapitres et patterns de référence](./03_chapitres/index.md)
- [Cartographie cible](./04_cartographie-cible.md)
