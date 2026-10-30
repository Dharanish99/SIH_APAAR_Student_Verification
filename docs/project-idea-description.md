# SetuTrace — Project Idea Description

**Expanded design brief · SIH26263 supplied brief · prepared 30 October 2026**

**Idea:** SetuTrace is an explainable evidence and correction layer for student reporting. It helps institutions reconcile enrolment records, lets students challenge incorrect institutional claims, gives approvers reproducible reporting snapshots, and shares only permitted, current assertions with named verifiers.

This description draws on the six research workstreams, preserved source trail and experiments in the separate research repository, and the implementation boundary in the prototype repository. The core synthesis below records the proposal as of 27 October 2026; later sections reconcile it with the focused prototype built on 28 October. “SetuTrace” remains a working name. SIH26263 is the team-supplied planning baseline; official wording and submission terms were not independently verified. Proposed outcomes are distinguished from implemented behavior and measured evidence.

**Count convention:** exactly 50,000 Unicode code points in the UTF-8-decoded Markdown file, including its final newline. This is a character count, not a word count.

---
## Core research synthesis (27 October 2026)

## A correctable evidence trail for student reporting

**Idea report · SIH26263 supplied brief · Completed 27 October 2026**

Prepared by a separate AI design-thinking innovator after the six research workstreams were assembled. Human workstream ownership remains as recorded in [team.json](../team.json); Kanishkar B is the human team lead. Research began 26 October. This is the 27 October research proposal for human review. At that stage no application had been implemented. The [28 October submission prototype](https://github.com/Dharanish99/SIH_Project_Prototype) now implements a focused subset; see [actual test evidence](TESTING.md). No provider credentials, live government integration, interviews or field pilot are claimed. SetuTrace is a working name, with no claim of official affiliation or name clearance.

**Recommendation:** build a narrow reporting and correction layer alongside institutional systems. Its useful output is an explainable submission snapshot: which enrolment records were counted, which approval and rule versions were used, what remains unresolved, and who can correct it. APAAR helps connect authorised evidence; it does not become a universal admission verdict.

The [ten requirements](problem-brief.md) come from the supplied statement. The official SIH page remained inaccessible during research, so final wording, event dates and submission conditions are **unverified**. Resolve this before submission; do not substitute a third-party listing for organiser confirmation. [Official verification record](official-problem-verification.md).

## 1. The problem worth solving

The problem is not simply that colleges lack software. Samarth already documents student imports, validation, allocation and edits. NAD already supports issuer-published academic awards and authorised sharing. AISHE collects programme-level intake and enrolment aggregates. These sources establish existing capabilities; they do not establish how consistently a particular institution reconciles them. [Samarth STU-001, GOP-103](https://docs.samarth.ac.in/docs/academics/student/); [NAD FAQ, SUD-103](https://nad.digilocker.gov.in/faq); [workflow research, GOP-110](../research/gopika/findings.md).

The proposed gap is the accountable handoff between a source record, a reporting total, a policy finding and a later correction. A total of 61 against a capacity of 60 is not useful enough unless a reviewer can reproduce the count and determine whether the cause is an extra admission, a replayed upload, a withdrawal, a wrong programme mapping or a revised approval.

For a student, the central need is to see and challenge an institution's claim without being excluded by a missing identifier. For staff, it is to complete reporting without entering the same facts again. For a regulator, it is to distinguish incomplete evidence from a substantive concern. For a verifier, it is to obtain a narrow current assertion from an authorised source. These are **design hypotheses**, informed by public workflows; their frequency and value have not been measured through interviews.

The proposed product succeeds only if it reduces total reconciliation work while preserving students' correction rights. More dashboards or more alerts are not success measures by themselves.

## 2. Alternatives and the selection

| Alternative | Useful strength | Main tradeoff | Decision |
|---|---|---|---|
| Replace the institutional ERP | One controlled workflow from application onward | High migration, training and integration burden; duplicates documented Samarth functions | Reject for this scope |
| Build an API-first national verification registry | Appealing single verification journey | Arbitrary-ID bulk lookup is not established; permission and source coverage remain external dependencies | Defer |
| Add SetuTrace beside existing systems | Imports existing records; preserves provenance, corrections and review | Mapping and reconciliation still cost time; operator governance is essential | Selected for evaluation |
| Improve spreadsheets, templates and checklists | Low setup cost; familiar to small institutions | Harder version control, access separation and correction propagation | Retain as baseline and possible final choice |

The selected approach is feasible without government API access because its first value is local evidence reconciliation. It does not prove superior value. If a small institution can meet its needs with an improved checklist and less effort, that is the better outcome there. The product must earn its extra complexity in comparative testing. [Gopika's opportunities](../research/gopika/findings.md); [Kanishkar's feasibility base](../research/kanishkar/findings.md).

## 3. Product concept and defensible differentiation

SetuTrace centres on an **evidence card**, attached to each report finding or student record. It displays four separate questions: what the institution asserted; what an authorised provider returned; what the applicable rule evaluated; and what a responsible reviewer resolved. Format, source, revision and freshness are visible. A signature adds integrity and issuer attribution; it does not make an incorrect assertion true.

The proposed differentiator is a connected correction trail: source revision → rule evaluation → approved reporting snapshot → later correction → superseded output. Staff can explain a changed total; a student receives a case reference; an authorised reviewer can reconstruct an earlier decision. This is a product hypothesis, not a claim that competitors lack all such functions. The research did not exhaustively inspect every Samarth deployment or NAD integration.

Samarth remains the local operational system. NAD remains the appropriate authorised award infrastructure. SetuTrace's first receipt describes an institution's enrolment assertion and reporting state, not a degree, official AICTE acknowledgement or NAD publication. [GOP-F01–F06](../research/gopika/findings.md); [credential trust design](../research/sudhir/privacy-design.md#credential-and-verification-lifecycle).

## 4. Journeys designed around people

### Institution staff and approver

An operator exports existing ERP data, chooses a saved mapping and previews changes before committing. Stable source keys distinguish a new enrolment from a replay or correction. Errors identify the field, reason and responsible action; staff do not repair the same value independently in two systems without a reconciliation record.

A separate approver reviews material differences, unresolved rows and the selected policy pack. Approval freezes an explicit snapshot. The dashboard distinguishes **locally accepted**, **export ready**, **submitted through an authorised route**, and **official acknowledgement evidenced**. A manually attached receipt records its uploader and provenance; it is not described as API readback. No current AICTE submission/readback contract has been established. [Dharanish's import protocol](../research/dharanish/findings.md); [SUD operation matrix](../research/sudhan/integration-review.md#3-operation-by-operation-matrix).

### Student, including missing or disputed APAAR

A student enters through an institution-approved account or assisted identity process and sees their own institution claims, evidence status and correction history. Access must not depend circularly on possessing the very APAAR being disputed. A missing or foreign-student linkage route creates an internal reference and a pending case; record capture continues. Whether a final regulator submission may omit APAAR remains unresolved.

The student can challenge a wrong course, date or identifier and receives an owner, status and reasoned outcome. They cannot silently overwrite an institution or provider record. Assisted access uses limited, recorded delegation, accessible language and keyboard/screen-reader support; disability does not imply incapacity. No invented deadline or automatic admission denial fills an unresolved policy gap. [Missing-ID research](../research/sudhan/integration-review.md#6-missing-ids-foreign-learners-and-correction); [permission design](../research/sudhir/privacy-design.md).

### Regulator analyst and case reviewer

An analyst starts with authorised aggregate views: reported count, policy coverage, unresolved evidence, reporting cutoff and data freshness. Counts reveal their denominator and incomplete population. A potential capacity breach opens an accountable review, not an automatic cancellation of the last student added.

Cross-institution matching is conditional on documented regulator authority. Matching cases remain internal to assigned reviewers. Every institution receives a uniform batch receipt; neither a special ticket nor a changed notification reveals that another institution has a matching record. Clarification asks only about the institution's own facts. Timing, exports and support responses need the same protection. Residual inference and collusion remain risks. [Security T03/T12](../research/sudhir/threat-model.md).

### Employer or other authorised verifier

A vetted verifier requests a purpose and limited fields. The student can approve or decline a separate disclosure grant naming recipient, fields, record revision and expiry. Declining does not alter admission. At retrieval, the service checks the recipient and current grant again and returns the source, assertion type, evidence date and status. A forwarded URL or QR alone grants nothing.

Withdrawal stops future service access, including pending exports once revocation commits; it cannot erase copies already downloaded. An unavailable status service produces an unavailable result, not a current-validity badge. Actual employer demand and institutional permission for this workflow remain unproven. [NAD verifier principles, SUD-103](https://nad.digilocker.gov.in/faq); [proposed disclosure lifecycle](../research/sudhir/privacy-design.md#student-and-employer-disclosure-journey).

## 5. Rules, exceptions and correction lifecycle

Use a versioned policy pack scoped to institution, campus, programme, entry route, cohort/year, jurisdiction and effective period. Each rule cites its authority, required inputs and exception route. Missing current authority yields `POLICY_UNAVAILABLE`; a historical percentage is never silently activated. The inspected AICTE base handbook came through an institution mirror, and current amendment completeness remains unresolved. [PRA-101–109](../research/pranav/sources.csv); [14-rule catalogue](../research/pranav/rule-catalogue.md).

Concurrent enrolments are not automatically invalid. UGC's modified guidance allows qualifying combinations and includes conditions for earlier programmes. Mode, timing, recognition and applicable council/university rules matter; the guidance excludes PhD. [UGC 2025 modification, PRA-103, guidelines 1–5](https://www.ugc.gov.in/pdfnews/6493421_UGC-Guidelines-pursuing-two-academic-programmes-simultaneously.pdf).

Nationality/status, candidature and seat entitlement remain separate. NRI, OCI, Foreign National, lateral-entry and other additional pools require their own applicable authority. There is no universal supernumerary percentage or shared extra-seat bucket. Worked cases explain why an apparent overlap or excess count can require correction rather than adverse action. [POL-03–06/12 and C15–C20](../research/pranav/worked-cases.md).

Correction follows **challenge → acknowledge → authenticate evidence → assign source owner → amend or explain refusal → re-evaluate → supersede affected outputs → appeal if contested**. Institution staff correct enrolment, the provider corrects academic identity, and the awarding body corrects an award. SetuTrace tracks these actions; it cannot repair external systems by itself or promise their turnaround.

Store event-effective time separately from recording time. For the inspected Maharashtra scope, an authenticated online cancellation takes effect irrespective of later signed-copy receipt; an internal approver must not delay that legal effect. This is a scoped rule, not a national default. [PRA-109, section 15(a), PDF p.13](https://dte.maharashtra.gov.in/wp-content/uploads/2026/07/Student-Transfer-Circular_2026-27-with-attachement.pdf); [C14](../research/pranav/worked-cases.md).

## 6. Architecture and practical data flow

Use a modular application with a relational database and a separate worker, keeping the operational footprint understandable. The conceptual flow is: **institution export → quarantined staging → mapping/preview → revisioned institution evidence → rule evaluation → approver snapshot → reporting/export**. Student corrections re-enter the revision path. Conditional provider evidence and restricted regulator review attach to records through separate permission boundaries.

The core entities are institution, institution-local student, identity claim, restricted person link, programme offering, approval version, enrolment revision, import job, rule finding, correction case, submission snapshot and disclosure grant. Internal random identifiers preserve continuity when APAAR is missing or corrected. Names and unverified repeated IDs never trigger automatic person merges. [Dharanish's entity model](../research/dharanish/findings.md#proposed-entities-and-invariants).

An upload token plus content/mapping fingerprint identifies a retry. Changed content under the same token conflicts; unchanged business records under a new token are no-ops. Corrections include an expected version, preventing a stale spreadsheet from restoring an old course or withdrawal state. Bounded chunks commit row outcomes, revisions, audit and outbox events atomically. Partial progress is visible and cannot masquerade as a completed snapshot. Duplicate-tolerant workers consume events and rebuild projections. [Proposed import protocol](../research/dharanish/findings.md#import-and-correction-protocol); [AWS outbox guidance, DHA-104](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html).

The optional provider adapter binds one authorised account session to one local case. Requester v2.4 documents a token-account APAAR operation with no arbitrary-ID parameter and recommends one call after acquiring the token. Its response may include personal and academic fields; selective provider-side projection is not established. Assess the payload, derive minimal needed evidence and discard unrelated fields without logging the response. Deposited credits do not establish exhaustive current admissions. [SUD-105, printed pp.16–19](https://cdn.apisetu.gov.in/portal/assets/Requester-MeriPehchaan-APISpecificationv2.4.pdf); [inspected contract and ambiguities](../research/sudhan/integration-review.md#2-current-api-discovery).

Provider calls occur outside database transactions. Denied permission, token failure, not-linked data, mismatch, outage and unexpected schemas remain distinct. Bound retries according to approved provider rules; expose staleness and preserve work. Never convert HTTP 404 or timeout into nonexistence or fraud. Institution acceptance does not depend on a successful provider call.

## 7. Complete proposed technology stack

These are engineering choices for a future implementation, not installed or tested project components. Pin supported versions and licences when implementation begins.

| Area | Proposed choice | Purpose and limit |
|---|---|---|
| User interface | React, TypeScript, Vite, semantic HTML/CSS | Responsive staff/student views; accessible forms; no sensitive offline cache |
| API and schemas | Python, FastAPI, Pydantic; generated OpenAPI | Typed request validation and explicit evidence contracts |
| Persistence | PostgreSQL 18, SQLAlchemy, Alembic | Scoped constraints, transactions, revisions and reversible migration planning |
| Jobs and events | Separate Python worker; PostgreSQL jobs, leases and outbox | Durable bounded work; postpone Redis/Kafka until measured need |
| Imports and exports | Python CSV parser; read-only openpyxl XLSX later; JSON and controlled CSV/PDF outputs | CSV first; bounded parsing, versioned mappings and spreadsheet-formula protection |
| Authentication | Existing institutional OIDC provider; Keycloak for local synthetic setup; maintained Authlib client | Server session in secure HttpOnly cookies, CSRF protection, privileged MFA and role removal |
| Files and secrets | Private S3-compatible storage; managed KMS and secret manager for deployment | Scoped downloads; encryption; separate signing/encryption keys; no secrets in source |
| Development and CI | Git, locked dependencies, Docker Compose; GitHub Actions; Ruff, TypeScript checks, dependency and secret scans | Reproducible synthetic environment and reviewable changes |
| Testing | pytest, Hypothesis, real PostgreSQL/Testcontainers; Playwright and axe-core; Locust for future workload tests | Invariants, real transaction races, browser/accessibility and measured load |
| Deployment | Ubuntu LTS container host behind Caddy; managed PostgreSQL, private storage and backups for a permitted pilot | TLS, restricted network paths, migrations and restoration; resize before real use |
| Operations | OpenTelemetry; Prometheus/Grafana; redacted structured logs and separate protected audit events | Queue age, failures, projection lag and access denials; no student IDs in metric labels |

FastAPI documents OpenAPI and validation capabilities; Vite supplies frontend build tooling. PostgreSQL RLS can add defence but owners and `BYPASSRLS` roles bypass ordinary policies: use separate migration roles and test non-owner application/worker roles. [FastAPI, DHA-108](https://fastapi.tiangolo.com/features/); [Vite, DHA-109](https://vite.dev/guide/); [PostgreSQL 18 RLS, DHA-103](https://www.postgresql.org/docs/18/ddl-rowsecurity.html).

Use a trusted issuer/key directory and maintained cryptographic libraries for an online signed assertion. Managed KMS can protect encryption/signing keys; policy, rotation and issuer mandate still require explicit design. No blockchain, LLM adjudicator or Kubernetes cluster is needed for the first loop. [Keycloak OIDC](https://www.keycloak.org/securing-apps/oidc-layers); [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html); [credential lifecycle](../research/sudhir/privacy-design.md#credential-and-verification-lifecycle).

## 8. Security and legal boundaries

Authorisation is checked on every API, worker, file and export, using trusted institution membership, role, purpose and resource scope. Separate operator and approver roles; restrict support to masked metadata. Tenant controls must survive pooled connections, caches and queued jobs. Sensitive changes and exceptional access need accountable approval and audit. [Permission matrix](../research/sudhir/privacy-design.md#permission-matrix); [OWASP authorisation, SUH-109](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html).

Treat uploads as hostile input: limit bytes, rows and processing time; quarantine files; reject unsupported formats; never execute formulas/macros; protect exported spreadsheet text. Protect claimed identifiers separately. Any authorised matching token is keyed, access-controlled and still personal data; a plain hash is not anonymisation. Do not collect Aadhaar, biometrics, wallet PINs or OTPs in this proposed application. [Threats T01–T09](../research/sudhir/threat-model.md).

DPDP is phased. On 27 October 2026, its main processing, notice, consent, child-data and rights provisions remain in the future commencement stage; the project cannot claim blanket DPDP compliance. The legal review records the final Rules, December corrigendum and October 2026 order and preserves publication-date uncertainty. Current IT Act/SPDI applicability and the full SPDI Rules retrieval remain open review items. [G.S.R.843(E), SUH-102](https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf); [legal-status assessment, SUH-101–116](../research/sudhir/legal-status.md).

A pilot needs a named operator, purpose/field/recipient authority map, processor agreements, retention schedule, age/guardian process, grievance route and incident responsibility. Institution reporting authority, provider permission and employer disclosure are different decisions. Applicable CERT-In incident/log obligations must be assessed separately; an educational purpose is not blanket sharing permission. [SUH-106 and pilot decisions](../research/sudhir/legal-status.md#current-security-directions-and-remaining-legal-work).

## 9. MVP boundaries and requirement coverage

The first future MVP is **one synthetic end-to-end correction and reporting loop** across two fictional tenants and one scoped rule pack. Include import, mapping, preview, approver snapshot, student challenge, rule explanations, export, audit and recipient-bound demonstration verification. Display synthetic provider/issuer labels throughout.

| Requirement | First demonstrator | Conditional next step | Acceptance evidence |
|---|---|---|---|
| R01 Upload/update | Scoped imports and revisions | Approved institutional contract | Retry and stale-edit tests |
| R02 Required dimensions | Separate intake, category, route and pool fields | Current course/year approval | Reviewed field map and denominator |
| R03 Detection | Deterministic data/policy findings | Authorised restricted overlap review | Boundary and exception cases |
| R04 Dashboards | Own-tenant and fictional regulator views | Approved real reporting scope | Reconciled totals and freshness |
| R05 Verification | Recipient-bound synthetic assertion | Vetted recipient and authority | Denial/revocation checks |
| R06 Verifiable records | Revision, provenance, demo signature/status | Trusted issuer mandate | Tamper, stale-status and key tests |
| R07 Integration | CSV/internal contracts; provider fixture | Approved provider/AICTE adapters | Contract and authorised test evidence |
| R08 Protection | Roles, grants, audit and threat fixtures | Legal/security entry gates | Independent scoped assessment |
| R09 Reports | Versioned totals and evidence export | Accepted regulator/accreditation definitions | Reproduction from snapshot |
| R10 Certificate IDs | Synthetic awarding-body template preview | Confirmed issuer/display requirements | Identifier distinction/privacy review |

R10 does not justify public identifier retrieval through a QR. Awarding bodies control real certificate printing; APAAR, institutional student ID and AICTE enrolment number remain distinct. Direct Aadhaar integration, universal ERP connectors, nationwide automatic enforcement, predictive fraud scores and W3C credential interoperability are outside the first MVP. Later work requires demonstrated need and authority. [POL-14/C22](../research/pranav/rule-catalogue.md); [SUD access ladder](../research/sudhan/integration-review.md#4-onboarding-sponsor-and-sandbox-reality).

## 10. What the evidence actually establishes

The assembled desk research establishes useful constraints: existing import/award systems, a documented account-linked provider operation, scoped policy exceptions, security design requirements and unresolved access dependencies. It does not establish adoption, saved time, accuracy on real students or operational compliance.

The independently reproduced original model contains **1,000 fictional rows**, a separate fictional reference cohort and twelve sequential model checks. Eight comparisons with preserved original outputs matched. Rules identified 80 labelled cases with zero false alerts in that constructed dataset; adding the statistical signal found ten additional labelled cases and added ten false alerts. Its incremental precision was therefore 50%. This supports a rules-first choice, not a real-world accuracy claim. [Reproduction README](../research/dharanish/experiments/README.md); [recorded results](../research/dharanish/experiments/reproduction-results.json).

Replay/correction behaviour in that model is not a database, concurrency or recovery test of the proposed product. The coarse four-millisecond observation excludes parsing, storage, network and the user workflow. No throughput, national scalability, secure tenancy or fraud-detection claim follows. Optional anomaly triage stays deferred until representative, held-out evaluation justifies the extra review burden.

### Supported key points and proposed solutions

| Problem addressed | Proposed solution | What is validated now |
|---|---|---|
| Replayed or corrected exports alter totals | Idempotent import, scoped keys and revision trail | Sequential fictional model reproduced; real database behavior untested |
| A valid-looking ID is treated as admission proof | Separate format, provider, institution and policy evidence | Provider contract and ecosystem boundaries inspected; live linkage untested |
| Legitimate concurrent study is wrongly flagged | Contextual rule and human correction route | Current UGC guidance inspected; pilot applicability still needs review |
| Historical intake assumptions cause false findings | Versioned approval and rule pack; UNKNOWN when incomplete | Base policy and a real corrigendum inspected; complete amendments unresolved |
| Corrections fail to reach reports or verifiers | Superseded snapshots and revision-bound online assertions | Design and threat analysis only; no product propagation test |
| Matching or QR lookup leaks student information | Uniform receipts, authorised internal review and scoped grants | Threat mechanism and controls reasoned; implementation security untested |
| Staff and students repeat reconciliation work | Reuse exports and give each correction an owner and trail | Existing reference workflows documented; time savings and adoption unmeasured |

The first three rows have supporting source or model evidence, not a field-tested solution. The [requirement matrix](requirements.md) records acceptance gates for every feature.

## 11. Workload, operating effort and cost

For planning only, target a later demonstrator at 10,000 records, 20 concurrent users and uploads capped at 10 MB or 10,000 rows, whichever comes first. Only the 1,000-row model has been executed. A sizing sketch of one million records × 2 KB × three revisions gives 6 GB; adding 1 GB ancillary payload and assuming 2× overhead gives 14 GB, before current rows, WAL, backups or replicas. This is arithmetic, not a storage measurement. [Dharanish sizing assumptions](../research/dharanish/findings.md#workload-and-costs).

Research priced an illustrative Linux 2 GB public-IPv4 Lightsail VM at USD12/month and an encrypted 2 GB standard database at USD30/month: USD42/month for those two components. The smaller USD15 database lacks encryption. These are list-price examples, not a pilot quotation or a capacity recommendation. [AWS Lightsail pricing, DHA-106](https://aws.amazon.com/lightsail/pricing/).

Add object storage, keys, logs, backups, network, identity service, notifications, support, taxes and staff effort. The complete proposed stack needs fresh sizing and region/contract review. Provider pricing/access is unknown. No resource has been purchased. The largest uncertain operating cost may be reconciliation: for an assumed 1% of 10,000 records requiring ten minutes each, review takes about 16.7 staff-hours before approvals or follow-up. Measure this input rather than hiding it behind cheap hosting.

## 12. Staged validation and stop conditions

**Stage A — evidence and workflow confirmation.** Obtain official SIH wording, a willing accountable institution, blank templates, current approval/amendment chain and permission to study tasks. Observe a small, diverse sample of operators, approvers and students, including missing-ID and assisted-access cases. Map actual corrections and compare the improved-checklist baseline. Interviews are qualitative, not national prevalence estimates. Stop product expansion if the workflow merely duplicates entry or lacks a responsible correction owner.

**Stage B — synthetic implementation, if authorised later.** Instantiate all 22 policy cases and provider failure fixtures; execute real database races, interrupted jobs, malformed uploads, tenant denials, revocation/export races and restore tests. Entry to real data requires zero known critical access failures, no silent lost updates, reproducible snapshot totals and visible unresolved states. Demonstrate that comparable matching/nonmatching submissions reveal no match bit across response, notification, export and timing channels; investigate residual inference. These are proposed criteria, not passed checks.

**Stage C — permitted shadow pilot.** Start with one institution/programme/cohort, two separated staff roles and a student grievance contact. Keep official workflow and rollback available. Add a second institution only after matching authority and access boundaries are approved. Live provider linkage requires sponsor/use-case approval, exact scopes, authorised test arrangements and acceptance: the partner SOP excludes temporary testing access. [SUD-106, section 5(vi)](https://cf-media.api-setu.in/resources/Partners-SOP.pdf).

Measure total operator, approver and student effort; correction completion; explanation comprehension; false-alert burden; exclusion complaints; reconciliation accuracy; and willingness to continue. Proposed progression targets are at least 90% successful completion of essential tasks without facilitator correction, at least 20% lower median total staff time than the baseline, and no increase in unresolved student cases. Agree targets beforehand; report sample size, distributions and failures. A small pilot cannot certify national effectiveness.

**Stage D — controlled expansion.** Recheck policy/legal commencement, complete independent security assessment, test restore and key-compromise procedures, and obtain genuine institutional acceptance. Expand one integration or cohort at a time. Stop affected processing on unauthorised disclosure, wrong-person linkage, failed revocation, silent overwrite, unreviewable policy, or irreversible wrongful rejection. Contain the event, preserve restricted evidence, use the manual route and reopen only after documented human review.

SetuTrace is defensible when it helps people correct and explain records without overstating what identity evidence proves. The current deliverable is the research-backed design and its testable assumptions. [Actual AI critique and resolutions](design-critique.md) remain separate from the human decisions still required.

**Lead publication update:** The final remote refresh incorporated newer Pranav and Sudhir contributions, preserved alongside their specialist reconciliations in the [assignment audit](research-audit.md).



## 13. What the prototype demonstrates

The project now has a focused synthetic web application in the separate [SIH_Project_Prototype repository](https://github.com/Dharanish99/SIH_Project_Prototype). Its interface uses React, TypeScript and Vite; the API uses Node 24 and Express; SQLite persists the demo; and Ed25519 signs synthetic assertions. A persona selector simulates institution staff, student, approver, regulator analyst and verifier. These simulated identities are not production authentication.

The demo follows Meera, a fictional student whose admission document says ECE while an institution export says CSE. It shows why a discrepancy needs a correction owner rather than another unexplained alert. A reasoned correction changes the fictional CSE count from 7/6 to 6/6, preserves the earlier revision and can be reviewed in a new snapshot. The student may then grant a named demo verifier a limited set of fields for a purpose and short period. Verification checks the recipient and current grant again; expiry, revocation or a superseding record withholds old claims.

The implementation demonstrates import preview and commit, repeat-import handling, expected-version checks against stale edits, transactionally recorded changes, source revisions, separate approval, a frozen snapshot, minimal JSON/CSV export, audit evidence and current-state verification. The prototype repository records 23 HTTP, database and proxy behavior tests. That count describes the tested application behavior only; it is not an accuracy, usability, security-certification or policy-validation result.

| Demonstrated now | Still proposed or gated |
|---|---|
| Fictional tenant-scoped records; import preview, commit, replay handling and revisions | Real student data, official institutional identity and complete admission schema |
| Source disagreement, simple capacity arithmetic and evidence-state findings | Current, human-approved rules for each programme, year and route |
| Student challenge, institution reason and correction history | Real correction authority, service levels, external source correction and appeals |
| Fictional dashboards, report summary and frozen exports | Regulator mandate, official reporting contract and receipt |
| Separate demo approver and synthetic signed claim | Trusted issuer directory, real recipients, lawful disclosure and credential interoperability |
| CSV and internal API with provider fixtures | Government credentials, approved scopes and authorized contract testing |
| Local persistence, demo audit checks and hosting health | Durable database, restore evidence, managed keys, monitoring and independent assessment |

All records and providers are fictional. The application makes no APAAR, AICTE, DigiLocker or government API calls; it issues no official certificate; and it has no field-tested impact. Free hosting may sleep, and temporary storage or a signing key can reset on restart. A signature binds synthetic bytes to a demo key; it does not prove the fact is true or legally recognized. A healthy endpoint proves neither policy accuracy nor privacy, security or continuity. Demonstrate the actual screen states, label simulations clearly and use the research repo for evidence and open questions.

## 14. The product promise

SetuTrace should make five promises: every institutional claim identifies its source and revision; missing evidence is not silently converted into a negative conclusion; an affected student has a traceable route to the responsible source owner; an approver can reproduce the exact records and rule version behind a report; and a verifier receives only permitted fields while permission and evidence remain current.

It must make the limits just as visible. It cannot correct a system it does not control, guarantee an external response or policy completeness, infer fraud from a duplicate or threshold, or erase a copy already downloaded. It cannot replace admission authorities, awarding bodies, policy makers, grievance officers or regulators. These are design commitments for human review, not a current legal warranty. Ask users to explain “verified,” “submitted” and “approved” in their own words; if they misunderstand these terms, the product has failed even when an API response is technically correct.

## 15. Journeys that make the idea tangible

### Institution operator

The operator selects a reporting window, campus, programme, entry cohort and locally approved export mapping. A bounded file enters quarantine. Before any record changes, a preview shows understood and ignored columns, new, unchanged, changed, repeated and invalid rows, the mapping version, and sample records. Errors identify source line, field, reason and next action. No preview action mutates current data.

Commit applies only changes that still match the versions reviewed. A competing edit causes a conflict and fresh preview, never silent overwrite. Replaying the same token and content/mapping fingerprint returns the original receipt; unchanged business facts can be no-ops. Partial work is labelled partial and cannot become an approved snapshot. Success is a report traceable to sources without a second full manual reconciliation—not simply a dashboard with zero warnings.

### Student, including a missing or disputed APAAR

The student enters through an institution-approved account or an assisted process. A local reference and case number allow them to report a missing, unavailable or disputed APAAR without requiring the correct identifier as proof of the identifier they are challenging. Names and unverified values never trigger automatic person merges.

The student sees the institution-held claim, its source category, effective date and whether it entered a report. They can challenge the programme, date, identifier linkage or another field, attach permitted evidence and request a correction. A plain-language status shows receipt, evidence request, assigned owner, referral, decision and any appeal path. Exact service times require institutional approval; the interface must not invent legal deadlines.

If another authority controls the source, the institution explains the handoff and offers a usable route. It must not close a case because an API timed out, expose a cross-institution match signal or tell the student to contact an unknown office without context. A refusal records what was reviewed and how a human can reconsider. Whether a pending link can be reported is an unresolved policy question, not a software default.

### Reviewer and approver

The reviewer sees the institution assertion, provider response, rule result and human decision separately, with source date, effective time, retrieval time, version and freshness. Provider outage means unavailable; incomplete policy means policy unavailable; neither means a breach. Each deterministic finding displays its inputs, calculation and assumptions. A capacity discrepancy opens review; it does not cancel admission.

The approver reviews denominators, included and excluded records, unresolved cases, source times, mapping and rule versions, exceptions and reporting cutoff. If an input changes during review, the approval detects a stale digest and requires a new review. Approval freezes the named row revisions and approver identity. A subsequent correction creates a successor snapshot or marks downstream outputs superseded; it does not rewrite history. Any future regulator view must show only authorized aggregates and must not expose case details just because an analyst can see totals.

### Verifier

A vetted verifier authenticates, gives a purpose and requests defined fields. The student sees recipient, fields, source revision and expiry before granting or declining. Declining cannot affect admission. Each retrieval rechecks recipient, grant, expiry, approval, issuer and current record status. A forwarded QR or link grants no access by itself.

The result says exactly what is attested, such as “institution-reported enrolment in the approved snapshot,” not “officially verified student.” It identifies the issuer and relevant dates while avoiding a public student identifier. A stale, withdrawn, superseded or unavailable response loses any current-valid badge. Future offline proofs must disclose that they cannot establish live status and may survive revocation.

## 16. Information model and evidence states

Do not treat one identifier as the person, one row as the truth or one score as the decision. Use a stable random institution-local student reference. Store restricted person-link evidence, linkage method and status separately from the APAAR identity claim. Model enrolment as a versioned institutional assertion tied to programme, campus, academic period, entry route and relevant category. Provider evidence, documentary evidence, policy pack, finding, correction case, approver snapshot and disclosure grant are separate objects with separate access rules.

An evidence envelope should identify the asserting party, subject reference, claim type, source and revision, effective time when known, observed and retrieval times, scope, evidence class, status, purpose and retention rule. Keep the event’s effective time distinct from when SetuTrace learned of it. Do not copy entire provider responses to ordinary logs or analytics; retain raw artifacts only when an approved purpose, access boundary and retention period justify them.

Define the same small vocabulary in screens, exports and APIs. “Asserted” means an authorized source made the claim. “Retrieved” means an integration returned data; it is not a match decision. “Evaluated” means a named rule version ran on specified inputs. “Needs review” means a human decision is required. “Resolved” means an assigned reviewer recorded an outcome within their authority. “Approved snapshot” means an approver froze a defined reporting view. “Submitted” means a route recorded dispatch. “Acknowledged” means the receiver supplied receipt evidence. “Current” means no known superseding event at a stated check time; it is not a truth guarantee. “Unknown” and “unavailable” are valid states. A signature cannot transform missing approval into zero capacity, an absent APAAR into rejection, a match into an accusation or an issuer’s assertion into established fact.

## 17. Rules and decision governance

Activate a rule only when a human owner can point to authority, population, effective period, required inputs, calculation, exception route and operational consequence. Store a stable ID and version, citation, jurisdiction and institution scope, programme, entry route, cohort, valid dates, recorded time, missing-data behavior, severity, reviewer role, test cases and human approval. A correction creates a new version and identifies prior findings to reevaluate.

The engine calculates and explains; it does not exercise institutional authority. A threshold result is a potential capacity discrepancy, not an “illegal student.” A possible overlap identifies an internal reconciliation need without revealing another institution. Missing category differs from a category count of zero. Concurrent study, revised approvals, withdrawals, transfers, foreign learners, NRI/OCI routes and lateral entry may change interpretation; there is no universal extra-seat formula.

Incomplete authority produces a neutral unresolved state. Do not silently fall back to a historical rule. Name the affected period and missing document. Separate rule authoring from live approval. Before activation, a human approver signs the pack and checks regression examples from Pranav’s 22 worked cases. Kanishkar’s team synthesis coordinates feasibility, but agent agreement is not human sign-off.

## 18. Privacy, security and reliable operation

Collect only fields needed for an identified reporting, correction, authorized matching or disclosure purpose. Keep identity-linkage evidence separate from ordinary programme reporting. Do not support public lookup by APAAR, name, phone or student number. The first loop needs no Aadhaar, biometrics, OTP or wallet credential. A hash of a predictable identifier remains sensitive data.

Enforce tenant, role, purpose and resource checks in every request path, background job, download, export and support tool. A pilot must use a non-owner database role, transaction-scoped tenant context, and tests for connection-pool reuse and failure paths. Keep operator and approver duties separate; use secure short-lived sessions, CSRF defenses, privileged-user MFA, role removal and audited support access. External responses should not disclose whether another student exists.

Treat uploads as hostile: cap size, row count and processing time; quarantine; reject unsupported or macro-enabled files; neutralize spreadsheet formula prefixes; and omit protected IDs from sample exports. Encrypt data and backups, separate key purposes, rotate keys and restrict signing access. A hash chain can reveal some changes but cannot defeat an administrator able to replace all local evidence. It is not a substitute for independent audit, governed administrator access and tested restore.

Degrade safely: provider outage does not block local correction; a failed transaction cannot return success; stale projections show source time; partial imports cannot appear complete; failed revocation fails closed; and status outage is not “current.” Define response paths for wrong-person linkage, disclosure, silent overwrite, incorrect rule, lost key and unavailable grievance route. Keep a manual route and pause control before a pilot.

Accessibility is part of correctness: keyboard-complete tasks, visible focus, text labels independent of color, useful error summaries, plain language and navigable tables. Assisted access must not require helpers to impersonate the student. Test relevant users and assistive technology; a checklist alone is not evidence of accessibility.

## 19. Evaluation and acceptance evidence

Compare the whole current workflow and an improved spreadsheet/checklist baseline. Measure operator, approver and student work, using the same cohort, task complexity, start/stop points, roles and treatment of missing or unresolved cases. Record source quality and policy certainty. Report sample size, distributions and failures; demo records are not representative evidence.

Measure total staff minutes per reportable cohort, repeat-entry steps, rows manually repaired, challenge-to-acknowledgement and decision time, cases with an accountable owner, student understanding of status, disclosure comprehension, snapshot reproducibility, stale-edit/replay behavior, false-alert burden, abandoned or inaccessible tasks, export leakage, permission denials, and operator willingness to continue. Also test whether response, timing, notification or export reveals another student’s existence. Reliability measures include interrupted-job recovery, restore time and preservation of approved totals.

The research proposes progression targets of 90 percent essential-task completion without facilitator correction, 20 percent lower median staff time than a measured baseline, and no increase in unresolved student cases. These are targets, not results. Agree a method and sample rationale before a permitted pilot; report failures and do not optimize one role by denying students a working correction path.

Before real records, exercise cross-tenant access, role escalation, session replay, malicious upload, formula injection, mistaken identity link, concurrent updates, stale import, retry, export authorization, revocation/export race, snapshot supersession, key rotation, audit reset, backup restore and outage. Independent reviewers assess privacy, threats and legal roles. Passing is an entry gate, not certification.

## 20. Rollout gates and stop conditions

**Gate 0 — authority.** Obtain official SIH wording and confirm deliverables. Identify an institution sponsor, data controller, processor, source owners, policy owners and security contact. Without them, remain synthetic.

**Gate 1 — observed work.** With permission, observe operators, approvers and students, including missing-ID and assisted-access cases. Compare existing work with the checklist baseline. Stop if the app duplicates entry, adds more work than it removes or has no accountable correction owner.

**Gate 2 — synthetic engineering.** Use PostgreSQL and concurrent workers to test real transaction boundaries, tenant isolation, durable jobs, interruptions, rollback, races, revocation, backups and accessibility. Replace the demo persona switcher with an approved identity route. Keep all data fictional.

**Gate 3 — shadow pilot.** Require written purpose and field authority, approved policy, retention plan, processor terms, grievance route, incident owner, legal review and independent security assessment. Start with one institution, programme and cohort. Keep the existing official process and rollback. Do not activate matching or external APIs without separate mandate and approved scope. Shadow findings do not trigger adverse decisions.

**Gate 4 — limited operation.** Require reliable recovery, agreed report contract, reviewed metrics, correction ownership and an approved method for unresolved cases. Add one integration or cohort at a time. A local approval, export, transmission and official acknowledgement are distinct states.

Pause affected processing for wrong-person association, unauthorized disclosure, failed revocation, silent data loss, stale rule, irreproducible report, adverse action without review or inaccessible challenge route. Preserve restricted evidence, notify the agreed owner, use the manual path, correct downstream snapshots and reopen after documented human review. Stop expansion if the product does not reduce total effort or unresolved cases increase.
