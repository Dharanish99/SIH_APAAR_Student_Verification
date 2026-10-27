# Decision log

Kanishkar coordinates shared decisions. Preserve alternatives and the reason for changes.

## D001 — Research ownership
- Status: Accepted — user-assigned.
- Date: 2026-10-23.
- Authority: Team instruction in project setup.
- Decision: Gopika owns role 1; Sudhan role 2; Pranav role 3; Dharanish R P role 4; Sudhir role 5; Kanishkar B is team lead and owns role 6.
- Consequence: [team.json](../team.json) and member folders reflect this mapping.
- Limitation: This is not a GitHub permissions assignment or evidence of research review.

## Proposed design decisions - 27 October 2026

All entries below are AI recommendations for human review. No human architecture or stack acceptance is recorded.

| ID | Proposal and reason | Tradeoff / revisit trigger |
|---|---|---|
| D002 | SetuTrace evidence/correction layer beside ERP/NAD; four alternatives compared in the report | Revert to improved checklist if total effort or adoption does not improve |
| D003 | Useful local reporting loop before live provider integration; token-account evidence stays separate | Obtain sponsor/scopes and test before enabling; do not promise arbitrary-ID checking |
| D004 | Deterministic rules first; complete scoped rule pack or UNKNOWN | Statistics added ten useful and ten false alerts in fictional data; revisit only with representative evaluation |
| D005 | Internal authorised matching with uniform institution receipts | Side-channel and inference tests required; no institution-visible match bit |
| D006 | Revisioned claims, expected-version corrections and approver snapshot | More storage/governance; benchmark and validate real DB races before use |
| D007 | Online recipient-bound assertion; trusted issuer and current status | Cannot revoke already downloaded copies; interoperability and offline status later |
| D008 | Modular FastAPI/PostgreSQL application and leased worker | Operational simplicity is a proposal; scale components only after measured limits |
| D009 | Human authority governs current policy and legally effective events | Reviewer acknowledgement must not delay an already effective scoped cancellation |

Evidence and actual agent feedback: [report](solution-report.md), [design critique](design-critique.md), [assignment audit](research-audit.md). Kanishkar coordinates genuine team acceptance. No provider, regulator or institution has endorsed these proposals.
