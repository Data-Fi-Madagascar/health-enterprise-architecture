# Vue intégrée — les 6 couches de l'architecture

Seconde vue intégrée, structurée cette fois par les **6 couches horizontales** de la
cartographie conceptuelle cible (ARTSN), traversées par **2 axes verticaux** transversaux.
Chaque couche aligne les réalisations des quatre familles.

![Vue intégrée — 6 couches](architecture-6-couches.svg)

## Les 6 couches (haut → bas)

| Couche | Rôle | Réalisation (ex.) |
|--------|------|------------------|
| 6 | Pilotage, Gouvernance & actions intersectorielles | CMP-01/02 · ART-0/9/11 · PART-ECHANGE-TRANSFRONTALIER / PART-ONE-HEALTH |
| 5 | Projections analytiques & Modèles | CMP-03/04/05 · ART-6/5/8B/4D · ABB-EXPOSITION-DONNEES-ANALYTIQUES / PAT-QUALITE-RECONCILIATION |
| 4 | Interopérabilité & services partagés | CMP-06…14 · ART-2/3/4/8A · ABB-ECHANGE-MEDIATION / ABB-CATALOGUE-CONTRATS / ABB-SERVICE-TERMINOLOGIE |
| 3 | Échange, transport & ingestion | CMP-15…18 · ART-1/8C · ABB-ECHANGE-MEDIATION / PART-ECHANGE-TRANSFRONTALIER |
| 2 | Point de service | CMP-19…25 · ENF-1/F.1 · ABB-IDENTITE-BENEFICIAIRE / ABB-REGISTRE-PROFESSIONNELS |
| 1 | Infrastructure | CMP-26…31 · ART-7 · ABB-CONFIANCE-AUTORISATION / ABB-AUDIT-PROVENANCE |

## Les 2 axes verticaux (transversaux)

- **Axe 1 — Sécurité & confiance numérique** : CMP-32…38 · ART-7 · ABB-CONFIANCE-AUTORISATION / ABB-AUDIT-PROVENANCE · GDHCN (ADR-0007).
- **Axe 2 — Gouvernance de données** : CMP-39…46 · F.4 · ART-0 · ADR d'homologation.

## Alignement inter-familles

- **CAESN → ARTSN** : les CMP réalisent les chapitres/fondations (ex. CMP-11 = ART-4A, CMP-12 = ART-4C).
- **CNISN → ARTSN** : chaque objet d'interopérabilité TOGAF est détaillé par les `STD-0001…0007` et `ADR-0001…0010` qui nourrissent les chapitres.
- **ARTSN → PTISN** : chaque chapitre est implémenté par un ou plusieurs profils (`PT-xx`).

## Source

Généré depuis `02_artsn/05_cartographie/index.md`, le `coherence-report.md` et l'état
`validate_ref.py` (CONFORME). Voir aussi la [vue par familles](vue-integree.md).
