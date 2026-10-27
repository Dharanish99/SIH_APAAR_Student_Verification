# Data architecture and validation — consolidated research

Owner: Dharanish R P. AI consolidation: lead research agent, 2026-10-26.
Original Notion work: [notebook](../provenance/notion/dharanish-notebook.md), [architecture](../provenance/notion/dharanish-architecture.md), [imports](../provenance/notion/dharanish-imports.md), [sources](../provenance/notion/dharanish-sources.md), [feasibility](../provenance/notion/dharanish-feasibility.md). These are preserved sources, not proof of human acceptance.

## Retained and completed
Retain institution-local student, identity claim, restricted person link, enrolment, revision, approval and credential as separate entities. APAAR is the academic linkage attribute; an internal UUID is the technical key so missing/corrected identifiers do not destroy admission history. No automatic person merge from an unverified repeated ID or fuzzy name.

Retain staged mapping, scoped business keys, idempotency, expected-version corrections, atomic audit/outbox and separate provider status. Complete the evidence with downloaded originals and an independently executed reproduction.

New integration evidence changes the design: DigiLocker requester v2.4 describes token-linked APAAR details, not bulk arbitrary-ID checks. Institution-reported values and consented account evidence remain distinct. [Sudhan supplement](../sudhan/findings.md). Policy findings never automatically sanction admission.

## Proposed entities and invariants
| Entity | Key fields | Invariant |
|---|---|---|
| institution/source_system | UUID, authority codes, administrators | Scope from trusted authentication |
| institution_student | institution + local key | Keys can repeat across institutions |
| identity_claim | encrypted reported value, source, evidence/time | Format is not identity |
| person_link | restricted evidence-bound subject link | Requires authorised resolution policy |
| programme_offering | institution/campus/programme/level/mode/cohort | Capacity must have full scope |
| approval_version | issuer/source reference/effective dates/seat bucket | Missing applicability => UNKNOWN |
| enrolment/revision | scoped source key, version, effective/recorded times | Current state and history differ |
| import_job/row | token, body+mapping fingerprint, row outcome | Repeat cannot duplicate effects |
| rule_version/finding | rule/data version, reason, scope, evidence | Revalidation supersedes, not rewrites |
| correction_case | disputed claim, owner, reason, resolution | Student disputes; authorised owner resolves |
| submission_snapshot | approved row versions, mapping/hash, acknowledgement | Partial import is not final submission |
| verification_receipt | issuer, audience/purpose, subject, version, expiry/status | A local receipt is not a degree/government seal |
| audit/outbox | actor/action/version/event ID | Atomic recording and duplicate-tolerant consumers |

These are proposed schemas. PostgreSQL [constraints](https://www.postgresql.org/docs/18/ddl-constraints.html) (DHA-101), [isolation](https://www.postgresql.org/docs/18/transaction-iso.html) (DHA-102) and AWS [outbox](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html) (DHA-104) support mechanisms, not domain policy.

## Import and correction protocol
1. Authenticate operator and institution. Stage original input and versioned mapping.
2. Bound file/row sizes, preserve string identifiers/leading zeros and parse strictly. CSV first; XLSX needs expansion/macro and parser controls.
3. Same institution/token/fingerprint returns the original job. Changed content under old token conflicts. New token/unchanged business values adds no canonical revision.
4. Preview differences. Require expected version for corrections; a stale file cannot silently undo withdrawal.
5. Commit bounded chunks with revisions, audit/outbox and row state atomically. Show partial completion; approver freezes an explicit snapshot.
6. Durable worker leases, bounded retries and idempotent event consumers. Never hold a DB transaction open during provider calls.
7. Revalidate on changed data/rules. Preserve old findings and invalidate/supersede related receipts.
8. Display source-effective, provider-check and projection times separately.

Tenant controls apply to API, jobs, files and exports. Use non-owner app roles without BYPASSRLS and trusted transaction-local scope; verify real negative cases later. PostgreSQL [RLS](https://www.postgresql.org/docs/18/ddl-rowsecurity.html) (DHA-103) is additional defence.

Capacity is a reporting check, not a race to reject the last student. Preserve every submitted admission; compare the scoped approved snapshot and raise a review finding. Use locks/serializable retries where concurrent changes could invalidate a final calculation.

## Executed original experiment reproduction
Run from repository root:
```powershell
node research/dharanish/experiments/reproduce.cjs
```
All eight comparisons of original metrics/checks/fixtures matched on Node v24.19.0, Windows. Source inspected before execution. [Results](experiments/reproduction-results.json).

| Method | TP | FP | FN | TN | Precision | Recall |
|---|---:|---:|---:|---:|---:|---:|
| Rules | 80 | 0 | 20 | 900 | 100% | 80% |
| Modified Z-score | 10 | 10 | 90 | 890 | 50% | 10% |
| Combined | 90 | 10 | 10 | 890 | 90% | 90% |

All 1,000 rows are fictional; seed26263, separate 300-observation reference seed26264. Additional statistics add twenty alerts: ten labelled cases and ten legitimate counterexamples. Incremental precision is 50%, not evidence of a real fraud detector. Ten duplicate pairs produce twenty flagged rows, not twenty duplicate students.

Twelve sequential model checks reproduced, including replay, ten corrections => 1,000 entities/1,010 revisions, interruption recovery and unavailable-provider stub. Zero-MAD check establishes zero dispersion; score function inspection confirms abstention. Sequential optimistic editing is not database concurrency. The coarse 4ms metric-evaluation observation excludes generation, parsing, storage and network.

Proposal: rules first, statistical triage only if representative evaluation justifies review effort. NIST's [outlier discussion](https://itl.nist.gov/div898/handbook/eda/section3/eda35h.htm) (DHA-105) motivates investigation, not adjudication. No LLM decides validity.

## Missing implementation evidence
Actual database races, rollback, worker termination, RLS, parser attacks, export handling and backup restoration remain untested. For future anomaly evaluation, hold out institutions/time periods; measure incremental useful findings per review-hour and false-alert slices. Do not claim production security or national throughput.

## Workload and costs
Prior [sizing assumptions](../provenance/notion/dharanish-feasibility.md): demo target10,000 records/20 concurrent users, 10MB and10,000-row upload caps, whichever binds first. Executed fixture:1,000 only. One million records ×2KB ×3 revisions =6GB; add1GB ancillary payload and assumed2× overhead =>14GB, before current rows/WAL/backups/replicas.

Rechecked 2026-10-26: [Lightsail](https://aws.amazon.com/lightsail/pricing/) Linux public-IPv4 2GB VM USD12/month; encrypted standard2GB database USD30/month (USD15 entry lacks data encryption). [Supabase Pro](https://supabase.com/pricing) starts USD25/month. Illustrative subtotals: USD12 self-managed demo; USD37 VM+Supabase; USD42 VM+encrypted Lightsail database. Not full-stack/pilot quotations. Taxes, region transfer allowances, object storage, logs, backup, messaging, API access, support and staff effort remain extra/unknown. No resources purchased.

## Handoff
Gopika supplies workflow validation; Pranav current rule packs/EoA; Sudhan authorised linking; Sudhir disclosure/retention; Kanishkar human acceptance. Desk research and model reproduction are complete to the stated scope. A deployed service is not certified.
