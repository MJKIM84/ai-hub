export type AssistantModel = {
  id: string;
  model: string;
  displayName?: string;
  supportedReasoningEfforts?: {
    reasoningEffort: string;
    description?: string;
  }[];
  defaultReasoningEffort?: string;
};
export type AssistantSettings = {
  scenario_dialogue_version?:number;
  personal_api?: boolean;
  key_expires_at?: number | null;
  key_ttl_seconds?: number;
  api_urls?: string[];
  connection_verified?: boolean;
  provider?: "codex" | "claude" | "api";
  base_url?: string;
  model: string;
  effort?: string;
  require_key?: boolean;
  has_key?: boolean;
  workspace_id?: string;
  configured: boolean;
  status: string;
  reason?: string;
  models?: AssistantModel[];
  account?: { type?: string; planType?: string } | null;
  rate_limits?: unknown;
  busy?: boolean;
  thread_id?: string | null;
};

const statusLabels: Record<string, string> = {
  key_verified: "API 인증 확인됨 · 응답 생성 전",
  key_expired: "개인 키 만료 · 다시 연결 필요",
  connected: "연결 확인됨",
  ready: "연결 준비됨",
  authenticated: "로그인됨",
  unconfigured: "연결 설정 필요",
  disconnected: "연결 끊김",
  error: "연결 오류",
  login_required: "ChatGPT 로그인 필요",
  login_pending: "로그인 대기 중",
  not_logged_in: "ChatGPT 로그인 필요",
  unavailable: "Codex를 실행할 수 없음",
  rate_limited: "사용 한도 도달",
  usage_limit: "사용 한도 도달",
  model_unavailable: "모델 재선택 필요",
  quota_exceeded: "사용 한도 도달",
  cancelled: "요청 취소됨",
  busy: "응답 생성 중",
  configured_unverified: "설정됨 · 실제 요청 미확인",
};
export function assistantStatusLabel(settings: AssistantSettings | null) {
  if (!settings) return "연결 상태 확인 중";
  return (
    statusLabels[settings.status] ??
    (settings.configured ? "연결 설정됨" : "연결 확인 필요")
  );
}
export function modelChoices(settings: AssistantSettings | null) {
  return (settings?.models ?? []).filter((m) => Boolean(m.model || m.id));
}
export function validEffort(model: AssistantModel | undefined, effort: string) {
  const supported = model?.supportedReasoningEfforts ?? [];
  if (supported.some((e) => e.reasoningEffort === effort)) return effort;
  if (
    supported.some((e) => e.reasoningEffort === model?.defaultReasoningEffort)
  )
    return model!.defaultReasoningEffort!;
  return supported[0]?.reasoningEffort ?? "";
}
export function safeExternalUrl(value: string | null | undefined) {
  if (!value) return null;
  try {
    const url = new URL(value);
    return url.protocol === "https:" || url.protocol === "http:"
      ? url.href
      : null;
  } catch {
    return null;
  }
}
export function rateLimitLines(value: unknown): string[] {
  if (!value || typeof value !== "object") return [];
  const root = value as Record<string, unknown>;
  if (
    root.rateLimitsByLimitId &&
    typeof root.rateLimitsByLimitId === "object" &&
    Object.keys(root.rateLimitsByLimitId).length
  ) {
    return Object.entries(root.rateLimitsByLimitId).flatMap(([id, bucket]) =>
      rateLimitLines(bucket).map((line) => `${id} · ${line}`),
    );
  }
  if (root.rateLimits && typeof root.rateLimits === "object")
    return rateLimitLines(root.rateLimits);
  const result: string[] = [];
  for (const [key, label] of [
    ["primary", "주 사용량"],
    ["secondary", "추가 사용량"],
  ]) {
    const window = root[key];
    if (!window || typeof window !== "object") continue;
    const w = window as Record<string, unknown>;
    const rawPercent = w.usedPercent ?? w.used_percent;
    if (rawPercent === null || rawPercent === undefined) continue;
    const percent = Number(rawPercent);
    if (!Number.isFinite(percent)) continue;
    const reset = Number(w.resetsAt ?? w.resets_at);
    const resetText =
      Number.isFinite(reset) && reset > 0
        ? ` · 갱신 ${new Date(reset * 1000).toLocaleString("ko-KR")}`
        : "";
    result.push(
      `${label}: ${Math.max(0, Math.min(100, percent))}% 사용${resetText}`,
    );
  }
  return result;
}
