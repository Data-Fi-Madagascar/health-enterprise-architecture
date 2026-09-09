---
domain: composants
id: CMP-19
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Dossiers & statistiques de sante (hopitaux)
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
implements: ["ENF-1", "F-1"]
maps_to: ["CAP-INT-09"]
applies_to: ["PRC-01", "PRC-02", "PRC-03", "PRC-06"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-19", "couche-2"]
related: ["VS-01", "VS-04"]
---
# CMP-19 : Dossiers & statistiques de sante (hopitaux)
**Contenu normatif.** Ce composant constitue le systeme d'information hospitalier de base au niveau de l'etablissement (Couche 2 du modele ARTSN). Il tient le dossier patient informatise, les admissions, les consultations, les hospitalisations, les actes cliniques et les comptes rendus, et produit les statistiques d'activite hospitaliere (RNAM, indicateurs CSU). Il alimente en amont les registres et l'entrepot national (CMP-03) ainsi que les tableaux de bord (CMP-01). Concu pour un environnement a connectivite intermittente, il fonctionne en mode degrade et se reconcilie avec les composants centraux au retour de couverture.
**Discipline de mise en oeuvre.** L'exhaustivite et l'exactitude des statistiques hospitalieres sont une discipline de premier ordre : tout episode de soin ouvert doit etre cloture et compte-rendu. Les donnees saisies restent reconciliables avec leur source clinique et horodatees. Le composant respecte les referentiels de terminologie (PT-07/CMP-07) et le format de messagerie HL7 FHIR pour l'echange avec le noeud regional (CMP-27).
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../fondations/f-1.md).
- **Processus soutenus** : [PRC-01: Acces, orientation et admission du patient](../processus/prc-01.md) (acces et admission), [PRC-02: Prestation des soins cliniques](../processus/prc-02.md) (prestation des soins), [PRC-03: Continuite, suivi et qualite des soins](../processus/prc-03.md) (suivi et qualite), [PRC-06: Cloture et capitalisation des episodes](../processus/prc-06.md) (cloture et capitalisation).
- **Statut : Brouillon.**
