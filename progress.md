# dsh-superagent Explainer — Progress

Last update: 2026-11-02
Current phase: **1a Foundation** — starter kit copied, explainer.json filled, git initialized. Foundation
subagent about to start.

This file is the memory of the project. A new session must be able to continue from it alone.
Update it after every subagent finishes and after every user decision.

## Phase status

| Phase | Status | Notes |
|---|---|---|
| 0 Plan approval | done (scaled-down scope) | plan.md §2, §11 |
| 1 Foundation + samples | in progress | plan.md §12 |
| Full build (plan §13) | not started | 12 pages total |
| F Final pass | not started | |

## Full build — batch status

| Batch | Writer | Spot-check | Committed |
|---|---|---|---|
| B1 Foundation | not started | – | – |
| B2 Samples | not started | – | – |
| B3 Domain core | not started | – | – |
| B4 Execution | not started | – | – |
| B5 Prompts and panel | not started | – | – |
| B6 Code map + reference | not started | – | – |

## USER INSTRUCTIONS

- 2026-11-02: Reuse the `deepseek-harness-explainer` scope defaults: single-depth pages, light
  supervisor-only spot-check (no separate fact-checker subagent), quizzes + one interactive visual, one
  subagent at a time. Approved as proposed, with the Ticket stage-machine stepper as the one visual.

## RESUME NOTES

(none — work has not started)

## Done

Newest first.

- 2026-11-02: DECISION: explainer.json filled (project, repo path/url/sha, TypeScript+TSX Prism
  components, including `prism-markup` ahead of `prism-jsx`/`prism-tsx` to avoid the dependency bug hit in
  `deepseek-harness-explainer`'s B2). Starter kit copied from the skill templates. Git initialized, author
  set repo-local (Thomas Paul <contact@thomaspaul.dev>).
- 2026-11-02: USER DECISION: 12-page structure and scaled-down scope approved — see plan.md §2, §4, §11.
- 2026-10-30: Codebase survey done (subagent, template A). Commit pinned:
  6337fc823ce20251c8de8085948165c81aaa701e (the repo's single squashed commit). Confirmed: dsh-superagent
  is a Cordis plugin set packaged as a DSH bundle (147 .ts + 30 .tsx files, ~30,180 production lines),
  with an exceptionally thorough self-documenting docs/000-008 series. See plan.md §3 for the full digest.
  Line counts and package.json's dsh.bundle.patch spot-checked directly by the supervisor: correct.

## Next step

Start the Phase 1a foundation subagent (template B): tooling, STYLE.md adapted, nav files for all 12
pages, core glossary, and `concepts/ticket-lifecycle` as the full reference sample page with the
stage-machine stepper visual.

## Questions for the user

(none open)

## Issues log

(none yet)

## Subagent log

| Date | Task | Result |
|---|---|---|
| 2026-10-30 | Codebase survey (template A) | Reported in plan.md §3. No files changed (read-only). |
