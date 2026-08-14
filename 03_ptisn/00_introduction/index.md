---
title: Préambule du PTISN
id: ptisn-introduction
domain: 03_ptisn
version: "0.4"
status: draft
last_reviewed: 2026-07-31
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "interopérabilité", "introduction"]
---

# Préambule du PTISN


## 1. Fonction du PTISN

Le PTISN (Profils techniques d'implémentation de la Santé Numérique) traduit les capacités et principes du CNISN en profils techniques utilisables par les initiatives numériques du secteur santé.

Le CNISN définit :

- les principes opposables ;
- les capacités requises ;
- les règles de gouvernance ;
- les responsabilités ;
- les mécanismes de dérogation.

L'ART définit :

- les contrats de conformité ;
- les propriétés architecturales attendues ;
- les patrons reconnus ;
- les preuves de conformité.

Le PTISN précise :

- les services nationaux attendus ;
- les standards à utiliser ;
- les profils d'échange à appliquer ;
- les versions de référence ;
- les produits ou implémentations candidats ;
- les décisions nationales déjà actées ;
- les exigences de conformité associées.

Le PTISN constitue donc le niveau auquel des standards, profils et produits peuvent être explicitement nommés.

------------------------------------------------------------------------

## 2. Position dans la hiérarchie architecturale

```plantuml
@startuml
skinparam component {
  BackgroundColor #E8F4FD
  BorderColor #2196F3
}
skinparam package {
  BackgroundColor #FFF3E0
  BorderColor #FF9800
}

package "Cadre national d'interopérabilité" as CN {
  component "Transversal à l'ensemble\nde l'administration" as CN_DESC
}

package "Cadre d'Architecture d'Entreprise\npour la Santé Numérique" as CAESN {
  component "Value streams, capacités\net gouvernance" as CAESN_DESC
}

package "CNISN" as CNISN {
  component "Principes et capacités\nd'interopérabilité" as CNISN_DESC
}

package "ARTSN" as ARTSN {
  component "Contrats et patrons\narchitecturaux" as ARTSN_DESC
}

package "PTISN" as PTISN {
  component "Services nationaux, standards,\nprofils et candidats d'implémentation" as PTISN_DESC
}

package "Spécifications propres\naux initiatives" as SPEC {
  component " " as SPEC_DESC
}

package "Systèmes homologués\net exploités" as SERV {
  component " " as SERV_DESC
}

' === Relations ===
CN --> CAESN
CAESN --> CNISN
CAESN --> ARTSN
CNISN --> PTISN
ARTSN --> PTISN
PTISN --> SPEC
SPEC --> SERV

@enduml
```

Une initiative ne doit pas recopier le PTISN dans son dossier d'architecture.

Elle doit produire un **profil technique d'initiative** indiquant :

- les services nationaux qu'elle consomme ou fournit ;
- les profils PTISN qu'elle applique ;
- les versions utilisées ;
- les produits retenus ;
- les écarts ;
- les preuves de conformité.

------------------------------------------------------------------------
