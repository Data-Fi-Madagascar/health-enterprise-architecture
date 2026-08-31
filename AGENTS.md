# AGENTS.md

Règles de travail pour toute tâche dans ce dépôt. À lire avant de créer ou modifier un document.

## Projet

Dépôt d'architecture documentée **as code** du secteur santé numérique de Madagascar, organisé selon la hiérarchie documentaire du CAESN en **quatre familles de documents**, chacune dans un dossier numéroté à la racine.

## Structure : dossiers numérotés

Tout dossier structurel du dépôt reçoit un **préfixe numérique de tri** sur deux chiffres (`00_`, `01_`, `02_`, …). Le numéro définit l'ordre de lecture et la hiérarchie ; le suffixe décrit le contenu en kebab-case.

| Niveau | Dossier | Contenu |
|--------|---------|---------|
| 1 | `00_caesn/` | Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) |
| 2 | `01_cnisn/` | Cadre National d'Interopérabilité de la Santé Numérique (CNISN) |
| 3 | `02_artsn/` | Architecture de Référence Technique de la Santé Numérique (ARTSN) |
| 4 | `03_ptisn/` | Profils techniques d'implémentation par initiative (PTISN) |

## Fondations : la trilogie HEAL, HEAF, HEART

Le cadre repose sur trois référentiels méthodologiques de l'OMS/WHO Digital Health, qui forment le socle théorique de l'architecture de santé numérique malagasy :

- **HEAL** (Health Enterprise Architecture Laboratory) : laboratoire de recherche établi au sein de la School of Computer Science de l'Université de KwaZulu-Natal (UKZN, Durban, Afrique du Sud), co-financé par la Fondation Rockefeller et le CRDI. Hébergé au CAIR (Centre for Artificial Intelligence Research), il mène une recherche appliquée sur les architectures de santé ouvertes pour pays à ressources limitées, en cycle bidirectionnel recherche ↔ implémentation de terrain (Jembi Health Systems, Rwanda, Mozambique, Afrique du Sud). Il forme des architectes de santé (MSc/PhD) pour la souveraineté technologique.
- **HEAF** (Health Enterprise Architecture Framework) : méthodologie de modélisation développée par le HEAL pour structurer les Systèmes d'Information Sanitaires nationaux (NHIS) en contextes à ressources limitées. Il simplifie une synthèse du GCM (Generic Component Model), de Zachman, du FEAF, de TOGAF, du suivi OMS/HMN et de HIS-DF. Caractéristiques clés : légèreté/modularité (implémentation verticale puis intégration nationale), modes de fonctionnement hybrides (connectivité intermittente, processus papier/numérique), et approche pilotée par les ontologies (Ontology-Driven).
- **HEART** (Health Enterprise Architecture Repository of Tools) : dépôt/catalogue d'artefacts d'architecture réutilisables pour matérialiser les principes du HEAF : outils logiciels « biens publics mondiaux » (OpenMRS, DHIS2), patrons d'architecture, standards/profils d'échange (HL7 FHIR, IHE mCSD, IHE SVCM, IHE mADX, SDMX-HD), et politiques/règles. Son cœur technique est l'architecture pilotée par les ontologies (ODIS) : reconfiguration à l'exécution de l'interopérabilité en manipulant les structures ontologiques sans réécrire le code.

### Correspondance avec la hiérarchie du dépôt

| Référentiel WHO | Rôle | Traduction dans ce dépôt |
|-----------------|------|--------------------------|
| HEAL | Recherche et renforcement des capacités | Collaboration continue universités / DEPSI / partenaires techniques |
| HEAF | Framework et hiérarchie documentaire | Structure CAESN/CNISN/ARTSN, déclinaison des valeurs nationales en capabilités (Architecture Runway CAP-13..16) |
| HEART | Dépôt d'artefacts réutilisables | Registre des profils techniques (PTISN) + compilateurs de métadonnées sémantiques (compile_rdf.py, yaml_to_fhir.py) |

### Implication pour la rédaction

- L'approche « Ontology-Driven » du HEAF se traduit par les artefacts `ontologie/hea.ttl` (ontologie OWL), `ontologie/hea-shapes.ttl` (shapes SHACL) et le pipeline graphify (`dist/hea-enriched.ttl`).
- L'esprit ODIS du HEART se matérialise via la génération automatique des règles de validation et des terminologies de production depuis la source unique de vérité GitHub.
- Tout nouveau document doit s'ancrer explicitement dans cette trilogie : le HEAL justifie la démarche collaborative, le HEAF impose la structure par couches/valeurs, le HEART impose la réutilisation d'artefacts et la génération de métadonnées.

## Sous-dossiers numérotés de `00_caesn/`

| Dossier | Contenu |
|---------|---------|
| `00_overview/` | Vue d'ensemble, fondements, modèle de valeur |
| `01_value-streams/` | Flux de valeur nationaux (VS-01 à VS-04) |
| `02_principles/` | Principes transversaux (PA) et de domaine (PD) |
| `03_capabilities/` | Capabilités CAP-01..18, maturité, runway |
| `04_data/` | Architecture des données et de l'information sanitaire |
| `05_application/` | Architecture applicative et systèmes numériques |
| `06_portfolio/` | Portefeuille d'initiatives orienté valeur |
| `07_governance/` | Instances, RACI, Bureau de Réalisation de la Valeur |
| `08_decisions/` | Architecture Decision Records (ADR) |
| `09_standards/` | Normes obligatoires et standards recommandés |
| `10_annexes/` | Matrice de lecture, glossaire, acronymes |

## Conventions des fichiers Markdown

Chaque fichier (sauf `README.md` racine) commence par un frontmatter YAML. Les valeurs de `domain` et les identifiants suivent la règle **« le nom reflète la localisation »** :

- `domain:` : **obligatoire** — valeur = nom du dossier parent immédiat, **préfixe numérique inclus** (ex. `domain: 01_value-streams` pour un fichier dans `00_caesn/01_value-streams/`). Il reflète ainsi la localisation exacte du document.
- `id:` : identifiant sémantique stable en kebab-case (ex. `data-governance`, `capabilities-business`). Ne change pas lorsque le dossier est renommé.
- Autres champs : `title`, `version`, `status`, `last_reviewed`, `owner`, `tags`.

## Règle « aligné sur la localisation »

À appliquer à tout nouveau document et à tout renommage de dossier :

1. **Nommer** le dossier avec le préfixe numérique dans l'ordre de lecture.
2. **Renseigner** `domain:` avec le nom du dossier parent immédiat, **préfixe numérique inclus** (ex. `01_value-streams`).
3. **Mettre à jour** tous les liens relatifs Markdown quand un dossier est déplacé ou renommé.
4. **Vérifier** qu'aucun lien n'est cassé après chaque changement de structure (aucun lien `url:` ou `id:` vers un chemin obsolète).

## Vérification des liens

Après toute modification de structure, valider qu'il n'existe aucun lien relatif cassé :

```bash
python3 - <<'EOF'
import glob, os, re
for f in glob.glob('**/*.md', recursive=True):
    for m in re.finditer(r'\[[^\]]*\]\(([^)]+)\)', open(f).read()):
        link = m.group(1).split('#')[0]
        if link and not link.startswith(('http://','https://')) \
           and not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), link))):
            print('BROKEN', f, '->', link)
EOF
```

## Qualité rédactionnelle de type Gartner

Tout document produit dans ce dépôt doit respecter la **qualité rédactionnelle de type Gartner**. Cette norme s'applique à tous les types de documents : analyse, spécification, guide, référentiel, ADR, etc.

### Principes fondamentaux

1. **Structure adaptée au type de document** : chaque type de document a une structure optimale. L'exemple ci-dessous montre une structure pour document d'analyse, mais d'autres types de documents ont leurs propres structures.
2. **Paragraphes analytiques** : chaque section doit contenir des paragraphes explicatifs qui contextualisent, expliquent la signification des constats, les implications et les risques.
3. **Pas de tableaux sans analyse** : chaque tableau doit être précédé ou suivi d'un commentaire qui en explique la signification.
4. **Vocabulaire formel** : utiliser des termes comme « constitue », « révèle », « conditionne », « traduit ».
5. **Connecteurs logiques** : utiliser des expressions comme « C'est précisément », « Cette observation », « Plus fondamentalement ».
6. **Interdiction des caractères chinois** : ne jamais utiliser de caractères chinois (kanji, hiragana, katakana) dans la rédaction.
7. **Interdiction des em-dashes** : ne pas utiliser de tirets longs. Utiliser des tirets courts (-) ou des deux-points (:) à la place.
8. **Interdiction des séparateurs** : ne pas utiliser de séparateurs horizontaux (---). Les sections sont séparées par des en-têtes et des paragraphes, pas par des lignes.

### Exemple de structure pour document d'analyse

1. En-tête métadonnées (Référence, Date, Version, Objet, Sources, Statut)
2. Table des matières numérotée
3. Contexte et objectif avec positionnement stratégique
4. Méthodologie détaillée
5. Synthèse quantitative avec tableaux et analyse
6. Analyse par domaine avec paragraphes explicatifs
7. Convergences inter-groupes
8. Points d'arbitrage
9. Recommandations priorisées
10. Annexe: Matrice de traçabilité

### Documents de référence
- `feedbacks/analyse-feedbacks-caesn.md` - Modèle pour document d'analyse
- `feedbacks/analyse-feedbacks-cnisn.md` - Modèle pour document d'analyse

## Langue

Les documents sont rédigés en **français**. Les noms de dossiers et identifiants sont en kebab-case anglais.