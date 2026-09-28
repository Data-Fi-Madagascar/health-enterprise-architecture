---
title: "P2 — Éligibilité et traçabilité One Health"
status: approved
date: 2026-09-24
owner: DEPSI
---

# P2 — Éligibilité et traçabilité One Health

## 1. Objet

Ce lot ferme les deux ambiguïtés laissées visibles par la vue TOGAF de traçabilité par partition :

1. le registre d'éligibilité CMP-12 ne possède pas d'ABB cible ni de profil PTISN propre ;
2. la partition One Health déclare VS-04 sans capacité commune, ce qui produit une chaîne incomplète.

Le dépôt `04_architecture-repository` reste la source canonique. Les documents CAESN, ARTSN, PTISN, les matrices, les schémas et le portail Mintlify sont des artefacts dérivés ou des enveloppes publiées.

## 2. Décisions d'architecture

### 2.1 Éligibilité et couverture

Le modèle cible sépare explicitement l'éligibilité de l'identité, du consentement et du registre des professionnels.

Un nouvel objet `ABB-ELIGIBILITE-COUVERTURE` représente le service national partagé qui maintient les droits ouverts, leur période de validité et les règles de couverture. Il réalise `CAP-07`, met en œuvre `ART-4C` et `ART-9`, appartient à `PART-VS-03` et accède à `DO-14`, `DO-15`, `DO-16` et `DO-17`.

Le profil `PT-20 — Éligibilité et couverture`, initialement `candidate`, définit l'interface implémentable de cet ABB. Son périmètre fonctionnel comprend :

- la consultation d'une couverture ;
- la demande de vérification des droits ;
- la réponse d'éligibilité avec période, prestations et restrictions ;
- la consultation du régime ou produit de couverture applicable ;
- la traçabilité des décisions de vérification.

Le socle d'échange est FHIR R4 : `Coverage`, `CoverageEligibilityRequest`, `CoverageEligibilityResponse` et, si un catalogue de régimes est exposé, `InsurancePlan`. Les règles nationales de codification, d'autorisation et d'audit restent portées par les ABB transverses existants ; PT-20 ne les redéfinit pas.

La chaîne cible est :

```text
PART-VS-03 → VS-03 → CAP-07 → PRC-09 / PRC-10
           → DO-14 / DO-15 / DO-16 / DO-17
           → ABB-ELIGIBILITE-COUVERTURE → PT-20 → CMP-12
```

Les relations héritées incohérentes sont supprimées :

- `ABB-REGISTRE-PROFESSIONNELS` et PT-05 ne mettent plus en œuvre `ART-4C` ;
- PT-11 ne s'applique plus à CMP-12 ;
- CMP-12 pointe vers `ABB-ELIGIBILITE-COUVERTURE` plutôt que directement vers `CAP-07` ;
- WP-03 réalise explicitement le nouvel ABB.

La décision est enregistrée dans `ADR-0011`.

### 2.2 One Health

La relation avec VS-04 est conservée. Elle est justifiée par la gouvernance intersectorielle portée par `CAP-08`, déjà mobilisée par `ART-11`, et par le centre de commande CMP-02 qui soutient le pilotage de la performance.

La chaîne cible est :

```text
PART-ONE-HEALTH
  ├─ VS-02 → CAP-18 / CAP-05 → surveillance, alerte et riposte
  └─ VS-04 → CAP-08          → coordination, pilotage et redevabilité

ABB-ECHANGE-MEDIATION + ABB-EXPOSITION-DONNEES-ANALYTIQUES
  → PT-15
  → CMP-02 / CMP-04 / CMP-06
  → WP-07
```

Les modifications canoniques sont :

- ajouter `CAP-08` au périmètre de `PART-ONE-HEALTH` ;
- ajouter `PART-ONE-HEALTH` aux partitions des ABB de médiation et d'exposition analytique ;
- faire pointer PT-15 vers ces deux ABB ainsi que vers `CAP-05`, `CAP-08` et `CAP-18` ;
- réaligner WP-07 sur `CAP-08`, `CAP-18`, PT-15 et les deux ABB ;
- retirer de WP-07 le rattachement à `CAP-03`, qui décrit la qualité et la sécurité des soins et non la coordination intersectorielle.

La décision est enregistrée dans `ADR-0012`.

## 3. Objets et artefacts affectés

### Sources canoniques

- nouvel ABB `ABB-ELIGIBILITE-COUVERTURE` ;
- nouveau profil `PT-20` ;
- CMP-12, PT-05, PT-11 et WP-03 ;
- `PART-ONE-HEALTH`, les ABB de médiation et d'analytique, PT-15 et WP-07 ;
- relations inverses des objets de données et des processus concernés ;
- ADR-0011 et ADR-0012, registre et index des décisions.

### Artefacts dérivés

- enveloppes CAESN, ARTSN et PTISN ;
- matrice PTISN et vue de traçabilité par partition ;
- index du repository ;
- OpenAPI PT-20 ;
- portail Mintlify.

## 4. Garde-fous automatiques

Les contrôles suivants deviennent bloquants :

1. `PT-20` doit atteindre `CAP-07` via `ABB-ELIGIBILITE-COUVERTURE` et ne doit pas se rattacher aux ABB d'identité ou de consentement ;
2. CMP-12 doit être réalisé par le nouvel ABB ;
3. PT-05, PT-11 et `ABB-REGISTRE-PROFESSIONNELS` ne doivent plus contenir les relations d'éligibilité supprimées ;
4. toute partition qui déclare explicitement un flux de valeur et des capacités doit posséder au moins une capacité commune avec ce flux ;
5. `PART-ONE-HEALTH` doit produire des chaînes non vides vers VS-02 et VS-04 ;
6. la vue dérivée doit présenter les ABB et profils attendus sans saisie manuelle ;
7. les générateurs ADR, wrappers, index, OpenAPI et Mintlify doivent rester idempotents.

## 5. Validation et critères d'acceptation

Le lot est terminé lorsque :

- les ADR-0011 et ADR-0012 sont conformes et indexés ;
- la chaîne d'éligibilité est complète de `PART-VS-03` jusqu'à CMP-12 ;
- PT-20 possède une spécification et un OpenAPI généré ;
- les deux lignes One Health de la vue de partition ne contiennent plus `n/a` pour les capacités et processus ;
- les anciens rattachements erronés sont absents ;
- tous les tests unitaires passent ;
- `make check` est entièrement vert ;
- la branche est publiée dans une PR distincte vers `main`, sans fusion automatique.

## 6. Hors périmètre

- choix d'un produit logiciel pour le registre d'éligibilité ;
- définition détaillée des règles métier propres à chaque régime de couverture ;
- création d'un nouveau flux de valeur ou d'une nouvelle capacité One Health ;
- modification des responsabilités légales des ministères partenaires ;
- déploiement d'une implémentation FHIR opérationnelle.
