---
title: "ADR-0017 : Retrait des objets métier au profit des thèmes de données et fusion dans CMP-10"
id: adr-0017
domain: 06_decisions
version: "1.0.0"
status: candidate
date: 2026-11-21
owner: DEPSI
tags: ["adr", "donnees", "composants", "metamodele", "rationalisation", "interoperabilite"]
related: ["DO-01", "DO-32", "CMP-10", "ART-4", "CAP-13", "CAP-14", "WP-02", "WP-03", "ADR-0014"]
---

# ADR-0017 : Retrait des objets métier au profit des thèmes de données et fusion dans CMP-10

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

Le référentiel portait deux couches concurrentes pour décrire les mêmes choses. La couche des objets métier, introduite au niveau 1 du cadre d'entreprise, classait la matière du domaine en sept ensembles : BO-01 « Patient & identité », BO-02 « Prestation & soins », BO-03 « Dispensation & produits », BO-04 « Financement & couverture », BO-05 « Risque & surveillance », BO-06 « Exploitation & gestion » et BO-07 « Interopérabilité transfrontalière ». La couche des objets de données, introduite au niveau 3 par le référentiel technique, classait la même matière en vingt-trois objets : DO-01 à DO-32, dont neuf avaient été retirés par fusion lors de l'ADR-0014.

Les deux couches n'étaient pas de même nature. Un objet de données est un actif informationnel : il porte un niveau de criticité, un système de référence, des ressources d'échange FHIR, des terminologies constrainantes et des accesseurs. Un objet métier était, dans le corpus, une liste de objets de données assortie d'une liste de flux de valeur et d'un renvoi vers le dictionnaire des données fonctionnelles. La mesure de l'état avant correction est nette : les sept objets métier portaient ensemble cinquante-six arêtes de relation, dont vingt-deux pointaient vers des objets de données ; aucune ne portait d'information que les vingt-trois objets de données ne portaient déjà. Sur le plan des liens, vingt-deux des vingt-trois objets de données étaient référencés par la couche métier, et un seul, DO-32 « Examen et résultat de laboratoire », ne l'était pas.

Cette structure posait trois problèmes distincts, dont la gravity était inégale.

Le premier était une contradiction de granularité. Le dictionnaire des données fonctionnelles de l'ARTSN classait déjà les objets de données en sept sections numérotées, dont les intitulés reprennent exactement les sept objets métier : « 1. Patient & identité », « 2. Prestation & soins », « 3. Dispensation & produits », « 4. Financement & couverture », « 5. Risque & surveillance », « 6. Exploitation & gestion », « 7. Interopérabilité transfrontalière & résumé patient ». Le corpus contenait donc deux taxonomies parallèles du même domaine, dont l'une était une copie de l'autre, et dont la copie s'écartait de la source sur un point : DO-32 était classé dans la section « Prestation & soins » du dictionnaire mais absent de la liste de BO-02. Un lecteur qui confrontait les deux documents.constatait une divergence sans avoir le moyen de savoir laquelle fait foi.

Le deuxième était une sous-déclaration sémantique. La couche métier n'était pas reliée au graphe de façon utile : ses relations pointaient vers des objets de données, ce qui créait des arêtes sans charge propre, et ses objets n'étaient atteignables que par leur énumération. Aucun lecteur ne pouvait demander quels objets de données appartiennent à un thème sans passer par une liste rédigée à la main, donc susceptible de dériver de la source.

Le troisième était un défaut de la couche composants, d'une autre nature. Le composant CMP-09 « Référentiel des métadonnées d'exploitation » et le composant CMP-10 « Registre des terminologies » portaient la même signature relationnelle : ils implémentaient tous deux ART-4, s'appliquaient tous deux aux mêmes deux processus PRC-07 et PRC-08, accèdent tous deux aux mêmes sept terminologies, et déclarent les mêmes objets de contexte. Sur les huit champs relationnels comparables, six étaient identiques ; ils ne divergeaient que sur le rattachement à un bloc d'architecture et sur le paquet de travail responsable. Le corpus Traitait donc un composant unique comme deux.

Ce doublon masquait en outre une contradiction. CMP-09 se déclarait rattaché à ABB-GESTION-CONSENTEMENT, le bloc de gestion du consentement, alors que son propre contenu décrit l'autorité sémantique de la plateforme, c'est-à-dire le registre des terminologies : c'est CMP-10 dont le rattachement à ABB-SERVICE-TERMINOLOGIE est exact. Le lien était faux, et il l'était précisément parce que les deux composants se recouvraient : l'agent qui a produit la fiche a choisi un bloc plausible pour un composant dont le bloc exact existait déjà sous un autre identifiant.

L'effet cumulé sur le corpus se lisait dans l'index des objets. Le référentiel comptait trois cent soixante-douze objets, dont sept objets métier qui n'apportaient aucune information propre et un composant dupliqué. Ces objets métier étaient par ailleurs mentionnés dans soixante-trois documents et CMP-09 dans trente-six, ce qui mesure l'ampleur de la reprise de texte que leur suppression impose.

## Décision

### La couche des objets métier est retirée du graphe

Les sept objets métier sont retirés du catalogue. Ils ne subsistent ni comme objets actifs, ni comme cibles de relation, ni comme mentions en prose. Le type `objet-metier` disparaît de l'ontologie OWL, des formes SHACL, du schéma de gouvernance et des scripts qui contrôlent le corpus. La rubrique « Business Object » de la matrice de couverture ArchiMate continue d'être satisfaite, mais par le seul type `objet-de-donnees`.

Ce retrait n'est pas une suppression d'information. Il est l'acceptation que l'information utile des objets métier était déjà portée ailleurs, et qu'il fallait choisir le support qui la porte le mieux.

### Le thème devient une propriété de l'objet de données

La charge utile des sept objets métier est reprise par une propriété `theme` portée par chaque objet de données. Le thème est une facette de classification, au même titre que le niveau de criticité : il ne crée pas d'arête dans le graphe et ne peut pas être la cible d'une relation. Il est déclaré dans le frontmatter de l'objet, ce qui le place au contact immédiat de l'objet qu'il qualifie.

Le vocabulaire des thèmes est contrôlé et externalisé. Le fichier `04_architecture-repository/00_metamodel/themes.yaml` porte, pour chaque thème, son slug, son libellé, sa description et les flux de valeur qu'il dessert. Un objet ne peut déclarer un thème qui ne figure pas dans ce vocabulaire. Ce fichier est le seul endroit où la liste des thèmes et leur dénomination sont écrits.

### La vue CAESN devient une vue générée par thème

Le document `00_caesn/04_data/objets.md`, qui présentait les sept objets métier, devient une vue dérivée. Son contenu est produit par le générateur d'enveloppes à partir des vingt-trois objets de données et du vocabulaire des thèmes. Il présente sept sections, une par thème, avec les objets du thème, leur niveau de criticité et leur système de référence. Les liens d'ancrage sont stables : l'ancre d'un thème est son slug, et les deux documents qui pointent vers ces ancres, la vue CAESN et le dictionnaire ARTSN, utilisent la même convention.

La table des matières du niveau 1 conserve ainsi son point d'entrée, mais elle ne peut plus diverger de la source : elle en est un produit.

### La trace des retraits est machine-lisible

Le fichier `04_architecture-repository/00_metamodel/object-migration.yaml` enregistre la trace de chaque retrait, sur le modèle déjà établi par `do-migration.yaml` pour les neuf fusions du catalogue des objets de données. Il distingue deux dispositions : `retired` pour un objet dont la charge utile est hébergée ailleurs, `merged` pour un objet fusionné dans un objet de même type. Pour les objets métier, il indique le thème qui les remplace et la liste exacte des objets de données que ce thème recouvre.

Cette trace est la seule source qui autorise la mention d'un identifiant retiré. Elle permet à un lecteur de reconstituer ce qui a disparu, et elle permet au validateur de refuser toute réapparition.

### CMP-09 est fusionné dans CMP-10

Le composant CMP-09 est fusionné dans CMP-10, qui survit sous son identifiant. Le composant fusionné porte une section « Fusion » qui nomme l'objet absorbé et renvoie à la trace de migration. Les paquets de travail réalisateurs sont réunis : CMP-10 déclare désormais `realized_by: ["WP-02", "WP-03"]`, et WP-02 est corrigé pour désigner le registre des terminologies.

Le rattachement erroné à ABB-GESTION-CONSENTEMENT disparaît avec CMP-09. CMP-10 conserve son rattachement exact à ABB-SERVICE-TERMINOLOGIE. La relation contextuelle des deux composants, qui déclarait CAP-09 « Gestion des ressources humaines en santé », est rectifiée en CAP-13 et CAP-14, les deux capacités que le registre des terminologies sert effectivement.

### Le validateur contrôle les trois nouveaux invariants

Trois contrôles sont ajoutés au validateur du référentiel, et sont exécutés à chaque intégration continue.

| Contrôle | Portée | Effet en cas de violation |
|---------|--------|---------------------------|
| Tout objet de données déclare exactement un `theme`, et ce thème figure dans le vocabulaire contrôlé | Objets de données | Le validateur échoue |
| Chaque thème du vocabulaire est porte par au moins un objet, et l'ensemble des objets d'un thème coïncide exactement avec la portée de l'objet métier retiré qui l'a créé | Objets de données et thèmes | Le validateur échoue |
| Aucun identifiant retiré ne subsiste comme objet actif, comme cible de relation, ni comme mention en prose hors des documents de décision et des traces de migration | Objets retirés | Le validateur échoue |

Le deuxième contrôle est le plus important. Il rend la propriété `theme` non décorative : un objet ne peut pas être rangé dans un thème sans que la trace de migration soit confrontée à la répartition. L'ajout d'un objet de données dans un thème et le déplacement d'un objet d'un thème vers un autre sont donc des opérations qui modifient l'état contrôlé du corpus, et non des réécritures locales.

La vérification de la répartition a été conduite sur le corpus avant toute modification. Le contenu actif des sept sections du dictionnaire des données fonctionnelles coïncide exactement, section par section, avec les vingt-trois objets répartis par la propriété `theme`. La seule divergence relevée entre les deux sources était l'absence de DO-32 dans la liste de BO-02, et le dictionnaire est conservé comme référence : DO-32 est rattaché au thème « Prestation & soins », ce que la trace consigne comme une correction et non comme une contradiction.

## Justification

La démarche HEAL impose de travailler avec les catégories du terrain plutôt qu'avec une nomenclature fermée. La présente décision en est l'application la plus directe dans le référentiel. Les sept objets métier n'étaient pas des catégories du terrain : ils en étaient la copie administrative, née du seul découpage du niveau 1 en sept sections. Le dictionnaire des données fonctionnelles était l'instrument de terrain : il classait les objets de données selon les périmètres que les professionnels de la donnée et les directions médicales reconnaissent, et sa structure servait déjà dans les chapitres ARTSN. Conserver la copie plutôt que la source revenait à préférer un document sans usage à un document qui en a un. La mesure confirme ce choix : sur les vingt-trois objets, vingt-deux étaient déjà rattachés par la couche métier, et le vingt-troisième était absent de la copie alors que le dictionnaire l'avait déjà classé.

Le HEAF impose une décomposition par valeurs et par couches, et son exigence de modularité se lit ici dans le refus de conserver deux chemins de vérité pour la même décomposition. La tentation aurait été de conserver les objets métier en lesalignant sur le dictionnaire, ou de les convertir en simples renvois vers les objets de données sans les retirer du graphe. C'eût été une sur-conception : la première produit deux états du corpus qui divergent à la première modification, la seconde produit des objets dont la seule fonction est d'exister pour être lus, c'est-à-dire des nœuds vides dans le graphe. La décision retire la couche et transfère sa charge utile vers la propriété qui peut la porter.

Le HEART impose la réutilisation d'artefacts et la génération de métadonnées depuis une source unique de vérité. La vue CAESN devient un artefact généré, le vocabulaire des thèmes devient une donnée à part entière, et la trace des retraits devient une source exploitable par les scripts. Aucun de ces trois éléments n'est une sur-conception : chacun remplace une rédaction manuelle par une production à partir de la source.

Trois points méritent d'être explicités, parce qu'ils conditionnent la robustesse de la décision.

D'abord, les flux de valeur portés par `themes.yaml` ne sont pas redondants avec le graphe. On pourrait croire que la couverture d'un thème par les flux de valeur se déduit de ses objets. La mesure contredit cette attente : sur les sept thèmes, six s'écartent de la dérivation, et seul le thème d'exploitation et de gestion coïncide. Cette information est donc déclarée dans le vocabulaire, et non reconstruite. Le choix est assumé : il vaut mieux une donnée déclarée et contrôlée qu'une dérivation fausse.

Ensuite, la fusion de CMP-09 dans CMP-10 conserve l'identifiant de CMP-10 plutôt que celui de CMP-09, alors que CMP-09 porte le titre plus explicite et que CMP-09 était réalisé par WP-02. Ce choix répond à un critère de correction : le rattachement de CMP-10 à ABB-SERVICE-TERMINOLOGIE est exact, celui de CMP-09 à ABB-GESTION-CONSENTEMENT est faux. Conserver l'identifiant dont la description est juste revient à préférer la correction à lacommodité.

Enfin, la suppression des mentions en prose est contrôlée, ce qui est plus strict qu'un simple remplacement de liens. Cinquante-six documents reprenaient les objets métier en toutes lettres, et trente-six reprenaient CMP-09. Un simple renvoi aurait laissé dans le corpus des phrases qui présentent des objets retirés comme des objets actifs, ce qui est la forme la plus insidieuse de résidu : elle ne casse aucun build et ne casse aucun lien, mais elle transmet une information périmée. La porte appliquée refuse la mention, tolère les documents de décision et les traces de migration, et tolère la section « Fusion » des composants issue d'une fusion.

## Conséquences

### Positives

- Le référentiel ne porte plus deux taxonomies du même domaine. Le corpus passe de trois cent soixante-douze à trois cent soixante-quatre objets, dont sept conteneurs d'information sans charge propre et un composant dupliqué qui disparaissent.
- La classification par thème devient vérifiable : le validateur refuse un objet sans thème, un thème hors vocabulaire, un thème vide et une répartition qui s'écarte de la trace de migration. La décomposition du domaine par les sept thèmes est donc une propriété contrôlée du corpus, et non une convention de lecture.
- La vue CAESN sur les objets de données ne peut plus diverger de la source, puisqu'elle en est un produit généré. Les deux documents qui pointent vers elle, la table des matières du niveau 1 et le dictionnaire du niveau 3, partagent la même convention d'ancrage.
- Le composant CMP-10 décrit un registre unique des terminologies, et son rattachement à un bloc d'architecture est exact. La contradiction que portait le doublon a disparu avec lui.
- La trace des huit retraits est lisible par un tiers et exploitable par les scripts : ce qui a disparu, ce qui l'a remplacé et pourquoi sont écrits dans un format que le validateur consomme.

### Négatives

- La charge de maintenance du corpus augmente sur un point précis : le vocabulaire des thèmes est une donnée à maintenir. L'ajout d'un objet de données dans un nouveau thème impose de modifier `themes.yaml` et `object-migration.yaml`, en plus de la fiche de l'objet. C'est le prix assumé de la traçabilité, et il est faible, car le regroupement d'objets par thème est une opération rare et l'opération elle-même est un acte de conception.
- La trace de migration s'allonge. Elle conserve des identifiants qui n'existent plus, ce qui introduit une forme de résidu dans un corpus qui vient précisément de les supprimer. Ce résidu est contraint et localisé : il vit dans deux fichiers de métamodèle et dans les documents de décision, et le validateur en refuse toute propagation.
- Le validateur refuse désormais des graphes qui étaient acceptés jusqu'ici, en particulier les mentions en prose d'identifiants retirés. Cette nouvelle porte produira des échecs de build sur des documents que le précédent état ne contrôlait pas. C'est la contrepartie d'une règle d'intégrité, et elle suppose de traiter ces échecs comme des défauts.
- La lecture du thème ne dispose d'aucune arête dans le graphe RDF. Un lecteur qui parcourt le graphe ne voit pas l'appartenance d'un objet à un thème sans lire le frontmatter ou le vocabulaire. Ce choix évite d'introduire une relation qui n'a pas de portée sémantique propre dans une architecture fondée sur les relations, mais il impose que les vues générées portent cette information.

## Alternatives considérées

| Alternative | Raison du refus |
|-------------|-----------------|
| Conserver les objets métier et les aligner sur le dictionnaire | Les deux listes resteraient deux listes. La première modification d'un objet de données ou d'une section du dictionnaire produirait une divergence que aucun contrôle ne détecterait. Le problème n'est pas l'écart constaté, il est l'existence de deux chemins de vérité. |
| Convertir les objets métier en nœuds de renvoi vers les objets de données | Un nœud dont le seul contenu est une liste de liens n'apporte rien et occupe une place dans l'index, dans le graphe RDF et dans la couverture ArchiMate. C'est la sur-conception que le HEAF et le HEART invitent à éviter. |
| Faire du thème une relation du graphe | Le thème ne désigne aucun objet cible : il est une facette, au même titre que le niveau de criticité. L'introduire comme relation aurait exigé de créer des objets « thème », donc de reconstruire la couche retirée sous une autre forme. |
| Supprimer les objets métier sans transfert de charge utile | Les descripteurs de thème et la couverture par les flux de valeur n'existent nulle part ailleurs. Les perdre aurait rendu le corpus moins précis, au prix d'un catalogue plus court. La réduction de redondance ne vaut que si aucune information n'est perdue. |
| Dériver la couverture en flux de valeur des objets du thème | La dérivation est fausse pour six des sept thèmes. Une information fausse introduite par commodité coûte plus cher qu'une information déclarée. |
| Fusionner CMP-09 dans CMP-10 en conservant l'identifiant CMP-09 | CMP-09 portait un rattachement à un bloc d'architecture qui n'était pas le sien. Conserver cet identifiant aurait conservé l'identifiant de l'objet le moins exact et aurait exigé de corriger son rattachement au lieu de supprimer l'erreur. |
| Supprimer CMP-09 sans fusion | Les deux composants partagent le même périmètre, le même chapitre normatif et les mêmes terminologies. Supprimer l'un reviendrait à désigner un porteur arbitraire du périmètre, alors que la fusion documente le recouvrement et unifie les paquets de travail.realized_by. |
| Corriger le rattachement de CMP-09 et conserver les deux composants | Le recouvrement était total sur six champs relationnels sur huit. Conserver deux fiches pour un seul composant entretient l'apparence d'une granularité que le contenu ne justifie pas. |

## Annexe : périmètre du lot

| Élément | Avant | Après |
|---------|-------|-------|
| Objets au catalogue | 372 | 364 |
| Objets métier | 7 | 0 |
| Composants dupliqués | 1 paire | 0 |
| Objets de données | 23 | 23, tous portant un thème |
| Thèmes de données | 7, non déclarés comme telle | 7, vocabulaire contrôlé |
| Types dans l'ontologie | `objet-de-donnees`, `objet-metier`, `terminologie` | `objet-de-donnees`, `terminologie` |
| Portes de validation | 0 sur le thème et le retrait | 3 |
| Fichiers de trace de migration | 1 | 2 |

## Références

- [Chaîne à quatre couches et règles d'intégrité](../../04_architecture-repository/00_metamodel/schema.md)
- [Vocabulaire contrôlé des thèmes de données](../../04_architecture-repository/00_metamodel/themes.yaml)
- [Trace des retraits d'objets](../../04_architecture-repository/00_metamodel/object-migration.yaml)
- [Thèmes de données](../../00_caesn/04_data/objets.md)
- [Dictionnaire de données fonctionnelles](../../02_artsn/03_objets-de-donnees/index.md)
- [ADR-0014 : Rationalisation du catalogue des objets de données](adr-0014-rationalisation-catalogue-donnees.md)
- [ADR-0015 : Deux emplois de l'accès aux données](adr-0015-semantique-acces-donnees.md)
- [ADR-0016 : La déclaration `fhir_resources` fait foi sur la projection FHIR](adr-0016-projection-fhir-source-de-verite.md)
- [CMP-10 : Registre des terminologies](../../04_architecture-repository/05_reference-library/building-blocks/sbb/cmp-10.md)
- [ART-4 : Référentiels de métadonnées de gestion](../../04_architecture-repository/05_reference-library/patterns/artsn-rules/art-4.md)
