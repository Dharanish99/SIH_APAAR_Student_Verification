# Pranav contribution reconciliation

AI-authored reconciliation on 2026-10-27 IST. This review distinguishes Pranav's incoming repository contribution from subsequent AI evidence work. It is not human peer review, regulator approval or field validation.

## What was received and preserved

The agent's initial checkout at `5ee5d57` contained workstream templates. A pre-publication fetch later revealed Pranav's October 26 contribution, committed after that baseline: findings `5aaa9a8`, progress `f938d15`, sources `0d12323`. The earlier description of an unfilled workstream was accurate only for the agent's baseline, not the later repository history.

The lead agent preserved [original findings](original-2026-10-26/findings.md), [original progress](original-2026-10-26/progress.md), [original sources](original-2026-10-26/sources.csv) and [provenance](original-2026-10-26/PROVENANCE.md). This reconciliation does not edit those originals. All three incoming research files were read in full. They contain answers to six questions, 16 preliminary rules, 15 fictional scenarios, four source starting points, an approval/correction proposal and explicit unresolved questions. Their caution about unverified amendments, actual approvals and API availability is retained.

The current [full findings](findings-2026-10-26.md), [14-rule catalogue](rule-catalogue.md), [22 worked cases](worked-cases.md) and evidence checks are AI-authored supplements, reconciled against that contribution. The 15 original scenarios remain attributable to Pranav; the 22 expanded cases are separately labelled AI-authored. Overlapping cases are not 37 independent tests, and none was an executed product test.

## Retained contribution by research question

| Original contribution | Consolidated treatment |
|---|---|
| Q1: institution/course/year EoA, revision history, no institution overwrite of official capacity | Retained in PRA-F01, POL-01/02 and authority/correction proposal. Reopened GJUST corrigendum adds concrete evidence. Valid multi-year intervals are explicitly allowed. |
| Q2: separate regular and authorised extra categories; no universal intake-plus-15% formula | Retained in PRA-F02/04/05 and POL-02 through POL-06. Clarified that NRI consumes base intake in the inspected base edition; current applicability remains unconfirmed. |
| Q3: declared status, evidence, seat used and route are different fields | Retained in field dictionary and POL-12. Maharashtra's scoped OCI exception supplies a worked example without creating a national entitlement. |
| Q4: verify clauses, amendments, scope and combined ceilings before coding | Retained as activation prerequisites and unresolved dependencies. Actual PDF passages supplement the original listing-only citations. |
| Q5: lifecycle history, transfer/withdrawal/course change, no duplicate-as-fraud rule | Retained in POL-07 through POL-11. UGC modification and scoped Maharashtra provisions provide more exact expectations. |
| Q6: separate data errors from policy adjudication; traceable authority/escalation/audit | Retained throughout the outcome model and correction proposal. Technical administrator access does not itself confer legal authority. |

## Rule mapping - all 16 preliminary rules

IDs below identify separate catalogues, not silently renamed legal provisions. The current POL rules remain proposed evaluation designs.

| Original rule | Current location | Retention or qualification |
|---|---|---|
| PRA-R01 approval resolution | POL-01/02; C01-C03/C21 | Retained; missing policy becomes `POLICY_UNAVAILABLE` rather than an ambiguous successful check. |
| PRA-R02 capacity dimensions | POL-02 through POL-06 | Retained; a category may consume base capacity, so regular-versus-additional must not misclassify NRI. |
| PRA-R03 apparent excess | POL-02; C02 | Retained as `POTENTIAL_CAPACITY_BREACH`; no automatic individual admission cancellation. |
| PRA-R04 supernumerary authority | POL-04/05/06; C16/C18/C20 | Retained; separate pool and evidence per provision. |
| PRA-R05 status/category consistency | POL-12; C17 | Retained; OCI plus an ordinary candidature is not inherently inconsistent. |
| PRA-R06 NRI | POL-03; C15 | Base-edition relationship inspected; live percentage still not activated. |
| PRA-R07 OCI | POL-12; C17 | State example added; no universal OCI rule inferred. |
| PRA-R08 Foreign National | POL-04; C16 | Official UGC guidance preserves statutory-body rules; no generic technical entitlement. |
| PRA-R09 lateral entry | POL-05; C18/C19 | Conditional arithmetic and vacancy provenance added; current pack remains required. |
| PRA-R10 combined ceilings | POL-04/05 and required rule inputs | Retained as a necessary pack-specific dependency. Complete current combined ceilings are still unresolved, not falsely marked researched nationally. |
| PRA-R11 other categories | POL-06; C20 | Retained as separate named pools, not one interchangeable supernumerary allowance. |
| PRA-R12 transfers | POL-10; C11-C13 | Scoped Maharashtra evidence added; missing authority cannot silently create or close an active seat. |
| PRA-R13 withdrawals | POL-11; C14/C19 | Retained; legal effect can precede institution acknowledgement. |
| PRA-R14 course changes | POL-10/07; C04/C11/C12 | Retained; correct course approval and lifecycle revisions are needed. |
| PRA-R15 simultaneous programmes | POL-08/09; C06-C10 | Official 2025 text confirms permitted combinations and historical conditions; no repeated-ID verdict. |
| PRA-R16 decisions/escalation | Catalogue activation section; findings authority/correction proposal | Retained; changed labels clarify data versus policy versus reviewer states. |

## Scenario mapping - all 15 original cases

The archived cases remain available as original contributions even where an AI case expands only one aspect. No case is presented as a real student's outcome.

| Original case | Consolidated coverage | Result of reconciliation |
|---|---|---|
| PRA-S01 within intake | C01 | Same conditional pass, now labelled `WITHIN_CONFIGURED_RULE`. |
| PRA-S02 excess intake | C02 | Same review-before-consequence boundary. |
| PRA-S03 authorised supernumerary | C18; POL-04/06 | C18 supplies a route-specific conditional arithmetic example. The original generic authorised-category scenario remains retained; it is not evidence that all pools are interchangeable. |
| PRA-S04 missing extra-seat authority | C16 | Preserve reported record; policy/authority incomplete. |
| PRA-S05 duplicate row | C04; POL-07 | Prevent duplicate ingestion/counting; exact replay may be accepted as a no-op rather than rejecting a whole batch. |
| PRA-S06 physical-mode timings unknown | C06/C07/C10; POL-08 | Unknown timing remains review-required; known compatible/conflicting schedules are separated. |
| PRA-S07 physical plus recognised online | C08 | Same no-automatic-rejection rule with recognition/session conditions. |
| PRA-S08 missing APAAR | C22 | Keep local record and pending linkage; no blanket admission exclusion. |
| PRA-S09 service unavailable | C22 and integration handoff | Retained as provider-pending, with an explicit outage variant below; plausible format is not verification. |
| PRA-S10 OCI/category discrepancy | C17 | Review actual entitlement; the mere coexistence of OCI status and ordinary candidature is not a contradiction. |
| PRA-S11 category ceiling exceeded | C19; POL-04/05/06 | C19 illustrates a lateral allowance only. Retain original generic category test pending that category's verified cap and denominator. |
| PRA-S12 transfer with old active record | C13 | Pending lifecycle evidence; no fraud label. |
| PRA-S13 withdrawal still active | C14/C19 | Verify legally effective event; don't make institution acknowledgement an invented extra condition. |
| PRA-S14 course change | C04/C11/C12 | Versioned correction plus applicable course-change authority. |
| PRA-S15 prior-year approval | C03 | Check effective coverage: prior issue date alone does not invalidate a multi-year approval. |

**Retained outage variant of PRA-S09:** when an identity-linkage provider is unavailable, keep previously supported facts and their timestamps, set current linkage to pending/unavailable, and apply the documented retry or lawful fallback process. Do not substitute synthetic success or a format-only identity verdict. This preserves a specific original case that C22 references more generally; it is not counted as a twenty-third newly executed test.

## Source mapping and verification status

Original IDs are retained as four attributed historical rows in [sources.csv](sources.csv); original reported access dates remain October 26. Their current verification/limitations cells append the October 27 reconciliation. The archived CSV preserves the exact original entries.

| Original ID | Current follow-up | What the evidence establishes |
|---|---|---|
| PRA-001 APH official route | PRA-101/102; PRA-108 approval example | Official route failure is recorded separately from the inspected institution mirror and recipient-hosted EoA. Current complete amendment chain remains unknown. |
| PRA-002 UGC KeyInitiative pointer | PRA-105/106 | The original pointer remains discovery evidence; the actual international-student PDF was inspected through the official guideline index. The KeyInitiative route itself was not newly relied on. |
| PRA-003 UGC guidelines listing | PRA-103/104/105 | Original and amended PDFs read together; 2025 amended guideline controls the changed historical provision. |
| PRA-004 project source/standards guide | PRA-110 | Local project source guide and research standards reread; they govern research method, not admission law. |

## Points corrected or qualified

1. **Attribution:** Pranav's contribution existed on the incoming branch and is retained. Describing the entire workstream as an unfilled human assignment is no longer accurate. Human ownership and contribution do not imply human approval of the AI supplement.
2. **Outcome vocabulary:** Original `PASS_DATA_CHECK`, `APPARENT_EXCESS`, `INCOMPLETE` and `PENDING_VERIFICATION` remain meaningful proposals. Current capacity outputs use `WITHIN_CONFIGURED_RULE` and `POTENTIAL_CAPACITY_BREACH`; missing data/linkage is a separate status, and missing policy is `POLICY_UNAVAILABLE`. There is no single global legal-validity badge.
3. **Withdrawal and previous-year documents:** Original cautions are retained, with the effective-event and multi-year-approval clarifications described above. These refine the examples without asserting the human draft claimed a universal delay or ban.
4. **Duplicate-row handling:** Original prevention intent is retained. A harmless exact replay can be an idempotent no-op, while conflicting/stale revisions require correction. Neither is a second student.
5. **Evidence strength:** The original register accurately marked policy extraction and current applicability as pending. Locating a primary-source listing is not the same as verifying its operative clauses; the AI supplement supplies inspected passages with residual limitations.
6. **Teach-back discrepancy:** Original progress reports a seven-minute teach-back outline, but no such outline was found in the three preserved research files. The six-question draft can support a future teach-back, but preparation/delivery of that missing outline is not independently evidenced. No performed teach-back or reviewer approval is recorded.

## Completeness and remaining work

All six question sections, 16 preliminary rules, 15 original scenarios, four source rows, the authority/correction proposal, audit requirements and eight official-clarification questions were assessed. None requires changing the preferred versioned-rule/reviewer architecture. The current work supplements the original research rather than claiming it was absent or independently validated by multiple reviewers.

Still external: complete applicable AICTE amendments and combined ceilings, actual pilot approval/affiliation/seat matrix, precise category evidence, competent authority and correction procedures, missing-APAAR/foreign-student provider pathways, user interviews and a genuine policy review. The human draft and AI supplement agree these must not be invented. The source/fixture/link/hash checks recorded in [progress](progress.md) establish document consistency only.
