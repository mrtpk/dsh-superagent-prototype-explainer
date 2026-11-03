"""The React panel's calls to the loopback Management API, the six tabs, and how a save versions safely.

Used by: src/concepts/panel-and-management-api.html
Sources (at the pinned commit in explainer.json):
  src/client/api.ts:33-37      api(): fetch('/orchestrator/api/<path>') with header x-orchestrator-request: 1
  src/app/http.ts:230-246      registerHttp(): the /orchestrator/api/ prefix, loopback host required, same-origin checked
  src/app/http.ts:75-79        sameOrigin(): host, marker header and Origin check
  scripts/dsh-superagent:81-84 the CLI script's own status check, same route and header
  src/client/route.ts:7        TABS, the six tab ids in order
  src/client/app.tsx:147-159   Pages(): one view per tab
  docs/005-panel.md:17-24      what each tab shows (the row texts in panel 2)
  src/app/versions.ts:21-28    Versions.save(): a full numbered snapshot, used by both Settings and Prompts
  src/app/store.ts:188         Store.blockRevision(): one counter per settings block
  src/app/settings.ts:150-151  a stale block revision throws SettingsConflict
  src/app/prompts.ts:206       a stale prompt revision throws PromptConflict
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import AMBER, BLUE, NEUTRAL, PINK, TEAL, Diagram  # noqa: E402

d = Diagram(width=1100)
d.header("The panel, the Management API, and how a save versions",
         "Scope  ·  one loopback HTTP API behind one same-origin check  ·  the panel and scripts/dsh-superagent both call it",
         params="registerHttp(), src/app/http.ts:230-246  ·  canvas 1100")

y0 = 112
P1_H = 170
d.panel(y0, P1_H, 1, "What calls the Management API, and how?", "A fetch with one marker header; the host checks it is loopback and same-origin.")
bx_y, bw, bh = y0 + 70, 290, 76
d.box(46, bx_y, bw, bh, "React panel", ["src/client/api.ts:37", "fetch('/orchestrator/api/...')"], col=BLUE)
d.arrow(46 + bw, bx_y + bh / 2, 400 - 2, bx_y + bh / 2, BLUE[0])
d.arrow_label(46 + bw + 32, bx_y + bh / 2, "x-orchestrator-request: 1", BLUE[0])
d.box(400, bx_y, bw, bh, "Management API", ["http.ts:230-246", "loopback + same-origin only"], col=TEAL)
d.arrow(400 + bw, bx_y + bh / 2, 754 - 2, bx_y + bh / 2, NEUTRAL[0])
d.arrow_label(400 + bw + 32, bx_y + bh / 2, "reads / writes", NEUTRAL[0])
d.box(754, bx_y, bw, bh, "Store, Prompts, Settings, Engine", ["src/app/*.ts"], col=NEUTRAL)

y1 = y0 + P1_H + 24
P2_H = 196
d.panel(y1, P2_H, 2, "What do the six tabs show?", "What each tab shows, as docs/005-panel.md:17-24 lists it.")
d.step_card(46, y1 + 70, 1008, 110, 1, "The panel's tabs, in order", BLUE, tag="route.ts:7", rows=[
    ("Overview", "needs-action items, problems, 24h activity, Executor load"),
    ("Source", "Source state, setup problems, filtered and dropped counts"),
    ("Trigger", "Threads by filter, each one's Triggers and Decisions"),
    ("Eval", "Decisions with their reason and matched rules"),
    ("Execution", "Executor state, the pause switch, Tickets by filter"),
    ("Settings", "Sources, Eval, Execution, Prompts and Deployment"),
])

y2 = y1 + P2_H + 24
P3_H = 170
d.panel(y2, P3_H, 3, "How does a save version safely?", "A full snapshot, plus one counter per block, so a stale save is refused, not overwritten.")
bx_y2 = y2 + 70
d.box(46, bx_y2, bw, bh, "Whole-object snapshot", ["Versions.save(), versions.ts:21-28", "one history for Settings, one for Prompts"], col=NEUTRAL)
d.arrow(46 + bw, bx_y2 + bh / 2, 400 - 2, bx_y2 + bh / 2, AMBER[0])
d.box(400, bx_y2, bw, bh, "One counter per block", ["store.blockRevision(), store.ts:188", "pause / eval / executor / policy / source:id"], col=AMBER)
d.arrow(400 + bw, bx_y2 + bh / 2, 754 - 2, bx_y2 + bh / 2, PINK[0])
d.box(754, bx_y2, bw, bh, "Stale revision → 409 Conflict", ["SettingsConflict, settings.ts:150-151", "PromptConflict, prompts.ts:206"], col=PINK)

y = y2 + P3_H + 24
d.legend(30, y, [(BLUE, "the panel's own call"), (TEAL, "the Management API"), (NEUTRAL, "host state / full snapshot"),
                 (AMBER, "per-block version counter"), (PINK, "optimistic-concurrency conflict")])
y += 40
y = d.footnotes(30, y, [
    "Not shown: scripts/dsh-superagent status calls the same GET /orchestrator/api/state route, with the same header (scripts/dsh-superagent:81-84).",
    "Simplified: settings.ts also refuses some fields, such as the execution directory, from any origin but the panel itself (settings.ts:44-45,50-51).",
])
d.save(height=y + 14)
