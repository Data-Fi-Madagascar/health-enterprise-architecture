---

title: Guide de lecture du PTISN (niveau 4)
id: ptisn-reading-guide
domain: 03_ptisn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: Équipes techniques des initiatives
tags: ["ptisn", "lecture", "niveau-4", "guide"]
---

# Guide de lecture du PTISN (niveau 4)

## Pour qui lire ce document

**Niveau :** niveau 4 : Profils techniques d'implémentation de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## 1. Qu'est-ce que le PTISN ?

Le PTISN (Profils techniques d'implémentation de la Santé Numérique) est le **niveau 4** de la hiérarchie documentaire du secteur santé numérique de Madagascar. Il traduit les capacités et principes des niveaux supérieurs en **spécifications techniques concrètes** pour chaque initiative numérique. Le PTISN est le seul niveau qui peut nommer explicitement des standards, profils et produits candidats.

```
Niveau 1 (CAESN)  →  Valeur, capabilités, gouvernance
Niveau 2 (CNISN)  →  Principes d'interopérabilité, capacités requises
Niveau 3 (ARTSN)  →  Patterns architecturaux, standards techniques
Niveau 4 (PTISN)  →  Services, profils, standards, produits candidats
```

## 2. Structure du PTISN

Le PTISN est organisé en huit parties complétées par des annexes. Le tableau suivant résume le contenu de chaque partie et identifie les publics concernés.

| Partie | Contenu | Qui la lit |
|--------|---------|------------|
| Préambule | Positionnement, fonction, hiérarchie | Tous |
| Règles d'utilisation | Types de décisions, statuts, versionnement | Équipes techniques, DEPSI |
| Topologie nationale cible | Architecture cible, couches, responsabilités | Architectes, intégrateurs |
| Profils techniques | 13 profils PT-01 à PT-13 | Développeurs, fournisseurs |
| Matrice d'alignement | Mapping capacités CNISN ↔ profils ↔ ART | DEPSI, validateurs |
| Profil d'initiative | Template pour chaque initiative | Équipes projet |
| Gouvernance | Processus d'adoption, critères, homologation | Décideurs, gouvernance |
| Conclusion | Synthèse, principes | Tous |

## 3. Parcours de lecture par profil

### 3.1 Décideur institutionnel

L'objectif pour le décideur institutionnel est de comprendre le rôle du PTISN dans la hiérarchie documentaire et les enjeux de gouvernance qui en découlent. La lecture recommandée débute par le Préambule (section « Fonction du PTISN »), se poursuit par la Gouvernance (sections « Instance porteuse » et « Homologation »), et s'achève par la Conclusion.

### 3.2 Direction métier / programme

L'objectif pour la direction métier ou le programme est de comprendre comment une initiative s'inscrit dans le cadre technique national. La lecture recommandée débute par le Préambule (section « Position hiérarchique »), se poursuit par les Règles d'utilisation (section « Applicabilité »), et s'achève par le Profil d'initiative, dont le template est à produire.

### 3.3 Équipe technique / développeur

L'objectif pour l'équipe technique ou le développeur est d'implémenter une initiative conforme aux standards nationaux. La lecture recommandée comprend le Préambule (lecture complète), les Règles d'utilisation (lecture complète), la Topologie nationale cible (pour comprendre l'architecture cible), les Profils techniques (consulter les profils applicables PT-XX), la Matrice d'alignement (pour vérifier l'alignement), et le Profil d'initiative (pour produire sa fiche).

### 3.4 Architecte / intégrateur

L'objectif pour l'architecte ou l'intégrateur est d'évaluer et de sélectionner les standards et profils applicables à une initiative. La lecture recommandée comprend la Topologie nationale cible, les Profils techniques (tous les profils), la Matrice d'alignement, et la Gouvernance (sections « Processus d'adoption » et « Critères »).

### 3.5 Partenaire technique / fournisseur

L'objectif pour le partenaire technique ou le fournisseur est d'évaluer la conformité d'un produit ou d'un service aux exigences nationales. La lecture recommandée comprend les Règles d'utilisation (sections « Statuts » et « Versionnement »), les Profils techniques (profils pertinents), et la Gouvernance (section « Homologation d'un produit »).

## 4. Catalogue des profils techniques

Les treize profils couvrent l'ensemble des capacités d'interopérabilité du CNISN. Le tableau suivant présente chaque profil, la capacité CNISN associée et une description synthétique.

| Profil | Capacité CNISN | Description |
|--------|----------------|-------------|
| PT-01 | CAP-INT-03 | Échange interinstitutionnel (X-Road) |
| PT-02 | CAP-INT-03 | Médiation intra-secteur |
| PT-03 | CAP-INT-06 | Catalogue de services et registre de contrats |
| PT-04 | CAP-INT-01 | Résolution d'identité bénéficiaire |
| PT-05 | CAP-INT-02 | Registre des professionnels |
| PT-06 | CAP-INT-04 | Référentiel des structures et services |
| PT-07 | CAP-INT-05 | Terminologie et codification |
| PT-08 | CAP-INT-07 | Échange de données agrégées |
| PT-09 | CAP-INT-07 | Analytique et exposition de données |
| PT-10 | CAP-INT-08 | Confiance, authentification, autorisation |
| PT-11 | CAP-INT-09 | Consentement et bases d'autorisation |
| PT-12 | CAP-INT-10 | Audit, provenance, traçabilité |
| PT-13 | CAP-INT-11 | Qualité et réconciliation des données |

## 5. Statuts des décisions techniques

Chaque standard, profil ou produit porte l'un des statuts suivants, qui indiquent le stade de maturité de la décision technique. Le tableau ci-dessous définit le moment opportun pour consulter chaque statut.

| Statut | Quand consulter |
|--------|-----------------|
| **À instruire** | Besoin identifié, pas encore de solution |
| **Candidat** | En évaluation |
| **Recommandé** | Nouvelles initiatives : privilégier |
| **Retenu pour pilote** | Expérimentation en cours |
| **Retenu nationalement** | Choix validé pour le pays |
| **Homologué** | Conformité démontrée |
| **Déprécié** | Compatibilité temporaire |
| **Retiré** | Ne plus utiliser |

## 6. Liens vers les autres niveaux

Le PTISN s'articule avec les trois niveaux supérieurs de la hiérarchie documentaire et avec le portefeuille national d'initiatives. Le tableau suivant synthétise ces liaisons.

| Niveau | Document | Lien |
|--------|----------|------|
| 1 : CAESN | Cadre d'Architecture d'Entreprise | ../00_caesn/00_overview/index.md |
| 2 : CNISN | Cadre National d'Interopérabilité | ../01_cnisn/index.md |
| 3 : ARTSN | Architecture de Référence Technique | ../02_artsn/index.md |
| : | Portefeuille national d'initiatives | ../00_caesn/06_portfolio/index.md |
| : | Référentiel des profils | ../referentiel/profils/ |

## 7. Documents complémentaires

Trois documents complémentaires accompagnent ce guide de lecture. La matrice de lecture propose une vue croisée profils par lecteurs. Le glossaire du PTISN fournit les définitions des termes techniques. La liste des acronymes du PTISN recense les abréviations utilisées dans ce dossier. Les annexes contiennent les supports complémentaires.

## Références

- **matrice de lecture** : Matrice de lecture du PTISN (niveau 4) (`03_ptisn/reading-matrix.md`)
- **Préambule** : Préambule du PTISN (`03_ptisn/00_introduction/index.md`)
- **Règles d'utilisation** : Partie I : Règles d'utilisation du PTISN (`03_ptisn/01_regles-utilisation/index.md`)
- **Topologie nationale cible** : Partie II : Topologie nationale cible (`03_ptisn/02_topologie-nationale-cible/index.md`)
- **Matrice d'alignement** : Partie IV : Matrice d'alignement (`03_ptisn/04_matrice-alignement/index.md`)
- **Profil d'initiative** : Partie V : Profil technique d'une initiative (`03_ptisn/05_profil-initiative/index.md`)
- **Gouvernance** : Partie VI : Gouvernance du PTISN (`03_ptisn/06_gouvernance/index.md`)
- **Conclusion** : Conclusion du PTISN (`03_ptisn/07_conclusion/index.md`)
- **PT-01** : Profil technique national (`03_ptisn/03_profils/pt-01-echange-interinstitutionnel.md`)
- **PT-02** : Profil technique national (`03_ptisn/03_profils/pt-02-mediation-intra-secteur.md`)
- **PT-03** : Profil technique national (`03_ptisn/03_profils/pt-03-catalogue-services-registre-contrats.md`)
- **PT-04** : Profil technique national (`03_ptisn/03_profils/pt-04-resolution-identite-beneficiaire.md`)
- **PT-05** : Profil technique national (`03_ptisn/03_profils/pt-05-registre-professionnels.md`)
- **PT-06** : Profil technique national (`03_ptisn/03_profils/pt-06-referentiel-structures-services.md`)
- **PT-07** : Profil technique national (`03_ptisn/03_profils/pt-07-terminologie-codification.md`)
- **PT-08** : Profil technique national (`03_ptisn/03_profils/pt-08-echange-donnees-agregees.md`)
- **PT-09** : Profil technique national (`03_ptisn/03_profils/pt-09-analytique-exposition-donnees.md`)
- **PT-10** : Profil technique national (`03_ptisn/03_profils/pt-10-confiance-authentification-autorisation.md`)
- **PT-11** : Profil technique national (`03_ptisn/03_profils/pt-11-consentement-bases-autorisation.md`)
- **PT-12** : Profil technique national (`03_ptisn/03_profils/pt-12-audit-provenance-traçabilité.md`)
- **PT-13** : Profil technique national (`03_ptisn/03_profils/pt-13-qualite-reconciliation.md`)
- **../00_caesn/00_overview/index.md** : Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) (`00_caesn/00_overview/index.md`)
- **../01_cnisn/index.md** : Cadre National d'Interopérabilité de la Santé Numérique (CNISN) (`01_cnisn/index.md`)
- **../02_artsn/index.md** : Architecture de Référence Technique de la Santé Numérique (ARTSN) (`02_artsn/index.md`)
- **../00_caesn/06_portfolio/index.md** : Portefeuille d'initiatives orienté valeur (`00_caesn/06_portfolio/index.md`)
- **glossaire du PTISN** : Glossaire du PTISN (niveau 4) (`03_ptisn/glossary.md`)
- **liste des acronymes du PTISN** : Acronymes et abréviations du PTISN (niveau 4) (`03_ptisn/acronyms.md`)

## Documents de la section

- [ptisn-glossary: Glossaire du PTISN (niveau 4)](glossary.md)
- [ptisn-reading-matrix: Matrice de lecture du PTISN (niveau 4)](reading-matrix.md)
- [ptisn-acronyms: Acronymes et abréviations du PTISN (niveau 4)](acronyms.md)
- [ptisn: Profils techniques d'implémentation de la Santé Numérique (PTISN)](index.md)
- [ptisn-PT-11-consentement-bases-autorisation: PT-11 : Profil technique national](03_profils/pt-11-consentement-bases-autorisation.md)
- [ptisn-PT-05-registre-professionnels: PT-05 : Profil technique national](03_profils/pt-05-registre-professionnels.md)
- [ptisn-PT-02-mediation-intra-secteur: PT-02 : Profil technique national](03_profils/pt-02-mediation-intra-secteur.md)
- [ptisn-PT-11-analyse: Analyse PT-11 : Profil technique du consentement](03_profils/pt-11-analyse-consentement.md)
- [ptisn-PT-13-qualite-reconciliation: PT-13 : Profil technique national](03_profils/pt-13-qualite-reconciliation.md)
- [ptisn-PT-01-echange-interinstitutionnel: PT-01 : Profil technique national](03_profils/pt-01-echange-interinstitutionnel.md)
- [ptisn-profils: Partie III : Profils techniques nationaux](03_profils/pt-00-index.md)
- [ptisn-PT-07-terminologie-codification: PT-07 : Profil technique national](03_profils/pt-07-terminologie-codification.md)
- [ptisn-PT-04-resolution-identite-beneficiaire: PT-04 : Profil technique national](03_profils/pt-04-resolution-identite-beneficiaire.md)
- [ptisn-PT-10-confiance-authentification-autorisation: PT-10 : Profil technique national](03_profils/pt-10-confiance-authentification-autorisation.md)
- [ptisn-PT-12-audit-provenance-traçabilité: PT-12 : Profil technique national](03_profils/pt-12-audit-provenance-traçabilité.md)
- [ptisn-PT-09-analytique-exposition-donnees: PT-09 : Profil technique national](03_profils/pt-09-analytique-exposition-donnees.md)
- [PT-15: PT-15 : Surveillance One Health](03_profils/pt-15-surveillance-one-health.md)
- [ptisn-PT-03-catalogue-services-registre-contrats: PT-03 : Profil technique national](03_profils/pt-03-catalogue-services-registre-contrats.md)
- [ptisn-PT-16-orchestration-processus: PT-16 : Orchestration de processus bornés](03_profils/pt-16-orchestration-processus.md)
- [ptisn-PT-08-echange-donnees-agregees: PT-08 : Profil technique national](03_profils/pt-08-echange-donnees-agregees.md)
- [ptisn-PT-06-referentiel-structures-services: PT-06 : Profil technique national](03_profils/pt-06-referentiel-structures-services.md)
- [PT-14-wrapper: PT-14 : Interopérabilité transfrontalière](03_profils/pt-14-interopabilite-transfrontaliere.md)
- [ptisn-exemples: Exemples de profils d'initiative remplis](05_exemples/index.md)
- [ptisn-matrice-alignement: Partie IV : Matrice d'alignement](04_matrice-alignement/index.md)
- [ptisn-regles-utilisation: Partie I : Règles d'utilisation du PTISN](01_regles-utilisation/index.md)
- [ptisn-introduction: Préambule du PTISN](00_introduction/index.md)
- [ptisn-profil-initiative: Partie V : Profil technique d'une initiative](05_profil-initiative/index.md)
- [ptisn-cas-usage-pilotage: Cas d'usage : Remontée de données et pilotage du système](08_annexes/cas-usage-pilotage-systeme.md)
- [ptisn-cas-usage-couverture: Cas d'usage : Couverture sanitaire et protection financière](08_annexes/cas-usage-couverture-sanitaire.md)
- [ptisn-cas-usage-surveillance: Cas d'usage : Surveillance et riposte épidémique](08_annexes/cas-usage-surveillance-epidemique.md)
- [ptisn-annexe-a: Annexe A : Synthèse des choix](08_annexes/a-synthese-choix.md)
- [ptisn-cas-usage-reference: Cas d'usage : Référence, contre-référence et évacuation sanitaire](08_annexes/cas-usage-reference-evacuation.md)
- [ptisn-annexe-c: Annexe C : Principes de mise en œuvre](08_annexes/c-principes-mise-en-oeuvre.md)
- [ptisn-priorisation-decisions: Priorisation et calendrier : 5 premières décisions PTISN](08_annexes/e-priorisation-decisions.md)
- [ptisn-annexe-b: Annexe B : Décisions à instruire](08_annexes/b-decisions-instruire.md)
- [ptisn-annexe-d: Annexe D : Glossaire](08_annexes/d-glossaire.md)
- [ptisn-topologie: Partie II : Topologie nationale cible](02_topologie-nationale-cible/index.md)
- [ptisn-conclusion: Conclusion du PTISN](07_conclusion/index.md)
- [ptisn-gouvernance: Partie VI : Gouvernance du PTISN](06_gouvernance/index.md)

<!-- liens-section-auto -->
