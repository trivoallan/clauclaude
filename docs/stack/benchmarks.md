---
sidebar_position: 4
---

# Benchmarks et données

## Ce qui est mesuré, ce qui ne l'est pas

Honnêteté d'abord : la couche "agentic coding stack" est **très peu benchmarkée** à ce jour. Chaque outil publie ses propres chiffres, rarement comparés head-to-head par des tiers.

## Le seul benchmark indépendant solide : ManoMano / Project AEGIS

[Article source](https://medium.com/manomano-tech/project-aegis-benchmarking-ai-agents-and-why-serena-is-our-new-must-have-311673db35dd) — publié le 19 mars 2026, test du 2 février 2026.

**Setup** : monorepo Java de production, 381 classes, 36 407 lignes de code, 1 017 tests. Test de 3 configurations : Claude vanilla, Claude Code + LSP natif, Claude + Serena.

### Tâche 4 — Refactoring multi-fichiers avec vérification build

| Setup | Durée | Coût | Résultat |
|---|---|---|---|
| Vanilla Claude | 1h | $23.54 | 12 subagents, échec de build |
| Claude Code + LSP natif | 1h | $28.63 | Abandon après 3 itérations, 9 tests rouges |
| **Claude + Serena** | **45 min** | **$27.30** | ✅ Build vert, 1 017 tests passent, 4 subagents |

Contexte lu par Serena pendant la tâche : **plus de 69 millions de tokens** grâce à son cache dédié, tout en maintenant un coût API contenu.

### Nuances importantes

ManoMano identifie 3 régimes d'usage différents :

**Pour l'exploration rapide (lecture seule)** : rester sur Claude vanilla. Sur une question simple de règle métier, Serena a coûté **~4x plus cher** et pris **+60% de temps**.

**Pour trouver l'usage d'une fonction** : Standard Claude et Serena font aussi bien au même coût. Le LSP natif de Claude Code hallucine et mélange les méthodes du même nom.

**Pour la modification profonde** : Serena est obligatoire. C'est là qu'il y a un gain décisif (build qui passe vs échec).

### Conséquence pratique

Désactiver Serena pour les tâches triviales via `/mcp` dans Claude Code. L'utiliser uniquement quand le coût est justifié (refactoring, debugging profond, onboarding sur codebase inconnue).

## Autres données disponibles

### jCodeMunch (benchmarks maison)

[Source](https://j.gravelle.us/jCodeMunch/) — mesures tiktoken cl100k_base sur 15 tâches, 3 repos.

**Réduction annoncée** : 95% moyens de tokens sur le retrieval de symboles.

**Exemple fastapi/fastapi** :
- Traditional (lecture de tous les fichiers) : 214 312 tokens
- jCodeMunch (retrieval par symboles) : ~480 tokens
- Réduction : 99.8%

**Limite méthodologique** : le test compare "donne-moi une fonction précise" vs "lire tous les fichiers" — cas qui avantage le plus l'approche symbol-based. Sur des requêtes plus floues, le gain est moindre. Pas de comparaison avec Serena ou Ctxo.

### SWE-bench Verified

[Source](https://www.swebench.com/) — 500 tâches GitHub réelles, évaluation standardisée.

Utilisé pour benchmarker les **modèles**, pas les MCP servers. Serena a sur sa roadmap officielle d'y être évalué, mais ça n'est pas encore fait.

## Ce qui n'a PAS de chiffres publics

- **Superpowers** : 0 benchmark tiers. Quelques témoignages Reddit ("90% fewer errors") mais anecdotiques.
- **GSD-2** : 0 benchmark. Retours forums positifs mais non quantifiés.
- **Ctxo vs codebase-memory-mcp vs Serena** : aucune comparaison head-to-head.
- **jDocMunch / jDataMunch** : benchmarks maison uniquement, sur leurs propres cas d'usage.

## Ma position

Le benchmark ManoMano **suffit à justifier Serena** comme meilleur choix pour la couche technical context, parce que :

1. C'est un test indépendant sur du code de production réel (pas un repo-jouet)
2. Les 3 régimes identifiés (read-only / find-usage / refactor) sont exactement ceux de mon usage quotidien
3. La conclusion opérationnelle ("désactivable à la demande") est implémentable immédiatement

**Ce que ça ne prouve PAS** : que les gains se transfèrent à Python/PHP/TS. C'est une hypothèse raisonnable (les LSP sous-jacents sont matures) mais non prouvée. Les [scénarios de test](../scenarios/overview.md) servent justement à valider ça sur mes propres projets.

## Sources

Voir [reference/sources.md](../reference/sources.md) pour la liste complète des articles et benchmarks consultés.
