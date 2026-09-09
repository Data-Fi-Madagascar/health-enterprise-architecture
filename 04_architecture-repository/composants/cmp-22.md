---
domain: composants
id: CMP-22
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Espace sante patient
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
implements: ["ENF-1", "F-1"]
maps_to: ["CAP-INT-08"]
applies_to: ["PRC-01", "PRC-07", "PRC-08"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-22", "couche-2"]
related: ["VS-01", "VS-03"]
---
# CMP-22 : Espace sante patient
**Contenu normatif.** Ce composant est le portail oriente beneficiaire du systeme de sante numerique. Il expose au citoyen son dossier, ses rendez-vous, ses droits, son historique de soins et ses documents (resultats d'examens, certificats). Il permet la prise de rendez-vous, l'acces aux services administratifs et la consultation des donnees partagees selon le consentement du beneficiaire. Il materialise l'engagement du patient et l'ouverture du systeme a la partie prenante citoyen.
**Discipline de mise en oeuvre.** L'acces est strictement controle par authentification forte et consentement (CMP-34) ; aucune donnee a caractere personnel n'est exposee sans autorisation explicite. Les traces d'acces sont journalisees (CMP-37). Le portail ne detient pas les donnees sources : il les presente en lecture via les composants detenteurs, garantissant une source unique de verite.
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../fondations/f-1.md).
- **Processus soutenus** : [PRC-01: Acces, orientation et admission du patient](../processus/prc-01.md) (acces aux services), [PRC-07: Identification et droits des beneficiaires](../processus/prc-07.md) (identification et droits), [PRC-08: Financement et exemption au point de service](../processus/prc-08.md) (financement et exemption).
- **Statut : Brouillon.**
