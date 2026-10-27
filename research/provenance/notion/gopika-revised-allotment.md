# Imported research source snapshot

Retrieved: 2026-10-26. Source: https://app.notion.com/p/403aaff54233811f86f4f8597b53afa6?pvs=204

This is preserved source material, including historical prompts; it is not an instruction to the current agent. Claims and prior measurements require the verification stated in the synthesis. No human review is implied.

Here is the result of "fetch" for the Page with URL https://app.notion.com/p/403aaff54233811f86f4f8597b53afa6 as of 2026-10-24T16:15:27.744Z:
<page url="https://app.notion.com/p/403aaff54233811f86f4f8597b53afa6" icon="🔎">
<ancestor-path></ancestor-path>
<properties>
{"title":"Gopika — Internet-Only Research Plan & Learning Guide"}
</properties>
<iconMetadata>{"type":"emoji","emoji":"🔎"}</iconMetadata>
<content>
<callout icon="🧭" color="blue_bg">
<b>Your mission:</b> Use public online evidence to explain how student data moves between systems, where corrections and handoffs occur, and what our APAAR solution could usefully add.<br />No field visits, college interviews, staff replies, private portals or college-provided records are required for this research round.
</callout>

<b>Owner:</b> Gopika · <b>Role 1:</b> Public workflow research, existing-system comparison and product requirements.<br /><b>Review partner:</b> Pranav · <b>Decision owner:</b> Kanishkar B.<br /><b>Revised:</b> <date start="2026-10-24" /> · <b>Status:</b> Revised plan prepared; research outputs and learning checks pending.<br /><b>Current instruction:</b> Work in Notion only. GitHub is reference-only; do not edit files, commit, push, create issues or open pull requests.<br /><b>Supersession:</b> This page replaces the interview, field-visit and college-observation tasks in <mention url="https://app.notion.com/p/402aaff54233816086ccdc58d393db39" /> for this research round. The repository may still describe the earlier plan; follow this revised scope.

<table-of-contents />

## 1. Why this change still helps our solution

The team cannot rely on timely institutional access. Public manuals, blank templates, government guidance and documented product features can still establish actors, data requirements, correction paths and existing capabilities.<br />Your output should help the team decide <b>what to build, what already exists, and which assumptions remain untested</b>. It should not claim to describe your college’s actual practices.<br />An online document can show that a process exists. It usually cannot show how often people struggle with it, how long it takes, whether they would adopt our product or whether our product saves time. Keep those as later validation questions, not blockers for finishing this round.

## 2. What changes in your assignment

<table fit-page-width="true" header-row="true">
<tr>
<td>
Earlier activity
</td>
<td>
Replacement for this round
</td>
<td>
Useful result
</td>
</tr>
<tr>
<td>
Visit college offices and interview staff/students
</td>
<td>
Inspect official manuals, FAQs and public walkthroughs
</td>
<td>
Source-backed actor and task map
</td>
</tr>
<tr>
<td>
Request college spreadsheets or private forms
</td>
<td>
Read publicly published blank templates and field definitions
</td>
<td>
Data requirements and mapping questions
</td>
</tr>
<tr>
<td>
Observe a real submission or correction
</td>
<td>
Reconstruct documented steps and walk through fictional cases
</td>
<td>
Reference workflow and exception table
</td>
</tr>
<tr>
<td>
Measure staff workload and repeated effort
</td>
<td>
Count documented steps only; propose a later measurement method
</td>
<td>
Process-complexity observations, with limits
</td>
</tr>
<tr>
<td>
Rank observed college pain points
</td>
<td>
Rank candidate opportunities by evidence, relevance and dependency
</td>
<td>
Five provisional opportunities for MVP discussion
</td>
</tr>
</table>

## 3. The five questions you own

1. <b>Who does what?</b> Which applicant, operator, approver or verifier handles each documented task?
2. <b>What moves between systems?</b> Which fields, files, identifiers, statuses and approvals are needed?
3. <b>What happens when something changes?</b> How are missing values, mismatches, rejected uploads, corrections and changed enrolments represented?
4. <b>What already exists?</b> Which relevant functions are documented in an ERP/student portal, an academic-award service and a reporting system?
5. <b>What useful addition is defensible?</b> Which proposed feature addresses a documented requirement or a clearly labelled hypothesis without duplicating existing functionality?<br /><b>Scope boundary:</b> Sudhan investigates actual API access; Pranav interprets admission rules; Dharanish designs processing and experiments; Sudhir owns security/privacy design. You identify workflow needs and questions for them. Do not duplicate their full research.

## 4. Start with these public sources

The links below were inspected during plan preparation on <date start="2026-10-24" />. “Inspected” describes the stated page/section only; linked files and current operational behaviour still require checking.

### A. Samarth Student Portal — existing student-data capabilities

[Open the official Student Portal guide](https://docs.samarth.ac.in/docs/academics/student/)<br /><b>Read:</b> Import Students; Feature & Functionality; Role Access; New Student Registration.<br /><b>Preparation finding:</b> The guide documents individual/bulk import, validation and allocation, and notes automatic import when students were admitted using the Samarth Admission Portal. It identifies version 1.4.12 and a July 2024 update.<br /><b>Extract:</b> Actor → action → input → output/status → source section.<br /><b>Solution implication:</b> Upload and validation alone are weak novelty claims. Investigate what additional requirement our project addresses.<br /><b>Limit:</b> These are documented capabilities for that product/version, not proof of usage or performance at every institution. Do not assume a technical integration from a feature description.

### B. Samarth Admissions Admin Guide — configuration and responsibilities

[Open the official admin guide](https://docs.samarth.ac.in/docs/academics/admissions2026/)<br /><b>Read:</b> Pre-launch Readiness; Programme Configuration; Student View — End-to-End Check.<br /><b>Preparation finding:</b> The guide covers the 2026–27 admission configuration process and documents checks for eligibility settings, fees, notices and the applicant-facing journey.<br /><b>Extract:</b> Configuration owner, prerequisites, student-visible effects and checks.<br /><b>Limit:</b> A configuration checklist is not an AICTE rule source and does not establish that any college follows every step.

### C. Uttarakhand Higher Education — applicant perspective

[Official source page](https://he.uk.gov.in/samarth-admission-portal/) · [Applicant guide PDF](https://cdnbbsr.s3waas.gov.in/s39ed9328611fe3f45b3cce8ffe386ee97/uploads/2025/02/20250204985748285.pdf)<br /><b>Read:</b> The Admission Process; Profile Details; Uploads; Preview; Programme Selection.<br /><b>Extract:</b> What the applicant supplies, sees and submits; where correction guidance is explicit or absent.<br /><b>Limit:</b> This is one state’s published workflow. It is a useful reference case, not a universal model for AICTE-approved institutions. Record the document’s stated year/version; do not infer publication date solely from the URL.

### D. DigiLocker NAD Resource Centre — academic-record formats

[Open the official resource centre](https://nad.digilocker.gov.in/resource-center)<br /><b>Read:</b> College Template & Guidelines; relevant data-definition documents; current User Manual.<br /><b>Preparation finding:</b> The page lists college marksheet and certificate CSV templates, their guidelines and a user manual. The listing currently identifies manual version 1.4.<br /><b>Extract:</b> Public field definitions, mandatory/optional distinctions, format constraints and documented correction steps from the files you actually open.<br /><b>Access caveat:</b> The separate [user-manual route](https://nad.digilocker.gov.in/user_manual) returned 403 during preparation; indexed results referenced an older version. Prefer the current resource listing and record any inaccessible download. Do not combine versions silently.<br /><b>Limit:</b> Academic-award publication is different from admission approval. Public templates do not grant access to publish or verify records.

### E. AISHE Web DCF — reporting reference, optional depth

[Official forms and manuals](https://aishe.gov.in/web-dcf/) · [College/Standalone manual PDF](https://cdnbbsr.s3waas.gov.in/s392049debbe566ca5782a3045cf300a3c/uploads/2024/12/20250728227262067.pdf) · [Blank college DCF PDF](https://cdnbbsr.s3waas.gov.in/s392049debbe566ca5782a3045cf300a3c/uploads/2024/12/202507141166032813.pdf)<br /><b>Preparation finding:</b> The official listing labels these resources 2024–25. The manual describes reviewing pre-filled institutional details and selecting the survey year before working through reporting modules.<br /><b>Extract:</b> Reporting year, programme/enrolment concepts, summary fields and validation dependencies.<br /><b>Limit:</b> AISHE reporting must not be presented as AICTE student-level verification. Distinguish individual records from aggregate counts. Do not infer that a shared field implies an integration or duplicated manual entry. Check for a later applicable version.

### F. Project and ecosystem — context only

[Supplied problem statement](https://zaidsayyed.in/tools/sih-problem-statements/sih26263) · [APAAR official FAQs](https://apaar.education.gov.in/faqs) · [GitHub assignment, read-only](https://github.com/Dharanish99/SIH_APAAR_Student_Verification/blob/main/research/gopika/README.md)<br />Use the supplied statement to trace requirements, and seek official SIH corroboration when accessible. Treat the third-party statement as supplied project context. The APAAR FAQ is an additional starting source to reopen; it is not evidence of this team’s API eligibility.<br /><b>Search only to fill a gap:</b> Try exact task terms such as <code>site:docs.samarth.ac.in "Import Students"</code>, <code>site:nad.digilocker.gov.in correction CSV</code>, or <code>site:aishe.gov.in "Web DCF"</code>. Prefer an original government/provider page over reposted PDFs. An official public engineering-institution manual can be an optional comparison, with no contact required.

## 5. Execute in four focused sessions

<b>Core estimate: about 4½ hours of active work, split as convenient.</b> This is a planning estimate, not a deadline. Add time only for unresolved consequential questions.

<table fit-page-width="true" header-row="true">
<tr>
<td>
Session
</td>
<td>
Work
</td>
<td>
Stop condition
</td>
</tr>
<tr>
<td>
1 · 45 minutes
</td>
<td>
Read the project brief and selected Samarth/NAD sections. Define applicant, enrolment, credential, validation, correction and handoff. Start evidence cards.
</td>
<td>
Explain the project and identify the source for each key concept.
</td>
</tr>
<tr>
<td>
2 · 90 minutes
</td>
<td>
Build two reference workflows: admission/import-to-validation; academic-record preparation-to-publication/correction. List missing links instead of inventing them.
</td>
<td>
Every step is sourced or explicitly a proposed/unknown step.
</td>
</tr>
<tr>
<td>
3 · 90 minutes
</td>
<td>
Make the system comparison, a compact field map and six fictional exception cases. Draft five opportunity cards.
</td>
<td>
Each recommendation has evidence, a limit and a team handoff.
</td>
</tr>
<tr>
<td>
4 · 45 minutes
</td>
<td>
Write a one-page decision brief, independently explain two passages, then do the team teach-back.
</td>
<td>
Brief ready; learning and review status recorded honestly.
</td>
</tr>
</table>

If a source is blocked, try its official resource index and one official alternative. Then record the gap and proceed. No account creation, private login, waiting for a response or college visit is required.

## 6. Your deliverables in this Notion page

### D1 — Two reference workflows

For each step record <b>actor, action, input, output/status, source/section and exception</b>. Keep system boundaries visible. Any proposed connection between Samarth, NAD or our platform must be labelled a design proposal; manuals from separate services do not prove an existing end-to-end integration.

### D2 — A compact field map

Aim for about 10–15 useful concepts supported by inspected documents: identifier, programme, academic year, enrolment status, award type and other relevant fields.<br />Record <b>exact source field name → meaning → record or aggregate level → format → mandatory status if documented → proposed mapping → ambiguity</b>.<br />Do not assume two similarly named fields have identical meanings. If a template cannot be opened, do not invent its column names.

### D3 — A fair comparison of four system categories

Compare <b>student ERP/portal, APAAR/ABC ecosystem, NAD/DigiLocker academic awards and reporting portals such as AISHE</b> by purpose, actor, documented capability, evidence and relevance to our project.<br />Use <b>documented / explicitly unsupported / not found / not applicable</b>. “Not found” never means “the product cannot do it.” These systems can be complementary; do not force them into one competitor ranking.

### D4 — Six fictional scenario cards

1. A valid new record proceeds through the documented path.
2. A required value is missing before submission.
3. A name or identifier differs across records.
4. A previously submitted record needs correction.
5. The same file is submitted again.
6. A withdrawal or course change occurs after an earlier submission.<br />For each: <b>trigger → affected actor → documented handling, if found → proposed handling → unresolved question → teammate owner</b>.<br />The last two may have no published handling in the inspected sources; that is a valid unknown. An identifier mismatch is not automatically fraud.

### D5 — Five opportunity cards and one-page decision brief

For each opportunity record <b>source-backed trigger, affected task, proposed benefit, existing capability, what remains unproven, dependency and a simple future evaluation</b>.<br />Prioritise High / Medium / Low with a short explanation based on project relevance, evidence strength, MVP effort and access dependencies. Leave frequency, adoption demand and time savings unknown unless supported by suitable evidence.<br />Finish the brief with <b>build candidate / investigate further / already covered elsewhere / defer</b>, and explain the recommendation.<br /><b>Example hypothesis, not a finding:</b> “A pre-submission checklist might reduce avoidable correction cycles.” This needs evidence of relevant checks and later comparison; it does not justify claiming a measured time reduction.

### D6 — Evidence and uncertainty ledger

Use one row per important claim:<br /><code>ID | claim | source URL | publisher | document version/year | accessed date | section/page | claim type | scope | limitation | solution implication</code><br />Use temporary IDs such as <b>GOP-WEB-01</b> to keep this round distinct from the repository’s existing register. Do not renumber or modify GitHub.<br />Claim types: <b>Documented fact / Researcher observation / Inference / Proposal / Unknown</b>. A walkthrough of a manual is a researcher exercise, not an interview or a real user test.

## 7. How to turn a source into a useful conclusion

<b>Documented fact:</b> Samarth’s Student Portal guide describes importing, validating and allocating student records. [Source: Import Students](https://docs.samarth.ac.in/docs/academics/student/)<br /><b>Inference:</b> A generic upload-and-validate feature may overlap with an existing system. This is an assessment of overlap, not proof that no institution needs it.<br /><b>Proposal:</b> Investigate whether clearer cross-system correction history or requirement-specific checks add value.<br /><b>Unknown:</b> Whether the intended institutions already have those capabilities, would adopt the proposal, or would save time.<br /><b>Handoff:</b> Ask Sudhan about feasible interfaces, Dharanish about correction history and Pranav about applicable checks. These questions can be investigated within the team without contacting a college.

## 8. Learn it yourself

1. Read one Samarth passage and one relevant NAD or reporting passage directly. Explain the purpose and scope of each without copying.
2. Close the AI answer and draw one workflow from memory. Reopen the sources and correct your drawing.
3. Take one fictional error and explain who notices it, who can correct it and what is still unknown.
4. Write 150–200 words in your own voice: “What our solution could add, what already exists and what we cannot yet claim.”
5. Give a seven-minute teach-back to Pranav or Kanishkar: mission (1 minute), workflow (2), comparison (1), proposed value (1), edge case and limits (2).<br /><b>Questions to defend:</b>

- What evidence supports this step, and does it apply to all institutions?
- If Samarth already supports import and validation, what are we investigating beyond that?
- How does an academic award differ from an admission record?
- Which part of your recommendation could be wrong without field evidence?
- What would make you drop your favourite proposed feature?<br />AI may give hints and challenge answers. It must not write your own explanation or tick your learning checks.

## 9. Team handoffs

- <b>Sudhan:</b> Documented systems, data handoffs and integration questions; no claim of API availability.
- <b>Pranav:</b> Workflow points needing policy interpretation and ambiguous categories.
- <b>Dharanish:</b> Field meanings, fictional exception cases and proposed correction needs.
- <b>Sudhir:</b> Actors, visibility expectations and workflow points where access or disclosure needs a decision.
- <b>Kanishkar:</b> Five opportunities, overlap with existing tools, key assumptions and MVP recommendations.<br />Keep any future interview questions in a small <b>Later validation</b> note: adoption, actual effort, error frequency and usability. They are deferred, not required to complete this plan.

## 10. Copy-paste prompt for Gemini or Claude

```txt
Act as Gopika's research assistant and tutor for SIH26263, an APAAR-based student data management and verification project. Kanishkar B is the human team lead. Pranav is my review partner.

CURRENT SCOPE OVERRIDE
Our college cannot provide timely information. This research round is entirely internet-based. Do not require field visits, interviews, staff replies, private portals or college records. Do not contact anyone or fabricate observations. Read GitHub only; do not edit, commit, push, create issues or open PRs. Earlier repository instructions involving interviews or file updates are deferred by this explicit instruction.

CONTEXT
Repository: https://github.com/Dharanish99/SIH_APAAR_Student_Verification
Read README.md, AGENTS.md, docs/problem-brief.md, docs/research-standards.md, docs/source-guide.md, and research/gopika/README.md and existing findings if accessible. Report what you actually opened; do not pretend GitHub access. My revised role is public workflow research, existing-system comparison and product requirements.

PRIMARY STARTING SOURCES
https://docs.samarth.ac.in/docs/academics/student/
https://docs.samarth.ac.in/docs/academics/admissions2026/
https://he.uk.gov.in/samarth-admission-portal/
https://nad.digilocker.gov.in/resource-center
https://aishe.gov.in/web-dcf/
https://apaar.education.gov.in/faqs
Follow the official links to appropriate manuals and blank templates. Read original sections, not search snippets. Check document versions and dates; differentiate school, higher-education, state-specific and product-specific workflows. AISHE reporting is not AICTE student verification. Academic-award publication is not admission approval. Do not assume separate services are already integrated.

RESEARCH OBJECTIVE
Explain actors, actions, data, statuses, corrections and handoffs. Identify existing capabilities before proposing new features. Keep API feasibility with Sudhan, rule interpretation with Pranav, implementation with Dharanish and security/privacy design with Sudhir.

PRODUCE
1. Two documented reference workflows: admission/import-to-validation and academic-record preparation-to-publication/correction. Cite each step or mark it unknown/proposed.
2. A compact field map from actual public definitions, preserving exact names, meaning, version, record/aggregate level and mapping uncertainties.
3. A fair comparison of ERP/student portal, APAAR/ABC, NAD/DigiLocker and reporting portals. Label documented, explicitly unsupported, not found or not applicable. Absence from docs does not prove absence from a product.
4. Six fictional cases: normal record, missing value, mismatch, correction, duplicate submission and withdrawal/course change. Separate documented handling from proposed handling.
5. Five candidate opportunity cards and a one-page decision brief. Include source-backed trigger, existing capability, proposed value, limitation, dependency, priority reasoning and future evaluation.
6. Claim/source ledger and unresolved questions. Keep time saved, demand and error frequency unknown without evidence.

METHOD
Start with a brief capability check and plan, then research. Use current primary documents for consequential claims. Record URL, publisher, version/year, access date and exact section/page. Separate Documented fact, Researcher observation, Inference, Proposal and Unknown. Preserve contradictions. If blocked, try the official resource index and one official alternative, then record the gap. Never invent fields, endpoints, measurements or user feedback. Use synthetic examples only, with no real student data or identifiers.

TEACH ME
Define unfamiliar terms in plain English. Explain a normal case and two exceptions. Require me to read two source passages, draw a workflow without copying and explain one new scenario. Complete a provisional research draft even while my answers are pending, but do not mark learning complete. Ask one teach-back question at a time, wait for my response, offer a hint and then test a fresh case. Do not write my personal reflection in my voice or fabricate human review.

DELIVERY
Use the revised Gopika Notion page supplied in this conversation as the plan. If I give you a writable research notebook, fetch it first and preserve existing content while adding findings. Otherwise create a private research-notebook draft if supported, or return import-ready Markdown and state that it was not saved. Keep GitHub unchanged.
End with findings, evidence limits, handoffs, actual saved-page link if any, and one unanswered teach-back question. Identify later field-validation needs as deferred, not prerequisites.
```

## 11. Completion checklist

- [ ] Two reference workflows have evidence or explicit unknown labels for every step.
- [ ] Field mappings come from inspected public documents.
- [ ] The comparison recognises existing functionality and complementary system roles.
- [ ] Six fictional scenarios distinguish documented and proposed handling.
- [ ] Five opportunities include evidence, limitations and dependencies.
- [ ] The one-page brief makes a clear recommendation without invented benefits.
- [ ] I read two primary passages, completed my own explanation and answered a new case.
- [ ] Human review and remaining corrections are recorded only after they happen.
- [ ] All work remains in Notion; no GitHub changes were made.<br /><b>Research-ready</b> means the evidence and limitations are documented. <b>Learning demonstrated</b> requires Gopika’s own answers. <b>Field validated</b> remains deferred for this round.
</content>
</page>

