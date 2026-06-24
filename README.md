# agent-template — the starter kit (Copier template)

> **Part of 图灵星球 Agent 军团.** New here? Start at the overview: **https://github.com/turingplanet/agent-legion**

This is a **[Copier](https://copier.readthedocs.io) template** for creating a new agent. A Copier-scaffolded repo records which template version it came from (in `.copier-answers.yml`), so it can pull future template changes with **`copier update`**. That provenance is what lets the platform ship **safe, automated migration PRs** across the whole fleet.

## Create a new agent

```bash
pipx install copier   # one-time (or: pip install copier)
copier copy gh:turingplanet/agent-template ./my-agent
cd my-agent && git init && git add -A && git commit -m "Scaffold from agent-template"
```

You'll be asked a few questions (name, description, author). The result is a **runnable python-mcp skeleton** that passes review out of the box — then replace the placeholder code in `/api` + `/mcp` with your logic and open a PR.

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
