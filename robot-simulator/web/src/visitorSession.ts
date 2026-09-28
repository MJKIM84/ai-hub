export type VisitorSession = {
  mode: "local" | "personal_api";
  workspace_id?: string;
  expires_at?: number;
  key_ttl_seconds?: number;
};
let current: VisitorSession = { mode: "local" };
const temporary = new Map<string, string>();
export const visitorSession = () => current;
export async function initializeVisitorSession() {
  const response = await fetch("/api/session", {
    headers: { "X-Robot-Request": "1" },
    cache: "no-store",
  });
  // Existing local servers may not yet expose this endpoint.
  if (
    response.status === 404 ||
    !response.headers.get("content-type")?.includes("application/json")
  )
    return current;
  const value = await response.json();
  if (!response.ok)
    throw new Error(value.detail || "체험 공간을 열지 못했습니다.");
  current = value;
  return current;
}
/** Personal workspaces never restore another session's local browser draft/history pointer. */
export const workspaceStorage = {
  getItem(key: string) {
    return current.mode === "personal_api"
      ? (temporary.get(key) ?? null)
      : localStorage.getItem(key);
  },
  setItem(key: string, value: string) {
    if (current.mode === "personal_api") temporary.set(key, value);
    else localStorage.setItem(key, value);
  },
};
