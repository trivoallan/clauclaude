# clauclaude

> Environnement for Claude Code on the Web — notes, stack agentic coding, scénarios de test.

Ce dépôt consolide mes notes, décisions et scénarios de test autour de l'usage agentic de Claude Code et des outils associés (MCP servers, skills, workflows).

## Structure

```
docs/
├── intro.md                    # Point d'entrée
├── stack/                      # La stack agentic coding
│   ├── overview.md             # Vue d'ensemble, 5 couches
│   ├── install.md              # Guide d'installation pas-à-pas
│   ├── agents-md-template.md   # Template AGENTS.md portable
│   ├── benchmarks.md           # Données chiffrées + limites
│   └── decisions.md            # Historique des arbitrages
├── scenarios/                  # Scénarios de test sur projets réels
│   ├── overview.md             # Index + calendrier
│   ├── 01-sanity-check.md
│   ├── 02-create-playbook-phase1.md
│   ├── 03-cicd-hardening-regression.md
│   ├── 04-sprint1-design-doc.md
│   ├── 05-bootstrap-docker-bug.md
│   ├── 06-architect-review.md
│   └── test-log-template.md    # Template pour noter les résultats
└── reference/
    └── sources.md              # Articles, benchmarks, liens utiles
```

## Docusaurus (optionnel)

La structure `docs/` est compatible Docusaurus si besoin de publier ça un jour. Pour l'instant c'est lisible directement sur GitHub.

Pour initialiser Docusaurus plus tard :

```bash
pnpm create docusaurus@latest . classic --typescript
# Puis migrer docs/ tel quel
```

## Licence

À définir selon votre préférence (MIT, CC-BY, etc.)
