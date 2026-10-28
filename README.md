# SetuTrace

### Every record has a story. Make it explainable.

**SIH26263 · Student records, accountable corrections and controlled verification**
Submission prototype · React / TypeScript / Node 24 / SQLite · Synthetic data only

![SetuTrace institution dashboard](prototype/docs/screenshots/submission-overview.png)

**[Three-minute demo](submission/DEMO.md)** · **[Submission brief](submission/PROJECT_SUMMARY.md)** · **[Architecture](prototype/docs/ARCHITECTURE.md)** · **[Tests](docs/TESTING.md)** · **[Team](TEAM.md)** · **[Research report](docs/solution-report.md)** · **[Mind map](docs/mind-map.md)**

## The problem we chose to solve

A linked academic identity can still have a wrong enrolment record. Institutions need defensible counts, students need a correction route, and verifiers need a current answer with permission. Repeated uploads and unexplained mismatch flags do not resolve the underlying source error.

SetuTrace works beside an institution's existing ERP: **import → explain → correct → approve → share**. It connects each count and disclosure to a specific source revision, preserves the reason for a correction, and withholds claims when permission or source evidence is no longer current.

The scope follows the team's [supplied problem brief](docs/problem-brief.md). The [official statement verification gap](docs/official-problem-verification.md) remains documented; this repository does not claim government endorsement.

## Run the submission demo

Use **Node 24.x** and npm. No cloud account, Docker, Python or API key is needed to run the application. Dependencies are locked; after installation, the demo runs without external service requests.

```sh
git clone https://github.com/Dharanish99/SIH_APAAR_Student_Verification.git
cd SIH_APAAR_Student_Verification
npm ci
npm run build
npm start
```

Open **http://127.0.0.1:4871**. On Windows, `START_DEMO.cmd` installs missing dependencies, builds and starts the app. Stop with Ctrl+C. For development use `npm run dev` and open **http://127.0.0.1:5178**; stop another API process first.

Optional settings are in [.env.example](.env.example). Keep the server on loopback: sign-in is deliberately simulated for the judging walkthrough. A fresh checkout creates its own fictional database and signing key under `prototype/data/`, both ignored by Git.

## What the judge can actually do

| Journey | Working implementation |
|---|---|
| Import an ERP export | Parse quoted CSV, preview row changes, commit atomically, detect stale versions and replay without duplicate effects |
| Explain a finding | See capacity arithmetic, missing/invalid evidence and source disagreement; findings trigger review, never automatic rejection |
| Correct the source | Student opens a case; institution records its decision and reason; both source revisions remain |
| Approve a report | Separate approver freezes exact rows, versions, findings and digest; download JSON or minimal CSV |
| Share selected fields | Student grants name/programme/status for a named recipient and purpose for fifteen minutes |
| Verify current evidence | Server checks recipient, live permission, expiry, source revision, snapshot and Ed25519 signature before returning fields |
| Withdraw access | Revocation blocks subsequent retrieval; a source change supersedes approval and invalidates earlier verification |
| Inspect accountability | Tenant-scoped reports, retained audit-chain verification and an aggregate-only regulator persona |

**The demo story:** Meera appears in CSE even though her fictional admission letter says ECE. Her linked account fixture does not fix that error. A reasoned correction changes CSE from **7/6 to 6/6**, retains the old revision, and carries the corrected programme into an approved snapshot and a limited verifier assertion. The built-in **3-minute walkthrough** guides these actions.

## Backend engineered for a credible prototype

- Real Express HTTP API and persistent SQLite/WAL, with foreign keys, consistency checks and uniqueness constraints.
- Transactional import, correction, approval and verification decisions; expected versions and canonical replay receipts.
- Database guards against application updates to source history, audit events and frozen evidence.
- Durable, expiring demo sessions stored as token hashes; role/tenant checks, mutation tokens, local origin/host checks and request limits.
- Bounded CSV/JSON input, structured errors with request IDs, security headers and spreadsheet-safe minimal CSV exports.
- Local Ed25519 signing with issuer, audience, purpose, revision, snapshot and field-binding checks.

See [API contracts](docs/API.md), [architecture and trade-offs](prototype/docs/ARCHITECTURE.md), and [security boundaries](SECURITY.md). These controls demonstrate behavior; they are not a production security certification.

## Validation

```sh
npm run check          # TypeScript, production build, 19 HTTP/database tests
npm run format:check   # Application source formatting
python tools/validate_research.py  # Optional: research links, ledgers and original-file hashes
```

**Locally passed:** 19 tests against real HTTP endpoints and SQLite, plus the browser walkthrough described in [TESTING.md](docs/TESTING.md). The [CI workflow](.github/workflows/ci.yml) repeats build, test, formatting and research integrity checks on pushes and pull requests. CI results are separate from local results.

## Built from six complementary workstreams

| Team member | Research ownership | Influence on the solution |
|---|---|---|
| **Gopika** | Institutional workflows and user needs | ERP-first imports, clear next actions and a student correction desk |
| **Sudhan** | APAAR / ABC / DigiLocker / NAD integration | CSV-first delivery and explicit provider evidence boundaries |
| **Pranav** | Admission policy and compliance reasoning | Scoped fictional rules, disclosed unknowns and no automatic sanction |
| **Dharanish R P** | Data architecture and validation | Versioned records, transactional imports and prototype consolidation |
| **Sudhir** | Privacy, security and credential lifecycle | Minimal recipient-bound sharing, revocation and separate trust checks |
| **Kanishkar B — team lead** | Synthesis, feasibility and evaluation | A focused, explainable end-to-end MVP and pilot criteria |

[TEAM.md](TEAM.md) links original contributions and explains AI-assisted research completion and implementation. Existing member commits and original source snapshots are retained, without attributing unrecorded coding or approvals to teammates.

## Repository guide

```text
prototype/          Runnable web app, backend, sample CSV and API tests
submission/         Concise project brief and timed judging script
research/           Six workstreams, cited sources and preserved originals
docs/               Requirements, API, tests, solution report and mind map
output/             Rendered research report and visual deliverables
tools/              Research integrity and artifact generation scripts
.github/            Continuous integration and contribution templates
```

## What remains for an authorised pilot

Personas, institutions, records, capacities, provider responses and issuer identity are fictional. There is **no live government integration, official report submission, official certificate issuance, institutional authentication, full legal rule engine or field-impact study**. Revocation stops future retrieval; it cannot recall downloaded copies. Local audit chaining cannot defeat an administrator rewriting the entire database.

A pilot needs approved policy/purpose/retention scope, real institutional OIDC and vetted recipients, PostgreSQL and managed keys, authorised provider access, backup/recovery exercises, independent security review and user testing. See [requirement coverage](docs/requirements.md) and [risks](docs/risks.md). National-scale performance, fraud accuracy, legal compliance and time savings are not claimed.
