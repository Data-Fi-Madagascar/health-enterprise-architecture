---
id: enf-5
type: exigence
niveau: "3"
title: ENF-5 — Coordination des processus complexes décentralisés et asynchrones
status: draft
owner: DEPSI
version: "0.1"
source: 02_artsn/02_exigences-contextuelles.md
maps_to: []
implements: []
applies_to: []
related: ["art-8a", "art-8", "art-5", "pt-14"]
tags: ['artsn', 'niveau-3', 'exigence', 'enf-5']
---
# ENF-5 — Coordination des processus complexes décentralisés et asynchrones

**Contraintes contextuelles.** Les parcours de soins critiques (référence d'un CSB rural vers un hôpital de district, contre-référence ascendante vers un CHU central, ou évacuation sanitaire internationale) s'étendent sur des fenêtres temporelles de plusieurs jours et impliquent des structures sanitaires autonomes sans lien hiérarchique ou technique direct.

**Contenu normatif.** Le système national doit être capable de suivre et d'orchestrer l'état d'avancement d'un parcours de soins distribué à étapes multiples, de bout en bout. L'architecture doit tolérer les interruptions temporaires de transmission, tout en garantissant le déclenchement automatique d'alertes d'escalade ou d'annulations (compensations) fonctionnelles si un établissement de destination est saturé ou inaccessible.

**Statut : Stable.** — appliqué par [ART-8a (orchestration de processus borné)](../chapitres/art-8a.md), [ART-5 (qualité des données)](../chapitres/art-5.md), [PT-14 (interopérabilité transfrontalière)](../../03_ptisn/03_profils/pt-14-interopabilite-transfrontaliere.md).
