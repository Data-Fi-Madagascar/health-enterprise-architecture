---
title: "Analyse de contenu — Synthèse des 4 niveaux"
id: content-analysis
domain: docs
version: "1.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: [analyse, qualité, contenu, synthèse]
---

# Analyse de contenu — Synthèse des 4 niveaux

## Vue d'ensemble

| Niveau | Score | Verdict |
|--------|-------|---------|
| 1 — CAESN | **7/10** | Solide et cohérent, mais draft sans ADR ni normes |
| 2 — CNISN | **7/10** | Qualité architecturale remarquable, mais instances inexistantes |
| 3 — ARTSN | **8/10** | Bon document technique, 7 chapitres encore en proposition |
| 4 — PTISN | **7/10** | Structure exemplaire, contenu en devenir (4 profils à instruire) |

**Score global : 7.25/10** — Documentation de bonne qualité pour un pays en développement, mais état de draft avancé avec des lacunes opérationnelles critiques.

---

## Problèmes critiques transversaux (bloquants)

| # | Problème | Niveaux impactés | Impact |
|---|----------|------------------|--------|
| **C1** | **Instances de gouvernance inexistantes** — CNASN, instance sectorielle, autorité cybersécurité, autorité données n'existent pas | 1, 2, 4 | Le cadre ne peut pas être mis en œuvre |
| **C2** | **Aucun ADR enregistré** — zero traçabilité des choix architecturaux | 1 | Aucune légitimité des décisions |
| **C3** | **Aucune norme établie** — homologation impossible | 1, 3 | Pas de critères de conformité |
| **C4** | **Référentiel absent** — fiches `referentiel/` non présentes dans le dépôt | 2, 3, 4 | Liens cassés, documents non autoporteurs |
| **C5** | **5 écarts CAESN ↔ ARTSN non arbitrés** (point de vigilance D-1 à D-5) | 1, 3 | Incohérence entre niveaux |
| **C6** | **Trajectoire sans dates ni jalons** — 5 phases sans calendrier | 2 | Impossible à piloter |
| **C7** | **PT-11 Consentement vide** — aucun standard technique choisi | 4 | Toute initiative de partage patients bloquée |
| **C8** | **Dictionnaire de données vide** — aucune sémantique universelle fixée | 3 | Contrats d'interface sans base commune |
| **C9** | **PDSS 2020-2024 potentiellement obsolète** | 1 | Perte de légitimité stratégique |
| **C10** | **18 décisions PTISN à instruire sans calendrier** | 4 | PTISN non opérationnel |

---

## Problèmes moyens transversaux

| # | Problème | Niveaux |
|---|----------|---------|
| M1 | Indicateurs non mesurables (pas de baseline, cibles, responsables) | 1, 2 |
| M2 | Glossaires incomplets (~20 termes chacun) | 1, 2, 3, 4 |
| M3 | Pas de mapping FHIR/IHE/OpenHIE | 2, 3, 4 |
| M4 | Diagrammes PlantUML manquants ou vides | 1, 3 |
| M5 | Rattachements CAP↔PRC tous identiques (artefact de génération) | 1 |
| M6 | Composition du Comité National non détaillée | 1, 2 |
| M7 | X-Road absent de la cartographie ARTSN | 3, 4 |
| M8 | Conflit d'autorité CNASN vs instance sectorielle | 2, 4 |
| M9 | Aucun exemple concret (profil d'initiative rempli, cas d'usage) | 4 |
| M10 | Nomenclature ARTSN vs ARTSN non unifiée | 3, 4 |

---

## Points forts transversaux

| # | Point fort | Niveaux |
|---|------------|---------|
| F1 | **Démarche value-driven cohérente** — chaîne flux → capabilité → initiative → bénéfice | 1 |
| F2 | **Structure documentaire mature** — hiérarchie 4 niveaux, frontmatter YAML, liens | 1, 2, 3, 4 |
| F3 | **Ancrage stratégique solide** — PDSS, SNSD, PSRSIS, DPI-H, OpenHIE, GovStack | 1, 2 |
| F4 | **25 principes CNISN de qualité** — P-INT-22 (connectivité contrainte), P-INT-14 (bases d'autorisation) pertinents | 2 |
| F5 | **6 fondations ARTSN justifiées** — discipline existentielle par risque concret | 3 |
| F6 | **Cartographie cible moderne** — 6 couches + 2 axes, event-driven | 3 |
| F7 | **Matrice d'alignement PTISN complète** — 0 écart, mapping CAP-INT → profils | 4 |
| F8 | **Séparation des responsabilités claire** — médiation vs plateforme vs services | 4 |
| F9 | **RACI complet** — 7 acteurs × 13 activités | 1 |
| F10 | **3 profils PTISN prêts à l'emploi** — PT-01 (X-Road), PT-04 (identité), PT-08 (agrégées) | 4 |

---

## Analyse par niveau

### Niveau 1 — CAESN (7/10)

**Ce qui fonctionne :**
- Chaîne valeur → capabilité → initiative bien formalisée
- 32 principes (12 PA + 20 PD) structurés
- 16 capabilités avec maturité et runway
- RACI complet, cycle de vie applicatif

**Ce qui manque :**
- ADR vide, normes vides
- Maturités non validées
- Registre initiatives inexistant
- Comité National non détaillé
- BRV sans moyens

**Priorité :** Arbitrer les 5 écarts avec l'ARTSN, valider les maturités, enregistrer les premiers ADR.

---

### Niveau 2 — CNISN (7/10)

**Ce qui fonctionne :**
- 25 principes de qualité (catégories A-F)
- 12 capacités bien réparties en 5 familles
- Matrice principes-capacités complète
- P-INT-22 (connectivité contrainte) directement pertinent

**Ce qui manque :**
- Instances de gouvernance inexistantes
- CAP-INT-12 référencie un dispositif inexistant
- Trajectoire sans dates
- Dossier conformité irréaliste (15 éléments)
- Indicateurs non mesurables

**Priorité :** Créer/ simuler les instances, simplifier la conformité, dater la trajectoire.

---

### Niveau 3 — ARTSN (8/10)

**Ce qui fonctionne :**
- 6 fondations solides et justifiées
- 5 exigences contextuelles complètes
- Cartographie cible en 6 couches
- Gouvernance technique robuste
- Transparence des écarts CAESN

**Ce qui manque :**
- 7 chapitres sur 19 en « Proposition ouverte »
- Dictionnaire de données vide
- Référentiel détaillé absent
- F.5 et F.6 au statut provisoire

**Priorité :** Peupler le dictionnaire (20-30 concepts), promouvoir ART-4C et ART-9 via pilotes.

---

### Niveau 4 — PTISN (7/10)

**Ce qui fonctionne :**
- Matrice d'alignement complète (0 écart)
- 3 profils prêts à l'emploi (PT-01, PT-04, PT-08)
- Convention de nommage rigoureuse
- 18 principes de mise en œuvre pertinents

**Ce qui manque :**
- PT-11 Consentement vide (risque bloquant)
- PT-09 et PT-13 à instruire
- X-Road non ancré dans l'ARTSN
- Aucun exemple de profil d'initiative rempli
- 18 décisions sans calendrier

**Priorité :** Trancher PT-11 (consentement), dater les 5 premières décisions, produire 2-3 exemples.

---

## Recommandations prioritaires (ordre d'exécution)

| Phase | Action | Délai | Niveaux |
|-------|--------|-------|---------|
| **Phase 1** | Arbitrer les 5 écarts CAESN ↔ ARTSN (D-1 à D-5) | Immédiat | 1, 3 |
| **Phase 1** | Valider les maturités des capabilités avec les directions métier | 1 mois | 1 |
| **Phase 1** | Créer les premiers ADR (choix structurants déjà faits) | 1 mois | 1 |
| **Phase 2** | Créer/simuler les instances de gouvernance (organigramme minimal) | 2 mois | 1, 2, 4 |
| **Phase 2** | Compléter les fichiers référentiel (`referentiel/`) | 2 mois | 2, 3, 4 |
| **Phase 2** | Prioriser et dater les 5 premières décisions PTISN | 2 mois | 4 |
| **Phase 3** | Établir les premières normes critiques (interopérabilité, sécurité) | 3 mois | 1 |
| **Phase 3** | Peupler le dictionnaire de données (20-30 concepts clés) | 3 mois | 3 |
| **Phase 3** | Commissionner l'analyse PT-11 (consentement) | 3 mois | 4 |
| **Phase 4** | Dater la trajectoire CNISN (5 phases avec jalons) | 4 mois | 2 |
| **Phase 4** | Produire 2-3 exemples de profils d'initiative remplis | 4 mois | 4 |
| **Phase 5** | Vérifier la pérennité PDSS/SNSD/PSRSIS | 5 mois | 1 |
| **Phase 5** | Ajouter des diagrammes C4 pour la cartographie cible | 5 mois | 3 |
| **Phase 6** | Élaborer une feuille de route de déploiement progressif | 6 mois | 1, 2 |

---

## Comparaison avec les standards internationaux

| Aspect | HEA | OpenHIE | GovStack | OMS DPI-H | Verdict |
|--------|-----|---------|----------|-----------|---------|
| **Autorité des données** | P-INT-01→04 | HFR, Client Registry | — | — | ✅ Couvert |
| **Consentement** | P-INT-14 (élargi) | — | — | — | ⚠️ Cadre sans technique |
| **Traçabilité** | P-INT-18, CAP-INT-10 | — | — | — | ✅ Couvert |
| **Catalogue de services** | CAP-INT-06 | — | — | — | ✅ Plus ambitieux |
| **Tests de conformité** | CAP-INT-12 | Connectathon | — | — | ❌ Pas d'outils |
| **Connectivité contrainte** | P-INT-22 | — | — | — | ✅ Plus pertinent |
| **Neutralité technologique** | P-INT-19 | Open source | — | — | ✅ Aligné |
| **Patterns architecturaux** | ART-0→11 | — | — | — | ✅ Couvert |

**Lacunes :** Pas de profiling IHE, pas de mapping FHIR, pas de référence explicite à OpenHIE dans le CNISN.

---

## État de maturité global

```
Niveau 1 (CAESN)  ████████░░  80% — Draft avancé, fondations solides
Niveau 2 (CNISN)  ███████░░░  70% — Contenu bon, opérationnalisation absente
Niveau 3 (ARTSN)  ████████░░  80% — Technique solide, 7 chapitres à valider
Niveau 4 (PTISN)  ███████░░░  70% — Structure exemplaire, 4 profils à instruire
```

**Moyenne : 72.5%** — Le cadre est intellectuellement mature mais opérationnellement immature.

---

## Conclusion

Le système documentaire HEA est une **réussite architecturale** pour un pays en développement. La chaîne CAESN → CNISN → ARTSN → PTISN est cohérente, les conventions sont respectées, et la démarche value-driven est authentique.

Les principaux risques sont :
1. **L'écart entre la théorie et la pratique** — le cadre suppose l'existence d'instances qui n'existent pas
2. **Le manque de concrétisation** — ADR vides, normes vides, référentiel absent
3. **Les lacunes bloquantes** — consentement (PT-11), dictionnaire de données, écarts CAESN-ARTSN

La priorité absolue est de **passer du draft à l'opérationnel** en arbitrant les choix structurants, en créant les instances minimalistes, et en produisant des exemples concrets qui prouvent la faisabilité du cadre.
