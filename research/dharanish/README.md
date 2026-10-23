# Dharanish R P
## Role 4: Data architecture, validation and anomaly detection

[Project](../../README.md) · [Findings](findings.md) · [Evidence register](sources.csv) · [Progress](progress.md)

**Owner:** Dharanish R P  
**Review partner:** Kanishkar B  
**Starting status:** Not started  
**Mission:** Design reliable processing of imperfect institutional data and evaluate useful anomaly detection.

## Questions to answer
1. How should students, enrolments, institutions, courses, approvals, credentials and verification events be separated?
2. How can CSV/Excel or ERP input be mapped, validated and corrected row by row?
3. How will retries, duplicate uploads, partial failures, concurrency and later corrections work?
4. How do we distinguish repeated rows from potentially conflicting enrolments and legitimate history?
5. Which checks are deterministic, and where could statistical or ML methods add measurable value?
6. What workload, freshness, storage and cost assumptions are realistic for a prototype and later pilot?

## Suggested work sequence
1. Use Gopika's workflow, Sudhan's interface constraints, Pranav's rules and Sudhir's access requirements as inputs.
2. Draft the data model, field dictionary and upload-to-validation flow.
3. Construct a reproducible synthetic experiment, suggested size 1,000 fictional records with seeded issues.
4. Compare rules-only validation with one justified anomaly approach if useful; report false alerts and missed issues.
5. Evaluate re-upload, correction, interrupted processing and external-service outage behaviour; document limitations.

## Required outputs
- [ ] Proposed data model and field dictionary.
- [ ] Import, validation, correction and idempotency design.
- [ ] Synthetic fixture generator or labelled synthetic fixture with a README and reproducible commands.
- [ ] Experiment report: seed, workload, expected issues, detections, misses, false positives and timing.
- [ ] Deployment/cost options with units, workload assumptions, date and prototype-versus-production distinction.

Write the main brief in [findings.md](findings.md); use additional files only when they improve clarity. Use the [shared templates](../../templates/README.md).

## Collaboration boundary
No real student dataset. Synthetic performance is not real-world fraud accuracy. Do not treat an anomaly score as a final adverse decision.

**Handoff:** Review implementation feasibility with Kanishkar; request missing rules from Pranav, API constraints from Sudhan and permissions from Sudhir.

## Evidence starting points
Use source entries **S01, S04** in the [source guide](../../docs/source-guide.md).
Check current versions, scope and access independently. Record actual evidence in [sources.csv](sources.csv), with IDs such as `DHA-001`.
Research additional primary sources as needed; this list is not exhaustive.

## Quality bar
- Explain the mechanism in your own words.
- Support material claims with an exact source or documented observation.
- Work through a normal case and at least two failure/edge cases.
- Separate confirmed findings from assumptions, proposals and unknowns.
- State the effect on the solution and the next handoff.
- Present a seven-minute teach-back, followed by questions.

**Question you must defend:** What happens when a college uploads the same file twice and then corrects ten rows?

## AI agent starting instruction
```text
I am Dharanish R P, responsible for Data architecture, validation and anomaly detection.
Read AGENTS.md, team.json, the shared research standards and this folder's current files.
Help me investigate one unanswered question from this assignment.
Open primary sources, record evidence and uncertainty, and explain the concept to me.
Update my findings, sources and progress only with work actually performed.
Do not invent research, external access, measurements or human review.
```
