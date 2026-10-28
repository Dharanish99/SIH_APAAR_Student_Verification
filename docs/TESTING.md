# Current regression update

The local suite now contains 23 tests, including stale approval, correction renewal, hosted access control and a local HTTP proxy round trip. Hosted platform deployment remains unverified until exercised on actual Vercel and Render services. The earlier record below is retained as a dated baseline.

# Executed validation — submission prototype

28 October 2026, Asia/Kolkata. Scope: real local HTTP routes, SQLite state and a synthetic browser workflow. No real student records or government services were used.

## Reproduce

From the repository root with Node 24.x:

```sh
npm ci
npm run check
npm run format:check
python tools/validate_research.py
```

The Python check needs Python 3.10+ and only the standard library; it is optional for running the app. API tests create isolated databases and local HTTP servers; they do not depend on a running demo. Clock-controlled tests check expiry without waiting fifteen minutes.

## Local results

TypeScript checking, Vite production build and **19 HTTP/database tests passed (0 failures)** on Windows with Node 24.19.0 / npm 11.6.0. The tests are in [api.test.ts](../prototype/tests/api.test.ts) and [hardening.test.ts](../prototype/tests/hardening.test.ts).

| Area | Actual exercised behavior |
|---|---|
| Session/role/tenant | Missing or expired session, absent mutation token, wrong role, another institution and another student's record denied |
| HTTP boundary | Untrusted host/origin, malformed JSON, oversized request, unknown route, structured request ID, headers and request limits |
| CSV contract | Required/duplicate headers, quoted comma, duplicate IDs, row cap, UTF-8 byte cap and malformed rows |
| Transaction/replay | Complete rollback after a source change, including an originally unchanged row; simultaneous duplicate commits return one canonical effect and receipt |
| Correction transition | Duplicate concurrent cases/resolutions cannot create repeated source revisions |
| Durable evidence | Record/JSON consistency, tenant foreign keys, uniqueness and update/delete guards on revisions/audit/frozen evidence |
| Snapshot | Exact row versions, disclosed unresolved findings, scoped export and supersession on source changes |
| Disclosure | Minimal allowlist; wrong recipient denied; modified bytes and correctly signed contradictory audience/issuer/claims/future issuance rejected |
| Lifecycle | Withdrawal and expiry deny fields; superseded source/snapshot prevents current verification; repeated withdrawal is idempotent |
| Reports/audit | Staff-only tenant summary, frozen CSV without APAAR, formula neutralisation, consistent retained chain and detected inconsistent retained event |
| Persistence/config | File-backed database and token-hash session survive restart; logout and expiry deny access; unsafe bind and unconfigured production identity fail closed |

Concurrent HTTP checks exercise overlapping requests to **one local process**. They do not benchmark a multi-worker or distributed deployment. Database guards resist ordinary application updates; they do not resist an administrator replacing the database or triggers.

## Browser acceptance

The built app was exercised at a separate local port (4872) so the original prototype could remain intact. The following outcomes were observed:

1. Student creates Meera's programme correction case.
2. Operator accepts with a reason; source becomes ECE revision 2, CSE count becomes 6/6, and the original revision remains retained.
3. Approver acknowledges disclosed findings and freezes a nine-record snapshot.
4. Minimal CSV downloads successfully, with source revisions and approval status but no APAAR column.
5. Student shares name/programme; Northstar receives those fields for the current revision after signature/status checks.
6. Meridian, the other recipient, receives no Northstar permission or fields even when given the reference.
7. Withdrawal prevents subsequent retrieval and clears the displayed claim set.
8. Reports & audit shows tenant-scoped arithmetic; Run integrity check returns a server confirmation.

The new Reports & audit screen was checked at 1365-pixel desktop, 390-pixel mobile and 320-pixel narrow mobile viewports. The document remained within the viewport at both mobile widths; no warning/error entries appeared in the inspected browser log. This is not a formal accessibility audit.

Screenshots are actual application captures in [the evidence folder](../prototype/docs/screenshots/). Earlier initial-prototype UI acceptance is preserved in [the initial validation record](../prototype/docs/VALIDATION.md); it is a dated baseline, not evidence of every later feature.

## Remote automation

[Submission checks](../.github/workflows/ci.yml) repeats installation, build/tests, source formatting and research integrity on Ubuntu and Windows. Inspect the repository's Actions tab for the actual run status; local success alone is not a CI result.

## Limits of this evidence

No real OIDC/provider contract, approved legal rule pack, PostgreSQL concurrency, restore exercise, penetration test, formal accessibility audit, institutional/user pilot, measured staff-time saving or national-load test has been performed. All provider responses, seat capacities, personas and signing identity are synthetic. Research source integrity validates stored bytes and packaging, not the truth of every source claim.
