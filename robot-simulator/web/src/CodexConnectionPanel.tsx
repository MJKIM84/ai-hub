/** @jsxImportSource react */
import { PersonalApiPanel } from "./PersonalApiPanel";
import { useEffect, useState } from "react";
import { ExternalLink, RefreshCw, X } from "lucide-react";
import { request } from "./api";
import {
  assistantStatusLabel,
  modelChoices,
  rateLimitLines,
  safeExternalUrl,
  validEffort,
  type AssistantSettings,
} from "./assistantConnection";

export function CodexConnectionPanel({
  settings,
  onChange,
  requestBusy = false,
}: {
  settings: AssistantSettings | null;
  onChange: (settings: AssistantSettings) => void;
  requestBusy?: boolean;
}) {
  const [provider, setProvider] = useState(settings?.provider ?? "codex");
  const [model, setModel] = useState(settings?.model ?? "");
  const [effort, setEffort] = useState(settings?.effort ?? "");
  const [baseUrl, setBaseUrl] = useState(settings?.base_url ?? "");
  const [workspaceId, setWorkspaceId] = useState(settings?.workspace_id ?? "");
  const [requireKey, setRequireKey] = useState(settings?.require_key ?? true);
  const [apiKey, setApiKey] = useState("");
  const [pending, setPending] = useState("");
  const [error, setError] = useState("");
  const [notice, setNotice] = useState("");
  const [login, setLogin] = useState<{
    loginId: string;
    authUrl: string;
  } | null>(null);
  const models = settings?.provider === provider ? modelChoices(settings) : [];
  const selectedModel = models.find((m) => (m.model || m.id) === model);
  const allowedEffort = validEffort(selectedModel, effort);
  const limits = rateLimitLines(settings?.rate_limits);
  useEffect(() => {
    if (!settings) return;
    setProvider(settings.provider ?? "codex");
    setModel(settings.model ?? "");
    setEffort(settings.effort ?? "");
    setBaseUrl(settings.base_url ?? "");
    setWorkspaceId(settings.workspace_id ?? "");
    setRequireKey(settings.require_key ?? true);
    if (settings.account?.type === "chatgpt" && settings.configured)
      setLogin(null);
  }, [settings]);
  useEffect(() => {
    if (!login) return;
    let disposed = false;
    const timer = window.setInterval(() => {
      request<AssistantSettings>("/assistant/settings")
        .then((value) => {
          if (!disposed) onChange(value);
        })
        .catch((e) => {
          if (!disposed) setError(e instanceof Error ? e.message : String(e));
        });
    }, 4000);
    return () => {
      disposed = true;
      window.clearInterval(timer);
    };
  }, [login, onChange]);
  const act = async (label: string, operation: () => Promise<void>) => {
    if (pending) return;
    setPending(label);
    setError("");
    setNotice("");
    try {
      await operation();
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setPending("");
    }
  };
  const authUrl = safeExternalUrl(login?.authUrl);
  if (settings?.personal_api) return <PersonalApiPanel settings={settings} onChange={onChange} requestBusy={requestBusy} />;
  return (
    <section className="planner-connection" aria-label="모델 연결 설정">
      <div className="planner-connection-heading">
        <div>
          <h3>모델 연결</h3>
          <p role="status">
            {assistantStatusLabel(settings)}
            {settings?.account?.planType
              ? ` · ${settings.account.planType}`
              : ""}
          </p>
        </div>
        <button
          type="button"
          disabled={!!pending}
          onClick={() =>
            void act("상태 확인 중", async () =>
              onChange(await request<AssistantSettings>("/assistant/settings")),
            )
          }
        >
          <RefreshCw size={15} /> 상태 새로고침
        </button>
      </div>
      {settings?.reason && <p className="notice">{settings.reason}</p>}
      {error && (
        <p className="notice error" role="alert">
          {error}
        </p>
      )}
      {notice && (
        <p className="notice" role="status">
          {notice}
        </p>
      )}
      {pending && <p role="status">{pending}…</p>}
      <form
        className="planner-settings"
        onSubmit={(e) => {
          e.preventDefault();
          void act("연결 설정 저장 중", async () => {
            const saved = await request<AssistantSettings>(
              "/assistant/settings",
              "PUT",
              provider === "codex" ? { provider: "codex", model, effort: allowedEffort }
                : provider === "claude" ? {
                    provider: "claude", model, workspace_id: workspaceId,
                    ...(apiKey ? { api_key: apiKey } : {}),
                  } : {
                    provider: "api",
                    base_url: baseUrl,
                    model,
                    require_key: requireKey,
                    ...(apiKey ? { api_key: apiKey } : {}),
                  },
            );
            onChange(saved);
            setApiKey("");
            setNotice(
              "설정을 저장했습니다. 연결 상태와 사용 가능한 모델을 확인하세요.",
            );
          });
        }}
      >
        <label>
          연결 방식
          <select
            value={provider}
            disabled={requestBusy || !!pending}
            onChange={(e) => {
              setProvider(e.target.value as "codex" | "claude" | "api");
              setModel("");
              setEffort("");
              setApiKey("");
              if (e.target.value === "codex") {
                void act("Codex 연결 확인 중", async () => {
                  onChange(
                    await request<AssistantSettings>(
                      "/assistant/settings",
                      "PUT",
                      { provider: "codex" },
                    ),
                  );
                });
              }
            }}
          >
            <option value="codex">ChatGPT 로그인 · 로컬 Codex</option>
            <option value="claude">Claude · Anthropic 공식 API</option>
            <option value="api">다른 모델 · OpenAI 호환 API</option>
          </select>
        </label>
        {provider === "codex" ? (
          <>
            <p>
              ChatGPT 계정 인증은 로컬 Codex가 관리합니다. 이 화면에 비밀번호나
              인증 토큰을 입력하지 않습니다. 사용 한도에 도달해도 저장한 계획은
              유지되며 별도 과금 API로 자동 전환하지 않습니다.
            </p>
            <label>
              사용 가능한 모델
              <select
                value={model}
                disabled={!!pending || requestBusy || !models.length}
                onChange={(e) => {
                  const next = models.find(
                    (m) => (m.model || m.id) === e.target.value,
                  );
                  setModel(e.target.value);
                  setEffort(validEffort(next, effort));
                }}
              >
                <option value="">
                  {models.length
                    ? "모델 선택"
                    : "로그인과 연결 후 모델을 불러옵니다"}
                </option>
                {models.map((m) => (
                  <option key={m.id || m.model} value={m.model || m.id}>
                    {m.displayName || m.model || m.id}
                  </option>
                ))}
              </select>
            </label>
            <label>
              추론 수준
              <select
                value={allowedEffort}
                disabled={
                  !!pending ||
                  requestBusy ||
                  !selectedModel?.supportedReasoningEfforts?.length
                }
                onChange={(e) => setEffort(e.target.value)}
              >
                {!selectedModel?.supportedReasoningEfforts?.length && (
                  <option value="">모델 기본값</option>
                )}
                {selectedModel?.supportedReasoningEfforts?.map((r) => (
                  <option key={r.reasoningEffort} value={r.reasoningEffort}>
                    {r.reasoningEffort}
                  </option>
                ))}
              </select>
              {selectedModel?.supportedReasoningEfforts?.find(
                (r) => r.reasoningEffort === allowedEffort,
              )?.description && (
                <small>
                  {
                    selectedModel.supportedReasoningEfforts.find(
                      (r) => r.reasoningEffort === allowedEffort,
                    )?.description
                  }
                </small>
              )}
            </label>
            <div className="planner-connection-actions">
              <button
                type="button"
                disabled={!!pending || requestBusy || !!login}
                onClick={() =>
                  void act("로그인 준비 중", async () => {
                    const response = await request<{
                      loginId: string;
                      authUrl: string;
                    }>("/assistant/login", "POST");
                    if (!safeExternalUrl(response.authUrl))
                      throw new Error(
                        "로그인 주소를 확인하지 못했습니다. 로컬 Codex의 로그인 상태를 확인하세요.",
                      );
                    setLogin(response);
                  })
                }
              >
                {settings?.account?.type === "chatgpt"
                  ? "ChatGPT 다시 로그인"
                  : "ChatGPT 로그인"}
              </button>
              {login && (
                <>
                  {authUrl && (
                    <a
                      className="planner-link-button"
                      href={authUrl}
                      target="_blank"
                      rel="noreferrer"
                    >
                      <ExternalLink size={15} /> 로그인 페이지 열기
                    </a>
                  )}
                  <button
                    type="button"
                    disabled={!!pending}
                    onClick={() =>
                      void act("로그인 취소 중", async () => {
                        await request("/assistant/login/cancel", "POST", {
                          login_id: login.loginId,
                        });
                        setLogin(null);
                        setNotice(
                          "로그인을 취소했습니다. 저장한 계획은 유지됩니다.",
                        );
                      })
                    }
                  >
                    <X size={14} /> 로그인 취소
                  </button>
                </>
              )}
            </div>
            {login && (
              <p role="status">
                로그인 페이지에서 인증을 마치면 연결 상태를 다시 확인합니다.
              </p>
            )}
            {limits.length > 0 && (
              <div className="planner-rate-limits" aria-label="Codex 사용 한도">
                {limits.map((line) => (
                  <p key={line}>{line}</p>
                ))}
              </div>
            )}
          </>
        ) : provider === "claude" ? (
          <>
            <p>Claude는 Claude Console API로 연결합니다. 요청할 때 관련 문서·도면과 프로젝트 요약이 Anthropic에 전송됩니다. Claude 웹 구독 로그인은 API 인증이 아니며 별도 과금이 적용될 수 있습니다. 자동 전환은 없고 API 키는 서버 메모리에만 보관합니다.</p>
            <label>
              Claude 모델
              <input value={model} onChange={(e) => setModel(e.target.value)}
                list="claude-model-choices" placeholder="모델 목록을 불러온 뒤 선택하거나 ID 입력" />
              <datalist id="claude-model-choices">
                {models.map((m) => <option key={m.id} value={m.id}>{m.displayName || m.id}</option>)}
              </datalist>
            </label>
            <label>
              Claude Console API 키
              <input type="password" autoComplete="off" value={apiKey}
                onChange={(e) => setApiKey(e.target.value)}
                placeholder={settings?.provider === "claude" && settings.has_key ? "등록됨 · 변경할 때만 입력" : "서버 환경 변수도 사용 가능"} />
            </label>
            <label>
              작업 공간 ID · 여러 작업 공간을 사용하는 키에만 필요
              <input value={workspaceId} onChange={(e) => setWorkspaceId(e.target.value)}
                placeholder="wrkspc_…" />
            </label>
            <div className="planner-connection-actions">
              <button type="button" disabled={!!pending || requestBusy || settings?.provider !== "claude" || !settings.has_key}
                onClick={() => void act("Claude 모델 목록 확인 중", async () => {
                  onChange(await request<AssistantSettings>("/assistant/models/refresh", "POST"));
                  setNotice("사용 가능한 Claude 모델 목록을 확인했습니다.");
                })}>모델 목록 불러오기</button>
            </div>
          </>
        ) : (
          <>
            <p>
              별도 API 연결을 직접 선택했습니다. 아래 주소로 메시지와 프로젝트
              정보가 전송되며, 해당 서비스의 과금 조건이 적용될 수 있습니다.
            </p>
            <label>
              OpenAI 호환 API 주소
              <input
                type="url"
                required
                value={baseUrl}
                onChange={(e) => setBaseUrl(e.target.value)}
                placeholder="https://api.openai.com/v1"
              />
            </label>
            <label>
              모델 이름
              <input
                required
                value={model}
                onChange={(e) => setModel(e.target.value)}
              />
            </label>
            <label>
              API 키 · 서버 메모리에만 보관
              <input
                type="password"
                autoComplete="off"
                value={apiKey}
                onChange={(e) => setApiKey(e.target.value)}
                placeholder={
                  settings?.has_key
                    ? "등록됨 · 변경할 때만 입력"
                    : "서버 환경 변수도 사용 가능"
                }
              />
            </label>
            <label className="check">
              <input
                type="checkbox"
                checked={requireKey}
                onChange={(e) => setRequireKey(e.target.checked)}
              />{" "}
              인증 키 사용
            </label>
          </>
        )}
        <div className="planner-connection-actions">
          <button
            type="submit"
            disabled={
              !!pending ||
              requestBusy ||
              (provider === "codex" && (!selectedModel || !model))
            }
          >
            연결 설정 저장
          </button>
        </div>
      </form>
    </section>
  );
}
