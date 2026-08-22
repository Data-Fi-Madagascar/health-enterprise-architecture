---
domain: composants
id: CMP-22
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Espace sante patient
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/composants.md
implements: ["ENF-1", "F-1"]
applies_to: ["PRC-01", "PRC-07", "PRC-08"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-22", "couche-2"]
---
# CMP-22 : Espace sante patient
**Contenu normatif.** Ce composant expose au citoyen un portail de services : son dossier, ses rendez-vous, ses droits et son historique de soins. Il est la face orientee beneficiaire du systeme (engagement patient).
**Discipline de mise en oeuvre.** L'acces est strictement controle par consentement et authentification. Aucune donnee n'est exposee sans autorisation explicite du beneficiaire.
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../fondations/f-1.md).
- **Processus soutenus** : [PRC-01: Acces, orientation et admission du patient](../processus/prc-01.md) (acces aux services), [PRC-07: Identification et droits des beneficiaires](../processus/prc-07.md) (identification et droits), [PRC-08: Financement et exemption au point de service](../processus/prc-08.md) (financement et exemption).
- **Statut : Brouillon.**
