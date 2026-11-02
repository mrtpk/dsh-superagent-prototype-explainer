# Writer brief (shared by every batch writer of "dsh-superagent Explained")

The supervisor's prompt gives you: the batch name, your pages and their scope, the visual (if any), and the
glossary terms you own. This file gives everything else. It is binding.

## This is an OVERVIEW site, not a full study guide
The user asked for an overview, not the nitty-gritty. Single depth, not the skill's usual two-depth
pattern:
- A short beginner start (one sentence, the idea, a diagram).
- Then one compact "More detail" section in prose: how the pieces fit together, what calls what, in what
  order, and the config knobs that change the behaviour. This replaces the skill's full "Deep dive".
- Reading the actual code is a LOW priority for the reader. Do not paste long code excerpts or do a
  line-by-line reading. A short `<x-code>` excerpt is fine when one line or a few lines make the point,
  but prefer saying what the code does in prose, with a `{{cite}}` to back it up.
- Where the repo's own docs go deeper (`docs/000-philosophy.md` through `docs/008-cookbook.md`), end the
  page with a one-line pointer to the matching doc instead of duplicating it. These docs are unusually
  thorough and already read like a tutorial sequence — lean on them, but still cite the code, not the doc,
  for every factual claim. Docs can be stale; the code cannot.
- Still: every claim about the code needs a citation. You open the cited lines yourself; "the docs say so"
  is not enough.

## There IS a sibling site — recap, do not re-teach
`../deepseek-harness-explainer` already teaches: Cordis plugins (`learn/plugins-and-cordis`), profiles and
bundles (`learn/profiles-and-bundles`), the turn/step/round session vocabulary
(`learn/session-and-loop-vocabulary`), skills (`concepts/skills`), and jobs/background work
(`concepts/jobs-workflow-goal-plan`). If your page touches one of these, give it **one sentence** and a
real link — do not re-explain the mechanism. Your job is what dsh-superagent itself adds on top: Source,
Trigger, Thread, Policy, Eval, Ticket, Executor, Effects, the Panel. This rule is binding for every batch,
not only `learn/what-this-is`.

**How to link to the sibling site (fixed in B2, do not redo this investigation):** use a real
`<a href="<dots>deepseek-harness-explainer/site/<page>.html">` link, not plain text naming the page.
`build.py`'s `check_links` has a narrow, verified allowance for this one sibling (see `explainer.json`'s
`sibling_sites`): it checks the target file actually exists on the sibling's built `site/`. Count `..`
levels from your own page's folder depth under `site/`: 3 `..` from a `learn/`, `concepts/`, `tours/`,
`code/` or `reference/` page; 2 `..` from the home page (`index.html`, at `site/` root). Example from a
concept page: `<a href="../../../deepseek-harness-explainer/site/concepts/skills.html">"Skills"</a>`.

## Paths
- Explainer folder: /mnt/c/Users/tpesc/Downloads/test-harness/dsh-superagent-prototype-explainer (git repo;
  do not commit: the supervisor commits).
- Target repo (READ ONLY, pinned): /mnt/c/Users/tpesc/Downloads/test-harness/dsh-superagent-prototype at
  6337fc823ce20251c8de8085948165c81aaa701e. Never change it.
- Sibling site: /mnt/c/Users/tpesc/Downloads/test-harness/deepseek-harness-explainer/site (already built;
  read its pages to recap correctly, but never edit it).

## Read first, in this order
1. STYLE.md (all of it).
2. plan.md §1-4 (goal, decisions, codebase facts, site structure) and the batch table (plan.md §13; find
   your batch).
3. instructions-svg.md (STYLE.md §10 overrides it: canvas 1100, min text 11).
4. notes/facts.md: [FC] and [S] entries are verified; [W] entries are not. Still open the code and cite it
   yourself.
5. The target repo's own `docs/000-philosophy.md` through `docs/008-cookbook.md` — read the ones that cover
   your batch's topic in full before you write.
6. The model page of your page type, once it exists (finished): `concepts/ticket-lifecycle.html` is the
   reference sample for concept pages (Phase 1a); later batches also copy the Phase 1b samples (home,
   `learn/what-this-is`, the tour).
7. ../mrtpk-agent-skills/skills/codebase-explainer/references/writing-and-accuracy.md and page-templates.md.

## Content rules
- Reader: knows TypeScript/Node well, and knows DSH/Cordis basics from the sibling site (see above). Does
  not know this project's own domain model.
- Every claim about the code: `{{cite path:line}}` or `<x-code>`. Open every cited line yourself. Narrowest
  range. No guesses — if the code does not answer a question, write it on the page as an open question and
  list it in your report.
- Scope: full pages for `src/`, `prompts/`, `skills/`, `cordis.patch.yml`, `scripts/dsh-superagent`. Out of
  scope, mention only in one line: `tests/` ("an unusually large test suite", do not walk through it),
  `locale/` (mentioned once as the i18n source, not a page), the two bundled Source skills' exact prompt
  text (link the file, do not reproduce it in full).
- `<x-simplified>` for simplifications. Site text in ASD-STE100 Simplified Technical English (short
  sentences, active voice, one instruction per sentence). Captions start with "Figure: ".
- Add a `<x-quiz>` "Check yourself" block at the end of every concept page, `learn/what-this-is`, and the
  tour (2-4 questions). Not on the code-map or reference pages.
- Diagrams: one script per diagram, Diagram(width=1100), max 3 boxes across, max 3 panels, no text below
  11. Prefix = your batch (diagrams/<batch>_*.py). This is a small site (target: 5-7 diagrams total,
  mostly one per concept page) — only add one where a picture genuinely clarifies the architecture.
- Literal tag syntax that is text (`{{cite}}`, `<x-code>`) must be escaped (`&#123;&#123;cite&#125;&#125;`).

## Prism note (avoid a known bug)
`explainer.json` lists `prism-markup` ahead of `prism-jsx`/`prism-tsx` because `src/client/` is real
`.tsx`. If you cite `.tsx` code, it will highlight correctly. Do not remove `prism-markup` from
`explainer.json` — removing it caused an uncaught TypeError on every page in the sibling project's build.

## Accuracy lessons
(The supervisor adds each repeated defect type here, with the trap and the correct place in the code.
Start with these — carried over from the sibling project, same kind of codebase and mistakes are likely.)
1. DEFAULTS: trace each default to where it is finally set (argument parsing, post-init hooks, platform
   code). Do not cite only a config class field or a type definition.
2. CONDITIONS: write "only when ..." where the code has a condition. No "always", "every", "all" unless you
   checked every path.
3. LINE RANGES: off-by-one is the most common defect. Open each cited range again after you finish the page.
4. COUNTS AND ORDER: "runs N times" or "before X" needs a check of every call site.
5. DOCS: the docs/000-008 series is thorough but still prose, not code. Cite the code. Report each
   docs-vs-code difference you find (FAQ material, or a note to the supervisor if it looks like a bug).
6. SINGLE COMMIT: this repo has exactly one commit (squashed for publication). Do not describe its git
   history, authorship, or commit messages as if normal development history exists.

## Ownership (parallel work)
- You own only: your page files, src/glossary/<batch>.json, diagrams/<batch>_*.py, and your visual
  assets/viz/<name>.js (shared visual styles only appended to assets/viz/viz.css).
- Search src/glossary/*.json before you add a term. Do not redefine; reuse with {{term id}}.
- Do NOT edit: build.py, assets/site.css, assets/site.js, nav files, other glossary files, notes/*,
  STYLE.md, plan.md, progress.md, other pages.
- Use `python3 build.py --preview` when another page is broken. Your pages must have 0 errors and no
  template or language warnings.

## No subagents
Do NOT start subagents or forks. The user allows 1 running agent at a time; you are it. Do all the work yourself.

## Claims that the code has a bug
Do NOT put a "this looks like a bug" claim on a page. Re-read the control flow twice (is the line inside or
after the loop or if? check the caller and the callee) and report it to the supervisor with exact lines.

## Report (final message only, no report files)
1. Pages written, diagrams, visual, glossary ids added.
2. Build result (errors and warnings for your pages).
3. NEW FACTS for notes/facts.md (each with file:line).
4. FACTS IN facts.md THAT ARE WRONG (with proof).
5. Claims you are less sure of (for the supervisor to spot-check hard).
6. Open questions, docs-vs-code differences, cross-page problems.
