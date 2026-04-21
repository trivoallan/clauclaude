---
sidebar_position: 7
---

# 06 — Architecte adversarial review (préparation pilote v1)

**Durée estimée** : 1h
**Risque** : 0 (lecture + questions, pas de modif)
**Quand le faire** : Sprint 1-3, avant le pilote

## Objectif

Anticiper les questions des **architectes de la Direction Expertise Applicative** qui seront les premiers utilisateurs du pilote v1.

Usage agentic sous-estimé : l'agent comme **reviewer adversarial** de votre propre documentation.

## Contexte roadmap

Votre [roadmap v1.0.0-alpha](https://github.com/trivoallan/regis/blob/main/docs/memory-bank/roadmap.md) cible :

> **Direction Expertise Applicative** — architectes et experts sécurité

Et précise :

> UX/DevEx : critiques — premiers utilisateurs sont des architectes, pas des SREs

Donc la doc actuelle doit tenir face au regard d'un architecte sécurité expérimenté.

## Prérequis

- Serena + Superpowers installés
- Projet regis avec memory bank à jour
- Site Docusaurus accessible localement ou version GitHub Pages déployée

## Protocole

Dans une session fraîche :

```
Active le projet regis. Lis :
- projectbrief.md
- productContext.md
- La doc Docusaurus (docs/website/docs/)

Tu es maintenant un architecte sécurité sénior de la Direction Expertise Applicative.
Tu découvres regis. Tu dois décider si tu le mets entre les mains de tes équipes.

Tu es exigeant, tu as vu passer plusieurs outils "miracles" pour la container security
qui ont déçu. Tu es méfiant par défaut.

Pose-moi les 5 questions critiques auxquelles la doc actuelle ne répond PAS
et qui bloqueraient ta décision d'adopter regis dans ton organisation.

Contrainte : pas de questions génériques ("quelle est la roadmap ?"). 
Des questions précises, sur des détails techniques ou de gouvernance.
```

## Observables clés

### Comportement attendu

1. L'agent **lit effectivement** les docs mentionnées (vérifier avec les tool calls)
2. Les questions sont **spécifiques à regis** (mentionnent trivy, playbooks, JSON Logic, Harbor, etc. — pas juste "et la scalabilité ?")
3. Les questions pointent **de vrais trous** de la doc — si elles sont déjà couvertes, c'est que l'agent n'a pas bien lu
4. Au moins 2-3 questions concernent des sujets **qui ne sont pas dans le code** (gouvernance, versioning des playbooks, compliance, audit trail)

### Signaux de qualité

- 🟢 **Excellent** : au moins 3 questions où vous vous dites "merde, je n'y avais pas pensé"
- 🟡 **OK** : les questions sont pertinentes mais vous avez déjà les réponses (peut-être pas bien documentées)
- 🔴 **Raté** : questions génériques, ou questions auxquelles la doc répond déjà

### Bonnes questions attendues (exemples)

- Comment versionner un playbook ? Si je durcis mes règles, les images qui passaient hier peuvent-elles échouer aujourd'hui sans que je sache pourquoi ?
- Comment auditer rétroactivement quelles règles étaient appliquées à une image donnée à une date donnée ?
- Harbor a N projets avec des équipes séparées. Un playbook central vs des playbooks par projet : quelle est la bonne granularité ?
- Si un analyzer (trivy, hadolint) retourne une erreur, le playbook échoue-t-il ou ignore-t-il silencieusement ? Comment distinguer "pas de vulnérabilité trouvée" de "analyzer KO" ?
- En cas de désaccord entre deux règles (trivy dit "fail", freshness dit "ok"), comment se résout le verdict final ?

## Valeur ajoutée du test

**Pour la stack** : test soft, pas critique. Juge plus la capacité de l'agent à adopter un rôle que les capacités techniques.

**Pour regis** : **la vraie valeur est ici**. Ces 5 questions vont directement alimenter le backlog Sprint 3 "finitions site de doc" et vous font gagner le coût d'une vraie session adversariale avec un architecte.

## Exploitation des résultats

Après le test, les 5 questions peuvent être ajoutées :

- En **GitHub issues** avec label `doc:pilot-readiness`
- Dans `roadmap.md` comme items du Sprint 3
- Dans un fichier `docs/pilot-readiness.md` qui trackera la réponse apportée

## Notes de résultat

À remplir après le test, utiliser [test-log-template.md](./test-log-template.md).
