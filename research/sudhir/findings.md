# Research findings — Sudhir

**Workstream:** Privacy, security, consent and credential verification  
**Role:** Role 5 (SIH26263)  
**Status:** In progress (50% Milestone Reached: Permission Matrix, Data Inventory, Threat Model, Verification Design drafted)  
**Last substantive update:** 2026-10-26  
**Reviewer / review date:** Awaiting review by Sudhan (Review partner) and Kanishkar B (Lead); no human review has occurred yet.

---

## 1. Research question and scope

This research establishes the privacy, security, authorization, and cryptographic verification model for the APAAR ID-based Student Data Management and Verification Platform for AICTE-approved institutions.

### Scope & Key Questions
1. **Access Boundaries:** What can each institutional operator/approver, AICTE regulator, student, third-party verifier (employer/evaluator), and administrator do? How do tenancy boundaries strictly isolate data?
2. **Defending APAAR Privacy:** If an adversary or unauthorized party learns an APAAR ID, what can they see, and why?
3. **Statutory Consent & Minors:** How does the Digital Personal Data Protection (DPDP) Act 2023 (specifically Section 6 on consent and Section 9 on children's data) govern student data processing, parental consent for minors (<18), and consent withdrawal?
4. **Data Minimisation & Lifecycle:** What fields must be collected, how long should they be retained, and how are records corrected or purged?
5. **Threat Modelling:** What are the realistic attack vectors (e.g. ID enumeration, cross-institutional scraping, compromised institutional tokens, forged credentials) and how are they mitigated?
6. **Credential Authenticity:** How do digital signatures (PKI / XML-DSig / W3C Verifiable Credentials) and QR codes prove integrity without leaking private attributes?

---

## 2. How it works — in my own words

### 2.1 Core Architectural Distinctions
To avoid common security flaws in academic registry design, four concepts are kept strictly separate:
- **Identifier (APAAR ID):** A 12-digit permanent academic identity number assigned to an individual student. It is *an identifier, not an authentication credential or authorization token*.
- **Identity Proof:** Proof that a live human is the rightful holder of an APAAR ID (achieved through Aadhaar e-KYC / DigiLocker OIDC auth, never through format inspection).
- **Enrolment Record:** An institution-specific event stating that Person X was enrolled in Program Y under Category Z for Academic Year N.
- **Verifiable Credential:** An immutable, tamper-evident digital certificate or marksheet issued and digitally signed by an authorized body (University/AICTE/Board) and verifiable offline or via public key infrastructure.

### 2.2 The Core Question: If someone knows my APAAR ID, what can they see, and why?
**Answer: Nothing.** Under this security architecture, an unauthenticated or unauthorized actor presenting an APAAR ID sees **zero personal or academic information**.

**Mechanism:**
1. **No Public Lookup by Identifier:** The platform exposes no public API or web endpoint where entering a 12-digit APAAR ID returns demographic or enrolment details.
2. **Attribute-Based and Role-Based Scoping:**
   - Institutional operators can only view students actively enrolled in their verified institution's tenancy.
   - AICTE officers can view anonymised/aggregated capacity reports by default, and only access identified student records during active regulatory audits.
   - Third parties (e.g., employers) cannot query by APAAR ID. They can only verify credentials if the student explicitly shares a **time-limited, cryptographically signed Consent Verification Token** or presents a digitally signed certificate carrying a selective-disclosure QR code.
3. **Anti-Enumeration Responses:** Queries for non-existent IDs or unauthorized access attempts return identical generic errors (`403 Forbidden` / `404 Not Found` with uniform response timing) to thwart brute-force APAAR harvesting.

---

## 3. Findings and evidence

| Finding ID | Claim | Type | Source ID(s) / section | Applicability | Confidence and limits |
|---|---|---|---|---|---|
| F-SUH-001 | Students under 18 years of age require verifiable parental/guardian consent prior to processing of personal data under DPDP Act 2023. | Verified fact | [SUH-001](sources.csv) (DPDP Act Sec 2(f), Sec 9) | Platform registration & institutional onboarding for minor diploma/first-year students | High. Enacted primary law; detailed verification guidelines pending complete rule notification. |
| F-SUH-002 | Data principals have a statutory right to withdraw consent at any time under Section 6(6) of DPDP Act 2023 without retroactive illegality. | Verified fact | [SUH-001](sources.csv) (DPDP Act Sec 6(6)) | Platform consent registry; third-party verification delegation | High. Withdrawal mechanisms must be provided with comparable ease to granting consent. |
| F-SUH-003 | DigiLocker NAD utilizes PKI digital signatures (compliant with IT Act 2000 Sec 4/5) and secure QR codes containing compressed signed payloads for offline/online verification. | Verified fact | [SUH-002](sources.csv) (NAD FAQs), [SUH-004](sources.csv) (IT Act Sec 4, 5) | Certificate generation (R10), verifiable records (R06), tamper-proof audit trails | High. Matches production DigiLocker implementation models. |
| F-SUH-004 | APAAR ID is a 12-digit identifier mapped to UDISE+ and Aadhaar demographics, and its generation is voluntary with explicit consent. | Verified fact | [SUH-003](sources.csv) (APAAR FAQs) | Student ID linkage (R01); fallback workflows for students without APAAR | High. Confirmed by Ministry of Education guidance. |
| F-SUH-005 | Institutions can act as Data Fiduciaries while AICTE acts as a Regulatory Data Fiduciary; institutional tenants must be strictly isolated to prevent horizontal privilege escalation. | Proposal | [SUH-001](sources.csv) (Sec 8), Project Scope | Multi-tenant platform architecture, RBAC/ABAC engine | High confidence architectural proposal; subject to AICTE data governance validation. |
| F-SUH-006 | Verification links shared with employers must be scoped to specific attributes, expire automatically (default: 72 hours), and record an immutable audit entry. | Proposal | [SUH-001](sources.csv) (Sec 6), [SUH-002](sources.csv) | Third-party verification portal (R05) | Sound security practice; pending usability feedback from Gopika's user research. |

---

## 4. Worked cases or experiment

### Case 1: Normal Authorized Flow — Institutional Admission & Third-Party Verification
- **Context:** An AICTE-approved engineering college enrolls Student S (Age 19, APAAR `9123-4567-8901`).
- **Step 1 (Admission Upload):** Institutional Operator (authenticated via institutional multi-factor authentication) uploads admission batch. The platform checks:
  1. Operator belongs to Institution Inst-101.
  2. Program approval intake limits are not exceeded (coordinating with Pranav/Dharanish).
  3. Student APAAR format and checksum pass validation.
- **Step 2 (Consent & Verification):** Student logs into their portal, observes that Inst-101 has submitted an enrolment record, and affirms consent.
- **Step 3 (Employer Verification):** Employer E requests verification of S's B.Tech degree.
  - S generates a short-lived Verification Link (valid for 48 hours, scoped strictly to Degree Name, Division, and Awarding University).
  - Employer E opens the link, sees the cryptographic signature of the awarding university, and verifies authenticity. S's date of birth, category, and Aadhaar-linked phone are completely redacted.
- **Outcome:** Successful verification with zero unnecessary disclosure.

### Case 2: Failure Case A — Adversarial APAAR Harvesting & Enumeration Attack
- **Context:** An attacker scripts a sequential loop of 12-digit numbers against the platform API to discover student identities.
- **Attack Payload:** `GET /api/v1/students/912345678901`, `GET /api/v1/students/912345678902`, ...
- **System Defense:**
  1. API requires Bearer JWT token bound to an authorized tenant; unauthenticated requests fail immediately with `401 Unauthorized`.
  2. If an authenticated operator from Inst-101 attempts querying an APAAR ID not enrolled in Inst-101:
     - The ABAC engine checks `student.institution_id == caller.institution_id`.
     - Match fails. System returns `404 Not Found` (rather than `403 Access Denied`, to hide whether the student exists).
     - Rate-limiter (token bucket) trips after 10 failed queries, alerting institutional security officers and generating an audit alert.
- **Outcome:** Attack fails completely; zero metadata leaked.

### Case 3: Failure Case B — Minor Student (<18) Admission without Parental Consent
- **Context:** Student M (Age 17, Polytech Diploma entrant) is registered by College C without signed parental consent.
- **System Defense:**
  1. System checks student birthdate against admission year cut-off. Status: Minor (<18).
  2. In compliance with DPDP Act Sec 9, personal data processing cannot be activated solely on student consent.
  3. Enrolment is placed in `Awaiting_Guardian_Consent` state.
  4. Notification sent to parent DigiLocker/Mobile for verifiable authorization.
  5. Institution is flagged in compliance monitoring if consent is not recorded within 15 days.
- **Outcome:** Prevents statutory non-compliance and safeguards minor student privacy.

---

## 5. Implications for our solution

### 5.1 Role, Action, and Resource Permission Matrix (RBAC & ABAC)

| Role | Allowed Actions | Accessible Resources | Scope & Boundary Conditions | Authentication & Audit Requirement |
|---|---|---|---|---|
| **Institutional Operator** | Upload batch; Draft student records; Edit pending records | Enrolment records within own institution only | Restricted to current academic year intake; cannot approve final submission | Institutional MFA; IP/Session bound; All mutations logged |
| **Institutional Approver (Principal / Head)** | Approve & Sign batch; Submit to AICTE; View institution audit logs | Finalized student enrolment & intake quotas for own institution | Own institution only; cannot view peer institutions' student lists | Hardware token / DSC / Aadhaar OTP signing; Non-repudiable audit log |
| **AICTE Monitoring Officer** | View aggregated intake vs actual counts; Run anomaly queries; Initiate audit | Aggregated metrics nationwide; Identified records only under formal audit flag | No casual browsing of student PII; Anonymised views by default | Official GOI SSO; Access reason mandatory; Justified audit trail |
| **Student (Data Principal)** | View own academic profile; Grant/Revoke verification access; Download signed credentials | Own profile, own enrolment history, own verifiable credentials | Own records only; cannot see other students or institutional quotas | DigiLocker / MeriPehchaan SSO; Audit log of all third-party disclosures |
| **Parent / Legal Guardian** | Grant/Withdraw consent for minor student (<18); View minor's profile | Minor ward's registration and consent status | Active until ward reaches 18 years of age | Aadhaar e-KYC / DigiLocker parental linkage |
| **Third-Party Verifier (Employer / University)** | Verify credential authenticity; Check validity status | Scoped credential attributes explicitly shared by student | Read-only; Time-limited token (e.g. 72 hrs); Zero access to student history | Pre-registered or one-time token access; Query logged to student dashboard |
| **Platform Administrator** | Manage system configuration; Monitor service health; Rotate service certificates | System telemetry, infrastructure logs (strictly pseudonymised) | Zero access to raw student PII or credential private keys | Multi-party authorization; Privileged Access Management (PAM) |

---

### 5.2 Student Data Inventory & Minimisation Policy

| Field Name | Category | Purpose | Collection Source | Visibility | Retention Period | Rationale & Protection |
|---|---|---|---|---|---|---|
| **APAAR ID** | Academic Identifier | Cross-institution academic tracking & ABC linkage | DigiLocker / Student | Student, Enrolled Institution, AICTE (Audits) | Permanent academic life | Salted hash indexed in DB; Plaintext displayed only to student and verified college |
| **Full Name** | Demographic | Identity confirmation against APAAR / 10th cert | DigiLocker e-KYC | Student, Enrolled Institution, Verifier | Permanent | Essential for certificate and verification |
| **Date of Birth** | Demographic / Legal | Age verification & DPDP minor status check | DigiLocker e-KYC | Student, Institution (Admin only); Redacted on public verifier | Permanent | Required to determine minor status under DPDP Sec 9 |
| **Category (General / OBC / SC / ST / EWS)** | Regulatory / Compliance | AICTE quota compliance & reservation audit | State Admission Portal / Student upload | Institution Approver, AICTE Regulators | Duration of course + 5 years | Regulatory requirement; Strictly concealed from prospective employers/public |
| **Supernumerary / NRI / OCI / FN Flag** | Regulatory / Compliance | Seat intake quota compliance (Handbook rules) | Institution upload / Verification portal | Institution Approver, AICTE Regulators | Duration of course + 5 years | Required for AICTE compliance checking; Prohibited from general display |
| **Parent/Guardian Contact & Consent** | Legal / Privacy | DPDP Sec 9 verifiable consent for minors | Guardian input / DigiLocker | Institution Admin, Compliance auditor | Until student turns 18 + statutory limitation | Mandatory for minor data processing; Deleted or archived post-majority |
| **Academic Marks / CGPA** | Academic Record | Progression, award issuing | Institution LMS / Controller of Exams | Student, Institution, Authorized Verifier | Permanent | Verifiable credential component |
| **Biometric / Aadhaar Number** | Sensitive Personal Data | **NOT STORED** (Forbidden) | UIDAI / e-KYC gateway | **NEVER STORED ON PLATFORM** | 0 seconds (Ephemeral token only) | Compliance with Aadhaar Act & MeitY guidelines. Only Aadhaar Reference Key or DigiLocker Token utilized |

---

### 5.3 Threat Model: 8 Realistic Abuse Cases, Mitigations & Residual Risks

| # | Threat Scenario / Abuse Case | Threat Actor | Impact | Proposed Mitigation | Residual Risk |
|---|---|---|---|---|---|
| **T1** | **Automated APAAR ID Enumeration & Harvesting** | External attacker | Mass reconnaissance, deanonymisation of student records | No public lookup by ID; ABAC tenancy filter; Generic 404 responses; Rate limiting (10 req/min per IP/token) | Distributed botnets could probe slowly; mitigated by requiring authenticated session. |
| **T2** | **Horizontal Privilege Escalation (Cross-Tenancy Snooping)** | Rogue operator at College A | College A reads admission data or marks of students at College B | Database multi-tenant isolation enforced at repository layer with row-level tenant security (`institution_id = current_user_tenant`) | Zero-day vulnerability in ORM / DB layer; mitigated by strict database policy checks. |
| **T3** | **Credential Tampering / Forged Graduation Certificate** | Unscrupulous applicant / Fake university | Acceptance of fraudulent degrees; reputation loss | Certificates signed with issuing authority's X.509 PKI key; QR code embeds compressed cryptographic signature; Offline verification checks root cert against AICTE trust store | Compromise of institution private signing key; mitigated by Hardware Security Modules (HSM) and key revocation lists (CRL). |
| **T4** | **Stale or Leaked Third-Party Verification Links** | Public eavesdropper / Unintended recipient | Unauthorized third party views student's academic credentials | Short-lived tokens (max 72 hours); Optional PIN/passcode shared out-of-band by student; Student can revoke link instantly via dashboard | Legitimate verifier takes screenshot or downloads PDF while link is active. |
| **T5** | **Compromised Institutional Operator Credentials** | Phished operator / Insider | Malicious upload of bogus students or fraudulent intake expansion | Two-man rule: Operator can only stage records; Institutional Head/Principal must digitally sign batch with DSC/OTP; Anomaly threshold alerts | Collusion between operator and principal; mitigated by AICTE cross-validation against approved seat matrix. |
| **T6** | **Unauthorised Surveillance & Data Mining by Regulators** | Rogue administrator / Overreaching staff | Mass surveillance of student demographic or caste details | Role-based data masking; AICTE views aggregate capacity numbers by default; Unmasking student PII requires formal audit order with justification logged to immutable audit ledger | Regulatory authority pressure; mitigated by institutional transparency reporting. |
| **T7** | **Replay Attack on Verification Responses** | Malicious intermediary | Resubmission of expired or revoked credential verification response | Nonce embedded in verification challenge; timestamped signatures with strict validity window; verification endpoint checks live Revocation Registry | Clocks out of sync; mitigated by NTP synchronisation and short tolerance windows. |
| **T8** | **Unauthorized Processing of Minor Student Data Post Consent Withdrawal** | Negligent institution | Violation of DPDP Act Section 6(6) and Section 9; regulatory penalty | Automated consent state machine: Upon withdrawal, processing flags lock records immediately to read-only archival; notifications triggered to institution | Retention of legally required statutory tax/admission records under Section 7 exemptions must be distinguished from discretionary processing. |

---

### 5.4 Credential Verification & Certificate Display Lifecycle (R06, R10)

```
+-----------------------------------------------------------------------------------+
| 1. RECORD CREATION                                                                |
| Institution Controller -> Finalizes Student Grades & Intake Verification           |
|                                                                                   |
| 2. CRYPTOGRAPHIC SIGNING (Issuer Level)                                           |
| Payload = { APAAR_ID, Student_Roll_No, Degree, Division, IssueDate, Issuer_ID }   |
| Signature = Sign_RSA_SHA256(Payload, Institution_Private_Key_HSM)                 |
|                                                                                   |
| 3. CERTIFICATE GENERATION & SECURE QR PACKAGING                                   |
| Printed Certificate displays:                                                     |
|  - Student Name, Institutional Roll No, APAAR ID                                  |
|  - Award Details (Degree, Branch, Class)                                          |
|  - Secure 2D QR Code: Contains base64url(Compressed(Payload + Signature))         |
|                                                                                   |
| 4. VERIFICATION WORKFLOW                                                          |
| Scanned via DigiLocker / Verification Portal:                                     |
|  a. Parse Payload and Signature from QR or Signed PDF                            |
|  b. Fetch Issuer Public Key from AICTE / DigiLocker Trusted Key Registry           |
|  c. Verify Cryptographic Integrity: Verify(Payload, Signature, PublicKey) == VALID|
|  d. Query Revocation Status: IsRevoked(Certificate_Serial_No) == FALSE            |
|  e. Display Authenticity Banner: "VERIFIED ORIGINAL ISSUED BY [INSTITUTION NAME]"|
+-----------------------------------------------------------------------------------+
```

---

## 6. Alternatives and recommendation

### Alternative 1: Public Direct QR Verification vs Scoped Token-Based Verification
- **Option A (Plain Public URL in QR):** QR code points to `https://platform.aicte.gov.in/verify?apaar=123456789012`.
  - *Drawback:* Anyone photographing the certificate can query the URL and continuously monitor or scrape student data. Violates data minimisation.
- **Option B (Cryptographically Encapsulated Self-Contained QR + Token Gateway - RECOMMENDED):**
  - QR code contains the signed payload itself (verifiable offline using public key without pinging server) OR an ephemeral token requiring student-consented scope.
  - *Benefit:* Zero tracking, offline verifiable, zero data leakage of unneeded attributes.

### Alternative 2: Plaintext APAAR Database Storage vs Salted Blind Indexing
- **Option A (Plaintext Storage):** Store 12-digit APAAR ID in SQL database tables.
  - *Risk:* SQL injection or backup leak exposes millions of national student IDs.
- **Option B (Encrypted At Rest + Salted Blind Index - RECOMMENDED):**
  - Store APAAR encrypted (AES-256-GCM).
  - Searchable using HMAC-SHA256(`APAAR`, `System_Pepper`) for exact match queries.
  - Plaintext decrypted only in memory when displaying to authorized user.

---

## 7. Unknowns and blockers

| Question | Impact | Next action | Dependency owner | Status |
|---|---|---|---|---|
| Does DigiLocker provide an open sandbox API for automated institutional bulk verification, or only manual/OIDC portals? | Determines whether batch verification is real-time or simulated in MVP | Review partner Sudhan to inspect DigiLocker/NAD partner API specs | Sudhan | Open |
| What specific exception provisions exist under DPDP Act for regulatory education archives (retention of student records post withdrawal)? | Determines exact data purge workflows upon student consent revocation | Cross-check Section 7 ("Certain legitimate uses") of DPDP Act 2023 | Sudhir | In progress |
| Does AICTE currently issue standardized X.509 digital certificates to all approved institutions for document signing? | Determines whether platform must provide a Certificate Authority (CA) or trust existing institutional PKI | Discuss with Kanishkar and Pranav on AICTE portal PKI standards | Kanishkar | Open |

---

## 8. Handoff

- **To Dharanish (Role 4 - Data Architecture):** Handing off the **Data Inventory (Section 5.2)** and **Multi-Tenant Isolation Constraints (Section 5.1)**. Ensure database schemas include `institution_id` partition keys and enforce encrypted storage for APAAR numbers.
- **To Sudhan (Role 2 - APAAR/DigiLocker Integration):** Handing off the **Third-Party Consent Flow (Section 5.4)** and verification token lifecycle. Validate with DigiLocker NAD specifications.
- **To Gopika (Role 1 - User Workflows & Dashboards):** Handing off the **Role Permission Matrix (Section 5.1)** to ensure UI dashboards enforce appropriate role views (e.g. masking sensitive fields from unauthorized operators).
- **To Kanishkar (Team Lead):** Handing off the threat model, privacy architecture, and open blockers regarding institutional PKI trust anchors.

---

## 9. Review

- **Review status:** Awaiting human peer review by Sudhan and Kanishkar B.
- **AI-use note:** Drafted with AI research assistance using verified primary statutes ([SUH-001](sources.csv), [SUH-004](sources.csv)) and verified technical models ([SUH-002](sources.csv), [SUH-003](sources.csv)). No human review has been recorded yet.
