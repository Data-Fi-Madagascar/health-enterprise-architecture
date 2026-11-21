---
title: "Standards externes : emplacement réservé"
domain: external-standards
id: README-EXTERNAL-STANDARDS
type: meta
status: active
version: "1.0.0"
owner: DEPSI
niveau: "3"
tags: ["referentiel", "standards-base", "standards-externes", "reservation"]
---

# Standards externes : emplacement réservé

Ce dossier est **volontairement vide**. Il matérialise une réservation de localisation, et non une collection manquante. La décision de créer l'emplacement avant son premier contenu évite qu'un standard externe ne soit rangé, par défaut de mieux faire, dans un dossier qui ne correspond pas à sa nature.

## Intention du dossier

Le référentiel HEA manipule deux catégories de normes qu'il convient de ne pas confondre. Les **profils d'interopérabilité** du dossier voisin décrivent des contraintes d'implémentation que le HEA élève lui-même : ils engagent le projet sur des choix structurants, portent un identifiant de projet et relèvent de la gouvernance interne. Les **standards externes** sont des normes publiées par des tiers : ils s'imposent par le consensus de leur écosystème et le HEA n'en maîtrise ni le contenu ni le calendrier d'évolution.

Cette distinction commande le découpage. Un profil PTISN qui transpose HL7 FHIR pour le contexte malgache relève de la première catégorie, parce que la transposition est un acte d'ingénierie du projet. La norme HL7 FHIR elle-même relève de la seconde, parce qu'elle est adoptée, pas produite.

Le tableau ci-dessous fixe les critères d'admission, qui seront appliqués au premier objet réellement introduit.

| Critère | Conséquence pour l'admission |
|---------|-----------------------------|
| Origine | Le document est publié par un organisme externe identifié, et non par le HEA |
| Propriété | Le HEA n'est ni l'auteur, ni le mainteneur, ni l'éditeur du contenu |
| Usage | Le référentiel cite, cite le profil ou contraints le standard dans au moins un objet |
| Traçabilité | La version de référence est notée, de même que l'URL de publication |

L'exigence d'usage mérite un commentaire. Un standard cité par la seule documentation, sans objet du référentiel qui l'implémente, ne relève pas de ce dossier : il relève de la prose du dossier de gouvernance qui le mentionne. Le dossier des standards externes sert donc les standards **opérationnels**, ceux dont l'implémentation est attestée par une fiche du référentiel.

## Conséquences de la réservation

La création de ce dossier a une portée technique immédiate. Les scripts de compilation et de validation parcourent le référentiel d'architecture de manière récursive, et un dossier vide n'apparaît dans aucun artefact généré. Sa seule existence documente dans l'arbre la place qu'occuperont les standards externes, et fournit un point d'ancrage aux rédacteurs qui doivent documenter l'adoption d'une norme tierce.

C'est cette fonction d'ancrage qui justifie le statut `active` du présent document, malgré l'absence de contenu normatif. Le dossier est opérationnel du point de vue de la gouvernance : il est identifiable, il est gouverné, et son contenu se remplira par l'introduction d'objets de type `standard-externe`.

## Références

- [Schéma du référentiel](../../../00_metamodel/schema.md) : types d'objets et répertoires canoniques
- [Bases de codes](../code-systems/README.md) : vocabulaires contrôlés du référentiel
- [Profils d'interopérabilité](../profiles/) : profils d'implémentation propiedad du HEA
