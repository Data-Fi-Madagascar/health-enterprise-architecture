---

title: "Journal des modifications des ADR"
id: adr-change-log
domain: 06_decisions
version: "1.0.0"
status: active
date: 2026-07-01
owner: DEPSI
tags: ["adr", "changelog", "suivi"]
---

# Journal des modifications des ADR

## A propos de ce document

Ce document suit l'historique des modifications apportees aux Architecture Decision Records (ADR) du cadre HEA. Il permet de :

- **Traquer les evolutions** : Suivre les changements de statut, les mises a jour et les remplacements d'ADR
- **Maintenir la tracabilite** : Conserver un historique complet des decisions architecturales
- **Faciliter l'audit** : Fournir une vue d'ensemble des decisions et de leur cycle de vie

## Format du journal

Chaque entree suit le format :

```markdown
### [Date] - [Type de modification] - [ADR concerne]
- **Auteur** : [Nom/Role]
- **Description** : [Description detaillee du changement]
- **Justification** : [Raison du changement, le cas echeant]
- **Liens** : [References vers d'autres documents ou ADR]
- **Impact** : [Consequences sur le systeme ou les autres ADR]
```

## Types de modifications

| Type | Description | Exemple |
|------|-------------|---------|
| **Creation** | Nouvel ADR ajoute | ADR-XXXX : Nouvelle decision sur X |
| **Acceptation** | ADR passe en statut "accepte" | ADR-0001 : Valide par le comite |
| **Application** | ADR passe en statut "applique" | ADR-0002 : Deployment termine |
| **Modification** | Mise a jour du contenu | ADR-0003 : Ajout de precisions |
| **Remplacement** | ADR remplace par une nouvelle decision | ADR-0004 remplace par ADR-XXXX |
| **Depreciation** | ADR marque comme deprecie | ADR-0005 : Plus pertinent |
| **Retrait** | ADR retire du registre | ADR-0006 : Decision abandonnee |

## Historique des modifications

### [2026-11-21] - Creation - ADR-0017
- **Auteur** : Equipes DEPSI
- **Description** : Creation de la decision qui retire la couche des objets metier du graphe et fusionne le composant CMP-09 dans CMP-10. Les sept objets metier BO-01 a BO-07 sont retires ; leur charge utile est reprise par une propriete `theme` portee par les vingt-trois objets de donnees. Le vocabulaire des sept themes est externalise dans `04_architecture-repository/00_metamodel/themes.yaml`, et la vue `00_caesn/04_data/objets.md` devient une vue generee par theme. Le type `objet-metier` disparait de l'ontologie, des formes SHACL, du schema de gouvernance et des scripts. La trace des huit retraits est enregistree dans `04_architecture-repository/00_metamodel/object-migration.yaml`. CMP-09, qui portait la meme signature relationnelle que CMP-10 sur six champs relationnels sur huit, est fusionne dans CMP-10, qui conserve le rattachement exact a ABB-SERVICE-TERMINOLOGIE ; les paquets de travail realisateurs sont reunis en `realized_by: ["WP-02", "WP-03"]`.
- **Statut initial** : `candidate`
- **Justification** : La mesure avant correction relevait deux taxonomies paralleles du meme domaine, dont une copie de l'autre qui s'ecartait de la source sur DO-32, cinquante-six aretes de relation sans charge propre, et un composant duplique dont le rattachement a un bloc d'architecture etait faux.
- **Liens** : [ADR-0017](adr-0017-reduction-redondance-objets-metier-composants.md), [Vocabulaire des themes](../../04_architecture-repository/00_metamodel/themes.yaml), [Trace des retraits](../../04_architecture-repository/00_metamodel/object-migration.yaml), [Themes de donnees](../../00_caesn/04_data/objets.md), [Dictionnaire des donnees fonctionnelles](../../02_artsn/03_objets-de-donnees/index.md), [CMP-10](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-10.md), [Chaine a quatre couches](../../04_architecture-repository/00_metamodel/schema.md)
- **Impact** : Le validateur refuse desormais un objet de donnees sans theme ou portant un theme hors vocabulaire, un theme vide ou une repartition qui s'ecarte de la trace de migration, et toute mention en prose d'un identifiant retire hors des documents de decision et des traces de migration. Le referentiel passe de trois cent soixante-douze a trois cent soixante-quatre objets.

### [2026-11-21] - Creation - ADR-0016
- **Auteur** : Equipes DEPSI
- **Description** : Creation de la decision qui rend la declaration `fhir_resources` de chaque objet de donnees source unique de verite pour la projection FHIR. La table interne de correspondance entre libelles francais et ressources FHIR est supprimee : une StructureDefinition est produite par ressource declaree, de type et d'identifiant conformes a la declaration. Le compilateur embarque le vocabulaire des cent quarante-neuf ressources du paquet FHIR R4 et leurs niveaux de maturite FMM, refuse toute ressource absente de R4 ou de maturite nulle, purge le repertoire de sortie des artefacts perimes, et soumet la declaration et sa projection a une porte de conformite executee dans le pipeline d'integration continue. Quatre declarations non echangeables en R4 sont rectifiees : DO-11 passe de `MedicationKnowledge` a `Medication`, DO-12 de `InventoryItem` a `Medication` et `SupplyDelivery`, DO-16 de `Claim` et `Invoice` a `Claim` et `ClaimResponse`, DO-31 de `Certificate` a `Endpoint`, `Provenance` et `Binary`. Les trois documents qui encadraient ces usages sont rectifies en consequence : la norme STD-0009, le profil PT-17 et le cas d'usage de chaine d'approvisionnement.
- **Statut initial** : `candidate`
- **Justification** : La mesure avant correction relevait vingt et un des vingt-trois objets divergents entre leur declaration et le type compile, seize d'entre eux retombant sur le repli generique `Basic`, neuf artefacts perimes d'objets retires du catalogue, et quatre declarations non echangeables en R4. Le compilateur ne produisait pas l'image du corpus mais l'historique de ses executions.
- **Liens** : [ADR-0016](adr-0016-projection-fhir-source-de-verite.md), [DO-01](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-01.md), [DO-12](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-12.md), [DO-31](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-31.md), [PT-17](../../03_ptisn/03_profils/pt-17-logistique-lmis.md), [STD-0009](../05_standards/std-0009-echange-donnees-logistiques-lmis.md), [Chaine a quatre couches](../../04_architecture-repository/00_metamodel/schema.md)
- **Impact** : Le compilateur echoue desormais sur un objet de donnees qui ne declare aucune ressource, sur une ressource absente du paquet R4 ou de maturite FMM nulle, sur une ressource declaree deux fois, sur un bloc `fhir:` dont la base n'est pas declaree, sur une ressource declaree sans artefact, et sur un artefact sans declaration correspondante. La correction de DO-12 modifie la lecture du stock, qui devient le solde des mouvements `SupplyDelivery` et non une ressource d'ecriture : le changement est cassant pour les consommateurs de la specification PT-17.

### [2026-11-21] - Creation - ADR-0015
- **Auteur** : Equipes DEPSI
- **Description** : Creation de la decision qui distingue les deux emplois de la relation `accesses` : le processus qui manipule la donnee et le composant qui la detient. Les cinq aretes de processus qui n'etaient adossees a aucun composant mobilise sont completees par la chaine `PRC` vers `CMP` vers `DO`, et les quatre declarations de `system_of_record` dont le systeme vise ne declarait aucun acces le sont devenues : le bloc ABB-REFERENTIEL-STRUCTURES-SERVICES pour DO-23 et DO-26, les autorites CMP-35 et CMP-36 pour DO-31. La decision ajoute trois controles au validateur : adossement d'une arete `PRC` vers `DO` a un composant mobilise qui porte l'objet, declaration d'acces du systeme de reference, symetrie de `uses` et `applies_to` pour le couple PRC/CMP.
- **Statut initial** : `candidate`
- **Justification** : La mesure avant correction relevait cinq aretes de processus sans support et quatre attributions de version faisant foi sans fondement dans le graphe. Le metamodele affirmait un acces unique et ne retenait pas l'enonce processus, ce que le corpus contredisait.
- **Liens** : [ADR-0015](adr-0015-semantique-acces-donnees.md), [CMP-13](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-13.md), [CMP-35](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-35.md), [DO-31](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-31.md), [Chaine a quatre couches](../../04_architecture-repository/00_metamodel/schema.md)
- **Impact** : Le validateur refuse desormais une manipulation de donnee par un processus sans composant porteur, un systeme de reference qui n'accede pas a l'objet dont il detient la version faisant foi, et une asymetrie entre `uses` et `applies_to`. Le metamodele nomme les deux emplois de l'acces aux donnees et expose l'etat mesure du corpus.

### [2026-11-21] - Creation - ADR-0014
- **Auteur** : Equipes DEPSI
- **Description** : Creation de la decision qui rationnalise le catalogue des objets de donnees. Le catalogue passe de trente et un a vingt-trois entrees : huit fusions, un retrait avec hebergement par CMP-01 pour le tableau de bord, et la creation de DO-32 pour l'examen et son resultat de laboratoire. La decision ajoute les proprietes `tier` et `system_of_record` a chaque objet de donnees, la propriete `absorbs` pour tracer les fusions, et le fichier `04_architecture-repository/00_metamodel/do-migration.yaml` comme source unique de la trace. La renumerotation proposee par le catalogue recu et quatre fusions supplementaires sont refusees.
- **Statut initial** : `candidate`
- **Justification** : La mesure avant correction relevait cinq familles de recouvrement dans un catalogue constitue par additions successives. Retirer une entree sans trace aurait casse deux cent dix-huit relations et deux cent soixante-quatorze liens sans laisser au lecteur de moyen de savoir ce que l'identifiant disparu designait.
- **Liens** : [ADR-0014](adr-0014-rationalisation-catalogue-donnees.md), [DO-01](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-01.md), [DO-32](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-32.md), [CMP-01](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-01.md), [Trace de migration](../../04_architecture-repository/00_metamodel/do-migration.yaml), [Chaine a quatre couches](../../04_architecture-repository/00_metamodel/schema.md)
- **Impact** : Le validateur refuse desormais un objet de donnees sans tier ou sans system_of_record, une fusion non tracee, et toute relation pointant vers un identifiant retire. Les neuf schemas de payload des objets retires sont supprimes : le changement est cassant pour leurs consommateurs.

### [2026-11-21] - Creation - ADR-0013
- **Auteur** : Equipes DEPSI
- **Description** : Creation de la decision qui enregistre la taxonomie des fonctions de domaine transmise par le Ministere comme reference de couverture, sans creation de couche ni de type d'objet. La decision arbitre trois fonctions par absorption dans des capacites existantes et en laisse cinq a l'arbitrage ministeriel. Elle etablit egalement la regle d'adossement : tout objet de donnees declare les capacites qu'il sert via `maps_to`, et toute capacite declaree doit etre realisee par au moins un processus qui manipule l'objet.
- **Statut initial** : `candidate`
- **Justification** : Rendre la chaine descendant de la capacite vers la donnee verifiable par l'outil. La mesure sur le corpus avant correction relevait vingt-cinq attributions contradictoires reparties sur dix-sept objets de donnees.
- **Liens** : [ADR-0013](adr-0013-cadrage-fonctions-domaine.md), [CAP-01](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-01.md), [CAP-07](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-07.md), [CAP-10](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-10.md), [CAP-13](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-13.md), [Chaine a quatre couches](../../04_architecture-repository/00_metamodel/schema.md)
- **Impact** : Le validateur du referentiel refuse desormais un objet de donnees sans attribution de capacite, une attribution visant autre chose qu'une capacite, et une capacite declaree non realisee par un processus accessor. Les cinq arbitrages ministeriels restent ouverts.

### [2026-09-24] - Creation - ADR-0011
- **Auteur** : Equipes DEPSI
- **Description** : Creation de la decision qui institue un service distinct d'eligibilite et de couverture, separe des responsabilites de resolution d'identite et de consentement. Les echanges de couverture et de verification des droits utilisent HL7 FHIR R4.
- **Statut initial** : `candidate`
- **Justification** : Rendre explicite et auditable la decision de droits applicable a une prestation, un programme et une date.
- **Liens** : [ADR-0011](adr-0011-eligibilite-couverture.md), [CAP-07](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-07.md), [ABB-ELIGIBILITE-COUVERTURE](../../04_architecture-repository/05_building-blocks/abb/abb-eligibilite-couverture.md), [PT-20](../../04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-20.md), [CMP-12](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-12.md)
- **Impact** : Etablit la chaine CAP-07 vers ABB-ELIGIBILITE-COUVERTURE, PT-20 et CMP-12. Aucun produit ni fournisseur n'est choisi ; les regles metier de couverture restent a definir par les programmes responsables.

### [2026-09-24] - Creation - ADR-0012
- **Auteur** : Equipes DEPSI
- **Description** : Creation de la decision qui conserve le rattachement de One Health a VS-02 pour la surveillance et la riposte via CAP-18, ainsi qu'a VS-04 pour la gouvernance intersectorielle, le pilotage et la redevabilite via CAP-08.
- **Statut initial** : `candidate`
- **Justification** : Completer les deux chaines de valeur de la partition sans creer un flux de valeur One Health supplementaire.
- **Liens** : [ADR-0012](adr-0012-one-health-pilotage.md), [PART-ONE-HEALTH](../../04_architecture-repository/01_partitions/sectorielles/part-one-health.md), [ABB-ECHANGE-MEDIATION](../../04_architecture-repository/05_building-blocks/abb/abb-echange-mediation.md), [ABB-EXPOSITION-DONNEES-ANALYTIQUES](../../04_architecture-repository/05_building-blocks/abb/abb-exposition-donnees-analytiques.md), [PT-15](../../04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-15.md), [WP-07](../../04_architecture-repository/07_migration/work-packages/wp-07.md)
- **Impact** : Reutilise les blocs d'echange et d'exposition analytique, preserve leur portee transverse et rend les chaines One Health derivables dans la vue de tracabilite. Le validateur controle une capabilite commune pour chaque flux declare.

### [2026-07-01] - Creation - ADR-0001 a ADR-0010
- **Auteur** : Equipes DEPSI
- **Description** : Creation initiale des 10 premiers ADR couvrant les decisions architecturales fondamentales du CNISN
- **ADR concernes** : ADR-0001 (X-Road), ADR-0002 (mADX), ADR-0003 (FHIR), ADR-0004 (Identite), ADR-0005 (Consentement), ADR-0006 (INP), ADR-0007 (GDHCN), ADR-0008 (ATNA), ADR-0009 (Terminologie), ADR-0010 (Cadre legal)
- **Statut initial** : Tous en statut "accepte" (accepted)
- **Justification** : Etablir les fondations de l'architecture d'interoperabilite du systeme de sante national
- **Impact** : Definition des standards techniques et organisationnels pour l'echange de donnees de sante

### [2026-07-01] - Acceptation - ADR-0006
- **Auteur** : Comite de gouvernance CNISN
- **Description** : Validation officielle de l'ADR-0006 sur l'adoption de l'Identite Nationale Patient (INP)
- **ADR concerne** : ADR-0006
- **Ancien statut** : proposee (proposed)
- **Nouveau statut** : acceptee (accepted)
- **Justification** : Consensus atteint sur l'approche d'identification des patients
- **Liens** : 
  - ADR-0004 : PIXm/PDQm (reference dans la decision)
  - ART-4 : Referentiels nationaux
  - ABB-IDENTITE-BENEFICIAIRE : Resolution d'identite du beneficiaire
- **Impact** : Permet la mise en oeuvre de l'identification unique des patients a travers le systeme

## Prochaines etapes

1. **Mettre a jour ce journal** a chaque modification d'un ADR
2. **Valider les changements** via le processus de revue de code
3. **Synchroniser avec le registre** des decisions pour maintenir la coherence
4. **Archiver les versions precedentes** des ADR modifies pour reference historique

## Bonnes pratiques

- **Tracabilite** : Chaque modification doit etre documentee dans ce journal
- **Clarte** : Les descriptions doivent etre suffisamment detaillees pour comprendre le changement
- **Liens croises** : Toujours referencer les ADR, articles ou capacites concernes
- **Validation** : Les modifications doivent etre validees par le proprietaire de l'ADR ou le comite de gouvernance

## Annexe : Statuts des ADR

| Statut | Description | Couleur |
|--------|-------------|---------|
| **proposee** (proposed) | Decision en cours d'elaboration | Jaune |
| **acceptee** (accepted) | Decision validee par le comite | Vert |
| **appliquee** (applied) | Decision mise en oeuvre | Vert |
| **remplacee** (replaced) | Decision remplacee par une nouvelle | Rouge |
| **depreciee** (deprecated) | Decision obsolete | Rouge |
| **brouillon** (draft) | Ebauche de decision | Gris |
| **active** (active) | Decision active (variante de acceptee) | Vert |

## References

- [ADR Template](adr-0000-template.md) - Modele pour les nouveaux ADR
- [Registre des decisions](registre-decisions.md) - Liste complete des ADR
- [Index des ADR](index.md) - Index des decisions architecturales
