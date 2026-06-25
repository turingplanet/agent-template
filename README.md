# agent-template — the starter kit (Copier template)

> **Part of 图灵星球 Agent 军团.** New here? Start at the overview: **https://github.com/turingplanet/agent-legion**

This is a **[Copier](https://copier.readthedocs.io) template** for creating a new agent. A Copier-scaffolded repo records which template version it came from (in `.copier-answers.yml`), so it can pull future template changes with **`copier update`**. That provenance is what lets the platform ship **safe, automated migration PRs** across the whole fleet.

## Create a new agent

**1. Install Copier** (one-time):
```bash
pipx install copier      # or: pip install copier
```

**2. Scaffold your repo** — Copier asks a few questions, then writes the files:
```text
$ copier copy gh:turingplanet/agent-template ./my-agent
🎤 Human-readable name of your agent
   my-agent
🎤 Package-style slug (lowercase, hyphens)
   my-agent
🎤 One-line description of your agent
   An 图灵星球 Agent 军团 member agent.
🎤 Your name / 🎤 Your email
   you / you@example.com
Copying from template version v0.0.7
   create  .copier-answers.yml      ← records the template version
   create  agent.manifest.yaml
   create  api/server.py
   create  mcp/server.py
   create  tests/test_smoke.py
   create  pyproject.toml
   create  .github/workflows/review.yml
```

**3. Turn it into a repo you own and push it:**
```bash
cd my-agent
git init && git add -A && git commit -m "Scaffold from agent-template"
gh repo create my-agent --private --source . --push
```

**(Optional) Enable the AI review.** The advisory reviewer stays **off** until you give it a key — without one the step skips gracefully (and fork PRs never receive it). To turn it on, add *your own* Anthropic API key as a repo secret (billed to your account):
```bash
gh secret set ANTHROPIC_API_KEY     # run inside your repo; paste the key when prompted
```

**4. Confirm the pipeline is green (smoke test).** The scaffold passes review out of the box, so open a throwaway PR *first* — this proves the gate works before you write any real code. A one-line README edit is ideal: it triggers the flow but can't trip `tests`/`lint`/`security` (those run on `/api`).
```bash
git switch -c smoke-test
printf '\n<!-- smoke-test: confirm the review pipeline is green -->\n' >> README.md
git commit -am "chore: smoke-test the review pipeline"
git push -u origin smoke-test
gh pr create --fill        # opens the PR; the policies@vN gate runs automatically
```
The hard checks run (**install · tests · lint · security**) and the gate decides. If you've set an `ANTHROPIC_API_KEY` repo secret, the advisory AI review also posts a comment (with a token-usage + estimated-cost line) — it never blocks. Once it's green, clean up:
```bash
gh pr merge --squash --delete-branch     # or, to discard it: gh pr close --delete-branch
```

**5. Make it yours.** Replace the placeholder `run()` in `/api`, expose it in `/mcp`, add real tests — then open a pull request. The review flow runs and the gate decides.

Later, run **`copier update`** in your repo to pull template improvements as a PR (your `.copier-answers.yml` is what makes that possible).

## Pull future template changes (in a generated repo)

`copier update` always targets the **latest** template version — you never name a version. Run it on a branch, open a PR so the gate runs, then merge:

```bash
git switch -c chore/template-sync
copier update --defaults --trust --conflict inline   # pull the latest template updates (keeps your code)
git add -A && git commit -m "chore: sync to the latest agent-template"
git push -u origin chore/template-sync
gh pr create --fill        # your policies@vN gate runs on the sync PR
# review the diff; resolve any <<<<<<< conflict markers if present, then:
gh pr merge --squash --delete-branch
git switch main && git pull   # back on main with the sync merged in
```

**What `copier update` does:** it merges the template's updates into your repo *without* overwriting your work. Your own code (`/api`, `/mcp`, tests) stays intact; new files or settings the template added just appear. The only thing you ever resolve by hand is when you **and** the template edited the *same lines* — those spots show up marked with `<<<<<<<` for you to fix. (The [fleet migration bot](https://github.com/turingplanet/agent-registry) runs this for you across all registered members whenever a new template ships — it opens the PR and never auto-merges.)

## What's in the template (the `template/` subdirectory)
- `api/`, `mcp/`, `tests/` — a runnable placeholder skeleton
- `agent.manifest.yaml` — concrete python-mcp manifest
- `manifest.schema.json` — the contract
- `pyproject.toml` — templated with your project name
- `.github/workflows/review.yml` — thin pointer to `policies@vN`
- `.copier-answers.yml` — provenance (the template version), written automatically

The repo **root** holds the Copier config (`copier.yml`) and this README; only the **`template/`** subdirectory is rendered into your new repo.
