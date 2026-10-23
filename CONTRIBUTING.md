# Contributing research

## Find your assignment
Use the [team table](README.md) or [team.json](team.json). Each folder contains:
- `README.md`: role, questions, tasks, outputs and handoffs.
- `findings.md`: your evidence-backed research brief.
- `sources.csv`: claim-level evidence register.
- `progress.md`: append-only updates and current status.

The [research standards](docs/research-standards.md) define evidence and completion expectations.

## Browser workflow (no terminal needed)
1. Open your member folder on GitHub and choose a file.
2. Use the pencil/Edit control, update the content, and preview Markdown.
3. Choose a new branch for the change, using `research/<member>/<short-topic>`.
4. Open a pull request to the repository's default branch, normally `main`.
5. Fill the PR template, naming the research owner and requested human reviewer.
6. Address review comments. Kanishkar coordinates merging and shared decisions.

GitHub may offer a fork if your account lacks write access. Do not infer collaborator permissions from a role assignment; contact the repository owner through the team's usual channel.

## Local Git workflow
After the repository is initialised:

```sh
git clone https://github.com/Dharanish99/SIH_APAAR_Student_Verification.git
cd SIH_APAAR_Student_Verification
git switch main
git pull --ff-only
git switch -c research/gopika/workflow-observations
# Edit the relevant files; substitute your own member/topic.
git add research/gopika
git diff --cached
git commit -m "docs(gopika): record admission workflow observations"
git push -u origin research/gopika/workflow-observations
```

Open a PR on GitHub. Do not force-push main. Review the staged diff so unrelated or private files are not included.

## Evidence and naming
Use source IDs prefixed by the owner: GOP, SUD, PRA, DHA, SUH or KAN, followed by a number, e.g. `DHA-001`.
Use ISO dates `YYYY-MM-DD`; include timezone for timed measurements.
Prefer short lowercase hyphenated filenames and relative links.
For experiments create `research/<member>/experiments/<topic>/README.md` and list exact commands/dependencies.
Store small synthetic fixtures only, labelled as synthetic. Link to external public documentation instead of copying entire publications.

## Review and handoffs
Gopika and Pranav cross-review; Sudhan and Sudhir cross-review; Dharanish and Kanishkar review technical feasibility.
Kanishkar reviews shared decisions and consolidates the solution. Reviewers may differ when expertise requires it.
State feedback and unresolved disagreements; never invent review approval.

## Before submitting
- [ ] Conclusions are in my own words with claim-level sources.
- [ ] Applicability, dates, assumptions and unknowns are explicit.
- [ ] Simulations and synthetic data are labelled.
- [ ] Findings and progress are updated.
- [ ] Links work locally; CSV columns and JSON remain valid.
- [ ] No personal records, secrets or confidential exports are included.
- [ ] My handoff and requested reviewer are stated.

Suggested commit prefixes: `docs(member): ...`, `research(member): ...`, `docs(shared): ...`.
Templates and review conventions are documentation, not proof that branch-protection settings are enabled.
