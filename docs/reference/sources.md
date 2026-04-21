---
sidebar_position: 1
---

# Sources et références

Liste des articles, benchmarks et dépôts consultés pendant la conception de la stack.

## Articles fondateurs

### Murat Aslan — Agentic Coding Stack

- [The Agentic Coding Stack: 7 Tools, 5 Layers, and the Missing Link Nobody Has Built Yet](https://blog.devgenius.io/the-agentic-coding-stack-7-tools-5-layers-and-the-missing-link-nobody-has-built-yet-de264b260db3) — Part 1, avril 2026. Cartographie des 5 couches. Base conceptuelle de cette stack.
- [Agentic Coding Part 2: Why Technical Context Deserves Its Own Layer](https://blog.devgenius.io/agentic-coding-part-2-why-technical-context-deserves-its-own-layer-11dd197806de) — Part 2, avril 2026. Argumentaire pour la couche technical context.

### Context engineering

- [Context Engineering Is the Real Product](https://cobusgreyling.medium.com/context-engineering-is-the-real-product-d938be65ce7e) — Cobus Greyling, avril 2026. Analyse de l'architecture d'OpenDev (compaction adaptive, observation masking).
- [Components of A Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent) — Sebastian Raschka. Vue d'ensemble des coding agents et harnesses.

## Benchmarks

### Indépendants

- [Project AEGIS — Benchmarking AI Agents and Why Serena is Our New Must-Have](https://medium.com/manomano-tech/project-aegis-benchmarking-ai-agents-and-why-serena-is-our-new-must-have-311673db35dd) — ManoMano, 19 mars 2026. Test Claude vs Claude+LSP vs Claude+Serena sur monorepo Java 36K LoC. **Seul benchmark indépendant solide trouvé** sur cette couche.

### Semi-indépendants

- [SWE-bench Verified](https://www.swebench.com/) — benchmark standard pour évaluer les modèles sur des tâches GitHub réelles. Pas spécifique aux MCP servers mais référence du domaine.
- [Epoch AI — SWE-bench Verified](https://epoch.ai/benchmarks/swe-bench-verified) — évaluation détaillée avec méthodologie.

### Maison (à prendre avec du recul)

- [jCodeMunch benchmarks](https://github.com/jgravelle/jcodemunch-mcp/blob/main/benchmarks/README.md) — benchmarks auto-publiés, méthode tiktoken cl100k_base.

## Outils de la stack

### Technical Context

- **[Serena MCP](https://github.com/oraios/serena)** — l'outil retenu. LSP-based, 40+ langages.
  - [Documentation](https://oraios.github.io/serena/)
  - [Page langages supportés](https://oraios.github.io/serena/01-about/020_programming-languages.html)
  - [Configuration](https://oraios.github.io/serena/02-usage/050_configuration.html)

### Technical Context (considérés puis écartés)

- **[Ctxo](https://github.com/alperhankendi/Ctxo)** — deep analysis TS/Go/C# seulement. Écarté faute de support Python/PHP.
- **[codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** — 66 langages tree-sitter, deep uniquement sur Go/C/C++. Écarté parce que ces langages ne sont pas dans ma stack.
- **[CodeGraph](https://github.com/suatkocar/codegraph)** — 32 langages tree-sitter + embeddings code-spécifiques. Rust natif.
- **[Claude Context](https://github.com/zilliztech/claude-context)** — 14 langages, nécessite Milvus/Zilliz.
- **[FileScopeMCP](https://mcpservers.org/servers/admica/FileScopeMCP)** — 12 langages, focus importance ranking.

### Discipline

- **[Superpowers](https://github.com/obra/superpowers)** — TDD, debugging systématique, verification. Retenu.

### Méthodologie

- **[GSD-2](https://github.com/zachwills/gsd-2)** — workflow Discuss → Plan → Execute → Verify. Retenu.
- **[BMAD-METHOD](https://github.com/bmadcode/BMAD-METHOD)** — simulation d'équipe agile complète. Écarté pour cause de sur-ingénierie.
- **[GitHub Spec Kit](https://github.com/github/spec-kit)** — spec-driven CLI. Écarté pour side-projects.

### Token Optimization

- **[jCodeMunch / jDocMunch / jDataMunch](https://j.gravelle.us/jCodeMunch/)** — retrieval chirurgical. jDocMunch recommandé, jCodeMunch optionnel.
- **[RTK (Redact Tokens Kit)](https://github.com/rtk-ai/rtk)** — compression shell output.

## Classement / comparaisons

- [Agentic Skills Frameworks Compared](https://rywalker.com/research/agentic-skills-frameworks) — Ry Walker. 11 frameworks comparés (Superpowers, BMAD, Spec Kit, Anthropic Skills, etc.).
- [6 Best Spec-Driven Development Tools for AI Coding in 2026](https://www.augmentcode.com/tools/best-spec-driven-development-tools) — Augment Code. Intent, Kiro, Spec Kit, OpenSpec, BMAD, Cursor rules.

## Documentation officielle

### Claude Code

- [Claude Code docs](https://code.claude.com/docs/en/setup) — installation, uninstallation, configuration.
- [Anthropic API](https://docs.claude.com/en/api) — pour les intégrations custom.
- [Prompting documentation](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) — guide des bonnes pratiques.

### MCP (Model Context Protocol)

- [Spec MCP officielle](https://modelcontextprotocol.io/)
- [MCP Registry](https://github.com/mcp)

## Mes sources de veille

- [Dev Genius blog](https://blog.devgenius.io/) — plusieurs articles sur l'agentic coding
- [Sebastian Raschka Magazine](https://magazine.sebastianraschka.com/)
- Raindrop de veille personnelle : <https://raindrop.io/trivoallan>
