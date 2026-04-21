---
sidebar_position: 2
---

# 01 — Sanity check sur regis

**Durée estimée** : 30 min
**Risque** : 0 (read-only)
**Quand le faire** : cette semaine, avant toute autre utilisation de la stack

## Objectif

Avant de tester sur du vrai travail, vérifier que Serena + LSPs ne plantent pas sur la structure de `regis`. C'est un monorepo Python+TypeScript avec `pipenv` (pas `uv`) pour Python.

## Prérequis

- Serena MCP installé (voir [install.md](../stack/install.md))
- Pyright + typescript-language-server installés globalement
- Claude Code avec Serena actif

## Protocole

### Session A — avec Serena

Dans une session fraîche de Claude Code :

1. Activer le projet :

```
Active the project located at /absolute/path/to/regis
```

2. Poser la question de référence :

```
Liste-moi les 15 analyzers de regis avec leur rôle en une ligne chacun.
Indique lesquels ont des dépendances externes (binaires PATH).
```

3. Noter :
   - Temps total
   - Nombre d'appels tool (Serena vs file reads)
   - Tokens consommés (visible avec `/cost`)

### Session B — sans Serena (contrôle)

Fermer, rouvrir Claude Code, désactiver Serena via `/mcp`. Nouvelle session fraîche, même question.

Noter les mêmes métriques.

## Critères de validation

### Réussite (Serena=ok)

- ✅ Les 15 analyzers sont identifiés correctement (recouper avec `ls regis/analyzers/`)
- ✅ Les dépendances externes mentionnées matchent ce qui est dans `docs/memory-bank/externalIntegrations.md` (trivy, skopeo, hadolint, dockle)
- ✅ Session A < 1.5x le temps de Session B (sinon Serena pèse plus qu'il n'aide)

### Échec (Serena=ko)

- ❌ Serena hallucine des analyzers qui n'existent pas
- ❌ Serena rate `endoflife`, `scorecarddev`, `provenance` ou d'autres analyzers moins évidents
- ❌ Timeout ou erreur d'indexation sur `regis`

### Ambigu (Serena=meh)

- ⚠️ Même qualité de réponse que vanilla, pas de gain visible
- ⚠️ Serena est plus lent sans apporter de précision supplémentaire

## Vérité terrain

Pour recouper, la liste exacte des analyzers :

```bash
ls regis/analyzers/ | grep -v __pycache__ | grep -v __init__
```

## Ce que ça mesure vraiment

**Côté positif** : capacité de Serena à indexer un projet Python avec `pipenv` (pas uv) et à gérer un plugin system (les analyzers sont chargés dynamiquement via entry points).

**Côté négatif** : si l'indexation plante sur regis, la stack est inutilisable pour mon projet principal — no-go complet.

## Notes de résultat

À remplir après le test, utiliser [test-log-template.md](./test-log-template.md).
