# Access, amendments and evidence limitations

AI-authored continuation of the 2026-10-26 research round, completed 2026-10-27 IST. The initial findings draft was retained and corrected transparently. Retrieval dates below are actual continuation dates; they are not backdated to the round's label. Source IDs resolve in [sources.csv](sources.csv).

| Source | What was checked on 2026-10-27 | Evidence status and implication |
|---|---|---|
| PRA-101 AICTE APH route | Direct web fetch of the official URL returned HTTP 403. The prior handoff reported HTTP 404 on October 26. | Official publication endpoint unavailable in this environment. Search-index text is not a substitute for inspecting the current authoritative amendment set. |
| PRA-102 APH institution mirror | Recovered the PVPIT mirror URL and downloaded it with Python. Its 4,155,819 bytes match the pre-existing cached file exactly. Sections 2.8/2.9, 2.25, 6.13, 6.42 and Annexure 6 were reread. | AICTE-authored base handbook on a third-party institution host; not a current consolidated official rule pack. SHA256: `153d54816f2cf11489218e239113544e8d49b73680009688baa7dc4880636051`. Hash equality establishes matching bytes, not publisher authentication. |
| PRA-103/104/105 UGC simultaneous programmes | Official listing and both PDFs reopened; June 5, 2025 modification and operative pp4-5 reread. | Official-host primary evidence. The old no-retrospective-benefit formulation must not override the modified guideline 5. PhD exclusion and council/university conditions remain. |
| PRA-106 international seats | Official UGC PDF downloaded and guidelines 2, 6 and 7 reread; listing gives publication 2022-09-30. | Official-host primary evidence. It is not a blanket technical-course entitlement to 25%. |
| PRA-107 Government Polytechnic Pune | Indexed PDF URL recovered. Direct web and Python requests returned 404, also for the www-host variant. | Initial AI draft reported inspection, but no retained PDF or detailed prior access record was available. Treat as an unconfirmed example in this continuation; no active claim depends on it. No conclusion about actual approval withdrawal follows from a broken URL. |
| PRA-108 GJUST | Official institution listing linked a seven-page AICTE EoA corrigendum. PDF opened/downloaded; initial EoA 2026-03-16, corrigendum 2026-04-29, upload listing 2026-05-01. | AICTE-issued document hosted by its recipient institution, not AICTE portal authentication. pp1-4 show course/year/intake/flags; p6 identifies change in approved intake. It also preserves separate State/affiliation permissions and says AICTE's approved record governs a discrepancy. |
| PRA-109 DTE Maharashtra | Official 15-page packet downloaded. July 2 amendment pp11-12 and 2026-27 brochure pp13-15 checked against older attached wording pp7-8. | Official state evidence in its stated scope. Amendment removes old section 16(2)(d) and expands the same-year restriction to first through fourth year. Cancellation rule section 15(a) gives legal effect to the online request irrespective of later signed-copy receipt; software must not invent an institute-approval delay. |

## Unresolved amendment dependency

The complete current AICTE APH addendum/corrigendum set applicable to the intended 2026-27 pilot has not been established. Secondary discovery references are not enough to activate changed international-seat percentages or carry forward base-edition NRI/lateral/TFW assumptions. No verified current percentage is asserted here. Obtain the authoritative amendment, scope, effective date, affected clauses and pilot EoA/affiliation/seat matrix before enabling the corresponding production checks.

The draft's reference to potential material changes is a discovery caution, not a verified assertion of a specific new national percentage. A course can have a multi-year approval; the necessary condition is that its interval covers the target academic year with all relevant revisions resolved, not necessarily that a new PDF was issued that year.

## Corrections and critique log

| Date | AI check or received critique | Action |
|---|---|---|
| 2026-10-27 | Initial draft named Pune and Hisar as directly inspected examples; Pune retrieval cannot now be reproduced. | Retained access history; used reopened GJUST as the operative approval example. No inference that Pune lacks approval. |
| 2026-10-27 | A general withdrawal workflow could wrongly imply institution approval is always needed. | Added C14 and clarified POL-11: apply the legal effective event, including this Maharashtra online-cancellation rule. |
| 2026-10-27 | Integration researcher: requester linkage is not arbitrary-ID bulk verification; unavailable/missing linkage cannot establish ineligibility. | Added C22 and kept capacity/policy findings independent of identity-linkage state. See [Sudhan](../sudhan/findings.md). |
| 2026-10-27 | Policy critique sent to integration/security researchers. | Concurrent enrolment is context-sensitive; cross-tenant evidence must be limited; category status is not entitlement; digest is not issuer authentication. See [Sudhir](../sudhir/findings.md). |
| 2026-10-27 | Security researcher: even an opaque collision-only ticket reveals a match/existence bit. | Revised the proposal to uniform batch receipts, internal reviewer-only collision cases and clarification limited to an institution's own facts. No peer-match disclosure. |

These are AI checks and exchanged AI critiques. No human review, regulator confirmation, interviews, live institutional-data validation or pilot occurred.
