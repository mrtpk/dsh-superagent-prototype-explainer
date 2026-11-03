"""How the gate judges a Trigger, and what an accept decision builds from it.

Used by: src/concepts/policy-and-authorization.html
Sources (at the pinned commit in explainer.json):
  src/core/evals.ts:94-101    Evals.start() calls policy.gate() per pending Trigger, keeps the strongest
  src/policy.ts:191-211       settingsPolicy(...).gate(): explicit checks (197, 204), then follow-up (206), then inferred cell (209)
  src/core/evals.ts:271-273   directEval(): the one other gate call, for a single Trigger
  src/core/ports.ts:7         GateResult: admissible:false+reason, or admissible:true+strength+basis
  src/core/evals.ts:306-316   Evals.accept() records the Decision and builds the Mandate
  src/core/model.ts:125-133   Mandate: strength, policyVersion, basis, actor, scope
  src/core/evals.ts:118       assessor.request() runs for every queued Eval, explicit or inferred
  src/app/assessment.ts:39,109-113  an explicit candidate is routed, not assessed
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import AMBER, BLUE, EMERALD, Diagram  # noqa: E402

d = Diagram(width=1100)
d.header("From a queued Trigger to a Mandate",
         "Scope  ·  one Thread's pending Triggers  ·  only accept creates a Mandate",
         params="gate runs once per pending Trigger  ·  canvas 1100")

y0 = 112
P1_H = 170
d.panel(y0, P1_H, 1, "What does the gate check on each Trigger?", "The strongest admissible Trigger gives the batch its strength.")
bx_y, bw, bh = y0 + 70, 290, 76
d.box(46, bx_y, bw, bh, "Trigger", ["src/core/model.ts:23-39", "human, addressed, actor"], col=AMBER)
d.arrow(46 + bw, bx_y + bh / 2, 400 - 2, bx_y + bh / 2, AMBER)
d.arrow_label(46 + bw + 32, bx_y + bh / 2, "policy.gate()", AMBER)
d.box(400, bx_y, bw, bh, "gate(trigger, thread, tickets)", ["src/policy.ts:191-211", "explicit → follow-up → inferred"], col=BLUE)
d.arrow(400 + bw, bx_y + bh / 2, 754 - 2, bx_y + bh / 2, BLUE)
d.arrow_label(400 + bw + 32, bx_y + bh / 2, "returns", BLUE)
d.box(754, bx_y, bw, bh, "GateResult", ["src/core/ports.ts:7", "admissible, strength, basis"], col=EMERALD)

y1 = y0 + P1_H + 24
P2_H = 170
d.panel(y1, P2_H, 2, "What does an accept decision build?", "Eval keeps the strongest GateResult; only accept creates a Mandate.")
bx_y2 = y1 + 70
d.box(46, bx_y2, bw, bh, "Eval (batch)", ["src/core/evals.ts:94-101", "keeps the strongest GateResult"], col=EMERALD)
d.arrow(46 + bw, bx_y2 + bh / 2, 400 - 2, bx_y2 + bh / 2, EMERALD)
d.arrow_label(46 + bw + 32, bx_y2 + bh / 2, "assessment accepts", EMERALD)
d.box(400, bx_y2, bw, bh, "Decision (accept)", ["src/core/evals.ts:306-316", "strength, reason, policyVersion"], col=BLUE)
d.arrow(400 + bw, bx_y2 + bh / 2, 754 - 2, bx_y2 + bh / 2, BLUE)
d.arrow_label(400 + bw + 32, bx_y2 + bh / 2, "carries", BLUE)
d.box(754, bx_y2, bw, bh, "Mandate", ["src/core/model.ts:125-133", "strength, scope, Policy version"], col=AMBER)

y = y1 + P2_H + 24
d.legend(30, y, [(AMBER, "Trigger / Mandate"), (BLUE, "the gate / the Decision"), (EMERALD, "GateResult / the Eval")])
y += 40
y = d.footnotes(30, y, ["Simplified: the gate's admission table and bot checks are collapsed into one box here; concepts/policy-and-authorization spells them out.",
                        "Not shown: the main Session between the gate and a Decision; it assesses an inferred candidate and routes an explicit one."])
d.save(height=y + 14)
