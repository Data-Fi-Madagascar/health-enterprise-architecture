---
title: Dictionnaire de données fonctionnelles
id: artsn-dictionnaire-donnees
domain: 02_artsn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: [artsn, dictionnaire, donnees, semantique, niveau-3]
---

# Dictionnaire de données fonctionnelles

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

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

### P-01 — Patient

| Champ | Valeur |
|-------|--------|
| **Nom** | Patient |
| **Définition** | Personne physique bénéficiaire de soins de santé, identifiée de manière unique au sein du système d'information sanitaire national. L'identité du patient est un actif stratégique national qui ne peut être dupliquée, fragmentée ou remplacée par des identifiants propriétaires de programmes ou de projets. |
| **Type** | Entité (identifiant unique + attributs) |
| **Contraintes** | Identifiant unique national (NIN ou identifiant provisoire) ; un seul enregistrement par personne physique ; traçabilité des doublons détectés et résolus |
| **Rattachement** | CAP-01 (continuité des soins), CAP-13 (interopérabilité données), VS-01 (parcours patient), VS-03 (protection financière) |
| **Référentiel source** | Référentiel des bénéficiaires / patients (CAESN) |

### P-02 — Identifiant national d'identification

| Champ | Valeur |
|-------|--------|
| **Nom** | Identifiant national d'identification (NIN) |
| **Définition** | Code alphanumérique unique attribué à chaque patient dans le référentiel national des bénéficiaires. Il garantit l'unicité de l'identité patient à travers tous les systèmes et toutes les initiatives. |
| **Type** | Identifiant |
| **Contraintes** | Format : 12 chiffres (selon le modèle INSTAT) ; attribué une seule fois ; non modifiable après validation ; traçabilité des attributions |
| **Rattachement** | CAP-01, CAP-14, PT-04 (identité nationale) |
| **Référentiel source** | Référentiel des bénéficiaires / patients |

### P-03 — Dossier patient

| Champ | Valeur |
|-------|--------|
| **Nom** | Dossier patient |
| **Définition** | Ensemble structuré des informations cliniques, administratives et de suivi relatives à un patient au cours de sa vie. Il comprend les antécédents, les épisodes de soins, les prescriptions, les résultats d'examens et les documents cliniques. |
| **Type** | Entité composite |
| **Contraintes** | Un seul dossier par patient (consolidation multi-sources) ; accessibilité au point de service même en connectivité limitée ; protection des données sensibles par rôle et finalité |
| **Rattachement** | CAP-01, CAP-13, VS-01 |
| **Référentiel source** | FHIR Patient, IHE PCD |

### P-04 — Épisode de soins

| Champ | Valeur |
|-------|--------|
| **Nom** | Épisode de soins |
| **Définition** | Période continue de prise en charge d'un patient par un ou plusieurs prestataires de soins, depuis l'admission jusqu'à la sortie ou le transfert. Un épisode peut couvrir une consultation, une hospitalisation, un suivi communautaire ou une téléconsultation. |
| **Type** | Entité temporelle |
| **Contraintes** | Date de début obligatoire ; date de fin conditionnelle (en cours) ; un épisode est rattaché à au moins un établissement et un patient |
| **Rattachement** | CAP-01, CAP-05, VS-01 |
| **Référentiel source** | FHIR Encounter |

---

## 2. Prestation & soins

### S-01 — Consultation

| Champ | Valeur |
|-------|--------|
| **Nom** | Consultation |
| **Définition** | Acte clinique réalisé par un prestataire de soins lors d'une rencontre avec un patient. Elle comprend l'anamnèse, l'examen clinique, le diagnostic, la prescription et le suivi. |
| **Type** | Événement |
| **Contraintes** | Date et heure de la consultation ; identification du prestataire ; motivation de la consultation ; diagnostic(s) ; prescription(s) |
| **Rattachement** | CAP-01, CAP-13, VS-01 |
| **Référentiel source** | FHIR Encounter, CIM-10 (diagnostics) |

### S-02 — Prescription

| Champ | Valeur |
|-------|--------|
| **Nom** | Prescription |
| **Définition** | Ordonnance émise par un prestataire de soins, détaillant les médicaments, actes, examens ou soins prescrits pour un patient. Elle constitue le lien clinique entre la consultation et la dispensation. |
| **Type** | Document structuré |
| **Contraintes** | Identification du prescripteur ; date de prescription ; liste des éléments prescrits (médicaments, dosages, posologies) ; durée de validité |
| **Rattachement** | CAP-01, CAP-10, VS-01 |
| **Référentiel source** | FHIR MedicationRequest |

### S-03 — Référence

| Champ | Valeur |
|-------|--------|
| **Nom** | Référence |
| **Définition** | Orientation d'un patient d'un niveau de soins vers un autre (ex. : centre de santé vers hôpital), accompagnée des informations cliniques pertinentes pour la prise en charge ultérieure. La référence initie un parcours inter-établissement : elle est émise par le prestataire d'origine et acceptée par l'établissement de destination. |
| **Type** | Événement inter-établissement |
| **Contraintes** | Établissement d'origine ; établissement de destination ; motif de la référence ; informations cliniques transmises ; acceptance par l'établissement de destination ; mode de transport (ambulance, avion, bateau) ; urgence (U0-U4) |
| **Rattachement** | CAP-02, CAP-05, CAP-14, VS-01 |
| **Référentiel source** | FHIR ServiceRequest (type: referral) |

### S-04 — Contre-référence

| Champ | Valeur |
|-------|--------|
| **Nom** | Contre-référence |
| **Définition** | Retour d'un patient vers l'établissement d'origine après prise en charge spécialisée, accompagné du compte-rendu clinique, des recommandations de suivi et de la prise en charge thérapeutique à poursuivre. La contre-référence clôture le parcours inter-établissement et rétablit la responsabilité clinique au niveau d'origine. |
| **Type** | Événement inter-établissement (retour) |
| **Contraintes** | Établissement d'origine (destination du retour) ; établissement émetteur (spécialisé) ; compte-rendu clinique structuré ; recommandations de suivi ; traitements prescrits ; prochaine échéance de contrôle ; consentement du patient pour le retour |
| **Rattachement** | CAP-02, CAP-05, CAP-14, VS-01 |
| **Référentiel source** | FHIR ServiceRequest (type: referral) + FHIR DocumentReference (compte-rendu) |

### S-05 — Évacuation sanitaire

| Champ | Valeur |
|-------|--------|
| **Nom** | Évacuation sanitaire (medevac) |
| **Définition** | Transfert urgent d'un patient d'un établissement vers un autre établissement ou vers un pays étranger, nécessitant des moyens de transport sanitaires spécialisés (ambulance, avion médicalisé, hélicoptère). L'évacuation sanitaire peut être nationale (de niveau faible vers un hôpital régional/central) ou internationale (vers un centre spécialisé à l'étranger). Elle implique la continuité des soins pendant le transport et la conformité aux réglementations de sortie/entrée du territoire. |
| **Type** | Événement de transport sanitaire |
| **Contraintes** | Établissement d'origine ; établissement/pays de destination ; motif médical de l'évacuation ; mode de transport ; équipe médicale accompagnatrice ; équipment médical embarqué ; autorisation de sortie du territoire (si international) ; accord du pays de réception (si international) ; couverture financière ; consentement éclairé du patient |
| **Rattachement** | CAP-02, CAP-05, CAP-10, CAP-14, CAP-17, VS-01, VS-02 |
| **Référentiel source** | FHIR ServiceRequest (type: transfer) + FHIR Transport + HL7 FHIR IPS (données cliniques embarquées) |

#### Sous-types d'évacuation sanitaire

| Code | Type | Description | Standards applicables |
|------|------|-------------|----------------------|
| **EVA-N1** | Nationale primaire | CSB → Hôpital de district/régional | FHIR ServiceRequest |
| **EVA-N2** | Nationale secondaire | Hôpital régional → CHU central | FHIR ServiceRequest |
| **EVA-I1** | Internationale programmée | Hôpital → Centre spécialisé étranger (planifiée) | FHIR IPS + PT-14 + accords bilatéraux |
| **EVA-I2** | Internationale d'urgence | Hôpital → Pays voisin le plus proche (non planifiée) | FHIR IPS + PT-14 + urgence humanitaire |

---

## 3. Dispensation & produits

### D-01 — Dispensation

| Champ | Valeur |
|-------|--------|
| **Nom** | Dispensation |
| **Définition** | Fourniture effective d'un produit de santé (médicament, vaccin, intrant) à un patient, en exécution d'une prescription. Elle constitue l'acte de sortie du stock et doit être tracée pour la gestion des stocks, la facturation et le suivi thérapeutique. |
| **Type** | Événement |
| **Contraintes** | Identification du patient ; identification du produit (lot, DCI) ; quantité dispensée ; date de dispensation ; identification du dispensateur |
| **Rattachement** | CAP-10, CAP-13, VS-01 |
| **Référentiel source** | FHIR MedicationDispense |

### D-02 — Produit de santé

| Champ | Valeur |
|-------|--------|
| **Nom** | Produit de santé |
| **Définition** | Tout produit pharmaceutique, vaccin, dispositif médical ou intrant de santé soumis à réglementation. Il est identifié par sa DCI (Dénomination Commune Internationale), son nom commercial, son dosage et son forme pharmaceutique. |
| **Type** | Entité référentielle |
| **Contraintes** | Code DCI obligatoire ; nom commercial ; dosage ; forme pharmaceutique ; statut réglementaire (autorisé, enregistré, retiré) |
| **Rattachement** | CAP-10, CAP-14, VS-01, VS-02 |
| **Référentiel source** | Référentiel des produits de santé (CAESN), OMS ATC |

### D-03 — Lot

| Champ | Valeur |
|-------|--------|
| **Nom** | Lot |
| **Définition** | Unité de production d'un produit de santé, identifiée par un numéro de lot, une date de fabrication et une date de péremption. Le lot permet la traçabilité complète de la chaîne d'approvisionnement. |
| **Type** | Entité |
| **Contraintes** | Numéro de lot unique par produit ; date de fabrication ; date de péremption ; fabricant ; pays d'origine |
| **Rattachement** | CAP-10, VS-01 |
| **Référentiel source** | FHIR Medication |

### D-04 — Stock

| Champ | Valeur |
|-------|--------|
| **Nom** | Stock |
| **Définition** | Quantité disponible d'un produit de santé dans un point de stockage (entrepôt, formation sanitaire, case de santé). Il est calculé comme le solde entre les entrées (réceptions, transferts) et les sorties (dispensations, pertes, péremptions). |
| **Type** | Mesure |
| **Contraintes** | Quantité ≥ 0 ; point de stockage identifié ; produit identifié ; date de dernière mise à jour ; seuil d'alerte |
| **Rattachement** | CAP-10, VS-01, VS-02 |
| **Référentiel source** | LMIS ( Logistics Management Information System) |

---

## 4. Financement & couverture

### F-01 — Éligibilité

| Champ | Valeur |
|-------|--------|
| **Nom** | Éligibilité |
| **Définition** | Statut déterminant si un patient bénéficie d'une couverture sanitaire (gratuité, assurance, programme). Il est calculé selon des critères définis par les programmes de protection financière (BPC, AMM, assurances). |
| **Type** | Statut |
| **Contraintes** | Statut : éligible, non-éligible, en attente de vérification ; source de l'éligibilité (programme, assureur) ; période de validité |
| **Rattachement** | CAP-02, CAP-07, VS-03 |
| **Référentiel source** | FHIR Coverage |

### F-02 — Couverture sanitaire

| Champ | Valeur |
|-------|--------|
| **Nom** | Couverture sanitaire |
| **Définition** | Ensemble des mécanismes financiers protégeant un patient contre les coûts directs des soins. Elle comprend les programmes publics (gratuité soins MIOHA, BPC), les assurances maladie et les mécanismes de tierce payante. |
| **Type** | Entité |
| **Contraintes** | Type de couverture (publique, privée, mixte) ; organisme gestionnaire ; période de validité ; plafonds et exclusions |
| **Rattachement** | CAP-02, CAP-07, VS-03 |
| **Référentiel source** | FHIR Coverage, normes IHE |

### F-03 — Facturation

| Champ | Valeur |
|-------|--------|
| **Nom** | Facturation |
| **Définition** | Processus de détermination et d'enregistrement des coûts des services et produits de santé fournis à un patient. Elle constitue la base du remboursement, du tiers-payant et du suivi financier. |
| **Type** | Événement financier |
| **Contraintes** | Montant total détaillé par élément ; statut (payée, en attente, remboursée) ; mode de paiement ; référence au paiement |
| **Rattachement** | CAP-07, VS-03, VS-04 |
| **Référentiel source** | FHIR Claim |

### F-04 — Vérification d'éligibilité

| Champ | Valeur |
|-------|--------|
| **Nom** | Vérification d'éligibilité |
| **Définition** | Contrôle en temps réel, au point de service, du statut d'éligibilité d'un patient à un mécanisme de protection financière (CSU, BPC, AMM, assurance). La vérification détermine si les soins peuvent être dispensés sans paiement direct ou avec prise en charge partielle. |
| **Type** | Événement transactionnel |
| **Contraintes** | Identifiant du patient (NIN) ; mécanisme de couverture vérifié ; résultat (éligible, non-éligible, erreur) ; horodatage ; point de service émetteur |
| **Rattachement** | CAP-07, CAP-08, VS-03 |
| **Référentiel source** | FHIR CoverageEligibilityRequest/Response |

---

## 5. Risque & surveillance

### R-01 — Signal

| Champ | Valeur |
|-------|--------|
| **Nom** | Signal |
| **Définition** | Information brute ou indice épidémiologique détecté par un agent communautaire, un formation sanitaire ou un système de surveillance, indiquant un événement sanitaire inhabituel susceptible de nécessiter une investigation. |
| **Type** | Événement |
| **Contraintes** | Date et heure de détection ; localisation (GPS ou fokontany) ; type de signal (suspecté, confirmé) ; source du signal |
| **Rattachement** | CAP-06, CAP-11, VS-02, VS-04 |
| **Référentiel source** | Système EVIPNet, DHIS2 |

### R-02 — Foyer

| Champ | Valeur |
|-------|--------|
| **Nom** | Foyer |
| **Définition** | Zone géographique ou population définie dans laquelle un événement sanitaire (épidémie, outbreak) est identifié ou suspecté. Il délimite le périmètre d'intervention de la riposte. |
| **Type** | Entité spatiale |
| **Contraintes** | Périmètre géographique ; population exposée ; date d'ouverture ; date de clôture ; statut (actif, clôturé) |
| **Rattachement** | CAP-11, VS-02, VS-04 |
| **Référentiel source** | OMS GOARN, OIE |

### R-03 — Investigation

| Champ | Valeur |
|-------|--------|
| **Nom** | Investigation |
| **Définition** | Enquête épidémiologique et/ou de laboratoire menée pour confirmer ou infirmer un signal, identifier la source, le mode de transmission et les facteurs de risque d'un événement sanitaire. |
| **Type** | Événement |
| **Contraintes** | Date de début et de fin ; enquêteurs ; échantillons prélevés ; résultats de laboratoire ; conclusion (confirmé, infirmé, en cours) |
| **Rattachement** | CAP-06, CAP-11, VS-02, VS-04 |
| **Référentiel source** | DHIS2, OMS protocoles |

### R-04 — Notification sanitaire

| Champ | Valeur |
|-------|--------|
| **Nom** | Notification sanitaire |
| **Définition** | Transmission formelle et obligatoire d'un événement sanitaire suspecté ou confirmé aux autorités compétentes (district, région, ministère, OMS). La notification initie le processus officiel de réponse et constitue un engagement juridique du déclarant. Elle se distingue de l'alerte par son caractère formel et institutionnel. |
| **Type** | Événement institutionnel |
| **Contraintes** | Événement notifié (signal, cas confirmé, foyer) ; autorité destinataire ; délai réglementaire de déclaration ; déclarant identifié ; statut (envoyée, confirmée, en attente) |
| **Rattachement** | CAP-06, CAP-11, VS-02 |
| **Référentiel source** | FHIR Communication, Règlement sanitaire international (RSI) |

### R-05 — Alerte sanitaire

| Champ | Valeur |
|-------|--------|
| **Nom** | Alerte sanitaire |
| **Définition** | Avertissement déclenché automatiquement ou manuellement lorsqu'un indicateur de surveillance dépasse un seuil prédéfini. L'alerte est une action opérationnelle qui découlent de la notification ; elle vise à mobiliser rapidement les acteurs compétents pour la riposte. |
| **Type** | Événement opérationnel |
| **Contraintes** | Indicateur déclencheur ; seuil franchi ; périmètre géographique concerné ; niveau d'urgence (1-4) ; destinataires ; statut (émise, acquittée, en cours de traitement) |
| **Rattachement** | CAP-06, CAP-11, VS-02, VS-04 |
| **Référentiel source** | FHIR Communication (priority: urgent), DHIS2 alerts |

---

## 6. Exploitation & gestion

### E-01 — Formation sanitaire

| Champ | Valeur |
|-------|--------|
| **Nom** | Formation sanitaire |
| **Définition** | Toute structure de soins publique, privée, confessionnelle ou communautaire identifiée de manière unique dans le référentiel national des formations sanitaires. C'est l'unité de base du réseau de soins. |
| **Type** | Entité référentielle |
| **Contraintes** | Code unique (selon INSTAT) ; dénomination officielle ; type (hôpital, centre de santé, case de santé) ; niveau de qualification ; statut (actif, fermé, en construction) |
| **Rattachement** | CAP-05, CAP-14, TOUS les VS |
| **Référentiel source** | Référentiel des formations sanitaires (CAESN) |

### E-02 — Agent de santé

| Champ | Valeur |
|-------|--------|
| **Nom** | Agent de santé |
| **Définition** | Toute personne physique exerçant une activité de soins, de prévention ou de promotion de la santé dans une formation sanitaire, identifiée par son rôle, ses qualifications et son affectation. |
| **Type** | Entité |
| **Contraintes** | Identifiant unique ; nom ; qualification (médecin, infirmier, ACS, etc.) ; affectation (formation sanitaire, zone) ; statut (actif, inactif) |
| **Rattachement** | CAP-09, CAP-13, TOUS les VS |
| **Référentiel source** | Référentiel des agents de santé (CAESN) |

### E-03 — Indicateur sanitaire

| Champ | Valeur |
|-------|--------|
| **Nom** | Indicateur sanitaire |
| **Définition** | Mesure standardisée d'une performance, d'un résultat ou d'un processus dans le domaine de la santé. Chaque indicateur doit avoir une définition unique, stable et partagée, avec une méthodologie de calcul précise. |
| **Type** | Entité référentielle |
| **Contraintes** | Code unique ; nom ; définition ; méthodologie de calcul ; unité de mesure ; fréquence de collecte ; source de données |
| **Rattachement** | CAP-03, CAP-08, TOUS les VS |
| **Référentiel source** | Référentiel des indicateurs sanitaires (CAESN), DHIS2 |

### E-04 — Zone sanitaire

| Champ | Valeur |
|-------|--------|
| **Nom** | Zone sanitaire |
| **Définition** | Unité territoriale de planification et de coordination des services de santé, correspondant généralement à un district sanitaire. Elle regroupe les formations sanitaires et les zones de couverture d'une même aire de responsabilité. |
| **Type** | Entité spatiale |
| **Contraintes** | Code unique ; dénomination ; limites géographiques ; population ; chef-lieu ; formations sanitaires rattachées |
| **Rattachement** | CAP-05, CAP-14, TOUS les VS |
| **Référentiel source** | Référentiel géographique sanitaire (CAESN), INSTAT |

### E-05 — Tâche

| Champ | Valeur |
|-------|--------|
| **Nom** | Tâche |
| **Définition** | Unité de travail assignée à un acteur (personne ou système) dans le cadre d'un processus opérationnel : investigation terrain, campagne de vaccination, distribution d'intrants, visite de suivi. La tâche porte un statut, des échéances et une traçabilité complète d'exécution. |
| **Type** | Entité opérationnelle |
| **Contraintes** | Description de l'action ; assigné à (agent ou organisation) ; date d'échéance ; statut (à faire, en cours, terminée, annulée) ; résultat ; priorité |
| **Rattachement** | CAP-06, CAP-11, CAP-14, VS-01, VS-02 |
| **Référentiel source** | FHIR Task |

### E-06 — Tableau de bord

| Champ | Valeur |
|-------|--------|
| **Nom** | Tableau de bord |
| **Définition** | Vue consolidée et synthétique d'indicateurs de performance affichée aux décideurs à des fins de pilotage. Il agrège des données provenant de plusieurs sources (formations sanitaires, programmes, districts) et les présente sous forme graphique avec des seuils d'alerte. |
| **Type** | Entité de restitution |
| **Contraintes** | Indicateurs affichés ; périmètre géographique ; période ; fréquence de mise à jour ; niveau d'accès requis ; destinataires |
| **Rattachement** | CAP-08, CAP-16, VS-04 |
| **Référentiel source** | FHIR Dashboard (profil national), DHIS2 |

---

## 7. Interopérabilité transfrontalière & résumé patient

### T-01 — Résumé international du patient (IPS)

| Champ | Valeur |
|-------|--------|
| **Nom** | Résumé international du patient (International Patient Summary — IPS) |
| **Définition** | Document clinique structuré, minimal et non exhaustif, destiné à faciliter la continuité des soins lors d'un episode de soins transfrontalier. Conforme au standard HL7 IPS, il comprend les informations cliniques essentielles du patient : démographie, allergies, médicaments en cours, problèmes de santé, antécédents, vaccinations, résultats de diagnostic, dispositifs médicaux et procédures. Il est échangeable entre systèmes de santé de pays différents grâce aux profils FHIR IPS. |
| **Type** | Document structuré (FHIR Composition) |
| **Contraintes** | Conforme au profil HL7 FHIR IPS (hl7.org/fhir/uv/ips) ; langue obligatoire (français + anglais) ; sections minimales obligatoires (allergies, médicaments, problèmes) ; date d'émission et validité ; signature électronique du prestataire |
| **Rattachement** | CAP-INT-13 (interopérabilité transfrontalière), PT-14 (interopérabilité transfrontalière), CAP-17 (engagement patient), VS-01 (parcours patient) |
| **Référentiel source** | HL7 FHIR R4 — International Patient Summary (IPS) |

### T-02 — Section du résumé patient

| Champ | Valeur |
|-------|--------|
| **Nom** | Section du résumé patient |
| **Définition** | Unité structurée du résumé international du patient (IPS), regroupant une catégorie clinique spécifique. Chaque section est un objet FHIR autonome pouvant être échangé individuellement selon le principe de minimisation des données. |
| **Type** | Entité composite |
| **Contraintes** | Code de section conforme au ValueSet IPS (allergies, médicaments, problèmes, antécédents, vaccinations, résultats, dispositifs, procédures, observations vitales) ; contenu structuré selon les profils FHIR IPS ; section vide autorisée (« no known… ») |
| **Rattachement** | CAP-INT-13, PT-14, VS-01 |
| **Référentiel source** | HL7 FHIR R4 — IPS Sections |

#### Sections IPS obligatoires

| Code | Section | Ressource FHIR IPS | Contenu minimal |
|------|---------|---------------------|-----------------|
| **ALGY** | Allergies et intolérances | AllergyIntolerance | Substance, réaction, sévérité, statut |
| **MDCA** | Médicaments actuels | MedicationStatement | Produit, dosage, statut, indication |
| **PROB** | Problèmes de santé | Condition | Code CIM-10, onset, statut |
| **HIST** | Antécédents | Condition | Épisodes passés, résolus |
| **IMMU** | Vaccinations | Immunization | Vaccin, date, lot, statut |
| **VITAL** | Signes vitaux | Observation | Mesures (TA, FC, SpO2, température) |
| **LAB** | Résultats de diagnostic | Observation | Résultats laboratoire |
| **DEVI** | Dispositifs médicaux | DeviceUseStatement | Dispositif, date, statut |
| **PROC** | Procédures | Procedure | Acte, date, résultat |
| **IDOI** | Identité du patient | Patient | NIN, nom, naissance, sexe |

### T-03 — Confiance internationale

| Champ | Valeur |
|-------|--------|
| **Nom** | Confiance internationale (Trust Anchor) |
| **Définition** | Point d'ancrage de confiance numérique permettant la vérification mutuelle de l'identité et de la conformité des systèmes de santé échangeant des données transfrontalières. Conforme au GDHCN (Global Digital Health Certification Network), il garantit l'authenticité, l'intégrité et la non-répudiation des résumés patients échangés. |
| **Type** | Entité infrastructure |
| **Contraintes** | Certificat X.509v3 signé par l'autorité GDHCN nationale ; révocation en temps réel (CRL/OCSP) ; renouvellement avant expiration ; journalisation de toutes les vérifications |
| **Rattachement** | CAP-INT-13, PT-14, ART-7, CAP-15 |
| **Référentiel source** | GDHCN, ITU-T X.509 |

---

## Liens

- Chapitres et patterns de référence
- ART-2 — Médiation et normalisation
- ART-7 — Sécurité, contrôle d'accès et résidence
- PT-14 — Interopérabilité transfrontalière
- CAP-INT-13 — Interopérabilité transfrontalière
- CAESN — données
- CAESN — domaines de données
- CAESN — référentiels nationaux

## Références

- **matrice de lecture** — Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **chapitre ART-2 (médiation et normalisation)** — Médiation et normalisation (`referentiel/chapitres/art-2.md`)
- **F.2** — F.2 — Préservation de la souveraineté intersectorielle (`referentiel/fondations/f-2.md`)
- **F.3** — F.3 — Éradication des silos technologiques (`referentiel/fondations/f-3.md`)
- **CAESN** — Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) (`00_caesn/00_overview/index.md`)
- **Chapitres et patterns de référence** — Chapitres et patterns de référence (`02_artsn/03_chapitres/index.md`)
- **ART-2 — Médiation et normalisation** — Médiation et normalisation (`referentiel/chapitres/art-2.md`)
- **ART-7 — Sécurité, contrôle d'accès et résidence** — Sécurité, contrôle d'accès et résidence de la donnée (`referentiel/chapitres/art-7.md`)
- **PT-14 — Interopérabilité transfrontalière** — Interopérabilité transfrontalière (`03_ptisn/03_profils/pt-14-interopabilite-transfrontaliere.md`)
- **CAP-INT-13 — Interopérabilité transfrontalière** — Partie II — Capacités nationales requises (`01_cnisn/02_capacites/index.md`)
- **CAESN — données** — Architecture des données et de l'information sanitaire (`00_caesn/04_data/index.md`)
- **CAESN — domaines de données** — Domaines de données prioritaires (`00_caesn/04_data/domains.md`)
- **CAESN — référentiels nationaux** — Référentiels nationaux (`00_caesn/04_data/referentials.md`)
