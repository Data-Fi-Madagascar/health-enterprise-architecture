# Migration étapes de valeur / processus métier — Plan d'implémentation

> **Note :** Document historique de planification. La structure du dépôt a été refactorisée ; les liens internes font référence à des chemins obsolètes. Ce document est conservé à titre d'archive.

> **Pour les travailleurs agentiques :** sous-skill requis — utiliser superpowers:subagent-driven-development (recommandé) ou superpowers:executing-plans pour exécuter ce plan tâche par tâche. Les étapes utilisent la syntaxe case à cocher (`- [ ]`).

**Objectif :** transformer les 28 objets « processus métier » actuels (copies 1:1 des étapes des tableaux CAESN) en 28 objets `etape-valeur` (`ev-01…28`) et créer 12 vrais objets `processus-metier` (`PRC-01…12`, 3 par flux de valeur) qui les regroupent, en réaffectant les 13 composants applicatifs au niveau processus.

**Architecture :** le référentiel reste la source de vérité ; les enveloppes (`00_caesn/…`) en sont la projection générée. Le type `processus-metier` devient une couche de régroupement au-dessus des étapes (rattachement Per-VS, contenu strictement dérivé). Deux commits atomiques chacun vert : (1) renommage mécanique `prc→ev` + ré-ancrage des blocs « Étapes de valeur » ; (2) création des 12 processus + bloc « Processus métier » + réaffectation sémantique des composants.

**Tech stack :** Markdown + frontmatter YAML, Python 3 stdlib (scripts de migration ponctuels), `scripts/build_wrappers.py` (génération d'enveloppes), `scripts/check_links.py`, Makefile.

**Documents de référence :**
- Design validé : `docs/superpowers/specs/2026-08-12-etapes-vs-processus-design.md`
- Conventions de transclusion : `docs/superpowers/specs/2026-08-11-enveloppes-lisibilite-design.md`
- Règles du dépôt : `AGENTS.md`

---

## Commandes de vérification (à répéter à chaque jalon)

| Commande | Sortie attendue |
|----------|-----------------|
| `make check` | exit 0 — « 54 enveloppes à jour », « 0 lien relatif cassé » |
| `ruby /tmp/validate_ref.rb` | 213 fichiers / 212 ids, 2 erreurs méta connues (`_schema.md`), 0 lien cassé, 0 relation non résolue |
| `python3 /tmp/trace_check.py` | tous les objets tracés (213 à la fin) |

> Si `/tmp/validate_ref.rb` ou `/tmp/trace_check.py` a disparu, refaire uniquement `make check` et signaler.

---

## Task 0 : Commit de baseline

**Contexte :** le dépôt n'est pas propre (HEAD `f8fd641`). 15 fichiers modifiés + 3 dossiers référentiel non commités (`composants/`, `parties-prenantes/`, `processus/`). Préalable obligatoire du design (§13) : committer l'état courant avant la migration, pour des diffs lisibles.

**Fichiers :**
- Staged : `00_caesn/` (value-model.md, 4 enveloppes VS, application-domains.md, shared-services.md), `coherence-report.md`, `referentiel/` (dont les 3 dossiers non commités), `scripts/build_wrappers.py`
- Exclus (convention) : `docs/`, `mintlify-site/`, `.mintignore`, les 2 `.docx`

- [ ] **Step 1 : Vérifier la baseline**

```bash
make check
ruby /tmp/validate_ref.rb
python3 /tmp/trace_check.py
```

Expected : `make check` vert ; validate_ref 202 fichiers/201 ids ; trace_check 197/201.

- [ ] **Step 2 : Commiter l'état courant**

```bash
git add 00_caesn/ coherence-report.md referentiel/ scripts/
git status --short          # ne doit contenir que ?? docs/, ?? mintlify-site/, ?? .mintignore, ?? *.docx
git commit -m "chore: baseline travail en-cours avant migration étapes/processus"
```

## Task 1 : Renommer les 28 étapes `prc-XX` → `ev-XX` et ré-ancrer les enveloppes (commit mécanique)

**But :** conversion formelle 1:1 (contenu du corps inchangé) + ré-ancrage des 4 blocs catalogue VS sur `referentiel/etapes-valeur/ev-XX.md` + réaffectation mécanique des composants (`prc-XX` → `ev-XX`). État final du commit : vert.

**Fichiers :**
- Rename : `referentiel/processus/prc-01..28.md` → `referentiel/etapes-valeur/ev-01..28.md`
- Modify : `referentiel/processus/` (vidé), `referentiel/composants/cmp-01..13.md`, `referentiel/_index.yaml`, `referentiel/_schema.md`, `00_caesn/01_value-streams/vs-0{1..4}-*.md`, `coherence-report.md`

- [ ] **Step 1 : Déplacer les fichiers avec git mv**

```bash
mkdir -p referentiel/etapes-valeur
for i in $(seq -w 1 28); do git mv referentiel/processus/prc-$i.md referentiel/etapes-valeur/ev-$i.md; done
ls referentiel/etapes-valeur/ | wc -l        # attendu : 28
```

- [ ] **Step 2 : Réécrire le frontmatter + H1 des 28 objets**

```bash
python3 - <<'EOF'
import re, glob
for f in sorted(glob.glob('referentiel/etapes-valeur/ev-*.md')):
    n = re.search(r'ev-(\d+)', f).group(1)
    s = open(f).read()
    s = s.replace(f'id: prc-{n}', f'id: ev-{n}')
    s = s.replace('type: processus-metier', 'type: etape-valeur')
    s = s.replace(f'title: PRC-{n}', f'title: EV-{n}')
    s = s.replace(f'# PRC-{n}', f'# EV-{n}')
    s = s.replace('"processus-metier"', '"etape-valeur"')
    s = s.replace(f'"prc-{n}"', f'"ev-{n}"')
    open(f, 'w').write(s)
EOF
grep -c "type: etape-valeur" referentiel/etapes-valeur/ev-*.md | awk -F: '{s+=$2} END {print s}'   # attendu : 28
```

- [ ] **Step 3 : Vérifier qu'aucun contenu de corps n'a changé (hors H1)**

```bash
git diff referentiel/etapes-valeur/ | grep -E '^[+-]' | grep -vE '^(---|\+\+\+|[+-](id|type|title):|[+-]# |[+-]tags:|[+-]")' || echo "CORPS OK"
```

- [ ] **Step 4 : Réaffecter mécaniquement les composants (applies_to + liens `## Liens`)**

```bash
python3 - <<'EOF'
import glob, re
for f in glob.glob('referentiel/composants/cmp-*.md'):
    s = open(f).read()
    s = re.sub(r'\[PRC-(\d+)\]\(\.\./processus/prc-\d+\.md\)',
               lambda m: '[EV-%s](../etapes-valeur/ev-%s.md)' % (m.group(1), m.group(1)), s)
    s = re.sub(r'"prc-(\d+)"', lambda m: '"ev-%s"' % m.group(1), s)
    open(f, 'w').write(s)
EOF
grep -l "prc-" referentiel/composants/*.md || echo "aucune référence prc- restante dans les composants"
```

- [ ] **Step 5 : Ré-ancrer les 4 blocs catalogue des enveloppes VS**

```bash
python3 - <<'EOF'
import re
envs = {'VS-01-access-care.md': (1,7), 'VS-02-risk-protection.md': (8,14),
        'VS-03-financial-protection.md': (15,21), 'VS-04-system-steering.md': (22,28)}
for env,(a,b) in envs.items():
    f = f'00_caesn/01_value-streams/{env}'
    s = open(f).read()
    s = s.replace('## Processus métier\n\n<!-- BEGIN:GENERATED mode=catalogue source=',
                  '## Étapes de valeur\n\n<!-- BEGIN:GENERATED mode=catalogue source=')
    s = re.sub(r'source=referentiel/processus/prc-\d+\.md(,referentiel/processus/prc-\d+\.md)*',
               'source=' + ','.join(f'referentiel/etapes-valeur/ev-{i:02d}.md' for i in range(a,b+1)), s)
    open(f, 'w').write(s)
EOF
grep -c "## Étapes de valeur" 00_caesn/01_value-streams/vs-0*.md     # attendu : 4
```

- [ ] **Step 6 : Mettre à jour `_index.yaml`**

```bash
python3 - <<'EOF'
import re
s = open('referentiel/_index.yaml').read()
s = s.replace('# processus métier (28)', '# étapes de valeur (28)')
s = s.replace('type: processus-metier', 'type: etape-valeur')
s = re.sub(r'chemin: processus/prc-(\d+)\.md', r'chemin: etapes-valeur/ev-\1.md', s)
open('referentiel/_index.yaml','w').write(s)
EOF
grep -c "etape-valeur" referentiel/_index.yaml    # attendu : 28 (type) — vérifier aussi chemin
```

- [ ] **Step 7 : Mettre à jour `_schema.md`**

Remplacer la ligne 29 :
`| `processus-metier` | `referentiel/processus/` | `prc-` | CAESN (PRC-01…28) |`
par deux lignes (dans l'ordre du tableau, `etape-valeur` avant `processus-metier`) :
```
| `etape-valeur` | `referentiel/etapes-valeur/` | `ev-` | CAESN (EV-01…28) |
| `processus-metier` | `referentiel/processus/` | `prc-` | CAESN (PRC-01…12) |
```

- [ ] **Step 8 : Noter le reclassement dans `coherence-report.md`**

Insérer juste après le titre `## 11. Ré-ancrage CAESN — processus métier, composants applicatifs, parties prenantes (2026-08-11) ✓` :

```markdown
> **NB (2026-08-12) :** les 28 objets décrits ci-dessous sont reclassés en **étapes de valeur** (`referentiel/etapes-valeur/ev-01…28.md`). Les **processus métier** (`referentiel/processus/prc-01…12.md`) les regroupent désormais — voir §12.
```

- [ ] **Step 9 : Régénérer et vérifier**

```bash
python3 scripts/build_wrappers.py
make check
ruby /tmp/validate_ref.rb
python3 /tmp/trace_check.py
```

Expected : `make check` vert ; validate_ref 213 fichiers/212 ids (les 28 ev présents, `processus/` non encore peuplé) ; `grep -c "etape-valeur"` cohérent. Si `build_wrappers.py` normalise la ligne de marqueur (liste `source=`), conserver la forme canonique écrite.

- [ ] **Step 10 : Commiter**

```bash
git add referentiel/ 00_caesn/01_value-streams/ coherence-report.md
git commit -m "feat: reclasser les 28 étapes de valeur (prc→ev) et ré-ancrer les enveloppes VS"
```

## Task 2 : Créer les 12 processus métier et réaffecter les composants au niveau processus (commit sémantique)

**But :** créer `referentiel/processus/prc-01…12.md` (contenu strictement dérivé des étapes), ajouter le bloc « Processus métier » aux 4 enveloppes VS, faire passer l'`applies_to` des composants des étapes aux processus (table §8 du design).

**Fichiers :**
- Create : `referentiel/processus/prc-01..12.md`
- Modify : `00_caesn/01_value-streams/vs-0{1..4}-*.md`, `referentiel/composants/cmp-01..13.md`, `referentiel/_index.yaml`, `coherence-report.md`, `00_caesn/10_annexes/glossary.md`

- [ ] **Step 1 : Créer les 12 objets processus**

Créer chacun des fichiers suivants avec exactement ce contenu.

`referentiel/processus/prc-01.md` (owner : Direction des soins) :
```markdown
---
id: PRC-01
type: processus-metier
niveau: "1"
title: PRC-01 — Accès, orientation et admission du patient
status: draft
owner: Direction des soins
version: "0.0.1"
source: 00_caesn/01_value-streams/vs-01-access-care.md
maps_to: []
implements: []
applies_to: ["CAP-01", "CAP-02", "CAP-03", "CAP-04", "CAP-09", "CAP-10", "CAP-11", "CAP-13", "CAP-14", "CAP-15", "PP-01", "PP-02", "PP-04", "PP-05", "PP-06"]
related: ["ev-01", "ev-02", "VS-01"]
tags: ["caesn", "niveau-1", "processus-metier", "PRC-01"]
---
# PRC-01 — Accès, orientation et admission du patient

## Objectif

Assurer l'entrée du patient dans le système de soins : reconnaissance du besoin, orientation vers le niveau de soins approprié, accueil et enregistrement.

## Étapes couvertes

- [EV-01 — Reconnaissance du besoin et orientation](../etapes-valeur/ev-01.md)
- [EV-02 — Accueil et enregistrement](../etapes-valeur/ev-02.md)

## Acteurs

Patient, famille, agent de santé communautaire, personnel d'accueil, registre patient

## Indicateurs

Taux de recours aux soins, délai moyen d'accès à une formation sanitaire, taux de dossiers ouverts, délai d'enregistrement
```

`referentiel/processus/prc-02.md` (owner : Direction des soins) :
```markdown
---
id: PRC-02
type: processus-metier
niveau: "1"
title: PRC-02 — Prestation des soins cliniques
status: draft
owner: Direction des soins
version: "0.0.1"
source: 00_caesn/01_value-streams/vs-01-access-care.md
maps_to: []
implements: []
applies_to: ["CAP-01", "CAP-02", "CAP-03", "CAP-04", "CAP-09", "CAP-10", "CAP-11", "CAP-13", "CAP-14", "CAP-15", "PP-01", "PP-02", "PP-04", "PP-05", "PP-06"]
related: ["ev-03", "ev-04", "ev-05", "VS-01"]
tags: ["caesn", "niveau-1", "processus-metier", "PRC-02"]
---
# PRC-02 — Prestation des soins cliniques

## Objectif

Assurer le cœur clinique du parcours : consultation et diagnostic, traitement et prise en charge, référence et contre-référence vers le niveau de soins supérieur.

## Étapes couvertes

- [EV-03 — Consultation et diagnostic](../etapes-valeur/ev-03.md)
- [EV-04 — Traitement et prise en charge](../etapes-valeur/ev-04.md)
- [EV-05 — Référence et contre-référence](../etapes-valeur/ev-05.md)

## Acteurs

Clinicien, dossier patient, pharmacie, laboratoire, formation sanitaire référente, formation cible, système de transport

## Indicateurs

Taux de consultations avec diagnostic documenté, taux de disponibilité des médicaments traceurs, taux de référence complétée avec retour d'information
```

`referentiel/processus/prc-03.md` (owner : Direction des soins) :
```markdown
---
id: PRC-03
type: processus-metier
niveau: "1"
title: PRC-03 — Continuité, suivi et qualité des soins
status: draft
owner: Direction des soins
version: "0.0.1"
source: 00_caesn/01_value-streams/vs-01-access-care.md
maps_to: []
implements: []
applies_to: ["CAP-01", "CAP-02", "CAP-03", "CAP-04", "CAP-09", "CAP-10", "CAP-11", "CAP-13", "CAP-14", "CAP-15", "PP-01", "PP-02", "PP-04", "PP-05", "PP-06"]
related: ["ev-06", "ev-07", "VS-01"]
tags: ["caesn", "niveau-1", "processus-metier", "PRC-03"]
---
# PRC-03 — Continuité, suivi et qualité des soins

## Objectif

Garantir la continuité des soins après l'épisode et l'amélioration continue de la qualité des services : suivi du patient, observance thérapeutique et revues qualité.

## Étapes couvertes

- [EV-06 — Suivi et continuité des soins](../etapes-valeur/ev-06.md)
- [EV-07 — Amélioration de la qualité](../etapes-valeur/ev-07.md)

## Acteurs

Agent de santé communautaire, clinicien, patient, gestionnaire de formation sanitaire, district, comité qualité

## Indicateurs

Taux de patients perdus de vue, taux d'observance thérapeutique, proportion de formations sanitaires ayant réalisé une revue qualité dans le mois
```

`referentiel/processus/prc-04.md` (owner : Direction de la protection sociale et de la promotion de la santé) :
```markdown
---
id: PRC-04
type: processus-metier
niveau: "1"
title: PRC-04 — Veille, prévention et surveillance sanitaire
status: draft
owner: Direction de la protection sociale et de la promotion de la santé
version: "0.0.1"
source: 00_caesn/01_value-streams/vs-02-risk-protection.md
maps_to: []
implements: []
applies_to: ["CAP-04", "CAP-05", "CAP-06", "CAP-09", "CAP-10", "CAP-11", "CAP-13", "CAP-14", "CAP-15", "PP-03", "PP-04", "PP-07", "PP-08"]
related: ["ev-08", "ev-09", "VS-02"]
tags: ["caesn", "niveau-1", "processus-metier", "PRC-04"]
---
# PRC-04 — Veille, prévention et surveillance sanitaire

## Objectif

Maintenir une veille sanitaire permanente : identification des risques et promotion de la santé, surveillance et détection des signaux sanitaires.

## Étapes couvertes

- [EV-08 — Identification des risques et promotion de la santé](../etapes-valeur/ev-08.md)
- [EV-09 — Surveillance et détection](../etapes-valeur/ev-09.md)

## Acteurs

Direction de la Protection Sociale et de la Promotion de la Santé, programmes, agents communautaires, formations sanitaires, laboratoires

## Indicateurs

Couverture des campagnes de prévention, taux de vaccination, complétude et promptitude des rapports, taux de signaux détectés
```

`referentiel/processus/prc-05.md` (owner : Direction de la protection sociale et de la promotion de la santé) :
```markdown
---
id: PRC-05
type: processus-metier
niveau: "1"
title: PRC-05 — Alerte, investigation et riposte
status: draft
owner: Direction de la protection sociale et de la promotion de la santé
version: "0.0.1"
source: 00_caesn/01_value-streams/vs-02-risk-protection.md
maps_to: []
implements: []
applies_to: ["CAP-04", "CAP-05", "CAP-06", "CAP-09", "CAP-10", "CAP-11", "CAP-13", "CAP-14", "CAP-15", "PP-03", "PP-04", "PP-07", "PP-08"]
related: ["ev-10", "ev-11", "ev-12", "VS-02"]
tags: ["caesn", "niveau-1", "processus-metier", "PRC-05"]
---
# PRC-05 — Alerte, investigation et riposte

## Objectif

Déclencher et conduire la réponse à un signal sanitaire validé : notification, vérification et investigation, et déploiement de la riposte.

## Étapes couvertes

- [EV-10 — Notification et alerte](../etapes-valeur/ev-10.md)
- [EV-11 — Vérification et investigation](../etapes-valeur/ev-11.md)
- [EV-12 — Riposte](../etapes-valeur/ev-12.md)

## Acteurs

District sanitaire, région, direction centrale, OMS, équipe d'investigation, laboratoire national de référence, partenaires internationaux

## Indicateurs

Délai moyen de notification d'une alerte, délai d'investigation, proportion d'alertes vérifiées dans les délais, délai de déploiement de la riposte, taux de contrôle de l'épidémie
```

`referentiel/processus/prc-06.md` (owner : Direction de la protection sociale et de la promotion de la santé) :
```markdown
---
id: PRC-06
type: processus-metier
niveau: "1"
title: PRC-06 — Clôture et capitalisation des épisodes
status: draft
owner: Direction de la protection sociale et de la promotion de la santé
version: "0.0.1"
source: 00_caesn/01_value-streams/vs-02-risk-protection.md
maps_to: []
implements: []
applies_to: ["CAP-04", "CAP-05", "CAP-06", "CAP-09", "CAP-10", "CAP-11", "CAP-13", "CAP-14", "CAP-15", "PP-03", "PP-04", "PP-07", "PP-08"]
related: ["ev-13", "ev-14", "VS-02"]
tags: ["caesn", "niveau-1", "processus-metier", "PRC-06"]
---
# PRC-06 — Clôture et capitalisation des épisodes

## Objectif

Clore l'épisode épidémique ou d'urgence et en capitaliser les leçons pour renforcer la préparation : suivi de situation, bilan documenté et revues après action.

## Étapes couvertes

- [EV-13 — Suivi de situation et clôture](../etapes-valeur/ev-13.md)
- [EV-14 — Capitalisation et amélioration](../etapes-valeur/ev-14.md)

## Acteurs

Comité de gestion de crise, direction centrale, comité technique national

## Indicateurs

Taux de létalité, durée de l'épisode épidémique, nombre de revues après action, proportion de recommandations mises en œuvre
```

`referentiel/processus/prc-07.md` (owner : Direction de la couverture santé universelle) :
```markdown
---
id: PRC-07
type: processus-metier
niveau: "1"
title: PRC-07 — Identification et droits des bénéficiaires
status: draft
owner: Direction de la couverture santé universelle
version: "0.0.1"
source: 00_caesn/01_value-streams/vs-03-financial-protection.md
maps_to: []
implements: []
applies_to: ["CAP-07", "CAP-08", "CAP-12", "CAP-13", "CAP-14", "CAP-15", "CAP-16", "PP-02", "PP-03", "PP-06"]
related: ["ev-15", "ev-16", "VS-03"]
tags: ["caesn", "niveau-1", "processus-metier", "PRC-07"]
---
# PRC-07 — Identification et droits des bénéficiaires

## Objectif

Constituer la base de la couverture santé universelle : identification et enregistrement des bénéficiaires, définition et communication de leurs droits et du panier de soins.

## Étapes couvertes

- [EV-15 — Identification et enregistrement des bénéficiaires](../etapes-valeur/ev-15.md)
- [EV-16 — Définition des droits et du panier de soins](../etapes-valeur/ev-16.md)

## Acteurs

Districts sanitaires, communes, fokontany, gestionnaires du registre, Ministère de la Santé, formations sanitaires, gestionnaires de la couverture santé

## Indicateurs

Taux de couverture du registre, taux d'exclusion estimé, proportion de formations sanitaires informées des droits
```

`referentiel/processus/prc-08.md` (owner : Direction de la couverture santé universelle) :
```markdown
---
id: PRC-08
type: processus-metier
niveau: "1"
title: PRC-08 — Financement et exemption au point de service
status: draft
owner: Direction de la couverture santé universelle
version: "0.0.1"
source: 00_caesn/01_value-streams/vs-03-financial-protection.md
maps_to: []
implements: []
applies_to: ["CAP-07", "CAP-08", "CAP-12", "CAP-13", "CAP-14", "CAP-15", "CAP-16", "PP-02", "PP-03", "PP-06"]
related: ["ev-17", "ev-18", "VS-03"]
tags: ["caesn", "niveau-1", "processus-metier", "PRC-08"]
---
# PRC-08 — Financement et exemption au point de service

## Objectif

Garantir la disponibilité des fonds et l'accès effectif aux soins sans paiement direct : mobilisation des financements et application de l'exemption au point de service.

## Étapes couvertes

- [EV-17 — Mobilisation des financements](../etapes-valeur/ev-17.md)
- [EV-18 — Prise en charge et exemption au point de service](../etapes-valeur/ev-18.md)

## Acteurs

Ministère de l'Économie et des Finances, Ministère de la Santé, partenaires, agent de santé, gestionnaire de la formation sanitaire

## Indicateurs

Taux d'exécution budgétaire, part du budget santé allouée à la protection financière, taux d'exemption appliqué, taux de refus de soins signalés
```

`referentiel/processus/prc-09.md` (owner : Direction de la couverture santé universelle) :
```markdown
---
id: PRC-09
type: processus-metier
niveau: "1"
title: PRC-09 — Remboursement et régulation des mécanismes
status: draft
owner: Direction de la couverture santé universelle
version: "0.0.1"
source: 00_caesn/01_value-streams/vs-03-financial-protection.md
maps_to: []
implements: []
applies_to: ["CAP-07", "CAP-08", "CAP-12", "CAP-13", "CAP-14", "CAP-15", "CAP-16", "PP-02", "PP-03", "PP-06"]
related: ["ev-19", "ev-20", "ev-21", "VS-03"]
tags: ["caesn", "niveau-1", "processus-metier", "PRC-09"]
---
# PRC-09 — Remboursement et régulation des mécanismes

## Objectif

Boucler le cycle financier de la protection : facturation et traitement des demandes, remboursement des formations sanitaires, et contrôle, audit et ajustement des mécanismes pour préserver l'équité.

## Étapes couvertes

- [EV-19 — Facturation et traitement des demandes de remboursement](../etapes-valeur/ev-19.md)
- [EV-20 — Remboursement](../etapes-valeur/ev-20.md)
- [EV-21 — Contrôle, audit et ajustement des mécanismes](../etapes-valeur/ev-21.md)

## Acteurs

Gestionnaire de la formation sanitaire, vérificateur, fonds de remboursement, fonds de couverture santé, Ministère de l'Économie et des Finances, inspection sanitaire, structures d'audit, comité technique national

## Indicateurs

Taux de factures rejetées, délai de validation des factures, délai moyen de remboursement, taux de remboursement effectif, proportion de contrôles réalisés, montant des anomalies détectées
```

`referentiel/processus/prc-10.md` (owner : Secrétariat Général) :
```markdown
---
id: PRC-10
type: processus-metier
niveau: "1"
title: PRC-10 — Planification et allocation des ressources
status: draft
owner: Secrétariat Général
version: "0.0.1"
source: 00_caesn/01_value-streams/vs-04-system-steering.md
maps_to: []
implements: []
applies_to: ["CAP-03", "CAP-08", "CAP-09", "CAP-12", "CAP-13", "CAP-14", "CAP-15", "CAP-16", "PP-03", "PP-07", "PP-08", "PP-09", "PP-10"]
related: ["ev-22", "ev-23", "ev-24", "VS-04"]
tags: ["caesn", "niveau-1", "processus-metier", "PRC-10"]
---
# PRC-10 — Planification et allocation des ressources

## Objectif

Définir les priorités nationales et traduire la stratégie en ressources : planification, budgétisation et allocation des ressources, coordination des acteurs et alignement des partenaires.

## Étapes couvertes

- [EV-22 — Définition des priorités et planification](../etapes-valeur/ev-22.md)
- [EV-23 — Budgétisation et allocation des ressources](../etapes-valeur/ev-23.md)
- [EV-24 — Coordination des acteurs et alignement des partenaires](../etapes-valeur/ev-24.md)

## Acteurs

Ministère, directions techniques, régions, districts, Direction des affaires financières, Ministère de l'Économie, partenaires, ONG

## Indicateurs

Proportion de plans opérationnels alignés sur le PDSS et la SNSD, taux d'exécution budgétaire, part du budget national allouée à la santé, proportion d'initiatives partenaires alignées sur le portefeuille national
```

`referentiel/processus/prc-11.md` (owner : Secrétariat Général) :
```markdown
---
id: PRC-11
type: processus-metier
niveau: "1"
title: PRC-11 — Suivi et pilotage de la performance
status: draft
owner: Secrétariat Général
version: "0.0.1"
source: 00_caesn/01_value-streams/vs-04-system-steering.md
maps_to: []
implements: []
applies_to: ["CAP-03", "CAP-08", "CAP-09", "CAP-12", "CAP-13", "CAP-14", "CAP-15", "CAP-16", "PP-03", "PP-07", "PP-08", "PP-09", "PP-10"]
related: ["ev-25", "ev-26", "VS-04"]
tags: ["caesn", "niveau-1", "processus-metier", "PRC-11"]
---
# PRC-11 — Suivi et pilotage de la performance

## Objectif

Piloter l'exécution sur la base de données fiables : suivi des plans et budgets, analyse de la performance et prise de décision corrective.

## Étapes couvertes

- [EV-25 — Suivi de l'exécution](../etapes-valeur/ev-25.md)
- [EV-26 — Analyse de la performance et prise de décision](../etapes-valeur/ev-26.md)

## Acteurs

Directions techniques, régions, districts, SIS, comités de pilotage

## Indicateurs

Complétude et promptitude des rapports, taux d'utilisation des tableaux de bord, nombre de revues de performance, proportion de décisions documentées
```

`referentiel/processus/prc-12.md` (owner : Secrétariat Général) :
```markdown
---
id: PRC-12
type: processus-metier
niveau: "1"
title: PRC-12 — Redevabilité et amélioration continue
status: draft
owner: Secrétariat Général
version: "0.0.1"
source: 00_caesn/01_value-streams/vs-04-system-steering.md
maps_to: []
implements: []
applies_to: ["CAP-03", "CAP-08", "CAP-09", "CAP-12", "CAP-13", "CAP-14", "CAP-15", "CAP-16", "PP-03", "PP-07", "PP-08", "PP-09", "PP-10"]
related: ["ev-27", "ev-28", "VS-04"]
tags: ["caesn", "niveau-1", "processus-metier", "PRC-12"]
---
# PRC-12 — Redevabilité et amélioration continue

## Objectif

Rendre compte à la population et aux instances et améliorer en continu le système : reddition de comptes, communication publique et mise en œuvre des plans d'amélioration.

## Étapes couvertes

- [EV-27 — Redevabilité et communication publique](../etapes-valeur/ev-27.md)
- [EV-28 — Amélioration continue](../etapes-valeur/ev-28.md)

## Acteurs

Ministère, Parlement, société civile, partenaires, Bureau de réalisation de la valeur, directions techniques, équipe d'architecture

## Indicateurs

Existence et publication de rapports annuels de performance, proportion de recommandations mises en œuvre, évolution de la maturité des capabilités
```

- [ ] **Step 2 : Vérifier la création et la partition**

```bash
ls referentiel/processus/ | wc -l                 # attendu : 12
grep -c "EV-" referentiel/processus/prc-*.md | awk -F: '{s+=$2} END {print s}'   # attendu : 28 liens d'étapes
```

- [ ] **Step 3 : Ajouter le bloc « Processus métier » aux 4 enveloppes VS**

Insérer après le `<!-- END:GENERATED -->` du bloc « Étapes de valeur » de chaque enveloppe (et avant toute section manuelle suivante) :

```
## Processus métier

<!-- BEGIN:GENERATED mode=catalogue source=referentiel/processus/prc-01.md,referentiel/processus/prc-02.md,referentiel/processus/prc-03.md -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->
<!-- END:GENERATED -->
```

Listes `source=` par enveloppe :
- `VS-01-access-care.md` : `prc-01.md,referentiel/processus/prc-02.md,referentiel/processus/prc-03.md`
- `VS-02-risk-protection.md` : `referentiel/processus/prc-04.md,referentiel/processus/prc-05.md,referentiel/processus/prc-06.md`
- `VS-03-financial-protection.md` : `referentiel/processus/prc-07.md,referentiel/processus/prc-08.md,referentiel/processus/prc-09.md`
- `VS-04-system-steering.md` : `referentiel/processus/prc-10.md,referentiel/processus/prc-11.md,referentiel/processus/prc-12.md`

- [ ] **Step 4 : Réaffecter les composants au niveau processus (table §8 du design)**

```bash
python3 - <<'EOF'
import re
mapping = {
    'CMP-01': ['PRC-01','PRC-02','PRC-03'],
    'CMP-02': ['PRC-01','PRC-02'],
    'CMP-03': ['PRC-01','PRC-03','PRC-04'],
    'CMP-04': ['PRC-04','PRC-05','PRC-06'],
    'CMP-05': ['PRC-04'],
    'CMP-06': ['PRC-07','PRC-08'],
    'CMP-07': ['PRC-09'],
    'CMP-08': ['PRC-02','PRC-05','PRC-08'],
    'CMP-09': ['PRC-10','PRC-11'],
    'CMP-10': ['PRC-03','PRC-06','PRC-09','PRC-11','PRC-12'],
    'CMP-11': ['PRC-10','PRC-12'],
    'CMP-12': ['PRC-01','PRC-07','PRC-10'],
    'CMP-13': ['PRC-01','PRC-05','PRC-09'],
}
for cmp, procs in mapping.items():
    f = f'referentiel/composants/{cmp}.md'
    lines = open(f).readlines()
    out, inserted = [], False
    for ln in lines:
        if re.match(r'\s*-\s*\[EV-\d+\]\(\.\./etapes-valeur/', ln):
            if not inserted:
                out.extend(f'- [{p.upper()}](../processus/{p}.md)\n' for p in procs)
                inserted = True
            continue
        out.append(ln)
    s = ''.join(out)
    s = re.sub(r'applies_to: \[.*?\]', 'applies_to: ["' + '", "'.join(procs) + '"]', s)
    open(f, 'w').write(s)
EOF
grep -l "ev-" referentiel/composants/*.md || echo "plus aucune référence d'étape dans les composants"
```

- [ ] **Step 5 : Ajouter les 12 entrées de processus à `_index.yaml`**

Insérer juste avant le commentaire `# composants applicatifs (13)` :

```yaml
# processus métier (12)
- id: PRC-01
  type: processus-metier
  niveau: "1"
  chemin: processus/prc-01.md
  status: draft
- id: PRC-02
  type: processus-metier
  niveau: "1"
  chemin: processus/prc-02.md
  status: draft
- id: PRC-03
  type: processus-metier
  niveau: "1"
  chemin: processus/prc-03.md
  status: draft
- id: PRC-04
  type: processus-metier
  niveau: "1"
  chemin: processus/prc-04.md
  status: draft
- id: PRC-05
  type: processus-metier
  niveau: "1"
  chemin: processus/prc-05.md
  status: draft
- id: PRC-06
  type: processus-metier
  niveau: "1"
  chemin: processus/prc-06.md
  status: draft
- id: PRC-07
  type: processus-metier
  niveau: "1"
  chemin: processus/prc-07.md
  status: draft
- id: PRC-08
  type: processus-metier
  niveau: "1"
  chemin: processus/prc-08.md
  status: draft
- id: PRC-09
  type: processus-metier
  niveau: "1"
  chemin: processus/prc-09.md
  status: draft
- id: PRC-10
  type: processus-metier
  niveau: "1"
  chemin: processus/prc-10.md
  status: draft
- id: PRC-11
  type: processus-metier
  niveau: "1"
  chemin: processus/prc-11.md
  status: draft
- id: PRC-12
  type: processus-metier
  niveau: "1"
  chemin: processus/prc-12.md
  status: draft
```

Vérifier : `grep -c "^- id: prc-" referentiel/_index.yaml` → attendu 12.

- [ ] **Step 6 : Documenter la migration dans `coherence-report.md`**

Ajouter en fin de fichier, après le §11 :

```markdown
## 12. Migration étapes de valeur / processus métier (2026-08-12) ✓

**Constat :** les 28 objets créés en §11 sous le type `processus-metier` reproduisaient 1:1 les étapes des tables CAESN : le type était utilisé à contresens (une étape n'est pas un processus) et les 13 composants pointaient vers des maillons isolés.

**Correctif appliqué (✓) — reclassement + couche de régroupement :**
- **28 étapes de valeur** (`referentiel/etapes-valeur/ev-01…28.md`) — reclassement formel des ex-`PRC-01…28` (id/type/title/tags, corps inchangé) ; `source:` = enveloppe VS-XX, `applies_to` granulaire conservé, `related` = flux.
- **12 processus métier** (`referentiel/processus/prc-01…12.md`) — 3 par flux de valeur (VS-01…04), contenus **strictement dérivés** des étapes (Objectif de synthèse, Étapes couvertes, Acteurs et Indicateurs = unions) ; `applies_to` = héritage intégral de la VS, `related` = étapes couvertes + flux.
- **13 composants** réaffectés au niveau processus (`applies_to` : étapes → processus couvrants, transformation mécanique depuis le découpage) — un composant soutient désormais des processus complets.
- **Enveloppes** VS-01…04 : deux blocs catalogue distincts « Étapes de valeur » et « Processus métier ».
- Traçabilité CAESN↔CNISN **intacte** ; aucun changement de `build_wrappers.py` ni de `manifest.json`.

**Vérifications (✓) :**
- `make check` : 54 enveloppes à jour, 0 lien relatif cassé.
- `validate_ref.rb` : 213 fichiers, 212 objets uniques, 2 erreurs méta connues (`_schema.md`), 0 lien cassé, 0 relation non résolue.
- `trace_check.py` : 213/213 objets tracés (les 12 processus via `related` → ev → vs → capabilités).
```

- [ ] **Step 7 : Ajouter les définitions au glossaire**

Insérer après la définition « Chaîne de valeur d'une initiative » dans `00_caesn/10_annexes/glossary.md` :

```markdown
**Étape de valeur** — Maillon séquentiel du cycle décrit par un flux de valeur du CAESN. Chaque flux (VS-01…04) en compte sept, documentées par leurs entrées, sorties, acteurs, ruptures fréquentes et indicateurs. Une étape décrit une transition du flux ; elle n'est pas un processus métier.

**Processus métier** — Régroupement cohérent d'étapes de valeur d'un même flux, constituant une chaîne d'activités porteuse de finalité (ex. PRC-01 « Accès, orientation et admission du patient » regroupe les étapes EV-01 et EV-02 du flux VS-01). Les 12 processus métier (PRC-01…12) sont dérivés des 28 étapes et constituent la couche de rattachement des composants applicatifs.
```

- [ ] **Step 8 : Régénérer et vérifier l'ensemble**

```bash
python3 scripts/build_wrappers.py
make check
ruby /tmp/validate_ref.rb
python3 /tmp/trace_check.py
```

Expected : `make check` vert ; validate_ref 213 fichiers / 212 ids ; trace_check 213/213 ; `grep -c "^- id:" referentiel/_index.yaml` = 213.

- [ ] **Step 9 : Commiter**

```bash
git add referentiel/ 00_caesn/01_value-streams/ coherence-report.md 00_caesn/10_annexes/glossary.md
git commit -m "feat: créer les 12 processus métier et rattacher les composants au niveau processus"
```

---

## Auto-revue du plan

**1. Couverture de la spec (design `2026-08-12-etapes-vs-processus-design.md`) :**
- D1 (deux types) → Task 1 Step 1-2 + Task 2 Step 1 ✓
- D2 (Per-VS, 3/VS, `source:` = enveloppe) → Task 2 Step 1 (frontmatter `source:`) + Step 3 ✓
- D3 (contenu dérivé : Objectif synthèse, Étapes couvertes, Acteurs/Indicateurs unions) → Task 2 Step 1 ✓
- D4 (capabilités = héritage intégral VS) → Task 2 Step 1 (`applies_to` intégraux) ✓
- D5 (relations `related` = ev + vs) → Task 2 Step 1 ✓
- D6 (découpage Option 1) → Task 2 Step 1 (les 12 fichiers) ✓
- D7 (renommage mécanique prc→ev) → Task 1 ✓
- D8 (cmp au niveau processus, table §8) → Task 1 Step 4 (mécanique) + Task 2 Step 4 (sémantique) ✓
- §4 modèle cible 213 objets → Task 2 Step 5 + Step 8 (count 213) ✓
- §7 index/schema/coherence/glossaire → Task 1 Step 6-8, Task 2 Step 5-7 ✓
- §9 enveloppes 3 blocs → Task 1 Step 5 + Task 2 Step 3 ✓
- §11 critères A1-A8 → Task 1 Step 9 / Task 2 Step 8 (make check, validate_ref, trace_check, partition, contenu, cmp) ✓
- §13 baseline commit → Task 0 ✓

**2. Scan des placeholders :** aucune étape « TBD/TODO » ; chaque script et chaque contenu de fichier est fourni intégralement.

**3. Cohérence des types/noms :** `ev-XX` (etapes-valeur) utilisés de façon cohérente dans Task 1 ; `PRC-01…12` (processus-metier) cohérents dans Task 2 ; le mapping cmp (§8) est identique au design ; la table des `applies_to` intégraux correspond aux `applies_to` de `referentiel/flux-valeur/vs-0X.md`.
