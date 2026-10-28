import path from "node:path";

export const LIMITS = {
  rows: 200,
  csvBytes: 512_000,
  sessionTtlMs: 60 * 60_000,
  activeSessions: 256,
};
export function readConfig(env: NodeJS.ProcessEnv = process.env) {
  const host = env.HOST ?? "127.0.0.1";
  if (!["127.0.0.1", "localhost", "::1"].includes(host))
    throw new Error(
      "This synthetic demo must bind to a loopback address. Configure real authentication before changing that boundary.",
    );
  if (env.DEMO_MODE === "false")
    throw new Error(
      "DEMO_MODE=false is fail-closed: an institutional authentication adapter is not implemented.",
    );
  const port = Number(env.PORT ?? "4871");
  if (!Number.isInteger(port) || port < 1024 || port > 65535)
    throw new Error("PORT must be an integer from 1024 to 65535.");
  return {
    host,
    port,
    dataDir: path.resolve(env.DATA_DIR ?? "data"),
    demoMode: true,
  };
}
