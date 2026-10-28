import { createProxy } from "../deployment/proxy.ts";
export default createProxy({ backendOrigin: process.env.RENDER_API_URL });
