# Integration evidence review and completion

**Human owner:** Sudhan. **Author:** integration_research AI agent, 2026-10-26, Asia/Kolkata.
**Completion audit:** integration_finish AI agent, 2026-10-27, Asia/Kolkata; retained research-round date 2026-10-26.
**Status:** all six assignment questions addressed through desk research and proposed contracts; live integration, human review and field validation remain pending.
**Original contribution:** [preserved verbatim](original-2026-10-25/findings.md), repository baseline `5ee5d57`. Corrections below supersede conflicting statements in that original.

## Recommendation

Use institutional enrolment evidence plus a separately authorised, account-linked APAAR check. An official **September 2026** requester specification documents this check, but it is **not an arbitrary APAAR-number lookup** and does not grant this team access. The demo should therefore use a clearly labelled simulated provider adapter until sponsorship, permission and integration tests exist. [SUD-105](https://cdn.apisetu.gov.in/portal/assets/Requester-MeriPehchaan-APISpecificationv2.4.pdf), [SUD-106](https://cf-media.api-setu.in/resources/Partners-SOP.pdf).

Keep four independent evidence dimensions: input format, provider account linkage, institution-reported enrolment and policy review. Success in one must not silently upgrade another.

## 1. Ecosystem and proof boundaries

| Component | Inspected evidence | Implication |
|---|---|---|
| APAAR | Lifelong 12-digit academic identifier linked to ABC/DigiLocker. [SUD-101](https://apaar.education.gov.in/faqs) | Shape alone establishes neither issuance nor ownership. No inspected APAAR specification establishes Verhoeff. |
| ABC | Credit storage/transfer using APAAR; current portal describes student creation/correction and awarding-institution registration. [SUD-102](https://www.abc.gov.in/) | Credits are not a live admission register. Preserve provenance when mapping historical ABC-ID fields. |
| NAD | Institutions lodge awards; students retrieve/share them through DigiLocker. [SUD-103](https://nad.digilocker.gov.in/faq) | Award authenticity is distinct from current enrolment and policy eligibility. |
| DigiLocker / Meri Pehchaan | Requester access binds permission to an account and permitted evidence. [SUD-105](https://cdn.apisetu.gov.in/portal/assets/Requester-MeriPehchaan-APISpecificationv2.4.pdf) | A successful session is not absolute proof about a physical applicant. |
| API Setu | Official provider documentation and partner entry point. [SUD-104](https://apisetu.gov.in/digilocker) | Documentation availability is not authorisation. |
| Institution / awarding body | The proposed design identifies the source asserting enrolment or issuing an award. | A project QR/signature cannot create the issuer's statutory authority. |

## 2. Current API discovery

The official resource index links Meri Pehchaan requester **v2.4, September 2026**, requester v1.12, issuer v1.13, terms and SOP. The v2.4 revision date is **2026-09-09**. [SUD-104](https://apisetu.gov.in/digilocker).

Inspected v2.4 printed pp.4–8 describes authorisation code, S256 PKCE, exact redirect, state, purpose/service name and optional OpenID. Printed pp.16–19 specifies `GET https://digilocker.meripehchaan.gov.in/public/oauth2/1/apaar`: bearer token, **no parameters**, returning the account's `apaar_id`, `student_details`, `academic_details`. Errors distinguish token/scope failure from not-linked/unavailable data. The revision history removes Verify Account. [SUD-105](https://cdn.apisetu.gov.in/portal/assets/Requester-MeriPehchaan-APISpecificationv2.4.pdf).

The operation recommends one call after acquiring the token. Do not design repeated background polling as an established capability; confirm retry and refresh arrangements during onboarding. Its academic fields describe institutions, courses and deposited credits. **Interpretation:** this does not establish an exhaustive, current admission register, sanctioned intake, or every concurrent enrolment; keep institution assertions and scoped policy evidence separate. [SUD-105](https://cdn.apisetu.gov.in/portal/assets/Requester-MeriPehchaan-APISpecificationv2.4.pdf), printed pp.16–18.

This was a normal unauthenticated PDF download (HTTP 200) after the web reader returned 403. PDF pages 17 and 20 (printed 16 and 19) were visually checked. **No API request or account creation was performed.**

**Ambiguities:** revision history says token-v1/refresh APIs were removed in v2.0, while later body pages retain descriptions. No exact APAAR scope name is specified in its operation section. One error example uses 500 while the table lists 530. Do not invent `apaar.read`, assume `openid` grants every permission, or adopt legacy refresh semantics without provider confirmation. The design proposes the v2 authorisation-code path and safe handling of unknown service errors.

## 3. Operation-by-operation matrix

“Documented” means inspected specification only. **Credentials available: none evidenced. Live calls tested: none.**

| Operation | Evidence and access | Response/proof boundary | Proposed fallback |
|---|---|---|---|
| Institution upload/update | Institution-specific CSV/ERP contract; no AICTE national API established here | Authenticated institution assertion, not government acknowledgement | Synthetic CSV/internal API; distinguish local acceptance from official submission. |
| APAAR shape | SUD-101; offline ASCII `^[0-9]{12}$`, with explicit previewed cleanup | Format only; no checksum and no invented ID | Missing value creates pending linkage case. |
| Student authorisation | SUD-105 authorisation/token-v2 sections | Approved client, registered redirect, minimal approved grant; token-bound account | Persistent SIMULATED label and synthetic fixture. |
| Account-linked APAAR | SUD-105 Get APAAR Details | Compare returned and submitted ID within the bound enrolment case; not global ID search | Match/mismatch/not-linked/unavailable fixtures. Manual review cannot become provider verification. |
| Selected academic award | SUD-105 issued documents/file/XML; SUD-103 | Permitted issuer evidence; XML not universal; self-uploaded scan has different trust | Synthetic issuer fixture and explicit source type. |
| Lodge/correct award | SUD-103 correction question and SUD-104 issuer resources | Separate issuer/institution authority; confirm current template | Our correction ledger only; do not claim NAD publication. |
| Correct APAAR details | SUD-102 update guidance | Provider/source correction, not an edit made by our service | Guided source correction; re-link after success; supersede old evidence. |
| Expire/revoke grant | SUD-105 revocation and consent expiry sections | Stop new access; retention of existing institutional records has a separate basis | Expiring disclosure and safe metadata; security owner defines retention. |
| AICTE approvals/readback | No accessible production contract verified | Needs authoritative course/year approval and submission receipt | Versioned approval fixture/export preview marked awaiting official submission. |
| Cross-institution overlap | Proposed regulated service, not discovered APAAR API | Needs lawful regulator-wide authority | Fictional two-tenant dataset; own-case action request only for institution. |
| Employer verification | SUD-103 verifier registration and permission | Organisation authorisation plus purpose-specific student grant | Minimal, expiring disclosure; no raw-ID search. |

## 4. Onboarding, sponsor and sandbox reality

The **5 June 2024** SOP requires an eligible organisation, authorised representative, official-domain email, vetted use case, terms/agreement, approval and integration tests. Section 5(vi), PDF p.4 excludes temporary testing access. An eligible sponsor and provider-approved route are therefore dependencies; hackathon participation alone is insufficient. [SUD-106](https://cf-media.api-setu.in/resources/Partners-SOP.pdf).

An older linked configuration manual names demo portals; the March 2025 support FAQ says there is no separate environment in its test-bed answer. This conflict means a public sandbox must not be promised. Confirm approved testing arrangements with the provider. [SUD-107](https://cdn.apisetu.gov.in/portal/assets/workflow_requester.pdf), [SUD-108](https://www.digilocker.gov.in/assets/FAQ%20DL%20EL_onboarding.pdf).

**Access ladder:** documentation → sponsor/use-case approval → credentials/scopes → authorised testing → operational acceptance. This research reaches documentation only. Sponsor/access dependency does not prevent a synthetic research demonstrator.

## 5. Verification states and outage handling — proposed design

Store evidence objects rather than one progressive verified badge:

- Check kind: FORMAT / ACCOUNT_LINK / INSTITUTION_ASSERTION / POLICY / CREDENTIAL.
- Result: NOT_CHECKED / PENDING / MATCH / MISMATCH / DENIED / UNAVAILABLE / NOT_LINKED / REVIEW_REQUIRED / SUPERSEDED.
- Provenance: source and contract version, evidence reference, checked time, effective period/expiry, correlation ID, mode LIVE or SIMULATED.
- Minimal retained payload: approved identifiers/claim results only; no OAuth token, raw APAAR, full academic history, phone or email in generic logs or QR.

A provider outage can coexist with valid input. A confirmed account link can coexist with a disputed enrolment. Historical snapshots remain immutable; corrections create revisions with reasons and authorised actors.

| Trigger | Proposed response | Never infer |
|---|---|---|
| Consent declined/expired | Explain unavailable permission; reconnect or permitted alternative | Fraud |
| Token failure (401) | Reauthorise if appropriate; bounded retry | Missing student |
| Insufficient scope (403) | Permission dependency/support route | Broader guessed scope is authorised |
| APAAR not linked or unavailable (404) | Account/data correction route | Registry-wide nonexistence |
| Timeout/throttle/service error | Bounded backoff, visible last-checked/stale time, preserved work | Invalid student |
| Unexpected schema/version | Quarantine mapping; safe diagnostics; unable to verify | Missing fields equal zero or false |
| Returned ID differs | Discrepancy review; do not merge automatically | Identity theft proven |
| Corrected provider record | New evidence version; supersede prior linkage | Historical assertions can be overwritten |

Provider-specific error distinctions come from SUD-105; proposed states, retry controls and case actions are our design. Actual rate limits, service guarantees and re-check intervals require provider/institution agreement.

## 6. Missing IDs, foreign learners and correction

The school-oriented APAAR FAQ uses school records and parental consent; this does not establish a higher-education exemption or deadline. ABC's current portal gives DigiLocker-based creation and correction guidance. [SUD-101](https://apaar.education.gov.in/faqs), [SUD-102](https://www.abc.gov.in/).

NAD's FAQ permits award publication without Aadhaar and describes foreign/NRI certificate access through supported accounts or institution/support assistance. It also documents correcting an award through `MARKS REC STATUS=M`. These are **award routes**, not a universal APAAR-issuance pathway. The FAQ mentions both standard CSV ingestion and secure bulk APIs; do not interpret its earlier CSV-only wording as universal. [SUD-103](https://nad.digilocker.gov.in/faq).

**Proposal:** use an internal student reference with pending/eligibility-review linkage state, reason, responsible office and correction queue. Do not fabricate APAAR, substitute Aadhaar, invent a deadline or automatically deny admission. Whether a final regulator submission may omit the ID remains unresolved.

## 7. Correction ledger for the original contribution

| Prior pattern | Current disposition |
|---|---|
| Verhoeff enforced or shown as APAAR warning | Withdraw. No inspected provider evidence; even a warning would create false work. |
| General APAAR registry lookup available | Replace with documented token-account operation; no arbitrary-ID parameter. |
| 404 proves nonexistent ID | Withdraw; not-linked and unavailable have different meanings. |
| OTP/name match proves physical applicant identity | Narrow to provider/account evidence; account compromise and mismatch remain. |
| Two full-time enrolments are illegal | Withdraw blanket claim; [Pranav](../pranav/findings.md) establishes legitimate simultaneous-programme cases. |
| “Admission sanctioned” follows identity and quota | Replace with evidence/rule findings; authorised humans/institutions decide admission. |
| CBSE school relaxation applies to HEI/foreign applicants | Withdraw scope transfer. |
| Architecture is fully DPDP compliant | Withdraw; see [Sudhir](../sudhir/findings.md); proposal is not compliance certification. |
| Aadhaar licensing/cost/storage claims are sufficient to choose direct verification | Not relied upon or revalidated; direct Aadhaar integration is outside proposed MVP. |
| All NAD ingestion must be CSV | Qualify against same FAQ's bulk API statement; active agreement/template controls. |
| Historical source entries were verified | Preserve as contributor claims; the new register flags limits and superseding evidence. |

## 8. Synthetic contract scenarios and future experiment

[contract-scenarios.csv](contract-scenarios.csv) provides 12 **designed, unexecuted** fictional cases covering normal and failure paths. It contains no real identifiers and is not provider acceptance evidence.

A later authorised experiment should trace: minimal consent → code exchange → account-linked evidence → mismatch/pending outcome → revocation → denied re-fetch. Record sponsor approval, pinned contract, approved synthetic/test identities and redacted response evidence. Execute only after provider authorisation; published documentation alone is not enough.

## 9. External dependencies and exact questions

| Question | Owner | Safe consequence while open |
|---|---|---|
| Which legal organisation sponsors this use case? | Human lead/institution | SIMULATED provider mode |
| Which scope permits v2.4 APAAR details; which fields and retention are approved? | Sudhan + provider | Minimal design only; no live access claim |
| Which test account/environment is approved? | Sponsor/provider | Synthetic local fixtures |
| How are legacy token sections and 500/530 ambiguity resolved? | Provider | No fragile production assumptions |
| What route applies to foreign/missing APAAR for intended courses? | Sudhan + Pranav | Pending case, no invented eligibility result |
| What current AICTE upload/readback/receipt contract exists? | Sponsor/AICTE | Local acceptance separate from national submission |
| Who may see cross-institution matches? | Sudhir + policy authority | Strict tenant isolation |
| Who corrects identity, enrolment and awards? | Provider/institution/awarding body | Separate queues and provenance |
| What is official SIH26263 wording? | Lead | Supplied baseline; see [verification note](../../docs/official-problem-verification.md) |

## 10. Checks, critique and handoff

- All six assignment questions addressed; sources include primary pages and actual provider PDFs.
- Completion audit on 2026-10-27 reopened the APAAR FAQ and API Setu resource index successfully; the official SIH listing still returned HTTP 403. SUD-101 correctly maps to Gopika's GOP-001 FAQ reference; no source renumbering is needed.
- v2.4 SHA-256: `430efeefe67068500ef29fcc6497cc281822ffb5c802f43db22f3c20033fafff`.
- SOP SHA-256: `3014a076c44116ad927dfe92451657bf42a2a68cb33d3159fb8d10c0ed6c1faa`.
- Hashes identify inspected files, not government digital signatures. Full provider publications are not reproduced in the repository.
- Archived findings and source ledger have the same Git blob hashes as baseline `5ee5d57`; the original contribution is unchanged.
- **AI critique actually exchanged:** policy agent corrected dual-enrolment claims; security agent required account-to-case binding, payload minimisation and distinct employer grants. No human approval is implied.
- **Completion critique exchanged:** the lead, security and policy agents were asked to preserve institution claims and correction cases without claiming arbitrary or batch provider validation. This is AI review feedback, not approval by Sudhan, Sudhir or the human team.
- **Dharanish:** independent check dimensions, stable internal key, revisioned evidence, account-linked adapter, no fake registry endpoint.
- **Gopika:** source-specific correction routes are documented; separate manuals do not prove existing end-to-end integration.
- **Sudhir:** provider grant and employer disclosure are different purposes; explicit scope confirmation and minimisation are required.
- **Lead:** the feasible contribution is explainable, correctable, evidenced reporting. The new API improves the future integration path, not the current validation status.

No interviews, real student records, credentials, production calls, performance tests, human review or measured field impact were obtained.
