---

title: "Exigences contextuelles nationales"
id: artsn-exigences-contextuelles
domain: 02_exigences-contextuelles
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: ["artsn", "exigences", "contexte", "niveau-3"]
---

# Exigences contextuelles nationales

## Pour qui lire ce document

**Niveau :** niveau 3 : Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.


Les exigences contextuelles traduisent les contraintes nationales (géographie, réseau, interopérabilité inter-institutionnelle) en obligations qui s'imposent à tout chapitre et à toute solution. Chaque exigence vit dans le référentiel : `referentiel/exigences/enf-X.md`.

## Catalogue des exigences

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Résilience à l’instabilité réseau

**Contenu normatif.** La connectivité internet et la couverture mobile (3G/4G/Fibre) sont hautement asymétriques, intermittentes, voire inexistantes dans la majorité des districts ruraux et des Centres de Santé de Base (CSB). L’indisponibilité, la coupure ou la dégradation du réseau ne doit en aucun cas bloquer, ralentir ou altérer l’acte clinique, la dispensation pharmaceutique au comptoir ou la saisie logistique. Tout logiciel et base de données utilisés sur le point de service ont l’obligation structurelle de **capturer, valider et persister les transactions de manière 100 % locale et autonome**, puis de gérer des mécanismes de **synchronisation asynchrone** pour différer la transmission centrale dès le retour de la connectivité.

**Statut : Stable.** — appliqué par [F.1](../../referentiel/fondations/f-1.md), [ART-1](../../referentiel/chapitres/art-1.md), Couche 2 (point de service).

#### Justification

La connectivité internet et mobile reste asymétrique, intermittente ou absente dans la majorité des districts ruraux et des CSB, rendant les architectures transactionnelles centralisées synchrones inadaptées. Cette exigence protège l’acte clinique, la dispensation et la saisie logistique contre toute coupure réseau en imposant la capture locale autonome et la synchronisation différée. Elle évite la perte ou la duplication d’événements de santé lors des micro-coupures.

#### Capabilités concernées

- [CAP-13: Système d'information sanitaire, données et recherche](../../referentiel/capabilites/cap-13.md) — Système d'information sanitaire, données et recherche
- [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../../referentiel/capabilites/cap-14.md) — Interopérabilité, référentiels nationaux et infrastructure numérique partagée
- [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../../referentiel/capabilites/cap-15.md) — Cybersécurité, confidentialité et gouvernance des données personnelles

#### Parties prenantes concernées

- [PP-05: Agent de santé](../../referentiel/parties-prenantes/pp-05.md) — Agent de santé
- [PP-06: Formation sanitaire](../../referentiel/parties-prenantes/pp-06.md) — Formation sanitaire
- [PP-10: Équipes techniques (DEPSI / SIS)](../../referentiel/parties-prenantes/pp-10.md) — Équipes techniques (DEPSI / SIS)

#### Fondations et chapitres garants

- **F.1** — Résilience face à la réalité géographique du pays
- [ART-1: Intégration et ingestion](../../referentiel/chapitres/art-1.md) — Intégration et ingestion
- [ART-3: Historisation événementielle et profils de déploiement](../../referentiel/chapitres/art-3.md) — Historisation événementielle et profils de déploiement
- [ART-7: Sécurité, contrôle d'accès et résidence de la donnée](../../referentiel/chapitres/art-7.md) — Sécurité, contrôle d'accès et résidence de la donnée
- **ART-8C** — Agrégation par lot
- **ART-4C** — Éligibilité et couverture

### Intégrité des flux et traçabilité des valeurs

**Contenu normatif.** Le déploiement national de la gratuité ciblée, des subventions de l’État et des mécanismes de la Couverture Santé Universelle (CSU) présente un risque systémique élevé de fraude, de double facturation, de falsification d’ordonnances et de détournement de stocks. L’architecture doit interdire toute modification, suppression ou altération rétroactive des transactions logistiques et financières validées. Tout mouvement de valeur (Ariary ou unités physiques de médicaments) doit obéir à des règles strictes de **double écriture comptable** et de **conservation de quantité** (Entrées − Sorties = Solde), garantissant une réconciliation exacte à somme nulle.

**Statut : Stable.** — appliqué par [ART-9 (garanties transactionnelles)](../../referentiel/chapitres/art-9.md), [ART-4C (éligibilité)](../../referentiel/chapitres/art-4c.md), [ART-8C (agrégation par lot)](../../referentiel/chapitres/art-8c.md).

#### Justification

Le déploiement national de la gratuité ciblée, des subventions et de la CSU crée un risque systémique de fraude, de double facturation et de détournement de stocks. Cette exigence interdit toute altération rétroactive des transactions et impose la double écriture comptable pour garantir une réconciliation à somme nulle. Elle protège l’argent public et la confiance des ménages dans les mécanismes de protection financière.

#### Capabilités concernées

- [CAP-07: Protection financière, couverture santé universelle](../../referentiel/capabilites/cap-07.md) — Protection financière, couverture santé universelle
- [CAP-10: Gestion des médicaments, vaccins, intrants et chaîne d'approvisionnement](../../referentiel/capabilites/cap-10.md) — Gestion des médicaments, vaccins, intrants et chaîne d'approvisionnement
- [CAP-12: Finances publiques, budget et allocation des ressources](../../referentiel/capabilites/cap-12.md) — Finances publiques, budget et allocation des ressources
- [CAP-13: Système d'information sanitaire, données et recherche](../../referentiel/capabilites/cap-13.md) — Système d'information sanitaire, données et recherche

#### Parties prenantes concernées

- [PP-02: Ménage et famille](../../referentiel/parties-prenantes/pp-02.md) — Ménage et famille
- [PP-06: Formation sanitaire](../../referentiel/parties-prenantes/pp-06.md) — Formation sanitaire
- [PP-08: Partenaires techniques et financiers](../../referentiel/parties-prenantes/pp-08.md) — Partenaires techniques et financiers

#### Fondations et chapitres garants

- [ART-9: Garanties transactionnelles fortes](../../referentiel/chapitres/art-9.md) — Garanties transactionnelles fortes
- **ART-4C** — Éligibilité et couverture
- **ART-8C** — Agrégation par lot

### Unicité de l’identité et résilience face à la fragmentation applicative

**Contraintes contextuelles.** Le paysage numérique historique est caractérisé par une dispersion de solutions logicielles et de bases de données isolées. Un même citoyen possède des fiches cliniques, des dossiers et des identifiants locaux différents selon les hôpitaux ou les programmes verticaux (Malariologie, Tuberculose, Vaccination), ce qui menace la sécurité des soins et empêche le suivi médical longitudinal.

**Contenu normatif.** Le système national doit posséder la capacité de rapprocher, consolider et unifier des identités de patients incertains, phonétiquement variables ou incomplètes. Cette brique d’**identitovigilance** doit générer un enregistrement pivot unique et souverain pour le citoyen, sans forcer le remplacement immédiat ou la refonte structurelle des bases locales des hôpitaux.

**Statut : Stable.** — appliqué par [ART-4A (résolution d’identité)](../../referentiel/chapitres/art-4a.md), [ART-2 (médiation)](../../referentiel/chapitres/art-2.md).

#### Justification

Le paysage numérique historique est marqué par une dispersion de solutions et de bases isolées, où un même citoyen cumule des fiches et identifiants différents selon les structures ou programmes. Cette fragmentation menace la sécurité des soins et empêche le suivi médical longitudinal. L’exigence d’unicité permet de consolider une identité pivot souveraine sans forcer la refonte immédiate des systèmes locaux.

#### Capabilités concernées

- [CAP-17: Engagement patient et identité numérique](../../referentiel/capabilites/cap-17.md) — Engagement patient et identité numérique
- [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../../referentiel/capabilites/cap-14.md) — Interopérabilité, référentiels nationaux et infrastructure numérique partagée
- [CAP-13: Système d'information sanitaire, données et recherche](../../referentiel/capabilites/cap-13.md) — Système d'information sanitaire, données et recherche

#### Parties prenantes concernées

- [PP-01: Patient et usager](../../referentiel/parties-prenantes/pp-01.md) — Patient et usager
- [PP-06: Formation sanitaire](../../referentiel/parties-prenantes/pp-06.md) — Formation sanitaire
- [PP-10: Équipes techniques (DEPSI / SIS)](../../referentiel/parties-prenantes/pp-10.md) — Équipes techniques (DEPSI / SIS)

#### Fondations et chapitres garants

- **ART-4A** — Résolution d'identité
- [ART-2: Médiation et normalisation](../../referentiel/chapitres/art-2.md) — Médiation et normalisation

### Cloisonnement inter-institutionnel et étanchéité des données (One Health)

**Contraintes contextuelles.** Le croisement de données massives entre le Ministère de la Santé (données cliniques), l’Agriculture et l’Élevage (zoonoses) et l’Environnement (climat, pollution) implique la manipulation de taxonomies, de secrets professionnels et de bases légales juridiquement et éthiquement étanches.

**Contenu normatif.** Le partage d’informations intersectoriel à des fins de recherche ou d’alerte épidémique précoce doit préserver la souveraineté de chaque institution, respecter le secret médical et protéger la vie privée des citoyens. Les pipelines de traitement analytique ont l’obligation d’opérer sur des données **définitivement dépouillées de tout identifiant direct** (Noms, INS). Les corrélations entre secteurs ne doivent s’effectuer qu’avec des dimensions de rapprochement **neutres et non nominatives** : l’espace géographique et le temps.

**Statut : Stable.** — appliqué par [ART-0 (accords de partage)](../../referentiel/chapitres/art-0.md), [ART-4B (bases d’autorisation)](../../referentiel/chapitres/art-4b.md), [ART-4D (référentiel géospatial)](../../referentiel/chapitres/art-4d.md).

#### Justification

Le croisement de données massives entre Santé, Agriculture/Élevage et Environnement implique des taxonomies, des secrets professionnels et des bases légales juridiquement étanches. Cette exigence préserve la souveraineté de chaque institution et le secret médical en opérant sur des données définitivement dépouillées d’identifiants directs. Les corrélations intersectorielles ne s’appuient ainsi que sur des dimensions neutres et non nominatives : l’espace géographique et le temps.

#### Capabilités concernées

- [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../../referentiel/capabilites/cap-14.md) — Interopérabilité, référentiels nationaux et infrastructure numérique partagée
- [CAP-18: Coordination intersectorielle (One Health)](../../referentiel/capabilites/cap-18.md) — Coordination intersectorielle (One Health)
- [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../../referentiel/capabilites/cap-15.md) — Cybersécurité, confidentialité et gouvernance des données personnelles

#### Parties prenantes concernées

- [PP-03: Population](../../referentiel/parties-prenantes/pp-03.md) — Population
- [PP-07: District, région et Ministère](../../referentiel/parties-prenantes/pp-07.md) — District, région et Ministère
- [PP-08: Partenaires techniques et financiers](../../referentiel/parties-prenantes/pp-08.md) — Partenaires techniques et financiers
- [PP-10: Équipes techniques (DEPSI / SIS)](../../referentiel/parties-prenantes/pp-10.md) — Équipes techniques (DEPSI / SIS)

#### Fondations et chapitres garants

- [ART-0: Accords de partage inter-institutionnels](../../referentiel/chapitres/art-0.md) — Accords de partage inter-institutionnels
- **ART-4B** — Bases d'autorisation
- **ART-4D** — Référentiel géospatial et d'exploitation partagé
- **F.2** — Préservation de la souveraineté intersectorielle
- [ART-2: Médiation et normalisation](../../referentiel/chapitres/art-2.md) — Médiation et normalisation
- [ART-6: Analytique et restitution](../../referentiel/chapitres/art-6.md) — Analytique et restitution
- **ART-8B** — Modélisation de relations en graphe
- **ART-8D** — Chorégraphie inter-institutionnelle
- [ART-4: Référentiels de métadonnées de gestion](../../referentiel/chapitres/art-4.md) — Référentiels de métadonnées de gestion

### Coordination des processus complexes décentralisés et asynchrones

**Contraintes contextuelles.** Les parcours de soins critiques (référence d'un CSB rural vers un hôpital de district, contre-référence ascendante vers un CHU central, ou évacuation sanitaire internationale) s'étendent sur des fenêtres temporelles de plusieurs jours et impliquent des structures sanitaires autonomes sans lien hiérarchique ou technique direct.

**Contenu normatif.** Le système national doit être capable de suivre et d'orchestrer l'état d'avancement d'un parcours de soins distribué à étapes multiples, de bout en bout. L'architecture doit tolérer les interruptions temporaires de transmission, tout en garantissant le déclenchement automatique d'alertes d'escalade ou d'annulations (compensations) fonctionnelles si un établissement de destination est saturé ou inaccessible.

**Statut : Stable.** — appliqué par [ART-8A (orchestration de processus borné)](../../referentiel/chapitres/art-8a.md), [ART-5 (qualité des données)](../../referentiel/chapitres/art-5.md), [PT-14 (interopérabilité transfrontalière)](../../03_ptisn/03_profils/pt-14-interopabilite-transfrontaliere.md).

#### Justification

Les parcours de soins critiques s’étendent sur plusieurs jours et impliquent des structures autonomes sans lien hiérarchique ou technique direct. Cette exigence permet de suivre et d’orchestrer un parcours distribué de bout en bout tout en tolérant les interruptions de transmission. Elle garantit le déclenchement d’alertes d’escalade ou de compensations si une structure de destination est saturée ou inaccessible.

#### Capabilités concernées

- [CAP-02: Gestion du parcours patient, référence et contre-référence](../../referentiel/capabilites/cap-02.md) — Gestion du parcours patient, référence et contre-référence
- [CAP-13: Système d'information sanitaire, données et recherche](../../referentiel/capabilites/cap-13.md) — Système d'information sanitaire, données et recherche
- [CAP-16: Gestion du portefeuille d'initiatives numériques](../../referentiel/capabilites/cap-16.md) — Gestion du portefeuille d'initiatives numériques

#### Parties prenantes concernées

- [PP-01: Patient et usager](../../referentiel/parties-prenantes/pp-01.md) — Patient et usager
- [PP-05: Agent de santé](../../referentiel/parties-prenantes/pp-05.md) — Agent de santé
- [PP-06: Formation sanitaire](../../referentiel/parties-prenantes/pp-06.md) — Formation sanitaire

#### Fondations et chapitres garants

- **ART-8A** — Orchestration de processus borné
- [ART-8: Orchestration de processus](../../referentiel/chapitres/art-8.md) — Orchestration de processus
- [ART-5: Cohérence et qualité des données](../../referentiel/chapitres/art-5.md) — Cohérence et qualité des données
- [PT-14: Interopérabilité transfrontalière](../../referentiel/profils/pt-14.md) — Interopérabilité transfrontalière

<!-- END:GENERATED -->
## Liens

- Fondations
- Chapitres et patterns de référence
- Cartographie cible

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **Fondations** : Fondations de l'ARTSN (`02_artsn/00_fondations/index.md`)
- **Chapitres et patterns de référence** : Chapitres et patterns de référence (`02_artsn/04_patterns/index.md`)
- **Cartographie cible** : Cartographie conceptuelle cible (`02_artsn/05_cartographie/index.md`)
