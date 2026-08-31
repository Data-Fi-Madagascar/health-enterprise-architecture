---

title: "Médiation et normalisation"
id: artsn-ART-2
domain: 04_patterns
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: ["artsn", "chapitres", "ART-2", "niveau-3"]
related: ["CAP-INT-03"]
---

# Médiation et normalisation

## Pour qui lire ce document

**Niveau :** niveau 3 : Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.


ART-2 : Médiation et normalisation constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `ART-2`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Contenu normatif.** La plateforme doit intégrer un moteur de médiation capable de traduire, transformer et valider structurellement et sémantiquement les payloads hétérogènes du terrain en messages canoniques standardisés. Ce moteur doit obligatoirement s’adosser à des dictionnaires de référence nationaux et internationaux uniques : concepts cliniques, biologie/laboratoire, et classification des maladies (voir les [objets de données métier](../03_objets-de-donnees/index.md)).

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (multiplicité d’éditeurs de logiciels, silos applicatifs d’ONG), cette discipline seule permet de garantir que les données partagent le même sens médical et la même structure technique sans rompre le pipeline.

- **Rattachement** : [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../../referentiel/capabilites/cap-14.md) (interopérabilité et infrastructure partagée).
- **Normes CNISN** : [STD-0001: Interopérabilité FHIR R4](../../01_cnisn/05_standards/std-0001-interopabilite-fhir.md) (format d'échange canonique, [ADR-0003](../../01_cnisn/06_decisions/adr-0003-fhir.md)), [STD-0006: Terminologie](../../01_cnisn/05_standards/std-0006-terminologie.md), [STD-0007: SNOMED CT](../../01_cnisn/05_standards/std-0007-snomed-ct.md).
- **Objets de données** : [BO-01 Patient & identité](../../00_caesn/04_data/objets.md), [BO-02 Prestation & soins](../../00_caesn/04_data/objets.md), [BO-03 Dispensation & produits](../../00_caesn/04_data/objets.md), [BO-04 Financement & couverture](../../00_caesn/04_data/objets.md), [BO-05 Risque & surveillance](../../00_caesn/04_data/objets.md), [BO-06 Exploitation & gestion](../../00_caesn/04_data/objets.md), [BO-07 Interopérabilité transfrontalière](../../00_caesn/04_data/objets.md) (objets métier CAESN) ; voir aussi le [dictionnaire des objets de données ARTSN](../03_objets-de-donnees/index.md).
- **Déduit selon** : [ENF-3: Unicité de l'identité et résilience face à la fragmentation applicative](../../referentiel/exigences/enf-3.md) (fragmentation applicative) et [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../../referentiel/exigences/enf-4.md) (One Health).
- **Statut : Stable.**

## Profils PTISN qui implémentent ce chapitre

Les profils techniques nationaux ci-dessous déclarent implémenter ce chapitre ART dans leur champ `implements` (frontmatter du référentiel). Le profil constitue la spécification implémentable et testable ; le chapitre demeure le cadre normatif opposable.

- [PT-02 : Médiation intra-secteur](../../referentiel/profils/pt-02.md)
- [PT-03 : Catalogue des services et registre des contrats](../../referentiel/profils/pt-03.md)
- [PT-07 : Terminologie et codification](../../referentiel/profils/pt-07.md)
- [PT-08 : Échange de données agrégées](../../referentiel/profils/pt-08.md)
- [PT-18 : Échange de réclamations et paiements](../../referentiel/profils/pt-18.md)
- [PT-19 : Aide à la décision clinique (CDS)](../../referentiel/profils/pt-19.md)

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`ART-2`** : Médiation et normalisation (`referentiel/chapitres/art-2.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/04_patterns/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
