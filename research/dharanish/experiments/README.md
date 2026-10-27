# Reproduce the original research
All records are fictional with SYN- identifiers. [Original Notion experiment](https://app.notion.com/p/403aaff5423381b8852bdf90e473ff83), retrieved 2026-10-26. Original attachments, including source CSV, remain in notion-original/.

The .txt JavaScript was inspected before execution. reproduce.cjs runs it in a restricted Node VM and compares deterministic metrics, checks and CSVs against originals.
```text
node research/dharanish/experiments/reproduce.cjs
```
Expected: eight comparisons true and twelve model checks PASS. Mismatch returns nonzero. Timing can vary. Output: reproduction-results.json. This is research reproduction, not a backend, concurrency test or security certification. See [findings](../findings.md).
