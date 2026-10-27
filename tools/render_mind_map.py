"""Generate canonical Mermaid plus a standalone SVG/PNG research mind map.

Requires Pillow. This is a research artifact, not a product prototype.
"""
from pathlib import Path
from html import escape
import textwrap
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
BRANCHES = [
('01  People and jobs', [
 'Student: inspect own claims, challenge errors, follow an appeal',
 'Operator: reuse ERP exports and resolve actionable exceptions',
 'Approver: review differences and freeze a reporting snapshot',
 'Regulator: scoped totals and internal authorised case review',
 'Verifier: narrow current assertion with a recipient-bound grant',
 'Assisted access: no dependency on the disputed APAAR to seek help']),
('02  Useful product hypothesis', [
 'SetuTrace sits beside ERP and NAD; local operations remain there',
 'Evidence card: institution claim, provider evidence, rule and resolution',
 'Trace source revision through findings, snapshots and corrections',
 'Explain changed totals and identify the responsible source owner',
 'Compare with ERP replacement, API-first registry and a checklist',
 'Choose the simpler checklist if the product adds no net value']),
('03  Reporting and correction loop', [
 'ERP export -> staged CSV -> versioned mapping -> change preview',
 'Commit bounded chunks with revisions, audit events and outbox',
 'Explain findings; approver freezes explicit accepted row versions',
 'Local acceptance, export readiness and official receipt are distinct',
 'Challenge -> evidence -> source correction or refusal -> appeal',
 'Re-evaluate affected findings and supersede old assertions',
 'Record legal effective time separately from acknowledgement time']),
('04  Policy and inclusion', [
 'Scope rules by institution, campus, programme, year and entry route',
 'Approval versions and effective dates determine counting scope',
 'Missing current rule pack returns UNKNOWN; no universal quotas',
 'Nationality, candidature and seat entitlement remain distinct',
 'Concurrent programmes can be legitimate; review timing and rules',
 'Missing or foreign APAAR keeps capture open and linkage pending',
 '14 proposed rules and 22 fictional cases; no automatic sanction']),
('05  Provider and system boundaries', [
 'Documented APAAR route is token-account linked, not bulk ID lookup',
 'Sponsor, use case, scopes and live access remain external gates',
 'No public sandbox promise or unapproved recurring polling',
 'Not-linked, denied, mismatch, outage and stale evidence differ',
 'Minimise retained response; credit data is not all enrolments',
 'CSV first; ERP, AICTE and award adapters require real contracts',
 'Mock provider and issuer labels remain explicit in demonstrations']),
('06  Privacy and trust', [
 'Separate reporting authority, provider permission and disclosure grant',
 'Tenant/resource checks on API, jobs, storage, downloads and exports',
 'Uniform institution receipts; matches internal to authorised regulator',
 'No raw-ID public search, match bit or authority from a QR alone',
 'Bind verifier to recipient, purpose, fields, revision and expiry',
 'Recheck grants and current status; revoke future access',
 'DPDP stages, SPDI applicability, retention and guardian review gated']),
('07  Architecture and data', [
 'Institution-local key and internal UUID; no automatic person merge',
 'Identity claim, enrolment, approval and credential are separate',
 'Immutable revisions, source evidence and effective/recorded times',
 'Idempotency token plus content and mapping fingerprint',
 'Expected-version correction prevents silent stale overwrites',
 'PostgreSQL constraints plus atomic audit/outbox; leased worker',
 'Provider calls outside transactions; visible partial/stale states']),
('08  Core implementation stack', [
 'React + TypeScript + Vite; accessible responsive web interface',
 'Python + FastAPI + Pydantic + generated OpenAPI contracts',
 'PostgreSQL 18 + SQLAlchemy + Alembic; separate Python worker',
 'CSV first; controlled JSON/CSV/PDF; read-only XLSX later',
 'Institution OIDC; Keycloak synthetic option; secure server session',
 'Private S3-compatible storage; managed signing keys and secrets',
 'Pin supported dependencies at implementation; no app built yet']),
('09  Operations and testing stack', [
 'Docker Compose development; GitHub Actions and dependency scans',
 'Ubuntu LTS + Caddy; managed DB, private storage and tested backups',
 'OpenTelemetry, Prometheus/Grafana and redacted structured logs',
 'pytest + Hypothesis; real PostgreSQL/Testcontainers race tests',
 'Playwright + axe-core; Locust for future measured workloads',
 'Test tenant isolation, replay, revoke/export races and restoration',
 'No Redis, Kafka, blockchain, LLM adjudication or Kubernetes needed']),
('10  Requirement coverage and MVP', [
 'R01-R03: scoped imports, required dimensions and reasoned checks',
 'R04-R06: dashboards, authorised assertion and issuer/status trust',
 'R07-R09: adapter contracts, permissions/audit and defined reports',
 'R10: synthetic issuer-controlled APAAR plus local-ID template',
 'First build: two fictional tenants and one narrow policy pack',
 'Live linking, real rules, real certificates and matching are gated',
 '10k records / 20 users is a future target; only 1k model executed']),
('11  Evidence and provenance', [
 'All six human allotments reconciled; originals remain identifiable',
 'GitHub + ten Notion snapshots + three supplied Gopika files',
 'Specialist research and independent innovator exchanged critiques',
 '1,000 fictional rows: eight comparisons and 12 model checks match',
 'Statistical increment: 10 useful labelled alerts + 10 false alerts',
 'No field study, real DB test, government call or human approval',
 'Official SIH wording and complete current amendments still open']),
('12  Pilot gates and measures', [
 'Confirm workflow, authority, current rules and correction ownership',
 'Compare total staff/student effort against an improved checklist',
 'Synthetic implementation tests precede any permitted shadow pilot',
 'Proposed targets: 90% task success; 20% lower median staff time',
 'No increase in unresolved student cases; report sample and failures',
 'Stop on disclosure, wrong-person link, silent overwrite or lost control',
 'USD42 VM+encrypted DB example excludes the rest of the stack'])
]

def main():
    asset=ROOT/'docs/assets'; asset.mkdir(parents=True,exist_ok=True)
    mmd=['mindmap','  root((SetuTrace))']
    for title,leaves in BRANCHES:
        mmd.append('    '+title)
        for leaf in leaves:
            # Quoted Mermaid labels preserve punctuation and arrows as text.
            mmd.append('      '+leaf.replace('->','to').replace('(', '').replace(')', ''))
    (ROOT/'docs/mind-map.mmd').write_text('\n'.join(mmd)+'\n',encoding='utf-8')
    W,H=2200,3350
    image=Image.new('RGB',(W,H),'#f5f8fb'); draw=ImageDraw.Draw(image)
    fonts=Path('C:/Windows/Fonts')
    if not fonts.exists(): fonts=Path('/usr/share/fonts/truetype/dejavu')
    regular='segoeui.ttf' if (fonts/'segoeui.ttf').exists() else 'DejaVuSans.ttf'
    bold='segoeuib.ttf' if (fonts/'segoeuib.ttf').exists() else 'DejaVuSans-Bold.ttf'
    def font(n,b=False): return ImageFont.truetype(str(fonts/(bold if b else regular)),n)
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         '<title>SetuTrace complete solution mind map</title>',
         '<desc>Proposed student reporting and correction layer. Twelve branches cover users, workflow, policy, integration, privacy, architecture, stack, scope, evidence and validation.</desc>',
         f'<rect width="{W}" height="{H}" fill="#f5f8fb"/>']
    def rect(x,y,w,h,fill,stroke=None,r=18):
        draw.rounded_rectangle((x,y,x+w,y+h),radius=r,fill=fill,outline=stroke,width=2)
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="2"' if stroke else '')+'/>')
    def text(x,y,s,size=24,color='#233247',b=False):
        draw.text((x,y),s,font=font(size,b),fill=color)
        svg.append(f'<text x="{x}" y="{y+size}" font-family="Segoe UI,DejaVu Sans,sans-serif" font-size="{size}" font-weight="{700 if b else 400}" fill="{color}">{escape(s)}</text>')
    def line(points,color='#a6bbc9',width=3):
        draw.line(points,fill=color,width=width,joint='curve')
        svg.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in points)+f'" fill="none" stroke="{color}" stroke-width="{width}"/>')
    text(50,24,'RESEARCH TO SOLUTION / 27 OCTOBER 2026',22,'#596b7c',True)
    rect(650,83,900,147,'#173650')
    text(973,100,'SetuTrace',43,'#ffffff',True)
    text(728,162,'A correctable evidence trail for student reporting',27,'#ffffff')
    text(568,247,'PROPOSAL: supported constraints; benefits and real deployment remain untested',23,'#596b7c')
    line([(1100,230),(1100,241)],'#abc2d0',5)
    line([(1100,293),(1100,3150)],'#abc2d0',5)
    colors=['#087e83','#405a99','#9a6331','#087e83','#405a99','#9a6331']
    for i,(title,leaves) in enumerate(BRANCHES):
        row=i//2; right=i%2; x=1210 if right else 40; y=320+row*470; w=950; h=440; col=colors[row]
        anchor=x if right else x+w
        line([(1100,y+48),(anchor,y+48)],col,4)
        rect(x,y,w,h,'#ffffff','#cbdbe4')
        rect(x,y,w,72,col,r=15)
        text(x+25,y+17,title,28,'#ffffff',True)
        yy=y+91
        for leaf in leaves:
            lines=textwrap.wrap(leaf,77,break_long_words=False)
            text(x+25,yy,'â€¢',22,col,True)
            for j,part in enumerate(lines): text(x+52,yy+j*27,part,22)
            yy+=max(37,len(lines)*27+7)
        if yy>y+h-8: raise ValueError(f'Card overflow: {title} ({yy-y})')
    rect(40,3180,2120,112,'#e5eef3')
    text(65,3197,'Decision discipline',25,'#173650',True)
    text(65,3237,'Keep institution assertion, provider evidence, policy finding and signature integrity distinct. No automated admission verdict.',24)
    svg.append('</svg>')
    (asset/'mind-map.svg').write_text('\n'.join(svg),encoding='utf-8')
    image.save(asset/'mind-map.png')
    print(f'{len(BRANCHES)} branches; {sum(len(v) for _,v in BRANCHES)} leaves; SVG/PNG {W}x{H}')

if __name__=='__main__': main()
