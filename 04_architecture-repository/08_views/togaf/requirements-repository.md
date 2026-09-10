---
domain: togaf
id: VIEW-TOGAF-REQUIREMENTS-REPOSITORY
type: repository-view
niveau: "0"
title: "Vue TOGAF - Requirements Repository"
status: draft
owner: DEPSI
version: "0.1"
tags: ["togaf", "requirements-repository", "repository-view"]
---
# Vue TOGAF - Requirements Repository

## Positionnement

Cette vue consolide les exigences contextuelles qui structurent l'ARTSN. Elle sert de registre transversal des contraintes persistantes : résilience réseau, fragmentation applicative, identité, cloisonnement interinstitutionnel et souveraineté.

<!-- BEGIN:GENERATED mode=table source=04_architecture-repository/03_requirements/*.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

| Code | Titre canonique | Rattachement | Statut | Fiche |
|---|---|---|---|---|
| ENF-1 | Résilience à l'instabilité réseau | — | draft | ENF-1 |
| ENF-2 | Intégrité des flux et traçabilité des valeurs | — | draft | ENF-2 |
| ENF-3 | Unicité de l'identité et résilience face à la fragmentation applicative | — | draft | ENF-3 |
| ENF-4 | Cloisonnement inter-institutionnel et étanchéité des données (One Health) | — | draft | ENF-4 |
| ENF-5 | Coordination des processus complexes décentralisés et asynchrones | — | draft | ENF-5 |
| REQ-OH-01 | Tout échange intersectoriel doit être couvert par un accord explicite entre ministères. | CAP-18, ART-0, ART-11 | candidate | REQ-OH-01 |
| REQ-OH-02 | Les identités humaines ne doivent jamais être croisées avec les identités animales. | CAP-18, ART-0, ART-11 | candidate | REQ-OH-02 |
| REQ-OH-03 | Les données agrégées croisées doivent être irréversiblement désanonymisées. | CAP-18, ART-0, ART-11 | candidate | REQ-OH-03 |
| REQ-OH-04 | Chaque secteur conserve la souveraineté sur ses données source. | CAP-18, ART-0, ART-11 | candidate | REQ-OH-04 |
| REQ-OH-05 | Les dimensions d'agrégation communes doivent être normalisées. | CAP-18, ART-0, ART-11 | candidate | REQ-OH-05 |
| REQ-OH-06 | Tous les échanges intersectoriels doivent être journalisés et auditables. | CAP-18, ART-0, ART-11 | candidate | REQ-OH-06 |
| REQ-OH-07 | Le cadre Tripartite Plus doit être respecté pour les flux internationaux. | CAP-18, ART-0, ART-11 | candidate | REQ-OH-07 |
| REQ-TF-01 | Tout flux transfrontalier doit être couvert par un accord explicite. | CAP-15, CAP-18, ART-0, ART-7 | candidate | REQ-TF-01 |
| REQ-TF-02 | Le consentement du patient doit être obtenu pour tout échange sortant sauf obligation légale. | CAP-15, CAP-18, ART-0, ART-7 | candidate | REQ-TF-02 |
| REQ-TF-03 | Seules les données minimisées nécessaires à la finalité peuvent être exportées. | CAP-15, CAP-18, ART-0, ART-7 | candidate | REQ-TF-03 |
| REQ-TF-04 | Tous les flux transfrontaliers doivent être journalisés et auditables. | CAP-15, CAP-18, ART-0, ART-7 | candidate | REQ-TF-04 |
| REQ-TF-05 | Le GDHCN doit être le référentiel de confiance pour les échanges internationaux. | CAP-15, CAP-18, ART-0, ART-7 | candidate | REQ-TF-05 |
| REQ-TF-06 | Les données souveraines ne quittent pas le territoire sauf dérogation. | CAP-15, CAP-18, ART-0, ART-7 | candidate | REQ-TF-06 |
| REQ-TF-07 | Les systèmes partenaires étrangers doivent démontrer leur conformité avant tout accès. | CAP-15, CAP-18, ART-0, ART-7 | candidate | REQ-TF-07 |
| REQ-TF-08 | Tout résumé patient échangé doit être conforme au profil HL7 FHIR IPS et contenir les sections minimales requises. | CAP-15, CAP-18, ART-0, ART-7 | candidate | REQ-TF-08 |

<!-- END:GENERATED -->

## Lecture

Le registre des exigences doit accompagner toutes les phases ADM. Une exigence ne constitue pas une solution ; elle encadre les choix de données, d'applications, de technologie et de migration qui seront ensuite vérifiés dans les profils.
