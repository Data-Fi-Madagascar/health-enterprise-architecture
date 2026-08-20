---

title: "ART-2 : Médiation et normalisation"
id: ART-2
domain: 02_artsn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: ["artsn", "chapitres", "ART-2", "niveau-3"]
related: ["CAP-INT-03"]
---

# ART-2 : Médiation et normalisation

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

**Contenu normatif.** La plateforme doit intégrer un moteur de médiation capable de traduire, transformer et valider structurellement et sémantiquement les payloads hétérogènes du terrain en messages canoniques standardisés. Ce moteur doit obligatoirement s’adosser à des dictionnaires de référence nationaux et internationaux uniques : concepts cliniques, biologie/laboratoire, et classification des maladies.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (multiplicité d’éditeurs de logiciels, silos applicatifs d’ONG), cette discipline seule permet de garantir que les données partagent le même sens médical et la même structure technique sans rompre le pipeline.

- **Rattachement** : [CAP-14: Interopérabilité, référentiels nationaux et infrastructure numérique partagée](../../referentiel/capabilites/cap-14.md) (interopérabilité et infrastructure partagée).
- **Déduit selon** : [ENF-3: Unicité de l'identité et résilience face à la fragmentation applicative](../../referentiel/exigences/enf-3.md) (fragmentation applicative) et [ENF-4: Cloisonnement inter-institutionnel et étanchéité des données (One Health)](../../referentiel/exigences/enf-4.md) (One Health).
- **Statut : Stable.**

*Rattachement : ENF-3, ENF-4, CAP-14 · fiche ART-2*

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`ART-2`** : Médiation et normalisation (`referentiel/chapitres/art-2.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/03_chapitres/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
