---

title: "Principes de l'architecture applicative"
id: application-principles
domain: 05_application
version: "1.0.0"
status: draft
last_reviewed: 2026-07-03
owner: Direction des Systèmes d'Information
tags: ["applications", "urbanisation", "principes"]
---

# Principes de l'architecture applicative

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ◐ |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.


Les principes suivants s'appliquent à toute application ou plateforme numérique du secteur santé. Chaque principe vit dans le référentiel : `referentiel/principes/aa-XX.md`.

## Catalogue des principes applicatifs

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Les applications sont dérivées des flux de valeur et des capabilités

#### Signification

Une application n’a de légitimité que si elle soutient une capabilité nécessaire à un flux de valeur national. Une application qui ne se rattache à aucun flux ni à aucune capabilité est redondante ou hors périmètre : elle n’a pas sa place dans le paysage cible.

#### Implications

Chaque application doit indiquer le flux de valeur, la capabilité, les données et les indicateurs qu’elle soutient. Ces informations permettent de détecter les doublons, de justifier les investissements et de retirer les applications qui ne servent plus aucune finalité de santé publique.

### Les applications ne doivent pas dupliquer les référentiels nationaux

#### Signification

Les référentiels nationaux sont des biens communs, pas des composants internes à une application. Chaque application qui gère sa propre liste en parallèle crée une source de données concurrente, dont l’écart ne cesse de croître avec la source officielle.

#### Implications

Une application consomme les référentiels nationaux plutôt que de créer ses propres listes (formations sanitaires, agents, produits, indicateurs, bénéficiaires). Lorsqu’une donnée de référence est nécessaire, elle est résolue par le référentiel officiel et référencée par identifiant stable, jamais recopiée comme donnée locale.

### Les applications doivent être interopérables par conception

#### Signification

L’interopérabilité est une exigence de conception, pas une option ajoutée après déploiement. Une application construite sans interfaces standardisées devient ensuite coûteuse à ouvrir et crée des points d’échange ad hoc difficiles à maintenir.

#### Implications

Toute application expose et consomme des interfaces documentées, sécurisées et conformes à l’Architecture de Référence Technique. Les échanges respectent les profils techniques nationaux dès la première version livrée, et non lors d’une mise à niveau ultérieure.

### Les applications opérationnelles et analytiques doivent être séparées

#### Signification

Les finalités opérationnelles et analytiques imposent des architectures différentes. Un outil de prestation ne doit pas devenir un outil de reporting, et un entrepôt ne doit pas remplacer un système opérationnel : chaque type de système a un rôle, des exigences de disponibilité et des garanties distinctes.

#### Implications

Les systèmes opérationnels soutiennent l’action en temps réel (soins, logistique, enregistrement) ; les entrepôts et tableaux de bord soutiennent l’analyse rétrospective et la décision. Les données circulent des premiers vers les seconds par des mécanismes d’intégration gouvernés, sans que le reporting ne pèse sur l’acte de prestation.

### Les applications doivent fonctionner dans les conditions réelles du terrain

#### Signification

Les usages de terrain se déroulent dans des conditions réelles de connectivité : coupures, zones blanches, bande passante réduite. Une application conçue pour un réseau stable devient inutilisable dès que la couverture disparaît, alors que l’acte clinique et la saisie ne peuvent pas attendre.

#### Implications

Les applications destinées au terrain prévoient un mode hors ligne ou dégradé : saisie locale, persistance autonome, puis synchronisation asynchrone au retour de la connectivité. Cette capacité est prévue dès la conception et testée dans les conditions réelles d’usage, pas seulement sur réseau de laboratoire.

### Les plateformes partagées doivent être réutilisées avant de créer de nouveaux composants

#### Signification

Le système doit éviter la multiplication de solutions parallèles qui se recouvrent. Chaque nouveau composant ajoute des coûts de maintenance, des doublons de données et des interfaces à préserver ; un service partagé existant rend ces coûts inutiles.

#### Implications

Avant de construire un nouveau composant, l’initiative vérifie l’existence d’un service partagé national répondant au besoin. Si le service existe, elle l’utilise ; si aucune plateforme ne convient, elle le documente et sollicite l’arbitrage avant tout développement.

### Les applications doivent être soutenables

#### Signification

Une dépendance durable à un partenaire unique fragilise le système national : elle expose l’État au coût, à l’interruption ou à la disparition du service. Une application doit pouvoir être maintenue et reprise par d’autres acteurs sans blocage.

#### Implications

Toute application modélise la maintenance, le support, le transfert de compétences, le coût total de possession et la réversibilité. Le contrat prévoit les conditions de reprise, l’accès au code et aux données, et la continuité de service en cas de changement de fournisseur.

### Les applications doivent être homologuées avant extension

#### Signification

Une application pilote ne doit pas être généralisée sans validation. Étendre une solution non évaluée à l’ensemble du territoire propage ses défauts et rend la correction plus coûteuse qu’avant déploiement.

#### Implications

L’extension est conditionnée à l’alignement sur le cadre, les standards, la sécurité et la valeur démontrée. Une homologation formelle valide le passage de l’échelle pilote à l’échelle nationale, sur la base de preuves issues du pilote et de l’absence d’écart bloquant.

### Les applications obsolètes ou redondantes doivent être rationalisées

#### Signification

Le portefeuille applicatif doit évoluer, pas s’accumuler. Conserver des systèmes obsolètes ou redondants entretient des doublons de données, des risques de sécurité et des coûts de maintenance sans bénéfice.

#### Implications

Les doublons, systèmes non utilisés ou non conformes sont consolidés, remplacés ou retirés. La rationalisation est planifiée, avec des critères explicites (usage réel, alignement au cadre, coût, risque) et un calendrier de retrait pour chaque système concerné.

<!-- END:GENERATED -->
## Liens

- Architecture applicative
- Règles d'urbanisation
- Rationalisation

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Architecture applicative** : Architecture applicative et systèmes numériques (`00_caesn/05_application/index.md`)
- **Règles d'urbanisation** : Règles d'urbanisation applicative (`00_caesn/05_application/urbanisation.md`)
- **Rationalisation** : Trajectoire de rationalisation du paysage applicatif (`00_caesn/05_application/rationalization.md`)
