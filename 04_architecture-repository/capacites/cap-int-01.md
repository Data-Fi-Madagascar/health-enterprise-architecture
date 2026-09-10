---
domain: capacites
id: CAP-INT-01
type: capacite
niveau: "2"
title: Résolution d’identité du bénéficiaire
status: candidate
owner: DEPSI
version: "0.5"
family: referentiels
maps_to: ["P-INT-01", "P-INT-02", "P-INT-03", "P-INT-04", "P-INT-14", "P-INT-15", "P-INT-16", "P-INT-17", "P-INT-18", "CAP-01", "CAP-02", "CAP-04", "CAP-07", "CAP-14", "CAP-17"]
implements: []
applies_to: []
related: []
tags: ["cnisn", "niveau-2", "capacite"]
realized_by: ["PL-01", "WP-01"]
---
# Résolution d’identité du bénéficiaire

### Finalité

Permettre aux systèmes autorisés de relier plusieurs représentations d’un même bénéficiaire sans confondre :

- identité fondationnelle ;
- identité fonctionnelle santé ;
- identifiants locaux ;
- identifiants temporaires ;
- identifiants de dossiers.

### Services attendus

- recherche démographique ;
- résolution d’identifiants ;
- rapprochement ;
- détection de doublons ;
- fusion contrôlée ;
- séparation après erreur ;
- gestion des identités temporaires ;
- conservation de la provenance ;
- vérification auprès de l’autorité fondationnelle lorsque l’accès est autorisé.

### Principes associés

- [P-INT-01: Autorité désignée](../02_architecture-elements/motivation/principles/p-int-01.md)
- [P-INT-02: Résolution contre l’autorité](../02_architecture-elements/motivation/principles/p-int-02.md)
- [P-INT-03: Copies locales non autoritatives](../02_architecture-elements/motivation/principles/p-int-03.md)
- [P-INT-04: Historisation des références](../02_architecture-elements/motivation/principles/p-int-04.md)
- [P-INT-14: Base d’autorisation explicite](../02_architecture-elements/motivation/principles/p-int-14.md)
- [P-INT-15: Limitation à la finalité](../02_architecture-elements/motivation/principles/p-int-15.md)
- [P-INT-16: Résidence et non-réplication](../02_architecture-elements/motivation/principles/p-int-16.md)
- [P-INT-17: Minimisation](../02_architecture-elements/motivation/principles/p-int-17.md)
- [P-INT-18: Traçabilité différenciée](../02_architecture-elements/motivation/principles/p-int-18.md)
