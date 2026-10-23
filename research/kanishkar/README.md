# Kanishkar B
## Role 6: Team lead: synthesis, feasibility, MVP and evaluation

[Project](../../README.md) · [Findings](findings.md) · [Evidence register](sources.csv) · [Progress](progress.md)

**Owner:** Kanishkar B  
**Review partner:** All five research owners  
**Starting status:** Not started  
**Mission:** Turn the five workstreams into one evidence-backed, feasible solution and a defensible prototype scope.

## Questions to answer
1. Does every problem-statement requirement have an owner and proposed response?
2. Which claims are supported, provisional, contradicted or untested?
3. How does our contribution fit existing systems and validated user needs?
4. Which integrations can be real in the demo, which must be simulated, and which belong later?
5. What architecture, cost and timeline are credible given the team's skills and dependencies?
6. How will we measure success, explain limits and defend tradeoffs?

## Suggested work sequence
1. Maintain the shared requirement matrix, status dashboard, decision log and risk register.
2. Review source quality, scope and conflicting findings; request targeted follow-ups.
3. Run paired reviews and the final teach-back with all members.
4. Compare approaches before selecting an MVP; record reasons, alternatives and evidence.
5. Consolidate a solution brief, demo scenarios, evaluation plan and unresolved external dependencies.

## Required outputs
- [ ] Combined evidence-backed solution brief and architecture proposal.
- [ ] Complete requirement-to-research-to-feature mapping.
- [ ] MVP scope: build now, clearly simulated integration, later capability and explicit exclusions.
- [ ] Risk register, assumptions, cost model and implementation plan.
- [ ] Evaluation plan, end-to-end demo sequence and jury questions with evidence-backed answers.

Write the main brief in [findings.md](findings.md); use additional files only when they improve clarity. Use the [shared templates](../../templates/README.md).

## Collaboration boundary
Kanishkar is the human team lead. AI agents are assistants, not an additional teammate or decision approver. Human review must not be fabricated.

**Handoff:** Receive findings from all five owners, return review feedback, resolve shared decisions and coordinate the final plan.

## Evidence starting points
Use source entries **S01, S09, S10, S11** in the [source guide](../../docs/source-guide.md).
Check current versions, scope and access independently. Record actual evidence in [sources.csv](sources.csv), with IDs such as `KAN-001`.
Research additional primary sources as needed; this list is not exhaustive.

## Quality bar
- Explain the mechanism in your own words.
- Support material claims with an exact source or documented observation.
- Work through a normal case and at least two failure/edge cases.
- Separate confirmed findings from assumptions, proposals and unknowns.
- State the effect on the solution and the next handoff.
- Present a seven-minute teach-back, followed by questions.

**Question you must defend:** Why is this solution viable, distinct and honestly demonstrable with the access we have?

## AI agent starting instruction
```text
I am Kanishkar B, responsible for Team lead: synthesis, feasibility, MVP and evaluation.
Read AGENTS.md, team.json, the shared research standards and this folder's current files.
Help me investigate one unanswered question from this assignment.
Open primary sources, record evidence and uncertainty, and explain the concept to me.
Update my findings, sources and progress only with work actually performed.
Do not invent research, external access, measurements or human review.
```
