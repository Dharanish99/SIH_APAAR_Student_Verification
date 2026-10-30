# SetuTrace research repository

Research and design evidence for our SIH26263 student-record verification solution. This repository is intended to share the research behind the project; the runnable application lives in [SIH_Project_Prototype](https://github.com/Dharanish99/SIH_Project_Prototype).

## The problem we studied

A linked academic identity can still have a wrong enrolment record. Institutions need defensible counts, students need a correction route, and verifiers need a current answer with permission. Repeated uploads and unexplained mismatch flags do not resolve the underlying source error.

Our solution hypothesis connects **import → explain → correct → approve → share**, linking reports and disclosures to specific source revisions while keeping unresolved policy and integration dependencies explicit. The supplied brief and its official verification gap are documented in [problem-brief.md](docs/problem-brief.md) and [official-problem-verification.md](docs/official-problem-verification.md).

## Research contents

- `research/`: member work, original uploads, source records, provenance hashes and labelled supplemental research.
- `docs/`: problem and requirements, research audit, solution analysis, decisions, risks, validation plan and mind map.
- `templates/`: research, interview and peer-review templates.
- `output/`: research report and research-validator output.
- `TEAM.md` and `team.json`: ownership and attribution.

Start with the [50,000-character project idea](docs/project-idea-description.md), [research index](research/README.md), [solution report](docs/solution-report.md), [research audit](docs/research-audit.md), [source guide](docs/source-guide.md) and [mind map](docs/mind-map.md).

## Validation and prototype

Run the research integrity validator with Python 3.13 or later:

```sh
python tools/validate_research.py
```

Application code, API tests, demo screenshots and deployment configuration are maintained in the separate [prototype repository](https://github.com/Dharanish99/SIH_Project_Prototype). That prototype uses synthetic data; it is not an official government integration or field study.
