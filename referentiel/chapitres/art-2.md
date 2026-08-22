---
domain: chapitres

id: ART-2
type: chapitre
niveau: "3"
title: Médiation et normalisation
status: stable
maturity_condition: "Stable pour registre structurel/sémantique/géospatial/tarifaire ; Proposition ouverte pour registre intersectoriel. Condition : confirmation du registre intersectoriel par une initiative concernée."
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-2-mediation-normalisation.md
maps_to: ["CAP-14"]
implements: []
applies_to: ["ENF-3", "ENF-4"]
related: []
tags: ["artsn", "niveau-3", "chapitre", "ART-2"]
---
# Médiation et normalisation

**Contenu normatif.** La plateforme doit intégrer un moteur de médiation capable de traduire, transformer et valider structurellement et sémantiquement les payloads hétérogènes du terrain en messages canoniques standardisés. Ce moteur doit obligatoirement s’adosser à des dictionnaires de référence nationaux et internationaux uniques : concepts cliniques, biologie/laboratoire, et classification des maladies (voir les [objets de données métier](../../02_artsn/03_objets-de-donnees/index.md)).

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (multiplicité d’éditeurs de logiciels, silos applicatifs d’ONG), cette discipline seule permet de garantir que les données partagent le même sens médical et la même structure technique sans rompre le pipeline.

- **Rattachement** : [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../capabilites/cap-14.md) (interopérabilité et infrastructure partagée).
- **Normes CNISN** : [STD-0001: Interopérabilité FHIR R4](../../01_cnisn/05_standards/std-0001-interopabilite-fhir.md) (format d'échange canonique, [ADR-0003](../../01_cnisn/06_decisions/adr-0003-fhir.md)), [STD-0006: Terminologie](../../01_cnisn/05_standards/std-0006-terminologie.md), [STD-0007: SNOMED CT](../../01_cnisn/05_standards/std-0007-snomed-ct.md).
- **Objets de données** : [BO-01 Patient & identité](../../00_caesn/04_data/objets.md), [BO-02 Prestation & soins](../../00_caesn/04_data/objets.md), [BO-03 Dispensation & produits](../../00_caesn/04_data/objets.md), [BO-04 Financement & couverture](../../00_caesn/04_data/objets.md), [BO-05 Risque & surveillance](../../00_caesn/04_data/objets.md), [BO-06 Exploitation & gestion](../../00_caesn/04_data/objets.md), [BO-07 Interopérabilité transfrontalière](../../00_caesn/04_data/objets.md) (objets métier CAESN) ; voir aussi le [dictionnaire des objets de données ARTSN](../../02_artsn/03_objets-de-donnees/index.md).
- **Déduit selon** : [ENF-3: Unicité de l'identité et résilience face à la fragmentation applicative](../exigences/enf-3.md) (fragmentation applicative) et [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../exigences/enf-4.md) (One Health).
- **Statut : Stable.**
