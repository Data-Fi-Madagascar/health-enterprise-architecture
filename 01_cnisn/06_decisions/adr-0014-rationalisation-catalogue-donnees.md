---
title: "ADR-0014 : Rationalisation du catalogue des objets de données par fusion, gouvernance de la valeur d'usage et traçabilité des retraits"
id: adr-0014
domain: 06_decisions
version: "1.0.0"
status: candidate
date: 2026-11-21
owner: DEPSI
tags: ["adr", "donnees", "rationalisation", "fusion", "gouvernance", "tracabilite"]
related: ["DO-01", "DO-03", "DO-07", "DO-12", "DO-14", "DO-18", "DO-25", "DO-29", "DO-32", "CMP-01"]
---

# ADR-0014 : Rationalisation du catalogue des objets de données par fusion, gouvernance de la valeur d'usage et traçabilité des retraits

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ○ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle.

- **Statut** : proposé
- **Date** : 2026-11-21
- **Groupe concerné** : DEPSI, CNASN, directions techniques du Ministère de la Santé

## Contexte

Le référentiel compte trente et un objets de données. Ce nombre n'a pas été atteint par une méthode de constitution : il résulte d'ajoutements successifs au fil des chantiers, chacun défendable au moment où il a été proposé, et plusieurs ne l'étant plus une fois que le catalogue s'est densifié. La question posée au Bureau de Réalisation de la Valeur était celle de la redondance : quelles entrées du catalogue décrivent la même réalité sous deux noms, et lesquelles n'en décrivent aucune.

La mesure sur le corpus avant correction a fait apparaître cinq situations distinctes. La première est celle de l'attribut promu en objet : l'identifiant national d'identification, DO-02, n'était pas une entité du système de santé mais une valeur portée par le dossier du patient. La deuxième est celle du contenant et de son contenu : l'épisode de soins, DO-04, était à la fois une entité de regroupement et une partie du dossier, DO-03, qui le porte déjà ; la section du résumé patient, DO-30, était une structure interne du résumé international du patient, DO-29. La troisième est celle de la quantité sans son support : le stock, DO-13, n'existait pas indépendamment du lot de produit de santé, DO-12, qui en porte la quantité. La quatrième est celle des étapes d'un même cycle : la notification sanitaire, DO-21, et l'alerte sanitaire, DO-22, sont deux moments du cycle signal, notification, alerte déjà porté par DO-18. La cinquième est d'une autre nature : le tableau de bord, DO-28, est un artefact de restitution, sa configuration relevant du composant qui l'expose et non d'une donnée du système de santé.

Un catalogue corrigé de vingt objets a été transmis à titre de proposition. Il comportait une renumérotation complète et quatre fusions supplémentaires. La renumérotation et ces quatre fusions ont été refusées, pour des raisons qui sont exposées plus bas. Ce qui en a été retenu, c'est l'analyse des recouvrements : elle est juste dans ses cinq situations, même si elle conclut à un catalogue plus court que vingt objets, parce que les fusions contestables ne sont pas des recouvrements.

Le risque propre à une opération de ce type est l'orphelinage de la trace. Le référentiel n'était pas un catalogue isolé : au moment de l'examen, il portait deux cent dix-huit relations pointant vers des objets de données, deux cent soixante-quatorze liens Markdown vers ces mêmes objets, et mille trois cent soixante-sept mentions textuelles de leurs identifiants dans le corpus. Une suppression non tracée n'aurait pas réduit la redondance ; elle aurait cassé une chaîne de deux cent dix-huit relations en laissant au lecteur la seule possibilité de deviner ce que l'identifiant disparu désignait.

## Décision

### Le catalogue compte vingt-trois objets de données, identifiants préservés

Les identifiants des objets qui survivent ne sont pas modifiés. Les neuf entrées retirées sont huit fusions et un retrait avec hébergement. Un objet est créé, DO-32, qui manquait. La liste complète est la suivante.

| Identifiant retiré | Titre d'origine | Sort | Successeur | Motif |
|--------------------|-----------------|------|------------|-------|
| DO-02 | Identifiant national d'identification | fusion | DO-01 | Le NIN est une valeur de l'identifiant patient, non une entité autonome : il est porté par DO-01. |
| DO-04 | Épisode de soins | fusion | DO-03 | Le dossier assume à la fois le regroupement des épisodes et l'index des documents qu'il contient. |
| DO-08 | Contre-référence | fusion | DO-07 | La contre-référence est le retour de la référence : les deux forment un seul événement inter-établissement. |
| DO-13 | Stock | fusion | DO-12 | Le stock est la mesure de quantité associée au lot : il rejoint DO-12 sous un seul objet. |
| DO-15 | Couverture sanitaire | fusion | DO-14 | La couverture et son statut d'éligibilité forment un seul objet de financement. |
| DO-21 | Notification sanitaire | fusion | DO-18 | La notification est l'étape formelle du cycle de surveillance, non un objet autonome. |
| DO-22 | Alerte sanitaire | fusion | DO-18 | L'alerte est l'étape opérationnelle du même cycle, portée par DO-18. |
| DO-28 | Tableau de bord | retrait hébergé | CMP-01 | Un tableau de bord est un artefact de restitution : sa configuration est décrite par CMP-01, sa source de vérité restant DO-25. |
| DO-30 | Section du résumé patient | fusion | DO-29 | La section est la structure interne du résumé international du patient : elle rejoint DO-29. |

Le tableau se lit par nature de recouvrement : les quatre premières fusions portent sur des relations de partie à tout ou d'attribut à porteur, les trois suivantes sur des étapes d'un cycle unique, la dernière sur un objet qui n'a pas sa place dans la couche. Ce sont ces différences de nature, et non une règle générale de fusion, qui ont fondé la décision.

L'objet créé, DO-32, couvre l'examen et son résultat de laboratoire. Le corpus ne comportait aucun objet pour le résultat d'examen, alors que le processus de prestation des soins cliniques, le processus de la lutte antituberculeuse, le composant des dossiers et statistiques de santé et le composant de laboratoire le manipulaient déjà. L'absence était un trou de la chaîne, non une simplification possible. L'objet est déclaré au service de trois capacités, l'offre de soins, la surveillance et la coordination intersectorielle, et il est adossé à la terminologie LOINC.

### La valeur d'usage de la donnée devient une propriété déclarée

Chaque objet de données déclare désormais deux propriétés qui décrivent sa valeur et non ses arêtes. `tier` classe la donnée en trois niveaux : `A` pour les données de référence et de pilotage, `B` pour les données transactionnelles et opérationnelles, `C` pour les données d'appui analytique. Le corpus se répartit en six objets de tier A, seize de tier B et un de tier C, l'indicateur sanitaire étant la seule donnée de restitution. `system_of_record` désigne le système qui détient la version faisant foi de la donnée, et ne peut viser qu'un composant ou un bloc d'architecture.

Ces deux propriétés sont délibérément des métadonnées et non des relations. Elles ne créent aucune arête dans le graphe : un objet de données n'est pas réalisé par le composant qui en est le système de référence au sens où une capacité est réalisée par un processus, et le traiter comme une relation aurait produit une deuxième chaîne concurrente de la chaîne à quatre couches. Elles ont en revanche une portée de contrôle : le validateur refuse un objet de données sans tier, un tier hors de l'ensemble A, B, C, et un system_of_record qui ne cible pas un composant ou un bloc d'architecture.

### Le retrait devient une propriété tracée

Chaque objet qui absorbe un ou plusieurs objets retirés déclare cette absorption dans la propriété `absorbs`. La propriété n'est pas une relation du graphe : elle porte un identifiant qui ne désigne plus aucun objet, et l'introduire comme cible de relation aurait cassé la résolution des cibles. Elle est confrontée au fichier `04_architecture-repository/00_metamodel/do-migration.yaml`, qui enregistre pour chaque identifiant retiré son titre d'origine, son sort, son successeur et la raison de la fusion.

Le fichier de migration est la seule source qui autorise la présence d'un identifiant retiré dans le corpus. Le validateur vérifie que ce fichier déclare bien les neuf retraits, que chaque fusion soit déclarée par le `absorbs` de son successeur, qu'aucun identifiant retiré ne subsiste comme objet actif ni comme cible d'une relation, et qu'aucun frontmatter du corpus ne pointe vers un identifiant retiré. La charge utile de l'objet retiré avec hébergement, DO-28, est vérifiée dans l'autre sens : le composant qui l'héberge, CMP-01, doit mentionner l'identifiant retiré dans son corps.

### Le tableau de bord cesse d'être une donnée

La configuration des tableaux de bord est un artefact de restitution : elle décrit ce qui est affiché, à qui, sur quelle période et avec quels seuils d'alerte, et non une donnée du système de santé. Elle est désormais décrite dans CMP-01, qui est le composant qui expose les tableaux de bord unifiés du pilotage national, tandis que DO-25 demeure la source de vérité des indicateurs affichés. La distinction est structurante pour la suite : elle écarte du catalogue des données ce qui n'est qu'une projection d'indicateurs, et elle rend l'artefact de présentation lisible là où il est mis en œuvre.

## Justification

La démarche HEAL, fondée sur la recherche appliquée architectures dans les pays à ressources limitées, impose de travailler avec les catégories du terrain plutôt qu'avec une nomenclature fermée. Le résultat du présent lot en est la conséquence directe : la réduction du catalogue n'a pas été obtenue par l'application d'un catalogue de référence extérieur, mais par l'analyse des recouvrements constatés dans le corpus malgache lui-même. La proposition reçue a servi de contre-évaluation, non de source.

Le HEAF impose une décomposition par valeurs et par couches, et son exigence de modularité se lit ici dans le refus de créer des îlots. Huit des neuf retraits sont des fusions : ils rapprochent des objets qui décrivaient un même fait sous deux entrées. Le neuvième est un déplacement de nature, vers le composant qui porte la réalité. Aucun de ces retraits n'a créé de couche, de type ou de famille nouvelle, et le catalogue reste lisible sans knowledge management annexe.

Le HEART impose la réutilisation d'artefacts et la génération de métadonnées depuis une source unique de vérité. C'est à cette exigence que la trace de migration répond : le fichier `do-migration.yaml` est, pour les objets de données, l'équivalent du fichier `cap-int-migration.yaml` qui assure la continuité des anciens identifiants d'interopérabilité. La propriété `absorbs` et le fichier de migration sont deux lectures du même fait, l'une dans le document, l'autre dans l'outil, et leur confrontation automatique est ce qui empêche la dérive entre les deux.

Le refus de renumérotation mérite une explication propre, car c'est le point sur lequel la proposition reçue et la présente décision divergent le plus nettement. La renumérotation aurait produit un catalogue de vingt objets dont les identifiants ne correspondraient plus à aucun document existant. Deux cent dix-huit relations, deux cent soixante-quatorze liens et mille trois cent soixante-sept mentions auraient dû être réécrits sur la base d'une correspondance qui n'était plus vérifiable. Le bénéfice attendu d'une numérotation continue est réel mais secondaire : il ne compense pas une rupture de traçabilité sur la couche la plus utilisée du référentiel. La décision conserve donc les identifiants, ce qui a une contrepartie assumée : la plage DO-01 à DO-32 contient désormais des vides, et la lecture du catalogue doit passer par la trace de migration et non par l'arithmétique des identifiants.

Les quatre fusions refusées sont refusées pour des raisons distinctes, qu'il est utile de distinguer. La fusion de la formation sanitaire et de la zone sanitaire en un objet de structure unique est refusée parce que les deux objets n'ont ni le même cycle de vie, ni le même producteur, ni la même autorité de codification : une formation est une entité physique dotée d'un code, une zone est un découpage administratif d'un district. La fusion de la facturation dans la couverture et l'éligibilité est refusée parce que la facturation est un acte de gestion de la trésorerie, qui survit à la période de couverture et se mesure dans une devise, tandis que l'éligibilité est un état de droit attaché à un bénéficiaire pour une période donnée. La fusion du dossier patient et de l'ancre de confiance est refusée parce que l'ancre de confiance est un mécanisme technique d'authentification et de signature, dont le cycle de vie est celui d'un artefact et non celui d'un dossier de soins. La fusion de l'indicateur sanitaire avec le tableau de bord est refusée par le présent ADR lui-même, pour la raison exposée ci-dessus.

Ces refus ne sont pas des conservations par principe. Ils expriment que la fusion d'objets de données n'est praticable que lorsque les objets partagent une identité de nature, et que le critère de fusion est la relation sémantique entre les objets, non leur proximité dans un tableau ou dans une liste de codes.

## Conséquences

### Positives

- Le catalogue des objets de données passe de trente et un à vingt-trois entrées, sans que la couche ne perde aucune des relations qu'elle portait : les cent soixante-quinze relations pointant vers des objets de données sont toutes résolues et toutes vérifiables.
- Chaque objet de données déclare son niveau de criticité et son système de référence, ce qui rend la question de la responsabilité sur la donnée réponse par le corpus et non par une convention orale.
- Les neuf retraits sont réversibles et auditablement tracés : le fichier de migration conserve le titre d'origine, le sort et la raison de chaque retrait, et le validateur refuse toute divergence entre le fichier et les documents.
- Le tableau de bord est enfin lisible comme ce qu'il est, un composant de restitution, et non comme une donnée parmi d'autres.

### Négatives

- La plage des identifiants comporte désormais des vides. Tout lecteur qui compte sur la continuité de la numérotation doit passer par la trace de migration, ce qui ajoute une étape de lecture.
- Les schémas de payload des neuf objets retirés ont été supprimés : un consommateur qui visait `03_ptisn/schemas/payloads/do-02.json` doit migrer vers `do-01.json`, et le changement est cassant pour lui.
- Le corpus gagne deux contraintes de maintenance : toute évolution du catalogue des objets de données doit préserver le tier, le system_of_record et la cohérence de la trace, faute de quoi le validateur échoue.
- Les neuf fusions ont modifié le contenu de huit objets de données survivants, ce qui impose une relecture par les directions métier concernées.

## Alternatives considérées

| Alternative | Raison du refus |
|-------------|-----------------|
| Appliquer la renumérotation du catalogue corrigé en vingt objets | Elle imposait la réécriture de deux cent dix-huit relations, deux cent soixante-quatorze liens et mille trois cent soixante-sept mentions sur une correspondance non vérifiable, pour un bénéfice de continuité de numérotation. |
| Fusionner la formation sanitaire et la zone sanitaire | Les deux objets ont des cycles de vie, des producteurs et des autorités de codification distincts : leur réunion produirait un objet dont les règles de gestion ne peuvent être énoncées. |
| Fusionner la facturation dans la couverture et l'éligibilité | La facturation est un acte de gestion de la trésorerie, l'éligibilité un état de droit : les deux fusionnés produiraient un objet dont la période de validité n'a pas de sens. |
| Fusionner l'ancre de confiance dans le dossier patient | L'ancre de confiance est un artefact technique d'authentification, dont le cycle de vie et la source de vérité ne sont pas ceux d'un dossier de soins. |
| Fusionner le tableau de bord dans l'indicateur sanitaire | Un tableau de bord est une restitution, non une donnée : la fusion aurait confondu la définition de l'indicateur avec son mode d'affichage. |
| Supprimer les objets redondants sans laisser de trace | Les identifiants disparus seraient devenues des trous muets dans la chaîne ; le lecteur n'aurait plus aucun moyen de savoir ce que chaque relation pointait auparavant. |
| Fusionner sur le seul critère du voisinage dans la numérotation | La numérotation est un artefact de présentation : la fusion d'objets de données doit résulter de leur identité de nature, non de leur position dans une liste. |
| Créer un objet pour chaque étape d'un cycle | Cette décomposition est légitime au niveau des processus, où chaque étape a un responsable ; au niveau des données, elle produit des objets sans producteur ni consommateur distincts. |
| Ne pas créer DO-32 et laisser le résultat d'examen non modélisé | Le résultat d'examen était déjà manipulé par des processus et des composants : l'absence d'objet rendait la chaîne incomplète sur ce point. |

## Annexe : contrôles ajoutés au validateur

| Contrôle | Portée | Effet en cas de violation |
|---------|--------|---------------------------|
| `tier` présent et valant A, B ou C | Objets de données | Le validateur échoue |
| `system_of_record` présent et ciblant un composant ou un bloc d'architecture | Objets de données | Le validateur échoue |
| `absorbs` conforme à la trace de migration | Objets de données | Le validateur échoue |
| Aucun identifiant retiré présent comme objet actif ou comme cible de relation | Catalogue des objets de données | Le validateur échoue |
| Aucun frontmatter du corpus pointant vers un identifiant retiré | Corpus | Le validateur échoue |
| Charge utile retirée documentée par le composant qui l'héberge | CMP-01 | Le validateur échoue |

## Références

- [Chaîne à quatre couches et règles d'intégrité](../../04_architecture-repository/00_metamodel/schema.md)
- [Trace de migration du catalogue des objets de données](../../04_architecture-repository/00_metamodel/do-migration.yaml)
- [ADR-0013 : Taxonomie des fonctions de domaine comme référence de couverture et réconciliation de la chaîne vers les données](adr-0013-cadrage-fonctions-domaine.md)
- [CMP-01 : Tableaux de bord et portails nationaux](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-01.md)
- [DO-25 : Indicateur sanitaire](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-25.md)
- [DO-32 : Examen et résultat de laboratoire](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-32.md)
