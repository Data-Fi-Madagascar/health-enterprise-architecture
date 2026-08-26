---

title: "Partie I : Règles d'utilisation du PTISN"
id: ptisn-regles-utilisation
domain: 01_regles-utilisation
version: "1.0.0"
status: draft
last_reviewed: 2026-07-31
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "interopérabilité", "regles"]
---


# Partie I : Règles d'utilisation du PTISN

## 1. Types de décisions techniques

Le PTISN distingue six catégories de décisions techniques, chacune correspondant à un niveau de spécificité et d'autorité distinct dans la chaîne d'interopérabilité.

### 1.1 Service national

Un service national désigne une capacité applicative partagée mise à disposition de plusieurs systèmes du secteur. Il s'agit d'un composant d'infrastructure logicielle dont la disponibilité et la fiabilité conditionnent le fonctionnement de multiples initiatives. Les services nationaux couvrent notamment la résolution d'identité, l'annuaire des formations sanitaires, les services terminologiques, le catalogue de services et la médiation inter-systèmes.

### 1.2 Standard de base

Un standard de base est une spécification générale utilisée pour structurer ou échanger une information. Il constitue le socle commun sur lequel s'appuient les profils d'interopérabilité. Les standards de base reconnus dans le cadre du PTISN incluent HL7 FHIR, REST, JSON, OAuth et OpenAPI.

### 1.3 Profil d'interopérabilité

Un profil d'interopérabilité est une contrainte appliquée à un ou plusieurs standards de base afin de répondre à un cas d'usage déterminé. Il restreint les options ambiguës ou optionnelles d'un standard pour garantir une interopérabilité effectif entre les systèmes participants. Les profils couramment mobilisés dans le secteur santé numérique malgache sont PIXm, PDQm, mCSD, SVCM et mADX.

### 1.4 Patron architectural

Un patron architectural est une organisation de composants destinée à résoudre une catégorie de problème récurrent. Les patrons architecturaux : tels que le médiateur, la fédération, CQRS, l'historisation événementielle ou la publication-abonnement : sont définis dans l'ARTSN et non par le présent document. Le PTISN se contente de les référencer lorsqu'ils sont mobilisés dans les profils d'initiative.

### 1.5 Produit ou implémentation candidate

Un produit ou une implémentation candidate est une solution concrète susceptible de mettre en œuvre un service national ou un patron architectural. Il peut s'agir d'une plateforme nationale d'échange, d'un médiateur sectoriel, d'un serveur terminologique, d'un registre ou d'un moteur analytique. La conformité d'un produit est évaluée sur la base de ses contrats et de ses preuves de conformité, et non sur la seule dénomination commerciale.

### 1.6 Décision nationale

Une décision nationale est un choix formellement validé par l'autorité compétente. Toute décision nationale doit disposer d'une référence, d'une date, d'une autorité de validation, d'un périmètre, d'une version et d'une stratégie d'évolution documentée.

## 2. Statuts des décisions

Les standards, profils et produits mentionnés dans le PTISN portent l'un des statuts suivants, qui reflètent leur degré de maturité et leur niveau d'engagement institutionnel.

| Statut | Signification |
|----|----|
| **À instruire** | Besoin identifié, solution non encore évaluée |
| **Candidat** | Solution ou profil identifié pour évaluation |
| **Recommandé** | Option privilégiée pour les nouvelles initiatives |
| **Retenu pour pilote** | Choix limité à une initiative ou une expérimentation |
| **Retenu nationalement** | Choix validé pour le périmètre national défini |
| **Homologué** | Conformité démontrée par les tests et la gouvernance |
| **Déprécié** | Maintenu temporairement pour compatibilité |
| **Retiré** | Ne doit plus être utilisé |

Le statut d'un produit est toujours distinct du statut du standard qu'il implémente. Un produit peut être homologué tandis que le standard sous-jacent reste simplement recommandé, ou inversement.

## 3. Versionnement

Toute référence à un profil d'interopérabilité doit préciser le nom officiel, l'organisme de publication, la version, la date de publication, la version du standard de base sur lequel il repose, les options obligatoires, les éventuelles extensions nationales ainsi que la date de révision prévue. La mention générique d'un standard sans indication de version n'est pas suffisante dans une spécification d'implémentation.

Le registre national des profils conserve les versions actives, les versions en transition, les versions dépréciées, les dates de fin de support ainsi que l'ensemble des dépendances entre profils et standards. Cette centralisation garantit la traçabilité et la cohérence du versionnement à l'échelle du système national.

## 4. Applicabilité

L'applicabilité des chapitres de l'ARTSN est définie dans le profil d'applicabilité de chaque initiative. Le PTISN n'impose pas à toutes les initiatives l'ensemble des standards décrits. Une initiative applique uniquement les profils correspondant à son périmètre, à ses données, à ses interfaces, à ses risques, à ses consommateurs et à ses obligations d'interopérabilité. Cette approche pragmatique évite l'application indiscriminée de standards non pertinents pour le contexte opérationnel considéré.

## 5. Extensions nationales

Une extension nationale à un standard doit être justifiée, documentée, versionnée, publiée, soumise à un contrôle de compatibilité, limitée aux besoins non couverts par le standard international et accompagnée d'exemples et de tests. Une extension ne doit pas modifier silencieusement la signification d'un élément standard, car une telle modification compromettrait l'interopérabilité avec les systèmes conformes au standard de base.

Lorsqu'une extension peut être proposée à la communauté internationale concernée, cette voie devrait être privilégiée avant la création d'une divergence nationale permanente. La standardisation internationale des extensions réduit les coûts de maintenance et facilite les échanges transfrontaliers.
