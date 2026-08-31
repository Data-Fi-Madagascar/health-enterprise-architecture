---
title: "STD-0008 : Norme d'échange des réclamations et paiements (protection financière)"
id: std-0008
domain: 05_standards
version: "1.0.0"
status: active
last_reviewed: 2026-08-27
owner: Comité National d'Architecture Santé Numérique
tags: ["standards", "interoperabilite", "protection-financiere", "claims", "obligatoire"]
related: ["Lot L4", "PT-18", "PT-07"]
---

# STD-0008 : Norme d'échange des réclamations et paiements (protection financière)

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

- **Type** : norme (obligatoire)
- **Statut** : approuvé
- **ADR de référence** : ADR-0001, ADR-0003
- **Date d'entrée en vigueur** : 2026-08-27

## Contexte

La protection financière (VS-03) exige un échange fiable entre les prestataires de soins, les payeurs (assurance maladie, mutuelles, État) et les bénéficiaires pour les **réclamations de soins**, l'**éligibilité à la couverture** et les **paiements**. Les systèmes existants fragmentent ces flux (formulaires papier, portails propriétaires, formats CSV), ce qui retarde les remboursements et affaiblit la couverture santé universelle.

Le modèle de l'échange de réclamations (claims exchange / HCX) — illustré par le Nigeria NDHI Health Claims Exchange et l'approche Open Health Care eXchange (HCX) — propose un bus d'échange neutre où prestataire et payeur s'interrogent via des ressources FHIR standardisées.

## Énoncé

Toute solution numérique échangeant des réclamations, de l'éligibilité ou des paiements dans le secteur santé de Madagascar **doit** :

1. **Utiliser HL7 FHIR R4** pour les ressources `CoverageEligibilityRequest`, `CoverageEligibilityResponse`, `Claim`, `ClaimResponse` et `PaymentNotice` (profilées selon l'ARTSN) ;
2. **Transmettre les flux via l'échange interinstitutionnel X-Road** (STD-0003, ADR-0001) en mode asynchrone ;
3. **Identifier le bénéficiaire** selon la norme PIXm/PDQm (STD-0005) et le prestataire selon CAP-INT-02 ;
4. **Coder les actes et diagnostics** selon les terminologies nationales (STD-0006, STD-0007) ;
5. **Garantir la traçabilité financière** (imputation, statut de paiement) via `ClaimResponse` et `PaymentNotice` signés.

## Champ d'application

Cette norme s'applique à :

- Toutes les solutions de facturation et de remboursement des prestataires ;
- Tous les payeurs (CNAM, mutuelles, programmes d'État, partenaires) ;
- Tous les profils PTISN d'échange financier ;
- Toutes les solutions soumises à homologation dans le domaine de la protection financière.

## Références au cadre

- **Principes** : PA-05 (Interopérabilité comme exigence), PA-02 (Neutralité technologique)
- **CNISN** : CAP-07 (Protection financière, couverture santé universelle)
- **ARTSN** : ART-2 (Médiation et normalisation), ART-9 (Garanties transactionnelles fortes)
- **ARTSN — lots consommateurs** : [L4 — Analytique & pilotage](../../02_artsn/07_lots/index.md)
- **PTISN** : [PT-18: Échange de réclamations et paiements](../../03_ptisn/03_profils/pt-18-echange-reclamations-paiements.md), [PT-07: Terminologie et codification](../../03_ptisn/03_profils/pt-07-terminologie-codification.md)
- **Standards internationaux** : HL7 FHIR R4, Nigeria NDHI HCX, Open Health Care eXchange (HCX)

## Contrôle et conformité

Lors de l'homologation, le Comité National vérifiera :

| Critère | Vérification |
|---------|--------------|
| Format d'échange | Réclamations en FHIR R4 (`Claim`/`ClaimResponse`) |
| Transport | Flux véhiculés par X-Road (STD-0003) |
| Identification | Bénéficiaire (STD-0005) et prestataire (CAP-INT-02) résolus |
| Terminologie | Actes/diagnostics codés (STD-0006 / STD-0007) |
| Traçabilité | `PaymentNotice` signé et statut de paiement exposé |

## Dérogations

Les dérogations sont possibles pour les payeurs legacy en phase de migration (batch CSV via médiation obligatoire). Toute dérogation doit être justifiée et approuvée par le Comité National.

## Références

- Normes et standards
- ADR-0001 : Échange interinstitutionnel X-Road
- ADR-0003 : Utilisation de HL7 FHIR
- ARTSN : ART-2 (Médiation), ART-9 (Garanties transactionnelles)
- CNISN : CAP-07 (Protection financière)

- **matrice de lecture** : Matrice de lecture du CNISN (niveau 2) (`01_cnisn/reading-matrix.md`)
