# Research findings - Sudhir

**Workstream:** privacy, security, consent and credential verification. **Status:** AI desk research ready for human review. **Research round:** 2026-10-26 (Asia/Kolkata). **Completion recheck:** 2026-10-27. **Human reviewer/date:** pending.

The research recommends institution-attested, versioned records with separate provider evidence and narrowly authorised disclosure. Knowing an APAAR ID must not reveal student data or existence. The service must support correction without labelling every overlap or provider failure as fraud.

This is AI-authored assistance; it does not claim that Sudhir performed or approved it. [Original 2026-10-23 templates](original-2026-10-23/findings.md) are preserved. Their unfinished prompts are historical, not current conclusions.

## Research outputs

| Output | Coverage / evidence boundary |
|---|---|
| [Research supplement](ai-research-2026-10-26.md) | Findings, alternatives and seven fictional walkthroughs; no executed system tests. |
| [Permission and data design](privacy-design.md) | Roles, tenant boundaries, field inventory, sharing journey, issuer/status lifecycle and pilot gates. Controls proposed. |
| [Legal status](legal-status.md) | Primary staged commencement/corrections and CERT-In directions; deployment applicability and full SPDI verification remain open. |
| [Threat model](threat-model.md) | Thirteen abuse cases, future checks, owners and residual risks. No penetration test or implementation. |
| [Source register](sources.csv) | SUH-101 through SUH-116, with primary URLs, inspected sections, access dates and retrieval limits. |
| [AI critique](critique-log.md) | Integration/policy critique and security handoffs; human review pending. |

## Supported conclusions and design consequences

- **Verified legal-text fact:** the main DPDP processing/consent/child/rights duties remain in the future stage on the research/recheck dates (SUH-101 to SUH-105). Plan for them; assess current duties and actual operator roles before real records.
- **Verified technical documentation:** requester v2.4's APAAR evidence concerns the authorised token account, not arbitrary-ID registry lookup. No live access or exact permitted APAAR scope is established (SUH-114).
- **Documented standards:** issuer trust, signature integrity, factual truth and current status are separate (SUH-107/108/113). A QR conveys a reference, not authority.
- **Design proposal:** default deny; tenant/resource/purpose checks cover APIs, files, exports and workers; student grants name recipient, fields, purpose, revision and expiry (SUH-109; privacy design).
- **Design inference:** even conditional match notification can expose another enrolment. Use uniform receipts and restricted internal review; return no other institution or match bit (T03).
- **Design limitation:** revocation stops future service retrieval, not downloaded copies. Student notices and recipient duties must be explicit (T06).

## Open dependencies and next handoff

| Dependency | Owner / next action | Effect |
|---|---|---|
| Provider approval, scopes, field retention and retry permission | Sudhan + proposed operator/provider | Synthetic adapter until authorised and tested. |
| Legal basis, reporting mandate, minors/guardians, retention and operator roles | Operator + qualified legal review; Pranav supplies policy scope | No compliance or deployment approval claim. |
| Full SPDI Rules verification/application | Legal review; SUH-115/116 | PIB clarification inspected; full instrument/application remains open. |
| Issuer mandate and certificate-display wording | Awarding body + lead | No self-appointed official issuer or public APAAR lookup. |
| Student grievance owner, response rules and appeal route | Institution/regulator + Gopika/Pranav | Disputed evidence stays explainable and reviewable. |
| Negative access, revocation, upload, recovery and abuse checks | Future implementation/security team | Proposed checks are not passed tests. |

Human review and seven-minute teach-back remain pending. Handoffs to Sudhan, Pranav, Dharanish and the lead support synthesis and critique, not acceptance on their behalf.
