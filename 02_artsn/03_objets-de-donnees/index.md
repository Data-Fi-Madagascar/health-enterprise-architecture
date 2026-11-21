---

title: Dictionnaire de données fonctionnelles
id: artsn-dictionnaire-donnees
domain: 03_objets-de-donnees
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: ["artsn", "dictionnaire", "donnees", "semantique", "niveau-3"]
related: ["ARTSN", "CNISN", "CAESN"]
---

# Dictionnaire de données fonctionnelles

## Pour qui lire ce document

**Niveau :** niveau 3 : Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

Le dictionnaire de données fixe l'**atome d'information métier pur**, exempt de toute abréviation ou contrainte technologique. Il sert de **référentiel de sémantique universelle** pour la validation inter-ministérielle des contrats d'interfaces, conformément au chapitre ART-2 (médiation et normalisation) et aux fondations F.2 et F.3.

Chaque contrat technique d'interface publié dans le registre de schémas doit s'appuyer sur les concepts sémantiques définis dans ce dictionnaire. Les définitions s'organisent par domaines fonctionnels du CAESN.

## Légende des champs

| Champ | Description |
|-------|-------------|
| **Nom** | Désignation canonique en français, sans abréviation |
| **Définition** | Sémantique métier précise, unique et non ambiguë |
| **Type** | Catégorie de donnée (identifiant, date, quantité, codage, texte libre, binaire) |
| **Contraintes** | Règles de validation, format, cardinalité |
| **Rattachement** | Capabilité(s) et/ou flux de valeur concerné(s) |
| **Référentiel source** | Référentiel national ou standard international de référence |
| **Codification** | Terminologie(s) dont les codes régissent les valeurs de l'objet |

## 1. Patient & identité

**Objet métier CAESN correspondant** : [BO-01 : Patient & identité](../../00_caesn/04_data/objets.md).

<!-- BEGIN:GENERATED mode=catalogue source=04_architecture-repository/02_architecture-elements/data/data-objects/do-01.md,04_architecture-repository/02_architecture-elements/data/data-objects/do-03.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### DO-01 : Patient

Personne physique bénéficiaire de soins de santé, identifiée de manière unique au sein du système d'information sanitaire national. L'identité du patient est un actif stratégique national qui ne peut être dupliquée, fragmentée ou remplacée par des identifiants propriétaires de programmes ou de projets. L'identifiant national d'identification est porté par cet objet, comme valeur de l'identifiant patient, et non comme un objet distinct.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-01 (continuité des soins)](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-01.md), [CAP-13 (interopérabilité données)](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-13.md), [CAP-14 (référentiels nationaux)](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-14.md) et [CAP-17 (engagement patient et identité numérique)](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-17.md), et contribue aux flux de valeur [VS-01 (parcours patient)](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-03 (protection financière)](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md). Il est porté par l'objet métier [BO-01 : Patient & identité](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-01.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md), [ART-7](../../04_architecture-repository/04_patterns/artsn-rules/art-7.md).

#### Attributs et contraintes

- **Type** : Entité (identifiant unique + attributs)
- **Contraintes** : Identifiant unique national (NIN ou identifiant provisoire) ; un seul enregistrement par personne physique ; traçabilité des doublons détectés et résolus
- **Identifiant national d'identification** : Format de 12 chiffres selon le modèle INSTAT ; attribué une seule fois ; non modifiable après validation ; traçabilité des attributions
- **Référentiel source** : Référentiel des bénéficiaires / patients (CAESN)

#### Rattachement

- **Capacités** : [CAP-01 (continuité des soins)](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-01.md), [CAP-13 (interopérabilité données)](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-13.md), [CAP-14 (référentiels nationaux)](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-14.md), [CAP-17 (engagement patient et identité numérique)](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-17.md)
- **Profils (PTISN)** : [PT-04 (identité nationale)](../../04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-04.md)
- **Tier** : A - données de référence (registres maîtres)
- **Système de référence** : [CMP-11 : Registre des clients / Index National des Patients](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-11.md)
- **Flux de valeur** : [VS-01 (parcours patient)](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-03 (protection financière)](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md)
- **Objet métier CAESN** : [BO-01 : Patient & identité](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-01.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md), [ART-7](../../04_architecture-repository/04_patterns/artsn-rules/art-7.md)

#### Fusions

Cet objet est le résultat de la fusion des objets suivants, retirés du catalogue :

- `DO-02` (Identifiant national d'identification)

La fusion est tracée dans `04_architecture-repository/00_metamodel/do-migration.yaml` et décidée par l'ADR-0014.

### DO-03 : Dossier et épisode de soins

Ensemble structuré des informations cliniques, administratives et de suivi relatives à un patient au cours de sa vie. Il comprend les antécédents, les épisodes de soins, les prescriptions, les résultats d'examens et les documents cliniques. Un épisode de soins est une période continue de prise en charge d'un patient par un ou plusieurs prestataires de soins, depuis l'admission jusqu'à la sortie ou le transfert ; il peut couvrir une consultation, une hospitalisation, un suivi communautaire ou une téléconsultation. Le dossier groupe les documents produits au cours de ces épisodes.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-01](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-01.md), [CAP-03 (qualité et sécurité des soins)](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-03.md), [CAP-13](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-13.md) et contribue aux flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md). Il est porté par l'objet métier [BO-01 : Patient & identité](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-01.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md), [ART-7](../../04_architecture-repository/04_patterns/artsn-rules/art-7.md).

#### Attributs et contraintes

- **Type** : Entité composite (groupeur d'épisodes et index de documents)
- **Contraintes** : Un seul dossier par patient (consolidation multi-sources) ; date de début d'épisode obligatoire ; date de fin conditionnelle, épisode en cours tant qu'elle est absente ; un épisode est rattaché à au moins un établissement et un patient ; accessibilité au point de service même en connectivité limitée ; protection des données sensibles par rôle et finalité
- **Référentiel source** : FHIR EpisodeOfCare (groupement) et FHIR DocumentReference (documents du dossier)

#### Rattachement

- **Capacités** : [CAP-01](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-01.md), [CAP-03 (qualité et sécurité des soins)](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-03.md), [CAP-13](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-13.md)
- **Tier** : B - données transactionnelles et opérationnelles
- **Système de référence** : [CMP-08 : Répertoire de données cliniques opérationnelles](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-08.md)
- **Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md)
- **Objet métier CAESN** : [BO-01 : Patient & identité](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-01.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md), [ART-7](../../04_architecture-repository/04_patterns/artsn-rules/art-7.md)

#### Fusions

Cet objet est le résultat de la fusion des objets suivants, retirés du catalogue :

- `DO-04` (Épisode de soins)

La fusion est tracée dans `04_architecture-repository/00_metamodel/do-migration.yaml` et décidée par l'ADR-0014.

<!-- END:GENERATED -->

## 2. Prestation & soins

**Objet métier CAESN correspondant** : [BO-02 : Prestation & soins](../../00_caesn/04_data/objets.md).

<!-- BEGIN:GENERATED mode=catalogue source=04_architecture-repository/02_architecture-elements/data/data-objects/do-05.md,04_architecture-repository/02_architecture-elements/data/data-objects/do-06.md,04_architecture-repository/02_architecture-elements/data/data-objects/do-07.md,04_architecture-repository/02_architecture-elements/data/data-objects/do-09.md,04_architecture-repository/02_architecture-elements/data/data-objects/do-32.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### DO-05 : Consultation

Acte clinique réalisé par un prestataire de soins lors d'une rencontre avec un patient. Elle comprend l'anamnèse, l'examen clinique, le diagnostic, la prescription et le suivi.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-01](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-01.md), [CAP-13](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-13.md) et contribue aux flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md). Il est porté par l'objet métier [BO-02 : Prestation & soins](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-02.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-3](../../04_architecture-repository/04_patterns/artsn-rules/art-3.md).

#### Attributs et contraintes

- **Type** : Événement
- **Contraintes** : Date et heure de la consultation ; identification du prestataire ; motivation de la consultation ; diagnostic(s) ; prescription(s)
- **Référentiel source** : FHIR Encounter, CIM-11 (diagnostics)

#### Rattachement

- **Capacités** : [CAP-01](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-01.md), [CAP-13](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-13.md)
- **Tier** : B - données transactionnelles et opérationnelles
- **Système de référence** : [CMP-19 : Dossiers et statistiques de santé (hôpitaux)](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-19.md)
- **Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md)
- **Objet métier CAESN** : [BO-02 : Prestation & soins](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-02.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-3](../../04_architecture-repository/04_patterns/artsn-rules/art-3.md)
- **Codification** : [TERM-CIM-11 : Classification internationale des maladies](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-cim-11.md)

### DO-06 : Prescription

Ordonnance émise par un prestataire de soins, détaillant les médicaments, actes, examens ou soins prescrits pour un patient. Elle constitue le lien clinique entre la consultation et la dispensation.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-01](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-01.md), [CAP-10](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-10.md) et contribue aux flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md). Il est porté par l'objet métier [BO-02 : Prestation & soins](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-02.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-3](../../04_architecture-repository/04_patterns/artsn-rules/art-3.md).

#### Attributs et contraintes

- **Type** : Document structuré
- **Contraintes** : Identification du prescripteur ; date de prescription ; liste des éléments prescrits (médicaments, dosages, posologies) ; durée de validité
- **Référentiel source** : FHIR MedicationRequest

#### Rattachement

- **Capacités** : [CAP-01](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-01.md), [CAP-10](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-10.md)
- **Tier** : B - données transactionnelles et opérationnelles
- **Système de référence** : [CMP-19 : Dossiers et statistiques de santé (hôpitaux)](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-19.md)
- **Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md)
- **Objet métier CAESN** : [BO-02 : Prestation & soins](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-02.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-3](../../04_architecture-repository/04_patterns/artsn-rules/art-3.md)
- **Codification** : [TERM-SNOMED-CT : Terminologie clinique SNOMED CT](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-snomed-ct.md), [TERM-RXNORM : Terminologie des médicaments RxNorm](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-rxnorm.md), [TERM-ATC : Classification pharmacologique ATC de l'OMS](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-atc.md), [TERM-DCI : Dénomination commune internationale](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-dci.md)

### DO-07 : Référence et contre-référence

Orientation d'un patient d'un niveau de soins vers un autre (ex. : centre de santé vers hôpital), accompagnée des informations cliniques pertinentes pour la prise en charge ultérieure. La référence initie un parcours inter-établissement : elle est émise par le prestataire d'origine et acceptée par l'établissement de destination. La contre-référence en est le retour : le patient revient à l'établissement d'origine après une prise en charge spécialisée, avec le compte-rendu clinique, les recommandations de suivi et les traitements à poursuivre. Elle clôt le parcours inter-établissement et rétablit la responsabilité clinique au niveau d'origine.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-02](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-02.md), [CAP-14](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-14.md) et contribue aux flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md). Il est porté par l'objet métier [BO-02 : Prestation & soins](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-02.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-3](../../04_architecture-repository/04_patterns/artsn-rules/art-3.md).

#### Attributs et contraintes

- **Type** : Événement inter-établissement (aller et retour)
- **Contraintes** : Établissement d'origine ; établissement de destination ; motif de la référence ; informations cliniques transmises ; acceptance par l'établissement de destination ; mode de transport (ambulance, avion, bateau) ; urgence (U0-U4) ; compte-rendu clinique structuré lors du retour ; recommandations de suivi ; traitements prescrits à poursuivre ; prochaine échéance de contrôle ; consentement du patient pour le retour
- **Référentiel source** : FHIR ServiceRequest (type: referral) et FHIR DocumentReference (compte-rendu de contre-référence)

#### Rattachement

- **Capacités** : [CAP-02](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-02.md), [CAP-14](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-14.md)
- **Tier** : B - données transactionnelles et opérationnelles
- **Système de référence** : [CMP-19 : Dossiers et statistiques de santé (hôpitaux)](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-19.md)
- **Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md)
- **Objet métier CAESN** : [BO-02 : Prestation & soins](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-02.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-3](../../04_architecture-repository/04_patterns/artsn-rules/art-3.md)

#### Fusions

Cet objet est le résultat de la fusion des objets suivants, retirés du catalogue :

- `DO-08` (Contre-référence)

La fusion est tracée dans `04_architecture-repository/00_metamodel/do-migration.yaml` et décidée par l'ADR-0014.

### DO-09 : Évacuation sanitaire

Transfert urgent d'un patient d'un établissement vers un autre établissement ou vers un pays étranger, nécessitant des moyens de transport sanitaires spécialisés (ambulance, avion médicalisé, hélicoptère). L'évacuation sanitaire peut être nationale (de niveau faible vers un hôpital régional/central) ou internationale (vers un centre spécialisé à l'étranger). Elle implique la continuité des soins pendant le transport et la conformité aux réglementations de sortie/entrée du territoire.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-02](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-02.md), [CAP-14](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-14.md), [CAP-15](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-15.md) et contribue aux flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md). Il est porté par l'objet métier [BO-02 : Prestation & soins](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-02.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-3](../../04_architecture-repository/04_patterns/artsn-rules/art-3.md).

#### Attributs et contraintes

- **Type** : Événement de transport sanitaire
- **Contraintes** : Établissement d'origine ; établissement/pays de destination ; motif médical de l'évacuation ; mode de transport ; équipe médicale accompagnatrice ; équipment médical embarqué ; autorisation de sortie du territoire (si international) ; accord du pays de réception (si international) ; couverture financière ; consentement éclairé du patient
- **Référentiel source** : FHIR ServiceRequest (type: transfer) + FHIR Transport + HL7 FHIR IPS (données cliniques embarquées)

#### Rattachement

- **Capacités** : [CAP-02](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-02.md), [CAP-14](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-14.md), [CAP-15](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-15.md)
- **Tier** : B - données transactionnelles et opérationnelles
- **Système de référence** : [CMP-19 : Dossiers et statistiques de santé (hôpitaux)](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-19.md)
- **Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md)
- **Objet métier CAESN** : [BO-02 : Prestation & soins](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-02.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-3](../../04_architecture-repository/04_patterns/artsn-rules/art-3.md)
#### Sous-types d'évacuation sanitaire

- **EVA-N1** : Nationale primaire — CSB → Hôpital de district/régional — FHIR ServiceRequest
- **EVA-N2** : Nationale secondaire — Hôpital régional → CHU central — FHIR ServiceRequest
- **EVA-I1** : Internationale programmée — Hôpital → Centre spécialisé étranger (planifiée) — FHIR IPS + PT-14 + accords bilatéraux
- **EVA-I2** : Internationale d'urgence — Hôpital → Pays voisin le plus proche (non planifiée) — FHIR IPS + PT-14 + urgence humanitaire

### DO-32 : Examen et résultat de laboratoire

Examen biologique, microbiologique, parasitologique, sérologique ou d'imagerie réalisé sur un échantillon prélevé chez un patient, et résultat d'analyse associé. L'objet couvre la demande d'examen, l'échantillon analysé, le résultat, son unité, sa valeur de référence et son interprétation. Le résultat est la preuve de confirmation d'un diagnostic, la base du suivi de l'efficacité d'un traitement et l'intrant de la surveillance épidémiologique et de la riposte.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-01](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-01.md), [CAP-04](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-04.md), [CAP-18](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-18.md) et contribue aux flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md). Il est porté par les objets métier [BO-02 : Prestation & soins](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-02.md) et [BO-05 : Risque & surveillance](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-05.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md).

#### Attributs et contraintes

- **Type** : Événement (demande d'examen) et résultat (mesure codée)
- **Contraintes** : Patient et episode de soins rattachés ; type d'examen et analyte ; méthode et laboratoire émetteur ; unité du résultat ; valeur de référence et bornes d'interprétation ; statut du résultat (prélèvement en cours, rendu, rendu critique) ; date et heure de prélèvement, date et heure de rendu ; prescripteur à l'origine de la demande
- **Référentiel source** : FHIR DiagnosticReport et FHIR Observation, codification LOINC

#### Rattachement

- **Capacités** : [CAP-01](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-01.md), [CAP-04](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-04.md), [CAP-18](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-18.md)
- **Tier** : B - données transactionnelles et opérationnelles
- **Système de référence** : [CMP-19 : Dossiers et statistiques de santé (hôpitaux)](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-19.md), [CMP-24 : Surveillance de la sante animale (zoonoses)](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-24.md)
- **Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md)
- **Objet métier CAESN** : [BO-02 : Prestation & soins](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-02.md), [BO-05 : Risque & surveillance](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-05.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md)
- **Codification** : [TERM-LOINC : Terminologie des observations de laboratoire](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-loinc.md)

<!-- END:GENERATED -->

## 3. Dispensation & produits

**Objet métier CAESN correspondant** : [BO-03 : Dispensation & produits](../../00_caesn/04_data/objets.md).

<!-- BEGIN:GENERATED mode=catalogue source=04_architecture-repository/02_architecture-elements/data/data-objects/do-10.md,04_architecture-repository/02_architecture-elements/data/data-objects/do-11.md,04_architecture-repository/02_architecture-elements/data/data-objects/do-12.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### DO-10 : Dispensation

Fourniture effective d'un produit de santé (médicament, vaccin, intrant) à un patient, en exécution d'une prescription. Elle constitue l'acte de sortie du stock et doit être tracée pour la gestion des stocks, la facturation et le suivi thérapeutique.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-10](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-10.md), [CAP-13](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-13.md) et contribue aux flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md). Il est porté par l'objet métier [BO-03 : Dispensation & produits](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-03.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md), [ART-9](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md).

#### Attributs et contraintes

- **Type** : Événement
- **Contraintes** : Identification du patient ; identification du produit (lot, DCI) ; quantité dispensée ; date de dispensation ; identification du dispensateur
- **Référentiel source** : FHIR MedicationDispense

#### Rattachement

- **Capacités** : [CAP-10](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-10.md), [CAP-13](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-13.md)
- **Tier** : B - données transactionnelles et opérationnelles
- **Système de référence** : [CMP-20 : Gestion des pharmacies (PMIS)](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-20.md)
- **Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md)
- **Objet métier CAESN** : [BO-03 : Dispensation & produits](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-03.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md), [ART-9](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md)
- **Codification** : [TERM-SNOMED-CT : Terminologie clinique SNOMED CT](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-snomed-ct.md), [TERM-RXNORM : Terminologie des médicaments RxNorm](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-rxnorm.md), [TERM-ATC : Classification pharmacologique ATC de l'OMS](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-atc.md), [TERM-DCI : Dénomination commune internationale](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-dci.md)

### DO-11 : Produit de santé

Tout produit pharmaceutique, vaccin, dispositif médical ou intrant de santé soumis à réglementation. Il est identifié par sa DCI (Dénomination Commune Internationale), son nom commercial, son dosage et son forme pharmaceutique.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-10](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-10.md), [CAP-14](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-14.md) et contribue aux flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md). Il est porté par l'objet métier [BO-03 : Dispensation & produits](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-03.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md), [ART-9](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md).

#### Attributs et contraintes

- **Type** : Entité référentielle
- **Contraintes** : Code DCI obligatoire ; nom commercial ; dosage ; forme pharmaceutique ; statut réglementaire (autorisé, enregistré, retiré)
- **Référentiel source** : Référentiel des produits de santé (CAESN), OMS ATC ; projection FHIR R4 : `Medication` (code DCI ou ATC, statut réglementaire)

#### Rattachement

- **Capacités** : [CAP-10](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-10.md), [CAP-14](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-14.md)
- **Tier** : A - données de référence (registres maîtres)
- **Système de référence** : [CMP-14 : Registre des produits, intrants et indicateurs](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-14.md)
- **Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md)
- **Objet métier CAESN** : [BO-03 : Dispensation & produits](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-03.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md), [ART-9](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md)
- **Codification** : [TERM-SNOMED-CT : Terminologie clinique SNOMED CT](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-snomed-ct.md), [TERM-RXNORM : Terminologie des médicaments RxNorm](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-rxnorm.md), [TERM-ATC : Classification pharmacologique ATC de l'OMS](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-atc.md), [TERM-DCI : Dénomination commune internationale](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-dci.md)

### DO-12 : Lot et stock

Unité de production d'un produit de santé, identifiée par un numéro de lot, une date de fabrication et une date de péremption. Le lot permet la traçabilité complète de la chaîne d'approvisionnement. Le stock associé à un lot est la quantité disponible de ce produit dans un point de stockage (entrepôt, formation sanitaire, case de santé) : il se calcule comme le solde entre les entrées (réceptions, transferts) et les sorties (dispensations, pertes, péremptions).

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-10](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-10.md) et contribue aux flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md). Il est porté par l'objet métier [BO-03 : Dispensation & produits](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-03.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md), [ART-9](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md).

#### Attributs et contraintes

- **Type** : Entité référentielle (lot) assortie de sa mesure de stock
- **Contraintes** : Numéro de lot unique par produit ; date de fabrication ; date de péremption ; fabricant ; pays d'origine ; quantité de stock supérieure ou égale à zéro ; point de stockage identifié ; produit identifié ; date de dernière mise à jour ; seuil d'alerte de stock
- **Référentiel source** : LMIS (Logistics Management Information System) pour les soldes ; projection FHIR R4 : `Medication.batch` (lot : numéro, fabrication, péremption) et `SupplyDelivery` (mouvements de stock)

#### Rattachement

- **Capacités** : [CAP-10](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-10.md)
- **Tier** : B - données transactionnelles et opérationnelles
- **Système de référence** : [CMP-23 : Chaîne logistique (LMIS)](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-23.md)
- **Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md)
- **Objet métier CAESN** : [BO-03 : Dispensation & produits](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-03.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md), [ART-9](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md)
- **Codification** : [TERM-DCI : Dénomination commune internationale](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-dci.md)

#### Fusions

Cet objet est le résultat de la fusion des objets suivants, retirés du catalogue :

- `DO-13` (Stock)

La fusion est tracée dans `04_architecture-repository/00_metamodel/do-migration.yaml` et décidée par l'ADR-0014.

<!-- END:GENERATED -->

## 4. Financement & couverture

**Objet métier CAESN correspondant** : [BO-04 : Financement & couverture](../../00_caesn/04_data/objets.md).

<!-- BEGIN:GENERATED mode=catalogue source=04_architecture-repository/02_architecture-elements/data/data-objects/do-14.md,04_architecture-repository/02_architecture-elements/data/data-objects/do-16.md,04_architecture-repository/02_architecture-elements/data/data-objects/do-17.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### DO-14 : Couverture sanitaire et éligibilité

Ensemble des mécanismes financiers protégeant un patient contre les coûts directs des soins, et statut d'éligibilité qui en découle. La couverture comprend les programmes publics (gratuité soins MIOHA, BPC), les assurances maladie et les mécanismes de tierce payante. L'éligibilité est le statut déterminant si un patient bénéficie effectivement d'une couverture (gratuité, assurance, programme), calculé selon des critères définis par les programmes de protection financière (BPC, AMM, assurances) : éligible, non-éligible ou en attente de vérification.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-07](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-07.md), [CAP-13](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-13.md) et contribue aux flux de valeur [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md). Il est porté par l'objet métier [BO-04 : Financement & couverture](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-04.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md), [ART-9](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md).

#### Attributs et contraintes

- **Type** : Entité de couverture assortie de son statut d'éligibilité
- **Contraintes** : Type de couverture (publique, privée, mixte) ; organisme gestionnaire ; source de l'éligibilité (programme, assureur) ; statut (éligible, non-éligible, en attente de vérification) ; période de validité ; plafonds et exclusions
- **Référentiel source** : FHIR Coverage, normes IHE

#### Rattachement

- **Capacités** : [CAP-07](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-07.md), [CAP-13](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-13.md)
- **Tier** : B - données transactionnelles et opérationnelles
- **Système de référence** : [CMP-12 : Registre d'éligibilité et de couverture](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-12.md)
- **Flux de valeur** : [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md)
- **Objet métier CAESN** : [BO-04 : Financement & couverture](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-04.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md), [ART-9](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md)

#### Fusions

Cet objet est le résultat de la fusion des objets suivants, retirés du catalogue :

- `DO-15` (Couverture sanitaire)

La fusion est tracée dans `04_architecture-repository/00_metamodel/do-migration.yaml` et décidée par l'ADR-0014.

### DO-16 : Facturation et demande de remboursement

Processus de détermination et d'enregistrement des coûts des services et produits de santé fournis à un patient. Elle constitue la base du remboursement, du tiers-payant et du suivi financier.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-07](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-07.md) et contribue aux flux de valeur [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md). Il est porté par l'objet métier [BO-04 : Financement & couverture](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-04.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md), [ART-9](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md).

#### Attributs et contraintes

- **Type** : Événement financier
- **Contraintes** : Montant total détaillé par élément ; statut (payée, en attente, remboursée) ; mode de paiement ; référence au paiement
- **Référentiel source** : projection FHIR R4 : `Claim` (demande de facturation ou de remboursement) et `ClaimResponse` (réponse d'adjudication)

#### Rattachement

- **Capacités** : [CAP-07](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-07.md)
- **Tier** : B - données transactionnelles et opérationnelles
- **Système de référence** : [CMP-12 : Registre d'éligibilité et de couverture](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-12.md)
- **Flux de valeur** : [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)
- **Objet métier CAESN** : [BO-04 : Financement & couverture](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-04.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md), [ART-9](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md)

### DO-17 : Demande et preuve de vérification d'éligibilité

Contrôle en temps réel, au point de service, du statut d'éligibilité d'un patient à un mécanisme de protection financière (CSU, BPC, AMM, assurance). La vérification détermine si les soins peuvent être dispensés sans paiement direct ou avec prise en charge partielle.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-07](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-07.md), [CAP-08](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-08.md) et contribue aux flux de valeur [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md). Il est porté par l'objet métier [BO-04 : Financement & couverture](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-04.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md), [ART-9](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md).

#### Attributs et contraintes

- **Type** : Événement transactionnel
- **Contraintes** : Identifiant du patient (NIN) ; mécanisme de couverture vérifié ; résultat (éligible, non-éligible, erreur) ; horodatage ; point de service émetteur
- **Référentiel source** : FHIR CoverageEligibilityRequest/Response

#### Rattachement

- **Capacités** : [CAP-07](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-07.md), [CAP-08](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-08.md)
- **Tier** : B - données transactionnelles et opérationnelles
- **Système de référence** : [CMP-12 : Registre d'éligibilité et de couverture](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-12.md)
- **Flux de valeur** : [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md)
- **Objet métier CAESN** : [BO-04 : Financement & couverture](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-04.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md), [ART-9](../../04_architecture-repository/04_patterns/artsn-rules/art-9.md)

<!-- END:GENERATED -->

## 5. Risque & surveillance

**Objet métier CAESN correspondant** : [BO-05 : Risque & surveillance](../../00_caesn/04_data/objets.md).

<!-- BEGIN:GENERATED mode=catalogue source=04_architecture-repository/02_architecture-elements/data/data-objects/do-18.md,04_architecture-repository/02_architecture-elements/data/data-objects/do-19.md,04_architecture-repository/02_architecture-elements/data/data-objects/do-20.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### DO-18 : Signal, notification et alerte sanitaires

Cycle de trois événements imbriqués qui structure la surveillance sanitaire. Le signal est l'information brute ou l'indice épidémiologique détecté par un agent communautaire, une formation sanitaire ou un système de surveillance, indiquant un événement sanitaire inhabituel susceptible de nécessiter une investigation. La notification est la transmission formelle et obligatoire d'un événement sanitaire suspecté ou confirmé aux autorités compétentes (district, région, ministère, OMS) ; elle initie le processus officiel de réponse et constitue un engagement juridique du déclarant. L'alerte est l'avertissement déclenché automatiquement ou manuellement lorsqu'un indicateur de surveillance dépasse un seuil prédéfini ; elle est l'action opérationnelle qui découle de la notification et vise à mobiliser rapidement les acteurs compétents pour la riposte.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-04](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-04.md), [CAP-05](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-05.md) et contribue aux flux de valeur [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md). Il est porté par l'objet métier [BO-05 : Risque & surveillance](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-05.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-3](../../04_architecture-repository/04_patterns/artsn-rules/art-3.md).

#### Attributs et contraintes

- **Type** : Événement de surveillance (cycle signal, notification, alerte)
- **Contraintes** : Date et heure de détection ; localisation (GPS ou fokontany) ; type de signal (suspecté, confirmé) ; source du signal ; autorité destinataire de la notification ; délai réglementaire de déclaration ; déclarant identifié ; statut de la notification (envoyée, confirmée, en attente) ; indicateur déclencheur de l'alerte ; seuil franchi ; périmètre géographique concerné ; niveau d'urgence (1-4) ; destinataires de l'alerte ; statut de l'alerte (émise, acquittée, en cours de traitement)
- **Référentiel source** : Système EVIPNet, DHIS2, FHIR Flag et FHIR Communication, Règlement sanitaire international (RSI)

#### Rattachement

- **Capacités** : [CAP-04](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-04.md), [CAP-05](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-05.md)
- **Tier** : B - données transactionnelles et opérationnelles
- **Système de référence** : [CMP-02 : Centre de commande et Crises intersectorielles](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-02.md)
- **Flux de valeur** : [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)
- **Objet métier CAESN** : [BO-05 : Risque & surveillance](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-05.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-3](../../04_architecture-repository/04_patterns/artsn-rules/art-3.md)

#### Fusions

Cet objet est le résultat de la fusion des objets suivants, retirés du catalogue :

- `DO-21` (Notification sanitaire)
- `DO-22` (Alerte sanitaire)

La fusion est tracée dans `04_architecture-repository/00_metamodel/do-migration.yaml` et décidée par l'ADR-0014.

### DO-19 : Foyer épidémique

Zone géographique ou population définie dans laquelle un événement sanitaire (épidémie, outbreak) est identifié ou suspecté. Il délimite le périmètre d'intervention de la riposte.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-04](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-04.md), [CAP-05](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-05.md) et contribue aux flux de valeur [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md). Il est porté par l'objet métier [BO-05 : Risque & surveillance](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-05.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-3](../../04_architecture-repository/04_patterns/artsn-rules/art-3.md).

#### Attributs et contraintes

- **Type** : Entité spatiale
- **Contraintes** : Périmètre géographique ; population exposée ; date d'ouverture ; date de clôture ; statut (actif, clôturé)
- **Référentiel source** : OMS GOARN, OIE

#### Rattachement

- **Capacités** : [CAP-04](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-04.md), [CAP-05](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-05.md)
- **Tier** : B - données transactionnelles et opérationnelles
- **Système de référence** : [CMP-02 : Centre de commande et Crises intersectorielles](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-02.md)
- **Flux de valeur** : [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)
- **Objet métier CAESN** : [BO-05 : Risque & surveillance](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-05.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-3](../../04_architecture-repository/04_patterns/artsn-rules/art-3.md)

### DO-20 : Investigation épidémiologique

Enquête épidémiologique et/ou de laboratoire menée pour confirmer ou infirmer un signal, identifier la source, le mode de transmission et les facteurs de risque d'un événement sanitaire.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-04](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-04.md), [CAP-05](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-05.md), [CAP-18](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-18.md) et contribue aux flux de valeur [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md). Il est porté par l'objet métier [BO-05 : Risque & surveillance](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-05.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-3](../../04_architecture-repository/04_patterns/artsn-rules/art-3.md).

#### Attributs et contraintes

- **Type** : Événement
- **Contraintes** : Date de début et de fin ; enquêteurs ; échantillons prélevés ; résultats de laboratoire ; conclusion (confirmé, infirmé, en cours)
- **Référentiel source** : DHIS2, OMS protocoles

#### Rattachement

- **Capacités** : [CAP-04](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-04.md), [CAP-05](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-05.md), [CAP-18](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-18.md)
- **Tier** : B - données transactionnelles et opérationnelles
- **Système de référence** : [CMP-02 : Centre de commande et Crises intersectorielles](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-02.md)
- **Flux de valeur** : [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)
- **Objet métier CAESN** : [BO-05 : Risque & surveillance](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-05.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-3](../../04_architecture-repository/04_patterns/artsn-rules/art-3.md)
- **Codification** : [TERM-LOINC : Terminologie des observations de laboratoire](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-loinc.md)

<!-- END:GENERATED -->

## 6. Exploitation & gestion

**Objet métier CAESN correspondant** : [BO-06 : Exploitation & gestion](../../00_caesn/04_data/objets.md).

<!-- BEGIN:GENERATED mode=catalogue source=04_architecture-repository/02_architecture-elements/data/data-objects/do-23.md,04_architecture-repository/02_architecture-elements/data/data-objects/do-24.md,04_architecture-repository/02_architecture-elements/data/data-objects/do-25.md,04_architecture-repository/02_architecture-elements/data/data-objects/do-26.md,04_architecture-repository/02_architecture-elements/data/data-objects/do-27.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### DO-23 : Formation sanitaire

Toute structure de soins publique, privée, confessionnelle ou communautaire identifiée de manière unique dans le référentiel national des formations sanitaires. C'est l'unité de base du réseau de soins.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-11](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-11.md), [CAP-14](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-14.md) et contribue aux flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md). Il est porté par l'objet métier [BO-06 : Exploitation & gestion](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-06.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md).

#### Attributs et contraintes

- **Type** : Entité référentielle
- **Contraintes** : Code unique (selon INSTAT) ; dénomination officielle ; type (hôpital, centre de santé, case de santé) ; niveau de qualification ; statut (actif, fermé, en construction)
- **Référentiel source** : Référentiel des formations sanitaires (CAESN)

#### Rattachement

- **Capacités** : [CAP-11](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-11.md), [CAP-14](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-14.md)
- **Tier** : A - données de référence (registres maîtres)
- **Système de référence** : [ABB-REFERENTIEL-STRUCTURES-SERVICES : Référentiel des structures et services de santé](../../04_architecture-repository/05_building-blocks/abb/abb-referentiel-structures-services.md), [CMP-05 : Moteur de graphes et Référentiel spatio-temporel](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-05.md)
- **Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)
- **Objet métier CAESN** : [BO-06 : Exploitation & gestion](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-06.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md)

### DO-24 : Agent de santé

Toute personne physique exerçant une activité de soins, de prévention ou de promotion de la santé dans une formation sanitaire, identifiée par son rôle, ses qualifications et son affectation.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-09](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-09.md), [CAP-13](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-13.md) et contribue aux flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md). Il est porté par l'objet métier [BO-06 : Exploitation & gestion](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-06.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md).

#### Attributs et contraintes

- **Type** : Entité
- **Contraintes** : Identifiant unique ; nom ; qualification (médecin, infirmier, ACS, etc.) ; affectation (formation sanitaire, zone) ; statut (actif, inactif)
- **Référentiel source** : Référentiel des agents de santé (CAESN)

#### Rattachement

- **Capacités** : [CAP-09](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-09.md), [CAP-13](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-13.md)
- **Tier** : A - données de référence (registres maîtres)
- **Système de référence** : [CMP-13 : Registre des personnels](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-13.md)
- **Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)
- **Objet métier CAESN** : [BO-06 : Exploitation & gestion](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-06.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md)

### DO-25 : Indicateur sanitaire

Mesure standardisée d'une performance, d'un résultat ou d'un processus dans le domaine de la santé. Chaque indicateur doit avoir une définition unique, stable et partagée, avec une méthodologie de calcul précise.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-03](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-03.md), [CAP-08](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-08.md) et contribue aux flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md). Il est porté par l'objet métier [BO-06 : Exploitation & gestion](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-06.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md).

#### Attributs et contraintes

- **Type** : Entité référentielle
- **Contraintes** : Code unique ; nom ; définition ; méthodologie de calcul ; unité de mesure ; fréquence de collecte ; source de données
- **Référentiel source** : Référentiel des indicateurs sanitaires (CAESN), DHIS2

#### Rattachement

- **Capacités** : [CAP-03](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-03.md), [CAP-08](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-08.md)
- **Tier** : C - données analytiques et agrégées
- **Système de référence** : [CMP-14 : Registre des produits, intrants et indicateurs](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-14.md)
- **Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)
- **Objet métier CAESN** : [BO-06 : Exploitation & gestion](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-06.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md)

### DO-26 : Zone sanitaire

Unité territoriale de planification et de coordination des services de santé, correspondant généralement à un district sanitaire. Elle regroupe les formations sanitaires et les zones de couverture d'une même aire de responsabilité.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-05](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-05.md), [CAP-14](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-14.md) et contribue aux flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md). Il est porté par l'objet métier [BO-06 : Exploitation & gestion](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-06.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md).

#### Attributs et contraintes

- **Type** : Entité spatiale
- **Contraintes** : Code unique ; dénomination ; limites géographiques ; population ; chef-lieu ; formations sanitaires rattachées
- **Référentiel source** : Référentiel géographique sanitaire (CAESN), INSTAT

#### Rattachement

- **Capacités** : [CAP-05](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-05.md), [CAP-14](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-14.md)
- **Tier** : A - données de référence (registres maîtres)
- **Système de référence** : [ABB-REFERENTIEL-STRUCTURES-SERVICES : Référentiel des structures et services de santé](../../04_architecture-repository/05_building-blocks/abb/abb-referentiel-structures-services.md), [CMP-05 : Moteur de graphes et Référentiel spatio-temporel](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-05.md)
- **Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md), [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md), [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)
- **Objet métier CAESN** : [BO-06 : Exploitation & gestion](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-06.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md)

### DO-27 : Tâche et action de suivi

Unité de travail assignée à un acteur (personne ou système) dans le cadre d'un processus opérationnel : investigation terrain, campagne de vaccination, distribution d'intrants, visite de suivi. La tâche porte un statut, des échéances et une traçabilité complète d'exécution.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-06](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-06.md), [CAP-08](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-08.md) et contribue aux flux de valeur [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md). Il est porté par l'objet métier [BO-06 : Exploitation & gestion](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-06.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md).

#### Attributs et contraintes

- **Type** : Entité opérationnelle
- **Contraintes** : Description de l'action ; assigné à (agent ou organisation) ; date d'échéance ; statut (à faire, en cours, terminée, annulée) ; résultat ; priorité
- **Référentiel source** : FHIR Task

#### Rattachement

- **Capacités** : [CAP-06](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-06.md), [CAP-08](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-08.md)
- **Tier** : B - données transactionnelles et opérationnelles
- **Système de référence** : [CMP-01 : Tableaux de bord et Portails nationaux](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-01.md)
- **Flux de valeur** : [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md), [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md)
- **Objet métier CAESN** : [BO-06 : Exploitation & gestion](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-06.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md)

<!-- END:GENERATED -->

## 7. Interopérabilité transfrontalière & résumé patient

**Objet métier CAESN correspondant** : [BO-07 : Interopérabilité transfrontalière](../../00_caesn/04_data/objets.md).

<!-- BEGIN:GENERATED mode=catalogue source=04_architecture-repository/02_architecture-elements/data/data-objects/do-29.md,04_architecture-repository/02_architecture-elements/data/data-objects/do-31.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### DO-29 : Résumé international du patient

Document clinique structuré, minimal et non exhaustif, destiné à faciliter la continuité des soins lors d'un episode de soins transfrontalier. Conforme au standard HL7 IPS, il comprend les informations cliniques essentielles du patient : démographie, allergies, médicaments en cours, problèmes de santé, antécédents, vaccinations, résultats de diagnostic, dispositifs médicaux et procédures. Il est échangeable entre systèmes de santé de pays différents grâce aux profils FHIR IPS.

Il est composé de sections, unités structurées regroupant une catégorie clinique spécifique. Chaque section est un objet FHIR Composition autonome, identifiable par un code conforme au ValueSet IPS, pouvant être échangé individuellement selon le principe de minimisation des données.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-15](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-15.md), [CAP-17 (engagement patient)](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-17.md) et contribue aux flux de valeur [VS-01 (parcours patient)](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md). Il est porté par l'objet métier [BO-07 : Interopérabilité transfrontalière](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-07.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-7](../../04_architecture-repository/04_patterns/artsn-rules/art-7.md).

#### Attributs et contraintes

- **Type** : Document structuré (Bundle FHIR de type document, profil IPS), composé de sections (Composition)
- **Contraintes** : Conforme au profil HL7 FHIR IPS (hl7.org/fhir/uv/ips) ; langue obligatoire (français + anglais) ; date d'émission et validité ; signature électronique du prestataire ; code de section conforme au ValueSet IPS ; contenu structuré selon les profils FHIR IPS ; section vide autorisée (« no known… »)
- **Référentiel source** : HL7 FHIR R4 : International Patient Summary (IPS) et IPS Sections

#### Sections IPS obligatoires

- **ALGY** : Allergies et intolérances - AllergyIntolerance - Substance, réaction, sévérité, statut
- **MDCA** : Médicaments actuels - MedicationStatement - Produit, dosage, statut, indication
- **PROB** : Problèmes de santé - Condition - Code CIM-11, onset, statut
- **HIST** : Antécédents - Condition - Épisodes passés, résolus
- **IMMU** : Vaccinations - Immunization - Vaccin, date, lot, statut
- **VITAL** : Signes vitaux - Observation - Mesures (TA, FC, SpO2, température)
- **LAB** : Résultats de diagnostic - Observation - Résultats laboratoire
- **DEVI** : Dispositifs médicaux - DeviceUseStatement - Dispositif, date, statut
- **PROC** : Procédures - Procedure - Acte, date, résultat
- **IDOI** : Identité du patient - Patient - NIN, nom, naissance, sexe

#### Rattachement

- **Capacités** : [CAP-15](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-15.md), [CAP-17 (engagement patient)](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-17.md)
- **Tier** : B - données transactionnelles et opérationnelles
- **Système de référence** : [CMP-06 : Intégration, Médiation, API Gateway, Broker et Registre schémas](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-06.md)
- **Capacités intégrées (CNISN)** : [PART-ECHANGE-TRANSFRONTALIER (interopérabilité transfrontalière)](../../04_architecture-repository/01_partitions/externes/part-echange-transfrontalier.md)
- **Flux de valeur** : [VS-01 (parcours patient)](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md)
- **Profils (PTISN)** : [PT-14 (interopérabilité transfrontalière)](../../04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-14.md)
- **Objet métier CAESN** : [BO-07 : Interopérabilité transfrontalière](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-07.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-7](../../04_architecture-repository/04_patterns/artsn-rules/art-7.md)

#### Fusions

Cet objet est le résultat de la fusion des objets suivants, retirés du catalogue :

- `DO-30` (Section du résumé patient)

La fusion est tracée dans `04_architecture-repository/00_metamodel/do-migration.yaml` et décidée par l'ADR-0014.

### DO-31 : Ancre de confiance

Point d'ancrage de confiance numérique permettant la vérification mutuelle de l'identité et de la conformité des systèmes de santé échangeant des données transfrontalières. Conforme au GDHCN (Global Digital Health Certification Network), il garantit l'authenticité, l'intégrité et la non-répudiation des résumés patients échangés.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-15](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-15.md). Il est porté par l'objet métier [BO-07 : Interopérabilité transfrontalière](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-07.md) et traité dans les chapitres ARTSN [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-7](../../04_architecture-repository/04_patterns/artsn-rules/art-7.md).

#### Attributs et contraintes

- **Type** : Entité infrastructure
- **Contraintes** : Certificat X.509v3 signé par l'autorité GDHCN nationale ; révocation en temps réel (CRL/OCSP) ; renouvellement avant expiration ; journalisation de toutes les vérifications
- **Référentiel source** : GDHCN, ITU-T X.509 ; projection FHIR R4 : `Endpoint` (point de service de l'ancre et des listes CRL/OCSP), `Provenance` (attestation signée par l'autorité) et `Binary` (charge utile X.509)

#### Rattachement

- **Capacités** : [CAP-15](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-15.md)
- **Tier** : A - données de référence (registres maîtres)
- **Système de référence** : [CMP-35 : Infrastructure de clés publiques (PKI)](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-35.md), [CMP-36 : Passerelle de confiance mondiale OMS (GDHCN)](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-36.md)
- **Capacités intégrées (CNISN)** : [PART-ECHANGE-TRANSFRONTALIER](../../04_architecture-repository/01_partitions/externes/part-echange-transfrontalier.md)
- **Profils (PTISN)** : [PT-14](../../04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-14.md)
- **Objet métier CAESN** : [BO-07 : Interopérabilité transfrontalière](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-07.md)
- **Chapitres ARTSN** : [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md), [ART-7](../../04_architecture-repository/04_patterns/artsn-rules/art-7.md)

<!-- END:GENERATED -->

## 8. Terminologies et codification

La couche sémantique du référentiel arrime les valeurs portées par les objets de données à des référentiels de codes publics et versionnés. Cette couche est la condition de comparabilité des données entre institutions : deux établissements qui échange le même objet de données n'échangent la même information que s'ils interprètent ses valeurs selon les mêmes codes. Elle conditionne également la validité des indicateurs calculés au-dessus de ces données, un indicateur n'ayant de sens que si sa population de départ est codée de façon homogène.

Chaque terminologie du référentiel est un objet à part entière, porteur d'une finalité, d'un contenu et d'une portée. Une terminologie constrain un ou plusieurs objets de données, et chaque objet de données declare les terminologies qui régissent ses valeurs. Les deux relations sont réciproques et contrôlées par le validateur du référentiel : une terminologie sans objet de données contraint, ou un objet de données dont la codification n'est portée par aucun composant applicatif, sont considérés comme des anomalies.

<!-- BEGIN:GENERATED mode=table source=04_architecture-repository/02_architecture-elements/data/terminologies/term-atc.md,04_architecture-repository/02_architecture-elements/data/terminologies/term-cim-11.md,04_architecture-repository/02_architecture-elements/data/terminologies/term-dci.md,04_architecture-repository/02_architecture-elements/data/terminologies/term-loinc.md,04_architecture-repository/02_architecture-elements/data/terminologies/term-rxnorm.md,04_architecture-repository/02_architecture-elements/data/terminologies/term-snomed-ct.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

| Code | Titre canonique | Rattachement | Statut | Fiche |
|---|---|---|---|---|
| TERM-ATC | TERM-ATC : Classification pharmacologique ATC de l'OMS | CAP-13, CAP-14, ART-2, ART-4, TERM-DCI, TERM-CODIFICATION-COMMUNE, CMP-10, DO-06, DO-10, DO-11 | candidate | TERM-ATC |
| TERM-CIM-11 | TERM-CIM-11 : Classification internationale des maladies | CAP-13, CAP-14, ART-2, ART-4, TERM-CODIFICATION-COMMUNE, CMP-09, CMP-10, STD-0006, DO-05 | candidate | TERM-CIM-11 |
| TERM-DCI | TERM-DCI : Dénomination commune internationale | CAP-13, CAP-14, ART-2, ART-4, TERM-SNOMED-CT, TERM-RXNORM, TERM-CODIFICATION-COMMUNE, CMP-10, DO-06, DO-10, DO-11, DO-12 | candidate | TERM-DCI |
| TERM-LOINC | TERM-LOINC : Terminologie des observations de laboratoire | CAP-13, CAP-14, ART-2, ART-4, TERM-CIM-11, TERM-CODIFICATION-COMMUNE, CMP-09, CMP-10, STD-0006, DO-20, DO-32 | candidate | TERM-LOINC |
| TERM-RXNORM | TERM-RXNORM : Terminologie des médicaments RxNorm | CAP-13, CAP-14, ART-2, ART-4, TERM-SNOMED-CT, TERM-CODIFICATION-COMMUNE, CMP-10, STD-0007, DO-06, DO-10, DO-11 | candidate | TERM-RXNORM |
| TERM-SNOMED-CT | TERM-SNOMED-CT : Terminologie clinique SNOMED CT | CAP-13, CAP-14, ART-2, ART-4, TERM-CODIFICATION-COMMUNE, TERM-RXNORM, CMP-09, CMP-10, STD-0007, DO-06, DO-10, DO-11 | candidate | TERM-SNOMED-CT |

<!-- END:GENERATED -->

Le registre chapeau de ces terminologies est publié au niveau CNISN sous l'identifiant [TERM-CODIFICATION-COMMUNE : Terminologie et codification communes](../../04_architecture-repository/02_architecture-elements/data/terminologies/term-codification-commune.md). Il fixe les services de consultation de systèmes de codes, de validation, d'expansion, de recherche et de traduction. Les terminologies ci-dessus en sont les déclinaisons métier : elles définissent, pour un usage donné, quel référentiel de codes s'applique.

## Liens

- Chapitres et patterns de référence
- ART-2 : Médiation et normalisation
- ART-7 : Sécurité, contrôle d'accès et résidence
- PT-14 : Interopérabilité transfrontalière
- PART-ECHANGE-TRANSFRONTALIER : Interopérabilité transfrontalière
- CAESN : données
- CAESN : domaines de données
- CAESN : référentiels nationaux

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **chapitre ART-2 (médiation et normalisation)** : Médiation et normalisation (`04_architecture-repository/04_patterns/artsn-rules/art-2.md`)
- **F.2** : F.2 : Préservation de la souveraineté intersectorielle (`04_architecture-repository/04_patterns/foundations/f-2.md`)
- **F.3** : F.3 : Éradication des silos technologiques (`04_architecture-repository/04_patterns/foundations/f-3.md`)
- **CAESN** : Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) (`00_caesn/00_overview/index.md`)
- **Chapitres et patterns de référence** : Chapitres et patterns de référence (`02_artsn/04_patterns/index.md`)
- **ART-2 : Médiation et normalisation** : Médiation et normalisation (`04_architecture-repository/04_patterns/artsn-rules/art-2.md`)
- **ART-7 : Sécurité, contrôle d'accès et résidence** : Sécurité, contrôle d'accès et résidence de la donnée (`04_architecture-repository/04_patterns/artsn-rules/art-7.md`)
- **PT-14 : Interopérabilité transfrontalière** : Interopérabilité transfrontalière (`03_ptisn/03_profils/pt-14-interopabilite-transfrontaliere.md`)
- **PART-ECHANGE-TRANSFRONTALIER : Interopérabilité transfrontalière** : Partie II : Objets d'interopérabilité requis (`01_cnisn/02_objets-interoperabilite/index.md`)
- **CAESN : données** : Architecture des données et de l'information sanitaire (`00_caesn/04_data/index.md`)
- **CAESN : domaines de données** : Domaines de données prioritaires (`00_caesn/04_data/domains.md`)
- **CAESN : référentiels nationaux** : Référentiels nationaux (`00_caesn/04_data/referentials.md`)
