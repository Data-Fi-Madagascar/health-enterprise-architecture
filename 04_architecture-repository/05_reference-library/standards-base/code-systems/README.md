---
title: "Bases de codes : terminologies et données de référence"
domain: code-systems
id: README-CODE-SYSTEMS
type: meta
status: active
version: "1.0.0"
owner: DEPSI
niveau: "3"
tags: ["referentiel", "standards-base", "code-systems", "terminologie"]
---

# Bases de codes : terminologies et données de référence

Ce dossier regroupe les **vocabulaires contrôlés** du référentiel HEA. Il matérialise la face sémantique de la `standards-base` : là où les profils d'interopérabilité décrivent des échanges de messages, les bases de codes décrivent les **valeurs admises** dans les champs de ces messages. Les deux notions sont complémentaires, et le compilateur ODA les exploite conjointement pour produire les schémas d'exécution.

## Contenu du dossier

Le dossier héberge deux familles d'objets, dont la distinction repose sur le degré de contrôle exercé sur le code lui-même.

| Famille | Préfixe | Nombre | Exemple |
|---------|---------|--------|---------|
| Terminologie | `TERM-` | 7 | [TERM-CIM-11](term-cim-11.md), classification internationale des maladies |
| Donnée de référence | `RD-` | 2 | [RD-STRUCTURES-SERVICES](rd-structures-services.md), référentiel national des formations sanitaires |

C'est précisément cette frontière qui distingue les deux familles. Une **terminologie** est un référentiel externe dont le code est produit et gouverné par un tiers : le HEA en consomme les codes sans les produire, et se contente d'indiquer, pour chaque champ de données concerné, quelle terminologie fait autorité. Une **donnée de référence** relève au contraire d'une gouvernance nationale : le HEA en est le maître, ce qui autorise le référentiel à fixer lui-même les listes de valeurs.

## Rôle dans la chaîne de production

La chaîne de compilation ODA transforme ces objets en artefacts exécutables. Chaque terminologie produit une ressource `CodeSystem` FHIR R4 et, le cas échéant, un schéma JSON Schema de payload ; chaque donnée de référence produit un catalogue de valeurs contrôlées. Cette transformation est entièrement automatique : le fichier Markdown de ce dossier constitue l'unique source de vérité, et le pipeline `scripts/compilers/compile_oda.py` répercute toute modification de statut, de version ou de liste de codes vers `dist/`.

Cette automatisation a une conséquence de gouvernance directe. Un vocabulaire publié ici n'est pas seulement décrit, il est **exécutable**. Toute modification du contenu d'un code se répercute immédiatement sur les messages échangés en production, ce qui justifie un cycle de revue formel pour toute évolution de liste de codes.

## Règles d'introduction

L'introduction d'un nouveau vocabulaire dans ce dossier est un acte de gouvernance et non une simple création de fiche. Elle suppose de documenter la source des codes, l'autorité qui les publie, la version de référence retenue, et les objets de données que le vocabulaire contraint. Cette dernière relation est déjà matérialisée dans les frontmatters par le champ `constrains`, dont la validation SHACL impose la cohérence de type.

C'est cette relation de contrainte qui donne au dossier sa valeur normative. Une terminologie sans objet de données contraint n'apporte rien : elle documente un usage sans le garantir.

## Références

- [Schéma du référentiel](../../../00_metamodel/schema.md) : types d'objets et répertoires canoniques
- [Annexe J : Guide de conception ODA](../../../../02_artsn/09_annexes/j-oda-conception-guide.md) : chaîne de compilation et pont entre modèle de gouvernance et modèle d'exécution
- [Profils d'interopérabilité](../profiles/) : qui consomment les valeurs produites par les bases de codes
