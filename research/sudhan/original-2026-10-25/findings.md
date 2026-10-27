# Research findings — Sudhan

**Workstream:** APAAR, ABC, DigiLocker/NAD and integration feasibility  
**Status:** In progress  
**Last substantive update:** 2026-10-25  
**Reviewer / review date:** Not reviewed (Sudhir assigned as review partner)

---

## 1. Research question and scope
This workstream answers the core architectural and feasibility questions for SIH26263:
* **Question 1:** *How do APAAR identity, ABC credits, DigiLocker and NAD relate, and what does each service establish?*
* **Question 2:** *What separately proves an ID's format, existence and association with a person?*

**Scope & Context:** 
This research defines the boundary between client-side string validation, authoritative registry lookup, biometric/demographic person binding, and institutional admission approval. It directly resolves the core defense question: *"What exactly does our verified badge prove?"*

---

## 2. How it works — in my own words

### A. The 4-Tier Ecosystem Stack
The Indian digital education infrastructure operates across the Ministry of Education (MoE) and the Ministry of Electronics & IT (MeitY):

```
+------------------------------------------------------------------------+
| 1. APAAR (Automated Permanent Academic Account Registry - MoE)          |
|    - Lifelong 12-digit student identifier ("One Nation, One Student ID")|
|    - Created via Aadhaar demographic verification + explicit consent   |
|    - Proves: Student identity anchor across Indian educational journey  |
+------------------------------------------------------------------------+
                                   |
                                   v
+------------------------------------------------------------------------+
| 2. ABC (Academic Bank of Credits - UGC / MoE)                          |
|    - Virtual credit ledger mapped 1:1 to APAAR ID                      |
|    - Accumulates, transfers, and redeems course credits                |
|    - Proves: Credit ledger balance & mobility across approved HEIs     |
+------------------------------------------------------------------------+
                                   |
                                   v
+------------------------------------------------------------------------+
| 3. NAD (National Academic Depository - MoE managed via DigiLocker)     |
|    - Secure repository of digital academic awards (degrees, marksheets)|
|    - Published directly by issuing academic boards and universities    |
|    - Proves: Authenticity and non-tampering of completed qualifications |
+------------------------------------------------------------------------+
                                   |
                                   v
+------------------------------------------------------------------------+
| 4. DigiLocker (NeGD / MeitY)                                           |
|    - Public digital wallet & consent-driven exchange backbone (API Setu)|
|    - OAuth 2.0 / OIDC requester flow for pulling verified docs         |
|    - Proves: Citizen consent & secure delivery mechanism               |
+------------------------------------------------------------------------+
```

### B. Deconstructing Identity: Format vs. Existence vs. Person Binding vs. Enrolment
One of the most dangerous design errors in student verification is treating a successful format check as proof of identity, or treating proof of identity as proof of valid admission. 

They are four completely separate tiers:

```
+-----------------------------------------------------------------------------------+
| Tier 1: FORMAT & CHECKSUM (Offline / Mathematical)                                 |
| - Check: 12 numeric digits, length == 12, regex `^\d{12}$`, Verhoeff checksum.     |
| - What it proves: The string is syntactically well-formed; catches typos.         |
| - What it CANNOT prove: It does not prove the ID exists in any database.          |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| Tier 2: EXISTENCE IN REGISTRY (Online Registry Lookup)                            |
| - Check: APAAR Central Registry / ABC database query via API Setu.                |
| - What it proves: This 12-digit number has been issued by MoE.                    |
| - What it CANNOT prove: It does not prove the person submitting it owns it.       |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| Tier 3: PERSON ASSOCIATION (Consent & Demographic/OTP Binding)                    |
| - Check: DigiLocker OAuth 2.0 / Aadhaar OTP / Demographic Name & DOB match.      |
| - What it proves: The physical human applicant is the legitimate owner of the ID. |
| - What it CANNOT prove: It does not prove the student is admitted to your college.|
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| Tier 4: ENROLMENT & COMPLIANCE (AICTE Institutional Sanction)                     |
| - Check: Matched against AICTE approved intake quota & duplicate enrolment rules.  |
| - What it proves: Student holds a legally valid, non-conflicting academic seat.   |
+-----------------------------------------------------------------------------------+
```

---

## 3. Findings and evidence
| Finding ID | Claim | Type | Source ID(s) / section | Applicability | Confidence and limits |
|---|---|---|---|---|---|
| F-SUD-001 | APAAR is a 12-digit lifelong student ID under NEP 2020, unified across school and higher education. | Verified fact | SUD-001 (Overview FAQs), SUD-005 (CBSE Circular) | All Indian students | High. Official MoE initiative. Seeded via UDISE+ in schools and ABC in HEIs. |
| F-SUD-002 | APAAR ID and ABC ID function as the same 12-digit identifier in higher education; APAAR is mandatory for ABC. | Verified fact | SUD-002 (About ABC / FAQs) | Higher Education Institutions (HEIs) | High. Confirmed by UGC/ABC portal and MoE guidelines. |
| F-SUD-003 | NAD is hosted on DigiLocker infrastructure; students access NAD academic awards through DigiLocker. | Verified fact | SUD-003 (About NAD FAQs) | Academic awards & credentials | High. Operates under DigiLocker/MeitY infrastructure for MoE. |
| F-SUD-004 | Requester API access to DigiLocker/NAD requires formal partner onboarding, NeGD approval committee sign-off, and an MoU. | Verified fact | SUD-004 (Consumer APIs / Requester Integration) | Institutional / Platform Requesters | High. Public live API calls cannot be made without registered Client ID and NeGD approval. |
| F-SUD-005 | Third-party student document retrieval requires explicit user consent via OAuth 2.0 / OIDC redirects. | Verified fact | SUD-004 (Consent Flow) | Data access & privacy | High. Aligned with DPDP Act and DigiLocker security standards. |
| F-SUD-006 | Syntactic checks (12-digits, Verhoeff checksum) only catch entry typos; they provide zero proof of existence or identity. | Verified fact | SUD-006 (Aadhaar Checksum Specs) | Input validation layer | High. A mathematically generated 12-digit number will pass Verhoeff but does not exist in MoE registries. |
| F-SUD-007 | APAAR generation requires voluntary parental/student consent; CBSE circulars confirm relaxations/provisional codes for missing IDs. | Verified fact | SUD-005 (CBSE 2025 Circulars) | School/HEI Admissions | High. Platform must support provisional enrolment status when APAAR is pending. |
| F-SUD-008 | Whether the production APAAR registry enforces the Verhoeff algorithm on the 12th digit remains unverified in public docs. | Unknown | SUD-001, SUD-006 | Central Registry API | Unknown / Unverified. Standard practice for 12-digit IDs in India, but unconfirmed in open APAAR specs. |

---

## 4. Worked cases or experiment

### Case 1: Normal Path (Domestic Student Complete Verification)
- **Input:** Student `Kavitha R` applies to an AICTE-approved B.Tech programme, providing her 12-digit APAAR ID `9123-4567-8901`.
- **Execution:**
  1. *Tier 1 (Format):* Regex `^\d{12}$` confirms 12 digits; Verhoeff check confirms mathematically valid check digit.
  2. *Tier 2 (Existence):* Central registry lookup returns `status: ACTIVE, registered_state: TN`.
  3. *Tier 3 (Person Association):* Student authenticates via DigiLocker OTP; OAuth token returned; profile name matches application (`Kavitha R`, DOB `2006-05-14`).
  4. *Tier 4 (Enrolment Binding):* System checks Class 12 marksheet from NAD via DigiLocker, verifies eligibility, and validates seat against college's AICTE approved intake.
- **Output Status:** `STATUS_VERIFIED_AND_ENROLLED` (Audit trail logged).

### Case 2: Failure Case A (Typo / Format Failure)
- **Input:** Data entry operator enters `9123-4567-8910` (adjacent digits `01` transposed to `10`).
- **Execution:**
  1. *Tier 1:* Verhoeff algorithm catches transposition immediately on client side.
- **Output Status:** `REJECTED_INVALID_FORMAT` (Zero network requests sent to government APIs).

### Case 3: Failure Case B (Valid Checksum, Synthetic Number / Non-Existent)
- **Input:** Fraudulent applicant generates a random 11-digit number and computes the valid 12th Verhoeff digit (`4812-9031-7546`).
- **Execution:**
  1. *Tier 1:* Passes (12 digits, valid check digit).
  2. *Tier 2 (Existence):* Registry lookup queries simulated/live API Setu APAAR endpoint. Endpoint returns `HTTP 404 NOT_FOUND` or `ERROR_ID_NOT_REGISTERED`.
- **Output Status:** `FLAGGED_NON_EXISTENT_ID`. Proves that format validation $\neq$ existence.

### Case 4: Failure Case C (Valid ID, Real Person, but Impersonation)
- **Input:** Candidate `Ramesh S` steals his classmate `Suresh S`'s genuine APAAR ID.
- **Execution:**
  1. *Tier 1:* Passes (valid format).
  2. *Tier 2:* Passes (ID exists and is active).
  3. *Tier 3 (Person Association):* DigiLocker authentication is triggered. OTP is sent to Suresh's Aadhaar-linked mobile phone. Ramesh cannot complete OTP, or DigiLocker returns demographic profile `Name: Suresh S`, failing similarity match against `Ramesh S`.
- **Output Status:** `FLAGGED_IDENTITY_MISMATCH`. Proves that existence $\neq$ identity ownership.

### Case 5: Failure Case D (Valid Person, but Illegal Dual Enrolment)
- **Input:** Student `Arun K` holds valid APAAR ID `8234-5678-9012` and enrolls in College A (B.Tech CSE Full-time). College B submits Arun's APAAR ID for B.Tech ECE (Full-time) in the same academic year.
- **Execution:**
  1. Tiers 1, 2, and 3 pass completely.
  2. *Tier 4 (Enrolment Engine):* AICTE cross-institutional registry flags active simultaneous regular degree enrolments.
- **Output Status:** `FLAGGED_DUAL_ENROLMENT`. Proves that authenticated identity $\neq$ valid institutional admission.

---

## 5. Implications for our solution

1. **Defending the "Verified" Badge:**
   - We must abandon any binary "Verified" vs "Unverified" boolean.
   - The platform UI must display a multi-state verification badge:
     - 🟡 `SYNTACTICALLY_VALID`: Format check passed (offline).
     - 🔵 `REGISTRY_LOCATED`: APAAR exists in central registry.
     - 🟣 `IDENTITY_AUTHENTICATED`: Matched via DigiLocker consent/OTP.
     - 🟢 `ADMISSION_SANCTIONED`: Confirmed against AICTE intake and free of duplicate/conflicting enrolments.
     - 🔴 `FLAGGED_CONFLICT` / `PROVISIONAL`: Pending dispute or consent relaxation.
2. **Provisional Admission Pathway:**
   - Aligned with CBSE Circulars (SUD-005), students lacking an APAAR ID due to pending parental consent, technical errors, or foreign national status must be assigned a `PROVISIONAL_PENDING_APAAR` status with a time-bound compliance deadline, preventing unfair denial of admission.
3. **Simulated Adapter Architecture:**
   - To decouple the frontend and verification engine from unapproved government network calls, the team must build a `VerificationAdapterInterface` with two implementations:
     - `LiveApiSetuClient`: For future production rollout with NeGD credentials.
     - `MockVerificationClient`: Deterministic mock testing Tiers 1 through 4 with synthetic datasets.

---

## 6. Alternatives and recommendation
- **Alternative 1: Direct Aadhaar OTP Verification**
  - *Drawback:* Expensive (AUA/KUA licensing), high compliance liability, prohibited from storing raw numbers.
- **Alternative 2: Standalone Format & Checksum Verification**
  - *Drawback:* Zero protection against fabricated numbers or stolen identity. Anyone could paste a classmate's APAAR ID.
- **Recommendation: Tiered Verification Pipeline (Format $\rightarrow$ Registry $\rightarrow$ DigiLocker OIDC $\rightarrow$ AICTE Enrolment Engine)**
  - Fully compliant with DPDP rules, privacy-preserving, mathematically eliminates input typos locally, verifies genuine ownership via citizen consent, and enforces AICTE intake ceilings.

---

## 7. Unknowns and blockers
| Question | Impact | Next action | Dependency owner | Status |
|---|---|---|---|---|
| Does the central APAAR registry use Verhoeff checksum algorithm on digit 12? | If not, strictly enforcing Verhoeff client-side could reject legitimate student IDs. | Implement Verhoeff check as a soft warning or configurable flag until verified. | Sudhan (Role 2) | Open |
| How are Foreign National / NRI students without Aadhaar officially provisioned in APAAR/ABC? | Blocks automated intake verification for supernumerary foreign seats. | Formulate formal clarification question for AICTE/MoE nodal officer. | Sudhan (Role 2) / Pranav (Role 3) | Open |
| Will AICTE or SIH organisers provide test API Setu sandbox credentials for SIH26263 participants? | Determines whether we can run live network tests vs simulated contract tests. | Flag as external dependency to team lead Kanishkar. | Kanishkar (Role 6) | Blocker |

---

## 8. Handoff
- **To Dharanish (Role 4 - Data Architecture):**
  - Use `string(12)` for APAAR IDs; never integer.
  - Implement the multi-tier status enum (`SYNTACTICALLY_VALID`, `REGISTRY_LOCATED`, `IDENTITY_AUTHENTICATED`, `ADMISSION_SANCTIONED`, `PROVISIONAL`).
  - Decouple student demographic entity from institutional enrolment seat records.
- **To Sudhir (Role 5 - Security & Consent):**
  - DigiLocker integration requires OAuth 2.0 redirection and explicit user consent logs. User tokens must be short-lived; no Aadhaar numbers may be stored locally.
- **To Kanishkar (Role 6 - Team Lead):**
  - Present the 4-tier verification model for cross-workstream adoption.

---

## 9. Review
Record actual reviewer feedback, corrections and unresolved disagreement. No human review has occurred yet.
