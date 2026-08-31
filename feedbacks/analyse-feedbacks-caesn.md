# Analyse des feedbacks de validation technique - CAESN

> **Référence** : HEA-ANA-CAESN-001
> **Date** : 30 août 2026
> **Version** : 2.0
> **Objet** : Restitution consolidée des observations issues de la validation technique du Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN)
> **Sources** : Matrices de validation des groupes G1, G2, G3, G4
> **Statut** : Livrable d'analyse - à valider avant plan d'amendement


## Table des matières

1. [Contexte et objectif](#1-contexte-et-objectif)
2. [Méthodologie](#2-méthodologie)
3. [Synthèse quantitative](#3-synthèse-quantitative)
4. [Analyse par domaine](#4-analyse-par-domaine)
   - 4.1 [Rédaction et mise en forme](#41-rédaction-et-mise-en-forme)
   - 4.2 [Références stratégiques et normatives](#42-références-stratégiques-et-normatives)
   - 4.3 [Flux de valeur et indicateurs](#43-flux-de-valeur-et-indicateurs)
   - 4.4 [Capabilités et architecture runway](#44-capabilités-et-architecture-runway)
   - 4.5 [Données et référentiels](#45-données-et-référentiels)
   - 4.6 [Portefeuille d'initiatives](#46-portefeuille-dinitiatives)
   - 4.7 [Gouvernance et responsabilités](#47-gouvernance-et-responsabilités)
   - 4.8 [Portée et applicabilité](#48-portée-et-applicabilité)
5. [Convergences inter-groupes](#5-convergences-inter-groupes)
6. [Points d'arbitrage](#6-points-darbitrage)
7. [Recommandations](#7-recommandations)
8. [Annexe - Matrice de traçabilité](#8-annexe--matrice-de-tracabilité)


## 1. Contexte et objectif

### 1.1 Positionnement stratégique du CAESN

Le Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) constitue le document fondateur de la hiérarchie documentaire HEA. En tant que niveau 1, il sert de référence normative pour l'ensemble des decisions architecturales touchant le secteur de la santé à Madagascar. Sa vocation est triple : **orienter** les investissements numériques vers des initiatives créatrices de valeur, **gouverner** le portefeuille des solutions pour éviter la fragmentation et la duplication, et **évaluer** la maturité des systèmes d'information par un cadre de conformité reproductible.

Dans un contexte où le secteur santé malgache a connu une multiplication rapide des plateformes numériques soutenues par une diversité de partenaires techniques et financiers - souvent sans coordination architecturale commune - le CAESN répond à un besoin critique de **rationalisation** et de **cohérence nationale**. Il ne s'agit pas simplement d'un document technique : c'est un instrument de pilotage stratégique qui traduit les orientations du Plan de Développement du Secteur Santé (PDSS) et de la Politique Nationale de Santé (PNS) en capabilités organisationnelles mesurables et en flux de valeur opérationnels.

### 1.2 Objectif de la présente analyse

Dans le cadre de l'atelier de validation technique HEA, **quatre groupes d'experts (G1, G2, G3, G4)** ont examiné le CAESN et produit **208 observations** couvrant la journée J1. Chaque groupe était composé d'experts aux profils complémentaires - architectes d'entreprise, responsables SI, spécialistes de la gouvernance des données, représentants des partenaires techniques et financiers - afin de couvrir l'ensemble des dimensions du cadre.

Le présent document consolide l'ensemble de ces feedbacks afin de :

- **Identifier** les observations convergentes, c'est-à-dire celles qui ont été soulevées indépendamment par plusieurs groupes, ce qui constitue un signal fort de priorité ;
- **Classer** les écarts par type (rédactionnel, lacune, incohérence, ambiguïté) et par domaine fonctionnel, permettant ainsi d'organiser le plan d'amendement de manière structurée ;
- **Proposer** une priorisation en trois niveaux (bloquant, important, souhaitable), permettant aux décideurs de concentrer les ressources sur les corrections à impact maximal.

L'objectif final est de transformer un ensemble brut de 208 observations en un **plan d'action exécutable** qui permettra au CAESN d'atteindre le statut de document de référence nationale fiable, cohérent et opérationnel.


## 2. Méthodologie

### 2.1 Processus de collecte

La collecte des observations a reposé sur une **matrice de validation technique standardisée**, documentée dans chaque fichier Excel remis par les groupes. Cette matrice comportait treize colonnes permettant de capturer chaque observation avec un niveau de détail suffisant pour permettre le traitement ultérieur : identification unique, rattachement au document et à la section concernée, description de l'écart, typologie, proposition d'amendement, décision, responsable, échéance, statut et point d'arbitrage.

Ce format a permis de garantir la **comparabilité** des observations entre groupes, malgré des approches de rédaction parfois différentes. Il a également facilité le traitement automatisé - comptage, classification, extraction - nécessaire à la consolidation.

### 2.2 Conventions de nommage

Pour chaque observation, l'identifiant suit le format `CAE-G{groupe}-{numéro}`, ce qui permet de **tracer l'origine** de chaque commentaire et d'identifier les zones de convergence ou de divergence entre groupes. Cette traçabilité est essentielle pour l'arbitrage : lorsqu'une observation est soulevée par un seul groupe, elle peut refléter un point de vue spécifique ; lorsqu'elle est soulevée par trois ou quatre groupes, elle constitue un consensus quasi-automatique.

### 2.3 Limites méthodologiques

Il convient de noter que les observations n'ont pas toutes été soumises au même niveau de scrutiny. Le G3, avec 88 observations, a produit un volume significativement plus élevé que les autres groupes, ce qui peut s'expliquer par un périmètre d'examen plus large ou par un niveau de détail requis différent. À l'inverse, le G1 (27 observations) s'est concentré sur les points les plus critiques. Cette hétérogénéité doit être prise en compte lors de l'interprétation des résultats : le nombre d'observations par domaine ne reflète pas nécessairement la gravité des écarts, mais plutôt l'attention portée par chaque groupe à ce domaine.


## 3. Synthèse quantitative

### 3.1 Volume d'observations par groupe

| Groupe | Nombre d'observations | Avec proposition | Sans proposition |
|--------|----------------------|------------------|-----------------|
| G1 | 27 | 27 | 0 |
| G2 | 62 | 42 | 20 |
| G3 | 88 | 88 | 0 |
| G4 | 31 | 31 | 0 |
| **Total** | **208** | **188** | **20** |

La répartition des observations entre les groupes révèle des **profils d'examen distincts**. Le G3, avec 88 observations, a produit le volume le plus élevé, ce qui correspond à un examen systématique couvrant à la fois la forme (grammaire, ponctuation, articles) et le fond (structure des flux de valeur, indicateurs, portefeuille). Le G2 (62 observations) s'est particularisé par des observations de nature opérationnelle - scoring, chaîne de valeur standardisée, priorisation - qui traduisent une préoccupation pour l'**applicabilité concrète** du cadre. Le G1 (27 observations) et le G4 (31 observations) ont adopté une approche plus ciblée, en se concentrant sur les points bloquants : références obsolètes, incohérences structurelles, lacunes de gouvernance.

Le fait que 20 observations sur 208 (10%) n'aient pas de proposition d'amendement associée est un signal : ces observations identifient des problèmes sans proposer de solution, ce qui nécessitera un travail de résolution supplémentaire lors de la phase d'amendement.

### 3.2 Répartition par type d'écart

| Type d'écart | Nombre | % |
|-------------|--------|---|
| Observation rédactionnelle | ~120 | 58% |
| Lacune | ~35 | 17% |
| Incohérence | ~15 | 7% |
| Exigence à préciser | ~20 | 10% |
| Ambiguïté | ~10 | 5% |
| Autre | ~8 | 3% |
| **Total** | **208** | **100%** |

La prédominance des **observations rédactionnelles** (58%) indique que le CAESN souffre principalement de problèmes de forme plutôt que de fond. C'est un résultat encourageant : les lacunes rédactionnelles sont généralement plus rapides à corriger que les lacunes conceptuelles. Cependant, les **lacunes** (17%) et les **incohérences** (7%) méritent une attention particulière, car elles révèlent des zones où le document est structurellement incomplet ou contradictoire. Les **exigences à préciser** (10%) signalent des domaines où le cadre pose des principes sans en définir les modalités d'application, ce qui pourrait générer des interprétations divergentes lors de la mise en œuvre.

### 3.3 Répartition par décision

| Décision | Nombre | % |
|----------|--------|---|
| Validé | ~8 | 4% |
| Validé sous réserve d'amendement | ~12 | 6% |
| À revoir | ~130 | 63% |
| Amendement requis | ~30 | 14% |
| À arbitrer | ~15 | 7% |
| Non renseigné | ~13 | 6% |
| **Total** | **208** | **100%** |

La décision « À revoir » domine largement (63%), ce qui est cohérent avec un document en cours de maturation. Les 14% « Amendement requisite » et 7% « À arbitrer » représentent les points nécessitant une intervention formelle - soit une correction obligatoire, soit une décision de gouvernance. Les 6% « Non renseigné » correspondent principalement aux observations du G2 qui n'ont pas toujours renseigné la colonne de décision, ce qui nécessitera un travail de classification complémentaire.

### 3.4 Taux de convergence inter-groupes

Environ **30% des observations** ont été soulevées par au moins deux groupes de manière indépendante. Ce taux de convergence est significatif : il indique que les problèmes identifiés ne sont pas le fait de perceptions individuelles mais reflètent des **dysfonctionnements réels** du document. Les zones de convergence les plus fortes touchent les références stratégiques (PDSS), la gouvernance (RACI, responsabilités), la terminologie (« malagasy », « architecture runway ») et la complétude des annexes.


## 4. Analyse par domaine

### 4.1 Rédaction et mise en forme

**Périmètre** : Structure du document, table des matières, glossaire, acronymes, gestion de version, mise en forme.

**Nombre d'observations** : ~45

#### Analyse détaillée

La qualité rédactionnelle d'un document de référence nationale n'est pas un enjeu cosmétique : elle conditionne directement la **capacité d'appropriation** par les parties prenantes. Un document contenant des acronymes non définis, des glossaires incohérents ou une table des matières défectueuse est un document qui ne sera pas lu, pas compris et pas appliqué. C'est précisément le risque qui est identifié ici.

L'absence de **liste d'acronymes** est un problème transversal signalé par les groupes G1, G2 et G3. Le CAESN utilise un vocabulaire technique dense - FOSA, DEPSI, CAP-13, architecture runway, steward de données, ISO 42010 - sans toujours en fournir la définition. Pour un document qui s'adresse à des « décideurs politiques, responsables de programmes, partenaires techniques et financiers » (comme le précise le guide de lecture), cette opacité terminologique est un obstacle majeur à l'adoption. Un décideur politique qui ne comprend pas le terme « capabilité » ne pourra pas évaluer pertinemment les initiatives qui lui sont soumises.

L'incohérence dans la définition de « **capabilité** » est particulièrement préoccupante. Le corps du document (page 5) la définit comme combinant « processus, responsabilités, ressources humaines, données, technologies, gouvernance et financement », tandis que le glossaire (page 115) la réduit à « compétences humaines, processus organisationnels, données et technologies ». Cette divergence n'est pas anodine : elle omet la gouvernance et le financement, qui sont pourtant des dimensions essentielles de toute capabilité organisationnelle. Si les utilisateurs du cadre ne peuvent pas s'accorder sur la définition d'un concept aussi fondamental, les évaluations de maturité qui en découlent perdront toute crédibilité.

Le terme « **architecture runway** » - emprunté à l'agile product management - est utilisé sans définition ni traduction française. Bien que le concept soit connu des practitioners agile, il est impropre à un document de référence nationale destiné à un public large. La proposition de G2 de le traduire par « socle d'architecture prioritaire » est pertinente et devrait être adoptée.

Les **annexes E à J** sont toutes vides, ce qui est inacceptable pour un document qui y renvoie explicitement. Ces annexes devraient contenir des matrices de correspondance, des modèles de fiche, des grilles de priorisation et un RACI de gouvernance - tous éléments essentiels à l'opérationnalisation du cadre.

#### Observations majeures

| # | Sujet | Observation | Groupes | Impact | Recommandation |
|---|-------|-------------|---------|--------|----------------|
| 1 | Liste acronymes | Absente du document | G1, G2, G3 | Incompréhension des abréviations | **Insérer** liste complète des acronymes et sigles |
| 2 | Glossaire | Incomplet ou absent | G1, G2 | Un lecteur ne peut pas comprendre le document sans référence externe | **Rédiger** un glossaire complet avec toutes les définitions |
| 3 | Gestion de version | Absente ou incohérente (« Version 0.1 – Draft – Large diffusion ») | G2 | Traçabilité des révisions non assurée | **Ajouter** bloc de gestion de version cohérent |
| 4 | Table des matières | Incohérente (taille de police, pagination, annexes manquantes) | G1, G2 | Navigation impossible | **Revoir** la TDM complète et régénérer |
| 5 | Annexes E-J | Vides sans contenu | G1, G3 | Document incomplet | **Compléter** ou retirer les références |
| 6 | Personnification | Usage de « ils, nous, vous » dans l'avant-propos | G1 | Registre inadapté à un document de référence | **Reformuler** au style impersonnel |
| 7 | « Capabilité » | Incohérence glossaire/corps (définition différente page 5 vs page 115) | G1, G2 | Confusion conceptuelle | **Harmoniser** la définition partout |
| 8 | « Architecture runway » | Non définie en français | G1, G2 | Terme incompris | **Définir** : « socle d'architecture prioritaire » |
| 9 | « Steward de données » | Non défini | G1 | Terme technique incompris | **Insérer** définition au glossaire |
| 10 | « FOSA » | Non défini | G1 | Abréviation incomprise | **Définir** : Formation Sanitaire |
| 11 | Capabilité majuscule | Usage incohérent (« Capabilité » vs « capabilité ») | G2, G3 | Mise en forme non professionnelle | **Uniformiser** en minuscule sauf en début de phrase |
| 12 | ISO 42010 | Cadre ne formalise pas suffisamment la description des architectures | G1 | Norme non respectée | **Préciser** l'alignement ISO 42010 si applicable |

**Verdict** : Les lacunes rédactionnelles du CAESN sont nombreuses mais de sévérité variable. Les plus critiques sont l'absence de glossaire et l'incohérence de définition de « capabilité », qui sont des concepts centraux du document. Ces lacunes, si elles ne sont pas corrigées, risquent de compromettre l'**adoptabilité** du cadre par les parties prenantes non techniques.


### 4.2 Références stratégiques et normatives

**Périmètre** : PDSS, PNS, référentiels internationaux, articulation avec les autres documents.

**Nombre d'observations** : ~25

#### Analyse détaillée

Un document d'architecture d'entreprise ne existe pas dans un vide institutionnel. Sa légitimité dépend de son **ancrage dans les politiques et stratégies nationales** qui le fondent. C'est précisément cet ancrage qui est mis en cause par les observations de ce domaine.

L'observation la plus convergente - soulevée par les quatre groupes - concerne la référence au **PDSS 2020-2024**, qui est obsolète. Le nouveau Plan de Développement du Secteur Santé couvre la période 2026-2030 et comporte 7 Orientations stratégiques (contre 8 Axes auparavant). Cette mise à jour n'est pas cosmétique : elle affecte la lecture des axes stratégiques nationaux dans le cadre, les domaines de données prioritaires, et potentiellement les flux de valeur eux-mêmes. Un CAESN qui référence un plan périmé perd immédiatement sa crédibilité aux yeux des décideurs et des partenaires techniques et financiers.

L'absence de la **Politique Nationale de Santé (PNS)** dans les références stratégiques est une lacune identifiée par le G3. La PNS 2025-2030 constitue la référence sectorielle de la politique publique en matière de santé, avec sa vision « D'ici 2035, Madagascar dispose d'une population en bonne santé ». Le CAESN, en tant que traduction architecturale de cette politique, devrait explicitement s'y référer pour établir sa légitimité et sa cohérence.

La question du nom du **Ministère** - « Ministère de la Santé Publique » vs « Ministère en charge de la Santé » - est un enjeu d'exactitude institutionnelle. Les noms des ministères évoluent avec les remaniements gouvernementaux ; un document de référence doit utiliser la dénomination officielle actuelle.

La mention de « **l'État numérique malgache** » dans la section des référentiels normatifs internationaux (GovStack) est identifiée comme impropre par le G3. Le terme exact devrait être « système numérique malgasy », ce qui est conceptuellement plus précis et évite la confusion avec une entité institutionnelle.

#### Observations majeures

| # | Sujet | Observation | Groupes | Impact | Recommandation |
|---|-------|-------------|---------|--------|----------------|
| 1 | PDSS 2020-2024 | Référence obsolète | G1, G2, G3, G4 | Référence périmée | → **PDSS 2026-2030** (7 Orientations stratégiques) |
| 2 | PNS absente | La Politique Nationale de Santé n'est pas citée | G3 | Contexte stratégique incomplet | **Insérer** PNS 2025-2030 |
| 3 | « malagasy » | « comparabilité des choix malagasy » | G1, G3 | Terme inapproprié | → **« malagasy »** ou reformuler |
| 4 | Ministère de la Santé Publique | Nom obsolète | G1 | Référence institutionnelle erronée | → **« Ministère en charge de la Santé »** |
| 5 | DEPSI | Sigle non défini | G1 | Incompréhension | **Définir** au glossaire |
| 6 | Référentiels normatifs internationaux | Pas de phrase introductive | G2 | Contexte manquant | **Insérer** phrase d'introduction |
| 7 | Relation avec documents de référence | CNISN omis de la liste | G3 | Référence manquante | **Ajouter** CNISN |
| 8 | « Etat numérique malgache » | Terme impropre (GovStack) | G3 | Inexactitude | → **« système numérique malagasy »** |
| 9 | Citation page 7 | Auteur non mentionné | G1 | Crédibilité | **Ajouter** le nom de l'auteur |

**Verdict** : La mise à jour du PDSS est une **action prioritaire et convergente** (4 groupes). L'absence de la PNS est une lacune significative identifiée par G3. Ces références stratégiques sont le socle de légitimité du CAESN ; sans elles, le document risque d'être perçu comme déconnecté des orientations nationales.


### 4.3 Flux de valeur et indicateurs

**Périmètre** : VS-01 à VS-04, étapes de valeur, indicateurs, dimensions de valeur.

**Nombre d'observations** : ~30

#### Analyse détaillée

Les flux de valeur constituent le **cœur opérationnel** du CAESN. Ils traduisent les priorités nationales en séquences d'activités mesurables, permettant ainsi de relier chaque initiative numérique à un bénéfice concret pour le patient, la communauté ou le système de santé. C'est cette logique de valeur qui distingue le CAESN d'un simple référentiel technique : il impose que toute initiative démontre sa contribution à un flux de valeur identifié.

Les observations de ce domaine révèlent des **problèmes de cohérence interne** au sein des flux de valeur. Par exemple, l'étape 1 du VS-01 mentionne « symptôme ou besoin ressenti par le patient », mais le G2 soulève que la maladie devrait précéder le symptôme dans la logique causale. Cette observation, bien que détaillée, traduit un enjeu plus large : les flux de valeur doivent être **cliniquement exacts** pour être crédibles aux yeux des professionnels de santé qui seront les principaux utilisateurs du cadre.

Les **indicateurs** constituent un enjeu majeur. Plusieurs indicateurs existants sont identifiés comme non pertinents (« délai de prise en charge » dépend de la maladie, indicateurs de VS-03 inadéquats) ou incomplets (indicateur de laboratoire manquant pour VS-02). Plus fondamentalement, le G2 soulève que les tableaux de ruptures ne comportent pas de colonne de « criticité/priorité », ce qui rend impossible la priorisation des investissements. C'est un défaut de conception : un flux de valeur sans hiérarchisation des ruptures ne peut pas orienter efficacement les décisions d'allocation des ressources.

La création d'une **8ème étape** pour le VS-03 (« Ajustement des mécanismes ») est une proposition pertinente du G3. L'étape 7 actuelle cumule le contrôle et l'amélioration, ce qui est conceptuellement confus. Séparer l'ajout d'une boucle de rétroaction distincte renforce la logique d'amélioration continue.

L'ajout de **VS-02 et VS-04** aux domaines de données prioritaires (proposition G2) est logique : les résultats cliniques (VS-02) et les remontées terrain (VS-04) nourrissent respectivement la surveillance sanitaire et le pilotage communautaire, deux fonctions essentielles du système de santé.

#### Observations majeures

| # | Sujet | Observation | Groupes | Impact | Recommandation |
|---|-------|-------------|---------|--------|----------------|
| 1 | VS-01 : soins de réhabilitation | « réhabilitation » non défini | G2 | Concept flou | **Clarifier** ou retirer |
| 2 | VS-01 : indicateurs | « Délai de prise en charge » dépend de la maladie | G2 | Indicateur non pertinent | **Retirer** ou reformuler |
| 3 | VS-01 : étapes | « Maladie » devrait précéder « symptôme » | G2 | Logique inversée | **Inverser** |
| 4 | VS-02 : indicateurs | Indicateur de laboratoire manquant | G2 | Couverture incomplète | **Ajouter** « Taux de laboratoire fonctionnel » |
| 5 | VS-02 : étapes | « Registre patient » est un outil, pas un acteur | G2 | Confusion acteur/outil | **Remplacer** par « Personnel d'accueil » |
| 6 | VS-03 : indicateurs | « Taux de satisfaction du patient » | G2 | Formulation incomplète | **Compléter** « Taux de satisfaction du patient » |
| 7 | VS-03 : indicateurs équité | Indicateurs non pertinents | G2 | Couverture incomplète | **Ajouter** taux de couverture en zones reculées |
| 8 | VS-03 : indicateurs système | Indicateurs non pertinents | G2 | Couverture incomplète | → **« indicateurs d'impact du PDSS 2026-2030 »** |
| 9 | VS-03 : étape 8 | « Ajustement des mécanismes » à séparer | G3 | Étape manquante | **Créer** une 8ème étape |
| 10 | VS-04 : domaines | VS-02 et VS-04 à ajouter aux domaines de données | G2 | Couverture incomplète | **Insérer** VS-02 et VS-04 |
| 11 | Criticité/priorité | Absente des tableaux de ruptures | G2 | Priorisation impossible | **Ajouter** colonne « Niveau de criticité » |
| 12 | Chaîne de valeur initiative | Non standardisée | G2 | Vision fragmentée | **Définir** modèle commun |

**Verdict** : Les flux de valeur nécessitent des **ajustements d'indicateurs** et la **création d'une étape 8** pour VS-03. La standardisation de la chaîne de valeur des initiatives est un besoin transversal identifié par le G2. Ces corrections sont essentielles pour que les flux de valeur puissent effectivement servir d'outil de pilotage.


### 4.4 Capabilités et architecture runway

**Périmètre** : Définition, typologie, runway (CAP-13 à CAP-16), matrice de maturité.

**Nombre d'observations** : ~15

#### Analyse détaillée

Les capabilités sont le **deuxième pilier** du CAESN, après les flux de valeur. Elles décrivent ce que le système de santé doit être capable de faire durablement pour produire de la valeur. La hiérarchie entre capabilités ordinaires et capabilités « runway » (ou « socle d'architecture prioritaire ») introduit une logique de priorisation : certaines capabilités sont si fondamentales qu'elles conditionnent la valeur de nombreuses autres.

L'observation la plus récurrente concerne l'**incohérence dans le glossaire** : le document présente quatre capabilités runway (CAP-13 à CAP-16) dans le corps du texte, mais le glossaire ne mentionne que CAP-14, CAP-15 et CAP-16, omettant CAP-13 (« Système d'information sanitaire, données et recherche »). Cette omission est particulièrement dommageable car CAP-13 est classée « Critique » avec un delta de maturité de +3, ce qui en fait la capacité runway la plus prioritaire. Ne pas la mentionner dans le glossaire crée une confusion sur le périmètre exact du socle d'architecture.

Le G2 soulève que les **trois catégories de capabilités** (stratégiques, opérationnelles, habilitantes) ne sont pas clarifiées, et propose de les présenter sous forme de tableau. Cette suggestion est pertinente : la forme narrative actuelle ne permet pas au lecteur de saisir rapidement la logique de classification. De même, l'absence de **schéma explicatif** du modèle de capabilités rend la compréhension du lien entre priorités nationales, flux de valeur et initiatives particulièrement ardue pour un lecteur non technique.

La question de la **priorisation des principes** (obligatoires dès la phase 1 vs progressifs) est soulevée par le G2. Cette distinction est essentielle pour l'opérationnalisation : sans elle, toutes les exigences sont traitées avec le même niveau de priorité, ce qui dilue l'effort d'implémentation.

#### Observations majeures

| # | Sujet | Observation | Groupes | Impact | Recommandation |
|---|-------|-------------|---------|--------|----------------|
| 1 | CAP-13 manquant glossaire | Glossaire cite CAP-14, 15, 16 mais pas CAP-13 | G1, G3 | Incohérence | **Insérer** CAP-13 dans le glossaire |
| 2 | Trois catégories de capabilités | Non clarifiées | G2 | Confusion | **Rendre** sous forme de tableau |
| 3 | Schéma explicatif | Absent du modèle capabilités | G2 | Compréhension difficile | **Ajouter** schéma : Priorité → Flux → Capabilités → Initiatives → Valeur |
| 4 | Priorisation des principes | Non précisée (obligatoires vs progressifs) | G2 | Application incertaine | **Identifier** les principes obligatoires phase 1 |
| 5 | Maturité des capabilités | Méthode de scoring 1-5 non détaillée | G3 | Évaluation non reproductible | **Définir** critères de chaque niveau |
| 6 | Priorisation des capabilités | Formule de calcul non transparente | G3 | Arbitrage opaque | **Formaliser** grille de scoring pondérée |
| 7 | Capabilité critique vs runway | Distinction incohérente dans tableaux | G3 | Confusion conceptuelle | **Harmoniser** classification unique |

**Verdict** : L'architecture runway est un concept central mais mal défini. L'incohérence CAP-13/glossaire est un point de friction récurrent (G1, G3). Ces corrections sont nécessaires pour que le modèle de capabilités soit crédible et opérationnel.


### 4.5 Données et référentiels

**Périmètre** : Architecture des données, domaines prioritaires, référentiels nationaux, qualité des données.

**Nombre d'observations** : ~25

#### Analyse détaillée

Le CAESN identifie les données de santé comme un « actif stratégique national » et définit les référentiels nationaux comme des « biens communs numériques ». Ces déclarations de principe sont fortes, mais leur mise en œuvre concrète se heurte à plusieurs lacunes identifiées par les groupes.

La principale concerne la **gouvernance des référentiels**. Le document identifie huit référentiels prioritaires (formations sanitaires, découpages géographiques, agents de santé, produits de santé, indicateurs, bénéficiaires, partenaires, initiatives) mais ne définit pas pour chacun d'eux : le responsable métier, le responsable technique, la source officielle, la fréquence de mise à jour, les règles de qualité et les modalités d'accès. Sans ces informations, les référentiels restent des déclarations d'intention plutôt que des composants gouvernés.

La question de la **qualité des données** est abordée via une annexe Excel (Annexe QD) qui définit huit dimensions : Complétude, Promptitude, Précision, Validité, Cohérence, Fiabilité, Intégrité, Confidentialité. Le G1 souligne que ces dimensions doivent être harmonisées avec le corps du document, ce qui n'est pas le cas actuellement. Cette harmonisation est essentielle pour que les évaluations de qualité soient reproductibles.

Les **domaines de données prioritaires** comportent des incohérences terminologiques : « vaccins, intrants, chaîne du froid » pour les données logistiques (le G3 propose « intrants et autres produits de santé, dispositifs médicaux »), et « zones sanitaires » en trop dans les données géographiques. Ces ajustements, bien que détaillés, sont nécessaires pour la précision du cadre.

La question des **rôles de gouvernance des données** (Data Owner, Data Steward, Producteur) est soulevée par le G3. Ces rôles, standards dans tout programme de gouvernance des données, ne sont pas distingués dans le CAESN, ce qui rend difficile l'attribution des responsabilités lors de la mise en œuvre.

#### Observations majeures

| # | Sujet | Observation | Groupes | Impact | Recommandation |
|---|-------|-------------|---------|--------|----------------|
| 1 | Qualité des données | Dimensions non harmonisées | G1 | Évaluation incohérente | **Harmoniser** avec annexe Excel |
| 2 | Domaines de données RH | « Ancienneté au poste » manquante | G1 | Couverture incomplète | **Ajouter** |
| 3 | Données géographiques | « zones sanitaires » en trop | G3 | Redondance | **Retirer** |
| 4 | Référentiel formations sanitaires | « privées, confessionnelles, communautaires et partenaires » | G3 | Périmètre trop large | **Limiter** à « publiques, privées » |
| 5 | Référentiel produits de santé | « médicaments, vaccins, intrants » | G3 | Formulation à adapter | → **« intrants et consommables, autres produits de santé »** |
| 6 | Données logistiques | « vaccins, intrants, chaîne du froid » | G3 | Formulation à adapter | → **« intrants et autres produits de santé, dispositifs médicaux »** |
| 7 | Référentiels comme biens communs | Propriété et gouvernance non détaillées | G3 | Gouvernance floue | **Ajouter** responsable métier/technique, source, fréquence, règles qualité |
| 8 | Vue cible du paysage applicatif | Non schématisée | G3 | Vision incomplète | **Schématiser** les 6 couches |
| 9 | Rôles Data Owner/Steward | Non distingués | G3 | Gouvernance floue | **Introduire** les rôles de gouvernance des données |
| 10 | CSU | Intégration incohérente | G3 | Confusion | **Reformuler** : « Protection financière et gestion des bénéficiaires » |

**Verdict** : Les référentiels nationaux sont identifiés comme « biens communs numériques » mais leur gouvernance (propriété, responsabilité, qualité) reste insuffisamment détaillée. Sans cette gouvernance, les référentiels risquent de rester des artefacts théoriques plutôt que des composants effectivement utilisés.


### 4.6 Portefeuille d'initiatives

**Périmètre** : Registre national, fiche standard, chaîne de valeur, scoring, priorisation.

**Nombre d'observations** : ~20

#### Analyse détaillée

Le portefeuille d'initiatives est l'**outil de pilotage stratégique** du CAESN. Il permet de passer d'une gestion projectuelle fragmentée à une gestion portfolio cohérente, où chaque initiative est évaluée non seulement par ses mérites intrinsèques mais aussi par sa contribution à l'ensemble de l'écosystème. C'est le mécanisme par lequel le CAESN exerce son rôle de « mécanisme national d'arbitrage de la valeur, de la cohérence et de la soutenabilité des investissements numériques en santé ».

Le principal problème identifié est l'absence de **mécanismes opérationnels** pour effectiver cet arbitrage. Le G2 propose l'instauration d'un scoring d'évaluation (0 = Non démontré, 1 = Faible, 2 = Partiel, 3 = Conforme, 4 = Très conforme) et la standardisation de la chaîne de valeur des initiatives (Problème → Initiative → Output → Usage → Changement métier → Bénéfice → Valeur). Ces deux outils sont essentiels : sans scoring, les évaluations sont subjectives et non comparables ; sans chaîne de valeur standardisée, chaque initiative est évaluée selon des critères différents.

La question de l'**obligation d'enregistrement** est soulevée par le G2 et le G3 : qui doit obligatoirement enregistrer une initiative dans le registre national ? Le document mentionne les partenaires techniques et financiers, mais ne précise pas si les programmes, les directions du ministère ou les projets financés par l'État y sont soumis. Cette ambiguïté est critique : si l'enregistrement n'est pas obligatoire pour tous les acteurs, le portefeuille sera incomplet et ne pourra pas remplir sa fonction de pilotage.

Le G3 soulève une question ouverte : l'**État peut-il être considéré comme financeur** dans le cadre du Registre des Projets d'Initiatives (RPI) ? Cette question a des implications sur la gouvernance : si l'État est financeur, ses propres initiatives doivent être soumises aux mêmes exigences que celles des partenaires.

#### Observations majeures

| # | Sujet | Observation | Groupes | Impact | Recommandation |
|---|-------|-------------|---------|--------|----------------|
| 1 | « Initiative orientée valeur » | Titre impropre | G3 | Confusion | → **« Les caractéristiques d'une initiative orientée valeur »** |
| 2 | Obligation d'enregistrement | Qui doit enregistrer ? | G2, G3 | Flou | **Étendre** aux programmes, directions, PTF, projets |
| 3 | Chaîne de valeur | Non standardisée | G2 | Vision fragmentée | **Définir** modèle commun |
| 4 | Scoring d'évaluation | Absent | G2 | Comparaison impossible | **Instaurer** : 0-4 |
| 5 | Règles de sortie | Sans articles | G3 | Mauvaise grammaire | **Rajouter** des articles |
| 6 | Règles d'entrée | Sans articles | G3 | Mauvaise grammaire | **Rajouter** des articles |
| 7 | Fiche standard | Périmètre « pilote limité » non explicité | G3 | Ambiguïté | **Préciser** |
| 8 | État comme financeur | Question ouverte | G3 | Flou | **Arbitrer** |
| 9 | Revue périodique | DEPSI cité sans contexte | G3 | Incohérence | **Harmoniser** la formulation |

**Verdict** : Le portefeuille est un outil structurant mais manque de **mécanismes opérationnels** (scoring, chaîne de valeur standardisée, obligations d'enregistrement). Sans ces mécanismes, le portefeuille risque de rester un registre passif plutôt qu'un outil d'arbitrage actif.


### 4.7 Gouvernance et responsabilités

**Périmètre** : Comité National d'Architecture, Bureau de Réalisation de la Valeur, RACI, rôles.

**Nombre d'observations** : ~25

#### Analyse détaillée

La gouvernance est le domaine qui a généré le **plus grand nombre de convergences** entre groupes (G1, G2, G3), ce qui est logique : un document de référence nationale ne peut pas être effectif sans une structure de gouvernance claire qui en assure la validité, la maintenance et l'évolution.

Le problème central est l'**attribution des responsabilités**. Le CAESN identifie de multiples niveaux de responsabilité - responsable de flux de valeur, responsable de capabilité, responsable métier, responsable technique, Comité d'architecture, Bureau de Réalisation de la Valeur - mais sans toujours clarifier les frontières entre ces rôles. Le risque de **chevauchement** est réel : si deux instances ont des responsabilités similaires sans délimitation claire, les décisions traîneront ou seront contradictoires.

La **matrice RACI** (Responsible, Accountable, Consulted, Informed) est identifiée comme absente par trois groupes (G1, G2, G3). C'est un outil fondamental de toute structure de gouvernance : il permet d'attribuer explicitement chaque décision à une instance spécifique. Son absence est d'autant plus problématique que le document mentionne une matrice RACI dans l'Annexe J, mais cette annexe est vide.

Le **Comité National d'Architecture Santé Numérique** est présenté comme l'instance d'arbitrage, mais sa composition complète, sa fréquence de réunion, son quorum, ses modalités de décision et son secrétariat ne sont pas suffisamment détaillés. Le G3 propose de compléter ces informations, ce qui est essentiel pour que le Comité puisse effectivement fonctionner.

Le **Bureau de Réalisation de la Valeur** est mentionné dans le document mais jamais défini. C'est une instance dont le rôle, la composition et le lien avec le Comité d'architecture restent à clarifier.

Le G2 propose de transformer les 7 questions d'évaluation des initiatives en une **fiche standard** sous forme de formulaire, et d'instaurer un mécanisme de scoring. Ces propositions traduisent un besoin d'**opérationnalisation** : les principes sont posés, mais les outils concrets de mise en œuvre manquent.

#### Observations majeures

| # | Sujet | Observation | Groupes | Impact | Recommandation |
|---|-------|-------------|---------|--------|----------------|
| 1 | Responsabilités acteurs | Insuffisamment précisées | G1, G2, G3 | Flou organisationnel | **Identifier et rédiger** les responsabilités |
| 2 | Matrice RACI | Absente de la gouvernance des données | G1, G2, G3 | Accountability absente | **Produire et insérer** la matrice RACI |
| 3 | Comité National d'Architecture | Composition, fréquence, quorum non détaillés | G3 | Gouvernance floue | **Compléter** |
| 4 | Bureau de Réalisation de la Valeur | Non défini | G1 | Instance inconnue | **Définir** rôle et composition |
| 5 | Chevauchement des responsabilités | Multiples niveaux sans distinction claire | G3 | Confusion | **Vérifier** et compléter le RACI |
| 6 | Workflow homologation | Non explicite | G3 | Processus flou | **Ajouter** diagramme de processus |
| 7 | Instance responsable d'évaluation | Non précisée | G2 | Flou | **Désigner** |
| 8 | Critères conformité/non-conformité | Absents | G2 | Évaluation impossible | **Définir** le processus complet |
| 9 | Fiche standard d'évaluation | Présentée sous forme de texte | G2 | Utilisation difficile | **Transformer** en formulaire |
| 10 | Maturité des capabilités | Méthodologie insuffisante | G3 | Évaluation non reproductible | **Définir** critères, sources, méthode |

**Verdict** : La gouvernance est le domaine le plus critique du CAESN. La matrice RACI et la clarification des rôles sont des **prérequis** pour l'opérationnalisation du cadre. Sans gouvernance claire, le CAESN restera un document de principes sans mécanisme d'application.


### 4.8 Portée et applicabilité

**Périmètre** : Périmètre du cadre, acteurs cibles, relation avec les autres documents.

**Nombre d'observations** : ~20

#### Analyse détaillée

La portée du CAESN définit son **champ d'application** : quelles initiatives, quels acteurs, quels systèmes sont concernés par ses exigences ? Une portée mal définie entraîne soit une sous-couverture (certaines initiatives échappent au cadre), soit une surcharge (le cadre s'applique à des domaines hors de sa compétence).

Le G3 soulève que la portée actuelle - « initiatives numériques du secteur santé à Madagascar » - est clarifiée par des exclusions (équipements biomédicaux, infrastructures physiques) mais que la distinction entre « systèmes d'information sanitaire » et « systèmes du MSANP » n'est pas toujours explicite. Cette question est particulièrement pertinente dans un contexte de décentralisation, où les systèmes peuvent être portés par des entités autres que le ministère central.

Le titre « **Ce que ce cadre n'est pas** » est identifié comme inadapté au registre d'un document de référence. Le G3 propose de le transformer en paragraphe narratif, ce qui est plus cohérent avec le style du reste du document.

La question des **acteurs cibles** est soulevée par le G3, qui note que le guide de lecture mentionne « les acteurs régionaux et districts sanitaires » mais pas les formations sanitaires. La proposition de remplacer par « les acteurs locaux » est pertinente car elle inclut les formations sanitaires tout en restant suffisamment large pour couvrir les autres entités territoriales.

Le G1 soulève que les **neuf critères** que toute initiative doit satisfaire sont présentés comme cumulatifs, mais que cette cumulative n'est pas explicitement indiquée. Si un seul critère n'est pas satisfait, l'initiative n'est pas « suffisamment mûre » - c'est une exigence forte qui doit être clairement formulée.

#### Observations majeures

| # | Sujet | Observation | Groupes | Impact | Recommandation |
|---|-------|-------------|---------|--------|----------------|
| 1 | Portée | Couvre-t-elle uniquement le MSANP ? | G3 | Périmètre flou | **Préciser** : « secteur santé à Madagascar » |
| 2 | « Ce que ce cadre n'est pas » | Titre inadapté | G3 | Registre inapproprié | → **Paragraphe** narratif |
| 3 | Équipements biomédicaux | Exclure sauf interface SI | G3 | Précision utile | **Maintenir** avec clarification |
| 4 | Acteurs cibles | « acteurs régionaux et districts sanitaires » | G3 | Incomplet | → **« acteurs locaux »** |
| 5 | Relation documents de référence | « Le cadre d'Architecture d'Entreprise (ce document) » | G2 | Ambiguïté | → **« document de niveau 1 »** |
| 6 | Initiative non conforme | « non suffisamment mûre pour être financée » | G1 | Exigence forte | **Ajouter** « homologuée » en premier |
| 7 | Neuf critères cumulatifs | Non explicités comme cumulatifs | G1 | Ambiguïté | **Clarifier** |
| 8 | Formations sanitaires | « communautaires et partenaires » en trop | G3 | Périmètre élargi | **Limiter** |

**Verdict** : La portée du CAESN doit être **clairement définie** pour éviter les interprétations divergentes. Les questions de périmètre et de cumulative des critères sont essentielles pour la crédibilité du cadre.


## 5. Convergences inter-groupes

Les observations suivantes ont été soulevées par **au moins 2 groupes**, indiquant un consensus :

| # | Sujet | Groupes | Décision recommandée |
|---|-------|---------|---------------------|
| 1 | PDSS 2020-2024 → 2026-2030 | G1, G2, G3, G4 | **Validé** - mise à jour immédiate |
| 2 | Responsabilités acteurs insuffisantes | G1, G2, G3 | **Amendement requis** - rédaction |
| 3 | Matrice RACI absente | G1, G2, G3 | **Amendement requis** - production |
| 4 | « Architecture runway » non définie | G1, G2 | **À traiter** - définition |
| 5 | Annexes vides | G1, G2, G3 | **À traiter** - complétion |
| 6 | VS terminology (réhabilitation, intrants) | G2, G4 | **Validé** - remplacement |
| 7 | VS indicateurs manquants | G2, G4 | **Validé** - ajout |
| 8 | Capabilité incohérence glossaire | G1, G2 | **À traiter** - harmonisation |
| 9 | « malagasy » → reformuler | G1, G3 | **Amendement requis** - correction |
| 10 | Scoring d'évaluation absent | G2 | **À traiter** - instauration |

Le taux de convergence de 30% confirme que les problèmes identifiés ne sont pas isolés mais systémiques. Les domaines de convergence les plus forts - références stratégiques, gouvernance, terminologie - sont précisément ceux qui conditionnent la **crédibilité** et l'**adoptabilité** du cadre.


## 6. Points d'arbitrage

Les points suivants nécessitent une décision formelle avant implémentation :

| # | Question | Contexte | Groupes | Recommandation |
|---|----------|----------|---------|----------------|
| 1 | **Statut du document** | Draft vs cadre de référence nationale ? | G2 | **Recommandation** : Présenter comme « projet de cadre de référence » jusqu'à validation officielle |
| 2 | **Rôle de l'État comme financeur** | L'État peut-il être considéré comme financeur dans le RPI ? | G3 | **Recommandation** : Oui, clarifier le rôle de l'État |
| 3 | **Neuf critères cumulatifs** | Sont-ils tous cumulatifs ? | G1 | **Recommandation** : Oui, les expliciter comme cumulatifs |
| 4 | **Portée du cadre** | Uniquement MSANP ou tout le secteur santé ? | G3 | **Recommandation** : Élargir à « secteur santé à Madagascar » |
| 5 | **Nom du Ministère** | « Santé Publique » ou « en charge de la Santé » ? | G1 | **Recommandation** : Utiliser la dénomination officielle actuelle |

Ces arbitrages sont distincts des amendements : ils nécessitent une **décision de gouvernance** plutôt qu'une correction rédactionnelle. Le processus de décision devrait impliquer les mêmes instances qui validationont le CAESN (Comité National d'Architecture, DEPSI).


## 7. Recommandations

### 7.1 Priorisation des amendements

**Priorité 1 - Bloqueurs (avant validation)**
1. PDSS 2020-2024 → PDSS 2026-2030 (validé, 4 groupes)
2. Insérer PNS 2025-2030 (G3)
3. « malagasy » → reformuler (G1, G3)
4. Ministère de la Santé Publique → dénomination actuelle (G1)
5. Rédiger glossaire complet avec capabilité, FOSA, architecture runway, steward de données
6. Résoudre incohérence CAP-13 dans glossaire (G1, G3)

**Priorité 2 - Important (pour amendement)**
1. Compléter ou retirer les annexes E-J
2. Harmoniser définition de « capabilité » (corps vs glossaire)
3. Mettre à jour la gestion de version
4. Produire la matrice RACI de gouvernance des données
5. Définir les responsabilités des acteurs
6. Standardiser la chaîne de valeur des initiatives
7. Instaurer un scoring d'évaluation (0-4)
8. Ajouter les indicateurs manquants (VS-02, VS-03, VS-04)

**Priorité 3 - Souhaitable (pour amélioration continue)**
1. Créer un schéma du modèle de capabilités
2. Schématiser les 6 couches du paysage applicatif
3. Formaliser la méthode de priorisation des capabilités
4. Définir les critères de chaque niveau de maturité
5. Ajouter une phrase introductive aux référentiels normatifs internationaux
6. Clarifier le workflow entre validation portefeuille et homologation technique
7. Introduire les rôles Data Owner / Data Steward

### 7.2 Processus de révision recommandé

1. **Phase 1** : Corrections immédiates (PDSS, PNS, « malagasy », Ministère)
2. **Phase 2** : Rédaction du glossaire
3. **Phase 3** : Complétion des annexes
4. **Phase 4** : Harmonisation terminologique
5. **Phase 5** : Structure de gouvernance (RACI, rôles)
6. **Phase 6** : Flux de valeur et indicateurs
7. **Phase 7** : Portefeuille et scoring
8. **Phase 8** : Relecture et validation finale


## 8. Annexe - Matrice de traçabilité

### Légende
- ✓ = Observation présente dans ce groupe
- - = Pas d'observation de ce groupe

| Thème | G1 | G2 | G3 | G4 |
|-------|----|----|----|-----|
| PDSS 2020→2026-2030 | ✓ | ✓ | ✓ | ✓ |
| PNS absente | - | - | ✓ | - |
| Glossaire/lexique | ✓ | ✓ | - | - |
| Annexes vides | ✓ | ✓ | ✓ | - |
| "malagasy" → reformuler | ✓ | - | ✓ | - |
| Ministère Santé Publique | ✓ | - | - | - |
| Architecture runway définition | ✓ | ✓ | - | - |
| Capabilité incohérence | ✓ | ✓ | - | - |
| Matrice RACI | ✓ | ✓ | ✓ | - |
| Responsabilités acteurs | ✓ | ✓ | ✓ | - |
| VS indicateurs manquants | - | ✓ | - | ✓ |
| VS terminology (réhabilitation) | - | ✓ | - | ✓ |
| Scoring d'évaluation | - | ✓ | - | - |
| Chaîne de valeur standardisée | - | ✓ | - | - |
| CAP-13 glossaire | ✓ | - | ✓ | - |
| Maturité capabilités | - | - | ✓ | - |
| Priorisation capabilités | - | - | ✓ | - |
| Schéma couches applicatives | - | - | ✓ | - |
| Portée du cadre | - | - | ✓ | - |
| CSU intégration | - | - | ✓ | - |
| Critères cumulatifs | ✓ | - | - | - |
| Gestion de version | - | ✓ | - | - |
| Référentiels normatifs | - | ✓ | ✓ | - |


*Document d'analyse CAESN - HEA-ANA-CAESN-001 - Version 2.0 - 30 août 2026*
