---
sidebar_position: 5
---

# Historique des décisions

Traçabilité des arbitrages faits pendant la conception de la stack. Utile dans 6 mois pour se rappeler *pourquoi* on a choisi Serena et pas autre chose.

## 2026-04-21 : Point de départ — article Aslan

**Contexte** : lecture de [l'article d'Aslan "Why Technical Context Deserves Its Own Layer"](https://blog.devgenius.io/agentic-coding-part-2-why-technical-context-deserves-its-own-layer-11dd197806de) et [Part 1 sur les 7 outils / 5 couches](https://medium.com/dev-genius/the-agentic-coding-stack-7-tools-5-layers-and-the-missing-link-nobody-has-built-yet-de264b260db3).

**Décision** : adopter le modèle à 5 couches comme grille d'analyse, pour éviter la confusion classique (comparer BMAD à Ctxo, qui ne résolvent pas le même problème).

## 2026-04-21 : Écarter BMAD pour cause de sur-ingénierie

**Contexte** : BMAD simule une équipe agile complète (PM, architecte, scrum master, developer, QA).

**Décision** : pas adopté.

**Raison** : je suis solo sur mes side-projects. BMAD est conçu pour des équipes enterprise greenfield. Le coût de setup (plusieurs jours) n'est pas justifié pour mon contexte.

**Alternative retenue** : GSD-2, plus léger, workflow Discuss → Plan → Execute → Verify sans les 12 agents spécialisés.

## 2026-04-21 : Écarter spec-kit

**Contexte** : spec-kit est centré sur le workflow spec-first avec gated phases.

**Décision** : pas adopté pour l'instant.

**Raison** : pour mes side-projects solo, un bon `PLAN.md` en markdown fait le travail à 90%. L'overhead de spec-kit n'est pas justifié.

**À reconsidérer si** : je rejoins une équipe où le spec-driven development est déjà la norme, ou pour un greenfield d'envergure.

## 2026-04-21 : Ctxo → codebase-memory-mcp (première révision)

**Contexte** : Ctxo est présenté dans la Part 2 d'Aslan comme l'outil candidat #1 pour la couche technical context.

**Découverte** : Ctxo ne fait de l'analyse sémantique profonde **que sur TypeScript, Go et C#**. Les autres langages tombent en tree-sitter syntaxique basique. Python est explicitement marqué *"demand-gated"* dans leur roadmap.

**Décision initiale** : basculer vers `codebase-memory-mcp` (66 langages, support multi-agent natif dont Antigravity).

## 2026-04-21 : codebase-memory-mcp → Serena (seconde révision)

**Contexte** : analyse de mon historique GitHub (80 repos publics) pour valider les choix.

**Première lecture erronée** : j'ai conclu que TypeScript était mon langage #1 à cause du nombre de repos "regis-archive-*" (11 variations d'archives d'un même projet).

**Correction importante** : j'ai précisé mon usage réel :
- **Python** pour les nouveaux projets (priorité)
- **PHP** pour la maintenance long terme des projets `constructions-incongrues`
- **TypeScript** uniquement quand je dois faire des interfaces

**Décision finale** : **Serena MCP**.

**Raison** : c'est le seul outil qui fait de l'analyse sémantique profonde (via LSP) sur mes 3 langages simultanément :
- Python → Pyright (LSP officiel Microsoft)
- PHP → Intelephense (LSP le plus abouti du marché) ou Phpactor (option 100% FOSS)
- TypeScript → typescript-language-server

Les alternatives (Ctxo, codebase-memory-mcp) ne font du *deep* que sur des langages que je n'utilise pas (Go, C#, C/C++).

**Benchmark à l'appui** : [ManoMano / Project AEGIS](./benchmarks.md#le-seul-benchmark-indépendant-solide-manomano--project-aegis) montre Serena comme seul setup capable de réussir un refactoring Java multi-fichiers où les alternatives échouent.

## 2026-04-21 : jCodeMunch positionné en token optim, pas technical context

**Contexte** : jCodeMunch est parfois présenté (y compris par Aslan) dans la couche technical context aux côtés de Ctxo.

**Analyse** : le FAQ de jCodeMunch lui-même reconnaît que *"RepoMapper est une carte de repo rankée... tandis que jCodeMunch est de la récupération symbol-accurate"*. Ce n'est pas la même chose qu'analyser des dépendances ou un blast radius.

**Décision** : jCodeMunch est classé **token optim**, pas technical context. Il fait bien une chose : récupérer un symbole précis sans lire le fichier entier. Ça ne remplace pas Serena qui comprend les *relations* entre symboles.

**Position dans la stack** : optionnel, à tester **après** Serena uniquement si la douleur tokens persiste.

## 2026-04-21 : Ordre d'installation progressif

**Décision** : ne pas installer toute la stack le même jour.

**Raison** : chaque couche demande 1 semaine d'usage réel pour évaluer son apport. Sinon on accumule des outils sans jamais en maîtriser un.

**Ordre retenu** :
1. AGENTS.md — immédiat
2. Superpowers — semaine 1 (discipline)
3. Serena — semaine 2 (technical context)
4. GSD-2 — semaine 3 (méthodologie)
5. jDocMunch — quand la doc grossit

## À tracer ici quand ça arrive

- Résultats des scénarios de test sur `regis` (voir [scenarios/](../scenarios/overview.md))
- Première couche abandonnée et pourquoi
- Ajout éventuel de jCodeMunch ou autres token optim
- Décision sur la couche "spec-to-code traceability" identifiée par Aslan comme le chaînon manquant
