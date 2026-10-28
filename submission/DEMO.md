# Three-minute presentation

Start at http://127.0.0.1:4871 as Institution operator, Aster Institute. Reset the fictional data before presenting. The built-in walkthrough changes personas but does not secretly perform the tasks for you.

| Time | Click / action | Explain |
|---|---|---|
| 0:00–0:25 | Overview → Review a student record | “Aster reports seven CSE records for six fictional seats. Meera's identity fixture is linked, but that does not prove her programme is right.” |
| 0:25–0:50 | Close evidence; select Student · Meera → Request programme correction | “Students can inspect and challenge institution claims without depending on the disputed APAAR. The request creates a case, not a silent edit.” |
| 0:50–1:20 | Select Institution operator → Review a student record → Accept source correction | “The institution owns its source amendment. A reason and both revisions remain. CSE returns to six; missing linkage elsewhere stays pending.” |
| 1:20–1:50 | Select Institution approver → Submission snapshots → acknowledge findings → Approve local snapshot | “A separate role freezes exact records, rule scope and exceptions. This local approval is different from a government acknowledgement.” |
| 1:50–2:20 | Select Student · Meera → Create limited permission → Verifier demo | “Meera chooses name and programme for a fifteen-minute internship check. APAAR and student ID are not offered to this verifier.” |
| 2:20–2:45 | Check current permission | “The recipient, current grant, source revision, snapshot and signature are checked independently. The signature preserves integrity; it does not establish an admission's legality.” |
| 2:45–3:00 | Select Student → Withdraw permission → select verifier → Check current permission | “Future access returns no student fields. The design makes corrections and permission changes matter after the initial upload.” |

If you have one extra minute: Operator → Import workspace → Use demo source → Preview → Commit → Replay. Show one unchanged record, one revision and one new record; then show that replay creates no duplicate effects. An import supersedes prior snapshots, as demonstrated by approval history.

Use the institution dropdown in the operator sidebar to show Riverbend's three separate fictional records. The regulator persona shows aggregate coverage, not student details. Our approach explains what is working, what is simulated, and what a real pilot needs.

## Honest submission statement

“We built and locally tested the correction/reporting/disclosure loop using a real SQLite API. All people, approvals, provider responses and issuer keys in this demonstration are synthetic. Government integration, current policy approval, institutional authentication and real-world usefulness still require an authorised pilot.”

Do not claim live APAAR verification, official AICTE approval, national fraud detection, measured staff-time savings or legal compliance.

## Backend credibility check (optional, 45 seconds)

Operator → Reports & audit → Run integrity check. Show tenant-scoped counts and the checked event count. Open Submission snapshots and download the minimal CSV; it omits APAAR and marks approval status. In the verifier persona, select Meridian Careers to show that another recipient sees no Northstar permission.

If an import changes the source after approval, the old snapshot remains available as superseded historical evidence; a fresh approval is required for new sharing.
