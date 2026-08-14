---
title: "Processus de dépréciation des composants"
id: depreciation
domain: 02_artsn
version: "0.1"
status: draft
last_reviewed: 2026-08-13
owner: CNASN
tags: [artsn, gouvernance, dépréciation, retrait, cycle-de-vie, niveau-2]
---

# Processus de dépréciation des composants

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle.

---

## Objet

Ce document définit le processus de retrait organizé de composants (standards, profils, chapitres, outils) du référentiel HEA. La dépréciation garantit que le paysage applicatif reste rationalisé, sécurisé et aligné sur les standards en vigueur.

---

## 1. Principe

Un composant est déprécié lorsqu'il n'est plus recommandé pour une nouvelle utilisation, mais peut encore être maintenu en production pendant une période de transition. Il est retiré lorsque toutes les initiatives qui l'utilisent ont migré vers une alternative.

**Règle fondamentale** : aucun composant n'est retiré sans alternative validée et sans plan de migration pour les initiatives concernées.

---

## 2. Signaux de dépréciation

| Signal | Source | Priorité | Délai d'action |
|--------|--------|----------|----------------|
| **Standard abandonné** par son auteur (OMS, HL7, IHE) | Veille internationale | Haute | 30 jours |
| **Technologie en fin de vie** (EOL annoncé par l'éditeur) | Veille technique | Haute | 30 jours |
| **Remplacement** par un standard supérieur | CNASN, veille | Moyenne | 60 jours |
| **Non-utilisation** (> 12 mois sans initiative) | Registre des composants | Basse | 90 jours |
| **Faille sécurité** sans correctif | Audit, CVE | Critique | Immédiat |
| **Non-conformité** réglementaire | Audit, juridique | Haute | 30 jours |

---

## 3. Types de dépréciation

| Type | Description | Préavis | Exemple |
|------|-------------|---------|---------|
| **Dépréciation douce** | Le composant est marqué « déprécié » mais reste utilisable | 12 mois | Un format de données remplacé par un standard plus récent |
| **Dépréciation forte** | Le composant ne doit plus être utilisé pour de nouvelles initatives | 6 mois | Une technologie avec faille de sécurité |
| **Retrait** | Le composant est supprimé du référentiel | 3 mois après fin de dépréciation | Un standard totalement abandonné |

---

## 4. Workflow de dépréciation

### 4.1 Phase 1 — Détection et proposition

| Étape | Action | Responsable | Délai |
|-------|--------|-------------|-------|
| 1.1 | Détecter le signal de dépréciation | Veille technique, CNASN | — |
| 1.2 | Rédiger la proposition de dépréciation | Auteur | 5 jours |
| 1.3 | Soumettre au CNASN | Auteur | 1 jour |

**Contenu de la proposition :**

| Champ | Description |
|-------|-------------|
| Composant concerné | Référence exacte (chapitre, profil, standard) |
| Signal détecté | Raison de la dépréciation |
| Alternative recommandée | Composant de remplacement |
| Initiatives impactées | Liste des initiatives utilisant le composant |
| Risques de non-action | Conséquences si le composant n'est pas déprécié |

### 4.2 Phase 2 — Instruction

| Étape | Action | Responsable | Délai |
|-------|--------|-------------|-------|
| 2.1 | Vérifier les initiatives impactées | Secrétariat CNASN | 5 jours |
| 2.2 | Contacter les responsables d'initiative | Secrétariat CNASN | 5 jours |
| 2.3 | Évaluer le plan de migration | Comité technique | 5 jours |
| 2.4 | Rédiger le rapport d'instruction | Secrétariat CNASN | 3 jours |

### 4.3 Phase 3 — Décision

| Étape | Action | Responsable | Délai |
|-------|--------|-------------|-------|
| 3.1 | Examiner le rapport d'instruction | CNASN | 2 jours |
| 3.2 | Statuer (dépréciation / rejet / report) | CNASN | 1 jour |
| 3.3 | Fixer la date de retrait | CNASN | 1 jour |
| 3.4 | Enregistrer la décision (ADR) | Secrétariat CNASN | 1 jour |

### 4.4 Phase 4 — Notification

| Étape | Action | Responsable | Délai |
|-------|--------|-------------|-------|
| 4.1 | Notifier les initiatives impactées | Secrétariat CNASN | 2 jours |
| 4.2 | Publier l'annonce de dépréciation | DEPSI | 1 jour |
| 4.3 | Mettre à jour le statut du composant | DEPSI | 1 jour |

### 4.5 Phase 5 — Migration

| Étape | Action | Responsable | Délai |
|-------|--------|-------------|-------|
| 5.1 | Les initiatives migrent vers l'alternative | Responsables d'initiative | Selon plan |
| 5.2 | Suivi trimestriel de la migration | CNASN | Trimestriel |
| 5.3 | Alertes aux initiatives en retard | Secrétariat CNASN | Si retard > 30 jours |

### 4.6 Phase 6 — Retrait

| Étape | Action | Responsable | Délai |
|-------|--------|-------------|-------|
| 6.1 | Vérifier que toutes les initiatives ont migré | Secrétariat CNASN | 5 jours |
| 6.2 | Retirer le composant du référentiel | DEPSI | 2 jours |
| 6.3 | Mettre à jour les documents impactés | DEPSI | 5 jours |
| 6.4 | Archiver le composant | DEPSI | 1 jour |

---

## 5. Timeline type

```
Mois 0    : Détection du signal
Mois 0+5j : Proposition rédigée
Mois 0+15j : Instruction terminée
Mois 0+20j : Décision CNASN
Mois 0+25j : Notification aux initiatives
Mois 1    : Annonce publique de dépréciation
Mois 3    : Première alerte aux initiatives
Mois 6    : Deuxième alerte + plan de migration obligatoire
Mois 9    : Dernière alerte
Mois 12   : Retiré du référentiel (statut « déprécié »)
Mois 15   : Archivé (si aucune utilisation résiduelle)
```

---

## 6. Registre des composants dépréciés

| Composant | Date dépréciation | Date retrait | Alternative | Initiatives migrées |
|-----------|-------------------|--------------|-------------|---------------------|
| *(Aucun pour le moment)* | — | — | — | — |

---

## 7. Exceptions

### 7.1 Maintien exceptionnel

Un composant déprécié peut être maintenu au-delà du délai de retrait si :
- Une initiative démontre une impossibilité technique de migration
- Le coût de migration est disproportionné par rapport au risque
- Une dérogation formelle est accordée par le CNASN

### 7.2 Retrait d'urgence

En cas de faille de sécurité critique (CVSS > 9), le composant peut être retiré immédiatement, sans préavis, avec communication d'urgence aux initiatives concernées.

---

## Liens

- [Guide du processus de gouvernance](../../00_caesn/07_governance/processus-gouvernance.md)
- [Registre des décisions](../../00_caesn/08_decisions/registre-decisions.md)
- [Table de maturité](../07_annexes/a-table-de-maturite.md)
- [Gouvernance ARTSN](./index.md)
