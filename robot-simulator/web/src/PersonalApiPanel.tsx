/** @jsxImportSource react */
import { useEffect, useState } from "react";
import { request } from "./api";
import {
  assistantStatusLabel,
  type AssistantSettings,
} from "./assistantConnection";

export function PersonalApiPanel({
  settings,
  onChange,
  requestBusy = false,
}: {
  settings: AssistantSettings;
  onChange: (s: AssistantSettings) => void;
  requestBusy?: boolean;
}) {
  const [provider, setProvider] = useState(
    settings.provider === "claude" ? "claude" : "api",
  );
  const [url, setUrl] = useState(
    settings.base_url ?? "https://api.openai.com/v1",
  );
  const [model, setModel] = useState(settings.model ?? "");
  const [key, setKey] = useState("");
  const [workspace, setWorkspace] = useState(settings.workspace_id ?? "");
  const [consent, setConsent] = useState(false);
  const [pending, setPending] = useState("");
  const [error, setError] = useState("");
  const [notice, setNotice] = useState("");
  const [now, setNow] = useState(Date.now());
  const same =
    settings.provider === provider &&
    (provider === "claude" || url === settings.base_url);
  const hasKey = same && settings.has_key;
  const models = same ? (settings.models ?? []) : [];
  useEffect(() => {
    const timer = window.setInterval(() => {
      setNow(Date.now());
      request<AssistantSettings>("/assistant/settings")
        .then(onChange)
        .catch(() => {});
    }, 15000);
    return () => clearInterval(timer);
  }, [onChange]);
  const act = async (label: string, fn: () => Promise<void>) => {
    if (pending) return;
    setPending(label);
    setError("");
    setNotice("");
    try {
      await fn();
    } catch (e) {
      setError(e instanceof Error ? e.message : "연결을 확인하지 못했습니다.");
    } finally {
      setPending("");
      setKey("");
    }
  };
  const remaining = settings.key_expires_at
    ? Math.min(
        Math.ceil((settings.key_ttl_seconds ?? 1800) / 60),
        Math.max(0, Math.ceil((settings.key_expires_at * 1000 - now) / 60000)),
      )
    : 0;
  return (
    <section
      className="planner-connection personal-api-panel"
      aria-label="개인 API 연결"
    >
      <div className="planner-connection-heading">
        <div>
          <h3>내 API로 AI 사용하기</h3>
          <p role="status">
            {assistantStatusLabel(settings)}
            {settings.has_key && ` · 키 보관 ${remaining}분 남음`}
          </p>
        </div>
        {settings.has_key && (
          <button
            type="button"
            disabled={!!pending}
            onClick={() =>
              void act("연결 해제 중", async () => {
                const next = await request<AssistantSettings>(
                  "/assistant/disconnect",
                  "POST",
                );
                onChange(next);
                setConsent(false);
                setNotice(
                  "개인 키를 제거했습니다. 작업과 계획은 유지됩니다. 이미 전송된 요청의 과금은 취소되지 않을 수 있습니다.",
                );
              })
            }
          >
            연결 해제 · 키 삭제
          </button>
        )}
      </div>
      <p>
        OpenAI 또는 Claude의 개인 API 키로 연결하세요. 계정 비밀번호는 입력하지
        않습니다. API 비용은 본인 계정에 청구되며, 채팅 구독과 별도입니다.
      </p>
      <p className="notice">
        키는 이 체험 공간의 서버 메모리에서만 최대 30분 사용합니다.
        파일·브라우저 저장소에 저장하지 않으며, 연결 해제 또는 만료 시
        제거합니다. 우리 서버가 키를 받아 선택한 AI 서비스로 요청을 전달합니다.
      </p>
      {settings.reason && <p role="status">{settings.reason}</p>}
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
          void act(key ? "개인 API 연결 확인 중" : "모델 적용 중", async () => {
            const saved = await request<AssistantSettings>(
              "/assistant/settings",
              "PUT",
              {
                provider,
                model,
                ...(provider === "api"
                  ? { base_url: url }
                  : { workspace_id: workspace }),
                ...(key ? { api_key: key, consent } : {}),
              },
            );
            onChange(saved);
            if (key) {
              const verified = await request<AssistantSettings>(
                "/assistant/models/refresh",
                "POST",
              );
              onChange(verified);
              setNotice(
                "키로 모델 목록을 확인했습니다. 업무에 사용할 모델을 선택하고 적용하세요. 실제 응답 생성은 채팅 요청 시 확인합니다.",
              );
            } else
              setNotice(
                "모델을 적용했습니다. 이제 업무 채팅에서 질문하거나 계획을 요청하세요.",
              );
          });
        }}
      >
        <label>
          AI 서비스
          <select
            value={provider}
            disabled={!!pending || requestBusy}
            onChange={(e) => {
              setProvider(e.target.value);
              setKey("");
              setModel("");
              setWorkspace("");
              setConsent(false);
              setError("");
              setNotice("");
              if (e.target.value === "api")
                setUrl(settings.api_urls?.[0] ?? "https://api.openai.com/v1");
            }}
          >
            <option value="api">OpenAI · 호환 API</option>
            <option value="claude">Claude · Anthropic</option>
          </select>
        </label>
        {provider === "api" && (
          <label>
            연결 서비스
            <select
              value={url}
              disabled={!!pending || requestBusy}
              onChange={(e) => {
                setUrl(e.target.value);
                setKey("");
                setModel("");
                setConsent(false);
              }}
            >
              {(settings.api_urls ?? ["https://api.openai.com/v1"]).map((u) => (
                <option key={u} value={u}>
                  {u === "https://api.openai.com/v1" ? "OpenAI 공식 API" : u}
                </option>
              ))}
            </select>
          </label>
        )}
        <label>
          개인 API 키
          <input
            type="password"
            autoComplete="off"
            spellCheck={false}
            maxLength={512}
            value={key}
            disabled={!!pending || requestBusy}
            onChange={(e) => setKey(e.target.value)}
            placeholder={
              hasKey ? "연결됨 · 교체할 때만 입력" : "제공자에서 발급한 API 키"
            }
          />
        </label>
        {provider === "claude" && (
          <label>
            작업 공간 ID · 선택
            <input
              value={workspace}
              disabled={!!pending || requestBusy}
              onChange={(e) => setWorkspace(e.target.value)}
              placeholder="여러 작업 공간을 사용하는 키에만 필요"
            />
          </label>
        )}
        <label>
          사용할 모델
          <input
            aria-label="사용할 모델"
            list="personal-api-models"
            value={model}
            disabled={!!pending || requestBusy}
            onChange={(e) => setModel(e.target.value)}
            placeholder="키 연결 후 목록에서 선택하거나 모델 ID 입력"
          />
          <datalist id="personal-api-models">
            {models.map((m) => (
              <option key={m.id} value={m.id}>
                {m.displayName || m.id}
              </option>
            ))}
          </datalist>
          <small>
            계정의 모델 목록입니다. 작업 계획은 JSON 응답, 도면 분석은 이미지
            입력을 지원하는 모델이 필요합니다.
          </small>
        </label>
        {(!hasKey || !!key) && (
          <label className="check">
            <input
              type="checkbox"
              checked={consent}
              onChange={(e) => setConsent(e.target.checked)}
              disabled={!!pending}
            />
            필요한 문서·도면·프로젝트 요약과 메시지가 선택한 AI 서비스로
            전송되고, 내 API 계정에 비용이 발생함을 확인했습니다.
          </label>
        )}
        <div className="planner-connection-actions">
          <button
            type="submit"
            disabled={
              !!pending ||
              requestBusy ||
              (!hasKey && !key) ||
              (!!key && !consent)
            }
          >
            {key || !hasKey ? "키 연결 · 모델 불러오기" : "선택한 모델 적용"}
          </button>
          {hasKey && (
            <button
              type="button"
              disabled={!!pending || requestBusy}
              onClick={() =>
                void act("모델 목록 확인 중", async () => {
                  onChange(
                    await request<AssistantSettings>(
                      "/assistant/models/refresh",
                      "POST",
                    ),
                  );
                  setNotice("모델 목록을 갱신했습니다.");
                })
              }
            >
              모델 목록 새로고침
            </button>
          )}
        </div>
      </form>
      <small>
        키 없이도 예제 시뮬레이션은 사용할 수 있습니다. 연결 오류나 사용 한도가
        발생해도 다른 유료 API로 자동 전환하지 않습니다.
      </small>
    </section>
  );
}
