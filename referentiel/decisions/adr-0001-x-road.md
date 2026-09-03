---

title: "ADR-0001 : Adoption de X-Road comme plateforme d'échange interinstitutionnel"
id: adr-0001
domain: decisions
type: decision
version: "1.0.0"
status: accepted
date: 2026-07-01
owner: DEPSI
tags: ["adr", "interopérabilité", "x-road", "plateforme"]
related: ["PT-01"]
---

# ADR-0001 : Adoption de X-Road comme plateforme d'échange interinstitutionnel

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ▸ |
| Directions métier / programmes | ◼ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ▸ |
| Partenaires techniques et financiers | ▸ |

Légende : ● prioritaire · ▸ complémentaire · ◼ ponctuelle. Vue d'ensemble : matrice de lecture.

- **Statut** : accepté
- **Date** : 2026-07-01
- **Groupe concerné** : DEPSI, UGD, Ministère de la Santé

## Contexte

Le système d'information sanitaire national doit échanger des données avec de multiples systèmes interministériels : état civil, registre de la population, protection sociale, finances publiques, éducation et collectivités territoriales. 

Le CNISN (Cadre National d'Interopérabilité de la Santé Numérique) exige un mécanisme d'échange sécurisé entre organisations membres, conforme au CNI (Cadre National d'Interopérabilité).

## Décision

Adopter **X-Road** comme plateforme d'échange interinstitutionnel pour les échanges entre le secteur santé et les autres secteurs de l'État.

## Justification

X-Road répond aux exigences du CNISN :

- **P-INT-01 à P-INT-04** : Autorité des données et gouvernance inter-organisations
- **P-INT-18** : Traçabilité des échanges
- **P-INT-19** : Neutralité technologique (open source)
- **P-INT-20** : Sécurité des échanges (chiffrement, authentification)
- **P-INT-21** : Interopérabilité sémantique

### Avantages spécifiques

1. **Maturité** : Solution éprouvée (utilisée en Estonie, Finlande, et d'autres pays)
2. **Sécurité** : Chiffrement de bout en bout, authentification forte
3. **Flexibilité** : Support de multiples protocoles (REST, SOAP, etc.)
4. **Gouvernance** : Modèle de gouvernance clair pour les échanges inter-organisations
5. **Open Source** : Licence MIT, pas de dépendance à un fournisseur

## Conséquences

### Positives
- **Standardisation** : Alignement avec les standards internationaux d'interopérabilité
- **Sécurité** : Renforcement de la sécurité des échanges de données de santé
- **Évolutivité** : Capacité à gérer un volume croissant d'échanges
- **Interopérabilité** : Facilitation de l'intégration avec les systèmes existants

### Négatives / Risques
- **Complexité** : Courbe d'apprentissage pour les équipes techniques
- **Infrastructure** : Nécessité de déployer et maintenir l'infrastructure X-Road
- **Formation** : Besoin de former les équipes à l'utilisation de X-Road

### Mitigation des risques
- **Formation** : Programme de formation complet pour les équipes techniques
- **Support** : Partenariat avec les experts X-Road pour le support
- **Documentation** : Documentation complète et adaptée au contexte malgache

## Alternatives envisagées

| Alternative | Avantages | Inconvénients | Décision |
|-------------|-----------|---------------|----------|
| **API Gateway custom** | Contrôle total, flexibilité | Coût de développement élevé, maintenance complexe | Rejetée |
| **MuleSoft** | Solution entreprise, support commercial | Coût de licence élevé, dépendance fournisseur | Rejetée |
| **Apache Camel** | Open source, flexible | Complexité de configuration, moins adapté aux échanges inter-organisations | Rejetée |
| **HAPI FHIR** | Spécialisé pour la santé | Limité aux échanges FHIR, pas adapté aux échanges interministériels | Rejetée |

## Références
- [X-Road Official Documentation](https://x-road.global/)
- [CNI - Cadre National d'Interopérabilité](https://www.cni.mg)
- [CNISN - Cadre National d'Interopérabilité de la Santé Numérique](https://www.cnisn.mg)
- [PT-01 : Échange interinstitutionnel](../../03_ptisn/03_profils/pt-01-echange-interinstitutionnel.md)
- [Lot L3 : Médiation & registres](../../02_artsn/07_lots/index.md)
- [Lot L7 : Sécurité & conformité](../../02_artsn/07_lots/index.md)
