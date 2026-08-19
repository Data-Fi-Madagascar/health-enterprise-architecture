---
title: Comparaison des architectures de santé numérique africaines
id: annexe-comparaison-architectures-africaines
domain: 10_annexes
version: "1.0.0"
status: draft
last_reviewed: 2026-08-19
owner: Bureau de Réalisation de la Valeur
tags: [annexes, comparaison, afrique, veille-strategique]
---

# Comparaison des architectures de santé numérique africaines

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## 1. Objectif et périmètre

Cette annexe de veille stratégique positionne le Cadre d'Architecture d'Entreprise de la Santé Numérique du Madagascar (HEA) par rapport aux architectures nationales et régionales de douze pays africains et de cinq cadres institutionnels panafricains.

L'analyse poursuit trois objectifs : identifier les bonnes pratiques transférables, mesurer l'avance ou le retard relatif du Madagascar, et alimenter les décisions du Comité National d'Architecture Santé Numérique (CNASN) en matière de priorisation et de dérogation.

Le périmètre couvre les dimensions suivantes : hiérarchie documentaire, gouvernance, standards d'interopérabilité, modèle en couches, identité patient, législation et maturité selon le Global Digital Health Monitor (GDHM) de l'OMS.

La méthodologie combine l'analyse documentaire des stratégies nationales, les évaluations GDHM 2023-2025, les fiches de profils OpenHIE, la littérature scientifique (BMC, JMIR, PLOS Digital Health) et les guides de l'Africa CDC.

## 2. Cadres régionaux

### 2.1 Union Africaine / Africa CDC

L'Africa CDC a publié en 2023 les *AU Health Information Exchange Guidelines and Standards*, validés dans les cinq régions lors d'ateliers tenus au Sénégal, au Congo-Brazzaville, au Rwanda, en Namibie et en Mauritanie. Ces directives définissent trois sections : orientations politiques pour l'échange d'informations de santé, standards d'interopérabilité et cas d'usage d'implémentation. Elles sont disponibles en anglais, français, portugais et arabe.

L'outil HIEMAT (*Health Information Exchange Maturity Assessment Toolkit*) évalue la maturité des échanges transfrontaliers selon quatre domaines : leadership et gouvernance, workforce et management, infrastructure TIC, standards et interopérabilité.

Pour Madagascar, les directives de l'Africa CDC fournissent le cadre normatif de référence pour le profil PT-14 (interopérabilité transfrontalière) et les accords bilatéraux de partage de données sanitaires.

### 2.2 WHO Région Afrique

La Stratégie mondiale prolongée sur la santé numérique dans la Région africaine de l'OMS, étendue à 2027, fixe des cibles mesurables : 80 % des États membres avec des stratégies de santé numérique (atteint : 38/47 = 81 %), 80 % formés en gouvernance numérique de la santé (17/47 = 36 %), 60 % avec un inventaire numérique réalisé (3 pays) et 50 % avec une architecture nationale développée et chiffrée.

Le GDHM 2023-2025 a évalué 32 pays de la région AFRO : aucun en phase 1 (naissante), 6 en phase 2 (émergente), 21 en phase 3 (établie) et 5 en phase 4 (avancée). Le domaine le plus fort est le leadership et la gouvernance (score moyen phase 3,75), tandis que le workforce reste le domaine le plus faible de manière persistante.

Le Regional Health Data Hub, en développement depuis 2025, vise une plateforme cloud interopérable avec les systèmes de données nationaux, avec une opérationnalisation complète prévue en 2030.

### 2.3 Smart Africa

Le Smart Africa Digital Health Blueprint (2025) propose une vision de marché unique de la santé numérique à l'échelle continentale, portée par le Rwanda comme pays champion du Digital Health Flagship Project. La plateforme technologique repose sur six composants : infrastructure de connectivité et technologies, infrastructure publique numérique fondamentale (identité, paiement, données), plateforme de santé numérique (services partagés), applications et systèmes de santé numérique, échange d'informations de santé au niveau continental et marché de l'industrie de la santé.

Cette initiative couvre plus de 40 États membres africains représentant plus d'un milliard d'habitants. Elle constitue le cadre de référence pour les échanges transfrontaliers que Madagascar intègre dans son profil PT-14.

### 2.4 ECOWAS / WAHO

La West African Health Organization (WAHO) soutient la coordination régionale des échanges d'informations de santé, avec des ateliers de validation des directives de l'UA au Sénégal et des évaluations régionales. Les pays actifs dans le cadre ECOWAS incluent le Ghana, le Nigeria, le Sénégal, le Mali, le Burkina Faso et la Côte d'Ivoire. WAHO facilite l'intégration de la surveillance transfrontalière des maladies et la harmonisation des standards régionaux.

Pour Madagascar, membre de la SADC et non de l'ECOWAS, l'intérêt principal réside dans les modèles francophones de gouvernance et d'interopérabilité développés au Sénégal et au Burkina Faso.

### 2.5 EAC / ECSA

L'East, Central and Southern Africa Health Community (ECSA) soutient la coordination régionale en Afrique de l'Est, avec des ateliers de validation des directives de l'UA au Rwanda, des pilotes d'échange de données transfrontalières et un partage d'expériences sur les implémentations OpenHIE. La Tanzanie, l'Ouganda, le Kenya et le Rwanda sont les pays les plus actifs de cette région.

Le modèle de la Tanzanie (Health Information Mediator) et celui du Kenya (Enterprise Service Bus) fournissent des références techniques directes pour l'implémentation du PT-02 (médiation intra-secteur).

## 3. Analyses pays

### 3.1 Rwanda

**Architecture :** Le Rwanda a lancé en 2025 le National Health Intelligence Center (NHIC) avec une architecture digitale à six couches : couche source, transformation des données, réplication, entrepôt de données, stockage et présentation. Cette architecture intègre DHIS2, eBuzima, CRVS, eLMIS et HWMS sous un identifiant national unique.

**Standards :** HL7 FHIR (en développement), DHIS2, OpenMRS. Le numéro d'identification nationale sert d'identifiant patient unique.

**Gouvernance :** Ministère de la Santé, avec un rôle de champion via le Smart Africa Digital Health Flagship Project pour les échanges transfrontaliers.

**Maturité GDHM :** Phase 4 — l'un des pays les plus avancés d'Afrique.

**Leçons pour Madagascar :** L'intégration de l'identifiant national unique dans le flux de données sanitaires est un modèle à suivre pour le développement de l'INP. Le modèle NHIC à six couches présente des similitudes avec la cartographie ARTSN à six couches, mais sans la séparation stricte entre couche 3 (échange sans logique métier) et couche 4 (interopérabilité avec registres).

### 3.2 Kenya

**Architecture :** Le Kenya Health Enterprise Architecture (KHEA) repose sur un Enterprise Service Bus (ESB) reliant les systèmes au niveau national et comtal. Les ressources partagées incluent le registre des patients, le registre des établissements, le registre des travailleurs de santé, le catalogue de produits, la couche d'interopérabilité et les dossiers de santé partagés. Le Digital Health Act 2023 a établi une Digital Health Agency avec un cadre réglementaire complet.

**Standards :** ICD-10, SNOMED-CT (terminologie), HL7 v2 (messagerie), HL7 CDA (résumés cliniques), ISO/TS 22220 (démographie patient), HL7 FHIR (en adoption).

**Gouvernance :** Digital Health Agency sous le Digital Health Act 2023, avec structure décentralisée (politique nationale, implémentation comtale).

**Maturité GDHM :** Phase 4 — avancée de deux phases en une seule année suivant l'adoption du Digital Health Act.

**Leçons pour Madagascar :** Le Digital Health Act 2023 démontre qu'une législation contraignante accélère significativement la maturité. Le modèle ESB du KHEA est directement comparable au PT-02 (médiation intra-secteur) mais la séparation des responsabilités entre médiation et orchestration (PT-16) est plus explicite dans l'HEA.

### 3.3 Ghana

**Architecture :** Le Ghana Health Service Enterprise Architecture combine DHIS2 (DHIMS-2) comme référentiel national central avec le Ghana Health Information Management System (GHIMS) et un e-Government Interoperability Framework (version 2, 2022). L'architecture d'entreprise a été formalisée dès 2009, mais l'interopérabilité pratique reste limitée à des échanges partiels ou unidirectionnels.

**Standards :** HL7, FHIR (pilotes), ICD-10.

**Gouvernance :** Fragmentée entre plusieurs institutions. Aucun organisme unique n'exerce une tutelle complète. L'unité ICT du Ghana Health Service gère 16 responsables régionaux.

**Maturité GDHM :** Phase 3 — adopteur précoce mais écosystème fragmenté.

**Leçons pour Madagascar :** Le Ghana illustre le risque de fragmentation lorsque la gouvernance n'est pas centralisée. L'HEA évite ce piège grâce au CNASN comme autorité unique de cohérence architecturale. Les plateformes parallèles et les systèmes pilotés par des bailleurs qui contournent les standards nationaux sont un risque identique pour Madagascar.

### 3.4 Afrique du Sud

**Architecture :** Le Health Normative Standards Framework (HNSF) 2021 constitue le cadre le plus complet d'Afrique. Il comprend un Master Patient Index basé sur le numéro d'identité nationale, un Health Patient Registration System, un National Data Dictionary, des registres de facilities, des dépôts cliniques partagés et une couche d'interopérabilité HIE. Le programme de tests de conformité CSIR est obligatoire pour tous les systèmes d'information de santé.

**Standards :** HL7 v3 RIM, ISO 13606/OpenEHR, profils IHE, HL7 FHIR, HL7 CDA/CCD, DICOM, ICD-10, LOINC, ISO 22220, ISO/TR 20514, profils IHE.

**Gouvernance :** Department of Health national, National eHealth Standards Board, alignement avec le South African Bureau of Standards (SABS). Le HNSF est publié sous le National Health Act — législation contraignante.

**Maturité GDHM :** Avancée — fréquemment citée pour la maturité réglementaire. MomConnect démontre l'interopérabilité structurelle.

**Leçons pour Madagascar :** Le HNSF est la référence normative la plus aboutie du continent. Le modèle de tests de conformité CSIR est un objectif à moyen terme pour le PTISN. La législation contraignante (National Health Act) est un facteur clé de succès absent de Madagascar.

### 3.5 Tanzanie

**Architecture :** La Tanzania Health Enterprise Architecture (TZHEA) définit quatre domaines (Business, Data, Applications, Technology) avec un Health Information Mediator (HIM) comme couche d'interopérabilité middleware. La plateforme HEALTHeLINK, open-source, connecte plus de 15 systèmes d'information de santé à travers cinq domaines : gestion hospitalière, mHealth, HMIS, vaccination et logistique. Le cadre Mind the GAPS (Governance, Architecture, Program Management, Standards) + Capacity and Use structure l'approche.

**Standards :** HL7, profils IHE, standards ouverts via HEALTHeLINK.

**Gouvernance :** Ministère de la Santé, sous-comité TZHEA établi par la National Digital Health Strategy 2019-2024.

**Maturité GDHM :** Phase 3 — l'un des premiers pays à appliquer une approche d'architecture d'entreprise aux systèmes d'information de santé.

**Leçons pour Madagascar :** Le HIM tanzanien est le modèle le plus directement comparable au PT-02 (médiation intra-secteur). La capacité à intégrer 14+ systèmes via un middleware démontre la faisabilité du modèle de médiation. La séparation entre médiation (HIM) et orchestration (non formalisée en Tanzanie) est plus explicite dans l'HEA avec PT-02 et PT-16.

### 3.6 Éthiopie

**Architecture :** L'eHealth Architecture (eHA), développée entre 2017 et 2019, définit une couche d'interopérabilité avec des services partagés. DHIS2 fonctionne comme eHMIS national dans plus de 30 000 établissements publics. Le Master Facility Registry, le National Health Data Dictionary et la stratégie Connected Woreda (chemin de maturité numérique par niveaux) complètent l'architecture. Le pilote HAPI FHIR + OpenHIM pour l'échange EMR-DHIS2 est en cours.

**Standards :** ICD-10, HL7 FHIR (pilote via HAPI FHIR), DHIS2.

**Gouvernance :** Ministère Fédéral de la Santé, cadre de gouvernance HIS avec structures nationales et régionales.

**Maturité GDHM :** DHIS2 au stade « défini » (score 2,81). L'eHA est établie mais l'interopérabilité n'est pas entièrement réalisée.

**Leçons pour Madagascar :** Le pilote HAPI FHIR + OpenHIM démontre la complémentarité des deux outils — exactement la distinction formalisée dans l'HEA entre PT-02 (OpenHIM pour la médiation) et PT-16 (OpenFN pour l'orchestration). L'absence de registre de patients et de programme d'ID nationale est un risque similaire pour Madagascar.

### 3.7 Nigeria

**Architecture :** Le Nigeria Digital Health Initiative (NDHI), lancé en mars 2024, repose sur trois composants : réseau de services de santé numériques interopérables, échange de réclamations santé (HCX) et échange d'informations de santé (HIE). Le Nigeria e-Government Interoperability Framework (Ne-GIF) basé sur TOGAF structure l'approche d'architecture d'entreprise avec une architecture orientée services (SOA).

**Standards :** Plus de 32 standards ISO/TC 215 en santé informatics adoptés en 2019, HL7, ICD-10, SNOMED-CT, Ne-GIF.

**Gouvernance :** Ministère de la Santé et du Bien-être Social, Comité de mise en œuvre du NDHI (20 personnes, multisectoriel), Digital Health Agency.

**Maturité GDHM :** Phase 3 — momentum important depuis le lancement du NDHI en 2024.

**Leçons pour Madagascar :** Le Nigeria démontre qu'un cadre législatif et institutionnel fort (comité multisectoriel de 20 personnes) peut accélérer la maturité en une seule année. L'adoption de 32+ standards ISO témoigne d'une ambition normalisatrice que Madagascar pourrait calibrer à son échelle.

### 3.8 Sénégal

**Architecture :** Le Plan Stratégique du Système d'Information Sanitaire 2022-2026 et la Stratégie Santé Digitale 2018-2023 structurent l'écosystème. DHIS2, déployé depuis 2014, s'est étendu à la surveillance épidémiologique, aux ressources humaines, à la chaîne d'approvisionnement, à la surveillance maternelle/périnatale et à l'état civil. Le Dossier Patient Informatisé (DPI) a été pilotedans deux hôpitaux, un centre de santé et un poste de santé, couvrant plus de 127 000 patients. Six projets phares ont été lancés en 2025 : DPI, télémédecine, SIH, SIGS, gestion numérique des médicaments et numérisation de la santé communautaire.

**Standards :** DHIS2, HL7 FHIR (interconnexion mHealth-DHIS2), standards ADIE de e-Government.

**Gouvernance :** CSSDOS (Cellule de la Carte sanitaire et sociale, de la Santé digitale et de l'Observatoire de la Santé) sous le Ministère de la Santé, Division du Système d'Information Sanitaire et Sociale.

**Budget :** 36 milliards FCFA (environ 58 millions USD) alloués à la numérisation de la santé.

**Leçons pour Madagascar :** Le Sénégal est le pays francophone le plus comparable. Le modèle DPI (dossier patient informatisé) est un objectif direct pour les profils PT-04 (résolution d'identité) et PT-08 (pipeline d'ingestion analytique). Le budget dédié de 58 millions USD constitue un benchmark pour le financement nécessaire à Madagascar.

### 3.9 Burkina Faso

**Architecture :** L'Architecture Nationale de Santé Numérique comprend un Centre d'Intelligence pour la Santé, des registres nationaux en développement et un Référentiel Général d'Interopérabilité. Le DHIS2 est déployé à l'échelle nationale depuis 2013, faisant du Burkina Faso l'un des premiers pays d'Afrique de l'Ouest à cette échelle.

**Standards :** DHIS2, référentiel d'interopérabilité national, cadre de cybersécurité et protection des données.

**Gouvernance :** Ministère de la Santé via la Direction des Statistiques Sectorielles, stratégie nationale de santé numérique avec feuille de route IA.

**Maturité GDHM :** Milieu de parcours — précoce dans l'adoption de DHIS2, en développement de la gouvernance IA.

**Leçons pour Madagascar :** Le programme DHALP (*Digital Health Leadership Program*) de HELINA, actif au Burkina Faso, est un modèle de renforcement des capacités que Madagascar pourrait rejoindre. Le référentiel général d'interopérabilité est directement comparable au CNISN.

### 3.10 Côte d'Ivoire

**Architecture :** SIGSANTE (basé sur DHIS2) constitue l'épine dorsale du Système National d'Information Sanitaire depuis 2015. La plateforme mHealth TICANALYSE interconnecte les données communautaires avec DHIS2. La Direction de l'Informatique et de la Santé Digitale (DISD) coordonne les efforts. Six projets de numérisation de la santé communautaire ont été lancés.

**Standards :** HL7 FHIR, DHIS2, API sécurisées.

**Gouvernance :** DISD sous le Ministère de la Santé, Comité National d'Information Stratégique.

**Maturité GDHM :** Phase 4 pour l'interopérabilité — remarquable pour un pays en développement.

**Leçons pour Madagascar :** Le modèle mHealth-DHIS2 de la Côte d'Ivoire est une référence pour l'intégration des données communautaires (couche 2 de l'ARTSN). La maturité interopérabilité en phase 4 démontre que des pays à ressources limitées peuvent atteindre des niveaux élevés avec une gouvernance ciblée.

### 3.11 Ouganda

**Architecture :** Le Digital Health Enterprise Architecture Framework (DHEAF) est l'un des cadres d'architecture d'entreprise les plus documentés d'Afrique. Il repose sur sept building blocks : vision, objectifs, principes, processus, domaines (Business, Data, Application, Technology), architecture de sécurité et modèle d'échange d'informations de santé (HIEM). L'approche combine TOGAF 9.2 et IEEE 1471-2000. Cinq registres numérisés (patient, établissement, personnel, terminologie, dossiers partagés) alimentent une Enterprise Service Bus comme plateforme d'interopérabilité.

**Standards :** HL7 FHIR, OpenHIE, DHIS2, TOGAF 9.2.

**Gouvernance :** Ministère de la Santé, aligné avec le e-Government Interoperability Framework de NITA-U.

**Maturité GDHM :** Avancée — momentum important en interopérabilité.

**Leçons pour Madagascar :** Le DHEAF est le cadre le plus comparable à l'HEA en termes de structure documentaire (7 parties vs notre hiérarchie 4 niveaux). L'utilisation de TOGAF comme méthode sous-jacente est un point commun. La différence majeure reste la séparation stricte dans l'HEA entre les niveaux normatif (CAESN/CNISN) et technique (ARTSN/PTISN), absente du DHEAF.

### 3.12 Zambie

**Architecture :** La Digital Health Strategy 2022-2026 et l'Interoperability Architectural Framework (IAF, 2023) structurent l'approche. SmartCare, un EHR offline-first et scalable à l'échelle nationale, est déployé dans 116 districts. L'Integrated National Registration Information System (INRIS) fournit un identifiant patient unique.

**Standards :** HL7 FHIR, profils IHE, DHIS2, API REST sécurisées.

**Gouvernance :** Direction ICT du Ministère de la Santé, Groupe de travail technique sur la santé numérique avec Sous-comité Standards et Interopérabilité.

**Maturité GDHM :** Milieu de parcours — déploiement national de SmartCare en cours, HIE basée sur les standards en développement.

**Leçons pour Madagascar :** Le modèle SmartCare (offline-first) est directement pertinent pour les couches 1 et 2 de l'ARTSN (infrastructure et point de service). L'INRIS zambien est un modèle pour le développement de l'INP malgache.

## 4. Analyse comparative transversale

### 4.1 Hiérarchie documentaire

| Pays | Nombre de documents | Séparation normatif/technique | Format |
|------|--------------------|-------------------------------|--------|
| **Madagascar** | **4 niveaux** (CAESN/CNISN/ARTSN/PTISN) | **Oui — séparation stricte** | **Markdown as code** |
| Kenya | 1 KHEA + loi | Non | PDF |
| Tanzanie | TZHEA 4 domaines | Partielle | PDF |
| Ouganda | DHEAF 7 building blocks | Partielle | PDF |
| Afrique du Sud | HNSF + stratégie | Partielle | PDF + législation |
| Rwanda | NHIC 6 couches | Non | PDF |
| Sénégal | Plan SIS unique | Non | PDF |
| Nigeria | NDHI 3 composants | Non | PDF |
| Ghana | EA + eGov Framework | Non | PDF |
| Burkina Faso | Architecture + référentiel | Partielle | PDF |
| Côte d'Ivoire | SIGSANTE + DISD | Non | PDF |
| Zambie | Stratégie + IAF | Partielle | PDF |

L'HEA est la seule architecture africaine à formaliser une hiérarchie de quatre niveaux avec séparation stricte entre les niveaux normatif (pourquoi, garanties) et technique (comment, avec quoi). Cette séparation permet une indépendance relative entre les évolutions de standards et les choix de produits.

### 4.2 Gouvernance

| Pays | Instance centrale | Validation portfolio | Validation architecture | Législation contraignante |
|------|-------------------|---------------------|------------------------|--------------------------|
| **Madagascar** | **CNASN** | **Bureau de Réalisation de la Valeur** | **CNASN (homologation)** | **Non** |
| Kenya | Digital Health Agency | Unique | Unique | **Digital Health Act 2023** |
| Afrique du Sud | eHealth Standards Board | Unique | CSIR (conformité) | **National Health Act** |
| Tanzanie | Sous-comité TZHEA | Unique | Unique | Non |
| Ouganda | Ministry + NITA-U | Unique | Unique | Non |
| Rwanda | Ministry of Health | Unique | Unique | Non |
| Sénégal | CSSDOS | Unique | Unique | Non |
| Nigeria | NDHI Implementation Committee | Unique | Unique | En développement |
| Ghana | Multiples (fragmenté) | Non formalisé | Non formalisé | Non |
| Burkina Faso | Direction des Statistiques | Unique | Unique | Non |
| Côte d'Ivoire | DISD | Unique | Unique | Non |
| Zambie | TWG + Sous-comité | Unique | Unique | Non |

Le modèle de gouvernance double de Madagascar (portfolio + homologation) est unique en Afrique. Le Kenya et l'Afrique du Sud sont les seuls pays dotés d'une législation contraignante, facteur identifié comme critique de succès par le GDHM.

### 4.3 Standards d'interopérabilité

| Standard | Adoption Afrique | Madagascar | Kenya | SA | Rwanda | Tanzanie | Nigeria |
|----------|-----------------|------------|-------|-----|--------|----------|---------|
| DHIS2 | 46/47 pays | Référencé | ✓ | ✓ | ✓ | ✓ | ✓ |
| HL7 FHIR R4 | 6+ pays (pilote→national) | **Obligatoire** | ✓ | ✓ | ✓ | ○ | ✓ |
| X-Road | 3 pays | **Couche 3** | ○ | ○ | ○ | ○ | ○ |
| OpenHIE | 7 pays actifs | Référencé | ○ | ○ | ✓ | ✓ | ✓ |
| IHE Profiles | 3 pays | Référencé | ○ | ✓ | ○ | ✓ | ○ |
| mADX | Francophone | ✓ | ○ | ○ | ○ | ○ | ○ |
| CIM-10/LOINC | 10+ pays | ✓ | ✓ | ✓ | ○ | ○ | ✓ |
| SNOMED CT | 2-3 pays | ○ | ✓ | ✓ | ○ | ○ | ✓ |

Madagascar se positionne dans le tiers supérieur pour l'ambition normative (FHIR obligatoire, X-Road pour l'interinstitutionnel), avec une couverture standard plus large que la plupart des pays francophones.

### 4.4 Couches d'architecture

| Pays | Couches explicites | Couche transport sans logique métier | CQRS | Offline-first | Identity isolation (One Health) |
|------|-------------------|-------------------------------------|------|---------------|-------------------------------|
| **Madagascar** | **6 + 2 axes** | **Oui (Couche 3)** | **Oui (Couche 5)** | **Oui (Couche 2)** | **Oui** |
| Tanzanie | 4 domaines | Non | Non | Partiel | Non |
| Ouganda | 4 domaines + HIE | Non | Non | Partiel | Non |
| Kenya | Non structuré | N/A | Non | Non | Non |
| Afrique du Sud | HNSF (normatif) | Non | Non | Partiel | Non |
| Rwanda | 6 couches NHIC | Non | Non | Non | Non |
| Sénégal | Non structuré | N/A | Non | Non | Non |
| Nigeria | Non structuré | N/A | Non | Non | Non |
| Zambie | Non structuré | N/A | Non | Oui (SmartCare) | Non |

L'HEA est la seule architecture africaine à formaliser explicitement l'absence de logique métier dans la couche de transport (Couche 3), l'utilisation du pattern CQRS pour l'analytique (Couche 5) et l'isolation d'identité pour les échanges One Health.

### 4.5 Patient ID

| Pays | Identifiant patient | Statut | Modèle |
|------|-------------------|--------|--------|
| **Madagascar** | **INP** | **En construction** | **Fédéral (PIXm/PDQm)** |
| Rwanda | NIN national | Opérationnel | National unique |
| Kenya | Huduma Namba / NIIMS | En déploiement | National unique |
| Afrique du Sud | ID nationale | Opérationnel | National unique |
| Zambie | INRIS | En déploiement | National unique |
| Sénégal | DPI (pas d'ID unique) | Pilote | Sectoriel |
| Tanzanie | NIDA | Partiel | National |
| Nigeria | NIN / BVN | Partiel | National |
| Ghana | Ghana Card | En cours | National |
| Éthiopie | Aucun | Non démarré | N/A |
| Burkina Faso | Aucun | Non démarré | N/A |
| Côte d'Ivoire | Aucun | Non démarré | N/A |
| Ouganda | Uganda Card | En cours | National |

Madagascar, avec l'INP en construction, se positionne dans la moyenne africaine. Les pays les plus avancés (Rwanda, Afrique du Sud) ont un identifiant national opérationnel. L'absence d'ID unique en Éthiopie, au Burkina Faso et en Côte d'Ivoire illustre le risque que Madagascar doit éviter.

### 4.6 Législation

| Pays | Loi e-santé spécifique | Protection des données | Mandat d'interopérabilité |
|------|----------------------|----------------------|--------------------------|
| **Madagascar** | **Non** | **En développement** | **Non** |
| Kenya | **Digital Health Act 2023** | Data Protection Act 2019 | Oui |
| Afrique du Sud | **National Health Act** | POPIA | Oui |
| Nigeria | En développement | NDPR 2019 | En développement |
| Rwanda | Non | Loi protection données | Non |
| Tanzanie | Non | Electronic and Postal Communications | Non |
| Ghana | Non | Data Protection Act 2012 | Non |
| Sénégal | Non | Loi protection données 2008 | Non |
| Autres | Non | Variable | Non |

Le Kenya et l'Afrique du Sud sont les seuls pays dotés d'une législation e-santé contraignante. Madagascar fait partie de la majorité sans cadre législatif spécifique, ce qui constitue une faiblesse identifiée dans l'analyse SWOT.

### 4.7 Maturité GDHM (2023-2025)

| Phase | Pays |
|-------|------|
| **Phase 4 (Avancée)** | Rwanda, Kenya, Afrique du Sud, Tanzanie (estimé), Nigeria (estimé) |
| **Phase 3 (Établie)** | Ghana, Éthiopie, Sénégal, Burkina Faso, Côte d'Ivoire, Ouganda, Zambie + 14 autres |
| **Phase 2 (Émergente)** | 6 pays |
| **Phase 1 (Naissante)** | 0 pays |
| **Madagascar** | **Non évalué** |

Madagascar n'a pas encore été évalué par le GDHM. La réalisation d'une évaluation constitue une priorité pour benchmarking la maturité et identifier les domaines d'amélioration.

## 5. Positionnement HEA

### 5.1 Forces

L'architecture HEA présente des forces structurelles rares en Afrique. La hiérarchie documentaire à quatre niveaux (CAESN/CNISN/ARTSN/PTISN) est unique et permet une séparation claire entre les niveaux normatif et technique. Le format Markdown as code avec YAML frontmatter et traçabilité automatisée constitue un avantage significatif pour la maintenance et l'évolution du cadre.

La gouvernance double (portfolio + homologation) évite les biais de fragmentation. La couche 3 sans logique métier et le pattern CQRS en couche 5 sont des patterns d'architecture avancés, rarement formalisés dans les architectures africaines. Les 16 profils techniques (PT-01 à PT-16) fournissent un niveau de granularité d'implémentation absent des autres cadres continentaux.

L'intégration de l'interopérabilité One Health (PT-15) avec isolation d'identité et les échanges transfrontaliers via GDHCN (PT-14) positionnent Madagascar dans le tiers supérieur des architectures africaines pour la couverture fonctionnelle.

### 5.2 Faiblesses

L'absence de loi e-santé spécifique constitue la faiblesse la plus critique. Le Kenya et l'Afrique du Sud démontrent qu'une législation contraignante est un facteur d'accélération majeur. L'INP (identifiant patient national) est en construction mais pas encore opérationnel, ce qui retarde l'implémentation des profils PT-04 et PT-11.

L'absence de programme de tests de conformité (comme le CSIR en Afrique du Sud) signifie que l'homologation reste théorique. Le budget de numérisation de la santé n'est pas sécurisé, contrairement au Sénégal (58 millions USD) ou au Nigeria (NDHI budgeté). Enfin, Madagascar n'a pas encore été évalué par le GDHM, ce qui empêche tout benchmarking formel.

### 5.3 Opportunities

Le modèle DPI sénégalais (127 000 patients pilotes) fournit un chemin d'implémentation direct pour le dossier patient informatisé malgache. Le programme DHALP de HELINA, actif au Burkina Faso et au Rwanda, offre un cadre de renforcement des capacités que Madagascar pourrait rejoindre.

La plateforme SmartCare de la Zambie (offline-first, 116 districts) est une référence technique pour les couches 1 et 2 de l'ARTSN. Le modèle mHealth-DHIS2 de la Côte d'Ivoire démontre l'interopérabilité communautaire à moindre coût. Le pilote HAPI FHIR + OpenHIM de l'Éthiopie valide la complémentarité PT-02/PT-16.

Le cadre Smart Africa offre une opportunité de positionnement régional via le Digital Health Flagship Project, avec le Rwanda comme champion susceptible de soutenir l'intégration de Madagascar dans les échanges transfrontaliers.

### 5.4 Menaces

La fragmentation des systèmes, identifiée au Ghana et dans de nombreux pays, est un risque permanent si la gouvernance CNASN faiblit. Les systèmes pilotés par des bailleurs qui contournent les standards nationaux (constaté au Ghana, en Éthiopie) menacent la cohérence architecturale.

Le retard de législation laisse la porte ouverte à des initiatives parallèles non coordonnées. L'absence de budget sécurisé crée une dépendance vis-à-vis des financements internationaux, avec le risque de priorités alignées sur les bailleurs plutôt que sur la stratégie nationale. La concurrence des approches monolithiques (un seul document, un seul produit) peut apparaître plus simple à mettre en œuvre à court terme, au détriment de la robustesse architecturale à long terme.

## 6. Recommandations

### 6.1 Court terme (atelier Aug 24-30)

L'évaluation GDHM de Madagascar doit être initiée en priorité pour établir un baseline de maturité et identifier les écarts par rapport aux pays comparables. La présentation du cadre HEA lors de l'atelier de validation doit inclure la comparaison avec le Sénégal (contexte francophone comparable) et la Tanzanie (modèle HIM directement pertinent).

L'architecture comparative doit être intégrée aux supports de plaidoyer pour le financement, en s'appuyant sur le budget sénégalais de 58 millions USD comme benchmark. Le profil PT-16 (orchestration, OpenFN) doit être présenté comme une differentiation par rapport au modèle tanzanien (médiation seule).

### 6.2 Moyen terme (6 mois)

La préparation d'une proposition de loi e-santé s'inspirant du Digital Health Act kenyan 2023 doit être initiée, en identifiant les éléments transférables au contexte malgache. Le programme DHALP de HELINA doit être sollicité pour un programme de renforcement des capacités en architecture d'entreprise.

Un pilote d'interopérabilité transfrontalière avec la Tanzanie ou le Mozambique (membres SADC) doit être envisagé pour valider le profil PT-14. Le référentiel de conformité, inspiré du modèle CSIR sud-africain, doit être défini pour opérationnaliser l'homologation PTISN.

### 6.3 Long terme (2 ans)

L'adhésion au Smart Africa Digital Health Flagship Project doit être formalisée pour intégrer le réseau continental d'échanges transfrontaliers. Le développement de l'INP doit atteindre l'opérationalité pour permettre le déploiement des profils PT-04 et PT-11.

Un budget dédié à la numérisation de la santé, calibré sur les standards régionaux (Sénégal, Nigeria), doit être sécurisé dans la loi de finances. L'évaluation GDHM annuelle doit être institutionnalisée pour suivre la progression de la maturité.

## Références

- **Africa CDC** — AU Health Information Exchange Guidelines and Standards (2023)
- **WHO AFRO** — Framework for Implementing the Global Strategy on Digital Health in the WHO African Region (2021-2027)
- **Smart Africa** — Digital Health Blueprint (2025)
- **GDHM** — Global Digital Health Monitor 2023-2025, WHO
- **Kenya** — Digital Health Act 2023, Kenya Gazette Supplement
- **South Africa** — Health Normative Standards Framework 2021, National Department of Health
- **Tanzania** — Tanzania Health Enterprise Architecture, Ministry of Health (2019-2024)
- **Uganda** — Digital Health Enterprise Architecture Framework (DHEAF), Ministry of Health
- **Rwanda** — National Health Intelligence Center Architecture (2025), Ministry of Health
- **Sénégal** — Plan Stratégique du Système d'Information Sanitaire 2022-2026, CSSDOS
- **Nigeria** — Nigeria Digital Health Initiative Blueprint (2024), Federal Ministry of Health
- **OpenHIE** — Country Profiles, OpenHIE Wiki
- **HELINA** — Digital Health Leadership Program (DHALP), Health Informatics in Africa
- **BMC / JMIR / PLOS Digital Health** — Littérature scientifique sur les architectures de santé numérique africaines
