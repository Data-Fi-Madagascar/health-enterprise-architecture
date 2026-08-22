---

title: "Sécurité, contrôle d'accès et résidence de la donnée"
id: artsn-ART-7
domain: 04_patterns
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: ["artsn", "chapitres", "ART-7", "niveau-3"]
related: ["CAP-INT-08"]
---

# Sécurité, contrôle d'accès et résidence de la donnée

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


ART-7 : Sécurité, contrôle d'accès et résidence de la donnée constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `ART-7`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Contenu normatif.** L’architecture impose un modèle de sécurité **strict par défaut**. Le contrôle d’accès doit combiner le rôle de l’agent et ses attributs contextuels ou territoriaux. Tout accès, lecture ou écriture doit être chiffré et journalisé de manière immuable. Les données de santé des citoyens ont l’obligation légale de **résider physiquement sur le territoire national** (copie maîtresse).

**Règle résidence ↔ échange.** La résidence obligatoire concerne la **donnée au repos** (copie maîtresse hébergée sur le territoire national, [STD-0002](../../01_cnisn/05_standards/std-0002-securite-chiffrement.md)). Elle ne fait pas obstacle aux **échanges transfrontaliers**, qui ne portent que des données **en transit**, chiffrées et horodatées, sans déplacement de la copie maîtresse : l’échange inter-institutionnel emprunte X-Road ([ADR-0001](../../01_cnisn/06_decisions/adr-0001-x-road.md)) et l’échange international emprunte la passerelle de confiance mondiale OMS GDHCN ([ADR-0007](../../01_cnisn/06_decisions/adr-0007-gdhcn.md)). La résidence et l’échange sont donc compatibles : seule la copie maîtresse est souveraine ; les flux sortants sont des vues chiffrées et révocables.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (terminaux mobiles volés sur le terrain, tentatives d’intrusions extérieures, flux sortants vers partenaires étrangers), cette discipline seule permet de garantir l’inviolabilité du secret médical et la souveraineté numérique de l’État sans rompre le pipeline.

- **Rattachement** : [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../../referentiel/capabilites/cap-15.md) (cybersécurité et gouvernance de la sécurité).
- **Modèles cibles** : Zero-Trust, RBAC, ABAC, chiffrement (AES-256), AuditEvent FHIR.
- **Normes CNISN** : [STD-0002: Sécurité et chiffrement](../../01_cnisn/05_standards/std-0002-securite-chiffrement.md), [ADR-0001: X-Road](../../01_cnisn/06_decisions/adr-0001-x-road.md), [ADR-0007: GDHCN](../../01_cnisn/06_decisions/adr-0007-gdhcn.md), [ADR-0008: Audit ATNA](../../01_cnisn/06_decisions/adr-0008-atna.md).
- **Objets de données** : [BO-01 Patient & identité](../../00_caesn/04_data/objets.md), [BO-07 Interopérabilité transfrontalière](../../00_caesn/04_data/objets.md) (objets métier CAESN) ; voir aussi le [dictionnaire des objets de données ARTSN](../03_objets-de-donnees/index.md).
- **Déduit selon** : [ENF-1: Résilience à l'instabilité réseau](../../referentiel/exigences/enf-1.md) (sécurité locale).
- **Statut : Stable.**

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`ART-7`** : Sécurité, contrôle d'accès et résidence de la donnée (`referentiel/chapitres/art-7.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/04_patterns/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
