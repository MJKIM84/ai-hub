import { ScenarioSampleForm } from "./ScenarioSampleForm";
import { ScenarioDraftPanel, ConfirmationControl, type ScenarioDraft, type ScenarioTask } from "./ScenarioDraftPanel";
import { workspaceStorage } from "./visitorSession";
import { useEffect, useRef, useState } from "react";
import {
  MessageSquare,
  Send,
  Play,
  RefreshCw,
  Settings2,
  Users,
  Lock,
  Pause,
  Square,
  BookOpen,
} from "lucide-react";
import { request, downloadJSON } from "./api";
import { PlanView } from "./PlanView";
import { CodexConnectionPanel } from "./CodexConnectionPanel";
import {
  assistantStatusLabel,
  type AssistantSettings,
} from "./assistantConnection";
import {
  OntologyPanel,
  PlanOntologyEvidence,
  type PlanOntology,
} from "./OntologyPanel";
import type { Project, RunState, PedestrianBehavior, Pose } from "./types";
import "./PlanningWorkbench.css";
import "./ScenarioDraftPanel.css";
import { taskStatusLabel } from "./uiMessages";
import { swapPlanningRobot, canRemovePlanningRobot } from "./planningSelection";

type Issue = {
  code: string;
  message: string;
  suggestion?: string;
  robot_id?: string;
  task_id?: string;
  resolution_options?: OccupancyResolution[];
};
type OccupancyResolution = {
  kind: "waiting_position" | "task_order" | "alternate_destination" | "route_detour" | "reachable_zone";
  label: string;
  robot_id?: string;
  blocked_task_id?: string;
  waiting_task_id?: string;
  task_id?: string;
  destination_id?: string;
  x?: number;
  y?: number;
  points?: { x: number; y: number }[];
};
type Selection = {
  robot_ids?: string[];
  task_robot_ids?: Record<string, string>;
  pedestrians?: {
    include?: boolean;
    total?: number;
    seed?: number;
    allowed_floor_ids?: string[];
    zone_ids?: string[];
    behavior?: Partial<PedestrianBehavior>;
  };
  pedestrian_avoidance?: Record<string, number | string>;
  occupancy_resolution?: OccupancyResolution;
};
type Option = {
  id: string;
  name: string;
  model_id: string;
  selected: boolean;
  locked: boolean;
  available: boolean;
  availability_reason?: string;
  reason: string;
  roles: string[];
  eligible_for: string[];
  task_rejections?: { task_id: string; blockers: { code: string; message: string }[] }[];
};
type Plan = {
  id: string;
  version: number;
  plan_hash: string;
  source_project_hash: string;
  source_project_revision?: number;
  source_environment_id?: string;
  source_environment_name?: string;
  source_environment_version?: number;
  origin: string;
  input_receipt?:{map_version:number;map_id:string;project_hash:string;ontology_hash:string;model_execution?:{provider?:string;model?:string}};
  selection: Selection;
  intent: { goal: string; scenario?: ScenarioDraft; tasks?:ScenarioTask[] };
  conversation: { role: string; content: string; references?: string[];
    runtime_basis?:{run_id:string;sim_time:number;status:string};
    related_documents?: { id: string; title: string; version: string }[] }[];
  approval?: { run_id: string; version: number };
  previous_approvals?: { run_id: string; version: number }[];
  compiled: {
    execution_policy?:{stop_when_tasks_terminal:boolean;basis:string};
    ontology?: PlanOntology;
    spatial_ontology?: { status: string; limits?: string[]; scale_basis?: string[] };
    preview?: {
      routes: { task_id: string; floor_id: string; points: Pose[] }[];
    };
    kind: string;
    can_approve: boolean;
    status: string;
    goal: string;
    project: Project | null;
    selection: Selection;
    selected_robot_ids: string[];
    robot_options: Option[];
    requirements: {
      id: string;
      task_id: string;
      capability: string;
      min_count: number;
      eligible_robot_ids: string[];
      alternative_robot_ids?: string[];
      reason: string;
    }[];
    steps: {
      id: string;
      number: number;
      name: string;
      robot_ids: string[];
      dependencies: string[];
      resources: string[];
      item_id?: string;
      floor_id: string;
      destination: { x: number; y: number };
      trip?: {source_floor:string;dest_floor:string;elevator_id:string;mass:number}|null;
      roles?:{donor_id?:string;carrier_id?:string;receiver_id?:string};
      completion_criterion?:string;
      parallel_with?:string[];
      failure_behavior: string;
      condition?:{task_id:string;outcome:"completed"|"failed"};
      confirmation?:{label:string; criterion:string; timeout_s:number};
      spatial_review?: {
        status: string;
        required_width_m: number;
        reviewed_apertures: { id: string; name: string; kind: string; width_m: number }[];
      };
    }[];
    recommendations: {
      robot_id: string;
      basis: string;
      reason: string;
      comparison: string;
    }[];
    blockers: Issue[];
    clarifications: Issue[];
    assumptions: string[];
    pedestrians: {
      total?: number;
      existing_count?: number;
      retained_count?: number;
      added_count?: number;
      seed?: number;
      excluded_nested_zones?: { id: string; name: string; floor_id: string }[];
    };
    resources: string[];
    occupancy_resolution?: OccupancyResolution;
  };
};
type StoredResult = {
  live: boolean;
  approval?: { run_id: string; version: number } | null;
  current_plan_version?: number;
  result: { snapshot: RunState } | null;
};
const measuredPedestrianClearance = (metrics: Record<string, unknown>): number | null => {
  const perRobot = metrics.pedestrian_min_clearance_m;
  if (!perRobot || typeof perRobot !== "object" || Array.isArray(perRobot)) return null;
  const measured = Object.values(perRobot).filter((value): value is number =>
    typeof value === "number" && Number.isFinite(value));
  return measured.length ? Math.min(...measured) : null;
};
const defaultAvoidance = {
  desired_clearance_m: 0.5,
  slowdown_distance_m: 2,
  stop_distance_m: 0.65,
  resume_distance_m: 0.9,
  max_near_speed_m_s: 0.2,
  strategy: "detour",
  replan_after_s: 2,
  blocked_timeout_s: 15,
  observation_range_m: 6,
  braking_deceleration_m_s2: 0.8,
};
const behaviorDefaults = {
  mode: "free_roam" as const,
  speed_min_m_s: 0.5,
  speed_max_m_s: 1.2,
  stop_rate_per_s: 0.08,
  stop_duration_min_s: 0.5,
  stop_duration_max_s: 2,
  destination_change_rate_per_s: 0.03,
  crossing_rate_per_s: 0.04,
};
const roleNames: Record<string, string> = {
  carrier: "운반",
  receiver: "인수·배치",
  donor: "상차",
  patrol: "순찰",
  inspect: "점검",
  delivery: "배송",
  transport: "운반",
  handoff: "물품 인계",
};
const runNames: Record<string, string> = {
  paused: "일시 정지",
  running: "실행 중",
  failed: "실패",
  completed: "전체 단계 완료 · 자동 정지",
  timed_out: "제한 시간 종료",
};
const statusNames: Record<string, string> = {
  ready: "승인 가능",
  blocked: "조건 수정 필요",
  clarification: "확인 필요",
  analysis: "질문 분석",
};
const issueText = (message: string) => {
  const match = message.match(/Value error, (.*?)(?:\s*\[type=|$)/s);
  return match ? match[1].trim() : message;
};
const textError = (e: unknown) => (e instanceof Error ? e.message : String(e));

export default function PlanningWorkbench({
  project,
  state,
  connected,
  onObserve,
  onReviewMap,
  onUseScenarioProject,
  focusPlan,
}: {
  project: Project;
  state: RunState | null;
  connected: boolean;
  onObserve: (id: string) => void;
  onReviewMap: () => void;
  onUseScenarioProject: (p:Project)=>Promise<void>;
  focusPlan?: {id:string; version:number; sequence:number} | null;
}) {
  const [settings, setSettings] = useState<AssistantSettings | null>(null),
    [settingsOpen, setSettingsOpen] = useState(false),
    [ontologyOpen, setOntologyOpen] = useState(false),
    [focusedDocumentId, setFocusedDocumentId] = useState(""),
    [cancelling, setCancelling] = useState(false);
  const [plan, setPlan] = useState<Plan | null>(null),
    [selection, setSelection] = useState<Selection>({}),
    [dirty, setDirty] = useState(false);
  const [message, setMessage] = useState(""),
    [mode, setMode] = useState("auto"),
    [busy, setBusy] = useState(""),
    [error, setError] = useState(""),
    [notice, setNotice] = useState("");
  const [selected, setSelected] = useState(""),
    [floor, setFloor] = useState(project.environment.floors[0]?.id ?? ""),
    [tab, setTab] = useState("robots");
  const [history, setHistory] = useState<
      { id: string; version: number; intent: { goal: string }; recovered_from?: string }[]
    >([]),
    [result, setResult] = useState<StoredResult | null>(null);
  const [stopped, setStopped] = useState(false);
  const [designerAvailable,setDesignerAvailable] = useState(false);
  const requestId = useRef<string | null>(null),
    source = useRef<string>("");
  const currentProject = useRef(project);
  const messagesRef = useRef<HTMLDivElement>(null);
  useEffect(()=>{
    if(messagesRef.current) messagesRef.current.scrollTop=messagesRef.current.scrollHeight;
  },[plan?.id,plan?.conversation?.length]);
  currentProject.current = project;
  useEffect(() => {
    const floors=(plan?.compiled.project ?? project).environment.floors;
    if (!floors.some((f) => f.id === floor))
      setFloor(floors[0]?.id ?? "");
  }, [project.environment.floors, plan?.compiled.project, floor]);
  useEffect(() => {
    request<AssistantSettings>("/assistant/settings")
      .then(s=>{setSettings(s);setDesignerAvailable(s.scenario_dialogue_version===1);setMode(s.scenario_dialogue_version===1?'design':'auto');})
      .catch((e) => setError(textError(e)));
    request<typeof history>("/plans")
      .then((rows) => {
        setHistory(rows);
        const last = workspaceStorage.getItem("robot-planner-last-id");
        if (!focusPlan && last && rows.some((r) => r.id === last))
          request<Plan>(`/plans/${last}`)
            .then(async (p) => {
              const map = p.compiled.project?.environment;
              const current = currentProject.current.environment;
              if ((p.source_environment_id ?? map?.id) === current.id &&
                  (p.source_environment_version ?? map?.version) === current.version) {
                const checkedProject = currentProject.current;
                let matches = false;
                try {
                  const check = await request<{ matches: boolean }>(`/plans/${p.id}/source-check`, "POST", {
                    version: p.version,
                    project: checkedProject,
                  });
                  matches = check.matches;
                } catch {
                  accept(p);
                  setDirty(true);
                  setNotice("저장 계획은 열었지만 현재 구성과의 일치 여부를 확인하지 못했습니다. 연결을 복구한 뒤 계획 갱신을 눌러 다시 검증하세요.");
                  return;
                }
                accept(p);
                setDirty(!matches || checkedProject !== currentProject.current);
              } else {
                setNotice("마지막 계획의 지도 버전이 현재 지도와 다릅니다. 현재 지도에서 새 계획을 요청하세요.");
              }
            })
            .catch((e) => setError(`저장 계획을 다시 열지 못했습니다. 계획 목록에서 다시 선택하세요. ${textError(e)}`));
      })
      .catch(() => {});
  }, []);
  useEffect(() => {
    if (plan && source.current && source.current !== JSON.stringify(project))
      setDirty(true);
  }, [project, plan]);
  useEffect(() => {
    if (!connected || !plan?.approval || !state?.run_id || plan.approval.run_id===state.run_id) return;
    let active=true;
    // A top-bar reset creates another run of the same approved conditions.
    // Refresh only execution identity, preserving unsaved selection edits.
    void request<Plan>(`/plans/${plan.id}`).then(latest => {
      if (!active || latest.version!==plan.version || latest.plan_hash!==plan.plan_hash || latest.approval?.run_id!==state.run_id) return;
      setPlan(current => current?.id===latest.id && current.version===latest.version
        ? {...current,approval:latest.approval,previous_approvals:latest.previous_approvals} : current);
      setResult(null);setStopped(false);
    }).catch(() => {});
    return () => {active=false;};
  }, [connected, state?.run_id, plan?.id, plan?.version]);
  useEffect(() => {
    if (!plan || !connected) return;
    const map = plan.compiled.project?.environment;
    const planMapId = plan.source_environment_id ?? map?.id;
    const planMapVersion = plan.source_environment_version ?? map?.version;
    if (planMapId && (planMapId !== project.environment.id || planMapVersion !== project.environment.version)) {
      setDirty(true);
      requestId.current = null;
      setNotice("이전 계획은 보존했습니다. 현재 지도와 달라 승인할 수 없습니다. 저장된 지시로 새 계획을 만들 수 있습니다.");
    }
  }, [connected, plan, project.environment.id, project.environment.version]);
  const act = async (label: string, fn: () => Promise<void>) => {
    if (busy) return;
    const requestProject = JSON.stringify(currentProject.current);
    setBusy(label);
    setError("");
    setNotice("");
    try {
      await fn();
    } catch (e) {
      setError(textError(e));
    } finally {
      if (requestProject !== JSON.stringify(currentProject.current))
        setDirty(true);
      setBusy("");
    }
  };
  const accept = (p: Plan) => {
    setPlan(p);
    setHistory((rows) => [
      { id: p.id, version: p.version, intent: p.intent,
        recovered_from: rows.find((row) => row.id === p.id && row.version === p.version)?.recovered_from },
      ...rows.filter((r) => r.id !== p.id || r.version !== p.version),
    ]);
    setSelection({
      ...(p.compiled.selection ?? p.selection),
      ...(p.selection.occupancy_resolution ? { occupancy_resolution: p.selection.occupancy_resolution } : {}),
      ...(p.compiled.project?.policy.pedestrian_avoidance
        ? {
            pedestrian_avoidance:
              p.compiled.project.policy.pedestrian_avoidance,
          }
        : {}),
    });
    setDirty(false);
    source.current = JSON.stringify(currentProject.current);
    requestId.current = null;
    setResult(null);
    setStopped(false);
    workspaceStorage.setItem("robot-planner-last-id", p.id);
    if (
      p.compiled.project &&
      !p.compiled.project.environment.floors.some((f) => f.id === floor)
    )
      setFloor(p.compiled.project.environment.floors[0]?.id ?? "");
  };
  const newScenario = () => {
    setPlan(null);setSelection({});setResult(null);setStopped(false);
    setDirty(false);setSelected('');setMessage('');setError('');setMode(designerAvailable?'design':'auto');
    requestId.current=null;source.current=JSON.stringify(currentProject.current);
    workspaceStorage.setItem('robot-planner-last-id','');
    setNotice('새 시나리오 대화를 시작합니다. 이전 계획·실행 기록은 저장한 계획 기록에 남아 있습니다.');
  };
  useEffect(() => {
    if (!focusPlan) return;
    let active = true;
    void (async () => {
      setError("");
      try {
        const selected = await request<Plan>(`/plans/${focusPlan.id}/versions/${focusPlan.version}`);
        if (!active) return;
        accept(selected);
        let matches = false;
        try {
          const check = await request<{matches:boolean}>(`/plans/${selected.id}/source-check`, "POST", {
            version: selected.version, project: currentProject.current,
          });
          matches = check.matches;
        } catch { /* The saved plan remains viewable when a source check is unavailable. */ }
        if (!active) return;
        setDirty(!matches);
        setNotice(matches ? "저장된 계획 버전을 열었습니다. 승인 상태와 실행 결과를 확인하세요." :
          "저장된 계획을 열었지만 현재 지도·로봇·작업 구성과 다릅니다. 수정안을 다시 검토하고 승인하세요.");
      } catch (error) {
        if (active) setError(`저장 계획을 열지 못했습니다. ${textError(error)}`);
      }
    })();
    return () => { active = false; };
  }, [focusPlan?.sequence]);
  const patch = (s: Partial<Selection>) => {
    setSelection((v) => ({ ...v, ...s }));
    setDirty(true);
  };
  const people = selection.pedestrians ?? {};
  const patchPeople = (p: NonNullable<Selection["pedestrians"]>) =>
    patch({ pedestrians: { ...people, ...p } });
  const preview = plan && (plan.source_environment_id!==project.environment.id || plan.source_environment_version!==project.environment.version) ? project : plan?.compiled.project ?? project;
  const entities = [
    ...preview.robots,
    ...preview.people,
    ...preview.items,
    ...preview.environment.elements,
  ];
  const entity = entities.find((e) => e.id === selected);
  const focus = (id: string) => {
    const e = entities.find((e) => e.id === id);
    setSelected(id);
    if (e) setFloor(e.floor_id);
    else {
      const task = preview.tasks.find((t) => t.id === id);
      if (task) {
        setFloor(task.floor_id);
        setSelected(task.preferred_robot ?? "");
      }
    }
  };
  const selectedRobots =
    selection.robot_ids ?? plan?.compiled.selected_robot_ids ?? [];
  const livePlan = !!plan?.approval && state?.run_id === plan.approval.run_id;
  const terminalRun = !!state && ['completed', 'failed', 'timed_out'].includes(state.status);
  const humanTotal =
    people.include === false ? 0 : (people.total ?? project.people.length);
  const submit = (answers?:Record<string,string>) =>
    act("요청 해석과 환경 검증 중", async () => {
      try {
        const p = await request<Plan>("/assistant/chat", "POST", {
          project,
          message: answers ? "화면에서 선택한 답변을 반영하고 다음 필요한 조건을 이어서 확인해주세요." : message,
          mode,
          version:plan?.version, answers:answers ?? {}, selection,
          plan_id: plan?.id,
        });
        accept(p);
        setMessage("");
      } finally {
        // Preserve the last accepted plan and the user's message on failure.
        // Refresh quota/cancellation status without replacing the chat error.
        void request<AssistantSettings>("/assistant/settings")
          .then(setSettings)
          .catch(() => {});
      }
    });
  const revise = () =>
    plan &&
    act("선택을 반영해 계획 갱신 중", async () =>
      accept(
        await request<Plan>(`/plans/${plan.id}/revise`, "POST", {
          version: plan.version,
          project,
          selection,
        }),
      ),
    );
  const chooseResolution = (resolution: OccupancyResolution) =>
    plan && act("계획 변경안 검증 중", async () =>
      accept(await request<Plan>(`/plans/${plan.id}/revise`, "POST", {
        version: plan.version,
        project,
        selection: {
          ...selection,
          robot_ids: resolution.kind === "reachable_zone" && resolution.robot_id
            ? [...new Set([...(selection.robot_ids ?? []), resolution.robot_id])]
            : selection.robot_ids,
          occupancy_resolution: resolution,
        },
      })),
    );
  const roleName = (id: string) =>
    project.robots.find((r) => r.id === id)?.name ?? id;
  const planHistoryGroups = Array.from(new Map(history.map((row) => [row.id, row.id])).keys())
    .map((id) => ({id, versions: history.filter((row) => row.id === id)
      .sort((a,b) => b.version-a.version)}));
  const historicalPlan = !!plan && history.some((row) => row.id === plan.id && row.version > plan.version);
  const planMapChanged = !!plan && !!plan.source_environment_id &&
    (plan.source_environment_id !== project.environment.id ||
      plan.source_environment_version !== project.environment.version);
  return (
    <section className="planning-workbench" aria-label="계획 도우미">
      <header className="planning-heading">
        <div>
          <span className="eyebrow">계획 · 검토 · 실행</span>
          <h2>계획 도우미</h2>
          <p>
            목표를 설명하고 구성을 선택하세요. 마지막 승인 후 새 실험이
            시작됩니다.
          </p>
        </div>
        <div className="planner-header-actions">
          {designerAvailable && <button disabled={!!busy} onClick={newScenario}>새 시나리오</button>}
          <button
            aria-expanded={ontologyOpen}
            onClick={() => setOntologyOpen((v) => !v)}
          >
            <BookOpen size={16} /> 로봇 기능·문서
          </button>
          <button
            aria-expanded={settingsOpen}
            onClick={() => setSettingsOpen((v) => !v)}
          >
            <Settings2 size={16} /> 모델 연결{" "}
            {settings?.configured ? "설정" : "필요"}
          </button>
        </div>
      </header>
      {error && (
        <div className="notice error" role="alert">
          {error}
        </div>
      )}
      {notice && (
        <div className="notice" role="status">
          {notice}
        </div>
      )}
      {busy && (
        <div className="notice" role="status">
          <span>{busy}…</span>
          {busy === "요청 해석과 환경 검증 중" && (
            <button
              disabled={cancelling}
              onClick={async () => {
                setCancelling(true);
                try {
                  const response = await request<{ cancelled: boolean }>(
                    "/assistant/cancel",
                    "POST",
                  );
                  setNotice(
                    response.cancelled
                      ? "모델 요청 취소를 전달했습니다. 저장한 계획과 실행은 유지됩니다."
                      : "현재 취소할 모델 요청이 없습니다. 도착한 응답을 확인하세요.",
                  );
                } catch (e) {
                  setError(textError(e));
                } finally {
                  setCancelling(false);
                }
              }}
            >
              <Square size={13} />{" "}
              {cancelling ? "취소 전달 중" : "모델 요청 취소"}
            </button>
          )}
        </div>
      )}
      {settingsOpen && (
        <CodexConnectionPanel
          settings={settings}
          onChange={setSettings}
          requestBusy={!!busy}
        />
      )}
      {ontologyOpen && (
        <OntologyPanel
          modelIds={[...new Set(project.robots.map((r) => r.model_id))]}
          focusDocumentId={focusedDocumentId}
          onChanged={() => {
            if (plan) setDirty(true);
          }}
        />
      )}
      <div className="planner-columns">
        <aside className="planner-chat">
          <div className="planner-chat-title">
            <MessageSquare size={18} />
            <strong>목표와 질문</strong>
            <span className={settings?.configured ? "" : "muted"}>
              {assistantStatusLabel(settings)}
            </span>
          </div>
          {!settings?.configured && (
            <div className="planner-empty">
              <strong>자연어 모델을 연결하세요</strong>
              <p>
                {settings?.personal_api ? "개인 OpenAI·Claude API 키를 연결하고 모델을 선택하세요. " : "ChatGPT 로그인 기반 Codex, Claude API 또는 다른 호환 모델을 선택하세요. "}
                연결하지 않아도 기존 작업 계획은 직접 구성할 수 있습니다.
              </p>
              <button onClick={() => setSettingsOpen(true)}>
                모델 연결 설정
              </button>
            </div>
          )}
          <div className="planner-messages" aria-live="polite" ref={messagesRef}>
            {plan?.conversation?.map((m, i) => (
              <article key={i} className={`planner-message ${m.role}`}>
                <small>
                  {m.role === "user" ? "사용자" : "계획 도우미 · 모델 제안"}
                </small>
                <p>{m.content}</p>
                <div className="planner-references">
                  {m.references?.map((id) => (
                    <button key={id} onClick={() => {
                      if (id.startsWith("document:")) {
                        setFocusedDocumentId(id.slice("document:".length));
                        setOntologyOpen(true);
                      } else focus(id);
                    }}>
                      {id.startsWith("document:") ? "문서 근거 열기" :
                        entities.find((e) => e.id === id)?.name ??
                        preview.tasks.find((t) => t.id === id)?.name ??
                        id}
                    </button>
                  ))}
                </div>
                {m.runtime_basis && <small>답변 근거: 시뮬레이션 {m.runtime_basis.sim_time.toFixed(2)}초의 실제 상태 · 실행 {m.runtime_basis.run_id.slice(0,8)}. 응답 이후의 상태는 관제 화면에서 확인하세요.</small>}
                {!!m.related_documents?.filter((document) => !m.references?.includes(`document:${document.id}`)).length &&
                  <div className="planner-references planner-related-documents">
                    <small>질문과 이름이 맞는 등록 문서 · 모델의 직접 인용은 아님</small>
                    {m.related_documents.filter((document) => !m.references?.includes(`document:${document.id}`))
                      .map((document) => <button key={document.id} onClick={() => {
                        setFocusedDocumentId(document.id); setOntologyOpen(true);
                      }}>{document.title} · {document.version}</button>)}
                  </div>}
              </article>
            ))}
            {!plan?.conversation?.length && (
              <p className="muted">
                “이 환경에서 배송하려면 어떤 로봇이 필요해?”
                <br />
                “사람이 10명 돌아다니는 상황으로 바꿔줘.”
              </p>
            )}
          </div>
          <form
            onSubmit={(e) => {
              e.preventDefault();
              void submit();
            }}
          >
            <label>
              요청 유형
              <select value={mode} onChange={(e) => setMode(e.target.value)}>
                {designerAvailable && <option value="design">대화로 복합 시나리오 구성</option>}
                <option value="auto">질문 / 계획 자동 구분</option>
                <option value="question">질문만 · 실행 초안 승인 불가</option>
                <option value="plan">작업 계획 요청</option>
              </select>
            </label>
            <label>
              한국어 질문 또는 지시
              <textarea
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="실제 장소와 물품을 포함해 목표를 설명하세요"
                rows={4}
                maxLength={12000}
              />
            </label>
            <button
              className="primary"
              disabled={
                !!busy || !connected || !message.trim() || !settings?.configured
              }
            >
              <Send size={15} /> 요청 보내기
            </button>
          </form>
          <details className="planner-manual">
            <summary>기존 작업으로 직접 계획</summary>
            <p>
              자연어 모델을 사용하지 않는 수동 구성입니다. 편집된 실제 작업을
              검증합니다.
            </p>
            <button
              disabled={!!busy || !project.tasks.length}
              onClick={() =>
                void act("기존 작업 계획 검증 중", async () =>
                  accept(
                    await request<Plan>("/plans", "POST", {
                      project,
                      intent: {
                        kind: "plan",
                        goal: "현재 편집 작업 실행",
                        tasks: project.tasks.map((t) => ({
                          existing_task_id: t.id,
                        })),
                      },
                      selection: {
                        pedestrians: {},
                        pedestrian_avoidance:
                          project.policy.pedestrian_avoidance ??
                          defaultAvoidance,
                      },
                    }),
                  ),
                )
              }
            >
              현재 작업으로 계획
            </button>
          </details>
          <div className="planner-history" aria-label="저장한 계획 기록">
            <div className="planner-history-heading"><strong>저장한 계획 기록</strong><span>{history.length}개 버전</span></div>
            {planHistoryGroups.length === 0 ? <p>저장한 계획이 없습니다. 질문하거나 작업을 지시해 시작하세요.</p> :
              planHistoryGroups.map((group) => <details key={group.id}>
                <summary>{group.versions[0].intent.goal} · {group.versions.length}개 버전</summary>
                {group.versions.map((row) => <div className="planner-history-row" key={`${row.id}-${row.version}`}>
                  <span>v{row.version} · {row.recovered_from ? "이전 검증 기록" : "앱 저장"}</span>
                  <button type="button" disabled={!!busy} onClick={() => void act("계획 기록 열기", async () =>
                    accept(await request<Plan>(`/plans/${row.id}/versions/${row.version}`)))}>열기</button>
                </div>)}
              </details>)}
          </div>
        </aside>
        <div className="planner-main">
          {designerAvailable && (mode === 'design' || plan?.intent.scenario) && <ScenarioDraftPanel
            draft={plan?.intent.scenario} tasks={plan?.intent.tasks??[]} steps={plan?.compiled.steps??[]} project={preview}
            version={plan?.version} busy={!!busy} dirty={dirty} selectedPlace={selected}
            onAnswer={answers=>void submit(answers)} onSave={()=>void revise()} onReviewMap={onReviewMap} onReference={id=>{if(id.startsWith('document:')){setFocusedDocumentId(id.slice(9));setOntologyOpen(true);}else focus(id);}}
            onDestination={(taskId,placeId)=>{if(plan)void act('목적지 변경과 경로 재검증 중',async()=>accept(await request<Plan>(`/plans/${plan.id}/scenario`,'POST',{
              version:plan.version,project,selection,task_id:taskId,destination_id:placeId,
            })));}} />}

          {plan?.input_receipt && <details className="scenario-input-receipt"><summary>모델에 전달한 기준 정보</summary>
            <p>지도 v{plan.input_receipt.map_version} · {plan.input_receipt.model_execution?.provider??'응답 연결 기록 없음'} / {plan.input_receipt.model_execution?.model??'모델 확인 필요'}</p>
            {plan.input_receipt.project_hash!==plan.source_project_hash && <p>이후 화면에서 구성이 바뀌었습니다. 마지막 모델 입력과 현재 초안이 다릅니다.</p>}
            <p>요청 당시 환경·로봇·물품·선택 구성, 문서 능력 및 공간 근거를 함께 전달했습니다. 답변 내용은 별도로 실행 검증합니다.</p>
            <small>구성 식별값 {plan.input_receipt.project_hash.slice(0,12)} · 근거 식별값 {plan.input_receipt.ontology_hash.slice(0,12)}</small>
          </details>}
          {designerAvailable && <ScenarioSampleForm onUse={async next=>{await onUseScenarioProject(next);newScenario();}} onEdit={onReviewMap}/>}
          <div className="planner-map-heading">
            <strong>
              {livePlan && tab === "results"
                ? "승인한 실행 · 실제 관측"
                : plan
                  ? "실행 구성 미리보기"
                  : "현재 편집 환경"}
            </strong>
            <span>
              {preview.robots.length}대 · 보행자 {preview.people.length}명
            </span>
            <select
              aria-label="계획 미리보기 층"
              value={floor}
              onChange={(e) => setFloor(e.target.value)}
            >
              {preview.environment.floors.map((f) => (
                <option key={f.id} value={f.id}>
                  {f.name}
                </option>
              ))}
            </select>
          </div>
          <div className="planner-map">
            <PlanView
              planningPreview={!livePlan || tab !== "results"}
              previewRoutes={plan?.compiled.preview?.routes ?? []}
              project={preview}
              state={livePlan && tab === "results" ? state : null}
              floorId={floor}
              selected={selected}
              onSelect={focus}
              editing={false}
              tool={null}
              onPlace={() => {}}
              onMove={() => {}}
            />
          </div>
          {entity && (
            <div className="planner-reference-detail">
              <strong>{entity.name}</strong>
              <span>
                {
                  preview.environment.floors.find(
                    (f) => f.id === entity.floor_id,
                  )?.name
                }{" "}
                · 미리보기 선택
              </span>
              <button onClick={() => onObserve(entity.id)}>
                현재 실행에서 관찰
              </button>
            </div>
          )}
          {!plan ? (
            <div className="planner-empty">
              <h3>목표를 입력하면 검토할 계획이 여기에 표시됩니다</h3>
              <p>
                지도와 로봇 능력, 필요한 협업을 확인한 뒤 구성과 단계가
                표시됩니다. 이 화면의 미리보기는 실행 상태를 바꾸지 않습니다.
              </p>
            </div>
          ) : (
            <>
              <div className="planner-plan-title">
                <div>
                  <small>
                    {plan.origin === "model"
                      ? "자연어 모델 제안 · 시스템 검증"
                      : "기존 작업 수동 계획 · 자연어 미사용"}{" "}
                    · 버전 {plan.version}
                  </small>
                  {plan.source_environment_name && (
                    <small>기준 지도 {plan.source_environment_name} v{plan.source_environment_version ?? "—"}
                      {plan.source_project_revision ? ` · 구성 v${plan.source_project_revision}` : ""}</small>
                  )}
                  <h3>{plan.compiled.goal}</h3>
                </div>
                <strong
                  className={
                    plan.compiled.can_approve
                      ? "planner-ready"
                      : "planner-blocked"
                  }
                >
                  {plan.approval
                    ? "승인한 실행"
                    : (statusNames[plan.compiled.status] ??
                      plan.compiled.status)}
                </strong>
              </div>
              {plan.compiled.spatial_ontology?.limits?.filter((line) => line.includes("미검토 후보")).map((line) => (
                <div className="notice" key={line} role="status">
                  <span>{line}. 현재 계획은 확정된 공간과 출입구 안에서만 경로를 검증합니다.</span>
                  <button type="button" onClick={onReviewMap}>지도 검토 계속</button>
                </div>
              ))}
              {!!plan.compiled.spatial_ontology?.scale_basis?.length &&
                <div className="notice" role="status">
                  <span>지도 길이의 근거: {[...new Set(plan.compiled.spatial_ontology.scale_basis.map((basis) =>
                    basis.startsWith("사용자 보정:") ? basis.replace("사용자 보정:", "기존 입력 · 출처 미확인(실측 아님):") : basis
                  ))].join(" · ")}</span>
                  <button type="button" onClick={onReviewMap}>원본·축척 확인</button>
                </div>}
              {[...plan.compiled.blockers, ...plan.compiled.clarifications]
                .length > 0 && (
                <ul className="planner-problems">
                  {[
                    ...plan.compiled.blockers,
                    ...plan.compiled.clarifications,
                  ].map((issue, i) => (
                    <li key={i}>
                      <strong>{issueText(issue.message)}</strong>
                      {issue.suggestion && <p>{issue.suggestion}</p>}
                      {issue.resolution_options?.map((option, index) => (
                        <button key={index} type="button" disabled={!!busy}
                          onClick={() => void chooseResolution(option)}>
                          {option.label} · 변경안 계산
                        </button>
                      ))}
                    </li>
                  ))}
                </ul>
              )}
              {plan.compiled.occupancy_resolution && (
                <div className="notice" role="status">
                  계획 변경안: {plan.compiled.occupancy_resolution.label}. 원래 요청에서 달라진 장소와 작업 범위를 확인한 뒤 새 버전을 승인하세요.
                </div>
              )}
              <div
                className="planner-tabs"
                role="tablist"
                aria-label="계획 구성"
              >
                {[
                  ["robots", "로봇 구성"],
                  ["people", "보행자와 회피"],
                  ["steps", "작업 단계"],
                  ["evidence", "기능 근거"],
                  ["results", "실행 결과"],
                ].map(([id, label]) => (
                  <button
                    key={id}
                    role="tab"
                    aria-selected={tab === id}
                    onClick={() => setTab(id)}
                  >
                    {label}
                  </button>
                ))}
              </div>
              {tab === "evidence" && (
                <PlanOntologyEvidence ontology={plan.compiled.ontology} />
              )}
              {tab === "robots" && (
                <div className="planner-options">
                  <h4>필수 능력과 최소 구성</h4>
                  {plan.compiled.requirements.map((r) => (
                    <div className="planner-requirement" key={r.id}>
                      <strong>
                        {roleNames[r.capability] ?? r.capability} · 최소{" "}
                        {r.min_count}대
                      </strong>
                      <span>{r.reason}</span>
                      <small>
                        가능한 구성:{" "}
                        {r.eligible_robot_ids.map(roleName).join(" / ") ||
                          "없음"}
                      </small>
                      {(r.alternative_robot_ids ?? r.eligible_robot_ids).length > 1 && (
                        <label>
                          동등 능력 로봇으로 교체
                          <select
                            value={
                              selection.task_robot_ids?.[r.task_id] ??
                              plan.compiled.steps.find((step) => step.id === r.task_id)?.robot_ids[0] ??
                              r.eligible_robot_ids.find((id) =>
                                selectedRobots.includes(id),
                              ) ?? ""
                            }
                            onChange={(e) => {
                              const change = swapPlanningRobot(
                                selectedRobots,
                                plan.compiled.requirements,
                                r.id,
                                e.target.value,
                                plan.compiled.steps.find((step) => step.id === r.task_id)?.robot_ids[0],
                              );
                              if (change.robotIds.includes(e.target.value))
                                patch({
                                  robot_ids: change.robotIds,
                                  task_robot_ids: {
                                    ...selection.task_robot_ids,
                                    [r.task_id]: e.target.value,
                                  },
                                });
                              if (change.reason) setNotice(change.reason);
                            }}
                          >
                            <option value="" disabled>
                              선택 필요
                            </option>
                            {(r.alternative_robot_ids ?? r.eligible_robot_ids).map((id) => (
                              <option key={id} value={id}>
                                {roleName(id)}
                              </option>
                            ))}
                          </select>
                        </label>
                      )}
                    </div>
                  ))}
                  <h4>참여 로봇 · {selectedRobots.length}대</h4>
                  {plan.compiled.robot_options.map((r) => {
                    const checked = selectedRobots.includes(r.id);
                    const required = !canRemovePlanningRobot(
                      selectedRobots,
                      plan.compiled.requirements,
                      r.id,
                    );
                    return (
                      <label className="planner-robot" key={r.id}>
                        <input
                          type="checkbox"
                          checked={checked}
                          disabled={required || !!busy || (!checked && r.eligible_for.length === 0)}
                          onChange={(e) =>
                            patch({
                              robot_ids: e.target.checked
                                ? [...selectedRobots, r.id]
                                : selectedRobots.filter((id) => id !== r.id),
                            })
                          }
                        />
                        <span>
                          <strong>
                            {r.name} <small>{r.model_id}</small>
                          </strong>
                          <span>
                            {required ? (
                              <>
                                <Lock size={12} /> 필수 조건 유지 · 대체 로봇을
                                먼저 선택하세요
                              </>
                            ) : (
                              r.reason
                            )}
                          </span>
                          <small>
                            {r.available
                              ? "초기 조건에서 사용 가능"
                              : String(
                                  r.availability_reason ?? "사용 불가",
                                )}{" "}
                            · 역할: {r.roles.map(id=>plan.compiled.steps.find(s=>s.id===id)?.name??id).join(", ") || (r.eligible_for.length ? "미배정" : "배정 불가")}
                          </small>
                          {r.task_rejections?.flatMap((rejection) =>
                            rejection.blockers.map((blocker) => (
                              <small className="planner-robot-rejection" key={`${rejection.task_id}-${blocker.code}`}>
                                {plan.compiled.steps.find(s=>s.id===rejection.task_id)?.name??'다른 업무 후보'} 제외: {blocker.message}
                              </small>
                            )),
                          )}
                        </span>
                        <button type="button" onClick={() => focus(r.id)}>
                          지도
                        </button>
                      </label>
                    );
                  })}
                  {plan.compiled.recommendations.length > 0 && (
                    <>
                      <h4>효율 개선 추천 · 측정 전 추정</h4>
                      {plan.compiled.recommendations.map((r) => (
                        <p key={r.robot_id}>
                          {roleName(r.robot_id)} — {r.comparison}. {r.reason}
                        </p>
                      ))}
                    </>
                  )}
                </div>
              )}
              {tab === "people" && (
                <div className="planner-options">
                  {Object.keys(people).length === 0 && (
                    <p className="notice">
                      편집 원본의 개별 보행자 행동과 경로를 보존합니다. 아래
                      옵션을 바꾸면 이번 실행의 공통 설정으로 계산합니다.
                    </p>
                  )}
                  <div className="planner-people-heading">
                    <Users size={18} />
                    <strong>이번 실행 총 {humanTotal}명</strong>
                    <span>편집 원본 {project.people.length}명 보존</span>
                  </div>
                  <label className="check">
                    <input
                      type="checkbox"
                      checked={people.include !== false}
                      onChange={(e) =>
                        patchPeople({ include: e.target.checked })
                      }
                    />{" "}
                    보행자 포함
                  </label>
                  <div className="planner-presets">
                    {[
                      [0, "없음"],
                      [3, "적음"],
                      [10, "보통"],
                      [20, "많음"],
                    ].map(([n, label]) => (
                      <button
                        key={n}
                        onClick={() =>
                          patchPeople({
                            include: Number(n) > 0,
                            total: Number(n),
                            behavior: behaviorDefaults,
                          })
                        }
                      >
                        {label} · {n}명
                      </button>
                    ))}
                  </div>
                  <p className="muted">
                    프리셋: 자유 배회 · 0.5~1.2 m/s · 평균 정지 빈도 0.08회/s.
                    실제 인원과 배치는 갱신 후 지도에서 확인하세요.
                  </p>
                  <div className="planner-fields">
                    <label>
                      총 보행자 수 (명)
                      <input
                        type="number"
                        min={0}
                        max={200}
                        value={people.total ?? project.people.length}
                        onChange={(e) =>
                          patchPeople({ total: Number(e.target.value) })
                        }
                      />
                    </label>
                    <label>
                      재현 시드
                      <input
                        type="number"
                        min={0}
                        max={4294967295}
                        value={people.seed ?? project.physics.seed}
                        onChange={(e) =>
                          patchPeople({ seed: Number(e.target.value) })
                        }
                      />
                    </label>
                  </div>
                  <fieldset>
                    <legend>이동 가능한 층</legend>
                    {project.environment.floors.map((f) => (
                      <label key={f.id} className="check">
                        <input
                          type="checkbox"
                          checked={(
                            people.allowed_floor_ids ??
                            project.environment.floors.map((x) => x.id)
                          ).includes(f.id)}
                          onChange={(e) => {
                            const ids =
                              people.allowed_floor_ids ??
                              project.environment.floors.map((x) => x.id);
                            patchPeople({
                              allowed_floor_ids: e.target.checked
                                ? [...ids, f.id]
                                : ids.filter((id) => id !== f.id),
                            });
                          }}
                        />
                        {f.name}
                      </label>
                    ))}
                    <small>
                      각 보행자는 배치한 층 안에서 이동합니다. 보행자 층간
                      이동은 지원하지 않습니다.
                    </small>
                  </fieldset>
                  <details>
                    <summary>초기 배치와 이동 구역 선택</summary>
                    <p>
                      선택하지 않으면 허용 층의 통행 가능 공간을 사용합니다.
                    </p>
                    {project.environment.elements
                      .filter((e) =>
                        [
                          "room",
                          "corridor",
                          "waiting",
                          "entrance",
                          "loading",
                        ].includes(e.kind),
                      )
                      .map((e) => (
                        <label className="check" key={e.id}>
                          <input
                            type="checkbox"
                            checked={(people.zone_ids ?? []).includes(e.id)}
                            onChange={(v) =>
                              patchPeople({
                                zone_ids: v.target.checked
                                  ? [...(people.zone_ids ?? []), e.id]
                                  : (people.zone_ids ?? []).filter(
                                      (id) => id !== e.id,
                                    ),
                              })
                            }
                          />
                          {e.name}
                        </label>
                      ))}
                  </details>
                  <details>
                    <summary>보행자 행동 상세</summary>
                    <label>
                      행동 유형
                      <select
                        value={people.behavior?.mode ?? "free_roam"}
                        onChange={(e) =>
                          patchPeople({
                            behavior: {
                              ...people.behavior,
                              mode: e.target
                                .value as PedestrianBehavior["mode"],
                            },
                          })
                        }
                      >
                        <option value="free_roam">자유 배회</option>
                        <option value="destinations">여러 목적지 이동</option>
                        <option value="route">지정 경로</option>
                      </select>
                    </label>
                    <div className="planner-fields">
                      {(
                        [
                          ["speed_min_m_s", "최저 속도 (m/s)"],
                          ["speed_max_m_s", "최고 속도 (m/s)"],
                          ["stop_rate_per_s", "정지 빈도 (회/s)"],
                          ["stop_duration_min_s", "최소 정지 시간 (s)"],
                          ["stop_duration_max_s", "최대 정지 시간 (s)"],
                          [
                            "destination_change_rate_per_s",
                            "방향·목적지 변경 (회/s)",
                          ],
                          ["crossing_rate_per_s", "진행 경로 횡단 (회/s)"],
                        ] as const
                      ).map(([k, label]) => (
                        <label key={k}>
                          {label}
                          <input
                            type="number"
                            min={0}
                            step="0.05"
                            value={people.behavior?.[k] ?? behaviorDefaults[k]}
                            onChange={(e) =>
                              patchPeople({
                                behavior: {
                                  ...people.behavior,
                                  [k]: Number(e.target.value),
                                },
                              })
                            }
                          />
                        </label>
                      ))}
                    </div>
                    <fieldset>
                      <legend>여러 목적지 · 실제 지도 위치</legend>
                      {project.environment.elements
                        .filter((e) =>
                          [
                            "room",
                            "corridor",
                            "waiting",
                            "entrance",
                            "loading",
                          ].includes(e.kind),
                        )
                        .map((e) => {
                          const checked = (
                            people.behavior?.destinations ?? []
                          ).some((p) => p.x === e.pose.x && p.y === e.pose.y);
                          return (
                            <label className="check" key={e.id}>
                              <input
                                type="checkbox"
                                checked={checked}
                                onChange={(v) =>
                                  patchPeople({
                                    behavior: {
                                      ...people.behavior,
                                      destinations: v.target.checked
                                        ? [
                                            ...(people.behavior?.destinations ??
                                              []),
                                            e.pose,
                                          ]
                                        : (
                                            people.behavior?.destinations ?? []
                                          ).filter(
                                            (p) =>
                                              p.x !== e.pose.x ||
                                              p.y !== e.pose.y,
                                          ),
                                    },
                                  })
                                }
                              />
                              {e.name}
                            </label>
                          );
                        })}
                    </fieldset>
                    <p>
                      지정 경로는 편집 원본의 경유점을 보존합니다. 새 보행자에게
                      경로가 없거나 목적지가 도달 불가능하면 승인할 수 없습니다.
                    </p>
                  </details>
                  <details open>
                    <summary>로봇의 사람 회피 정책</summary>
                    {!selection.pedestrian_avoidance &&
                      !project.policy.pedestrian_avoidance && (
                        <p>
                          <strong>
                            상세 회피 정책 미적용 · 기존 안전 제어 사용 중
                          </strong>
                          <button
                            onClick={() =>
                              patch({ pedestrian_avoidance: defaultAvoidance })
                            }
                          >
                            표시된 회피 정책 적용
                          </button>
                        </p>
                      )}
                    <p>
                      단순화된 사람 추적 관측에 가림·센서 지연·잡음·누락을
                      적용합니다. 아래 거리는 외형 경계 사이 거리이며 제동·지연
                      여유를 추가합니다.
                    </p>
                    <div className="planner-fields">
                      {[
                        ["desired_clearance_m", "목표 간격 (m)"],
                        ["slowdown_distance_m", "감속 시작 (m)"],
                        ["stop_distance_m", "정지 간격 (m)"],
                        ["resume_distance_m", "재출발 간격 (m)"],
                        ["max_near_speed_m_s", "근접 최대 속도 (m/s)"],
                        ["replan_after_s", "재계획 대기 (s)"],
                        ["blocked_timeout_s", "차단 종료 기준 (s)"],
                        ["observation_range_m", "사람 관측 범위 (m)"],
                        ["braking_deceleration_m_s2", "제동 감속도 (m/s²)"],
                      ].map(([k, label]) => (
                        <label key={k}>
                          {label}
                          <input
                            type="number"
                            min={0}
                            step="0.05"
                            value={
                              selection.pedestrian_avoidance?.[k] ??
                              project.policy.pedestrian_avoidance?.[k] ??
                              defaultAvoidance[
                                k as keyof typeof defaultAvoidance
                              ]
                            }
                            onChange={(e) =>
                              patch({
                                pedestrian_avoidance: {
                                  ...defaultAvoidance,
                                  ...project.policy.pedestrian_avoidance,
                                  ...selection.pedestrian_avoidance,
                                  [k]: Number(e.target.value),
                                },
                              })
                            }
                          />
                        </label>
                      ))}
                      <label>
                        차단 대응
                        <select
                          value={
                            selection.pedestrian_avoidance?.strategy ??
                            project.policy.pedestrian_avoidance?.strategy ??
                            "detour"
                          }
                          onChange={(e) =>
                            patch({
                              pedestrian_avoidance: {
                                ...defaultAvoidance,
                                ...project.policy.pedestrian_avoidance,
                                ...selection.pedestrian_avoidance,
                                strategy: e.target.value,
                              },
                            })
                          }
                        >
                          <option value="yield">양보·대기</option>
                          <option value="detour">양보 후 우회 시도</option>
                        </select>
                      </label>
                    </div>
                  </details>
                  <p>
                    계산된 구성: 원본 유지{" "}
                    {plan.compiled.pedestrians.retained_count ?? 0}명 + 추가{" "}
                    {plan.compiled.pedestrians.added_count ?? 0}명 = 실제 실행{" "}
                    {plan.compiled.pedestrians.total ?? 0}명
                  </p>
                  {!!plan.compiled.pedestrians.excluded_nested_zones?.length && (
                    <p role="status">
                      허용 구역 안의 별도 공간도 자동 출입하지 않습니다: {plan.compiled.pedestrians.excluded_nested_zones.map((zone) => zone.name).join(", ")}. 이 공간을 허용하려면 보행자 구역에 직접 추가하고 계획을 다시 검토하세요.
                    </p>
                  )}
                </div>
              )}
              {tab === "steps" && (
                <div className="planner-options">
                  {plan.compiled.execution_policy && <p>{plan.compiled.execution_policy.basis}</p>}
                  <ol className="planner-steps">
                    {plan.compiled.steps.map((s) => {
                      const task = plan.compiled.project?.tasks.find((item) => item.id === s.id);
                      const taskName = task && s.name.endsWith(` ${task.kind}`)
                        ? `${s.name.slice(0, -(task.kind.length + 1))} ${roleNames[task.kind] ?? task.kind}`
                        : s.name;
                      const floorName = plan.compiled.project?.environment.floors.find((item) => item.id === s.floor_id)?.name ?? s.floor_id;
                      return <li key={s.id}>
                        <h4>{taskName}</h4>
                        <div className="planner-references">
                          {s.robot_ids.map((id) => (
                            <button key={id} onClick={() => focus(id)}>
                              {roleName(id)}
                            </button>
                          ))}
                          {s.item_id && (
                            <button onClick={() => focus(s.item_id!)}>
                              대상 물품
                            </button>
                          )}
                        </div>
                        <p>
                          {s.dependencies.length
                            ? `선행 작업: ${s.dependencies.map(id=>plan.compiled.steps.find(step=>step.id===id)?.name??id).join(", ")}`
                            : "즉시 시작 가능"}{" "}
                          · {floorName} · 목적지 ({s.destination.x.toFixed(1)},{" "}
                          {s.destination.y.toFixed(1)}) m
                        </p>
                        <p>
                          공용 자원:{" "}
                          {s.resources.map(id=>{const key=id.split(':').slice(1).join(':')||id;return plan.compiled.project?.environment.elements.find(e=>e.id===key)?.name??plan.compiled.project?.items.find(i=>i.id===key)?.name??key;}).join(", ") ||
                            "경로 검사상 추가 자원 없음"}
                        </p>
                        {s.trip && <p>적재 승강기 이동: {plan.compiled.project?.environment.floors.find(f=>f.id===s.trip!.source_floor)?.name} → {floorName} · {plan.compiled.project?.environment.elements.find(e=>e.id===s.trip!.elevator_id)?.name} · 로봇·장비·물품 합계 {s.trip.mass.toFixed(1)} kg</p>}
                        {s.roles?.carrier_id && <p>물품 흐름: {s.roles.donor_id?`${roleName(s.roles.donor_id)} 파지·상차 → `:'초기 적재 확인 → '}{roleName(s.roles.carrier_id)} 지지 운반 → {roleName(s.roles.receiver_id??'')} 파지·배치 · 접촉·지지·해제·후퇴 관측으로 완료</p>}
                        {!!s.parallel_with?.length && <p>병행 가능: {s.parallel_with.map(id=>plan.compiled.steps.find(t=>t.id===id)?.name??id).join(', ')}</p>}
                        {task && (
                          <p>
                            작업 조건: 목적지 체류 {task.dwell}초 · 제한 시간 {task.timeout}초
                          </p>
                        )}
                        {s.spatial_review?.status === "validated" && (
                          <p>
                            검토 도면 경로 확인 · 필요 통과 폭 {s.spatial_review.required_width_m.toFixed(2)} m ·{" "}
                            {s.spatial_review.reviewed_apertures.length
                              ? s.spatial_review.reviewed_apertures.map((a) =>
                                  `${a.name} (${a.kind === "reviewed_opening" ? "개방 통로" : "문"}, ${a.width_m.toFixed(2)} m)`
                                ).join(" → ")
                              : "한 공간 안에서 이동"}
                          </p>
                        )}
                        {s.condition && <p>승인된 분기: {plan.compiled.steps.find(step=>step.id===s.condition!.task_id)?.name??s.condition.task_id} {s.condition.outcome==='completed'?'완료':'최종 실패'} 시에만 실행</p>}
                        {s.confirmation && <p>현장 확인: {s.confirmation.label} · {s.confirmation.criterion} · 확인 대기 한도 {s.confirmation.timeout_s}초</p>}
                        <small>{s.failure_behavior}</small>
                      </li>;
                    })}
                  </ol>
                  {!plan.compiled.steps.length && (
                    <p>아직 실행할 작업 단계가 없습니다.</p>
                  )}
                  <details>
                    <summary>검증 근거와 가정</summary>
                    <ul>
                      {plan.compiled.assumptions.map((a, i) => (
                        <li key={i}>{a}</li>
                      ))}
                    </ul>
                  </details>
                  <button
                    onClick={() => downloadJSON("검토할-계획.json", plan)}
                  >
                    계획 데이터 내보내기
                  </button>
                </div>
              )}
              {tab === "results" && (
                <div className="planner-options">
                  {!plan.approval ? (
                    <p>현재 계획 v{plan.version}은 승인 전입니다. 이전에 승인한 실행은 아래에서 확인할 수 있습니다.</p>
                  ) : (
                    <>
                      <p>
                        실행 {plan.approval.run_id.slice(0, 8)} ·{" "}
                        {livePlan
                          ? `${state?.sim_time.toFixed(2)}초 · ${stopped && !terminalRun?'사용자 중단 · 마지막 관측 상태 보존':runNames[state?.status ?? ""] ?? state?.status}`
                          : "현재 관제와 다른 실행 · 저장 결과 확인"}
                      </p>
                      {livePlan && state && (
                        <>
                          <p>
                            작업 완료{" "}
                            {
                              state.tasks.filter(
                                (t) => t.status === "completed",
                              ).length
                            }{" "}
                            / {state.tasks.length} · 실제 보행자{" "}
                            {Object.keys(state.people ?? {}).length}명
                          </p>
                          <p>
                            물리 접촉 {String(state.metrics.collisions ?? "—")}건 ·
                            근접 사건 {String(state.metrics.near_misses ?? "—")}
                            건 · 실패 작업 {String(state.metrics.failed ?? "—")}
                            건
                          </p>
                          <p>물리 접촉에는 물품을 잡거나 적재 상태로 지지한 접촉도 포함됩니다. 근접 사건은 별도 기록하며 삭제하지 않습니다.</p>
                          {measuredPedestrianClearance(state.metrics) !== null && <p>로봇–보행자 최소 분리거리 {measuredPedestrianClearance(state.metrics)!.toFixed(3)} m · 물리 계산 단계 계측</p>}
                          {state.tasks.map((t) => (
                            <p key={t.id}>
                              {t.name ?? t.id} · {taskStatusLabel(t.status)} ·{" "}
                              {String(t.reason ?? "")}
                            </p>
                          ))}
                          {state.tasks.filter(t=>t.status==='running' && t.confirmation_requested_at!=null && !t.confirmation_receipt).map(t=>{
                            const confirmation=plan.compiled.steps.find(s=>s.id===t.id)?.confirmation;
                            return confirmation && <ConfirmationControl key={t.id} label={confirmation.label} criterion={confirmation.criterion}
                              disabled={!!busy||state.status!=='running'||stopped||dirty} onConfirm={note=>void act('현장 확인 기록 중',async()=>{
                                await request(`/plans/${plan.id}/confirm`,'POST',{run_id:state.run_id,version:plan.approval?.version,task_id:t.id,note});
                                setNotice('확인 내용을 기록했습니다. 도착·정지 상태를 다시 관측한 뒤 다음 단계로 진행합니다.');
                              })}/>;
                          })}
                          {state.robots.map(robot=>{
                            const next=plan.compiled.steps.filter(s=>s.robot_ids.includes(robot.id)&&!['completed','failed','cancelled','skipped'].includes(state.tasks.find(t=>t.id===s.id)?.status??'pending')&&s.id!==robot.task_id);
                            return <p key={robot.id}>{robot.name} · 현재 {state.tasks.find(t=>t.id===robot.task_id)?.name??'작업 대기'} · 다음 {next[0]?.name??'없음'} · {robot.reason}</p>;
                          })}
                          {!!state.items?.length && <div><strong>물품 상태 · 시뮬레이션 물리 관측</strong>{state.items.map(item=><p key={item.id}>{item.name} · 위치 {item.position.map(x=>x.toFixed(2)).join(', ')} m · 담당 {roleName(item.owner??'')||'소유 미확인/해제'} · {item.custody}{item.damaged?' · 손상 관측':''}</p>)}</div>}
                          <p>위 비율은 완료한 단계 수 기준이며 남은 시간 예측이 아닙니다.</p>
                          <div className="planner-actions">
                            <button
                              disabled={
                                !connected ||
                                !!busy ||
                                stopped ||
                                ['completed','failed','timed_out'].includes(state.status) ||
                                result?.live === false
                              }
                              onClick={() =>
                                void act("실행 제어 중", async () => {
                                  await request(
                                    `/plans/${plan.id}/control`,
                                    "POST",
                                    {
                                      run_id: plan.approval?.run_id,
                                      action:
                                        state.status === "running"
                                          ? "pause"
                                          : "resume",
                                    },
                                  );
                                })
                              }
                            >
                              <Pause size={15} />
                              {state.status === "running"
                                ? "일시 정지"
                                : "재개"}
                            </button>
                            <button
                              disabled={
                                !connected ||
                                !!busy ||
                                stopped ||
                                result?.live === false
                              }
                              onClick={() =>
                                void act(
                                  terminalRun ? "종료 기록 저장 중" : "실험 중단과 기록 저장 중",
                                  async () => {
                                    await request(
                                      `/plans/${plan.id}/stop`,
                                      "POST",
                                      { run_id: plan.approval?.run_id },
                                    );
                                    setStopped(true);
                                    setNotice(
                                      terminalRun ? "종료 상태와 전체 실행 기록을 저장했습니다." : "실험을 중단하고 실제 기록을 저장했습니다. 미완료 작업은 그대로 남습니다.",
                                    );
                                  },
                                )
                              }
                            >
                              <Square size={15} />
                              {terminalRun ? '종료 기록 저장' : '중단'}
                            </button>
                          </div>
                        </>
                      )}
                      <button
                        onClick={() =>
                          void act("실행 결과 확인 중", async () =>
                            setResult(
                              await request<StoredResult>(
                                `/plans/${plan.id}/result`,
                              ),
                            ),
                          )
                        }
                      >
                        저장 결과 확인
                      </button>
                    </>
                  )}
                  {!!plan.previous_approvals?.length && (
                    <div className="planner-history-results">
                      <strong>이전 승인 실행</strong>
                      {plan.previous_approvals.slice().reverse().map((approval) => (
                        <button key={approval.run_id} onClick={() =>
                          void act("이전 실행 결과 확인 중", async () =>
                            setResult(await request<StoredResult>(
                              `/plans/${plan.id}/runs/${approval.run_id}`,
                            )),
                          )
                        }>
                          계획 v{approval.version} · 실행 {approval.run_id.slice(0, 8)} 결과 보기
                        </button>
                      ))}
                    </div>
                  )}
                  {result !== null && (
                    <>
                      <p>
                        {result.approval ? `승인 계획 v${result.approval.version} · 실행 ${result.approval.run_id.slice(0, 8)}` : "저장 실행"}
                        {result.current_plan_version && result.approval?.version !== result.current_plan_version
                          ? ` · 현재 검토 계획 v${result.current_plan_version}과 별도` : ""}
                      </p>
                      {result.result ? (
                        <>
                          <p>
                            저장된 실제 기록 · {result.result.snapshot.sim_time.toFixed(2)} 시뮬레이션 초 · 완료{" "}
                            {String(result.result.snapshot.metrics.completed ?? 0)} / {result.result.snapshot.tasks.length} · 물리 접촉{" "}
                            {String(result.result.snapshot.metrics.collisions ?? 0)}건 · 근접{" "}
                            {String(result.result.snapshot.metrics.near_misses ?? 0)}건
                          </p>
                          {measuredPedestrianClearance(result.result.snapshot.metrics) !== null &&
                            <p>로봇–보행자 최소 분리거리 {measuredPedestrianClearance(result.result.snapshot.metrics)!.toFixed(3)} m · 물리 계산 단계 계측</p>}
                        </>
                      ) : <p>이 승인 실행의 저장 결과가 없습니다. 실행 상태와 기록 저장 여부를 확인하세요.</p>}
                      <details>
                        <summary>실행 기록 원본과 계측 상세</summary>
                        <pre className="planner-result">{JSON.stringify(result, null, 2)}</pre>
                      </details>
                      <button onClick={() => downloadJSON("승인-실험-결과.json", result)}>
                        실행 결과 내보내기
                      </button>
                    </>
                  )}
                </div>
              )}
              <footer className="planner-approval">
                <div>
                  <strong>
                    {dirty
                      ? "선택 변경 · 다시 계산 필요"
                      : plan.approval
                        ? livePlan && !terminalRun ? "실행 요청 수락됨" : "이전 승인 실행 · 결과 보존됨"
                        : plan.compiled.kind === "question"
                          ? "질문은 실행되지 않습니다"
                          : `검토한 버전 ${plan.version} 승인`}
                  </strong>
                  <small>
                    {plan.approval && (!livePlan || terminalRun)
                      ? "다시 실행 준비 → 구성 검토 → 승인하면 처음부터 새 실행을 시작합니다."
                      : "편집 초기 배치로 새 실험 시작 · 진행 중인 실행은 먼저 일시 정지"}
                  </small>
                </div>
                {(historicalPlan || planMapChanged) && <button disabled={!!busy} onClick={() => void act("저장된 지시로 새 계획 계산 중", async () => {
                  accept(await request<Plan>("/plans", "POST", {project, intent: plan.intent, selection}));
                  setNotice("이전 지시를 현재 구성에서 다시 검증한 새 계획입니다. 모델을 다시 호출한 결과는 아닙니다. 승인 전 내용을 확인하세요.");
                })}>이전 지시로 새 계획 만들기</button>}
                <button disabled={!!busy || historicalPlan || planMapChanged} onClick={() => void revise()}>
                  <RefreshCw size={15} />
                  {plan.approval && !dirty && (!livePlan || terminalRun) ? "다시 실행 준비" : "계획 갱신"}
                </button>
                <button
                  className="primary"
                  disabled={
                    !!busy ||
                    dirty ||
                    historicalPlan ||
                    planMapChanged ||
                    !plan.compiled.can_approve ||
                    !!plan.approval ||
                    !connected ||
                    !['paused', 'completed', 'failed', 'timed_out'].includes(state?.status ?? '')
                  }
                  onClick={() =>
                    void act("승인한 계획 실행 요청 중", async () => {
                      requestId.current ??= crypto.randomUUID();
                      const receipt = await request<{ run_id: string }>(
                        `/plans/${plan.id}/approve`,
                        "POST",
                        {
                          version: plan.version,
                          plan_hash: plan.plan_hash,
                          source_project_hash: plan.source_project_hash,
                          project,
                          request_id: requestId.current,
                        },
                      );
                      setPlan({ ...plan, approval: { ...receipt, version: plan.version } });
                      setTab("results");
                      setNotice(
                        "실행 요청을 수락했습니다. 물리 작업 완료 여부는 실제 결과로 확인합니다.",
                      );
                    })
                  }
                >
                  <Play size={15} />
                  계획 승인 및 실행
                </button>
              </footer>
            </>
          )}
        </div>
      </div>
    </section>
  );
}
