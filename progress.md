# dsh-superagent Explainer — Progress

Last update: 2026-11-02
Current phase: **Full build, in progress.** User approved the sample pages and said "build everything."
B3, B4 done. B5, B6 and the final pass F remain.

This file is the memory of the project. A new session must be able to continue from it alone.
Update it after every subagent finishes and after every user decision.

## Phase status

| Phase | Status | Notes |
|---|---|---|
| 0 Plan approval | done (scaled-down scope) | plan.md §2, §11 |
| 1 Foundation + samples | done | Stop point 2: waiting for user review |
| Full build (plan §13) | not started | 12 pages total |
| F Final pass | not started | |

## Full build — batch status

| Batch | Writer | Spot-check | Committed |
|---|---|---|---|
| B1 Foundation | done | done (supervisor, 0 defects in the page; 1 survey error found and logged) | fa6638e |
| B2 Samples | done | done (supervisor, 0 defects; build.py fixed for sibling links) | 93bc333 |
| B3 Domain core | done | done (supervisor, 0 defects) | c96fd30 |
| B4 Execution | done | done (supervisor, 1 precision defect found and fixed) | (next commit) |
| B5 Prompts and panel | not started | – | – |
| B6 Code map + reference | not started | – | – |

## USER INSTRUCTIONS

- 2026-11-02: Reuse the `deepseek-harness-explainer` scope defaults: single-depth pages, light
  supervisor-only spot-check (no separate fact-checker subagent), quizzes + one interactive visual, one
  subagent at a time. Approved as proposed, with the Ticket stage-machine stepper as the one visual.
- 2026-11-02: "build everything" — approved the sample pages at stop point 2, run the full build (B3-B6, F)
  without further review stops.

## RESUME NOTES

(none — work has not started)

## Done

Newest first.

- 2026-11-02: B4 execution committed: `concepts/executor-and-worker-sessions` (Executor port,
  `DshExecutor`, `WorkerSlots`, background jobs) and `concepts/effects-and-store` (Effects queue, Store,
  one-writer rules). 2 new diagrams (b4_executor_and_slots, b4_effects_and_store). 1 new glossary term
  (`store`); all others reused. build.py --strict: 0 errors on both new pages; 3 pre-existing "coming soon"
  warnings on not-yet-written B5 pages only. Supervisor spot-checked the resume/restart mechanic
  (`Assignments.interrupted()`) and found the page's claim ("unless its last Report already settled it")
  dropped a real condition (no later Input delivered after that Report) — fixed directly on the page, with
  an added `{{cite}}`; rebuilt clean. 2 more claims spot-checked (Effects.enqueue upsert key, Engine as sole
  writer): correct. Findings logged in notes/facts.md under "Execution (B4)". Playwright 1280/390px: 0
  overflow, 0 JS errors; both sibling links (session-and-loop-vocabulary, jobs-workflow-goal-plan) resolve
  HTTP 200.
- 2026-11-02: B3 domain core committed: `concepts/sources-and-triggers` (Source, Trigger, Thread, Channel)
  and `concepts/policy-and-authorization` (Policy, Eval, Decision, Mandate, Strength, admission). 2 new
  diagrams (b3_source_channel, b3_gate_and_mandate). 1 new glossary term (`admission`); all others reused
  from core.json. No interactive visual (none scoped for B3). build.py --strict: 0 errors on both new
  pages; 6 pre-existing "coming soon" warnings on not-yet-written B4/B5 pages only. Supervisor spot-checked
  5 claims directly against the code (assessor.request() runs for every strength; via:'listed' is produced
  only by the one-time migration, not the live gate; via:'bot' is always inferred by the type; DecisionKind
  declares 'reopen' but no code path produces it; the policy.ts:203-204 comment/check line numbers): all
  correct, 0 defects. Findings logged in notes/facts.md under "Domain core (B3)".
- 2026-11-02: B2 samples committed: home page (real system map, start-here, sibling-site mention), new
  `learn/what-this-is` (the site's one basics page, with the sibling-site recap), new
  `tours/life-of-a-github-mention` (13 stops, GitHub comment to Ticket end). 2 new diagrams
  (b2_domain_map, b2_mention_tour). No new glossary terms needed (core.json already covers them).
  DECISION (supervisor): fixed a real build.py gap the writer found and correctly refused to work around
  by guessing — `check_links` hard-errored on any link leaving `site/`, with no way to link the sibling
  site `deepseek-harness-explainer`. Added `sibling_sites` to explainer.json (`["deepseek-harness-explainer"]`)
  and a narrow allowance in `check_links`: a link matching `(../)+<sibling>/site/<path>` is accepted only if
  that exact file exists on the sibling's built site (verified on disk, not a blind allow). Converted the
  writer's plain-text sibling mentions (worked around the gap) into real `<a href>` links in
  `learn/what-this-is.html` and `index.html`; rebuilt clean (0 errors) and confirmed all 5 sibling links
  resolve (HTTP 200 via Playwright) with no visual regression. This rule now applies to every later batch:
  sibling-site links must be real `<a href="../.../deepseek-harness-explainer/site/...">` links, not named
  text. Supervisor spot-checked 2 of the tour's harder claims (policy.ts's explicit-before-followup gate
  order; assignments.ts's followsDone-gated `ready`/`dropped` ending logic): both correct, 0 defects.
  Spot-checked the diagram-bug fix the writer reported (title text no longer clipped behind a tag pill):
  confirmed in the built SVG. build.py --strict: 0 errors, 12 expected "coming soon" warnings. Playwright
  1280/390px on all 3 pages: 0 overflow, 0 JS errors.
  **STOP POINT 2 reached: waiting for user review of the sample pages before the full build starts.**
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

Start B5 (concepts/prompts-and-skills, concepts/panel-and-management-api), one subagent at a time,
through B6 and the final pass F.

## Questions for the user

(none open)

## Issues log

(none yet)

## Subagent log

| Date | Task | Result |
|---|---|---|
| 2026-10-30 | Codebase survey (template A) | Reported in plan.md §3. No files changed (read-only). |
| 2026-11-02 | B1 foundation (template B) | STYLE.md, nav, glossary, concepts/ticket-lifecycle + stepper visual + 1 diagram. 0 build errors. Supervisor spot-check: 0 defects, 1 survey error found (see notes/facts.md). |
| 2026-11-02 | B2 samples (template C) | home, learn/what-this-is, tours/life-of-a-github-mention + 2 diagrams. 0 build errors. Found a build.py gap (sibling links); supervisor fixed it. Supervisor spot-check: 0 defects. |
| 2026-11-02 | B3 domain core | sources-and-triggers, policy-and-authorization + 2 diagrams + 1 glossary term. 0 build errors. Supervisor spot-check: 0 defects. |
| 2026-11-02 | B4 execution | executor-and-worker-sessions, effects-and-store + 2 diagrams + 1 glossary term. 0 build errors. Supervisor spot-check: 1 precision defect found and fixed (resume/restart condition). |
