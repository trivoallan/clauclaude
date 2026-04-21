---
sidebar_position: 6
---

# 05 — Bug Docker sur bootstrap (test chirurgical)

**Durée estimée** : 45 min
**Risque** : faible (branche isolée, sans merge)
**Quand le faire** : pendant les congés

## Objectif

Tester la stack sur un **bug réel connu** dont vous connaissez déjà la cause et le fix. Idéal pour chronométrer Serena vs grep.

## Contexte

Dans `docs/memory-bank/decisionLog.md`, on trouve :

> **Fixed `bootstrap` command failure in Docker image** :
> - Moved `cookiecutters/` directory into the `regis` package.
> - Updated `cli.py` to use `importlib.resources.files` for finding templates, ensuring compatibility with installed packages.
> - Updated `pyproject.toml` to include `cookiecutters/**/*` in package data.

C'est un bug **non-trivial** : la cause n'est pas dans le code Python, c'est dans la config de packaging (`pyproject.toml`). Un agent qui se concentre sur le code va tourner en rond.

## Prérequis

- Serena + Superpowers installés
- Git propre sur `main` (pas de WIP)

## Protocole

### Préparation de la régression

1. Créer une branche :

```bash
git checkout -b test-bootstrap-regression
```

2. Supprimer la ligne du `package_data` dans `pyproject.toml` qui inclut les cookiecutters. Approximativement :

```toml
# Retirer ou commenter cette ligne :
# [tool.setuptools.package-data]
# regis = ["cookiecutters/**/*", ...]
```

3. Build l'image Docker pour reproduire le bug réel :

```bash
docker build -t regis-test .
docker run --rm regis-test bootstrap playbook /tmp/test-pb
# Doit fail avec FileNotFoundError sur le template cookiecutter
```

### Test de l'agent

Dans une session fraîche de Claude Code :

```
Active le projet regis. J'ai un bug : dans l'image Docker, la commande 
`regis bootstrap playbook` échoue avec FileNotFoundError sur le template cookiecutter.

Reproduis le bug d'abord (pas de fix avant reproduction).
Puis trouve la cause racine et propose un fix.
```

### Chronométrage

Noter **explicitement** :

- **T0** : démarrage de l'agent
- **T1** : moment où l'agent a reproduit le bug
- **T2** : moment où l'agent a identifié que le problème est dans `pyproject.toml` (pas dans le code Python)
- **T3** : fix proposé

## Observables clés

### Comportement attendu (Superpowers ok)

1. L'agent **reproduit le bug** avant de chercher le fix (critère Superpowers)
2. Il explore le code Python en premier (normal, c'est là que l'erreur est levée)
3. Il **pivote** rapidement quand il comprend que `importlib.resources.files` cherche des fichiers package — donc la question est "pourquoi les fichiers ne sont pas packagés ?"
4. Il inspecte `pyproject.toml` et trouve le `package_data` manquant

### Signaux d'échec

- ❌ Propose un fix dans le code Python sans avoir reproduit
- ❌ Reste bloqué dans le code Python, ne pense pas à `pyproject.toml`
- ❌ Propose de downgrader une dépendance (comportement connu des agents sur ce type de bug)
- ❌ T2 > 20 min — grep aurait été plus rapide

### Serena=ok vs Serena=meh

- **ok** : T2 < 10 min, identification propre de la chaîne d'imports `importlib.resources.files` → `pyproject.toml`
- **meh** : T2 entre 10 et 20 min, l'agent trouve mais tâtonne
- **ko** : T2 > 20 min ou l'agent abandonne

## Cleanup

```bash
git checkout main
git branch -D test-bootstrap-regression
docker rmi regis-test
```

## Valeur ajoutée du test

**Pour la stack** : teste la capacité de l'agent à **pivoter** quand l'erreur visible ne vient pas d'où on croit. C'est typiquement là où Claude vanilla part en vrille et consomme des tokens inutilement.

**Pour votre expérience** : vous mesurez combien de temps l'agent met vs combien vous auriez mis. Si vous auriez trouvé plus vite avec `grep -rn "importlib.resources" regis/` en 2 minutes, Serena n'apporte rien.

## Notes de résultat

À remplir après le test, utiliser [test-log-template.md](./test-log-template.md).
