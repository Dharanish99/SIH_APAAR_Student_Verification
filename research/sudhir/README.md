# Sudhir
## Role 5: Privacy, security, consent and credential verification

[Project](../../README.md) · [Findings](findings.md) · [Evidence register](sources.csv) · [Progress](progress.md)

**Owner:** Sudhir
**Review partner:** Sudhan
**Current status:** member research plus AI reconciliation ready for review (round 2026-10-26; rechecked 2026-10-27)
**Mission:** Define trustworthy access and credential verification with appropriate data protection.

Sudhir's substantive [26 October submission](original-2026-10-26/findings.md), with self-disclosed AI assistance, was recovered after the initial template baseline. Its original four files remain preserved. Read the [contribution review](human-contribution-review.md) for attribution, retained ideas, corrections and source mapping; the current AI supplements are not human-approved findings.

## Questions to answer
1. What can each institutional operator/approver, regulator, student, employer and administrator do?
2. How should institution boundaries, purposes and record ownership constrain access?
3. Which purposes depend on consent, and how do scope, expiry and withdrawal work?
4. Which current legal provisions apply, including commencement dates and treatment of minors?
5. How should fields be minimised, retained, corrected and protected?
6. How do issuer authentication, signatures, current validity, correction and revocation support credential trust?

## Suggested work sequence
1. Build an actor/action/data permission matrix; consider both institution and purpose restrictions.
2. Read authoritative privacy/security requirements and distinguish enacted, commenced and future provisions.
3. Model at least eight realistic threats including cross-institution access, ID enumeration, forged uploads, compromised accounts and leaked verification links.
4. Design a minimal disclosure workflow and credential verification lifecycle.
5. Review proposed integration permissions with Sudhan and schema/storage decisions with Dharanish.

## Required outputs
- [x] Proposed role/action/resource permission matrix.
- [x] Data inventory: field, purpose, source, visibility, proposed retention and rationale.
- [x] Proposed consent and third-party verification workflow.
- [x] Threat model with thirteen abuse cases, mitigations and residual risks.
- [x] Credential verification design and unresolved legal/access questions.

Checkmarks mean research artifacts exist, not implemented controls, passed security tests or Sudhir's approval. See [findings](findings.md), [legal status](legal-status.md), [privacy design](privacy-design.md), [threat model](threat-model.md) and [AI critique](critique-log.md). Human review and teach-back remain pending.

Write the main brief in [findings.md](findings.md); use additional files only when they improve clarity. Use the [shared templates](../../templates/README.md).

## Collaboration boundary
Knowing an ID is not authorisation. Do not claim legal compliance based on a generic checklist. Do not post real vulnerabilities with sensitive details publicly.

**Handoff:** Send access and data constraints to Sudhan and Dharanish; raise policy conflicts or deployment blockers with Kanishkar.

## Evidence starting points
Use source entries **S04, S05, S08** in the [source guide](../../docs/source-guide.md).
Check current versions, scope and access independently. Record actual evidence in [sources.csv](sources.csv), with IDs such as `SUH-101`.
Research additional primary sources as needed; this list is not exhaustive.

## Quality bar
- Explain the mechanism in your own words.
- Support material claims with an exact source or documented observation.
- Work through a normal case and at least two failure/edge cases.
- Separate confirmed findings from assumptions, proposals and unknowns.
- State the effect on the solution and the next handoff.
- Present a seven-minute teach-back, followed by questions.

**Question you must defend:** If someone knows my APAAR ID, what can they see, and why?

## AI agent starting instruction
```text
I am Sudhir, responsible for Privacy, security, consent and credential verification.
Read AGENTS.md, team.json, the shared research standards and this folder's current files.
Help me investigate one unanswered question from this assignment.
Open primary sources, record evidence and uncertainty, and explain the concept to me.
Update my findings, sources and progress only with work actually performed.
Do not invent research, external access, measurements or human review.
```
