---
sidebar_position: 1
---

# Introduction

Ce dépôt consolide mes notes de travail sur l'usage **agentic** de Claude Code et des outils associés (MCP servers, skills, workflows).

## Ce qu'il y a ici

**[Stack](./stack/overview.md)** — la stack que j'ai retenue après analyse, avec guide d'installation, template AGENTS.md, benchmarks et historique des arbitrages.

**[Scénarios](./scenarios/overview.md)** — 6 scénarios de test gradués sur mes projets réels (principalement `regis`), pour valider empiriquement la stack avant de l'adopter durablement.

**[Références](./reference/sources.md)** — articles, benchmarks, URLs officielles des outils.

## Mon contexte

- **Solo dev** sur des side-projects et un projet pro majeur (`regis`)
- **Langages** : Python (priorité pour nouveaux projets), PHP (maintenance long terme), TypeScript (interfaces ponctuelles)
- **Agents** utilisés : Claude Code (CLI + desktop + web), Antigravity, GitHub Copilot
- **Fallback local** : Ollama sur MacBook Pro M1 16 Go quand plus de tokens cloud

## Philosophie

La stack n'est **pas** une liste de tools qu'on installe tous le même jour. C'est un empilement progressif où chaque couche se justifie par une douleur concrète :

1. **Discipline** d'abord (Superpowers) — empêche l'agent d'être négligent
2. **Méthodologie** ensuite (GSD-2) — structure le workflow
3. **Contexte technique** (Serena MCP) — donne une vraie compréhension du code
4. **Optimisation tokens** (RTK, jDocMunch) — seulement si on sent la douleur

L'objectif : **ne rien installer dont je ne sens pas encore le manque.**
