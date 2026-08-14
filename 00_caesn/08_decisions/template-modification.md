---
title: "Template — Demande de modification architecturale"
id: template-modification
domain: 08_decisions
version: "0.1"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: [template, modification, changement, gouvernance, niveau-1]
---

# Template — Demande de modification architecturale

## Utilisation

Ce template est utilisé pour soumettre toute modification au CAESN, à l'ARTSN ou au référentiel PTISN. Il assure un traitement structuré, traçable et documenté des changements.

**Comment utiliser ce template :**
1. Copier ce fichier en le renommant `MOD-XXXX-titre-court.md`
2. Remplir tous les champs obligatoires
3. Soumettre au CNASN via le processus de gouvernance
4. Le numéro MOD-XXXX est attribué par le secrétariat du CNASN

---

## MOD-XXXX — [Titre de la modification]

### Métadonnées

| Champ | Valeur |
|-------|--------|
| **ID** | MOD-XXXX |
| **Titre** | [Titre court descriptif] |
| **Date de soumission** | AAAA-MM-JJ |
| **Auteur** | [Nom, rôle, organisation] |
| **Niveau impacté** | CAESN / ARTSN / CNISN / PTISN (cocher) |
| **Composant impacté** | [Nom du composant, fichier, chapitre] |
| **Type de modification** | Ajout / Modification / Suppression / Dépréciation |
| **Priorité** | Critique / Haute / Moyenne / Basse |
| **Statut** | Brouillon / Soumis / En revue / Approuvé / Rejeté |

---

### 1. Contexte

**Décrire la situation actuelle et le problème ou l'opportunité identifié.**

> Exemple : « Le chapitre ART-4 ne définit pas de mécanisme de résolution d'identité pour les patients sans NIN, ce qui bloque l'implémentation de PT-04 dans les zones rurales. »

---

### 2. Proposition

**Décrire la modification proposée de manière claire et concise.**

> Exemple : « Ajouter une section ART-4c décrivant un mode dégradé de résolution d'identité basé sur la recherche démographique floue (nom + commune + date de naissance) avec score de confiance. »

---

### 3. Justification

**Expliquer pourquoi cette modification est nécessaire.**

| Critère | Évaluation |
|---------|------------|
| Alignement flux de valeur | [Quel flux est amélioré ?] |
| Renforcement capabilité | [Quelle capabilité est renforcée ?] |
| Conformité standards | [Quel standard est respecté ou adopté ?] |
| Impact sécurité/souveraineté | [Impact positif, neutre ou négatif ?] |
| Coût d'implémentation | [Estimation effort : faible / moyen / élevé] |

---

### 4. Alternatives considérées

**Décrire les alternatives évaluées et les raisons du choix.**

| Alternative | Avantages | Inconvénients | Raison du rejet |
|-------------|-----------|---------------|-----------------|
| [Alternative 1] | ... | ... | ... |
| [Alternative 2] | ... | ... | ... |
| **Choix retenu** | ... | ... | — |

---

### 5. Impact

**Décrire les impacts de la modification sur les différents niveaux.**

| Niveau | Impact | Action requise |
|--------|--------|----------------|
| **CAESN** | [Nul / Faible / Moyen / Élevé] | [Mise à jour document, nouvelle capacité, etc.] |
| **ARTSN** | [Nul / Faible / Moyen / Élevé] | [Nouveau chapitre, modification chapitre, etc.] |
| **CNISN** | [Nul / Faible / Moyen / Élevé] | [Nouvelle capacité, modification principes, etc.] |
| **PTISN** | [Nul / Faible / Moyen / Élevé] | [Nouveau profil, modification profil, etc.] |
| **Référentiel** | [Nul / Faible / Moyen / Élevé] | [Ajout objet, modification objet, etc.] |
| **Systèmes existants** | [Nul / Faible / Moyen / Élevé] | [Migration, compatibilité, etc.] |

---

### 6. Risques

**Identifier les risques associés à cette modification.**

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| [Risque 1] | Faible / Moyenne / Élevée | Faible / Moyen / Élevé / Critique | [Action de mitigation] |
| [Risque 2] | ... | ... | ... |

---

### 7. Plan d'implémentation

**Décrire les étapes d'implémentation si la modification est approuvée.**

| Étape | Description | Responsable | Échéance |
|-------|-------------|-------------|----------|
| 1 | [Rédaction/update document] | ... | ... |
| 2 | [Validation technique] | ... | ... |
| 3 | [Publication] | ... | ... |
| 4 | [Formation/communication] | ... | ... |
| 5 | [Déploiement] | ... | ... |

---

### 8. Approbation

| Rôle | Nom | Date | Décision |
|------|-----|------|----------|
| Auteur | ... | ... | — |
| Relecture technique | ... | ... | Approuvé / Rejeté / À modifier |
| CNASN | ... | ... | Approuvé / Rejeté / Dérogation |
| Secrétaire Général | ... | ... | Approuvé / Rejeté |

---

### 9. Références

- [Lien vers le document impacté](...)
- [Lien vers le standard de référence](...)
- [ADR associée si applicable](...)

---

## Liens

- [Registre des décisions](./registre-decisions.md)
- [Processus de gouvernance](../07_governance/processus-gouvernance.md)
- [Template ADR](./adr-0000-template.md)
