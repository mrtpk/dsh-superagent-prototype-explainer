"""How a queued effect survives a crash, and which part of Store each writer owns.

Used by: src/concepts/effects-and-store.html
Sources (at the pinned commit in explainer.json):
  src/app/effects.ts:42-45    Effects: persists side effects inside command transactions, dispatches after commit
  src/app/effects.ts:60-66    enqueue(): upserts a row in the caller's transaction
  src/app/store.ts:80-82      the effect table: PRIMARY KEY (kind, key), one row per pair
  src/app/effects.ts:67-74    handle(): exactly one handler per effect kind
  src/core/engine.ts:19-20    Engine: the single writer of Triggers, Threads, Decisions, Tickets, Assignments
  src/app/store.ts:253        "only Outbox writes to receipts"
  src/app/runtime.ts:90-93    the state-directory lock taken before Store opens
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import AMBER, BLUE, EMERALD, NEUTRAL, Diagram  # noqa: E402

d = Diagram(width=1100)
d.header("The effect queue, and who may write which part of Store",
         "Scope  ·  one SQLite file, one process  ·  a durable row, run only after its transaction commits",
         params="6 effect kinds, 1 handler each  ·  canvas 1100")

y0 = 112
P1_H = 170
d.panel(y0, P1_H, 1, "How does a side effect survive a crash?", "It is a row in Store before it is a promise in memory.")
bx_y, bw, bh = y0 + 70, 290, 76
d.box(46, bx_y, bw, bh, "A command", ["src/app/effects.ts:60-66", "enqueue(kind, key, payload)"], col=NEUTRAL)
d.arrow(46 + bw, bx_y + bh / 2, 400 - 2, bx_y + bh / 2, BLUE)
d.arrow_label(46 + bw + 32, bx_y + bh / 2, "in the transaction", BLUE)
d.box(400, bx_y, bw, bh, "effect row (Store)", ["src/app/store.ts:80-82", "PRIMARY KEY (kind, key)"], col=BLUE)
d.arrow(400 + bw, bx_y + bh / 2, 754 - 2, bx_y + bh / 2, EMERALD)
d.arrow_label(400 + bw + 32, bx_y + bh / 2, "after commit", EMERALD)
d.box(754, bx_y, bw, bh, "Handler", ["src/app/effects.ts:67-74", "exactly one per kind"], col=EMERALD)

y1 = y0 + P1_H + 24
P2_H = 196
d.panel(y1, P2_H, 2, "Who may write which state?", "Engine owns the domain aggregates; Outbox owns its own receipts.")
row_y, bwA, bwB, gap = y1 + 70, 230, 400, 40
d.box(46, row_y, bwA, bh, "Engine", ["src/core/engine.ts:19-20", "the single writer"], col=BLUE)
d.arrow(46 + bwA, row_y + bh / 2, 46 + bwA + gap - 2, row_y + bh / 2, BLUE)
d.arrow_label(46 + bwA + gap / 2, row_y + bh / 2, "writes", BLUE)
d.box(46 + bwA + gap, row_y, bwB, bh, "Trigger · Thread · Decision · Ticket", ["Triggers, Threads, Decisions,", "Tickets, Assignments"], col=NEUTRAL)
row_y2 = row_y + bh + 24
d.box(46, row_y2, bwA, bh, "Outbox", ["src/app/store.ts:253", "only writer of receipts"], col=AMBER)
d.arrow(46 + bwA, row_y2 + bh / 2, 46 + bwA + gap - 2, row_y2 + bh / 2, AMBER)
d.arrow_label(46 + bwA + gap / 2, row_y2 + bh / 2, "writes", AMBER)
d.box(46 + bwA + gap, row_y2, bwB, bh, "receipts (Store table)", ["one row per message id,", "pending / sent / dropped"], col=NEUTRAL)

y = y1 + P2_H + 24
d.legend(30, y, [(BLUE, "Engine and the domain tables"), (EMERALD, "a handler running after commit"),
                 (AMBER, "Outbox and its receipts"), (NEUTRAL, "a Store table")])
y += 40
y = d.footnotes(30, y, [
    "Simplified: settings, prompts and key-value records have their own writers too; only the domain aggregates and the",
    "  outbox receipts are shown here (src/app/store.ts:183-199, :251-254).",
    "Not shown: the directory lock Runtime takes before it opens Store, so a second process cannot write it too (src/app/runtime.ts:90-93).",
])
d.save(height=y + 14)
