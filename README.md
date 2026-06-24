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
Copying from template version v0.0.4
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

**4. Make it yours, then open a PR.** It's green out of the box, so you can confirm the pipeline works *before* changing anything. Then replace the placeholder `run()` in `/api`, expose it in `/mcp`, add real tests — and open a pull request. The review flow runs and the gate decides.

Later, run **`copier update`** in your repo to pull template improvements as a PR (your `.copier-answers.yml` is what makes that possible).

## Pull future template changes (in a generated repo)

```bash
copier update    # 3-way merge; your code is preserved, conflicts appear as git-style markers
```

## What's in the template (the `template/` subdirectory)
- `api/`, `mcp/`, `tests/` — a runnable placeholder skeleton
- `agent.manifest.yaml` — concrete python-mcp manifest
- `manifest.schema.json` — the contract
- `pyproject.toml` — templated with your project name
- `.github/workflows/review.yml` — thin pointer to `policies@vN`
- `.copier-answers.yml` — provenance (the template version), written automatically

The repo **root** holds the Copier config (`copier.yml`) and this README; only the **`template/`** subdirectory is rendered into your new repo.
