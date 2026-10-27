# Institutional workflows and user needs — completed desk-research supplement

Human workstream owner: Gopika. AI supplement: lead research agent, 2026-10-26.
Status: public-document research assembled; adoption, user testing and human review unperformed.
Original uploads are preserved in [original-upload](original-upload/findings.md). The [revised Notion allotment](../provenance/notion/gopika-revised-allotment.md) requests internet-only research. Its historical GitHub restrictions are superseded by the current user's request.

## Decision brief
Build a correction and reporting layer compatible with institutional exports. Connect claims to their sources, explain exceptions, and let students dispute errors. A generic upload portal is weak novelty because existing systems already cover parts of it. This is a design inference, not evidence of demand, workload or time savings.

## Findings and fair system comparison
| ID | Documented scope | Design implication |
|---|---|---|
| GOP-F01 | Samarth STU-001 v1.4.12 describes individual/Excel imports, validation, allocation, administrator edits and automatic import from its admission portal. [GOP-103](https://docs.samarth.ac.in/docs/academics/student/) | Preserve ERP ownership; avoid a second full ERP. |
| GOP-F02 | Samarth's April 2026 guide covers programme eligibility, fees, notices and student-view checks. [GOP-104](https://docs.samarth.ac.in/docs/academics/admissions2026/) | Admissions configuration differs from post-admission reconciliation. |
| GOP-F03 | NAD separates institution issuance, student retrieval and consented verifier access; issuers manage award lifecycle. [GOP-106](https://nad.digilocker.gov.in/about) | Reuse authorised award infrastructure; an enrolment receipt is not a degree. |
| GOP-F04 | AISHE's 2024–25 college form has programme-level intake and enrolment grids. [GOP-110](https://cdnbbsr.s3waas.gov.in/s392049debbe566ca5782a3045cf300a3c/uploads/2024/12/202507141166032813.pdf) | Aggregate totals do not identify which individual was counted. |
| GOP-F05 | APAAR/ABC identity and credit functions do not establish admission validity. [Integration research](../sudhan/findings.md) | Keep identity, enrolment, policy and award statuses distinct. |
| GOP-F06 | The [prior public-reporting brief](../provenance/notion/current-reporting-evidence.md) distinguishes AICTE, AISHE, TNEA and UMIS. Current policy is rechecked [here](../pranav/findings.md). | Do not claim colleges submit no data; state systems and historical figures have bounded scope. |

ERP operations, academic identity, award infrastructure and aggregate reporting are complementary system categories. Cross-system correction synchronisation and this project's access are **not found/unknown**, not “explicitly unsupported.” No claim of exhaustive competitor analysis is made.

## D1 — Two separate reference workflows
| Flow / actor | Input and action | Output | Exception / evidence |
|---|---|---|---|
| A1 Institution administrator | Add record or populate offered Excel format | Imported records | Exact live columns uninspected; GOP-103 |
| A2 Administrator | Validate and allocate to programme | Product validation/allocation result | Error semantics incompletely documented; GOP-103 |
| A3 Administrator | View/edit student record | Updated operational record | Regulatory propagation unknown; GOP-103 |
| A4 Configuration owner | Check programme/fees/notices in student view | Configuration checked | Not proof of completed admission; GOP-104 |
| B1 Academic issuer | Prepare and lodge award | Issuer-published digital award | Activation/publishing authority required; GOP-106, SUD-103 |
| B2 Student | Retrieve and choose to share award | Access/sharing | Missing award requires source follow-up; GOP-106 |
| B3 Authorised verifier | Request with student consent | Award evidence | Not unrestricted enrolment access; GOP-106 |
| B4 Issuer | Correct through supported route | Revised award lifecycle | FAQ correction marker inspected by integration agent; exact template contract pending; SUD-103 |

These are reference flows, not proof of a live interconnection. Proposed bridge: record batch, mapping version, correction and final snapshot. Show an AICTE acknowledgement only when actually received through an authorised route.

## D2 — Source field map
Exact labels below are source concepts, not an official project schema. Mandatory status/lengths were not established.
| Source label / concept | Level/type | Proposed mapping | Ambiguity |
|---|---|---|---|
| Samarth Programme | individual reference | programme_offering_id | Resolve local code |
| Name (as on ID card) | individual text | display_name | Name match is not identity binding |
| Enrollment Number/Examination Roll Number | string key | source_record_key | Separate key namespaces |
| Academic Session | period reference | academic_session_id | Not necessarily admission cohort |
| Admission Type | enumeration | admission_route | Not nationality |
| Section – Organization Unit | organisation reference | source_unit_id | Not automatically campus |
| Mobile Number | contact string | optional contact reference | Collect only if needed |
| Email Address | contact string | optional contact reference | Provider login need not imply storage |
| AISHE Survey Year | aggregate period | report_period | Separate effective dates |
| Approved Intake: (Seats for first year) | programme count | intake mapping | EoA needed for authority |
| Supernumerary Seats | programme count | seat bucket mapping | Eligibility from policy |
| Student Enrolment – Regular Mode | aggregate grid | derived count | Requires denominator definition |
| NRI Students / Other foreign national students | aggregate categories | report-specific map | Not identical to seat entitlement |
| Name of the Programme | label | display + external code | Names are not stable keys |

Sources: GOP-103 registration/import; GOP-110 pp.1,7–9. Preserve source version and meaning. These are proposed mappings, not implemented integrations.

## D3 — Six fictional scenarios
| Trigger | Documented handling / gap | Proposed handling | Owner |
|---|---|---|---|
| Normal new record | Samarth import/validate exists | Preview, separate checks, approver snapshot | Dharanish |
| Required value missing | Provider requirements differ | Incomplete linkage and next action; no automatic admission denial | Sudhan |
| Name/ID mismatch | Universal resolution unknown | Separate reported ID from account evidence; correction case | Sudhir |
| Correction after submission | Local edit/award lifecycle documented separately | Versioned correction, revalidation, superseded receipt | Dharanish |
| Same file sent twice | Product replay behaviour unknown | Same-token replay; fresh-token unchanged records are no-op | Dharanish |
| Withdrawal/course change | Cross-system propagation unknown | Effective-dated event, recalculate snapshot, preserve history | Pranav |

These are design walkthroughs, not executed product tests or observed user cases.

## D4 — Five opportunity cards
| Priority / candidate | Evidence and existing capability | Proposed value/dependency | Unproven assumption and future test |
|---|---|---|---|
| High: exception-first import receipt | Import exists; reporting granularity varies | Explain unresolved rows; mapping and retries | Compare task time with existing checklist/export |
| High: correction propagation | Record/award lifecycles differ | Show changed source, owner and stale outputs | Actual frequency unknown; test six correction tasks |
| High: student dispute receipt | Identity differs from enrolment | Visible case owner/status | Student comprehension/adoption unknown |
| High: policy evidence card | Rules depend on year/category/approval | Show applicability and unknowns | Independent policy reviewer checks boundary cases |
| Medium: scoped verification receipt | NAD already enables consented award verification | Minimal current-enrolment claim with issuer/freshness | Employer demand and access eligibility unproven |

Build candidate: one correction-first reporting loop. Investigate: account-linked APAAR and applicable intake rules. Already covered elsewhere: general admissions/fees and digital award storage. Defer: national fraud scoring, full ERP replacement and universal connectors.

## Completion and limits
The revised public-research outputs are represented: two flows, field map, comparison, six cases, five opportunities/brief, source ledger. Supplied GOP-001–009 verification outcomes are in [sources.csv](sources.csv); access failures remain explicit. Human teach-back, observed workflows, time savings and usability are pending. No interviews/contact occurred. Agents can complete desk research, not invent field validation.
