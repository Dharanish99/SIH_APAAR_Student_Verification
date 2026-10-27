# Research findings - Sudhir

**Workstream:** privacy, security, consent and credential verification. **Status:** member contribution and AI reconciliation ready for human review. **Research round:** 2026-10-26 (Asia/Kolkata). **Completion recheck:** 2026-10-27. **Human reviewer/date:** pending.

The research recommends institution-attested, versioned records with separate provider evidence and narrowly authorised disclosure. Knowing an APAAR ID must not reveal student data or existence. The service must support correction without labelling every overlap or provider failure as fraud.

Sudhir submitted substantive research on 2026-10-26, with AI assistance disclosed in his findings; it was recovered during the pre-publication fetch after the initial template baseline. His [submitted findings](original-2026-10-26/findings.md), [README](original-2026-10-26/README.md), [progress](original-2026-10-26/progress.md) and [four-source ledger](original-2026-10-26/sources.csv) are preserved unchanged. The [human-contribution review](human-contribution-review.md) maps retained ideas, corrections and source IDs. The current consolidation includes subsequent AI-authored checks/design and does not imply Sudhir approved those additions. [23 October templates](original-2026-10-23/findings.md) are a separate earlier baseline, not the full extent of his contribution.

## Research outputs

| Output | Coverage / evidence boundary |
|---|---|
| [Contribution reconciliation](human-contribution-review.md) | Credits Sudhir's recovered research and records retained ideas, qualified claims and source mapping. |
| [Research supplement](ai-research-2026-10-26.md) | Findings, alternatives and seven fictional walkthroughs; no executed system tests. |
| [Permission and data design](privacy-design.md) | Roles, tenant boundaries, field inventory, sharing journey, issuer/status lifecycle and pilot gates. Controls proposed. |
| [Legal status](legal-status.md) | Primary staged commencement/corrections and CERT-In directions; deployment applicability and full SPDI verification remain open. |
| [Threat model](threat-model.md) | Thirteen abuse cases, future checks, owners and residual risks. No penetration test or implementation. |
| [Source register](sources.csv) | Historical SUH-001 through SUH-004 plus AI SUH-101 through SUH-118; 22 entries with attribution, inspected sections and retrieval limits. |
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

Peer review of the consolidated findings and seven-minute teach-back remain pending. The historical contribution's self-reported 50% milestone is not an independently measured completion score. Handoffs to Sudhan, Pranav, Dharanish and the lead support synthesis and critique, not acceptance on their behalf.
