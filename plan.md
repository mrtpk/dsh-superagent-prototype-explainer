# dsh-superagent Explainer — Plan

Status: **APPROVED (scaled-down scope).**
Date: 2026-11-02
Source repo: `../dsh-superagent-prototype` at commit `6337fc8` (https://github.com/deepseek-ai/dsh-superagent-prototype)

---

## 1. Goal

Make a static website that gives a beginner an overview of the `dsh-superagent-prototype` codebase: a
proactive coding agent for one GitHub repository, packaged as a DSH (DeepSeek Harness) bundle.
The reader clicks through the pages and learns step by step. Full code-reading is a low priority; every
claim still cites `file:line`.

## 2. Decisions (approved by the user, 2026-11-02)

| Topic | Decision |
|---|---|
| Reader | Knows TypeScript/Node, and knows DSH/Cordis basics from the sibling site `deepseek-harness-explainer` (same user, same folder level). Does not know this project's own domain model (Source, Ticket, Eval, Executor, Panel). |
| Depth of detail | **Single-depth overview** (not the skill's full two-depth pattern): a short beginner start, then one compact "More detail" section. No long code-excerpt deep dives. Same scope decision as `deepseek-harness-explainer`. |
| Hosting | Local files only (`site/index.html` opens from `file://`). CDN allowed for Inter font and Prism (cdnjs); the site degrades to a system font and plain code offline. |
| Structure | learn + concepts + one tour + code map + reference. One page per domain concept group, not one page per file. |
| Sibling site | `deepseek-harness-explainer` already teaches Cordis plugins, profiles/bundles, session vocabulary, skills, jobs/background work. This site recaps each in one line and links out — see `learn/what-this-is`. No new page re-teaches them. |
| Location | `dsh-superagent-prototype-explainer/` (sibling folder to the target repo checkout). The target repo stays unchanged. |
| Site language | ASD-STE100 Simplified Technical English. |
| Scope | Full pages: `src/`, `prompts/`, `skills/`, `cordis.patch.yml`, `scripts/dsh-superagent`. Out of scope: `tests/` (explained only as "the project has an unusually large test suite", not walked through), `locale/` (mentioned once, not a page), the two bundled Source skills' exact prompt text (linked, not reproduced in full). |
| Name | "dsh-superagent Explained" |
| Look | Light article look (light always; dark only by toggle). Diagrams follow `instructions-svg.md` + STYLE.md §10. |
| Code version | Commit `6337fc823ce20251c8de8085948165c81aaa701e` (2026-10-31, the repo's single squashed commit). Version line on every page, full SHA in the footer, home section `#code-version`. |
| Fact-check mode | **Light**: supervisor spot-checks a sample of each batch's higher-risk claims directly against the code. No separate fact-checker subagent. Same scope decision as `deepseek-harness-explainer`. |
| Checkpoint | Stop after Phase 1 (foundation + samples) for the user to review the look and the sample pages, before the full build starts. |
| Budget | One subagent at a time. |
| Git | Commit per stage; push only when the user asks; author `Thomas Paul <contact@thomaspaul.dev>` (repo-local). |

## 3. Facts about the codebase (from the survey, 2026-10-30)

- Size: 147 `.ts` files / 25,388 lines + 30 `.tsx` files / 4,794 lines production code (~30,180 lines);
  65 test files / 14,960 lines (tests are nearly as large as production code).
- It is a Cordis plugin set packaged as a DSH bundle (`package.json` `dsh.bundle.patch` →
  `cordis.patch.yml`), not a standalone framework. It runs inside a dedicated DSH profile (`superagent`),
  reuses DSH's own Session machinery, and injects a React panel into DSH's Web sidebar.
- History: **one commit** (squashed for publication, per README.md:3-5's own disclosure). No submodules.
- Good docs in the repo: `docs/000-philosophy.md` through `docs/008-cookbook.md`, each building only on
  the ones before it — exceptionally thorough, close to a pre-written architecture reference
  (`docs/007-architecture.md` has a module index, a test index and a Mermaid flowchart).
  No image/diagram assets exist; two Mermaid flowcharts (in `docs/001` and `docs/007`) are the only
  existing diagrams and should be redrawn as site SVGs, not embedded as Mermaid.
- Comments in another language: no. Chinese text appears only as deliberate bilingual `{zh, en}` UI-label
  pairs (`src/client/locales.ts`, `locale/*.json`) — intentional i18n, not stray comments.
- Unusual: the README says the project was built largely by coding agents; both agent presets run with
  full OS-user access (no real sandbox, docs/006:13-19 says so explicitly); a meta-test
  (`tests/docs.spec.ts`) checks the docs' own internal consistency.

## 4. Site structure (12 pages)

```
dsh-superagent-prototype-explainer/
  index.html     Home: what dsh-superagent is, system map, "Start here", code version
  learn/         1 page: recap of DSH/Cordis basics (links to the sibling site) + what is new here
  concepts/      7 pages, in groups (domain core, execution, prompts/panel)
  tours/         1 page: "Life of a GitHub mention", 13 stops
  code/          1 page: the ~18 central files
  reference/     1 page: config, env vars, deployment
```

### Part 1 — Learn the basics
1. `learn/what-this-is`: what dsh-superagent is and how it sits on DSH + Cordis; one-line recap + link
   to each basic already taught by `deepseek-harness-explainer` (plugins/Cordis, profiles/bundles, session
   vocabulary, skills, jobs/background work).

### Part 2 — Concepts
- **Domain core:** `concepts/sources-and-triggers` (Source, Trigger, Thread, Channel) ·
  `concepts/policy-and-authorization` (Policy, Eval, Decision, Mandate, strength, admission) ·
  `concepts/ticket-lifecycle` (Ticket, stage machine, Assignment, Subscription — **Phase 1 sample page**,
  carries the stage-machine interactive visual)
- **Execution:** `concepts/executor-and-worker-sessions` (DshExecutor, worker slots, background jobs) ·
  `concepts/effects-and-store` (durable Effects queue, SQLite Store, one-writer-per-state dependency rules)
- **Prompts and panel:** `concepts/prompts-and-skills` (prompt assembly/precedence, bundled Source skills) ·
  `concepts/panel-and-management-api` (React panel, tabs, Management API, settings versioning)

### Part 3 — Guided tour
1. **Life of a GitHub mention** — a GitHub comment that @-mentions the agent, to an opened pull request
   (13 stops, from the survey's numbered data-flow).

### Part 4 — Code map
- Folder tree (`tools/gen_folder_tree.py`), `code/central-files`: the ~18 files from the survey's table
  (`src/executor/dsh.ts`, `src/sources/github.ts`, `src/core/tickets.ts`, `src/core/model.ts`,
  `src/core/evals.ts`, `src/client/locales.ts`, `src/app/sessions.ts`, and 11 more).

### Part 5 — Reference
- `reference/config-and-deployment`: env vars (`tools/gen_env_table.py` or hand-verified table if no
  generator fits), `cordis.patch.yml` structure, `scripts/dsh-superagent` CLI, the Management API.
- Glossary (generated by `build.py`).

## 5. Page design

Templates: see STYLE.md §4 (basics, concept, tour, module, reference), adapted for single-depth pages
(see §2 above: no full "Deep dive" section, one compact "More detail" section instead).

### Interactive visual (one)
- **Ticket stage-machine stepper** on `concepts/ticket-lifecycle`: click through the stage table from
  docs/003-execution.md:9-18 (idle → queued → working → review/blocked/failed → attention), each stage
  naming the real file:line that computes it (`src/core/stage.ts`).

### Quizzes
One short `<x-quiz>` on each concept page, the tour, and `learn/what-this-is`.

## 6. Technology

Static HTML, `build.py` (standard library only), `explainer.json` for project values, SVG diagrams from
Python scripts with `svglib.py`, Prism from cdnjs, Inter from Google Fonts. Output `site/` opens from disk.

## 7. Writing rules

See STYLE.md §6-7. Every claim about the code cites `file:line` at the pinned commit. Single-depth pages
per §2: short beginner start + one "More detail" section, not a full two-depth "Deep dive".

## 8. How the supervisor works

Supervisor + one subagent at a time. Writer → build 0 errors → supervisor spot-checks a sample of the
batch's higher-risk claims directly against the code (no separate fact-checker subagent) → commit.
`progress.md` is updated after every event. The target repo is never changed. No push without a user
request. Open questions go to `progress.md` "Questions for the user".

## 9. Definition of done

- All 12 planned pages exist and `python3 build.py --strict` has 0 errors, 0 warnings.
- Every concept page and the tour have a diagram (or the one interactive visual), code citations, a
  "More detail" section and a quiz.
- The supervisor spot-check log in `progress.md` states plainly what was checked, batch by batch (light
  fact-check scope, not a full adversarial pass — same disclosure as `deepseek-harness-explainer`'s README).
- Site check at 1280 and 390 px: no overflow, no JS errors, no broken links; the visual and all quizzes work.
- A beginner can follow Home → `learn/what-this-is` → the tour with no dead end.

## 10. Risks

| Risk | What we do |
|---|---|
| Wrong explanations | Writers read the code themselves; supervisor spot-checks higher-risk claims; citations always |
| Re-teaching the sibling site's basics | `learn/what-this-is` recaps in one line and links out; writer briefs name the sibling site explicitly |
| Prism dependency bug (hit in `deepseek-harness-explainer`'s B2: jsx/tsx without prism-markup threw a build-time TypeError) | `explainer.json` here already includes `prism-markup` ahead of `prism-jsx`/`prism-tsx`, since this project's `src/client/` is real `.tsx` that may get cited |
| Too large to finish | Priority: Home → `learn/what-this-is` → tour → domain-core concepts → execution/prompts/panel concepts → code map → reference |

## 11. Answers from the user (2026-11-02)

1. Approve the ~11-12 page structure and reuse `deepseek-harness-explainer`'s scope defaults (single-depth,
   light fact-check, quizzes + one visual, one subagent at a time): **approved as proposed**.
2. Which diagram should be the one interactive visual: **Ticket stage-machine stepper** (not the
   Eval/Decision gate flow).

## 12. Phase 1 in detail (the review package)

| Step | Work | Who |
|---|---|---|
| 1a | Tooling, STYLE.md adapted, nav files with all 12 planned pages, core glossary (~20-25 domain terms), `concepts/ticket-lifecycle` built as the full reference sample page (every tag, the stage-machine visual) | 1 subagent |
| 1b | Samples: home + system map + code version; `learn/what-this-is`; the tour | 1 subagent at a time |
| 1c | Supervisor spot-check of the sample pages' higher-risk claims; site check | supervisor |
| 1d | Stop. Show the user the sample pages. | supervisor |

## 13. Full build (after user approval at stop point 2)

Pipeline per batch: writer → build 0 errors → supervisor spot-check → commit.

| Batch | Pages | Interactive visual / notes |
|---|---|---|
| B1 Foundation | tooling + `concepts/ticket-lifecycle` (sample) | stage-machine stepper |
| B2 Samples | `index`, `learn/what-this-is`, `tours/life-of-a-github-mention` | — |
| B3 Domain core | `concepts/sources-and-triggers`, `concepts/policy-and-authorization` | — |
| B4 Execution | `concepts/executor-and-worker-sessions`, `concepts/effects-and-store` | — |
| B5 Prompts and panel | `concepts/prompts-and-skills`, `concepts/panel-and-management-api` | — |
| B6 Code map + reference | `code/central-files`, `reference/config-and-deployment` | — |
| F | Final consistency + site check pass | — |

Waves: all batches run one at a time (user's budget decision). Order: B1 → B2 → (stop point 2) → B3 → B4
→ B5 → B6 → F.

## 14. Deferred pages

(none)

## 15. Future work (not in this build)

Adding the skill's full two-depth "Deep dive" pattern to every page: shapes/types, algorithm steps, edge
cases, a worked example with numbers, on top of the existing single-depth "More detail" section. This is
additive — it does not require a rebuild. Same future-work note as `deepseek-harness-explainer` plan.md §15.
