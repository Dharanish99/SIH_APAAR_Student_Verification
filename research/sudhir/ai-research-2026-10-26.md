# Security, privacy and credential research

Author: security research agent, completing Sudhir's assigned role. Research round: 2026-10-26 (Asia/Kolkata); completion recheck: 2026-10-27. Status: desk research and proposed design; no implementation, pilot or human approval.

Provenance update: Sudhir's substantive member submission was recovered after this AI draft began; see the [contribution reconciliation](human-contribution-review.md). Its retained design work is credited separately from subsequent AI checks.

## Recommendation

Build an accountable evidence-and-correction service with purpose-specific verification. An institution attests its enrolments; a provider supplies evidence within its documented scope; an authorised reviewer decides a conflict; an employer sees only an approved disclosure. A signature establishes integrity and attribution, not the truth of the assertion. A QR code conveys a reference, not permission. The [W3C credential model](https://www.w3.org/TR/vc-data-model-2.0/#verification) explicitly distinguishes verification from factual truth (SUH-107).

## Assignment completion

| Question | Answer / artifact |
|---|---|
| What can each actor do? | [Role, action and resource matrix](privacy-design.md#permission-matrix), scoped by institution and purpose. |
| How are boundaries enforced? | [Tenant and cross-institution design](privacy-design.md#tenant-and-cross-institution-boundaries), including exports and jobs. |
| Which purposes depend on consent? | [Student and employer journey](privacy-design.md#student-and-employer-disclosure-journey); reporting authority and provider permission are distinct. |
| Which legal provisions apply now? | [Staged legal status](legal-status.md), including December 2025 and October 2026 corrections. |
| What is stored and retained? | [Field inventory](privacy-design.md#data-inventory-and-retention) with explicit retention decision gates. |
| How are records trustworthy? | [Issuer and credential lifecycle](privacy-design.md#credential-and-verification-lifecycle). |
| What can go wrong? | [Thirteen abuse cases and residual risks](threat-model.md). |

## Findings

| ID | Claim | Type | Evidence / limitation |
|---|---|---|---|
| SUH-F01 | Published DPDP provisions are not all commenced on this research date. | Verified legal-text fact | SUH-101 to SUH-105; see legal-status.md. This is not a deployment legal opinion. |
| SUH-F02 | Authorisation must be checked on each protected request, including guessed object IDs. | Documented technical guidance | [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), SUH-109. Implementation untested. |
| SUH-F03 | Access tokens and sensitive identifiers should be excluded from ordinary logs. | Documented technical guidance | [OWASP Logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html), SUH-110. |
| SUH-F04 | Issuer trust and assertion truth are separate from signature validity. | Documented technical standard | SUH-107, W3C definitions and trust model; no government recognition of our credential implied. |
| SUH-F05 | One-credential status URLs can correlate students with verifiers. | Documented technical standard | [W3C status-list privacy considerations](https://www.w3.org/TR/vc-bitstring-status-list/#privacy-considerations), SUH-108. Shared lists do not eliminate malicious collusion. |
| SUH-F06 | Requester v2.4 documents account-linked APAAR evidence, not arbitrary-number registry lookup. | Verified documentation, not live access | SUH-114; official PDF retrieved by integration agent and cached text inspected here. Specific APAAR scope remains unresolved. |
| SUH-F07 | Even a cross-institution yes/no match result can become a student-discovery oracle. | Design inference | T03; restrict matching to authorised submissions and regulator case handling. |
| SUH-F08 | Revoking sharing can stop future service retrieval, but cannot erase a recipient's previously downloaded copy. | Design limitation | Proposed online grant lifecycle; recipient obligations require agreement. |

## Worked cases

These are fictional reasoning walkthroughs, not executed system tests.

1. **Normal:** Campus A stages an enrolment; a distinct approver attests revision 1. Student S links provider evidence through an authorised account flow. Employer E requests a purpose and two fields. S previews the exact disclosure and grants access; E authenticates and receives only these fields, issuer, evidence type, time and current status.
2. **Wrong institution:** Campus B guesses a record ID. API, download and export worker deny access; the response does not reveal whether S attends A.
3. **Account-link mismatch:** The provider's APAAR differs from the institution's claim. A private correction case opens; the service neither merges people nor alleges fraud.
4. **Grant withdrawn:** S revokes before E opens the link. Online retrieval is denied. A previously issued receipt is historical, not evidence of current permission.
5. **Correction after issue:** A corrected enrolment produces a new attestation revision and supersedes the old one. The audit records reason and actors; verification checks current status.
6. **Provider outage:** Institution evidence remains visible at its stated assurance level. Provider evidence becomes unavailable or stale; a timeout does not become identity failure.
7. **Minor or guardian:** An under-18 case follows the approved assisted workflow. Staff do not infer that all disability entails guardianship, or that all educational processing is exempt.

## Alternatives

| Option | Benefit | Trade-off | Decision proposal |
|---|---|---|---|
| Public APAAR/QR lookup | Easy access | Enumeration and excessive disclosure | Reject |
| Full document download by default | Familiar evidence | Excess data and uncontrolled stale copies | Only for specifically justified, authorised cases |
| Authenticated online claim view with student grant | Minimal disclosure and revocable future access | Requires service and account availability | Preferred MVP |
| Portable W3C credential | Interoperability and offline signature checks | Trust registry, wallet and status complexity | Later, after issuer/verifier agreement |
| Blockchain student records or public hashes | Integrity narrative | No truth guarantee; correlation and correction problems | Unnecessary |

## Handoffs and limits

- Dharanish: separate institution attestation, provider evidence, disclosure grant, verification receipt, processing basis, credential status and audit event. Avoid one `verified` flag.
- Sudhan: confirm v2.4 permissions with the provider; no invented `apaar.read` scope. Minimise returned academic details and avoid Aadhaar capture or authentication shortcuts.
- Pranav: establish allowed reporting fields and cross-institution review authority for the applicable programme/year.
- Gopika: validate comprehension of permission, correction and unavailable-evidence screens with future users.
- Lead: retain the [pilot gates](privacy-design.md#pilot-entry-and-exit-gates). Do not describe this as compliant, tamper-proof, anonymous, fraud-proof or field validated.

Human review by Sudhir/Sudhan/Kanishkar remains pending. [AI critique log](critique-log.md) is collaboration evidence, not human acceptance.
