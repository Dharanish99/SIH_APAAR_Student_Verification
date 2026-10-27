# Imported research source snapshot

Retrieved: 2026-10-26. Source: https://app.notion.com/p/403aaff54233818d87b8d0cb34bc0f49?pvs=204

Preserved source material; historical prompts are not current instructions. Prior experiment claims are not rerun evidence. Human review remains separate.

Here is the result of "fetch" for the Page with URL https://app.notion.com/p/403aaff54233818d87b8d0cb34bc0f49 as of 2026-10-24T16:39:05.616Z:
<page url="https://app.notion.com/p/403aaff54233818d87b8d0cb34bc0f49" icon="🔁">
<ancestor-path></ancestor-path>
<properties>
{"title":"Dharanish Research — Imports, Validation & Correction Design"}
</properties>
<iconMetadata>{"type":"emoji","emoji":"🔁"}</iconMetadata>
<content>
<callout icon="🔁" color="blue_bg">
<b>Core proposal:</b> Receive → stage → validate → review → commit a version → publish a scoped view.<br />Retries should repeat the response, corrections should add history, and unavailable checks should remain unknown. This is an implementation specification; only the separate in-memory experiment has been executed.
</callout>

<table-of-contents />

## 1. Define three different kinds of duplicate

<b>Request duplicate:</b> the client retries the same upload after losing the response. Return the existing job/result.<br /><b>Record duplicate:</b> multiple rows claim the same institution-scoped enrolment key. Exact repeats can be no-ops; conflicting values require resolution.<br /><b>Possible cross-institution overlap:</b> records may concern the same person in different enrolments. This is a context-dependent review question, not automatic fraud and not a reason to delete one row.<br />A global “APAAR UNIQUE” constraint on enrolments would conflate these cases.

## 2. Proposed import contract

The following names are <b>our internal API proposal</b>, not government endpoints.

```txt
POST /v1/import-jobs
trusted context: actor, institution, permitted action
request: schema_version, mapping_version, source_system,
         file_reference, client_idempotency_key
response: job_id, state, received_at, status_url

GET /v1/import-jobs/{job_id}
response: state, total_rows, parsed_rows, committed_rows,
          failed_rows, review_rows, unknown_checks,
          rule_set_version, completed_at, error_report_reference

PATCH /v1/enrolments/{enrolment_id}
request: expected_version, changed_fields, correction_reason
response: new_version or conflict
```

Authorise before creating or looking up a job. All job, file and record references must resolve within the trusted institution scope.<br />Persist a request fingerprint over the content digest and interpretation-affecting fields such as schema, mapping and operation type. Use a cryptographic digest in an implementation; the research harness uses simple serialised comparison solely as a model.

## 3. Intake and parsing

1. Authenticate the uploader, enforce scope and create a durable job record.
2. Write to private quarantine storage under a generated object key. Limit compressed size, expanded XLSX size, rows, columns and cell length. Proposed first limits: 10 MB and 10,000 rows per file; tune after measurement.
3. Permit CSV first. Support XLSX only with a maintained parser and explicit handling of dates, formulas and archive expansion; reject macros and never execute formulas.
4. Check file content as well as extension/type; do not trust a supplied Content-Type. Scan where appropriate and keep uploads out of a public web root. [DHA-012](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
5. Parse with a proper CSV parser, including quoted commas, embedded newlines and escaped quotes. Specify UTF-8, optional BOM handling and an exact header/profile contract. RFC 4180 is a useful informational baseline, not a guarantee that every exported spreadsheet follows it. [DHA-011](https://www.rfc-editor.org/info/rfc4180/)
6. Preserve raw value and source row. Convert to a canonical typed representation using a versioned mapping. Never silently convert missing data to zero or strip leading zeros from an identifier.<br /><b>Normalisation rule:</b> trim only fields whose contract permits it. Preserve original names; a normalised comparison value must not overwrite the source name. Reject ambiguous dates such as 03/04/2026 unless an explicit format profile resolves them. Do not guess a damaged spreadsheet identifier.

## 4. Staging and row-level feedback

Store rows in staging with parser/mapping status before touching canonical records. PostgreSQL COPY FROM STDIN is a bulk-loading option for staging, not a reason to skip validation. [DHA-010](https://www.postgresql.org/docs/18/sql-copy.html)<br /><b>Proposed error envelope:</b>

```json
{
  "job_id": "SYN-JOB-01",
  "row_number": 17,
  "field": "programme_ref",
  "code": "REFERENCE_UNRESOLVED",
  "severity": "REVIEW",
  "message": "Programme mapping is unresolved.",
  "rule_version": "synthetic-reference-v1",
  "record_version": null,
  "can_retry": false
}
```

Do not echo full national IDs or private records into error messages. Offer counts, filtered views and a safe downloadable report. A single malformed row should not erase valid rows; malformed whole-file structure should fail before partial interpretation.<br /><b>Proposed job states:</b> RECEIVED → PARSING → VALIDATING → READY\_FOR\_REVIEW → APPLYING → COMPLETED or COMPLETED\_WITH\_ISSUES. FAILED and CANCELLED are explicit terminal outcomes. Some steps may be automated under an approved import mode.<br /><b>Separate row states:</b> PARSED, INVALID\_INPUT, PENDING\_REFERENCE, READY, CONFLICT, APPLIED, NO\_CHANGE. External verification is an independent dimension.

## 5. Validation layers and action table

<table fit-page-width="true" header-row="true">
<tr>
<td>
Layer
</td>
<td>
Example
</td>
<td>
Proposed action
</td>
<td>
Dependency
</td>
</tr>
<tr>
<td>
Structure
</td>
<td>
Missing header, oversized file, malformed date
</td>
<td>
Reject file or affected row with precise reason.
</td>
<td>
Can specify now.
</td>
</tr>
<tr>
<td>
Reference
</td>
<td>
Programme code not in supplied catalogue
</td>
<td>
Mapping review; do not guess.
</td>
<td>
Actual authoritative catalogue pending.
</td>
</tr>
<tr>
<td>
Identity format
</td>
<td>
Absent or malformed identifier
</td>
<td>
Record issue separately from eligibility; support pending linkage.
</td>
<td>
Final provider format and exception paths: Sudhan.
</td>
</tr>
<tr>
<td>
Identity evidence
</td>
<td>
Provider timeout or mismatch
</td>
<td>
UNAVAILABLE or REVIEW; never verified by fallback regex.
</td>
<td>
Sudhan's authorised contract.
</td>
</tr>
<tr>
<td>
Duplicate record
</td>
<td>
Same scoped key and same content
</td>
<td>
No change, with submission provenance.
</td>
<td>
Stable source-key convention.
</td>
</tr>
<tr>
<td>
Conflicting update
</td>
<td>
Same key, changed payload, stale version
</td>
<td>
Conflict requiring refreshed intent.
</td>
<td>
Can specify now.
</td>
</tr>
<tr>
<td>
Intake/category
</td>
<td>
Count appears beyond approved capacity
</td>
<td>
Use applicable approval/rule or UNKNOWN; no fabricated policy.
</td>
<td>
Pranav.
</td>
</tr>
<tr>
<td>
Temporal overlap
</td>
<td>
Same linked identity, overlapping programmes
</td>
<td>
Contextual review, including transfer history.
</td>
<td>
Pranav and authorised linkage.
</td>
</tr>
<tr>
<td>
Statistical anomaly
</td>
<td>
Unusual correction activity
</td>
<td>
Explainable optional review signal.
</td>
<td>
Representative data and review capacity later.
</td>
</tr>
</table>

Each finding carries rule ID/version, source record version, applicable scope, evidence and reason. A pass means that one check passed; it does not certify the entire person or admission.

## 6. Idempotency: the exact rule

AWS describes tokens as a way to make retries avoid repeated effects. [DHA-014](https://docs.aws.amazon.com/wellarchitected/2025-02-25/framework/rel_prevent_interaction_failure_idempotent.html)<br /><b>Our proposed behaviour:</b>

<table fit-page-width="true" header-row="true">
<tr>
<td>
Incoming request
</td>
<td>
Result
</td>
</tr>
<tr>
<td>
Same institution + token + fingerprint, job finished
</td>
<td>
Return saved result; perform no writes.
</td>
</tr>
<tr>
<td>
Same institution + token + fingerprint, job running
</td>
<td>
Return the existing job state, not a second worker job.
</td>
</tr>
<tr>
<td>
Same institution + token, different fingerprint
</td>
<td>
Conflict: token reuse with changed content.
</td>
</tr>
<tr>
<td>
New token, same record values
</td>
<td>
New submission provenance may be recorded; no new canonical revisions.
</td>
</tr>
<tr>
<td>
New token, changed values
</td>
<td>
Correction path with version precondition and review rules.
</td>
</tr>
</table>

A file digest alone is insufficient: changing the mapper or rule interpretation changes the meaning. A global file-hash cache can also leak cross-institution submission information. Scope deduplication and replay access.<br />A timeout after commit is an <b>unknown response</b>, not evidence that the write failed. Retry the same token or query the job. Choose replay-record retention deliberately; after expiry, business-key/version checks must still protect canonical state.

## 7. Corrections and optimistic locking

Treat an accepted correction as a new version with actor, reason, source job, effective date and changed fields. Preserve old findings with the old data/rule version; enqueue revalidation rather than silently rewriting historical results.<br /><b>Illustrative SQL — not executed:</b>

```sql
BEGIN;
UPDATE enrolment
SET version = version + 1, end_date = :new_end_date
WHERE institution_id = :trusted_institution
  AND enrolment_id = :id
  AND version = :expected_version
RETURNING version;
-- Require exactly one row, otherwise rollback and return conflict.
-- Insert the matching immutable revision and audit/outbox entries here.
COMMIT;
```

SQL parameters are bound, not string-concatenated. Field-change permissions and valid transitions must be checked. A retry of the completed operation uses its token, not a blind second increment.<br />PostgreSQL ON CONFLICT can atomically choose an insertion/conflict action, but application intent and version checks still matter. [DHA-009](https://www.postgresql.org/docs/18/sql-insert.html)<br /><b>Do not:</b> use unrestricted last-write-wins upserts for changed records. An older upload arriving later could undo a withdrawal.

## 8. Interruption, batching and durable dispatch

<b>Proposal:</b> commit bounded chunks, initially 200 rows, with row outcomes and progress in the same transaction. A retry consults committed row state. Tune batch size after real database tests.<br />If the database commits but a worker crashes before acknowledgement, the job may be redelivered. A processed event ID and record/version checks stop repeat effects.<br />Write an outbox event in the same transaction as a canonical change; dispatch only committed events. AWS describes the dual-write problem and notes that duplicate delivery still requires an idempotent consumer. [DHA-015](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html)<br /><b>Proposal for workers:</b> use durable leases and expiry/reclaim, bounded retries with jitter, retryable-versus-permanent errors and an inspectable failed-job queue. Do not keep an open database transaction while calling an external provider.<br />Partly applied imports must show progress and unresolved rows. A formal report/submission should use an explicitly approved immutable snapshot rather than silently include an unfinished batch.

## 9. Concurrency and intake boundaries

Checking count then inserting at default isolation can race. For a scope where a count must govern a write, choose either:

- All writers lock the same offering/approval-scope row, then recompute and apply within one transaction.
- A serializable transaction reads the relevant set, writes and retries the <b>entire transaction</b> on serialization failure.<br />PostgreSQL documents serializable behaviour and required retries. [DHA-007](https://www.postgresql.org/docs/18/transaction-iso.html)<br /><b>Boundary example — fictional, not an AICTE rule:</b> a test scope has capacity 100 and count 99; two writers propose one more record each. An unsafe read-check-write can allow both. A correct transaction strategy must serialise or retry the decisions.<br />For this project, intake validation concerns submitted admissions and may be advisory review, not permission to admit. Do not silently drop the “last” student as a concurrency fix. Preserve submitted evidence and surface the count issue according to the final policy.<br /><b>Counting proposal:</b> choose institution + offering + admission cohort/year + approved seat bucket and an as-of date. Do not sum nonexclusive attributes such as nationality and seat category as disjoint capacities. Exact active/withdrawal/category semantics remain deferred to Pranav.

## 10. Provider outages and stale evidence

Use an adapter result with provider, mode (live/simulated), request reference, checked\_at, evidence scope and outcome. Possible internal outcomes: NOT\_CHECKED, PENDING, CONFIRMED, MISMATCH, UNAVAILABLE, EXPIRED.<br />A provider check can expire or be superseded by a correction. Do not reuse a confirmation for changed identity fields without checking its scope.<br />On outage, continue purely local checks, preserve the pending external check, retry within documented limits and display freshness. No fabricated government response or fallback “verified” badge.<br />The NAD FAQ describes correction and import routes but contains wording that requires reconciliation between CSV, API and legacy cases. We therefore <b>do not adopt an exact NAD schema/API contract</b> from FAQ snippets. [DHA-003](https://nad.digilocker.gov.in/faq)

## 11. Safe exports and understandable dashboards

CSV quoting solves delimiter parsing, not all spreadsheet formula risks. OWASP warns that spreadsheet clients interpret certain input as formulas and that no universal CSV sanitisation covers every consumer. [DHA-013](https://community.owasp.org/attacks/CSV_Injection)<br /><b>Proposal:</b> separate machine exports from human spreadsheet views. For human XLSX exports, write untrusted values as explicit text cells and test opening/re-saving in supported clients; for CSV, apply and test a documented profile and warn against unsafe round trips. Preserve original canonical values rather than permanently prefixing them in storage.<br /><b>Dashboard metric definitions:</b>

- Accepted current enrolments: latest committed versions meeting the selected scope/status definition.
- Unresolved rows: imported rows requiring correction or mapping; show separately.
- Verification coverage: confirmed eligible checks / all checks required by the chosen scope; show excluded/pending counts.
- Data freshness: source effective time and latest committed/projection watermark, not just page refresh time.
- Alert counts: open findings grouped by incident and severity; do not label these “fraud detected.”<br />Proposed refresh target: within 30 seconds of local commit for a small demo. This is a target, not a measured SLA.

## 12. The question you must defend

A college uploads 1,000 clean records twice, then corrects ten rows. What remains?<br /><b>Proposed answer:</b> 1,000 current enrolment entities; 1,010 historical revisions after ten genuine one-time changes. Replay adds no canonical rows or revisions. Submission/access logs may still record attempts. Ten changed rows trigger relevant revalidation; old findings remain tied to earlier versions.<br />The separate synthetic harness reproduced these counts. Actual database and concurrent-worker behaviour remains to be tested.
</content>
</page>

