---
sidebar_position: 3
---

# Template AGENTS.md

Fichier portable entre tous les agents de coding modernes (Claude Code, Antigravity, Copilot, Cursor, Codex...). Droppez-le au root de chaque projet.

## Comment l'utiliser

1. Copier le contenu de la [section Template](#template) dans un fichier `AGENTS.md` à la racine du projet
2. Remplir les `<!-- TODO -->` en 2 minutes max (si vous y passez 30 min, vous sur-ingénierez)
3. Pour Claude Code, faire un lien symbolique : `ln -s AGENTS.md CLAUDE.md`

## Principes de conception

**Pourquoi ce format.** Chaque section correspond à une couche de la stack :

- *How I work with you* + *TDD workflow* + *Debugging protocol* → couche **discipline** (rôle de Superpowers en attendant qu'il soit installé)
- *Token & context hygiene* → couche **token optim** (pré-RTK)
- *Architecture rules* → début de couche **technical context** (ce que Serena fera automatiquement plus tard)
- *Non-negotiables* + *What done looks like* → garde-fous qui manquent aux agents par défaut

**Piège à éviter.** Ne laissez pas ce fichier grandir à 500 lignes. Si une règle n'a pas servi en 3 mois, supprimez-la. Un AGENTS.md que personne ne lit vaut zéro.

## Template

```markdown
# AGENTS.md

> Single source of truth for any AI coding agent working on this repo.
> Read this fully before your first action. Re-read before large changes.

## Project snapshot

- **Name**: <!-- TODO: project name -->
- **Purpose (one sentence)**: <!-- TODO: what problem does it solve, for whom -->
- **Status**: <!-- prototype / alpha / beta / production -->
- **Owner**: solo developer — no team, no PRs-from-others workflow
- **Stack**: <!-- TODO: language, framework, DB, key libs -->

## How I work with you

I'm a solo dev running side-projects. I use you (the agent) as a collaborator, not a code generator. That means:

- **Plan before code.** For anything beyond a trivial edit, propose a short plan first (bullet list, 3–8 steps). Wait for my ack before writing code.
- **Small diffs.** Prefer 5 focused commits over 1 giant one. Each commit should be revertable on its own.
- **Ask when unsure.** If a requirement is ambiguous, ask ONE specific question rather than guessing. Guessing wastes more time than asking.
- **Never silently downgrade deps, change config, or bypass linters.** Surface the problem, propose options, let me pick.

## Non-negotiables

These are hard rules. Violating them is worse than not completing the task.

1. **No commits without tests passing locally.** If tests don't exist yet for the area you touch, write them first.
2. **No `--force` git operations** on `main`/`master`. Ever.
3. **No new dependencies without justification.** Every new dep is a long-term liability. Prefer stdlib, then existing deps, then new one.
4. **Secrets stay in `.env`** (gitignored). Never hardcode, never commit, never paste in chat.
5. **If you break something, say so.** Don't paper over failures with broader try/except or skipped tests.

## Code conventions

<!-- TODO: adapt to your stack -->

- **Language version**: <!-- e.g. Python 3.12, Node 20 LTS -->
- **Formatter**: <!-- e.g. ruff + black, prettier -->
- **Linter**: <!-- e.g. ruff, eslint -->
- **Type checking**: <!-- e.g. mypy strict, tsc strict -->
- **Test framework**: <!-- e.g. pytest, vitest -->
- **Naming**: snake_case for Python, camelCase for JS/TS, PascalCase for classes/components.
- **Imports**: absolute where possible, sorted by the formatter.
- **Comments**: explain *why*, not *what*. If the code needs a comment to explain what, it probably needs to be rewritten.

## Architecture rules

<!-- TODO: adapt. These are examples of the kind of rules that save you pain later. -->

- Business logic stays out of route handlers / CLI entry points. Handlers do validation + delegation only.
- No circular imports between top-level modules.
- Any external API call goes through a dedicated client module, never inline.
- Database migrations are append-only. Never edit a migration that has been applied.

## TDD workflow (required for non-trivial changes)

For anything more than a typo fix or a one-line change:

1. **Reproduce first.** Write a failing test that captures the bug or the missing feature.
2. **Implement minimally.** Smallest change that makes the test pass.
3. **Refactor.** Only after green. Tests stay green throughout.
4. **Verify.** Run the full test suite, not just the new test. Run the linter. Run the type checker.
5. **Only then claim done.**

Do not say "this should work" or "this is done" without having actually run the checks.

## Debugging protocol

When something breaks:

1. **Read the actual error message.** Don't guess. Don't assume you know what it means.
2. **Form a hypothesis.** Write it down in one sentence before touching code.
3. **Test the hypothesis cheaply.** Print statement, single test, minimal repro. Not a refactor.
4. **If wrong, form a new hypothesis.** Do not start changing things randomly.
5. **After 3 failed hypotheses, stop and tell me.** I'd rather talk it through than let you flail.

## Token & context hygiene

- **Don't dump whole files** into your context if grep + read-specific-lines works.
- **Don't re-read files** you've already read in this session unless they've been edited.
- **Summarize long tool outputs** in your own words; don't echo them back.
- **When context gets tight**, ask me to start a fresh session rather than forgetting silently.

## What "done" looks like

A task is done when **all** of these are true:

- [ ] Code compiles / interpreter accepts it
- [ ] New tests written, all tests pass
- [ ] Linter + formatter + type checker clean
- [ ] Manual smoke test performed (you ran it, not just "it should work")
- [ ] Commit message explains the *why*, not just the *what*
- [ ] No TODOs or `// FIXME` left in code you wrote (move them to an issue if needed)

## Things to avoid

- **Over-engineering.** This is a side-project. YAGNI is the default. No premature abstractions, no plugin systems, no dependency injection frameworks for 3 classes.
- **Silent scope creep.** If you notice another bug while fixing the current one, tell me. Don't fix it silently.
- **Commenting out code "in case we need it later".** That's what git is for. Delete it.
- **Adding "just in case" error handling** that swallows errors without logging or re-raising.

## Useful context files

<!-- TODO: list any other md files the agent should know about -->

- `README.md` — public-facing overview
- `docs/decisions/` — ADRs for non-obvious choices (add one if you're making a call I might question later)
- `.env.example` — required env vars, always kept in sync with actual `.env`

## When in doubt

Ask. One specific question beats ten lines of wrong code.
```

## Variantes

Pour **regis**, l'équivalent est déjà couvert par [le memory bank](https://github.com/trivoallan/regis/tree/main/docs/memory-bank) qui va plus loin (activeContext, progress, systemPatterns, etc.). Pour un side-project, AGENTS.md seul suffit largement.
