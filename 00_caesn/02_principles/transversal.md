---

title: "Principes d'architecture transversaux"
id: pa
domain: 02_principles
version: "1.0.0"
status: draft
last_reviewed: 2026-07-03
owner: Comité National d'Architecture Santé Numérique
tags: ["principes", "transversaux"]
---

# Principes d'architecture transversaux

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ◐ |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.


Le cadre repose sur douze principes d'architecture transversaux. Chaque initiative numérique doit être évaluée selon sa conformité à ces principes. Chaque principe vit dans le référentiel : `referentiel/principes/pa-XX.md`.

## Catalogue des principes

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### La valeur pour la population est la finalité de tout investissement numérique

- **Signification** : aucun système, plateforme ou outil numérique n’a de valeur en soi. Sa valeur dépend de sa contribution mesurable à l’amélioration de la santé de la population, de l’accès aux soins, de la protection financière, de la santé publique ou du pilotage du système.
- **Implications** : toute initiative doit démontrer sa contribution à un bénéficiaire identifié, à un flux de valeur national, à un problème métier concret et à un indicateur de bénéfice mesurable.

*Rattachement : VS-01, VS-02, VS-03, VS-04 · fiche PA-01*

### Les flux de valeur précèdent les systèmes

- **Signification** : l’architecture numérique est dérivée des résultats que le système de santé doit produire, et non d’une liste d’applications à financer.
- **Implications** : avant de proposer une solution technique, toute initiative doit identifier le flux de valeur, l’étape ciblée, la rupture à corriger et la capabilité à renforcer.

*Rattachement : VS-01, VS-02, VS-03, VS-04 · fiche PA-02*

### Les bénéfices doivent être mesurés, pas seulement déclarés

- **Signification** : la livraison d’un outil ou d’une plateforme ne prouve pas que la valeur attendue a été produite.
- **Implications** : des indicateurs de valeur doivent être définis avant démarrage, puis suivis pendant la mise en œuvre, l’exploitation et l’évaluation.

*Rattachement : VS-01, VS-02, VS-03, VS-04 · fiche PA-03*

### Les données de santé sont un actif stratégique national

- **Signification** : les données produites par le système de santé constituent un bien stratégique national.
- **Implications** : aucun acteur ne peut contrôler, héberger ou exploiter exclusivement des données nationales sans cadre validé. Toute initiative doit garantir portabilité, sécurité, traçabilité et restitution.

*Rattachement : VS-01, VS-02, VS-03, VS-04 · fiche PA-04*

### Une donnée doit être collectée une seule fois et réutilisée plusieurs fois

- **Signification** : la multiplication des collectes parallèles crée de la charge, fragmente l’information et dégrade la qualité.
- **Implications** : avant de créer un formulaire, registre ou flux, toute initiative doit vérifier si la donnée existe déjà dans un système national ou référentiel partagé.

*Rattachement : VS-01, VS-02, VS-03, VS-04 · fiche PA-05*

### L’interopérabilité est une exigence non négociable

- **Signification** : tout système doit pouvoir échanger des données avec les autres composantes selon les standards définis.
- **Implications** : aucune solution fermée, isolée ou non interopérable ne doit être homologuée. L’interopérabilité se vérifie avant déploiement, non après.

*Rattachement : VS-01, VS-02, VS-03, VS-04 · fiche PA-06*

### Les référentiels nationaux sont des biens communs indivisibles

- **Signification** : les référentiels (formations sanitaires, agents, géographie, produits, indicateurs, bénéficiaires) doivent être partagés et maintenus comme biens communs.
- **Implications** : toute initiative utilise les référentiels existants et, pour les enrichir, utilise les mécanismes nationaux de gouvernance et de mise à jour.

*Rattachement : VS-01, VS-02, VS-03, VS-04 · fiche PA-07*

### Les systèmes doivent être soutenables sans dépendance externe permanente

- **Signification** : un système dépendant de manière durable d’un appui externe fragilise la souveraineté nationale.
- **Implications** : le coût total de possession, la maintenance, les compétences, l’hébergement, le support et la capacité de reprise nationale doivent être évalués avant tout déploiement.

*Rattachement : VS-01, VS-02, VS-03, VS-04 · fiche PA-08*

### L’architecture doit être adaptée aux réalités du terrain

- **Signification** : les systèmes doivent fonctionner dans les conditions réelles du pays : connectivité intermittente, zones rurales, littératie variable, équipements limités.
- **Implications** : toute solution de terrain intègre le mode hors ligne, la simplicité d’usage, la performance en conditions contraintes et l’accompagnement des utilisateurs.

*Rattachement : VS-01, VS-02, VS-03, VS-04 · fiche PA-09*

### La souveraineté nationale du système d’information sanitaire est non négociable

- **Signification** : le Ministère de la Santé Publique est l’autorité responsable de l’architecture, des données, des référentiels et des standards.
- **Implications** : les partenaires contribuent au système national mais ne définissent pas seuls les choix d’architecture, standards, référentiels ou plateformes structurantes.

*Rattachement : VS-01, VS-02, VS-03, VS-04 · fiche PA-10*

### La protection des données personnelles est une condition de confiance

- **Signification** : la confiance des patients et des agents dépend de la capacité à protéger les données personnelles et sensibles.
- **Implications** : sécurité, confidentialité, consentement, gestion des accès, traçabilité et droits des personnes sont intégrés dès la conception.

*Rattachement : VS-01, VS-02, VS-03, VS-04 · fiche PA-11*

### Toute initiative numérique doit être conforme au cadre national

- **Signification** : toute initiative, quelle que soit sa source de financement, doit être évaluée selon les mêmes règles.
- **Implications** : aucune initiative ne doit être financée, développée, déployée ou étendue sans alignement explicite avec le cadre, les flux, les capabilités prioritaires et l’architecture de référence technique.

*Rattachement : VS-01, VS-02, VS-03, VS-04 · fiche PA-12*

<!-- END:GENERATED -->
## Liens

- Principes de domaine
- Flux de valeur
- Normes

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Principes de domaine** : Principes de domaine par flux de valeur (`00_caesn/02_principles/domain/index.md`)
- **Flux de valeur** : Flux de valeur nationaux de santé (`00_caesn/01_value-streams/index.md`)
- **Normes** : Normes et standards d'architecture (`01_cnisn/05_standards/index.md`)
