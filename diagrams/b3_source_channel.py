"""How a native event becomes a Trigger on a Thread, and how a reply gets back through a Channel.

Used by: src/concepts/sources-and-triggers.html
Sources (at the pinned commit in explainer.json):
  src/sources/github-trigger.ts:65-77   commentTrigger() builds a Trigger from one GitHub comment
  src/core/model.ts:23-39               Trigger: threads, actor, human, addressed
  src/core/model.ts:157-182             Thread: the aggregate a Trigger's threads[0] names
  src/core/model.ts:9                   ChannelRef: source, thread, address
  src/sources/github-trigger.ts:8-9     githubChannel() builds the reply address
  src/sources/registry.ts:95-98         SourceRegistry.send() hands the message to the Source kind's channel
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import AMBER, BLUE, EMERALD, Diagram  # noqa: E402

d = Diagram(width=1100)
d.header("From one GitHub comment to a Trigger, a Thread, and back",
         "Scope  ·  one Source instance (GitHub)  ·  the write side uses the same address",
         params="one PR/Issue number = one Thread  ·  canvas 1100")

y0 = 112
P1_H = 170
d.panel(y0, P1_H, 1, "What turns a native event into domain objects?", "One Source instance normalizes it into a Trigger on a Thread.")
bx_y, bw, bh = y0 + 70, 290, 76
d.box(46, bx_y, bw, bh, "Source instance (github)", ["src/sources/github-trigger.ts:65-77", "commentTrigger(comment, ref)"], col=BLUE)
d.arrow(46 + bw, bx_y + bh / 2, 400 - 2, bx_y + bh / 2, BLUE)
d.arrow_label(46 + bw + 32, bx_y + bh / 2, "produces", BLUE)
d.box(400, bx_y, bw, bh, "Trigger", ["src/core/model.ts:23-39", "id, threads, actor, addressed"], col=EMERALD)
d.arrow(400 + bw, bx_y + bh / 2, 754 - 2, bx_y + bh / 2, EMERALD)
d.arrow_label(400 + bw + 32, bx_y + bh / 2, "threads[0]", EMERALD)
d.box(754, bx_y, bw, bh, "Thread", ["src/core/model.ts:157-182", "one PR/Issue number"], col=AMBER)

y1 = y0 + P1_H + 24
P2_H = 170
d.panel(y1, P2_H, 2, "How does a reply reach the same place?", "The Channel is the Thread's write side, in the Source's own address format.")
bx_y2 = y1 + 70
d.box(46, bx_y2, bw, bh, "Trigger.channel", ["src/core/model.ts:9", "ChannelRef: source, thread, address"], col=EMERALD)
d.arrow(46 + bw, bx_y2 + bh / 2, 400 - 2, bx_y2 + bh / 2, EMERALD)
d.arrow_label(46 + bw + 32, bx_y2 + bh / 2, "same address", EMERALD)
d.box(400, bx_y2, bw, bh, "Channel", ["src/sources/github-trigger.ts:8-9", "githubChannel(number, url)"], col=AMBER)
d.arrow(400 + bw, bx_y2 + bh / 2, 754 - 2, bx_y2 + bh / 2, AMBER)
d.arrow_label(400 + bw + 32, bx_y2 + bh / 2, "kind.channel.send()", AMBER)
d.box(754, bx_y2, bw, bh, "Source instance (github)", ["src/sources/registry.ts:95-98", "SourceRegistry.send()"], col=BLUE)

y = y1 + P2_H + 24
d.legend(30, y, [(BLUE, "Source instance"), (EMERALD, "Trigger / its Channel"), (AMBER, "Thread / Channel delivery")])
y += 40
y = d.footnotes(30, y, ["Simplified: one comment makes one Trigger here; an opened Issue or PR instead uses issueTrigger()/pullTrigger().",
                        "Not shown: the SourceScope filter that can drop a Trigger before it reaches a Thread at all."])
d.save(height=y + 14)
