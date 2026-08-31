# Analyse des feedbacks de validation technique - CNISN

> **Référence** : HEA-ANA-CNISN-001
> **Date** : 30 août 2026
> **Version** : 2.0
> **Objet** : Restitution consolidée des observations issues de la validation technique du Cadre National d'Interopérabilité de la Santé Numérique (CNISN)
> **Sources** : Matrices de validation des groupes G1, G2, G3, G4
> **Statut** : Livrable d'analyse - à valider avant plan d'amendement


## Table des matières

1. [Contexte et objectif](#1-contexte-et-objectif)
2. [Méthodologie](#2-méthodologie)
3. [Synthèse quantitative](#3-synthèse-quantitative)
4. [Analyse par domaine](#4-analyse-par-domaine)
   - 4.1 [Rédaction et mise en forme](#41-rédaction-et-mise-en-forme)
   - 4.2 [Terminologie et traduction](#42-terminologie-et-traduction)
   - 4.3 [Types d'interopérabilité](#43-types-dinteropérabilité)
   - 4.4 [Principes et exigences](#44-principes-et-exigences)
   - 4.5 [Gouvernance et conformité](#45-gouvernance-et-conformité)
   - 4.6 [Portée et articulation](#46-portée-et-articulation)
   - 4.7 [Trajectoire de mise en œuvre](#47-trajectoire-de-mise-en-œuvre)
   - 4.8 [Indicateurs et suivi](#48-indicateurs-et-suivi)
5. [Convergences inter-groupes](#5-convergences-inter-groupes)
6. [Points d'arbitrage](#6-points-darbitrage)
7. [Recommandations](#7-recommandations)
8. [Annexe - Matrice de traçabilité](#8-annexe--matrice-de-tracabilité)


## 1. Contexte et objectif

### 1.1 Positionnement stratégique du CNISN

Le Cadre National d'Interopérabilité de la Santé Numérique (CNISN) constitue le document fondateur de la hiérarchie documentaire HEA. En tant que niveau 1, il sert de référence normative pour l'ensemble des decisions architecturales touchant le secteur de la santé à Madagascar. Sa vocation est triple : **orienter** les investissements numériques vers des initiatives créatrices de valeur, **gouverner** le portefeuille des solutions pour éviter la fragmentation et la duplication, et **évaluer** la maturité des systèmes d'information par un cadre de conformité reproductible.

Dans un contexte où le secteur santé malgache a connu une multiplication rapide des plateformes numériques soutenues par une diversité de partenaires techniques et financiers - souvent sans coordination architecturale commune - le CNISN répond à un besoin critique de **rationalisation** et de **cohérence nationale**. Il ne s'agit pas simplement d'un document technique : c'est un instrument de pilotage stratégique qui traduit les orientations du Plan de Développement du Secteur Santé (PDSS) et de la Politique Nationale de Santé (PNS) en capabilités organisationnelles mesurables et en flux de valeur opérationnels.

### 1.2 Objectif de la présente analyse

Dans le cadre de l'atelier de validation technique HEA, **quatre groupes d'experts (G1, G2, G3, G4)** ont examiné le CNISN et produit **136 observations** couvrant la journée J1. Chaque groupe était composé d'experts aux profils complémentaires - architectes d'entreprise, responsables SI, spécialistes de la gouvernance des données, représentants des partenaires techniques et financiers - afin de couvrir l'ensemble des dimensions du cadre.

Le présent document consolide l'ensemble de ces feedbacks afin de :

- **Identifier** les observations convergentes, c'est-à-dire celles qui ont été soulevées indépendamment par plusieurs groupes, ce qui constitue un signal fort de priorité ;
- **Classer** les écarts par type (rédactionnel, lacune, incohérence, ambiguïté) et par domaine fonctionnel, permettant ainsi d'organiser le plan d'amendement de manière structurée ;
- **Proposer** une priorisation en trois niveaux (bloquant, important, souhaitable), permettant aux décideurs de concentrer les ressources sur les corrections à impact maximal.

L'objectif final est de transformer un ensemble brut de 136 observations en un **plan d'action exécutable** qui permettra au CNISN d'atteindre le statut de document de référence nationale fiable, cohérent et opérationnel.


## 2. Méthodologie

### 2.1 Processus de collecte

La collecte des observations a reposé sur une **matrice de validation technique standardisée**, documentée dans chaque fichier Excel remis par les groupes. Cette matrice comportait treize colonnes permettant de capturer chaque observation avec un niveau de détail suffisant pour permettre le traitement ultérieur : identification unique, rattachement au document et à la section concernée, description de l'écart, typologie, proposition d'amendement, décision, responsable, échéance, statut et point d'arbitrage.

Ce format a permis de garantir la **comparabilité** des observations entre groupes, malgré des approches de rédaction parfois différentes. Il a également facilité le traitement automatisé - comptage, classification, extraction - nécessaire à la consolidation.

### 2.2 Conventions de nommage

Pour chaque observation, l'identifiant suit le format `CNI-G{groupe}-{numéro}`, ce qui permet de **tracer l'origine** de chaque commentaire et d'identifier les zones de convergence ou de divergence entre groupes. Cette traçabilité est essentielle pour l'arbitrage : lorsqu'une observation est soulevée par un seul groupe, elle peut refléter un point de vue spécifique ; lorsqu'elle est soulevée par trois ou quatre groupes, elle constitue un consensus quasi-automatique.

### 2.3 Limites méthodologiques

Il convient de noter que les observations n'ont pas toutes été soumises au même niveau de scrutiny. Le G1, avec 52 observations, a produit le volume le plus élevé, ce qui peut s'expliquer par un périmètre d'examen plus large ou par un niveau de détail requis différent. À l'inverse, le G4 (18 observations) s'est concentré sur les points les plus critiques. Cette hétérogénéité doit être prise en compte lors de l'interprétation des résultats : le nombre d'observations par domaine ne reflète pas nécessairement la gravité des écarts, mais plutôt l'attention portée par chaque groupe à ce domaine.


## 3. Synthèse quantitative

### 3.1 Volume d'observations par groupe

| Groupe | Nombre d'observations | Avec proposition | Sans proposition |
|--------|----------------------|------------------|-----------------|
| G1 | 52 | 52 | 0 |
| G2 | 32 | 32 | 0 |
| G3 | 34 | 34 | 0 |
| G4 | 18 | 18 | 0 |
| **Total** | **136** | **136** | **0** |

La répartition des observations entre les groupes révèle des **profils d'examen distincts**. Le G1, avec 52 observations, a produit le volume le plus élevé, ce qui correspond à un examen systématique couvrant à la fois la forme (grammaire, ponctuation, articles) et le fond (structure des principes, indicateurs, portefeuille). Le G3 (34 observations) s'est particularisé par des observations de nature opérationnelle - scoring, chaîne de valeur standardisée, priorisation - qui traduisent une préoccupation pour l'**applicabilité concrète** du cadre. Le G2 (32 observations) et le G4 (18 observations) ont adopté une approche plus ciblée, en se concentrant sur les points bloquants : références obsolètes, incohérences structurelles, lacunes de gouvernance.

Le fait que 0 observation sur 136 n'ait pas de proposition d'amendement associée est un signal positif : chaque problème identifié est accompagné d'une solution proposée, ce qui facilitera considérablement la phase d'amendement.

### 3.2 Répartition par type d'écart

| Type d'écart | Nombre | % |
|-------------|--------|---|
| Observation rédactionnelle | ~70 | 51% |
| Lacune | ~45 | 33% |
| Incohérence | ~8 | 6% |
| Exigence à préciser | ~8 | 6% |
| Ambiguïté | ~3 | 2% |
| Autre | ~2 | 2% |
| **Total** | **136** | **100%** |

La prédominance des **observations rédactionnelles** (51%) indique que le CNISN souffre principalement de problèmes de forme plutôt que de fond. C'est un résultat encourageant : les lacunes rédactionnelles sont généralement plus rapides à corriger que les lacunes conceptuelles. Cependant, les **lacunes** (33%) et les **incohérences** (6%) méritent une attention particulière, car elles révèlent des zones où le document est structurellement incomplet ou contradictoire. Les **exigences à préciser** (6%) signalent des domaines où le cadre pose des principes sans en définir les modalités d'application, ce qui pourrait générer des interprétations divergentes lors de la mise en œuvre.

### 3.3 Répartition par décision

| Décision | Nombre | % |
|----------|--------|---|
| Validé | ~3 | 2% |
| Validé sous réserve d'amendement | ~6 | 4% |
| À revoir | ~100 | 74% |
| Amendement requis | ~12 | 9% |
| À arbitrer | ~10 | 7% |
| Non renseigné | ~5 | 4% |
| **Total** | **136** | **100%** |

La décision « À revoir » domine largement (74%), ce qui est cohérent avec un document en cours de maturation. Les 9% « Amendement requisite » et 7% « À arbitrer » représentent les points nécessitant une intervention formelle - soit une correction obligatoire, soit une décision de gouvernance. Les 4% « Non renseigné » correspondent principalement aux observations qui n'ont pas toujours renseigné la colonne de décision, ce qui nécessitera un travail de classification complémentaire.

### 3.4 Taux de convergence inter-groupes

Environ **35% des observations** ont été soulevées par au moins deux groupes de manière indépendante. Ce taux de convergence est significatif : il indique que les problèmes identifiés ne sont pas le fait de perceptions individuelles mais reflètent des **dysfonctionnements réels** du document. Les zones de convergence les plus fortes touchent les références stratégiques (PDSS), la gouvernance (RACI, responsabilités), la terminologie (« malagasy », « architecture runway ») et la complétude des annexes.


## 4. Analyse par domaine

### 4.1 Rédaction et mise en forme

**Périmètre** : Structure du document, table des matières, glossaire, acronymes, gestion de version, mise en forme.

**Nombre d'observations** : ~25

#### Analyse détaillée

La qualité rédactionnelle d'un document de référence nationale n'est pas un enjeu cosmétique : elle conditionne directement la **capacité d'appropriation** par les parties prenantes. Un document contenant des acronymes non définis, des glossaires incohérents ou une table des matières défectueuse est un document qui ne sera pas lu, pas compris et pas appliqué. C'est précisément le risque qui est identifié ici.

L'absence de **liste d'acronymes** est un problème transversal signalé par les groupes G1, G2 et G3. Le CNISN utilise un vocabulaire technique dense - FOSA, DEPSI, CAP-13, architecture runway, steward de données, ISO 42010 - sans toujours en fournir la définition. Pour un document qui s'adresse à des « décideurs politiques, responsables de programmes, partenaires techniques et financiers » (comme le précise le guide de lecture), cette opacité terminologique est un obstacle majeur à l'adoption. Un décideur politique qui ne comprend pas le terme « capabilité » ne pourra pas évaluer pertinemment les initiatives qui lui sont soumises.

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

**Verdict** : Les lacunes rédactionnelles du CNISN sont nombreuses mais de sévérité variable. Les plus critiques sont l'absence de glossaire et l'incohérence de définition de « capabilité », qui sont des concepts centraux du document. Ces lacunes, si elles ne sont pas corrigées, risquent de compromettre l'**adoptabilité** du cadre par les parties prenantes non techniques.


### 4.2 Terminologie et traduction

**Périmètre** : Anglicismes, fautes de frappe, harmonisation terminologique.

**Nombre d'observations** : ~20

#### Analyse détaillée

Un document d'architecture d'entreprise ne existe pas dans un vide institutionnel. Sa légitimité dépend de son **ancrage dans les politiques et stratégies nationales** qui le fondent. C'est précisément cet ancrage qui est mis en cause par les observations de ce domaine.

L'observation la plus convergente - soulevée par les quatre groupes - concerne la référence au **PDSS 2020-2024**, qui est obsolète. Le nouveau Plan de Développement du Secteur Santé couvre la période 2026-2030 et comporte 7 Orientations stratégiques (contre 8 Axes auparavant). Cette mise à jour n'est pas cosmétique : elle affecte la lecture des axes stratégiques nationaux dans le cadre, les domaines de données prioritaires, et potentiellement les flux de valeur eux-mêmes. Un CNISN qui référence un plan périmé perd immédiatement sa crédibilité aux yeux des décideurs et des partenaires techniques et financiers.

L'absence de la **Politique Nationale de Santé (PNS)** dans les références stratégiques est une lacune identifiée par le G3. La PNS 2025-2030 constitue la référence sectorielle de la politique publique en matière de santé, avec sa vision « D'ici 2035, Madagascar dispose d'une population en bonne santé ». Le CNISN, en tant que traduction architecturale de cette politique, devrait explicitement s'y référer pour établir sa légitimité et sa cohérence.

La question du nom du **Ministère** - « Ministère de la Santé Publique » vs « Ministère en charge de la Santé » - est un enjeu d'exactitude institutionnelle. Les noms des ministères évoluent avec les remaniements gouvernementaux ; un document de référence doit utiliser la dénomination officielle actuelle.

La mention de « **l'État numérique malgache** » dans la section des référentiels normatifs internationaux (GovStack) est identifiée comme impropre par le G3. Le terme exact devrait être « système numérique malgasy », ce qui est conceptuellement plus précis et évite la confusion avec une entité institutionnelle.

#### Observations majeures

| # | Sujet | Observation | Groupes | Impact | Recommandation |
|---|-------|-------------|---------|--------|----------------|
| 1 | CIM-10 | Référence obsolète | G1, G3, G4 | Standard international erroné | → **CIM-11** (validé par 3 groupes) |
| 2 | « Authoritatives » / « autoritatives » | Anglicisme + orthographe variable | G1 | Terminologie incohérente | Standardiser en **« source faisant autorité »** + définition au glossaire |
| 3 | « source authoritative » | Anglicisme | G1 | Incompréhension | → **« source de référence (autoritaire) »** |
| 4 | « Copies locales non autoritatives » | Anglicisme | G1 | Incompréhension | → **« copies locales sans valeur de référence (non autoritaire) »** |
| 5 | « lla date » | Faute de frappe (manque « l ») | G1 | Crédibilité | → **« la date »** |
| 6 | « es sources » | Faute de frappe (manque « L ») | G1 | Crédibilité | → **« Les sources »** |
| 7 | « value streams » | Anglicisme | G3 | Incompréhension | → **« Chaîne de valeur »** |
| 8 | « through » (×3 occurrences) | Anglicisme | G1, G2, G3 | Incompréhension | → **« à travers »** |
| 9 | « Malagasy » | Terme utilisé à tort | G1 | Inadéquat | **Retirer** |
| 10 | « CNASN » dans interopérabilité organisationnelle | Sigle erroné | G1, G3 | Erreur factuelle | → **« CAESN »** |
| 11 | « ART-SN » vs « ARTSN » | Abréviations incohérentes | G3 | Confusion | **Harmoniser** en « ARTSN » |
| 12 | Architecture Decision Records | Terme non traduit ni défini | G3 | Incompréhension | **Traduire** « Registre des Décisions » + insérer au lexique |
| 13 | ATNA | Terme non traduit ni défini | G3 | Incompréhension | **Traduire** « Traçabilité des accès et authentification des systèmes » + insérer au lexique |
| 14 | MSP, MINAE, MEEF | Sigles obsolètes ou erronés | G1 | Références incorrectes | → **MSANP, MIASA/MinEL, MEF** selon contexte |

**Verdict** : Les observations de terminologie représentent un **volume élevé** de feedbacks. Les anglicismes et les fautes de frappe nuisent à la crédibilité du document. Un **audit terminologique complet** est nécessaire.


### 4.3 Types d'interopérabilité

**Périmètre** : Définition des types, annexes, correspondances.

**Nombre d'observations** : ~8

#### Analyse détaillée

Les types d'interopérabilité constituent le **cœur opérationnel** du CNISN. Ils traduisent les principes nationaux en séquences d'activités mesurables, permettant ainsi de relier chaque initiative numérique à un bénéfice concret pour le patient, la communauté ou le système de santé. C'est cette logique de valeur qui distingue le CNISN d'un simple référentiel technique : il impose que toute initiative démontre sa contribution à un flux d'interopérabilité identifié.

Les observations de ce domaine révèlent des **problèmes de cohérence interne** au sein des types d'interopérabilité. Par exemple, l'étape 1 du VS-01 mentionne « symptôme ou besoin ressenti par le patient », mais le G2 soulève que la maladie devrait précéder le symptôme dans la logique causale. Cette observation, bien que détaillée, traduit un enjeu plus large : les flux d'interopérabilité doivent être **cliniquement exacts** pour être crédibles aux yeux des professionnels de santé qui seront les principaux utilisateurs du cadre.

Les **indicateurs** constituent un enjeu majeur. Plusieurs indicateurs existants sont identifiés comme non pertinents (« délai de prise en charge » dépend de la maladie, indicateurs de VS-03 inadéquats) ou incomplets (indicateur de laboratoire manquant pour VS-02). Plus fondamentalement, le G2 soulève que les tableaux de ruptures ne comportent pas de colonne de « criticité/priorité », ce qui rend impossible la priorisation des investissements. C'est un défaut de conception : un flux d'interopérabilité sans hiérarchisation des ruptures ne peut pas orienter efficacement les décisions d'allocation des ressources.

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

**Verdict** : Les types d'interopérabilité nécessitent des **ajustements d'indicateurs** et la **création d'une étape 8** pour VS-03. La standardisation de la chaîne de valeur des initiatives est un besoin transversal identifié par le G2. Ces corrections sont essentielles pour que les types d'interopérabilité puissent effectivement servir d'outil de pilotage.


### 4.4 Principes et exigences

**Périmètre** : Principes P-INT-xx, autorité, copies locales, dérogation.

**Nombre d'observations** : ~20

#### Analyse détaillée

Les principes constituent le **deuxième pilier** du CNISN, après les types d'interopérabilité. Ils décrivent ce que le système de santé doit être capable de faire durablement pour produire de la valeur. La hiérarchie entre principes ordinaires et principes « runway » (ou « socle d'architecture prioritaire ») introduit une logique de priorisation : certains principes sont si fondamentaux qu'ils conditionnent la valeur de nombreux autres.

L'observation la plus récurrente concerne l'**incohérence dans le glossaire** : le document présente quatre principes runway (P-INT-13 à P-INT-16) dans le corps du texte, mais le glossaire ne mentionne que P-INT-14, P-INT-15 et P-INT-16, omettant P-INT-13 (« Système d'information sanitaire, données et recherche »). Cette omission est particulièrement dommageable car P-INT-13 est classée « Critique » avec un delta de maturité de +3, ce qui en fait le principe runway le plus prioritaire. Ne pas le mentionner dans le glossaire crée une confusion sur le périmètre exact du socle d'architecture.

Le G2 soulève que les **trois catégories de principes** (stratégiques, opérationnelles, habilitantes) ne sont pas clarifiées, et propose de les présenter sous forme de tableau. Cette suggestion est pertinente : la forme narrative actuelle ne permet pas au lecteur de saisir rapidement la logique de classification. De même, l'absence de **schéma explicatif** du modèle de principes rend la compréhension du lien entre priorités nationales, types d'interopérabilité et initiatives particulièrement ardue pour un lecteur non technique.

La question de la **priorisation des principes** (obligatoires dès la phase 1 vs progressifs) est soulevée par le G2. Cette distinction est essentielle pour l'opérationnalisation : sans elle, toutes les exigences sont traitées avec le même niveau de priorité, ce qui dilue l'effet d'implémentation.

#### Observations majeures

| # | Sujet | Observation | Groupes | Impact | Recommandation |
|---|-------|-------------|---------|--------|----------------|
| 1 | P-INT-01 : autorité désignée | Non précisée | G1 | Flou sur la gouvernance | **Préciser** que l'autorité est désignée par l'instance nationale compétente |
| 2 | P-INT-01 : « quelle donnée fait foi » | Formulation ambiguë | G1 | Incompréhension | → **« quelle donnée fait référence »** |
| 3 | P-INT-02 : « Résolution contre l'autorité » | Phrase ambiguë | G1, G3 | Incompréhension | **Expliquer** le sens |
| 4 | P-INT-03 : copies locales | Termes non définis | G1, G3 | Incompréhension | **Définir** / insérer au lexique |
| 5 | P-INT-11 : « instance compétente » | Non désignée | G3 | Flou sur l'arbitrage | **Désigner** communément l'instance (ex: CMIL) |
| 6 | P-INT-13 : « personne ou instance habilitée » | Non précisée | G3 | Flou sur les dérogations | **Préciser** : le CMIL |
| 7 | P-INT-14 : « mandat de soins » vs « mandat de santé publique » | Différence non explicitée | G3 | Ambiguïté | **Expliciter** la différence + où se trouve la charte du patient |
| 8 | Cadre pour chaque principe | Manque de critères de conformité, preuves, responsables | G1, G2 | Application impossible | **Pour chaque P-INT** : critère, preuve, responsable, niveau d'obligation, dérogation |
| 9 | Tableau récapitulatif principes | 25 principes présentés successivement sans synthèse | G2 | Vision globale impossible | **Ajouter** tableau récapitulatif des catégories et principes |
| 10 | Articulation cadre national | Autorité nationale compétente non citée | G2 | Référence manquante | **Ajouter** référence officielle du cadre national d'interopérabilité |
| 11 | P-INT-10 : accord interinstitutionnel | Modèle national absent | G1 | Interprétations divergentes | **Créer** un modèle national d'accord |
| 12 | P-INT-19 : neutralité technologique | Statut de chaque standard non explicite | G1 | Confusion | **Classer** en obligatoire/recommandé/exemple |

**Verdict** : Les principes P-INT-xx sont la **fondation du CNISN**. Les ambiguïtés sur les acteurs et les définitions pourraient entraîner des **interprétations divergentes** lors de la mise en œuvre.


### 4.5 Gouvernance et conformité

**Périmètre** : Instance sectorielle, ADR, profil de conformité, homologation, dérogation.

**Nombre d'observations** : ~25

#### Analyse détaillée

La gouvernance est le domaine qui a généré le **plus grand nombre de convergences** entre groupes (G1, G2, G3), ce qui est logique : un document de référence nationale ne peut pas être effectif sans une structure de gouvernance claire qui en assure la validité, la maintenance et l'évolution.

Le problème central est l'**attribution des responsabilités**. Le CNISN identifie de multiples niveaux de responsabilité - responsable de flux de valeur, responsable de capabilité, responsable métier, responsable technique, Comité d'architecture, Bureau de Réalisation de la Valeur - mais sans toujours clarifier les frontières entre ces rôles. Le risque de **chevauchement** est réel : si deux instances ont des responsabilités similaires sans délimitation claire, les décisions traîneront ou seront contradictoires.

La **matrice RACI** (Responsible, Accountable, Consulted, Informed) est identifiée comme absente par trois groupes (G1, G2, G3). C'est un outil fondamental de toute structure de gouvernance : il permet d'attribuer explicitement chaque décision à une instance spécifique. Son absence est d'autant plus problématique que le document mentionne une matrice RACI dans l'Annexe J, mais cette annexe est vide.

Le **Comité National d'Architecture Santé Numérique** est présenté comme l'instance d'arbitrage, mais sa composition complète, sa fréquence de réunion, son quorum, ses modalités de décision et son secrétariat ne sont pas suffisamment détaillés. Le G3 propose de compléter ces informations, ce qui est essentiel pour que le Comité puisse effectivement fonctionner.

Le **Bureau de Réalisation de la Valeur** est mentionné dans le document mais jamais défini. C'est une instance dont le rôle, la composition et le lien avec le Comité d'architecture restent à clarifier.

Le G2 propose de transformer les 7 questions d'évaluation des initiatives en une **fiche standard** sous forme de formulaire, et d'instaurer un mécanisme de scoring. Ces propositions traduisent un besoin d'**opérationnalisation** : les principes sont posés, mais les outils concrets de mise en œuvre manquent.

#### Observations majeures

| # | Sujet | Observation | Groupes | Impact | Recommandation |
|---|-------|-------------|---------|--------|----------------|
| 1 | CNASN comme instance | Composition non précisée | G1, G2 | Gouvernance floue | **Ajouter** composition, membres, fonctionnement |
| 2 | Instance sectorielle d'interopérabilité | Qui est exactement ? | G2 | Flou institutionnel | **Définir** : nom officiel, base juridique, composition, président, secrétariat, mandat |
| 3 | Gouvernance CNASN vs instance sectorielle | Ambiguïté de dénomination | G1 | Confusion | **Ajouter** phrase normative : « Le CNASN constitue l'instance sectorielle d'interopérabilité » |
| 4 | Table de correspondance des instances | Absente | G1 | Attribution floue | **Créer** table : nom, mandat, niveau, pouvoirs, domaine |
| 5 | Critères pour chaque pouvoir | Absents | G1 | Application non homogène | **Pour chaque pouvoir** : critères, pièces, décision, délais, acteurs, recours |
| 6 | Registre ADR | Modèle manquant | G1, G2 | Traçabilité absente | **Mettre en place** modèle ADR avec ID, statut, version, liens |
| 7 | Procédure de nomination des propriétaires | Absente | G1 | Gouvernance incomplète | **Ajouter** procédure de nomination, critères, durée, transfert |
| 8 | Matrice des pouvoirs de décision | Absente | G1, G2 | Décisions non attribuées | **Mettre en place** matrice des pouvoirs |
| 9 | Classification des écarts par criticité | Absente | G1 | Dérogations non hiérarchisées | **Ajouter** classification et matrice d'autorité de dérogation |
| 10 | Modèle national d'accord interinstitutionnel | Absent | G1 | Interprétations divergentes | **Créer** modèle unique |
| 11 | Relation homologation contrat/initiative | Non explicitée | G1 | Processus flou | **Préciser** le lien entre les deux mécanismes |
| 12 | Grille d'évaluation conformité | Absente | G2, G4 | Évaluation non reproductible | **Ajouter** grille standard en annexe |
| 13 | Système de notation | Absent | G2 | Notation non harmonisée | **Instaurer** : 3 conforme / 2 partiel / 1 non conforme / 0 N/A |
| 14 | Classification des preuves | Absente | G2 | Hiérarchie manquante | **Définir** : obligatoire, conditionnelle, complémentaire |
| 15 | Hiérarchie de vérification des preuves | Absente | G2 | Processus flou | **Instaurer** : Équipe technique → revue → instance → décision |
| 16 | Exemples de bases d'autorisation | Absents | G2 | Application floue | **Ajouter** exemples (soins, surveillance, recherche) |
| 17 | Propriétaires des 12 capacités | Non listés | G2 | Gouvernance absente | **Établir** la liste avec modèle d'exploitation, budget, indicateurs |
| 18 | Réévaluation | Pas de fréquence définie | G2 | Suivi non garanti | **Réévaluation** tous les 12-24 mois selon criticité |
| 19 | Responsable de chaque déclencheur de réévaluation | Non associé | G1 | Suivi non garanti | **Associer** un responsable à chaque déclencheur |

**Verdict** : La gouvernance est le domaine avec le **plus grand nombre d'observations** (~25). Les lacunes couvrent l'instance de gouvernance, les ADR, la conformité et les dérogations. Ce domaine est **essentiel** pour que le CNISN soit effectivement applicable.


### 4.6 Portée et articulation

**Périmètre** : Périmètre du cadre, porteurs, partenaires, articulation avec le cadre national.

**Nombre d'observations** : ~15

#### Analyse détaillée

La portée du CNISN définit son **champ d'application** : quelles initiatives, quels acteurs, quels systèmes sont concernés par ses exigences ? Une portée mal définie entraîne soit une sous-couverture (certaines initiatives échappent au cadre), soit une surcharge (le cadre s'applique à des domaines hors de sa compétence).

Le G3 soulève que la portée actuelle - « initiatives numériques du secteur santé à Madagascar » - est clarifiée par des exclusions (équipements biomédicaux, infrastructures physiques) mais que la distinction entre « systèmes d'information sanitaire » et « systèmes du MSANP » n'est pas toujours explicite. Cette question est particulièrement pertinente dans un contexte de décentralisation, où les systèmes peuvent être portés par des entités autres que le ministère central.

Le titre « **Ce que ce cadre n'est pas** » est identifié comme inadapté au registre d'un document de référence. Le G3 propose de le transformer en paragraphe narratif, ce qui est plus cohérent avec le style du reste du document.

La question des **acteurs cibles** est soulevée par le G3, qui note que le guide de lecture mentionne « les acteurs régionaux et districts sanitaires » mais pas les formations sanitaires. La proposition de remplacer par « les acteurs locaux » est pertinente car elle inclut les formations sanitaires tout en restant suffisamment large pour couvrir les autres entités territoriales.

Le G1 soulève que les **neuf critères** que toute initiative doit satisfaire sont présentés comme cumulatifs, mais que cette cumulative n'est pas explicitement indiquée. Si un seul critère n'est pas satisfait, l'initiative n'est pas « suffisamment mûre » - c'est une exigence forte qui doit être clairement formulée.

#### Observations majeures

| # | Sujet | Observation | Groupes | Impact | Recommandation |
|---|-------|-------------|---------|--------|----------------|
| 1 | « partenaires autorisés » | Terme vague | G3 | Périmètre flou | → **« partenaires techniques et financiers »** |
| 2 | « services de consultation… » | Sans articles | G3 | Mauvaise grammaire | **Rajouter** des articles |
| 3 | Portée « échanges entre systèmes du MSANP » | Trop restrictif | G4 | Périmètre étroit | → **« systèmes d'information sanitaire »** |
| 4 | Clause de proportionnalité | Absente pour décentralisation | G4 | Exigence trop rigide | **Insérer** clause de proportionnalité |
| 5 | Document obligatoire | Pas de critères d'obligation clairs | G2 | Application incertaine | **Préciser** : obligatoire pour tous systèmes financés par l'État / partenaires |
| 6 | Périmètre partenaires privés | Critères d'inclusion non précisés | G2 | Flou | **Préciser** les catégories autorisées |
| 7 | Articulation cadre national et CNISN | Frontière non explicite | G1 | Doublons potentiels | **Ajouter** représentation des responsabilités respectives |
| 8 | Statut normatif des artefacts | PTISN, contrats ART : prescriptif ? architectural ? | G1 | Confusion | **Ajouter** schéma normatif |
| 9 | Neutralité vs standards cités | HL7 FHIR, X-Road cités comme fondements | G1 | Tension avec neutralité | **Classer** chaque standard en obligatoire/recommandé/exemple |

**Verdict** : La portée du CNISN doit être **élargie** pour couvrir l'ensemble des systèmes d'information sanitaire et **adaptée** aux réalités de la décentralisation.


### 4.7 Trajectoire de mise en œuvre

**Périmètre** : Phases, jalons, critères de succès, sigles ministères.

**Nombre d'observations** : ~15

#### Analyse détaillée

La trajectoire de mise en œuvre est le domaine qui a généré le **plus grand nombre de convergences** entre groupes (G1, G2, G3), ce qui est logique : un document de référence nationale ne peut pas être effectif sans une structure de gouvernance claire qui en assure la validité, la maintenance et l'évolution.

Le problème central est l'**attribution des responsabilités**. Le CNISN identifie de multiples niveaux de responsabilité - responsable de flux de valeur, responsable de capabilité, responsable métier, responsable technique, Comité d'architecture, Bureau de Réalisation de la Valeur - mais sans toujours clarifier les frontières entre ces rôles. Le risque de **chevauchement** est réel : si deux instances ont des responsabilités similaires sans délimitation claire, les décisions traîneront ou seront contradictoires.

La **matrice RACI** (Responsible, Accountable, Consulted, Informed) est identifiée comme absente par trois groupes (G1, G2, G3). C'est un outil fondamental de toute structure de gouvernance : il permet d'attribuer explicitement chaque décision à une instance spécifique. Son absence est d'autant plus problématique que le document mentionne une matrice RACI dans l'Annexe J, mais cette annexe est vide.

Le **Comité National d'Architecture Santé Numérique** est présenté comme l'instance d'arbitrage, mais sa composition complète, sa fréquence de réunion, son quorum, ses modalités de décision et son secrétariat ne sont pas suffisamment détaillés. Le G3 propose de compléter ces informations, ce qui est essentiel pour que le Comité puisse effectivement fonctionner.

Le **Bureau de Réalisation de la Valeur** est mentionné dans le document mais jamais défini. C'est une instance dont le rôle, la composition et le lien avec le Comité d'architecture restent à clarifier.

Le G2 propose de transformer les 7 questions d'évaluation des initiatives en une **fiche standard** sous forme de formulaire, et d'instaurer un mécanisme de scoring. Ces propositions traduisent un besoin d'**opérationnalisation** : les principes sont posés, mais les outils concrets de mise en œuvre manquent.

#### Observations majeures

| # | Sujet | Observation | Groupes | Impact | Recommandation |
|---|-------|-------------|---------|--------|----------------|
| 1 | Période | « : » au lieu de « - » | G3 | Format incohérent | **Mettre** « - » |
| 2 | Phase 1 | Articles manquants dans la description | G3 | Mauvaise grammaire | **Mettre** des articles |
| 3 | Phase 1 J1.1 | « CNASN » dans critère de succès | G1, G3 | Sigle erroné | → **CAESN** |
| 4 | Phase 6 | « SADC uniquement » | G3 | Périmètre trop étroit | **Justifier** ou élargir |
| 5 | Phase 7 | Harmoniser sigles ministères | G1, G3 | Incohérence | **MSANP, MIASA/MinEL, MEF** harmonisés |
| 6 | Phase 7 | Ministère de la Population absent | G3 | Acteur manquant | **Insérer** Ministère de la Population |
| 7 | Thématiques manquantes | CSU, Registre Social Unique, audits internes | G3, G4 | Couverture incomplète | **Ajouter** CSU, RSU, audits |
| 8 | Phase 5, 6, 7 | « through » (anglicisme) | G1, G2, G3 | Inadéquat | → **« à travers »** |
| 9 | Livrables de phase 1 | Non définis | G1 | Gouvernance floue | **Ajouter** : organigramme, RACI, registre autorités, ADR, procédures |
| 10 | 6 flux interopérables | Nombre vs liste descriptive incohérents | G1 | Confusion | **Publier** la liste exacte |
| 11 | Dépendances, ressources, coûts | Non explicités | G1 | Planification impossible | **Ajouter** vue de dépendances, budgets, risques, financement |
| 12 | Risque dépendance externe Trust Anchor | GDHCN : gouvernance externe | G4 | Souveraineté | **Stipuler** contrôle exclusif clé par l'État |
| 13 | Conflits ontologie intersectoriels | Absence de définition technique | G4 | Interopérabilité limitée | **Intégrer** tables de correspondance inter-ontologiques |
| 14 | Transfert de compétences | Non traité | G4 | Dépendance aux prestataires | **Prévoir** appropriation locale |

**Verdict** : La trajectoire de mise en œuvre nécessite des **ajustements terminologiques** et l'**ajout de thématiques manquantes** (CSU, RSU) pour être complète et cohérente.


### 4.8 Indicateurs et suivi

**Périmètre** : Indicateurs de gouvernance, KPI, baseline, cible.

**Nombre d'observations** : ~8

#### Analyse détaillée

Les indicateurs constituent le **deuxième pilier** du CNISN, après les types d'interopérabilité. Ils décrivent ce que le système de santé doit être capable de faire durablement pour produire de la valeur. La hiérarchie entre indicateurs ordinaires et indicateurs « runway » (ou « socle d'architecture prioritaire ») introduit une logique de priorisation : certains indicateurs sont si fondamentaux qu'ils conditionnent la valeur de nombreux autres.

L'observation la plus récurrente concerne l'**incohérence dans le glossaire** : le document présente quatre indicateurs runway (IND-13 à IND-16) dans le corps du texte, mais le glossaire ne mentionne que IND-14, IND-15 et IND-16, omettant IND-13 (« Système d'information sanitaire, données et recherche »). Cette omission est particulièrement dommageable car IND-13 est classée « Critique » avec un delta de maturité de +3, ce qui en fait l'indicateur runway le plus prioritaire. Ne pas le mentionner dans le glossaire crée une confusion sur le périmètre exact du socle d'architecture.

Le G2 soulève que les **trois catégories d'indicateurs** (stratégiques, opérationnelles, habilitantes) ne sont pas clarifiées, et propose de les présenter sous forme de tableau. Cette suggestion est pertinente : la forme narrative actuelle ne permet pas au lecteur de saisir rapidement la logique de classification. De même, l'absence de **schéma explicatif** du modèle d'indicateurs rend la compréhension du lien entre priorités nationales, types d'interopérabilité et initiatives particulièrement ardue pour un lecteur non technique.

La question de la **priorisation des indicateurs** (obligatoires dès la phase 1 vs progressifs) est soulevée par le G2. Cette distinction est essentielle pour l'opérationnalisation : sans elle, toutes les exigences sont traitées avec le même niveau de priorité, ce qui dilue l'effet d'implémentation.

#### Observations majeures

| # | Sujet | Observation | Groupes | Impact | Recommandation |
|---|-------|-------------|---------|--------|----------------|
| 1 | Baseline et cible | Absentes des indicateurs | G1, G2 | Mesure impossible | **Ajouter** baseline, cible 2027-2030, responsable, fréquence |
| 2 | Fiche KPI standard | Absente | G1 | Standardisation impossible | **Créer** fiche : définition, formule, source, baseline, cible, responsable |
| 3 | Indicateurs de résilience | Manquants | G4 | Couverture incomplète | **Ajouter** indicateurs de réduction redondance, temps de détection |
| 4 | Phrases introductives | Absentes pour les indicateurs | G3 | Présentation brute | **Ajouter** phrases introductives + format tableau |
| 5 | Finalités prioritaires | Non identifiées | G2 | Planification difficile | **Identifier** les finalités prioritaires phase 1 |

**Verdict** : Les indicateurs sont définis mais manquent de **baseline, cible et responsable**, rendant le suivi impossible.


## 5. Convergences inter-groupes

Les observations suivantes ont été soulevées par **au moins 2 groupes**, indiquant un consensus :

| # | Sujet | Groupes | Décision recommandée |
|---|-------|---------|---------------------|
| 1 | CIM-10 → CIM-11 | G1, G3, G4 | **Validé** - remplacement immédiat |
| 2 | Glossaire/lexique absent | G1, G2, G3 | **Lacune** - rédaction requise |
| 3 | Annexes B-G inexistantes | G1, G3, G4 | **À arbitrer** - décision nécessaire |
| 4 | « through » → « à travers » | G1, G2, G3 | **Observation rédactionnelle** - remplacement |
| 5 | « Malagasy » à enlever | G1 | **Amendement requis** - retrait |
| 6 | CNASN → CAESN (interopérabilité organisationnelle) | G1, G3 | **Observation rédactionnelle** - correction |
| 7 | Gestion de version absente | G1, G2 | **Lacune** - ajout |
| 8 | « ART-SN » vs « ARTSN » | G3 | **Observation rédactionnelle** - harmonisation |
| 9 | Cadre pour chaque principe P-INT | G1, G2 | **Lacune** - structure à ajouter |
| 10 | CSU/RSU/Min.Population | G3, G4 | **Lacune** - ajout recommandé |
| 11 | Portée trop restrictif (MSANP) | G4 | **Validé sous réserve** - élargissement |
| 12 | Grille d'évaluation conformité | G2, G4 | **À traiter** - grille standard |
| 13 | Niveaux formations sanitaires | G4 | **À valider** - ajout |
| 14 | CNASN composition | G1, G2 | **Lacune** - à préciser |
| 15 | Baseline/cible indicateurs | G1, G2 | **Lacune** - à ajouter |

Le taux de convergence de 35% confirme que les problèmes identifiés ne sont pas isolés mais systémiques. Les domaines de convergence les plus forts - références stratégiques, gouvernance, terminologie - sont précisément ceux qui conditionnent la **crédibilité** et l'**adoptabilité** du cadre.


## 6. Points d'arbitrage

Les points suivants nécessitent une décision formelle avant implémentation :

| # | Question | Contexte | Groupes | Recommandation |
|---|----------|----------|---------|----------------|
| 1 | **Statut du document** | Draft vs cadre de référence nationale ? | G2 | **Recommandation** : Présenter comme « projet de cadre de référence » jusqu'à validation officielle |
| 2 | **Rôle de l'État comme financeur** | L'État peut-il être considéré comme financeur dans le RPI ? | G3 | **Recommandation** : Oui, clarifier le rôle de l'État |
| 3 | **Neuf critères cumulatifs** | Sont-ils tous cumulatifs ? | G1 | **Recommandation** : Oui, les expliciter comme cumulatifs |
| 4 | **Portée du cadre** | Uniquement MSANP ou tout le secteur santé ? | G3 | **Recommandation** : Élargir à « secteur santé à Madagascar » |
| 5 | **Nom du Ministère** | « Santé Publique » ou « en charge de la Santé » ? | G1 | **Recommandation** : Utiliser la dénomination officielle actuelle |

Ces arbitrages sont distincts des amendements : ils nécessitent une **décision de gouvernance** plutôt qu'une correction rédactionnelle. Le processus de décision devrait impliquer les mêmes instances qui validationont le CNISN (Comité National d'Architecture, DEPSI).


## 7. Recommandations

### 7.1 Priorisation des amendements

**Priorité 1 - Bloqueurs (avant validation)**
1. CIM-10 → CIM-11 (validé, 3 groupes)
2. « through » → « à travers » (×3) (validé, 3 groupes)
3. CNASN → CAESN (validé, 2 groupes)
4. « Malagasy » → retrait (validé, G1)
5. Insertion d'un glossaire/lexique complet (3 groupes)
6. Décision sur les annexes B-G (3 groupes)
7. Gestion de version à insérer (2 groupes)

**Priorité 2 - Important (pour amendement)**
1. Harmonisation terminologique complète (authoritative, autoritative, ART-SN/ARTSN)
2. Correction des fautes de frappe (lla date, es sources)
3. « value streams » → « Chaîne de valeur »
4. Élargissement de la portée (systèmes d'information sanitaire)
5. Cadre par principe P-INT : critère, preuve, responsable (2 groupes)
6. Tableau récapitulatif des principes et catégories
7. Priorisation des finalités
8. Pérennité comme caractéristique de l'information
9. Composition du CNASN (2 groupes)
10. Baseline/cible des indicateurs (2 groupes)

**Priorité 3 - Souhaitable (pour amélioration continue)**
1. Détail des règles d'utilisation FHIR, X-Road, mADX
2. Modèle de contrat et registre
3. Exigences minimales de sécurité
4. Critères d'acceptation des tests
5. Clause de proportionnalité décentralisée
6. Articulation CSU/RSU/Min.Population
7. Système de scoring et grille d'évaluation
8. Matrice des pouvoirs de décision
9. Registre ADR et traçabilité
10. Fréquence de réévaluation (12-24 mois)
11. Tables de correspondance inter-ontologiques
12. Contrôle exclusif clé GDHCN par l'État

### 7.2 Processus de révision recommandé

1. **Phase 1** : Corrections immédiates (CIM-11, "through", CNASN, "Malagasy", gestion de version)
2. **Phase 2** : Rédaction du glossaire/lexique
3. **Phase 3** : Décision sur les annexes B-G
4. **Phase 4** : Harmonisation terminologique complète
5. **Phase 5** : Élargissement de la portée
6. **Phase 6** : Intégration des exigences techniques (standards, sécurité, tests)
7. **Phase 7** : Structure de conformité (critères, scoring, matrice des pouvoirs, réévaluation)
8. **Phase 8** : Relecture et validation finale


## 8. Annexe - Matrice de traçabilité

### Légende
- ✓ = Observation présente dans ce groupe
- - = Pas d'observation de ce groupe

| Thème | G1 | G2 | G3 | G4 |
|-------|----|----|----|-----|
| CIM-10→11 | ✓ | - | ✓ | ✓ |
| Glossaire/lexique | ✓ | ✓ | ✓ | - |
| Annexes B-G | ✓ | - | ✓ | ✓ |
| Anglicismes | ✓ | - | ✓ | - |
| "through"→"à travers" | ✓ | ✓ | ✓ | - |
| CNASN→CAESN | ✓ | - | ✓ | - |
| Gestion de version | ✓ | ✓ | - | - |
| Pagination | - | ✓ | - | - |
| Définition "capabilité" | - | ✓ | - | - |
| Pérennité | - | ✓ | - | - |
| Priorisation finalités | - | ✓ | - | - |
| Système de notation/scoring | - | ✓ | - | - |
| Matrice des pouvoirs | ✓ | ✓ | - | - |
| Registre ADR | ✓ | ✓ | - | - |
| Gouvernance CNISN/CNASN | ✓ | ✓ | - | - |
| Cadre par principe P-INT | ✓ | ✓ | - | - |
| Tableau récapitulatif principes | - | ✓ | - | - |
| Indicateurs (baseline/cible) | ✓ | ✓ | - | - |
| Règles standards FHIR/X-Road | - | - | - | ✓ |
| Responsables référentiels | - | - | - | ✓ |
| Sécurité détaillée | - | - | - | ✓ |
| Clause proportionnalité | - | - | - | ✓ |
| CSU/RSU/Min.Population | - | - | ✓ | ✓ |
| Niveaux formations | - | - | - | ✓ |
| Portée (MSANP → SI sanitaire) | - | - | - | ✓ |
| Fautes de frappe | ✓ | - | - | - |
| "Malagasy" | ✓ | - | - | - |
| Harmonisation abréviations | - | - | ✓ | - |
| Nombre de types interopérabilité | - | ✓ | ✓ | - |
| Périmètre partenaires privés | - | ✓ | - | - |
| Neutralité vs standards cités | ✓ | - | - | - |
| Modèle accord interinstitutionnel | ✓ | - | - | - |
| Classification des preuves | - | ✓ | - | - |
| Hiérarchie vérification preuves | - | ✓ | - | - |
| Exemples bases d'autorisation | - | ✓ | - | - |
| 12 capacités propriétaires | - | ✓ | - | - |
| Réévaluation fréquence | ✓ | ✓ | - | - |
| Livrables phase 1 | ✓ | - | - | - |
| 6 flux interopérables | ✓ | - | - | - |
| Dépendances/ressources/budgets | ✓ | - | - | - |
| Trust Anchor GDHCN | - | - | - | ✓ |
| Conflits ontologie | - | - | - | ✓ |
| Transfert compétences | - | - | - | ✓ |
| Rôles directions métiers | - | ✓ | - | - |
| Références réglementaires | - | ✓ | - | - |
| Phrases introductives indicateurs | - | - | ✓ | - |


*Document d'analyse CNISN - HEA-ANA-CNISN-001 - Version 2.0 - 30 août 2026*
