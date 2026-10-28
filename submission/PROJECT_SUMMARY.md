# SetuTrace — explainable student records

**Working problem reference:** SIH26263, based on the supplied brief.
**Human team lead:** Kanishkar B.
**Stage:** Locally tested synthetic web prototype, 28 October 2026.

## Problem and users

Institution exports can contain stale or conflicting enrolment information. A linked academic identity establishes a different fact from programme correctness, approval scope or admission legality. Students need a way to challenge an error; institutions need reproducible reporting; authorised verifiers need a current, limited answer.

## Proposed solution

SetuTrace adds an evidence and correction layer beside existing institution systems. An operator previews an ERP CSV and commits version-checked changes. Explainable findings retain uncertainty rather than rejecting a student. A student can open a source correction case; an institution records its decision and reason while preserving both versions. A separate approver freezes rows, findings and rule context. A student then permits selected fields for a named recipient and purpose. Retrieval checks current permission, expiry, source revision, approved snapshot and signature.

The central innovation is **carrying the source correction through reporting and later verification**, while keeping identity linkage, institution claims, policy context and disclosure permission distinct.

## Demonstrated scenario

Meera is incorrectly exported as CSE instead of ECE. The initial CSE count is 7 against 6 fictional seats. A student case and reasoned institution correction produce revision 2 and a 6/6 CSE count. The old CSE revision remains inspectable. A local approval freezes that corrected state. A verifier receives only permitted name/programme fields; withdrawing permission prevents later retrieval. This behavior is implemented, not a slide-only scenario.

## Feasibility and technology

| Layer | Choice and reason |
|---|---|
| Interface | React, TypeScript, Vite and bundled Manrope/Lucide; clear role journeys with no runtime CDN dependency |
| API | Node 24, Express, Zod and csv-parse; one language, explicit contracts and bounded input |
| Durable state | SQLite/WAL with constraints, atomic transactions and evidence guards; runs on one laptop without infrastructure |
| Disclosure | Node crypto Ed25519; synthetic issuer, minimal claims and live status checks |
| Quality | Node test runner over actual HTTP/SQLite, TypeScript build, Prettier and CI |
| Pilot evolution | Institutional OIDC, PostgreSQL, controlled key custody, approved policy packs and authorised provider adapters |

The prototype excludes heavy infrastructure, opaque fraud scoring and an LLM admission decision-maker. A limited local workflow tests the product hypothesis before institutional integration costs.

## Validated key points

- Twenty-three HTTP/database and proxy tests pass locally, covering permission boundaries, atomicity, replay, stale edits, evidence guards, signature bindings, expiry/revocation, report scoping and persistent sessions.
- The browser demonstration exercises correction, approval, disclosure and denial after withdrawal.
- Counts reconcile to synthetic source rows; frozen JSON/CSV exports identify captured revisions.
- Research provenance retains original member contributions, cited sources and AI supplements separately.

These results establish prototype behavior. They do not establish real-world usefulness, policy correctness, production security, live APAAR access or national-scale performance. [Detailed validation](../docs/TESTING.md).

## Success criteria for a permitted pilot

Observe staff/student work with an approved synthetic or consented dataset. Measure source errors resolved, repeated upload work, time to a reasoned correction, report reproducibility and inappropriate disclosure denials against the current workflow. Set targets after baseline measurement; no invented time savings or accuracy percentage is reported here.

## Submission boundaries

All records, institutions, capacities, providers, sign-in personas and issuer identity are fictional. No official report submission or awarding-body certificate is implemented. Full category/seat rules and cross-institution matching remain research/design work. [Ten-requirement coverage](../docs/requirements.md) makes those gaps explicit.
