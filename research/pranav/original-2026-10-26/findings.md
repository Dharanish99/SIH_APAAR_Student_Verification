# Pranav — AICTE Admission Rules and Compliance Logic

**Project:** SIH APAAR Student Verification  
**Owner:** Pranav  
**Review partner:** Gopika  
**Status:** Initial research draft — primary-source and team review still required  
**Last updated:** 2026-10-26

> **Research integrity statement:** This document is a working draft, not legal advice or an official AICTE/UGC interpretation. It separates source-based findings from proposed system behavior and unresolved questions. The general policy sources below have been identified, but current amendments and institution-specific approvals have not been exhaustively verified. No live AICTE/APAAR API access, institution-specific EoA retrieval, or human review is claimed.

## Executive summary

The proposed validation system must compare each student's admission record against the applicable approval for the institution, programme/course and academic year. It must distinguish regular intake from separately authorized supernumerary categories, validate the category actually used, and treat duplicate identity matches as signals for review rather than automatic evidence of misconduct.

The rule engine should provide explainable outcomes, retain the source and rule version used, and route ambiguous policy questions to the competent authority. Exact category limits, exceptions and effective dates must be grounded in the current applicable official provisions before production use.

## Research question 1 — Which approval record establishes institution/course/year capacity?

### Finding

The authoritative starting record is the applicable AICTE Extension of Approval (EoA) or approval letter for the specific institution, programme/course and academic year. AICTE's Approval Process Handbook 2024–2027, Clause 2.25, is the starting reference for the approval process and EoA.

Capacity must not be taken solely from a number typed by the institution into a student-upload form. Subsequent official amendments, revised approvals or applicable orders must be considered if they change the original approval.

### Required inputs

| Input | Purpose |
|---|---|
| Institution identifier | Identifies the institution |
| Programme/course identifier | Distinguishes courses offered by the same institution |
| Academic year | Selects the applicable approval period |
| Approval/EoA identifier | Traces the authoritative document |
| Approved intake | Establishes the capacity for the relevant programme |
| Approval status/effective dates | Determines whether the record applies |
| Amendments/subsequent orders | Resolves revisions to the original approval |
| Retrieval timestamp/version | Supports auditability |

### Rule `PRA-R01` — Resolve authoritative approval

- **Condition:** A current, applicable approval record must be available for the institution, programme and academic year.
- **Inputs:** Institution ID, programme ID, academic year, approval status and approved intake.
- **Action:** Match submitted enrolment against the applicable approval.
- **Outcome:** `PASS_DATA_CHECK` when the approval is matched and the specific capacity check passes.
- **Exception:** Missing, ambiguous, outdated or conflicting approval → `REVIEW_REQUIRED`.
- **Source:** AICTE Approval Process Handbook 2024–2027, Clause 2.25 (exact text and any later amendments must be checked before production use).
- **Scope:** Relevant institution/programme within the applicable AICTE approval requirements.

### Approval-data authority and correction proposal

1. Retrieve the official approval through an authorized AICTE source or obtain the official document.
2. Match institution, programme and academic year.
3. Check for later amendments and category-specific permissions.
4. Store document identifier, effective dates, approved intake, retrieval date and version.
5. Do not allow an institution to overwrite official capacity directly.
6. If the institution disputes the value, create a correction request with evidence and refer it to the competent authority.

This is a proposed workflow. The actual current correction procedure and availability of an approved API have not been verified.

### Evidence limitation

A current institution-specific EoA and its amendment history have not been retrieved for this research. Therefore, no particular institution/course/year capacity is asserted as verified.

### Effect on the system

Use versioned approval data, not a manually entered capacity. Retain the approval version used for every validation decision.

## Research question 2 — How do approved intake, regular seats and supernumerary categories differ?

### Finding

Approved intake is the approved capacity for the relevant programme. Regular admissions are counted under the applicable ordinary-intake rules. Supernumerary seats are additional seats permitted by specific provisions and must be tracked by category.

A total above ordinary approved intake is not automatically a violation. The system must establish whether additional admissions fall under a permitted category and satisfy its conditions.

### Category research matrix

| Category | What must be verified | Validation approach |
|---|---|---|
| Regular intake | Approved capacity for course/year | Compare regular admissions with applicable intake |
| NRI | Applicable NRI provision, eligibility, limit and approval | Check category-specific rules; do not assume universal applicability |
| OCI | Relevant eligibility and allocation provision | Confirm category used and supporting evidence |
| Foreign National (FN) | Applicable AICTE/UGC provisions and any permission | Verify eligibility, authorization and applicable limit |
| Children of Indian Workers in Gulf Countries (CIWG), where applicable | Specific provision and any subcategory conditions | Keep separate where the rule requires it |
| Lateral entry | Entry route, eligibility and permitted intake | Apply its own provision and scope |
| Tuition Fee Waiver (TFW), where applicable | TFW eligibility/allocation provisions | Do not equate TFW automatically with international/NRI seats |
| Other categories | Applicable rule and authorization | Add only after source verification |

The table lists research topics; it does not mean every category applies to every programme or institution.

### Rules

**`PRA-R02` — Separate capacity dimensions**
- **Condition:** Admissions must be classified as regular or into a specifically identified additional category.
- **Inputs:** Approved intake, admission route, category used, admission status and authorization evidence.
- **Action:** Maintain separate counts for regular intake and each applicable category.
- **Outcome:** Pass the classification check when the inputs and evidence are supported.
- **Exception:** Category selection alone does not establish authorization.
- **Source:** Relevant AICTE handbook definitions and category provisions.
- **Scope:** Applicable programme/institution/year.

**`PRA-R03` — Apparent excess regular admissions**
- **Condition:** Regular admission count exceeds applicable approved intake.
- **Inputs:** Current approved intake, admission status and correctly classified regular admissions.
- **Action:** Generate `APPARENT_EXCESS` and require review before final clearance.
- **Exception:** Recalculate if duplicates, withdrawals, misclassification or verified exceptions affect the count.
- **Source:** Applicable approval record and current intake rules.
- **Scope:** Institution/course/year.

**`PRA-R04` — Supernumerary authorization**
- **Condition:** Admission is recorded under a supernumerary category.
- **Inputs:** Category, applicable rule, count, eligibility evidence and required authorization.
- **Action:** Check the category-specific conditions and limits.
- **Outcome:** Pass the specific check if evidence and conditions are satisfied; otherwise review.
- **Exception:** Category limits and conversion rules may differ.
- **Source:** Applicable AICTE provisions and any required institution-specific approval.
- **Scope:** Only categories/programmes covered by the applicable provision.

### Important calculation principle

Do not implement one universal formula such as `total admissions ≤ approved intake + 15%` unless an applicable, verified provision explicitly establishes that calculation for the exact category and context. Track categories separately and apply only documented combined ceilings.

### Evidence limitation

Complete category-by-category limits, exceptions, amendments and current-year applicability have not yet been exhaustively verified. This is a research framework, not confirmation that every listed category applies.

### Effect on the system

Maintain separate regular and category-specific counts. Dashboards should distinguish apparent excess from a violation confirmed by an authorized decision-maker.

## Research question 3 — How do nationality/status and the seat category actually used relate?

### Finding

A student's declared nationality/status, the evidence supporting it, and the category in which the institution admitted the student are different data points. A declared NRI, OCI or Foreign National status does not by itself establish eligibility for a particular seat category.

Eligibility depends on applicable rules, documentary/authoritative evidence, admission route and any required authorization.

### Proposed data model

| Field | Purpose |
|---|---|
| Declared status | Status reported by the student/institution |
| Evidence type | Type of supporting document or authoritative confirmation |
| Evidence verification status | Pending, verified, rejected or review required |
| Actual seat category used | Category under which admission was recorded |
| Admission route | Regular, lateral entry or other applicable route |
| Applicable rule version | Identifies policy used for validation |
| Reviewer decision | Records authorized resolution if required |

Sensitive documents should be protected through role-based access and data minimization.

### Rule `PRA-R05` — Category/status consistency

- **Condition:** Recorded status, category used and eligibility evidence must be consistent with applicable rules.
- **Inputs:** Declared status, category, admission route, evidence and relevant category provisions.
- **Action:** Check consistency and evidence completeness.
- **Outcome:** `PASS_DATA_CHECK` if the specific consistency check passes.
- **Exception:** Missing evidence or disputed eligibility → `REVIEW_REQUIRED`.
- **Source:** Applicable AICTE category provisions and relevant UGC/competent-authority rules.
- **Scope:** Relevant admission category/programme.

### Examples

- **Normal:** Required evidence is present and consistent with the category. The evidence-completeness check may pass; overall eligibility still needs the other applicable checks.
- **Failure:** Evidence required by the applicable rule is missing. Mark incomplete or request review.
- **Ambiguous:** Declared OCI status conflicts with the seat category used. Flag the discrepancy and refer it to an authorized reviewer.

### Evidence limitation

Exact evidence and eligibility requirements for NRI, OCI and Foreign National categories must be extracted from the applicable clauses. No single universal evidence requirement is asserted here.

### Effect on the system

Keep status and seat category separate. Do not infer nationality or category eligibility from an APAAR ID, name or unverified label.

## Research question 4 — Which rules cover NRI, OCI, Foreign National, lateral entry and other categories?

### Primary-source starting points

- **PRA-001:** AICTE, *Approval Process Handbook 2024–2027*: https://www.aicte.gov.in/sites/default/files/APH%20Final.pdf
- **PRA-002:** UGC, international-student guidelines and related guidance: https://www.ugc.gov.in/KeyInitiative
- **PRA-003:** UGC guidelines listing, including simultaneous-programme guidance: https://www.ugc.gov.in/Guideline

### Rule catalogue

| Rule ID | Rule to establish | Inputs | Action | Exceptions/scope |
|---|---|---|---|---|
| `PRA-R06` | NRI eligibility and limit | Approved intake, NRI count, evidence, course/year | Apply verified NRI provision | Confirm exact clause and category-conversion rules |
| `PRA-R07` | OCI eligibility | Status evidence, category, programme/year | Validate against applicable rule | Do not assume OCI and FN rules are identical |
| `PRA-R08` | Foreign National eligibility/limit | Category, evidence, count, authorization | Apply verified AICTE/UGC provisions | Check programme scope and specific ceiling |
| `PRA-R09` | Lateral-entry eligibility/intake | Route, prior qualification, programme, entry year | Apply relevant lateral-entry provision | Do not apply a generic formula without checking scope |
| `PRA-R10` | Combined ceiling, if applicable | Relevant category counts and approved intake | Calculate only the categories named in the verified clause | Confirm exact categories, denominator, exceptions and year |
| `PRA-R11` | Other applicable category seats | Category, evidence, permission and count | Apply its own rule | Do not generalize another category's limit |

### Research procedure

For every category:
1. Open the official source.
2. Search for the category and read the complete clause in context.
3. Record exact clause/page, publication/version and effective academic year.
4. Identify programme/institution scope and exceptions.
5. Check amendments/corrigenda and required institution-specific permissions.
6. Translate the provision into a rule with inputs, action and exceptions.
7. Record uncertainty and seek review before implementation.

### Evidence limitation

The exact current provisions for every category and combination have not been exhaustively verified. This catalogue is a research plan and initial design, not confirmation that every rule applies to every institution.

### Effect on the system

Version rules by academic year, programme and category. Never hardcode a single category percentage across all admissions.

## Research question 5 — How do transfers, withdrawals, course changes and simultaneous programmes affect validation?

### Primary source

**PRA-003:** UGC, *Guidelines for Pursuing Two Academic Programmes Simultaneously* and the modification published 5 June 2025.

Official guidelines listing: https://www.ugc.gov.in/Guideline

Read the original guidelines together with the modification and any applicable institutional, statutory or professional-council rules.

### Finding

A repeated APAAR ID is a matching signal, not proof of an invalid admission. A student may have transferred, withdrawn, changed course, or be pursuing programmes simultaneously in circumstances permitted by applicable rules. The system needs a lifecycle model rather than a single permanent active flag.

### Rules

**`PRA-R12` — Transfers**
- **Condition:** Student is recorded as moving between institutions.
- **Inputs:** Old/new institution, course, effective date, transfer evidence and status.
- **Action:** Verify transfer and update active status without deleting historical records.
- **Outcome:** Pass the lifecycle check after authorized verification.
- **Exception:** Missing/conflicting evidence → review.
- **Source:** Applicable institution/university rules; exact transfer clauses still to be researched.

**`PRA-R13` — Withdrawals**
- **Condition:** Institution reports withdrawal.
- **Inputs:** Withdrawal status/date, supporting record and submitter authorization.
- **Action:** Update status and recalculate counts using applicable effective-date rules.
- **Outcome:** Pass after verification.
- **Exception:** Disputed/undated withdrawal → review.
- **Source:** Applicable institution/university rules; exact clauses still to be researched.

**`PRA-R14` — Course changes**
- **Condition:** Student changes programme/course.
- **Inputs:** Old/new course, effective date and approval/eligibility evidence.
- **Action:** Preserve history and validate the new course under its own applicable rules.
- **Outcome:** Pass if the change is authorized and relevant checks succeed.
- **Exception:** Missing approval or inconsistent record → review.
- **Source:** Applicable AICTE, university and institutional rules.

**`PRA-R15` — Simultaneous programmes**
- **Condition:** Same APAAR ID appears in multiple active programmes.
- **Inputs:** Programme mode, dates, institution, timetable where relevant, recognition status and applicable policy.
- **Action:** Apply current UGC guidance and relevant programme-specific rules.
- **Outcome:** Do not automatically reject merely because the identity is repeated.
- **Exception:** Missing evidence, conflicting rules or potentially overlapping schedules → review.
- **Source:** UGC simultaneous-programme guidelines and modification.

### Worked cases

**Transfer:** A student appears active at College A and College B. College B reports a transfer, but College A has not updated its record.  
**Outcome:** `REVIEW_REQUIRED`; obtain effective-dated transfer evidence and preserve both historical records.

**Withdrawal:** A student withdrew in September, but the institution still reports the student as active.  
**Outcome:** `REVIEW_REQUIRED` until withdrawal and effective date are verified; then recalculate counts under the applicable rules.

**Simultaneous programmes:** A student appears in two programmes, but mode and timetable evidence are missing.  
**Outcome:** `REVIEW_REQUIRED`; apply the UGC guidance and relevant institution/programme rules after gathering facts.

### Evidence limitation

UGC simultaneous-programme guidance does not settle every transfer, withdrawal or course-change case. The relevant authority and documentary process must be established for the institution type.

### Effect on the system

Use effective-dated enrolment states such as `ACTIVE`, `WITHDRAWN`, `TRANSFERRED` and `COMPLETED`, retaining evidence and authority for every change. These are proposed data fields, not a claim that all institutions use identical status labels.

## Research question 6 — Which cases should pass, fail or require review, and who has authority to resolve them?

### Finding

The system should separate deterministic data-quality checks from admission-policy decisions. It can automatically detect missing fields, duplicate rows and arithmetic discrepancies. It should not automatically declare misconduct based on a repeated identity or make unsupported legal determinations about category eligibility.

The competent decision-maker depends on the issue. Institutions may correct their submitted data through an authorized workflow; changes to official approval capacity or disputed regulatory interpretations require the relevant competent authority.

### Outcome matrix

| Condition | Proposed outcome | Reason | Resolution route |
|---|---|---|---|
| Required field missing | `INCOMPLETE` | Record cannot be fully evaluated | Authorized institution user corrects submission |
| Duplicate row in same upload | Data-quality failure | Prevent duplicate ingestion | Institution corrects file; system logs event |
| APAAR format invalid | Data-quality failure/correction request | Identifier fails format check | Institution corrects; identity verification remains separate |
| APAAR verification service unavailable | `PENDING_VERIFICATION` | No authoritative response | Retry or use approved fallback |
| Same APAAR ID at two institutions | `WARNING` / `REVIEW_REQUIRED` | Multiple enrolment, stale status or permitted simultaneous study may explain it | Authorized admission/institution authority |
| Regular admissions exceed verified intake | `APPARENT_EXCESS` | Arithmetic suggests capacity issue | Competent authority reviews approval and exceptions |
| Category evidence missing | `INCOMPLETE` / `REVIEW_REQUIRED` | Eligibility cannot be established | Authorized admission authority |
| Category count appears above verified limit | `APPARENT_EXCESS` / `REVIEW_REQUIRED` | Potential breach of applicable ceiling | Competent authority verifies facts and policy scope |
| Approval missing/conflicting | `REVIEW_REQUIRED` | Capacity cannot be established reliably | AICTE or authority responsible for the approval |
| Transfer/withdrawal disputed | `REVIEW_REQUIRED` | Active status/count may be wrong | Authorized institution/university authority |
| Policy exception unclear | `REVIEW_REQUIRED` | Rule cannot be applied confidently | Competent regulatory/admission authority |
| Authorized reviewer resolves case | `RESOLVED_BY_AUTHORITY` | Decision and evidence are recorded | Named authorized reviewer |

### Rule `PRA-R16` — Decision and escalation boundary

- **Condition:** Each result must be traceable to a rule and evidence.
- **Inputs:** Record, rule version, approval version, calculation, source evidence and result.
- **Action:** Generate an explainable result and escalate unresolved policy questions.
- **Outcome:** A result such as `PASS_DATA_CHECK`, `INCOMPLETE`, `WARNING`, `APPARENT_EXCESS` or `REVIEW_REQUIRED`.
- **Exception:** Do not produce a definitive failure when rule scope, inputs or exceptions are unverified.
- **Source:** Applicable AICTE/UGC provisions and proposed project governance.
- **Scope:** All admission validation rules.

### Audit requirements

Store rule ID/version, official source/clause, academic year, institution/course and approval record, inputs/calculation, flag reason, timestamp, submitting institution, reviewer role and resolution evidence. Preserve old values and outcomes when a correction is made.

### Evidence limitation

The outcome vocabulary and escalation workflow are proposals. They need team review and alignment with actual authority and correction procedures.

### Effect on the system

Every flag must explain why the admission was flagged and which applicable rule supports it. A warning is not a confirmed violation.

## Worked scenarios (fictional)

These scenarios illustrate proposed logic. They do not establish legal outcomes for real students. Each must be tied to the exact verified rule before production use.

| ID | Scenario | Expected outcome | Reasoning |
|---|---|---|---|
| `PRA-S01` | Current approval matches course/year; regular admissions are within intake | `PASS_DATA_CHECK` | Count is within capacity for this check |
| `PRA-S02` | Regular admissions exceed verified approved intake | `APPARENT_EXCESS` | Investigate approval and applicable exceptions |
| `PRA-S03` | Supernumerary admission has required evidence and authorization | Category check may pass | Check category-specific ceiling and all conditions |
| `PRA-S04` | Supernumerary admission has no required authorization evidence | `REVIEW_REQUIRED` | Category cannot be assumed authorized |
| `PRA-S05` | Same student row occurs twice in one upload | Data-quality failure | Prevent duplicate ingestion |
| `PRA-S06` | Same APAAR ID active at two physical-mode institutions; timing/status unknown | `REVIEW_REQUIRED` | More evidence needed; no automatic fraud conclusion |
| `PRA-S07` | Same APAAR ID in physical and recognized ODL/online programmes | No automatic duplicate rejection | Apply current UGC and recognition rules |
| `PRA-S08` | APAAR ID missing | `INCOMPLETE` | Request correction or formally authorized exception handling |
| `PRA-S09` | APAAR format looks plausible but verification service is unavailable | `PENDING_VERIFICATION` | Format is not identity verification |
| `PRA-S10` | Declared OCI status conflicts with recorded seat category | `REVIEW_REQUIRED` | Check status evidence and applicable rule |
| `PRA-S11` | Category-specific ceiling appears exceeded | `APPARENT_EXCESS` / `REVIEW_REQUIRED` | Confirm clause, denominator, category counts and exceptions |
| `PRA-S12` | Transfer reported but previous institution still reports active enrolment | `REVIEW_REQUIRED` | Verify transfer and effective date |
| `PRA-S13` | Withdrawal reported but record remains active | `REVIEW_REQUIRED` | Verify withdrawal date and recalculate counts |
| `PRA-S14` | Student changes from Course A to Course B | `REVIEW_REQUIRED` until authorized | Validate change and both programme records |
| `PRA-S15` | Only previous year's approval is available for a new admission year | `REVIEW_REQUIRED` | Do not assume previous capacity carries forward |

## Questions requiring official clarification

| Question | Why it matters | Next action |
|---|---|---|
| Which authorized interface provides current institution/course/year approvals and amendments? | Establishes capacity source | Check official technical documentation or ask through an authorized channel |
| Which current category provisions apply to NRI, OCI and Foreign Nationals for each programme? | Prevents incorrect limits/eligibility | Extract exact clauses and amendments |
| What lateral-entry rule and any combined ceiling apply to each relevant programme/year? | Prevents category rules being mixed | Verify exact scope and denominator |
| What evidence is required for category-status verification? | Determines automated validation capability | Check applicable official category provisions |
| Who may correct uploaded admission/withdrawal records? | Defines correction workflow | Confirm with competent authority and institutional users |
| Who resolves conflicts between institution data and official approval orders? | Defines escalation | Confirm authority for each order type |
| What happens when APAAR validation is unavailable or an ID is missing? | Prevents fabricated verification outcomes | Confirm authorized policy and fallback |
| Which amendments/corrigenda affect the relevant academic year? | Ensures currency | Review official notices and date each rule |





**Current status:** Initial research structure drafted. Not yet fully verified or human-reviewed.
