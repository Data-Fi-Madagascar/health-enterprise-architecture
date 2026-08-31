# Guide de Conception ODA — Ontology-Driven Architecture

## 1. Principe fondamental : deux modèles, un pont

L'architecture ODA du référentiel HEA repose sur la séparation claire de deux modèles qui coexistent via un **pont de compilation automatisé** :

```
┌─────────────────────────────────────────────────────────────────┐
│                    MODÈLE DE GOUVERNANCE                        │
│                    (Méta-schéma d'auteur)                       │
│                                                                 │
│  Source : YAML/Markdown dans referentiel/                       │
│  Validateur : ontologie/hea-governance-schema.json              │
│  Usage : validation des fichiers d'architecture sur GitHub      │
│  Contraintes : id, version, status, owner, artRef, x-hea-*     │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           │ scripts/compilers/compile_oda.py
                           │ (pont de compilation)
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    MODÈLE D'IMPLÉMENTATION                      │
│                    (Schéma d'exécution / Payload)                │
│                                                                 │
│  Source : généré automatiquement                                │
│  Validateurs :                                                  │
│    - 03_ptisn/schemas/payloads/*.json (JSON Schema Draft-07)    │
│    - 03_ptisn/schemas/terminologies/*.json (FHIR R4)           │
│    - 03_ptisn/schemas/openapi/*.json (OpenAPI 3.0)             │
│  Usage : validation des messages REST en production             │
│  Contraintes : types, formats, cardinalités, terminologies      │
└─────────────────────────────────────────────────────────────────┘
```

## 2. Arborescence physique du dépôt

```
hea/
├── referentiel/                          # SOURCE DE VÉRITÉ (Niveau 3)
│   ├── objets-de-donnees/
│   │   ├── do-01.md ... do-31.md        # Objets de données (YAML/MD)
│   │   └── nomenclatures/               # NOUVEAU : nomenclatures autonomes
│   │       └── fosa-status.md           #   Statut opérationnel FOSA
│   └── profils/
│       ├── pt-06.md                     # Profil mCSD
│       └── pt-07.md                     # Profil SVCM
│
├── ontologie/                            # PONT SÉMANTIQUE
│   ├── hea.ttl                           # Ontologie OWL (ArchiMate 3.1)
│   ├── hea-shapes.ttl                   # SHACL shapes (gouvernance)
│   └── hea-governance-schema.json       # NOUVEAU : JSON Schema gouvernance
│
├── 03_ptisn/schemas/                     # SCHÉMAS D'IMPLÉMENTATION (Niveau 4)
│   ├── payloads/                        # NOUVEAU : schémas de payload
│   │   ├── fosa-status.json             #   JSON Schema pour messages REST
│   │   └── ...
│   ├── terminologies/                   # NOUVEAU : ressources FHIR
│   │   ├── hea-fosa-status-cs.json      #   CodeSystem FHIR R4
│   │   └── ...
│   └── openapi/                         # NOUVEAU : spécifications API
│       ├── pt-06-mcsd.json             #   OpenAPI 3.0 pour mCSD
│       └── pt-07-svcm.json             #   OpenAPI 3.0 pour SVCM
│
├── scripts/compilers/                    # PONT DE COMPILATION
│   ├── compile_oda.py                   # NOUVEAU : compilateur principal
│   ├── compile_fhir.py                  # Existant : FHIR R4
│   ├── compile_jsonschema.py            # Existant : JSON Schema
│   └── compile_openapi.py              # Existant : OpenAPI 3.0
│
└── dist/                                 # ARTÉFACTS GÉNÉRÉS (gitignorés)
    ├── schemas/
    ├── fhir/
    └── openapi/
```

## 3. Modèle de Gouvernance (Méta-schéma)

Le méta-schéma valide les fichiers d'auteur YAML/Markdown sur GitHub.

### 3.1 Obligations de gouvernance

| Champ | Type | Obligatoire | Description |
|-------|------|-------------|-------------|
| `id` | string | Oui | Identifiant stable (ex: `FOSA-STATUS`) |
| `title` | string | Oui | Titre canonique |
| `type` | enum | Oui | Type d'objet (nomenclature, objet-de-donnees, profil) |
| `status` | enum | Oui | draft, active, stable, candidate, deprecated |
| `version` | string | Oui | Semver (ex: `1.0.0`) |
| `owner` | string | Oui | Entité responsable (DEPSI, équipes techniques) |
| `domain` | string | Oui | Domaine du dossier parent |
| `niveau` | integer | Oui | Niveau hiérarchique (1-5) |

### 3.2 Obligations d'urbanisation

| Champ | Type | Obligatoire | Description |
|-------|------|-------------|-------------|
| `artRef` | array | Oui | Chapitres ARTSN concernés |
| `maps_to` | array | Oui | Capacités CNISN implémentées |
| `implements` | array | Oui | Standards/fondations implémentés |
| `related` | array | Non | Objets liés |
| `tags` | array | Oui | Étiquettes de catégorisation |

## 4. Modèle d'Implémentation (Payload)

Les schémas de payload valident les données réelles en transit.

### 4.1 JSON Schema Draft-07

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "FOSA Status",
  "type": "string",
  "enum": ["actif", "inactif", "temporaire", "ferme"],
  "description": "Statut opérationnel d'une formation sanitaire"
}
```

### 4.2 FHIR R4 CodeSystem

```json
{
  "resourceType": "CodeSystem",
  "id": "hea-fosa-status",
  "url": "https://healmadagascar.mg/fhir/CodeSystem/hea-fosa-status",
  "status": "active",
  "content": "complete",
  "concept": [...]
}
```

## 5. Pipeline de compilation

```
Auteur humain                    Pont de compilation              Schémas d'exécution
(YAML/Markdown)                  (Python automatisé)              (JSON/FHIR/OpenAPI)

fosa-status.md  ──────────────►  compile_oda.py  ──────────────►  fosa-status.json
                                  │                                hea-fosa-status-cs.json
                                  │                                fosa-status-openapi.json
                                  │
                                  ├── lecture frontmatter YAML
                                  ├── extraction des codes
                                  ├── génération JSON Schema
                                  ├── génération FHIR CodeSystem
                                  └── validation SPARQL/SHACL
```

## 6. Contraintes de validation

### 6.1 Gouvernance (méta-schéma)

- Chaque fichier doit avoir un `id` unique
- Le `status` doit être dans la liste contrôlée
- La `version` doit être au format semver
- L'`owner` doit être une entité connue
- Les `artRef` doivent pointer vers des chapitres existants
- Les `maps_to` doivent pointer vers des capacités existantes

### 6.2 Implémentation (JSON Schema)

- Les codes doivent être dans la nomenclature définie
- Les formats (date, email, téléphone) doivent être respectés
- Les cardinalités (min/max) doivent être respectées
- Les dépendances entre champs doivent être vérifiées

### 6.3 Sémantique (SPARQL/SHACL)

- Chaque nomenclature doit être rattachée à un chapitre ARTSN
- Chaque code doit avoir un libellé et une description
- Les nomenclatures ne doivent pas être orphelines
- Les versions doivent être cohérentes entre elles
