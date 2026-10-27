# Research and deployment risk register

Updated 27 October 2026. These are evidenced dependencies and design risks; no probabilities or production incidence are invented.

| Risk / owner | Evidence or uncertainty | Mitigation and decision gate | Status |
|---|---|---|---|
| RK01 Provider access - Sudhan | Documented token-account API; onboarding and scope unproven | Useful CSV/correction core; label mock; sponsor and real contract tests before live claims | External dependency |
| RK02 Wrong policy - Pranav | Current complete APH amendments unavailable; scoped EoA/corrigenda matter | UNKNOWN on incomplete pack; signed-off course/year scope; source/effective/recorded versions | External dependency |
| RK03 Extra work - Gopika | Documented reference workflows, no observed users | Measure total staff, approver and student effort vs existing process and spreadsheet alternative | Benefit unvalidated |
| RK04 Silent overwrite/replay - Dharanish | Sequential model reproduced; no real DB tests | Scoped keys, expected versions, atomic row/audit/outbox, rollback and race tests | Proposed controls |
| RK05 Disclosure/oracle - Sudhir | Raw-ID lookup or conditional receipts reveal others' data | Uniform receipt semantics/timing; internal authorised matches; permission at every retrieval/export | Security tests pending |
| RK06 Scope overload - Kanishkar | Ten requirements span multiple authorities | One programme/cohort end-to-end; conditional integrations and clearly scoped demonstrations | MVP proposed |
| RK07 Missing/foreign APAAR - Sudhan/Pranav | Universal exception process not established | Capture local record; pending linkage; assisted resolution; no automatic admission denial | Policy dependency |
| RK08 Official SIH wording - Kanishkar | Official portal returns403 | Obtain official publication/organiser confirmation before submission | Open |
| RK09 Wrong effective event - Pranav | Withdrawal/cancellation authority varies; Maharashtra online event has effect | Configure applicable authority/effective event; do not invent institutional approval delay | Human pack review pending |
| RK10 Revocation/staleness - Sudhir/Dharanish | Signed bytes may be old or wrongly issued | Revision-bound, purpose/audience/time-bound assertions; current status at retrieval; downloaded-copy limit explicit | Proposed controls |
| RK11 Legal/retention roles - Sudhir | DPDP commencement staged; SPDI full text/application unresolved | Operator-specific legal review, contracts, field/purpose matrix and retention schedule before real data | External dependency |
| RK12 Scale and cost - Dharanish | Component prices and sizing assumptions only | Measure at stated load; account for operations/backup/egress/support; no national-scale claim | Benchmark/quotation pending |

See [threat model](../research/sudhir/threat-model.md), [policy gaps](../research/pranav/access-and-amendment-log.md), [integration contracts](../research/sudhan/contract-scenarios.csv) and [validation plan](solution-report.md). Human owners remain responsible for acceptance; agent consensus is not sign-off.
