# Proposed permission, data and credential design

All contents are design proposals unless explicitly attributed to a source. No described control is implemented or tested. The legal evidence and unresolved application decisions are in [legal-status.md](legal-status.md).

## Permission matrix

Default decision: deny. Evaluate authenticated actor, active role, institution scope, resource ownership, purpose, case assignment and current grant on every API, file, export and worker action. A caller-supplied institution ID never establishes scope. This follows [OWASP authorisation guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) (SUH-109).

| Actor | Allowed action | Resource boundary | Explicitly unavailable |
|---|---|---|---|
| Institution operator | Stage/validate uploads; propose corrections; see row errors | Assigned institution and programme permissions; own batches | Other institutions' students; self-approval; issuer keys |
| Institution approver | Review diffs; attest submit/correction; request withdrawal | Own institution; distinct approver for sensitive changes | Editing history; silent approval of own bulk action |
| Authorised regulator analyst | Aggregate monitoring; open assigned compliance cases | Approved jurisdiction/purpose; masked details until needed | Unlimited national browsing by default |
| Regulator case reviewer | Inspect minimal overlap evidence, request clarification and record resolution | Named case plus documented authority | Employer-style reuse; exposing another institution to unassigned staff |
| Student | See own submitted claims and evidence status; challenge errors; choose/withdraw sharing | Strongly bound account-to-student relation | Editing authoritative college/provider claims directly |
| Lawful guardian / assisted operator | Act on verified delegation with visible audit | Scope and duration of approved relationship; student accessibility needs | Permanent broad access inferred from disability or relationship assertion |
| Employer / other verifier | Request a narrow purpose; view an approved claim; check current status | Verified organisation/account plus unexpired recipient-bound grant | Search by APAAR; national history; unrestricted bulk export |
| Awarding-body issuer | Issue/reissue/revoke its own award attestation | Approved issuer and signing scope | Signing as AICTE/another awarding body; treating enrolment as a degree |
| Platform support | Diagnose batch/status and masked metadata | Time-limited support case; supervised escalation | Routine raw student access; downloading national dataset |
| Service worker | Validate a bounded batch; publish transactional events | Job tenant and minimal service role; no end-user impersonation | Omnipotent shared admin database connection |
| Security auditor | Read protected security events and access decisions | Audit mandate; minimum identifiers; independent log access | Routine admission data modification |
| Public visitor | Read product information and issuer directory | Public non-personal metadata | Student record existence, private verification result or full identifier |

Institution administrators may grant only roles within their institution and an approved permission ceiling. Staff removal disables active sessions and queued exports. Sensitive overrides require a reason, second approval, expiry and a later review.

## Tenant and cross-institution boundaries

Use tenant-scoped keys and constraints in the database, server-derived session scope, row-level policies as defence in depth, scoped object-storage paths, short-lived downloads, and tenant-aware queue messages. Tests must include connections reused by a pool, batch jobs, cache keys, reporting endpoints, and orphaned files. A successful user API denial does not prove worker isolation.

Keep the cross-institution collision index behind a dedicated service role. A plain hash of a low-entropy national identifier is not anonymisation; use a keyed matching token with access-controlled keys and versioned rotation, while protecting the authoritative value separately. Such tokens remain linkable personal data. Do not give institutions a free matching query. Process only justified submissions and enforce quotas and anomaly detection. Return a uniform receipt for every accepted batch: even an opaque case reference shown only on collision would reveal a match bit. Cross-institution cases remain internal to an authorised reviewer. Any institution clarification concerns its own supplied record and reveals neither a match result nor another institution. A regulator reviewer sees minimal conflicting evidence only after case assignment and authority checks. No other institution name, programme or student profile appears to an ordinary uploader. False/collusive submissions remain an operational risk even with cryptography.

Separate three status dimensions: `institution_attestation`, `provider_evidence`, and `review_resolution`. Add freshness and source timestamps to each. A format pass cannot set provider evidence. A missing provider link cannot automatically revoke an institution's admission record.

## Data inventory and retention

Retention values below are proposed operational ceilings for transient copies, **conditional on the signed legal retention schedule**. They are not statutory periods. Any required evidentiary copy goes to a restricted retention store, not ordinary logs. Before real processing, reconcile the applicable one-year future Rules and current directions described in legal-status.md; do not blindly deploy a 7-day delete job against a legal hold or a required retained record.

| Data | Purpose / source | Visibility | Proposed lifecycle and unresolved decision |
|---|---|---|---|
| Internal random student reference | Stable local relationships / service | Scoped staff and student | Keep with authorised record; not public identity |
| Claimed APAAR and linkage status | Academic identity reference / institution, optionally authorised provider | Full value only where needed; masked normal UI | Encrypted separately; retain per approved academic-record schedule; no public hash |
| Provider subject / linkage evidence | Bind authorised account to local case / provider response | Integration service and assigned reviewer | Store minimal source, time, result, evidence reference; delete unnecessary response fields immediately |
| Name / required identity-match fields | Reconcile record / institution and approved source | Student and assigned reviewers | Do not request extra address, picture or academic history merely because API returns it |
| DOB or age evidence | Age workflow / authorised source | Restricted matching/guardian workflow | Prefer derived under-18 status where exact DOB unnecessary; preserve provenance of derivation |
| Institution, programme, year, effective dates, enrolment status | Reporting / institution attestation | Institution; approved regulator view; selected student disclosure | Versioned history; retention duration decided by record owner and applicable duty |
| Seat category and nationality/status | Applicable rule checks / institution | Scoped compliance users | Separate concepts; no employer disclosure by default; evidence only when needed |
| Approval version and provenance | Explain rule decisions / authoritative approval | Rule administrators, institutions, regulator | Retain versions needed to reproduce historical decisions; no assumed perpetual student-data retention |
| Upload object and parsing error rows | Correct input / institution | Batch owner/approver only | Working copy target 7 days after acceptance; unaccepted batch target 30 days, subject to approved evidence/hold policy |
| Access/refresh tokens, secrets | One authorised provider transaction / provider | Secret vault and integration service | Prefer no refresh-token persistence in MVP; delete/revoke when no longer needed; never logs/source control |
| Disclosure grant and receipt | Prove purpose, recipient, fields and withdrawal / student | Student; recipient only its grant; audit role | Grant default 24 hours in synthetic demo; real TTL is policy-configurable; receipt retention reviewed separately |
| Credential status and version reference | Detect supersession/revocation / issuer | Approved verifier sees status only | Keep sufficient status history for active credentials and approved records duty; avoid tracking endpoint per student |
| Audit/security event | Accountability and incident handling / service | Security/audit roles | Event IDs, actor, action, purpose, resource token, result and time; no raw payloads; legally approved retention and India log location if applicable |
| Aggregate reports | Monitoring / accepted records | Approved analysts | Suppress small cells and limit repeated slicing; no claim that aggregation always anonymises |
| Backups | Recovery / service | Restricted operations | Encrypted; deletion/hold manifests applied on restoration; tested expiry and recovery before pilot |

Do not collect Aadhaar numbers, biometrics, wallet PINs or OTPs in this application. Use the provider's authorised authentication experience when available. This is an MVP minimisation choice, not a blanket statement about all lawful government processing.

## Student and employer disclosure journey

1. Employer E authenticates under a vetted organisation and states a purpose, required claim, expiry and recipient identity. It cannot search students by APAAR.
2. Student S opens the request from their own account or a non-revealing invitation, sees plain-language purpose and the exact fields, and can decline without altering the admission record. Provide an assisted route that does not require sharing passwords.
3. If new provider evidence is needed, an approved requester initiates the code flow. Use transaction-bound state, S256 PKCE and exact redirects; validate issuer, audience, signature, expiry and subject if an ID token is used. [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html) (SUH-112) and [RFC 8725](https://www.rfc-editor.org/rfc/rfc8725.html) (SUH-113) inform these checks.
4. The adapter binds returned evidence to the case, checks the local claim and lets an authorised reviewer resolve mismatch. Requester v2.4's account-linked APAAR route is documented, but the needed provider permission and production access are unconfirmed (SUH-114). Never invent a scope or translate `apaar_not_linked` or `apaar_not_available` into nonexistence. The endpoint strongly recommends one call after token acquisition; confirm retry/refresh permission rather than polling. Its academic details concern deposited credits and are not an exhaustive current-admissions registry. Discard unrelated response fields; preserve only the authorised evidence needed for this case.
5. S approves a separate platform disclosure grant specifying recipient, purpose, fields, record revision, expiry and permitted view/download. Provider OAuth consent is not automatically an employer-sharing grant. Call this a permission feature, not a registered DPDP Consent Manager.
6. E authenticates again at retrieval. The server checks grant and record state on every request; the URL alone is not a bearer permission. Return the minimal assertion with source/issuer, evidence category, version, issuance/check times and current status.
7. S can revoke future access through the same account view. Deny subsequent retrieval; schedule provider revocation where applicable; explain any legally retained evidence. Do not promise to erase copies E already downloaded.
8. Student corrections route to the authoritative institution/provider. Show acknowledged, under review, corrected or reasoned refusal states; disclose only the case information needed by the requester.

Use opaque, high-entropy invitation references; store only token digests where feasible. Avoid personal identifiers in URLs, referer headers, browser titles and analytics. Set no-store responses and prevent referrer leakage. Keep scope checks server-side even when the UI hides unavailable fields.

## Credential and verification lifecycle

**Issuer authority:** verify institution/awarding-body identity and signing mandate out of band before enrolling a real issuer. Platform-generated evidence in a demo is explicitly `SYNTHETIC DEMO ISSUER`; it is not an official degree or AICTE certificate. An enrolment attestation has a different type from an academic award.

**Issue:** bind the minimum assertion to an immutable record revision and evidence references; include issuer ID, credential ID, schema/type, issue time, status reference and expiry where appropriate. A service signing key signs a defined byte representation using a maintained library. Restrict algorithm and issuer allowlists; do not use a token-supplied key URL without validation. A valid signature from an untrusted issuer is insufficient.

**Key custody:** separate test and live keys; production private keys in managed key storage, never repository or ordinary database exports. Two authorised roles approve key enrollment and emergency rotation. Publish a trusted issuer-to-key mapping with version and validity interval; retain old public keys for historical verification while marking compromised keys and the affected interval. A lost signing key requires suspension and investigation, not silent regeneration.

**Verify:** check structure, expected credential type, signature, issuer authority, evidence scope, temporal validity, current status, recipient grant and replay binding. Return `valid current issuer assertion`, `superseded`, `revoked`, `expired`, `untrusted issuer`, `integrity failure`, or `status unavailable`; avoid a universal green identity/admission badge.

**Correct/revoke:** a correction creates a new revision, supersedes the old assertion and updates status atomically with an outbox event. Rollback and replay cannot restore an old grant or claim. Authorised issuers can suspend for investigation and record reason in restricted history; public status does not expose the student's dispute details.

**QR / paper / offline:** a printed QR contains only an opaque reference to the verification entry point. Certificate display of APAAR plus institutional ID remains awarding-body controlled and conditional on confirmed requirement/policy; do not expose either through public QR retrieval. An offline verifier may establish signature validity at the included timestamp, but cannot assert current revocation state, latest corrections or ongoing permission without a fresh trusted status check. The final UI must say so.

Use an online authenticated assertion for MVP. [W3C VC 2.0](https://www.w3.org/TR/vc-data-model-2.0/) and [Bitstring Status List](https://www.w3.org/TR/vc-bitstring-status-list/) (SUH-107/108) are later interoperability candidates, not a claim that a JSON object or QR is a conforming VC.

## Pilot entry and exit gates

Before real records: named accountable operator; data-sharing/processor agreements; lawful basis and field mapping; age/guardian design; approved provider access; issuer mandate; retention schedule; student grievance owner; incident contact; current legal review. Pass negative permission tests across API/jobs/files/exports, secret/log scans, dependency review, upload abuse tests, backup restore/deletion tests and credential revocation/key-rotation exercises. Commission an independent security assessment appropriate to deployment scope.

Pilot only a named institution/programme/cohort with limited operators and rollback. Record actual error/review times, user comprehension, unauthorised-access attempts, false alerts, correction outcomes and exclusion complaints. Stop expansion on cross-tenant disclosure, silent record overwrites, irreversible wrongful rejection, unresolvable identity binding or failed revocation. Expansion needs measured evidence and human approval, not agent consensus.
