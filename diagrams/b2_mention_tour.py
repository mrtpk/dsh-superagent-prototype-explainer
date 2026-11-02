"""Overview of the tour: a GitHub mention, through Eval, to a Ticket, a pull request, and the Ticket's end.

Used by: src/tours/life-of-a-github-mention.html
Sources (at the pinned commit in explainer.json):
  src/sources/github-trigger.ts:60-76   mentions() and commentTrigger() mark a mention
  src/policy.ts:191-211                 the gate: an allowed, addressed sender is explicit
  src/core/evals.ts:306-316             Evals.accept() creates the Mandate and the Ticket
  src/executor/dsh.ts:424-470           DshExecutor.launch() starts the worker Session
  src/sources/github-pull.ts:57-69      observePull() binds and later closes the pull request
  src/core/tickets.ts:77-90             Tickets.threadClosed() ends the Ticket
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import AMBER, BLUE, EMERALD, VIOLET, Diagram  # noqa: E402

d = Diagram(width=1100)
d.header("Life of a GitHub mention, in three parts",
         "Scope  ·  one explicit mention  ·  the stops this tour visits, grouped",
         params="13 numbered stops below group into 3 parts here")

y0 = 112
P_H = 152
cw = 322
CH = 78

d.panel(y0, P_H, 1, "How does a mention become a Ticket?", "Intake, the gate and Eval turn it into an accept.")
cy = y0 + 56
d.step_card(46, cy, cw, CH, 1, "A comment mentions the agent", BLUE,
            rows=[("at", "github-trigger.ts:71"), ("in", "intake.ts receive()")])
d.arrow(46 + cw + 4, cy + CH / 2, 46 + cw + 36, cy + CH / 2, BLUE)
d.step_card(46 + cw + 40, cy, cw, CH, 2, "The gate admits it as explicit", BLUE,
            rows=[("at", "policy.ts:197"), ("in", "evals.ts start()")])
d.arrow(46 + 2 * cw + 44, cy + CH / 2, 46 + 2 * cw + 76, cy + CH / 2, BLUE)
d.step_card(46 + 2 * (cw + 40), cy, cw, CH, 3, "Accept creates the Ticket", EMERALD,
            rows=[("at", "tickets.ts:37-56"), ("in", "evals.ts accept()")])

y1 = y0 + P_H + 20
d.panel(y1, P_H, 2, "How does the Ticket get its work done?", "The Executor launches a worker Session that opens a pull request.")
cy = y1 + 56
d.step_card(46, cy, cw, CH, 4, "The Executor launches a worker", VIOLET,
            rows=[("at", "dsh.ts:424-470"), ("in", "DshExecutor.launch()")])
d.arrow(46 + cw + 4, cy + CH / 2, 46 + cw + 36, cy + CH / 2, VIOLET)
d.step_card(46 + cw + 40, cy, cw, CH, 5, "The worker Session opens a PR", VIOLET,
            rows=[("at", "github-pull.ts:27-28"), ("in", "branch name match")])
d.arrow(46 + 2 * cw + 44, cy + CH / 2, 46 + 2 * cw + 76, cy + CH / 2, VIOLET)
d.step_card(46 + 2 * (cw + 40), cy, cw, CH, 6, "The worker reports ready", VIOLET,
            rows=[("at", "executor.ts:74-103"), ("in", "orchestrator_report")])

y2 = y1 + P_H + 20
d.panel(y2, P_H, 3, "How does the Ticket end?", "GitHub shows its own outcome, so no extra message repeats it there.")
cy = y2 + 56
d.step_card(46, cy, cw, CH, 7, "GitHub observes the PR close", AMBER,
            rows=[("at", "github-pull.ts:80-84"), ("in", "closePull()")])
d.arrow(46 + cw + 4, cy + CH / 2, 46 + cw + 36, cy + CH / 2, AMBER)
d.step_card(46 + cw + 40, cy, cw, CH, 8, "The Ticket ends", AMBER,
            rows=[("at", "tickets.ts:345-363"), ("in", "Tickets.end()")])

y = y2 + P_H + 24
d.legend(30, y, [(BLUE, "intake and the gate"), (EMERALD, "Eval's accept"), (VIOLET, "execution"), (AMBER, "closing")])
y += 40
y = d.footnotes(30, y, ["Simplified: this condenses the tour's 13 numbered stops into 3 parts; each x-stop below cites its own exact lines.",
                        "Not shown: the acknowledgement reply the accept sends back to GitHub before the worker starts."])
d.save(height=y + 14)
