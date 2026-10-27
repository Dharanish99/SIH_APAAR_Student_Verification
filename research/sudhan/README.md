# Sudhan
## Role 2: APAAR, ABC, DigiLocker/NAD and integration feasibility

[Project](../../README.md) · [Findings](findings.md) · [Evidence register](sources.csv) · [Progress](progress.md)

**Owner:** Sudhan
**Review partner:** Sudhir
**Current status:** Desk research complete; provider access, human review and field validation pending. See the [current integration review](integration-review.md).<br>
**Mission:** Establish what can actually be verified or exchanged and what access is required.

## Questions to answer
1. How do APAAR identity, ABC credits, DigiLocker and NAD relate, and what does each service establish?
2. What separately proves an ID's format, existence and association with a person?
3. Which documented interfaces cover required operations, and who can use them?
4. What partner registration, permissions, agreements, sandbox access or institutional sponsorship are needed?
5. How should outages, expired permissions, unmatched identities and unsuccessful checks be represented?
6. What documented routes cover missing or corrected IDs and foreign students? What remains unresolved?

## Suggested work sequence
1. Read official documentation and distinguish school workflows from higher-education workflows.
2. Create an operation-by-operation integration matrix with exact documentation and access requirements.
3. Investigate sandbox availability; test only with authorised credentials and synthetic or approved data.
4. Separate documentation found, access available, integration tested and simulated adapter states.
5. Define verification statuses and failure responses, and send blocking access dependencies to Kanishkar immediately.

## Required outputs
- [x] Ecosystem map and explanation: integration review section 1.
- [x] Integration matrix: operation, provider, source, access, response evidence, tested status, fallback; sections 2–4.
- [x] Verification-state and outage-handling proposal: section 5.
- [x] External dependency list and official clarification questions: sections 6 and 9.
- [x] Explicitly simulated contract proposal: section 8 and [12 designed scenarios](contract-scenarios.csv). No experiment was executed and no authorised live access is evidenced.

These checks record AI-assisted desk-research coverage, not human approval or implemented capability. The original human findings remain preserved and their corrections are explicit.

Write the main brief in [findings.md](findings.md); use additional files only when they improve clarity. Use the [shared templates](../../templates/README.md).

## Collaboration boundary
Never infer an endpoint, checksum or permission from an AI answer. A prototype-generated ID is not a government-issued APAAR ID.

**Handoff:** Give Dharanish confirmed input/output constraints and Sudhir access/consent requirements. Resolve security and permission questions together.

## Evidence starting points
Use source entries **S02, S03, S04, S05** in the [source guide](../../docs/source-guide.md).
Check current versions, scope and access independently. Record actual evidence in [sources.csv](sources.csv), with IDs such as `SUD-001`.
Research additional primary sources as needed; this list is not exhaustive.

## Quality bar
- Explain the mechanism in your own words.
- Support material claims with an exact source or documented observation.
- Work through a normal case and at least two failure/edge cases.
- Separate confirmed findings from assumptions, proposals and unknowns.
- State the effect on the solution and the next handoff.
- Present a seven-minute teach-back, followed by questions.

**Question you must defend:** What exactly does our verified badge prove?

## AI agent starting instruction
```text
I am Sudhan, responsible for APAAR, ABC, DigiLocker/NAD and integration feasibility.
Read AGENTS.md, team.json, the shared research standards and this folder's current files.
Help me investigate one unanswered question from this assignment.
Open primary sources, record evidence and uncertainty, and explain the concept to me.
Update my findings, sources and progress only with work actually performed.
Do not invent research, external access, measurements or human review.
```
