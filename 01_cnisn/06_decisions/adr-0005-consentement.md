---

title: "ADR-0005 : Adoption de FHIR Consent pour le consentement structuré"
id: adr-0005
domain: 06_decisions
version: "1.0.0"
status: candidate
date: 2026-08-13
owner: DEPSI
tags: ["adr", "consentement", "fhir", "souveraineté", "données"]
related: ["Lot L5", "PT-10", "PT-11"]
---

# ADR-0005 : Adoption de FHIR Consent pour le consentement structuré

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle.

- **Statut** : proposé
- **Date** : 2026-08-13
- **Groupe concerné** : DEPSI, directions juridiques, CNASN

## Contexte

Le consentement du patient est un pilier fondamental de la souveraineté des données de santé. La loi 2014-038 sur la protection des données personnelles impose un consentement éclairé, spécifique et révocable pour tout traitement de données de santé.

Actuellement, le consentement est géré de manière informelle (formulaire papier, accord verbal) sans structure numérique exploitable. Ceci pose plusieurs problèmes :
- Pas de traçabilité des consentements accordés ou refusés
- Pas de mécanisme de révocation en temps réel
- Impossibilité de vérifier le consentement avant un échange de données
- Non-conformité aux standards internationaux (HL7, GDPR-like)

## Décision

Adopter **HL7 FHIR Consent** comme standard national pour la gestion structurée du consentement patient, en complément du RBAC défini dans PT-10.

## Justification

FHIR Consent répond aux exigences du cadre :

- **CAP-INT-09** : Gestion du consentement et des autorisations
- **ART-4B** : Bases d'autorisation
- **ART-7** : Sécurité, contrôle d'accès et résidence des données
- **PT-11** : Profil technique consentement
- **Loi 2014-038** : Protection des données personnelles

Le modèle FHIR Consent permet :
- De structurer le consentement par type de donnée, de finalité et de destinataire
- De gérer les cycles de vie (accord, refus, révocation, expiration)
- De vérifier automatiquement le consentement avant chaque accès
- D'interoperer avec les systèmes régionaux et internationaux

## Conséquences

### Positives
- Conformité juridique renforcée (Loi 2014-038)
- Traçabilité complète des consentements
- Vérification automatique avant échange de données
- Interopérabilité avec les standards internationaux
- Contrôle patient renforcé sur ses données

### Négatives
- Nécessite la formation des personnels soignants
- Complexité d'implémentation pour les systèmes legacy
- Nécessite un mécanisme d'urgence vitale (dérogation au consentement)
- Coût de développement du module consentement

## Alternatives considérées

| Alternative | Raison du refus |
|-------------|-----------------|
| Consentement papier uniquement | Pas de traçabilité numérique, non vérifiable |
| Consentement propriétaire (JSON maison) | Pas d'interopérabilité, dépendance éditeur |
| Consentement basé sur les seuls rôles RBAC | Insuffisant : ne couvre pas le consentement patient |
| GDPR Consent (UE) | Trop strict pour le contexte malgache, inadapté |

## Références
- **ARTSN — lots consommateurs** : [L5 — Extension & pérennisation](../../02_artsn/07_lots/index.md)

- PT-11 : Consentement
- ART-4B : Bases d'autorisation
- ART-7 : Sécurité
- [Loi 2014-038 : Protection des données personnelles](https://www.lexpress.mg)

