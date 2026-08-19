# AGENTS.md

> Single source of truth for AI coding agents working on the `clauclaude` repository.
> Read this fully before your first action.

## Project snapshot

- **Name**: clauclaude
- **Purpose**: Knowledge base, documentation, and test scenarios for Claude Code & agentic coding stack.
- **Status**: Active documentation repository
- **Owner**: Solo developer
- **Stack**: Markdown, Docusaurus-compatible structure, Python validation scripts

## How I work with you

- **Plan before code or docs changes.** Propose a short plan before editing or adding files.
- **Docusaurus compatibility.** Ensure all `.md` files in `docs/` include valid YAML frontmatter (e.g. `sidebar_position`).
- **Link integrity.** Always verify internal relative links when adding or moving documentation files.
- **Language**: Documentation is written in French (technical terms in English when standard).

## Non-negotiables

1. **No broken internal markdown links.**
2. **Keep the documentation progressive and pragmatic.** Do not add tools without clear rationale.
3. **Validate before claiming done.** Run `python3 scripts/validate_docs.py` to ensure docs formatting and link integrity.

## What "done" looks like

- [ ] Markdown files pass validation (`scripts/validate_docs.py`).
- [ ] Frontmatter included on all `docs/` pages.
- [ ] Clean commit message explaining changes.
