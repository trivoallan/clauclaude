---
sidebar_position: 1
---

# Vue d'ensemble de la stack

## Les 5 couches (d'après Murat Aslan)

L'[article d'Aslan](../reference/sources.md#articles-fondateurs) cartographie l'écosystème agentic coding en 5 couches distinctes. Comparer des outils qui vivent sur des couches différentes est une confusion classique — BMAD ≠ Ctxo ≠ RTK même si les trois "aident les agents".

| Couche | Question à laquelle elle répond | Outils cités |
|---|---|---|
| **Méthodologie / Process** | Dans quel ordre le travail doit-il se faire ? | BMAD-METHOD, spec-kit, GSD-2 |
| **Discipline d'exécution** | Comment empêcher l'agent d'être négligent ? | Superpowers |
| **Technical Context** | Qu'est-ce que ce code veut *vraiment* dire ? | Ctxo, jcodemunch-mcp, Serena, codebase-memory-mcp |
| **Token Optimization** | Comment survivre à la fenêtre de contexte ? | RTK, context-mode, jDocMunch |
| **Product Surface / Orchestration** | Comment opérer l'ensemble de la machine ? | gsd-2 |

## Ma stack retenue

Après analyse de mes besoins réels (voir [decisions.md](./decisions.md) pour l'historique), j'ai retenu :

| Couche | Outil | Statut |
|---|---|---|
| **Méthodologie** | GSD-2 | À installer semaine 3 |
| **Discipline** | Superpowers | À installer semaine 1 |
| **Technical Context** | **Serena MCP** | À installer semaine 2 |
| **Token Optim (code)** | jCodeMunch — *optionnel* | Tester après si douleur |
| **Token Optim (docs)** | jDocMunch — *recommandé* | Dès que la doc grossit |

## Pourquoi Serena et pas les autres

Les détails sont dans [decisions.md](./decisions.md), mais en bref :

- **Ctxo** — supporte TypeScript, Go, C# en deep analysis. Mes langages prioritaires (Python, PHP) tombent en tree-sitter syntaxique seulement → écarté.
- **codebase-memory-mcp** — 66 langages en tree-sitter, mais deep analysis uniquement sur Go/C/C++ que je n'utilise pas → pas de bonus pour moi.
- **Serena** — LSP-based, qualité IDE sur Python (Pyright), PHP (Intelephense), TypeScript (ts-language-server). Seul outil qui couvre mes 3 langages avec de l'analyse sémantique profonde.

## Philosophie d'installation

**Ne pas tout installer le même jour.** Chaque couche demande une semaine d'usage réel pour évaluer son apport. L'ordre est :

1. [AGENTS.md](./agents-md-template.md) — immédiat, zéro dépendance
2. Superpowers — semaine 1, discipline de base
3. Serena MCP — semaine 2, compréhension du code
4. GSD-2 — semaine 3, workflow structuré
5. jDocMunch — quand la doc devient un problème

Détails d'install : voir [install.md](./install.md).

## Le chaînon manquant (Aslan)

Aslan identifie une couche **pas encore couverte** par le marché : la **spec-to-code traceability** — tracker un requirement depuis le design jusqu'aux tests et à la maintenance ongoing. Aucun outil ne fait ça bien aujourd'hui.

Pour mon cas, c'est particulièrement pertinent : `regis` a des playbooks (spec) qui pilotent des analyzers (code) dont les résultats alimentent des rapports. La traçabilité spec→code→test est un vrai sujet qui sera sans doute à creuser.
