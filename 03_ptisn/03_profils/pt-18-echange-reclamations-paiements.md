---
title: Échange de réclamations et paiements
id: ptisn-PT-18
domain: 03_profils
version: "1.0.0"
status: draft
last_reviewed: 2026-08-27
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "profils", "PT-18"]
related: ["CAP-INT-07", "ART-2", "ART-9"]
---

# Échange de réclamations et paiements

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

## 1. Objet et périmètre

Le **profil PT-18 — Échange de réclamations et paiements** définit le bus d’échange de réclamations entre prestataires et payeurs, dans le cadre de la protection financière et de la couverture santé universelle.

Périmètre : vérification d’éligibilité, soumission de réclamation, adjudication et notification de paiement. Norme de référence : [STD-0008: échange des réclamations et paiements](../../01_cnisn/05_standards/std-0008-echange-reclamations-paiements.md).

## 2. Capacité CNISN

[CAP-07: Protection financière, couverture santé universelle](../../referentiel/capabilites/cap-07.md)

## 3. Chapitres ART applicables

- [ART-2: médiation et normalisation](../../referentiel/chapitres/art-2.md)
- [ART-9: garanties transactionnelles fortes](../../referentiel/chapitres/art-9.md)
- [STD-0008: échange des réclamations et paiements](../../01_cnisn/05_standards/std-0008-echange-reclamations-paiements.md)

## 4. Acteurs (Actors)

- **Prestataire (Provider)** — système du prestataire soumettant l’éligibilité et la réclamation.
- **Payeur (Payer)** — système du payeur répondant à l’éligibilité, adjudiquant et notifiant le paiement.
- **Bus d’échange de réclamations (Claims Exchange Hub)** — achemine et assure l’intégrité des flux entre prestataire et payeur.

*Référence — capacité CNISN mise en œuvre : [CAP-INT-02](../../referentiel/capacites/cap-int-02.md).
## 5. Transactions

| Transaction | Acteurs | R/O | Standard |
|----|----|----|----|
| T1 — Vérification d’éligibilité | Prestataire → Payeur (via Bus) | R | FHIR `CoverageEligibilityRequest` / `CoverageEligibilityResponse` (R4) |
| T2 — Soumission de réclamation | Prestataire → Payeur (via Bus) | R | FHIR `Claim` (R4) |
| T3 — Adjudication | Payeur → Prestataire (via Bus) | R | FHIR `ClaimResponse` (R4) |
| T4 — Notification de paiement | Payeur → Prestataire (via Bus) | R | FHIR `PaymentNotice` signé (R4) |

R = requis ; O = optionnel (à définir si le dépôt ne précise pas).

*Référence — capacité CNISN mise en œuvre : [CAP-INT-02](../../referentiel/capacites/cap-int-02.md).
## 6. Content Modules

- **FHIR `CoverageEligibilityRequest` / `Response`** : éligibilité et couverture (résolution du bénéficiaire STD-0005, du prestataire CAP-INT-02).
- **FHIR `Claim` / `ClaimResponse`** : réclamation et adjudication.
- **FHIR `PaymentNotice`** : notification de paiement signée et traçable.

## 7. Options

- **O1 — Modèle de bus** : HCX (Inde) ou Nigeria NDHI comme référence d’implémentation.
- **O2 — Transport** : X-Road (STD-0003, ADR-0001).
- **O3 — Terminologie** : CIM-11 + LOINC (STD-0006), SNOMED CT (STD-0007).

## 8. Service national

Un bus d’échange de réclamations (modèle HCX / Nigeria NDHI) est requis entre prestataires et payeurs.

### Éligibilité et couverture

- vérification de la couverture via `CoverageEligibilityRequest` / `CoverageEligibilityResponse` ;
- résolution du bénéficiaire (STD-0005) et du prestataire (CAP-INT-02).

### Réclamation et paiement

- soumission de `Claim` par le prestataire ;
- adjudication et retour `ClaimResponse` par le payeur ;
- notification de paiement `PaymentNotice` signée et traçable.

## 9. Formats et standards recommandés

| Type d'échange | Format recommandé |
|----------------|-------------------|
| Éligibilité | HL7 FHIR `CoverageEligibilityRequest/Response` (R4) |
| Réclamation | HL7 FHIR `Claim` / `ClaimResponse` (R4) |
| Paiement | HL7 FHIR `PaymentNotice` (R4) |
| Transport | X-Road (STD-0003, ADR-0001) |
| Terminologie | CIM-11 + LOINC (STD-0006), SNOMED CT (STD-0007) |

*Référence — normes et standards CNISN : [01_cnisn/05_standards](../../01_cnisn/05_standards/index.md).
## 10. Exigences

Aucun produit national n’est encore retenu (**statut : à instruire**). Le bus d’échange doit assurer l’intégrité et la non-répudiation des flux (ART-9) et le transport via X-Road.

## 11. Déclaration de conformité (Integration Statement)

- ressources FHIR profilées publiées ;
- flux véhiculé par X-Road ;
- `PaymentNotice` signé et statut de paiement exposé ;
- traçabilité de l’adjudication.

## 12. Articulation avec les autres profils

- [PT-04: résolution d’identité bénéficiaire](../../referentiel/profils/pt-04.md)
- [PT-05: registre des professionnels](../../referentiel/profils/pt-05.md)
- [PT-02: médiation intra-secteur](../../referentiel/profils/pt-02.md)
- [PT-10: confiance, authentification, autorisation](../../referentiel/profils/pt-10.md)

## 13. Limites et dépendances

Produit national à instruire. Dépendance : X-Road (transport), terminologie (PT-07), résolution bénéficiaire/prestataire (PT-04/PT-05), et norme STD-0008.

<!-- END:GENERATED -->

## Références au cadre

- **ARTSN — lots consommateurs** : [L1 — Infrastructure & sécurité](../../02_artsn/07_lots/index.md), [L2 — Applications terrain](../../02_artsn/07_lots/index.md), [L3 — Médiation & registres](../../02_artsn/07_lots/index.md), [L4 — Analytique & pilotage](../../02_artsn/07_lots/index.md)
