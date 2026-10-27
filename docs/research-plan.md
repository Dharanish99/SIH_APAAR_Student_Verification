# Research plan

**Continuation status, 27 October 2026:** The desk-research round and independent synthesis are complete. This original plan is retained for context. Actual completion and external gates are recorded in [status](status.md), [assignment audit](research-audit.md), [report](solution-report.md) and [validation](validation.md). Suggested sprint days below are not observed durations.

## Objective
Produce a coherent, feasible solution supported by sources, operational observations and small experiments. See [member assignments](../research/README.md).

## Suggested three-working-day sprint
Allow roughly 6–8 focused research hours per member plus shared reviews. This is an internal suggestion, not an SIH deadline.

| Stage | Activity | Exit evidence |
|---|---|---|
| Day 1 — facts and scope | 30-minute team briefing; source reading; interview planning | Five supported findings or clearly marked preliminary observations, three unknowns and blockers per member |
| Day 2 — test assumptions | Interviews, worked policy cases, permitted integration checks, synthetic experiments | Concrete case/experiment and a draft recommendation in each workstream |
| Day 3 — synthesis | Pair review; seven-minute teach-back plus five-minute Q&A per member | Reviewed briefs, MVP proposal, dependency list and remaining decisions |

If access or interviews are unavailable, record the gap and fallback. Do not invent evidence to satisfy the schedule.

## Handoffs
| From | To | Information |
|---|---|---|
| Gopika | Sudhan, Dharanish | Actual workflows, systems and blank input structures |
| Sudhan | Dharanish, Sudhir | Documented interfaces, access evidence and permission constraints |
| Pranav | Dharanish | Versioned rules, exceptions and worked outcomes |
| Sudhir | Sudhan, Dharanish | Access boundaries, data requirements and trust mechanisms |
| All owners | Kanishkar | Findings, sources, risks, alternatives and unresolved decisions |

Review pairs: Gopika ↔ Pranav; Sudhan ↔ Sudhir; Dharanish ↔ Kanishkar.
Send blocking findings promptly rather than waiting for the final review.

## Common deliverable
A 2–4-page equivalent main brief in each findings.md, with appendices where helpful:
question; own explanation; evidence; example/experiment; implications; alternatives; recommendation; unknowns; handoff.
Use [research standards](research-standards.md) and [templates](../templates/README.md).

## Readiness for implementation
- [ ] All ten requirements have research coverage.
- [ ] At least one real operational workflow has been investigated, or that evidence gap is explicit.
- [ ] Critical policy rules have scope, version and exceptions.
- [ ] External operations are classified as accessible/tested, documented only, simulated or unavailable.
- [ ] Identity, admission and credential claims have separate evidence.
- [ ] Synthetic experiments are reproducible and limitations are explicit.
- [ ] Access and correction workflows are designed.
- [ ] Kanishkar records the MVP decision, alternatives and remaining risks.
- [ ] Prototype success criteria are measurable without invented impact estimates.

## Candidate evaluation measures — targets not yet set
Import correctness and re-upload behaviour; rule-case correctness; false alerts and missed seeded issues; processing time at stated load; cross-institution access denial; verification disclosure scope; correction traceability; user-task completion.
The lead sets realistic targets after baseline evidence and experiments.
