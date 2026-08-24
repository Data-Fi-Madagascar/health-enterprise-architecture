---

title: Dictionnaire de données fonctionnelles
id: artsn-dictionnaire-donnees
domain: 03_objets-de-donnees
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: ["artsn", "dictionnaire", "donnees", "semantique", "niveau-3"]
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

---

## 1. Patient & identité

**Objet métier CAESN correspondant** : [BO-01 : Patient & identité](../../00_caesn/04_data/objets.md).

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/objets-de-donnees/do-01.md,referentiel/objets-de-donnees/do-02.md,referentiel/objets-de-donnees/do-03.md,referentiel/objets-de-donnees/do-04.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

accessed_by: ["SRV-02"]

### DO-01 : Patient

Personne physique bénéficiaire de soins de santé, identifiée de manière unique au sein du système d'information sanitaire national. L'identité du patient est un actif stratégique national qui ne peut être dupliquée, fragmentée ou remplacée par des identifiants propriétaires de programmes ou de projets.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-01 (continuité des soins)](../../referentiel/capabilites/cap-01.md), [CAP-13 (interopérabilité données)](../../referentiel/capabilites/cap-13.md) et contribue aux flux de valeur [VS-01 (parcours patient)](../../referentiel/flux-valeur/vs-01.md), [VS-03 (protection financière)](../../referentiel/flux-valeur/vs-03.md). Il est porté par l'objet métier [BO-01 : Patient & identité](../../referentiel/objets-metier/bo-01.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-7](../../referentiel/chapitres/art-7.md).

#### Attributs et contraintes

- **Type** : Entité (identifiant unique + attributs)
- **Contraintes** : Identifiant unique national (NIN ou identifiant provisoire) ; un seul enregistrement par personne physique ; traçabilité des doublons détectés et résolus
- **Référentiel source** : Référentiel des bénéficiaires / patients (CAESN)

#### Rattachement

- **Capacités** : [CAP-01 (continuité des soins)](../../referentiel/capabilites/cap-01.md), [CAP-13 (interopérabilité données)](../../referentiel/capabilites/cap-13.md)
- **Flux de valeur** : [VS-01 (parcours patient)](../../referentiel/flux-valeur/vs-01.md), [VS-03 (protection financière)](../../referentiel/flux-valeur/vs-03.md)
- **Objet métier CAESN** : [BO-01 : Patient & identité](../../referentiel/objets-metier/bo-01.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-7](../../referentiel/chapitres/art-7.md)

accessed_by: ["SRV-03"]

### DO-02 : Identifiant national d'identification (NIN)

Code alphanumérique unique attribué à chaque patient dans le référentiel national des bénéficiaires. Il garantit l'unicité de l'identité patient à travers tous les systèmes et toutes les initiatives.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-14](../../referentiel/capabilites/cap-14.md). Il est porté par l'objet métier [BO-01 : Patient & identité](../../referentiel/objets-metier/bo-01.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-7](../../referentiel/chapitres/art-7.md).

#### Attributs et contraintes

- **Type** : Identifiant
- **Contraintes** : Format : 12 chiffres (selon le modèle INSTAT) ; attribué une seule fois ; non modifiable après validation ; traçabilité des attributions
- **Référentiel source** : Référentiel des bénéficiaires / patients

#### Rattachement

- **Capacités** : [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-14](../../referentiel/capabilites/cap-14.md)
- **Profils (PTISN)** : [PT-04 (identité nationale)](../../referentiel/profils/pt-04.md)
- **Objet métier CAESN** : [BO-01 : Patient & identité](../../referentiel/objets-metier/bo-01.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-7](../../referentiel/chapitres/art-7.md)

accessed_by: ["SRV-04", "SRV-05"]

### DO-03 : Dossier patient

Ensemble structuré des informations cliniques, administratives et de suivi relatives à un patient au cours de sa vie. Il comprend les antécédents, les épisodes de soins, les prescriptions, les résultats d'examens et les documents cliniques.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-13](../../referentiel/capabilites/cap-13.md) et contribue aux flux de valeur [VS-01](../../referentiel/flux-valeur/vs-01.md). Il est porté par l'objet métier [BO-01 : Patient & identité](../../referentiel/objets-metier/bo-01.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-7](../../referentiel/chapitres/art-7.md).

#### Attributs et contraintes

- **Type** : Entité composite
- **Contraintes** : Un seul dossier par patient (consolidation multi-sources) ; accessibilité au point de service même en connectivité limitée ; protection des données sensibles par rôle et finalité
- **Référentiel source** : FHIR Patient, IHE PCD

#### Rattachement

- **Capacités** : [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-13](../../referentiel/capabilites/cap-13.md)
- **Flux de valeur** : [VS-01](../../referentiel/flux-valeur/vs-01.md)
- **Objet métier CAESN** : [BO-01 : Patient & identité](../../referentiel/objets-metier/bo-01.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-7](../../referentiel/chapitres/art-7.md)

accessed_by: ["SRV-06"]

### DO-04 : Épisode de soins

Période continue de prise en charge d'un patient par un ou plusieurs prestataires de soins, depuis l'admission jusqu'à la sortie ou le transfert. Un épisode peut couvrir une consultation, une hospitalisation, un suivi communautaire ou une téléconsultation.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-05](../../referentiel/capabilites/cap-05.md) et contribue aux flux de valeur [VS-01](../../referentiel/flux-valeur/vs-01.md). Il est porté par l'objet métier [BO-01 : Patient & identité](../../referentiel/objets-metier/bo-01.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-7](../../referentiel/chapitres/art-7.md).

#### Attributs et contraintes

- **Type** : Entité temporelle
- **Contraintes** : Date de début obligatoire ; date de fin conditionnelle (en cours) ; un épisode est rattaché à au moins un établissement et un patient
- **Référentiel source** : FHIR Encounter

#### Rattachement

- **Capacités** : [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-05](../../referentiel/capabilites/cap-05.md)
- **Flux de valeur** : [VS-01](../../referentiel/flux-valeur/vs-01.md)
- **Objet métier CAESN** : [BO-01 : Patient & identité](../../referentiel/objets-metier/bo-01.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-7](../../referentiel/chapitres/art-7.md)
---

<!-- END:GENERATED -->

## 2. Prestation & soins

**Objet métier CAESN correspondant** : [BO-02 : Prestation & soins](../../00_caesn/04_data/objets.md).

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/objets-de-donnees/do-05.md,referentiel/objets-de-donnees/do-06.md,referentiel/objets-de-donnees/do-07.md,referentiel/objets-de-donnees/do-08.md,referentiel/objets-de-donnees/do-09.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### DO-05 : Consultation

Acte clinique réalisé par un prestataire de soins lors d'une rencontre avec un patient. Elle comprend l'anamnèse, l'examen clinique, le diagnostic, la prescription et le suivi.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-13](../../referentiel/capabilites/cap-13.md) et contribue aux flux de valeur [VS-01](../../referentiel/flux-valeur/vs-01.md). Il est porté par l'objet métier [BO-02 : Prestation & soins](../../referentiel/objets-metier/bo-02.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md).

#### Attributs et contraintes

- **Type** : Événement
- **Contraintes** : Date et heure de la consultation ; identification du prestataire ; motivation de la consultation ; diagnostic(s) ; prescription(s)
- **Référentiel source** : FHIR Encounter, CIM-10 (diagnostics)

#### Rattachement

- **Capacités** : [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-13](../../referentiel/capabilites/cap-13.md)
- **Flux de valeur** : [VS-01](../../referentiel/flux-valeur/vs-01.md)
- **Objet métier CAESN** : [BO-02 : Prestation & soins](../../referentiel/objets-metier/bo-02.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md)

### DO-06 : Prescription

Ordonnance émise par un prestataire de soins, détaillant les médicaments, actes, examens ou soins prescrits pour un patient. Elle constitue le lien clinique entre la consultation et la dispensation.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-10](../../referentiel/capabilites/cap-10.md) et contribue aux flux de valeur [VS-01](../../referentiel/flux-valeur/vs-01.md). Il est porté par l'objet métier [BO-02 : Prestation & soins](../../referentiel/objets-metier/bo-02.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md).

#### Attributs et contraintes

- **Type** : Document structuré
- **Contraintes** : Identification du prescripteur ; date de prescription ; liste des éléments prescrits (médicaments, dosages, posologies) ; durée de validité
- **Référentiel source** : FHIR MedicationRequest

#### Rattachement

- **Capacités** : [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-10](../../referentiel/capabilites/cap-10.md)
- **Flux de valeur** : [VS-01](../../referentiel/flux-valeur/vs-01.md)
- **Objet métier CAESN** : [BO-02 : Prestation & soins](../../referentiel/objets-metier/bo-02.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md)

### DO-07 : Référence

Orientation d'un patient d'un niveau de soins vers un autre (ex. : centre de santé vers hôpital), accompagnée des informations cliniques pertinentes pour la prise en charge ultérieure. La référence initie un parcours inter-établissement : elle est émise par le prestataire d'origine et acceptée par l'établissement de destination.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-02](../../referentiel/capabilites/cap-02.md), [CAP-05](../../referentiel/capabilites/cap-05.md), [CAP-14](../../referentiel/capabilites/cap-14.md) et contribue aux flux de valeur [VS-01](../../referentiel/flux-valeur/vs-01.md). Il est porté par l'objet métier [BO-02 : Prestation & soins](../../referentiel/objets-metier/bo-02.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md).

#### Attributs et contraintes

- **Type** : Événement inter-établissement
- **Contraintes** : Établissement d'origine ; établissement de destination ; motif de la référence ; informations cliniques transmises ; acceptance par l'établissement de destination ; mode de transport (ambulance, avion, bateau) ; urgence (U0-U4)
- **Référentiel source** : FHIR ServiceRequest (type: referral)

#### Rattachement

- **Capacités** : [CAP-02](../../referentiel/capabilites/cap-02.md), [CAP-05](../../referentiel/capabilites/cap-05.md), [CAP-14](../../referentiel/capabilites/cap-14.md)
- **Flux de valeur** : [VS-01](../../referentiel/flux-valeur/vs-01.md)
- **Objet métier CAESN** : [BO-02 : Prestation & soins](../../referentiel/objets-metier/bo-02.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md)

### DO-08 : Contre-référence

Retour d'un patient vers l'établissement d'origine après prise en charge spécialisée, accompagné du compte-rendu clinique, des recommandations de suivi et de la prise en charge thérapeutique à poursuivre. La contre-référence clôture le parcours inter-établissement et rétablit la responsabilité clinique au niveau d'origine.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-02](../../referentiel/capabilites/cap-02.md), [CAP-05](../../referentiel/capabilites/cap-05.md), [CAP-14](../../referentiel/capabilites/cap-14.md) et contribue aux flux de valeur [VS-01](../../referentiel/flux-valeur/vs-01.md). Il est porté par l'objet métier [BO-02 : Prestation & soins](../../referentiel/objets-metier/bo-02.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md).

#### Attributs et contraintes

- **Type** : Événement inter-établissement (retour)
- **Contraintes** : Établissement d'origine (destination du retour) ; établissement émetteur (spécialisé) ; compte-rendu clinique structuré ; recommandations de suivi ; traitements prescrits ; prochaine échéance de contrôle ; consentement du patient pour le retour
- **Référentiel source** : FHIR ServiceRequest (type: referral) + FHIR DocumentReference (compte-rendu)

#### Rattachement

- **Capacités** : [CAP-02](../../referentiel/capabilites/cap-02.md), [CAP-05](../../referentiel/capabilites/cap-05.md), [CAP-14](../../referentiel/capabilites/cap-14.md)
- **Flux de valeur** : [VS-01](../../referentiel/flux-valeur/vs-01.md)
- **Objet métier CAESN** : [BO-02 : Prestation & soins](../../referentiel/objets-metier/bo-02.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md)

### DO-09 : Évacuation sanitaire (medevac)

Transfert urgent d'un patient d'un établissement vers un autre établissement ou vers un pays étranger, nécessitant des moyens de transport sanitaires spécialisés (ambulance, avion médicalisé, hélicoptère). L'évacuation sanitaire peut être nationale (de niveau faible vers un hôpital régional/central) ou internationale (vers un centre spécialisé à l'étranger). Elle implique la continuité des soins pendant le transport et la conformité aux réglementations de sortie/entrée du territoire.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-02](../../referentiel/capabilites/cap-02.md), [CAP-05](../../referentiel/capabilites/cap-05.md), [CAP-10](../../referentiel/capabilites/cap-10.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-17](../../referentiel/capabilites/cap-17.md) et contribue aux flux de valeur [VS-01](../../referentiel/flux-valeur/vs-01.md), [VS-02](../../referentiel/flux-valeur/vs-02.md). Il est porté par l'objet métier [BO-02 : Prestation & soins](../../referentiel/objets-metier/bo-02.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md).

#### Attributs et contraintes

- **Type** : Événement de transport sanitaire
- **Contraintes** : Établissement d'origine ; établissement/pays de destination ; motif médical de l'évacuation ; mode de transport ; équipe médicale accompagnatrice ; équipment médical embarqué ; autorisation de sortie du territoire (si international) ; accord du pays de réception (si international) ; couverture financière ; consentement éclairé du patient
- **Référentiel source** : FHIR ServiceRequest (type: transfer) + FHIR Transport + HL7 FHIR IPS (données cliniques embarquées)

#### Rattachement

- **Capacités** : [CAP-02](../../referentiel/capabilites/cap-02.md), [CAP-05](../../referentiel/capabilites/cap-05.md), [CAP-10](../../referentiel/capabilites/cap-10.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-17](../../referentiel/capabilites/cap-17.md)
- **Flux de valeur** : [VS-01](../../referentiel/flux-valeur/vs-01.md), [VS-02](../../referentiel/flux-valeur/vs-02.md)
- **Objet métier CAESN** : [BO-02 : Prestation & soins](../../referentiel/objets-metier/bo-02.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md)
#### Sous-types d'évacuation sanitaire

- **EVA-N1** : Nationale primaire — CSB → Hôpital de district/régional — FHIR ServiceRequest
- **EVA-N2** : Nationale secondaire — Hôpital régional → CHU central — FHIR ServiceRequest
- **EVA-I1** : Internationale programmée — Hôpital → Centre spécialisé étranger (planifiée) — FHIR IPS + PT-14 + accords bilatéraux
- **EVA-I2** : Internationale d'urgence — Hôpital → Pays voisin le plus proche (non planifiée) — FHIR IPS + PT-14 + urgence humanitaire

---

<!-- END:GENERATED -->

## 3. Dispensation & produits

**Objet métier CAESN correspondant** : [BO-03 : Dispensation & produits](../../00_caesn/04_data/objets.md).

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/objets-de-donnees/do-10.md,referentiel/objets-de-donnees/do-11.md,referentiel/objets-de-donnees/do-12.md,referentiel/objets-de-donnees/do-13.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### DO-10 : Dispensation

Fourniture effective d'un produit de santé (médicament, vaccin, intrant) à un patient, en exécution d'une prescription. Elle constitue l'acte de sortie du stock et doit être tracée pour la gestion des stocks, la facturation et le suivi thérapeutique.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-10](../../referentiel/capabilites/cap-10.md), [CAP-13](../../referentiel/capabilites/cap-13.md) et contribue aux flux de valeur [VS-01](../../referentiel/flux-valeur/vs-01.md). Il est porté par l'objet métier [BO-03 : Dispensation & produits](../../referentiel/objets-metier/bo-03.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-9](../../referentiel/chapitres/art-9.md).

#### Attributs et contraintes

- **Type** : Événement
- **Contraintes** : Identification du patient ; identification du produit (lot, DCI) ; quantité dispensée ; date de dispensation ; identification du dispensateur
- **Référentiel source** : FHIR MedicationDispense

#### Rattachement

- **Capacités** : [CAP-10](../../referentiel/capabilites/cap-10.md), [CAP-13](../../referentiel/capabilites/cap-13.md)
- **Flux de valeur** : [VS-01](../../referentiel/flux-valeur/vs-01.md)
- **Objet métier CAESN** : [BO-03 : Dispensation & produits](../../referentiel/objets-metier/bo-03.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-9](../../referentiel/chapitres/art-9.md)

### DO-11 : Produit de santé

Tout produit pharmaceutique, vaccin, dispositif médical ou intrant de santé soumis à réglementation. Il est identifié par sa DCI (Dénomination Commune Internationale), son nom commercial, son dosage et son forme pharmaceutique.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-10](../../referentiel/capabilites/cap-10.md), [CAP-14](../../referentiel/capabilites/cap-14.md) et contribue aux flux de valeur [VS-01](../../referentiel/flux-valeur/vs-01.md), [VS-02](../../referentiel/flux-valeur/vs-02.md). Il est porté par l'objet métier [BO-03 : Dispensation & produits](../../referentiel/objets-metier/bo-03.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-9](../../referentiel/chapitres/art-9.md).

#### Attributs et contraintes

- **Type** : Entité référentielle
- **Contraintes** : Code DCI obligatoire ; nom commercial ; dosage ; forme pharmaceutique ; statut réglementaire (autorisé, enregistré, retiré)
- **Référentiel source** : Référentiel des produits de santé (CAESN), OMS ATC

#### Rattachement

- **Capacités** : [CAP-10](../../referentiel/capabilites/cap-10.md), [CAP-14](../../referentiel/capabilites/cap-14.md)
- **Flux de valeur** : [VS-01](../../referentiel/flux-valeur/vs-01.md), [VS-02](../../referentiel/flux-valeur/vs-02.md)
- **Objet métier CAESN** : [BO-03 : Dispensation & produits](../../referentiel/objets-metier/bo-03.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-9](../../referentiel/chapitres/art-9.md)

### DO-12 : Lot

Unité de production d'un produit de santé, identifiée par un numéro de lot, une date de fabrication et une date de péremption. Le lot permet la traçabilité complète de la chaîne d'approvisionnement.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-10](../../referentiel/capabilites/cap-10.md) et contribue aux flux de valeur [VS-01](../../referentiel/flux-valeur/vs-01.md). Il est porté par l'objet métier [BO-03 : Dispensation & produits](../../referentiel/objets-metier/bo-03.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-9](../../referentiel/chapitres/art-9.md).

#### Attributs et contraintes

- **Type** : Entité
- **Contraintes** : Numéro de lot unique par produit ; date de fabrication ; date de péremption ; fabricant ; pays d'origine
- **Référentiel source** : FHIR Medication

#### Rattachement

- **Capacités** : [CAP-10](../../referentiel/capabilites/cap-10.md)
- **Flux de valeur** : [VS-01](../../referentiel/flux-valeur/vs-01.md)
- **Objet métier CAESN** : [BO-03 : Dispensation & produits](../../referentiel/objets-metier/bo-03.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-9](../../referentiel/chapitres/art-9.md)

### DO-13 : Stock

Quantité disponible d'un produit de santé dans un point de stockage (entrepôt, formation sanitaire, case de santé). Il est calculé comme le solde entre les entrées (réceptions, transferts) et les sorties (dispensations, pertes, péremptions).

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-10](../../referentiel/capabilites/cap-10.md) et contribue aux flux de valeur [VS-01](../../referentiel/flux-valeur/vs-01.md), [VS-02](../../referentiel/flux-valeur/vs-02.md). Il est porté par l'objet métier [BO-03 : Dispensation & produits](../../referentiel/objets-metier/bo-03.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-9](../../referentiel/chapitres/art-9.md).

#### Attributs et contraintes

- **Type** : Mesure
- **Contraintes** : Quantité ≥ 0 ; point de stockage identifié ; produit identifié ; date de dernière mise à jour ; seuil d'alerte
- **Référentiel source** : LMIS ( Logistics Management Information System)

#### Rattachement

- **Capacités** : [CAP-10](../../referentiel/capabilites/cap-10.md)
- **Flux de valeur** : [VS-01](../../referentiel/flux-valeur/vs-01.md), [VS-02](../../referentiel/flux-valeur/vs-02.md)
- **Objet métier CAESN** : [BO-03 : Dispensation & produits](../../referentiel/objets-metier/bo-03.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-9](../../referentiel/chapitres/art-9.md)
---

<!-- END:GENERATED -->

## 4. Financement & couverture

**Objet métier CAESN correspondant** : [BO-04 : Financement & couverture](../../00_caesn/04_data/objets.md).

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/objets-de-donnees/do-14.md,referentiel/objets-de-donnees/do-15.md,referentiel/objets-de-donnees/do-16.md,referentiel/objets-de-donnees/do-17.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### DO-14 : Éligibilité

Statut déterminant si un patient bénéficie d'une couverture sanitaire (gratuité, assurance, programme). Il est calculé selon des critères définis par les programmes de protection financière (BPC, AMM, assurances).

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-02](../../referentiel/capabilites/cap-02.md), [CAP-07](../../referentiel/capabilites/cap-07.md) et contribue aux flux de valeur [VS-03](../../referentiel/flux-valeur/vs-03.md). Il est porté par l'objet métier [BO-04 : Financement & couverture](../../referentiel/objets-metier/bo-04.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-9](../../referentiel/chapitres/art-9.md).

#### Attributs et contraintes

- **Type** : Statut
- **Contraintes** : Statut : éligible, non-éligible, en attente de vérification ; source de l'éligibilité (programme, assureur) ; période de validité
- **Référentiel source** : FHIR Coverage

#### Rattachement

- **Capacités** : [CAP-02](../../referentiel/capabilites/cap-02.md), [CAP-07](../../referentiel/capabilites/cap-07.md)
- **Flux de valeur** : [VS-03](../../referentiel/flux-valeur/vs-03.md)
- **Objet métier CAESN** : [BO-04 : Financement & couverture](../../referentiel/objets-metier/bo-04.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-9](../../referentiel/chapitres/art-9.md)

### DO-15 : Couverture sanitaire

Ensemble des mécanismes financiers protégeant un patient contre les coûts directs des soins. Elle comprend les programmes publics (gratuité soins MIOHA, BPC), les assurances maladie et les mécanismes de tierce payante.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-02](../../referentiel/capabilites/cap-02.md), [CAP-07](../../referentiel/capabilites/cap-07.md) et contribue aux flux de valeur [VS-03](../../referentiel/flux-valeur/vs-03.md). Il est porté par l'objet métier [BO-04 : Financement & couverture](../../referentiel/objets-metier/bo-04.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-9](../../referentiel/chapitres/art-9.md).

#### Attributs et contraintes

- **Type** : Entité
- **Contraintes** : Type de couverture (publique, privée, mixte) ; organisme gestionnaire ; période de validité ; plafonds et exclusions
- **Référentiel source** : FHIR Coverage, normes IHE

#### Rattachement

- **Capacités** : [CAP-02](../../referentiel/capabilites/cap-02.md), [CAP-07](../../referentiel/capabilites/cap-07.md)
- **Flux de valeur** : [VS-03](../../referentiel/flux-valeur/vs-03.md)
- **Objet métier CAESN** : [BO-04 : Financement & couverture](../../referentiel/objets-metier/bo-04.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-9](../../referentiel/chapitres/art-9.md)

### DO-16 : Facturation

Processus de détermination et d'enregistrement des coûts des services et produits de santé fournis à un patient. Elle constitue la base du remboursement, du tiers-payant et du suivi financier.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-07](../../referentiel/capabilites/cap-07.md) et contribue aux flux de valeur [VS-03](../../referentiel/flux-valeur/vs-03.md), [VS-04](../../referentiel/flux-valeur/vs-04.md). Il est porté par l'objet métier [BO-04 : Financement & couverture](../../referentiel/objets-metier/bo-04.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-9](../../referentiel/chapitres/art-9.md).

#### Attributs et contraintes

- **Type** : Événement financier
- **Contraintes** : Montant total détaillé par élément ; statut (payée, en attente, remboursée) ; mode de paiement ; référence au paiement
- **Référentiel source** : FHIR Claim

#### Rattachement

- **Capacités** : [CAP-07](../../referentiel/capabilites/cap-07.md)
- **Flux de valeur** : [VS-03](../../referentiel/flux-valeur/vs-03.md), [VS-04](../../referentiel/flux-valeur/vs-04.md)
- **Objet métier CAESN** : [BO-04 : Financement & couverture](../../referentiel/objets-metier/bo-04.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-9](../../referentiel/chapitres/art-9.md)

### DO-17 : Vérification d'éligibilité

Contrôle en temps réel, au point de service, du statut d'éligibilité d'un patient à un mécanisme de protection financière (CSU, BPC, AMM, assurance). La vérification détermine si les soins peuvent être dispensés sans paiement direct ou avec prise en charge partielle.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-07](../../referentiel/capabilites/cap-07.md), [CAP-08](../../referentiel/capabilites/cap-08.md) et contribue aux flux de valeur [VS-03](../../referentiel/flux-valeur/vs-03.md). Il est porté par l'objet métier [BO-04 : Financement & couverture](../../referentiel/objets-metier/bo-04.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-9](../../referentiel/chapitres/art-9.md).

#### Attributs et contraintes

- **Type** : Événement transactionnel
- **Contraintes** : Identifiant du patient (NIN) ; mécanisme de couverture vérifié ; résultat (éligible, non-éligible, erreur) ; horodatage ; point de service émetteur
- **Référentiel source** : FHIR CoverageEligibilityRequest/Response

#### Rattachement

- **Capacités** : [CAP-07](../../referentiel/capabilites/cap-07.md), [CAP-08](../../referentiel/capabilites/cap-08.md)
- **Flux de valeur** : [VS-03](../../referentiel/flux-valeur/vs-03.md)
- **Objet métier CAESN** : [BO-04 : Financement & couverture](../../referentiel/objets-metier/bo-04.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md), [ART-9](../../referentiel/chapitres/art-9.md)
---

<!-- END:GENERATED -->

## 5. Risque & surveillance

**Objet métier CAESN correspondant** : [BO-05 : Risque & surveillance](../../00_caesn/04_data/objets.md).

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/objets-de-donnees/do-18.md,referentiel/objets-de-donnees/do-19.md,referentiel/objets-de-donnees/do-20.md,referentiel/objets-de-donnees/do-21.md,referentiel/objets-de-donnees/do-22.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### DO-18 : Signal

Information brute ou indice épidémiologique détecté par un agent communautaire, un formation sanitaire ou un système de surveillance, indiquant un événement sanitaire inhabituel susceptible de nécessiter une investigation.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-06](../../referentiel/capabilites/cap-06.md), [CAP-11](../../referentiel/capabilites/cap-11.md) et contribue aux flux de valeur [VS-02](../../referentiel/flux-valeur/vs-02.md), [VS-04](../../referentiel/flux-valeur/vs-04.md). Il est porté par l'objet métier [BO-05 : Risque & surveillance](../../referentiel/objets-metier/bo-05.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md).

#### Attributs et contraintes

- **Type** : Événement
- **Contraintes** : Date et heure de détection ; localisation (GPS ou fokontany) ; type de signal (suspecté, confirmé) ; source du signal
- **Référentiel source** : Système EVIPNet, DHIS2

#### Rattachement

- **Capacités** : [CAP-06](../../referentiel/capabilites/cap-06.md), [CAP-11](../../referentiel/capabilites/cap-11.md)
- **Flux de valeur** : [VS-02](../../referentiel/flux-valeur/vs-02.md), [VS-04](../../referentiel/flux-valeur/vs-04.md)
- **Objet métier CAESN** : [BO-05 : Risque & surveillance](../../referentiel/objets-metier/bo-05.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md)

### DO-19 : Foyer

Zone géographique ou population définie dans laquelle un événement sanitaire (épidémie, outbreak) est identifié ou suspecté. Il délimite le périmètre d'intervention de la riposte.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-11](../../referentiel/capabilites/cap-11.md) et contribue aux flux de valeur [VS-02](../../referentiel/flux-valeur/vs-02.md), [VS-04](../../referentiel/flux-valeur/vs-04.md). Il est porté par l'objet métier [BO-05 : Risque & surveillance](../../referentiel/objets-metier/bo-05.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md).

#### Attributs et contraintes

- **Type** : Entité spatiale
- **Contraintes** : Périmètre géographique ; population exposée ; date d'ouverture ; date de clôture ; statut (actif, clôturé)
- **Référentiel source** : OMS GOARN, OIE

#### Rattachement

- **Capacités** : [CAP-11](../../referentiel/capabilites/cap-11.md)
- **Flux de valeur** : [VS-02](../../referentiel/flux-valeur/vs-02.md), [VS-04](../../referentiel/flux-valeur/vs-04.md)
- **Objet métier CAESN** : [BO-05 : Risque & surveillance](../../referentiel/objets-metier/bo-05.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md)

### DO-20 : Investigation

Enquête épidémiologique et/ou de laboratoire menée pour confirmer ou infirmer un signal, identifier la source, le mode de transmission et les facteurs de risque d'un événement sanitaire.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-06](../../referentiel/capabilites/cap-06.md), [CAP-11](../../referentiel/capabilites/cap-11.md) et contribue aux flux de valeur [VS-02](../../referentiel/flux-valeur/vs-02.md), [VS-04](../../referentiel/flux-valeur/vs-04.md). Il est porté par l'objet métier [BO-05 : Risque & surveillance](../../referentiel/objets-metier/bo-05.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md).

#### Attributs et contraintes

- **Type** : Événement
- **Contraintes** : Date de début et de fin ; enquêteurs ; échantillons prélevés ; résultats de laboratoire ; conclusion (confirmé, infirmé, en cours)
- **Référentiel source** : DHIS2, OMS protocoles

#### Rattachement

- **Capacités** : [CAP-06](../../referentiel/capabilites/cap-06.md), [CAP-11](../../referentiel/capabilites/cap-11.md)
- **Flux de valeur** : [VS-02](../../referentiel/flux-valeur/vs-02.md), [VS-04](../../referentiel/flux-valeur/vs-04.md)
- **Objet métier CAESN** : [BO-05 : Risque & surveillance](../../referentiel/objets-metier/bo-05.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md)

### DO-21 : Notification sanitaire

Transmission formelle et obligatoire d'un événement sanitaire suspecté ou confirmé aux autorités compétentes (district, région, ministère, OMS). La notification initie le processus officiel de réponse et constitue un engagement juridique du déclarant. Elle se distingue de l'alerte par son caractère formel et institutionnel.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-06](../../referentiel/capabilites/cap-06.md), [CAP-11](../../referentiel/capabilites/cap-11.md) et contribue aux flux de valeur [VS-02](../../referentiel/flux-valeur/vs-02.md). Il est porté par l'objet métier [BO-05 : Risque & surveillance](../../referentiel/objets-metier/bo-05.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md).

#### Attributs et contraintes

- **Type** : Événement institutionnel
- **Contraintes** : Événement notifié (signal, cas confirmé, foyer) ; autorité destinataire ; délai réglementaire de déclaration ; déclarant identifié ; statut (envoyée, confirmée, en attente)
- **Référentiel source** : FHIR Communication, Règlement sanitaire international (RSI)

#### Rattachement

- **Capacités** : [CAP-06](../../referentiel/capabilites/cap-06.md), [CAP-11](../../referentiel/capabilites/cap-11.md)
- **Flux de valeur** : [VS-02](../../referentiel/flux-valeur/vs-02.md)
- **Objet métier CAESN** : [BO-05 : Risque & surveillance](../../referentiel/objets-metier/bo-05.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md)

### DO-22 : Alerte sanitaire

Avertissement déclenché automatiquement ou manuellement lorsqu'un indicateur de surveillance dépasse un seuil prédéfini. L'alerte est une action opérationnelle qui découlent de la notification ; elle vise à mobiliser rapidement les acteurs compétents pour la riposte.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-06](../../referentiel/capabilites/cap-06.md), [CAP-11](../../referentiel/capabilites/cap-11.md) et contribue aux flux de valeur [VS-02](../../referentiel/flux-valeur/vs-02.md), [VS-04](../../referentiel/flux-valeur/vs-04.md). Il est porté par l'objet métier [BO-05 : Risque & surveillance](../../referentiel/objets-metier/bo-05.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md).

#### Attributs et contraintes

- **Type** : Événement opérationnel
- **Contraintes** : Indicateur déclencheur ; seuil franchi ; périmètre géographique concerné ; niveau d'urgence (1-4) ; destinataires ; statut (émise, acquittée, en cours de traitement)
- **Référentiel source** : FHIR Communication (priority: urgent), DHIS2 alerts

#### Rattachement

- **Capacités** : [CAP-06](../../referentiel/capabilites/cap-06.md), [CAP-11](../../referentiel/capabilites/cap-11.md)
- **Flux de valeur** : [VS-02](../../referentiel/flux-valeur/vs-02.md), [VS-04](../../referentiel/flux-valeur/vs-04.md)
- **Objet métier CAESN** : [BO-05 : Risque & surveillance](../../referentiel/objets-metier/bo-05.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-3](../../referentiel/chapitres/art-3.md)
---

<!-- END:GENERATED -->

## 6. Exploitation & gestion

**Objet métier CAESN correspondant** : [BO-06 : Exploitation & gestion](../../00_caesn/04_data/objets.md).

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/objets-de-donnees/do-23.md,referentiel/objets-de-donnees/do-24.md,referentiel/objets-de-donnees/do-25.md,referentiel/objets-de-donnees/do-26.md,referentiel/objets-de-donnees/do-27.md,referentiel/objets-de-donnees/do-28.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### DO-23 : Formation sanitaire

Toute structure de soins publique, privée, confessionnelle ou communautaire identifiée de manière unique dans le référentiel national des formations sanitaires. C'est l'unité de base du réseau de soins.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-05](../../referentiel/capabilites/cap-05.md), [CAP-14](../../referentiel/capabilites/cap-14.md) et contribue aux flux de valeur [VS-01](../../referentiel/flux-valeur/vs-01.md), [VS-02](../../referentiel/flux-valeur/vs-02.md), [VS-03](../../referentiel/flux-valeur/vs-03.md), [VS-04](../../referentiel/flux-valeur/vs-04.md). Il est porté par l'objet métier [BO-06 : Exploitation & gestion](../../referentiel/objets-metier/bo-06.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md).

#### Attributs et contraintes

- **Type** : Entité référentielle
- **Contraintes** : Code unique (selon INSTAT) ; dénomination officielle ; type (hôpital, centre de santé, case de santé) ; niveau de qualification ; statut (actif, fermé, en construction)
- **Référentiel source** : Référentiel des formations sanitaires (CAESN)

#### Rattachement

- **Capacités** : [CAP-05](../../referentiel/capabilites/cap-05.md), [CAP-14](../../referentiel/capabilites/cap-14.md)
- **Flux de valeur** : [VS-01](../../referentiel/flux-valeur/vs-01.md), [VS-02](../../referentiel/flux-valeur/vs-02.md), [VS-03](../../referentiel/flux-valeur/vs-03.md), [VS-04](../../referentiel/flux-valeur/vs-04.md)
- **Objet métier CAESN** : [BO-06 : Exploitation & gestion](../../referentiel/objets-metier/bo-06.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md)

### DO-24 : Agent de santé

Toute personne physique exerçant une activité de soins, de prévention ou de promotion de la santé dans une formation sanitaire, identifiée par son rôle, ses qualifications et son affectation.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-09](../../referentiel/capabilites/cap-09.md), [CAP-13](../../referentiel/capabilites/cap-13.md) et contribue aux flux de valeur [VS-01](../../referentiel/flux-valeur/vs-01.md), [VS-02](../../referentiel/flux-valeur/vs-02.md), [VS-03](../../referentiel/flux-valeur/vs-03.md), [VS-04](../../referentiel/flux-valeur/vs-04.md). Il est porté par l'objet métier [BO-06 : Exploitation & gestion](../../referentiel/objets-metier/bo-06.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md).

#### Attributs et contraintes

- **Type** : Entité
- **Contraintes** : Identifiant unique ; nom ; qualification (médecin, infirmier, ACS, etc.) ; affectation (formation sanitaire, zone) ; statut (actif, inactif)
- **Référentiel source** : Référentiel des agents de santé (CAESN)

#### Rattachement

- **Capacités** : [CAP-09](../../referentiel/capabilites/cap-09.md), [CAP-13](../../referentiel/capabilites/cap-13.md)
- **Flux de valeur** : [VS-01](../../referentiel/flux-valeur/vs-01.md), [VS-02](../../referentiel/flux-valeur/vs-02.md), [VS-03](../../referentiel/flux-valeur/vs-03.md), [VS-04](../../referentiel/flux-valeur/vs-04.md)
- **Objet métier CAESN** : [BO-06 : Exploitation & gestion](../../referentiel/objets-metier/bo-06.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md)

### DO-25 : Indicateur sanitaire

Mesure standardisée d'une performance, d'un résultat ou d'un processus dans le domaine de la santé. Chaque indicateur doit avoir une définition unique, stable et partagée, avec une méthodologie de calcul précise.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-03](../../referentiel/capabilites/cap-03.md), [CAP-08](../../referentiel/capabilites/cap-08.md) et contribue aux flux de valeur [VS-01](../../referentiel/flux-valeur/vs-01.md), [VS-02](../../referentiel/flux-valeur/vs-02.md), [VS-03](../../referentiel/flux-valeur/vs-03.md), [VS-04](../../referentiel/flux-valeur/vs-04.md). Il est porté par l'objet métier [BO-06 : Exploitation & gestion](../../referentiel/objets-metier/bo-06.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md).

#### Attributs et contraintes

- **Type** : Entité référentielle
- **Contraintes** : Code unique ; nom ; définition ; méthodologie de calcul ; unité de mesure ; fréquence de collecte ; source de données
- **Référentiel source** : Référentiel des indicateurs sanitaires (CAESN), DHIS2

#### Rattachement

- **Capacités** : [CAP-03](../../referentiel/capabilites/cap-03.md), [CAP-08](../../referentiel/capabilites/cap-08.md)
- **Flux de valeur** : [VS-01](../../referentiel/flux-valeur/vs-01.md), [VS-02](../../referentiel/flux-valeur/vs-02.md), [VS-03](../../referentiel/flux-valeur/vs-03.md), [VS-04](../../referentiel/flux-valeur/vs-04.md)
- **Objet métier CAESN** : [BO-06 : Exploitation & gestion](../../referentiel/objets-metier/bo-06.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md)

### DO-26 : Zone sanitaire

Unité territoriale de planification et de coordination des services de santé, correspondant généralement à un district sanitaire. Elle regroupe les formations sanitaires et les zones de couverture d'une même aire de responsabilité.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-05](../../referentiel/capabilites/cap-05.md), [CAP-14](../../referentiel/capabilites/cap-14.md) et contribue aux flux de valeur [VS-01](../../referentiel/flux-valeur/vs-01.md), [VS-02](../../referentiel/flux-valeur/vs-02.md), [VS-03](../../referentiel/flux-valeur/vs-03.md), [VS-04](../../referentiel/flux-valeur/vs-04.md). Il est porté par l'objet métier [BO-06 : Exploitation & gestion](../../referentiel/objets-metier/bo-06.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md).

#### Attributs et contraintes

- **Type** : Entité spatiale
- **Contraintes** : Code unique ; dénomination ; limites géographiques ; population ; chef-lieu ; formations sanitaires rattachées
- **Référentiel source** : Référentiel géographique sanitaire (CAESN), INSTAT

#### Rattachement

- **Capacités** : [CAP-05](../../referentiel/capabilites/cap-05.md), [CAP-14](../../referentiel/capabilites/cap-14.md)
- **Flux de valeur** : [VS-01](../../referentiel/flux-valeur/vs-01.md), [VS-02](../../referentiel/flux-valeur/vs-02.md), [VS-03](../../referentiel/flux-valeur/vs-03.md), [VS-04](../../referentiel/flux-valeur/vs-04.md)
- **Objet métier CAESN** : [BO-06 : Exploitation & gestion](../../referentiel/objets-metier/bo-06.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md)

### DO-27 : Tâche

Unité de travail assignée à un acteur (personne ou système) dans le cadre d'un processus opérationnel : investigation terrain, campagne de vaccination, distribution d'intrants, visite de suivi. La tâche porte un statut, des échéances et une traçabilité complète d'exécution.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-06](../../referentiel/capabilites/cap-06.md), [CAP-11](../../referentiel/capabilites/cap-11.md), [CAP-14](../../referentiel/capabilites/cap-14.md) et contribue aux flux de valeur [VS-01](../../referentiel/flux-valeur/vs-01.md), [VS-02](../../referentiel/flux-valeur/vs-02.md). Il est porté par l'objet métier [BO-06 : Exploitation & gestion](../../referentiel/objets-metier/bo-06.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md).

#### Attributs et contraintes

- **Type** : Entité opérationnelle
- **Contraintes** : Description de l'action ; assigné à (agent ou organisation) ; date d'échéance ; statut (à faire, en cours, terminée, annulée) ; résultat ; priorité
- **Référentiel source** : FHIR Task

#### Rattachement

- **Capacités** : [CAP-06](../../referentiel/capabilites/cap-06.md), [CAP-11](../../referentiel/capabilites/cap-11.md), [CAP-14](../../referentiel/capabilites/cap-14.md)
- **Flux de valeur** : [VS-01](../../referentiel/flux-valeur/vs-01.md), [VS-02](../../referentiel/flux-valeur/vs-02.md)
- **Objet métier CAESN** : [BO-06 : Exploitation & gestion](../../referentiel/objets-metier/bo-06.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md)

### DO-28 : Tableau de bord

Vue consolidée et synthétique d'indicateurs de performance affichée aux décideurs à des fins de pilotage. Il agrège des données provenant de plusieurs sources (formations sanitaires, programmes, districts) et les présente sous forme graphique avec des seuils d'alerte.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-08](../../referentiel/capabilites/cap-08.md), [CAP-16](../../referentiel/capabilites/cap-16.md) et contribue aux flux de valeur [VS-04](../../referentiel/flux-valeur/vs-04.md). Il est porté par l'objet métier [BO-06 : Exploitation & gestion](../../referentiel/objets-metier/bo-06.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md).

#### Attributs et contraintes

- **Type** : Entité de restitution
- **Contraintes** : Indicateurs affichés ; périmètre géographique ; période ; fréquence de mise à jour ; niveau d'accès requis ; destinataires
- **Référentiel source** : FHIR Dashboard (profil national), DHIS2

#### Rattachement

- **Capacités** : [CAP-08](../../referentiel/capabilites/cap-08.md), [CAP-16](../../referentiel/capabilites/cap-16.md)
- **Flux de valeur** : [VS-04](../../referentiel/flux-valeur/vs-04.md)
- **Objet métier CAESN** : [BO-06 : Exploitation & gestion](../../referentiel/objets-metier/bo-06.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-4](../../referentiel/chapitres/art-4.md)
---

<!-- END:GENERATED -->

## 7. Interopérabilité transfrontalière & résumé patient

**Objet métier CAESN correspondant** : [BO-07 : Interopérabilité transfrontalière](../../00_caesn/04_data/objets.md).

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/objets-de-donnees/do-29.md,referentiel/objets-de-donnees/do-30.md,referentiel/objets-de-donnees/do-31.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### DO-29 : Résumé international du patient (International Patient Summary : IPS)

Document clinique structuré, minimal et non exhaustif, destiné à faciliter la continuité des soins lors d'un episode de soins transfrontalier. Conforme au standard HL7 IPS, il comprend les informations cliniques essentielles du patient : démographie, allergies, médicaments en cours, problèmes de santé, antécédents, vaccinations, résultats de diagnostic, dispositifs médicaux et procédures. Il est échangeable entre systèmes de santé de pays différents grâce aux profils FHIR IPS.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-17 (engagement patient)](../../referentiel/capabilites/cap-17.md) et contribue aux flux de valeur [VS-01 (parcours patient)](../../referentiel/flux-valeur/vs-01.md). Il est porté par l'objet métier [BO-07 : Interopérabilité transfrontalière](../../referentiel/objets-metier/bo-07.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-7](../../referentiel/chapitres/art-7.md).

#### Attributs et contraintes

- **Type** : Document structuré (FHIR Composition)
- **Contraintes** : Conforme au profil HL7 FHIR IPS (hl7.org/fhir/uv/ips) ; langue obligatoire (français + anglais) ; sections minimales obligatoires (allergies, médicaments, problèmes) ; date d'émission et validité ; signature électronique du prestataire
- **Référentiel source** : HL7 FHIR R4 : International Patient Summary (IPS)

#### Rattachement

- **Capacités** : [CAP-17 (engagement patient)](../../referentiel/capabilites/cap-17.md)
- **Capacités intégrées (CNISN)** : [CAP-INT-13 (interopérabilité transfrontalière)](../../referentiel/capacites/cap-int-13.md)
- **Flux de valeur** : [VS-01 (parcours patient)](../../referentiel/flux-valeur/vs-01.md)
- **Profils (PTISN)** : [PT-14 (interopérabilité transfrontalière)](../../referentiel/profils/pt-14.md)
- **Objet métier CAESN** : [BO-07 : Interopérabilité transfrontalière](../../referentiel/objets-metier/bo-07.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-7](../../referentiel/chapitres/art-7.md)

### DO-30 : Section du résumé patient

Unité structurée du résumé international du patient (IPS), regroupant une catégorie clinique spécifique. Chaque section est un objet FHIR autonome pouvant être échangé individuellement selon le principe de minimisation des données.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-INT-13](../../referentiel/capacites/cap-int-13.md) et contribue aux flux de valeur [VS-01](../../referentiel/flux-valeur/vs-01.md). Il est porté par l'objet métier [BO-07 : Interopérabilité transfrontalière](../../referentiel/objets-metier/bo-07.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-7](../../referentiel/chapitres/art-7.md).

#### Attributs et contraintes

- **Type** : Entité composite
- **Contraintes** : Code de section conforme au ValueSet IPS (allergies, médicaments, problèmes, antécédents, vaccinations, résultats, dispositifs, procédures, observations vitales) ; contenu structuré selon les profils FHIR IPS ; section vide autorisée (« no known… »)
- **Référentiel source** : HL7 FHIR R4 : IPS Sections

#### Rattachement

- **Capacités intégrées (CNISN)** : [CAP-INT-13](../../referentiel/capacites/cap-int-13.md)
- **Flux de valeur** : [VS-01](../../referentiel/flux-valeur/vs-01.md)
- **Profils (PTISN)** : [PT-14](../../referentiel/profils/pt-14.md)
- **Objet métier CAESN** : [BO-07 : Interopérabilité transfrontalière](../../referentiel/objets-metier/bo-07.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-7](../../referentiel/chapitres/art-7.md)
#### Sections IPS obligatoires

- **ALGY** : Allergies et intolérances — AllergyIntolerance — Substance, réaction, sévérité, statut
- **MDCA** : Médicaments actuels — MedicationStatement — Produit, dosage, statut, indication
- **PROB** : Problèmes de santé — Condition — Code CIM-10, onset, statut
- **HIST** : Antécédents — Condition — Épisodes passés, résolus
- **IMMU** : Vaccinations — Immunization — Vaccin, date, lot, statut
- **VITAL** : Signes vitaux — Observation — Mesures (TA, FC, SpO2, température)
- **LAB** : Résultats de diagnostic — Observation — Résultats laboratoire
- **DEVI** : Dispositifs médicaux — DeviceUseStatement — Dispositif, date, statut
- **PROC** : Procédures — Procedure — Acte, date, résultat
- **IDOI** : Identité du patient — Patient — NIN, nom, naissance, sexe

### DO-31 : Confiance internationale (Trust Anchor)

Point d'ancrage de confiance numérique permettant la vérification mutuelle de l'identité et de la conformité des systèmes de santé échangeant des données transfrontalières. Conforme au GDHCN (Global Digital Health Certification Network), il garantit l'authenticité, l'intégrité et la non-répudiation des résumés patients échangés.

#### Rôle et contexte

Ce concept est mobilisé par les capacités [CAP-15](../../referentiel/capabilites/cap-15.md). Il est porté par l'objet métier [BO-07 : Interopérabilité transfrontalière](../../referentiel/objets-metier/bo-07.md) et traité dans les chapitres ARTSN [ART-2](../../referentiel/chapitres/art-2.md), [ART-7](../../referentiel/chapitres/art-7.md).

#### Attributs et contraintes

- **Type** : Entité infrastructure
- **Contraintes** : Certificat X.509v3 signé par l'autorité GDHCN nationale ; révocation en temps réel (CRL/OCSP) ; renouvellement avant expiration ; journalisation de toutes les vérifications
- **Référentiel source** : GDHCN, ITU-T X.509

#### Rattachement

- **Capacités** : [CAP-15](../../referentiel/capabilites/cap-15.md)
- **Capacités intégrées (CNISN)** : [CAP-INT-13](../../referentiel/capacites/cap-int-13.md)
- **Profils (PTISN)** : [PT-14](../../referentiel/profils/pt-14.md)
- **Objet métier CAESN** : [BO-07 : Interopérabilité transfrontalière](../../referentiel/objets-metier/bo-07.md)
- **Chapitres ARTSN** : [ART-2](../../referentiel/chapitres/art-2.md), [ART-7](../../referentiel/chapitres/art-7.md)
---

<!-- END:GENERATED -->

## Liens

- Chapitres et patterns de référence
- ART-2 : Médiation et normalisation
- ART-7 : Sécurité, contrôle d'accès et résidence
- PT-14 : Interopérabilité transfrontalière
- CAP-INT-13 : Interopérabilité transfrontalière
- CAESN : données
- CAESN : domaines de données
- CAESN : référentiels nationaux

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **chapitre ART-2 (médiation et normalisation)** : Médiation et normalisation (`referentiel/chapitres/art-2.md`)
- **F.2** : F.2 : Préservation de la souveraineté intersectorielle (`referentiel/fondations/f-2.md`)
- **F.3** : F.3 : Éradication des silos technologiques (`referentiel/fondations/f-3.md`)
- **CAESN** : Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) (`00_caesn/00_overview/index.md`)
- **Chapitres et patterns de référence** : Chapitres et patterns de référence (`02_artsn/04_patterns/index.md`)
- **ART-2 : Médiation et normalisation** : Médiation et normalisation (`referentiel/chapitres/art-2.md`)
- **ART-7 : Sécurité, contrôle d'accès et résidence** : Sécurité, contrôle d'accès et résidence de la donnée (`referentiel/chapitres/art-7.md`)
- **PT-14 : Interopérabilité transfrontalière** : Interopérabilité transfrontalière (`03_ptisn/03_profils/pt-14-interopabilite-transfrontaliere.md`)
- **CAP-INT-13 : Interopérabilité transfrontalière** : Partie II : Capacités nationales requises (`01_cnisn/02_capacites/index.md`)
- **CAESN : données** : Architecture des données et de l'information sanitaire (`00_caesn/04_data/index.md`)
- **CAESN : domaines de données** : Domaines de données prioritaires (`00_caesn/04_data/domains.md`)
- **CAESN : référentiels nationaux** : Référentiels nationaux (`00_caesn/04_data/referentials.md`)
