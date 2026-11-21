---
title: "ADR-0018 : Réorganisation de l'arborescence du référentiel d'architecture en couches alignées sur le cycle de vie"
id: adr-0018
domain: 06_decisions
version: "1.0.0"
status: candidate
date: 2026-11-21
owner: DEPSI
tags: ["adr", "metamodele", "arborescence", "referentiel", "gouvernance"]
related: ["ADR-0017", "CAP-13", "CAP-14", "ART-4", "DO-06"]
---

# ADR-0018 : Réorganisation de l'arborescence du référentiel d'architecture en couches alignées sur le cycle de vie

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ○ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ○ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle.

- **Statut** : proposé
- **Date** : 2026-11-21
- **Groupe concerné** : DEPSI, CNASN

## Contexte

Le référentiel d'architecture `04_architecture-repository/` a été constitué par accumulation, et son arborescence ne correspond plus ni à la hiérarchie documentaire du cadre, ni aux phases du cycle de vie de l'architecture de référence qu'il est censé outiller. Cette inadéquation ne se voyait pas sur le contenu des fiches, qui est de qualité, mais sur la seule organisation des dossiers, que la règle « le nom reflète la localisation » du référentiel impose de tenir à jour.

Le premier défaut est un **décalage de numérotation**. Les exigences occupaient le préfixe `03_requirements/`, alors qu'elles fondent l'architecture et ne la dépendent pas : dans la logique du cycle de vie, le référentiel des exigences est la première chose qui s'écrit, avant les principes, les capacités et les artefacts techniques. Le préfixe `03_` plaçait donc la source la plus amont du référentiel au troisième rang de lecture, et laissait croire que les exigences dépendaient des exigences de niveau inférieur. Les profils d'interopérabilité, qui sont des artefacts de la bibliothèque de référence, partageaient le même défaut sous une forme plus grave : ils résidaient dans `05_building-blocks/sbb/legacy-profiles/`, un emplacement dont le nom ne désignait pas leur nature.

Le deuxième défaut est l'**accumulation de qualificatifs de transition**. Trois dossiers portaient le préfixe `legacy-` : `legacy-components/`, `legacy-profiles/` et `legacy-services/`. Ces qualificatifs décrivaient un état de migration temporaire, jamais levé depuis. Un lecteur du référentiel rencontrait ainsi, au sein d'un même niveau, des dossiers sans qualificatif et des dossiers qualification, sans que rien n'indique la raison de la différence ni la durée de vie prévue de ces derniers. La règle de nommage du référentiel exige des noms courts, en kebab-case, désignant la nature du contenu ; les trois dossiers y contrevenaient, et leur persistance déplaçait vers l'arborescence la charge de dire ce que les noms auraient dû dire.

Le troisième défaut est l'**absence de bibliothèque de référence**. Le référentiel contenait des patrons, des fondations, des blocs d'architecture, des blocs de solution, des profils, des terminologies et des données de référence, mais aucun dossier ne regroupait ces artefacts sous une notion unique. La phase ADM de construction des artefacts n'avait pas de lieu dans l'arbre. C'est ce qui explique la promiscuité des noms : faute de catégorie de destination, les artefacts ont été rangés dans des dossiers créés au fil de l'eau, dont les trois dossiers `legacy-` sont la trace la plus tardive.

Le quatrième défaut est l'**ambiguïté des objets non couverts par la table de migration**. Trois ensembles d'objets n'étaient pas mentionnés par la règle de déplacement envisagée : les sept terminologies `TERM-*` et les deux données de référence `RD-*`, d'une part, les cinq services transverses `SRV-02` à `SRV-06`, d'autre part. La règle « le nom reflète la localisation » étant une règle de cohérence stricte, laisser ces trois ensembles en suspens aurait produit une arborescence où une partie des objets obéit à la règle et l'autre partie non. C'est cette ambiguïté, et non une préférence esthétique, qui a rendu la décision nécessaire.

La mesure de l'état avant correction établit l'ampleur du chantier. Le référentiel comptait trois cent soixante-seize fichiers Markdown, répartis sur neuf préfixes de premier niveau et quarante-six dossiers, dont trois portent un qualificatif de transition. Le corpus de l'ensemble du dépôt en compte huit cent quatorze. Les liens relatifs inter-fichiers, dont la validité est contrôlée à chaque intégration continue, se comptent par milliers. L'index des objets référence trois cent soixante-quatre objets, dont aucun ne change de nature dans la présente décision : ce sont les chemins qui changent, non le graphe.

## Décision

### L'arborescence du référentiel est réorganisée en quatre couches

Le référentiel adopte l'arborescence suivante, dont les préfixes suivent l'ordre de lecture du cycle de vie de l'architecture.

| Couche | Préfixe | Contenu | Fichiers |
|--------|---------|---------|----------|
| Fondations | `00_metamodel/`, `01_partitions/`, `02_requirements/` | méta-schéma, partitions, exigences | 1, 12, 20 |
| Architecture d'entreprise | `03_business-architecture/` | motivation, stratégie, métier | 174 |
| Architecture de données | `04_data-architecture/` | objets de données | 23 |
| Bibliothèque de référence | `05_reference-library/` | patrons, blocs de construction, standards de base | 111 |
| Gouvernance et trajectoire | `06_governance/`, `07_migration/`, `08_views/` | contrats, conformité, preuves, écarts, paquets, vues | 37 |

Les trois derniers préfixes conservent leur numérotation d'origine. Cette invariance n'est pas un détail de nomenclature : elle borne le périmètre du changement et évite que la révision ne se propage aux couches qui n'ont pas besoin d'être renumérotées.

### La table de migration est intégralement appliquée

Le déplacement est défini par une table de correspondance entre chemins anciens et chemins nouveaux, dont la règle de résolution est que **le préfixe le plus long l'emporte**. Cette règle est nécessaire parce que certains chemins anciens sont des préfixes d'autres chemins anciens : `05_building-blocks/abb/legacy-components/` est un sous-ensemble de `05_building-blocks/abb/`, qui est lui-même un sous-ensemble de `05_building-blocks/`.

| Chemin ancien | Chemin nouveau |
|---------------|----------------|
| `03_requirements/` | `02_requirements/` |
| `02_architecture-elements/motivation/` | `03_business-architecture/motivation/` |
| `02_architecture-elements/strategy/` | `03_business-architecture/strategy/` |
| `02_architecture-elements/business/` | `03_business-architecture/business/` |
| `02_architecture-elements/data/data-objects/` | `04_data-architecture/data-objects/` |
| `04_patterns/` | `05_reference-library/patterns/` |
| `05_building-blocks/abb/abb-*.md` | `05_reference-library/building-blocks/abb/abb-*.md` |
| `05_building-blocks/abb/legacy-components/cmp-*.md` | `05_reference-library/building-blocks/sbb/cmp-*.md` |
| `05_building-blocks/abb/legacy-profiles/pt-*.md` | `05_reference-library/standards-base/profiles/pt-*.md` |
| `05_building-blocks/abb/legacy-services/srv-*.md` | `03_business-architecture/business/business-services/srv-*.md` |
| `02_architecture-elements/data/terminologies/` | `05_reference-library/standards-base/code-systems/` |
| `02_architecture-elements/data/reference-data/` | `05_reference-library/standards-base/code-systems/` |
| `06_governance/`, `07_migration/`, `08_views/` | inchangés |

Les déplacements sont exécutés par `git mv`, de sorte que l'historique de chaque fichier est conservé et que chaque renommage est traçable par l'outil de versionnement.

### Les liens et les mentions de chemin sont réécrits mécaniquement

Le déplacement d'un fichier déplace ses liens relatifs, et le déplacement de la cible d'un lien déplace ce lien. La réécriture est donc exécutée en deux temps : la cible est résolue depuis l'emplacement ancien du document qui porte le lien, projetée vers son nouvel emplacement, puis le chemin relatif est recalculé depuis l'emplacement nouveau du document. Les documents qui ne sont pas déplacés mais dont une cible est déplacée subissent la même opération, la résolution relative étant alors inchangée.

Cette précision est nécessaire, car les deux déplacements ne s'annulent pas. Un document déplacé vers un niveau plus profond voit ses liens vers des cibles demeurées en place devenir faux, si leur préfixe `../` n'est pas recalculé. C'est la principale source d'erreur d'une telle opération, et la validation des liens relatifs, qui contrôle chaque cible du corpus, est l'instrument qui la détecte.

Les mentions de chemin en prose et les attributs `source=` des blocs générés sont réécrits selon la même table. Les chemins nus, c'est-à-dire les fragments de chemin sans leur préfixe de dépôt, ne sont réécrits qu'à l'intérieur du référentiel : en dehors, la mention `04_patterns` désigne le dossier des chapitres de l'ARTSN, et non l'ancien dossier du référentiel.

### Le champ `domain:` est aligné sur le nouveau dossier parent

La règle « le nom reflète la localisation » impose que le champ `domain:` de chaque fiche vaille le nom de son dossier parent immédiat, préfixe numérique compris. La vérification préalable a établi que les trois cent soixante-seize fichiers du référentiel respectaient cette règle sans exception, ce qui autorise un alignement mécanique : le champ prend la valeur du nouveau dossier parent, sans arbitrage ni exception.

### Les trois ensembles non couverts sont tranchés explicitement

Les terminologies et les données de référence rejoignent la bibliothèque de référence, dans un dossier `standards-base/code-systems/`. Ce choix est cohérent avec la nature de ces objets : ce sont des artefacts de la bibliothèque de référence, et non des données du modèle d'information de l'entreprise, dont la couche `04_data-architecture/` ne contient que les objets de données proprement dits.

Les services transverses `SRV-02` à `SRV-06` rejoignent `SRV-01` dans `03_business-architecture/business/business-services/`. La table de migration envisagée plaçait initialement ces services dans la bibliothèque de référence, par extension de la règle qui déplaçait les composants hérités. Cette extension a été écartée : un service transversal est un port d'entrée dans le métier, au même titre que les processus et les acteurs, et sa nature ne change pas selon l'ancienneté de sa fiche. Les six services forment désormais un ensemble homogène de six objets.

Un dossier `standards-base/external-standards/` est créé et documenté, mais reste vide. Il réserve la place des normes publiées par des tiers, que le référentiel cité sans les posséder, là où la bibliothèque de référence distingue les artefacts qu'il produit, les profils d'implémentation, des normes qu'il adopte. Le dossier est documenté par une fiche qui en fixe les critères d'admission, et le référentiel y gagne une localisation stable pour un contenu qui n'existe pas encore.

### Les scripts et les artefacts générés sont alignés

Dix scripts portent des chemins de repository codés en dur ou des listes d'exclusion ; ils sont mis à jour. Six concernaient la localisation des sources de compilation : le compilateur JSON Schema, le compilateur FHIR, le compilateur ODA, le compilateur OpenAPI et les deux scripts d'audit du référentiel. Quatre concernaient l'exclusion des documents non-objets du graphe et de l'index : le générateur d'enveloppes, le générateur d'index, le compilateur RDF et le validateur du référentiel. Les deux fiches de réservation créées dans les dossiers de la bibliothèque de référence sont déclarées dans ces quatre listes d'exclusion, au même titre que les documents de métamodèle : ce sont des documents de navigation, non des objets d'architecture.

Les artefacts générés sont ensuite régénérés : enveloppes, index des objets, schémas JSON Schema, spécifications OpenAPI, ressources FHIR, graphe RDF et artefact Mintlify. Le résultat est vérifié par les treize étapes de l'intégration continue, qui doivent toutes repasser au vert.

## Justification

La démarche HEAL impose de travailler avec les catégories du terrain plutôt qu'avec une nomenclature fermée. La présente décision applique cette exigence à l'architecture elle-même : l'arborescence du référentiel est une nomenclature fermée, construite par strates successives, dont les catégories ont nommé des états de chantier plutôt que des natures de contenu. Les trois dossiers `legacy-` en sont la preuve la plus lisible. Un répertoire d'architecture destiné à des équipes distribuées, à des partenaires techniques et à des évaluateurs externes ne peut pas présenter des noms de chantier comme des noms de structure, sous peine d'imposer à chaque lecteur une interprétation que le nom devrait porter.

Le HEAF impose une décomposition par couches et par valeurs, et son exigence de modularité se lit ici dans la séparation des trois couches que la décision établit. La couche `03_business-architecture/` porte ce qui décrit l'entreprise : ses parties prenantes, ses valeurs, ses principes, ses flux, ses capacités, ses processus, ses acteurs, ses rôles et ses localisations. La couche `04_data-architecture/` porte le modèle d'information, c'est-à-dire les objets de données du niveau 3. La couche `05_reference-library/` porte les artefacts réutilisables, c'est-à-dire les patrons, les blocs de construction et les standards de base. Cette décomposition n'est pas une invention du référentiel : elle reprend la structure du référentiel TOGAF, où l'architecture de référence est précisément ce qui est réutilisable, et où le domaine, la donnée et les artefacts occupent des registres distincts.

Le HEART impose la réutilisation d'artefacts et la génération de métadonnées depuis une source unique de vérité. La décision applique ces deux exigences à la structure du dépôt lui-même. La table de migration est écrite une fois, en un seul endroit, et appliquée par un outil unique ; les liens, les mentions de prose et les attributs `source=` des blocs générés en découlent mécaniquement, et le corpus ne peut pas diverger de la table sans que la validation des liens le signale. De même, le regroupement des terminologies et des données de référence dans un dossier unique de bibliothèque de référence rend leur gouvernance lisible : elles partagent un dossier, donc un statut, donc un cycle de revue.

Deux points méritent d'être explicités, parce qu'ils conditionnent la robustesse de la décision.

D'abord, le maintien des numérotations `06`, `07` et `08` aurait pu être perçu comme une incohérence, les trois couches conservées portant des préfixes qui ne correspondent pas à leur rang dans la nouvelle décomposition. Il n'y a pas d'incohérence : ces trois couches sont inchangées, et leur rang dans l'ordre de lecture n'a pas bougé. Le principe retenu est que le numéro détermine l'ordre de lecture, et que seule une modification de contenu justifie de modifier un numéro. Cette discipline évite que la présente révision ne déclenche, en réaction, une révision des trois couches qui n'en ont pas besoin.

Ensuite, la décision ne crée aucun objet et ne supprime aucun objet. Les trois cent soixante-quatre objets de l'index sont les mêmes avant et après, et le graphe de relations est inchangé. Ce qui change, c'est l'adresse de chaque objet et le regroupement des dossiers qui les contiennent. C'est ce qui rend l'opération réversible en cas de contestation : le diff produit par la migration est un diff de chemins, et aucun contenu d'architecture n'a été touché. La seule exception est le champ `domain:`, aligné mécaniquement sur la règle de nommage, et les trois lignes de la table des types du méta-schéma, corrigées à la main parce que le remplacement automatique y avait produit des répertoires inexistants.

## Conséquences

### Positives

- L'arborescence du référentiel s'aligne sur le cycle de vie de l'architecture : les exigences sont lues avant les principes, les principes avant les capacités, les capacités avant les artefacts. Un lecteur qui parcourt les préfixes dans l'ordre comprend la dépendance entre les couches sans consulter la documentation.
- Les trois qualificatifs de transition disparaissent du corpus. Aucun dossier du référentiel ne porte plus de mention d'état de chantier, et la règle de nommage tient désormais sans exception.
- La bibliothèque de référence devient une couche identifiable, ce qui donne un point d'entrée unique aux artefacts réutilisables et un lieu naturel pour la documentation de leur gouvernance.
- Les liens relatifs du corpus sont intégralement validés après la migration : le contrôle porte sur six mille cinq cent soixante-dix-sept liens et n'en déclare aucun cassé. La règle « le nom reflète la localisation » est ainsi vérifiée par l'outil, et non par l'attention du rédacteur.
- Les scripts qui portent des chemins codés en dur sont alignés sur la nouvelle structure, et les artefacts générés sont vérifiés idempotents par l'intégration continue.

### Négatives

- Le diff de la migration est volumineux : trois cent vingt-six fichiers déplacés, quatre mille deux cent soixante-quatre liens et mille quatre cent quarante-huit mentions de chemin en prose réécrits, pour une modification qui ne change aucun contenu d'architecture. La relecture du diff demande de la discipline, car le volume masque la petitesse du changement de fond.
- Les liens historiques qui pointent vers des chemins du référentiel depuis l'extérieur du dépôt, par exemple dans des dépôts tiers ou dans des correspondances antérieures à la révision, ne sont pas mis à jour : la révision change les adresses publiques du référentiel sans dispositif de redirecteur.
- Trois documents de septembre 2026 conservent l'arborescence de leur rédaction, parce qu'ils enregistrent une décision prise à cette date et non l'état courant du dépôt : la spécification de conception, le plan d'exécution et le rapport de tâche de la refonte du référentiel. Cette conservation est délibérée, mais elle laisse dans le dépôt trois documents qui décrivent une structure qui n'existe plus.
- La règle de résolution « le préfixe le plus long l'emporte » doit être comprise par toute personne qui reprendra la table de migration. Une table de correspondance mal lue produit des déplacements erronés, et c'est la raison pour laquelle la table a été outillée plutôt qu'appliquée à la main.

## Alternatives considérées

| Alternative | Raison du refus |
|-------------|-----------------|
| Ne rien changer et se contenter de corriger les trois dossiers `legacy-` | La correction des qualificatifs aurait traité le symptôme le plus visible en laissant les trois défauts de fond : le décalage de numérotation des exigences, l'absence de bibliothèque de référence et la dispersion des artefacts. Le corpus serait plus lisible à la surface et aussi incohérent en profondeur. |
| Renuméroter intégralement les neuf couches, y compris `06_governance`, `07_migration` et `08_views` | La renumérotation aurait propagé la modification à trois couches qui n'en ont pas besoin, pour un gain de régularité formelle. Le coût aurait été un diff sans information : trois cent soixante-dix fichiers déplacés pour modifier un numéro que rien ne définit. |
| Répartir les artefacts entre `05_reference-library/` et un dossier `06_standards/` distinct | La séparation entre ce que le projet produit et ce qu'il adopte est pertinente, mais elle ne justifie pas un dossier de premier niveau : les standards adoptés sont une sous-catégorie de la bibliothèque de référence, au même titre que les profils d'implémentation. Un dossier de premier niveau aurait créé une cinquième couche dont le contenu tient en un sous-dossier. |
| Placer les terminologies et les données de référence dans `04_data-architecture/` | Le choix est défendable, car les terminologies contraignent les objets de données. Il confond cependant la donnée de l'entreprise, qui est le modèle d'information du niveau 3, avec les vocabulaires externes qu'elle mobilise. Les deux notions sont de niveaux différents : l'une est produite par le projet, l'autre est adoptée. |
| Placer les services transverses `SRV-02` à `SRV-06` dans la bibliothèque de référence | L'extension de la règle de déplacement des composants hérités aurait produit un dossier de services dans la couche des artefacts, à côté de composants et de profils. Un service transversal est un port d'entrée dans le métier : sa nature ne change pas avec l'ancienneté de sa fiche. |
| Réécrire les liens pointant vers le référentiel depuis des correspondances externes par un mécanisme de redirecteur | Le référentiel est un dépôt documentaire versionné, non un service. Un redirecteur supposerait une infrastructure de publication qui n'existe pas. La perte de compatibilité des adresses externes est le prix d'une réorganisation de dépôt, et elle est bornée par le corpus lui-même. |

## Annexe : périmètre de la réorganisation

| Élément | Avant | Après |
|---------|-------|-------|
| Fichiers Markdown du référentiel | 376 | 378, dont 2 fiches de réservation créées |
| Objets à l'index | 364 | 364, inchangés |
| Préfixes de premier niveau du référentiel | 9 | 9, dont quatre renommés ou regroupés |
| Dossiers portant un qualificatif `legacy-` | 3 | 0 |
| Fichiers déplacés | 0 | 326, par `git mv` |
| Liens relatifs réécrits | 0 | 4 264 |
| Mentions de chemin en prose réécrites | 0 | 1 448 |
| Champs `domain:` alignés | 0 | 326 |
| Scripts mis à jour | 0 | 10 |
| Liens relatifs cassés après migration | 0 | 0, sur 6 577 liens contrôlés |
| Fichiers du corpus citant un chemin de l'ancienne arborescence | 348 | 5, dont le présent ADR, son entrée dans le journal de modifications et les trois documents de septembre 2026 |
| Étapes de l'intégration continue au vert | 13 sur 13 | 13 sur 13 |

## Références

- [Schéma du référentiel](../../04_architecture-repository/00_metamodel/schema.md)
- [Guide de conception ODA](../../02_artsn/09_annexes/j-oda-conception-guide.md)
- [Guide de contribution](../../CONTRIBUTING.md)
- [Bases de codes : terminologies et données de référence](../../04_architecture-repository/05_reference-library/standards-base/code-systems/README.md)
- [Standards externes : emplacement réservé](../../04_architecture-repository/05_reference-library/standards-base/external-standards/README.md)
- [ADR-0017 : Retrait des objets métier au profit des thèmes de données](adr-0017-reduction-redondance-objets-metier-composants.md)
