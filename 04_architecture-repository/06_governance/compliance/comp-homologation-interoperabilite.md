---
domain: compliance
id: COMP-HOMOLOGATION-INTEROPERABILITE
type: compliance-rule
niveau: "2"
title: Homologation d'interopérabilité
status: candidate
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-12
envelope: 01_cnisn/02_capacites/index.md
togaf_repository_section: governance-log
togaf_adm_phase: G
architecture_level: enterprise-transversal
architecture_domain: governance
architecture_scope: interoperability
architecture_state: target
maps_to: ["CAP-14", "CAP-16"]
implements: ["F-4"]
related: ["EVID-TESTS-INTEROPERABILITE", "P-INT-23", "P-INT-24", "P-INT-25"]
tags: ["cnisn", "compliance", "homologation", "interoperabilite"]
---
# Homologation d'interopérabilité

## Finalité

Permettre de vérifier objectivement qu'un système respecte les contrats et profils applicables.

## Contrôles attendus

- validation des contrats ;
- tests automatisés ;
- tests de sécurité ;
- tests de compatibilité ;
- tests de performance ;
- jeux de données de référence ;
- publication des résultats ;
- déclaration de conformité ;
- gestion des dérogations ;
- suivi de remédiation.

## Principes associés

- [P-INT-19: Neutralité technologique](../../02_architecture-elements/motivation/principles/p-int-19.md)
- [P-INT-20: Portabilité et réversibilité](../../02_architecture-elements/motivation/principles/p-int-20.md)
- [P-INT-21: Progressivité](../../02_architecture-elements/motivation/principles/p-int-21.md)
- [P-INT-22: Fonctionnement en connectivité contrainte](../../02_architecture-elements/motivation/principles/p-int-22.md)
- [P-INT-23: Conformité fondée sur des preuves](../../02_architecture-elements/motivation/principles/p-int-23.md)
- [P-INT-24: Applicabilité déclarée](../../02_architecture-elements/motivation/principles/p-int-24.md)
- [P-INT-25: Réévaluation continue](../../02_architecture-elements/motivation/principles/p-int-25.md)

## Réponse nationale

La conformité ne se traduit pas par un service exposé mais par un processus d'homologation : cadre CNISN Partie IV, fondation F.4 et dispositif CNASN. Les tests associés sont portés par les profils et outils PTISN.
