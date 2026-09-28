import type {
  Catalog,
  Experiment,
  MeshData,
  Pose,
  Project,
  RunState,
  SavedProject,
  Policy,
  Recording,
  RecoveryRequest,
  RecoveryState,
} from "./types";
export class ApiError extends Error {
  constructor(
    message: string,
    public status?: number,
    public uncertain = false,
  ) {
    super(message);
    this.name = "ApiError";
  }
}
export async function request<T>(
  path: string,
  method = "GET",
  body?: unknown,
): Promise<T> {
  const abort = new AbortController();
  const timeout = setTimeout(
    () => abort.abort(),
    (path === "/experiments" || path === "/assistant/chat" || path.endsWith("/extract/model") || path.endsWith("/inspect")) && method === "POST"
      ? 600000
      : path === "/scene" && method === "GET"
        ? 60000
      : method === "GET"
        ? 5000
        : 30000,
  );
  try {
    const response = await fetch(`/api${path}`, {
      method,
      signal: abort.signal,
      headers:
        body === undefined ? { "X-Robot-Request": "1" } : { "Content-Type": "application/json", "X-Robot-Request": "1" },
      body: body === undefined ? undefined : JSON.stringify(body),
    });
    if (!response.ok) {
      let message = await response.text();
      try {
        const data = JSON.parse(message);
        message =
          typeof data.detail === "string"
            ? data.detail
            : JSON.stringify(data.detail ?? data);
      } catch {
        /* Preserve plain text server diagnostics. */
      }
      throw new ApiError(
        message || `요청 실패 (${response.status})`,
        response.status,
      );
    }
    return (await response.json()) as T;
  } catch (error) {
    if (error instanceof ApiError) throw error;
    throw new ApiError(
      method === "GET"
        ? abort.signal.aborted
          ? "실행부 응답이 지연되고 있습니다. 자동으로 다시 연결합니다."
          : "실행부와 연결이 끊겼습니다. 로컬 서버 상태를 확인하세요."
        : "요청 결과를 확인하지 못했습니다. 연결이 복구되면 상태와 명령 이력을 확인하세요. 같은 명령을 자동으로 재전송하지 않습니다.",
      undefined,
      method !== "GET",
    );
  } finally {
    clearTimeout(timeout);
  }
}
export const api = {
  catalog: () => request<Catalog>("/catalog"),
  project: () => request<Project>("/project"),
  template: (id: string) =>
    request<Project>(`/templates/${encodeURIComponent(id)}`),
  apply: (project: Project) => request<Project>("/project", "PUT", project),
  save: (project: Project) =>
    request<Project>("/projects/save", "POST", { project }),
  saved: () => request<SavedProject[]>("/projects"),
  load: (id: string, revision: number) =>
    request<Project>(
      `/projects/${encodeURIComponent(id)}/versions/${revision}`,
    ),
  clone: (id: string) =>
    request<Project>(`/projects/${encodeURIComponent(id)}/clone`, "POST"),
  cancelTask: (id: string) =>
    request<unknown>(`/tasks/${encodeURIComponent(id)}/cancel`, "POST"),
  recoverTask: (id: string, body: RecoveryRequest) =>
    request<RecoveryState>(
      `/tasks/${encodeURIComponent(id)}/recovery`,
      "POST",
      body,
    ),
  cancelRecovery: (id: string, recovery_id: string) =>
    request<RecoveryState>(
      `/tasks/${encodeURIComponent(id)}/recovery/cancel`,
      "POST",
      { recovery_id },
    ),
  resumeRobot: (id: string) =>
    request<unknown>(`/robots/${encodeURIComponent(id)}/resume`, "POST"),
  facilityTarget: (id: string, target: Pose) =>
    request<unknown>(
      `/facilities/${encodeURIComponent(id)}/target`,
      "POST",
      target,
    ),
  recording: () => request<Recording>("/recording"),
  state: () => request<RunState>("/state"),
  scene: () => request<{ run_id: string; meshes: MeshData[] }>("/scene"),
  control: (action: string, steps?: number, speed?: number) =>
    request<unknown>("/control", "POST", { action, steps, speed }),
  command: (id: string, kind: string, target?: Pose) =>
    request<Record<string, unknown>>(
      `/robots/${encodeURIComponent(id)}/command`,
      "POST",
      {
        kind,
        target,
      },
    ),
  fault: (
    target_id: string,
    kind: string,
    duration: number,
    magnitude: number,
  ) =>
    request<unknown>("/faults", "POST", {
      target_id,
      kind,
      duration,
      magnitude,
    }),
  experiments: () => request<Experiment[]>("/experiments"),
  experimentProject: (experimentId: string, runId: string) => request<Project>(
    `/experiments/${encodeURIComponent(experimentId)}/runs/${encodeURIComponent(runId)}/project`),
  experiment: (
    project: Project,
    seeds: number[],
    duration: number,
    policies: Policy[],
  ) =>
    request<Experiment>("/experiments", "POST", {
      project,
      seeds,
      duration,
      policies,
    }),
};
export function downloadJSON(name: string, data: unknown) {
  // Capture this exact draft/recording now, before checking server availability.
  const payload = JSON.stringify(data, null, 2);
  if (payload === undefined) throw new Error("내보낼 JSON이 없습니다.");
  const localDownload = () => {
    const url = URL.createObjectURL(
      new Blob([payload], { type: "application/json" }),
    );
    const a = document.createElement("a");
    a.href = url;
    a.download = name;
    a.hidden = true;
    document.body.append(a);
    try {
      a.click();
    } finally {
      a.remove();
      window.setTimeout(() => URL.revokeObjectURL(url), 60_000);
    }
  };
  if (!navigator.onLine) {
    localDownload();
    return;
  }
  const requestDownload = async () => {
    const abort = new AbortController();
    const timeout = window.setTimeout(() => abort.abort(), 3_000);
    let available = false;
    try {
      const response = await fetch("/api/exports/json", {
        method: "HEAD",
        cache: "no-store",
        redirect: "error",
        signal: abort.signal,
      });
      available =
        response.ok && response.headers.get("X-JSON-Export") === "form-post-v1";
    } catch {
      // Offline/older servers keep the existing local download option.
    } finally {
      window.clearTimeout(timeout);
    }
    if (!available) {
      localDownload();
      return;
    }
    const frame = document.createElement("iframe");
    frame.name = `json-export-${crypto.randomUUID()}`;
    frame.hidden = true;
    frame.title = "JSON 다운로드 응답";
    const form = document.createElement("form");
    form.method = "POST";
    form.action = "/api/exports/json";
    form.target = frame.name;
    form.enctype = "application/x-www-form-urlencoded";
    form.acceptCharset = "UTF-8";
    form.hidden = true;
    for (const [key, value] of Object.entries({ name, payload })) {
      const field = document.createElement("textarea");
      field.name = key;
      field.value = value;
      form.append(field);
    }
    document.body.append(frame, form);
    try {
      // Native HTTP attachment handling; do not navigate the editor or expose
      // document data in a GET URL. Submission is not download confirmation.
      form.submit();
    } catch {
      frame.remove();
      localDownload();
    } finally {
      form.remove();
      window.setTimeout(() => frame.remove(), 60_000);
    }
  };
  void requestDownload();
}
