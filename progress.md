# dsh-superagent Explainer — Progress

Last update: 2026-11-02
Current phase: **1b Samples** — B1 foundation done and committed. Next: home, learn/what-this-is, the tour.

This file is the memory of the project. A new session must be able to continue from it alone.
Update it after every subagent finishes and after every user decision.

## Phase status

| Phase | Status | Notes |
|---|---|---|
| 0 Plan approval | done (scaled-down scope) | plan.md §2, §11 |
| 1 Foundation + samples | in progress (1a done) | plan.md §12 |
| Full build (plan §13) | not started | 12 pages total |
| F Final pass | not started | |

## Full build — batch status

| Batch | Writer | Spot-check | Committed |
|---|---|---|---|
| B1 Foundation | done | done (supervisor, 0 defects in the page; 1 survey error found and logged) | (next commit) |
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

- 2026-11-02: B1 foundation committed: STYLE.md adapted (vocabulary table, out-of-scope list, single-depth
  + sibling-recap rules), nav files for all 12 pages, core glossary (22 terms), concepts/ticket-lifecycle
  as the full reference sample page, with the Ticket stage-machine stepper (the site's one interactive
  visual, 7 stations) and one diagram (b1_ticket_anatomy). Supervisor spot-checked 9 higher-risk claims
  directly against the target repo (stage.ts's full check order, Ticket's missing stage field, Strength's
  2 values vs. GateResult's admissible:false, AssignmentState transitions, Tickets.create(), Subscription
  fan-out with no new Eval, WorkerSlots.reserve()'s person exception, dropped-Report ending a Ticket): all
  correct, 0 defects. Found and logged one real error from the Phase 0 survey: `scripts/dsh-superagent` is
  a 250-line Python script, not a shell script (notes/facts.md "Survey correction") — it had not reached
  any page yet; B6 must get this right. build.py: 0 errors, 6 expected "coming soon" warnings. Playwright
  1280/390px on index.html and concepts/ticket-lifecycle.html: 0 overflow, 0 JS errors; stepper click
  interaction confirmed (7 stations, DOM updates on click). Added `site/` to .gitignore (the writer flagged
  it was missing).
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

Start Phase 1b (samples, plan.md §12): one subagent for `index` (home, system map, code version),
`learn/what-this-is` (recap + links to the sibling site), and `tours/life-of-a-github-mention`. Then Stop
point 2 — show the user the sample pages before the full build (B3-B6, F) starts.

## Questions for the user

(none open)

## Issues log

(none yet)

## Subagent log

| Date | Task | Result |
|---|---|---|
| 2026-10-30 | Codebase survey (template A) | Reported in plan.md §3. No files changed (read-only). |
| 2026-11-02 | B1 foundation (template B) | STYLE.md, nav, glossary, concepts/ticket-lifecycle + stepper visual + 1 diagram. 0 build errors. Supervisor spot-check: 0 defects, 1 survey error found (see notes/facts.md). |
