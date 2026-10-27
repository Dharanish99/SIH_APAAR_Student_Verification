// Research reproduction only. Runs the inspected original pure-JavaScript harness.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const crypto = require('node:crypto');
const dir = path.join(__dirname, 'notion-original');
const source = fs.readFileSync(path.join(dir, 'dharanish-research-harness.txt'), 'utf8');
const context = { console: { log() {} } };
vm.createContext(context);
const result = vm.runInContext(source + '\nresult;', context, { timeout: 5000 });
const original = JSON.parse(fs.readFileSync(path.join(dir, 'dharanish-experiment-results.json'), 'utf8'));
const comparisons = {};
for (const key of ['rules', 'statistical', 'combined', 'typeCounts', 'checks']) {
  comparisons[key] = JSON.stringify(result.report[key]) === JSON.stringify(original[key]);
}
for (const [key, file] of Object.entries({csv:'dharanish-synthetic-records.csv',truthCsv:'dharanish-synthetic-labels.csv',referenceCsv:'dharanish-reference-cohort.csv'})) {
  comparisons[file] = result[key] === fs.readFileSync(path.join(dir, file), 'utf8');
}
const report = {
  run_date: '2026-10-26', runtime: process.version, platform: process.platform,
  source_sha256: crypto.createHash('sha256').update(source).digest('hex'),
  scope: 'Sequential in-memory model only; not PostgreSQL, real providers, concurrent workers, or field validation.',
  comparison_with_original: comparisons, result: result.report
};
fs.writeFileSync(path.join(__dirname, 'reproduction-results.json'), JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report,null,2));
if (Object.values(comparisons).some(v=>!v)) process.exitCode=1;
