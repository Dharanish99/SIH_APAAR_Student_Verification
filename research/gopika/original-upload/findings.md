# Research Findings — Gopika

**Workstream:** Institutional workflows, user needs and existing solutions  
**Status:** Preliminary desk research; claim-level verification and teammate review pending  
**Last updated:** 26 October 2026

## 1. Research question and scope

This research looks at publicly documented systems and workflows related to academic identity, student-management/admission processes, academic-award verification, and higher-education reporting. The goal is to understand what existing systems appear to cover and identify questions the SIH26263 project should investigate before proposing a solution.

This is preliminary desk research, not a complete evaluation of every institution or product.

## 2. How the systems work — in my own words

- **APAAR:** Public information describes APAAR as an academic identity framework associated with a student’s academic records. The documentation is useful for understanding the purpose of academic identity, but it does not by itself prove that our project has permission to use a live API or access individual student records.
- **Samarth Student Portal:** The reviewed documentation describes student-management functions, including adding student records and importing student information using an Excel file. These are documented features of the described system, not proof that every institution uses the same workflow.
- **Samarth admissions documentation:** The example workflow includes steps such as registration, entering profile and academic details, uploading documents, reviewing information, and submitting an application. Exact steps depend on the particular implementation.
- **National Academic Depository (NAD):** Its public information describes services related to academic awards and their verification. Award verification should not automatically be treated as the same task as admission approval or resolving a student's identity mismatch.
- **AISHE:** The Web DCF is associated with higher-education data collection and reporting. It is useful context for institutional reporting, but it is not the same as an individual student's admission or award-verification workflow.

## 3. Preliminary findings and evidence

| ID | Preliminary finding | Evidence/source to check | Confidence and limitation |
|---|---|---|---|
| F-01 | Academic identity and access to academic records are related, but documentation about an identity framework does not establish that our project can access its API. | GOP-001, GOP-002 | Supported as a scope distinction; live access has not been tested. |
| F-02 | Student-management systems may support both individual record entry and bulk import workflows. | GOP-003 | Applies to the reviewed Samarth documentation; do not generalise to all institutions. |
| F-03 | Admission workflows can involve multiple stages, including registration, details, documents, review, and submission. | GOP-004 | Implementation-specific; exact steps may differ. |
| F-04 | Academic-award verification is a distinct function from admission decisions and student identity correction. | GOP-005, GOP-006, GOP-007 | Useful distinction based on the documented purposes; exact institutional procedures need confirmation. |
| F-05 | Higher-education reporting is another separate workflow from an individual student's record verification. | GOP-008 | The source provides context about reporting, not evidence about every institution's process. |
| F-06 | The reviewed sources do not establish a universal workflow, measured staff workload, or average correction time. | GOP-001 to GOP-008 | Absence of evidence in the reviewed documents is not proof that such evidence does not exist elsewhere. |
| F-07 | The SIH problem statement should be checked against the official event/problem-statement material before making precise claims about requirements. | GOP-009 | The currently registered link is a third-party reference and should not be treated as the authoritative source. |

**Evidence note:** The source IDs above are intended to match `research/gopika/sources.csv`. Verify that each source entry exists, is accurate, and supports the related claim before treating the findings as final.

## 4. Worked cases / possible test scenarios

The following are proposed synthetic scenarios for discussion and testing. They are not real student cases, and they have not been executed against a live system.

1. **Matching record:** The submitted identity details match the record available to an authorised reviewer. Expected design question: what evidence and status should be shown?
2. **Possible mismatch:** A name or date field differs between two records. Expected design question: how can the system flag the discrepancy without automatically labelling it fraud?
3. **Missing award information:** The requested academic award cannot be found in the information available to the workflow. Expected design question: should the result be “not found,” “unable to verify,” or another clearly defined status rather than an unsupported rejection?
4. **Unavailable integration:** A connected service or API is unavailable. Expected design question: how should the system explain the limitation and provide a safe manual fallback?
5. **Insufficient permission:** A user does not have permission to access a record. Expected design question: how should the system deny access and record the attempt without exposing private data?

These scenarios need review against the actual project requirements and applicable policies.

## 5. Implications for the SIH26263 project

- Define the exact verification problem before designing a broad all-in-one student platform.
- Keep academic identity, admission/enrolment, academic-award verification, and institutional reporting as separate concepts.
- Make any external integration conditional on confirmed authorisation, documented interfaces, and appropriate access controls.
- Use clear outcomes such as “matched,” “possible mismatch,” “unable to verify,” or “manual review required,” if they fit the agreed requirements.
- Do not equate a mismatch or missing record with fraud.
- Minimise personal data, restrict access by role, and consider logging, retention, and secure handling before using real records.
- Use synthetic records during early testing and clearly distinguish a proposed design from a tested implementation.

## 6. Alternatives and preliminary recommendation

Possible approaches to compare:

1. **Manual review supported by a checklist:** simplest fallback; can be slower and depends on consistent staff practice.
2. **A workflow that organises evidence and flags discrepancies:** may improve consistency, but requires clear rules and human review for uncertain cases.
3. **Integration with an authorised external service:** may reduce repeated data entry if an appropriate interface and permission are available; access and technical feasibility are not yet confirmed.
4. **Bulk-file processing:** may help when institutions already use spreadsheet-based imports, but requires validation, access controls, error reporting, and careful handling of personal information.

**Preliminary recommendation:** Start by defining one narrow verification use case and its authorised data sources. Prototype with synthetic data, document a manual fallback, and compare options against accuracy, usability, privacy, accessibility, cost, and implementation feasibility. Do not claim measured benefits until testing provides evidence.

## 7. Unknowns and blockers

| Unknown / blocker | Why it matters | Suggested next step |
|---|---|---|
| Exact workflow and user roles intended by the problem statement | Determines the correct scope | Compare this draft with the official SIH26263 statement and team decisions. |
| Whether an authorised API or integration is available | Determines technical feasibility | Check official documentation and obtain permission from the responsible organisation. |
| Actual staff pain points and time spent | Needed to justify impact claims | Ask the team to arrange appropriate stakeholder research; do not invent measurements. |
| Rules for resolving mismatches | Affects fairness and correctness | Agree on status definitions and a human-review path. |
| Privacy, retention, and access requirements | Protects sensitive student information | Confirm applicable institutional and legal requirements before using real data. |
| Whether source details support every claim | Prevents inaccurate conclusions | Verify each source entry and record access date and limitations. |
| Official status of the third-party SIH26263 link | Affects reliability of project requirements | Replace or corroborate it with the official problem statement. |

## 8. Handoff notes for teammates

- **Integration / technical work:** APAAR-related public information does not establish live API access for our project. Treat any integration as conditional until authorised access and interface details are confirmed; provide a documented fallback.
- **Workflow / rules work:** Keep identity mismatch, admission/enrolment decisions, and academic-award checks distinct. A mismatch alone should not be treated as fraud; define statuses and a human-review route.
- **Implementation / testing work:** Existing documentation describes student entry and bulk-import patterns in the reviewed Samarth materials. Check whether the proposed workflow duplicates existing functionality, then test synthetic cases. Do not state that tests passed unless they have actually been run.
- **Privacy / security work:** Plan for data minimisation, role-based access, logging, and retention rules. Avoid real student data in prototypes unless the team has confirmed appropriate safeguards and authorisation.
- **Research / presentation work:** The reviewed systems have different purposes. Focus the project on a specific verification gap, verify the official problem statement, and avoid unsupported claims about universal pain points or quantified benefits.

## 9. Review and quality check

- [ ] Confirm the official SIH26263 problem statement and align the scope with it.
- [ ] Open and verify every source in `sources.csv`.
- [ ] Ensure the source IDs used here match the source register.
- [ ] Check that each factual claim is supported by the cited source.
- [ ] Keep assumptions, proposals, and unknowns labelled as such.
- [ ] Record the actual date each source was accessed; do not use a guessed date.
- [ ] Ask teammates to review and record their real feedback.
- [ ] Update this file when verification or testing is completed.

## Research limitations

This draft is based on publicly available documentation. No interviews, institutional observations, private-portal checks, real student records, or live API tests were conducted. The proposed scenarios have not been executed, and no teammate review has been recorded yet. These findings are preliminary and do not demonstrate measured benefits or universal institutional practices.
