# Reconciliation of Sudhir's 26 October contribution

**Research owner:** Sudhir. **Reconciliation author:** AI security researcher. **Date:** 2026-10-27 (Asia/Kolkata), completing the 2026-10-26 research round. **Status:** documented reconciliation; no new human approval, implementation or security-test result.

## Provenance and attribution

The initial local baseline contained assignment templates. During the lead's pre-publication fetch, a substantive Sudhir contribution was recovered from the remote history: merge `3efafe1` for [PR #1](https://github.com/Dharanish99/SIH_APAAR_Student_Verification/pull/1), present in inspected `origin/main` revision `0d1232367078197c77f6882a3444bb0a9b6d1b83`. Its four files are preserved separately:

- [Submitted README](original-2026-10-26/README.md)
- [Submitted findings](original-2026-10-26/findings.md)
- [Submitted progress](original-2026-10-26/progress.md)
- [Submitted source ledger](original-2026-10-26/sources.csv)

All four were read during this reconciliation. These are member-submitted research, with AI assistance explicitly disclosed in the submitted findings. They are not merely templates and must not be attributed wholly to the later AI agent. The earlier [23 October baseline](original-2026-10-23/findings.md) remains a separate historical snapshot. The submitted contribution itself records peer review as pending; a repository merge does not establish independent legal/security validation.

The current [findings](findings.md), [privacy design](privacy-design.md), [threat model](threat-model.md) and [legal review](legal-status.md) consolidate that contribution with subsequent AI evidence checks. The two archives are unchanged. Relative links inside exact snapshots may reflect their original location; use current navigation for the consolidated assessment.

## Contributions retained and extended

| Submitted contribution | Retained value | Current location / extension |
|---|---|---|
| Sections 1-2: identifier, identity, enrolment and credential distinctions | Knowing an identifier gives no permission; admission and award are separate assertions. | Three evidence/status dimensions plus issuer authority; provider account evidence is narrower than physical-person proof. |
| Section 5.1 role/action/resource matrix | Institution boundaries, separate operator/approver, scoped student/verifier access and auditable regulator access. | [Permission matrix](privacy-design.md#permission-matrix); workers, exports, support and case-specific regulator boundaries added. |
| Section 5.2 inventory | Field-level purpose, visibility, protection and employer minimisation. | [Current inventory](privacy-design.md#data-inventory-and-retention); unsupported retention periods replaced by operator decisions and transient-copy proposals. |
| Section 5.3 eight threat cases | Enumeration, cross-tenant access, forgery, link leakage, compromised staff, regulatory overreach, replay and withdrawal risks. | [Thirteen-case model](threat-model.md); uploads, account binding, student disputes, correlation, recovery and future negative checks added. |
| Section 5.4 issuer signing and status lifecycle | Trusted issuer, integrity, status checks and key custody matter. | [Credential lifecycle](privacy-design.md#credential-and-verification-lifecycle); revision, supersession and offline limits made explicit. |
| Section 6 storage comparison | Encrypt identifiers and use a secret-keyed exact-match index rather than ordinary plaintext lookup. | Restricted keyed matching service; rotation and linkability limits; no institution query oracle. |
| Sections 7-9 questions and handoffs | Provider access, record retention, issuer trust and cross-team review are genuine dependencies. | Provider contract checked via SUH-114; current access and issuer mandate remain unconfirmed; actual AI exchanges recorded separately. |

## Claims corrected or qualified

The rows below explain changes without deleting the submitted reasoning. “Unsupported” means the supplied source does not establish the particular claim; it does not prove the opposite.

| Submitted location / claim | Current assessment and reason | Evidence / design consequence |
|---|---|---|
| F-SUH-001 and minor case: DPDP section 9 immediately governs all processing; detailed rules pending | **Correct commencement.** Final Rules and later corrections exist, but core processing/consent/child duties are future-stage on 26/27 October 2026. Retain future-ready guardian design; assess current requirements separately. | SUH-101 to SUH-105; [legal status](legal-status.md). |
| F-SUH-002: withdrawal right attributed to section 6(6) | **Correct subsection and scope.** Section 6(4) states withdrawal/ease; 6(5) covers effect on prior lawful processing; 6(6) addresses cessation subject to legal exceptions. These provisions are in the future commencement stage. | SUH-101/102. Provider permission, reporting basis and employer grant remain distinct. |
| F-SUH-003: NAD universally uses compressed signed QR payloads and IT Act compliance establishes a tamper-proof audit | **Narrow evidence.** NAD FAQ supports award access and permission workflows; it does not establish this exact universal QR encoding, our legal compliance or tamper-proof logs. | Historical SUH-002/004; SUH-107/108/113. Verify each issuer's actual document/signature contract. |
| F-SUH-004: APAAR creation/voluntariness and school mapping treated as one universal higher-education workflow | **Retain narrowly.** The April 2026 parliamentary answer states voluntary consent-based generation and no exclusion from Board examinations; its Board statement is school-scoped. School UDISE+/guardian steps do not define every HEI workflow. The original FAQ publication date is unverified. | SUH-003/118; SUH-114; [integration review](../sudhan/integration-review.md). |
| F-SUH-005: institution and AICTE fiduciary labels | **Keep as proposal.** Actual purpose/means, authority and contracts determine roles; “Regulatory Data Fiduciary” is not an established project appointment. | SUH-101; actual operator/legal review required. |
| Section 2.1: e-KYC/OIDC proves a live human is rightful APAAR holder | **Narrow assurance.** Authorised provider account linkage is evidence, not absolute physical-person proof or an admission verdict. The application must not capture Aadhaar OTP/PIN/biometrics. | SUH-112/113/114; account-to-case binding and mismatch review. |
| Worked normal case: APAAR checksum passes | **Withdraw unsupported checksum.** No inspected authoritative APAAR checksum contract is established. A 12-digit format check is only input shape. | SUH-114 and [integration review](../sudhan/integration-review.md); no Aadhaar checksum transfer. |
| Enumeration case: attack fails completely, zero metadata and uniform timing | **Convert to test objective.** These are fictional walkthroughs; no timing, penetration or leakage measurement occurred. Generic HTTP errors alone do not cover jobs, counts or conditional collision receipts. | SUH-109; T01/T03/T12/T13; uniform outward receipts and restricted review. |
| Retention: permanent APAAR/name/DOB/marks; course plus five years for categories | **Remove as legal defaults.** No specific records duty supports these periods in the submitted ledger. Separate necessary source records, transient copies, logs, receipts and legal holds. | SUH-103/106; [current retention design](privacy-design.md#data-inventory-and-retention). |
| Consent/link defaults: 48 versus 72 hours; ten failed queries versus ten/minute; minor flag after 15 days | **Treat as unvalidated parameters.** No statutory/provider mandate or measured usability basis is established. The current 24-hour synthetic grant is also merely a configurable demo example. | Configuration/rate limits and any response deadline require operator/user validation; no invented statutory penalty trigger. |
| Minor age checked only against admission-year cutoff; guardian permanently linked via assumed provider feature | **Correct workflow.** Determine age/authority at the relevant processing action and reassess changes. Verified delegation, accessibility and majority transition need design; do not assume available parent linkage or blanket disability guardianship. | SUH-101/103/105; no new identity-collection shortcut. |
| Aadhaar/biometrics “forbidden” globally; reference key/token automatically safe | **Scope the decision.** No capture/storage is our minimisation choice. The submitted sources do not prove a universal legal ban or grant this platform an approved Aadhaar reference-key route. Tokens themselves need protection. | SUH-110/112/114; provider-authorised flow only. |
| QR payload contains full APAAR/roll number yet promises selective disclosure, zero tracking and zero leakage | **Reject guarantee and unsafe default.** Signing, compression and base64url do not hide fields. Offline copies cannot provide current withdrawal/revocation assurance. | SUH-107/108/113. Preferred MVP: opaque reference, authenticated recipient and current field/revision grant; no public embedded identifiers. |
| Verification fetches from an AICTE/DigiLocker trusted key registry; suggests creating our own CA if absent | **Keep dependency, remove assumed capability.** No inspected source establishes this universal registry or authorises the team as an official issuer/CA. | SUH-114; issuer mandate and key onboarding separate; synthetic demo keys explicitly labelled. |
| “Salted hash” described alongside HMAC exact matching | **Clarify mechanism.** A keyed index is different from a public salted hash; use separately managed encryption/matching keys and rotation if implemented. Linkability remains and caller access must be restricted. | Design proposal in privacy design; no anonymity guarantee or implemented cryptographic control claimed. |
| Immediate archival-only lock after consent withdrawal | **Separate purposes.** Stop future optional sharing according to the grant; assess remaining reporting/records duties. Indefinite read-only storage is still processing, not automatic erasure compliance or a blanket section 7 exception. | SUH-101/102/103; approved retention/basis schedule. |
| SUH-004 limitation: electronic evidence governed generally by section 65B | **Update legal reference.** BSA sections 61-63 are the current electronic-evidence framework, with section 170 saving specified already-pending matters under the former Act. A signed audit export alone does not guarantee admissibility. | SUH-117; [electronic-evidence note](legal-status.md#electronic-evidence-and-credential-recognition). |
| Progress says one normal and three failure cases and compliant credential lifecycle | **Correct evidence label.** Submitted findings show one normal plus two failure cases. All are reasoning examples, not test results; legal compliance was not demonstrated. | Snapshot section 4; current supplement has seven fictional walkthroughs. |

## Original-to-current source mapping

Original IDs are retained in the current ledger as **attributed historical entries**, with present-day verification qualifications. They are not renumbered or silently promoted to verified current claims.

| Original ID | What remains useful | Current corroboration / qualification |
|---|---|---|
| SUH-001 | DPDP statute discovery and section questions | SUH-101 official Act PDF; SUH-102 commencement; SUH-103 Rules; SUH-104/105 corrections. Original landing page returned no substantive text on recheck. |
| SUH-002 | NAD award-access/permission discovery | SUH-107/108/113 for credential/security distinctions; SUH-114 for actual requester contract; integration source SUD-103 for NAD scope. FAQ indexed text and prior integration reading support narrow award workflows, not the asserted universal QR format. Targeted reopens returned 403. |
| SUH-003 | APAAR definition and consent workflow discovery | SUH-114 account-link contract; SUH-118 April 2026 primary parliamentary answer; integration source SUD-101. No checksum or universal HEI route established. |
| SUH-004 | IT Act recognition/privacy questions | SUH-101/102 govern the pending section 43A transition; SUH-115/116 flag current SPDI applicability; SUH-117 updates evidence-law framing. MeitY landing page was empty and alternate Act PDF timed out, so full current IT Act re-verification remains open. |

## Effect on the solution

Retain the correction-first institution-evidence layer and its online minimal-disclosure MVP. The new contribution strengthens attribution and prior design coverage; it does not justify a public registry, embedded personal QR payload, permanent retention, live provider claim or automatic legal/security-compliance badge. Add evidence-export provenance and legal-review handling without promising a court-admissible certificate. Human review of the consolidated work and its disagreements remains pending.
