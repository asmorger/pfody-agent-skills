# Schedule a recurring run

**When** transcripts keep arriving and the index should keep up without being asked.

**Why.** Three of the four steps are deterministic and idempotent, so they are safe to automate. Only
extraction needs a model, which is the one part that cannot be put on a timer unattended.

**Steps.**

1. **Automate `prepare` only**, or `prepare` plus a notification. It is cheap, safe and tells you
   whether there is anything to do
   ([`prepare-the-briefs.md`](prepare-the-briefs.md)).
2. **Keep extraction attended.** It is the step that can invent a citation, and it is the step whose
   quality is the index's quality
   ([`extract-knowledge-items.md`](extract-knowledge-items.md)).
3. **Wrap the four steps in one script** if the whole cycle is to run, and have it fail loudly rather
   than render a partial index.
4. **Pin the paths in a config file** rather than on the command line, so the scheduled run and a
   manual run cannot diverge ([`../patterns/tool-config.md`](../patterns/tool-config.md)).
5. **Windows Task Scheduler**, daily:

       $a = New-ScheduledTaskAction -Execute "python" -Argument "-m tkb.cli prepare --folder C:\Transcripts --state C:\kb\index.state.json"
       Register-ScheduledTask -TaskName "KB Prepare" -Action $a -Trigger (New-ScheduledTaskTrigger -Daily -At 7am)

6. **cron**, the same idea: one line invoking the same script, with absolute paths and the state file
   in a stable location.
7. **Keep the state file where the schedule can find it and nothing else writes it.** A state file
   lost between runs means the whole corpus is reprocessed
   ([`../patterns/state-file.md`](../patterns/state-file.md)).
8. **Review what accumulated** periodically rather than trusting the automation
   ([`curate-a-large-corpus.md`](curate-a-large-corpus.md)).

**Done when** the deterministic steps run on a schedule with absolute paths and a pinned config, the
extraction step is still a person's, and a failed run is visible rather than silently partial.
