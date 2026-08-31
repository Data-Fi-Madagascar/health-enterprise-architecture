---
domain: capacites
id: CAP-INT-15
type: capacite
niveau: "2"
title: Échange et traçabilité de la chaîne d'approvisionnement sanitaire
status: candidate
owner: DEPSI
version: "0.5"
family: logistique
envelope: 01_cnisn/02_capacites/index.md
maps_to: ["CAP-06", "CAP-10", "CAP-11", "CMP-23"]
implements: []
applies_to: []
related: ["CAP-INT-03", "CAP-INT-10"]
tags: ["cnisn", "niveau-2", "capacite", "logistique", "approvisionnement", "lmis"]
---

# Échange et traçabilité de la chaîne d'approvisionnement sanitaire

### Finalité

Permettre l'interopérabilité des données de la chaîne d'approvisionnement sanitaire (médicaments, vaccins, intrants, équipements) : catalogue produit partagé, niveaux de stock, lots et traçabilité des mouvements, afin d'éviter les ruptures et les péremptions.

### Services attendus

- catalogue produit normalisé (désignation, code, unité, seuils) ;
- remontée des niveaux de stock par établissement ;
- traçabilité des lots et des mouvements (réception, transfert, distribution) ;
- alerte de rupture et de péremption ;
- corrélation stock → consommation → épidémiologie.

### Principe de séparation

Cette capacité est distincte de la gestion logistique applicative (LMIS métier) ; elle normalise l'échange et la traçabilité inter-initatives, sans remplacer le système de gestion des stocks.

### Principes associés

- [P-INT-03: Copies locales non autoritatives](../principes/p-int-03.md)
- [P-INT-07: Responsabilité de la donnée](../principes/p-int-07.md)
- [P-INT-18: Traçabilité différenciée](../principes/p-int-18.md)

### Rattachement

- [CAP-10: Gestion des médicaments, vaccins, intrants et chaîne d'approvisionnement](../../referentiel/capabilites/cap-10.md)
- [CAP-11: Gestion des infrastructures, équipements et maintenance](../../referentiel/capabilites/cap-11.md)
- [CMP-23: LMIS (logistique)](../../referentiel/composants/cmp-23.md)
- [ART-10: Logistique](../../referentiel/chapitres/art-10.md)
- [CAP-INT-03: Échange et médiation](cap-int-03.md)
- [CAP-INT-10: Provenance, audit et traçabilité](cap-int-10.md)
