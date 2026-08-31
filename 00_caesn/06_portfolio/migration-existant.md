---

title: "Plan de migration : De l'existant au futur état"
id: caesn-migration
domain: 06_portfolio
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: ["caesn", "portfolio", "migration", "transition", "niveau-1"]
---

# Plan de migration : De l'existant au futur état

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle.

---

## Objectif

Ce document décrit la stratégie et les étapes concrètes pour passer de l'état actuel du système d'information sanitaire national à l'architecture cible HEA. Il identifie les systèmes existants, les risques de migration et les plans d'action par phase.

---

## 1. État actuel : Inventaire des systèmes existants

### 1.1 Systèmes en production

| Système | Propriétaire | Technologie | Données gérées | Statut | Risque d'obsolescence |
|---------|-------------|-------------|----------------|--------|----------------------|
| **DHIS2** | MoS / OMS | Web (PHP/MySQL) | Indicateurs, rapports, dashboards | Actif, utilisé nationwide | Faible : standard mondial |
| **LMIS** (eLMIS) | MoS / USAID | Web (Java/PostgreSQL) | Stocks produits de santé | Actif dans certains districts | Moyen : dépendance fournisseur |
| **OpenMRS** | CHW / ONG | Web (Java/MySQL) | Dossiers patients (programmes ciblés) | Actif (programmes VIH, TB) | Moyen : données fragmentées |
| **Systèmes locaux** (Excel, Access) | Formations sanitaires | Hétérogène | Données cliniques, stocks | Très utilisé | Élevé : pas d'interopérabilité |
| **Registres papier** | Agents communautaires | Papier | Signaux, visites, vaccinations | Majoritaire en rural | Élevé : perte de données |
| **SMS-based** (mHealth) | Programmes divers | SMS / USSD | Notifications, rappels | Actif (BPC, vaccination) | Moyen : limited data |
| **PaySim / systèmes paiement** | BNP / opérateurs mobile | Mobile money | Transactions financières | Actif | Faible : infrastructure existante |

### 1.2 Données existantes : Volume et qualité

| Source | Volume estimé | Qualité | Interopérabilité actuelle |
|--------|---------------|---------|---------------------------|
| DHIS2 | ~50 000 rapports/an | Moyenne | Export Excel/CSV |
| LMIS | ~200 000 mouvements/an | Moyenne | API limitée |
| OpenMRS | ~500 000 patients (programmes) | Bonne (dans les programmes) | FHIR partiel |
| Systèmes locaux | ~1M de patients (estimation) | Faible | Aucune |
| Registres papier | ~2M de consultations/an | Variable | Aucune |

### 1.3 Gap analysis : Écart entre existant et cible

| Dimension | État actuel | État cible (HEA) | Écart |
|-----------|-------------|-------------------|-------|
| **Identité patient** | Fragmentée (programmes) | INP unique national | Critique : aucun ID partagé |
| **Échange de données** | Excel, email, papier | FHIR R4 via X-Road | Critique : aucune interopérabilité |
| **Terminologie** | Codes locaux hétérogènes | CIM-11, LOINC standardisés | Élevé : mappings inexistants |
| **Consentement** | Non formalisé | FHIR Consent structuré | Élevé : cadre juridique absent |
| **Traçabilité** | Partielle (DHIS2) | Audit trail complet | Élevé : pas de piste d'audit |
| **Sécurité** | Auth basique / mots de passe | OAuth 2.0, RBAC, chiffrement | Critique : failles de sécurité |
| **Données agrégées** | DHIS2 (isolé) | mADX normalisé | Moyen : DHIS2 fonctionne mais non intégré |
| **Transfrontalier** | Aucun | IPS + GDHCN | Critique : zéro infrastructure |

---

## 2. Stratégie de migration

### 2.1 Principes directeurs

1. **Migration progressive** : pas de Big Bang, passage par étapes avec validation intermédiaire
2. **Coexistence** : l'ancien et le nouveau fonctionnent en parallèle pendant la transition
3. **Priorité données** : la migration des données passe avant la migration des applications
4. **Zéro perte** : aucune donnée patient ne doit être perdue pendant la migration
5. **Retour arrière possible** : chaque phase doit permettre de revenir à l'état précédent si échec

### 2.2 Modèle de migration

```
┌─────────────────────────────────────────────────────────────┐
│                    PHASE DE MIGRATION                       │
│                                                             │
│  État actuel ──── Coexistence ──── Basculage ──── Nouveau  │
│  (legacy)        (parallèle)      (cutover)     état       │
│                                                             │
│  1. Inventaire   4. Validation    7. Basculage  10. Décommission │
│  2. Analyse gaps 5. Test intégr.  8. Vérification 11. Archives │
│  3. Conception   6. Formation     9. Monitoring  12. Amélioration │
└─────────────────────────────────────────────────────────────┘
```

### 2.3 Approche par couche

| Couche | Approche | Priorité |
|--------|----------|----------|
| **Données** | Copie → normalisation → validation → bascule | 1 (haute) |
| **Identité** | INP dédié → mappage existant → consolidation | 1 (haute) |
| **Échange** | X-Road déployé → connecteurs legacy → remplacement | 2 (moyenne) |
| **Applications** | Nouveaux modules → parallèle → remplacement progressif | 3 (standard) |
| **Gouvernance** | Nouvelles instances → formation → transfert responsabilités | 2 (moyenne) |

---

## 3. Plan de migration par phase

### Phase 1 : Fondations (T4 2026 : T1 2027)

| Action | Système impacté | Livrable | Risque |
|--------|-----------------|----------|--------|
| Déployer X-Road (Security Server) | Aucun (infra nouvelle) | X-Road opérationnel | Faible |
| Créer l'INP (référentiel patients) | OpenMRS + DHIS2 | INP avec 500K patients migrés | Élevé : qualité données |
| Mettre en place le registre formations | DHIS2 +LMIS | Registre national formations | Moyen |
| Déployer PT-10 (confiance/auth) | Aucun (infra nouvelle) | RBAC fonctionnel | Faible |
| Pilote référence (2 districts) | OpenMRS + système local | ServiceRequest FHIR opérationnel | Moyen : adoption |

**Critère de succès Phase 1** : INP fonctionnel, X-Road opérationnel, 2 districts pilotes interconnectés.

### Phase 2 : Interopérabilité nationale (T1 2027 : T2 2027)

| Action | Système impacté | Livrable | Risque |
|--------|-----------------|----------|--------|
| Connecter OpenMRS à X-Road | OpenMRS | Échange FHIR via X-Road | Moyen : API OpenMRS |
| Mapper terminologie (CIM-11, LOINC) | Systèmes locaux | Référentiel terminologique | Élevé : travail manuel |
| Déployer PT-02 (médiation) | Systèmes locaux | Connecteurs de transformation | Élevé : hétérogénéité |
| Étendre référence à 10 districts | Systèmes locaux | 10 districts interconnectés | Moyen |
| Déployer PT-12 (audit) | Tous | Piste d'audit complète | Faible |

**Critère de succès Phase 2** : 10 districts échangeant des données via FHIR, audit trail actif.

### Phase 3 : Couverture et programme (T2 2027 : T3 2027)

| Action | Système impacté | Livrable | Risque |
|--------|-----------------|----------|--------|
| Intégrer LMIS au X-Road | LMIS | Échange produits/stocks FHIR | Moyen |
| Connecter BPC/AMM à l'INP | Systèmes BPC/AMM | Éligibilité temps réel | Élevé : juridique |
| Déployer PT-04 (identité nationale) | Tous | NIN utilisable partout | Moyen |
| Étendre à 20 districts | Systèmes locaux | 20 districts | Moyen |
| Déployer PT-11 (consentement) | Tous | Consentement structuré | Moyen : adoption |

**Critère de succès Phase 3** : Vérification d'éligibilité temps réel, 20 districts connectés.

### Phase 4 : Surveillance et pilotage (T3 2027 : T4 2027)

| Action | Système impacté | Livrable | Risque |
|--------|-----------------|----------|--------|
| Intégrer DHIS2 au X-Road | DHIS2 | Données agrégées via mADX | Faible |
| Déployer PT-08 (données agrégées) | DHIS2 | Échange mADX normalisé | Faible |
| Déployer PT-09 (analytique) | DHIS2 + moteur analytique | Dashboards temps réel | Moyen |
| Connecter EVIPNet | EVIPNet | Signal épidémique → alerte | Moyen |
| Étendre à 40 districts | Tous | 40 districts | Moyen |

**Critère de succès Phase 4** : Dashboard national temps réel, alerte épidémique < 15min.

### Phase 5 : Transfrontalier (T4 2027 : T2 2028)

| Action | Système impacté | Livrable | Risque |
|--------|-----------------|----------|--------|
| Déployer GDHCN (Trust Anchor) | Aucun (infra nouvelle) | Certificat GDHCN national | Moyen |
| Implémenter PT-14 | Tous | IPS échangeable | Élevé : complexité |
| Connecter pays partenaires (SADC) | Systèmes voisins | Échange IPS transfrontalier | Élevé : accords bilatéraux |
| Déployer PT-15 (One Health) | OIE, FAO, OMS | Surveillance zoonose | Élevé : multi-acteurs |
| Décommissionner systèmes legacy | Systèmes obsolètes | Migration complète | Élevé : résistance |

**Critère de succès Phase 5** : Premier échange IPS transfrontalier réussi, GDHCN opérationnel.

---

## 4. Gestion des risques de migration

### 4.1 Risques identifiés

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| **Perte de données** pendant migration | Faible | Critique | Backup complet avant chaque phase, validation checksum |
| **Résistance au changement** des utilisateurs | Élevée | Élevé | Formation, accompagnement, champions métier |
| **Incompatibilité** avec systèmes legacy | Moyenne | Élevé | Tests d'intégration exhaustifs, mode dégradé |
| **Dépassement budget** | Moyenne | Moyen | Reserve de 20%, priorisation stricte |
| **Dépassement délais** | Élevée | Moyen | Planning conservateur, jalons intermédiaires |
| **Faille sécurité** pendant transition | Faible | Critique | Audit sécurité par phase, chiffrement permanent |
| **Non-conformité** réglementaire | Faible | Élevé | Veille juridique continue, ADRs documentées |

### 4.2 Plan de contingence

| Scénario | Action de contingence |
|----------|----------------------|
| Échec pilote Phase 1 | Retour à l'ancien système, analyse causes, correction, relance |
| Données corrompues | Restauration backup, vérification intégrité, re-migration |
| Rejet utilisateurs | Renforcement formation, simplification interface, champions locaux |
| Faille sécurité | Isolation immédiate, audit forensique, correction, notification |
| Indisponibilité X-Road | Mode dégradé (API directe), rétablissement prioritaire |

---

## 5. Indicateurs de suivi de la migration

| Indicateur | Cible Phase 1 | Cible Phase 3 | Cible Phase 5 |
|------------|----------------|----------------|----------------|
| Nombre de systèmes connectés à X-Road | 2 | 10 | Tous |
| Patients dans l'INP | 500 000 | 2 000 000 | 5 000 000 |
| Districts interconnectés | 2 | 20 | Tous (114) |
| Transactions FHIR / jour | 100 | 10 000 | 100 000 |
| Taux d'adoption utilisateurs | 20% | 60% | 90% |
| Disponibilité plateforme | 95% | 99% | 99,9% |
| Temps moyen réponse API | < 3s | < 2s | < 1s |
| Incidents sécurité / mois | < 5 | < 2 | 0 |

---

## 6. Gouvernance de la migration

### 6.1 Instance de pilotage

| Rôle | Responsabilité | Fréquence |
|------|----------------|-----------|
| **Comité de pilotage migration** | Décisions stratégiques, arbitrages | Mensuelle |
| **Chef de projet migration** | Coordination opérationnelle, jalons | Hebdomadaire |
| **Comité technique** | Validation intégration, tests | Bi-hebdomadaire |
| **Responsable données** | Qualité, intégrité, sécurité données | Quotidienne |
| **Responsable formation** | Accompagnement utilisateurs | Continue |

### 6.2 Matrice RACI migration

| Activité | Direction | DEPSI | Techniques | Partenaires |
|----------|-----------|-------|------------|-------------|
| Décision de migration | **A** | R | C | I |
| Conception technique | I | **A** | R | C |
| Déploiement infrastructure | I | C | **A** | R |
| Migration données | C | **A** | R | I |
| Tests intégration | I | **A** | R | C |
| Formation utilisateurs | C | **A** | R | R |
| Communication changement | **A** | R | I | I |

*Légende : R = Responsible · A = Accountable · C = Consulted · I = Informed*

---

## Liens

- Portefeuille d'initiatives
- Feuille de route ARTSN
- Trajectoire CNISN
- Protocole de test

## Références

- **Portefeuille d'initiatives** : Portefeuille d'initiatives orienté valeur (`00_caesn/06_portfolio/index.md`)
- **Feuille de route ARTSN** : Feuille de route de déploiement progressif de l'ARTSN (`02_artsn/07_lots/index.md`)
- **Trajectoire CNISN** : Partie V : Trajectoire de mise en œuvre (`01_cnisn/05_trajectoire/index.md`)
- **Protocole de test** : Annexe D : Protocole de test d'interopérabilité (`02_artsn/08_annexes/d-protocole-test-interopabilite.md`)
