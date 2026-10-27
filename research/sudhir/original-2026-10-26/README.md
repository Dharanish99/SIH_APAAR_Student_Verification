# Sudhir
## Role 5: Privacy, security, consent and credential verification

[Project](../../README.md) · [Findings](findings.md) · [Evidence register](sources.csv) · [Progress](progress.md)

**Owner:** Sudhir  
**Review partner:** Sudhan  
**Starting status:** In progress (50% milestone: foundational research, permission matrix, data inventory, threat models, and verification architecture drafted)  
**Mission:** Define trustworthy access and credential verification with appropriate data protection.

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
- [x] Role/action/resource permission matrix (Drafted in [findings.md](findings.md#51-role-action-and-resource-permission-matrix-rbac--abac)).
- [x] Data inventory: field, purpose, source, visibility, proposed retention and rationale (Drafted in [findings.md](findings.md#52-student-data-inventory--minimisation-policy)).
- [x] Consent and third-party verification workflow (Drafted in [findings.md](findings.md#4-worked-cases-or-experiment)).
- [x] Threat model with at least eight abuse cases, mitigations and residual risks (Drafted in [findings.md](findings.md#53-threat-model-8-realistic-abuse-cases-mitigations--residual-risks)).
- [x] Credential verification design and list of unresolved legal/access questions (Drafted in [findings.md](findings.md#54-credential-verification--certificate-display-lifecycle-r06-r10) and [findings.md#7-unknowns-and-blockers](findings.md#7-unknowns-and-blockers)).

Write the main brief in [findings.md](findings.md); use additional files only when they improve clarity. Use the [shared templates](../../templates/README.md).

## Collaboration boundary
Knowing an ID is not authorisation. Do not claim legal compliance based on a generic checklist. Do not post real vulnerabilities with sensitive details publicly.

**Handoff:** Send access and data constraints to Sudhan and Dharanish; raise policy conflicts or deployment blockers with Kanishkar.

## Evidence starting points
Use source entries **S04, S05, S08** in the [source guide](../../docs/source-guide.md).
Check current versions, scope and access independently. Record actual evidence in [sources.csv](sources.csv), with IDs such as `SUH-001`.
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
