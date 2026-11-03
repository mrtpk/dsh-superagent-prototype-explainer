"""What a Ticket is made of, and how a Trigger reaches one through a Subscription.

Used by: src/concepts/ticket-lifecycle.html
Sources (at the pinned commit in explainer.json):
  src/core/model.ts:125-133    Mandate: strength, scope, Policy version, basis; it never changes
  src/core/model.ts:277-308    Ticket: mandate, channels, assignments, inputs
  src/core/model.ts:218-233    Assignment: one binding to one Executor instance
  src/core/intake.ts:19-30     Intake.receive() stores a Trigger and finds its Threads
  src/core/model.ts:163-164    Thread.subscriptions: the Tickets subscribed to the Thread
  src/core/intake.ts:34-48     fan-out: every live subscribed Ticket on the Trigger's Threads
  src/core/intake.ts:49-52     the Trigger becomes a new Input on each Ticket reached
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import AMBER, BLUE, EMERALD, VIOLET, Diagram  # noqa: E402

d = Diagram(width=1100)
d.header("What a Ticket is made of, and how work reaches it",
         "Scope  ·  one open Ticket  ·  how a later Trigger becomes one of its Inputs",
         params="accept creates it  ·  canvas 1100")

y0 = 112
P1_H = 170
d.panel(y0, P1_H, 1, "What does an open Ticket hold?", "A Mandate it refers to, and Assignments it owns.")
bx_y, bw, bh = y0 + 70, 290, 76
d.box(46, bx_y, bw, bh, "Mandate", ["src/core/model.ts:125-133", "strength, scope, Policy ver."], col=BLUE)
d.arrow(46 + bw, bx_y + bh / 2, 400 - 2, bx_y + bh / 2, BLUE)
d.arrow_label(46 + bw + 32, bx_y + bh / 2, "accept creates", BLUE)
d.box(400, bx_y, bw, bh, "Ticket", ["src/core/model.ts:277-308", "mandate, channels, inputs"], col=EMERALD)
d.arrow(400 + bw, bx_y + bh / 2, 754 - 2, bx_y + bh / 2, EMERALD)
d.arrow_label(400 + bw + 32, bx_y + bh / 2, "holds", EMERALD)
d.box(754, bx_y, bw, bh, "Assignment[]", ["src/core/model.ts:218-233", "one binding per attempt"], col=VIOLET)

y1 = y0 + P1_H + 24
P2_H = 170
d.panel(y1, P2_H, 2, "How does a later Trigger reach that Ticket?", "A Subscription on the Thread fans it out as an Input.")
bx_y2 = y1 + 70
d.box(46, bx_y2, bw, bh, "Source → Trigger", ["src/core/intake.ts:19-30", "receive(trigger)"], col=AMBER)
d.arrow(46 + bw, bx_y2 + bh / 2, 400 - 2, bx_y2 + bh / 2, AMBER)
d.arrow_label(46 + bw + 32, bx_y2 + bh / 2, "trigger.threads", AMBER)
d.box(400, bx_y2, bw, bh, "Thread", ["src/core/model.ts:163-164", "subscriptions: string[]"], col=AMBER)
d.arrow(400 + bw, bx_y2 + bh / 2, 754 - 2, bx_y2 + bh / 2, AMBER)
d.arrow_label(400 + bw + 32, bx_y2 + bh / 2, "fan-out", AMBER)
d.box(754, bx_y2, bw, bh, "Ticket (Input)", ["src/core/intake.ts:49-52", "addInput(): a new Input"], col=EMERALD)

y = y1 + P2_H + 24
d.legend(30, y, [(BLUE, "Mandate — the authorization"), (EMERALD, "Ticket — the aggregate"),
                 (VIOLET, "Assignment — one Executor binding"), (AMBER, "intake flow")])
y += 40
y = d.footnotes(30, y, ["Note: a Ticket's Mandate is set once at accept and never changes after that (model.ts:125).",
                        "Not shown: Policy, Eval and Decision, which run before a Ticket exists."])
d.save(height=y + 14)
