# Mémoire de projet - HEA

## Standards rédactionnels

### Qualité rédactionnelle de type Gartner

Tout document d'analyse ou de livrable produit dans ce dépôt doit respecter la **qualité rédactionnelle de type Gartner**. Cette norme implique :

#### Structure obligatoire
1. **En-tête métadonnées** : Référence, Date, Version, Objet, Sources, Statut
2. **Table des matières** numérotée avec liens
3. **Contexte et objectif** avec positionnement stratégique du document
4. **Méthodologie** détaillée (processus de collecte, conventions, limites)
5. **Synthèse quantitative** avec tableaux et analyse des tendances
6. **Analyse par domaine** avec paragraphes explicatifs
7. **Convergences inter-groupes**
8. **Points d'arbitrage**
9. **Recommandations** priorisées
10. **Annexe: Matrice de traçabilité**

#### Style rédactionnel
- **Paragraphes analytiques** après chaque en-tête de section expliquant :
  - Le contexte du domaine
  - La signification des constats
  - Les implications pour le projet
  - Les risques si non corrigé
- **Tables de verdict** en fin de section synthétisant l'impact
- **Pas de tableaux sans analyse** : chaque tableau doit être précédé ou suivi d'un commentaire
- **Vocabulaire formel** : « constitue », « révèle », « conditionne », « traduit »
- **Connecteurs logiques** : « C'est précisément », « Cette observation », « Plus fondamentalement »
- **Interdiction des caractères chinois** : ne jamais utiliser de caractères chinois (kanji, hiragana, katakana)
- **Interdiction des em-dashes** : ne pas utiliser de tirets longs. Utiliser des tirets courts (-) ou des deux-points (:) à la place
- **Interdiction des séparateurs** : ne pas utiliser de séparateurs horizontaux (---). Les sections sont séparées par des en-têtes et des paragraphes, pas par des lignes

#### Exemple de paragraphe analytique (à reproduire)
> La qualité rédactionnelle d'un document de référence nationale n'est pas un enjeu cosmétique : elle conditionne directement la **capacité d'appropriation** par les parties prenantes. Un document contenant des acronymes non définis, des glossaires incohérents ou une table des matières défectueuse est un document qui ne sera pas lu, pas compris et pas appliqué. C'est précisément le risque qui est identifié ici.

#### Documents de référence
- `feedbacks/analyse-feedbacks-caesn.md` - Modèle Gartner pour CAESN
- `feedbacks/analyse-feedbacks-cnisn.md` - Modèle Gartner pour CNISN


## Conventions du projet

- Dépôt : architecture documentée as code du secteur santé numérique de Madagascar
- Hiérarchie : CAESN (niveau 1) > CNISN (niveau 2) > ARTSN (niveau 3) > PTISN (niveau 4)
- Langue : français
- Noms de dossiers : kebab-case anglais avec préfixe numérique
- Domain : nom du dossier parent immédiat avec préfixe numérique
