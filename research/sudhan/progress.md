# Progress — Sudhan

**Current status:** In progress  
**Next action:** Investigate Question 3 & 4 (Integration matrix: Documented interfaces, API Setu endpoints, and partner onboarding requirements).  
**Blockers:** Need official API Setu sandbox access/credentials from organizers/AICTE (flagged to Kanishkar).  
**Handoff:** Shared 4-tier verification status enum with Dharanish (Role 4) and consent redirection model with Sudhir (Role 5).

## Update log

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
