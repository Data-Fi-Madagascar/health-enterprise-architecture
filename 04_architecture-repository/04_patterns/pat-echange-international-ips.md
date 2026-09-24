---
domain: 04_patterns
id: PAT-ECHANGE-INTERNATIONAL-IPS
type: architecture-pattern
niveau: "2"
title: Pattern d'échange international IPS
status: candidate
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-13
envelope: 01_cnisn/02_capacites/index.md
togaf_repository_section: reference-library
togaf_adm_phase: C
architecture_level: extended-enterprise
architecture_domain: application
architecture_scope: interoperability
architecture_state: target
maps_to: ["CAP-15", "CAP-18"]
implements: ["ART-0", "ART-1", "ART-7"]
related: ["PART-ECHANGE-TRANSFRONTALIER", "DO-29", "DO-30", "DO-31"]
tags: ["cnisn", "pattern", "transfrontalier", "ips", "gdhcn"]
---
# Pattern d'échange international IPS

## Finalité

Encadrer les échanges de données et de services de santé au-delà des frontières nationales tout en garantissant la confiance mutuelle, la souveraineté des données et la conformité aux cadres internationaux.

## Mécanismes attendus

### Gouvernance des échanges transfrontaliers

- identification des flux autorisés vers ou depuis l'international ;
- définition des données échangeables et des données souveraines ;
- enregistrement des accords de confiance mutuelle ;
- gestion des autorisations d'accès pour les acteurs internationaux ;
- arbitrage des conflits de juridiction.

### Confiance mutuelle et certification

- adhésion et conformité au GDHCN (Global Digital Health Certification Network) ;
- gestion des certificats de confiance mutuelle ;
- vérification de la conformité des systèmes partenaires étrangers ;
- publication de la politique de confiance nationale ;
- révocation en cas d'incident.

### Échange de résumé patient

- production et réception de résumés internationaux du patient (HL7 FHIR IPS) ;
- mapping des données nationales vers les sections IPS ;
- validation de conformité des IPS émis et reçus ;
- minimisation stricte des sections incluses ;
- conservation des IPS échangés selon la politique de rétention nationale.

## Rattachement

- [Partition échange transfrontalier](../01_partitions/externes/part-echange-transfrontalier.md)
- [ART-7: Sécurité, contrôle d'accès et résidence de la donnée](artsn-rules/art-7.md)
