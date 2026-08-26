---

title: "Annexe D : Principes de lecture"
id: cnisn-annexe-d
domain: 08_annexes
version: "1.0.0"
status: draft
last_reviewed: 2026-08-18
owner: DEPSI
tags: ["cnisn", "niveau-2", "annexes"]
---


# Annexe D : Principes de lecture


Le CNISN fixe ce qui doit être garanti dans les échanges de données de santé. L'ARTSN fixe les contrats et patrons architecturaux permettant de le garantir. Le PTISN fixe les standards, profils et implémentations candidats pour réaliser ces contrats.

Une autorité nationale n'implique pas toujours une base physique unique : elle signifie qu'une règle non ambiguë détermine qui fait autorité et quelle donnée fait foi. Les copies locales sont autorisées lorsqu'elles restent non autoritatives et sont soumises à des politiques de synchronisation et d'expiration. Une interface technique ne remplace pas un accord de gouvernance : l'interopérabilité organisationnelle précède toujours l'interopérabilité technique.

Le consentement n'est pas l'unique base d'autorisation : il coexiste avec le mandat de soins, le mandat de santé publique, l'obligation légale et l'intérêt vital. Une technologie ne prouve pas la conformité : c'est l'ensemble des preuves (contrats, résultats de tests, mesures de sécurité) qui détermine la conformité. La conformité doit être fondée sur des preuves vérifiables, et non sur des déclarations narratives.

Une dérogation doit être explicite, limitée dans le temps et assortie de mesures compensatoires. Une urgence peut accélérer la procédure, mais ne supprime pas la gouvernance : la dérogation d'urgence doit être régularisée après l'événement. La portabilité et la réversibilité sont obligatoires pour les services critiques : toute initiative doit prévoir la récupération de ses données et la migration vers une autre implémentation.

Les événements métier, la provenance des données, l'audit et les logs techniques sont distincts et ne doivent pas être confondus, même s'ils peuvent être corrélés. Les services nationaux doivent disposer d'un propriétaire et d'un modèle d'exploitation : une capacité sans propriétaire n'est pas considérée comme disponible. Enfin, l'interopérabilité est une capacité de gouvernance autant qu'une capacité technique : elle repose autant sur des accords institutionnels que sur des protocoles de communication.
