# Design critique and decision record

Completed 2026-10-27. This records actual AI-agent exchanges during the separate innovator's synthesis. It does not record approval, review or acceptance by any human team member, institution, regulator or provider. The human ownership mapping remains unchanged.

## Proposed choice sent for critique

The innovator sent the lead, integration_finish and security_finish agents the SetuTrace direction: a correction-first institution evidence/reporting layer beside ERP/NAD; optional account-linked provider evidence; versioned findings and snapshots; student correction receipt; uniform institution receipts; restricted regulator matching. Four alternatives were proposed, including retaining a spreadsheet/checklist workflow when a product adds no net value.

## Feedback actually received and response

| ID / source | Critique received | Design response | Remaining evidence needed |
|---|---|---|---|
| DC01 / integration_finish | A new portal can duplicate ERP entry. Measure all correction, approval and student effort, not import speed. | Preserve stable source keys and field mappings; compare against improved spreadsheets; make total work a progression criterion. | Observed workflow and comparative task measurement |
| DC02 / integration_finish | Student, institution, provider and awarding body have different correction powers. A local case cannot fix an external source. | Separate dispute, enrolment, identity and award queues; show pending source correction; supersede evidence when source changes. | Actual contracts, responsible contacts and correction procedures |
| DC03 / integration_finish | A student without APAAR/DigiLocker must be able to inspect and dispute institution claims; disputed ID cannot be the only login route. | Institution-approved account/assisted route with independently established student-to-case binding. Missing linkage does not block capture. | Accessible identity/support design and misuse testing |
| DC04 / integration_finish | Local acceptance and export readiness are not official submission/readback. | Separate statuses; attribute manually attached receipts to their source/uploader; no government acknowledgement without evidence. | Authorised AICTE submission contract and receipt semantics |
| DC05 / integration_finish | v2.4 returns token-account evidence with no arbitrary-ID parameter and recommends one call. It returns broad fields; server-side projection is not established. | No bulk lookup or polling claim; optional adapter, payload assessment, minimal derived retention, unrelated fields discarded and raw responses excluded from logs. | Sponsor, exact scopes, testing permission, retry/refresh clarification |
| DC06 / security_finish | Uniformity must cover polling, dashboards, emails, timing, support and exports. Collision-only clarification reasons still leak. | No institution-visible match bit in any outward channel; restricted reviewer asks only about own supplied facts. | Repeated-probe/timing tests; residual inference and collusion assessment |
| DC07 / security_finish | Corrections need authenticated case binding, immutable revisions, appeal history and accountable reviewers; delayed acknowledgement must not override legal event time. | Separate effective/recorded times and source evidence; preserve history; explicitly honour the scoped Maharashtra cancellation event. | Current applicable policy pack and genuine policy review |
| DC08 / security_finish | Recipient, purpose, fields, revision and expiry must be rechecked at retrieval and queued-export execution; forwarded QR and stale badges are unsafe. | Recipient-bound online assertions, transactional revocation checks, no URL-only access; explain downloaded-copy limitation. | Revocation races, wrong-recipient and stale-status implementation tests |
| DC09 / lead policy handoff | Maharashtra section 15(a) makes the authenticated online cancellation effective irrespective of signed-copy receipt. | Corrected the generic approver model for that scoped legal event; no national extrapolation. | Pilot-specific applicability and overriding orders |

## Assumptions challenged by the innovator

1. **“A larger central database is the innovation.”** Rejected as the selection criterion. The proposed benefit is a reproducible correction trail; existing systems already perform substantial operational and award functions.
2. **“Provider integration must happen first.”** Rejected as an MVP dependency. Institution claims, policy explanations and correction ownership can be demonstrated with labelled fixtures. Live linkage remains a separate access gate.
3. **“More detected anomalies means a better service.”** Rejected. The reproduced statistical signal added ten labelled findings and ten false alerts; field review effort and harm must be measured before adding it.
4. **“Approval means every institutional action waits for staff.”** Qualified. A reviewer governs an assertion or correction, but cannot delay an already legally effective cancellation merely because internal acknowledgement is late.
5. **“Consent is one checkbox.”** Rejected. Reporting authority, provider permission and recipient-specific disclosure have separate purposes and evidence. Applicable law and commencement still need operator-specific review.
6. **“A student must create another account.”** Challenged. Institutional federation and assisted access should be evaluated first; the team must prove the proposed student view improves access without creating an exclusion barrier.
7. **“The research validates the product.”** Rejected. Source inspection and the sequential fictional model constrain a proposal; they do not establish adoption, database behaviour, field accuracy, legal approval or security.

## Decisions and revisit triggers

The evidence-layer option is a design recommendation only. Revisit it if total task effort is not lower than an improved checklist, source correction cannot be assigned, a current policy pack cannot be obtained, or institutions cannot lawfully support the proposed disclosure. Keep the simpler workflow as a valid outcome.

Use deterministic rules first; reconsider statistical triage only after representative held-out evaluation demonstrates incremental useful findings per review-hour with acceptable false-alert effects. Use a modular application and database-backed worker; introduce additional infrastructure only after measured limitations.

Before any real pilot, require an accountable operator, applicable purpose/retention/guardian decisions, current rule approval, institutional and provider permissions where relevant, and independent security review. No agent consensus satisfies those gates. Unresolved official SIH wording is separately tracked in the [verification note](official-problem-verification.md).

Evidence anchors: [integration review](../research/sudhan/integration-review.md), [privacy design](../research/sudhir/privacy-design.md), [security critique log](../research/sudhir/critique-log.md), [policy cases](../research/pranav/worked-cases.md), [synthetic reproduction](../research/dharanish/experiments/README.md). The final [solution report](solution-report.md) incorporates the responses above.

## Lead review of late incoming contributions

The final fetch discovered newer human-owned Pranav and Sudhir research. The specialists read the incoming files, preserved their useful foundations and reconciled overclaims against the current evidence. Neither identified a reversal of the selected concept. Their [policy reconciliation](../research/pranav/human-contribution-review.md) and [security reconciliation](../research/sudhir/human-contribution-review.md) record the details. This was a lead/specialist update after the independent innovator saved the report, not a claim that the innovator saw these later commits.
