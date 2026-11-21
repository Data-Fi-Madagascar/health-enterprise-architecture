# Plan de remédiation : cadre HEA

**Date :** 2026-11-21
**Version :** 1.0
**Statut :** Plan d'expert, non homologué. Document d'analyse externe.
**Document de référence :** `architecture-review.md` (revue d'architecture du 2026-11-21)
**Carte des risques :** `risk-map.dot`

## 1. Principe de séquencement

La revue établit un constat qui détermine l'ordre des actions : **la marginalité du référentiel est aujourd'hui négative sur le contenu et positive sur la preuve.** Ajouter des chapitres, des profils ou des composants augmente la surface d'affirmation sans augmenter la surface de preuve, et dégrade le ratio de crédibilité.

Le plan ci-dessous procède donc en trois vagues, de la moins risquée à la plus engageante. Chaque action porte un critère de validation qui peut être exécuté mécaniquement ou par relecture ciblée. Aucune action ne devrait être engagée tant que la vague précédente n'est pas close, sous peine de reproduire exactement le problème que la revue identifie.

## 2. Vague 1 : Restaurer la crédibilité de l'assertion

Cette vague est peu coûteuse et produit l'effet le plus fort sur la perception du cadre. Elle ne modifie pas l'architecture ; elle rend l'architecture exprimable.

### A1. Unifier le vocabulaire de statut des ADR

**Problème :** quatre vocabulaux coexistent pour le même ADR (frontmatter `active`, corps « accepté », registre « appliqué », annexe « acceptée »). Le mot « appliqué » est employé là où le sens réel est « décidé », et lue comme « déployé ».

**Action :** retenir quatre états et les définir une fois : `proposé`, `accepté` (décision prise, non implémentée), `appliqué` (mise en œuvre engagée, constatée sur au moins un site), `en production` (usage effectif, avec volumétrie). Aligner le registre, les frontmatter, les corps d'ADR et le change-log. Reclasser les ADR-0001 à ADR-0004 en `accepté`, leur calendrier d'application ne les portant pas au-delà de 2028.

**Critère de validation :** `grep` sur l'ensemble des ADR et du registre ne retourne que les quatre valeurs définies ; un lecteur non-initié du registre ne peut pas conclure qu'une norme est en production nationale.

**Dépendances :** aucune. Prérequis de A2, A3 et de la vague 2.

### A2. Trancher la contradiction GDHM

**Problème :** `00_caesn/10_annexes/comparaison-architectures-africaines.md` (§ 4.7) indique « Madagascar | Non évalué » et en déduit que le benchmarking formel est empêché ; `00_caesn/10_annexes/evaluation-gdhm.md` (ligne 33) affirme une soumission 2024 avec Phase 3, score 2,5/5, rang 17ᵉ sur 32 pays, et s'en sert comme preuve de la qualité du cadre.

**Action :** vérifier la source primaire. Si l'évaluation existe, corriger l'annexe comparative et citer la référence exacte. Si elle n'existe pas, retirer l'affirmation de l'annexe d'évaluation, et reformuler la position de Madagascar comme non évalué, ce qui en fait une action prioritaire du plan.

**Point d'attention :** dans l'hypothèse où la soumission n'existe pas, le second effet est plus grave que la contradiction elle-même : le fichier d'évaluation utilise un score externe comme **preuve de la qualité de l'architecture**. Cet usage doit être retiré indépendamment du résultat de la vérification, car une évaluation de maturité numérique nationale ne dit rien de la qualité d'un référentiel d'architecture.

**Critère de validation :** relecture croisée des deux annexes ; aucune affirmation de score GDHM pour Madagascar sans source primaire résolue.

### A3. Purger les comptes périmés

**Problème :** « 16 profils techniques (PT-01 à PT-16) » dans le § 5.1 de l'annexe comparative, contre dix-neuf profils existants. Cinq emplacements citent encore 16 capacités d'interopérabilité, dont un tableau qui n'en liste que 14.

**Action :** mettre à jour l'annexe comparative ; aligner `01_cnisn/index.md`, `01_cnisn/reading-guide.md`, `01_cnisn/08_annexes/b-articulation-art-sn.md`, `f-articulation-complete.md` et `g-matrice-interop-types.md` sur la nomenclature réellement en vigueur. Décider explicitement, dans le cadre de B2, quelle nomenclature s'applique, afin que la correction ne soit pas 

**Critère de validation :** aucun document ne mentionne « 16 capacités » sans qualification ; le compte des profils est exact dans toute occurrence.

### A4. Rétablir la chaîne de validation

**Problème :** `scripts/validate_ref.py` contient des marqueurs de conflit non résolus et ne s'exécute plus ; l'idempotence des enveloppes signale quatre fichiers générés hors synchronisation ; `scripts/validate_adr.py` échoue sur `adr-change-log.md`, qui n'est pas un ADR mais réside dans le répertoire des ADR.

**Action :** résoudre le conflit en conservant `REL_DIRS = [ARCH_REPOSITORY_DIR]` **et** `ADR_DIRS = ["01_cnisn/06_decisions"]`, cette seconde liste étant encore référencée par le script. Régénérer les quatre enveloppes. Traiter le change-log : soit le déplacer hors du répertoire des ADR, soit l'exclure explicitement du périmètre du validateur. **La seconde option est préférable**, afin que le journal de décision reste physiquement adjacent aux décisions qu'il retrace.

**Critère de validation :** `make check` repasse au vert sur la branche principale.

**Point d'attention :** le Correctif A4 est exactement le genre de travail que la revue qualifie de défaut de comptabilité plutôt que d'architecture. Il n'est pas moins prioritaire pour autant : c'est lui qui produit la preuve mécanique que le référentiel est maîtrisé.

### A5. Corriger le rapport de cohérence

**Problème :** `coherence-report.md` conclut « clos » et « validate_ref → CONFORME », ce qui n'est plus exact.

**Action :** requalifier le statut des sections concernées et renommer le rapport pour refléter son état réel. Un rapport de cohérence qui se déclare clos quand il ne l'est pas est plus dommageable qu'un rapport absent.

**Critère de validation :** les affirmations du rapport correspondent à la sortie des validateurs au jour de la revue.

## 3. Vague 2 : Combler les deux trous d'architecture

### B1. Créer les deux profils manquants

**Problème :** aucun profil ne définit le dossier de santé, et aucun profil ne couvre la référence et la contre-référence. PT-19 « Aide à la décision clinique » présuppose un dossier que rien ne définit. CAP-02 « Parcours patient et référence » est au niveau de maturité 1 et l'ensemble du flux VS-01 en dépend.

**Action :** rédiger deux profils sources dans `04_architecture-repository/05_reference-library/standards-base/profiles/`, au format IHE : acteurs, transactions avec statut lecture/écriture, modules de contenu, sécurité, standards. **Un profil de dossier de santé**, portant FHIR R4, et **un profil de référence et contre-référence**, portant FHIR `ServiceRequest` et `Task`. Déclarer `implements` vers les chapitres ART concernés et `maps_to` vers CAP-02, CAP-03, CAP-13 et CAP-14. Rejouer `make wrappers` et `make check`.

**Critère de validation :** CAP-02 dispose d'au moins un profil déclaré ; un fournisseur peut déterminer, depuis le seul profil, comment un patient est identifié, référencé et pris en charge.

**Dépendances :** B3 (exigence d'autorisation d'API) est nécessaire pour que les profils soient sécurisables ; B1 peut commencer en parallèle.

### B2. Trancher le maillon manquant de la chaîne de capacités

**Problème :** la hiérarchie VS → CAP → capacité d'interopérabilité → ART → PT est rompue au niveau 2. Les CAP-INT-01 à CAP-INT-16 ont été retirés du référentiel objet et remplacés par 36 objets qui ne sont pas des capacités. Le chapitre du niveau 2 ne définit plus de capacités, mais la documentation continue d'en revendiquer 16. La gouvernance exige huit attributs par capacité ; aucun n'existe.

**Action :** ces deux voies sont exclusives et doivent être tranchées par le CNASN, pas par la documentation.

*Voie 1, restoration.* Recréer une couche de capacités d'interopérabilité, chacune portant les huit attributs exigés par `01_cnisn/03_gouvernance/index.md` : finalité, périmètre, propriétaire institutionnel, niveau de maturité, dépendance, critère de conformité, référence normative, indicateurs. Déclarer le mappage CAP-01 à CAP-18 vers ces capacités dans le frontmatter, de façon à ce que la traçabilité soit mécanique.

*Voie 2, dissolution assumée.* Retirer toute revendication de capacité au niveau 2, renommer le chapitre en conséquence, et réancrer la chaîne par un artefact de décomposition explicite reliant les 18 capabilities de niveau 1 aux 22 chapitres ART et aux 19 profils PT.

**Recommandation :** la voie 1 si les capacités d'interopérabilité sont un objet de pilotage, ce que le fait qu'un comité de gouvernance en évalue la maturité suggère fortement. La voie 2 si elles ne le sont pas et si la couche doit rester mince.

**Critère de validation :** le document de niveau 2 et ses annexes décrivent la même chose ; la question « la capability CAP-13 est-elle couverte par un contrat d'interopérabilité testable ? » reçoit une réponse mécanique.

**Dépendances :** conditionne A3, qui doit être fait après, et non avant.

### B3. Ajouter les modèles de sécurité manquants

**Problème :** en sécurité, le dépôt est fort sur le chiffrement et l'habilitation, et vide sur trois sujets : aucun modèle de menace, aucune exigence d'autorisation d'API (ni OAuth 2.0, ni OIDC, ni mTLS), aucun cycle de vie de clé ou de certificat.

**Action :** rédiger un modèle de menace, par exemple STRIDE appliqué aux composants de terrain CMP-19 à CMP-25 et aux services d'identité, de consentement et d'audit. Ajouter à STD-0002 une section d'autorisation d'API et de gestion de clés. Arbitrer explicitement le conflit FHIR contre PIXm/PDQm, en ajoutant une règle de précédence ou une clause de médiation dans STD-0001 et STD-0005. Trancher SNOMED CT en faveur de CIM-11 plus LOINC avec service de mapping, conformément à l'ADR-0009, et aligner STD-0007 et le chapitre des capacités.

**Critère de validation :** un fournisseur peut déterminer, depuis les seules normes en vigueur, quel mécanisme d'autorisation appliquer à quel appel d'API, et comment obtenir, faire tourner et révoquer un certificat.

### B4. Ajouter le modèle de charge et les composants manquants

**Problème :** 46 composants à instancier sans aucune hypothèse de volume ; observabilité et reprise après sinistre sans objet porteur ; aucun composant de paiement ni de gestion du consentement, alors que VS-03 et PT-18 existent.

**Action :** produire un document de dimensionnement, avec volumes annuels par categorie (patients, consultations, transactions d'interopérabilité, lignes de stock, observations), hypothèses de connectivité par strate, et stratégie de partitionnement. Créer un composant d'observabilité et un composant de reprise après sinistre avec leurs interfaces, et les inscrire au lot L1 plutôt qu'au lot L5.

**Critère de validation :** chaque engagement de RTO, de RPO et de disponibilité porte un composant et un lot ; le dimensionnement est réutilisé par le modèle TCO de C1.

### B5. Renseigner les écarts et réconcilier la maturité

**Problème :** les trois écarts de trajectoire sont des emplacements réservés ; le tableau de maturité et la feuille de route sont incompatibles ; le tableau présente en outre une incohérence interne sur CAP-18 et sur la moyenne du runway.

**Action :** renseigner les trois écarts avec leur contenu actuel et cible, la condition de franchissement et le lot qui les ferme. Exprimer les cibles de maturité dans l'unité du calendrier des lots, par exemple « niveau 3 à l'issue du lot L3 ». Corriger les deux incohérences arithmétiques internes du tableau de maturité.

**Critère de validation :** chaque écart a un lot de fermeture ; aucun objectif de maturité n'est daté en contradiction avec le calendrier de livraison.

## 4. Vague 3 : Rendre la trajectoire gouvernable et finançable

### C1. Transformer le TCO en modèle d'arbitrage

**Problème :** l'enveloppe de 88 à 131 millions de MGA sur sept ans ne comporte ni coût unitaire, ni facteur de volume, ni scénario, ni sensibilité, et « ne fige aucun montant ». Elle ne peut donc pas arbitrer entre deux options, ce dont la priorisation à sept critères pondérés a besoin.

**Action :** construire le modèle par coûts unitaires (par service national, par catégorie de données, par site de déploiement), par facteurs de volume, avec trois scénarios (minimal, nominal, ambitious) et une analyse de sensibilité sur les deux paramètres dominants, le volume de transactions et la part de connectivité. Comparer explicitement aux enveloppes des pays comparables déjà cités dans l'annexe comparative. Fixer un modèle de financement par lot et le rattacher aux jalons J1 à J11.

**Critère de validation :** deux options d'investissement concurrentes peuvent être départagées par le modèle sur des critères chiffrés et justifiables.

### C2. Avancer la gouvernance et la loi avant le lot L1

**Problème :** la CNASN est constituée en T4 2026, les instances en 2027, alors que le lot L1 court de T4 2026 à T2 2027. On ne peut pas homologuer des profils au titre d'un critère qu'aucune instance n'est en mesure d'appliquer.

**Action :** avancer la constitution de la CNASN et le dépôt de l'avant-projet de loi e-santé avant l'ouverture du lot L1. Faire avancer l'institution et le texte juridique **en parallèle** du socle technique, et non en séquence derrière lui. Trancher le critère d'homologation C4, qui impose X-Road pour les échanges inter-systèmes alors que la topologie nationale cible réserve X-Road aux institutions non sanitaires.

**Critère de validation :** l'instance d'homologation existe avant la première décision d'homologation ; le critère C4 est cohérent avec la topologie cible.

### C3. Corriger la sémantique des liens, pas seulement leur résolution

**Problème :** le pipeline garantit que les liens se résolvent, pas qu'ils désignent la bonne cible. Six liens service vers composant et objet de données sont décalés, trois composants sont cités dans un rôle qu'ils n'occupent pas, les 22 chapitres ART n'ont aucun `implements` déclaré, et les exigences ENF-1 à ENF-5 s'appuient sur des chapitres au statut `candidate`.

**Action :** corriger les liens fautifs. Rendre `implements` obligatoire pour tout chapitre ART et tout profil. Ajouter au validateur un contrôle sémantique minimal : tout service doit référencer un composant de catégorie compatible, tout composant applicatif doit référencer au moins un objet de données, toute exigence ne peut s'appuyer que sur un chapitre de statut `stable` ou `active`, et la symétrie `uses` / `applies_to` doit être vérifiée par couple et non par agrégat.

**Critère de validation :** le validateur échoue sur un commit qui introduit un lien résolu mais faux, ce que le validateur actuel n'est pas en mesure de faire.

**Dépendances :** C3 est l'action qui distingue une architecture outillée d'une architecture simplement documentée. Elle mérite d'être financée en tant que telle.

## 5. Ce qui n'est pas recommandé

**Ne pas ajouter de contenu normatif.** Le référentiel n'a pas besoin d'un vingtième profil ni d'un vingt-troisième chapitre ART. Chaque ajout non accompagné d'une preuve mesurée dégrade la crédibilité du corpus.

**Ne pas créer de cinquième niveau.** La hiérarchie à quatre niveaux plus le référentiel objet atteint la limite de la navigabilité. Toute structure supplémentaire doit être produite comme vue, non comme famille.

**Ne pas traiter la production documentaire comme la production de valeur.** Les livrables DOCX, PDF et Mintlify sont des vecteurs de communication. Le score de maturité des capabilities n'est pas un indicateur de résultat. Une confusion sur ce point ferait du référentiel un excellent support de présentation et un mauvais instrument de pilotage.

## 6. Tableau de synthèse

| Action | Vague | Coût | Impact | Prérequis | Critère de validation |
|--------|-------|-------|--------|-----------|------------------------|
| A1 Vocabulaire ADR unifie | 1 | Faible | Eleve | Aucun | Quatre valeurs seulement dans tout le corpus ADR |
| A2 Conflit GDHM tranche | 1 | Faible | Eleve | Aucun | Aucune affirmation de score sans source primaire |
| A3 Comptes perimes purges | 1 | Faible | Moyen | B2 | Zero occurrence non qualifiee de « 16 capacites » |
| A4 Chaine de validation retablie | 1 | Faible | Eleve | Aucun | `make check` au vert |
| A5 Rapport de coherence requalifie | 1 | Tres faible | Moyen | A4 | Correspondance avec la sortie des validateurs |
| B1 Profil dossier + profil reference | 2 | Moyen | Critique | B3 | CAP-02 couvert par un profil declare |
| B2 Chaine de capacites tranchee | 2 | Moyen | Critique | A1 | Niveau 2 et annexes decrits de facon coherente |
| B3 Modeles de securite | 2 | Moyen | Critique | Aucun | Regle d'autorisation d'API explicite et testable |
| B4 Modele de charge + composants | 2 | Moyen | Eleve | B2 | Chaque RTO/RPO porte un composant et un lot |
| B5 Ecarts renseignes, maturite alignee | 2 | Faible | Moyen | B1 | Chaque ecart a un lot de fermeture |
| C1 TCO discriminant | 3 | Moyen | Critique | B4 | Deux options departageables par le modele |
| C2 Gouvernance avancee avant L1 | 3 | Eleve | Critique | A1 | Instance d'homologation preexistante a son premier usage |
| C3 Validation semantique des liens | 3 | Moyen | Eleve | B3 | Le validateur rejette un lien resolu mais faux |
