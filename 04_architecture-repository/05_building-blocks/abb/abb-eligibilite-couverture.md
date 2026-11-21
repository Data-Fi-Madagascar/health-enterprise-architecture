---
domain: abb
id: ABB-ELIGIBILITE-COUVERTURE
type: architecture-building-block
niveau: "2"
title: Éligibilité et couverture sanitaire
status: candidate
owner: DEPSI
version: "0.1"
building_block_role: ABB
building_block_domain: application
togaf_repository_section: reference-library
togaf_adm_phase: C
architecture_level: enterprise
architecture_domain: application
architecture_scope: financial-protection
architecture_state: target
partitions: ["PART-VS-03"]
maps_to: ["CAP-07"]
implements: ["ART-4C", "ART-9"]
accesses: ["DO-14", "DO-15", "DO-16", "DO-17"]
related: ["PART-VS-03", "PRC-09", "PRC-10"]
tags: ["abb", "eligibilite", "couverture", "protection-financiere"]
---
# Éligibilité et couverture sanitaire

## Finalité

Cet ABB porte les services nationaux de consultation de la couverture et de vérification des droits au point de service. Il contribue à la [CAP-07 : Protection financière et couverture santé universelle](../../02_architecture-elements/strategy/capabilities/cap-07.md) dans la [partition VS-03](../../01_partitions/value-streams/part-vs-03.md), conformément à [ART-4C](../../04_patterns/artsn-rules/art-4c.md) et [ART-9](../../04_patterns/artsn-rules/art-9.md).

La démarche collaborative HEAL guide l'évaluation des règles de droits avec les programmes. HEAF situe ce bloc dans la couche applicative du flux de protection financière ; HEART privilégie un contrat d'échange réutilisable et des métadonnées générées depuis le référentiel.

## Services attendus

- consulter la couverture applicable à une personne et ses périodes de validité ;
- vérifier les droits pour une prestation, un programme et une date donnés ;
- produire une décision temporelle explicite, avec sa source, sa période de validité et les règles appliquées ;
- conserver la preuve de chaque vérification et une piste d'audit permettant d'expliquer une décision ultérieure ;
- exposer les données nécessaires aux processus [PRC-09](../../02_architecture-elements/business/processes/prc-09.md) et [PRC-10](../../02_architecture-elements/business/processes/prc-10.md).

L'ABB consulte les objets [DO-14 : Éligibilité](../../02_architecture-elements/data/data-objects/do-14.md), [DO-15 : Couverture sanitaire](../../02_architecture-elements/data/data-objects/do-15.md), [DO-16 : Facturation](../../02_architecture-elements/data/data-objects/do-16.md) et [DO-17 : Vérification d'éligibilité](../../02_architecture-elements/data/data-objects/do-17.md). Leur échange s'appuie sur HL7 FHIR R4, sans imposer de produit.

## Séparation des responsabilités

La résolution de l'identité bénéficiaire relève de [ABB-IDENTITE-BENEFICIAIRE](abb-identite-beneficiaire.md). La gestion du consentement et des autres bases d'autorisation relève de [ABB-GESTION-CONSENTEMENT](abb-gestion-consentement.md). Une identité résolue ou une autorisation d'accès ne constitue pas, à elle seule, une preuve de couverture ou une décision d'éligibilité. L'ABB d'éligibilité utilise les résultats autorisés de ces services sans en reprendre la responsabilité.
