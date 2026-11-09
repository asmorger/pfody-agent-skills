"""Trigger measurement: one single-turn `claude -p` per query, inside a fixture that holds the skills
and nothing else — no CLAUDE.md, no README, no project files — so a skill can only be reached through
its own description. A hit is a Skill tool call naming the skill. Single sample per query, so treat
+/-1 as noise. Each query is one `claude -p --max-turns 1` call, billed like any other.

    python3 scripts/measure-skill-triggers.py fixture              # (re)build the fixture
    python3 scripts/measure-skill-triggers.py run [N] [skill] [reps]   # N in parallel, reps per query

Keep N low. Nested `claude -p` calls contend with each other, and a contended call returns output
with no assistant turn - which `fired` reports as an error rather than as a non-trigger, because the
two are not the same measurement.

**Run this from a plain terminal, not from inside a Claude Code session.** A nested run inherits
CLAUDECODE=1 and CLAUDE_CODE_CHILD_SESSION=1, and measured triggering there is both lower and far
noisier than in a real session: two identical 56-query runs disagreed on 19% of their positives, and
one query that fires about a third of the time scored 0/5 in one batch. Precision survives that noise
- a false positive is a real finding - but **recall at reps=1 is not a measurement**, it is one coin
flip per query. Use reps=5 or more before believing a recall number, and treat a 1/5 as different
from a 4/5 rather than reading either as pass or fail.
    python3 scripts/measure-skill-triggers.py one "<query>"        # smoke-test one query

Queries live in skills/<skill>/evals/trigger-queries.json. Record a run's numbers in that skill's
evals/trigger-results.json by hand, with the analysis — the raw per-query output goes to
/tmp/trigger-raw.json. Rebuild the fixture after editing a skill: it copies the skills at build time.
Nested `claude -p` calls die silently under the rate limit (exit 1, empty output); `fired` backs off
and retries, and reports None (counted as an error) if every attempt fails.

A false negative here means the description does not reach the task. A false positive means it
reaches past it — usually a trigger phrase that belongs to a sibling skill.
"""
import json, subprocess, sys, shutil, pathlib, concurrent.futures as cf, time

REPO = pathlib.Path(__file__).resolve().parents[1]
FIXTURE = pathlib.Path("/tmp/trigger-fixture")
OUT = pathlib.Path("/tmp/trigger-raw.json")
SKILLS = sorted(p.name for p in (REPO / "skills").iterdir() if (p / "SKILL.md").exists())


def build_fixture():
    shutil.rmtree(FIXTURE, ignore_errors=True)
    (FIXTURE / ".claude").mkdir(parents=True)
    subprocess.run(["rsync", "-a", "--exclude", "__pycache__/", "--exclude", ".knowledge-index.work/",
                    str(REPO / "skills") + "/", str(FIXTURE / ".claude/skills") + "/"], check=True)
    subprocess.run(["git", "init", "-q"], cwd=FIXTURE, check=True)
    print("fixture at", FIXTURE, "with", ", ".join(SKILLS))


def fired(query, attempts=3):
    """Returns the skills a single turn invoked, or None when the run itself failed.

    A run that successfully fires a skill ends as `error_max_turns` with exit code 1, so the exit
    code says nothing. The signal that a run is MEANINGFUL is the presence of an assistant event:
    without one, the nested call died (rate limit, contention) and reporting [] would be scored as a
    deliberate non-trigger. That conflation silently depresses recall, so it is an error here."""
    for attempt in range(attempts):
        r = subprocess.run(["claude", "-p", query, "--output-format", "stream-json", "--verbose", "--max-turns", "1"],
                           cwd=FIXTURE, capture_output=True, text=True, timeout=300)
        hits, saw_assistant = set(), False
        for line in r.stdout.splitlines():
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if event.get("type") != "assistant":
                continue
            saw_assistant = True
            for block in event.get("message", {}).get("content", []):
                if block.get("type") == "tool_use" and block.get("name") == "Skill":
                    hits.add(str(block.get("input", {}).get("skill", "")).split(":")[-1])
        if saw_assistant:
            return sorted(hits)
        time.sleep(20 * (attempt + 1))  # nested calls die silently under the rate limit; back off
    return None


def run(parallel, only=None, reps=1):
    jobs = []
    for skill in ([only] if only else SKILLS):
        queries = REPO / f"skills/{skill}/evals/trigger-queries.json"
        if not queries.exists():
            print(f"{skill}: no evals/trigger-queries.json — skipped")
            continue
        for q in json.loads(queries.read_text()):
            jobs.extend([(skill, q["query"], q["should_trigger"])] * reps)
    results = []
    with cf.ThreadPoolExecutor(parallel) as pool:
        futures = {pool.submit(fired, query): (skill, query, should) for skill, query, should in jobs}
        for done, future in enumerate(cf.as_completed(futures), 1):
            skill, query, should = futures[future]
            hits = future.result()
            results.append({"skill": skill, "query": query, "should_trigger": should, "fired": hits})
            print(f"[{done}/{len(jobs)}] {skill} {'T' if should else 'F'} -> {hits} :: {query[:70]}", flush=True)
    OUT.write_text(json.dumps(results, indent=2))
    for skill in ([only] if only else SKILLS):
        rows = [r for r in results if r["skill"] == skill and r["fired"] is not None]
        if not rows:
            continue
        tp = sum(r["should_trigger"] and skill in r["fired"] for r in rows)
        fn = sum(r["should_trigger"] and skill not in r["fired"] for r in rows)
        fp = sum((not r["should_trigger"]) and skill in r["fired"] for r in rows)
        tn = sum((not r["should_trigger"]) and skill not in r["fired"] for r in rows)
        errors = sum(r["fired"] is None for r in results if r["skill"] == skill)
        print(f"{skill}: tp={tp} fn={fn} fp={fp} tn={tn} errors={errors} "
              f"recall={tp / max(tp + fn, 1):.2f} precision={tp / max(tp + fp, 1):.2f}"
              + ("  [recall from reps=1 is one coin flip per query - do not read it as pass/fail]"
                 if reps == 1 else f"  [reps={reps}]"))
        if reps > 1:  # per-query rates are the readable output of a repeated run
            seen = {}
            for r in results:
                if r["skill"] != skill or r["fired"] is None:
                    continue
                k = (r["query"], r["should_trigger"])
                seen.setdefault(k, []).append(skill in r["fired"])
            for (query, should), outcomes in sorted(seen.items(), key=lambda kv: -sum(kv[1]) / len(kv[1])):
                print(f"    {sum(outcomes)}/{len(outcomes)} {'T' if should else 'F'} :: {query[:72]}")


if __name__ == "__main__":
    command = sys.argv[1]
    if command == "fixture":
        build_fixture()
    elif command == "run":
        run(int(sys.argv[2]) if len(sys.argv) > 2 else 4,
            sys.argv[3] if len(sys.argv) > 3 and not sys.argv[3].isdigit() else None,
            int(sys.argv[-1]) if len(sys.argv) > 3 and sys.argv[-1].isdigit() else 1)
    elif command == "one":
        print(fired(sys.argv[2]))
