/* ticket-stage-stepper.js - step through the stage table of docs/003-execution.md:9-18.
 *
 * Mounts into <x-viz id="ticket-stage-stepper"> on concepts/ticket-lifecycle.html.
 * Vanilla JS, no libraries, no network. Every station's text is fixed (no randomness), so every
 * reader sees the same example ticket.
 *
 * Sources (at the pinned commit in explainer.json):
 *   docs/003-execution.md:9-18   the stage table itself (panel label column, condition column)
 *   src/core/stage.ts:9-21       ticketStage(): the first matching row of the table wins
 *   src/core/model.ts:349-353    waitsForPerson(): a later human message lifts blocked/failed
 *   src/core/model.ts:334        latestAssignment(): a ticket's current Assignment
 *   src/core/model.ts:336        latestReport(): the state any Assignment last reported
 *
 * Station order reads as a lifecycle (idle, queued, working, then a person-needed stage), not the
 * table's own top-to-bottom row order and not ticketStage()'s own check order (docs/003-execution.md's
 * table and ticketStage() both check person/delivery and person/answer before anything else).
 * This visual leaves out person/delivery (Input undelivered) - see the page's "Simplified" note.
 * Also left out: the exact retry backoff timers, and the "ended" stage (an ended ticket has no stage
 * at all - ticketStage is called only on an open ticket).
 *
 * Rules (STYLE.md section 10): IIFE scope; prefixed classes scoped under the mount; colours from the
 * site.css custom properties (dark mode works); real <button> elements (min 40 px); keyboard and
 * touch; an aria-live region; works at 390 px width; deterministic; a Reset button.
 */
(function () {
  "use strict";

  var VIZ_ID = "ticket-stage-stepper";

  var STATIONS = [
    {
      label: "Waiting for a Trigger", group: "idle", where: "src/core/stage.ts:19",
      condition: "The latest Report is “waiting”, or the Assignment ended.",
      detail: "The ticket finished its turn with no open question. A Trigger on a subscribed " +
        "Thread, or a person's message, can continue it from here.",
      part: "idle"
    },
    {
      label: "Queued", group: "working / queued", where: "src/core/stage.ts:18",
      condition: "No Assignment exists yet, or the latest one is still “pending”.",
      detail: "The ticket has a Mandate but no worker slot yet. It waits here until the " +
        "configured concurrency limit frees one (docs/003-execution.md:55-61).",
      part: "working"
    },
    {
      label: "Working", group: "working", where: "src/core/stage.ts:20",
      condition: "Everything else: an Assignment is running and nothing above matched.",
      detail: "This is the fallback row (ticketStage()'s last line). The worker's turn is " +
        "active, or it is busy with background shell jobs or subagents.",
      part: "working"
    },
    {
      label: "Awaiting review", group: "person / review", where: "src/core/stage.ts:15",
      condition: "The latest Report is “ready”.",
      detail: "A result is ready for a person, most often a pull request. “Awaiting review” " +
        "means a ready Report with a pull request (docs/003-execution.md:106).",
      part: "person"
    },
    {
      label: "Blocked", group: "person / blocked", where: "src/core/stage.ts:17",
      condition: "The latest Report is “blocked”, and no human message reached the ticket since.",
      detail: "waitsForPerson() (src/core/model.ts:349-353) is what makes this row hold: once a " +
        "later human message arrives, the ticket moves to the next matching row, usually Working.",
      part: "person"
    },
    {
      label: "Failed", group: "person / failed", where: "src/core/stage.ts:17",
      condition: "The latest Report is “failed”, and no human message reached the ticket since.",
      detail: "Same rule as Blocked, with the other report state. A retry starts a fresh " +
        "Assignment in the same Session, directory, branch and pull request.",
      part: "person"
    },
    {
      label: "Awaiting answer", group: "person / answer", where: "src/core/stage.ts:12",
      condition: "The ticket has an open Attention (a question for a person).",
      detail: "This row is checked second, right after “Input undelivered”, which this " +
        "visual leaves out. An answer, or the worker clearing the question, ends it.",
      part: "person"
    }
  ];
  var PART_COLOR = { idle: "var(--mute)", working: "var(--viz-c1)", person: "var(--viz-c4)" };
  var PART_NAME = { idle: "Between turns", working: "Active or waiting for a slot", person: "Needs a person" };

  var CSS = [
    ".tss-root{font-family:var(--sans);color:var(--ink)}",
    ".tss-rail{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 14px;padding:0;list-style:none}",
    ".tss-btn-station{min-width:40px;min-height:40px;padding:4px 10px;border:1px solid var(--line);",
    "  border-radius:6px;background:var(--surface);font:600 12.5px var(--sans);color:var(--ink);cursor:pointer;",
    "  text-align:left;line-height:1.2}",
    ".tss-btn-station[aria-current=step]{border-color:var(--tss-c,var(--blue));box-shadow:inset 0 -3px 0 var(--tss-c,var(--blue))}",
    ".tss-btn-num{display:inline-block;min-width:16px;font:700 12.5px var(--mono)}",
    ".tss-card{border-left:4px solid var(--tss-c,var(--line));padding:10px 16px;margin:0 0 12px;",
    "  background:var(--panel-bg);border-radius:0 8px 8px 0}",
    ".tss-kind{display:inline-block;font:700 10.5px var(--mono);letter-spacing:.04em;",
    "  text-transform:uppercase;color:var(--tss-c,var(--mute));margin:0 0 4px}",
    ".tss-title{margin:0 0 2px;font-weight:700;font-size:17px}",
    ".tss-where{margin:0 0 8px;font:12.5px var(--mono);color:var(--mute);overflow-wrap:anywhere}",
    ".tss-lede{margin:0 0 6px;font-size:14.5px}",
    ".tss-detail{margin:0;font-size:13.5px;color:var(--mute)}",
    ".tss-ctrl{display:flex;flex-wrap:wrap;gap:8px}",
    ".tss-btn{min-height:40px;padding:0 16px;border:1px solid var(--line);border-radius:6px;",
    "  background:var(--surface);color:var(--ink);font:600 14.5px var(--sans);cursor:pointer}",
    ".tss-btn:disabled{opacity:.45;cursor:default}",
    ".tss-live{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}",
    "@media (max-width:460px){.tss-btn-station{flex:1 1 40%}}"
  ].join("\n");

  function injectCss() {
    if (document.getElementById("tss-style")) return;
    var st = document.createElement("style");
    st.id = "tss-style";
    st.textContent = CSS;
    document.head.appendChild(st);
  }

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  function Viz(mount) {
    this.mount = mount;
    mount.innerHTML = ""; // removes the .viz-fallback text
    var root = el("div", "tss-root");

    this.rail = el("ol", "tss-rail");
    var self = this;
    this.stationBtns = STATIONS.map(function (s, i) {
      var li = el("li");
      var b = el("button", "tss-btn-station");
      b.type = "button";
      var num = el("span", "tss-btn-num", String(i + 1) + ". ");
      b.appendChild(num);
      b.appendChild(document.createTextNode(s.label));
      b.setAttribute("aria-label", "Stage " + (i + 1) + " of " + STATIONS.length + ": " + s.label);
      b.addEventListener("click", function () { self.go(i); });
      li.appendChild(b);
      self.rail.appendChild(li);
      return b;
    });

    this.card = el("div", "tss-card");
    this.kindEl = el("p", "tss-kind");
    this.titleEl = el("p", "tss-title");
    this.whereEl = el("p", "tss-where");
    this.ledeEl = el("p", "tss-lede");
    this.detailEl = el("p", "tss-detail");
    [this.kindEl, this.titleEl, this.whereEl, this.ledeEl, this.detailEl].forEach(function (e) {
      self.card.appendChild(e);
    });

    var ctrl = el("div", "tss-ctrl");
    this.prev = el("button", "tss-btn", "← Previous");
    this.next = el("button", "tss-btn", "Next →");
    var rst = el("button", "tss-btn", "Reset");
    [this.prev, this.next, rst].forEach(function (b) { b.type = "button"; ctrl.appendChild(b); });

    this.live = el("div", "tss-live");
    this.live.setAttribute("aria-live", "polite");

    this.prev.addEventListener("click", function () { self.go(self.i - 1); });
    this.next.addEventListener("click", function () { self.go(self.i + 1); });
    rst.addEventListener("click", function () { self.go(0); });

    root.appendChild(this.rail);
    root.appendChild(this.card);
    root.appendChild(ctrl);
    root.appendChild(this.live);
    mount.appendChild(root);

    this.go(0, true);
  }

  Viz.prototype.go = function (i, quiet) {
    if (i < 0 || i >= STATIONS.length) return;
    this.i = i;
    var s = STATIONS[i];
    var col = PART_COLOR[s.part] || "var(--line)";
    this.card.style.setProperty("--tss-c", col);
    this.kindEl.textContent = PART_NAME[s.part] + " · panel label “" + s.group + "”";
    this.kindEl.style.setProperty("--tss-c", col);
    this.titleEl.textContent = (i + 1) + ". " + s.label;
    this.whereEl.textContent = s.where + " (first matching row wins)";
    this.ledeEl.textContent = s.condition;
    this.detailEl.textContent = s.detail;
    this.stationBtns.forEach(function (b, k) {
      b.style.setProperty("--tss-c", PART_COLOR[STATIONS[k].part] || "var(--line)");
      if (k === i) b.setAttribute("aria-current", "step"); else b.removeAttribute("aria-current");
    });
    this.prev.disabled = i === 0;
    this.next.disabled = i === STATIONS.length - 1;
    if (!quiet) {
      this.live.textContent = "Stage " + (i + 1) + " of " + STATIONS.length + ": " + s.label + ". " + s.condition;
    }
  };

  function init() {
    injectCss();
    var mounts = document.querySelectorAll('[data-viz="' + VIZ_ID + '"]');
    Array.prototype.forEach.call(mounts, function (m) { new Viz(m); });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
