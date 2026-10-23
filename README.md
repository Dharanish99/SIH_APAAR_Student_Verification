# SIH APAAR Student Verification
### Research workspace · SIH26263 · AICTE

A shared research workspace for an **APAAR ID-based Student Data Management and Verification Platform for AICTE-approved institutions**.

**Current phase:** research planning. The folders contain assignments and templates; no completed research, production service, verified government integration or accepted architecture is claimed.

[Start contributing](CONTRIBUTING.md) · [Research plan](docs/research-plan.md) · [Team status](docs/status.md) · [AI agent instructions](AGENTS.md) · [Source guide](docs/source-guide.md)

## The problem we are investigating

How can institutions submit trustworthy student-level admission data, connect records to academic identity, identify genuine inconsistencies, and enable authorised verification with appropriate privacy?

The supplied statement covers uploads and updates, intake and student categories, automated validation, dashboards, authorised verification, verifiable records, interoperability, security/consent/audit history, reports and certificate display of APAAR plus student ID.

Read the [problem brief and scope](docs/problem-brief.md). The supplied third-party statement is a starting reference; verify the official statement and event dates before submission. This is a student project, not an official AICTE/APAAR service.

## Team and research ownership

| Member | Responsibility | Assignment and updates |
|---|---|---|
| Gopika | Institutional workflows, user needs and existing solutions | [Open folder](research/gopika/README.md) |
| Sudhan | APAAR, ABC, DigiLocker/NAD and integration feasibility | [Open folder](research/sudhan/README.md) |
| Pranav | AICTE admission rules and compliance logic | [Open folder](research/pranav/README.md) |
| Dharanish R P | Data architecture, validation and anomaly detection | [Open folder](research/dharanish/README.md) |
| Sudhir | Privacy, security, consent and credential verification | [Open folder](research/sudhir/README.md) |
| Kanishkar B **(Leader)** | Team lead: synthesis, feasibility, MVP and evaluation | [Open folder](research/kanishkar/README.md) |

The named roles were assigned by the team on **23 October 2026**. They do not imply GitHub account permissions. GitHub usernames for review routing have not been supplied; no CODEOWNERS identities are guessed.

## Start here in 10 minutes

1. Read [the problem brief](docs/problem-brief.md) and [research standards](docs/research-standards.md).
2. Open your folder above and read its assignment.
3. Add evidence to your `sources.csv`, write your own explanations in `findings.md`, and update `progress.md`.
4. Use [templates](templates/README.md) for interviews, experiments and cross-member review.
5. Open a focused pull request following [CONTRIBUTING.md](CONTRIBUTING.md). Kanishkar coordinates review.

**For an AI agent:** read [AGENTS.md](AGENTS.md), [team.json](team.json), the member's assignment and current findings before editing. Begin with the requested research task; do not mark placeholders as results.

## Where information belongs

| Location | Purpose |
|---|---|
| [research/](research/README.md) | Six member workspaces; detailed assignments, findings, evidence and progress |
| [docs/](docs/README.md) | Shared scope, plan, standards, requirements, decisions, risks and status |
| [templates/](templates/README.md) | Reusable interview, experiment and review forms |
| [team.json](team.json) | Machine-readable member/role/path mapping |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Browser and Git contribution instructions |
| [AGENTS.md](AGENTS.md) | Repository-wide instructions for AI assistants |
| [.github/](.github/README.md) | Research issue, blocker and pull-request templates |

## What a successful research phase produces

- Evidence of actual user problems and a fair comparison with existing systems.
- Documented integration availability and clearly labelled simulation boundaries.
- Versioned admission rules with worked valid, invalid and ambiguous cases.
- A feasible data design and reproducible synthetic experiments.
- Access, consent and verification design with realistic threat analysis.
- A lead-reviewed solution brief, MVP, evaluation plan and unresolved dependency list.

See the [requirements matrix](docs/requirements.md) and [research plan](docs/research-plan.md).

## Working principles

- Use AI to accelerate learning; open sources, check applicability and explain conclusions yourself.
- Separate **verified facts, observations, assumptions and proposals**.
- Identifier format, identity verification, enrolment validity and credential authenticity are different checks.
- Repeated enrolment is a review signal, not automatically fraud.
- No real student IDs, admission exports, private interview details, credentials or API secrets in this public repository.
- Use synthetic data and label every simulated government response.
- Choose technology after evidence and constraints are understood.

## Project status and governance

No application has been implemented yet, so there are no application install/run commands.
The initial setup does not configure branch protection, invite collaborators or grant a software licence.
Kanishkar coordinates research decisions; repository access is managed by its owner.
Future application code should be added only when a concrete implementation task is assigned.

[Repository](https://github.com/Dharanish99/SIH_APAAR_Student_Verification) · [Supplied problem statement](https://zaidsayyed.in/tools/sih-problem-statements/sih26263)
