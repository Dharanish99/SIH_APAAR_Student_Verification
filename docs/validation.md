# Validation record - 27 October 2026

This is a research and artifact validation record. It does not certify an implemented product, legal compliance, government access or field usefulness.

## Executed evidence checks

| Check | Observed outcome | Boundary |
|---|---|---|
| Original Dharanish model reproduction | Eight comparisons matched; twelve sequential model checks reproduced; 1,000 fictional rows and separate 300-observation reference | Not a database, concurrent-worker, provider or field test |
| Source preservation | 35 preserved source/snapshot and provenance files have recorded SHA-256 hashes; original upload bytes were compared during import | Hashes establish file integrity, not truth or authorship |
| Policy reasoning package | 14 proposed rules and 22 numbered fictional cases, with source/applicability limits | Expected outcomes, not an executed rule engine |
| Integration package | 15 integration source records and 12 explicit future contract scenarios; provider PDF hashes checked | No API call or credentials; scenarios unexecuted |
| Security package | 22 source records, 13 abuse cases and substantive agent critiques | Proposed controls, no penetration test or human approval |
| Documentation | CSV widths, source-ID references, JSON parsing, local link targets and cross-file heading anchors checked | Historical source snapshots and example IDs are not treated as current claims; remote URLs are checked during research, not claimed permanently available |
| Report PDF | Ten pages rendered; every page visually inspected; final contents-page change separately re-rendered and inspected | PDF is not tagged for accessibility; Markdown remains available |
| Mind map | 12 branches, 82 leaves; local SVG/PNG inspected; 95 editable canvas nodes and 94 connectors | Initial overlapping layout corrected; final node-bounds check found zero overlapping node pairs |

Machine-readable packaging results are in [research-checks.json](../output/validation/research-checks.json). Original experiment evidence is in [reproduction-results.json](../research/dharanish/experiments/reproduction-results.json). The [preservation manifest](../research/provenance/preserved-files.json) records stored-source hashes.

Commands from repository root:

```sh
node research/dharanish/experiments/reproduce.cjs
python tools/validate_research.py
git -c core.whitespace=cr-at-eol diff --check -- . ":(exclude)research/provenance/notion/**" ":(exclude)**/original-*/**" ":(exclude)**/notion-original/**"
```

Whitespace checks cover authored changes; archived source bytes retain their original formatting.

The reproduction was already executed during research; its measured metric-computation time is not an ingestion benchmark. Rendering uses [artifact tools](../tools/README.md). External PDFs used for research are linked; cached full publications and temporary files are excluded from Git.

## Remaining gates

Official SIH wording; complete current applicable AICTE amendments; pilot-specific approvals and reporting contracts; provider sponsorship/scopes/access; current operator-specific legal, retention and guardian decisions; human policy/design review; actual database/security/load testing; and a permitted comparative field pilot.

The proposal is research-grounded, **not real-world validated**. Proposed 90% task success and 20% staff-time reduction are progression targets, not measurements. Passing source checks does not turn a policy hypothesis or user-benefit claim into a proven product result.

## Publication

The research was initially published through draft PR #2. On 28 October the owner explicitly authorised consolidating the preserved research history and executable prototype on main. See the [current application testing record](TESTING.md); the earlier research checks below do not certify application behavior.

Final remote update: newer Pranav/Sudhir contributions were imported and reconciled; all original rules/cases and both revised ledgers were checked. The research branch includes origin/main history through0d12323. Source snapshots remain byte-identical under archive-specific Git attributes.
