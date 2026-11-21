---
title: "ADR-0015 : Deux emplois de l'accès aux données, adossement des arêtes de processus et autorité du système de référence"
id: adr-0015
domain: 06_decisions
version: "1.0.0"
status: candidate
date: 2026-11-21
owner: DEPSI
tags: ["adr", "donnees", "acces", "processus", "composant", "systeme-de-reference", "integrite"]
related: ["DO-17", "DO-23", "DO-24", "DO-27", "DO-31", "PRC-01", "PRC-03", "PRC-04", "PRC-08", "PRC-10", "CMP-01", "CMP-05", "CMP-12", "CMP-13", "CMP-35", "CMP-36", "ABB-REFERENTIEL-STRUCTURES-SERVICES"]
---

# ADR-0015 : Deux emplois de l'accès aux données, adossement des arêtes de processus et autorité du système de référence

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ○ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle.

- **Statut** : proposé
- **Date** : 2026-11-21
- **Groupe concerné** : DEPSI, CNASN, directions techniques du Ministère de la Santé

## Contexte

La relation `accesses` a été généralisée à l'ensemble des acteurs de la chaîne lors de l'ouverture des ponts entre la couche applicative et la couche des données. Ce choix a produit un champ `accessed_by` porté par les objets de données qui ne distingue pas deux énoncés de nature différente. Le premier est déclaratif : le processus métier qui manipule la donnée, c'est-à-dire celle qu'il produit, met à jour ou consomme. Le second est technique : le composant, le service ou le bloc d'architecture qui détient la donnée, la produit, l'expose ou la met à jour. Le premier répond à la question « à quelle activité la donnée est-elle adossée », le second à la question « où la donnée est-elle logée et qui la tient ».

Cette ambiguïté n'était pas seulement documentaire. Elle a produit des ruptures de chaîne que la mesure rend visibles. Sur les quarante-neuf arêtes qui relient un processus à un objet de données, cinq n'étaient adossées à aucun composant mobilisé par ce processus : le processus manipulait une donnée qu'aucun de ses composants ne portait. Le tableau ci-dessous recense les cinq cas relevés avant correction, avec le composant mobilisé par la correction.

| Processus | Objet de données | Composant mobilisé par la correction |
|-----------|------------------|-------------------------------------|
| PRC-01, accès, orientation et admission du patient | DO-23, formation sanitaire | CMP-13, registre des personnels |
| PRC-03, continuité, suivi et qualité des soins | DO-24, agent de santé | CMP-13, registre des personnels |
| PRC-04, veille, prévention et surveillance sanitaire | DO-27, tâche et action de suivi | CMP-01, tableaux de bord et portails nationaux |
| PRC-08, financement et exemption au point de service | DO-17, demande et preuve de vérification d'éligibilité | CMP-12, registre d'éligibilité et de couverture |
| PRC-10, planification et allocation des ressources | DO-24, agent de santé | CMP-13, registre des personnels |

Le tableau se lit comme un diagnostic et non comme une liste d'ajouts. Les cinq objets concernés sont des données de gestion et de suivi : la formation sanitaire, l'agent de santé, la demande et la preuve de vérification d'éligibilité, la tâche et l'action de suivi. Les processus qui les manipulent sont l'admission du patient, la continuité des soins, la surveillance sanitaire, le financement au point de service et l'allocation des ressources. Le composant mobilisé est, dans chaque cas, celui qui détient effectivement l'objet : le registre des personnels pour les données d'agents et de formation, le registre d'éligibilité pour la preuve de vérification, le tableau de bord national pour le suivi des tâches. La correction ne crée pas de relation arbitraire : elle restaure un maillon que la chaîne à quatre couches rendait obligatoire.

Un second ensemble de trois cas relevait d'une nature différente. Sur les vingt-sept déclarations de `system_of_record` portées par les vingt-trois objets de données, quatre visaient un système qui ne déclarait lui-même aucun accès à l'objet. Elles se répartissaient sur trois objets : DO-23 et DO-26, dont le système de référence est le bloc ABB-REFERENTIEL-STRUCTURES-SERVICES, et DO-31, l'ancre de confiance, dont les systèmes de référence sont la PKI nationale CMP-35 et la passerelle de confiance mondiale CMP-36. La déclaration était donc une attribution sans fondement dans le graphe : un système était désigné comme détenteur de la version faisant foi d'une donnée sans qu'aucune arête ne dise qu'il y accède.

Le métamodèle n'était pas en mesure de trancher ces situations, parce qu'il affirmait que `accesses` et `accessed_by` décrivent un accès unique dont l'énoncé processus n'était pas retenu. Le corpus, lui, stockait les deux familles d'acteurs dans le même champ. La contradiction entre la règle écrite et les documents n'était visible que par la mesure, et elle a été confirmée par la mesure : quarante-neuf arêtes de processus sur soixante-quinze arêtes techniques, deux familles d'acteurs dans un même champ, et aucune règle qui dise laquelle des deux lectures doit être vérifiée.

## Décision

### `accesses` porte deux énoncés distincts, qui sont déclarés comme tels

La relation `accesses` reste une relation unique, conforme au vocabulaire ArchiMate. Ce qui change, c'est que le métamodèle nomme désormais ses deux emplois et les range dans deux directions distinctes de la chaîne à quatre couches. `accesses` porté par le composant est l'énoncé de détention, `accesses` porté par le processus est l'énoncé de manipulation, et `accessed_by`, porté par l'objet, rassemble les deux familles d'acteurs dans la liste inverse. Le lecteur d'un objet de données doit savoir lire ce champ en deux temps, et le métamodèle le lui dit.

Cette distinction est une exigence de fond et non une commodité de présentation. Les deux énoncés ne se déduisent pas l'un de l'autre. Sur le corpus mesuré, les quarante-neuf arêtes de processus se déduisent de la chaîne `PRC` vers `CMP` vers `DO`, mais vingt des soixante-quinze arêtes techniques ne sont pas restituables par cette chaîne : leurs dix porteurs sont le moteur de graphes et référentiel spatio-temporel CMP-05, cinq services d'interface (SRV-02 à SRV-06), les deux blocs d'architecture ABB-ELIGIBILITE-COUVERTURE et ABB-REFERENTIEL-STRUCTURES-SERVICES, et les deux autorités de certification CMP-35 et CMP-36. Aucun processus déclaré ne les mobilise. Aucun objet de données ne peut donc être ramené à l'une de ses deux extrémités, et les deux familles d'acteurs ne sont pas interchangeables.

### Toute arête de processus est adossée à un composant mobilisé

Le validateur refuse désormais une arête `PRC` vers `DO` lorsqu'aucun composant mobilisé par ce processus ne déclare lui-même `accesses` vers l'objet. La règle se lit dans la chaîne : le processus ne peut manipuler une donnée qu'aucun de ses composants ne porte. Elle est vérifiée sur le corpus, où elle ne trouve plus aucun cas.

La correction des cinq cas relevés s'est faite par la chaîne et non par la suppression. Dans chaque cas, le processus mobilise le composant qui porte la donnée, et le composant déclare en retour `applies_to` ce processus. La relation `uses` et sa réciproque `applies_to` sont ainsi symétriques sur les cinq paires ajoutées, et le validateur refuse désormais toute asymétrie entre ces deux relations, ce qui aurait laissé passer une correction appliquée d'un seul côté.

### Le système de référence déclare lui-même son accès

Le validateur refuse une déclaration de `system_of_record` dont le système visé ne déclare pas `accesses` vers l'objet. Le contrôle porte sur la déclaration d'accès portée par le système lui-même, qui fait foi, et non sur la liste inverse portée par l'objet : une liste inverse peut être omise ou contredite, une déclaration d'accès ne peut pas l'être sans que le lien soit rompu dans les deux sens.

Les quatre déclarations concernées ont été rétablies. Le bloc ABB-REFERENTIEL-STRUCTURES-SERVICES déclare désormais son accès à DO-23 et à DO-26, et les deux objets l'inscrivent dans leur liste d'accesseurs. CMP-35 et CMP-36 déclarent leur accès à DO-31, l'ancre de confiance, et l'objet les inscrit également. Cette correction relève d'une exception nommée et strictement limitée : ces deux composants sont les autorités émettrices des certificats dont l'ancre de confiance est faite, ils les émettent, les publient et les vérifient, et ne les transportent pas au sens où le ferait un composant applicatif. L'exception ne s'étend à aucune donnée métier et ne préfigure pas un rattachement général du socle transverse aux objets de données.

### Le contrôle de l'autorité remplace le contrôle de l'appartenance à une liste

La formulation de la règle d'intégrité a été corrigée en conséquence. Elle ne dit plus que le système de référence figure parmi les accesseurs de l'objet, mais que le système de référence déclare lui-même l'accès à cet objet et figure parmi ses accesseurs. La seconde proposition est une conséquence de la première et du contrôle de symétrie entre `accesses` et `accessed_by` ; elle est énoncée pour que le lecteur ne croie pas que l'appartenance à une liste suffit.

L'état mesuré du corpus après correction est le suivant : sur les trente-huit composants, vingt-deux déclarent des objets de données portés, dont vingt composants applicatifs et les deux autorités de confiance CMP-35 et CMP-36 ; les treize processus déclarent tous leurs données ; les vingt-trois objets de données sont tous détenus et tous utilisés ; les sept terminologies sont toutes portées par un composant ; les quarante-neuf arêtes de processus sont toutes adossées à un composant mobilisé ; les vingt-sept déclarations de système de référence sont toutes adossées à une déclaration d'accès.

## Justification

La démarche HEAL impose de travailler avec les catégories du terrain plutôt qu'avec une nomenclature fermée. La présente décision en est une application directe : la distinction entre manipulation et détention n'a pas été imposée par un catalogue extérieur, elle a été déduite de la mesure du corpus malgache, qui a fait apparaître cinq arêtes sans support et quatre attributions sans fondement. Le nombre de règles est resté constant : une relation, deux emplois, trois contrôles.

Le HEAF impose une décomposition par valeurs et par couches, et son exigence de modularité se lit ici dans le refus de créer une relation supplémentaire. La tentation aurait été d'introduire deux relations distinctes, l'une pour la manipulation et l'autre pour la détention, afin que la liste d'accesseurs ne mêle plus les familles d'acteurs. Ce serait une sur-conception : le vocabulaire ArchiMate connaît `access`, et le référentiel n'a pas de besoin propre d'une relation supplémentaire. La correction porte sur la déclaration et sur le contrôle, non sur le vocabulaire du modèle.

Le HEART impose la réutilisation d'artefacts et la génération de métadonnées depuis une source unique de vérité. Les trois contrôles ajoutés au validateur sont, à ce titre, des artefacts de la décision : ils sont exécutés à chaque build, et leurs tests sont écrits de façon que chaque violation soit détectable sur un graphe fautif et non seulement sur un corpus sain. La décision ne s'arrête donc pas à la correction des huit cas relevés, cinq arêtes de processus et trois objets de données : elle installe les conditions qui font que ces cas ne puissent revenir sans que le build échoue.

## Conséquences

### Positives

- La chaîne à quatre couches est bouclée sur ses deux maillons faibles : toute arête de processus est adossée à un composant mobilisé, et toute attribution de version faisant foi est adossée à une déclaration d'accès.
- Le champ `accessed_by` d'un objet de données devient lisible : le lecteur sait que la liste mêle les processus qui manipulent la donnée et les composants qui la détiennent, et il sait pourquoi les deux y figurent.
- Les asymétries entre `uses` et `applies_to` sont impossibles à introduire : le validateur les refuse, et les corrections apportées aux cinq couples ont été bilatérales par construction.
- Le contrôle de l'autorité du système de référence a une portée qui dépasse le présent lot : toute déclaration future de `system_of_record` devra être adossée à un accès déclaré, ce qui protège la couche données contre les attributions de convenance.

### Négatives

- La charge de maintenance du corpus augmente : toute évolution d'un processus qui manipule une donnée impose de vérifier que le composant qui porte la donnée est bien mobilisé, et toute évolution d'un `system_of_record` impose que le système visé déclare son accès.
- Le bloc ABB-REFERENTIEL-STRUCTURES-SERVICES et les deux autorités de certification CMP-35 et CMP-36 ne sont pas adossés à un processus déclaré. Leur rattachement au reste de la chaîne reste porté par les composants et les blocs qui les exploitent, et le validateur ne le vérifie pas.
- La correction des cinq cas a modifié le contenu de cinq processus, de trois composants, de trois objets de données et d'un bloc d'architecture. Elle impose une relecture par les directions métier concernées, en particulier sur le rattachement de PRC-04 à CMP-01, qui lie la surveillance sanitaire aux tableaux de bord.
- Le validateur refuse désormais des graphes qui étaient acceptés jusqu'ici. C'est la contrepartie assumée d'une règle d'intégrité : elle produit des échecs de build sur des graphes legacy, ce qui suppose de traiter ces échecs comme des défauts et non comme des faux positifs.

## Alternatives considérées

| Alternative | Raison du refus |
|-------------|-----------------|
| Supprimer les cinq arêtes de processus non adossées | Chaque processus manipule réellement la donnée : le financement a besoin de la preuve de vérification d'éligibilité, l'admission du patient a besoin de la formation des agents, la surveillance a besoin du tableau de bord des tâches. Supprimer l'arête aurait effacé un fait métier pour rendre le corpus conforme à un outil. |
| Supprimer les quatre déclarations de système de référence non adossées | Le référentiel des structures et services et la chaîne de confiance détiennent réellement la version faisant foi de ces objets. Supprimer la déclaration aurait laissé la donnée sans autorité, ce qui est le défaut inverse de celui que la décision corrige. |
| Introduire deux relations, l'une de manipulation et l'autre de détention | La relation supplémentaire aurait accru la surface du modèle sans bénéfice : le vocabulaire ArchiMate connaît `access`, et la distinction se règle par la documentation et le contrôle, non par une arête de plus. |
| Contrôler le système de référence par sa présence dans la liste `accessed_by` | Une liste inverse peut être omise ou contredite. Le contrôle doit porter sur la déclaration d'accès du système lui-même, qui est l'éncé source, et non sur une liste dérivée. |
| Rendre la manipulation des données par le processus optionnelle | La chaîne à quatre couches suppose que le maillon applicatif existe. Rendre le maillon facultatif aurait réintroduit la rupture que la chaîne prétend supprimer. |
| Étendre le rattachement du socle transverse à tous les objets de données | Le socle est atteint par `uses` depuis les composants applicatifs. L'attacher directement à tous les objets aurait créé une seconde chaîne concurrente et faussé la lecture de la détention. |

## Annexe : contrôles ajoutés au validateur

| Contrôle | Portée | Effet en cas de violation |
|---------|--------|---------------------------|
| Toute arête `PRC` vers `DO` est adossée à un composant mobilisé qui porte l'objet | Objets de données et processus métiers | Le validateur échoue |
| Tout `system_of_record` déclare lui-même `accesses` vers l'objet dont il est le système de référence | Objets de données | Le validateur échoue |
| `uses` et `applies_to` sont symétriques pour le couple PRC/CMP | Processus métiers et composants | Le validateur échoue |

## Références

- [Chaîne à quatre couches et règles d'intégrité](../../04_architecture-repository/00_metamodel/schema.md)
- [ADR-0014 : Rationalisation du catalogue des objets de données](adr-0014-rationalisation-catalogue-donnees.md)
- [PRC-01 : Accès, orientation et admission du patient](../../04_architecture-repository/03_business-architecture/business/processes/prc-01.md)
- [PRC-04 : Veille, prévention et surveillance sanitaire](../../04_architecture-repository/03_business-architecture/business/processes/prc-04.md)
- [CMP-13 : Registre des personnels](../../04_architecture-repository/05_reference-library/building-blocks/sbb/cmp-13.md)
- [CMP-35 : Infrastructure de cles publiques (PKI)](../../04_architecture-repository/05_reference-library/building-blocks/sbb/cmp-35.md)
- [ABB-REFERENTIEL-STRUCTURES-SERVICES : Référentiel des structures et services de santé](../../04_architecture-repository/05_reference-library/building-blocks/abb/abb-referentiel-structures-services.md)
- [DO-31 : Ancre de confiance](../../04_architecture-repository/04_data-architecture/data-objects/do-31.md)
