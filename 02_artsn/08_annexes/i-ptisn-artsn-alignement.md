---
title: "Annexe I : Index des profils PTISN implémentant chaque chapitre ART"
id: ptisn-artsn-alignement
domain: 08_annexes
version: "1.0.0"
status: draft
last_reviewed: 2026-08-31
owner: DEPSI
tags: ["artsn", "ptisn", "annexes", "alignement", "traçabilité"]
---

# Annexe I : Index des profils PTISN implémentant chaque chapitre ART

Cet index inverse établit la correspondance entre chaque chapitre de l'Architecture de Référence Technique (ARTSN) et les profils techniques nationaux (PTISN) qui le déclarent implémenter. Il répond à la question : *quel profil PTISN mobilise ce chapitre ART ?* Chaque profil prescrit, pour un service national, les standards, acteurs, transactions et règles d'échange à respecter (modèle IHE) ; le chapitre ART constitue le cadre normatif opposable qu'il opérationnalise.

La source de vérité est le champ `implements` du frontmatter de chaque profil dans `referentiel/profils/pt-XX.md`. Le champ `related` n'est pas repris ici car il documente des dépendances transversales et non des implémentations directes.

## Index chapitre ART → profils PTISN

| Chapitre ART | Titre canonique | Profils PTISN qui l'implémentent |
|---|---|---|
| [ART-0](../../02_artsn/04_patterns/art-0-accords-partage.md) | Accords de partage inter-institutionnels | [PT-01](../../03_ptisn/03_profils/pt-01-echange-interinstitutionnel.md), [PT-10](../../03_ptisn/03_profils/pt-10-confiance-authentification-autorisation.md), [PT-11](../../03_ptisn/03_profils/pt-11-consentement-bases-autorisation.md), [PT-14](../../03_ptisn/03_profils/pt-14-interopabilite-transfrontaliere.md), [PT-15](../../03_ptisn/03_profils/pt-15-surveillance-one-health.md) |
| [ART-1](../../02_artsn/04_patterns/art-1-integration-ingestion.md) | Intégration et ingestion | [PT-01](../../03_ptisn/03_profils/pt-01-echange-interinstitutionnel.md), [PT-02](../../03_ptisn/03_profils/pt-02-mediation-intra-secteur.md), [PT-03](../../03_ptisn/03_profils/pt-03-catalogue-services-registre-contrats.md), [PT-08](../../03_ptisn/03_profils/pt-08-echange-donnees-agregees.md), [PT-14](../../03_ptisn/03_profils/pt-14-interopabilite-transfrontaliere.md) |
| [ART-2](../../02_artsn/04_patterns/art-2-mediation-normalisation.md) | Médiation et normalisation | [PT-02](../../03_ptisn/03_profils/pt-02-mediation-intra-secteur.md), [PT-03](../../03_ptisn/03_profils/pt-03-catalogue-services-registre-contrats.md), [PT-07](../../03_ptisn/03_profils/pt-07-terminologie-codification.md), [PT-08](../../03_ptisn/03_profils/pt-08-echange-donnees-agregees.md), [PT-18](../../03_ptisn/03_profils/pt-18-echange-reclamations-paiements.md), [PT-19](../../03_ptisn/03_profils/pt-19-aide-decision-clinique.md) |
| [ART-3](../../02_artsn/04_patterns/art-3-historisation-evenementielle.md) | Historisation événementielle | [PT-09](../../03_ptisn/03_profils/pt-09-analytique-exposition-donnees.md), [PT-12](../../03_ptisn/03_profils/pt-12-audit-provenance-tracabilite.md) |
| [ART-4](../../02_artsn/04_patterns/art-4-referentiels-metadonnees.md) | Référentiels de métadonnées de gestion | [PT-04](../../03_ptisn/03_profils/pt-04-resolution-identite-beneficiaire.md), [PT-05](../../03_ptisn/03_profils/pt-05-registre-professionnels.md), [PT-06](../../03_ptisn/03_profils/pt-06-referentiel-structures-services.md), [PT-07](../../03_ptisn/03_profils/pt-07-terminologie-codification.md), [PT-13](../../03_ptisn/03_profils/pt-13-qualite-reconciliation.md) |
| [ART-4A](../../02_artsn/04_patterns/art-4a-resolution-identite.md) | Résolution d'identité | [PT-04](../../03_ptisn/03_profils/pt-04-resolution-identite-beneficiaire.md), [PT-05](../../03_ptisn/03_profils/pt-05-registre-professionnels.md) |
| [ART-4B](../../02_artsn/04_patterns/art-4b-bases-autorisation.md) | Bases d'autorisation | [PT-04](../../03_ptisn/03_profils/pt-04-resolution-identite-beneficiaire.md), [PT-10](../../03_ptisn/03_profils/pt-10-confiance-authentification-autorisation.md), [PT-11](../../03_ptisn/03_profils/pt-11-consentement-bases-autorisation.md) |
| [ART-4C](../../02_artsn/04_patterns/art-4c-eligibilite-couverture.md) | Éligibilité et couverture | [PT-05](../../03_ptisn/03_profils/pt-05-registre-professionnels.md) |
| [ART-4D](../../02_artsn/04_patterns/art-4d-referentiel-geospatial.md) | Référentiel géospatial et d'exploitation partagé | [PT-15](../../03_ptisn/03_profils/pt-15-surveillance-one-health.md) |
| [ART-5](../../02_artsn/04_patterns/art-5-coherence-qualite-donnees.md) | Cohérence et qualité des données | [PT-02](../../03_ptisn/03_profils/pt-02-mediation-intra-secteur.md), [PT-06](../../03_ptisn/03_profils/pt-06-referentiel-structures-services.md), [PT-07](../../03_ptisn/03_profils/pt-07-terminologie-codification.md), [PT-08](../../03_ptisn/03_profils/pt-08-echange-donnees-agregees.md), [PT-09](../../03_ptisn/03_profils/pt-09-analytique-exposition-donnees.md), [PT-13](../../03_ptisn/03_profils/pt-13-qualite-reconciliation.md) |
| [ART-6](../../02_artsn/04_patterns/art-6-analytique-restitution.md) | Analytique et restitution | [PT-06](../../03_ptisn/03_profils/pt-06-referentiel-structures-services.md), [PT-08](../../03_ptisn/03_profils/pt-08-echange-donnees-agregees.md), [PT-09](../../03_ptisn/03_profils/pt-09-analytique-exposition-donnees.md), [PT-13](../../03_ptisn/03_profils/pt-13-qualite-reconciliation.md) |
| [ART-7](../../02_artsn/04_patterns/art-7-securite-controle-acces.md) | Sécurité, contrôle d'accès et résidence de la donnée | [PT-01](../../03_ptisn/03_profils/pt-01-echange-interinstitutionnel.md), [PT-02](../../03_ptisn/03_profils/pt-02-mediation-intra-secteur.md), [PT-04](../../03_ptisn/03_profils/pt-04-resolution-identite-beneficiaire.md), [PT-05](../../03_ptisn/03_profils/pt-05-registre-professionnels.md), [PT-09](../../03_ptisn/03_profils/pt-09-analytique-exposition-donnees.md), [PT-10](../../03_ptisn/03_profils/pt-10-confiance-authentification-autorisation.md), [PT-11](../../03_ptisn/03_profils/pt-11-consentement-bases-autorisation.md), [PT-12](../../03_ptisn/03_profils/pt-12-audit-provenance-tracabilite.md), [PT-14](../../03_ptisn/03_profils/pt-14-interopabilite-transfrontaliere.md), [PT-16](../../03_ptisn/03_profils/pt-16-orchestration-processus.md) |
| [ART-8A](../../02_artsn/04_patterns/art-8a-orchestration-processus-borne.md) | Orchestration de processus borné | [PT-16](../../03_ptisn/03_profils/pt-16-orchestration-processus.md) |
| [ART-8B](../../02_artsn/04_patterns/art-8b-modelisation-graphe.md) | Modélisation de relations en graphe | [PT-15](../../03_ptisn/03_profils/pt-15-surveillance-one-health.md) |
| [ART-8C](../../02_artsn/04_patterns/art-8c-agregation-par-lot.md) | Agrégation par lot | [PT-02](../../03_ptisn/03_profils/pt-02-mediation-intra-secteur.md) |
| [ART-8D](../../02_artsn/04_patterns/art-8d-choregraphie-interinstitutionnelle.md) | Chorégraphie inter-institutionnelle | [PT-02](../../03_ptisn/03_profils/pt-02-mediation-intra-secteur.md) |
| [ART-9](../../02_artsn/04_patterns/art-9-garanties-transactionnelles.md) | Garanties transactionnelles fortes | [PT-10](../../03_ptisn/03_profils/pt-10-confiance-authentification-autorisation.md), [PT-18](../../03_ptisn/03_profils/pt-18-echange-reclamations-paiements.md) |
| [ART-10](../../02_artsn/04_patterns/art-10-logistique.md) | Logistique | [PT-17](../../03_ptisn/03_profils/pt-17-logistique-lmis.md) |
| [ART-11](../../02_artsn/04_patterns/art-11-coordination-intersectorielle.md) | Coordination intersectorielle | [PT-01](../../03_ptisn/03_profils/pt-01-echange-interinstitutionnel.md), [PT-11](../../03_ptisn/03_profils/pt-11-consentement-bases-autorisation.md), [PT-15](../../03_ptisn/03_profils/pt-15-surveillance-one-health.md) |
| [ART-12](../../02_artsn/04_patterns/art-12-aide-decision-clinique.md) | Aide à la décision clinique | [PT-19](../../03_ptisn/03_profils/pt-19-aide-decision-clinique.md) |

## Notes

- **ART-7** (sécurité, contrôle d'accès et résidence de la donnée) concentre le plus grand nombre de profils (10), confirmant son rôle transversal dans l'ensemble du paysage.
- **ART-5** (cohérence et qualité des données) et **ART-2** (médiation et normalisation) viennent ensuite avec respectivement 6 et 6 profils, traduisant leur position dans la couche de médiation sémantique.
- **ART-8** (orchestration de processus parent) n'est déclaré par aucun profil via son champ `implements` ; les sous-chapitres ART-8A/8B/8C/8D couvrent ses cas d'usage spécialisés via PT-02, PT-15 et PT-16.
- **ART-4C** (éligibilité et couverture) est couvert par un seul profil (PT-05), ce qui est attendu car la couverture santé universelle est un service encore en phase de conception.
- La correspondance inverse (PT → chapitres ART) est disponible dans la [matrice d'alignement PTISN](../../03_ptisn/04_matrice-alignement/index.md#2-alignement-avec-lart).
- Le mapping est dérivé du champ `implements` du frontmatter de chaque profil dans `referentiel/profils/pt-XX.md`. Le champ `related` n'est pas repris car il documente des dépendances transversales et non des implémentations directes.
