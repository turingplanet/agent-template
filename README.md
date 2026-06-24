# agent-template

The **scaffold** for 图灵星球 Agent 军团 member repos (Platform-owned, the COPY source). Holds only stable, declarative things: the manifest schema and a thin workflow pointer. Copied once into a new member repo at creation, then it **detaches** — updating this template does *not* update existing repos. Versioned by tag (`v1`, `v2`, …).

> **Part of 图灵星球 Agent 军团.** For the full picture — the three repos and how change flows between them — start at the overview: **https://github.com/turingplanet/agent-legion**

## What's here
- `manifest.schema.json` — the contract a member's `agent.manifest.yaml` must satisfy.
- `agent.manifest.yaml` — the starter manifest (placeholders to fill in).
- `.github/workflows/review.yml` — the thin pointer to the central review flow in `policies@vN`.

## Greenfield onboarding
Copy this repo → fill `/api` + `/mcp` and the manifest values → open a PR. You're immediately on the standard rails, reviewed by the one standing agent.
