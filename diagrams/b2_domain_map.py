"""What dsh-superagent is, and what it adds on top of DSH and Cordis.

Used by: src/learn/what-this-is.html
Sources (at the pinned commit in explainer.json):
  package.json (dsh.bundle.patch)   dsh-superagent is packaged as a DSH bundle
  cordis.patch.yml                  the Cordis plugin set the bundle installs
  src/core/model.ts:276-308         Ticket: the domain model's own unit of work
  src/executor/dsh.ts:207-266       DshExecutor: the port that runs Assignments
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import AMBER, BLUE, EMERALD, VIOLET, Diagram  # noqa: E402

d = Diagram(width=1100)
d.header("What dsh-superagent is, and what it adds",
         "Scope  ·  where this project sits  ·  the domain model it adds on top",
         params="one Cordis plugin set, packaged as one DSH bundle")

y0 = 112
P1_H = 170
d.panel(y0, P1_H, 1, "What does dsh-superagent run inside?", "A DSH profile loads it as a Cordis plugin set.")
bx_y, bw, bh = y0 + 70, 290, 76
d.box(46, bx_y, bw, bh, "Cordis", ["plugins, services, typed events", "DSH's own plugin runtime"], col=BLUE)
d.arrow(46 + bw, bx_y + bh / 2, 400 - 2, bx_y + bh / 2, BLUE)
d.arrow_label(46 + bw + 32, bx_y + bh / 2, "profile loads", BLUE)
d.box(400, bx_y, bw, bh, "DSH Session", ["profiles, bundles", "turn / step / round"], col=BLUE)
d.arrow(400 + bw, bx_y + bh / 2, 754 - 2, bx_y + bh / 2, BLUE)
d.arrow_label(400 + bw + 32, bx_y + bh / 2, "bundle = this repo", BLUE)
d.box(754, bx_y, bw, bh, "dsh-superagent", ["cordis.patch.yml", "the superagent profile"], col=EMERALD)

y1 = y0 + P1_H + 24
P2_H = 170
d.panel(y1, P2_H, 2, "What domain model does it add?", "Three groups of concepts this site explains, not DSH's own.")
bx_y2 = y1 + 70
d.box(46, bx_y2, bw, bh, "Source, Trigger", ["src/sources/github.ts", "events in, replies out"], col=AMBER)
d.arrow(46 + bw, bx_y2 + bh / 2, 400 - 2, bx_y2 + bh / 2, AMBER)
d.arrow_label(46 + bw + 32, bx_y2 + bh / 2, "Eval decides", AMBER)
d.box(400, bx_y2, bw, bh, "Policy, Eval", ["src/core/evals.ts", "who may ask for work"], col=AMBER)
d.arrow(400 + bw, bx_y2 + bh / 2, 754 - 2, bx_y2 + bh / 2, AMBER)
d.arrow_label(400 + bw + 32, bx_y2 + bh / 2, "accept creates", AMBER)
d.box(754, bx_y2, bw, bh, "Ticket, Executor", ["src/core/model.ts:276-308", "the authorized work itself"], col=VIOLET)

y = y1 + P2_H + 24
d.legend(30, y, [(BLUE, "DSH and Cordis — the sibling site's territory"),
                 (AMBER, "intake and authorization — new in this project"),
                 (VIOLET, "execution — new in this project")])
y += 40
y = d.footnotes(30, y, ["Simplified: a fourth group, the prompts and the React panel, is left off this map; concept pages cover them.",
                        "Not shown: Feishu, the project's second Source kind, which follows the same Source contract as GitHub."])
d.save(height=y + 14)
