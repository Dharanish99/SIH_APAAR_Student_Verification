# Progress — Sudhan

**Current status:** Desk research complete for all six questions; live integration and human review pending.<br>
**Next action:** Lead synthesises the current integration review with policy, security and institution workflows; the human sponsor later confirms provider permission and authoritative AICTE contracts.<br>
**External dependencies:** Eligible sponsor, approved use case/client/scopes/testing arrangements, foreign/missing-ID submission rules, and official SIH wording. No public sandbox or temporary testing access is promised.<br>
**Handoff:** [Current integration review](integration-review.md) supersedes the historical checksum/registry/linear-status design; use independent evidence dimensions, account-to-case binding, and institution-owned correction workflows.

## Update log

### 2026-10-26 research round — completed 2026-10-27 (Asia/Kolkata)
- **Authors:** integration_research AI agent; completion audit by integration_finish AI agent. Human owner remains Sudhan; no human approval is recorded.
- **Work completed:** Addressed all six assignment questions in [integration-review.md](integration-review.md): ecosystem, proof boundaries, operation matrix, partner access, failure states, missing/foreign-ID and correction routes. Added [12 fictional contract scenarios](contract-scenarios.csv), explicitly designed and unexecuted.
- **Evidence:** SUD-101–109 record inspected official pages, September 2026 Meri Pehchaan requester v2.4, onboarding SOP, historical manual/support conflicts, and unavailable official SIH listing. Completion audit reopened the APAAR FAQ/resource index and rechecked cached specification/SOP sections; it did not repeat the entire source investigation.
- **Key correction:** The documented APAAR GET operation accepts no ID parameter and returns the token-linked account's evidence. Its 404 cases do not establish registry-wide nonexistence; it recommends one call after token acquisition. Academic credit details do not establish exhaustive current admissions or sanction an intake.
- **Original preservation:** Historical findings and source records remain under [original-2026-10-25](original-2026-10-25/findings.md); their Git blob hashes match baseline `5ee5d57`. The historical update log below remains unchanged and is superseded where the correction ledger says so.
- **Critique/handoff:** Shared the no-arbitrary/batch-validation boundary and institution-assertion-first recommendation with the lead, security and policy AI agents. Preserve separate provider linkage, enrolment, credential and policy evidence; missing linkage must not automatically become fraud or ineligibility.
- **Checks:** Validated local Markdown targets and source-ID resolution in current integration documents; parsed current source/scenario CSVs; verified cached PDF SHA-256 values and original Git blobs. All 12 scenarios remain unexecuted. See the completion audit record in the integration review.
- **Remaining limits:** No provider credentials/calls, interviews, real student records, measured performance, field pilot or human review. Official SIH wording remains unverified after another HTTP 403 on 2026-10-27. No external contact, account creation or product implementation occurred.

### 2026-10-25 — Question 2 Investigation: Format, Existence, Person Association & Enrolment
- **Question investigated:** Question 2: What separately proves an ID's format, existence and association with a person?
- **Work actually completed:**
  - Deconstructed student verification into 4 discrete architectural tiers: Tier 1 (Format & Checksum), Tier 2 (Registry Existence), Tier 3 (Person Association via DigiLocker OIDC), and Tier 4 (AICTE Enrolment & Compliance).
  - Researched mathematical check-digit algorithms (Verhoeff dihedral $D_5$ group) and analyzed its applicability to 12-digit Indian national identifiers.
  - Inspected CBSE 2025 circulars regarding APAAR mandatory usage, parental consent rules, and relaxation/provisional mechanisms for students awaiting IDs.
  - Designed 4 worked failure scenarios illustrating format rejection, synthetic ID non-existence, identity impersonation, and conflicting dual enrolments.
  - Formulated the exact architecture to defend the core team question ("What exactly does our verified badge prove?").
- **Evidence added (source IDs):** SUD-005 (CBSE Circulars 2025), SUD-006 (UIDAI / Checksum Specifications) in `sources.csv`.
- **Key finding or remaining uncertainty:**
  - Finding: Format validation only guarantees mathematical string consistency; it provides zero evidence of existence or legitimate person ownership.
  - Uncertainty: While Aadhaar uses Verhoeff, whether the production APAAR registry strictly enforces Verhoeff on digit 12 is not published in open `.gov.in` docs. Recommended configuring Verhoeff as an advisory flag until sandbox access is obtained.
- **Files changed:**
  - `research/sudhan/findings.md`
  - `research/sudhan/sources.csv`
  - `research/sudhan/progress.md`
- **Review/handoff needed:**
  - Dharanish (Role 4): Update schema with multi-tier status enum (`SYNTACTICALLY_VALID`, `REGISTRY_LOCATED`, `IDENTITY_AUTHENTICATED`, `ADMISSION_SANCTIONED`, `PROVISIONAL`).
  - Sudhir (Role 5): Review consent and OTP redirection specifications.
  - Kanishkar (Role 6): Present 4-tier model for team consensus.
- **Next action:** Build the comprehensive Integration Matrix (Question 3 & 4).

---

### 2026-10-24 — Question 1 Investigation: APAAR, ABC, DigiLocker & NAD Ecosystem
- **Question investigated:** Question 1: How do APAAR identity, ABC credits, DigiLocker and NAD relate, and what does each service establish?
- **Work actually completed:**
  - Read official guidelines and FAQs from `apaar.education.gov.in`, `abc.gov.in`, `nad.digilocker.gov.in`, and `partners.apisetu.gov.in`.
  - Mapped the 4-tier stack (APAAR as Identity Layer, ABC as Credit Ledger, NAD as Academic Award Depository, DigiLocker/API Setu as Consent/Transport Gateway).
  - Clarified differences between School (UDISE+/PEN) and Higher Education (ABC/HEI) generation pathways.
  - Worked through normal path and critical failure modes (impersonation vs dual enrolment).
- **Evidence added (source IDs):** SUD-001, SUD-002, SUD-003, SUD-004 in `sources.csv`.
- **Key finding or remaining uncertainty:**
  - In higher education, APAAR ID and ABC ID function as the same 12-digit identifier. DigiLocker/NAD Requester integration strictly follows OAuth 2.0 / OIDC consent flows.
- **Files changed:**
  - `research/sudhan/findings.md`
  - `research/sudhan/sources.csv`
  - `research/sudhan/progress.md`
- **Next action:** Investigate Question 2.
