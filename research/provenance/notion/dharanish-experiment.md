# Imported research source snapshot

Retrieved: 2026-10-26. Source: https://app.notion.com/p/403aaff5423381b8852bdf90e473ff83?pvs=204

Preserved source material; historical prompts are not current instructions. Prior experiment claims are not rerun evidence. Human review remains separate.

Here is the result of "fetch" for the Page with URL https://app.notion.com/p/403aaff5423381b8852bdf90e473ff83 as of 2026-10-24T16:35:28.904Z:
<page url="https://app.notion.com/p/403aaff5423381b8852bdf90e473ff83" icon="🧪">
<ancestor-path></ancestor-path>
<properties>
{"title":"Dharanish Research — Synthetic Experiment & Reproducible Files"}
</properties>
<iconMetadata>{"type":"emoji","emoji":"🧪"}</iconMetadata>
<content>
<callout icon="🧪" color="blue_bg">
<b>Executed synthetic experiment — not real student data or field accuracy.</b><br />One hosted JavaScript V8 model compared deterministic checks with a statistical review signal on 1,000 fictional rows. Twelve in-memory lifecycle checks passed. No PostgreSQL server, real API or production application was exercised.
</callout>

<b>Owner:</b> Dharanish R P · <b>Run date:</b> <date start="2026-10-24" /> · <b>Harness:</b> v1.0 · <b>Seed:</b> 26263.<br /><b>Status:</b> Experiment completed for this model; production validation and human review pending.

<table-of-contents />

## Download the evidence

<b>Full generator and test harness, JavaScript stored as text</b>

<file source="notion-file-block://2ee87d32-4168-412f-92e9-c91c5100cfa2/ff4966ab-279d-49e6-a8ac-48660f2bda92?space_id=7729c767-2e43-4f09-a60e-fd81adbefe50&name=dharanish-research-harness.txt" />

<b>Generated records — 1,000 rows</b>

<file source="notion-file-block://001ae9d6-bc68-45df-b9fc-074a8390e428/ed450d14-e668-4c6a-85b9-c1c9c6428177?space_id=7729c767-2e43-4f09-a60e-fd81adbefe50&name=dharanish-synthetic-records.csv" />

<b>Ground-truth labels — separate from model input</b>

<file source="notion-file-block://f1c2f79d-a56c-476c-b597-8fbcbef99181/47aa4c45-9efb-4315-8aaa-733562609d1e?space_id=7729c767-2e43-4f09-a60e-fd81adbefe50&name=dharanish-synthetic-labels.csv" />

<b>Reference cohort — 300 correction-count observations</b>

<file source="notion-file-block://6568c355-a552-4599-9656-d08a5d5ef428/6bd3fe5c-7613-47b7-a1fc-a9f1c90cda3e?space_id=7729c767-2e43-4f09-a60e-fd81adbefe50&name=dharanish-reference-cohort.csv" />

<b>Actual reported results</b>

<file source="notion-file-block://a2a3a2a0-a7a6-47af-ae85-3c99e0105878/c4f8240b-f608-4e66-bfc4-0e603886e5bd?space_id=7729c767-2e43-4f09-a60e-fd81adbefe50&name=dharanish-experiment-results.json" />

## What question this answers

Can we demonstrate that data checks, retries and corrections behave predictably, and show the cost of adding an anomaly signal?<br />This experiment is deliberately small and understandable. It tests constructed mechanisms, not whether unusual students or institutions are fraudulent. A label here means “injected review case” under the generator, not a real policy violation.

## Dataset design

There are five fictional institution namespaces and three fictional courses. Identity values use <b>SYN-</b> prefixes; they are deliberately not government-looking APAAR numbers. Only identity presence is tested, not APAAR format, existence or ownership.<br />A seeded shuffle assigns disjoint issue groups:

<table fit-page-width="true" header-row="true">
<tr>
<td>
Injected group
</td>
<td>
Rows labelled positive
</td>
<td>
Meaning
</td>
</tr>
<tr>
<td>
Missing synthetic identity reference
</td>
<td>
20
</td>
<td>
Incomplete linkage; merits follow-up, not automatic admission rejection.
</td>
</tr>
<tr>
<td>
End date earlier than start date
</td>
<td>
20
</td>
<td>
Constructed interval inconsistency.
</td>
</tr>
<tr>
<td>
Unknown course reference
</td>
<td>
20
</td>
<td>
Fails the synthetic reference list.
</td>
</tr>
<tr>
<td>
Duplicate business key
</td>
<td>
20
</td>
<td>
Ten pairs; both rows in each ambiguous pair are labelled for review.
</td>
</tr>
<tr>
<td>
Additional constructed review cases
</td>
<td>
20
</td>
<td>
Ten have unusually high correction counts; ten blend into the normal range.
</td>
</tr>
<tr>
<td>
Total positive rows
</td>
<td>
100
</td>
<td>
No overlap between these labelled groups.
</td>
</tr>
<tr>
<td>
Negative rows
</td>
<td>
900
</td>
<td>
Includes ten legitimate high-correction cases to expose false alerts.
</td>
</tr>
</table>

Both sides of a duplicate pair are counted at the <b>row level</b>; there are only ten duplicate incidents. Do not report “twenty duplicate students.” Operational import should group a conflict for review instead of accusing either record.<br />The model uses a separate reference cohort generated with seed 26264. No ground-truth labels are passed into the detector. This separation avoids a basic leakage mistake, but does not make an author-designed fixture independent validation.

## Methods

<b>Rules baseline:</b> flag missing identity, reversed date interval, unknown course, or repeated tenant/source-system/source-key combination. Dates are generated in valid ISO format; this harness does not test a general date parser.<br /><b>Statistical signal:</b> apply a modified Z-score to a synthetic correction-count feature using the reference median and median absolute deviation (MAD). Here median = 2 and MAD = 1.

```txt
MAD = median(abs(reference_value - reference_median))
score = 0.6745 * abs(corrections - reference_median) / MAD
review signal if score > 3.5
if MAD = 0: abstain; do not divide or silently add epsilon
```

[NIST, DHA-016: outlier labeling and modified Z-score](https://itl.nist.gov/div898/handbook/eda/section3/eda35h.htm) provides the statistical starting point. Applying it to correction counts is <b>our exploratory proposal</b>, not a validated domain rule. Discrete counts and mixed institutional workflows may not fit the statistical assumptions.<br /><b>Combined:</b> rule flag OR statistical signal. In a product these must remain separate reasons and action levels.<br />We chose this simple baseline because it is transparent and executable without dependencies. Isolation Forest was researched as a later option but <b>was not trained or benchmarked</b>. [DHA-017](https://scikit-learn.org/stable/modules/outlier_detection.html)

## Actual results

<table fit-page-width="true" header-row="true">
<tr>
<td>
Method
</td>
<td>
TP
</td>
<td>
FP
</td>
<td>
FN
</td>
<td>
TN
</td>
<td>
Precision
</td>
<td>
Recall
</td>
<td>
Alerts
</td>
</tr>
<tr>
<td>
Rules
</td>
<td>
80
</td>
<td>
0
</td>
<td>
20
</td>
<td>
900
</td>
<td>
100%
</td>
<td>
80%
</td>
<td>
80
</td>
</tr>
<tr>
<td>
Statistical signal alone
</td>
<td>
10
</td>
<td>
10
</td>
<td>
90
</td>
<td>
890
</td>
<td>
50%
</td>
<td>
10%
</td>
<td>
20
</td>
</tr>
<tr>
<td>
Combined
</td>
<td>
90
</td>
<td>
10
</td>
<td>
10
</td>
<td>
890
</td>
<td>
90%
</td>
<td>
90%
</td>
<td>
100
</td>
</tr>
</table>

Precision = TP/(TP+FP); recall = TP/(TP+FN). The harness returns null when a denominator is zero. Combined false-positive rate = 10/900 ≈ <b>1.11%</b>, which differs from the <b>10% false-alert share</b> among the 100 alerts. [Metric definitions: DHA-018](https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measures)<br /><b>Incremental result:</b> twenty additional alerts buy ten additional detected cases and ten false alerts. The additional review queue is only 50% precise in this constructed fixture. Reporting combined precision alone hides that operational tradeoff.<br /><b>Why cases were missed:</b> ten injected cases have a correction count of 4, indistinguishable from ordinary records on the selected feature. No threshold can recover those from this feature without also flagging similar valid records.<br /><b>Measured timing:</b> the saved final run reported <b>4 ms</b> for the three metric evaluations, using [Date.now](http://Date.now). This excludes generation, CSV parsing, database/network IO, model lifecycle checks and writing outputs. Hardware and exact V8 version are not exposed. It is a single coarse observation, not a throughput or scaling claim.

## Lifecycle tests actually executed

These tests use a separate clean 1,000-record fixture and a sequential in-memory map, not the polluted validation fixture.

1. <b>PASS — initial insert 1000.</b>
2. <b>PASS — same request replay creates no revisions.</b>
3. <b>PASS — new request token same content is no-op.</b>
4. <b>PASS — ten corrections yield 1000 entities and 1010 revisions.</b>
5. <b>PASS — changed body with old token is rejected.</b>
6. <b>PASS — tenant mismatch denied before writes.</b>
7. <b>PASS — crash after 37 committed rows resumes without repeated revisions.</b>
8. <b>PASS — stale optimistic version denied.</b>
9. <b>PASS — two same-version edits: one accepted in sequential model.</b>
10. <b>PASS — provider unavailable does not become identity verified.</b>
11. <b>PASS — tenant-scoped business keys keep equal local IDs separate.</b>
12. <b>PASS — zero-MAD reference abstains.</b><br /><b>Key trace:</b> first import → 1,000 current entities and 1,000 revisions; exact replay → unchanged; new token with same data → unchanged; ten corrections → 1,000 entities and 1,010 revisions.<br />The interruption test then adds 100 separate records, fails after 37 committed inserts, and resumes to 1,100 entities and 1,110 revisions without duplicate revisions.<br /><b>Limits of these checks:</b> tenant denial is a model condition, not a security penetration test. “Two same-version edits” is a sequential optimistic-version simulation, not simultaneous database clients. Provider outage is a stub that reports unavailable. Atomic rollback, lock contention, RLS, durable storage and outbox delivery are not implemented in this harness.<br />The simplified batch model does not include a production expected-version protocol for every import, transaction rollback, request hashing or durable job leases. Do not use this model as a deployable backend.

## Reproduce without using your computer’s terminal

Open the attached text in any suitable <b>cloud JavaScript execution environment</b> supporting modern JavaScript, paste the code and run it. It uses only standard language features, Math and Date; no packages, files, credentials or network requests.<br />The last lines print the report. The returned <code>result.csv</code>, <code>result.truthCsv</code> and <code>result.referenceCsv</code> reproduce the attached datasets. If using a cloud Node terminal, save the text as <code>research-harness.js</code> and run:

```txt
node research-harness.js
```

Metric counts, fixtures and checks should match; milliseconds will vary. The generator uses the specified linear congruential PRNG, not Math.random. Source and generated outputs are included so the work can be inspected rather than trusted as a screenshot.

## What to test next in an implementation

- PostgreSQL: race two inserts with the same tenant/business key; verify only one logical entity and consistent history.
- Stale edit: two sessions read version 2; only one update to version 3 succeeds. The other receives a conflict with no partial audit write.
- Capacity: two transactions read a count at the boundary; use a shared lock or serializable transaction and retry. Test applicable policy separately after Pranav supplies it.
- Crash: terminate a worker after database commit but before acknowledgement; restart and check current rows, history and outbox.
- Parser: quoted commas/newlines, BOM, missing headers, leading zeros, malformed dates, excessive rows and XLSX expansion.
- Isolation: normal user cannot read/write another institution, including through exports and background jobs.
- Recovery: restore backup and reconcile projection watermark and outstanding jobs.<br />These are fully specified next-stage checks, <b>not reported as passed</b>.

## Interpretation and decision

<b>Proposal:</b> deliver deterministic data-quality checks and a transparent review queue first. Keep statistical anomalies optional and non-adjudicative until a representative evaluation exists.<br />Future evaluation should split by institution/time where appropriate, fit preprocessing on training data only, keep a final test set untouched and measure incremental useful findings per review-hour. Do not feed identities, raw names, protected categories or arbitrary programme codes into a distance model as if they were meaningful numerical features. [Leakage guidance: DHA-019](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage)

## Learning check

Without looking back: if the combined detector raises 100 alerts and 10 are false, why is its false-positive rate not 10%? Then explain why ten legitimate high-correction records prevent us from calling the statistical signal a fraud detector.<br /><b>Your answer and human review: pending.</b>
</content>
</page>

