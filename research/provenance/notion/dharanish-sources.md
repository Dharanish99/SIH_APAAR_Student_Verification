# Imported research source snapshot

Retrieved: 2026-10-26. Source: https://app.notion.com/p/403aaff5423381eea299dd866107f272?pvs=204

Preserved source material; historical prompts are not current instructions. Prior experiment claims are not rerun evidence. Human review remains separate.

Here is the result of "fetch" for the Page with URL https://app.notion.com/p/403aaff5423381eea299dd866107f272 as of 2026-10-24T16:41:41.752Z:
<page url="https://app.notion.com/p/403aaff5423381eea299dd866107f272" icon="📖">
<ancestor-path></ancestor-path>
<properties>
{"title":"Dharanish Research — Sources, Reading Guide & Evidence Limits"}
</properties>
<iconMetadata>{"type":"emoji","emoji":"📖"}</iconMetadata>
<content>
<callout icon="📖" color="blue_bg">
<b>Read sources to verify decisions, not to collect links.</b><br />This register contains 22 source entries with their purpose, version, reading section and limitations. It includes explicit access gaps rather than treating every entry as fully verified.
</callout>

<b>Research access date:</b> <date start="2026-10-24" />. Publication dates are separate; unknown means unknown.

## Download the source register

<file source="notion-file-block://222ee0ba-1d1a-4efb-9a75-a1882ee34d7d/e0412be9-a7e9-43e7-9bd2-562beb39e550?space_id=7729c767-2e43-4f09-a60e-fd81adbefe50&name=dharanish-sources.csv" />

The CSV follows the repository’s existing 12-column evidence format, but <b>has not been committed to GitHub</b>.

## Start here: a focused reading order

1. <b>Samarth (DHA-002, 10 minutes):</b> identify what import/validation already exists. Write one sentence about why our project needs a more specific contribution.
2. <b>PostgreSQL constraints (DHA-006, 20 minutes):</b> study scoped uniqueness and foreign keys. Explain why an enrolment key differs from a person identifier.
3. <b>Idempotency and outbox (DHA-014/015, 20 minutes):</b> draw the crash between database commit and response/event delivery. Explain how a retry becomes safe.
4. <b>Transaction isolation (DHA-007, 20 minutes):</b> work through two writers near a capacity boundary. Distinguish a model example from a passed database test.
5. <b>NIST and metrics (DHA-016/018, 20 minutes):</b> calculate the experiment’s precision, recall and false-positive rate yourself.
6. <b>RLS and upload/export security (DHA-008/012/013, 20 minutes):</b> explain two ways a safe-looking import can expose another institution’s data.
7. <b>Pricing (DHA-020/021, 10 minutes):</b> list what a quoted component price excludes.<br />These times are suggested study blocks. Prioritise the questions you cannot yet explain.

## Evidence log and access workarounds

- <b>Official SIH listing:</b> direct request to [https://www.sih.gov.in/sih2026PS](https://www.sih.gov.in/sih2026PS) returned 403. An exact-ID official-domain search did not provide usable corroboration. We retain the supplied statement as the scope baseline and leave official confirmation to the lead.
- <b>APAAR FAQ:</b> direct and www-host requests failed in this round. An official-domain search returned the indexed FAQ, including the identifier-format description. This supports limited background, not a current operational API contract.
- <b>NAD:</b> the resource index was readable earlier in this conversation, then returned 403 on the current retry. A separate FAQ request succeeded after retry. The older indexed manual and current resource listing have different version indicators; no exact downloadable template is claimed as inspected.
- <b>OWASP CSV injection:</b> initially tried unavailable cheat-sheet URLs; an official-domain search found the accessible OWASP community page. That is the cited source, not the failed URL.
- <b>AISHE PDF:</b> used the official listing’s direct PDF and extracted the relevant module/page text. A cloud PDF screenshot request for index 14 returned an image marker but no usable image payload in this interface. Therefore the finding relies on readable PDF text; <b>no visual verification or saved screenshot is claimed</b>. [Open PDF at page 15](https://cdnbbsr.s3waas.gov.in/s392049debbe566ca5782a3045cf300a3c/uploads/2024/12/20250728227262067.pdf#page=15).<br />We did not use local PowerShell, local files, your desktop browser or private government accounts. The research used connected cloud tools and a hosted JavaScript isolate.

## Claim-level conclusions and their status

<table fit-page-width="true" header-row="true">
<tr>
<td>
ID
</td>
<td>
Conclusion
</td>
<td>
Evidence
</td>
<td>
Status / limit
</td>
</tr>
<tr>
<td>
F01
</td>
<td>
Import and validation already appear in a public student portal guide.
</td>
<td>
DHA-002
</td>
<td>
Documented capability; not adoption evidence.
</td>
</tr>
<tr>
<td>
F02
</td>
<td>
Separate person, enrolment, approval and credential concepts.
</td>
<td>
Project scope + model reasoning; DHA-001/005/006
</td>
<td>
Our design proposal.
</td>
</tr>
<tr>
<td>
F03
</td>
<td>
Use tenant-scoped keys and version-aware corrections.
</td>
<td>
DHA-006/009/014 plus lifecycle model
</td>
<td>
Proposal with limited synthetic support; no database proof.
</td>
</tr>
<tr>
<td>
F04
</td>
<td>
Capacity/count checks need an explicit concurrency strategy.
</td>
<td>
DHA-007
</td>
<td>
Technical basis documented; domain rule deferred.
</td>
</tr>
<tr>
<td>
F05
</td>
<td>
A statistical signal adds both detections and false alerts in our fixture.
</td>
<td>
Attached harness/results; DHA-016/018 for method
</td>
<td>
Executed synthetic observation, not field accuracy.
</td>
</tr>
<tr>
<td>
F06
</td>
<td>
Data-category meanings must be mapped to the reporting context.
</td>
<td>
DHA-005
</td>
<td>
Specific AISHE reporting example, not AICTE policy.
</td>
</tr>
<tr>
<td>
F07
</td>
<td>
Price options require component and security-feature distinctions.
</td>
<td>
DHA-020/021
</td>
<td>
Observed list prices; workload and architecture estimates remain assumptions.
</td>
</tr>
<tr>
<td>
F08
</td>
<td>
Provider payloads, exact policy rules and real permissions remain unresolved.
</td>
<td>
Repository scope; source-access log; teammate boundaries
</td>
<td>
Unknown/deferred. No fabricated integration.
</td>
</tr>
</table>

## Source cards

### DHA-001 — SIH26263 supplied statement

[Read the source](https://zaidsayyed.in/tools/sih-problem-statements/sih26263)<br /><b>Publisher/version:</b> Zaid Sayyed · unknown.<br /><b>Read:</b> Problem Description; Key Requirements.<br /><b>Use:</b> Project requirements baseline. <b>Scope:</b> Project scope only.<br /><b>Access:</b> Opened. <b>Limit:</b> Official SIH listing remains inaccessible; generic commentary excluded.

### DHA-002 — Student Portal Guide

[Read the source](https://docs.samarth.ac.in/docs/academics/student/)<br /><b>Publisher/version:</b> Samarth · 1.4.12; last update 2024-07-25.<br /><b>Read:</b> Import Students; Role Access.<br /><b>Use:</b> Existing import and validation capability. <b>Scope:</b> Samarth documented workflow.<br /><b>Access:</b> Opened. <b>Limit:</b> Not an observed college workflow or proof of integration access.

### DHA-003 — NAD FAQ

[Read the source](https://nad.digilocker.gov.in/faq)<br /><b>Publisher/version:</b> DigiLocker NAD · unknown.<br /><b>Read:</b> CSV headers; mistaken upload correction; importing data; secure API.<br /><b>Use:</b> Award records; correction workflow; format documentation. <b>Scope:</b> Academic awards.<br /><b>Access:</b> Opened after retry. <b>Limit:</b> FAQ contains CSV-only wording alongside API/legacy routes; current contract unresolved.

### DHA-004 — NAD Resource Centre

[Read the source](https://nad.digilocker.gov.in/resource-center)<br /><b>Publisher/version:</b> DigiLocker NAD · Listing: college marksheet 7.2; guidelines 2.12; manual 1.4.<br /><b>Read:</b> College Template & Guidelines; User Manual.<br /><b>Use:</b> NAD templates and manual discovery. <b>Scope:</b> Discovery of award formats.<br /><b>Access:</b> Earlier session page opened; current retry 403. <b>Limit:</b> Specific template downloads not inspected; do not invent exact headers.

### DHA-005 — AISHE College/Standalone Web DCF manual

[Read the source](https://cdnbbsr.s3waas.gov.in/s392049debbe566ca5782a3045cf300a3c/uploads/2024/12/20250728227262067.pdf)<br /><b>Publisher/version:</b> Ministry of Education / AISHE · 2024-25 listing; publication date unknown.<br /><b>Read:</b> Module 3; PDF page 15 (index 14).<br /><b>Use:</b> Reporting dimensions differ from admission categories. <b>Scope:</b> AISHE survey reporting only.<br /><b>Access:</b> PDF text opened; screenshot request returned image marker only. <b>Limit:</b> Not an AICTE admission-rule source; visual inspection could not be confirmed.

### DHA-006 — PostgreSQL Constraints

[Read the source](https://www.postgresql.org/docs/18/ddl-constraints.html)<br /><b>Publisher/version:</b> PostgreSQL · 18.<br /><b>Read:</b> 5.5.1; 5.5.3; 5.5.5.<br /><b>Use:</b> Relational integrity and scoped uniqueness. <b>Scope:</b> Proposed PostgreSQL design.<br /><b>Access:</b> Opened. <b>Limit:</b> Does not validate our schema or policy assumptions.

### DHA-007 — PostgreSQL Transaction Isolation

[Read the source](https://www.postgresql.org/docs/18/transaction-iso.html)<br /><b>Publisher/version:</b> PostgreSQL · 18.<br /><b>Read:</b> 13.2.1; 13.2.3.<br /><b>Use:</b> Concurrent aggregate checks and retries. <b>Scope:</b> Concurrency design.<br /><b>Access:</b> Opened. <b>Limit:</b> Actual multi-session database tests not executed.

### DHA-008 — PostgreSQL Row Security Policies

[Read the source](https://www.postgresql.org/docs/18/ddl-rowsecurity.html)<br /><b>Publisher/version:</b> PostgreSQL · 18.<br /><b>Read:</b> 5.9; default deny; table-owner and BYPASSRLS behaviour.<br /><b>Use:</b> Tenant isolation capabilities and bypass caveats. <b>Scope:</b> Defence-in-depth proposal.<br /><b>Access:</b> Opened. <b>Limit:</b> Requires real role/policy tests; does not replace application authorisation.

### DHA-009 — PostgreSQL INSERT

[Read the source](https://www.postgresql.org/docs/18/sql-insert.html)<br /><b>Publisher/version:</b> PostgreSQL · 18.<br /><b>Read:</b> ON CONFLICT clause.<br /><b>Use:</b> Atomic conflict handling. <b>Scope:</b> Import persistence.<br /><b>Access:</b> Opened. <b>Limit:</b> Upsert alone does not resolve semantic conflicts or stale edits.

### DHA-010 — PostgreSQL COPY

[Read the source](https://www.postgresql.org/docs/18/sql-copy.html)<br /><b>Publisher/version:</b> PostgreSQL · 18.<br /><b>Read:</b> COPY FROM STDIN; CSV format.<br /><b>Use:</b> Bulk-load staging option. <b>Scope:</b> Proposed staging ingestion.<br /><b>Access:</b> Opened. <b>Limit:</b> No throughput benchmark performed.

### DHA-011 — RFC 4180

[Read the source](https://www.rfc-editor.org/info/rfc4180/)<br /><b>Publisher/version:</b> RFC Editor / IETF · October 2005; Informational.<br /><b>Read:</b> Section 2; text/csv registration.<br /><b>Use:</b> Quoted CSV fields and format profile. <b>Scope:</b> CSV parser profile.<br /><b>Access:</b> Opened. <b>Limit:</b> Informational baseline; not all real CSV dialects conform.

### DHA-012 — OWASP File Upload Cheat Sheet

[Read the source](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)<br /><b>Publisher/version:</b> OWASP · Living page; date unknown.<br /><b>Read:</b> Introduction; File Upload Protection; limits.<br /><b>Use:</b> Safe file intake controls. <b>Scope:</b> Upload boundary.<br /><b>Access:</b> Opened. <b>Limit:</b> Specific library and controls still require implementation and testing.

### DHA-013 — OWASP CSV Injection

[Read the source](https://community.owasp.org/attacks/CSV_Injection)<br /><b>Publisher/version:</b> OWASP · Living page; date unknown.<br /><b>Read:</b> Spreadsheet formula interpretation; mitigation limitations.<br /><b>Use:</b> Formula injection on export. <b>Scope:</b> Human-readable spreadsheet exports.<br /><b>Access:</b> Opened through alternative official URL. <b>Limit:</b> No universal CSV sanitisation across spreadsheet clients.

### DHA-014 — Make mutating operations idempotent

[Read the source](https://docs.aws.amazon.com/wellarchitected/2025-02-25/framework/rel_prevent_interaction_failure_idempotent.html)<br /><b>Publisher/version:</b> AWS · Framework snapshot 2025-02-25.<br /><b>Read:</b> Implementation guidance.<br /><b>Use:</b> Retry token semantics. <b>Scope:</b> Proposed idempotent request contract.<br /><b>Access:</b> Opened. <b>Limit:</b> Our replay and content rules are project proposals.

### DHA-015 — Transactional outbox pattern

[Read the source](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html)<br /><b>Publisher/version:</b> AWS · Living page; date unknown.<br /><b>Read:</b> Intent; Issues and considerations; outbox table.<br /><b>Use:</b> Avoid database/event dual-write gap. <b>Scope:</b> Proposed job/event dispatch.<br /><b>Access:</b> Opened. <b>Limit:</b> Duplicate delivery still requires consumer deduplication.

### DHA-016 — Detection of Outliers

[Read the source](https://itl.nist.gov/div898/handbook/eda/section3/eda35h.htm)<br /><b>Publisher/version:</b> NIST/SEMATECH · Publication date unknown.<br /><b>Read:</b> Outlier labeling; modified Z-score.<br /><b>Use:</b> Potential outliers and modified Z-score. <b>Scope:</b> Exploratory review signal.<br /><b>Access:</b> Opened. <b>Limit:</b> Threshold is not a student-fraud rule; distribution and cohort assumptions matter.

### DHA-017 — Novelty and Outlier Detection

[Read the source](https://scikit-learn.org/stable/modules/outlier_detection.html)<br /><b>Publisher/version:</b> scikit-learn · Served as 1.9.1 on access.<br /><b>Read:</b> 2.7; 2.7.3.2.<br /><b>Use:</b> Isolation Forest as a later candidate. <b>Scope:</b> Later comparative evaluation.<br /><b>Access:</b> Opened. <b>Limit:</b> No Isolation Forest was trained in this research.

### DHA-018 — Metrics and scoring

[Read the source](https://scikit-learn.org/stable/modules/model_evaluation.html)<br /><b>Publisher/version:</b> scikit-learn · Served as 1.9.1 on access.<br /><b>Read:</b> 3.4.4.9; binary classification.<br /><b>Use:</b> Precision/recall definitions. <b>Scope:</b> Synthetic metric definitions.<br /><b>Access:</b> Opened. <b>Limit:</b> Synthetic prevalence and labels do not estimate field accuracy.

### DHA-019 — Common pitfalls and recommended practices

[Read the source](https://scikit-learn.org/stable/common_pitfalls.html)<br /><b>Publisher/version:</b> scikit-learn · Served as 1.9.1 on access.<br /><b>Read:</b> 12.2 Data leakage.<br /><b>Use:</b> Prevent evaluation leakage. <b>Scope:</b> Future model evaluation design.<br /><b>Access:</b> Opened. <b>Limit:</b> Designed fixture remains a mechanism demonstration, not external validation.

### DHA-020 — Amazon Lightsail Pricing

[Read the source](https://aws.amazon.com/lightsail/pricing/)<br /><b>Publisher/version:</b> AWS · Current page observed 2026-10-24.<br /><b>Read:</b> Linux public IPv4 bundles; databases; snapshots; region footnotes.<br /><b>Use:</b> Cloud cost components. <b>Scope:</b> Illustrative synthetic-demo deployment options.<br /><b>Access:</b> Opened. <b>Limit:</b> USD list prices; taxes, actual usage, region and other components extra.

### DHA-021 — Supabase Pricing

[Read the source](https://supabase.com/pricing)<br /><b>Publisher/version:</b> Supabase · Current page observed 2026-10-24.<br /><b>Read:</b> Free; Pro; compute credits.<br /><b>Use:</b> Managed PostgreSQL alternative cost. <b>Scope:</b> Alternative prototype backend.<br /><b>Access:</b> Opened. <b>Limit:</b> Application worker hosting and overages not included in comparison.

### DHA-022 — APAAR FAQ

[Read the source](https://apaar.education.gov.in/faqs)<br /><b>Publisher/version:</b> Ministry of Education / APAAR · unknown.<br /><b>Read:</b> Questions 2-4.<br /><b>Use:</b> APAAR identifier format background. <b>Scope:</b> Background format only.<br /><b>Access:</b> Current direct open 403; official indexed text retrieved. <b>Limit:</b> Format reference only; no existence/ownership or API verification.

## How to use this register

For a claim in your presentation, open the linked source and inspect the named section. State the version and scope. Use the claim ID from the notes and the DHA source ID when handing evidence to a teammate.<br />A source may support a technical primitive without validating our architecture. A pricing page cannot prove performance. An official FAQ cannot prove this team’s credentials work. A statistical reference cannot prove an unusual record is fraudulent.<br /><b>No full government datasets, personal records or copyrighted manuals have been copied into these notes.</b> Links and short paraphrases are used; attached records are synthetic.

## Human verification log

<b>Pending:</b> record which two primary passages Dharanish personally read, his interpretation, one counterexample and any correction to these notes. Do not mark the work reviewed merely because the assistant checked links and calculations.
</content>
</page>

