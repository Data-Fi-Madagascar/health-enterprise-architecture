---
id: CAP-INT-14
type: capacite
niveau: "2"
title: Échanges intersectoriels One Health
status: active
owner: DEPSI
version: "0.5"
family: intersectoriel
envelope: 01_cnisn/02_capacites/index.md
maps_to: ["P-INT-01", "P-INT-05", "P-INT-10", "P-INT-14", "P-INT-16", "P-INT-22"]
implements: []
applies_to: []
related: ["CAP-INT-03", "CAP-INT-13", "CAP-18"]
tags: ["cnisn", "niveau-2", "capacite", "one-health", "intersectoriel"]
---

# Échanges intersectoriels One Health

### Finalité

Permettre les échanges de données entre le secteur santé et les autres secteurs de l'État (agriculture/élevage, environnement, intérieur, météorologie) dans le cadre de l'approche One Health, tout en préservant l'étanchéité juridique et éthique des bases de chaque institution.

### Contexte

L'approche One Health reconnaît l'interdépendance entre la santé humaine, la santé animale et l'environnement. À Madagascar, les enjeux incluent :

- **Zoonoses** : peste, rage, fièvre hémorragique de Rift Valley, brucellose, tuberculose bovine
- **Surveillance environnementale** : déforestation, climat, pollution, eau
- **Sécurité alimentaire** : contamination alimentaire, résistance aux antimicrobiens
- **Épidémies émergentes** : détection précoce à l'interface homme-animal-environnement

Les secteurs concernés :

| Secteur | Ministère | Données produites |
|---------|-----------|-------------------|
| Santé humaine | MSP | Cas cliniques, laboratoire, mortalité |
| Élevage | MINAE | Cheptels, maladies animales, vaccinations animales |
| Environnement | MEEF | Climat, pollution, biodiversité, eau |
| Intérieur | MINUST | Administrations territoriales, populations |
| Météo | DGM | Données climatiques, prévisions |
| Agriculture | MINAE | Productions agricoles, intrants |

### Services attendus

#### Gouvernance des échanges intersectoriels

- enregistrement des accords de partage entre ministères ;
- définition des flux autorisés par secteur et par finalité ;
- gestion des bases légales par secteur (secret médical, secret professionnel vétérinal, secret environnemental) ;
- arbitrage des conflits d'autorité entre secteurs ;
- suivi de la conformité des échanges.

#### Médiation intersectorielle

- transformation sémantique entre taxonomies sectorielles (CIM-10 pour santé humaine, OIE pour animaux, classification environnementale) ;
- normalisation des dimensions communes (espace, temps, géographie) ;
- corrélation des signaux faibles entre secteurs ;
- détection de clusters intersectoriels.

#### Cloisonnement et étanchéité

- séparation stricte des identités entre secteurs (pas de croisement d'identités humaines et animales) ;
- agrégation croisée sans désanonymisation ;
- journalisation distincte par secteur ;
- contrôle d'accès différencié par rôle sectoriel.

#### Alertes et coordination

- déclenchement d'alertes intersectorielles ;
- notification aux autorités compétentes de chaque secteur ;
- coordination des plans de riposte ;
- retour d'expérience post-crise.

### Exigences de conformité

| Exigence | Description |
|----------|-------------|
| **EXG-OH-01** | Tout échange intersectoriel doit être couvert par un accord explicite entre ministères ([P-INT-10: Accord préalable](../principes/p-int-10.md)) |
| **EXG-OH-02** | Les identités humaines ne doivent jamais être croisées avec les identités animales |
| **EXG-OH-03** | Les données agrégées croisées doivent être irréversiblement désanonymisées |
| **EXG-OH-04** | Chaque secteur conserve la souveraineté sur ses données source |
| **EXG-OH-05** | Les dimensions d'agrégation communes (espace, temps, géographie) doivent être normalisées |
| **EXG-OH-06** | Tous les échanges intersectoriels doivent être journalisés et auditables |
| **EXG-OH-07** | Le cadre Tripartite Plus (OMS–WOAH–FAO–PNUE) doit être respecté pour les flux internationaux |

### Principes associés


- [P-INT-01: Autorité désignée](../principes/p-int-01.md) (Autorité désignée) : chaque secteur reste l'autorité de ses données ;
- [P-INT-05: Contrat explicite](../principes/p-int-05.md) (Contrat explicite) : tout flux intersectoriel nécessite un accord ;
- [P-INT-10: Accord préalable](../principes/p-int-10.md) (Accord préalable) : accord obligatoire entre ministères ;
- [P-INT-14: Base d’autorisation explicite](../principes/p-int-14.md) (Base d'autorisation explicite) : base légale documentée par secteur ;
- [P-INT-16: Résidence et non-réplication](../principes/p-int-16.md) (Résidence) : les données restent dans leur secteur d'origine ;
- [P-INT-22: Fonctionnement en connectivité contrainte](../principes/p-int-22.md) (Connectivité contrainte) : les secteurs ont des niveaux de connectivité variables.

### Rattachement

- [CAP-18: Coordination intersectorielle (One Health)](../../referentiel/capabilites/cap-18.md) (Coordination intersectorielle — One Health)
- [CAP-05: Surveillance épidémiologique, alerte, investigation et riposte](../../referentiel/capabilites/cap-05.md) (Surveillance épidémiologique)
- [ART-11](../../referentiel/chapitres/art-11.md) (Coordination intersectorielle)
- [ART-0](../../referentiel/chapitres/art-0.md) (Accords de partage inter-institutionnels)
- [ART-4d](../../referentiel/chapitres/art-4d.md) (Référentiel géospatial)
- [F.2](../../referentiel/fondations/f-2.md) (Souveraineté intersectorielle)
- [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../../referentiel/exigences/enf-4.md) (Cloisonnement inter-institutionnel One Health)
