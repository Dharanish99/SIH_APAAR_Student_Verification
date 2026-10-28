# Deploy the synthetic demo on Vercel and Render

Live demo: https://setutrace-sih.vercel.app with API https://setutrace-sih-api.onrender.com. The owner selected Render free hosting with DATA_DIR=/tmp/setutrace; records, sessions and issuer keys reset on restarts and deployments, and the service may sleep. The paid persistent Blueprint below is an optional upgrade, not the current configuration. All visitors who have the judge code can choose any demo persona and share one fictional dataset. A reset affects all viewers. Do not enter real student data. This is not production authentication.

Vercel serves the built React app and a same-origin `/api/*` proxy. Render runs one Node 24 Express process with SQLite and the synthetic Ed25519 key on one persistent disk. The browser never needs a cross-site cookie or a public backend URL. Alternatively, Render can serve the complete app directly.

## 1. Prepare Render

1. Import this repository as a Render Blueprint using `render.yaml`. Select the `main` branch. The Blueprint provisions a **paid starter service and 1 GB persistent disk**; review actual charges in Render before creating it. Render's free filesystem is ephemeral and cannot provide this durable setup. [Render disk documentation](https://render.com/docs/disks).
2. When prompted for `APP_ORIGINS`, enter the exact HTTPS Vercel production origin you plan to use, for example `https://your-project.vercel.app` (no trailing slash). After Render assigns its URL, append its exact HTTPS origin separated by a comma if you also want the direct Render app to work. Preview deployments need their own exact origin added explicitly.
3. The Blueprint generates `DEMO_ACCESS_CODE` privately. In the Render dashboard retrieve it and share it privately with judges. Change it to rotate access; existing sessions last up to one hour, so rotate/restart alone does not revoke existing database sessions.
4. Render supplies its public hostname through `RENDER_EXTERNAL_HOSTNAME`. For a custom Render hostname, set `ALLOWED_HOSTS` to a comma-separated list of exact hostnames including the original Render hostname. Add corresponding HTTPS origins to `APP_ORIGINS`.
5. Confirm `/api/health` returns `status: ok`. The server binds `0.0.0.0` only when `HOSTED_DEMO=true`; hosting also requires a code of at least 16 characters, explicit HTTPS origins, configured hostname and an absolute `DATA_DIR`.

SQLite and the signing key both reside on `/var/data/setutrace`. Keep **one instance**; horizontal scaling and multi-instance rate limiting are not supported. The disk is not a substitute for a tested backup/restore procedure. Destroying or replacing it loses the synthetic records and key.

## 2. Prepare Vercel

1. Import the same GitHub repository as a Vercel project with repository root as the project root. `vercel.json` selects Vite, runs `npm ci` and `npm run build`, and serves `prototype/dist`.
2. In Vercel project environment variables set `RENDER_API_URL` to the exact HTTPS origin of the Render service, e.g. `https://your-service.onrender.com`, with **no trailing slash or path**. It is used server-side by the function and must not have a `VITE_` prefix.
3. Deploy. Ensure the actual Vercel origin is present in Render `APP_ORIGINS`, then redeploy/restart Render after changing it.
4. Visit Vercel's URL and enter the judge code. Test persona switching, a correction, approval, sharing, verification and reset. Verify denied access with an incorrect code and with an unconfigured browser origin. Test downloaded CSV and a fresh browser session.

API routing uses a Vercel Node function under `api/proxy.ts` with an explicit multi-segment rewrite; it forwards only the bounded request body, cookie, content type, browser origin and action token to the configured backend. It rejects redirects, oversized traffic and non-API targets. It does not cache responses. The backend issues host-only Secure, HttpOnly, SameSite=Strict cookies, which the browser associates with the Vercel origin. Keep Vercel deployment protection settings and approved domains aligned with the judging setup.

## Render-only alternative

Use the same Blueprint, set `APP_ORIGINS` to the exact Render HTTPS origin, and visit the Render URL directly. The API and built UI are served by the same process. This still requires the judge code and paid persistent disk.

## Operations and limits

- The code is a shared-demo gate, not individual authentication. Everyone with it has access to all simulated roles and can reset the workspace. Share only through a private channel and replace it after use.
- Rate limits are in-process and may aggregate requests behind platform proxies; they are not a distributed abuse-protection system. No real production or legal-compliance claim is made.
- Persona switching rotates the current session token. Sessions expire after an hour; no administrative session revocation UI exists.
- API, provider responses, issuer and policy remain synthetic. A production service needs real identity, role governance, key custody, data retention and security review.
- A local adapter test exercises the Vercel proxy with a real Express backend, cookies, CSRF, origin denial and CSV. It is not a live platform test. Complete the platform smoke test above before giving a link to judges.
- See [Vercel Node functions](https://vercel.com/docs/functions/runtimes/node-js) and [Render web services](https://render.com/docs/web-services) for platform behavior and current requirements.
