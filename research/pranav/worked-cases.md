# Worked policy cases - fictional reasoning fixtures

AI-authored for the 2026-10-26 research round; completed 2026-10-27 IST. All students, institutions, dates of student events and capacities below are invented. `FIC-Pxx` is a fictional internal key, never an APAAR number. These are expected outcomes for a future implementation, not executed tests, human adjudications or evidence of fraud-detection accuracy.

Read the [rule catalogue](rule-catalogue.md) and [source register](sources.csv). Unless stated otherwise, assume the fictional policy administrator has confirmed the exact institution/campus/course/year approval, affiliation, effective rule pack and counting scope. This assumption is for arithmetic examples only: no production policy pack has been approved in this project. A result applies only to the stated check; `WITHIN_CONFIGURED_RULE` is not an identity, admission-legality or credential-authenticity verdict.

## C01 - Regular capacity at the boundary

**Input:** Fictional Course A has a confirmed first-year base capacity of 60 for 2026-27. It reports 60 distinct, active, in-scope admissions; no replay rows or additional pools occur.

**Expected:** `WITHIN_CONFIGURED_RULE` for POL-02: 60 <= 60. Explain the numerator, denominator, snapshot time and approval revision. Identity, eligibility and other checks remain independent. **Basis:** PRA-102 definition 10; POL-01/02. **Owner:** institution approver supplies the counted facts.

## C02 - One reported admission over capacity

**Input:** C01 plus one distinct in-scope admission; no applicable extra pool or corrigendum is evidenced.

**Expected:** `POTENTIAL_CAPACITY_BREACH`, 61 > 60 by one. Preserve all 61 records, open an institution-level reconciliation case and request the applicable approval or correction. Do not select the last student for automatic cancellation. **Basis:** PRA-102 definition 10; POL-02. **Owner:** competent authority assesses any admission consequence.

## C03 - Last year's approval supplied

**Input:** 60 admissions in 2026-27; only a document whose approval interval ends in 2025-26 is supplied.

**Expected:** `POLICY_UNAVAILABLE`, not pass and not over-intake. Obtain a document whose approved interval covers the target year, including a valid multi-year approval if applicable, and resolve amendments. **Basis:** PRA-102 section 2.25; PRA-108; POL-01. **Owner:** authorised policy administrator.

## C04 - Replayed file and later correction

**Input:** An import repeats the same 60 business records with unchanged canonical values under a new upload token. A subsequent row changes FIC-P04's course and cites current record revision 3; stored revision is 4.

**Expected:** Replay is a no-op: count stays 60. The stale change is a `DATA_ERROR`/revision conflict, not a second admission or automatic overwrite. Request reconciliation against revision 4 and retain import provenance. **Basis:** POL-07, a design proposal rather than a legal clause. **Owner:** institution operator/approver.

## C05 - Impossible dates

**Input:** FIC-P05 has start date 2026-08-01 and withdrawal effective date 2026-07-15, with no explanation or correction record.

**Expected:** `DATA_ERROR` for inconsistent temporal input. Keep a pending row and request corrected source facts; do not silently exclude it to improve capacity totals. Disclose incomplete counts. **Basis:** proposed lifecycle validation in POL-07/11. **Owner:** institution approver. This is invalid data, not proof of invalid admission.

## C06 - Two physical programmes with compatible timings

**Input:** FIC-P06 has overlapping enrolment dates in two physical full-time non-PhD programmes. Confirmed class schedules are 08:00-11:00 and 14:00-17:00; applicable university mechanisms and council requirements are satisfied.

**Expected:** Initial identity collision is resolved as `WITHIN_CONFIGURED_RULE` for the concurrent-programme check, with evidence. **Basis:** PRA-103 guideline 1 and scope; POL-08. **Owner:** designated reviewer records the allowed combination. No fraud label or global one-enrolment-per-APAAR constraint.

## C07 - Physical programmes with conflicting timings

**Input:** C06, but classes are 09:00-13:00 and 12:00-16:00 on the same days, and the verified rule pack contains no applicable exception.

**Expected:** `REVIEW_REQUIRED` with a documented timing conflict: the stated combination does not satisfy guideline 1's condition. Refer to the competent authority and offer correction/dispute handling; the application does not adjudicate misconduct or cancel either record. **Basis:** PRA-103 guideline 1; POL-08.

## C08 - Physical plus recognised online programme

**Input:** FIC-P08 is in one physical programme and one online degree; programme-specific recognition for the relevant admission session and applicable council/university conditions are documented.

**Expected:** `WITHIN_CONFIGURED_RULE` for this combination. If recognition is merely asserted or recognition applies to a different session, change outcome to `REVIEW_REQUIRED`. **Basis:** PRA-103 guidelines 2-4; POL-08. **Owner:** designated reviewer checks recognition scope, not just a university name.

## C09 - Historical dual programmes before the original guideline

**Input:** FIC-P09 completed two programmes begun before April 2022. Evidence of the historical university rules and applicable UGC/council/DEC/DEB requirements is incomplete.

**Expected:** `REVIEW_REQUIRED`; no date-only rejection. The 2025 amended provision allows qualifying earlier programmes subject to stated conditions; obtain that evidence before a conclusion. **Basis:** PRA-103 amended guideline 5; PRA-104 retained only for supersession history; POL-09.

## C10 - PhD or unknown programme mode

**Input:** FIC-P10 has two active records and one is a PhD; alternatively the mode of one record is unknown.

**Expected:** PhD: `POLICY_UNAVAILABLE` for applying this particular simultaneous-programme guidance; seek the applicable rules. Unknown mode: `REVIEW_REQUIRED` for missing inputs. Neither state establishes that the student violated policy. **Basis:** PRA-103 final scope; POL-08.

## C11 - Transfer with sufficient applicable evidence

**Input:** A fictional Maharashtra student seeks an eligible transfer after the completed year, between permitted institution types, outside the same-year prohibition. Required result/eligibility, NOCs, vacancy, DTE approval and final authority approval are evidenced; no restricted supernumerary pool applies. Old and new enrolment effective intervals are reconciled.

**Expected:** Resolve the transfer case and count each enrolment in its applicable interval; preserve history. **Basis:** PRA-109 section 16, PDF pp14-15; POL-10. **Owner:** the stated competent authorities, not a platform administrator acting independently.

## C12 - Same-academic-year transfer request

**Input:** Under the same verified Maharashtra scope, FIC-P12 has just entered third year and requests a different course/institution during that academic year; no overriding order is supplied.

**Expected:** `REVIEW_REQUIRED` with the current restriction identified. Do not grant it automatically or use the superseded rule that mentioned only first/second year. **Basis:** PRA-109 July 2 amendment clause 7(1), PDF p12; POL-10. **Owner:** competent authority considers any claimed exception.

## C13 - Transfer waiting for approval

**Input:** FIC-P13 has a new institution's offer but no required competent approval and the old record remains active.

**Expected:** `REVIEW_REQUIRED`; new event stays a pending transition, not a silently confirmed second active seat. Do not automatically close the old record or classify the student as fraudulent. **Basis:** PRA-109 section 16; POL-10. **Owner:** institutions supply evidence, competent authority resolves.

## C14 - Maharashtra online cancellation with missing signed copy

**Input:** An authenticated in-scope online cancellation was submitted before the applicable cutoff; the institute has not received the signed printout. The cancellation event itself is authoritative.

**Expected:** Under the inspected section 15(a), treat admission as cancelled from the online event; do not keep it active solely because the signed copy is missing. Preserve historic snapshots and recompute the applicable current allocation view. Refund/document-return processing has separate conditions. **Basis:** PRA-109 PDF p13; POL-11. An unverified email/request does not substitute for this event.

## C15 - NRI seats consume base capacity

**Input:** For a fictional historical pack where PRA-102 section 2.8 is confirmed applicable, approved intake is 60, NRI approval exists and 3 seats are allocated to NRI within intake. There are 57 other base-pool admissions plus 3 NRI admissions.

**Expected:** Base count is 60, not 63; `WITHIN_CONFIGURED_RULE`. With 60 other base admissions plus 3 NRI, report 63 > 60. **Basis:** PRA-102 section 2.8; POL-03. For an unconfirmed 2026-27 pack, return `POLICY_UNAVAILABLE`; the historical 5% is not activated here.

## C16 - Generic international percentage offered as authority

**Input:** Fictional Technical Course B has 60 base seats. An operator adds 15 extra seats by citing UGC's 25% wording, but has no applicable current technical-body rule/course approval.

**Expected:** `POLICY_UNAVAILABLE` for that pool, retaining admissions as reported facts. Do not infer entitlement from 60 x 25%. **Basis:** PRA-106 guidelines 2/6/7; PRA-108 approval flags; POL-04. **Owner:** policy administrator obtains current authority; the same caution applies to a stale 15% constant.

## C17 - OCI status with a scoped candidature decision

**Input:** In the Maharashtra scope, FIC-P17 obtained OCI before 2021-03-04, passed 10th and 10+2 in Maharashtra, and meets the ten-year residence condition. The competent authority grants the relevant Maharashtra candidature.

**Expected:** Record OCI as status and the granted candidature/seat pool separately; do not force an international pool. Eligibility conditions and the authority decision must be evidenced. **Basis:** PRA-109 amendment clause 3, PDF p11; POL-12. Different dates or missing schooling/residence proof require review, not inferred entitlement.

## C18 - Lateral entry with verified vacancies

**Input:** A fictional historical pack confirms PRA-102 section 6.13 applies: intake 60, applicable additional allowance 6, and 4 evidenced unfilled first-year seats. Eligible lateral admissions total 10; no no-admission or other restriction applies.

**Expected:** 6 + 4 = 10 for this route-specific calculation; `WITHIN_CONFIGURED_RULE`. Do not compare these 10 with an unrelated total across every study year. **Basis:** PRA-102 section 6.13(a-f); POL-05. Current-year applicability is assumed only for the fixture, not established nationally.

## C19 - Withdrawal counted twice as a lateral vacancy

**Input:** C18's 4 vacancies already include a withdrawn student's seat. A spreadsheet adds that withdrawal again and claims 11 available lateral seats; provenance shows only 4 distinct vacancies.

**Expected:** `DATA_ERROR` for duplicate vacancy evidence; reconciled allowance remains 10. The eleventh admission triggers `POTENTIAL_CAPACITY_BREACH` only once the applicable cap and facts are confirmed. **Basis:** POL-05/07; PRA-102 section 6.13. Never sum historical withdrawal rows without distinct seat/cohort provenance.

## C20 - Supernumerary/TFW transfer restriction

**Input:** A fictional student admitted under a supernumerary quota seeks transfer under the inspected Maharashtra rules. An operator treats all categories as ordinary seats.

**Expected:** `REVIEW_REQUIRED` with section 16(3)'s restriction, unless a competent overriding authority is evidenced. Keep the original admission record; do not transfer the entitlement automatically. **Basis:** PRA-109 PDF p15; POL-06/10. Base APH section 6.42 also has TFW-specific conditions, but is not a substitute for confirming the current pack.

## C21 - Corrected approval changes the result

**Input:** Fictional EoA v1 approves 60, v2 explicitly supersedes it for the relevant course/year and approves 90; reported count is 70. Dates and effective scope are confirmed.

**Expected:** Preserve the earlier 70 > 60 finding and its evidence, then record a new 70 <= 90 evaluation under v2; resolve the old capacity alert with a reason. Do not rewrite history or assume every corrigendum is retroactive. **Basis:** PRA-108 demonstrates a real corrigendum chain; numbers here are fictional; POL-01/02.

## C22 - Missing APAAR and mistaken certificate identifier

**Input:** FIC-P22 has a legitimate institution-local record with provider linkage pending. The certificate template proposes putting an AICTE enrolment number into the APAAR field because the two identifiers are assumed equivalent.

**Expected:** Preserve the record with a visible pending linkage reason and correction path; do not infer ineligibility. Reject the identifier substitution as `DATA_ERROR`. The supplied problem's certificate-display objective needs an authorised awarding-body workflow and privacy review. **Basis:** PRA-102 Annexure 6 sections 6.8/6.9; POL-14; [integration findings](../sudhan/findings.md). Admission exception/APAAR issuance is still a provider-policy dependency.

## Review protocol

For future acceptance testing, instantiate each fixture with synthetic data and a specified rule revision; record observed versus expected outcome separately. Check counterfactuals (cap 59/60/61; timing known/unknown; approval present/missing; duplicate/revision; old/new effective date). These documents do not claim that such a rule engine has been built or these tests executed. Human policy review, jurisdiction selection and current amendment completeness remain pending.
