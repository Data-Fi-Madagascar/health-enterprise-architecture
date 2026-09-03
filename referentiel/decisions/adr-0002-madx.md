---

title: "ADR-0002 : Adoption du profil IHE mADX pour l'échange de données agrégées"
id: adr-0002
domain: decisions
type: decision
version: "1.0.0"
status: accepted
date: 2026-07-01
owner: DEPSI
tags: ["adr", "ihe", "madx", "données-agregées", "échange"]
related: ["PT-08"]
---

# ADR-0002 : Adoption du profil IHE mADX pour l'échange de données agrégées

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ▸ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ▸ |

Légende : ● prioritaire · ▸ complémentaire · ◼ ponctuelle. Vue d'ensemble : matrice de lecture.

- **Statut** : accepté
- **Date** : 2026-07-01
- **Groupe concerné** : DEPSI, UGD, Ministère de la Santé

## Contexte

Le système d'information sanitaire national doit permettre l'échange de données de santé agrégées entre différentes institutions et partenaires. Ces données agrégées sont essentielles pour :

- La planification stratégique des services de santé
- Le suivi-évaluation des programmes de santé publique
- La recherche épidémiologique et la veille sanitaire
- La prise de décision basée sur des preuves

Le CNISN exige un standard pour structurer et échanger ces données agrégées de manière interopérable.

## Décision

Adopter **IHE mADX (Mobile Aggregate Data Exchange)** comme standard pour l'échange de données agrégées dans le système de santé national.

## Justification

IHE mADX répond aux exigences du CNISN :

- **P-INT-05** : Standardisation des formats d'échange
- **P-INT-06** : Interopérabilité sémantique
- **P-INT-19** : Neutralité technologique
- **P-INT-21** : Interopérabilité avec les standards internationaux

### Avantages spécifiques

1. **Standard international** : Reconnue par IHE International et adoptée dans de nombreux pays
2. **Flexibilité** : Support de différents types de données agrégées (statistiques, indicateurs, etc.)
3. **Extensibilité** : Capacité à définir des extensions spécifiques au contexte malgache
4. **Intégration** : Compatible avec d'autres profils IHE (FHIR, etc.)
5. **Open Standard** : Spécification ouverte, sans coût de licence

## Conséquences

### Positives
- **Normalisation** : Standardisation des échanges de données agrégées
- **Interopérabilité** : Facilitation de l'intégration avec les systèmes existants
- **Qualité des données** : Amélioration de la qualité et de la comparabilité des données
- **Efficacité** : Réduction des coûts de développement et de maintenance

### Négatives / Risques
- **Complexité** : Courbe d'apprentissage pour la mise en œuvre de mADX
- **Adaptation** : Nécessité d'adapter le profil aux besoins spécifiques de Madagascar
- **Formation** : Besoin de former les équipes à l'utilisation de mADX

### Mitigation des risques
- **Formation** : Programme de formation spécifique à mADX
- **Support** : Collaboration avec les experts IHE pour le support technique
- **Documentation** : Développement de guides de mise en œuvre adaptés au contexte local
- **Pilotes** : Mise en œuvre progressive via des projets pilotes

## Alternatives envisagées

| Alternative | Avantages | Inconvénients | Décision |
|-------------|-----------|---------------|----------|
| **CSV/Excel** | Simplicité, familiarité | Pas de sémantique, problèmes d'interopérabilité | Rejetée |
| **FHIR Aggregates** | Standard moderne, flexible | Moins mature pour les données agrégées | Rejetée |
| **HL7 v2** | Large adoption | Complexe, pas optimisé pour l'agrégation | Rejetée |
| **Custom XML/JSON** | Flexibilité totale | Pas de standard, maintenance complexe | Rejetée |
| **SDMX** | Standard pour données statistiques | Trop générique, pas adapté à la santé | Rejetée |

## Références
- [IHE mADX Profile](https://wiki.ihe.net/index.php/Mobile_Aggregate_Data_Exchange_(mADX))
- [IHE International](https://www.ihe.net/)
- [PT-08 : Échange de données agrégées](../../03_ptisn/03_profils/pt-08-echange-donnees-agregees.md)
- [CAP-08 : Analyse et reporting des données de santé](../capabilites/cap-08.md)
