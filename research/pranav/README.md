# Pranav
## Role 3: AICTE admission rules and compliance logic

[Project](../../README.md) · [Findings](findings.md) · [Evidence register](sources.csv) · [Progress](progress.md)

**Owner:** Pranav
**Review partner:** Gopika
**Starting status:** Not started (original assignment); **current status:** AI research supplement ready for human review, 2026-10-27.
**Mission:** Translate authoritative, applicable admission policies into explainable checks.

## Questions to answer
1. Which approval record establishes institution/course/year capacity?
2. How do approved intake, regular seats and each relevant supernumerary category differ?
3. How do nationality/status and the seat category actually used relate?
4. Which rules cover NRI, OCI, Foreign National, lateral entry and other applicable categories?
5. How do transfers, withdrawals, course changes and simultaneous programmes affect validation?
6. Which cases should pass, fail or require review, and who has authority to resolve them?

## Suggested work sequence
1. Locate the AICTE handbook, applicable amendments/corrigenda and current institution-specific approval records.
2. For each rule capture its clause, applicable academic year, institution/course scope and exceptions.
3. Read applicable UGC simultaneous-programme guidance and modifications rather than assuming a repeated identity is misconduct.
4. Produce at least 12 fictional worked scenarios covering valid, invalid and ambiguous cases.
5. Record policy uncertainties; send versioned rules and expected outcomes to Dharanish.

## Required outputs
- [x] AI-authored [rule catalogue](rule-catalogue.md): 14 proposed checks with source/scope/input/outcome boundaries.
- [x] [22 fictional worked scenarios](worked-cases.md) with expected outcomes and reasoning.
- [x] Approval-data authority and correction process proposal in the [full findings](findings-2026-10-26.md).
- [x] Questions needing official clarification and [access/amendment limitations](access-and-amendment-log.md).
- [x] Boundary between automatic validation, warning and competent-authority adjudication.
- [ ] Human review, authoritative current policy-pack approval and field validation (not claimed).

Write the main brief in [findings.md](findings.md); use additional files only when they improve clarity. Use the [shared templates](../../templates/README.md).

## Collaboration boundary
Do not hardcode a percentage from an old handbook or apply one category's rules to all programmes. Recommendations are not legal determinations.

**Handoff:** Give Dharanish rule definitions and scenario outcomes. Reconcile operational practicality with Gopika and disputed policies with Kanishkar.

## Evidence starting points
Use source entries **S06, S07** in the [source guide](../../docs/source-guide.md).
Check current versions, scope and access independently. Record actual evidence in [sources.csv](sources.csv), with IDs such as `PRA-102`.
Research additional primary sources as needed; this list is not exhaustive.

## Quality bar
- Explain the mechanism in your own words.
- Support material claims with an exact source or documented observation.
- Work through a normal case and at least two failure/edge cases.
- Separate confirmed findings from assumptions, proposals and unknowns.
- State the effect on the solution and the next handoff.
- Present a seven-minute teach-back, followed by questions.

**Question you must defend:** Why was this admission flagged, and which applicable rule supports that decision?

## AI agent starting instruction
```text
I am Pranav, responsible for AICTE admission rules and compliance logic.
Read AGENTS.md, team.json, the shared research standards and this folder's current files.
Help me investigate one unanswered question from this assignment.
Open primary sources, record evidence and uncertainty, and explain the concept to me.
Update my findings, sources and progress only with work actually performed.
Do not invent research, external access, measurements or human review.
```
