---
sidebar_position: 2
---

# Guide d'installation — Stack agentic coding

Stack ciblée : Python + TypeScript + PHP, solo dev, side-projects.

**Ordre d'installation** (respecter la progression, ne pas tout installer d'un coup) :

0. [Reset complet Claude Code](#0-reset-complet-claude-code) — optionnel mais recommandé
1. [AGENTS.md](#1-agentsmd-immédiat) — immédiat
2. [Superpowers](#2-superpowers-semaine-1) — semaine 1
3. [Serena MCP](#3-serena-mcp-semaine-2) — semaine 2
4. [GSD-2](#4-gsd-2-semaine-3) — semaine 3
5. [jDocMunch](#5-jdocmunch-optionnel) — optionnel, quand la doc grossit

---

## 0. Reset complet Claude Code

À faire si vous avez une install existante potentiellement corrompue, ou si vous voulez partir sur une base propre avant d'installer toute la stack. Vous partez d'une install vierge ? Sautez cette section.

⚠️ **Cette procédure supprime toute votre config Claude Code, vos MCP servers existants, et l'historique de vos sessions.** Faites un backup si besoin.

### 0a. Backup (optionnel mais recommandé)

```bash
# Sauvegarder la config avant suppression
mkdir -p ~/claude-backup-$(date +%Y%m%d)
cp -r ~/.claude ~/claude-backup-$(date +%Y%m%d)/ 2>/dev/null
cp ~/.claude.json ~/claude-backup-$(date +%Y%m%d)/ 2>/dev/null
```

### 0b. Identifier la méthode d'installation

```bash
# Où se trouve le binaire ?
which -a claude
type -a claude

# Déclinaisons possibles :
# ~/.claude/bin/claude       → installeur natif
# ~/.local/bin/claude        → installeur natif (fallback)
# /opt/homebrew/bin/claude   → Homebrew (Mac Apple Silicon)
# /usr/local/bin/claude      → Homebrew (Mac Intel) ou npm
# ~/.npm-global/bin/claude   → npm global
```

### 0c. Désinstallation — toutes les variantes

Exécuter **toutes** les commandes ci-dessous. Celles qui ne s'appliquent pas échoueront silencieusement, c'est normal.

```bash
# Méthode officielle (si le binaire répond encore)
claude uninstall 2>/dev/null || true

# npm
npm uninstall -g @anthropic-ai/claude-code 2>/dev/null || true

# Homebrew (macOS)
brew uninstall claude-code 2>/dev/null || true
brew cleanup claude-code 2>/dev/null || true

# Bun
bun uninstall -g @anthropic-ai/claude-code 2>/dev/null || true
rm -f ~/.bun/bin/claude

# Binaires résiduels
rm -f ~/.local/bin/claude
rm -rf ~/.claude/bin
```

### 0d. Nettoyer la config, les caches et les sessions

```bash
# User-scope (settings, MCP servers, sessions)
rm -rf ~/.claude
rm -f ~/.claude.json

# Caches npm (si vous aviez installé via npm)
rm -rf ~/.npm/_cacache
npm cache clean --force 2>/dev/null || true

# Caches spécifiques macOS
rm -rf ~/Library/Application\ Support/claude-code 2>/dev/null
rm -rf ~/Library/Caches/claude-code 2>/dev/null
```

### 0e. Nettoyer les configs projet (dans chaque repo actif)

```bash
# À exécuter depuis chaque projet où vous aviez utilisé Claude Code
rm -rf .claude
rm -f .mcp.json
```

### 0f. Vérifier que tout est parti

```bash
which claude
# Doit retourner : "claude not found"

ls ~/.claude 2>/dev/null
# Doit retourner : "No such file or directory"
```

Si `which claude` retourne encore un chemin, supprimez-le manuellement et vérifiez votre `PATH` dans `~/.zshrc` / `~/.bashrc`.

### 0g. Réinstallation propre (installeur natif recommandé)

Anthropic recommande désormais l'installeur natif plutôt que npm — pas de conflit de package manager, auto-update intégré.

```bash
# macOS / Linux
curl -fsSL https://claude.ai/install.sh | bash

# Ouvrir une NOUVELLE fenêtre de terminal (ne pas juste source ~/.zshrc)
# Puis vérifier
claude --version
```

Windows (PowerShell) :

```powershell
irm https://claude.ai/install.ps1 | iex
```

### 0h. Authentification

```bash
claude
# Suivre le flow d'auth au premier lancement
```

### 0i. Sanity check

```bash
claude doctor
# Doit afficher "install method: native" sans warning PATH
```

Si `claude doctor` remonte des problèmes, suivre ses recommandations avant de passer à la suite du guide.

---

## Prérequis

```bash
# Vérifier Node.js (pour les LSP TypeScript/PHP)
node --version   # >= 20 recommandé

# Vérifier Python (pour Serena)
python3 --version   # >= 3.11

# Installer uv (gestionnaire de paquets Python utilisé par Serena)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 1. AGENTS.md (immédiat)

Fichier portable entre tous vos agents (Claude Code, Antigravity, Copilot).

```bash
# Depuis la racine d'un projet
curl -o AGENTS.md https://raw.githubusercontent.com/your-gist/AGENTS.md
# OU : copiez le fichier AGENTS.md que je vous ai fourni précédemment

# Pour Claude Code spécifiquement, faire un lien symbolique
ln -s AGENTS.md CLAUDE.md
```

Remplissez les `<!-- TODO -->` en 2 minutes par projet.

---

## 2. Superpowers (semaine 1)

Couche discipline — TDD, debug systématique, vérification avant de claim "done".

### Installation Claude Code

```bash
# Installer via le plugin marketplace de Claude Code
claude plugins install obra/superpowers-marketplace
claude plugins install superpowers@superpowers-marketplace
```

### Vérification

```bash
# Dans Claude Code, taper
/plugins
# Doit lister "superpowers" comme actif
```

### Test rapide

Dans un repo, demander à Claude Code : *"Implémente la fonction X"*. Il devrait maintenant :
- Écrire un test qui échoue d'abord
- Implémenter
- Vérifier que le test passe
- Refuser de dire "done" sans avoir exécuté les checks

Si ce comportement n'apparaît pas, relancer Claude Code.

---

## 3. Serena MCP (semaine 2)

Couche technical context — analyse sémantique via LSP pour Python/TS/PHP.

### 3a. Installer les LSP

```bash
# Python (Pyright)
npm install -g pyright

# TypeScript
npm install -g typescript-language-server typescript

# PHP (Intelephense — recommandé)
npm install -g intelephense
# OU Phpactor si vous préférez 100% FOSS
# composer global require phpactor/phpactor
```

### 3b. Installer Serena

```bash
# Clone (uv gère le reste)
git clone https://github.com/oraios/serena.git ~/.serena-src
cd ~/.serena-src
```

### 3c. Configurer Claude Code

Créer ou éditer `~/.config/claude-code/mcp.json` :

```json
{
  "mcpServers": {
    "serena": {
      "command": "uvx",
      "args": [
        "--from", "git+https://github.com/oraios/serena.git",
        "serena", "start-mcp-server",
        "--context", "claude-code"
      ]
    }
  }
}
```

### 3d. Configurer Antigravity

Dans Antigravity : Agent pane → menu **⋮** → **MCP Servers** → **Manage MCP Servers** → **View raw config**.

```json
{
  "mcpServers": {
    "serena": {
      "command": "uvx",
      "args": [
        "--from", "git+https://github.com/oraios/serena.git",
        "serena", "start-mcp-server",
        "--context", "ide"
      ]
    }
  }
}
```

### 3e. Indexer un projet (recommandé pour les gros repos)

```bash
# Depuis la racine du projet à indexer
uvx --from git+https://github.com/oraios/serena.git index-project .
```

### 3f. Activer Serena dans une session

Dans Claude Code ou Antigravity :

> Active the project located at /absolute/path/to/my/project

### 3g. Désactivation temporaire (pour les tâches triviales)

ManoMano a mesuré que Serena coûte ~4x plus cher sur les questions simples en lecture seule. Pour ces cas :

```
/mcp
```

Puis désactiver `serena` temporairement.

---

## 4. GSD-2 (semaine 3)

Couche méthodologie — workflow Discuss → Plan → Execute → Verify avec subagents.

### Installation

```bash
# Repository officiel
git clone https://github.com/zachwills/gsd-2.git ~/.gsd-2

# Depuis la racine d'un projet
cp -r ~/.gsd-2/.claude ./
cp ~/.gsd-2/CLAUDE.md ./CLAUDE.gsd.md
```

### Fusionner avec votre AGENTS.md existant

```bash
# Si vous avez déjà un AGENTS.md, mergez manuellement
cat CLAUDE.gsd.md >> AGENTS.md
rm CLAUDE.gsd.md
ln -sf AGENTS.md CLAUDE.md
```

### Utilisation

Dans Claude Code, lancer un workflow avec :

```
/discuss   # Phase 1 — cadrage
/plan      # Phase 2 — planification
/execute   # Phase 3 — implémentation
/verify    # Phase 4 — vérification
```

---

## 5. jDocMunch (optionnel)

Token optim pour les docs — à installer quand votre dossier `docs/` ou vos READMEs commencent à polluer le contexte.

```bash
pip install git+https://github.com/jgravelle/jdocmunch-mcp.git
```

Ajouter dans `~/.config/claude-code/mcp.json` :

```json
{
  "mcpServers": {
    "jdocmunch": {
      "command": "jdocmunch-mcp"
    }
  }
}
```

### Usage

```
index_doc_local("/path/to/project/docs")
search_sections("auth flow")
```

---

## Vérification finale

```bash
# Lister les MCP servers actifs dans Claude Code
claude mcp list

# Doit afficher : serena, (jdocmunch si installé)
```

Test de bout en bout dans un vrai projet :

1. Ouvrir un projet avec un fichier Python ou PHP
2. `Active the project located at <path>`
3. Demander : *"Liste les symboles définis dans le fichier X"*
4. Serena doit retourner une liste structurée (pas un dump du fichier entier)

---

## Rollback / désinstallation

```bash
# Serena
rm -rf ~/.serena-src ~/.serena
# Retirer la section "serena" de ~/.config/claude-code/mcp.json

# Superpowers
claude plugins uninstall superpowers

# GSD-2
rm -rf .claude CLAUDE.gsd.md  # dans chaque projet

# jDocMunch
pip uninstall jdocmunch
```

---

## Dépannage

**Serena ne démarre pas** : vérifier `uv --version` et réinstaller si besoin avec `curl -LsSf https://astral.sh/uv/install.sh | sh`.

**LSP Intelephense lent au premier lancement** : normal, il indexe le projet. Deuxième lancement rapide.

**Claude Code ne voit pas Serena** : redémarrer Claude Code après avoir édité `mcp.json`.

**Superpowers n'impose pas TDD** : vérifier `/plugins` liste `superpowers` actif. Sinon relancer `claude plugins install`.

**Commandes GSD-2 non reconnues** : vérifier que le dossier `.claude/commands/` existe à la racine du projet.

---

## Notes importantes

- **Les URLs et commandes d'install peuvent changer.** Vérifier les READMEs officiels avant copier-coller : [Serena](https://github.com/oraios/serena), [Superpowers](https://github.com/obra/superpowers), [GSD-2](https://github.com/zachwills/gsd-2), [jDocMunch](https://github.com/jgravelle/jdocmunch-mcp).
- **Installer dans l'ordre.** Sauter des étapes rend le debugging impossible.
- **Ne pas installer tout le même jour.** Vivre avec chaque couche une semaine minimum avant d'ajouter la suivante.
