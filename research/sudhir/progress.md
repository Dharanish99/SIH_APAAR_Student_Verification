# Progress — Sudhir

**Current status:** In progress (50% milestone: foundational research, permission matrix, data inventory, threat models, and verification architecture drafted)  
**Next action:** Validate DigiLocker/NAD API integration models with Sudhan (Role 2) and coordinate encrypted APAAR database schema with Dharanish (Role 4).  
**Blockers:** Awaiting confirmation of DigiLocker sandbox availability for automated institutional bulk verification.  
**Handoff:** Data Inventory & Multi-Tenancy isolation constraints sent to Dharanish; Credential verification lifecycle sent to Sudhan; RBAC matrix sent to Gopika.

## Update log

### 2026-10-26 — Foundational research & 50% milestone completion
- **Question investigated:** What can each actor do, how do institutional boundaries isolate records, what does an APAAR ID reveal to unauthorized parties, how does the DPDP Act 2023 govern student data/minors, and what threat models/credential verification flows apply?
- **Work actually completed:**
  - Formulated and answered the core defense question: an APAAR ID alone yields zero data to an unauthorized actor.
  - Constructed comprehensive Role/Action/Resource Permission Matrix (RBAC + ABAC) spanning institutional operators, principals, AICTE regulators, students, parents/guardians, third-party verifiers, and administrators.
  - Created Student Data Inventory with minimization rationale, retention bounds, and strict prohibition on raw Aadhaar/biometric storage.
  - Modelled 8 realistic threat abuse cases (including ID enumeration, horizontal tenant escalation, certificate forgery, and minor consent withdrawal) with mitigations and residual risks.
  - Designed the credential verification and QR-code display lifecycle compliant with IT Act 2000 digital signature provisions.
  - Worked through 1 normal case and 3 failure/edge cases (including ID enumeration attack and minor student consent workflows).
- **Evidence added (source IDs):** [SUH-001](sources.csv), [SUH-002](sources.csv), [SUH-003](sources.csv), [SUH-004](sources.csv) in `sources.csv`.
- **Key finding or remaining uncertainty:** Knowing an APAAR ID yields zero data; processing minor data (<18) requires verifiable parental consent under DPDP Act Sec 9. Uncertainty remains regarding whether AICTE operates its own PKI CA or trusts individual university CAs.
- **Files changed:**
  - [findings.md](findings.md) (Full draft of sections 1 through 9)
  - [sources.csv](sources.csv) (Added authoritative primary source records SUH-001 through SUH-004)
  - [README.md](README.md) (Updated status to In progress and checked off drafted outputs)
  - [progress.md](progress.md) (Recorded progress and log)
- **Review/handoff needed:** Handoff to Dharanish (Data schema), Sudhan (DigiLocker integration), Gopika (UI dashboards), and Kanishkar (Architecture). Human peer review pending from Sudhan and Kanishkar B.
- **Next action:** Investigate DigiLocker sandbox integration options with Sudhan and review DPDP Act Section 7 statutory exemptions for permanent academic records.
