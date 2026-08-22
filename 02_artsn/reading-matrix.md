---

title: Matrice de lecture de l'ARTSN (niveau 3)
id: artsn-reading-matrix
domain: 02_artsn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-09
owner: DEPSI
tags: ["artsn", "lecture", "niveau-3", "profils"]
---

# Matrice de lecture de l'ARTSN (niveau 3)

Légende : **●** = lecture prioritaire, **◐** = lecture complémentaire, **○** = lecture ponctuelle.

L'ARTSN décline le niveau 1 en **familles de patterns validées**, **standards techniques et formats d'échange**, **contrats d'interfaces** et **règles d'homologation**. Elle s'adresse en priorité au DEPSI, aux architectes et aux intégrateurs ; les décideurs et directions métier ne la consultent que sur des points précis.

| Document du niveau 3 | Décideurs institutionnels | Directions métier / programmes | DEPSI / équipes techniques | SIS / données / suivi-évaluation | Partenaires techniques et financiers |
|----------------------|---------------------------|-------------------------------|----------------------------|----------------------------------|--------------------------------------|
| Guide de lecture de l'ARTSN | ● | ◐ | ● | ◐ | ● |
| Index de l'ARTSN | ● | ◐ | ● | ◐ | ● |
| Partie I : Fondations invariantes | ● | ◐ | ● | ◐ | ● |
| Partie II : Flux de valeur | ◐ | ● | ● | ◐ | ◐ |
| Partie III : Exigences contextuelles nationales | ◐ | ◐ | ● | ◐ | ◐ |
| Partie IV : Chapitres et patterns de référence | ○ | ◐ | ● | ● | ◐ |
| ART-0 : Accords de partage | ◐ | ● | ● | ◐ | ◐ |
| ART-1 : Intégration et ingestion | ○ | ○ | ● | ● | ◐ |
| ART-2 : Médiation et normalisation | ○ | ○ | ● | ● | ◐ |
| ART-3 : Historisation événementielle | ○ | ○ | ● | ● | ◐ |
| ART-4 : Référentiels de métadonnées | ○ | ○ | ● | ● | ◐ |
| ART-4a : Résolution d'identité | ○ | ○ | ● | ● | ◐ |
| ART-4b : Bases d'autorisation | ○ | ○ | ● | ● | ◐ |
| ART-4c : Éligibilité et couverture | ○ | ● | ● | ◐ | ◐ |
| ART-4d : Référentiel géospatial | ○ | ● | ● | ◐ | ◐ |
| ART-5 : Cohérence et qualité des données | ○ | ○ | ● | ● | ◐ |
| ART-6 : Analytique et restitution | ◐ | ● | ● | ● | ◐ |
| ART-7 : Sécurité et contrôle d'accès | ◐ | ◐ | ● | ● | ◐ |
| ART-8 : Orchestration de processus | ○ | ◐ | ● | ● | ◐ |
| ART-8a : Orchestration de processus borné | ○ | ○ | ● | ● | ◐ |
| ART-8b : Modélisation en graphe | ○ | ○ | ● | ● | ◐ |
| ART-8c : Agrégation par lot | ○ | ○ | ● | ● | ◐ |
| ART-8d : Chorégraphie inter-institutionnelle | ◐ | ● | ● | ◐ | ◐ |
| ART-9 : Garanties transactionnelles | ○ | ● | ● | ◐ | ◐ |
| Partie V : Cartographie conceptuelle cible | ◐ | ◐ | ● | ● | ◐ |
| Partie VI : Dictionnaire de données | ○ | ◐ | ● | ● | ◐ |
| Partie VI : Gouvernance de l'ARTSN | ● | ◐ | ● | ◐ | ● |
| Annexe A : Table de maturité | ○ | ◐ | ● | ◐ | ◐ |
| Annexe B : Glossaire des patterns | ○ | ○ | ● | ◐ | ◐ |
| Glossaire de l'ARTSN | ○ | ◐ | ● | ◐ | ◐ |
| Acronymes de l'ARTSN | ○ | ◐ | ● | ◐ | ◐ |
| Annexe C : Renvoi CAESN et capacités candidates | ● | ● | ● | ◐ | ● |

## Lectures croisées

Pour compléter la lecture de l'ARTSN, plusieurs documents du CAESN et de la CNISN offrent des perspectives transversales. L'architecture applicative décrite dans les couches et composants figure dans CAESN : applications. Les standards et normes déclinés dans l'ARTSN sont détaillés dans CAESN : normes. Enfin, les chapitres ART sont rattachés au CAESN via l'index des chapitres et la table de maturité.

## Matrices des autres niveaux

La matrice de lecture de l'ARTSN s'inscrit dans un ensemble cohérent de matrices couvrant les quatre niveaux de l'architecture. Le niveau 1 : CAESN présente la vue d'ensemble stratégique. Le niveau 2 : CNISN détaille le cadre d'interopérabilité. Le niveau 4 : PTISN référence les profils techniques par initiative.

## Liens

Les ressources complémentaires incluent l'Index de l'ARTSN, le Glossaire de l'ARTSN, les Acronymes de l'ARTSN, l'ensemble des Chapitres ART-0..ART-9 et le CAESN niveau 1.

## Références

- **Guide de lecture de l'ARTSN** : Guide de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-guide.md`)
- **Index de l'ARTSN** : Architecture de Référence Technique de la Santé Numérique (ARTSN) (`02_artsn/index.md`)
- **Partie I : Fondations invariantes** : Fondations de l'ARTSN (`02_artsn/00_fondations/index.md`)
- **Partie II : Flux de valeur** : Flux de valeur (`02_artsn/01_flux-de-valeur/index.md`)
- **Partie III : Exigences contextuelles nationales** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
- **Partie IV : Chapitres et patterns de référence** : Chapitres et patterns de référence (`02_artsn/04_patterns/index.md`)
- **ART-0 : Accords de partage** : Accords de partage inter-institutionnels (`referentiel/chapitres/art-0.md`)
- **ART-1 : Intégration et ingestion** : Intégration et ingestion (`referentiel/chapitres/art-1.md`)
- **ART-2 : Médiation et normalisation** : Médiation et normalisation (`referentiel/chapitres/art-2.md`)
- **ART-3 : Historisation événementielle** : Historisation événementielle et profils de déploiement (`referentiel/chapitres/art-3.md`)
- **ART-4 : Référentiels de métadonnées** : Référentiels de métadonnées de gestion (`referentiel/chapitres/art-4.md`)
- **ART-4a : Résolution d'identité** : Résolution d'identité (`referentiel/chapitres/art-4a.md`)
- **ART-4b : Bases d'autorisation** : Bases d'autorisation (`referentiel/chapitres/art-4b.md`)
- **ART-4c : Éligibilité et couverture** : Éligibilité et couverture (`referentiel/chapitres/art-4c.md`)
- **ART-4d : Référentiel géospatial** : Référentiel géospatial et d'exploitation partagé (`referentiel/chapitres/art-4d.md`)
- **ART-5 : Cohérence et qualité des données** : Cohérence et qualité des données (`referentiel/chapitres/art-5.md`)
- **ART-6 : Analytique et restitution** : Analytique et restitution (`referentiel/chapitres/art-6.md`)
- **ART-7 : Sécurité et contrôle d'accès** : Sécurité, contrôle d'accès et résidence de la donnée (`referentiel/chapitres/art-7.md`)
- **ART-8 : Orchestration de processus** : Orchestration de processus (`referentiel/chapitres/art-8.md`)
- **ART-8a : Orchestration de processus borné** : Orchestration de processus borné (`referentiel/chapitres/art-8a.md`)
- **ART-8b : Modélisation en graphe** : Modélisation de relations en graphe (`referentiel/chapitres/art-8b.md`)
- **ART-8c : Agrégation par lot** : Agrégation par lot (`referentiel/chapitres/art-8c.md`)
- **ART-8d : Chorégraphie inter-institutionnelle** : Chorégraphie inter-institutionnelle (`referentiel/chapitres/art-8d.md`)
- **ART-9 : Garanties transactionnelles** : Garanties transactionnelles fortes (`referentiel/chapitres/art-9.md`)
- **Partie V : Cartographie conceptuelle cible** : Cartographie conceptuelle cible (`02_artsn/05_cartographie/index.md`)
- **Partie VI : Dictionnaire de données** : Dictionnaire de données fonctionnelles (`02_artsn/03_objets-de-donnees/index.md`)
- **Partie VI : Gouvernance de l'ARTSN** : Gouvernance de l'ARTSN (`02_artsn/06_gouvernance/index.md`)
- **Annexe A : Table de maturité** : Annexe A : Table de maturité par chapitre (`02_artsn/08_annexes/a-table-de-maturite.md`)
- **Annexe B : Glossaire des patterns** : Annexe B : Glossaire des patterns cités (`02_artsn/08_annexes/b-glossaire-patterns.md`)
- **Glossaire de l'ARTSN** : Glossaire de l'ARTSN (niveau 3) (`02_artsn/glossary.md`)
- **Acronymes de l'ARTSN** : Acronymes et abréviations de l'ARTSN (niveau 3) (`02_artsn/acronyms.md`)
- **Annexe C : Renvoi CAESN et capacités candidates** : Annexe C : Renvoi CAESN et capacités candidates (`02_artsn/08_annexes/c-renvoi-capacites-candidates.md`)
- **CAESN : applications** : Architecture applicative et systèmes numériques (`00_caesn/05_application/index.md`)
- **CAESN : normes** : Normes et standards d'architecture (`01_cnisn/05_standards/index.md`)
- **index des chapitres** : Chapitres et patterns de référence (`02_artsn/04_patterns/index.md`)
- **table de maturité** : Annexe A : Table de maturité par chapitre (`02_artsn/08_annexes/a-table-de-maturite.md`)
- **niveau 1 : CAESN** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **niveau 2 : CNISN** : Matrice de lecture du CNISN (niveau 2) (`01_cnisn/reading-matrix.md`)
- **niveau 4 : PTISN** : Matrice de lecture du PTISN (niveau 4) (`03_ptisn/reading-matrix.md`)
- **Chapitres ART-0..ART-9** : Chapitres et patterns de référence (`02_artsn/04_patterns/index.md`)
- **CAESN niveau 1** : Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) (`00_caesn/00_overview/index.md`)

## Documents de la section

- [artsn-glossary: Glossaire de l'ARTSN (niveau 3)](glossary.md)
- [artsn-acronyms: Acronymes et abréviations de l'ARTSN (niveau 3)](acronyms.md)
- [artsn: Architecture de Référence Technique de la Santé Numérique (ARTSN)](index.md)
- [artsn-reading-guide: Guide de lecture de l'ARTSN (niveau 3)](reading-guide.md)
- [artsn-annexe-a-maturite: Annexe A : Table de maturité par chapitre](08_annexes/a-table-de-maturite.md)
- [artsn-annexe-c-renvoi: Annexe C : Renvoi CAESN et capacités candidates](08_annexes/c-renvoi-capacites-candidates.md)
- [artsn-annexe-b-glossaire-patterns: Annexe B : Glossaire des patterns cités](08_annexes/b-glossaire-patterns.md)
- [artsn-annexes: Annexes de l'ARTSN](08_annexes/index.md)
- [artsn-protocole-test: Annexe D : Protocole de test d'interopérabilité](08_annexes/d-protocole-test-interopabilite.md)
- [artsn-sla-performance: Annexe E : SLA et métriques de performance par profil](08_annexes/e-sla-performance.md)
- [artsn-cartographie-cible: Cartographie conceptuelle cible](05_cartographie/index.md)
- [ART-8D: ART-8d : Chorégraphie inter-institutionnelle](04_patterns/art-8d-choregraphie-interinstitutionnelle.md)
- [ART-8: ART-8 : Orchestration de processus](04_patterns/art-8-orchestration-processus-borne.md)
- [ART-4D: ART-4d : Référentiel géospatial et d'exploitation partagé](04_patterns/art-4d-referentiel-geospatial.md)
- [ART-7: ART-7 : Sécurité, contrôle d'accès et résidence de la donnée](04_patterns/art-7-securite-controle-acces.md)
- [ART-3: ART-3 : Historisation événementielle et profils de déploiement](04_patterns/art-3-historisation-evenementielle.md)
- [ART-10: ART-10 : Logistique](04_patterns/art-10-logistique.md)
- [ART-8B: ART-8b : Modélisation de relations en graphe](04_patterns/art-8b-modelisation-graphe.md)
- [ART-4C: ART-4c : Éligibilité et couverture](04_patterns/art-4c-eligibilite-couverture.md)
- [ART-5: ART-5 : Cohérence et qualité des données](04_patterns/art-5-coherence-qualite-donnees.md)
- [ART-0: ART-0 : Accords de partage inter-institutionnels](04_patterns/art-0-accords-partage.md)
- [ART-4B: ART-4b : Bases d'autorisation](04_patterns/art-4b-bases-autorisation.md)
- [ART-11: ART-11 : Coordination intersectorielle](04_patterns/art-11-coordination-intersectorielle.md)
- [ART-8C: ART-8c : Agrégation par lot](04_patterns/art-8c-agregation-par-lot.md)
- [ART-2: ART-2 : Médiation et normalisation](04_patterns/art-2-mediation-normalisation.md)
- [ART-4: ART-4 : Référentiels de métadonnées de gestion](04_patterns/art-4-referentiels-metadonnees.md)
- [artsn-chapitres: Chapitres et patterns de référence](04_patterns/index.md)
- [ART-6: ART-6 : Analytique et restitution](04_patterns/art-6-analytique-restitution.md)
- [ART-1: ART-1 : Intégration et ingestion](04_patterns/art-1-integration-ingestion.md)
- [ART-8A: ART-8a : Orchestration de processus borné](04_patterns/art-8a-orchestration-processus-borne.md)
- [ART-9: ART-9 : Garanties transactionnelles fortes](04_patterns/art-9-garanties-transactionnelles.md)
- [ART-4A: ART-4a : Résolution d'identité](04_patterns/art-4a-resolution-identite.md)
- [artsn-dictionnaire-donnees: Dictionnaire de données fonctionnelles](03_objets-de-donnees/index.md)
- [artsn-exigences-contextuelles: Exigences contextuelles nationales](02_exigences-contextuelles/index.md)
- [artsn-fondations: Fondations de l'ARTSN](00_fondations/index.md)
- [roadmap-deploiement-artsn: Feuille de route de déploiement progressif de l'ARTSN](07_lots/index.md)
- [artsn-flux-de-valeur: Flux de valeur](01_flux-de-valeur/index.md)
- [artsn-gouvernance: Gouvernance de l'ARTSN](06_gouvernance/index.md)
- [conformite: Tableau de bord de conformité architecturale](06_gouvernance/conformite.md)
- [depreciation: Processus de dépréciation des composants](06_gouvernance/depreciation.md)
- [veille-architecturale: Veille architecturale](06_gouvernance/veille-architecturale.md)

<!-- liens-section-auto -->
