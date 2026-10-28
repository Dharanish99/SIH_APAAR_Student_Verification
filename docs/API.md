# Internal prototype API

Version 0.3.0. These are SetuTrace's local application routes, **not government API endpoints**. API responses use `Cache-Control: no-store` and `X-Request-ID`. JSON errors have `{error, code, requestId}`. No CORS access is granted to external websites.

## Session and transport contract

The local persona endpoint returns `{session}` and an HttpOnly, SameSite=Strict `setutrace_demo` cookie. Use the cookie for subsequent requests and `session.csrf` as `x-csrf-token` on mutations. The cookie is a selectable synthetic identity, not production authentication. Session tokens are stored only as SHA-256 hashes with a one-hour expiry; the database survives restart. New sessions are capped at 256 active entries.

Default request limits per IP/minute: API 1000, session creation 100, verification 60. JSON is limited to 600 KB. CSV is limited to 512,000 UTF-8 bytes and 200 rows. Limits are in-process. Local mode accepts loopback hosts and local origins; hosted mode requires explicitly configured hosts and HTTPS origins. Hosted rate limits can aggregate traffic behind platform proxies. `DEMO_MODE=false` refuses startup because real authentication is not configured.

## Routes

| Method / path (under `/api`) | Role | Contract / resulting behavior |
|---|---|---|
| GET `/health` | Public/local | Version, database type, schema version and synthetic mode; no student data |
| GET `/capabilities` | Public/local | Upload/session limits and explicit simulated boundaries |
| POST `/demo/session` | Public/local | `{role, tenant, recipient?, accessCode?}`; hosted first session requires the private judge code; creates synthetic session; roles operator/approver/student/verifier/regulator; tenants aster/river; recipients Northstar Skills/Meridian Careers |
| GET `/session` | Session | Current session metadata and mutation token |
| POST `/session/logout` | Session | Deletes the current token hash and clears cookie |
| GET `/state` | Session | Role-filtered current workspace; students receive only their record; verifier receives permission metadata without assertion/claims; regulator receives aggregates |
| GET `/records/:id/revisions` | Operator/approver/own student | Same-tenant revision history; internal record IDs are tenant-qualified |
| POST `/imports/preview` | Operator | `{csv}` → staged preview with fingerprint and line outcomes; no canonical source mutation |
| POST `/imports/:id/commit` | Operator | Commits one preview atomically; checks all source versions; a matching committed batch returns its original receipt |
| POST `/cases` | Student | `{programme, reason, expectedVersion}` for the student's programme; one open case per source record |
| POST `/cases/:id/reopen` | Own student | Supersedes a stale open request with a linked request against the current source revision |
| POST `/cases/:id/resolve` | Operator | `{decision, reason}`; the original case retains its expected source version; accept/decline a case, preserve reason and source history |
| POST `/records/:id/provider-fixture` | Operator | `{response, expectedVersion}`; responses linked/unavailable/denied/not_linked; changes evidence and supersedes approval |
| POST `/snapshots` | Approver | `{note, reviewDigest}` → approval ID; rejects a changed reviewed source set or cases, freezes exact rows, findings, digest and fictional rule pack |
| GET `/snapshots/:id/export` | Operator/approver | Same-tenant frozen JSON, explicitly local/synthetic, including current snapshot status |
| GET `/snapshots/:id/report.csv` | Operator/approver | Minimal frozen CSV: student ID, name, programme, status, source revision, snapshot status; no APAAR; formula prefixes neutralised |
| POST `/grants` | Student | `{fields, purpose}`; allowed fields name/programme/status; current frozen source required; fifteen-minute grant for the session's recipient |
| POST `/grants/:id/revoke` | Own student | Idempotent withdrawal; repeated withdrawal creates no repeated audit event |
| POST `/verify` | Verifier | `{id, assertion?}`; checks recipient, live status/expiry, source revision, snapshot, signature and signed bindings before returning minimal claims |
| GET `/reports/summary` | Operator/approver | Same-tenant current counts, programme arithmetic, open cases and audit inspection |
| GET `/audit/verify` | Operator/approver | Recomputes tenant chain; 200 consistent / 409 inconsistent; not protection from privileged complete-chain rewriting |
| POST `/demo/reset` | Operator | Restores all fictional tenant fixtures and clears demo evidence; intentionally resets the local presentation dataset |

The JSON export is a staff evidence manifest containing fictional identifiers. The minimal CSV is distinct from the verifier's permitted claim set. A superseded export remains downloadable as an explicitly labelled historical artifact; it cannot authorise current verification.

## CSV input

Exactly these six unique headers, in any order:

```csv
student_id,name,programme,apaar,status,expected_version
AIT-26-001,Aarav Menon,CSE,910000000001,Active,1
```

Use existing version for updates and 0 for a new row. Programmes are CSE/ECE; status is Active/Withdrawn. Quoted names, BOM and CRLF are accepted. Duplicate IDs, duplicate/unknown/missing headers, malformed values and oversized input are rejected. Missing or malformed academic identifiers remain source findings; they are not proof of identity or a rejected admission.

## Failure behavior

- 400: malformed JSON/CSV, schema violation or unsupported field.
- 401: absent/expired/logged-out session.
- 403: role, mutation token or host/origin denial.
- 404: unavailable resource, wrong tenant/recipient resource or unknown authenticated API route.
- 409: stale version, repeated workflow transition, source/snapshot mismatch, evidence inconsistency or database state conflict.
- 410: withdrawn or expired disclosure permission.
- 413: request/CSV byte bound exceeded.
- 429: request/session bound reached; timed request limits return Retry-After.
- 500: redacted unexpected error with correlation ID; no raw stack or query returned.

See executable tests for exact examples. Signature integrity does not establish academic truth; real issuer/recipient onboarding and lawful authority remain pilot dependencies.
