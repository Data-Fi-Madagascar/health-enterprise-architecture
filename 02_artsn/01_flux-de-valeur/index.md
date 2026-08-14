---
title: Flux de valeur
id: artsn-flux-de-valeur
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, flux-de-valeur, niveau-3]
---

# Flux de valeur

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

Les quatre flux de valeur stratégiques dictent la finalité de santé publique de la plateforme numérique nationale. Ils constituent les **piliers directeurs non négociables** auxquels toute brique logicielle de l'architecture doit apporter une contribution mesurable. Cette partie définit l'intention politique et la traduit en actions humaines sur le terrain (macro-processus), posant la matrice de déduction des besoins en données.

Les flux de valeur sont identiques à ceux définis par le [CAESN](../../00_caesn/01_value-streams/index.md). L'ARTSN les décline en exigences techniques opposables.

## VS-01 — Accéder à des services de santé essentiels, intégrés, équitables et de qualité

**Contenu normatif.** L'infrastructure technologique doit garantir l'unification des parcours de soins et l'intégration native des dossiers médicaux individuels à l'échelle du pays. Tout professionnel de santé (médecin, infirmier, pharmacien), quel que soit son point de service ou son mode d'exercice, doit pouvoir accéder de manière sécurisée à l'historique clinique partagé du patient. L'équité d'accès impose que la capacité de capture clinique soit pleinement opérationnelle en zone rurale isolée.

**Statut : Stable.** — voir chapitre [ART-3 (historisation événementielle)](../../referentiel/chapitres/art-3.md) et [ART-4a (résolution d'identité)](../../referentiel/chapitres/art-4a.md).

## VS-02 — Prévenir, détecter et répondre aux risques sanitaires

**Contenu normatif.** La plateforme doit matérialiser l'approche **One Health** (Santé Unique) en organisant le croisement systématique et automatisé des signaux d'alertes issus de la santé humaine, de la santé animale (zoonoses) et de la surveillance environnementale (climat, pollution). Le système doit détecter les signaux faibles, isoler les clusters de symptômes anormaux de manière ultra-précoce et déclencher des alertes automatisées. En cas de crise validée, l'architecture doit soutenir la coordination immédiate des plans de contingence et la mobilisation des réponses intersectorielles.

**Statut : Stable.** — voir [ART-8b (modélisation en graphe)](../../referentiel/chapitres/art-8b.md) et [ART-8d (chorégraphie inter-institutionnelle)](../../referentiel/chapitres/art-8d.md).

## VS-03 — Protéger financièrement la population face aux dépenses de santé

**Contenu normatif.** L'architecture doit intégrer nativement les flux financiers et les régimes d'assurance maladie publique (Fonds d'équité, Couverture Santé Universelle) au cœur du point de service pour éradiquer les dépenses de santé catastrophiques. Le système a l'obligation de calculer et d'appliquer automatiquement les subventions, le tiers-payant ou la gratuité ciblée lors de la dispensation d'un soin ou d'un médicament, sans que le patient n'ait à avancer les fonds. La transparence absolue et l'immuabilité de ces transactions doivent être garanties pour éliminer tout risque de détournement de fonds ou de double facturation.

**Statut : Stable.** — voir [ART-4c (éligibilité et couverture)](../../referentiel/chapitres/art-4c.md) et [ART-9 (garanties transactionnelles fortes)](../../referentiel/chapitres/art-9.md).

## VS-04 — Piloter, coordonner et améliorer la performance du système de santé

**Contenu normatif.** La plateforme nationale doit opérer la transformation automatique des données opérationnelles de terrain (cliniques, financières et logistiques) en indicateurs de performance macro-sanitaires (KPI) standardisés et incontestables. Les instances dirigeantes de l'État doivent disposer de tableaux de bord unifiés pour évaluer en temps réel l'efficacité des politiques publiques, mesurer la couverture vaccinale réelle, anticiper les ruptures de stocks et piloter la performance globale du système.

**Statut : Stable.** — voir [ART-6 (analytique et restitution)](../../referentiel/chapitres/art-6.md) et [Couche 6 (pilotage)](../04_cartographie-cible/index.md#couche-6--pilotage-gouvernance-et-actions-intersectorielles).

## Liens

- [Fondations](../00_fondations/index.md)
- [Exigences contextuelles nationales](../02_exigences-contextuelles/index.md)
- [Chapitres et patterns de référence](../03_chapitres/index.md)
- [CAESN — flux de valeur](../../00_caesn/01_value-streams/index.md)
