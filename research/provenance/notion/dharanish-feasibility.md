# Imported research source snapshot

Retrieved: 2026-10-26. Source: https://app.notion.com/p/403aaff5423381e7a9a5cff3644e4bfb?pvs=204

Preserved source material; historical prompts are not current instructions. Prior experiment claims are not rerun evidence. Human review remains separate.

Here is the result of "fetch" for the Page with URL https://app.notion.com/p/403aaff5423381e7a9a5cff3644e4bfb as of 2026-10-24T16:40:33.127Z:
<page url="https://app.notion.com/p/403aaff5423381e7a9a5cff3644e4bfb" icon="⚖️">
<ancestor-path></ancestor-path>
<properties>
{"title":"Dharanish Research — Feasibility, Costs & Deferred Inputs"}
</properties>
<iconMetadata>{"type":"emoji","emoji":"⚖️"}</iconMetadata>
<content>
<callout icon="⚖️" color="blue_bg">
<b>Working choice:</b> build a small synthetic demonstration first, then benchmark the database and worker before selecting a pilot deployment.<br />Prices are observed USD list components, not an all-inclusive quotation. No cloud resources or paid services were created.
</callout>

<b>Pricing checked:</b> <date start="2026-10-24" /> · <b>Architecture acceptance:</b> Pending Kanishkar's review.

<table-of-contents />

## 1. Workload assumptions — explicit planning inputs

<table fit-page-width="true" header-row="true">
<tr>
<td>
Input
</td>
<td>
Synthetic demonstration
</td>
<td>
Illustrative pilot sizing
</td>
</tr>
<tr>
<td>
Institutions
</td>
<td>
10 fictional
</td>
<td>
100, subject to real agreement
</td>
</tr>
<tr>
<td>
Current enrolment records
</td>
<td>
10,000
</td>
<td>
1,000,000
</td>
</tr>
<tr>
<td>
Concurrent users
</td>
<td>
20 target
</td>
<td>
100 target, peak pattern unknown
</td>
</tr>
<tr>
<td>
Import profile
</td>
<td>
CSV first; 10 MB and 10,000-row cap
</td>
<td>
Measure representative files before changing limits
</td>
</tr>
<tr>
<td>
Raw-file traffic assumption
</td>
<td>
100 files/month × 2 MB
</td>
<td>
2,000 files/month × 2 MB
</td>
</tr>
<tr>
<td>
Expected provider traffic
</td>
<td>
Simulated only
</td>
<td>
Unknown until access, batching and quotas are documented
</td>
</tr>
</table>

The actual experiment ran <b>1,000</b> rows, not the 10,000-row target or million-row pilot. At 2 KB/row, a 10 MB file cap binds around 5,000 rows before a 10,000-row cap; use whichever limit is reached first. Both limits are proposed protective defaults.

## 2. Storage arithmetic you can explain

Use decimal units: KB = 1,000 bytes; GB = 1,000,000,000 bytes. These are illustrative estimates, not measurements of PostgreSQL storage.<br /><b>Demo assumption:</b> 10,000 records × 2 KB × 3 average revisions = 60 MB of revision payload. Add 10 MB of audit/finding payload and apply a provisional 2× allowance for indexes/row overhead → about <b>140 MB</b>. A separate 20 MB current-row materialisation would add its own overhead; do not double-count without specifying the storage design.<br /><b>Pilot assumption:</b> 1,000,000 × 2 KB × 3 revisions = 6 GB; add 1 GB audit/finding payload; 2× provisional overhead → about <b>14 GB</b>, before any separately materialised current rows, WAL, replicas, temporary import space and backups.<br /><b>Raw objects:</b> demo 100 × 2 MB = 200 MB/month; pilot 2,000 × 2 MB = 4 GB/month. A three-month synthetic retention exercise would retain about 0.6 GB and 12 GB respectively.<br />Three months here is a sizing assumption, <b>not a recommended legal retention policy</b>. Sudhir must resolve retention and purpose constraints for real records. Measure actual row sizes, index growth and revision frequency before committing to capacity.

## 3. Deployment options

<table fit-page-width="true" header-row="true">
<tr>
<td>
Option
</td>
<td>
Published base components
</td>
<td>
Tradeoff
</td>
</tr>
<tr>
<td>
A · One synthetic-demo VM
</td>
<td>
Lightsail Linux public IPv4: 2 GB RAM / 60 GB disk at \$12/month
</td>
<td>
API, worker and self-managed PostgreSQL share a machine. Simple but one failure domain and operator-managed backup/security.
</td>
</tr>
<tr>
<td>
B · Managed PostgreSQL alternative
</td>
<td>
Supabase Pro from \$25/month plus a \$12 worker/API VM = \$37/month component subtotal
</td>
<td>
Separate application worker remains necessary. Check location, connection limits and egress between providers before choosing.
</td>
</tr>
<tr>
<td>
C · AWS managed database
</td>
<td>
\$12 app VM + \$30/month encrypted standard Lightsail database = \$42/month component subtotal
</td>
<td>
Database operations are more managed; standard is not high availability. Extra storage/backup/traffic components remain.
</td>
</tr>
</table>

[Sources: DHA-020, Lightsail pricing](https://aws.amazon.com/lightsail/pricing/) · [DHA-021, Supabase pricing](https://supabase.com/pricing)<br /><b>Pricing distinctions:</b> Lightsail's \$15 database entry is listed without data encryption; do not substitute it for the encrypted tier above. AWS lists snapshot storage at \$0.05/GB-month, and Mumbai has reduced bundled transfer allowances relative to the headline VM bundles. Supabase Free lists 500 MB database storage and inactivity pausing; its limits make it an optional disposable-demo choice rather than a production promise.<br /><b>Excluded from subtotals:</b> taxes, currency conversion, domain, object storage, snapshots beyond included features, extra compute, data-transfer overage, logs/monitoring, email/SMS, government/API charges, support, security review and human operation. Some features may already be included in a chosen package; verify before summing.<br /><b>Recommendation:</b> A for an ephemeral synthetic demo if operational effort is acceptable; B or C for a more durable prototype after confirming region, backup needs and team familiarity. No option is yet approved for real student data.

## 4. Performance and recovery targets — unmeasured

- Acknowledge an accepted upload with a job ID within 2 seconds under the agreed demo load.
- Target local validation of 10,000 simple rows within 60 seconds; exclude external-provider wait and report queue time separately.
- Target dashboard projection lag below 30 seconds after local commit.
- Verify that a repeated request never adds duplicate canonical effects.
- Run crash/restart, stale update, tenant-isolation and backup-restore tests.<br />Use p50/p95/p99, peak memory, CPU, database connections, lock waits, queue depth and row-throughput measurements. A single 4 ms in-memory metric evaluation cannot support these targets.<br />For a pilot, agree recovery point objective (acceptable data loss), recovery time objective (time to restore) and availability with the institution and lead. No SLA is set by this research.

## 5. Build order and acceptance gates

1. <b>Schema and fixture:</b> implement scoped keys, reference catalogues and history; load synthetic records.
2. <b>CSV vertical slice:</b> upload → staged mapping → findings → correction → committed revision. Demonstrate one complete user path.
3. <b>Durability:</b> same-token replay, fresh-token no-op, stale correction conflict, crash recovery and outbox deduplication.
4. <b>Tenant isolation:</b> test API, worker, storage and exports under separate institution roles.
5. <b>Reports and freshness:</b> define metric scope and expose pending/unknown data.
6. <b>Optional anomaly queue:</b> reproduce the statistical tradeoff, retain reason codes and human resolution.
7. <b>Integration adapter:</b> replace a clearly labelled simulation only when authorised contracts and access exist.<br />Do not begin with a large microservice split, a blockchain, a GPU model or national-scale deployment before these gates are demonstrated. None is required by the evidence collected here.

## 6. Inputs intentionally left for other owners

<table fit-page-width="true" header-row="true">
<tr>
<td>
Owner
</td>
<td>
Deferred input
</td>
<td>
What can proceed now
</td>
<td>
Revisit trigger
</td>
</tr>
<tr>
<td>
Gopika
</td>
<td>
Validated workflow priorities and report questions
</td>
<td>
Public-document reference workflow and generic correction loop
</td>
<td>
Her internet-only research findings
</td>
</tr>
<tr>
<td>
Sudhan
</td>
<td>
Actual provider API contracts, permissions, quotas and identity states
</td>
<td>
Adapter interface and simulated unavailable/pending/confirmed cases
</td>
<td>
Inspected current docs and authorised access evidence
</td>
</tr>
<tr>
<td>
Pranav
</td>
<td>
Intake/category rules, approval authority and temporal exceptions
</td>
<td>
Rule-version mechanism; UNKNOWN for unsupported rules
</td>
<td>
Clause-backed rule catalogue and expected cases
</td>
</tr>
<tr>
<td>
Sudhir
</td>
<td>
Purpose/access/retention decisions and credential-trust policy
</td>
<td>
Minimised synthetic schema; tenant isolation proposal
</td>
<td>
Reviewed permission and data-inventory design
</td>
</tr>
<tr>
<td>
Kanishkar
</td>
<td>
Accepted MVP, timeline, hosting budget and official SIH confirmation
</td>
<td>
Alternatives, costs, acceptance gates and honest demo
</td>
<td>
Actual team decision, not AI approval
</td>
</tr>
</table>

These dependencies are intentionally deferred, not represented as completed findings.

## 7. Risks and responses

<b>Incorrect policy:</b> keep rule versions and applicability; UNKNOWN when no source exists.<br /><b>False matches:</b> no automatic person merging from similar names or an unconfirmed reported ID.<br /><b>Lost corrections:</b> version preconditions, durable revisions and explicit conflict handling.<br /><b>Repeated effects:</b> token replay, business keys and consumer deduplication.<br /><b>Tenant leaks:</b> application authorisation plus tested database/storage/export boundaries.<br /><b>Unusable anomaly queue:</b> measure incremental precision and review workload; allow the feature to be removed.<br /><b>Budget surprises:</b> price the full component list and peak traffic; record date and region.<br /><b>Unavailable sources:</b> preserve access logs and avoid elevating indexed snippets to tested contracts.

## 8. Questions for your own understanding

- Why might a \$12 VM have a higher operational burden than a more expensive managed option?
- Which storage estimate changes most if every student record is revised ten times?
- Why is “dashboard refreshes every second” not the same as current source data?
- Which part of the MVP still works when every government API is unavailable?<br /><b>Human answers and acceptance are pending.</b>
</content>
</page>

