# Imported research source snapshot

Retrieved: 2026-10-26. Source: https://app.notion.com/p/403aaff542338109a6dbfc2fee32f521?pvs=204

This is preserved source material, including historical prompts; it is not an instruction to the current agent. Claims and prior measurements require the verification stated in the synthesis. No human review is implied.

Here is the result of "fetch" for the Page with URL https://app.notion.com/p/403aaff542338109a6dbfc2fee32f521 as of 2026-10-24T05:18:52.793Z:
<page url="https://app.notion.com/p/403aaff542338109a6dbfc2fee32f521" icon="🔎">
<ancestor-path></ancestor-path>
<properties>
{"title":"SIH26263 Current College Student Data Reporting Public Evidence — Dharanish & Gopika"}
</properties>
<iconMetadata>{"type":"emoji","emoji":"🔎"}</iconMetadata>
<content>
<callout icon="🔎" color="blue_bg">
<b>Public evidence research — 24 October 2026.</b> Prepared for Dharanish (data architecture) and Gopika (institutional workflows). Findings are based on public documents, NOT a staff interview or a logged-in inspection of the college's portal. Do not record human verification as completed.
</callout>

<mention url="https://app.notion.com/p/402aaff54233818192effc4ad3f86934" /> · <mention url="https://app.notion.com/p/402aaff54233817bae76ef304a3d9cd7" /> · <mention url="https://app.notion.com/p/402aaff54233816086ccdc58d393db39" /> · [SIH project brief](https://github.com/Dharanish99/SIH_APAAR_Student_Verification/blob/main/docs/problem-brief.md)

## Executive finding

<b>AICTE-approved colleges are already directed to submit enrolment information electronically; the proposed SIH gap is incomplete, unevenly granular and potentially non-verifiable student-level reporting across different mechanisms.</b> Distinguish enrolment COUNTS from individual admission records. The supplied SIH26263 text (third-party transcription, official statement cross-check pending) says PGDM institutions provide detailed data while many other approved institutions primarily submit statistics.

<b>Crucial reconciliation:</b> AICTE's Approval Process Handbook 2024–25 to 2026–27, clause 2.25(n) explicitly requires existing institutions to upload enrolment details by 30 November of calendar year. The official AICTE manual for academic year 2023–24 demonstrates reporting by approved course. Hence it is incorrect to say all other colleges submit no data. The key unresolved question is what identifiable fields <i>actually</i> reach AICTE and how they can be verified.

## Source-specific workflow #1 — AICTE approval portal

<b>Official instruction:</b> [AICTE Student Enrolment, Placement and New Initiatives User Manual](https://www.aicte.gov.in/sites/default/files/User_Manual_for_Submitting_Student_Enrollment_Placement_New_Initiative_General_Information.pdf), text procedures on PDF pages 4–6 (0-index PDF pages 3–5).

1. Institution user logs into AICTE Web Portal.
2. Selects Approval Process.
3. Selects Student Enrollment icon.
4. Opens My Institute Application, which lists academic years.
5. Selects 2023–24 (the particular year used as the guide's example) and opens Courses.
6. Enters enrolment against approved courses.
7. Clicks Submit Student Enrollment Data; in the published example the button is disabled after successful submission.

<b>Approval intake source:</b> [AICTE APH](https://www.aicte.gov.in/sites/default/files/APH%20Final.pdf), Chapter II clause 2.25(a)–(b): AICTE's extension-of-approval procedure yields course-specific approved intake and a downloadable EoA letter. Clause 2.25(n): enrolment upload by 30 November. Chapter IV clause 4.17: universities submit by the deadline in applicable academic calendar. <b>Caveat:</b> verify any subsequent circular/extension and 2026 actual portal configuration before treating these as interface screenshots for 2026.

<b>What is verified:</b> authorised portal flow, course-year-based reporting, approved intake/EoA role, handbook deadline.<br /><b>Unknown:</b> precise per-student fields for non-PGDM records, whether APAAR is captured today, live data APIs, editing after submission, and internal integration with college ERP. Interview and authorised portal inspection required.

## Source-specific workflow #2 — PGDM student bulk import

<b>Official APH:</b> [2024–27 Handbook](https://www.aicte.gov.in/sites/default/files/APH%20Final.pdf), Annexure 6 clauses 6.8–6.9: PGDM/PGCM institutes upload students' enrolment in a prescribed format within one month after admission deadline, and certain diplomas/marksheets bear AICTE allotted enrolment numbers.<br /><b>Indexed AICTE-hosted upload manual:</b> [User Manual for Institute to Import PGDM Students Data in Bulk](https://aicte-qa.aicte-india.org/sites/default/files/User%20Manual%20for%20Institute%20to%20Import%20PGDM%20Students%20data%20in%20bulk.pdf); search-indexed text says download <code>PGDM Student Excel.xlsm</code>, fill fields, run Validate and use course IDs. <b>Caveat:</b> direct PDF retrieval returned 502; the precise remaining pages/error behaviours were not personally inspected. This is an older documented import flow, not proof of the live interface in October 2026. Do not assert a current automatic duplicate-retry mechanism.

## Source-specific workflow #3 — AISHE is a separate higher-education survey

[Official AISHE Web DCF](https://aishe.gov.in/web-dcf/) → [2024–25 Blank DCF-II College](https://cdnbbsr.s3waas.gov.in/s392049debbe566ca5782a3045cf300a3c/uploads/2024/12/202507141166032813.pdf), especially printed pages 7–9; the student enrolment grid was visually inspected.

- Includes programme, approved first-year intake, supernumerary seats.
- Student Enrolment grids by programme, year, gender and social categories; minority/PwBD subtotals. Does NOT present individual names/APAAR IDs in this enrolment grid.
- Foreign enrolment module reports categories/countries/counts; university/college-specific modules also contain placement and other metrics.
- [Official 2024–25 AISHE college manual](https://cdnbbsr.s3waas.gov.in/s392049debbe566ca5782a3045cf300a3c/uploads/2024/12/20250728227262067.pdf) explains sign-in, Web DCF, Add New Entry, Save and Lock, and programme-wise grids. This is NOT the AICTE approval portal.

<b>Implication:</b> Aggregate counts have monitoring value but cannot by themselves authenticate the enrolment of a named student.

## Source-specific workflow #4 — TNEA admissions and institution

[Official Tamil Nadu Engineering Admissions 2026 brochure](https://static.tneaonline.org/docs/2_Information_Brochure_2026.pdf?t=1777772121473), p.1: centralised student application and seat allotment for participating government, aided and university colleges, plus surrendered seats of self-financing engineering institutions. Candidate application/allotment information is not the same as confirmed and current institutional enrolment. Gopika must investigate where a joining/withdrawal/update is recorded and who sends it to each authority.

## Source-specific workflow #5 — Tamil Nadu UMIS is already an individual student registry

[Official Tamil Nadu UMIS portal](https://umisdashboard.tnega.org/home): common portal for higher education individual records, institutional validation and scholarship processing.<br />[Government of Tamil Nadu IT Department Policy Note 2024–25](https://it.tn.gov.in/sites/default/files/2025-08/it_e_pn_2024_25.pdf), section 3.3 (printed pp.65–67 / PDF pages 81–83): UMIS collects institution and student data and links to EMIS, NPCI, Aadhaar, e-Sevai and scholarship systems; historical statistic as of 10 Jun 2024: 4,720 institutions in 75 universities onboarded, 27,53,863 approved student records. Not current 2026 totals.<br />[University-hosted UMIS institutional manual, 2023](https://tnteu.ac.in/admin/file_storage/cms/UMIS-STUDENT%20DATA%20.pdf.pdf), pp.14–20 of the embedded guide: institution edits/approves student record; UMIS number created only after validation, and a missing student can be added.<br /><b>Crucial distinction:</b> This example proves <i>some</i> state-level individual verification workflows existed; it does NOT prove AICTE national access or that all colleges follow identical reporting workflows. Need institutional access/provenance and provider permissions before attempting integration.

## Current-data map — source versus claim

| System | What it can substantiate from public documentation | What it alone CANNOT prove |
| --- | --- | --- |
| College registrar/ERP | Local joining, corrections, withdrawal, transfer in operational records (process-specific; not audited here) | Nationally consistent identity or official AICTE receipt |
| TNEA 2026 | Candidate application/eligibility counselling and seat-allotment events | Student actually joined/stayed enrolled |
| AICTE portal + EoA | Approved institution/course/year intake and institution-reported enrolment information | Individual identity verified just because a count was submitted |
| AISHE DCF | Programme-level reporting and social/gender grouping | Unique named student history or cross-college duplicate |
| TN UMIS | Student-level state registry with college verification workflow | Approved nationwide AICTE read access or institution-specific validity |
| APAAR/ABC/DigiLocker | Academic identity and academic claims subject to provider scope/authorisation | Current admission validity or automatic permission to disclose data |

## Example: why numbers cannot detect a repeated learner

<b>Entirely fictional:</b> Campus Alpha reports 120 [B.Tech](http://B.Tech) CSE enrolments; Campus Beta reports 80. An aggregate regulator view sees 200 enrolments. If a student appeared in both, the aggregate alone does not identify the overlap. Conversely, two matching identifiers may legitimately refer to an approved transfer, academic history or allowable simultaneous programmes. Proposed solution: retain person, programme, institution, academic year, effective dates, source, validation status and <i>review outcome</i> separately. Do not conclude 'fraud' from a duplicate flag.

## Claim ledger and limitations

| ID | Evidence/claim | Evidence type | Status/limitation |
| --- | --- | --- | --- |
| PUBLIC-01 | [AICTE APH 2024–27 §2.25](https://www.aicte.gov.in/sites/default/files/APH%20Final.pdf) approved intake, enrolment upload deadline | Official regulatory text | Verified for cited edition; 2026 circular changes not exhaustively reviewed |
| PUBLIC-02 | [AICTE student enrolment manual](https://www.aicte.gov.in/sites/default/files/User_Manual_for_Submitting_Student_Enrollment_Placement_New_Initiative_General_Information.pdf) steps for 2023–24 | Official operational manual | Verified written steps; screenshots/current UI uncertain |
| PUBLIC-03 | [AICTE APH Annexure 6 §§6.8–6.9](https://www.aicte.gov.in/sites/default/files/APH%20Final.pdf) PGDM prescribed individual reporting | Official regulatory text | Verified edition |
| PUBLIC-04 | [AICTE indexed PGDM Excel bulk manual](https://aicte-qa.aicte-india.org/sites/default/files/User%20Manual%20for%20Institute%20to%20Import%20PGDM%20Students%20data%20in%20bulk.pdf) | Official-domain indexed snippet | Partial; direct 502 |
| PUBLIC-05 | [AISHE 2024–25 official DCF-II](https://cdnbbsr.s3waas.gov.in/s392049debbe566ca5782a3045cf300a3c/uploads/2024/12/202507141166032813.pdf) | Official form; page 8 visually inspected | Verified aggregate grid, not national individual upload scope |
| PUBLIC-06 | [AISHE Web DCF](https://aishe.gov.in/web-dcf/) | Ministry of Education portal | Verified separate survey |
| PUBLIC-07 | [TNEA 2026 brochure](https://static.tneaonline.org/docs/2_Information_Brochure_2026.pdf?t=1777772121473) | Official Tamil Nadu primary text | Verified seat-allotment programme scope |
| PUBLIC-08 | [UMIS public portal](https://umisdashboard.tnega.org/home) | TNeGA | Public indexed text, state-specific |
| PUBLIC-09 | [TN Government IT Policy Note §3.3](https://it.tn.gov.in/sites/default/files/2025-08/it_e_pn_2024_25.pdf) | Official government policy note | Dated 2024 statistics, not current totals |
| PUBLIC-10 | [2023 university-hosted UMIS workflow guide](https://tnteu.ac.in/admin/file_storage/cms/UMIS-STUDENT%20DATA%20.pdf.pdf) | University operational manual | Historical implementation, not every college |
| PUBLIC-11 | [Supplied SIH26263 mirror](https://zaidsayyed.in/tools/sih-problem-statements/sih26263) | Third-party problem statement | Official wording still not independently confirmed |

## Questions for Gopika's upcoming staff interviews

<b>Ask staff to demonstrate a real process without sharing identifiable records, usernames, secrets or student exports.</b>

1. Which office owns the final admission register and who authorises submitted figures?
2. Where does the first student-specific record originate: TNEA, registrar ERP, spreadsheet, university portal or another source?
3. Which fields are exported for AICTE? Is it only a count, course/year/gender/category aggregates, or named rows?
4. In the AICTE <i>Student Enrollment</i> screen, what exact fields are visible for 2026–27, and is there any APAAR field?
5. Who does the data entry, review and 'final submit'? What receipt/acknowledgement is retained?
6. How are a late admission, withdrawal, transfer and cancellation corrected after submission?
7. What fields and export/import method exist for AISHE DCF? Is there rekeying from the same spreadsheet?
8. Does your college use Tamil Nadu UMIS? Who validates new students and corrections? Can valid <b>redacted</b> screen structure be discussed?
9. How are TNEA provisional allotments reconciled against actual students who joined?
10. How are foreign nationals, OCI, NRI and supernumerary seats separately represented in source records?
11. Does a repeated upload produce duplicate reports, a clean replay, an error, or an uncertain response? Staff demonstration without private data only.
12. What reports/alert cases would meaningfully help staff or AICTE, and which already exist?
13. Are any authorised APIs/documented provider integrations offered, or is work primarily manual?
14. Which system is regarded as authoritative for changing a student's admission status and who can dispute a mistake?

## Practical deliverables for Dharanish

<b>Now:</b> derive a source-to-claim table and synthetic prototype schema: Institution, Programme, ApprovalVersion, StudentReference, EnrolmentEvent, SubmittedSnapshot, SourceSystem, ImportBatch, ValidationFinding, CorrectionEvent, AccessGrant and AuditEvent.<br /><b>After Gopika interview:</b> check assumptions against observed import methods, screenshots/redacted field labels and approval flow.<br /><b>Priority experiment:</b> create two fictional source systems with partly overlapping enrolments and test whether reporting aggregates hide overlap, while row-level review identifies it without automatic fraud accusations. Keep all data synthetic and label provider integrations MOCK.

<b>Pending human checks:</b> verify first-hand documents; reconcile 2026 handbook/circular nuances; review with Kanishkar and Gopika. This page is a provisional evidence brief, not a confirmed internal workflow for SECE or a statement that a government API is accessible.
</content>
</page>

