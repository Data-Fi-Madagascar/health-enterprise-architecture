---

title: Guide de lecture du CNISN (niveau 2)
id: cnisn-reading-guide
domain: 01_cnisn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-18
owner: DEPSI
tags: ["cnisn", "lecture", "niveau-2", "guide"]
---

# Guide de lecture du CNISN (niveau 2)

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## 1. Qu'est-ce que le CNISN ?

Le CNISN (Cadre National d'Interopérabilité de la Santé Numérique) constitue le deuxième niveau de la hiérarchie documentaire du secteur santé. Il définit les principes, capacités et règles de gouvernance qui s'appliquent aux échanges de données et de services impliquant le secteur santé à Madagascar.

Le CNISN fixe les principes opposables auxquels toute initiative doit se conformer, établit les responsabilités institutionnelles de chaque acteur, identifie les capacités nationales indispensables à l'interopérabilité, précise les règles applicables aux données et services partagés, et organise les mécanismes de conformité permettant de vérifier le respect de ces règles. Il reste volontairement neutre sur le plan technologique : il ne sélectionne aucun produit, fournisseur, technologie ni plateforme particulière.

```
Niveau 1 (CAESN)  →  Valeur, capabilités, gouvernance
Niveau 2 (CNISN)  →  Principes d'interopérabilité  ← CE DOCUMENT
Niveau 3 (ARTSN)  →  Patterns architecturaux, standards
Niveau 4 (PTISN)  →  Services, profils, produits candidats
```

## 2. Structure du CNISN

Le CNISN est organisé en huit parties qui couvrent l'ensemble du cycle de vie du cadre d'interopérabilité.

| Partie | Contenu | Qui la lit |
|--------|---------|------------|
| Préambule | Positionnement, portée, articulation | Tous |
| Principes | 25 principes (catégories A-F) | DEPSI, architectes |
| Capacités | 16 capacités d'interopérabilité | DEPSI, équipes techniques |
| Gouvernance | Instances, processus, responsabilités | Décideurs, gouvernance |
| Conformité | Critères, tests, homologation | Équipes techniques |
| Standards | Normes obligatoires et standards recommandés | Équipes techniques |
| Trajectoire | Feuille de route, jalons | Décideurs, planificateurs |
| Indicateurs | Métriques, suivi | SIS, suivi-évaluation |
| Conclusion | Synthèse | Tous |

## 3. Parcours de lecture par profil

### 3.1 Décideur institutionnel

Le décideur institutionnel cherche à comprendre les enjeux d'interopérabilité et les responsabilités qui en découlent. Il est invité à consulter le préambule pour le positionnement du cadre, la gouvernance pour les instances et responsabilités, la trajectoire pour la feuille de route, et la conclusion pour la synthèse.

### 3.2 Direction métier / programme

La direction métier ou le responsable de programme cherche à comprendre les règles applicables aux échanges de données dans son domaine. Elle doit lire le préambule pour la portée du cadre, les principes pour les catégories A et B, et les capacités pour les éléments pertinents à son domaine.

### 3.3 Équipe technique / DEPSI

L'équipe technique ou la DEPSI cherche à implémenter des échanges conformes au CNISN. Elle doit lire l'ensemble du préambule, les 25 principes, les 16 capacités, la conformité pour les critères et tests, puis se référer à l'ARTSN (niveau 3) pour les patterns techniques et au PTISN (niveau 4) pour les standards et profils.

### 3.4 Partenaire technique

Le partenaire technique cherche à évaluer la conformité d'une solution. Il doit consulter les principes (catégories D et E), les capacités couvertes par sa solution, et la conformité pour les preuves requises.

## 4. Les 25 principes du CNISN

Les principes sont organisés en six catégories qui couvrent l'ensemble des dimensions de l'interopérabilité.

| Catégorie | Principes | Objet |
|-----------|-----------|-------|
| **A** : Autorité et données de référence | P-INT-01 à P-INT-04 | Sources autoritatives, résolution, copies, historisation |
| **B** : Contractualisation | P-INT-05 à P-INT-09 | Contrats, versionnement, responsabilités, catalogues |
| **C** : Gouvernance interinstitutionnelle | P-INT-10 à P-INT-13 | Accords, arbitrage, dérogations |
| **D** : Sécurité et autorisation | P-INT-14 à P-INT-18 | Bases d'autorisation, finalité, résidence, minimisation |
| **E** : Neutralité et réversibilité | P-INT-19 à P-INT-22 | Neutralité technologique, portabilité, progressivité |
| **F** : Conformité | P-INT-23 à P-INT-25 | Preuves, applicabilité, réévaluation |

## 5. Les 16 capacités d'interopérabilité

| Capacité | Famille | Description |
|----------|---------|-------------|
| CAP-INT-01 | Référentiels et identités | Résolution d'identité du bénéficiaire |
| CAP-INT-02 | Référentiels et identités | Registre des professionnels de santé |
| CAP-INT-03 | Échange et médiation | Échange interinstitutionnel et médiation |
| CAP-INT-04 | Référentiels et identités | Référentiel des structures et services |
| CAP-INT-05 | Référentiels et identités | Terminologie et codification |
| CAP-INT-06 | Échange et médiation | Catalogue de services et registre de contrats |
| CAP-INT-07 | Données analytiques | Échange de données agrégées et analytique |
| CAP-INT-08 | Confiance et sécurité | Authentification et autorisation |
| CAP-INT-09 | Confiance et sécurité | Consentement et bases d'autorisation |
| CAP-INT-10 | Confiance et sécurité | Audit, provenance, traçabilité |
| CAP-INT-11 | Qualité et conformité | Qualité et réconciliation des données |
| CAP-INT-12 | Qualité et conformité | Conformité et homologation |
| CAP-INT-13 | Transfrontalier | Interopérabilité transfrontalière |
| CAP-INT-14 | One Health | Échanges intersectoriels |

## 6. Liens vers les autres niveaux

| Niveau | Document | Lien |
|--------|----------|------|
| 1 : CAESN | Cadre d'Architecture d'Entreprise | ../00_caesn/00_overview/index.md |
| 3 : ARTSN | Architecture de Référence Technique | ../02_artsn/index.md |
| 4 : PTISN | Profils techniques d'implémentation | ../03_ptisn/index.md |

## 7. Documents complémentaires

Le guide de lecture s'accompagne de la matrice de lecture offrant une vue croisée des parties et des lecteurs, du glossaire définissant les termes d'interopérabilité, de la liste des acronymes, et des annexes contenant l'articulation avec l'ARTSN et les supports complémentaires.

## Références

- **matrice de lecture** : Matrice de lecture du CNISN (niveau 2) (`01_cnisn/reading-matrix.md`)
- **Préambule** : Préambule du CNISN (`01_cnisn/00_introduction/index.md`)
- **Principes** : Partie I : Principes nationaux d'interopérabilité de santé (`01_cnisn/01_principes/index.md`)
- **Capacités** : Partie II : Capacités nationales requises (`01_cnisn/02_capacites/index.md`)
- **Gouvernance** : Partie III : Gouvernance (`01_cnisn/03_gouvernance/index.md`)
- **Conformité** : Partie IV : Conformité (`01_cnisn/04_conformite/index.md`)
- **Standards** : Normes et standards d'architecture (`01_cnisn/05_standards/index.md`)
- **Trajectoire** : Partie V : Trajectoire de mise en œuvre (`01_cnisn/05_trajectoire/index.md`)
- **Indicateurs** : Partie VI : Indicateurs de suivi (`01_cnisn/06_indicateurs/index.md`)
- **Conclusion** : Conclusion du CNISN (`01_cnisn/07_conclusion/index.md`)
- **../00_caesn/00_overview/index.md** : Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) (`00_caesn/00_overview/index.md`)
- **../02_artsn/index.md** : Architecture de Référence Technique de la Santé Numérique (ARTSN) (`02_artsn/index.md`)
- **../03_ptisn/index.md** : Profils techniques d'implémentation de la Santé Numérique (PTISN) (`03_ptisn/index.md`)

## Documents de la section

- [cnisn-glossary: Glossaire du CNISN (niveau 2)](glossary.md)
- [cnisn-reading-matrix: Matrice de lecture du CNISN (niveau 2)](reading-matrix.md)
- [cnisn-acronyms: Acronymes et abréviations du CNISN (niveau 2)](acronyms.md)
- [cnisn: Cadre National d'Interopérabilité de la Santé Numérique (CNISN)](index.md)
- [std-0001: STD-0001 : Norme d'interopérabilité : HL7 FHIR R4](05_standards/std-0001-interopabilite-fhir.md)
- [std-0003: STD-0003 : Norme d'échange interinstitutionnel : X-Road](05_standards/std-0003-x-road.md)
- [norm-007: NORM-007 : Règlement Sanitaire International (RSI 2005)](05_standards/norm-007-rsi.md)
- [std-0007: STD-0007 : Standard terminologique : SNOMED CT](05_standards/std-0007-snomed-ct.md)
- [std-0005: STD-0005 : Norme d'identité patient : PIXm/PDQm](05_standards/std-0005-identite-pixm.md)
- [std-0004: STD-0004 : Norme de données agrégées : mADX](05_standards/std-0004-madx.md)
- [std-0006: STD-0006 : Norme terminologique : CIM-11 + LOINC](05_standards/std-0006-terminologie.md)
- [standards: Normes et standards d'architecture](05_standards/index.md)
- [norm-008: NORM-008 : Tripartite Plus OMS–WOAH–FAO–PNUE](05_standards/norm-008-tripartite.md)
- [std-0000: STD-0000 : <Titre de la norme>](05_standards/std-0000-template.md)
- [std-0002: STD-0002 : Norme de sécurité : Chiffrement et contrôle d'accès](05_standards/std-0002-securite-chiffrement.md)
- [cnisn-trajectoire: Partie V : Trajectoire de mise en œuvre](05_trajectoire/index.md)
- [adr-0003: ADR-0003 : Utilisation de HL7 FHIR comme standard d'interopérabilité](06_decisions/adr-0003-fhir.md)
- [adr-0005: ADR-0005 : Adoption de FHIR Consent pour le consentement structuré](06_decisions/adr-0005-consentement.md)
- [adr-0009: ADR-0009 : Adoption d'un référentiel terminologique national (CIM-11 + LOINC)](06_decisions/adr-0009-terminologie.md)
- [adr-0004: ADR-0004 : Adoption des profils IHE PIXm/PDQm pour la résolution d'identité](06_decisions/adr-0004-identite.md)
- [adr-0001: ADR-0001 : Adoption de X-Road comme plateforme d'échange interinstitutionnel](06_decisions/adr-0001-x-road.md)
- [decisions: Décisions d'architecture (ADR)](06_decisions/index.md)
- [adr-0006: ADR-0006 : Adoption de l'Identité Nationale Patient (INP) via PIXm/PDQm](06_decisions/adr-0006-inp.md)
- [adr-0010: ADR-0010 : Cadre légal et mandat d'opposabilité du CNASN](06_decisions/adr-0010-cadre-legal.md)
- [adr-0000: ADR-0000 : <Titre de la décision>](06_decisions/adr-0000-template.md)
- [adr-0002: ADR-0002 : Adoption du profil IHE mADX pour l'échange de données agrégées](06_decisions/adr-0002-madx.md)
- [adr-0007: ADR-0007 : Adoption du GDHCN pour la confiance transfrontalière](06_decisions/adr-0007-gdhcn.md)
- [registre-decisions: Registre des décisions d'architecture (ADR)](06_decisions/registre-decisions.md)
- [template-modification: Template : Demande de modification architecturale](06_decisions/template-modification.md)
- [adr-0008: ADR-0008 : Adoption d'ATNA et journalisation pour l'audit et la traçabilité](06_decisions/adr-0008-atna.md)
- [cnisn-indicateurs: Partie VI : Indicateurs de suivi](06_indicateurs/index.md)
- [cnisn-introduction: Préambule du CNISN](00_introduction/index.md)
- [cnisn-principes: Partie I : Principes nationaux d'interopérabilité de santé](01_principes/index.md)
- [cnisn-annexe-c: Annexe C : Articulation avec le PTISN](08_annexes/c-articulation-ptisn.md)
- [cnisn-annexe-f: Annexe F : Articulation complète CAESN → CNISN → ARTSN → PTISN](08_annexes/f-articulation-complete.md)
- [cnisn-annexe-g: Annexe G : Matrice des types d'interopérabilité](08_annexes/g-matrice-interop-types.md)
- [cnisn-annexe-d: Annexe D : Principes de lecture](08_annexes/d-principes-lecture.md)
- [cnisn-annexe-a: Annexe A : Matrice principes–capacités](08_annexes/a-matrice-principes-capacites.md)
- [cnisn-annexe-b: Annexe B : Articulation avec l'ARTSN](08_annexes/b-articulation-art-sn.md)
- [cnisn-annexe-e: Annexe E : Correspondance CAESN–CNISN](08_annexes/e-correspondance-caesn.md)
- [cnisn-gouvernance: Partie III : Gouvernance](03_gouvernance/index.md)
- [cnisn-capacites: Partie II : Capacités nationales requises](02_capacites/index.md)
- [cnisn-conclusion: Conclusion du CNISN](07_conclusion/index.md)
- [cnisn-programme-conformite: Partie IV bis : Programme de conformité opérationnel](04_conformite/programme-conformite.md)
- [cnisn-conformite: Partie IV : Conformité](04_conformite/index.md)

<!-- liens-section-auto -->
