---
sidebar_position: 5
---

# 04 — Design doc InputsAnalyzer (Sprint 1)

**Durée estimée** : 2h
**Risque** : 0 (design doc uniquement, pas de code)
**Quand le faire** : au retour des congés, début Sprint 1 (19 mai)

## Objectif

Produire un **livrable à valeur réelle** pour le Sprint 1 tout en testant la stack sur une tâche cross-cutting (design cohérent avec l'architecture existante).

## Contexte roadmap

Sprint 1 contient :

> **Playbook bundle format** — Playbooks sous forme de répertoire : `playbook.yaml` + `README.md` + `inputs.schema.json`. Nouveau `InputsAnalyzer`.

Cet analyzer doit s'intégrer dans le plugin system existant (15 analyzers dans `regis/analyzers/`), suivre les conventions, et supporter les schémas JSON draft-07 pour la validation d'inputs non-image (project IDs, URLs de docs sécurité, etc.).

## Prérequis

- Stack complète installée et validée par Scénarios 1-3
- GSD-2 installé pour le workflow Discuss → Plan → Execute
- Claude Code actif sur regis

## Protocole

### Phase Discuss

```
Active le projet regis. Lis le memory bank, notamment systemPatterns.md et 
docs/memory-bank/plans/create-playbook-skill.md (Phase 3 mentionne inputs.schema.json).

Je prépare le Sprint 1. Je veux un design doc de 2 pages max pour le InputsAnalyzer
du playbook bundle format.

Ne génère pas de code. Commence par me poser les 3 questions les plus importantes
avant de proposer un design.
```

### Phase Plan (après réponses aux questions)

```
OK, sur la base de nos échanges, propose :
1. Une API cohérente avec les analyzers existants (regarde BaseAnalyzer et 2-3 analyzers
   représentatifs pour le pattern)
2. 3 premiers tests à écrire en TDD (avec leurs assertions principales)
3. Les 2 risques d'intégration avec le playbook bundle format

Format : markdown, 2 pages max.
```

### Phase Verify (optionnelle)

```
Relis ton design. Quels sont les 2 points faibles de cette proposition
qu'un reviewer sévère pointerait ?
```

## Observables clés

### Comportement attendu

1. L'agent pose des **vraies questions** (pas des trucs génériques type "quel est ton use case ?")
   - Bonnes questions attendues : "L'analyzer doit-il valider au load time ou au runtime ?" / "Inputs requis manquants : erreur bloquante ou warning ?" / "Évolution schéma : compat arrière garantie ou breaking acceptable en v1 ?"
2. Le design **respecte les patterns existants** (hérite de `BaseAnalyzer`, méthodes `default_rules()`, etc.)
3. Les 3 tests en TDD sont **exécutables mentalement** — pas des "tester que ça marche"
4. Les 2 risques d'intégration sont **spécifiques à regis**, pas génériques

### Signaux d'échec

- ❌ L'agent saute les questions et pond un design en une passe
- ❌ Le design ignore les conventions des analyzers existants (invente une nouvelle hiérarchie)
- ❌ Tests trop vagues ("tester que l'analyzer fonctionne")
- ❌ Risques génériques ("attention à la rétrocompat")
- ❌ Contradiction avec des décisions du `decisionLog.md` (ex: ignore les choix sur JSON schema de 2026-03-21)

## Vérité terrain

Pour juger de la qualité du design :

1. **Cohérence avec `regis/analyzers/BaseAnalyzer`** (ou équivalent) — le design doit suivre le même pattern
2. **Compatibilité avec `regis/schemas/playbook/definition.schema.json`** — InputsAnalyzer doit produire des outputs qui s'intègrent au playbook engine
3. **Faisabilité pour Sprint 1** (2 semaines) — si le design nécessite 6 semaines de refonte, c'est un échec

## Valeur ajoutée du test

**Pour la stack** : c'est le test le plus exigeant — design cross-cutting qui demande de comprendre l'architecture globale, pas juste un fichier.

**Pour regis** : si le design est bon, il fait gagner **3-4h** au retour des congés. Si mauvais, vous savez immédiatement (pas de surprise en cours de sprint).

## Notes de résultat

À remplir après le test, utiliser [test-log-template.md](./test-log-template.md).
