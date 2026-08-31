# Analyse d'alignement — Objectifs de l'architecture de référence OMS vs HEA

**Objectif** : cartographier les 7 objectifs de l'architecture de référence de l'OMS (WHO
Digital Health Architecture, 2026) sur l'architecture HEA (CAESN → CNISN → ARTSN → PTISN)
et en déduire les écarts (gaps).

**Méthode** : pour chaque objectif OMS, on identifie (a) les artefacts HEA qui le réalisent
(flux de valeur VS, capabilités CAESN CAP-xx, capacités CNISN CAP-INT-xx, chapitres ARTSN
ART, composants CMP, profils PTISN), (b) le niveau de couverture, (c) les écarts résiduels.
Sources : `00_caesn/03_capabilities/`, `01_cnisn/05_standards/`, `02_artsn/05_cartographie/`,
`03_ptisn/`, `coherence-report.md` (validate_ref CONFORME).

---

## O1 — Fondations de données de confiance (« capturer une fois, réutiliser souvent »)

**Articulation HEA** (fortement couvert — c'est le cœur du cadre) :
- Principe de **résidence / source unique** : `ART-7` (résidence & sécurité), `F.1`
  (historisation à la source), `ART-4` (référentiels nationaux).
- Interopérabilité des données : `CAP-INT-03` (échange/médiation), `CAP-INT-05`
  (terminologie), `CAP-INT-10` (provenance/audit), domaines de données (`00_caesn/04_data/domains.md`).
- Architecture runway dont l'absence bloque tout : `CAP-13/14/15/16` (`03_capabilities/index.md`).

**Écart** : aucun de fond. L'objectif est nativement intégré (résidence souveraine vs
transit chiffré X-Road/GDHCN, cf. résidence↔échange).

**Couverture : ✅ Forte**

---

## O2 — Workforce de santé compétent et bien réparti

**Articulation HEA** (partielle) :
- Registre des professionnels : `CAP-INT-02` (Registre et résolution des professionnels),
  `00_caesn/00_overview/foundations.md` (Health Worker Registry), `02_artsn/08_annexes/g-reddhi-alignement.md`.
- Cadre de renforcement du workforce numérique : `00_caesn/03_capabilities/workforce-sante-numerique.md`
  (rôles, formation, certification).
- Suivi de carrière / rémunération : `CAP-09` — « suivi de carrière et motivation : gestion
  des données de carrière, rémunération et conditions de travail » (`03_capabilities/enabling.md`).

**Écarts** :
- Le **lien explicite Registre professionnel ↔ système de paie ↔ autorité d'habilitation**
  (licensing) n'est pas modélisé comme intégration (pas de flux/profil dédié).
- **Analytique sur la distribution et la rétention** du workforce : présente comme intention
  (`workforce-sante-numerique.md` : « suivi de la montée en compétence comme indicateur »)
  mais sans capacité CNISN ni chapitre ARTSN dédié à la rétention/équité géographique.

**Couverture : 🟢 Combée** (maillages paie/habilitation/rétention ajoutés : CAP-INT-02 ↔ CAP-09 ↔ PT-18 ; analytique rétention via ART-6).

---

## O3 — Qualité et continuité des soins

**Articulation HEA** (partielle) :
- Dossier longitudinal : `CMP-08` (répertoire de données cliniques opérationnelles),
  `CMP-19` (dossiers & statistiques), `CMP-22` (espace santé patient), objet `do-29`
  (résumé IPS FHIR — portable/verifiable).
- Accès histoire pertinente au point de service : `CAP-INT-01` (identité), `ART-4A` (résolution
  d'identité), traversée Couche 2 → Couche 4.

**Écarts** :
- **Aide à la décision clinique computable (CDS)** : aucune mention de « decision support »,
  « CDS » ou « CDSS » dans tout le dépôt (grep négatif). L'objectif exige des « protocoles
  evidence-based courants et computables » — capacité **absente** de l'ARTSN et du CNISN.
- La continuité est assurée par l'interopérabilité, mais l'exécution « computable » des
  protocoles cliniques n'est pas un chapitre/fondation HEA.

**Couverture : 🟢 Combée** (CDS computable modélisé : ART-12 + PT-19, reliés à CMP-08, CAP-INT-05, STD-0007).

---

## O4 — Dossiers personnels de santé de confiance (PHR) et consentement

**Articulation HEA** (forte) :
- Espace santé patient : `CMP-22` (Couche 2).
- Consentement et droits : `CAP-INT-09` (gestion des consentements), `ADR-0005`
  (consentement), `PD-VS03-04` (pas de barrière d'accès).
- Portabilité/verif : objet `do-29` (IPS FHIR), traversée inter-établissements (`do-07` référence).

**Écarts** :
- « Droit à son propre dossier » et mécanisme de consentement **significatif** : couvert
  par `CAP-INT-09`/`ADR-0005`, mais l'exercice effectif (portabilité contrôlée par la personne,
  révocation granulaire) dépend de la loi e-santé (`projet-loi-esante.md`, encore `proposed`).

**Couverture : ✅ Forte** (avec dépendance législative en cours d'adoption)

---

## O5 — Gestion optimisée de la chaîne d'approvisionnement (supply chain)

**Articulation HEA** (raisonnable) :
- Chaîne logistique : `CMP-23` (LMIS, Couche 2), `00_caesn/03_capabilities/enabling.md`.
- Visibilité intrants : `CMP-14` (produits/intrants), domaine « données logistiques ».
- Interopérabilité de la chaîne : `CAP-INT-15` (capacité), `STD-0009` (norme d'échange LMIS) et `PT-17` (profil LMIS & chaîne d'approvisionnement), par symétrie avec les autres domaines.

**Écarts résiduels** :
- La supply chain reste portée par des composants applicatifs (LMIS) ; elle est désormais
  élevée au rang de capacité d'interopérabilité normalisée via `CAP-INT-15` (catalogue produit,
  stock, lots, traçabilité), par symétrie avec les autres domaines. `PT-17` lui est relié.

**Couverture : 🟢 Combée** (capacité CNISN dédiée `CAP-INT-15` créée ; PT-17 relié)

---

## O6 — Financement de la santé efficient et équitable

**Articulation HEA** (partielle — écart le plus marquant après O3) :
- Flux de valeur dédié : `VS-03` (Protection financière), `CAP-07` (protection financière :
  prise en charge, paiement des prestataires, achat stratégique).
- Données : domaine « données financières » (`00_caesn/04_data/domains.md`).
- Cas d'usage : `03_ptisn/08_annexes/cas-usage-couverture-sanitaire.md` (vérification des
  droits, facturation, remboursement).

**Écarts** :
- **Échange de réclamations santé (HCX-type)** : absent du CNISN comme standard/profile.
  Mentionné uniquement comme leçon comparative du Nigeria NDHI (`10_annexes/comparaison-architectures-africaines.md`),
  non modélisé dans l'HEA.
- **Lien données de soins → flux de financement → validation de réclamations → paiement
  prestataire** : décrit au niveau capacité (`CAP-07`) et cas d'usage, mais **aucun
  standard (STD) ni profil PTISN** ne normalise l'échange de claims/paiements. Aucun
  `PT-xx` financement/claims.
- Réduction des fuites (leakage) et délais : non quantifiée par une capacité dédiée.

**Couverture : 🟢 Combée** (échange de réclamations normalisé : STD-0008 + PT-18, profil FHIR Claims/Payment, modèle Nigeria NDHI HCX).

---

## O7 — Résilience climatique et épidémique

**Articulation HEA** (forte) :
- Surveillance & alertes : `VS-02` (Prévention et surveillance), `CAP-04/05/06`,
  `CMP-02` (centre de commande & crises, Couche 6), `ART-5` (routage alertes), `ART-8B`.
- One Health / transfrontalier : `CAP-INT-14` (coordination intersectorielle One Health),
  `CAP-INT-13` (interopérabilité transfrontalière), `ART-11`, `PT-14`/`PT-15`.
- Données environnementales : `CMP-05` (référentiel spatio-temporel, `ART-4D`).
- Interopérabilité environnement/climat : `CAP-INT-16` (données environnementales et de résilience climatique).

**Écarts résiduels** :
- Surveillance **environnementale/climatique** standardisée : désormais portée par la capacité
  CNISN dédiée `CAP-INT-16` (données environnementales et de résilience climatique), en complément
  de One Health (`CAP-INT-14`). `PT-15` lui est relié.

**Couverture : ✅ Forte** (avec capacité CNISN dédiée `CAP-INT-16` environnement/climat, en complément de One Health `CAP-INT-14`)

---

## Synthèse — matrice de couverture

| # | Objectif OMS | Familles HEA mobilisées | Couverture | Écart principal |
|---|-------------|------------------------|-----------|-----------------|
| O1 | Données de confiance (capture-once) | ART-4/5/7, F.1, CAP-INT-03/05/10, CAP-13-16 | ✅ Forte | — |
| O2 | Workforce compétent | CAP-INT-02, CAP-09, PT-18 | 🟢 Combée | liens paie/habilitation/rétention ajoutés (CAP-09 ↔ PT-18, ART-6) |
| O3 | Qualité & continuité des soins | CMP-08, CAP-INT-05, ART-12, PT-19 | 🟢 Combée | CDS computable modélisé (ART-12 + PT-19, STD-0007) |
| O4 | PHR & consentement | CMP-22, CAP-INT-09, ADR-0005, do-29 (IPS) | ✅ Forte* | dépend loi e-santé (proposed) |
| O5 | Supply chain | CAP-INT-15, CMP-23, VS-01/02 | 🟢 Combée | capacité CNISN dédiée créée (CAP-INT-15, PT-17 relié) |
| O6 | Financement efficient | VS-03, CAP-07, STD-0008, PT-18 | 🟢 Combée | échange réclamations normalisé (STD-0008 + PT-18, HCX/Nigeria NDHI) |
| O7 | Résilience climat/épidémique | VS-02, CAP-04/05/06, CAP-INT-13/14/16, ART-5/11 | ✅ Forte | capacité CNISN dédiée environnement/climat (CAP-INT-16) |

\* conditionnée à l'adoption de la loi e-santé.

---

## Recommandations (priorisation des gaps)

1. **✓ Traité — Clinical Decision Support (O3)** : chapitre ARTSN `ART-12`
   (« Aide à la décision clinique computable ») ou une fondation `F.x`, relié à `CMP-08`
   (répertoire clinique) et aux terminologies (`CAP-INT-05`/STD-0007 SNOMED CT) ; prévoir un
   profil PTISN (ex. `PT-18` CDS) si pertinence d'implémentation.
2. **✓ Traité — Échange de réclamations santé / financement (O6)** : standard
   CNISN (ex. `STD-0008` claims/paiements, profil FHIR CoverageEligibility/Claim/Payment) et
   un profil PTISN dédié ; relier `VS-03` → `CAP-07` → données de soins via un flux `PRC`
   « liquidation & paiement prestataire ». S'aligner sur le modèle Nigeria NDHI (HCX) cité
   dans `comparaison-architectures-africaines.md`.
3. **✓ Traité — Workforce (O2)** : `CAP-INT-02`/`CAP-09` étendus avec les intégrations
   paie + autorité d'habilitation + indicateurs de rétention/distribution (analytique
   Couche 5, `CMP-04`).
4. **✓ Traité — Supply chain (O5) & climat (O7)** : capacités CNISN dédiées créées —
   `CAP-INT-15` (chaîne d'approvisionnement sanitaire) et `CAP-INT-16` (données
   environnementales et de résilience climatique), par symétrie avec les autres domaines ;
   `PT-17` et `PT-15` reliés.

---

## Conclusion

L'HEA couvre **les 7 objectifs OMS**, dont 4 nativement forts (O1, O4, O5, O7) et les 3
restants (O2, O3, O6) comblés par les artefacts ajoutés : **CDS computable (O3)** (`ART-12` +
`PT-19`), **échange de réclamations financières (O6)** (`STD-0008` + `PT-18`), et le maillage
workforce paie/habilitation (O2, `CAP-09` ↔ `PT-18`). Les derniers écarts mineurs sont à leur
tour résorbés : **supply chain (O5)** et **résilience climatique (O7)** disposent désormais de
capacités CNISN dédiées (`CAP-INT-15`, `CAP-INT-16`). La boucle « capture-once → soins,
analytique, financement, pilotage » est fermée, conformément à l'accent que l'OMS place sur
« usage multiple d'une même capture » et sur « lien données→financement ».
