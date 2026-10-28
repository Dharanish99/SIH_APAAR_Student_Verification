# Contributing to SetuTrace

Read [AGENTS.md](AGENTS.md), [TEAM.md](TEAM.md) and the relevant research workstream. Preserve original member contributions and label AI-assisted additions.

Use Node 24.x, then run `npm ci` from the repository root. `npm run dev` starts the local API and Vite UI. Before publishing, run:

```sh
npm run check
npm run format:check
python tools/validate_research.py
```

Use `npm run format` for application source formatting. The Python validator uses the standard library and checks research packaging, not application behavior. Check the affected browser journey when changing the interface.

The current submission consolidation is published directly to **main** at the owner's request. Do not create Codex-named branches. Preserve history, use descriptive commits, and never force-push or fabricate co-authorship. Future review arrangements belong to the human team.

Use fictional data only. Do not commit `.env`, databases, sessions, signing keys, dependency folders or local build output. Do not change the preserved originals in the provenance manifest. Source corrections belong in labelled supplements with dates and reasons. Keep findings, assumptions, proposals and unknowns separate; no invented policy clauses, API access, interviews, measured impact or human approvals.
