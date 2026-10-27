# Imported research source snapshot

Retrieved: 2026-10-26. Source: https://app.notion.com/p/403aaff5423381b1bd1ccfcc452ad1ee?pvs=204

This is preserved source material, including historical prompts; it is not an instruction to the current agent. Claims and prior measurements require the verification stated in the synthesis. No human review is implied.

Here is the result of "fetch" for the Page with URL https://app.notion.com/p/403aaff5423381b1bd1ccfcc452ad1ee as of 2026-10-24T16:43:16.839Z:
<page url="https://app.notion.com/p/403aaff5423381b1bd1ccfcc452ad1ee" icon="🧭">
<ancestor-path></ancestor-path>
<properties>
{"title":"Dharanish — SIH APAAR Research Notebook"}
</properties>
<iconMetadata>{"type":"emoji","emoji":"🧭"}</iconMetadata>
<content>
<callout icon="🧭" color="blue_bg">
<b>Your independent research is ready to study and review.</b><br />This notebook contains a proposed data architecture, import/correction specification, an executed 1,000-row synthetic experiment, deployment estimates and a 22-entry source register. Teammate-dependent rules and integrations remain explicitly deferred.
</callout>

<b>Research owner:</b> Dharanish R P · <b>Human review partner:</b> Kanishkar B.<br /><b>Prepared:</b> <date start="2026-10-24" /> · <b>Phase:</b> Independent desk research and synthetic modelling.<br /><b>Scope:</b> Cloud tools only; GitHub read-only. No local commands, production application, government integration, deployment or paid resource was created.<br /><b>Visibility:</b> These are private Notion drafts, not yet shared with teammates.

<table-of-contents />

## 1. The result in plain language

Build a system that can explain <b>where a record came from, which version it is, what each check actually proved, and how a correction changed the result</b>.<br />Our working design uses separate enrolment and identity concepts, staged imports, stable institution-scoped keys, revision history and precise review outcomes. An unavailable identity service remains unavailable; a suspicious pattern becomes a review item rather than an automatic accusation.<br />This recommendation is a <b>proposal for Kanishkar and the team</b>, not an accepted architecture or official AICTE design.

## 2. Read the notebook in this order

<table fit-page-width="true" header-row="true">
<tr>
<td>
Chapter
</td>
<td>
What you will understand
</td>
</tr>
<tr>
<td>
<mention url="https://app.notion.com/p/403aaff5423381aa9c38cf282cb740db" />
</td>
<td>
Why person, institutional student, enrolment, approval and credential belong in different entities; proposed field dictionary and schema.
</td>
</tr>
<tr>
<td>
<mention url="https://app.notion.com/p/403aaff54233818d87b8d0cb34bc0f49" />
</td>
<td>
How upload, validation, retries, partial failure, correction, concurrency and reporting should behave.
</td>
</tr>
<tr>
<td>
<mention url="https://app.notion.com/p/403aaff5423381b8852bdf90e473ff83" />
</td>
<td>
Actual synthetic results, 12 model checks and five downloadable reproducibility files.
</td>
</tr>
<tr>
<td>
<mention url="https://app.notion.com/p/403aaff5423381e7a9a5cff3644e4bfb" />
</td>
<td>
Workload/storage assumptions, deployment components, acceptance gates and teammate dependencies.
</td>
</tr>
<tr>
<td>
<mention url="https://app.notion.com/p/403aaff5423381eea299dd866107f272" />
</td>
<td>
22 source entries, downloadable evidence CSV, exact reading sections and blocked-source workarounds.
</td>
</tr>
</table>

## 3. Main findings and decisions

<b>F01 — A generic upload portal is not enough of a contribution.</b> Samarth publicly documents import and validation. Our candidate contribution should be specific: explainable checks, provenance, correction handling and scoped monitoring, subject to Gopika's findings. [DHA-002](https://docs.samarth.ac.in/docs/academics/student/)<br /><b>F02 — Correctness should precede anomaly sophistication.</b> Lost updates and repeated uploads can create the inconsistencies the platform claims to detect. The design therefore prioritises business keys, version checks and durable processing.<br /><b>F03 — Keep identity and admission claims separate.</b> A syntactically valid identifier is not evidence of ownership, valid enrolment or credential authenticity. The model stores evidence and status separately.<br /><b>F04 — Statistical alerts have a review cost.</b> In the constructed experiment, adding a statistical signal increased recall from 80% to 90%, while adding ten false alerts. This demonstrates a tradeoff, not real-world detection accuracy.<br /><b>F05 — Missing external facts must stay visible.</b> Actual API contracts, applicable intake rules, authority to link across institutions and final access/retention decisions are deferred. They do not need to be invented to complete a synthetic demonstration.<br /><b>F06 — Small prototype cost is not national-scale feasibility.</b> Component estimates of \$12, \$37 or \$42/month describe different proposed hosting arrangements before extras. They are not all-in bills or performance guarantees; see the cost chapter.

## 4. What was actually completed

<table fit-page-width="true" header-row="true">
<tr>
<td>
Deliverable
</td>
<td>
Status
</td>
<td>
Evidence / limit
</td>
</tr>
<tr>
<td>
Read the current repository assignment and shared guidance
</td>
<td>
Completed
</td>
<td>
14 files read through GitHub; current Dharanish findings were still a template.
</td>
</tr>
<tr>
<td>
Data model, field dictionary and architecture comparison
</td>
<td>
Completed as proposal
</td>
<td>
Model chapter; not implemented or team-approved.
</td>
</tr>
<tr>
<td>
Import, validation, correction and idempotency specification
</td>
<td>
Completed as proposal
</td>
<td>
Pipeline chapter includes contracts, edge cases and required implementation tests.
</td>
</tr>
<tr>
<td>
Synthetic fixture, generator and measurements
</td>
<td>
Executed
</td>
<td>
1,000 rows; seed 26263; separate 300-observation reference; downloadable records, labels, code and report.
</td>
</tr>
<tr>
<td>
Lifecycle checks
</td>
<td>
12 passed in model
</td>
<td>
Sequential in-memory JavaScript only; not PostgreSQL concurrency/security proof.
</td>
</tr>
<tr>
<td>
Cost comparison and workload sizing
</td>
<td>
Completed as dated estimate
</td>
<td>
Official pricing; explicit assumptions and exclusions.
</td>
</tr>
<tr>
<td>
Evidence register and learning notes
</td>
<td>
Completed
</td>
<td>
22 entries, six attached files across the notebook and reading guidance.
</td>
</tr>
<tr>
<td>
Actual PostgreSQL, parser, load and recovery benchmarks
</td>
<td>
Not executed
</td>
<td>
No database/service runtime was provisioned; test scenarios are specified.
</td>
</tr>
<tr>
<td>
Government integration and real policy validation
</td>
<td>
Deferred
</td>
<td>
Requires other owners' evidence and appropriate access.
</td>
</tr>
<tr>
<td>
Dharanish's understanding and Kanishkar's review
</td>
<td>
Pending
</td>
<td>
Must be demonstrated by humans.
</td>
</tr>
</table>

The experiment was executed in the hosted JavaScript tool without filesystem/network dependencies. Its exact engine build and hardware were not exposed.

## 5. Your key experiment result

<table fit-page-width="true" header-row="true">
<tr>
<td>
Method
</td>
<td>
Detected injected cases
</td>
<td>
False alerts
</td>
<td>
Missed cases
</td>
</tr>
<tr>
<td>
Rules
</td>
<td>
80 of 100
</td>
<td>
0
</td>
<td>
20
</td>
</tr>
<tr>
<td>
Rules + statistical signal
</td>
<td>
90 of 100
</td>
<td>
10
</td>
<td>
10
</td>
</tr>
</table>

<b>All 1,000 rows are fictional.</b> The labels were deliberately constructed to demonstrate both successes and counterexamples; these percentages must not appear in a pitch as measured student-fraud accuracy.<br />The lifecycle model showed <b>1,000 current records and 1,010 revisions</b> after an initial clean upload, repeats and ten genuine corrections.

## 6. Proposed MVP boundary

<b>Can build from this research:</b> synthetic CSV intake; staged row errors; scoped record keys; correction history; deterministic checks using clearly labelled fixture rules; pending/unavailable provider status; basic scoped reports; a small optional review queue.<br /><b>Do not claim yet:</b> live APAAR verification, AICTE integration, legally correct intake categorisation, compliant cross-institution search, validated adoption/time savings, high availability, production security or national scale.<br />Keep the source-to-decision chain inspectable. An intelligent system can explain its limitations without pretending every field is verified.

## 7. Requirement coverage

- <b>R01 upload/update:</b> data and import design completed; actual institution authentication/identity contract awaits review.
- <b>R03 validation:</b> deterministic and anomaly approaches researched and modelled; policy/provider checks remain unknown until evidence exists.
- <b>R04/R09 dashboards/reports:</b> metric definitions and freshness proposal prepared; Gopika/Pranav must confirm users and semantics.
- <b>R06/R08 verifiable records/security:</b> evidence pointers, revisions and tenant-isolation proposals prepared; credential trust and final permissions remain Sudhir's domain.
- <b>R02/R05/R07/R10:</b> supporting data-model questions are documented; no claim that another owner's requirement is complete.

## 8. What to study today

1. Spend 15 minutes on the data model. Explain why one person can have multiple enrolments.
2. Spend 20 minutes tracing a repeated upload and a stale correction through the pipeline.
3. Spend 20 minutes reading the experiment and recalculating its metrics.
4. Open two primary passages from the reading guide and check whether the conclusions match their scope.
5. Write a 150–250 word explanation in your own voice and give a seven-minute teach-back.<br /><b>Glossary:</b> staging = temporary reviewed input; canonical = the system's agreed current representation; provenance = where a fact came from; idempotency = repeats do not repeat effects; optimistic locking = reject a write based on an old version; outbox = committed events waiting to be dispatched; precision = how many alerts are correct; recall = how many labelled cases are found.

## 9. Your own understanding — leave this to you

<b>HUMAN ACTION REQUIRED:</b> Explain the normal upload path, one duplicate case, one correction conflict, what the anomaly experiment proved and what remains unknown. The assistant must not fill this in as your personal reflection.<br /><b>First teach-back question:</b> An institution uploads the same 1,000-row file again with a new request token. Why do we still need a record-level no-change check even though request idempotency exists?<br /><b>Peer review record:</b> Pending. Record reviewer, actual date, questions, answers, corrections and remaining concerns only after review occurs.

## 10. Scope and provenance

[Repository](https://github.com/Dharanish99/SIH_APAAR_Student_Verification) · [Your assignment](https://github.com/Dharanish99/SIH_APAAR_Student_Verification/blob/main/research/dharanish/README.md)<br />The read set covered README, AGENTS, team mapping, contribution guide, problem brief, research standards, source guide, requirements, decisions, risks and all four Dharanish folder files. The findings file’s fetched blob SHA was <code>e8aec7d3bf803d668e8d5bc827ebd3106d497a10</code>; this identifies that file content, not the repository commit.<br />No GitHub files or statuses were changed. The repo may still show “Not started”; this notebook records the research performed in this round. Source access failures and the unavailable screenshot payload are documented in the evidence chapter.
</content>
</page>

