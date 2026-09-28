---
title: "ADR-0012 : Rattachement One Health à la surveillance et au pilotage"
id: adr-0012
domain: 06_decisions
version: "1.0.0"
status: candidate
date: 2026-09-24
owner: DEPSI
tags: ["adr", "one-health", "surveillance", "pilotage", "gouvernance"]
related: ["PART-ONE-HEALTH", "VS-02", "VS-04", "CAP-08", "CAP-18", "CMP-02", "ABB-ECHANGE-MEDIATION", "ABB-EXPOSITION-DONNEES-ANALYTIQUES", "PT-15", "WP-07"]
---

# ADR-0012 : Rattachement One Health à la surveillance et au pilotage

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle.

- **Statut** : proposé
- **Date** : 2026-09-24
- **Groupe concerné** : DEPSI, CNASN et institutions de santé humaine, animale et environnementale

## Contexte

La partition One Health organise les échanges entre santé humaine, santé animale et environnement. Elle déclare deux responsabilités complémentaires : la surveillance et la riposte coordonnées dans VS-02, ainsi que la coordination institutionnelle, le pilotage et la redevabilité dans VS-04. Son rattachement initial à CAP-18 seul ne permettait pas de dériver la seconde chaîne : le flux VS-04 restait sans capabilité ni processus explicites dans la vue de traçabilité.

Le centre de commande CMP-02 consomme les alertes et les indicateurs pour soutenir les décisions intersectorielles. Sa responsabilité de pilotage implique CAP-08, qui porte la gouvernance institutionnelle, la planification, la coordination et la redevabilité. La surveillance portée par CAP-18 reste nécessaire pour détecter les menaces et coordonner la riposte.

## Décision

Conserver le rattachement de [PART-ONE-HEALTH](../../04_architecture-repository/01_partitions/sectorielles/part-one-health.md) à [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md) et à [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md), avec [CAP-18](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-18.md) pour la surveillance et la riposte, et [CAP-08](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-08.md) pour la gouvernance intersectorielle, le pilotage et la redevabilité. La création d'un nouveau flux de valeur One Health est explicitement rejetée.

Les deux chaînes réutilisent [ABB-ECHANGE-MEDIATION](../../04_architecture-repository/05_building-blocks/abb/abb-echange-mediation.md) et [ABB-EXPOSITION-DONNEES-ANALYTIQUES](../../04_architecture-repository/05_building-blocks/abb/abb-exposition-donnees-analytiques.md), rattachés à la partition One Health en complément de leurs partitions transverses existantes. [PT-15](../../04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-15.md) matérialise ces blocs avec les composants CMP-02, CMP-04 et CMP-06. [WP-07](../../04_architecture-repository/07_migration/work-packages/wp-07.md) réalise les deux capabilités, les deux ABB et le déploiement du profil.

## Justification

VS-02 produit la valeur attendue de détection et de réponse aux menaces sanitaires ; VS-04 assure la coordination des autorités, le suivi des décisions et le rendu de comptes. Le maintien de VS-04 traduit la responsabilité institutionnelle du [centre de commande CMP-02](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-02.md), qui doit disposer d'indicateurs gouvernés et d'un cadre de décision partagé. CAP-08 fournit cette responsabilité de gouvernance ; CAP-18 porte son articulation entre secteurs pour la surveillance et la riposte.

Les échanges contrôlés et l'exposition analytique constituent des moyens réutilisables par plusieurs partitions. Leur rattachement à One Health ne modifie pas leur portée transverse. Les autorités de données demeurent distinctes et les accords de partage encadrent l'accès aux informations nécessaires au pilotage.

La démarche collaborative HEAL soutient l'analyse des besoins avec les institutions de terrain. Le HEAF rattache la partition sectorielle aux valeurs et capabilités nationales existantes. Le HEART impose la réutilisation des blocs et du profil, avec des relations structurées qui permettent de générer la vue de traçabilité depuis la source de vérité.

## Conséquences

### Positives

- La vue dérivée présente deux chaînes complètes vers les capabilités et processus de surveillance et de pilotage.
- Le rôle institutionnel du centre de commande, la coordination et la redevabilité sont explicites.
- Le profil et le lot de migration réutilisent les mêmes blocs d'échange et d'exposition analytique que les partitions transverses.

### Négatives

- Les institutions doivent préciser les responsabilités de décision, les indicateurs de pilotage et les accords de partage.
- Les évolutions du modèle doivent préserver une capabilité commune pour chaque flux déclaré, sous contrôle du validateur de référentiel.

## Alternatives considérées

| Alternative | Raison du refus |
|-------------|-----------------|
| Retirer VS-04 de la partition | Le pilotage par CMP-02, la gouvernance intersectorielle et la redevabilité resteraient sans rattachement explicite. |
| Créer un nouveau flux de valeur One Health | La surveillance et le pilotage sont déjà couverts par VS-02 et VS-04 ; un nouveau flux dupliquerait leurs responsabilités. |
| Conserver CAP-18 comme seule capabilité | CAP-18 ne couvre pas la gouvernance institutionnelle portée par CAP-08 dans VS-04. |
| Créer des ABB spécifiques One Health | Les blocs d'échange et d'exposition analytique existants répondent aux besoins et doivent rester réutilisables. |

## Références

- [PART-ONE-HEALTH : Partition One Health](../../04_architecture-repository/01_partitions/sectorielles/part-one-health.md)
- [VS-02 : Surveillance et réponse aux menaces sanitaires](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md)
- [VS-04 : Pilotage, coordination et amélioration de la performance](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)
- [CAP-08 : Gouvernance institutionnelle, planification, coordination et redevabilité](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-08.md)
- [CAP-18 : Coordination intersectorielle One Health](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-18.md)
- [PT-15 : Surveillance One Health](../../04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-15.md)
- [WP-07 : Coordination One Health](../../04_architecture-repository/07_migration/work-packages/wp-07.md)
