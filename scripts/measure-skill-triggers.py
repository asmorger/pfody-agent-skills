"""Trigger measurement: one single-turn `claude -p` per query, inside a fixture that holds the skills
and nothing else — no CLAUDE.md, no README, no project files — so a skill can only be reached through
its own description. A hit is a Skill tool call naming the skill. Single sample per query, so treat
+/-1 as noise. Each query is one `claude -p --max-turns 1` call, billed like any other.

    python3 scripts/measure-skill-triggers.py fixture              # (re)build the fixture
    python3 scripts/measure-skill-triggers.py run [N] [skill]      # all queries (or one skill's), N in parallel
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
    for attempt in range(attempts):
        r = subprocess.run(["claude", "-p", query, "--output-format", "stream-json", "--verbose", "--max-turns", "1"],
                           cwd=FIXTURE, capture_output=True, text=True, timeout=300)
        if r.returncode == 0 or r.stdout.strip():
            hits = set()
            for line in r.stdout.splitlines():
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if event.get("type") != "assistant":
                    continue
                for block in event.get("message", {}).get("content", []):
                    if block.get("type") == "tool_use" and block.get("name") == "Skill":
                        hits.add(str(block.get("input", {}).get("skill", "")).split(":")[-1])
            return sorted(hits)
        time.sleep(20 * (attempt + 1))  # nested calls die silently under the rate limit; back off
    return None


def run(parallel, only=None):
    jobs = []
    for skill in ([only] if only else SKILLS):
        queries = REPO / f"skills/{skill}/evals/trigger-queries.json"
        if not queries.exists():
            print(f"{skill}: no evals/trigger-queries.json — skipped")
            continue
        for q in json.loads(queries.read_text()):
            jobs.append((skill, q["query"], q["should_trigger"]))
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
              f"recall={tp / max(tp + fn, 1):.2f} precision={tp / max(tp + fp, 1):.2f}")


if __name__ == "__main__":
    command = sys.argv[1]
    if command == "fixture":
        build_fixture()
    elif command == "run":
        run(int(sys.argv[2]) if len(sys.argv) > 2 else 4, sys.argv[3] if len(sys.argv) > 3 else None)
    elif command == "one":
        print(fired(sys.argv[2]))
