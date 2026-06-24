# agent-template

The **scaffold** for 图灵星球 Agent 军团 member repos (Platform-owned, the COPY source). Holds only stable, declarative things: the manifest schema and a thin workflow pointer. Copied once into a new member repo at creation, then it **detaches** — updating this template does *not* update existing repos. Versioned by tag (`v1`, `v2`, …).

> **Part of 图灵星球 Agent 军团.** For the full picture — the three repos and how change flows between them — start at the overview: **https://github.com/turingplanet/agent-legion**

## What's here
- `manifest.schema.json` — the contract a member's `agent.manifest.yaml` must satisfy.
- `agent.manifest.yaml` — the starter manifest (placeholders to fill in).
- `.github/workflows/review.yml` — the thin pointer to the central review flow in `policies@vN`.

## Greenfield onboarding
1. Click **"Use this template" → Create a new repository** — this gives you a detached copy you own. It is **not** a fork.
2. In your new repo, fill `/api` + `/mcp` and the manifest values.
3. Open a pull request **inside your own repo** (feature branch → your `main`). That PR triggers the central review flow referenced from `policies@vN`, and the deterministic gate decides the merge.

You never fork this repo or `policies` — you take a one-time copy of this template, and your workflow *references* `policies` by version. See the overview for the full picture.
