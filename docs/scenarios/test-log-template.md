---
sidebar_position: 99
---

# Template — test log

Template à copier après chaque scénario. L'idée est de rester bref (tenir en moins d'une page) pour que ça reste faisable sans friction.

## Comment l'utiliser

1. Copier le contenu ci-dessous dans un nouveau fichier `test-log-XX.md` (XX = numéro du scénario)
2. Remplir pendant/juste après le test
3. Copier la ligne-résumé dans `activeContext.md` de regis

## Template

```markdown
# Test log — Scénario XX : <nom court>

**Date** : YYYY-MM-DD
**Durée réelle** : Xh XX min (vs estimée : XX min)
**Agent utilisé** : Claude Code (CLI / desktop / web) avec modèle <nom>
**Stack active** : Serena=<on|off>, Superpowers=<on|off>, GSD-2=<on|off>

## Verdict

- **Serena** : ok / meh / ko
- **Superpowers** : ok / meh / ko
- **GSD-2** : ok / meh / ko / n/a

## Ce qui a marché

- 

## Ce qui a raté ou surpris

- 

## Métriques

- Tokens consommés : XXX (visible avec /cost)
- Nombre d'interventions manuelles (pour corriger l'agent) : X
- Comparaison avec même tâche sans la stack : <+/-X% temps, +/-X% tokens>

## Livrable produit

- Fichier(s) : 
- Qualité : <usable direct / utilisable après revue / à jeter>

## Points spécifiques à noter

### Sur la stack

- 

### Sur le projet cible

- 

## Décision / Action

- [ ] Garder la configuration actuelle
- [ ] Ajuster <quoi>
- [ ] Noter dans decisionLog
- [ ] Autre : 

## Ligne pour activeContext.md de regis

[YYYY-MM-DD] Stack test — Scénario XX (<nom>) : Serena=<>, Superpowers=<>, surprise=<une phrase>
```

## Exemple rempli (fictif)

```markdown
# Test log — Scénario 01 : Sanity check sur regis

**Date** : 2026-04-22
**Durée réelle** : 35 min (vs estimée : 30 min)
**Agent utilisé** : Claude Code CLI avec Opus 4.7
**Stack active** : Serena=on, Superpowers=off, GSD-2=off

## Verdict

- **Serena** : ok
- **Superpowers** : n/a (pas encore installé)
- **GSD-2** : n/a

## Ce qui a marché

- Indexation réussie sur regis (env Python avec pipenv, pas de souci)
- 14 analyzers trouvés sur les 15 attendus, dépendances externes bien identifiées
- Serena a utilisé find_symbol directement, 4 tool calls vs 23 pour vanilla

## Ce qui a raté ou surpris

- Serena a oublié `provenance` (analyzer le plus récent, peut-être pas dans index ?)
- L'indexation initiale a pris 90s (plus que prévu, projet est gros)

## Métriques

- Tokens consommés : ~12k avec Serena, ~45k sans
- Interventions manuelles : 1 (demander la liste complète après oubli de provenance)
- Gain : -70% tokens, temps similaire

## Livrable produit

- Aucun (test read-only)

## Points spécifiques à noter

### Sur la stack

- Ré-indexer avec ctxo watch ou équivalent quand on modifie les analyzers
- Vérifier si Serena doit être relancé après ajout d'un nouvel analyzer

### Sur le projet cible

- Le memory bank `activeContext.md` est utile comme source pour Serena — continuer à le maintenir

## Décision / Action

- [x] Garder la configuration actuelle
- [x] Ajuster : activer `serena index-project` dans un pre-commit hook
- [x] Noter dans decisionLog

## Ligne pour activeContext.md de regis

[2026-04-22] Stack test — Scénario 01 (sanity check) : Serena=ok, Superpowers=n/a, surprise=oublie le dernier analyzer ajouté si index pas rafraîchi
```
