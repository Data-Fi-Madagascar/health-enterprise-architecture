---
title: "ADR-0011 : Séparation du service d'éligibilité et de couverture"
id: adr-0011
domain: 06_decisions
version: "1.0.0"
status: candidate
date: 2026-09-24
owner: DEPSI
tags: ["adr", "eligibilite", "couverture", "protection-financiere"]
related: ["ABB-ELIGIBILITE-COUVERTURE", "CAP-07", "ART-4C", "ART-9", "WP-03"]
---

# ADR-0011 : Séparation du service d'éligibilité et de couverture

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle.

- **Statut** : proposé
- **Date** : 2026-09-24
- **Groupe concerné** : DEPSI, CNASN et programmes de protection financière

## Contexte

La vérification des droits à une couverture sanitaire exige une décision dépendant de la prestation, du programme et de la date. Un registre de professionnels résout une qualité professionnelle, tandis qu'un service de consentement établit une base d'autorisation d'accès. Ces responsabilités ne déterminent pas les droits financiers du bénéficiaire. Leur confusion rendrait la décision d'éligibilité difficile à expliquer et à auditer.

## Décision

Instituer [ABB-ELIGIBILITE-COUVERTURE](../../04_architecture-repository/05_building-blocks/abb/abb-eligibilite-couverture.md) comme bloc applicatif distinct pour la consultation de couverture, la vérification des droits, la décision temporelle, sa preuve et son audit. Le bloc reçoit l'identité résolue et l'autorisation nécessaire, mais ne réalise ni la résolution d'identité ni la gestion du consentement. Les échanges de couverture et d'éligibilité utilisent HL7 FHIR R4. Cette décision ne sélectionne aucun produit ni fournisseur.

## Justification

La séparation traduit [CAP-07](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-07.md) dans la [partition VS-03](../../04_architecture-repository/01_partitions/value-streams/part-vs-03.md) et rend explicite le périmètre de [ART-4C](../../04_architecture-repository/04_patterns/artsn-rules/art-4c.md) et [ART-9](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md). Une preuve horodatée, associée aux règles et à la période de validité, permet de reconstituer le droit applicable au moment de la prestation. FHIR R4 fournit le cadre d'échange commun aux données de couverture et aux demandes et réponses de vérification.

La recherche collaborative HEAL éclaire la validation des règles avec les programmes de terrain. La structure HEAF distingue ce bloc des services d'identité et d'autorisation ; le catalogue HEART favorise la réutilisation du contrat FHIR R4 et la production de métadonnées depuis la source de vérité.

## Conséquences

### Positives

- Les services cliniques et financiers disposent d'une décision de droits traçable dans le temps.
- Les responsabilités d'identité, d'autorisation et de couverture deviennent vérifiables séparément.
- Les échanges de couverture et d'éligibilité restent interopérables sans dépendance envers un produit.

### Négatives

- Les équipes doivent gouverner les règles de droits, les sources de couverture et leurs périodes de validité.
- Les intégrations doivent conserver les preuves et corréler leurs journaux d'audit avec les décisions rendues.

## Alternatives considérées

| Alternative | Raison du refus |
|-------------|-----------------|
| Intégrer l'éligibilité au registre d'identité | L'identité d'une personne n'établit pas ses droits financiers à une date donnée. |
| Intégrer l'éligibilité au service de consentement | Une base d'autorisation d'accès ne détermine pas la couverture d'une prestation. |
| Choisir immédiatement un produit de registre | Le choix d'implémentation précéderait la définition et la validation de l'interface nationale. |

## Références

- [ABB-ELIGIBILITE-COUVERTURE](../../04_architecture-repository/05_building-blocks/abb/abb-eligibilite-couverture.md)
- [CMP-12 : Registre d'éligibilité et de couverture](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-12.md)
- [WP-03 : Médiation et registres partagés](../../04_architecture-repository/07_migration/work-packages/wp-03.md)
- ADR-0003 : Utilisation de HL7 FHIR comme standard d'interopérabilité
