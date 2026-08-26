---

title: "Partie IV : Conformité"
id: cnisn-conformite
domain: 04_conformite
version: "1.0.0"
status: draft
last_reviewed: 2026-08-18
owner: DEPSI
tags: ["cnisn", "niveau-2", "interopérabilité", "conformite"]
---


# Partie IV : Conformité


## 1. Profil de conformité d'une initiative

Toute initiative de santé numérique doit produire un profil de conformité indiquant les principes applicables, les capacités qu'elle fournit et celles qu'elle consomme, les contrats ART applicables, les profils PTISN utilisés, les services exposés, les données échangées, les sources autoritatives mobilisées, les preuves de conformité produites et les dérogations éventuellement accordées.

## 2. Dossier minimal

Le dossier de conformité comprend une note de concept justifiant l'initiative, un rattachement aux value streams et capacités du CAESN, les architectures fonctionnelle, des données, applicative et technique, les contrats d'échange, les matrices des responsabilités et des données, le modèle de sécurité, la politique de conservation, la stratégie d'exploitation et de réversibilité, les résultats de tests, et la déclaration de conformité finale.

## 3. Critères de conformité

La revue de conformité porte sur l'autorité des données, la contractualisation, le versionnement, la sécurité, la minimisation, la résidence, la portabilité, la qualité, la réconciliation, l'exploitabilité, la continuité, le coût total de possession et l'alignement stratégique.

### 3.1 Autorité d'homologation et articulation des critères

L'homologation est de la compétence unique du **CNASN**, qui instruit et statue. Le **sous-comité d'interopérabilité sectoriel santé** prépare la revue sectorielle et remonte au CNASN (voir `01_cnisn/03_gouvernance/index.md` §3). Aucune instance ne peut délivrer une homologation concurrente.

Les critères ci-dessus (13) sont la **déclinaison opérationnelle** d'un même référentiel appliqué à trois niveaux normatifs. Ils ne sont pas redondants mais complémentaires par couche :

| Couche | Source | Nature des critères | Rôle |
|--------|--------|--------------------|------|
| Niveau 3 — ARTSN | `02_artsn/06_gouvernance/index.md` (Rôle du CNASN) | 5 critères qualitatifs : ouverture, alignement normatif, interopérabilité, souveraineté des données, coût total de possession | Portes architecturales ; deviennent des vérifications techniques contre les chapitres ART au statut *Stable* |
| Niveau 2 — CNISN | ce document §3 | 13 dimensions de conformité | Grille d'instruction détaillée par initiative |
| Niveau 1 — CAESN | `00_caesn/07_governance/homologation.md` (checklist C1–C16) | 12 critères obligatoires + 4 complémentaires, orientés portefeuille | Checklist d'admission de l'initiative (migration, KPI, TCO) |

**Mapping ARTSN (5) → CNISN (13) :**

| Critère ARTSN | Dimensions CNISN couvertes |
|---------------|----------------------------|
| Ouverture | Exploitabilité, Continuité, Portabilité |
| Alignement normatif | Autorité des données, Contractualisation, Versionnement, Alignement stratégique |
| Interopérabilité | Qualité, Réconciliation, Portabilité |
| Souveraineté des données | Résidence, Sécurité, Minimisation |
| Coût total de possession | Coût total de possession |

Tout écart à un critère CNISN doit être documenté comme une **dérogation explicite et justifiée** (voir `01_cnisn/03_gouvernance/index.md` §2.5), et non constaté silencieusement après déploiement.

## 4. Homologation

Une initiative peut recevoir l'un des statuts suivants : non évaluée lorsqu'aucun examen formel n'a été réalisé, en revue lorsque le dossier est en cours d'instruction, pilote autorisé pour une mise en œuvre limitée et encadrée, conforme sous conditions lorsque des écarts limités sont identifiés avec un plan de correction, conforme lorsque toutes les exigences applicables sont démontrées, suspendue en cas de risque ou de non-conformité majeure, et retirée lorsque le service ou le système n'est plus autorisé.

## 5. Homologation conditionnelle

Une homologation conditionnelle doit préciser les écarts identifiés, les risques associés, les mesures compensatoires mises en place, le responsable désigné, l'échéance de correction, les conditions de retrait et les preuves attendues pour régulariser la situation.

## 6. Réévaluation

La conformité doit être réévaluée de manière périodique, après une version majeure du système, après un incident critique, après une nouvelle intégration, après un changement de propriétaire ou de données, et à l'expiration d'une dérogation.

## 7. Programme de conformité opérationnel

L'instruction des critères ci-dessus est opérationnalisée par le **programme de conformité** (`programme-conformite.md`), qui définit les tests, les acteurs, les sanctions et le jalon de démarrage.

## Documents de la section

- [cnisn-programme-conformite: Partie IV bis : Programme de conformité opérationnel](programme-conformite.md)

<!-- liens-section-auto -->
