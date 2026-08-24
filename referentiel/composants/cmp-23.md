---
domain: composants
id: CMP-23
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Chaine logistique (LMIS)
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
implements: ["ENF-1", "F-1"]
maps_to: ["CAP-INT-10"]
applies_to: ["PRC-05", "PRC-10"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-23", "couche-2"]
---
realized_by: ["WP-02"]
# CMP-23 : Chaine logistique (LMIS)
**Contenu normatif.** Ce composant pilote la logistique medicale de bout en bout : prevision des besoins, approvisionnement, stockage, distribution et dispensation des intrants (medicaments, consommables, vaccins, reactifs). Il interconnecte les pharmacies (CMP-20), les districts, les regions et le noeud central, et calcule les seuils de reapprovisionnement a partir des donnees d'activite clinique. Il emet les alertes de rupture et orchestre les flux physiques et informationnels.
**Discipline de mise en oeuvre.** La tracabilite de bout en bout est obligatoire (lot, periode de validite, lieu). Les seuils de securite sont parametres par type d'intrant et de structure. Les donnees d'activite issues des etablissements (CMP-19) alimentent la prevision. Tout mouvement est historise de facon immuable et reconcilie avec la comptabilite.
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../fondations/f-1.md).
- **Processus soutenus** : [PRC-05: Alerte, investigation et riposte](../processus/prc-05.md) (approvisionnement et riposte), [PRC-10: Planification et allocation des ressources](../processus/prc-10.md) (planification des ressources).
- **Statut : Brouillon.**
