"""How a role's system prompt is assembled, in order, and how an override or a bundled skill joins it.

Used by: src/concepts/prompts-and-skills.html
Sources (at the pinned commit in explainer.json):
  src/app/prompts.ts:14-17    TEAM_SECTIONS (communication, scope, delivery) and their headings
  src/app/prompts.ts:24-26    PART_KEYS, the 15 built-in parts a team may override
  src/app/prompts.ts:77-78    builtIn(): the team's override text, else the built-in default
  src/app/prompts.ts:102-116  promptParts(): the fixed join order for a role
  src/app/prompts.ts:111,114  runtime/admission and runtime/policy: orchestrator only
  src/app/prompts.ts:141-144  Prompts.compose(): environment for both roles, Policy for the main Session
  src/app/prompts.ts:146-148  Prompts.skills(): github always, feishu only if configured, then team skills
  src/app/runtime.ts:102      the feishu() check: setup complete and a Feishu bot in the deployment
  src/app/sessions.ts:319-324 bindSkills(): registers each as dsh-superagent-<name> in the Session's skill scope
  src/app/sessions.ts:248     the composed prompt gets a revision header and, for a live Ticket, a trailing mandate note
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import AMBER, BLUE, NEUTRAL, TEAL, VIOLET, Diagram  # noqa: E402

d = Diagram(width=1100)
d.header("How a role's system prompt is assembled",
         "Scope  ·  15 built-in parts, 3 team sections, 2 bundled Source skills  ·  composePrompt() joins the parts with blank lines",
         params="promptParts(), src/app/prompts.ts:102-116  ·  canvas 1100")

y0 = 112
P1_H = 346
d.panel(y0, P1_H, 1, "In what order are the parts joined?",
        "Top to bottom is the order promptParts() returns. Rows 8 and 11 are for the main Session only.")
card_y = y0 + 68
d.step_card(46, card_y, 1008, 256, 1, "A role's prompt, part by part", BLUE, tag="prompts.ts:102-116", rows=[
    ("1", "runtime/shared, then the role's own runtime/orchestrator or runtime/worker"),
    ("2", "communication (team section)", VIOLET[0]),
    ("3", "scope (team section)", VIOLET[0]),
    ("4", "delivery (team section)", VIOLET[0]),
    ("5", "subscriptions"),
    ("6", "replies"),
    ("7", "dispatch for the main Session, or work for a worker"),
    ("8", "admission — main Session only, dropped for a worker", AMBER[0]),
    ("9", "handoff/orchestrator or handoff/worker"),
    ("10", "environment (generated again for each model request)"),
    ("11", "policy — main Session only, generated, always last", AMBER[0]),
])
d.text(46, card_y + 256 + 18, "Unmarked rows are fixed text both roles read; a worker's own prompt skips rows 8 and 11.", 11.5, NEUTRAL[0], italic=True)

y1 = y0 + P1_H + 24
P2_H = 212
d.panel(y1, P2_H, 2, "Which text does a built-in part use?", "builtIn() reads the team's saved override only when one exists for that part.")
bx_y = y1 + 70
bw, bh, gap = 290, 72, 16
d.box(46, bx_y, bw, bh, "Built-in text", ["prompts/*.md files", "context.ts:7-24"], col=NEUTRAL)
d.box(46, bx_y + bh + gap, bw, bh, "Team override (optional)", ["config.overrides[part].text", "keeps every {placeholder}"], col=AMBER)
cx = 754
ch = bh * 2 + gap
d.box(cx, bx_y, bw, ch, "Text used for this part", ["builtIn(), prompts.ts:77-78", "override ?? built-in default"], col=BLUE)
d.arrow(46 + bw, bx_y + bh / 2, cx - 2, bx_y + ch * 0.32, NEUTRAL[0])
d.arrow_label(46 + bw + 60, bx_y + bh / 2 - 6, "if none saved", NEUTRAL[0])
d.arrow(46 + bw, bx_y + bh + gap + bh / 2, cx - 2, bx_y + ch * 0.68, AMBER[0])
d.arrow_label(46 + bw + 60, bx_y + bh + gap + bh / 2 + 16, "if saved", AMBER[0])

y2 = y1 + P2_H + 24
P3_H = 212
d.panel(y2, P3_H, 3, "Which Source skills does a Session get?", "github is always registered; feishu only when a Feishu bot is configured.")
bx_y2 = y2 + 70
d.box(46, bx_y2, bw, bh, "github skill", ["always registered", "prompts.ts:146-148"], col=NEUTRAL)
d.box(46, bx_y2 + bh + gap, bw, bh, "feishu skill", ["only if a Feishu bot is set up", "feishu() check, prompts.ts:147"], col=AMBER)
ch2 = bh * 2 + gap
d.box(cx, bx_y2, bw, ch2, "Session skill scope", ["dsh-superagent-<name>", "sessions.ts:319-324"], col=TEAL)
d.arrow(46 + bw, bx_y2 + bh / 2, cx - 2, bx_y2 + ch2 * 0.32, NEUTRAL[0])
d.arrow(46 + bw, bx_y2 + bh + gap + bh / 2, cx - 2, bx_y2 + ch2 * 0.68, AMBER[0])
d.callout(cx, bx_y2 + ch2 + 16, bw, "+ team skills:", "config.skills, registered the same way.", VIOLET[0], h=34)

y = y2 + P3_H + 24
d.legend(30, y, [(NEUTRAL, "built-in default"), (VIOLET, "team-authored"), (AMBER, "optional / main Session only"),
                 (BLUE, "composed result"), (TEAL, "registered in the Session's skill scope")])
y += 40
y = d.footnotes(30, y, [
    "Simplified: a worker's prompt has no admission or policy section at all, not an empty one (src/app/prompts.ts:111,114).",
    "Not shown: a part with empty text, such as an empty team section, is left out (src/app/prompts.ts:115).",
    "Not shown: the composed prompt gets a revision header and, for a live Ticket, a trailing mandate note (src/app/sessions.ts:248).",
])
d.save(height=y + 14)
