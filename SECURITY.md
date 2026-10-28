# Security scope and reporting

SetuTrace is a loopback-only SIH submission prototype with deliberately selectable demo identities. It is not ready to host real student data or expose publicly.

Implemented controls include API role/tenant scoping, expiring token-hash sessions, mutation tokens, local origin/host restrictions, request and upload limits, database constraints, immutable evidence guards, transactional state changes and live verification of minimal signed assertions. See [API contracts](docs/API.md) and [tests](docs/TESTING.md).

- Persona selection simulates authentication; anyone using the local demo can choose a role.
- HTTP cookies are intentionally local; a real service needs HTTPS, secure cookies and institutional identity federation.
- SQLite and the synthetic issuer key share the local trust boundary. A privileged administrator can modify storage, rewrite audit history or replace a key. No external audit anchor or managed key custody is implemented.
- Revocation/expiry denies later service retrieval; it does not erase copies already obtained.
- Rate limits are in-process. This is one local server, not a distributed security design.
- Demo reset intentionally removes fictional evidence and restores fixtures; it is not a production retention/deletion workflow.
- No penetration test, DPDP certification, production security or legal compliance is claimed.

Do not include vulnerabilities containing credentials or real student information in public issues. Use an existing private contact route to the repository owner; no unverified security email is provided here. Never commit reproduction data containing real identifiers.

Before a pilot: approve purposes/retention and policy scope, integrate real authentication and recipient onboarding, move to controlled PostgreSQL storage and key custody, test backup/restore and concurrent workers, and obtain independent security/privacy review.
