---
sidebar_position: 3
---

# 02 — Exécution de la Phase 1 du plan create-playbook-skill

**Durée estimée** : 1h
**Risque** : 0 (génération d'un fichier doc, pas de modif code)
**Quand le faire** : cette semaine, après le Scénario 1

## Objectif

**C'est le meilleur test possible** parce que vous avez déjà rédigé le plan détaillé dans `docs/memory-bank/plans/create-playbook-skill.md`. Vous savez exactement ce qui est attendu, donc vous êtes juge parfait.

**Bonus** : le livrable (`references/available-rules.md`) débloque le Sprint 3 (playbook creation skill).

## Prérequis

- Serena + Superpowers installés
- Le plan `create-playbook-skill.md` existe dans `docs/memory-bank/plans/`
- Claude Code actif sur le projet regis

## Protocole

Dans une session fraîche :

```
Active le projet regis. Lis le plan docs/memory-bank/plans/create-playbook-skill.md.

Exécute uniquement la Phase 1 du plan (Discover Available Rule Templates).

Livrable attendu : references/available-rules.md avec la structure prescrite
dans la Phase 4 du plan.

Contraintes :
- Chaque slug doit être vérifié via grep dans le source (cf. Phase 1 du plan)
- Ne pas inventer de slug qui n'existe pas
- Une section par provider
```

## Observables clés

### Comportement attendu (Superpowers+Serena ok)

1. L'agent commence par **lire le plan complet** (ou au moins les Phases 1 et 4)
2. Il utilise `find_symbol` ou équivalent pour localiser `default_rules()` dans chaque analyzer
3. Il **vérifie** (grep) chaque slug qu'il extrait — la Phase 1 dit explicitement *"Every slug in the catalog must appear in the source file"*
4. Il produit un fichier markdown structuré avec une section par provider

### Signaux d'échec

- ❌ L'agent saute directement à la génération sans lire le plan
- ❌ Slugs inventés qui n'existent pas dans le code (hallucinations)
- ❌ Providers oubliés (default.yaml liste : trivy, skopeo, sbom, hadolint, freshness, size, popularity, endoflife, scorecarddev, provenance)
- ❌ Absence totale de vérification

## Vérité terrain

La commande de contrôle (à exécuter après le test de l'agent) :

```bash
grep -rn "def default_rules" regis/analyzers/
grep -rn '"slug"' regis/analyzers/
```

Comparer avec le fichier produit par l'agent — chaque slug du fichier doit être retrouvé dans les sources.

## Valeur ajoutée du test

**Pour la stack** : c'est un test ciblé sur 3 capacités critiques :

1. **Compréhension d'un plan multi-phases** (discipline : ne pas tout faire d'un coup)
2. **Navigation sémantique Python** (Serena trouve-t-il `default_rules()` dans 10+ fichiers efficacement ?)
3. **Vérification de l'output** (Superpowers : grep après extraction, ou l'agent "fait confiance" à sa propre sortie ?)

**Pour regis** : le fichier produit fait avancer le Sprint 3. Même si la stack déçoit, le livrable reste utile (à vérifier manuellement bien sûr).

## Notes de résultat

À remplir après le test, utiliser [test-log-template.md](./test-log-template.md).
