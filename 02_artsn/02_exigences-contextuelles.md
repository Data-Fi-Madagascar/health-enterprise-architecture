---
title: Exigences et contraintes contextuelles nationales
id: artsn-exigences-contextuelles
domain: 02_artsn
version: "0.1.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, exigences, contraintes, niveau-3]
---

# Exigences et contraintes contextuelles nationales

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](reading-matrix.md).

Pour transposer les flux de valeur en patterns techniques de référence applicables, la plateforme numérique nationale de santé doit résoudre des contraintes physiques, infrastructurelles et réglementaires propres au contexte malgache. Ces exigences dictent la transition logique entre l'objectif de santé publique et la conception du système d'information.

## ENF-1 — Résilience à l'instabilité réseau

**Contenu normatif.** La connectivité internet et la couverture mobile (3G/4G/Fibre) sont hautement asymétriques, intermittentes, voire inexistantes dans la majorité des districts ruraux et des Centres de Santé de Base (CSB). L'indisponibilité, la coupure ou la dégradation du réseau ne doit en aucun cas bloquer, ralentir ou altérer l'acte clinique, la dispensation pharmaceutique au comptoir ou la saisie logistique. Tout logiciel et base de données utilisés sur le point de service a l'obligation structurelle de **capturer, valider et persister les transactions de manière 100% locale et autonome**, puis de gérer des mécanismes de **synchronisation asynchrone** pour différer la transmission centrale dès le retour de la connectivité.

**Statut : Stable.** — appliqué par [F.1](./00_fondations.md#f1--résilience-face-à-la-réalité-géographique-du-pays), [ART-1](./03_chapitres/art-1-integration-ingestion.md), [Couche 2 (point de service)](./04_cartographie-cible.md#couche-2--point-de-service).

## ENF-2 — Intégrité des flux et traçabilité des valeurs

**Contenu normatif.** Le déploiement national de la gratuité ciblée, des subventions de l'État et des mécanismes de la Couverture Santé Universelle (CSU) présente un risque systémique élevé de fraude, de double facturation, de falsification d'ordonnances et de détournement de stocks. L'architecture doit interdire toute modification, suppression ou altération rétroactive des transactions logistiques et financières validées. Tout mouvement de valeur (Ariary ou unités physiques de médicaments) doit obéir à des règles strictes de **double écriture comptable** et de **conservation de quantité** (Entrées − Sorties = Solde), garantissant une réconciliation exacte à somme nulle.

**Statut : Stable.** — appliqué par [ART-9 (garanties transactionnelles)](./03_chapitres/art-9-garanties-transactionnelles.md), [ART-4c (éligibilité)](./03_chapitres/art-4c-eligibilite-couverture.md), [ART-8c (agrégation par lot)](./03_chapitres/art-8c-agregation-par-lot.md).

## ENF-3 — Unicité de l'identité et résilience face à la fragmentation applicative

**Contraintes contextuelles.** Le paysage numérique historique est caractérisé par une dispersion de solutions logicielles et de bases de données isolées. Un même citoyen possède des fiches cliniques, des dossiers et des identifiants locaux différents selon les hôpitaux ou les programmes verticaux (Malariologie, Tuberculose, Vaccination), ce qui menace la sécurité des soins et empêche le suivi médical longitudinal.

**Contenu normatif.** Le système national doit posséder la capacité de rapprocher, consolider et unifier des identités de patients incertains, phonétiquement variables ou incomplètes. Cette brique d'**identitovigilance** doit générer un enregistrement pivot unique et souverain pour le citoyen, sans forcer le remplacement immédiat ou la refonte structurelle des bases locales des hôpitaux.

**Statut : Stable.** — appliqué par [ART-4a (résolution d'identité)](./03_chapitres/art-4a-resolution-identite.md), [ART-2 (médiation)](./03_chapitres/art-2-mediation-normalisation.md).

## ENF-4 — Cloisonnement inter-institutionnel et étanchéité des données (One Health)

**Contraintes contextuelles.** Le croisement de données massives entre le Ministère de la Santé (données cliniques), l'Agriculture et l'Élevage (zoonoses) et l'Environnement (climat, pollution) implique la manipulation de taxonomies, de secrets professionnels et de bases légales juridiquement et éthiquement étanches.

**Contenu normatif.** Le partage d'informations intersectoriel à des fins de recherche ou d'alerte épidémique précoce doit préserver la souveraineté de chaque institution, respecter le secret médical et protéger la vie privée des citoyens. Les pipelines de traitement analytique ont l'obligation d'opérer sur des données **définitivement dépouillées de tout identifiant direct** (Noms, INS). Les corrélations entre secteurs ne doivent s'effectuer qu'avec des dimensions de rapprochement **neutres et non nominatives** : l'espace géographique et le temps.

**Statut : Stable.** — appliqué par [ART-0 (accords de partage)](./03_chapitres/art-0-accords-partage.md), [ART-4b (bases d'autorisation)](./03_chapitres/art-4b-bases-autorisation.md), [ART-4d (référentiel géospatial)](./03_chapitres/art-4d-referentiel-geospatial.md).

## ENF-5 — Coordination des processus complexes décentralisés et asynchrones

**Contraintes contextuelles.** Les parcours de soins critiques (référence d'un CSB rural vers un hôpital de district, contre-référence ascendante vers un CHU central, ou évacuation sanitaire internationale) s'étendent sur des fenêtres temporelles de plusieurs jours et impliquent des structures sanitaires autonomes sans lien hiérarchique ou technique direct.

**Contenu normatif.** Le système national doit être capable de suivre et d'orchestrer l'état d'avancement d'un parcours de soins distribué à étapes multiples, de bout en bout. L'architecture doit tolérer les interruptions temporaires de transmission, tout en garantissant le déclenchement automatique d'alertes d'escalade ou d'annulations (compensations) fonctionnelles si un établissement de destination est saturé ou inaccessible.

**Statut : Stable.** — appliqué par [ART-8a (orchestration de processus borné)](./03_chapitres/art-8a-orchestration-processus-borne.md), [ART-5 (qualité des données)](./03_chapitres/art-5-coherence-qualite-donnees.md).

## Liens

- [Fondations](./00_fondations.md)
- [Flux de valeur](./01_flux-de-valeur.md)
- [Chapitres et patterns de référence](./03_chapitres/index.md)
