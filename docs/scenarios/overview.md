---
sidebar_position: 1
---

# Scénarios de test — vue d'ensemble

Tester la stack sur des tâches **réelles à valeur ajoutée**, pas des exercices artificiels. Cible principale : `regis`, le projet avec le plus d'enjeu.

## Principe

Chaque scénario est conçu pour :

1. **Stresser une couche spécifique** de la stack (discipline, technical context, méthodologie...)
2. **Produire un livrable utile** même si la stack déçoit
3. **Permettre une évaluation objective** — je connais assez regis pour juger si l'agent raconte n'importe quoi

## Ordre recommandé (adapté au calendrier)

Vu le calendrier regis (7j ouvrés avant congés du 30 avril au 17 mai, puis Sprint 1 dès le 19 mai) :

### Cette semaine (pré-sprint actif, 21-29 avril)

Scénarios **rapides, à faible risque, à valeur immédiate** :

- [**01 — Sanity check**](./01-sanity-check.md) (30 min) — valider que Serena indexe regis sans casse
- [**02 — Create-playbook Phase 1**](./02-create-playbook-phase1.md) (1h) — produit `references/available-rules.md` qui débloque le Sprint 3

### Pendant les congés (30 avril - 17 mai)

Si envie de bidouiller, **pas de production engagée** :

- [**03 — CI/CD hardening regression test**](./03-cicd-hardening-regression.md) (1h30) — valide le memory bank avec un bug volontaire
- [**05 — Bootstrap Docker bug**](./05-bootstrap-docker-bug.md) (45 min) — test chirurgical sur bug connu

### Au retour (Sprint 1, 19 mai - 2 juin)

Scénarios à **haute valeur** pour les sprints à venir :

- [**04 — Design doc InputsAnalyzer**](./04-sprint1-design-doc.md) (2h) — prépare le livrable Sprint 1
- [**06 — Architecte adversarial review**](./06-architect-review.md) (1h) — prépare le pilote v1

## Ce qu'il faut noter pour chaque test

Utiliser le [template de test log](./test-log-template.md) après chaque scénario, puis copier la ligne-résumé dans `activeContext.md` de regis au format :

```
[2026-04-XX] Stack test — Scénario X : Serena=<ok|meh|ko>, Superpowers=<ok|meh|ko>, 
surprise=<ce qui a raté/fonctionné au-delà des attentes>
```

## Critères de décision

À la fin des scénarios, trois issues possibles :

**Si ≥ 4/6 scénarios donnent Serena=ok** → la stack mérite d'être installée définitivement. Poursuivre avec GSD-2 + jDocMunch.

**Si 2-3/6 scénarios donnent Serena=ok** → usage à la carte (activer via MCP uniquement pour les tâches lourdes, désactivé par défaut).

**Si ≤ 1/6 scénarios donnent Serena=ok** → retour à Claude Code vanilla + Superpowers uniquement.

L'objectif est une **décision empirique et documentée**, pas un avis théorique.
