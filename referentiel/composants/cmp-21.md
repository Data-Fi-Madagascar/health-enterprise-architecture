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
envelope: 02_artsn/05_cartographie/composants.md
implements: ["ENF-1", "F-1"]
maps_to: ["CAP-INT-09"]
applies_to: ["PRC-01", "PRC-02", "PRC-03"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-21", "couche-2"]
---
# CMP-21 : Sante communautaire mobile (offline)
**Contenu normatif.** Ce composant equipe les agents de sante de proximite (agents communautaires, sages-femmes, relais) sur terminaux mobiles fonctionnant hors ligne. Il capture les donnees communautaires : vaccinations, consultations, references vers le niveau superieur, releves de terrain et enquetes, et assure la remontee d'information vers la structure de reference. Il s'appuie sur le resolveur d'identite local (CMP-32) pour rattacher le beneficiaire sans ambiguite, meme hors reseau.
**Discipline de mise en oeuvre.** La perte de connectivite ne doit entrainer aucune perte de donnee : une file d'attente locale chiffree conserve les ecritures en attente et la synchronisation differentielle se declenche au retour de couverture. Les terminaux sont authentifies et leurs donnees signees. Le composant reste conforme a l'exigence de resilience au reseau (ENF-1).
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../fondations/f-1.md).
- **Processus soutenus** : [PRC-01: Acces, orientation et admission du patient](../processus/prc-01.md) (acces au beneficiaire), [PRC-02: Prestation des soins cliniques](../processus/prc-02.md) (soins de proximite), [PRC-03: Continuite, suivi et qualite des soins](../processus/prc-03.md) (suivi communautaire).
- **Statut : Brouillon.**
