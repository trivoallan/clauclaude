---
sidebar_position: 4
---

# 03 — Regression test sur le CI/CD hardening

**Durée estimée** : 1h30
**Risque** : faible (branche isolée, pas de merge)
**Quand le faire** : pendant les congés

## Objectif

Tester la capacité de la stack à **détecter et corriger une régression volontaire** sur un workflow déjà durci. Bonus : valide que le memory bank fonctionne en pratique, pas juste en théorie.

## Contexte

Le plan `docs/memory-bank/plans/ci-cd-hardening-plan.md` a été complété avec les cases cochées :

> - [x] Toutes les actions sont pinnées par SHA
> - [x] Aucune permission globale `write`/`all` sauf nécessité documentée

Son scénario de test dit explicitement :

> Ajout d'une action non pinnée → la CI doit échouer

On teste donc ce comportement avec un agent.

## Protocole

### Préparation (hors agent)

1. Créer une branche de test :

```bash
cd regis
git checkout -b feature/test-stack-regression
```

2. Introduire volontairement 2 régressions dans `.github/workflows/trunk.yml` :

```bash
# Remplacer un SHA d'action par @v4 (régression 1)
# Par exemple, si on a actions/checkout@<sha>, le remplacer par actions/checkout@v4

# Ajouter une permission globale trop large (régression 2)
# En haut du fichier, ajouter :
# permissions:
#   contents: write
#   pull-requests: write
```

3. Commit ces régressions (sans push) :

```bash
git commit -am "test: regressions volontaires pour test de la stack"
```

### Test de l'agent

Dans une session fraîche (important : pas d'indice donné) :

```
Active le projet regis. Je viens de faire des changements sur .github/workflows/trunk.yml
dans la branche feature/test-stack-regression.

Audite ce workflow et corrige tous les problèmes de sécurité que tu identifies.
```

**Volontairement vague** — on veut voir si l'agent détecte *spontanément* les deux régressions sans qu'on lui dise quoi chercher.

## Observables clés

### Comportement attendu (memory bank + stack ok)

1. L'agent **lit le memory bank** au démarrage (c'est dans `docs/memory-bank/RULES.md` : *"Read ALL .md files in docs/memory-bank/ at the start of every session"*)
2. Il trouve `plans/ci-cd-hardening-plan.md` et identifie les règles de durcissement
3. Il détecte les DEUX régressions :
   - Action non pinnée (`@v4` au lieu d'un SHA)
   - Permission globale trop large
4. Il propose un fix avec **SHA résolu** via `gh api` (pas un hash inventé)

### Signaux d'échec

- ❌ L'agent ignore le memory bank et audite "à l'aveugle"
- ❌ Rate la régression `@v4` (erreur commune : considérer `@v4` comme acceptable)
- ❌ Rate la permission globale
- ❌ Invente un SHA au lieu de le résoudre (hallucination)
- ❌ Propose un fix qui modifie autre chose que les deux régressions introduites

## Vérité terrain

Les deux régressions sont explicitement contraires aux règles du plan :

> - [x] Toutes les actions sont pinnées par SHA
> - [x] Aucune permission globale `write`/`all` sauf nécessité documentée

Si l'agent rate ça, le memory bank n'est pas exploité (grave) ou le modèle n'applique pas les règles qu'il a lues (aussi grave).

## Cleanup

Après le test :

```bash
git checkout main
git branch -D feature/test-stack-regression
```

## Valeur ajoutée du test

**Pour la stack** : c'est le test le plus important pour valider que **votre memory bank fonctionne**. Tout le reste (Serena, Superpowers) ne compense pas un memory bank ignoré.

**Pour regis** : identifier les trous dans le protocole "lire le memory bank au démarrage". Si l'agent le rate, il faut peut-être reformuler `RULES.md` plus agressivement, ou ajouter un skill Claude Code qui force la lecture.

## Notes de résultat

À remplir après le test, utiliser [test-log-template.md](./test-log-template.md).
