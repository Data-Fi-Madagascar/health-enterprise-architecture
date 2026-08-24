---
title: "Acteurs et rôles du système de santé numérique"
id: caesn-acteurs-roles
domain: 07_governance
version: "1.0.0"
status: draft
last_reviewed: 2026-08-24
owner: Ministère de la Santé Publique
tags: ["caesn", "acteurs", "roles", "governance"]
---

# Acteurs et rôles du système de santé numérique

Les acteurs opérationnalisent les parties prenantes (stakeholders) : un acteur *représente* une partie prenante. Les rôles sont *assignés* aux acteurs et *réalisent* des processus métier. Cette vue complète le modèle de valeur CAESN en ajoutant la couche organisationnelle (Business Actor / Role) issue d'ArchiMate.

## Acteurs

| Acteur | Représente | Localisation | Enveloppe |
|--------|------------|--------------|-----------|
| [ACT-01: Patient et usager](acteurs/act-01-patient-et-usager-acteur.md) | PP-01 | LOC-01 | act-01 |
| [ACT-02: Agent de santé de première ligne](acteurs/act-02-agent-de-sant-de-premi-re-ligne.md) | PP-05 | LOC-01, LOC-02 | act-02 |
| [ACT-03: Formation sanitaire](acteurs/act-03-formation-sanitaire-tablissement.md) | PP-06 | LOC-02, LOC-05 | act-03 |
| [ACT-04: Autorité district, région et Ministère](acteurs/act-04-autorit-district-r-gion-et-minist-re.md) | PP-07 | LOC-03, LOC-04 | act-04 |
| [ACT-05: Partenaire technique et financier](acteurs/act-05-partenaire-technique-et-financier-acteur.md) | PP-08 | LOC-06 | act-05 |
| [ACT-06: Équipe technique DEPSI / SIS](acteurs/act-06-quipe-technique-depsi-sis.md) | PP-10 | LOC-06 | act-06 |

## Rôles

| Rôle | Assigné à | Réalise (processus) | Enveloppe |
|------|-----------|---------------------|-----------|
| [ROL-01: Clinicien / prestataire de soins](roles/rol-01-clinicien-prestataire-de-soins.md) | ACT-02 | PRC-01 | rol-01 |
| [ROL-02: Gestionnaire de parcours / référence](roles/rol-02-gestionnaire-de-parcours-r-f-rence.md) | ACT-02 | PRC-02 | rol-02 |
| [ROL-03: Gestionnaire de données / registre](roles/rol-03-gestionnaire-de-donn-es-registre.md) | ACT-06 | PRC-09 | rol-03 |
| [ROL-04: Gestionnaire logistique](roles/rol-04-gestionnaire-logistique.md) | ACT-03 | PRC-08 | rol-04 |
| [ROL-05: Contrôleur / auditeur](roles/rol-05-contr-leur-auditeur.md) | ACT-04 | PRC-13 | rol-05 |
