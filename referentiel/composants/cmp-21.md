---
domain: composants
id: CMP-21
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Sante communautaire mobile (offline)
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/composants.md
implements: ["ENF-1", "F-1"]
applies_to: ["PRC-01", "PRC-02", "PRC-03"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-21", "couche-2"]
---
# CMP-21 : Sante communautaire mobile (offline)
**Contenu normatif.** Ce composant equipe les agents de sante de proximite sur terminaux mobiles fonctionnant hors ligne (connectivite contrainte). Il capture les donnees communautaires, les vaccinations, les references et la remontee d'information, puis se synchronise des le retour de couverture.
**Discipline de mise en oeuvre.** Il tolere la perte de connectivite sans perte de donnee (file d'attente locale chiffree). L'identite du beneficiaire est resolue localement via le resolveur d'identite.
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../fondations/f-1.md).
- **Processus soutenus** : [PRC-01: Acces, orientation et admission du patient](../processus/prc-01.md) (acces au beneficiaire), [PRC-02: Prestation des soins cliniques](../processus/prc-02.md) (soins de proximite), [PRC-03: Continuite, suivi et qualite des soins](../processus/prc-03.md) (suivi communautaire).
- **Statut : Brouillon.**
