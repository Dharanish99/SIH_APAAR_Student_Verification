# SIH APAAR Student Verification

Research and solution design for the supplied SIH26263 brief. Consolidated on **27 October 2026**.

**Phase:** evidence-backed proposal, ready for human review. Research includes GitHub contributions, ten relevant Notion snapshots, Gopika's uploads, specialist agent research and a reproduced synthetic experiment. No application, live government integration or field pilot is claimed.

## Read the result

- [Solution report](docs/solution-report.md) / [PDF](output/pdf/solution-report.pdf): idea, alternatives, user journeys, validated constraints, complete proposed stack, MVP and evaluation.
- [Research audit](docs/research-audit.md): every person's allotment, what was found, what agents completed and remaining external work.
- [Requirement coverage](docs/requirements.md): all ten supplied requirements and their acceptance gates.
- [Mind map](docs/mind-map.md): complete map, editable source and canvas.
- [Validation record](docs/validation.md): what was actually checked and what remains untested.

## Research base

| Human owner | Research and provenance |
|---|---|
| Gopika | [Workflows, field mapping and opportunities](research/gopika/findings.md); [original uploads](research/gopika/original-upload/) |
| Sudhan | [Integration review and corrected assumptions](research/sudhan/integration-review.md); [original contribution](research/sudhan/original-2026-10-25/) |
| Pranav | [Admission policy, rule catalogue and worked cases](research/pranav/findings.md) |
| Dharanish R P | [Architecture, imports, feasibility and reproduced experiment](research/dharanish/findings.md) |
| Sudhir | [Security, privacy, legal status and trust](research/sudhir/findings.md) |
| Kanishkar B, human team lead | [Consolidation and feasibility](research/kanishkar/findings.md) |

Each workstream has a source ledger and progress log. [Provenance](research/provenance/README.md) preserves original Notion context and attachment hashes. AI supplements are identified; no human reviewer or interview is invented. Sudhan and Sudhir are distinct contributors.

## Evidence boundary

The strongest result is a design constrained by current primary documentation, with an independently reproduced **1,000-row fictional experiment**. User benefit, production security, scale, current institution-specific policy packs and live provider access still require testing. The [official SIH cross-check](docs/official-problem-verification.md) remains unresolved because the portal returned 403; the supplied statement is the explicit scope baseline.

## Reproduce the research checks

```sh
node research/dharanish/experiments/reproduce.cjs
python tools/validate_research.py
```

The first checks the preserved sequential synthetic model; the second checks documentation structure and source preservation. Neither runs an application or proves compliance.

[AGENTS.md](AGENTS.md) defines this research workflow and specialist roles. [Team status](docs/status.md), [decisions](docs/decisions.md), [risks](docs/risks.md), [research standards](docs/research-standards.md) and [contributing](CONTRIBUTING.md) retain human review governance. [team.json](team.json) preserves the original ownership mapping.

This is a student research project, not an official AICTE, APAAR or DigiLocker service. Original contributions and historical source snapshots remain distinguishable from the current synthesis. No real student data or government credentials were used.
