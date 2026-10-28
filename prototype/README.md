# SetuTrace application

Start from the [repository README](../README.md) for installation and the [three-minute submission demo](../submission/DEMO.md).

Run commands from the **repository root** so npm uses its single workspace lockfile:

```sh
npm ci
npm run build
npm start
npm run check
```

Node 24.x is required. The API defaults to http://127.0.0.1:4871; development UI uses port 5178. The root `.env` is optional. `DATA_DIR` resolves from this workspace directory and defaults to `prototype/data/`. Local mode refuses non-loopback binding. Explicit hosted mode requires an access code, exact hosts/origins and a persistent data directory; see [deployment](../docs/DEPLOYMENT.md). `DEMO_MODE=false` refuses startup until a real identity adapter exists.

| Location | Responsibility |
|---|---|
| `src/` | Responsive React interface, persona walkthrough and report views |
| `shared/contracts.ts` | Shared student/import types |
| `server/app.ts` | Role-scoped workflows, transactions, corrections, snapshots and disclosure |
| `server/database.ts` | Schema version, constraints and evidence guards |
| `server/http.ts` | Headers, origin/host restrictions, request limits and structured errors |
| `server/imports.ts` | Bounded CSV parsing, preview and spreadsheet-safe reports |
| `server/signing.ts` | Synthetic Ed25519 issuer, key persistence and signatures |
| `server/audit.ts` | Tenant-scoped retained event-chain verification |
| `server/config.ts`, `server/index.ts` | Local configuration, static bundle and lifecycle |
| `tests/` | Twenty-three HTTP/database and proxy behavioral tests |
| `public/samples/` | Fictional input CSV |
| `docs/` | Architecture, presenter notes, validation and screenshots |

The app does not make government API requests. Fonts and icons are bundled. Source revisions and audit rows are guarded at the database layer, except the explicit operator demo reset. A machine administrator can still alter local storage. Private keys, sessions and database files must remain untracked.

[Architecture](docs/ARCHITECTURE.md) · [API](../docs/API.md) · [Tests](../docs/TESTING.md) · [Security](../SECURITY.md)
