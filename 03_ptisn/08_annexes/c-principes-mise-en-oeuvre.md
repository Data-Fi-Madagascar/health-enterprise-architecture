---

title: "Annexe C : Principes de mise en œuvre"
id: ptisn-annexe-c
domain: 08_annexes
version: "1.0.0"
status: draft
last_reviewed: 2026-07-31
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "annexes"]
---


# Annexe C : Principes de mise en œuvre

Les principes énoncés ci-dessous guident la mise en œuvre technique du PTISN. Ils établissent les distinctions conceptuelles fondamentales, les règles d'assemblage des profils et les garde-fous d'architecture qui doivent être respectés par chaque initiative.

Un service national ne doit pas être confondu avec le produit qui l'implémente, car le premier désigne une capacité applicative partagée et gouvernée, tandis que le second renvoie à une solution technique spécifique susceptible d'évoluer ou d'être remplacée. De même, un standard ne constitue pas à lui seul une architecture complète : il définit un contrat d'interface ou un modèle de données, mais l'architecture résulte de l'assemblage coordonné de plusieurs standards et profils. Tout profil d'échange doit être versionné afin de garantir la compatibilité ascendante et de documenter les évolutions au fil du temps.

Une technologie ne prouve pas à elle seule la conformité : l'adoption d'un produit spécifique (par exemple OpenHIM ou X-Road) ne dispense pas de valider la conformité aux profils d'interopérabilité et aux exigences fonctionnelles. X-Road ne remplace pas la médiation sectorielle, qui assure la transformation sémantique et le routage intelligent des messages, pas plus que la médiation sectorielle ne remplace les services métier chargés de la logique applicative. mADX concerne exclusivement les données agrégées et non la terminologie, qui relève de SVCM. SVCM constitue le profil cible pour la terminologie partagée, tandis que mCSD est le profil cible pour les structures, services et annuaires associés. PIXm et PDQm sont les profils cibles des nouvelles interfaces de résolution d'identité, et l'identité du patient est distincte de l'identité professionnelle, tout comme l'authentification, le registre professionnel et l'autorisation constituent des services distincts.

AuditEvent, Provenance, événements métier et logs techniques ne doivent pas être confondus : chacun répond à un besoin spécifique de traçabilité et de preuve. Le pattern CQRS n'implique pas automatiquement l'Event Sourcing, et la plateforme RMA est une première implémentation, non un modèle obligatoire pour toutes les initiatives. Les profils provisoires doivent être testés avant d'être rendus opposables, et toute extension nationale doit être documentée et publiée. Enfin, toute initiative doit disposer d'une stratégie de réversibilité permettant de substituer ou de remplacer les composants sans interrompre le service.

1. Un service national ne doit pas être confondu avec le produit qui l'implémente.
2. Un standard ne constitue pas une architecture complète.
3. Un profil d'échange doit être versionné.
4. Une technologie ne prouve pas à elle seule la conformité.
5. X-Road ne remplace pas la médiation sectorielle.
6. La médiation sectorielle ne remplace pas les services métier.
7. mADX concerne les données agrégées et non la terminologie.
8. SVCM est le profil cible pour la terminologie partagée.
9. mCSD est le profil cible pour les structures, services et annuaires associés.
10. PIXm et PDQm sont les profils cibles des nouvelles interfaces de résolution d'identité.
11. L'identité du patient et l'identité professionnelle sont deux domaines distincts.
12. L'authentification, le registre professionnel et l'autorisation sont des services distincts.
13. AuditEvent, Provenance, événements métier et logs techniques ne doivent pas être confondus.
14. CQRS n'implique pas automatiquement l'Event Sourcing.
15. La plateforme RMA est une première implémentation, non un modèle obligatoire pour toutes les initiatives.
16. Les profils provisoires doivent être testés avant d'être rendus opposables.
17. Toute extension nationale doit être documentée et publiée.
18. Toute initiative doit disposer d'une stratégie de réversibilité.
