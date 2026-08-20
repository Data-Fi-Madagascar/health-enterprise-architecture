---
id: CAP-INT-13
type: capacite
niveau: "2"
title: Interopérabilité transfrontalière et confiance internationale
status: active
owner: DEPSI
version: "0.5"
family: transfrontalier
source: 01_cnisn/02_capacites/index.md
maps_to: ["P-INT-01", "P-INT-05", "P-INT-10", "P-INT-14", "P-INT-16", "P-INT-17", "P-INT-19", "CAP-15"]
implements: []
applies_to: []
related: ["CAP-INT-03", "CAP-INT-08", "CAP-INT-09"]
tags: ["cnisn", "niveau-2", "capacite", "transfrontalier", "gdhcn", "ips"]
---

# Interopérabilité transfrontalière et confiance internationale

### Finalité

Permettre les échanges de données et de services de santé au-delà des frontières nationales tout en garantissant la confiance mutuelle, la souveraineté des données et la conformité aux cadres internationaux.

### Contexte

Madagascar est membre de l'Union Africaine (UA), de la Commission Économique des Nations Unies pour l'Afrique (CEUA) et candidat à l'adhésion à la Communauté de Développement de l'Afrique Australe (SADC) et à l'Organisation Internationale de la Francophonie (OIF). Les flux de données de santé transfrontaliers concernent notamment :

- la surveillance épidémique régionale (OMS AFRO, CDC Africa) ;
- les déplacements de patients entre pays de la SADC ;
- les programmes de santé multilatéraux (OMS, UNICEF, Gavi) ;
- la recherche clinique internationale ;
- les échanges d'actes médicaux pour patients transfrontaliers ;
- la logistique pharmaceutique transfrontalière.

### Services attendus

#### Gouvernance des échanges transfrontaliers

- identification des flux autorisés vers/lors de l'international ;
- définition des données échangeables vs. les données souveraines ;
- enregistrement des accords de confiance mutuelle ;
- gestion des autorisations d'accès pour les acteurs internationaux ;
- arbitrage des conflits de juridiction.

#### Confiance mutuelle et certification

- adhésion et conformité au GDHCN (Global Digital Health Certification Network) ;
- gestion des certificats de confiance mutuelle ;
- vérification de la conformité des systèmes partenaires étrangers ;
- publication de la politique de confiance nationale ;
- révocation en cas d'incident.

#### Identification transfrontalière

- résolution d'identité pour patients étrangers sur le territoire national ;
- mapping des identifiants nationaux vers les standards internationaux (OID, HL7) ;
- gestion des identifiants temporaires pour patients de passage ;
- prévention des confusions d'identité transfrontalières.

#### Consentement et autorisation pour échanges internationaux

- gestion du consentement spécifique aux échanges internationaux ;
- vérification de la base légale pour chaque flux sortant ;
- minimisation stricte des données exportées ;
- pseudonymisation pour les flux de recherche.

#### Résidence et souveraineté

- contrôle de sortie des données sensibles ;
- journalisation de tous les flux transfrontaliers ;
- audit des accès internationaux ;
- alertes en cas d'export non autorisé ;
- rapport périodique aux autorités compétentes.

#### Échange de résumé patient (IPS)

- production et réception de résumés internationaux du patient (HL7 FHIR IPS) ;
- mapping des données nationales vers les sections IPS (allergies, médicaments, problèmes, identité) ;
- validation de conformité des IPS émis et reçus ;
- minimisation stricte : seules les sections nécessaires à la finalité clinique sont incluses ;
- conservation des IPS échangés selon la politique de rétention nationale.

### Exigences de conformité

| Exigence | Description |
|----------|-------------|
| **EXG-TF-01** | Tout flux transfrontalier doit être couvert par un accord explicite (P-INT-10) |
| **EXG-TF-02** | Le consentement du patient doit être obtenu pour tout échange sortant sauf obligation légale |
| **EXG-TF-03** | Seules les données minimisées nécessaires à la finalité peuvent être exportées |
| **EXG-TF-04** | Tous les flux transfrontaliers doivent être journalisés et auditable |
| **EXG-TF-05** | Le GDHCN doit être le référentiel de confiance pour les échanges internationaux |
| **EXG-TF-06** | Les données souveraines (identité nationale complète, données génomiques) ne quittent pas le territoire sauf dérogation |
| **EXG-TF-07** | Les systèmes partenaires étrangers doivent démontrer leur conformité avant tout accès |
| **EXG-TF-08** | Tout résumé patient échangé (IPS) doit être conforme au profil HL7 FHIR IPS et contenir au minimum les sections ALGY, MDCA, PROB, IDOI |

### Principes associés

- **P-INT-01** (Autorité désignée) : l'autorité nationale reste l'autorité pour les données malgaches, même lors d'échanges ;
- **P-INT-05** (Contrat explicite) : tout flux transfrontalier nécessite un accord bilatéral ou multilatéral ;
- **P-INT-10** (Accord préalable) : accord obligatoire avant tout échange avec une institution étrangère ;
- **P-INT-14** (Base d'autorisation explicite) : base légale documentée pour chaque type de flux sortant ;
- **P-INT-16** (Résidence) : les contraintes de résidence s'appliquent aux flux transfrontaliers ;
- **P-INT-17** (Minimisation) : minimisation renforcée pour les échanges internationaux ;
- **P-INT-19** (Neutralité technologique) : le GDHCN est un cadre de confiance, pas un produit.

### Rattachement

- [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../../referentiel/capabilites/cap-15.md) (Sécurité, contrôle d'accès et résidence)
- [CAP-18: Coordination intersectorielle (One Health)](../../referentiel/capabilites/cap-18.md) (Coordination intersectorielle — One Health)
- [ART-7](../../referentiel/chapitres/art-7.md) (Sécurité, contrôle d'accès et résidence)
- [ART-0](../../referentiel/chapitres/art-0.md) (Accords de partage inter-institutionnels)
- [PT-14](../../03_ptisn/03_profils/pt-14-interopabilite-transfrontaliere.md) (Profil technique transfrontalier — IPS)
