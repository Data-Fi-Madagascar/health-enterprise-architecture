---
domain: abb
id: ABB-REGISTRE-PROFESSIONNELS
type: architecture-building-block
niveau: "2"
title: Registre et résolution des professionnels de santé
status: candidate
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-02
envelope: 01_cnisn/02_capacites/index.md
building_block_role: ABB
building_block_domain: data
togaf_repository_section: reference-library
togaf_adm_phase: C
architecture_level: enterprise-transversal
architecture_domain: data
architecture_scope: interoperability
architecture_state: target
partitions: ["PART-TRANSVERSE-IDENTITE"]
maps_to: ["CAP-09", "CAP-14"]
implements: ["ART-4", "ART-4A", "ART-7", "ART-4C"]
related: ["PART-TRANSVERSE-IDENTITE", "P-INT-01", "P-INT-02", "P-INT-03", "P-INT-04", "P-INT-14", "P-INT-15"]
tags: ["cnisn", "abb", "professionnels", "interoperabilite"]
---
# Registre et résolution des professionnels de santé

## Finalité

Permettre de déterminer l'identité professionnelle, la qualification, le statut et l'affectation d'un professionnel ou travailleur de santé.

## Services attendus

- recherche d'un professionnel ;
- vérification de la profession ;
- vérification de la qualification ;
- vérification de la licence ;
- vérification du statut d'exercice ;
- consultation de l'affectation ;
- consultation des habilitations ;
- historisation des changements.

## Principe de séparation

Ce bloc d'architecture est distinct :

- de l'authentification ;
- du registre des bénéficiaires ;
- de l'identité fondationnelle ;
- de la décision d'autorisation.

## Principes associés

- [P-INT-01: Autorité désignée](../../02_architecture-elements/motivation/principles/p-int-01.md)
- [P-INT-02: Résolution contre l'autorité](../../02_architecture-elements/motivation/principles/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../../02_architecture-elements/motivation/principles/p-int-03.md)
- [P-INT-04: Historisation des références](../../02_architecture-elements/motivation/principles/p-int-04.md)
- [P-INT-14: Base d'autorisation explicite](../../02_architecture-elements/motivation/principles/p-int-14.md)
- [P-INT-15: Limitation à la finalité](../../02_architecture-elements/motivation/principles/p-int-15.md)

## Articulation avec la paie et les habilitations

- La résolution des professionnels alimente la [CAP-09: Gestion des ressources humaines en santé](../../02_architecture-elements/strategy/capabilities/cap-09.md) et les habilitations rattachées à la [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../../02_architecture-elements/strategy/capabilities/cap-15.md) ; elle ne gère pas la rémunération.
- Échange financier associé : [PT-18: Échange de réclamations et paiements](../../../03_ptisn/03_profils/pt-18-echange-reclamations-paiements.md).
