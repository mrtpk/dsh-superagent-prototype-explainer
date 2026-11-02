"""One Executor Session and directory per Ticket, and how WorkerSlots caps how many run at once.

Used by: src/concepts/executor-and-worker-sessions.html
Sources (at the pinned commit in explainer.json):
  src/core/ports.ts:59-69       Executor port: start(), deliver(), stop()
  src/executor/dsh.ts:207       DshExecutor: the only Executor implementation
  src/executor/dsh.ts:23-24     workerSessionId() -> "worker-<ticket id>"
  src/executor/dsh.ts:171-199   WorkerSlots: reserve()/free(), max() from settings
  src/executor/dsh.ts:192-194   reserve(): one extra slot only when by === 'person'
  src/executor/dsh.ts:305-310   a person's message wakes its worker ahead of new launches
  src/policy.ts:93              executor.maxWorkers default 3 (range 1-16, src/limits.ts:6)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import AMBER, BLUE, EMERALD, NEUTRAL, Diagram  # noqa: E402

d = Diagram(width=1100)
d.header("One Executor Session per Ticket, and the slot that reserves it",
         "Scope  ·  DshExecutor, the only Executor  ·  worker slots cap how many run at once",
         params="maxWorkers default = 3, range 1-16 (src/policy.ts:93)  ·  canvas 1100")

y0 = 112
P1_H = 170
d.panel(y0, P1_H, 1, "What does the Executor give a Ticket?", "One Session and one directory, reached through three port methods.")
bx_y, bw, bh = y0 + 70, 290, 76
d.box(46, bx_y, bw, bh, "Ticket", ["src/core/ports.ts:59-69", "start / deliver / stop(ticket, ...)"], col=NEUTRAL)
d.arrow(46 + bw, bx_y + bh / 2, 400 - 2, bx_y + bh / 2, BLUE)
d.arrow_label(46 + bw + 32, bx_y + bh / 2, "Executor port", BLUE)
d.box(400, bx_y, bw, bh, "DshExecutor", ["src/executor/dsh.ts:207", "the only Executor in this repo"], col=BLUE)
d.arrow(400 + bw, bx_y + bh / 2, 754 - 2, bx_y + bh / 2, EMERALD)
d.arrow_label(400 + bw + 32, bx_y + bh / 2, "one each", EMERALD)
d.box(754, bx_y, bw, bh, "Session + directory", ["src/executor/dsh.ts:23-24", "worker-<ticket id>"], col=EMERALD)

y1 = y0 + P1_H + 24
P2_H = 256
d.panel(y1, P2_H, 2, "How many Tickets can run at once?", "maxWorkers caps normal slots; a person's message may use one more.")
row1_y, bw2, bh2, gap = y1 + 70, 290, 76, 32
for i, label in enumerate(["Ticket A", "Ticket B", "Ticket C"]):
    x = 46 + i * (bw2 + gap)
    d.box(x, row1_y, bw2, bh2, label, ["launch running", "holds 1 of 3 normal slots"], col=BLUE)
row2_y = row1_y + bh2 + 24
bw3 = 460
d.box(46, row2_y, bw3, bh2, "Ticket D - person's message", ["dsh.ts:192-194, :305-310", "extra slot, by === 'person'"], col=AMBER)
d.box(46 + bw3 + 48, row2_y, bw3, bh2, "Ticket E - new launch", ["dsh.ts:194", "waits: used() >= max()"], col=NEUTRAL)

y = y1 + P2_H + 24
d.legend(30, y, [(BLUE, "running on a normal slot"), (EMERALD, "Session / directory"),
                 (AMBER, "the one extra slot, person only"), (NEUTRAL, "waits for a free slot")])
y += 40
y = d.footnotes(30, y, [
    "Simplified: WorkerSlots tracks ticket IDs in a Set, not numbered slots (src/executor/dsh.ts:171-180).",
    "Not shown: a Ticket also keeps its slot while shell jobs or subagents run after its turn ends (src/executor/dsh.ts:403-409).",
])
d.save(height=y + 14)
