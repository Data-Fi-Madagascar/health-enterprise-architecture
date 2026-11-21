---
domain: specs
id: hea-review-gaps-design
title: Conception des corrections de cohérence HEA
version: "1.0"
status: active
last_reviewed: 2026-09-24
owner: DEPSI
tags: ["hea", "togaf", "coherence", "validation"]
---

# Conception des corrections de cohérence HEA

## Objectif

Rétablir un pipeline de validation vert, compléter le métamodèle TOGAF, corriger les mappings sémantiques hérités et produire une vue dérivée par partition sans dupliquer les objets du référentiel canonique.

## Principes de conception

`04_architecture-repository` reste la source canonique. Les documents publiés et les vues TOGAF sont des artefacts dérivés, régénérés par les scripts existants. Les corrections sémantiques sont décidées objet par objet à partir de la finalité métier, et non par substitution textuelle globale.

Le travail est divisé en quatre lots indépendamment validables. Chaque lot se termine par les contrôles ciblés, la régénération nécessaire et un commit dédié.

## Lot 1: rétablissement du pipeline

Le conflit résiduel de `scripts/validate_ref.py` est supprimé en conservant `REL_DIRS = [ARCH_REPOSITORY_DIR]` et `ADR_DIRS = ["01_cnisn/06_decisions"]`. Un test de régression vérifie l'absence de marqueurs Git et le maintien de ces deux constantes. Les artefacts actuellement désynchronisés sont régénérés avant l'exécution du pipeline complet.

## Lot 2: métamodèle TOGAF

Le schéma canonique documente les champs `partition_kind`, `togaf_repository_section`, `togaf_adm_phase`, `architecture_level`, `architecture_domain`, `architecture_scope`, `architecture_state`, `partitions`, `building_block_role`, `building_block_domain` et `legacy_id`.

Le champ `partitions` devient une relation de graphe. Le validateur résout chacune de ses cibles et exige que la cible porte le type `architecture-partition`. Un test négatif couvre une cible existante de type incorrect et un test positif couvre une partition valide.

## Lot 3: mappings sémantiques

Les services SRV-03 à SRV-06, le profil PT-01, la matrice PTISN et les composants CMP-10, CMP-11, CMP-12, CMP-14 et CMP-23 sont revus selon leur responsabilité métier. Les cibles principales attendues sont les suivantes:

- terminologie et codification: `ABB-SERVICE-TERMINOLOGIE`;
- identité bénéficiaire: `ABB-IDENTITE-BENEFICIAIRE`;
- logistique LMIS: `ABB-ECHANGE-LOGISTIQUE-LMIS`;
- transport et médiation: `ABB-ECHANGE-MEDIATION`;
- pilotage et exposition analytique: `ABB-EXPOSITION-DONNEES-ANALYTIQUES`.

Les relations complémentaires sont conservées uniquement lorsqu'elles expriment une responsabilité réelle, par exemple l'audit comme exigence transverse d'un flux logistique, et non comme ABB principal du LMIS. Toute ambiguïté restante est signalée dans la PR.

## Lot 4: vue dérivée par partition

Une vue TOGAF est générée à partir des frontmatters canoniques. Pour chaque objet de type `architecture-partition`, le générateur parcourt les relations du graphe et présente au minimum la chaîne `PART -> VS -> CAP -> PRC -> DO/ABB/SBB`. La vue ne crée aucun nouvel objet et ne recopie pas manuellement les métadonnées.

Le script de génération doit rester déterministe. Le mode `--check` du pipeline détecte toute divergence entre la source canonique et la vue publiée.

## Validation et livraison

Les contrôles ciblés précèdent le contrôle global. La preuve finale est un `make check` complet avec code de sortie nul. La branche dédiée est poussée et une PR est ouverte sans fusion. La description de PR sépare les corrections P0 et P1, inventorie les mappings corrigés et explicite les éventuels points ambigus.
