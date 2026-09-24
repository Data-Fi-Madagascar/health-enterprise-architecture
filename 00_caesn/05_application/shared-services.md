---

title: Services numériques partagés prioritaires
id: application-shared-services
domain: 05_application
version: "1.0.0"
status: draft
last_reviewed: 2026-07-03
owner: Direction des Systèmes d'Information
tags: ["applications", "services-partagés"]
---

# Services numériques partagés prioritaires

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

Certains services doivent être conçus comme des services nationaux partagés, réutilisables par plusieurs applications. Ils sont réutilisés par défaut ; la création d'un service parallèle doit être justifiée, limitée et validée par la gouvernance.

| Service partagé | Rôle | Applications consommatrices |
|-----------------|------|------------------------------|
| Service d'identité patient / bénéficiaire | Identifier fiablement les patients et bénéficiaires pour la continuité et la protection | Dossier patient, CSU, référence, surveillance, entrepôt |
| Service d'identité agent de santé | Identifier les professionnels, rôles, affectations, droits d'accès | RH santé, dossier patient, surveillance, logistique, tableaux de bord |
| Référentiel FOSA | Identifier les structures et leurs caractéristiques | Tous les systèmes métier |
| Référentiel géographique | Harmoniser les zones administratives et sanitaires | Surveillance, planification, tableaux de bord, logistique, CSU |
| Référentiel produits de santé | Harmoniser médicaments, vaccins, intrants, consommables | Logistique, vaccination, FOSA, entrepôt |
| Référentiel indicateurs | Définitions communes et stables des indicateurs | DHIS2/HMIS, tableaux de bord, entrepôt, portefeuille |
| Service d'authentification et gestion des accès | Contrôler l'accès selon les rôles | Toutes les applications nationales |
| Service de notification | Envoyer alertes, rappels, messages opérationnels | Vaccination, référence, surveillance, CSU, supervision |
| Catalogue des API et contrats d'interface | Documenter les échanges autorisés | Applications métier, couche d'échange, intégrateurs |
| Registre national des initiatives numériques | Suivre projets, financements, partenaires, bénéfices | Gouvernance, portefeuille, VRO, Comité |

## Composants des services partagés

<!-- BEGIN:GENERATED source=04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-12.md,04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-13.md -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### Registre d'éligibilité et de couverture (CSU — ART-4C)

**Contenu normatif.** Ce composant gère les données d'éligibilité et de couverture santé (CSU). Il assure la vérification en temps réel des droits des patients et fournit les services de contrôle d'éligibilité pour les applications métier.

**Discipline de mise en œuvre.** Il est l'autorité de vérification des droits. Toute opération de soins nécessitant une vérification de couverture transite par ce registre, ce qui garantit la conformité financière.

- **Rattachement** : [ART-4C](../../04_architecture-repository/04_patterns/artsn-rules/art-4c.md) (éligibilité/couverture), [ABB-GESTION-CONSENTEMENT: Gestion des consentements et bases d’autorisation](../../04_architecture-repository/05_building-blocks/abb/abb-gestion-consentement.md).
- **Processus soutenus** : [PRC-09: Remboursement et régulation des mécanismes](../../04_architecture-repository/02_architecture-elements/business/processes/prc-09.md) (finance), [PRC-10: Planification et allocation des ressources](../../04_architecture-repository/02_architecture-elements/business/processes/prc-10.md) (planification).
- **Statut : Stable.**

### Registre des personnels

**Contenu normatif.** Ce composant gère les données des personnels de santé (identités, qualifications, affectations). Il assure la traçabilité des interventions et des responsabilités, et fournit les services de recherche et d'identification des personnels.

**Discipline de mise en œuvre.** Il constitue le référentiel de référence pour l'identification des intervenants. Toute intervention médicale enregistre l'identité du personnel via ce registre, ce qui garantit la traçabilité et la responsabilité.

- **Rattachement** : [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md) (référentiel des métadonnées), [ABB-GESTION-CONSENTEMENT: Gestion des consentements et bases d’autorisation](../../04_architecture-repository/05_building-blocks/abb/abb-gestion-consentement.md).
- **Processus soutenus** : [PRC-04: Veille, prévention et surveillance sanitaire](../../04_architecture-repository/02_architecture-elements/business/processes/prc-04.md) (soins), [PRC-05: Alerte, investigation et riposte](../../04_architecture-repository/02_architecture-elements/business/processes/prc-05.md) (pharmacie).
- **Statut : Stable.**

<!-- END:GENERATED -->
## Liens

- Paysage applicatif cible
- Domaines applicatifs
- Référentiels nationaux

## Références

- [matrice de lecture](../reading-matrix.md)
- [VS-01](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-01.md)
- [VS-02](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-02.md)
- [VS-03](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-03.md)
- [VS-04](../../04_architecture-repository/02_architecture-elements/strategy/value-streams/vs-04.md)
- [PRC-01](../../04_architecture-repository/02_architecture-elements/business/processes/prc-01.md)
- [PRC-07](../../04_architecture-repository/02_architecture-elements/business/processes/prc-07.md)
- [PRC-10](../../04_architecture-repository/02_architecture-elements/business/processes/prc-10.md)
- [ABB-REGISTRE-PROFESSIONNELS](../../04_architecture-repository/05_building-blocks/abb/abb-registre-professionnels.md)
- [ABB-REFERENTIEL-STRUCTURES-SERVICES](../../04_architecture-repository/05_building-blocks/abb/abb-referentiel-structures-services.md)
- [ABB-SERVICE-TERMINOLOGIE](../../04_architecture-repository/05_building-blocks/abb/abb-service-terminologie.md)
- [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md)
- [ART-4D](../../04_architecture-repository/04_patterns/artsn-rules/art-4d.md)
- [fiche](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-12.md)
- [PRC-05](../../04_architecture-repository/02_architecture-elements/business/processes/prc-05.md)
- [PRC-09](../../04_architecture-repository/02_architecture-elements/business/processes/prc-09.md)
- [ABB-IDENTITE-BENEFICIAIRE](../../04_architecture-repository/05_building-blocks/abb/abb-identite-beneficiaire.md)
- [ABB-CATALOGUE-CONTRATS](../../04_architecture-repository/05_building-blocks/abb/abb-catalogue-contrats.md)
- [ABB-CONFIANCE-AUTORISATION](../../04_architecture-repository/05_building-blocks/abb/abb-confiance-autorisation.md)
- [ABB-GESTION-CONSENTEMENT](../../04_architecture-repository/05_building-blocks/abb/abb-gestion-consentement.md)
- [ART-1](../../04_architecture-repository/04_patterns/artsn-rules/art-1.md)
- [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md)
- [ART-4A](../../04_architecture-repository/04_patterns/artsn-rules/art-4a.md)
- [ART-4B](../../04_architecture-repository/04_patterns/artsn-rules/art-4b.md)
- [ART-7](../../04_architecture-repository/04_patterns/artsn-rules/art-7.md)
- [Paysage applicatif cible](layers.md)
- [Domaines applicatifs](application-domains.md)
- [Référentiels nationaux](../04_data/referentials.md)
