---
domain: abb
id: ABB-CATALOGUE-CONTRATS
type: architecture-building-block
niveau: "2"
title: Catalogue des services et registre des contrats
status: candidate
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-06
envelope: 01_cnisn/02_capacites/index.md
building_block_role: ABB
building_block_domain: application
togaf_repository_section: reference-library
togaf_adm_phase: C
architecture_level: enterprise-transversal
architecture_domain: application
architecture_scope: interoperability
architecture_state: target
partitions: ["PART-TRANSVERSE-INTEROPERABILITE"]
maps_to: ["CAP-12", "CAP-14", "CAP-16"]
implements: ["ART-1", "ART-2", "F-3", "F-4"]
related: ["AC-CATALOGUE-SERVICES", "PART-TRANSVERSE-INTEROPERABILITE", "P-INT-05", "P-INT-06", "P-INT-07", "P-INT-08", "P-INT-09", "P-INT-23", "P-INT-24", "P-INT-25"]
tags: ["cnisn", "abb", "catalogue", "contrats"]
---
# Catalogue des services et registre des contrats

## Finalité

Rendre visibles, gouvernables et réutilisables les services et interfaces du secteur.

## Services attendus

### Catalogue des services

- enregistrement des services ;
- publication des propriétaires ;
- publication des consommateurs ;
- publication des niveaux de service ;
- publication des conditions d'accès ;
- publication du statut.

### Registre des contrats

- publication des interfaces ;
- publication des événements ;
- publication des schémas ;
- versionnement ;
- compatibilité ;
- dépréciation ;
- gestion des extensions nationales.

## Principes associés

- [P-INT-05: Contrat explicite](../../02_architecture-elements/motivation/principles/p-int-05.md)
- [P-INT-06: Versionnement et compatibilité](../../02_architecture-elements/motivation/principles/p-int-06.md)
- [P-INT-07: Responsabilité de la donnée](../../02_architecture-elements/motivation/principles/p-int-07.md)
- [P-INT-08: Publication au catalogue des services](../../02_architecture-elements/motivation/principles/p-int-08.md)
- [P-INT-09: Publication des contrats](../../02_architecture-elements/motivation/principles/p-int-09.md)
- [P-INT-23: Conformité fondée sur des preuves](../../02_architecture-elements/motivation/principles/p-int-23.md)
- [P-INT-24: Applicabilité déclarée](../../02_architecture-elements/motivation/principles/p-int-24.md)
- [P-INT-25: Réévaluation continue](../../02_architecture-elements/motivation/principles/p-int-25.md)

## Rattachement

- [Contrat d'architecture du catalogue de services](../../06_governance/architecture-contracts/ac-catalogue-services.md)
- [Partition transverse - Interopérabilité](../../01_partitions/transverses/part-transverse-interoperabilite.md)
