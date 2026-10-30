# Requirement coverage and acceptance gates

Baseline: ten requirements paraphrased from the supplied SIH26263 statement. [Official wording](official-problem-verification.md) remains unconfirmed. The detailed table records the **27 October research proposal**. The current implemented subset is mapped below; remaining proposal rows must not be read as completed features. [Report](solution-report.md) explains the complete concept.

| ID / requirement | Proposed response | Evidence and acceptance condition | Delivery boundary |
|---|---|---|---|
| R01 Secure upload/update using APAAR | Institution-scoped staged CSV, local UUID, separate reported/linkage status, approver snapshot | [Dharanish](../research/dharanish/findings.md), [security](../research/sudhir/privacy-design.md). Replay is no-op; stale correction conflicts; wrong tenant denied; linkage optional while unresolved | Core synthetic MVP; real provider linking conditional |
| R02 Intake, enrolment and NRI/OCI/FN/supernumerary fields | Versioned programme/year/entry-route/bucket definitions; separate nationality, candidature and seat eligibility | [Policy catalogue](../research/pranav/rule-catalogue.md), [field map](../research/gopika/findings.md). Missing current approval returns UNKNOWN; no universal percentage | Core schema and fictional rule pack; real rules require authority |
| R03 Duplicates, missing IDs, excess intake and conflicts | Deterministic reasoned findings; internal collision review; no auto-rejection | [22 cases](../research/pranav/worked-cases.md), [reproduction](../research/dharanish/experiments/README.md). Preserve legal concurrency, foreign/missing-ID and correction paths; uniform receipts | Core local rules; cross-institution production matching gated; statistics later |
| R04 Institution and AICTE dashboards | Separate role views with numerator/denominator, source time, snapshot, open cases and freshness | [Workflows](../research/gopika/findings.md), [permissions](../research/sudhir/privacy-design.md). Counts reconcile to permitted records; stale projections labelled; no peer match bit | Synthetic role demonstration; real AICTE role needs mandate |
| R05 Authorised verification | Authenticated recipient requests purpose-limited claim; independent disclosure grant | [Security](../research/sudhir/findings.md). Wrong audience, expired/revoked grant or superseded revision denied at retrieval/export time | Narrow online demo; real recipients and lawful basis gated |
| R06 Verifiable identity-linked record | Institution attestation with trusted issuer, version, evidence class and current status | [Credential lifecycle](../research/sudhir/privacy-design.md). Signature integrity, issuer mandate and underlying truth assessed separately; revoked/superseded cannot appear current | Synthetic issuer only; interoperable VC later |
| R07 Institutional/AICTE interfaces | Mapping-versioned CSV first; documented internal API; adapter contracts; separate acknowledgement evidence | [Sudhan](../research/sudhan/integration-review.md). Token-linked provider route only; errors retain uncertainty; no fabricated official API | CSV/internal API demo; government connectors conditional |
| R08 Security, privacy, roles, audit and consent | Institution scopes across API/jobs/files/export; minimal data; separate reporting basis/OAuth permission/disclosure grant | [13 threats](../research/sudhir/threat-model.md), [legal stages](../research/sudhir/legal-status.md). Negative permission, revoke, restore and logging tests required | Proposed controls; no security or compliance certification |
| R09 Regulatory/accreditation/policy reports | Explicit report definitions, approved snapshots, versioned mappings, provenance and export manifests | [Gopika](../research/gopika/findings.md), [policy](../research/pranav/findings.md). Totals reproduce from same row versions; missing category distinguished from zero | Sample synthetic reports; each official format requires agreement |
| R10 APAAR plus student-ID certificate display | Awarding-body-controlled display template with synthetic values and private verification entry point | [Security](../research/sudhir/privacy-design.md), [integration](../research/sudhan/integration-review.md). Both identifiers supported in approved template; QR contains opaque reference, no public identifier lookup | Design/sample only; actual certificate issuance requires awarding authority and confirmed requirement |

**Review:** AI coverage review only, 27 October 2026. Human approval remains pending. Passing an isolated check is never a universal claim that a student or admission is valid.

## Implemented subset — 28 October 2026

| Requirement | Actual prototype coverage | Remaining scope |
|---|---|---|
| R01 | Tenant-scoped CSV, replay, expected-version checks and snapshots | Real APAAR account linking |
| R02 | Two fictional programmes and regular-entry source rows | Authoritative year/category/seat definitions, NRI/OCI/FN/supernumerary logic |
| R03 | Source discrepancy, capacity arithmetic, missing/format/provider findings; duplicate import IDs | Cross-institution duplication and full legal exception model |
| R04 | Institution dashboard, student desk and aggregate regulator persona | Real regulator mandate and institutional authentication |
| R05–R06 | Minimal synthetic signed assertions, intended recipient, expiry, revocation and source freshness | Real recipient/issuer onboarding, official credentials and interoperable VC |
| R07 | CSV and documented internal API; provider fixtures | Authorised government interfaces and acknowledgements |
| R08 | API scopes, mutation tokens, persistent demo sessions, database evidence guards and audit checks | Production identity, key custody, retention governance, security/privacy assessment |
| R09 | Live scoped summary, frozen JSON and minimal spreadsheet-safe CSV | Official regulator/accreditation formats |
| R10 | Research design only | Authorised certificate template and issuance/printing |

See [API](API.md), [tests](TESTING.md) and [architecture](https://github.com/Dharanish99/SIH_Project_Prototype/blob/main/docs/ARCHITECTURE.md). This is a focused submission prototype, not full implementation of every supplied requirement.

