---

title: "ADR-0004 : Adoption des profils IHE PIXm/PDQm pour la résolution d'identité"
id: adr-0004
domain: 06_decisions
version: "1.0.0"
status: accepté
date: 2026-07-01
owner: DEPSI
tags: ["adr", "identité", "pixm", "pdqm", "ihe"]
---

# ADR-0004 : Adoption des profils IHE PIXm/PDQm pour la résolution d'identité

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ○ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ○ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

- **Statut** : accepté
- **Date** : 2026-07-01
- **Groupe concerné** : DEPSI, développeurs, intégrateurs

## Contexte

La résolution d'identité du bénéficiaire est une capabilité fondamentale pour la continuité des soins, la protection financière et l'interopérabilité des systèmes. Elle comprend la recherche démographique, la gestion des identifiants et le rapprochement de dossiers.

Le PT-04 définit les profils IHE PIXm (Patient Identifier Cross-referencing for mobile) et PDQm (Patient Demographics Query for mobile) comme profils cibles pour les nouveaux services.

## Décision

Adopter les **profils IHE PIXm et PDQm** comme standard national pour la résolution d'identité du bénéficiaire, en complément du modèle HL7 FHIR Patient.

## Justification

PIXm et PDQm répondent aux exigences du CNISN et de l'ARTSN :

- **CAP-INT-01** : Résolution d'identité du bénéficiaire
- **ART-4** : Référentiels nationaux
- **ART-4a** : Résolution d'identité
- **ART-4b** : Bases d'autorisation

PIXm fournit des transactions REST pour gérer et rechercher les identifiants d'un patient entre domaines. PDQm définit une interface REST légère pour la recherche de patients à partir de données démographiques.

## Conséquences

### Positives
- Standard international reconnu par l'IHE
- API REST moderne et légère
- Compatibilité avec les systèmes HL7 FHIR
- Séparation claire entre identité fondationnelle et fonctionnelle

### Négatives
- Nécessite la définition de seuils de rapprochement nationaux
- Stratégie de golden record à définir
- Procédures de fusion et contrôle humain à développer
- Lien juridique avec la CNIE à clarifier

## Alternatives considérées

| Alternative | Raison du refus |
|-------------|-----------------|
| PIX/PDQ historiques (HL7 v2) | Moins adapté aux environnements mobiles |
| Résolution propriétaire | Pas d'interopérabilité, dépendance éditeur |
| OpenHIE Client Registry | Moins de traction internationale |

## Références

- PT-04 : Profil technique national
- ARTSN : Chapitre ART-4
- ARTSN : Fondation F.1

- **matrice de lecture** : Matrice de lecture du CNISN (niveau 2) (`01_cnisn/reading-matrix.md`)
