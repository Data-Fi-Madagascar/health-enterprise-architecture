---
title: "Méthode TCO et enveloppe de financement du portefeuille"
id: financement-tco
domain: 06_portfolio
version: "1.0.0"
status: draft
last_reviewed: 2026-08-26
owner: Bureau de Réalisation de la Valeur
tags: ["portefeuille", "financement", "tco", "investissement", "adhmat"]
---

# Méthode TCO et enveloppe de financement du portefeuille

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ◐ |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## Objet et lacune comblée

Le [portefeuille](index.md) définit un registre national des initiatives dont le champ « coût total de possession » (TCO) est prévu mais non renseigné. L'évaluation **ADHMAT** (Africa CDC) de Madagascar recommande explicitement un *costed national implementation roadmap and financing plan*. Ce document comble le gap en fixant la méthode TCO et une enveloppe indicatives par plateau/lot.

## Composantes du TCO

Pour chaque initiative, le TCO agrège :

- **Investissement** : capital (serveurs, licences, connexions), hébergement souverain ([ART-7](../../referentiel/chapitres/art-7.md)).
- **Exploitation** : maintenance, connectivité, licences récurrentes (ex. [STD-0007 SNOMED CT](../../01_cnisn/05_standards/std-0007-snomed-ct.md)).
- **Hommes** : formation et certification du [workforce numérique](../03_capabilities/workforce-sante-numerique.md).
- **Conduite de changement** : gestion du changement, support, conduite de bénéfices.

## Enveloppe par plateau / lot (indicatif)

| Plateau / Lot | Périmètre | Poste principal de coût |
|---------------|-----------|--------------------------|
| L1 — Infrastructure & sécurité | Hébergement souverain, X-Road, chiffrement | Hébergement, [STD-0002](../../01_cnisn/05_standards/std-0002-securite-chiffrement.md) |
| L2 — Applications terrain | Dossier patient, terminologies | Licences, formation |
| L3 — Médiation & registres | X-Road, registres, identité | Infrastructure d'échange |
| L4 — Analytique & pilotage | Entrepôt, tableaux de bord | Calcul, stockage |
| L5 — Extension & pérennisation | Consentement, conduite de changement | Formation, support |
| L6 — Interopérabilité transfrontalière | GDHCN | Passerelle, conformité |
| L7 — Coordination One Health | Graphe, crise | Intégration intersectorielle |

## Sources de financement

- Budget national (enveloppe e-santé, alignée [SNSD](../../00_caesn/00_overview/foundations.md)).
- Partenaires techniques et financiers (conditionnés à la conformité HEA, voir [ADR-0010](../../01_cnisn/06_decisions/adr-0010-cadre-legal.md)).
- Programmes verticaux (coordonnés via le portefeuille pour éviter la fragmentation).

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Portefeuille** : Portefeuille d'initiatives orienté valeur (`index.md`)
- **Feuille de route ARTSN** : Feuille de route de déploiement (`../../02_artsn/07_lots/index.md`)
- **ADHMAT** : Africa CDC — *costed national implementation roadmap and financing plan*
