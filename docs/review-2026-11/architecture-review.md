# Revue d'architecture : Cadre d'Architecture d'Entreprise de la Santé Numérique (HEA) de Madagascar

**Date :** 2026-11-21
**Version :** 1.0
**Objet :** Evaluation de l'architecture d'entreprise HEA en tant que référentiel national, indépendamment de l'état du code et de l'outillage.
**Périmètre :** Les quatre familles documentaires (00_caesn, 01_cnisn, 02_artsn, 03_ptisn), le référentiel objet 04_architecture-repository (369 objets), l'ontologie et les artefacts compilés.
**Sources :** Lecture directe du dépôt (documents, frontmatter des objets, ADR, registres, annexes, ontologie), exécution des validateurs du dépôt, benchmarks internes (comparaison 12 pays africains, ADHMAT, GDHM).
**Statut :** Revue d'expert, non homologuée. Document d'analyse externe, hors hiérarchie CAESN/CNISN/ARTSN/PTISN.
**Méthode :** Approche « risque et qualité » appliquée à un référentiel d'architecture. Chaque constat est adossé à une preuve localisée dans le dépôt. Les défauts de doctrine rédactionnelle sont distingués des défauts d'architecture.

## 1. Verdict

Ce référentiel est l'un des cadres d'architecture d'entreprise les plus aboutis que l'on puisse trouver dans le secteur de la santé numérique d'un pays à ressources contraintes. Sa conception stratégique, sa discipline de décision et son outillage de génération sont d'un niveau qu'atteignent rarement les ministères de la santé, y compris dans les pays à revenu élevé.

Le constat central de cette revue est le suivant : **le référentiel a devancé son autorité institutionnelle, et il a transformé cet avance en créance.** Le dépôt énonce des normes obligatoires « en vigueur », des décisions « appliquées » et des profils d'implémentation complets, alors que le cadre est explicitement consultatif, que le comité de gouvernance n'est pas constitué, que le programme de conformité ne démarre qu'en 2028 et que la loi qui donnerait force contraignante n'existe pas encore.

Autrement dit, la Madison architecture n'est pas le facteur d'échec. Le facteur d'échec est un **déficit de crédibilité de l'assertion** : le dépôt affirme plus fort que ce qu'il peut prouver. La preuve en est interne au dépôt lui-même : deux annexes du même dossier se contredisent sur l'évaluation internationale de Madagascar, un registre de décision « applique » des décisions dont le calendrier d'application est fixé deux ans plus tard, et les annexes de correspondance ne concordent pas avec le frontmatter qui est censé faire référence.

Ce que cela produit est concret et mesurable : chaque nouvel élément de détail ajouté au référentiel **réduit** sa crédibilité nette, parce qu'il augmente la surface d'affirmation sans augmenter la surface de preuve. C'est contre-intuitif, et c'est la principale décision que cette revue recommande de prendre.

## 2. Évaluation de la pertinence stratégique

### 2.1 La méthode de conception est la bonne

Le parti pris « Value-Driven Enterprise Architecture » est correctement mis en œuvre, et rarement. Le modèle national de valeur (`00_caesn/00_overview/value-model.md`) identifie huit bénéficiaires distincts, cinq dimensions de valeur et surtout une **chaîne causale exigée en neuf éléments** : priorité nationale, flux de valeur, étape, capacité, problème métier, bénéficiaire, bénéfice mesurable, responsable redevable, chaîne causale entre livrable technique et valeur produite.

C'est une discipline réelle. La plupart des cadres d'architecture d'entreprise partent du système d'information et remontent vers le métier ; celui-ci part du bénéficiaire et impose une démonstration de contribution. La conséquence est structurante : une initiative qui ne peut pas démontrer les neuf éléments n'est financeable ni déployable. C'est une règle d'élimination utile, et elle est formulée.

Le second indicateur de méthode juste est le **modèle de double gouvernance** (portefeuille plus homologation), separation des deux questions « est-ce que cela mérite d'être financé » et « est-ce que cela est conforme ». L'annexe comparative note que ce modèle est unique en Afrique. Il l'est, et il est correctement conçu : il évite que la pression de financement ne détermine la norme, et que la norme ne bloque le financement sans arbitrage.

### 2.2 La mesure de la valeur n'est pas outillée

Le modèle de valeur est déclaré, pas exploité. `00_caesn/03_capabilities/maturity.md` déclare lui-même : « Les niveaux ci-dessous sont une estimation de cadrage, à valider avec les directions métier et techniques. » Aucun niveau n'est daté, aucun n'est rattaché à une source, aucune direction métier n'a validé. Le tableau reste en `status: draft` sur un sujet qui devrait être l'ancrage de toute décision d'investissement.

La conséquence est directe : le delta de maturité, qui est le critère central de priorisation, est lui-même une estimation non étayée. On priorise sur la base d'un différentiel entre deux nombres non mesurés. Le Bureau de Réalisation de la Valeur (`00_caesn/07_governance/value-realization-office.md`) est l'instrument correct pour ce problème, mais il est sans mandat, sans dotation et sans équipe.

### 2.3 La chaîne de causalité est rompue au niveau 2

C'est le défaut structurel le plus important du référentiel, et il n'apparaît pas dans le rapport de cohérence interne, qui conclut à « clos ».

La hiérarchie attendue est VS (niveau 1) → CAP (niveau 1) → capacités d'interopérabilité (niveau 2) → chapitres ART (niveau 3) → profils PT (niveau 4). Le maillon manquant est le troisième. Les 16 capacités d'interopérabilité CAP-INT-01 à CAP-INT-16 ont été retirées du référentiel objet au cours du refactor TOGAF (traçable dans `04_architecture-repository/08_views/togaf/cap-int-migration.md`). Elles ont été remplacées par 36 objets de nature différente : blocs d'architecture d'architecture (ABB), patrons (PAT), contrats (AC), données de référence (RD), partitions (PART) et quinze exigences ponctuelles (REQ-TF, REQ-OH).

Le chapitre lui-même l'admet : `01_cnisn/02_capacites/index.md` s'ouvre désormais sur « Ce chapitre ne définit pas de nouvelles capacités nationales ». Le niveau 2 n'est donc plus une couche de capacités : c'est une couche de composants d'interopérabilité. Cela peut être un choix délibéré et défendable, mais trois choses n'ont pas suivi.

Premièrement, la documentation continue d'affirmer l'existence de 16 capacités d'interopérabilité en au moins cinq emplacements : `01_cnisn/index.md`, `01_cnisn/reading-guide.md` (dont le propre tableau n'en liste que 14), `01_cnisn/08_annexes/b-articulation-art-sn.md`, `f-articulation-complete.md` et `g-matrice-interop-types.md`. Un lecteur qui suit la trace affine lit une contradicción de compte à chaque niveau.

Deuxièmement, la gouvernance du niveau 2 exige huit attributs par capacité (finalité, périmètre, propriétaire institutionnel, niveau de maturité, dépendance, critère de conformité, référence normative, indicateurs), selon `01_cnisn/03_gouvernance/index.md`. Aucun des 36 objets ne porte ces attributs : pas de propriétaire autre que DEPSI, pas d'indicateur, pas de critère de conformité, pas de niveau de maturité.

Troisièmement, les annexes de correspondance ne sont plus alignées sur le frontmatter du référentiel, qu'elles prétendent pourtant refléter. `01_cnisn/08_annexes/e-correspondance-caesn.md` attribue à ABB-IDENTITE-BENEFICIAIRE les capacités CAP-02, 14 et 17, alors que le frontmatter porte CAP-01, 02, 04, 07, 14 et 17. Près de 26 objets (PAT, AC, REQ, TERM, RD) sont absents de cette annexe. L'annexe A et l'annexe E se contredisent sur les mêmes objets.

Cette situation n'est pas catastrophique, mais elle a un coût précis : **il n'existe plus d'entité intermédiaire responsable de la décomposition entre l'intention d'entreprise et la réalisation technique.** La question « cette capability CAP-13 du SIS est-elle réellement couverte par des contrats d'interopérabilité testables ? » n'a aujourd'hui personne à qui poser, et aucune traçabilité ne permet d'y répondre mécaniquement.

## 3. Évaluation de la maturité structurelle

### 3.1 Le référentiel objet est un vrai niveau 3 sur l'échelle ADM

Le passage à une source de vérité unique (04_architecture-repository, 369 objets, un objet par fichier) avec métamodèle explicite (`00_metamodel/schema.md`), modèle de relations typé et bidirectionnel calqué sur ArchiMate, et registre central indexé, constitue une avancée méthodologique réelle. Le modèle de relations couvre les treize concepts ArchiMate retenus avec leurs inverses, et les règles d'intégrité sont énoncées : pas de capacité orpheline, symétrie obligatoire de `uses` et `applies_to`, socle transverse atteint par les composants applicatifs et non directement par les processus.

Cette discipline est ce qui rend le reste possible. L'alignement des 18 capabilities, des 15 principes, des 4 flux de valeur, des 13 processus et des 25 composants applicatifs sur un graphe unique, avec un mini-outillage de validation qui détecte les îlots, est exactement ce que le modèle HEAF/HEART désigne comme « architecture pilotée par les ontologies ». Ici, l'idée est réellement implémentée et non seulement citée.

### 3.2 La traçabilité syntaxique est parfaite, la traçabilité sémantique n'est pas vérifiée

C'est le point le plus important de cette revue pour la suite. Le dépôt dispose de la meilleure vérification automatique de ce type qu'on puisse trouver dans un référentiel national de santé, et cette vérification porte sur la **forme** et non sur le **sens**.

Le pipeline garantit que chaque lien relatif résout, que chaque bloc généré est à jour, que le graphe RDF est conforme aux shapes SHACL, que les structures FHIR compilent, que les schémas JSON sont valides. Il ne garantit pas qu'un service pointe sur le bon objet de données. Et il ne le garantit pas, parce que les liens sont corrects mais erronés :

- Les six liens service vers composant et service vers objet de données sont décalés d'un cran. `SRV-01` s'appuie sur « le composant d'identité (cmp-08) », alors que cmp-08 est le référentiel clinique et que l'identité est cmp-11. `SRV-02` accède à DO-01 (Patient) au lieu de DO-03 (Dossier). `SRV-06` s'appuie sur CMP-12 « composant de pilotage », alors que le pilotage est CMP-01.
- Le catalogue cite des composants inexistants dans ce rôle : CMP-04 alimente « la facturation (CMP-10 : Registre des terminologies) » ; CMP-20 cite « les référentiels de médicaments normalisés (CMP-07) », or CMP-07 est le gestionnaire de Sagas.
- Les 22 chapitres ART portent tous `implements: []`. L'index chapitre vers profil est donc déduit, jamais déclaré.
- Les exigences ENF-1 à ENF-5 citent ART-9, ART-4C et ART-8C comme garanties, alors que ces trois chapitres sont en statut `candidate`.
- `ART-8` et `ART-8A` portent un texte normatif identique au caractère près. La déclinaison « ART-8x » est un procédé de classement, pas une différenciation de patron.
- `02_artsn/08_annexes/i-ptisn-artsn-alignement.md` affirme qu'« ART-8 n'est déclaré par aucun profil », ce qui est faux : PT-02 le déclare.

Le dépôt est donc **syntaxiquement irréprochable et sémantiquement non audité**. Un mécanisme de validation qui vérifie qu'un lien existe mais pas qu'il désigne la bonne cible donne une assurance Trompeuse : le « zéro lien cassé » affiché dans le rapport de cohérence inspire une confiance que les faits ne justifient pas.

### 3.3 Le catalogue de données n'est pas un modèle d'information canonique

Les 31 objets de données offrent la granularité, la discipline de codification et les métadonnées de traçabilité d'un vrai catalogue, mais pas la cohérence conceptuelle d'un modèle canonique.

La granularité est irrégulière : DO-04 (Épisode) et DO-05 (Consultation) se recouvrent sur la ressource FHIR `Encounter` ; DO-01 et DO-03 sur `Patient` ; DO-07 et DO-08 sur `ServiceRequest` ; DO-14 et DO-17 sur `CoverageEligibilityRequest` ; DO-18 et DO-22 sur `Flag`. Les contradictions entre prose et frontmatter existent dans les deux sens (DO-14 dit « FHIR Coverage » et porte `CoverageEligibilityRequest` ; DO-09 cite ServiceRequest, Transport et IPS et porte `Encounter`).

Le trou le plus coûteux est clinique : **il n'existe aucun objet Observation, Condition, Immunization, CarePlan ou Device.** Sans objets d'observation, de diagnostic, de vaccination et de prescription, le dossier de santé n'a pas de contenu. Les objets de notification, d'audit, de consentement et de terminologie, tous présentés comme exigences somewhere, n'existent pas non plus comme objets de données.

Sur le plan de la compilation, l'affirmation de l'annexe ODA est trop forte : `g-oda-conception-guide.md` annonce des payloads validant « types, formats, cardinalités, terminologies ». Sur 31 schémas JSON, **16 sont vides de tout champ métier** et ne contiennent que `id`, `version`, `statut` et des références. Un seul, `fosa-status.json`, est un véritable domaine de valeurs.

Et le catalogue n'est relié à rien : la feuille de route des lots ne référence aucun objet de données, et les six services de référence n'en référencent que quatre sur trente et un.

## 4. Évaluation des attributs de qualité

Les notations ci-dessous sont une appréciation d'expert, étayée par les engagements chiffrés du dépôt et non par une mesure d'exécution, puisque aucune implémentation n'existe encore.

| Attribut | Note | Fondement |
|----------|------|-----------|
| Interopérabilité | 4/5 | Noyau FHIR R4 + X-Road + mADX + IHE cohérent, 19 profils, protocole de test à 4 niveaux, ~40 scénarios codés, SHACL, compilation FHIR. Deux contradictions techniques non arbitrées. |
| Sécurité | 3,5/5 | Le domaine le plus riche : ART-7 est spécifique (AES-256, RBAC+ABAC, zéro confiance, AuditEvent, résidence). Aucun modèle de menace, aucune exigence d'autorisation d'API, aucun cycle de vie de clé. |
| Fiabilité | 3/5 | SLA chiffrés (disponibilité, P95, RTO/RPO, rétention 5 ans) et pile de supervision nommée. SLA ne couvrant que 11 profils sur 19, aucun pour le socle de terrain hors ligne. |
| Maintenabilité | 3/5 | Doc-as-code, versionnement sémantique, processus de dépréciation à 15 mois, idempotence vérifiée en CI. `implements` vide partout, aucune RACI de composant. |
| Scalabilité | 2/5 | Aucun modèle de charge, aucune dimensionnement, aucun partitionnement, 46 composants à instancier pour un pays où la connectivité est contrainte. |
| Observabilité | 1/5 | F.6 est une fondation sans composant, sans service, sans contrat et sans lot avant L5, alors que l'observabilité est nommée dans le modèle de valeur. |

### 4.1 L'observabilité est le trou le plus coûteux rapport à son importance

La fondation F.6 « Observabilité » figure dans le modèle de valeur comme garant de la capacité CAP-13 et CAP-16. Le document `02_artsn/08_annexes/e-sla-performance.md` décrit une pile complète : Prometheus, ELK, Jaeger, Grafana, une severity P1 à P4, une escalade SMS et téléphone. Aucun de ces éléments n'existe comme composant dans le référentiel, ni comme service, ni comme contrat d'interface, ni comme lot avant le lot L5, c'est-à-dire la fin de la trajectoire.

Il en va de même du composant de reprise après sinistre : des engagements RTO et RPO sont formulés sans qu'aucun composant, service ou procédure ne les porte. Dans une architecture où la perte de données de santé est irréversible, c'est une incohérence de première importance.

### 4.2 Deux contradictions techniques qu'un comité d'experts aurait vues à la première lecture

**FHIR contre PIXm/PDQm.** STD-0001 impose le FHIR R4 REST à « toutes les API échangeant des données de santé ». STD-0005 impose les profils IHE PIXm/PDQm pour la résolution d'identité. PIXm et PDQm ne sont pas des profils FHIR. Aucune règle de précédence, aucune clause de médiation n'arbitre. Un fournisseur qui lit STD-0001 et STD-0005 ensemble ne sait pas lequel appliquer pour le service d'identité.

**SNOMED CT.** L'ADR-0009 rejette explicitement SNOMED CT, au motif qu'il est « trop complexe pour le contexte malgache, coût de licence ». Le STD-0007 en fait un standard recommandé, et le chapitre des capacités d'interopérabilité l'attache à la terminologie. Deux documents du même niveau se contredisent frontalement sur une décision à fort impact financier et technique.

Deux autres points méritent arbitrage explicite. L'ADR-0001 justifie X-Road par « P-INT-19 : Neutralité technologique (open source) », ce qui est une erreur de catégorie : prescrire une plateforme est l'inverse de la neutralité technologique, et le niveau 2 s'est par ailleurs déclaré « volontairement neutre sur le plan technologique » alors qu'il mandates neuf normes spécifiques. Par ailleurs, aucune exigence d'autorisation d'API n'existe en niveau 2 : ni OAuth2, ni OIDC, ni mTLS, seulement « TLS 1.2 minimum », « AES-256 » et un RBAC, sans exigence de gestion de clés, de hachage ni de certification.

### 4.3 L'absence de modèle de charge

Aucun document ne dimensionne quoi que ce soit. Combien de patients, de consultations, de transactions d'interopérabilité par jour et par an ? Quelle taille de instance, quel partitionnement, quelle stratégie de montée en charge, à quel coût ? La trajectoire TCO (`00_caesn/06_portfolio/financement-tco.md`) donne une enveloppe de 88 à 131 millions de MGA sur sept ans, sans coût unitaire, sans facteur de coût, sans scénario, sans analyse de sensibilité, et en déclarant qu'elle « ne fige aucun montant ».

Une enveloppe qui ne comporte ni scénario ni sensibilité **ne peut pas arbitrer**. Elle ne peut donc pas servir la priorisation, qui en a besoin. Par ailleurs, mis en regard des montants que le dépôt cite lui-même pour les pays comparables dans son annexe comparative, l'enveloppe apparaît courte d'un ordre de grandeur pour deux centres de données, des nœuds régionaux, une fédération X-Road, une LMIS et une plateforme FHIR.

## 5. Évaluation de la gouvernance et de la faisabilité institutionnelle

### 5.1 La gouvernance est conçue et non constituée

Le design est excellent et c'est un point rare : RACI complet, instances sectorielles, commission d'homologation à cinq phases avec délais et matrice de décision, Bureau de Réalisation de la Valeur avec seuils d'escalade, processus de changement avec formulaire, régime de dérogation avec conditions de sortie.

La réalité est nulle. `00_caesn/07_governance/fondement-legal.md` est explicite : « Le cadre HEA est aujourd'hui consultatif [...] n'ont pas de mandat légal contraignant. » L'ADR-0010 le confirme et qualifie l'ensemble. Le programme de conformité est au statut « proposé », conditionné à l'adoption de l'ADR-0010 et à la dotation en moyens, et ses pilotes débutent en T4 2028. La CNASN n'est constituée que par décret ministériel en T4 2026.

L'ADR-0010 mérite d'être signalé positivement : c'est un auto-diagnostic lucid, argumenté, avec des comparatifs crédibles (Kenya DHA 2023, POPIA, NHA, NDPR). Beaucoup de référentiels évitent ce document. Celui-ci l'a écrit.

### 5.2 L'inversion de séquence est l'erreur de planification principale

Le calendrier place les institutions après le travail qu'elles doivent gouverner. La CNASN arrive en T4 2026, les instances sectorielles en T1 2027, les instances spécialisées en T2 2027, les comités techniques en T3 2027. Or le lot L1 « Socle de confiance numérique » court de T4 2026 à T2 2027, et le lot L3 « Services de terrain et interopérabilité » démarre en T4 2027.

Il en résulte deux impossibilités. On ne peut pas homologuer des profils au titre d'un critère C4 exigeant le passage par X-Road (`00_caesn/07_governance/homologation.md`) quand le comité qui applique ce critère n'existe pas encore. Et on ne peut pas faire dépendre la constitution de la gouvernance de l'adoption d'une loi alors que cette loi doit précisément être portée par la gouvernance.

La correction est simple et n'exige aucun contenu nouveau : **avancer la constitution de la CNASN et de l'avant-projet de loi à une position antérieure au lot L1**, de façon à ce que l'institution et le texte juridique avancent en parallèle avec le socle technique, et non en séquence derrière lui. Le dépôt possède déjà un avant-projet de loi competent de 20 articles (`00_caesn/07_governance/projet-loi-esante.md`). Il s'agit de l'aligner sur le calendrier, non de l'écrire.

### 5.3 Le registre des décisions ne peut pas être lu comme une source de vérité

Le registre se présente comme la source unique de vérité des décisions. Il emploie quatre vocabulaires de statut pour le même ADR (frontmatter `active`, corps « accepté », registre « appliqué », annexe du change-log « acceptée »), et il qualifie d'« appliqué » les ADR-0001 à ADR-0004 datés du 2026-07-01, alors que les échanges que ces décisions activent sont programmés en T2-T3 2028 et que la CNASN n'est pas constituée.

Le mot « appliqué » est le point de rupture. Il signifie ici « décidé », mais se lit comme « déployé ». Un bailleur qui lit ce tableau comprendra que X-Road, mADX, FHIR et PIXm sont en production nationale. Aucun ne l'est. C'est le type d'écart qui, une fois constaté, disqualifie l'ensemble du référentiel.

Deux défauts supplémentaires méritent un arbitrage explicite. STD-0008 (réclamations et paiements) et STD-0009 (logistique LMIS) sont des normes obligatoires sans aucune décision d'architecture correspondante : rien n'explique le choix de FHIR `Claim` pour les réclamations, ni de GS1 et du modèle événementiel pour le stock. Et STD-0005, approuvé, cite un ADR-0006 qui est « proposé » ; STD-0008 rend contraignant un STD-0007 qui est « draft ».

### 5.4 Les écarts de trajectoire sont des emplacements réservés

Les trois écarts qui sont censés justifier la trajectoire (GAP-01 couverture de terrain en zone isolée, GAP-02 interopérabilité transfrontalière et One Health, GAP-03 cadre légal et gouvernance publique) se terminent tous par le même texte littéral : « Décrit ce qui n'est pas encore couvert... ». Aucune table de lots ne référence un écart. Le champ `between` de GAP-03 ne contient qu'un seul plateau au lieu des deux attendus.

Autrement dit, **les trois questions qui justifieraient la structure de la roadmap ne sont pas posées.** Ce qui reste est un séquencement de lots intuitionnel, ce qui est déjà utile, mais qui ne peut pas être defended devant un bailleur comme le résultat d'une analyse d'écarts.

### 5.5 La trajectoire et le runway de maturité se contredisent

Le tableau de maturité vise CAP-13 au niveau 5 à douze mois et CAP-14 au niveau 4 à douze mois. La feuille de route place le lot L4 « Analytique et pilotage » en T2-T4 2028 et le lot L3 en T4 2027 - T2 2028. Les deux documents ne peuvent pas être vrais.

Le tableau présente par ailleurs une incohérence interne mineure : le résumé de priorisation classe CAP-18 en « Moyenne » alors que le tableau de détail le classe en « Normale », et le runway CAP-13/14/15/16 est annoncé à 1,5/5 alors que la moyenne des niveaux courants de ces quatre capacités est de 1,25.

## 6. Evaluation de l'intégrité des preuves

C'est le point sur lequel la revue doit être la plus ferme, parce qu'il conditionne la crédibilité de tout le reste.

### 6.1 Deux annexes du même dossier se contredisent sur l'évaluation internationale

`00_caesn/10_annexes/comparaison-architectures-africaines.md` (§ 4.7, lignes 336 et 338) indique : « Madagascar | Non évalué » et « Madagascar n'a pas encore été évalué par le GDHM ». Le § 5.2 de la même annexe en déduit que l'absence d'évaluation « empêche tout benchmarking formel ».

`00_caesn/10_annexes/evaluation-gdhm.md` (ligne 33) indique : « Madagascar a soumis ses données GDHM en 2024 : résultat Phase 3, score composité 2,5/5, rang 17ᵉ sur 32 pays africains », avec une référence PMC. Le fichier utilise ensuite ce score comme **preuve de la qualité du cadre HEA lui-même**, en notant le domaine 1 à la phase 2,5 sur la base de la stratégie nationale et de la gouvernance.

Les deux affirmations ne peuvent pas être vraies. L'une des deux est fausse, et l'enjeu n'est pas le score mais le fait d'utiliser une évaluation internationale comme argument de la qualité d'une architecture qui, par ailleurs, n'a pas encore de gouvernance constituée.

### 6.2 Un comptage périmé circule comme une force

La même annexe comparative, § 5.1, présente comme une force du HEA : « Les 16 profils techniques (PT-01 à PT-16) ». Il existe dix-neuf profils, PT-01 à PT-19, et la force est surestimée dans le même passage.

### 6.3 La conclusion « clos » du rapport de cohérence n'est pas soutenable

`coherence-report.md` conclut : « Statut : clos - l'ensemble des points de cohérence inter-documents est résolu ; le référentiel passe les gates (validate_ref → CONFORME, build_wrappers --check → 97 enveloppes) ». L'exécution des mêmes gates aujourd'hui ne confirme pas cette affirmation : le validateur de graphe `scripts/validate_ref.py` ne s'exécute plus du tout (marqueurs de conflit non résolus dans le fichier), le contrôle d'idempotence des enveloppes signale quatre fichiers générés hors synchronisation, et le validateur d'ADR échoue sur un fichier de suivi qui n'est pas un ADR.

Il faut cependant rester précis sur la nature de ces écarts : **il s'agit pour l'essentiel de défauts de comptabilité documentaire, non de défauts d'architecture.** La distinction importe pour l'allocation de l'effort. Corriger ces défauts ne rend pas l'architecture meilleure, cela rend l'architecture *exprimable*. Or c'est précisément ce qui manque.

## 7. Ce qui est réellement fort

Une revue honnête doit énoncer ce qui mérite d'être conservé, parce que ce sont ces éléments qui rendent le reste réparable.

**L'ancrage hors ligne et en connectivité contrainte est la meilleure décision architecturale du référentiel.** Il n'est pas décoratif : il traverse la fondation F.1, l'exigence ENF-1, le chapitre ART-3, le patron ART-8C, les composants CMP-19, 21, 27 et 28, le lot L2, le profil PT-01 et son scénario T03, et les engagements de service. Quarante-cinq documents du dépôt le portent. C'est le pari correct pour Madagascar, et la plupart des architectures nationales africaines recopient le modèle du pays connecté et se trompent. Ce fil est le seul élément du référentiel qui soit à la fois stratégique, techniquement cohérent et progressivement exécuté.

**L'outillage est un actif national.** Pour un ministère qui n'a pas encore d'autorité, disposer d'une ontologie OWL avec formes SHACL, d'une compilation vers FHIR StructureDefinition, CodeSystem et ValueSet, d'une génération de schémas JSON et de spécifications OpenAPI, d'un graphe de connaissances RDF avec aller-retour vérifié, et de contrôles d'idempotence en intégration continue, constitue une capacité réelle et exportable. C'est l'idée HEART/ODIS mise en œuvre plutôt que citée. Le fait que l'échec actuel de `pt-14` et `pt-15` vienne de la détection d'une clé YAML dupliquée, et non d'un défaut de conception, démontre que le système fonctionne.

**La discipline de décision est réelle.** Les ADR examinent des alternatives et les rejettent avec des motifs : API REST propriétaires, ADX classique, CDA, OpenEHR, certificats auto-signés, blockchain. L'ADR-0009 évalue la terminologie par coût de maintenance. L'ADR-0003 argumente le choix FHIR. C'est une discipline de décision, pas une formalisation décorative.

**L'ouverture externe est réelle et utile.** L'auto-évaluation ADHMAT avec, pour chaque domaine, des écarts ramenés à des artefacts HEA concrets, constitue un référentiel falsifiable. L'annexe comparative couvre douze pays africains et cinq cadres régionaux. Le benchmark a une valeur réelle, à condition de le mettre à jour.

**Le cadre juridique et institutionnel est approached avec lucidité.** Loi 2014-038, décret 2023-1541, Convention de Malabo, loi 2024-004 : l'ancrage normatif existant est correctement identifié, l'avant-projet de loi e-santé de vingt articles est techniquement abouti, et le vide est nommé sans détour.

## 8. Synthèse des risques

Le tableau ci-dessous hiérarchise les constats par impact sur les objectifs d'architecture du cadre. La colonne « Nature » distingue explicitement le défaut d'architecture du défaut de preuve, parce que leur traitement n'est pas le même.

| # | Constat | Gravité | Confiance | Nature | Objectif affecté |
|---|---------|----------|------------|--------|------------------|
| R1 | Absence de profil de dossier de santé et de profil de référence/contre-référence, alors que CAP-02 est au niveau de maturité 1 | Critique | Élevée | Architecture | Couverture des flux VS-01 |
| R2 | Chaîne VS → CAP → [capacité interopérabilité] → ART → PT rompue au niveau 2, avec compte obsolète en circulation | Critique | Élevée | Architecture | Traçabilité bout en bout |
| R3 | Aucune exigence d'autorisation d'API, aucun modèle de menace, aucun cycle de vie de clé en sécurité | Critique | Élevée | Architecture | Sécurité et protection des données |
| R4 | Enveloppe TCO sans coût unitaire, sans scénario ni sensibilité, donc incapable d'arbitrer | Critique | Élevée | Architecture | Décision d'investissement |
| R5 | Registre d'ADR : quatre vocabulaires de statut, « appliqué » employé pour « décidé » | Élevée | Élevée | Preuve | Opposabilité |
| R6 | Contradiction GDHM entre deux annexes d'un même dossier | Élevée | Élevée | Preuve | Crédibilité externe |
| R7 | Observabilité et reprise après sinistre sans composant, service ni lot jusqu'à L5 | Élevée | Élevée | Architecture | Fiabilité, exploitabilité |
| R8 | Aucune composante de dimensionnement ni de charge | Élevée | Élevée | Architecture | Scalabilité |
| R9 | Gouvernance et loi séquencées après le lot L1 qu'elles doivent gouverner | Élevée | Moyenne | Institutionnel | Faisabilité |
| R10 | Les trois écarts de trajectoire sont des emplacements réservés non renseignés | Moyenne | Élevée | Architecture | Justification de la roadmap |
| R11 | Contradictions FHIR contre PIXm/PDQm, et SNOMED rejeté par ADR-0009 mais recommandé par STD-0007 | Moyenne | Élevée | Architecture | Interopérabilité |
| R12 | Runway de maturité incompatible avec le calendrier des lots | Moyenne | Élevée | Architecture | Cohérence de la trajectoire |
| R13 | Douze chapitres ART sans `implements` déclaré ; liens service vers composant et objet de données faux | Moyenne | Élevée | Architecture | Traçabilité sémantique |
| R14 | Annexes de correspondance divergentes du frontmatter du référentiel | Moyenne | Élevée | Preuve | Traçabilité |
| R15 | Périmètre de la stratégie doctorale absent : gestion des risques inter-sectoriels traitée comme un critère sur quatorze | Faible | Moyenne | Architecture | Couverture |

## 9. Recommandations priorisées

### Priorité 1 : Restaurer la crédibilité de l'assertion (faible coût, effet le plus élevé)

1. Adopter un vocabulaire de statut unique à quatre valeurs pour les ADR : **proposé, accepté, appliqué, en production**, avec une définition explicite distinguant « décision prise » de « mise en œuvre constatée ». Aligner le registre, les frontmatter, les corps d'ADR et le change-log sur ce vocabulaire, et corriger les ADR-0001 à ADR-0004.
2. Arbitrer la contradiction GDHM en retenant une seule source. Si l'évaluation 2024 existe, citer la source primaire et corriger l'annexe comparative ; si elle n'existe pas, retirer l'affirmation et traiter l'évaluation comme une action prioritaire, ce qui est de toute façon ce que dit la comparaison.
3. Corriger le compte de profils dans l'annexe comparative et les cinq emplacements qui citent 16 capacités d'interopérabilité.
4. Résoudre le conflit de validation : marqueurs de conflit dans `scripts/validate_ref.py`, dérive de quatre enveloppes générées, placement du change-log d'ADR hors du répertoire des ADR.

Critère de validation : `make check` repasse au vert, le registre des ADR n'emploie plus qu'un vocabulaire, et une relecture des quatre annexes ne révèle plus de contradiction interne.

### Priorité 2 : Combler les deux trous d'architecture (coût modéré, effet structurel)

5. **Créer le profil de dossier de santé** et **le profil de référence et contre-référence**. C'est la lacune la plus coûteuse du référentiel : PT-19 « Aide à la décision clinique » présuppose un dossier que aucun profil ne définit, et CAP-02 « Parcours patient et référence » est au niveau de maturité 1 alors que tout le flux VS-01 en dépend. Ce sont deux profils, pas un chapitre de plus.
6. **Combler le maillon manquant de la chaîne de capacités.** Deux voies sont possibles. La première consiste à restaurer une couche de capacités d'interopérabilité opérationnelles, avec les huit attributs que la gouvernance exige et des résultats mesurables, en mappant CAP-01 à CAP-18 vers ces capacités par un mécanisme déclaratif dans le frontmatter. La seconde consiste à assumer formellement la dissolution de la couche, à retirer toute revendication de capacité au niveau 2, et à réancrer la chaîne par un artefact de décomposition explicite. La première option est préférable si les capacités d'interopérabilité sont un objet de pilotage ; la seconde si elles ne le sont pas. **Dans les deux cas, l'écart actuel doit être tranché**, car un référentiel qui présente une couche manquante sous un intitulé périmé ne peut être ni audité ni piloté.
7. **Ajouter les trois modèles absents** : modèle de menace (par exemple STRIDE appliqué aux composants CMP-19 à CMP-25 et aux services d'identité et de consentement), exigence d'autorisation d'API (OAuth 2.0 ou OIDC, plus mTLS pour le transport interinstitutionnel), et modèle de dimensionnement. Le troisième conditionne les deux autres.
8. **Promouvoir l'observabilité au rang de composant et de lot de première vague**, et créer un composant de reprise après sinistre assorti d'une procédure de test. Les engagements RTO et RPO doivent être portés par un objet.
5. 9. **Renseigner les trois écarts** et **réconcilier le tableau de maturité avec la feuille de route**, en exprimant les cibles de maturité dans la même unité de temps que les lots.

### Priorité 3 : Rendre la trajectoire finançable et gouvernable

10. Transformer le TCO en véritable modèle d'aide à la décision : coûts unitaires par service et par catégorie de données, facteurs de volume, trois scénarios (minimal, nominal, ambitious), analyse de sensibilité sur les deux paramètres dominants (volume de transactions, part de connectivité), et une comparaison explicite avec les enveloppes financières des pays comparables. Sans cela, la priorisation à sept critères pondérés reste décorative.
11. **Avancer la constitution de la CNASN et l'avant-projet de loi avant le lot L1**, de façon à ce que l'institution et le texte juridique avancent en parallèle avec le socle technique.
12. Arbitrer les deux contradictions techniques : règle de précédence explicite entre FHIR R4 et PIXm/PDQm pour le service d'identité, et décision unique sur SNOMED CT, à trancher en faveur de CIM-11 plus LOINC avec un service de mapping, conformément à l'ADR-0009 qui est la source la plus récente et la mieux argumentée.

## 10. Ce qu'il ne faut pas faire

**Ne pas ajouter de niveau de détail.** La marginalité du référentiel est aujourd'hui négative sur le contenu et positive sur la preuve. Ajouter des chapitres ART, des profils ou des composants augmente la surface d'affirmation sans augmenter la surface de preuve, et dégrade le ratio de crédibilité. Le référentiel n'a pas besoin de plus de matière ; il a besoin que ce qui existe soit mesuré, daté et opposable.

**Ne pas créer de cinquième niveau.** La hiérarchie à quatre niveaux plus un référentiel objet est déjà à la limite de la navigabilité. Le référentiel objet est la bonne abstraction supplémentaire, pas une cinquième famille.

**Ne pas traiter la production documentaire comme la production de valeur.** Les DOCX consolidés, le site Mintlify et les exports PDF sont des livrables de communication, pas des indicateurs de réalisation. Le score de maturité n'est pas un indicateur de résultat.

## 11. Lacunes de cette revue

Cette revue s'appuie sur la lecture documentaire. Aucune implémentation n'existe, donc aucune affirmation ne repose sur du comportement observé en exécution. Les notations d'attributs de qualité sont des appréciations d'expert fondées sur les engagements chiffrés du dépôt et non sur des mesures.

Trois points n'ont pas été vérifiés faute d'accès : l'état réel du déploiement de X-Road à Madagascar, qui conditionne la crédibilité de l'ADR-0001 ; l'existence effective d'une soumission GDHM 2024, dont l'annexe comparative et l'annexe d'évaluation se contredisent ; et la position de l'OMS et de l'Africa CDC sur la stratégie malgache, qui pourrait contredire l'auto-évaluation de l'annexe comparative.

## 12. Documents de cette revue

- `risk-map.dot` : réseau de risques, reliant les constats aux objectifs d'architecture et aux couches concernées.
- `remediation-plan.md` : plan de remédiation séquencé, avec critères de validation et dépendances.

**Producteur :** revue d'architecture indépendante, méthode risque et qualité
**Sources :** dépôt HEA (documents, frontmatter des objets, ADR, registres, annexes, ontologie), exécution des validateurs du dépôt, benchmarks internes
**Confiance globale :** élevée sur les constats documentaires et structurels ; moyenne sur les hypothèses de faisabilité institutionnelle, faute d'accès aux acteurs institutionnels
