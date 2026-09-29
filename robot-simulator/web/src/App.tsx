import { workspaceStorage } from "./visitorSession";
import { CargoProgress } from "./CargoProgress";
import { Fragment, useCallback, useEffect, useRef, useState } from "react";
import {
  Activity,
  MessageSquare,
  ArrowDownToLine,
  ArrowLeftRight,
  Box,
  Boxes,
  Dog,
  Truck,
  Bot,
  Route,
  Waypoints,
  Building2,
  Check,
  ChevronRight,
  CircleAlert,
  Copy,
  FileUp,
  FolderOpen,
  FlaskConical,
  Layers3,
  LayoutDashboard,
  Map,
  MousePointer2,
  Package,
  Pause,
  Play,
  Plus,
  RotateCcw,
  Redo2,
  Undo2,
  Search,
  PanelLeftClose,
  PanelRightClose,
  List,
  Menu,
  Save,
  Settings2,
  ShieldAlert,
  SkipForward,
  Square,
  Trash2,
  Users,
  X,
} from "lucide-react";
import type { LucideIcon } from "lucide-react";
import { api, ApiError, downloadJSON, request } from "./api";
import {
  executionConfigurationDisplay,
  type RunApproval,
} from "./approvalDisplay";
import { PhysicsView, PlanView } from "./WorldView";
import PlanningWorkbench from "./PlanningWorkbench";
import FloorplanPanel from "./FloorplanPanel";
import { WorkspaceFullscreen } from "./WorkspaceFullscreen";
import HistoryLibrary from "./HistoryLibrary";
import PedestrianInspector from "./PedestrianInspector";
import RecordingView from "./RecordingView";
import RuntimeTimeline from "./RuntimeTimeline";
import ChargingEnergyPanel from "./ChargingEnergyPanel";
import ChargingWorkflowPanel from "./ChargingWorkflowPanel";
import {
  chargingWorkflowIsActive,
  chargingWorkflowHasHistory,
} from "./chargingWorkflow";
import EnergyConsumptionPanel from "./EnergyConsumptionPanel";
import PedestrianSafetyPanel from "./PedestrianSafetyPanel";
import MotionLimitPanel from "./MotionLimitPanel";
import {
  commandStatusLabel,
  commandFeedbackSummary,
  robotStatusLabel,
  robotReasonLabel,
  describeRuntimeEvent,
  userFacingError,
  validateMoveTarget,
} from "./uiMessages";
import {
  draftKey,
  fingerprint,
  validateProject,
  projectStructureErrors,
  transformed,
  duplicateEntities,
  deletionReferences,
} from "./workspace";
import type { EntityTransform } from "./workspace";
import { floorAtHeight } from "./spatial";
import { agvRouteGuidance, editAgvRoute } from "./agvRoute";
import type { AgvRouteEdit } from "./agvRoute";
import type {
  Catalog,
  CooperativeTask,
  Element,
  ElementKind,
  Experiment,
  Item,
  MeshData,
  Person,
  Policy,
  Pose,
  Project,
  RecoveryRequest,
  RecoveryState,
  RobotInstance,
  RobotModel,
  RuntimeEvent,
  RunState,
  SavedProject,
  Task,
  TaskKind,
  TaskState,
} from "./types";
type Page =
  | "history"
  | "monitor"
  | "planner"
  | "environment"
  | "robots"
  | "scenario"
  | "policy"
  | "facilities"
  | "events"
  | "experiments";
const isDraftPage = (page: Page) =>
  ["environment", "robots", "scenario", "policy", "planner"].includes(page);
const pages: {
  id: Page;
  name: string;
  icon: LucideIcon;
  description: string;
}[] = [
  {
    id: "history",
    name: "작업 기록",
    icon: FolderOpen,
    description: "저장한 구성과 도면·계획·실험, 샘플을 다시 찾아 이어갑니다.",
  },
  {
    id: "planner",
    name: "계획 도우미",
    icon: MessageSquare,
    description: "질문에서 실행 계획, 참여 구성과 최종 승인까지 연결합니다.",
  },
  {
    id: "monitor",
    name: "실시간 관제",
    icon: LayoutDashboard,
    description: "물리 실행과 관측 상태, 명령의 결과를 함께 확인합니다.",
  },
  {
    id: "environment",
    name: "환경 편집",
    icon: Map,
    description:
      "같은 환경 데이터로 2D 공간을 설계하고 3D 물리 형상을 확인합니다.",
  },
  {
    id: "robots",
    name: "로봇 라이브러리",
    icon: Boxes,
    description: "모델을 선택하고 개체별 장비·센서·제어 조건을 구성합니다.",
  },
  {
    id: "scenario",
    name: "운영 시나리오",
    icon: ArrowLeftRight,
    description: "작업 흐름과 사람, 물품을 정의하고 운영 조건을 구성합니다.",
  },
  {
    id: "policy",
    name: "정책과 물리 설정",
    icon: Settings2,
    description: "관제 판단 기준과 관측·물리 실행 주기를 설정합니다.",
  },
  {
    id: "facilities",
    name: "시설과 예약",
    icon: Building2,
    description: "공용 시설의 상태, 예약과 대기열을 확인합니다.",
  },
  {
    id: "events",
    name: "사건 타임라인",
    icon: Activity,
    description:
      "현재 실행의 명령·물리 사건·관제 결정을 시간순으로 추적합니다.",
  },
  {
    id: "experiments",
    name: "실험과 비교",
    icon: FlaskConical,
    description:
      "동일 환경과 여러 시드에서 정책을 반복 실행하고 결과를 비교합니다.",
  },
];
const robotIcons: Record<string, LucideIcon> = {
  spot: Dog,
  delivery: Truck,
  amr: Bot,
  agv: Route,
  logistics: Package,
  arm: Waypoints,
  mobile_manipulator: Boxes,
};
function RobotIcon({ model, size = 22 }: { model: string; size?: number }) {
  const Icon = robotIcons[model] ?? Bot;
  return <Icon size={size} />;
}
const elementNames: Record<ElementKind, string> = {
  room: "방",
  corridor: "통로",
  wall: "벽",
  column: "기둥",
  door: "문",
  opening: "개방 통로",
  stairs: "계단",
  ramp: "경사로",
  elevator: "엘리베이터",
  charger: "충전소",
  dock: "도킹",
  loading: "상하차",
  shelf: "선반",
  workbench: "작업대",
  conveyor: "컨베이어",
  waiting: "대기 구역",
  obstacle: "장애물",
  restricted: "출입 제한",
  speed_zone: "속도 제한",
  one_way: "일방 통행",
  entrance: "출입구",
};
const taskNames: Record<TaskKind, string> = {
  delivery: "배송",
  transport: "운반",
  load: "상차",
  unload: "하차",
  retrieve: "회수",
  patrol: "순찰",
  inspect: "설비 점검",
  manipulate: "물품 조작",
  handoff: "공정 간 인계",
};
const cooperativeFormKinds: TaskKind[] = [
  "handoff",
  "transport",
  "unload",
  "load",
  "delivery",
  "retrieve",
];
const cooperativeSchemaKinds = cooperativeFormKinds;
const cooperationPhases: Record<string, string> = {
  loading_approach: "예약된 상차 위치로 접근",
  loading: "초기 상차",
  loaded: "적재 확인",
  await_load: "적재 지지 확인",
  transport: "적재물 운반",
  settle: "운반 로봇 정차 확인",
  await_receiver: "수신 준비 확인",
  handoff_grasp: "수신 로봇 파지",
  separating: "운반 지지면에서 분리",
  confirm_handoff: "양측 인계 확인",
  await_prepare: "수신 준비 대기",
  approach: "물품 접근",
  ready: "준비 자세 확인",
  descend: "그리퍼 하강",
  grasp: "그리퍼 파지",
  grasped: "파지 확인",
  lift: "물품 들기",
  received: "물품 인수 확인",
  clearance: "이동 높이 확보",
  translate: "최종 배치 위치로 이동",
  lower: "물품 내려놓기",
  release: "그리퍼 해제",
  retract: "팔 후퇴",
  placed: "최종 배치 확인",
};
const loadingPhases: Record<string, string> = {
  await_source: "초기 물품 관측 대기",
  await_prepare: "상차 준비 대기",
  received: "상차 로봇의 물품 들기 확인",
  translate: "운반 로봇의 적재 위치로 이동",
  placed: "적재면 배치 확인",
  retreat: "상차 로봇 후퇴 확인",
};
function cooperativeIssues(task: Task, project: Project): string[] {
  const cooperation = task.cooperation;
  if (!cooperation) return [];
  const issues: string[] = [];
  if (!cooperativeSchemaKinds.includes(task.kind))
    issues.push("이 작업 유형은 협업 설정을 사용할 수 없습니다.");
  const roles = [
    ["운반", cooperation.carrier_id],
    ["수신", cooperation.receiver_id],
    ...(cooperation.donor_id != null ? [["상차", cooperation.donor_id]] : []),
  ];
  const previous: Record<string,Task> = {};
  const collect = (id:string) => {
    const prior=project.tasks.find(t=>t.id===id);
    if(!prior||previous[id])return;
    previous[id]=prior;prior.predecessor_ids.forEach(collect);
  };
  if(cooperation.source_floor_id)task.predecessor_ids.forEach(collect);
  const sourceFloor=cooperation.source_floor_id||task.floor_id;
  for (const [label, id] of roles) {
    const robot = project.robots.find((r) => r.id === id);
    const expected=id===cooperation.receiver_id?task.floor_id:sourceFloor;
    const arrives=Object.values(previous).some(t=>t.cooperation?.carrier_id===id&&t.floor_id===expected);
    if (!id.trim() || !robot) issues.push(`${label} 로봇을 선택하세요.`);
    else if (robot.floor_id !== expected&&!arrives)
      issues.push(`${label} 로봇의 초기 층 또는 선행 작업 도착 층을 확인하세요.`);
  }
  if (new Set(roles.map(([, id]) => id)).size !== roles.length)
    issues.push("참여 역할마다 서로 다른 로봇을 선택하세요.");
  if (!cooperation.workspace_id?.trim())
    issues.push("공유 작업 공간의 예약 이름을 입력하세요.");
  if (
    cooperation.loading_offset !== undefined &&
    (!Array.isArray(cooperation.loading_offset) ||
      cooperation.loading_offset.length !== 2 ||
      cooperation.loading_offset.some(
        (value) => typeof value !== "number" || !Number.isFinite(value),
      ))
  )
    issues.push("적재 위치는 유한한 X·Y 숫자 두 개여야 합니다.");
  const item = project.items.find((i) => i.id === task.item_id);
  if (!item) issues.push("협업할 물품을 선택하세요.");
  else if (item.floor_id !== sourceFloor&&!Object.values(previous).some(t=>t.item_id===item.id&&t.floor_id===sourceFloor))
    issues.push("물품의 초기 층 또는 선행 배치 층이 상차 층과 일치해야 합니다.");
  if (
    task.preferred_robot != null &&
    task.preferred_robot !== cooperation.carrier_id
  )
    issues.push("우선 로봇은 협업의 운반 로봇과 같아야 합니다.");
  return issues;
}
function CooperationProgress({ value }: { value?: TaskState["cooperation"] }) {
  if (!value) return <span className="muted">협업 관측 대기</span>;
  const phase = (name?: string, loading = false) =>
    name
      ? ((loading ? loadingPhases[name] : undefined) ??
        cooperationPhases[name] ??
        statusNames[name] ??
        name)
      : "관측 대기";
  return (
    <div>
      {(value.phase === "loading" ||
        value.loading_phase !== undefined ||
        value.loading_committed !== undefined) && (
        <>
          <div>상차: {phase(value.loading_phase, true)}</div>
          <small className="muted">
            {value.loading_committed === true
              ? "운반 로봇에 적재 인계 확인"
              : value.loading_committed === false
                ? "적재 인계 미확인"
                : "적재 인계 관측 대기"}
          </small>
        </>
      )}
      <div>운반·인계: {phase(value.phase)}</div>
      <div>수신·배치: {phase(value.receiver_phase)}</div>
      <small className="muted">
        {value.committed === true
          ? "수신 소유권 이전 확인"
          : value.committed === false
            ? "수신 소유권 이전 미확인"
            : "소유권 관측 대기"}
        {" · "}
        {value.resources_retained === true
          ? "예약 유지"
          : value.resources_retained === false
            ? "예약 반납"
            : "예약 관측 대기"}
      </small>
    </div>
  );
}
const modelKindNames: Record<string, string> = {
  quadruped: "사족 보행",
  delivery: "배송 로봇",
  amr: "자율 이동 로봇",
  agv: "유도 경로 로봇",
  logistics: "물류 운반",
  arm: "고정형 로봇팔",
  mobile_manipulator: "이동형 조작 로봇",
};
const gripperResearchModels = new Set(["arm", "mobile_manipulator"]);
const locomotionNames: Record<string, string> = {
  legs: "관절·발 접촉 보행",
  differential: "차동 바퀴",
  guided: "지정 경로",
  fixed: "고정 기반",
};
const statusNames: Record<string, string> = {
  info: "정보",
  warning: "경고",
  error: "오류",
  paused: "일시 정지",
  running: "실행 중",
  failed: "실패",
  idle: "대기",
  moving: "이동 중",
  executing: "수행 중",
  completed: "완료",
  queued: "대기열",
  pending: "배정 대기",
  assigned: "배정됨",
  blocked: "진행 불가",
  charging: "충전 절차 중",
  cooperating: "협업 수행 중",
  approach: "충전소 접근",
  dock: "접점 정렬",
  undock: "충전 접점 분리",
  recovery_required: "복구 확인 필요",
  recovering: "물품 복구 중",
  fault: "고장",
  stopped: "정지",
  accepted: "수락",
  rejected: "거부",
  success: "성공",
  disconnected: "연결 끊김",
  ready: "준비",
  cancelled: "취소",
  stand: "서기",
  sit: "앉기",
};
const fmt = (value: unknown, digits = 2) =>
  typeof value === "number"
    ? value.toLocaleString("ko-KR", { maximumFractionDigits: digits })
    : value === null || value === undefined
      ? "—"
      : String(value);
const uid = (prefix: string) => `${prefix}-${crypto.randomUUID().slice(0, 8)}`;
const pose = (x = 0, y = 0, z = 0): Pose => ({ x, y, z, yaw: 0 });
function Badge({ value, tone }: { value: string; tone?: string }) {
  return (
    <span
      className={`badge ${tone ?? (["completed", "success", "ready"].includes(value) ? "good" : ["failed", "rejected", "disconnected"].includes(value) ? "danger" : ["running", "moving", "executing"].includes(value) ? "accent" : "")}`}
    >
      {statusNames[value] ??
        (/[가-힣]/.test(value) ? value : robotStatusLabel(value))}
    </span>
  );
}
function Empty({
  title,
  children,
}: {
  title: string;
  children?: React.ReactNode;
}) {
  return (
    <div className="empty">
      <Box size={27} />
      <strong>{title}</strong>
      <p>{children}</p>
    </div>
  );
}
function Field({
  label,
  value,
  onChange,
  min,
  max,
  step = 0.1,
}: {
  label: string;
  value: number;
  onChange: (value: number) => void;
  min?: number;
  max?: number;
  step?: number | "any";
}) {
  const [text, setText] = useState(String(value));
  useEffect(() => setText(String(value)), [value]);
  const n = Number(text);
  const invalid =
    text.trim() === "" ||
    !Number.isFinite(n) ||
    (min !== undefined && n < min) ||
    (max !== undefined && n > max);
  return (
    <label>
      {label}
      <input
        type="number"
        value={text}
        min={min}
        max={max}
        step={step}
        aria-label={label}
        aria-invalid={invalid || undefined}
        onChange={(e) => {
          setText(e.target.value);
          const next = Number(e.target.value);
          if (e.target.value.trim() && Number.isFinite(next)) onChange(next);
        }}
      />
      {invalid && (
        <small className="field-error" role="status">
          {min !== undefined || max !== undefined
            ? `${min ?? "제한 없음"} ~ ${max ?? "제한 없음"} 범위의 숫자를 입력하세요.`
            : "유한한 숫자를 입력하세요."}
        </small>
      )}
    </label>
  );
}

function JsonDetails({ title, data }: { title: string; data: unknown }) {
  return (
    <details className="details">
      <summary>{title}</summary>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </details>
  );
}
function JsonEditor({
  value,
  onApply,
  label = "세부 데이터 편집",
}: {
  value: unknown;
  onApply: (value: unknown) => void;
  label?: string;
}) {
  const [text, setText] = useState(JSON.stringify(value, null, 2));
  const [error, setError] = useState("");
  useEffect(() => setText(JSON.stringify(value, null, 2)), [value]);
  return (
    <details className="details">
      <summary>{label}</summary>
      <label style={{ marginTop: 12 }}>
        JSON
        <textarea
          className="code"
          value={text}
          onChange={(e) => setText(e.target.value)}
          rows={12}
        />
      </label>
      {error && <p className="muted">{error}</p>}
      <button
        style={{ marginTop: 8 }}
        onClick={() => {
          try {
            onApply(JSON.parse(text));
            setError("");
          } catch (e) {
            setError(`JSON 형식을 확인하세요: ${String(e)}`);
          }
        }}
      >
        초안에 반영
      </button>
    </details>
  );
}
function Stat({
  label,
  value,
  unit = "",
}: {
  label: string;
  value: unknown;
  unit?: string;
}) {
  return (
    <div className="metric">
      <small>{label}</small>
      <strong>
        {fmt(value)}
        {value !== null && value !== undefined && <small> {unit}</small>}
      </strong>
    </div>
  );
}
type RecoveryDraft = {
  actor: string;
  destination: Pose;
  target: "source" | "destination" | "custom";
  retry: boolean;
  timeout: number;
  request?: RecoveryRequest;
  receipt?: RecoveryState;
  pending?: boolean;
  uncertain?: boolean;
};
function RecoveryPanel({
  task,
  spec,
  state,
  project,
  cache,
  cacheKey,
  busy,
  connected,
  isCurrent,
  run,
  refresh,
}: {
  task: TaskState;
  spec: Task;
  state: RunState;
  project: Project;
  cache: Map<string, RecoveryDraft>;
  cacheKey: string;
  busy: boolean;
  connected: boolean;
  isCurrent: () => boolean;
  run: (label: string, action: () => Promise<unknown>) => Promise<void>;
  refresh: () => Promise<void>;
}) {
  const executionId = task.execution_id ?? task.cooperation?.execution_id ?? "";
  const ledger = state.cooperation?.executions[executionId];
  const participants = Object.values(ledger?.participants ?? {}).length
    ? Object.values(ledger!.participants)
    : (task.participant_ids ?? []);
  const arms = state.robots.filter(
    (robot) =>
      participants.includes(robot.id) &&
      ["arm", "mobile_manipulator"].includes(robot.model_id),
  );
  const donor = ledger?.participants.donor ?? spec.cooperation?.donor_id;
  const source =
    spec.source ?? project.items.find((item) => item.id === spec.item_id)?.pose;
  const [initialDraft, setDraft] = useState<RecoveryDraft>(() => {
    const previous = cache.get(cacheKey);
    if (previous) return previous;
    const actor =
      arms.find((robot) => robot.id === ledger?.owner)?.id ??
      arms.find((robot) => robot.id === donor)?.id ??
      arms[0]?.id ??
      "";
    const initial: RecoveryDraft = {
      actor,
      destination: {
        ...(actor === donor && source ? source : spec.destination),
      },
      target: actor === donor && source ? "source" : "destination",
      retry: false,
      timeout: 90,
    };
    cache.set(cacheKey, initial);
    return initial;
  });
  const draft = cache.get(cacheKey) ?? initialDraft;
  const update = (next: RecoveryDraft) => {
    cache.set(cacheKey, next);
    setDraft(next);
  };
  // Retain request identity across navigation and uncertain transport responses.
  const edit = (next: Partial<RecoveryDraft>) => update({ ...draft, ...next });
  const receipt = draft.receipt;
  const recovery =
    receipt &&
    (!task.recovery ||
      receipt.started_at > task.recovery.started_at ||
      (receipt.recovery_id !== task.recovery.recovery_id &&
        receipt.recovery_id === draft.request?.request_id &&
        receipt.started_at === task.recovery.started_at) ||
      (receipt.recovery_id === task.recovery.recovery_id &&
        receipt.status !== "running" &&
        task.recovery.status === "running"))
      ? receipt
      : task.recovery;
  const active = recovery?.status === "running";
  const eligible =
    ["failed", "cancelled"].includes(task.status) &&
    task.cooperation?.resources_retained === true;
  const retryAllowed =
    draft.actor === donor &&
    source !== undefined &&
    (["x", "y", "z"] as const).every(
      (axis) => Math.abs(draft.destination[axis] - source[axis]) <= 1e-6,
    );
  const valid =
    arms.some((robot) => robot.id === draft.actor) &&
    Object.values(draft.destination).every(Number.isFinite) &&
    Number.isFinite(draft.timeout) &&
    draft.timeout > 0 &&
    draft.timeout <= 300;
  const blocked = busy || draft.pending || !connected;
  const submit = () => {
    if (
      !isCurrent() ||
      cache.get(cacheKey)?.pending ||
      blocked ||
      active ||
      !eligible ||
      !valid
    )
      return;
    const body = {
      actor_id: draft.actor,
      destination: draft.destination,
      retry: retryAllowed && draft.retry,
      timeout: draft.timeout,
    };
    const previous = draft.request;
    const same =
      previous &&
      JSON.stringify({
        actor_id: previous.actor_id,
        destination: previous.destination,
        retry: previous.retry,
        timeout: previous.timeout,
      }) === JSON.stringify(body);
    const finished =
      recovery?.recovery_id === previous?.request_id &&
      recovery?.status !== "running";
    const request: RecoveryRequest =
      same && !finished
        ? previous
        : { ...body, request_id: crypto.randomUUID() };
    update({ ...draft, request, pending: true, uncertain: false });
    void run("물품 복구 요청 중", async () => {
      try {
        const accepted = await api.recoverTask(task.id, request);
        if (!isCurrent()) return;
        update({
          ...draft,
          request,
          receipt: accepted,
          pending: false,
          uncertain: false,
        });
        await refresh();
      } catch (error) {
        if (!isCurrent()) return;
        const current = cache.get(cacheKey) ?? draft;
        update({
          ...current,
          pending: false,
          uncertain:
            current.receipt?.recovery_id !== request.request_id &&
            (!(error instanceof ApiError) || error.uncertain),
        });
        throw error;
      }
    });
  };
  const cancel = () => {
    if (
      !recovery ||
      !active ||
      !isCurrent() ||
      cache.get(cacheKey)?.pending ||
      blocked
    )
      return;
    update({ ...draft, pending: true });
    void run("물품 복구 취소 요청 중", async () => {
      try {
        const cancelled = await api.cancelRecovery(
          task.id,
          recovery.recovery_id,
        );
        if (!isCurrent()) return;
        update({ ...draft, receipt: cancelled, pending: false });
        await refresh();
      } catch (error) {
        if (!isCurrent()) return;
        update({ ...(cache.get(cacheKey) ?? draft), pending: false });
        throw error;
      }
    });
  };
  const stages: Record<string, string> = {
    verify: "현재 상태 확인",
    verify_held: "현재 파지 확인",
    await_pickup: "운반 로봇 위 물품 확인",
    pregrasp: "파지 준비 위치로 이동",
    approach: "물품 접근",
    descend: "파지 위치 정렬",
    grip: "양쪽 파지 확인",
    grasp: "양쪽 파지 확인",
    lift: "들림·분리 확인",
    hold: "파지 안정 확인",
    received: "파지 안정 확인",
    transport: "복구 위치로 이동",
    move: "복구 위치로 이동",
    lower: "지지면으로 내리기",
    release: "파지 해제",
    retreat: "팔 물러나기",
    retract: "팔 물러나기",
    verify_placement: "지지·해제·안정 확인",
    placed: "배치 확인",
  };
  return (
    <details className="recovery-panel">
      <summary>
        물품 복구{" "}
        {recovery ? `· ${statusNames[recovery.status]}` : "· 예약 유지 중"}
      </summary>
      <div className="recovery-content">
        <p className="muted">
          기존 작업의 실패·취소 기록을 유지하며 물품을 지정 위치로 복구합니다.
          요청 수락 후 실제 관측으로 완료를 확인합니다.
        </p>
        {recovery && (
          <div className="recovery-status" aria-live="polite">
            <div className="statusrow">
              <Badge value={recovery.status} />
              <strong>
                {stages[recovery.phase ?? ""] ?? recovery.phase ?? "상태 확인"}
              </strong>
            </div>
            <p>{recovery.reason}</p>
            <small className="muted">
              복구 요청 {recovery.recovery_id.slice(0, 8)} · 시작{" "}
              {fmt(recovery.started_at)}초 · 완료{" "}
              {recovery.completed_at == null
                ? "미완료"
                : `${fmt(recovery.completed_at)}초`}{" "}
              (시뮬레이션 시각)
            </small>
            <p className="muted">
              복구 팔:{" "}
              {state.robots.find((robot) => robot.id === recovery.actor_id)
                ?.name ?? "로봇"}{" "}
              · {recovery.actor_id} · 목표: {fmt(recovery.destination.x)},{" "}
              {fmt(recovery.destination.y)}, {fmt(recovery.destination.z)}m
              {recovery.retry ? " · 원래 작업 재시도 요청 포함" : ""}
            </p>
          </div>
        )}
        {active ? (
          <div className="form-actions">
            <button className="danger" disabled={blocked} onClick={cancel}>
              <X size={15} />
              {draft.pending ? "요청 전송 중…" : "진행 중인 복구 취소"}
            </button>
          </div>
        ) : (
          eligible && (
            <form
              onSubmit={(event) => {
                event.preventDefault();
                submit();
              }}
            >
              <fieldset disabled={blocked}>
                <div className="form-grid recovery-fields">
                  <label>
                    복구할 참여 팔
                    <select
                      value={draft.actor}
                      onChange={(event) => {
                        const actor = event.target.value;
                        edit({
                          actor,
                          destination: {
                            ...(actor === donor && source
                              ? source
                              : spec.destination),
                          },
                          target:
                            actor === donor && source
                              ? "source"
                              : "destination",
                          retry: false,
                        });
                      }}
                    >
                      <option value="" disabled>
                        참여 팔 선택
                      </option>
                      {arms.map((robot) => (
                        <option key={robot.id} value={robot.id}>
                          {robot.name} · {robot.id}
                          {robot.id === ledger?.owner ? " · 현재 소유" : ""}
                        </option>
                      ))}
                    </select>
                  </label>
                  <label>
                    복구 위치
                    <select
                      value={draft.target}
                      onChange={(event) => {
                        const target = event.target
                          .value as RecoveryDraft["target"];
                        edit({
                          target,
                          destination: {
                            ...(target === "source" && source
                              ? source
                              : target === "destination"
                                ? spec.destination
                                : draft.destination),
                          },
                          retry: false,
                        });
                      }}
                    >
                      <option value="source" disabled={!source}>
                        원래 물품 출발점
                      </option>
                      <option value="destination">작업의 최종 배치점</option>
                      <option value="custom">좌표 직접 지정</option>
                    </select>
                  </label>
                  {(["x", "y", "z"] as const).map((axis) => (
                    <Field
                      key={axis}
                      label={`물품 바닥 ${axis.toUpperCase()} (m)`}
                      value={draft.destination[axis]}
                      step="any"
                      onChange={(value) =>
                        edit({
                          destination: { ...draft.destination, [axis]: value },
                          target: "custom",
                          retry: false,
                        })
                      }
                    />
                  ))}
                  <Field
                    label="복구 제한 시간 (초)"
                    value={draft.timeout}
                    min={0}
                    max={300}
                    step="any"
                    onChange={(timeout) => edit({ timeout })}
                  />
                </div>
                <p className="muted recovery-help">
                  {project.environment.floors.find(
                    (floor) => floor.id === spec.floor_id,
                  )?.name ?? spec.floor_id}{" "}
                  바닥 기준 물품 바닥 중심 좌표입니다. 현재 실행에 적용된 구성을
                  사용합니다.
                </p>
                <label className="recovery-retry">
                  <input
                    type="checkbox"
                    checked={retryAllowed && draft.retry}
                    disabled={!retryAllowed}
                    onChange={(event) => edit({ retry: event.target.checked })}
                  />
                  복구 완료 후 원래 작업 재시도
                </label>
                <p className="muted">
                  최초 상차 팔로 원래 출발점에 복구할 때만 선택할 수 있습니다.
                  남은 횟수·기한은 실행부가 확인합니다.
                </p>
              </fieldset>
              {!arms.length && (
                <p className="muted">
                  예약된 참여 팔 정보를 확인할 수 없습니다.
                </p>
              )}
              {!valid && arms.length > 0 && (
                <p className="muted">
                  참여 팔과 유효한 좌표, 0초 초과 300초 이하의 제한 시간을
                  입력하세요.
                </p>
              )}
              {draft.uncertain && (
                <p className="notice" role="status">
                  요청 응답을 확인하지 못했습니다. 같은 내용으로 다시 보내면
                  같은 요청 번호를 사용합니다.
                </p>
              )}
              <div className="form-actions">
                <button
                  className="primary"
                  type="submit"
                  disabled={blocked || !valid}
                >
                  <RotateCcw size={15} />
                  {draft.pending
                    ? "요청 전송 중…"
                    : draft.uncertain
                      ? "같은 복구 요청 다시 보내기"
                      : recovery
                        ? "새 복구 요청"
                        : "물품 복구 요청"}
                </button>
              </div>
            </form>
          )
        )}
        {!connected && (
          <p className="muted">실행부 연결을 확인한 뒤 요청할 수 있습니다.</p>
        )}
        {state.status === "paused" && (
          <p className="muted">
            시뮬레이션이 일시 정지되어 있습니다. 요청이 수락되어도 실행이
            재개되기 전에는 물리 복구가 진행되지 않습니다.
          </p>
        )}
      </div>
    </details>
  );
}
function App() {
  const [page, setPage] = useState<Page>("monitor");
  const currentPage = useRef(page);
  currentPage.current = page;
  const [catalog, setCatalog] = useState<Catalog>({
    models: [],
    templates: [],
  });
  const [project, setProject] = useState<Project | null>(null);
  const [state, setState] = useState<RunState | null>(null);
  const [runApproval, setRunApproval] = useState<RunApproval | null>(null);
  const [runtimeProject, setRuntimeProject] = useState<{
    runId: string;
    project: Project;
  } | null>(null);
  const recoveryDrafts = useRef(new globalThis.Map<string, RecoveryDraft>());
  const currentState = useRef(state);
  currentState.current = state;
  const [meshes, setMeshes] = useState<MeshData[]>([]);
  const [dirty, setDirty] = useState(false);
  const [connected, setConnected] = useState(false);
  const [error, setError] = useState("");
  const [busy, setBusy] = useState("");
  const [selected, setSelectedValue] = useState("");
  const [selectedIds, setSelectedIds] = useState<string[]>([]);
  const setSelected = useCallback((id: string) => {
    setSelectedValue(id);
    setSelectedIds(id ? [id] : []);
  }, []);
  const [snap, setSnap] = useState(true);
  const [browserOpen, setBrowserOpen] = useState(true);
  const [inspectorOpen, setInspectorOpen] = useState(false);
  const [browserTab, setBrowserTab] = useState<"objects" | "tools">("objects");
  const [objectSearch, setObjectSearch] = useState("");
  const [objectFilter, setObjectFilter] = useState("robots");
  const [robotSearch, setRobotSearch] = useState("");
  const [robotLibraryMode, setRobotLibraryMode] = useState<
    "instances" | "models"
  >("instances");
  const contentRef = useRef<HTMLDivElement>(null);
  const [toolSearch, setToolSearch] = useState("");
  const [unsaved, setUnsaved] = useState(false);
  const [savedRevision, setSavedRevision] = useState<number | null>(null);
  const [notice, setNotice] = useState("");
  const [clockNow, setClockNow] = useState(Date.now());
  const [redoCount, setRedoCount] = useState(0);
  const [sceneRunId, setSceneRunId] = useState("");
  const previousNoticeRun = useRef<string | null>(null);
  const [commandReceipt, setCommandReceipt] = useState<{
    runId: string;
    robotId: string;
    value: Record<string, unknown>;
  } | null>(null);
  const currentProject = useRef(project);
  currentProject.current = project;
  const savedFingerprint = useRef("");
  const savePending = useRef(false);
  const draftGeneration = useRef(0);
  const appliedFingerprint = useRef("");
  const redoHistory = useRef<Project[]>([]);
  const operations = useRef(new globalThis.Map<string, string>());
  const stateRequest = useRef(0);
  const statePublished = useRef(0);
  const stateEpoch = useRef(0);
  const runTransition = useRef(false);
  const commandPending = useRef(new Set<string>());
  const [floorId, setFloorId] = useState("");
  const [view, setView] = useState<"2d" | "3d">("3d");
  const [cameraFocusRequest, setCameraFocusRequest] = useState<{
    id: string;
    sequence: number;
  } | null>(null);
  const cameraFocusSequence = useRef(0);
  const [tool, setTool] = useState<ElementKind | null>(null);
  const [speed, setSpeed] = useState(1);
  const [saved, setSaved] = useState<SavedProject[]>([]);
  const [savedChoice, setSavedChoice] = useState("");
  const [focusedDrawing, setFocusedDrawing] = useState<{id:string; sequence:number} | null>(null);
  const [focusedPlan, setFocusedPlan] = useState<{id:string; version:number; sequence:number} | null>(null);
  const [experiments, setExperiments] = useState<Experiment[]>([]);
  const [eventFilter, setEventFilter] = useState("");
  const [scenarioTab, setScenarioTab] = useState("tasks");
  const [selectedTask, setSelectedTask] = useState("");
  const [recordingSeek, setRecordingSeek] = useState<{
    runId: string;
    time: number;
    entityId?: string | null;
  }>();
  const [seeds, setSeeds] = useState("11, 23, 42");
  const [duration, setDuration] = useState(30);
  const [comparePolicies, setComparePolicies] = useState([
    "nearest",
    "balanced",
  ]);
  const [robotCounts, setRobotCounts] = useState<Record<string, number>>({});
  const [faultKind, setFaultKind] = useState("motor");
  const [faultDuration, setFaultDuration] = useState(5);
  const [moveTarget, setMoveTarget] = useState<Record<keyof Pose, string>>({
    x: "0",
    y: "0",
    z: "0",
    yaw: "0",
  });
  const [lastUpdate, setLastUpdate] = useState(0);
  const upload = useRef<HTMLInputElement>(null);
  const undoHistory = useRef<Project[]>([]);
  const [undoCount, setUndoCount] = useState(0);
  const matchedRuntimeProject =
    runtimeProject && runtimeProject.runId === state?.run_id
      ? runtimeProject.project
      : null;
  const floorProject = isDraftPage(page) ? project : matchedRuntimeProject;
  const navigate = (next: Page) => {
    // Initialize may restore a draft before the first run response arrives.
    // Update the ref immediately so that run-bound cleanup knows its context.
    currentPage.current = next;
    setPage(next);
    const targetProject = isDraftPage(next)
      ? currentProject.current
      : matchedRuntimeProject;
    setFloorId((id) =>
      targetProject?.environment.floors.some((floor) => floor.id === id)
        ? id
        : (targetProject?.environment.floors[0]?.id ?? ""),
    );
    if (next === "environment") {
      setView("2d");
      setBrowserTab("tools");
      setObjectFilter("all");
    } else if (next === "monitor") {
      setBrowserTab("objects");
      setObjectFilter("robots");
      setTool(null);
    }
  };
  useEffect(() => {
    contentRef.current?.scrollTo({ top: 0 });
  }, [page]);
  useEffect(() => {
    // Navigation can precede receipt of the run-matched configuration.
    // Validate again when that configuration arrives or its floors change.
    setFloorId((id) =>
      floorProject?.environment.floors.some((floor) => floor.id === id)
        ? id
        : (floorProject?.environment.floors[0]?.id ?? ""),
    );
  }, [floorProject, page]);
  const configurationDisplay = executionConfigurationDisplay(
    dirty,
    state?.run_id,
    runApproval,
  );
  const pageInfo = pages.find((p) => p.id === page)!;
  const mapPage = page === "monitor" || page === "environment";
  const stale = lastUpdate > 0 && clockNow - lastUpdate > 4000;
  const connectionState = !lastUpdate
    ? "connecting"
    : !connected
      ? "disconnected"
      : stale
        ? "stale"
        : "connected";
  const live = connected && !stale;
  const run = useCallback(
    async (label: string, action: () => Promise<unknown>) => {
      const operation = uid("request");
      operations.current.set(operation, label);
      setBusy(label);
      setError("");
      try {
        await action();
      } catch (e) {
        const detail = userFacingError(e);
        setError(`${detail.message} ${detail.nextAction ?? ""}`);
      } finally {
        operations.current.delete(operation);
        setBusy([...operations.current.values()].at(-1) ?? "");
      }
    },
    [],
  );
  const readState = useCallback(async () => {
    const request = ++stateRequest.current,
      epoch = stateEpoch.current;
    try {
      const s = await api.state();
      if (
        epoch === stateEpoch.current &&
        request > statePublished.current &&
        !runTransition.current
      ) {
        statePublished.current = request;
        currentState.current = s;
        setState(s);
        if (typeof s.speed === "number" && Number.isFinite(s.speed))
          setSpeed(s.speed);
        setConnected(true);
        setLastUpdate(Date.now());
      }
      return s;
    } catch (error) {
      if (epoch === stateEpoch.current && request > statePublished.current)
        setConnected(false);
      throw error;
    }
  }, []);
  const refresh = useCallback(async () => {
    await readState();
  }, [readState]);
  const adopt = useCallback(
    (p: Project, changed = true) => {
      const issues = validateProject(p);
      if (issues.length) throw new Error(issues.join(" "));
      const prior = currentProject.current;
      const signature = fingerprint(p);
      const identical = !!prior && fingerprint(prior) === signature;
      draftGeneration.current++;
      if (prior && changed && !identical) {
        undoHistory.current.push(structuredClone(prior));
        if (undoHistory.current.length > 60) undoHistory.current.shift();
      } else if (!changed) {
        undoHistory.current = [];
        savedFingerprint.current = fingerprint(p);
        appliedFingerprint.current = fingerprint(p);
      }
      currentProject.current = p;
      setProject(p);
      setFloorId(p.environment.floors[0]?.id ?? "");
      setSelected(
        p.id === "example-elevator-pedestrian-60s" ? "sample-amr" : "",
      );
      setSelectedTask("");
      setDirty(signature !== appliedFingerprint.current);
      setUnsaved(signature !== savedFingerprint.current);
      if (!identical) setSavedRevision(null);
      setError("");
      redoHistory.current = [];
      setRedoCount(0);
      setUndoCount(undoHistory.current.length);
      if (changed)
        setNotice(
          "구성을 초안으로 불러왔습니다. 실행 취소로 이전 작업을 복원할 수 있습니다.",
        );
    },
    [setSelected],
  );
  useEffect(() => {
    const timer = setInterval(() => setClockNow(Date.now()), 1000);
    return () => clearInterval(timer);
  }, []);
  useEffect(() => {
    if (!project) return;
    const timer = setTimeout(() => {
      try {
        workspaceStorage.setItem(
          draftKey,
          JSON.stringify({
            project,
            unsaved,
            savedRevision,
            workspace: {
              page,
              floorId,
              view,
              browserOpen,
              inspectorOpen,
              selectedIds,
            },
          }),
        );
      } catch {
        setNotice(
          "브라우저 임시 보관 공간이 부족합니다. 프로젝트 저장 또는 JSON 내보내기를 사용하세요.",
        );
      }
    }, 300);
    const preserve = () => {
      try {
        workspaceStorage.setItem(
          draftKey,
          JSON.stringify({
            project: currentProject.current,
            unsaved,
            savedRevision,
            workspace: {
              page,
              floorId,
              view,
              browserOpen,
              inspectorOpen,
              selectedIds,
            },
          }),
        );
      } catch {
        /* The visible warning covers unavailable browser storage. */
      }
    };
    window.addEventListener("pagehide", preserve);
    return () => {
      clearTimeout(timer);
      window.removeEventListener("pagehide", preserve);
    };
  }, [
    project,
    unsaved,
    savedRevision,
    page,
    floorId,
    view,
    browserOpen,
    inspectorOpen,
    selectedIds,
  ]);
  useEffect(() => {
    let active = true;
    let initTimer: ReturnType<typeof setTimeout>;
    async function initialize() {
      try {
        const [c, p] = await Promise.all([api.catalog(), api.project()]);
        if (!active) return;
        setCatalog(c);
        // A reconnect never overwrites the user's live draft.
        if (!currentProject.current) {
          let recovered = false;
          try {
            const stored = JSON.parse(workspaceStorage.getItem(draftKey) ?? "null");
            if (stored?.project && !validateProject(stored.project).length) {
              adopt(stored.project, false);
              const workspace = stored.workspace;
              // Restore draft editing context only. Live selection belongs to a run.
              if (
                workspace &&
                ["environment", "robots", "scenario", "policy"].includes(
                  workspace.page,
                )
              ) {
                navigate(workspace.page);
                if (workspace.view === "2d" || workspace.view === "3d")
                  setView(workspace.view);
                if (
                  stored.project.environment.floors.some(
                    (f: { id: string }) => f.id === workspace.floorId,
                  )
                )
                  setFloorId(workspace.floorId);
                if (typeof workspace.browserOpen === "boolean")
                  setBrowserOpen(workspace.browserOpen);
                if (typeof workspace.inspectorOpen === "boolean")
                  setInspectorOpen(workspace.inspectorOpen);
                const entities = [
                  ...stored.project.robots,
                  ...stored.project.environment.elements,
                  ...stored.project.people,
                  ...stored.project.items,
                ];
                const ids: string[] = Array.isArray(workspace.selectedIds)
                  ? workspace.selectedIds.filter(
                      (id: unknown) =>
                        typeof id === "string" &&
                        entities.some((e) => e.id === id),
                    )
                  : [];
                setSelectedIds(ids);
                setSelectedValue(ids.at(-1) ?? "");
              }
              setDirty(fingerprint(stored.project) !== fingerprint(p));
              appliedFingerprint.current = fingerprint(p);
              setUnsaved(!!stored.unsaved);
              setSavedRevision(stored.savedRevision ?? null);
              if (stored.unsaved) savedFingerprint.current = "";
              recovered = true;
              if (
                stored.unsaved ||
                fingerprint(stored.project) !== fingerprint(p)
              )
                setNotice(
                  "마지막 편집 초안을 복원했습니다. 실행 구성과 다른 변경은 적용 후 실행하세요.",
                );
            }
          } catch {
            /* Invalid browser drafts never replace the server project. */
          }
          if (!recovered) adopt(p, false);
        }
        void api
          .saved()
          .then((value) => active && setSaved(value))
          .catch(() => {});
        void api
          .experiments()
          .then((value) => active && setExperiments(value))
          .catch(() => {});
      } catch (e) {
        if (active) {
          setError(e instanceof Error ? e.message : String(e));
          initTimer = setTimeout(initialize, 3000);
        }
      }
    }
    void initialize();
    let timer: ReturnType<typeof setTimeout>;
    async function poll() {
      let delay = 1000;
      try {
        const s = await readState();
        delay = 1000 / Math.max(1, Math.min(20, s.render_hz ?? 5));
      } catch {
        /* readState fences stale failures as well as successful responses. */
      }
      if (active) timer = setTimeout(poll, delay);
    }
    void poll();
    return () => {
      active = false;
      clearTimeout(timer);
      clearTimeout(initTimer);
    };
  }, [adopt, readState]);
  useEffect(() => {
    const runId = state?.run_id;
    let active = true;
    setRunApproval(null);
    if (runId) {
      // Receipt identity, not a local plan choice or a truncated event timeline,
      // establishes which approved configuration produced the current run.
      void request<{ approval?: RunApproval | null }[]>("/plans")
        .then((plans) => {
          if (active)
            setRunApproval(
              plans.find((p) => p.approval?.run_id === runId)?.approval ?? null,
            );
        })
        .catch(() => {
          /* Keep the existing unapplied-draft indication if unknown. */
        });
    }
    return () => {
      active = false;
    };
  }, [state?.run_id]);
  useEffect(() => {
    const runId = state?.run_id;
    if (!runId) return;
    if (previousNoticeRun.current && previousNoticeRun.current !== runId)
      setNotice("새 실행의 상태로 전환했습니다.");
    previousNoticeRun.current = runId;
    let active = true;
    let timer: ReturnType<typeof setTimeout>;
    recoveryDrafts.current.clear();
    setRuntimeProject(null);
    setMeshes([]);
    setSceneRunId("");
    setCameraFocusRequest(null);
    setCommandReceipt(null);
    setRecordingSeek(undefined);
    setError("");
    if (!isDraftPage(currentPage.current))
      setSelected(
        currentProject.current?.id === "example-elevator-pedestrian-60s"
          ? "sample-amr"
          : "",
      );
    setMoveTarget({ x: "0", y: "0", z: "0", yaw: "0" });
    const load = async () => {
      try {
        const before = await api.state();
        if (!active) return;
        if (before.run_id !== runId) {
          timer = setTimeout(load, 300);
          return;
        }
        const [p, m, s] = await Promise.all([
          api.project(),
          api.scene(),
          api.state(),
        ]);
        if (!active || currentState.current?.run_id !== runId) return;
        if (m.run_id !== runId || s.run_id !== runId) {
          timer = setTimeout(load, 300);
          return;
        }
        setRuntimeProject({ runId, project: p });
        appliedFingerprint.current = fingerprint(p);
        setDirty(
          !!currentProject.current &&
            fingerprint(currentProject.current) !== appliedFingerprint.current,
        );
        setMeshes(m.meshes ?? []);
        setSceneRunId(runId);
      } catch {
        if (active) timer = setTimeout(load, 1500);
      }
    };
    void load();
    return () => {
      active = false;
      clearTimeout(timer);
    };
  }, [state?.run_id, setSelected]);
  const commitDraft = useCallback((next: Project, remember = true) => {
    const prior = currentProject.current;
    if (!prior) return;
    const structure = projectStructureErrors(next);
    if (structure.length) {
      setError(
        `변경을 적용하지 못했습니다. 기존 초안은 보존됩니다. ${structure.join(" ")}`,
      );
      return;
    }
    if (fingerprint(prior) === fingerprint(next)) return;
    if (remember) {
      undoHistory.current.push(structuredClone(prior));
      if (undoHistory.current.length > 60) undoHistory.current.shift();
      redoHistory.current = [];
    }
    currentProject.current = next;
    setProject(next);
    setFloorId((id) =>
      next.environment.floors.some((floor) => floor.id === id)
        ? id
        : (next.environment.floors[0]?.id ?? ""),
    );
    setDirty(fingerprint(next) !== appliedFingerprint.current);
    setUnsaved(fingerprint(next) !== savedFingerprint.current);
    setUndoCount(undoHistory.current.length);
    setRedoCount(redoHistory.current.length);
  }, []);
  const edit = useCallback(
    (fn: (p: Project) => void) => {
      const prior = currentProject.current;
      if (!prior) return;
      const next = structuredClone(prior);
      fn(next);
      commitDraft(next);
    },
    [commitDraft],
  );
  const travelHistory = useCallback(
    (redo = false) => {
      const from = redo ? redoHistory.current : undoHistory.current,
        to = redo ? undoHistory.current : redoHistory.current;
      const next = from.pop(),
        prior = currentProject.current;
      if (!next || !prior) return;
      to.push(structuredClone(prior));
      commitDraft(next, false);
      setUndoCount(undoHistory.current.length);
      setRedoCount(redoHistory.current.length);
      const entities = [
        ...next.environment.elements,
        ...next.robots,
        ...next.people,
        ...next.items,
      ];
      const remaining =
        prior.id === next.id
          ? selectedIds.filter((id) =>
              entities.some((entity) => entity.id === id),
            )
          : [];
      // Keep the inspector on surviving edited objects; removed objects and
      // history across different projects must not retain a stale selection.
      setSelectedIds(remaining);
      const primary = remaining.includes(selected)
        ? selected
        : (remaining[0] ?? "");
      setSelectedValue(primary);
      setTool(null);
      setFloorId(
        (id) =>
          entities.find((entity) => entity.id === primary)?.floor_id ??
          (next.environment.floors.some((f) => f.id === id)
            ? id
            : (next.environment.floors[0]?.id ?? "")),
      );
      setNotice(
        redo ? "편집을 다시 실행했습니다." : "편집을 실행 취소했습니다.",
      );
    },
    [commitDraft, selected, selectedIds],
  );
  const checkDraft = () => {
    const p = currentProject.current;
    if (!p) throw new Error("프로젝트를 먼저 불러오세요.");
    const issues = validateProject(p);
    if (issues.length) throw new Error(issues.join(" "));
    if (document.querySelector('input[aria-invalid="true"]'))
      throw new Error("표시된 입력 오류를 수정한 뒤 저장·적용하세요.");
    return structuredClone(p);
  };
  const control = (action: string) =>
    run("실행 제어", async () => {
      const changesRun = action === "reset";
      if (changesRun) {
        stateEpoch.current++;
        runTransition.current = true;
      }
      try {
        if(action==='reset' && runApproval?.status==='accepted' && runApproval.run_id===currentState.current?.run_id) {
          const receipt=await request<RunApproval>(`/plans/${encodeURIComponent(runApproval.plan_id)}/reset`,'POST',{
            run_id:runApproval.run_id,
          });
          setRunApproval(receipt);
        } else if(runApproval && runApproval.run_id===currentState.current?.run_id && runApproval.status==='accepted' && ['start','resume','pause'].includes(action)) {
          await request(`/plans/${encodeURIComponent(runApproval.plan_id)}/control`,'POST',{
            run_id:runApproval.run_id,action:action==='pause'?'pause':'resume',
          });
        } else await api.control(action, action === "step" ? 1 : undefined, speed);
      } catch (error) {
        runTransition.current = false;
        // Rejected controls may pause a run. Never leave the old screen state
        // saying it is still running (or keep a stale success notice).
        setNotice("");
        await refresh().catch(() => {});
        throw error;
      } finally {
        if (changesRun) runTransition.current = false;
      }
      await refresh();
      setNotice(
        action === "step"
          ? "물리 한 단계 실행 결과를 수신했습니다."
          : action === "reset"
            ? "0초·초기 배치로 돌아왔습니다. 이전 기록은 보존되며 시작을 누르면 다시 실행합니다."
            : action === "pause"
              ? "시뮬레이션을 일시 정지했습니다."
              : "시뮬레이션 실행 상태를 확인했습니다.",
      );
    });
  const apply = () =>
    run("실행부 적용 중", async () => {
      const sent = checkDraft(),
        signature = fingerprint(sent),
        generation = draftGeneration.current;
      stateEpoch.current++;
      runTransition.current = true;
      let applied: Project;
      try {
        applied = await api.apply(sent);
      } finally {
        runTransition.current = false;
      }
      const appliedSignature = fingerprint(applied);
      appliedFingerprint.current = appliedSignature;
      // The server fills omitted schema defaults in imported older projects.
      // Adopt that response only while the exact submitted draft is still open.
      if (
        draftGeneration.current === generation &&
        currentProject.current &&
        fingerprint(currentProject.current) === signature
      ) {
        currentProject.current = applied;
        setProject(applied);
        setUnsaved(appliedSignature !== savedFingerprint.current);
      }
      setDirty(
        !!currentProject.current &&
          fingerprint(currentProject.current) !== appliedSignature,
      );
      await refresh();
      setNotice(
        "구성을 새 실행에 적용했습니다. 이후 편집 내용은 초안에 보존됩니다.",
      );
    });
  const save = async () => {
    if (savePending.current) return;
    savePending.current = true;
    const generation = draftGeneration.current;
    try {
      await run("프로젝트 저장 중", async () => {
        const sent = checkDraft(),
          signature = fingerprint(sent),
          result = await api.save(sent);
        const latest = currentProject.current;
        const sameDraft =
          generation === draftGeneration.current && latest?.id === sent.id;
        if (latest && sameDraft) {
          savedFingerprint.current = signature;
          const next = { ...latest, revision: result.revision };
          currentProject.current = next;
          setProject(next);
          setUnsaved(fingerprint(latest) !== signature);
          setSavedRevision(result.revision);
        }
        setNotice(
          `${sent.name} 버전 ${result.revision}을 저장했습니다.${!sameDraft ? " 현재 불러온 초안의 저장 상태는 변경하지 않았습니다." : latest && fingerprint(latest) !== signature ? " 저장 중 추가한 편집 내용은 초안에 남아 있습니다." : ""}`,
        );
        setSaved(await api.saved());
      });
    } finally {
      savePending.current = false;
    }
  };
  const preserveCurrentDraft = async () => {
    const current = currentProject.current;
    if (!current) return;
    const alreadySaved = saved.some((item) => item.id === current.id &&
      item.versions?.some((version) => version.revision === current.revision));
    if (alreadySaved && fingerprint(current) === savedFingerprint.current) return;
    const issues = validateProject(current);
    if (issues.length) throw new Error(`현재 초안을 보존할 수 없어 전환을 중단했습니다. ${issues.join(" ")}`);
    await api.save(structuredClone(current));
    setSaved(await api.saved());
  };
  const openSavedVersion = async (id: string, revision: number, prepare = false) => {
    const loaded = await api.load(id, revision);
    await preserveCurrentDraft();
    setFocusedDrawing(null);
    setFocusedPlan(null);
    if (prepare) {
      stateEpoch.current++;
      runTransition.current = true;
      try {
        const applied = await api.apply(loaded);
        adopt(applied, false);
        await refresh();
      } finally {
        runTransition.current = false;
      }
    } else adopt(loaded);
    savedFingerprint.current = fingerprint(loaded);
    setUnsaved(false);
    setSavedRevision(loaded.revision);
    setNotice(`${loaded.name} 저장 버전 ${revision}을 ${prepare ? "실행부에 적용했습니다. 시작을 누르면 시뮬레이션이 진행됩니다." : "초안으로 불러왔습니다."} 이전 초안도 작업 기록에 남아 있습니다.`);
  };
  const refreshSaved = useCallback(async () => { setSaved(await api.saved()); }, []);
  const loadExample = async (templateId: string, prepare: boolean) => {
    const loaded = await api.template(templateId);
    await preserveCurrentDraft();
    setFocusedDrawing(null);
    setFocusedPlan(null);
    if (!prepare) { adopt(loaded); return; }
    stateEpoch.current++;
    runTransition.current = true;
    try {
      const applied = await api.apply(loaded);
      adopt(applied, false);
      savedFingerprint.current = "";
      setUnsaved(true);
      setSavedRevision(null);
      await refresh();
      setNotice(`${loaded.name} 구성을 실행부에 적용했습니다. 시작을 누르면 시뮬레이션이 진행됩니다.`);
    } finally {
      runTransition.current = false;
    }
  };
  const openExperimentRun = async (experimentId: string, runId: string, prepare: boolean) => {
    const loaded = structuredClone(await api.experimentProject(experimentId, runId));
    // A historical run is a starting point for a new experiment, not a new
    // revision of its original project. Keep the source record untouched.
    loaded.id = `experiment-${experimentId}-${runId.slice(0, 8)}`;
    loaded.name += " · 실험 이어하기";
    loaded.revision = 1;
    await preserveCurrentDraft();
    setFocusedDrawing(null);
    setFocusedPlan(null);
    if (prepare) {
      stateEpoch.current++;
      runTransition.current = true;
      try {
        const applied = await api.apply(loaded);
        adopt(applied, false);
        await refresh();
      } finally {
        runTransition.current = false;
      }
    } else adopt(loaded);
    savedFingerprint.current = "";
    setUnsaved(true);
    setSavedRevision(null);
    setNotice(`실험 실행의 지도·로봇·사람·작업·정책·시드를 ${prepare ? "실행부에 적용했습니다. 시작 전에 구성을 확인하세요." : "초안으로 불러왔습니다."}`);
  };
  const sendCommand = (kind: string, target?: Pose) => {
    if (kind === "move") {
      const validation = validateMoveTarget(moveTarget, moveTargetFloor);
      if (!validation.target) {
        setError(validation.reason ?? "이동 목표를 확인하세요.");
        return;
      }
      target = validation.target;
    }
    const id = selected,
      runId = state?.run_id;
    if (!runId || commandPending.current.has(`${id}:${kind}`)) return;
    const key = `${id}:${kind}`;
    commandPending.current.add(key);
    setCommandReceipt({
      runId,
      robotId: id,
      value: { kind, status: "sending" },
    });
    void run("명령 요청 중", async () => {
      try {
        const result = await api.command(id, kind, target);
        if (currentState.current?.run_id === runId)
          setCommandReceipt({ runId, robotId: id, value: result });
        await refresh();
      } catch (e) {
        if (currentState.current?.run_id === runId)
          setCommandReceipt({
            runId,
            robotId: id,
            value: {
              kind,
              status:
                e instanceof ApiError && e.uncertain ? "unknown" : "rejected",
              reason: e instanceof Error ? e.message : String(e),
            },
          });
        throw e;
      } finally {
        commandPending.current.delete(key);
      }
    });
  };
  const displayProject = isDraftPage(page) ? project : matchedRuntimeProject;
  const selectedRobot = displayProject?.robots.find((r) => r.id === selected);
  const selectedModel = catalog.models.find(
    (m) => m.id === selectedRobot?.model_id,
  );
  const observed = state?.robots.find((r) => r.id === selected);
  // Manual routing uses the nearest landing to observed body Z minus .35 m.
  // Match that server floor choice; never use the draft or the viewed floor.
  const moveObservedZ = observed?.observed_pose?.z;
  const moveTargetFloor =
    matchedRuntimeProject &&
    typeof moveObservedZ === "number" &&
    Number.isFinite(moveObservedZ)
      ? ([...matchedRuntimeProject.environment.floors].sort(
          (a, b) =>
            Math.abs(moveObservedZ - a.elevation - 0.35) -
            Math.abs(moveObservedZ - b.elevation - 0.35),
        )[0] ?? null)
      : null;
  const moveValidation = validateMoveTarget(moveTarget, moveTargetFloor);
  const element = displayProject?.environment.elements.find(
    (e) => e.id === selected,
  );
  const measuredFacilities = state?.metrics.facilities as
    Record<string, Record<string, unknown>> | undefined;
  const selectedFacilityMetrics = selected
    ? measuredFacilities?.[selected]
    : undefined;
  const facilityMeasurement = (key: string) =>
    Number(selectedFacilityMetrics?.known_seconds ?? 0) > 0
      ? selectedFacilityMetrics?.[key]
      : undefined;
  const floor = project?.environment.floors.find((f) => f.id === floorId);
  const task = project?.tasks.find((t) => t.id === selectedTask);
  const cooperationErrors =
    project?.tasks.flatMap((entry) =>
      cooperativeIssues(entry, project).map(
        (message) => `${entry.name}: ${message}`,
      ),
    ) ?? [];
  const researchSettingsErrors: string[] = [];
  const finiteRange = (value: unknown, min: number, max: number) =>
    typeof value === "number" &&
    Number.isFinite(value) &&
    value >= min &&
    value <= max;
  if (
    project?.physics.impratio !== undefined &&
    !finiteRange(project.physics.impratio, 1, 100)
  )
    researchSettingsErrors.push(
      "접촉 임피던스 비는 1~100의 유한한 숫자로 입력하세요.",
    );
  for (const robot of project?.robots ?? []) {
    if (
      robot.gripper_kp !== undefined &&
      !finiteRange(robot.gripper_kp, 100, 2000)
    )
      researchSettingsErrors.push(
        `${robot.name} · ${robot.id}: 그리퍼 강성은 100~2000 N/m의 유한한 숫자로 입력하세요.`,
      );
    else if (
      robot.gripper_kp !== undefined &&
      robot.gripper_kp !== 400 &&
      !gripperResearchModels.has(robot.model_id)
    )
      researchSettingsErrors.push(
        `${robot.name} · ${robot.id}: 그리퍼 강성 변경은 연구용 고정형·이동형 팔에서만 지원합니다. 현재 모델은 기본값 400을 유지해야 합니다.`,
      );
  }
  const configurationErrors = [
    ...(project ? validateProject(project) : []),
    ...cooperationErrors,
    ...researchSettingsErrors,
  ];
  const updateRobot = (changes: Partial<RobotInstance>) =>
    edit((p) => {
      const r = p.robots.find((r) => r.id === selected);
      if (r) Object.assign(r, changes);
    });
  const updateElement = (changes: Partial<Element>) =>
    edit((p) => {
      const e = p.environment.elements.find((e) => e.id === selected);
      if (e) Object.assign(e, changes);
    });
  const updateTask = (changes: Partial<Task>) =>
    edit((p) => {
      const t = p.tasks.find((t) => t.id === selectedTask);
      if (t) Object.assign(t, changes);
    });
  const updateCooperation = (changes: Partial<CooperativeTask>) => {
    if (!task?.cooperation) return;
    updateTask({
      cooperation: { ...task.cooperation, ...changes },
      ...(changes.carrier_id !== undefined
        ? { preferred_robot: changes.carrier_id || null }
        : {}),
    });
  };
  const toggleCooperation = (enabled: boolean) => {
    if (!task || !project) return;
    if (!enabled) {
      updateTask({ cooperation: null });
      return;
    }
    const robots = project.robots.filter((r) => r.floor_id === task.floor_id);
    const carrier =
      robots.find((r) => r.id === task.preferred_robot) ??
      robots.find((r) =>
        ["delivery", "amr", "agv", "logistics", "mobile_manipulator"].includes(
          r.model_id,
        ),
      ) ??
      robots[0];
    const receiver =
      robots.find(
        (r) =>
          r.id !== carrier?.id &&
          ["arm", "mobile_manipulator"].includes(r.model_id),
      ) ?? robots.find((r) => r.id !== carrier?.id);
    const item =
      project.items.find(
        (i) => i.id === task.item_id && i.floor_id === task.floor_id,
      ) ?? project.items.find((i) => i.floor_id === task.floor_id);
    updateTask({
      cooperation: {
        carrier_id: carrier?.id ?? "",
        receiver_id: receiver?.id ?? "",
        workspace_id: `workspace-${task.id}`,
        carrier_destination: {
          ...(carrier?.pose ?? pose()),
          z: (carrier?.pose.z ?? 0) + 0.3,
        },
        donor_id: null,
        loading_offset: [0, 0],
      },
      item_id: item?.id ?? null,
      preferred_robot: carrier?.id ?? null,
    });
  };
  const addElement = (kind: ElementKind, x: number, y: number) => {
    const id = uid(kind);
    edit((p) =>
      p.environment.elements.push({
        id,
        kind,
        name: elementNames[kind],
        floor_id: floorId,
        pose: pose(x, y, 0),
        size: {
          x: kind === "wall" ? 3 : kind === "room" ? 4 : 1.5,
          y: kind === "wall" ? 0.15 : kind === "room" ? 3 : 1.5,
          z: kind === "wall" ? 2 : kind === "room" ? 0.05 : 0.4,
        },
        material: "concrete",
        friction: 0.8,
        mass: 20,
        slope: 0,
        step_height: 0.15,
        speed_limit: 0.5,
        allowed_groups: [],
        dynamic: kind === "obstacle",
        facility: {
          capacity: 1,
          max_load: 500,
          speed: 0.5,
          door_duration: 2,
          served_floors: [floorId],
          fault: false,
          automatic: true,
          charge_power_w: 400,
          charge_efficiency: 0.9,
        },
      }),
    );
    setSelected(id);
    setTool(null);
  };
  const moveEntity = (id: string, position: Pose) =>
    edit((p) => {
      const e = [
        ...p.environment.elements,
        ...p.robots,
        ...p.people,
        ...p.items,
      ].find((e) => e.id === id);
      if (e) e.pose = position;
    });
  const addRobots = (model: RobotModel) => {
    const count = Math.max(1, Math.floor(robotCounts[model.id] ?? 1));
    if (!Number.isSafeInteger(count)) {
      setError("로봇 대수는 양의 정수로 입력하세요.");
      return;
    }
    edit((p) => {
      const targetFloor = p.environment.floors.some(
        (floor) => floor.id === floorId,
      )
        ? floorId
        : (p.environment.floors[0]?.id ?? "");
      const floorElevation =
        p.environment.floors.find((floor) => floor.id === targetFloor)
          ?.elevation ?? 0;
      const zones = p.environment.id.startsWith("floorplan-")
        ? p.environment.elements.filter(
            (e) =>
              e.floor_id === targetFloor &&
              (e.kind === "room" || e.kind === "corridor"),
          )
        : [];
      for (let n = 0; n < count; n++) {
        const id = uid(model.id);
        const startZone = zones.length
          ? zones[p.robots.length % zones.length]
          : null;
        const zoneSlot = zones.length
          ? Math.floor(p.robots.length / zones.length)
          : 0;
        const clearance = Math.max(model.size.x, model.size.y) / 2 + 0.3;
        const zoneX = startZone
          ? Math.max(
              0,
              Math.min(startZone.size.x / 4, startZone.size.x / 2 - clearance),
            )
          : 0;
        const zoneY = startZone
          ? Math.max(
              0,
              Math.min(startZone.size.y / 4, startZone.size.y / 2 - clearance),
            )
          : 0;
        const zoneIndex = zones.length ? p.robots.length % zones.length : 0;
        p.robots.push({
          id,
          name: `${model.name} ${p.robots.filter((r) => r.model_id === model.id).length + 1}`,
          model_id: model.id,
          floor_id: targetFloor,
          pose: startZone
            ? pose(
                startZone.pose.x + (zoneIndex % 2 ? 1 : -1) * zoneX,
                startZone.pose.y + (zoneSlot % 2 ? -1 : 1) * zoneY,
                floorElevation,
              )
            : pose(
                2 + (n % 5) * 1.5,
                2 + Math.floor(n / 5) * 1.5,
                floorElevation,
              ),
          group: "기본",
          battery: 100,
          battery_capacity_wh: 400,
          estimated_drive_power_w: 120,
          payload_mass: 0,
          gripper_kp: 400,
          equipment: [],
          sensors: {
            position_noise: 0.01,
            yaw_noise: 0.005,
            observation_delay: 0.05,
            communication_delay: 0.02,
            dropout: 0,
            rate_hz: 20,
            camera: false,
            lidar: true,
            imu: true,
            item_tracking: true,
          },
          max_speed: Math.max(0.01, Math.min(0.5, model.max_speed)),
          controller: "default",
          fault: "none",
          agv_route: [],
        });
        setSelected(id);
      }
    });
  };
  const addTask = () => {
    const id = uid("task");
    edit((p) =>
      p.tasks.push({
        id,
        name: `작업 ${p.tasks.length + 1}`,
        kind: "patrol",
        destination: pose(2, 0, floor?.elevation ?? 0),
        floor_id: floorId,
        source: null,
        item_id: null,
        predecessor_ids: [],
        preferred_robot: null,
        priority: 5,
        release_time: 0,
        deadline: null,
        quantity: 1,
        interval: 0,
        retries: 1,
        timeout: 120,
        dwell: 1,
        cooperation: null,
      }),
    );
    setSelectedTask(id);
  };
  const transformEntities = (changes: EntityTransform[]) => {
    if (currentProject.current)
      commitDraft(transformed(currentProject.current, changes));
  };
  const copySelection = () => {
    if (!currentProject.current || !selectedIds.length) return;
    const result = duplicateEntities(currentProject.current, selectedIds, uid);
    commitDraft(result.project);
    setSelectedValue(result.ids.at(-1) ?? "");
    setSelectedIds(result.ids);
    setNotice(
      `${result.ids.length}개 객체를 복제했습니다. 실행 취소로 되돌릴 수 있습니다.`,
    );
  };
  const deleteSelection = () => {
    if (!currentProject.current || !selectedIds.length) return;
    const references = deletionReferences(currentProject.current, selectedIds);
    if (references.length) {
      setError(
        `선택한 객체를 사용하는 작업이 있습니다: ${references.join(", ")}. 해당 작업의 물품·참여 로봇 설정을 먼저 변경하세요.`,
      );
      return;
    }
    edit((p) => {
      p.environment.elements = p.environment.elements.filter(
        (e) => !selectedIds.includes(e.id),
      );
      p.robots = p.robots.filter((e) => !selectedIds.includes(e.id));
      p.people = p.people.filter((e) => !selectedIds.includes(e.id));
      p.items = p.items.filter((e) => !selectedIds.includes(e.id));
    });
    setSelected("");
    setNotice("선택한 객체를 삭제했습니다. 실행 취소로 복원할 수 있습니다.");
  };
  const entityFloor = (p: Project, id: string, editing: boolean) => {
    const entity = [
      ...p.robots,
      ...p.environment.elements,
      ...p.people,
      ...p.items,
    ].find((e) => e.id === id);
    if (!entity || editing) return entity?.floor_id;
    const robot = state?.robots.find((r) => r.id === id);
    if (robot)
      return floorAtHeight(p.environment.floors, robot.pose.z, entity.floor_id);
    const person = p.people.some((e) => e.id === id);
    const geom = state?.geoms.find(
      (g) => g.name === `${id}/${person ? "torso" : "shape"}`,
    );
    const dynamic =
      person ||
      p.items.some((e) => e.id === id) ||
      ("dynamic" in entity && entity.dynamic);
    if (dynamic && geom)
      return floorAtHeight(
        p.environment.floors,
        geom.position[2] -
          (person ? 0.85 : "size" in entity ? entity.size.z / 2 : 0),
        entity.floor_id,
      );
    return entity.floor_id;
  };
  const chooseEntity = (id: string) => {
    setCameraFocusRequest(null);
    setSelected(id);
    setInspectorOpen(true);
    const p =
      view === "3d" && (page === "environment" || page === "monitor")
        ? runtimeProject && runtimeProject.runId === state?.run_id
          ? runtimeProject.project
          : null
        : page === "environment"
          ? project
          : displayProject;
    const nextFloor =
      p &&
      entityFloor(
        p,
        id,
        view !== "3d" &&
          (page === "environment" || page === "robots" || page === "scenario"),
      );
    if (nextFloor) setFloorId(nextFloor);
  };
  const cameraFocusReason = (id: string) => {
    if (!matchedRuntimeProject || sceneRunId !== state?.run_id)
      return "현재 실행의 3D 형상을 받는 중입니다. 연결 후 다시 선택하세요.";
    if (
      !state?.robots.some((robot) => robot.id === id) &&
      !matchedRuntimeProject.people.some((person) => person.id === id) &&
      !matchedRuntimeProject.items.some((item) => item.id === id)
    )
      return "현재 실행에 없는 대상입니다. 계획을 승인하거나 초안을 적용한 뒤 확인하세요.";
    if (!state.geoms.some((geom) => geom.entity_id === id))
      return "이 대상의 물리 형상을 아직 받지 못했습니다. 연결 상태를 확인하세요.";
    return "";
  };
  const showRobotIn3D = (id: string) => {
    const reason = cameraFocusReason(id);
    if (reason) {
      setNotice(reason);
      return;
    }
    // Observation-only navigation: no draft edit, robot command, or run mutation.
    navigate("monitor");
    setView("3d");
    setSelected(id);
    setInspectorOpen(true);
    setCameraFocusRequest({ id, sequence: ++cameraFocusSequence.current });
    // PhysicsView changes the floor after saving the previous camera view.
  };
  const relatedEventEntity = (event: RuntimeEvent) => {
    const p =
      runtimeProject && runtimeProject.runId === state?.run_id
        ? runtimeProject.project
        : null;
    if (!p) return undefined;
    const ids = new Set(
      [...p.robots, ...p.people, ...p.items, ...p.environment.elements].map(
        (e) => e.id,
      ),
    );
    const detail = event.details ?? {};
    const taskState = state?.tasks.find(
      (t) => t.id === event.entity_id || t.id === detail.task_id,
    );
    const taskConfig = p.tasks.find(
      (t) => t.id === taskState?.id || t.id === event.entity_id,
    );
    const candidates = [
      event.entity_id,
      detail.robot_id,
      detail.carrier_id,
      detail.receiver_id,
      detail.donor_id,
      detail.item_id,
      detail.station_id,
      detail.elevator_id,
      detail.a,
      detail.b,
      taskState?.robot_id,
      ...(taskState?.participant_ids ?? []),
      taskConfig?.item_id,
      taskConfig?.preferred_robot,
    ];
    return candidates.find(
      (id): id is string => typeof id === "string" && ids.has(id),
    );
  };
  useEffect(() => {
    const handle = (event: KeyboardEvent) => {
      const writing = (event.target as HTMLElement)?.closest(
        'input,textarea,select,[contenteditable="true"]',
      );
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "s") {
        event.preventDefault();
        void save();
        return;
      }
      if (writing) return;
      if (
        (event.metaKey || event.ctrlKey) &&
        ["z", "y"].includes(event.key.toLowerCase())
      ) {
        event.preventDefault();
        travelHistory(event.shiftKey || event.key.toLowerCase() === "y");
      }
      if (
        page === "environment" &&
        (event.metaKey || event.ctrlKey) &&
        event.key.toLowerCase() === "d"
      ) {
        event.preventDefault();
        copySelection();
      }
      if (
        page === "environment" &&
        ["Delete", "Backspace"].includes(event.key) &&
        selectedIds.length
      ) {
        event.preventDefault();
        deleteSelection();
      }
      if (event.key === "Escape") {
        setTool(null);
        setSelected("");
      }
    };
    window.addEventListener("keydown", handle);
    return () => window.removeEventListener("keydown", handle);
  });
  const objectRows = displayProject
    ? [
        ...displayProject.robots.map((e) => ({
          ...e,
          category: "robots",
          kindLabel:
            catalog.models.find((m) => m.id === e.model_id)?.name ?? e.model_id,
        })),
        ...displayProject.environment.elements.map((e) => ({
          ...e,
          category: "elements",
          kindLabel: elementNames[e.kind],
        })),
        ...displayProject.people.map((e) => ({
          ...e,
          category: "people",
          kindLabel: "사람",
        })),
        ...displayProject.items.map((e) => ({
          ...e,
          category: "items",
          kindLabel: "물품",
        })),
      ].filter(
        (e) =>
          ((page === "monitor" && e.category === "robots") ||
            entityFloor(
              displayProject,
              e.id,
              page === "environment" ||
                page === "robots" ||
                page === "scenario",
            ) === floorId) &&
          (objectFilter === "all" ||
            e.category === objectFilter ||
            (objectFilter.startsWith("model:") &&
              "model_id" in e &&
              e.model_id === objectFilter.slice(6))) &&
          `${e.name} ${e.id} ${e.kindLabel}`
            .toLowerCase()
            .includes(objectSearch.toLowerCase()),
      )
    : [];
  const paletteGroups: { name: string; items: ElementKind[] }[] = [
    {
      name: "공간과 구조",
      items: [
        "room",
        "corridor",
        "wall",
        "column",
        "door",
        "stairs",
        "ramp",
        "obstacle",
      ],
    },
    {
      name: "시설과 작업",
      items: [
        "elevator",
        "charger",
        "dock",
        "loading",
        "shelf",
        "workbench",
        "conveyor",
      ],
    },
    {
      name: "운영 구역",
      items: ["waiting", "restricted", "speed_zone", "one_way", "entrance"],
    },
  ];
  const visiblePaletteGroups = paletteGroups
    .map((group) => ({
      ...group,
      items: group.items.filter((kind) =>
        elementNames[kind].includes(toolSearch.trim()),
      ),
    }))
    .filter((group) => group.items.length > 0);
  const robotTable = (
    source: "draft" | "runtime",
    filteredRobots?: RobotInstance[],
  ) => {
    const tableProject = source === "draft" ? project : matchedRuntimeProject;
    const robots = filteredRobots ?? tableProject?.robots ?? [];
    const selectRobot = source === "runtime" ? chooseEntity : setSelected;
    return (
      <div className="table-wrap">
        <table>
          <thead>
            <tr>
              <th>{source === "draft" ? "로봇 / 초안 개체" : "로봇 / 개체"}</th>
              <th>{source === "draft" ? "현재 실행 상태" : "상태"}</th>
              <th>{source === "draft" ? "초안 배터리" : "관측 배터리"}</th>
              <th>{source === "draft" ? "현재 실행 작업" : "작업"}</th>
              <th>관측 나이</th>
              <th>대기·실패 이유</th>
              <th>관찰</th>
            </tr>
          </thead>
          <tbody>
            {robots.map((r) => {
              const s = matchedRuntimeProject
                ? state?.robots.find((x) => x.id === r.id)
                : undefined;
              return (
                <tr
                  key={r.id}
                  className={`selectable ${selected === r.id ? "selected" : ""}`}
                  onClick={() => selectRobot(r.id)}
                >
                  <td>
                    <button className="ghost" onClick={() => selectRobot(r.id)}>
                      <RobotIcon model={r.model_id} size={15} />
                      <strong>{r.name}</strong>
                    </button>
                    <small className="muted">{r.id}</small>
                  </td>
                  <td>
                    <Badge
                      value={
                        s?.status ??
                        (matchedRuntimeProject && source === "draft"
                          ? "미적용"
                          : "미수신")
                      }
                    />
                  </td>
                  <td className="number">
                    {fmt(source === "draft" ? r.battery : s?.battery, 1)}%
                  </td>
                  <td>
                    {matchedRuntimeProject?.tasks.find(
                      (t) => t.id === s?.task_id,
                    )?.name ??
                      s?.task_id ??
                      "—"}
                  </td>
                  <td className="number">{fmt(s?.observation_age, 3)} s</td>
                  <td>{s?.reason ? robotReasonLabel(s.reason) : "—"}</td>
                  <td>
                    <button
                      className="ghost"
                      disabled={!!cameraFocusReason(r.id)}
                      title={
                        cameraFocusReason(r.id) ||
                        "현재 실행 위치로 카메라만 이동합니다"
                      }
                      aria-label={`${r.name} 3D에서 보기`}
                      onClick={(event) => {
                        event.stopPropagation();
                        showRobotIn3D(r.id);
                      }}
                    >
                      3D에서 보기
                    </button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
        {!robots.length && (
          <Empty
            title={
              source === "runtime" && !tableProject
                ? "현재 실행 구성을 기다리고 있습니다"
                : tableProject?.robots.length
                  ? "검색 조건에 맞는 로봇이 없습니다"
                  : source === "runtime"
                    ? "현재 실행에 로봇이 없습니다"
                    : "배치된 로봇이 없습니다"
            }
          >
            {source === "runtime"
              ? "실행 구성과 상태를 수신하면 현재 실행의 로봇이 표시됩니다."
              : tableProject?.robots.length
                ? "검색어를 지우거나 다른 이름·모델·ID를 입력하세요."
                : "모델 추가에서 모델과 대수를 선택하세요."}
          </Empty>
        )}
      </div>
    );
  };
  const inspectorProject =
    runtimeProject?.runId === state?.run_id ? runtimeProject?.project : null;
  const faultTargets = inspectorProject
    ? [
        ...inspectorProject.robots,
        ...inspectorProject.environment.elements.filter((element) =>
          ["elevator", "door", "charger"].includes(element.kind),
        ),
      ]
    : [];
  const faultTargetAvailable = faultTargets.some(
    (target) => target.id === selected,
  );
  const inspectedItem = inspectorProject?.items.find(
    (item) => item.id === selected,
  );
  const inspectedPerson = inspectorProject?.people.find(
    (person) => person.id === selected,
  );
  const inspectedOther = inspectedItem ?? inspectedPerson;
  const inspectedGeometries = inspectedOther
    ? (state?.geoms ?? []).filter(
        (geom) =>
          geom.entity_id === inspectedOther.id &&
          geom.position.length === 3 &&
          geom.position.every(Number.isFinite),
      )
    : [];
  // These are received physics geometry centers, not inferred sensor observations or draft coordinates.
  const inspectedGeometry =
    inspectedGeometries.find(
      (geom) =>
        geom.name === `${selected}/${inspectedItem ? "shape" : "torso"}`,
    ) ??
    (inspectedGeometries.length === 1 ? inspectedGeometries[0] : undefined);
  const inspectedFloor = inspectedGeometry
    ? [...(inspectorProject?.environment.floors ?? [])]
        .sort((a, b) => b.elevation - a.elevation)
        .find(
          (floor) => inspectedGeometry.position[2] >= floor.elevation - 0.06,
        )
    : undefined;
  const equipmentLabels: Record<string, string> = {
    cargo_tray: "적재함",
    arm: "로봇팔",
    gripper: "그리퍼",
    inspection_camera: "점검 카메라",
  };
  const custodyLabels: Record<string, string> = {
    unassigned: "소유 미배정",
    observed_held: "관측에 따라 보유",
    observed_released: "해제 관측",
    observed_cooperative: "협업 보유 보고",
    observed_recovery: "복구 중 보유 보고",
    recovery_required: "복구 확인 필요",
    custody_pending: "소유권 확인 대기",
  };
  const payloadRecord = (value: unknown): Record<string, unknown> | null =>
    value && typeof value === "object" && !Array.isArray(value)
      ? (value as Record<string, unknown>)
      : null;
  const payloadId = (value: unknown): string | null => {
    const row = payloadRecord(value);
    return typeof row?.id === "string"
      ? row.id
      : typeof value === "string"
        ? value
        : null;
  };
  const payloadLabel = (value: unknown, index: number) => {
    const row = payloadRecord(value),
      id = payloadId(value);
    const name =
      typeof row?.name === "string"
        ? row.name
        : (inspectorProject?.items.find((item) => item.id === id)?.name ?? id);
    const mass =
      typeof row?.mass === "number" && Number.isFinite(row.mass)
        ? ` · ${fmt(row.mass, 3)} kg`
        : "";
    const custody =
      typeof row?.custody === "string"
        ? ` · ${custodyLabels[row.custody] ?? row.custody}`
        : "";
    return `${name || `식별되지 않은 적재 보고 ${index + 1}`}${mass}${custody}`;
  };
  const inspectedHolders = inspectedItem
    ? (state?.robots ?? []).filter(
        (robot) =>
          Array.isArray(robot.payload) &&
          robot.payload.some((entry) => payloadId(entry) === inspectedItem.id),
      )
    : [];
  const inspectedTasks = inspectedItem
    ? (inspectorProject?.tasks ?? []).filter(
        (task) => task.item_id === inspectedItem.id,
      )
    : [];
  const inspectedCustody = inspectedItem
    ? Object.entries(state?.cooperation?.executions ?? {}).filter(
        ([, execution]) => execution.item_id === inspectedItem.id,
      )
    : [];
  const renderChargingWorkflow = () =>
    selectedRobot && inspectorProject && observed?.charging_workflow ? (
      <ChargingWorkflowPanel
        report={observed.charging_workflow}
        robotId={selectedRobot.id}
        project={inspectorProject}
        now={state?.sim_time ?? 0}
        live={live}
        runId={state?.run_id}
        consumption={observed.consumption_meter}
        robotState={{
          status: observed.status,
          reason: observed.reason,
          operator_hold: observed.operator_hold,
          observation_age: observed.observation_age,
        }}
        busy={!!busy}
        resumeAllowed={
          live &&
          observed.status !== "fault" &&
          !!(
            observed.operator_hold ||
            (observed.status === "recovery_required" &&
              observed.charging_station_id)
          )
        }
        onResume={() => {
          void run("로봇 운영 재개 요청", () => api.resumeRobot(selected));
        }}
      />
    ) : null;
  const runtimeInspector = () =>
    selectedRobot ? (
      <>
        <div className="section-head">
          <h2>{selectedRobot.name}</h2>
          <Badge value={observed?.status ?? "미적용"} />
        </div>
        <p className="muted" style={{ fontSize: 12 }}>
          {selectedModel?.name ?? selectedRobot.model_id} ·{" "}
          {selectedRobot.group}
        </p>
        {chargingWorkflowIsActive(observed?.charging_workflow) &&
          renderChargingWorkflow()}
        <dl className="kv">
          <dt>개체 ID</dt>
          <dd>{selectedRobot.id}</dd>
          <dt>경로</dt>
          <dd>{observed?.path.length ?? 0}개 경유점</dd>
          <dt>위치 · 관측 (m)</dt>
          <dd>
            {observed?.observed_pose
              ? [
                  observed.observed_pose.x,
                  observed.observed_pose.y,
                  observed.observed_pose.z,
                ]
                  .map((v) => fmt(v))
                  .join(" / ")
              : "—"}
          </dd>
          <dt>방향 (rad)</dt>
          <dd>{fmt(observed?.observed_pose?.yaw)}</dd>
          <dt>배터리</dt>
          <dd>{fmt(observed?.battery, 1)} %</dd>
          <dt>충전 입력</dt>
          <dd>{fmt(observed?.charging_power_w, 1)} W</dd>
          <dt>현재 작업</dt>
          <dd>
            {inspectorProject?.tasks.find((t) => t.id === observed?.task_id)
              ?.name ??
              observed?.task_id ??
              "—"}
          </dd>
          <dt>보고된 적재물</dt>
          <dd>
            {Array.isArray(observed?.payload)
              ? observed.payload.length
                ? observed.payload.map((entry, index) => (
                    <div key={`${payloadId(entry) ?? "unknown"}-${index}`}>
                      {payloadLabel(entry, index)}
                    </div>
                  ))
                : "적재 목록에 보고된 물품 없음"
              : "실행부 적재 보고 없음"}
          </dd>
          <dt>장착 장비</dt>
          <dd>
            {selectedRobot.equipment
              .map(
                (equipment) =>
                  equipmentLabels[equipment.kind] ?? equipment.kind,
              )
              .join(", ") || "추가 장비 없음"}
          </dd>
          <dt>초기 추가 하중</dt>
          <dd>
            {fmt(selectedRobot.payload_mass, 3)} kg{" "}
            <small className="muted">· 구성값</small>
          </dd>
          <dt>관측 지연</dt>
          <dd>{fmt(observed?.observation_age, 3)} s</dd>
          <dt>대기·실패 이유</dt>
          <dd>{observed?.reason ? robotReasonLabel(observed.reason) : "—"}</dd>
        </dl>
        <PedestrianSafetyPanel
          report={observed?.pedestrian_avoidance}
          metrics={state?.metrics.pedestrian_safety}
          robotId={selectedRobot.id}
          project={inspectorProject ?? null}
          now={state?.sim_time ?? 0}
          live={live}
          robotStatus={observed?.status}
          robotReason={observed?.reason ?? undefined}
          operatorHold={observed?.operator_hold}
        />
        <MotionLimitPanel
          report={observed?.motion_limit}
          project={inspectorProject ?? null}
          now={state?.sim_time ?? 0}
          live={live}
        />
        <EnergyConsumptionPanel
          report={observed?.consumption_meter}
          runId={state?.run_id}
          robotId={selectedRobot.id}
          now={state?.sim_time ?? 0}
          live={live}
          staleAfter={inspectorProject?.policy.stale_after}
        />
        {!chargingWorkflowIsActive(observed?.charging_workflow) &&
          chargingWorkflowHasHistory(observed?.charging_workflow) && (
            <details className="charging-workflow-history">
              <summary>충전 이력</summary>
              {renderChargingWorkflow()}
            </details>
          )}
        {observed?.charging_energy &&
          inspectorProject &&
          selectedModel &&
          ["differential", "guided"].includes(selectedModel.locomotion) && (
            <ChargingEnergyPanel
              report={observed.charging_energy}
              robotState={{
                status: observed.status,
                reason: observed.reason,
                operator_hold: observed.operator_hold,
                observation_age: observed.observation_age,
              }}
              reservedStationId={observed.charging_station_id}
              project={inspectorProject}
              now={state?.sim_time ?? 0}
              live={live}
            />
          )}
        <div className="toolbar">
          <button
            disabled={!live}
            title={
              !live
                ? "실행부에 다시 연결되면 정지 명령을 보낼 수 있습니다."
                : "로봇 제어기에 정지를 요청합니다."
            }
            onClick={() => sendCommand("stop")}
          >
            <Square size={13} />
            로봇 정지
          </button>
          <button
            disabled={
              !live ||
              !!busy ||
              !(
                observed?.operator_hold ||
                (observed?.status === "recovery_required" &&
                  observed?.charging_station_id)
              )
            }
            title="자동 배정과 예약된 하차·충전을 재개합니다. 취소한 작업은 다시 생성되지 않습니다."
            onClick={() =>
              run("로봇 운영 재개 요청", () => api.resumeRobot(selected))
            }
          >
            운영 재개
          </button>
          {selectedModel?.kind === "quadruped" && (
            <>
              <button
                disabled={!live || !!busy}
                title={
                  !live
                    ? "새 관측을 수신한 뒤 명령을 보낼 수 있습니다."
                    : busy
                      ? "진행 중인 요청의 응답을 기다리고 있습니다."
                      : "관측으로 서기 명령의 결과를 확인합니다."
                }
                onClick={() => sendCommand("stand")}
              >
                서기
              </button>
              <button
                disabled={!live || !!busy}
                title={
                  !live
                    ? "새 관측을 수신한 뒤 명령을 보낼 수 있습니다."
                    : busy
                      ? "진행 중인 요청의 응답을 기다리고 있습니다."
                      : "관측으로 앉기 명령의 결과를 확인합니다."
                }
                onClick={() => sendCommand("sit")}
              >
                앉기
              </button>
            </>
          )}
        </div>
        {selectedModel?.locomotion !== "fixed" && (
          <details className="details">
            <summary>이동 명령</summary>
            <div className="form-grid">
              {(["x", "y", "z", "yaw"] as const).map((axis) => {
                const label =
                  axis === "yaw"
                    ? "방향 (rad)"
                    : `목표 ${axis.toUpperCase()} (m)`;
                const inputError = moveValidation.errors[axis];
                return (
                  <label key={axis}>
                    {label}
                    <input
                      type="number"
                      step="any"
                      required
                      min={axis === "x" || axis === "y" ? 0 : undefined}
                      max={
                        axis === "x"
                          ? moveTargetFloor?.width
                          : axis === "y"
                            ? moveTargetFloor?.depth
                            : undefined
                      }
                      value={moveTarget[axis]}
                      aria-label={label}
                      aria-invalid={!!inputError || undefined}
                      aria-describedby={
                        inputError
                          ? `move-target-${axis}-error`
                          : "move-target-guidance"
                      }
                      onChange={(event) =>
                        setMoveTarget((previous) => ({
                          ...previous,
                          [axis]: event.target.value,
                        }))
                      }
                    />
                    {inputError && (
                      <small
                        id={`move-target-${axis}-error`}
                        className="field-error"
                        role="status"
                      >
                        {inputError}
                      </small>
                    )}
                  </label>
                );
              })}
            </div>
            <p id="move-target-guidance" className="panel-hint">
              {moveTargetFloor
                ? `${moveTargetFloor.name} 기준 · X 0~${moveTargetFloor.width} m · Y 0~${moveTargetFloor.depth} m. 몸체 간격과 장애물 경로는 실행부에서 추가로 검사합니다. Z 입력으로 다른 층으로 이동하지 않습니다.`
                : "현재 실행의 로봇 관측과 층 구성을 수신한 뒤 목표 범위를 확인하세요."}
            </p>
            <button
              style={{ marginTop: 12 }}
              disabled={!live || !!busy || !moveValidation.target}
              title={
                !live
                  ? "새 관측을 수신한 뒤 명령을 보낼 수 있습니다."
                  : busy
                    ? "진행 중인 요청의 응답을 기다리고 있습니다."
                    : (moveValidation.reason ??
                      "경로와 로봇 능력을 검사한 뒤 이동을 요청합니다.")
              }
              onClick={() => sendCommand("move")}
            >
              이동 요청
            </button>
          </details>
        )}
        {observed?.task_id && (
          <button
            className="danger"
            disabled={!live || !!busy}
            onClick={() =>
              run("작업 취소 요청", () => api.cancelTask(observed.task_id!))
            }
          >
            현재 작업 취소 요청
          </button>
        )}
        {(() => {
          const receipt =
            commandReceipt?.runId === state?.run_id &&
            commandReceipt?.robotId === selected
              ? commandReceipt.value
              : null;
          const reported = observed?.last_command;
          const feedback =
            reported &&
            (typeof reported.status === "string" ||
              typeof reported.command_id === "string")
              ? reported
              : null;
          const active =
            receipt && receipt.command_id !== feedback?.command_id
              ? receipt
              : (feedback ?? receipt);
          return (
            <section className="command-feedback" aria-live="polite">
              <h3>최근 명령</h3>
              {active ? (
                <>
                  <strong>
                    {commandStatusLabel(String(active.status ?? "unknown"))}
                  </strong>
                  <p>{commandFeedbackSummary(active)}</p>
                  {active.command_id ? (
                    <small>명령 {String(active.command_id).slice(0, 12)}</small>
                  ) : null}
                </>
              ) : (
                <p>이 로봇의 명령 이력이 없습니다.</p>
              )}
            </section>
          );
        })()}
        <JsonDetails
          title="최근 명령과 피드백"
          data={observed?.last_command ?? { message: "명령 이력 없음" }}
        />
        <JsonDetails title="센서 관측 보고" data={observed?.sensors} />
        <JsonDetails
          title="적재물 보고와 장비 구성 상세"
          data={{
            payload: observed?.payload ?? null,
            equipment: selectedRobot.equipment,
            initial_payload_mass_kg: selectedRobot.payload_mass,
          }}
        />
        <JsonDetails title="관절 실제 상태 · 평가용" data={observed?.joints} />
      </>
    ) : element ? (
      <>
        <h2>{element.name}</h2>
        <p className="muted">
          {elementNames[element.kind]} · {element.id}
        </p>
        <JsonDetails
          title="현재 시설 상태"
          data={
            state?.facilities.find(
              (f) => f.id === element.id || f.entity_id === element.id,
            ) ?? { message: "시설 상태 보고가 없습니다." }
          }
        />
        <button onClick={() => navigate("facilities")}>
          시설과 예약에서 보기
        </button>
      </>
    ) : inspectedOther ? (
      <>
        <div className="section-head">
          <h2>{inspectedOther.name}</h2>
          <Badge
            value={
              inspectedGeometries.length ? "물리 형상 수신" : "형상 보고 없음"
            }
          />
        </div>
        <p className="muted">
          {inspectedItem ? "물품" : "사람"} · {inspectedOther.id}
        </p>
        {inspectedPerson && inspectorProject && (
          <>
            <button
              disabled={!!cameraFocusReason(inspectedPerson.id)}
              title={
                cameraFocusReason(inspectedPerson.id) ||
                "선택한 사람에게 카메라 이동"
              }
              onClick={() => showRobotIn3D(inspectedPerson.id)}
            >
              3D에서 보기
            </button>
            <PedestrianInspector
              person={inspectedPerson}
              runtime={state?.people?.[inspectedPerson.id]}
              project={inspectorProject}
              connected={live}
              simTime={state?.sim_time}
            />
          </>
        )}
        <dl className="kv">
          <dt>현재 위치 · 형상 중심 (m)</dt>
          <dd>
            {inspectedGeometry
              ? inspectedGeometry.position
                  .map((value) => fmt(value, 3))
                  .join(" / ")
              : inspectedGeometries.length
                ? "아래 형상별 위치 참조"
                : "확인할 물리 형상 없음"}
          </dd>
          <dt>현재 층 · 중심 높이 기준</dt>
          <dd>{inspectedFloor?.name ?? "현재 형상으로 확인되지 않음"}</dd>
          <dt>물리 상태 시각</dt>
          <dd>
            {fmt(state?.sim_time, 3)} s{!live ? " · 마지막 수신값" : ""}
          </dd>
          <dt>초기 위치 설정 · 층 기준 (m)</dt>
          <dd>
            {[
              inspectedOther.pose.x,
              inspectedOther.pose.y,
              inspectedOther.pose.z,
            ]
              .map((value) => fmt(value, 3))
              .join(" / ")}
          </dd>
          <dt>초기 층 설정</dt>
          <dd>
            {inspectorProject?.environment.floors.find(
              (floor) => floor.id === inspectedOther.floor_id,
            )?.name ?? inspectedOther.floor_id}
          </dd>
          <dt>질량 · 구성값</dt>
          <dd>{fmt(inspectedOther.mass, 3)} kg</dd>
          {inspectedItem ? (
            <>
              <dt>크기 · 구성값 (m)</dt>
              <dd>
                {[
                  inspectedItem.size.x,
                  inspectedItem.size.y,
                  inspectedItem.size.z,
                ]
                  .map((value) => fmt(value, 3))
                  .join(" / ")}
              </dd>
              <dt>보유 로봇 · 적재 보고</dt>
              <dd>
                {inspectedHolders.length
                  ? inspectedHolders.map((robot) => (
                      <div key={robot.id}>
                        {robot.name} · {robot.id}
                      </div>
                    ))
                  : "로봇 적재 목록에 보고되지 않음"}
              </dd>
            </>
          ) : inspectedPerson ? (
            <>
              <dt>이동 경로 설정</dt>
              <dd>{inspectedPerson.path.length}개 경유점</dd>
              <dt>이동 속도 설정</dt>
              <dd>{fmt(inspectedPerson.speed)} m/s</dd>
            </>
          ) : null}
        </dl>
        <p className="muted">
          {inspectedGeometries.length
            ? "현재 위치는 실행부의 물리 형상 중심입니다. 로봇 센서 관측·초기 배치 좌표와 기준이 다릅니다."
            : "현재 실행에서 일치하는 물리 형상을 받지 못했습니다. 초기 설정을 현재 위치로 표시하지 않습니다."}
        </p>
        {inspectedGeometries.length > 1 && (
          <details className="details">
            <summary>형상별 현재 중심 위치</summary>
            <dl className="kv">
              {inspectedGeometries.map((geom) => (
                <Fragment key={geom.id}>
                  <dt>{geom.name}</dt>
                  <dd>
                    {geom.position.map((value) => fmt(value, 3)).join(" / ")} m
                  </dd>
                </Fragment>
              ))}
            </dl>
          </details>
        )}
        {inspectedItem && (
          <section className="command-feedback">
            <h3>관련 작업과 적재</h3>
            {inspectedTasks.length ? (
              inspectedTasks.map((task) => {
                const report = state?.tasks.find(
                  (entry) => entry.id === task.id,
                );
                return (
                  <div key={task.id}>
                    <strong>{task.name}</strong>
                    <p>
                      {report
                        ? (statusNames[report.status] ?? report.status)
                        : "실행 보고 없음"}
                      {report?.reason ? ` · ${report.reason}` : ""}
                    </p>
                    <small className="muted">{task.id}</small>
                  </div>
                );
              })
            ) : (
              <p>이 물품을 지정한 작업이 없습니다.</p>
            )}
            {inspectedCustody.length > 0 && (
              <details className="details">
                <summary>협업 소유권 보고</summary>
                {inspectedCustody.map(([id, entry]) => (
                  <p key={id}>
                    {entry.owner
                      ? `${state?.robots.find((robot) => robot.id === entry.owner)?.name ?? entry.owner} · ${entry.owner}`
                      : "소유 로봇 없음"}
                    <small className="muted"> · 실행 {id.slice(0, 12)}</small>
                  </p>
                ))}
              </details>
            )}
            <small className="muted">
              적재 목록과 소유권 보고만으로 현재 접촉·지지 상태를 판정하지
              않습니다.
            </small>
          </section>
        )}
        <JsonDetails title="현재 물리 형상 원본" data={inspectedGeometries} />
        <JsonDetails
          title={inspectedItem ? "물품 구성 상세" : "보행자 경로와 구성 상세"}
          data={inspectedOther}
        />
      </>
    ) : (
      <Empty title="객체를 선택하세요">
        도면이나 목록에서 로봇·시설·사람·물품을 선택하면 현재 실행의 정보를
        확인할 수 있습니다.
      </Empty>
    );
  const selectedOther = [
    ...(project?.people ?? []),
    ...(project?.items ?? []),
  ].find((e) => e.id === selected);
  const updateOther = (changes: Partial<Person & Item>) =>
    edit((p) => {
      const entity = [...p.people, ...p.items].find((e) => e.id === selected);
      if (entity) Object.assign(entity, changes);
    });
  const elementInspector = () =>
    element ? (
      <>
        <div className="section-head">
          <h2>{elementNames[element.kind]}</h2>
          <button
            className="ghost danger"
            aria-label="선택 요소 삭제"
            onClick={deleteSelection}
          >
            <Trash2 size={15} />
          </button>
        </div>
        <label>
          이름
          <input
            value={element.name}
            onChange={(e) => updateElement({ name: e.target.value })}
          />
        </label>
        <div className="form-grid">
          <label className="span-2">
            층
            <select
              value={element.floor_id}
              onChange={(e) => {
                updateElement({ floor_id: e.target.value });
                setFloorId(e.target.value);
              }}
            >
              {project?.environment.floors.map((f) => (
                <option key={f.id} value={f.id}>
                  {f.name}
                </option>
              ))}
            </select>
          </label>
          <Field
            label="X (m)"
            value={element.pose.x}
            onChange={(x) => updateElement({ pose: { ...element.pose, x } })}
          />
          <Field
            label="Y (m)"
            value={element.pose.y}
            onChange={(y) => updateElement({ pose: { ...element.pose, y } })}
          />
          <Field
            label="Z (m)"
            value={element.pose.z}
            onChange={(z) => updateElement({ pose: { ...element.pose, z } })}
          />
          <Field
            label="방향 (rad)"
            value={element.pose.yaw}
            onChange={(yaw) =>
              updateElement({ pose: { ...element.pose, yaw } })
            }
          />
          {(["x", "y", "z"] as const).map((axis) => (
            <Field
              key={axis}
              label={`크기 ${axis.toUpperCase()} (m)`}
              value={element.size[axis]}
              min={0.01}
              onChange={(v) =>
                updateElement({ size: { ...element.size, [axis]: v } })
              }
            />
          ))}
          <Field
            label="마찰 계수"
            value={element.friction}
            min={0}
            max={5}
            onChange={(friction) => updateElement({ friction })}
          />
          <label>
            재질
            <select
              value={element.material}
              onChange={(e) => updateElement({ material: e.target.value })}
            >
              <option value="concrete">콘크리트</option>
              <option value="steel">강철</option>
              <option value="rubber">고무</option>
              <option value="wood">목재</option>
              <option value="tile">타일</option>
            </select>
          </label>
          <Field
            label="경사 (rad)"
            value={element.slope}
            onChange={(slope) => updateElement({ slope })}
          />
          <Field
            label="속도 제한 (m/s)"
            value={element.speed_limit}
            min={0.01}
            onChange={(speed_limit) => updateElement({ speed_limit })}
          />
          <Field
            label="질량 (kg)"
            value={element.mass}
            min={0.01}
            onChange={(mass) => updateElement({ mass })}
          />
          {element.kind === "door" && <label>문이 열리는 방향
            <select value={element.facility.door_motion ?? ''} onChange={e=>updateElement({facility:{...element.facility,door_motion:(e.target.value || null) as 'lateral'|'normal'|'vertical'|null}})}>
              <option value="">기존 환경 기본값</option>
              <option value="lateral">문 폭 방향으로 옆으로 열기</option>
              <option value="normal">문 앞뒤 방향으로 이동</option>
              <option value="vertical">위로 올리기</option>
            </select><small>문 전체가 움직일 공간이 필요합니다. 벽·층 바닥·로봇과 겹치지 않게 배치하세요.</small>
          </label>}
          {element.kind === "charger" && (
            <>
              <Field
                label="충전 입력 전력 (W)"
                value={element.facility.charge_power_w ?? 400}
                min={0.01}
                onChange={(charge_power_w) =>
                  updateElement({
                    facility: { ...element.facility, charge_power_w },
                  })
                }
              />
              <Field
                label="충전 효율 (0–1)"
                value={element.facility.charge_efficiency ?? 0.9}
                min={0.01}
                max={1}
                onChange={(charge_efficiency) =>
                  updateElement({
                    facility: { ...element.facility, charge_efficiency },
                  })
                }
              />
              <p className="muted span-2">
                호환 바퀴형 연구 모델의 양쪽 접점이 연결되면 충전합니다.
                전력·용량은 실험 설정값입니다.
              </p>
            </>
          )}
          <label className="span-2">
            로봇 출입 허용 그룹 (쉼표로 구분)
            <input
              value={element.allowed_groups.join(", ")}
              onChange={(e) =>
                updateElement({
                  allowed_groups: e.target.value
                    .split(",")
                    .map((s) => s.trim())
                    .filter(Boolean),
                })
              }
            />
          </label>
          {element.kind === "restricted" && <label className="span-2">
            <input type="checkbox" checked={element.pedestrian_access ?? false}
              onChange={(e) => updateElement({ pedestrian_access: e.target.checked })} />
            보행자 통행 허용 · 로봇 그룹 제한은 유지
          </label>}
          <label>
            <input
              type="checkbox"
              checked={element.dynamic}
              onChange={(e) => updateElement({ dynamic: e.target.checked })}
            />
            이동 가능한 물체
          </label>
        </div>
        <JsonEditor
          label="시설·계단 세부 설정"
          value={element}
          onApply={(data) => updateElement(data as Element)}
        />
      </>
    ) : selectedRobot ? (
      <RobotEditor
        robot={selectedRobot}
        model={selectedModel}
        project={project!}
        update={updateRobot}
        remove={deleteSelection}
      />
    ) : selectedOther ? (
      <>
        <div className="section-head">
          <h2>{"size" in selectedOther ? "물품" : "사람"} 속성</h2>
          <button
            className="ghost danger"
            aria-label="선택 객체 삭제"
            onClick={deleteSelection}
          >
            <Trash2 size={14} />
          </button>
        </div>
        <label>
          이름
          <input
            value={selectedOther.name}
            onChange={(e) => updateOther({ name: e.target.value })}
          />
        </label>
        <div className="form-grid">
          <label className="span-2">
            층
            <select
              value={selectedOther.floor_id}
              onChange={(e) => {
                updateOther({ floor_id: e.target.value });
                setFloorId(e.target.value);
              }}
            >
              {project?.environment.floors.map((f) => (
                <option key={f.id} value={f.id}>
                  {f.name}
                </option>
              ))}
            </select>
          </label>
          {(["x", "y", "z", "yaw"] as const).map((axis) => (
            <Field
              key={axis}
              label={
                axis === "yaw" ? "방향 (rad)" : `${axis.toUpperCase()} (m)`
              }
              value={selectedOther.pose[axis]}
              onChange={(value) =>
                updateOther({ pose: { ...selectedOther.pose, [axis]: value } })
              }
            />
          ))}
          <Field
            label="질량 (kg)"
            value={selectedOther.mass}
            min={0.01}
            onChange={(mass) => updateOther({ mass })}
          />
          {"size" in selectedOther &&
            (["x", "y", "z"] as const).map((axis) => (
              <Field
                key={axis}
                label={`크기 ${axis.toUpperCase()} (m)`}
                value={(selectedOther as Item).size[axis]}
                min={0.01}
                onChange={(value) =>
                  updateOther({
                    size: { ...(selectedOther as Item).size, [axis]: value },
                  })
                }
              />
            ))}
        </div>
        <JsonEditor
          label="세부 물리·행동 설정"
          value={selectedOther}
          onApply={(data) => updateOther(data as Partial<Person & Item>)}
        />
      </>
    ) : (
      <>
        <h2>{floor?.name ?? "층 구성"}</h2>
        {floor && (
          <div className="form-grid">
            <label className="span-2">
              층 이름
              <input
                value={floor.name}
                onChange={(e) =>
                  edit((p) => {
                    p.environment.floors.find((f) => f.id === floorId)!.name =
                      e.target.value;
                  })
                }
              />
            </label>
            <Field
              label="기준 높이 (m)"
              value={floor.elevation}
              onChange={(v) =>
                edit((p) => {
                  p.environment.floors.find(
                    (f) => f.id === floorId,
                  )!.elevation = v;
                })
              }
            />
            <Field
              label="폭 (m)"
              value={floor.width}
              min={1}
              onChange={(v) =>
                edit((p) => {
                  p.environment.floors.find((f) => f.id === floorId)!.width = v;
                })
              }
            />
            <Field
              label="깊이 (m)"
              value={floor.depth}
              min={1}
              onChange={(v) =>
                edit((p) => {
                  p.environment.floors.find((f) => f.id === floorId)!.depth = v;
                })
              }
            />
          </div>
        )}
        <Empty title="도면에서 요소를 선택하세요">
          팔레트에서 요소를 선택한 뒤 도면을 누르면 배치됩니다. 드래그 또는 속성
          입력으로 위치와 크기를 조정하세요.
        </Empty>
      </>
    );
  const executionEnded = !!state && ["failed", "completed", "timed_out"].includes(state.status);
  const executionLabel = !live
    ? "연결 대기"
    : executionEnded
      ? state?.status === "completed" ? "실행 완료" : "실행 종료"
      : state?.status === "running" ? "실행 중" : state?.sim_time ? "재개" : "시작";
  const executeReason = !live
    ? "실행부에 연결된 뒤 사용할 수 있습니다."
    : executionEnded
      ? "종료된 실행입니다. 같은 구성으로 다시 실행하려면 초기화 후 시작하세요. 구성 변경은 다시 승인해야 합니다."
    : dirty && !(runApproval?.status==='accepted' && runApproval.run_id===state?.run_id)
      ? "초안 변경을 실행부에 먼저 적용하세요."
      : state?.status === "running"
        ? "시뮬레이션이 실행 중입니다."
        : busy
            ? `${busy} 작업이 끝나면 사용할 수 있습니다.`
            : "";
  const executionControls = () => (
    <div className="execution-strip">
      <div className="toolbar">
        <button
          className="primary"
          disabled={!!executeReason}
          title={
            executeReason || "구성된 작업을 물리 시뮬레이션으로 실행합니다."
          }
          onClick={() => control(state?.sim_time ? "resume" : "start")}
        >
          <Play size={14} />
          {executionLabel}
        </button>
        <button
          disabled={!live || state?.status !== "running"}
          title={
            !live
              ? "실행부 연결이 필요합니다."
              : state?.status !== "running"
                ? "현재 실행 중이 아닙니다."
                : "시뮬레이션 시간 진행을 일시 정지합니다."
          }
          onClick={() => control("pause")}
        >
          <Pause size={14} />
          일시 정지
        </button>
        <button
          disabled={!!executeReason}
          title={executeReason || "물리 한 단계 실행"}
          onClick={() => control("step")}
        >
          <SkipForward size={14} />한 단계
        </button>
        <button
          disabled={!live || !!busy}
          title={
            !live
              ? "실행부 연결이 필요합니다."
              : "이전 기록을 보존하고 현재 실행 구성의 0초·초기 배치로 돌아갑니다. 승인 구성과 편집 초안은 변경하지 않습니다."
          }
          onClick={() => control("reset")}
        >
          <RotateCcw size={14} />
          초기화
        </button>
        <select
          aria-label="시뮬레이션 배속"
          value={speed}
          disabled={!live || !!busy}
          title={
            !live
              ? "실행부 연결이 복구되면 배속을 변경할 수 있습니다."
              : "실행부가 보고한 배속입니다."
          }
          onChange={(e) => {
            const value = Number(e.target.value);
            void run("배속 변경", async () => {
              await api.control(
                currentState.current?.status === "running" ? "resume" : "pause",
                undefined,
                value,
              );
              await refresh();
            });
          }}
        >
          {[0.25, 0.5, 1, 2, 4].map((v) => (
            <option key={v} value={v}>
              {v}× 배속
            </option>
          ))}
        </select>
      </div>
      <div className="simclock">
        <Badge value={!live ? "상태 수신 대기" : (state?.status ?? "미연결")} />
        <strong>
          {fmt(state?.sim_time, 3)} <small>s</small>
        </strong>
        <small>
          {!live && state
            ? "마지막 수신값"
            : state?.run_id
              ? `실행 ${state.run_id.slice(0, 8)}`
              : "시뮬레이션"}
        </small>
      </div>
      {(!live || executionEnded) && (
        <div className="execution-help" role="status">
          <span>{!live
            ? "실행부 연결을 기다리고 있습니다. 연결을 다시 확인하세요. 체험 시간이 끝났다면 시작 화면에서 새 체험을 열어 주세요. 표시된 시간과 결과는 마지막 수신 기록입니다."
            : "이 실행은 종료되었습니다. 같은 구성은 초기화 → 시작으로 다시 실행하고, 구성 변경은 계획에서 다시 승인하세요."}</span>
          {!live
            ? <button disabled={!!busy} onClick={() => void run("연결 확인", refresh)}>연결 다시 확인</button>
            : <button onClick={() => navigate("planner")}>계획 다시 검토</button>}
        </div>
      )}
      {project?.id === "example-elevator-pedestrian-60s" &&
        (() => {
          const robot = state?.robots.find((item) => item.id === "sample-amr");
          const lift = state?.facilities.find((item) => item.id === "lift");
          const phase = String(lift?.phase ?? lift?.status ?? "대기");
          const floor =
            robot &&
            project.environment.floors.reduce((nearest, candidate) =>
              Math.abs(candidate.elevation + 0.3 - robot.pose.z) <
              Math.abs(nearest.elevation + 0.3 - robot.pose.z)
                ? candidate
                : nearest,
            ).name;
          const stop = state?.events
            .slice()
            .reverse()
            .find((event) => event.kind === "sample_stopped");
          return (
            <div className="sample-runtime-status" role="status">
              <strong>
                {state?.status === "completed"
                  ? "완료"
                  : state?.status === "timed_out"
                    ? "60초 도달"
                    : state?.status === "failed"
                      ? "실패"
                      : `${fmt(state?.sim_time, 1)} / 60초`}
              </strong>
              <span>
                현재 층{" "}
                {phase === "moving" ? "1→2층 상승 중" : (floor ?? "1층")} ·
                승강기 {phase}
              </span>
              <span>
                {stop?.message ??
                  robot?.reason ??
                  "시작을 누르면 승강기를 호출합니다."}
              </span>
              <span>
                보행자 거리{" "}
                {fmt(
                  (
                    state?.metrics.pedestrian_min_clearance_m as
                      Record<string, number> | undefined
                  )?.["sample-amr"],
                  2,
                )}
                m · 목표 0.50m
              </span>
            </div>
          );
        })()}
    </div>
  );
  const world = (editing = false) => (
    <div
      className={`workspace ${view === "3d" ? "is-3d" : ""} ${browserOpen ? "has-browser" : ""} ${inspectorOpen ? "has-inspector" : ""}`}
    >
      {browserOpen && (
        <aside
          className="workspace-browser"
          aria-label={editing ? "편집 도구와 객체" : "현재 층 객체"}
        >
          <div className="browser-heading">
            <strong>{editing ? "환경 구성" : "로봇과 객체"}</strong>
            <button
              className="ghost"
              onClick={() => setBrowserOpen(false)}
              aria-label="객체·도구 패널 접기"
            >
              <PanelLeftClose size={15} />
            </button>
          </div>
          {editing && (
            <div className="segmented browser-tabs">
              <button
                aria-pressed={browserTab === "objects"}
                onClick={() => setBrowserTab("objects")}
              >
                객체
              </button>
              <button
                aria-pressed={browserTab === "tools"}
                onClick={() => setBrowserTab("tools")}
              >
                배치 도구
              </button>
            </div>
          )}
          {editing && browserTab === "tools" ? (
            <>
              <label className="search-field">
                <Search size={14} />
                <input
                  aria-label="편집 도구 검색"
                  placeholder="도구 검색"
                  value={toolSearch}
                  onChange={(e) => setToolSearch(e.target.value)}
                />
              </label>
              <button
                className={`tool-select ${!tool ? "active" : ""}`}
                onClick={() => {
                  setTool(null);
                  setView("2d");
                }}
              >
                <MousePointer2 size={14} />
                선택·이동
              </button>
              {visiblePaletteGroups.map((group) => (
                <details className="tool-group" key={group.name} open>
                  <summary>{group.name}</summary>
                  <div>
                    {group.items.map((id) => (
                      <button
                        key={id}
                        aria-pressed={tool === id}
                        onClick={() => {
                          setTool(id);
                          setView("2d");
                        }}
                      >
                        {elementNames[id]}
                      </button>
                    ))}
                  </div>
                </details>
              ))}
              {!visiblePaletteGroups.length && (
                <div className="panel-hint" role="status">
                  <p>
                    일치하는 도구가 없습니다. 검색어를 지우고 다시 선택하세요.
                  </p>
                  <button className="ghost" onClick={() => setToolSearch("")}>
                    검색어 지우기
                  </button>
                </div>
              )}
              <p className="panel-hint">
                도구를 고른 뒤 도면을 눌러 배치합니다. Esc로 배치를 취소합니다.
              </p>
            </>
          ) : (
            <>
              <label className="search-field">
                <Search size={14} />
                <input
                  aria-label="객체 검색"
                  placeholder="이름·모델 검색"
                  value={objectSearch}
                  onChange={(e) => setObjectSearch(e.target.value)}
                />
              </label>
              <select
                aria-label="객체 유형 필터"
                value={objectFilter}
                onChange={(e) => setObjectFilter(e.target.value)}
              >
                <option value="all">전체 객체</option>
                <option value="robots">로봇</option>
                <option value="elements">공간·시설</option>
                <option value="people">사람</option>
                <option value="items">물품</option>
                {catalog.models.map((m) => (
                  <option key={m.id} value={`model:${m.id}`}>
                    {m.name}
                  </option>
                ))}
              </select>
              <div
                className="object-list"
                role="list"
                aria-label={
                  page === "monitor"
                    ? "객체 목록 · 로봇은 모든 층"
                    : "현재 층 객체 목록"
                }
              >
                {objectRows.map((e) => (
                  <button
                    key={e.id}
                    title={`${e.name} · ${e.kindLabel}`}
                    className={selectedIds.includes(e.id) ? "selected" : ""}
                    aria-pressed={selectedIds.includes(e.id)}
                    onClick={(event) => {
                      if (editing && event.shiftKey) {
                        const next = selectedIds.includes(e.id)
                          ? selectedIds.filter((id) => id !== e.id)
                          : [...selectedIds, e.id];
                        setSelectedIds(next);
                        setSelectedValue(next.at(-1) ?? "");
                      } else if (
                        page === "monitor" &&
                        view === "3d" &&
                        e.category === "robots"
                      ) {
                        showRobotIn3D(e.id);
                      } else chooseEntity(e.id);
                    }}
                  >
                    <span className="object-kind">
                      {e.category === "robots" && "model_id" in e ? (
                        <RobotIcon model={e.model_id} size={15} />
                      ) : e.category === "people" ? (
                        <Users size={15} />
                      ) : e.category === "items" ? (
                        <Package size={15} />
                      ) : (
                        <Box size={15} />
                      )}
                    </span>
                    <span>
                      <strong>{e.name}</strong>
                      <small>
                        {e.kindLabel}
                        {page === "monitor" &&
                        e.category === "robots" &&
                        displayProject
                          ? ` · ${displayProject.environment.floors.find((f) => f.id === entityFloor(displayProject, e.id, false))?.name ?? "층 확인 중"}`
                          : ""}
                      </small>
                    </span>
                    {selectedIds.includes(e.id) && <Check size={12} />}
                  </button>
                ))}
              </div>
              {page === "monitor" && selectedRobot && (
                <button
                  className="ghost"
                  disabled={!!cameraFocusReason(selectedRobot.id)}
                  title={
                    cameraFocusReason(selectedRobot.id) ||
                    "카메라를 로봇 전방 사선으로 이동합니다"
                  }
                  onClick={() => showRobotIn3D(selectedRobot.id)}
                >
                  3D에서 보기
                </button>
              )}
              {!objectRows.length && (
                <p className="panel-hint">
                  해당 층에 일치하는 객체가 없습니다. 검색어나 유형을
                  변경하세요.
                </p>
              )}
              {editing && (
                <button
                  className="add-object"
                  onClick={() => setBrowserTab("tools")}
                >
                  <Plus size={14} />
                  객체 배치
                </button>
              )}
            </>
          )}
        </aside>
      )}
      <div className="viewport-panel">
        <div className="viewport-tools">
          <div className="toolbar">
            {!browserOpen && (
              <button
                className="ghost"
                onClick={() => setBrowserOpen(true)}
                title="객체·도구 패널 펼치기"
              >
                <List size={15} />
                객체
              </button>
            )}
            {view !== "3d" && (
              <select
                aria-label="관찰 층"
                value={floorId}
                onChange={(e) => {
                  setFloorId(e.target.value);
                  setSelected("");
                  setTool(null);
                }}
              >
                {(editing ? project : displayProject)?.environment.floors.map(
                  (f) => (
                    <option key={f.id} value={f.id}>
                      {f.name}
                    </option>
                  ),
                )}
              </select>
            )}
            {editing && (
              <button
                className="ghost"
                title="층 추가"
                onClick={() => {
                  const id = uid("floor");
                  edit((p) =>
                    p.environment.floors.push({
                      id,
                      name: `${p.environment.floors.length + 1}층`,
                      elevation: p.environment.floors.length * 3.2,
                      width: 20,
                      depth: 14,
                    }),
                  );
                  setFloorId(id);
                  setSelected("");
                }}
              >
                <Plus size={13} />층
              </button>
            )}
          </div>
          <div className="toolbar">
            <WorkspaceFullscreen />
            <button
              className="ghost workspace-focus"
              aria-pressed={!browserOpen && !inspectorOpen}
              title="객체 목록과 속성 패널을 함께 접거나 펼칩니다."
              onClick={() => {
                const open = !browserOpen && !inspectorOpen;
                setBrowserOpen(open);
                setInspectorOpen(open);
              }}
            >
              <PanelLeftClose size={15} />
              {browserOpen || inspectorOpen
                ? "작업 공간 넓히기"
                : "패널 펼치기"}
            </button>
            <div className="segmented">
              <button
                aria-pressed={view === "2d"}
                onClick={() => {
                  setCameraFocusRequest(null);
                  setView("2d");
                }}
              >
                2D {editing ? "편집" : "도면"}
              </button>
              <button
                aria-pressed={view === "3d"}
                onClick={() => setView("3d")}
              >
                3D 물리
              </button>
            </div>
            {!inspectorOpen && (
              <button className="ghost workspace-properties-toggle" onClick={() => setInspectorOpen(true)}>
                속성
              </button>
            )}
          </div>
        </div>
        {editing && (
          <div className="edit-actions">
            <button
              disabled={!undoCount}
              title="실행 취소 (Ctrl/⌘ Z)"
              onClick={() => travelHistory()}
            >
              <Undo2 size={14} />
              실행 취소
            </button>
            <button
              disabled={!redoCount}
              title="다시 실행 (Ctrl/⌘ Shift Z)"
              onClick={() => travelHistory(true)}
            >
              <Redo2 size={14} />
              다시 실행
            </button>
            <span className="action-divider" />
            <button
              disabled={!selectedIds.length}
              onClick={copySelection}
              title="선택 객체 복제 (Ctrl/⌘ D)"
            >
              <Copy size={14} />
              복제
            </button>
            <button
              disabled={!selectedIds.length}
              onClick={deleteSelection}
              title="선택 객체 삭제 (Delete)"
            >
              <Trash2 size={14} />
              삭제
            </button>
            <label>
              <input
                type="checkbox"
                checked={snap}
                onChange={(e) => setSnap(e.target.checked)}
              />
              0.25 m 맞춤
            </label>
            {selectedIds.length > 1 && <span>{selectedIds.length}개 선택</span>}
          </div>
        )}
        {editing && view === "3d" && dirty && (
          <p className="view-notice">
            3D는 적용된 물리 실행입니다. 새 초안은 실행부 적용 후 확인할 수
            있습니다.
          </p>
        )}
        {!editing && matchedRuntimeProject && state && <CargoProgress project={matchedRuntimeProject} state={state} onFocus={showRobotIn3D}/>}
        {view === "3d" ? (
          <PhysicsView
            state={sceneRunId === state?.run_id ? state : null}
            meshes={meshes}
            selected={selected}
            onSelect={chooseEntity}
            project={
              runtimeProject && runtimeProject.runId === state?.run_id
                ? runtimeProject.project
                : null
            }
            floorId={floorId}
            focusRequest={cameraFocusRequest}
            onFloorChange={setFloorId}
            connectionState={connectionState}
          />
        ) : (
          <PlanView
            project={editing ? project : displayProject}
            state={state}
            floorId={floorId}
            selected={selected}
            selectedIds={selectedIds}
            onSelect={chooseEntity}
            onSelectionChange={(ids: string[]) => {
              setSelectedIds(ids);
              setSelectedValue(ids.at(-1) ?? "");
              if (ids.length) setInspectorOpen(true);
            }}
            tool={tool}
            onCancelTool={() => setTool(null)}
            onPlace={addElement}
            onMove={moveEntity}
            onTransform={transformEntities}
            editing={editing}
            snap={snap}
            models={catalog.models}
          />
        )}
      </div>
      {inspectorOpen && (
        <aside
          className="inspector"
          aria-label={editing ? "선택 객체 속성" : "선택 객체 상태"}
        >
          <div className="inspector-heading">
            <strong>{editing ? "속성" : "실행 상태"}</strong>
            <button
              className="ghost"
              aria-label="속성 패널 접기"
              onClick={() => setInspectorOpen(false)}
            >
              <PanelRightClose size={15} />
            </button>
          </div>
          {editing ? elementInspector() : runtimeInspector()}
        </aside>
      )}
    </div>
  );
  return (
    <div className={`app ${mapPage ? "map-app" : ""}`}>
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-mark">
            <Layers3 size={20} />
          </div>
          <div>
            <strong>ROBOT LAB</strong>
            <small>로봇 운영 실험실</small>
          </div>
        </div>
        <p className="nav-group">작업 공간</p>
        <nav className="nav-list" aria-label="주 메뉴">
          {pages.map((p) => (
            <button
              key={p.id}
              aria-current={page === p.id ? "page" : undefined}
              title={`${p.name} · ${p.description}`}
              onClick={() => {
                if (p.id === "environment") setFocusedDrawing(null);
                if (p.id === "planner") setFocusedPlan(null);
                navigate(p.id);
                if (p.id === "environment") {
                  setView("2d");
                  setBrowserTab("tools");
                  setObjectFilter("all");
                }
                if (p.id === "monitor") {
                  setBrowserTab("objects");
                  setObjectFilter("robots");
                }
              }}
            >
              <p.icon size={18} />
              <span className="nav-long">{p.name}</span>
              <span className="nav-short">
                {
                  {
                    history: "작업 기록",
                    planner: "계획 도우미",
                    monitor: "관제",
                    environment: "환경 편집",
                    robots: "로봇 모델",
                    scenario: "시나리오",
                    policy: "정책 설정",
                    facilities: "시설 예약",
                    events: "사건 기록",
                    experiments: "실험 비교",
                  }[p.id]
                }
              </span>
            </button>
          ))}
        </nav>
        <div className="side-foot">
          <span>실험 구성</span>
          <strong>{project?.name ?? "실행부 연결 대기"}</strong>
          <span>구성 버전 {project?.revision ?? "—"}</span>
          <span>실장비 검증: 미검증</span>
        </div>
      </aside>
      <main className="main">
        <header className="app-header">
          <div className="topbar">
            <div className="project-identity">
              <label className="sr-only" htmlFor="project-title">
                프로젝트 이름
              </label>
              <input
                id="project-title"
                value={project?.name ?? "연결 중"}
                disabled={!project}
                onChange={(e) =>
                  edit((p) => {
                    p.name = e.target.value;
                  })
                }
              />
              <span className={`save-state ${unsaved ? "changed" : ""}`}>
                {unsaved
                  ? "미저장 변경"
                  : savedRevision
                    ? `저장됨 · v${savedRevision}`
                    : "변경 없음"}
              </span>
              <span
                title={configurationDisplay.description}
                aria-label={configurationDisplay.description}
              >
                <Badge
                  value={configurationDisplay.value}
                  tone={configurationDisplay.tone}
                />
              </span>
            </div>
            <div className="project-actions">
              <div className={`connection ${connectionState}`} role="status">
                <span className={`dot ${live ? "connected" : ""}`} />
                {connectionState === "connected"
                  ? "연결됨"
                  : connectionState === "stale"
                    ? "수신 지연"
                    : connectionState === "connecting"
                      ? "연결 중"
                      : "연결 끊김"}
              </div>
              <details className="project-files">
                <summary>
                  <Menu size={14} />
                  프로젝트
                </summary>
                <div className="file-menu">
                  <div className="section-head">
                    <div className="toolbar">
                      <label>
                        <select
                          aria-label="예제 환경 불러오기"
                          value=""
                          onChange={(e) => {
                            const templateId = e.target.value;
                            if (templateId)
                              void run("예제 불러오기", () =>
                                loadExample(templateId, templateId === "elevator-pedestrian-60s"));
                          }}
                        >
                          <option value="">예제 환경 불러오기</option>
                          {catalog.templates.map((t) => (
                            <option key={t.id} value={t.id}>
                              {t.name}
                            </option>
                          ))}
                        </select>
                      </label>
                      <button onClick={() => upload.current?.click()}>
                        <FileUp size={14} />
                        가져오기
                      </button>
                      <button
                        disabled={!project}
                        onClick={() => {
                          if (!project) return;
                          downloadJSON(`${project.name}.json`, project);
                          setNotice(
                            "현재 초안의 JSON 다운로드를 요청했습니다. 브라우저 다운로드 목록을 확인하세요.",
                          );
                        }}
                      >
                        <ArrowDownToLine size={14} />
                        JSON 내보내기
                      </button>
                      <input
                        ref={upload}
                        className="file-input"
                        type="file"
                        accept=".json,application/json"
                        onChange={(e) => {
                          const f = e.target.files?.[0];
                          if (f)
                            void run("설정 가져오기", async () => {
                              const data = JSON.parse(await f.text());
                              const issues = validateProject(data);
                              if (issues.length)
                                throw new Error(
                                  `가져오지 못했습니다. 현재 초안을 보존했습니다. ${issues.join(" ")}`,
                                );
                              await preserveCurrentDraft();
                              adopt(data);
                            });
                          e.target.value = "";
                        }}
                      />
                    </div>
                    <div className="toolbar">
                      <select
                        aria-label="저장된 구성"
                        value={savedChoice}
                        onChange={(e) => setSavedChoice(e.target.value)}
                      >
                        <option value="">저장된 구성</option>
                        {saved.map((s, i) => (
                          <option
                            key={`${s.id}-${s.revision}`}
                            value={String(i)}
                          >
                            {s.name} · v{s.revision}
                          </option>
                        ))}
                      </select>
                      <button
                        disabled={savedChoice === "" || !!busy}
                        onClick={() =>
                          run("구성 불러오기", async () => {
                            const s = saved[Number(savedChoice)];
                            await openSavedVersion(s.id, s.revision);
                          })
                        }
                      >
                        불러오기
                      </button>
                      <button
                        disabled={savedChoice === "" || !!busy}
                        onClick={() =>
                          run("구성 복제", async () => {
                            await preserveCurrentDraft();
                            adopt(
                              await api.clone(saved[Number(savedChoice)].id),
                            );
                            setSaved(await api.saved());
                          })
                        }
                      >
                        <Copy size={13} />
                        복제
                      </button>
                    </div>
                    <div className="project-history" aria-label="저장된 지도와 구성 기록">
                      <div className="project-history-heading"><strong>저장된 지도·구성</strong>
                        <button type="button" onClick={() => void run("저장 기록 새로고침", async () => setSaved(await api.saved()))}>새로고침</button></div>
                      {saved.length === 0 ? <p>저장된 구성이 없습니다. 현재 구성을 저장하면 여기에 버전별로 쌓입니다.</p> :
                        saved.map((item) => <details key={item.id}>
                          <summary>{item.name} · {item.version_count ?? item.versions?.length ?? 1}개 버전</summary>
                          <div className="project-history-versions">{(item.versions ?? [{revision:item.revision,name:item.name,map_name:item.name,map_version:1,floor_count:0,robot_count:0}]).map((version) =>
                            <div key={version.revision}><span><strong>v{version.revision}</strong> · {version.name}<small>{version.map_name} · 지도 v{version.map_version} · {version.floor_count}층 · 로봇 {version.robot_count}대{version.source ? ` · ${version.source}` : ""}</small></span>
                              <button type="button" disabled={!!busy} onClick={() => void run("이전 지도 열기", () => openSavedVersion(item.id, version.revision))}>열기</button></div>)}</div>
                        </details>)}
                    </div>
                  </div>
                </div>
              </details>
              <button
                disabled={
                  !project || !live || !!busy || configurationErrors.length > 0
                }
                onClick={save}
                title={
                  !live
                    ? "연결이 복구되면 서버에 저장할 수 있습니다. 초안은 이 브라우저에 보관됩니다."
                    : "프로젝트 버전 저장 (Ctrl/⌘ S)"
                }
              >
                <Save size={14} />
                저장
              </button>
              <button
                disabled={
                  !project ||
                  !live ||
                  !!busy ||
                  state?.status === "running" ||
                  configurationErrors.length > 0
                }
                onClick={apply}
                title={
                  state?.status === "running"
                    ? "일시 정지한 뒤 초안을 적용하세요."
                    : "초안을 적용하고 초기 조건에서 새 실행을 만듭니다."
                }
              >
                <Check size={14} />
                적용
              </button>
            </div>
          </div>
          {executionControls()}
        </header>
        <div
          ref={contentRef}
          className={`content page-${page} ${mapPage ? "workspace-content" : ""}`}
        >
          <div className="page-heading">
            <div>
              <div className="breadcrumb">
                <span>
                  {page === "history" ? "보관함" :
                    ["environment", "robots", "scenario", "policy"].includes(page)
                      ? "구성 초안" : "현재 실행"}
                </span>
                <ChevronRight size={12} />
                <strong>{pageInfo.name}</strong>
              </div>
              <h1>{pageInfo.name}</h1>
            </div>
            <div className="page-context">
              <div className="context-next">
                {page === "environment" ? (
                  <>
                    <span>공간을 편집한 뒤 로봇과 작업을 구성하세요.</span>
                    <button
                      className="ghost"
                      onClick={() => navigate("robots")}
                    >
                      로봇 구성
                      <ChevronRight size={14} />
                    </button>
                  </>
                ) : page === "robots" ? (
                  <>
                    <span>개체별 설정을 확인한 뒤 작업을 정합니다.</span>
                    <button
                      className="ghost"
                      onClick={() => navigate("scenario")}
                    >
                      작업 설정
                      <ChevronRight size={14} />
                    </button>
                  </>
                ) : page === "scenario" ? (
                  <>
                    <span>초안을 적용하면 실행할 수 있습니다.</span>
                    <button
                      className="ghost"
                      onClick={() => navigate("monitor")}
                    >
                      관제로 이동
                      <ChevronRight size={14} />
                    </button>
                  </>
                ) : page === "history" ? (
                  <span>기록을 열어 구성을 확인하거나 실행부에 적용하세요.</span>
                ) : page === "monitor" ? (
                  <>
                    <span>
                      로봇을 선택해 상태를 확인하거나 사건을 조사하세요.
                    </span>
                    <button
                      className="ghost"
                      onClick={() => navigate("events")}
                    >
                      문제 확인
                      <ChevronRight size={14} />
                    </button>
                  </>
                ) : page === "events" || page === "facilities" ? (
                  <>
                    <span>사건의 원인을 확인한 뒤 정책을 조정하세요.</span>
                    <button
                      className="ghost"
                      onClick={() => navigate("policy")}
                    >
                      정책 변경
                      <ChevronRight size={14} />
                    </button>
                  </>
                ) : page === "policy" ? (
                  <>
                    <span>변경한 초안으로 같은 조건의 결과를 비교하세요.</span>
                    <button
                      className="ghost"
                      onClick={() => navigate("experiments")}
                    >
                      비교 재실험
                      <ChevronRight size={14} />
                    </button>
                  </>
                ) : (
                  <>
                    <span>
                      {page === "planner"
                        ? "계획을 검토하고 마지막 승인으로 실행하세요."
                        : "측정 결과를 확인하고 다음 구성을 준비하세요."}
                    </span>
                    <button
                      className="ghost"
                      onClick={() => navigate("environment")}
                    >
                      공간 다시 편집
                      <ChevronRight size={14} />
                    </button>
                  </>
                )}
              </div>
              {!!state?.warnings?.length && (
                <details className="notice validation-scope">
                  <summary>
                    <ShieldAlert size={16} />
                    <span>검증 범위 확인 · {state.warnings.length}개 안내</span>
                    <ChevronRight size={14} />
                  </summary>
                  <ul>
                    {state.warnings.map((w, i) => (
                      <li key={i}>{w}</li>
                    ))}
                  </ul>
                </details>
              )}
            </div>
          </div>
          {notice && (
            <div className="feedback-banner" role="status">
              <Check size={14} />
              <span>{notice}</span>
              <button
                className="ghost"
                aria-label="알림 닫기"
                onClick={() => setNotice("")}
              >
                <X size={14} />
              </button>
            </div>
          )}
          {!live && state && (
            <div className="notice error" role="alert">
              <CircleAlert size={15} />
              <span>
                {connectionState === "stale"
                  ? "실행부 응답이 늦어지고 있습니다."
                  : "실행부 연결이 끊겼습니다."}{" "}
                화면은 마지막 수신 상태입니다. 초안은 유지되며 자동
                재연결합니다.
              </span>
            </div>
          )}
          {busy && (
            <div className="request-status" role="status">
              {busy}…
            </div>
          )}
          {error && (
            <div className="notice error" role="alert">
              <CircleAlert size={16} />
              <span>{error}</span>
              <button aria-label="오류 닫기" onClick={() => setError("")}>
                <X size={15} />
              </button>
            </div>
          )}
          {configurationErrors.length > 0 && (
            <div className="notice" role="status">
              <CircleAlert size={16} />
              <span>
                구성 값을 확인하면 저장·적용할 수 있습니다.{" "}
                {configurationErrors.join(" ")}
              </span>
            </div>
          )}
          {project && (
            <div hidden={page !== "planner"}>
              <PlanningWorkbench
                focusPlan={focusedPlan}
                onUseScenarioProject={async next=>{
                  await preserveCurrentDraft();
                  adopt(next);
                  const savedSample=await api.save(next);
                  setSaved(await api.saved());
                  setNotice(`가상 샘플 v${savedSample.revision}을 저장했습니다. 실제 도면이 아닙니다. 참여 구성과 대화 초안을 다시 검토하세요.`);
                }}
                project={project}
                state={state}
                connected={live}
                onReviewMap={() => navigate("environment")}
                onObserve={(id) => {
                  if (
                    matchedRuntimeProject?.robots.some((r) => r.id === id) ||
                    matchedRuntimeProject?.people.some((p) => p.id === id)
                  )
                    showRobotIn3D(id);
                  else {
                    navigate("monitor");
                    setSelected(id);
                    setInspectorOpen(true);
                    const entity =
                      matchedRuntimeProject?.environment.elements.find(
                        (e) => e.id === id,
                      ) ??
                      matchedRuntimeProject?.items.find((e) => e.id === id);
                    if (entity) setFloorId(entity.floor_id);
                  }
                }}
              />
            </div>
          )}
          {page === "history" && <HistoryLibrary
            catalog={catalog} saved={saved} currentProjectId={project?.id}
            currentProjectRevision={project?.revision} currentProjectName={project?.name}
            running={state?.status === "running"} busy={!!busy}
            onRefreshProjects={refreshSaved}
            onOpenProject={(id, revision, prepare) => void run("저장 구성 열기", async () => {
              await openSavedVersion(id, revision, prepare);
              navigate(prepare ? "monitor" : "environment");
            })}
            onLoadExample={(id, prepare) => void run("예제 불러오기", async () => {
              await loadExample(id, prepare);
              navigate(prepare ? "monitor" : "environment");
            })}
            onReviewDrawing={(id) => {
              setFocusedDrawing({ id, sequence: Date.now() });
              navigate("environment");
            }}
            onOpenPlan={(id, version) => {
              setFocusedPlan({ id, version, sequence: Date.now() });
              navigate("planner");
            }}
            onViewExperiments={() => navigate("experiments")}
            onOpenExperimentRun={(experimentId, runId, prepare) => void run("실험 구성 열기", async () => {
              await openExperimentRun(experimentId, runId, prepare);
              navigate(prepare ? "monitor" : "environment");
            })}
          />}
          {page === "monitor" && (
            <>
              {world()}
              <details className="supporting-details">
                <summary>로봇 상태 목록</summary>
                <section className="section">
                  <div className="section-head">
                    <h2>로봇 상태</h2>
                    <p>
                      {matchedRuntimeProject
                        ? `${matchedRuntimeProject.robots.length}대`
                        : "구성 수신 중"}{" "}
                      · 실행 {state?.run_id?.slice(0, 12) ?? "—"}
                    </p>
                  </div>
                  {robotTable("runtime")}
                </section>
              </details>
              <details className="supporting-details">
                <summary>작업 진행과 물리 복구</summary>
                <section className="section">
                  <div className="section-head">
                    <h2>작업 진행</h2>
                    <p>현재 실행부가 보고한 작업과 협업 상태</p>
                  </div>
                  {state?.tasks.length ? (
                    <div className="table-wrap">
                      <table>
                        <thead>
                          <tr>
                            <th>작업</th>
                            <th>상태</th>
                            <th>참여 로봇</th>
                            <th>협업 진행</th>
                            <th>대기·실패 이유</th>
                          </tr>
                        </thead>
                        <tbody>
                          {state.tasks.map((entry) => (
                            <Fragment key={entry.id}>
                              <tr>
                                <td>{entry.name}</td>
                                <td>
                                  <Badge value={entry.status} />
                                </td>
                                <td>
                                  {(
                                    entry.participant_ids ??
                                    (entry.robot_id ? [entry.robot_id] : [])
                                  )
                                    .map((id) => {
                                      const role = Object.entries(
                                        state.cooperation?.executions[
                                          entry.execution_id ??
                                            entry.cooperation?.execution_id ??
                                            ""
                                        ]?.participants ?? {},
                                      ).find(
                                        ([, participant]) => participant === id,
                                      )?.[0];
                                      const roles: Record<string, string> = {
                                        donor: "상차",
                                        loader: "상차",
                                        carrier: "운반",
                                        receiver: "수신",
                                      };
                                      return `${state.robots.find((r) => r.id === id)?.name ?? "로봇"} · ${id}${role ? ` (${roles[role] ?? role})` : ""}`;
                                    })
                                    .join(" / ") || "배정 대기"}
                                </td>
                                <td>
                                  {entry.cooperation ||
                                  entry.participant_ids?.length ? (
                                    <CooperationProgress
                                      value={entry.cooperation}
                                    />
                                  ) : (
                                    "—"
                                  )}
                                </td>
                                <td>{entry.reason}</td>
                              </tr>
                              {(entry.recovery ||
                                (["failed", "cancelled"].includes(
                                  entry.status,
                                ) &&
                                  entry.cooperation?.resources_retained ===
                                    true)) && (
                                <tr className="recovery-row">
                                  <td colSpan={5}>
                                    {runtimeProject?.runId === state.run_id &&
                                    runtimeProject.project.tasks.find(
                                      (task) => task.id === entry.id,
                                    ) ? (
                                      <RecoveryPanel
                                        key={`${state.run_id}:${entry.id}:${entry.execution_id ?? entry.cooperation?.execution_id ?? ""}`}
                                        cacheKey={`${state.run_id}:${entry.id}:${entry.execution_id ?? entry.cooperation?.execution_id ?? ""}`}
                                        cache={recoveryDrafts.current}
                                        task={entry}
                                        spec={runtimeProject.project.tasks.find(
                                          (task) => task.id === entry.id,
                                        )!}
                                        project={runtimeProject.project}
                                        state={state}
                                        connected={connected}
                                        busy={!!busy}
                                        run={run}
                                        refresh={refresh}
                                        isCurrent={() => {
                                          const current = currentState.current;
                                          const latest = current?.tasks.find(
                                            (task) => task.id === entry.id,
                                          );
                                          return (
                                            current?.run_id === state.run_id &&
                                            latest !== undefined &&
                                            (latest.execution_id ??
                                              latest.cooperation
                                                ?.execution_id) ===
                                              (entry.execution_id ??
                                                entry.cooperation?.execution_id)
                                          );
                                        }}
                                      />
                                    ) : (
                                      <p className="muted">
                                        복구 입력을 위해 현재 실행의 작업 구성을
                                        확인하고 있습니다.
                                      </p>
                                    )}
                                  </td>
                                </tr>
                              )}
                            </Fragment>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  ) : (
                    <Empty title="실행 중인 작업 기록이 없습니다">
                      운영 시나리오에서 구성한 작업을 적용하면 진행 상태가
                      표시됩니다.
                    </Empty>
                  )}
                </section>
              </details>
            </>
          )}
          {page === "environment" && (
            <>
              {project && (
                <FloorplanPanel
                  focusDrawing={focusedDrawing}
                  project={project}
                  onApply={async (next) => {
                    await preserveCurrentDraft();
                    const stored = await api.save(next);
                    adopt(stored);
                    savedFingerprint.current = fingerprint(stored);
                    setUnsaved(false);
                    setSavedRevision(stored.revision);
                    setSaved(await api.saved());
                  }}
                />
              )}
              {world(true)}
              <JsonEditor
                label="전체 환경 데이터 편집"
                value={project?.environment}
                onApply={(data) =>
                  edit((p) => {
                    p.environment = data as Project["environment"];
                  })
                }
              />
            </>
          )}
          {page === "robots" && (
            <>
              <div className="split">
                <section>
                  <div className="section-head robot-manager-heading">
                    <h2>로봇 관리</h2>
                    <div className="segmented" aria-label="로봇 관리 보기">
                      <button
                        aria-pressed={robotLibraryMode === "instances"}
                        onClick={() => setRobotLibraryMode("instances")}
                      >
                        배치한 로봇 {project?.robots.length ?? 0}대
                      </button>
                      <button
                        aria-pressed={robotLibraryMode === "models"}
                        onClick={() => setRobotLibraryMode("models")}
                      >
                        모델 추가
                      </button>
                    </div>
                  </div>
                  {robotLibraryMode === "instances" ? (
                    <section className="robot-instances">
                      <div className="section-head">
                        <h2
                          id="placed-robots-heading"
                          tabIndex={-1}
                          style={{ scrollMarginTop: "1rem" }}
                        >
                          배치한 로봇
                        </h2>
                        <label className="search-field">
                          <Search size={14} />
                          <input
                            aria-label="배치한 로봇 검색"
                            placeholder="이름·모델·ID 검색"
                            value={robotSearch}
                            onChange={(e) => setRobotSearch(e.target.value)}
                          />
                        </label>
                        <p>
                          편집 초안 {project?.robots.length ?? 0}대 · 상태와
                          작업은 현재 실행 보고
                        </p>
                      </div>
                      {robotTable(
                        "draft",
                        project?.robots.filter((r) =>
                          `${r.name} ${r.model_id} ${r.id}`
                            .toLowerCase()
                            .includes(robotSearch.toLowerCase()),
                        ),
                      )}
                    </section>
                  ) : (
                    <>
                      <div className="catalogue">
                        {catalog.models.map((m) => (
                          <article className="model-item" key={m.id}>
                            <RobotIcon model={m.id} size={31} />
                            <div>
                              <h2>{m.name}</h2>
                              <p>
                                {modelKindNames[m.kind] ?? m.kind} ·{" "}
                                {locomotionNames[m.locomotion] ?? m.locomotion}
                                <br />
                                질량 {fmt(m.mass)} kg · 최대 적재{" "}
                                {fmt(m.max_payload)} kg
                              </p>
                              <div className="model-meta">
                                {m.capabilities.map((c) => (
                                  <Badge
                                    key={c}
                                    value={`${taskNames[c as TaskKind] ?? c} · ${m.capability_status?.[c] ?? "검증 범위 확인"}`}
                                  />
                                ))}
                              </div>
                              <p>
                                {m.limitations?.[0] ??
                                  "지원 범위는 모델 검증 문서를 확인하세요."}
                              </p>
                              <div className="toolbar">
                                <label style={{ width: 80 }}>
                                  배치 대수
                                  <input
                                    type="number"
                                    min={1}
                                    step={1}
                                    value={robotCounts[m.id] ?? 1}
                                    onChange={(e) =>
                                      setRobotCounts({
                                        ...robotCounts,
                                        [m.id]: Number(e.target.value),
                                      })
                                    }
                                  />
                                </label>
                                <button
                                  disabled={!project}
                                  onClick={() => addRobots(m)}
                                >
                                  <Plus size={14} />
                                  배치
                                </button>
                              </div>
                              <JsonDetails
                                title="출처와 검증 수준"
                                data={{
                                  source: m.source,
                                  support: m.support,
                                  limitations: m.limitations,
                                }}
                              />
                            </div>
                          </article>
                        ))}
                        {catalog.documentation_models?.map((m) => (
                          <article className="model-item" key={m.id}>
                            <RobotIcon model={m.id} size={31} />
                            <div>
                              <h2>{m.name}</h2>
                              <p>
                                {m.id} · {m.status}
                              </p>
                              <p>
                                로봇 문서와 기능 검토는 계획 도우미에서
                                진행하세요. 물리 모델과 실행 어댑터가 없으므로
                                배치할 수 없습니다.
                              </p>
                            </div>
                          </article>
                        ))}
                      </div>
                      {!catalog.models.length && (
                        <Empty title="모델 목록을 기다리고 있습니다">
                          실행부 연결 후 사용 가능한 검증 모델을 불러옵니다.
                        </Empty>
                      )}
                    </>
                  )}
                </section>
                <aside className="form-panel robot-editor-panel">
                  {selectedRobot ? (
                    <>
                      <div className="robot-location-actions">
                        <button
                          className="ghost"
                          onClick={() => {
                            navigate("environment");
                            setFloorId(selectedRobot.floor_id);
                            setBrowserTab("objects");
                            setInspectorOpen(true);
                          }}
                        >
                          도면에서 보기
                        </button>
                        <button
                          className="ghost"
                          disabled={!!cameraFocusReason(selectedRobot.id)}
                          title={
                            cameraFocusReason(selectedRobot.id) ||
                            "이 로봇의 현재 실행 위치를 3D에서 관찰합니다."
                          }
                          onClick={() => showRobotIn3D(selectedRobot.id)}
                        >
                          3D에서 보기
                        </button>
                      </div>
                      <RobotEditor
                        robot={selectedRobot}
                        model={selectedModel}
                        project={project!}
                        update={updateRobot}
                        remove={deleteSelection}
                      />
                    </>
                  ) : (
                    <Empty title="배치한 개체를 선택하세요">
                      목록에서 선택한 개체의 배터리, 장비, 센서와 초기 위치를
                      편집할 수 있습니다.
                    </Empty>
                  )}
                </aside>
              </div>
            </>
          )}
          {page === "scenario" && (
            <>
              <div className="section-head">
                <div className="segmented">
                  {[
                    ["tasks", "작업 흐름"],
                    ["people", "사람"],
                    ["items", "물품"],
                  ].map(([id, n]) => (
                    <button
                      key={id}
                      aria-pressed={scenarioTab === id}
                      onClick={() => setScenarioTab(id)}
                    >
                      {n}
                    </button>
                  ))}
                </div>
                {scenarioTab === "tasks" && (
                  <button disabled={!project} onClick={addTask}>
                    <Plus size={14} />
                    작업 추가
                  </button>
                )}
              </div>
              {scenarioTab === "tasks" ? (
                <div className="split">
                  <div className="table-wrap">
                    <p className="muted">
                      진행 상태는 현재 실행의 관측값입니다. 초안 변경은 실행부에
                      적용한 뒤 반영됩니다.
                    </p>
                    <table>
                      <thead>
                        <tr>
                          <th>작업</th>
                          <th>유형</th>
                          <th>발생 / 기한</th>
                          <th>상태</th>
                          <th>협업 진행</th>
                        </tr>
                      </thead>
                      <tbody>
                        {project?.tasks.map((t) => (
                          <tr
                            key={t.id}
                            className={`selectable ${selectedTask === t.id ? "selected" : ""}`}
                            onClick={() => setSelectedTask(t.id)}
                          >
                            <td>
                              <button
                                className="ghost"
                                onClick={() => setSelectedTask(t.id)}
                              >
                                {t.name}
                              </button>
                            </td>
                            <td>{taskNames[t.kind]}</td>
                            <td>
                              {t.release_time}s /{" "}
                              {t.deadline === null ? "없음" : `${t.deadline}s`}
                            </td>
                            <td>
                              <Badge
                                value={
                                  state?.tasks.find((s) => s.id === t.id)
                                    ?.status ?? "초안"
                                }
                              />
                            </td>
                            <td>
                              {t.cooperation ? (
                                <CooperationProgress
                                  value={
                                    state?.tasks.find((s) => s.id === t.id)
                                      ?.cooperation
                                  }
                                />
                              ) : (
                                "—"
                              )}
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                    {!project?.tasks.length && (
                      <Empty title="작업을 추가하세요">
                        배송·순찰·설비 점검·인계 등 운영 흐름을 구성합니다.
                      </Empty>
                    )}
                  </div>
                  <aside className="form-panel">
                    {task ? (
                      <>
                        <div className="section-head">
                          <h2>작업 설정</h2>
                          <button
                            aria-label="작업 삭제"
                            className="ghost danger"
                            onClick={() => {
                              const dependents =
                                project?.tasks.filter((t) =>
                                  t.predecessor_ids.includes(selectedTask),
                                ) ?? [];
                              if (dependents.length) {
                                setError(
                                  `이 작업을 선행 작업으로 사용하는 작업이 있습니다: ${dependents.map((t) => t.name).join(", ")}. 먼저 해당 작업의 선행 작업 설정을 변경하세요.`,
                                );
                                return;
                              }
                              edit((p) => {
                                p.tasks = p.tasks.filter(
                                  (t) => t.id !== selectedTask,
                                );
                              });
                              setSelectedTask("");
                            }}
                          >
                            <Trash2 size={15} />
                          </button>
                        </div>
                        <div className="form-grid">
                          <label className="span-2">
                            작업 이름
                            <input
                              value={task.name}
                              onChange={(e) =>
                                updateTask({ name: e.target.value })
                              }
                            />
                          </label>
                          <label>
                            유형
                            <select
                              value={task.kind}
                              onChange={(e) =>
                                updateTask({ kind: e.target.value as TaskKind })
                              }
                            >
                              {Object.entries(taskNames).map(([id, n]) => (
                                <option
                                  value={id}
                                  key={id}
                                  disabled={
                                    !!task.cooperation &&
                                    !cooperativeSchemaKinds.includes(
                                      id as TaskKind,
                                    )
                                  }
                                >
                                  {n}
                                </option>
                              ))}
                            </select>
                          </label>
                          <label>
                            목표 층
                            <select
                              value={task.floor_id}
                              onChange={(e) =>
                                updateTask({ floor_id: e.target.value })
                              }
                            >
                              {project?.environment.floors.map((f) => (
                                <option key={f.id} value={f.id}>
                                  {f.name}
                                </option>
                              ))}
                            </select>
                          </label>
                          {(cooperativeFormKinds.includes(task.kind) ||
                            task.cooperation) && (
                            <label className="span-2">
                              <input
                                type="checkbox"
                                checked={!!task.cooperation}
                                onChange={(e) =>
                                  toggleCooperation(e.target.checked)
                                }
                              />
                              상차·운반·인계·배치 협업 사용
                            </label>
                          )}
                          {task.cooperation && (
                            <>
                              <p className="muted span-2">
                                상차 로봇을 선택하면 물품을 싣는 단계부터
                                시작합니다. 선택하지 않으면 이미 실린 물품을
                                운반·인계합니다. 상차 층과 목표 층이 다르면
                                물품을 실을 수 있는 승강기 경로가 필요합니다.
                              </p>
                              <label className="span-2">상차·재인수 층<select
                                value={task.cooperation.source_floor_id ?? task.floor_id}
                                onChange={e=>updateCooperation({source_floor_id:e.target.value})}>
                                {project?.environment.floors.map(f=><option key={f.id} value={f.id}>{f.name}</option>)}
                              </select></label>
                              {(
                                [
                                  "carrier_id",
                                  "receiver_id",
                                  "donor_id",
                                ] as const
                              ).map((role) => (
                                <label
                                  key={role}
                                  className={
                                    role === "donor_id" ? "span-2" : undefined
                                  }
                                >
                                  {role === "carrier_id"
                                    ? "운반 로봇"
                                    : role === "receiver_id"
                                      ? "수신 로봇"
                                      : "상차 로봇 (선택)"}
                                  <select
                                    value={task.cooperation![role] ?? ""}
                                    onChange={(e) =>
                                      updateCooperation({
                                        [role]:
                                          role === "donor_id"
                                            ? e.target.value || null
                                            : e.target.value,
                                      })
                                    }
                                  >
                                    <option value="">
                                      {role === "donor_id"
                                        ? "없음 · 이미 적재된 물품"
                                        : "로봇 선택 (필수)"}
                                    </option>
                                    {task.cooperation![role] &&
                                      !project?.robots.some(
                                        (r) => r.id === task.cooperation![role],
                                      ) && (
                                        <option value={task.cooperation![role]}>
                                          없는 로봇 · {task.cooperation![role]}
                                        </option>
                                      )}
                                    {project?.robots.map((r) => (
                                      <option
                                        key={r.id}
                                        value={r.id}
                                        disabled={
                                          (
                                            [
                                              "carrier_id",
                                              "receiver_id",
                                              "donor_id",
                                            ] as const
                                          ).some(
                                            (other) =>
                                              other !== role &&
                                              r.id === task.cooperation![other],
                                          )
                                        }
                                      >
                                        {r.name} · {project?.environment.floors.find(f=>f.id===r.floor_id)?.name}
                                      </option>
                                    ))}
                                  </select>
                                </label>
                              ))}
                              <p className="muted span-2">
                                상차·수신은 고정형 또는 이동형 로봇팔, 운반은
                                적재면을 갖춘 지원 바퀴 모델을 사용합니다.
                                앞 작업으로 이동한 운반차는 도착 층에서 다시 참여할 수 있습니다.
                                층·장비·물품·선행 작업의 적합성은 승인 전과 실행 중 확인합니다.
                              </p>
                              {task.cooperation.donor_id && (
                                <>
                                  <strong className="span-2">
                                    상차·재인수 위치 · 물품 바닥 중심
                                  </strong>
                                  <label className="span-2">
                                    <input
                                      type="checkbox"
                                      checked={task.source != null}
                                      onChange={(e) =>
                                        updateTask({
                                          source: e.target.checked
                                            ? {
                                                ...(project?.items.find(
                                                  (i) => i.id === task.item_id,
                                                )?.pose ?? pose()),
                                              }
                                            : null,
                                        })
                                      }
                                    />
                                    선행 배치 위치 지정 · 실제 관측과 일치해야 진행
                                  </label>
                                  {task.source ? (
                                    (["x", "y", "z", "yaw"] as const).map(
                                      (axis) => (
                                        <Field
                                          key={`source-${axis}`}
                                          label={
                                            axis === "yaw"
                                              ? "초기 물품 방향 (rad)"
                                              : `초기 물품 바닥 ${axis.toUpperCase()} (m)`
                                          }
                                          value={task.source![axis]}
                                          onChange={(value) =>
                                            updateTask({
                                              source: {
                                                ...task.source!,
                                                [axis]: value,
                                              },
                                            })
                                          }
                                        />
                                      ),
                                    )
                                  ) : (
                                    <p className="muted span-2">
                                      물품 설정의 배치 위치를 초기 바닥 중심
                                      위치로 사용합니다.
                                    </p>
                                  )}
                                  <p className="muted span-2">
                                    상차 로봇이 물품을 집는 시작 위치입니다. Z는
                                    선택한 층의 바닥 기준이며 물품 중심 높이가
                                    아닙니다.
                                  </p>
                                  <strong className="span-2">
                                    운반 로봇 위 적재 위치
                                  </strong>
                                  {([0, 1] as const).map((axis) => (
                                    <Field
                                      key={`loading-${axis}`}
                                      label={`적재 ${axis === 0 ? "X" : "Y"} 오프셋 (m)`}
                                      value={
                                        (task.cooperation!.loading_offset ?? [
                                          0, 0,
                                        ])[axis]
                                      }
                                      onChange={(value) => {
                                        const offset: [number, number] = [
                                          ...(task.cooperation!
                                            .loading_offset ?? [0, 0]),
                                        ];
                                        offset[axis] = value;
                                        updateCooperation({
                                          loading_offset: offset,
                                        });
                                      }}
                                    />
                                  ))}
                                  <p className="muted span-2">
                                    운반 로봇 몸체 좌표계의 X·Y입니다. 기본값은
                                    [0, 0]이며, 로봇 회전과 함께 방향이
                                    바뀝니다.
                                  </p>
                                </>
                              )}
                              <label className="span-2">
                                공유 작업 공간의 예약 이름
                                <input
                                  required
                                  value={task.cooperation.workspace_id}
                                  onChange={(e) =>
                                    updateCooperation({
                                      workspace_id: e.target.value,
                                    })
                                  }
                                />
                              </label>
                              <p className="muted span-2">
                                같은 예약 이름을 쓰는 작업은 작업 공간을
                                공유합니다. 로봇과 물품의 실제 적합성은 실행부가
                                확인합니다.
                              </p>
                              {task.cooperation.donor_id && <>
                                <label className="check span-2">
                                  <input type="checkbox" checked={!!task.cooperation.carrier_loading_pose}
                                    onChange={(e) => updateCooperation({carrier_loading_pose: e.target.checked
                                      ? {x: 0, y: 0, z: 0, yaw: 0} : null})} />
                                  상차 전 운반차 접근 위치 지정
                                </label>
                                {task.cooperation.carrier_loading_pose && <>
                                  <p className="muted span-2">팔과 작업 공간을 예약하고 접근합니다. 도착·정렬·정지가 확인된 뒤 물품을 집습니다.</p>
                                  {(["x", "y", "yaw"] as const).map((axis) => <Field key={`loading-${axis}`}
                                    label={axis === "yaw" ? "상차 접근 방향 (rad)" : `상차 접근 ${axis.toUpperCase()} (m)`}
                                    value={task.cooperation!.carrier_loading_pose![axis]}
                                    onChange={(value) => updateCooperation({carrier_loading_pose: {
                                      ...task.cooperation!.carrier_loading_pose!, [axis]: value}})} />)}
                                </>}
                              </>}
                              <strong className="span-2">
                                적재 후 수신 로봇과 만날 위치 · 몸체 원점
                              </strong>
                              {(["x", "y", "z", "yaw"] as const).map((axis) => (
                                <Field
                                  key={`carrier-${axis}`}
                                  label={
                                    axis === "yaw"
                                      ? "운반 방향 (rad)"
                                      : `운반 ${axis.toUpperCase()} (m)`
                                  }
                                  value={
                                    task.cooperation!.carrier_destination[axis]
                                  }
                                  onChange={(value) =>
                                    updateCooperation({
                                      carrier_destination: {
                                        ...task.cooperation!
                                          .carrier_destination,
                                        [axis]: value,
                                      },
                                    })
                                  }
                                />
                              ))}
                              <p className="muted span-2">
                                Z는 선택한 층 바닥 기준입니다. 몸체 원점 높이는
                                물품 바닥 높이와 다릅니다. 적재를 마친 운반
                                로봇이 수신 로봇에게 이동할 목표를 지정하세요.
                              </p>
                              <strong className="span-2">
                                최종 물품 배치 목표 · 바닥 중심
                              </strong>
                            </>
                          )}
                          {(["x", "y", "z"] as const).map((axis) => (
                            <Field
                              key={axis}
                              label={`${task.cooperation ? "물품 바닥" : "목표"} ${axis.toUpperCase()} (m)`}
                              value={task.destination[axis]}
                              onChange={(v) =>
                                updateTask({
                                  destination: {
                                    ...task.destination,
                                    [axis]: v,
                                  },
                                })
                              }
                            />
                          ))}
                          {task.cooperation && (
                            <>
                              <Field
                                label="물품 방향 (rad)"
                                value={task.destination.yaw}
                                onChange={(yaw) =>
                                  updateTask({
                                    destination: { ...task.destination, yaw },
                                  })
                                }
                              />
                              <p className="muted span-2">
                                물품 Z도 선택한 층의 바닥 기준이며, 물품 중심
                                높이가 아닙니다.
                              </p>
                            </>
                          )}
                          <Field
                            label="우선순위"
                            value={task.priority}
                            min={0}
                            max={100}
                            step={1}
                            onChange={(priority) => updateTask({ priority })}
                          />
                          <Field
                            label="발생 시각 (s)"
                            value={task.release_time}
                            min={0}
                            onChange={(release_time) =>
                              updateTask({ release_time })
                            }
                          />
                          <label>
                            기한 (s, 비워두면 없음)
                            <input
                              type="number"
                              min={task.release_time}
                              value={task.deadline ?? ""}
                              onChange={(e) =>
                                updateTask({
                                  deadline:
                                    e.target.value === ""
                                      ? null
                                      : Number(e.target.value),
                                })
                              }
                            />
                          </label>
                          <Field
                            label="작업 수량"
                            value={task.quantity}
                            min={1}
                            step={1}
                            onChange={(quantity) => updateTask({ quantity })}
                          />
                          <Field
                            label="반복 간격 (s)"
                            value={task.interval}
                            min={0}
                            onChange={(interval) => updateTask({ interval })}
                          />
                          <Field
                            label="재시도 횟수"
                            value={task.retries}
                            min={0}
                            step={1}
                            onChange={(retries) => updateTask({ retries })}
                          />
                          <Field
                            label="시간 제한 (s)"
                            value={task.timeout}
                            min={0.1}
                            onChange={(timeout) => updateTask({ timeout })}
                          />
                          <label>
                            사용 물품
                            <select
                              value={task.item_id ?? ""}
                              onChange={(e) =>
                                updateTask({ item_id: e.target.value || null })
                              }
                            >
                              <option value="">
                                {task.cooperation
                                  ? "물품 선택 (필수)"
                                  : "지정 안 함"}
                              </option>
                              {project?.items.map((i) => (
                                <option
                                  key={i.id}
                                  value={i.id}
                                  disabled={
                                    !!task.cooperation &&
                                    i.floor_id !== task.floor_id
                                  }
                                >
                                  {i.name}
                                </option>
                              ))}
                            </select>
                          </label>
                          {!task.cooperation && (
                            <label>
                              우선 로봇
                              <select
                                value={task.preferred_robot ?? ""}
                                onChange={(e) =>
                                  updateTask({
                                    preferred_robot: e.target.value || null,
                                  })
                                }
                              >
                                <option value="">정책이 선택</option>
                                {project?.robots.map((r) => (
                                  <option key={r.id} value={r.id}>
                                    {r.name}
                                  </option>
                                ))}
                              </select>
                            </label>
                          )}
                          <label className="span-2">
                            선행 작업 식별자 (쉼표로 구분)
                            <input
                              value={task.predecessor_ids.join(", ")}
                              onChange={(e) =>
                                updateTask({
                                  predecessor_ids: e.target.value
                                    .split(",")
                                    .map((s) => s.trim())
                                    .filter(Boolean),
                                })
                              }
                            />
                          </label>
                        </div>
                        <JsonEditor
                          value={task}
                          label="출발·인계·체류 세부 설정"
                          onApply={(data) => updateTask(data as Task)}
                        />
                      </>
                    ) : (
                      <Empty title="작업을 선택하세요">
                        선후행, 기한, 물품과 실패 규칙을 설정합니다.
                      </Empty>
                    )}
                  </aside>
                </div>
              ) : (
                <EntityEditor
                  project={project}
                  kind={scenarioTab as "people" | "items"}
                  floorId={floorId}
                  edit={edit}
                />
              )}
            </>
          )}
          {page === "policy" && project && (
            <div className="split">
              <section className="form-panel">
                <h2>오케스트레이션 정책</h2>
                <div className="form-grid">
                  <label className="span-2">
                    정책 이름
                    <input
                      value={project.policy.name}
                      onChange={(e) =>
                        edit((p) => {
                          p.policy.name = e.target.value;
                        })
                      }
                    />
                  </label>
                  <label>
                    배차 기준
                    <select
                      value={project.policy.assignment}
                      onChange={(e) =>
                        edit((p) => {
                          p.policy.assignment = e.target
                            .value as Policy["assignment"];
                        })
                      }
                    >
                      <option value="nearest">가까운 로봇 우선</option>
                      <option value="balanced">작업 분산</option>
                      <option value="deadline">기한 우선</option>
                    </select>
                  </label>
                  <label>
                    통행 경쟁
                    <select
                      value={project.policy.traffic}
                      onChange={(e) =>
                        edit((p) => {
                          p.policy.traffic = e.target
                            .value as Policy["traffic"];
                        })
                      }
                    >
                      <option value="priority">우선순위</option>
                      <option value="fifo">먼저 요청한 순서</option>
                    </select>
                  </label>
                  <label>
                    실패 대응
                    <select
                      value={project.policy.failure}
                      onChange={(e) =>
                        edit((p) => {
                          p.policy.failure = e.target
                            .value as Policy["failure"];
                        })
                      }
                    >
                      <option value="retry">재시도</option>
                      <option value="reassign">재할당</option>
                      <option value="stop">정지</option>
                    </select>
                  </label>
                  <label>
                    충전 목표 방식
                    <select
                      value={project.policy.charge_target_mode ?? "fixed"}
                      onChange={(e) =>
                        edit((p) => {
                          p.policy.charge_target_mode = e.target
                            .value as Policy["charge_target_mode"];
                        })
                      }
                      aria-describedby="charge-target-mode-help"
                    >
                      <option value="fixed">설정값에서 종료</option>
                      <option value="task_budget">예정 작업에 맞춰 충전</option>
                    </select>
                  </label>
                  {(
                    [
                      ["version", "정책 버전", 1],
                      ["safety_distance", "안전 거리 (m)", 0.05],
                      ["speed_limit", "속도 제한 (m/s)", 0.05],
                      ["charge_below", "충전 최소 기준 (%)", 1],
                      ["charge_until", "충전 종료 (%)", 1],
                      ["stale_after", "관측 만료 (s)", 0.1],
                      ["deadlock_timeout", "교착 감지 (s)", 1],
                    ] as const
                  ).map(([key, label, step]) => (
                    <Field
                      key={key}
                      label={label}
                      value={project.policy[key]}
                      step={step}
                      onChange={(v) =>
                        edit((p) => {
                          p.policy[key] = v;
                        })
                      }
                    />
                  ))}
                </div>
                <p className="muted" id="charge-target-mode-help">
                  {(project.policy.charge_target_mode ?? "fixed") ===
                  "task_budget"
                    ? "종료 설정값을 최소 목표로 삼아 통로 비움·다음 작업·충전 복귀·예비량을 계산합니다. 업무 목표가 100%를 넘거나 미정이어도, 통로 비움과 다음 충전 예비량을 계산할 수 있으면 기본 충전을 따로 검토합니다. 기본 예비량도 미정이거나 100%를 넘으면 예약을 보류합니다. 작업 배정이나 완료를 보장하지 않습니다."
                    : "충전 종료 설정값에 도달하면 분리를 진행합니다. 이후 이동·업무에 필요한 잔량도 확인하세요."}
                </p>
                <p className="muted">
                  대기·접근·도킹에 필요한 예상 에너지와 예비량에 따라 최소
                  기준보다 일찍 충전을 요청할 수 있습니다. 충전 종료 기준이 이후
                  이동·업무 예비량을 충족하는지도 확인하세요.
                </p>
                <JsonDetails
                  title="현재 실행에 적용한 정책 식별"
                  data={
                    runtimeProject && runtimeProject.runId === state?.run_id
                      ? {
                          run_id: runtimeProject.runId,
                          policy: runtimeProject.project.policy,
                        }
                      : {
                          message:
                            "현재 실행과 일치하는 정책 구성을 아직 받지 못했습니다.",
                        }
                  }
                />
                <JsonDetails
                  title="편집 중인 정책 초안"
                  data={{
                    policy: project.policy,
                    matches_current_run:
                      runtimeProject && runtimeProject.runId === state?.run_id
                        ? JSON.stringify(
                            Object.entries(project.policy).sort(),
                          ) ===
                          JSON.stringify(
                            Object.entries(
                              runtimeProject.project.policy,
                            ).sort(),
                          )
                        : null,
                    note: "변경한 정책은 초안을 적용한 새 실행부터 사용됩니다.",
                  }}
                />
              </section>
              <aside>
                <section className="form-panel">
                  <h2>물리와 실행 주기</h2>
                  <div className="form-grid">
                    {(
                      [
                        ["timestep", "물리 시간 간격 (s)", 0.0005],
                        ["control_hz", "로봇 제어 (Hz)", 1],
                        ["orchestration_hz", "관제 (Hz)", 1],
                        ["render_hz", "상태 화면 전송 (Hz)", 1],
                        ["seed", "난수 시드", 1],
                      ] as const
                    ).map(([key, label, step]) => (
                      <Field
                        key={key}
                        label={label}
                        value={project.physics[key]}
                        step={step}
                        onChange={(v) =>
                          edit((p) => {
                            p.physics[key] = v;
                          })
                        }
                      />
                    ))}
                    <label>
                      정밀도
                      <select
                        value={project.physics.fidelity}
                        onChange={(e) =>
                          edit((p) => {
                            p.physics.fidelity = e.target.value as
                              "detailed" | "operational";
                          })
                        }
                      >
                        <option value="detailed">상세 동역학</option>
                        <option value="operational">운영 정밀도</option>
                      </select>
                    </label>
                    <Field
                      label="접촉 임피던스 비 (impratio · 무차원)"
                      value={project.physics.impratio ?? 1}
                      min={1}
                      max={100}
                      step="any"
                      onChange={(impratio) =>
                        edit((p) => {
                          p.physics.impratio = impratio;
                        })
                      }
                    />
                    <p className="muted span-2">
                      MuJoCo 전역 접촉 연구 설정입니다. 기본 1, 범위 1~100이며
                      제조사 사양이 아닙니다. 변경은 실행부 적용 시 새 실행에
                      반영됩니다.
                    </p>
                  </div>
                </section>
                <section className="form-panel section">
                  <h2>현재 실행에 장애 주입</h2>
                  <div className="form-grid">
                    <label className="span-2">
                      대상
                      <select
                        value={selected}
                        onChange={(e) => setSelected(e.target.value)}
                      >
                        <option value="">대상 선택</option>
                        {faultTargets.map((x) => (
                          <option key={x.id} value={x.id}>
                            {x.name}
                          </option>
                        ))}
                      </select>
                    </label>
                    <label>
                      장애 유형
                      <select
                        value={faultKind}
                        onChange={(e) => setFaultKind(e.target.value)}
                      >
                        {[
                          ["motor", "구동기"],
                          ["sensor", "센서"],
                          ["communication", "통신"],
                          ["battery", "배터리"],
                          ["facility", "시설"],
                          ["push", "외력"],
                          ["recover", "복구"],
                        ].map(([v, n]) => (
                          <option key={v} value={v}>
                            {n}
                          </option>
                        ))}
                      </select>
                    </label>
                    <Field
                      label="지속 시간 (s)"
                      value={faultDuration}
                      min={0.1}
                      onChange={setFaultDuration}
                    />
                  </div>
                  <button
                    className="danger"
                    disabled={!faultTargetAvailable || !live || !!busy}
                    title={
                      !live
                        ? "최신 실행 상태를 수신한 뒤 사용할 수 있습니다."
                        : !faultTargetAvailable
                          ? "현재 실행에 있는 대상을 선택하세요."
                          : "선택한 대상에 시뮬레이션 장애를 요청합니다."
                    }
                    style={{ marginTop: 16 }}
                    onClick={() =>
                      run("장애 주입", () =>
                        api.fault(selected, faultKind, faultDuration, 100),
                      )
                    }
                  >
                    <ShieldAlert size={14} />
                    실행에 주입
                  </button>
                </section>
              </aside>
            </div>
          )}
          {page === "facilities" &&
            (() => {
              const snapshot = state;
              const project =
                runtimeProject &&
                snapshot &&
                runtimeProject.runId === snapshot.run_id &&
                !runTransition.current
                  ? runtimeProject.project
                  : null;
              if (!project || !snapshot)
                return (
                  <Empty title="현재 실행의 시설 구성을 기다립니다">
                    실행 식별자가 일치하는 구성을 받으면 시설 목록과 조작이
                    표시됩니다. 편집 초안은 환경 편집에서 확인하세요.
                  </Empty>
                );
              const facilities = project.environment.elements.filter((entry) =>
                ["elevator", "door", "charger", "dock", "loading"].includes(
                  entry.kind,
                ),
              );
              if (!facilities.length)
                return (
                  <Empty title="현재 실행에 표시할 시설이 없습니다">
                    환경 편집에서 시설을 추가한 뒤 실행부에 적용하세요.
                  </Empty>
                );
              const element = facilities.find((entry) => entry.id === selected);
              const selectedRuntime = element
                ? snapshot.facilities.find(
                    (entry) =>
                      entry.id === element.id || entry.entity_id === element.id,
                  )
                : undefined;
              const draftFacility = element
                ? currentProject.current?.environment.elements.find(
                    (entry) => entry.id === element.id,
                  )
                : undefined;
              const phaseLabels: Record<string, string> = {
                closing_empty: "빈 객실 문 닫기",
                positioning: "탑승층으로 이동",
                opening_call: "호출층 문 열기",
                opening_board: "탑승층 문 열기",
                boarding: "탑승 확인",
                closing_depart: "출발 전 문 닫기",
                opening_exit: "목적층 문 열기",
                alighting: "하차 확인",
              };
              const robotLabels = (ids: unknown) =>
                Array.isArray(ids)
                  ? ids.length
                    ? ids
                        .map((id) =>
                          typeof id === "string"
                            ? `${snapshot.robots.find((robot) => robot.id === id)?.name ?? project.robots.find((robot) => robot.id === id)?.name ?? "이름 미확인"} (${id})`
                            : "식별자 미확인",
                        )
                        .join(", ")
                    : "없음"
                  : "미수신";
              return (
                <>
                  <p className="muted">
                    현재 실행 {snapshot.run_id.slice(0, 8)} ·{" "}
                    {fmt(snapshot.sim_time, 3)} s
                    {!live
                      ? " · 마지막 수신 상태 · 연결 복구 전에는 요청할 수 없습니다."
                      : " · 실행 구성 기준"}
                  </p>
                  <div className="table-wrap">
                    <table>
                      <thead>
                        <tr>
                          <th>시설</th>
                          <th>유형</th>
                          <th>구성 층 / 서비스 층</th>
                          <th>용량 설정 / 하중 한도</th>
                          <th>상태</th>
                          <th>예약 / 대기 / 보고 점유</th>
                          <th>누적 대기 (대·초)</th>
                        </tr>
                      </thead>
                      <tbody>
                        {facilities.map((e) => {
                          const runtime = snapshot.facilities.find(
                            (f) => f.id === e.id || f.entity_id === e.id,
                          );
                          return (
                            <tr
                              key={e.id}
                              className="selectable"
                              onClick={() => setSelected(e.id)}
                            >
                              <td>
                                <button
                                  className="ghost"
                                  onClick={() => setSelected(e.id)}
                                >
                                  {e.name}
                                </button>
                                <div
                                  className="muted"
                                  title={`시설 ID: ${e.id}`}
                                >
                                  {e.id.length > 18
                                    ? `${e.id.slice(0, 8)}…${e.id.slice(-6)}`
                                    : e.id}
                                </div>
                                <div className="muted">
                                  구성 X {fmt(e.pose.x)} / Y {fmt(e.pose.y)} m
                                </div>
                              </td>
                              <td>{elementNames[e.kind]}</td>
                              <td>
                                {project.environment.floors.find(
                                  (f) => f.id === e.floor_id,
                                )?.name ?? `층 확인 불가 (${e.floor_id})`}{" "}
                                /{" "}
                                {e.facility.served_floors
                                  .map(
                                    (id) =>
                                      project.environment.floors.find(
                                        (f) => f.id === id,
                                      )?.name ?? `층 확인 불가 (${id})`,
                                  )
                                  .join(", ") || "구성 층만"}
                              </td>
                              <td>
                                {e.facility.capacity}대 / {e.facility.max_load}{" "}
                                kg
                              </td>
                              <td>
                                <Badge
                                  value={
                                    phaseLabels[
                                      String(runtime?.status ?? runtime?.phase)
                                    ] ??
                                    String(
                                      runtime?.status ??
                                        runtime?.phase ??
                                        "상태 미수신",
                                    )
                                  }
                                />
                              </td>
                              <td>
                                <div>
                                  예약:{" "}
                                  {robotLabels(
                                    runtime?.reserved_by ??
                                      runtime?.reservations,
                                  )}
                                </div>
                                <div>대기: {robotLabels(runtime?.queue)}</div>
                                <div>
                                  점유: {robotLabels(runtime?.occupants)}
                                </div>
                              </td>
                              <td>
                                {Number(
                                  measuredFacilities?.[e.id]?.known_seconds ??
                                    0,
                                ) > 0
                                  ? fmt(
                                      measuredFacilities?.[e.id]
                                        ?.queue_wait_seconds,
                                    )
                                  : "—"}
                              </td>
                            </tr>
                          );
                        })}
                      </tbody>
                    </table>
                  </div>
                  {element && (
                    <section className="section form-panel">
                      <h2>{element.name} · 시설 상세</h2>
                      {["elevator", "charger"].includes(element.kind) && (
                        <>
                          <div className="metric-strip">
                            <Stat
                              label="누적 대기"
                              value={facilityMeasurement("queue_wait_seconds")}
                              unit="대·초"
                            />
                            <Stat
                              label="배정 완료 평균 대기"
                              value={facilityMeasurement(
                                "completed_queue_wait_mean_seconds",
                              )}
                              unit="초"
                            />
                            <Stat
                              label="보고된 점유"
                              value={facilityMeasurement("occupied_seconds")}
                              unit="초"
                            />
                            <Stat
                              label="고장 상태"
                              value={facilityMeasurement("fault_seconds")}
                              unit="초"
                            />
                          </div>
                          <p className="muted">
                            누적 대기는 각 로봇이 대기열에서 기다린 시간의
                            합입니다. 평균은 진입부터 배정까지 확인된 대기만
                            포함하며, 취소·진행 중·관측이 끊긴 구간은
                            제외합니다. 점유는 시설이 보고한 로봇 목록을
                            기준으로 합니다. 실행 전에는 측정값이 표시되지
                            않습니다.
                          </p>
                        </>
                      )}
                      {element.kind === "elevator" && (
                        <div className="toolbar" style={{ marginTop: 16 }}>
                          {(element.facility.served_floors.length
                            ? element.facility.served_floors
                            : [element.floor_id]
                          ).map((id) => {
                            const targetFloor = project.environment.floors.find(
                              (f) => f.id === id,
                            );
                            const sourceFloor = project.environment.floors.find(
                              (f) => f.id === element.floor_id,
                            );
                            return (
                              <button
                                key={id}
                                disabled={
                                  !live ||
                                  !!busy ||
                                  !selectedRuntime ||
                                  !targetFloor ||
                                  !sourceFloor
                                }
                                title={
                                  !live
                                    ? "신선한 실행 상태를 받은 뒤 요청할 수 있습니다."
                                    : busy
                                      ? "진행 중인 요청이 끝나면 사용할 수 있습니다."
                                      : !selectedRuntime
                                        ? "현재 시설 상태를 아직 받지 못했습니다."
                                        : !targetFloor || !sourceFloor
                                          ? "현재 실행에서 대상·기준 층을 확인할 수 없습니다."
                                          : "현재 실행의 승강기에 층 이동을 요청합니다. 도착은 이후 시설 상태로 확인하세요."
                                }
                                onClick={() =>
                                  run("승강기 목표 층 요청", async () => {
                                    if (
                                      currentState.current?.run_id !==
                                        snapshot.run_id ||
                                      runTransition.current ||
                                      !targetFloor ||
                                      !sourceFloor
                                    )
                                      throw new Error(
                                        "실행이 바뀌었거나 시설의 층 정보를 확인할 수 없습니다. 현재 실행 구성을 받은 뒤 다시 요청하세요.",
                                      );
                                    await api.facilityTarget(
                                      element.id,
                                      pose(
                                        0,
                                        0,
                                        targetFloor.elevation -
                                          sourceFloor.elevation,
                                      ),
                                    );
                                    await refresh();
                                    if (
                                      currentState.current?.run_id ===
                                      snapshot.run_id
                                    )
                                      setNotice(
                                        "승강기 요청 응답을 받았습니다. 실제 도착은 시설의 위치·문 상태에서 확인하세요.",
                                      );
                                  })
                                }
                              >
                                {targetFloor?.name ?? `층 확인 불가 (${id})`}{" "}
                                이동 요청
                              </button>
                            );
                          })}
                        </div>
                      )}
                      <JsonDetails
                        title="현재 실행 상태"
                        data={
                          snapshot.facilities.find(
                            (f) =>
                              f.id === element.id || f.entity_id === element.id,
                          ) ?? { message: "실행 상태 미수신" }
                        }
                      />
                      <JsonDetails
                        title="현재 실행의 시설 설정"
                        data={element.facility}
                      />
                      <p className="muted">
                        시설 설정은 환경 편집의 초안에서 수정한 뒤 적용하세요.
                      </p>
                      <button
                        disabled={!draftFacility}
                        title={
                          !draftFacility
                            ? "현재 편집 초안에 동일한 시설이 없습니다."
                            : "환경 편집의 초안으로 이동합니다. 현재 실행은 바뀌지 않습니다."
                        }
                        onClick={() => {
                          if (!draftFacility) return;
                          setSelected(draftFacility.id);
                          setFloorId(draftFacility.floor_id);
                          setTool(null);
                          navigate("environment");
                        }}
                      >
                        환경 편집의 초안에서 수정
                      </button>
                    </section>
                  )}
                </>
              );
            })()}
          {page === "events" && (
            <>
              <div className="section-head">
                <div className="toolbar">
                  <input
                    aria-label="사건 검색"
                    placeholder="사건·개체·이유 검색"
                    value={eventFilter}
                    onChange={(e) => setEventFilter(e.target.value)}
                  />
                  <button
                    disabled={!state}
                    onClick={() => {
                      if (!state) return;
                      downloadJSON(`events-${state.run_id}.json`, state.events);
                      setNotice(
                        `실행 ${state.run_id.slice(0, 8)}의 사건 JSON 다운로드를 요청했습니다.`,
                      );
                    }}
                  >
                    <ArrowDownToLine size={14} />
                    사건 내보내기
                  </button>
                </div>
                <span className="muted">
                  현재 실행의 기록 · 시뮬레이션 시간
                </span>
              </div>
              <div className="timeline">
                {state?.events
                  .filter((e) =>
                    JSON.stringify(e)
                      .toLowerCase()
                      .includes(eventFilter.toLowerCase()),
                  )
                  .slice()
                  .reverse()
                  .map((e) => (
                    <article className="event" key={e.seq}>
                      <time>{fmt(e.time, 3)} s</time>
                      <span className="dot" />
                      <div>
                        <strong>{describeRuntimeEvent(e).title}</strong>
                        <p>{describeRuntimeEvent(e).summary}</p>
                        <p>
                          {e.entity_id ?? "실행"} · {e.kind}
                        </p>
                        <div className="event-actions">
                          {relatedEventEntity(e) && (
                            <button
                              className="ghost"
                              onClick={() => {
                                navigate("monitor");
                                chooseEntity(relatedEventEntity(e)!);
                              }}
                            >
                              관련 객체 보기
                            </button>
                          )}
                          <button
                            className="ghost"
                            onClick={() =>
                              setRecordingSeek({
                                runId: state!.run_id,
                                time: e.time,
                                entityId: relatedEventEntity(e),
                              })
                            }
                          >
                            기록 시점 보기
                          </button>
                        </div>
                        {Object.keys(e.details ?? {}).length > 0 && (
                          <JsonDetails
                            title="결정 근거와 상세"
                            data={e.details}
                          />
                        )}
                      </div>
                      <Badge
                        value={e.severity}
                        tone={
                          e.severity === "error"
                            ? "danger"
                            : e.severity === "warning"
                              ? "warn"
                              : undefined
                        }
                      />
                    </article>
                  ))}
              </div>
              {!state?.events.length && (
                <Empty title="아직 기록된 사건이 없습니다">
                  실행을 시작하면 명령과 물리 사건, 정책 결정이 같은 타임라인에
                  기록됩니다.
                </Empty>
              )}
              <RecordingView
                seek={recordingSeek}
                adopt={(p) => {
                  adopt(p);
                  navigate("environment");
                  setView("2d");
                }}
                run={run}
              />
            </>
          )}
          {page === "experiments" && (
            <>
              <p className="muted">
                아래 현재 측정값은 실행 {state?.run_id ?? "미수신"} 기준입니다.
                {!live && state
                  ? " 마지막 수신 상태이며 연결을 확인하고 있습니다."
                  : ""}
                저장된 반복 실험 결과와 구분해 확인하세요.
              </p>
              <div className="metric-strip">
                <Stat
                  label="종료 작업 성공률"
                  value={
                    typeof state?.metrics.success_rate === "number"
                      ? state.metrics.success_rate * 100
                      : null
                  }
                  unit="%"
                />
                <Stat
                  label="이동 거리"
                  value={state?.metrics.distance_m}
                  unit="m"
                />
                <Stat
                  label="충돌"
                  value={state?.metrics.collisions}
                  unit="회"
                />
                <Stat
                  label="물리 처리 배속"
                  value={state?.metrics.physics_realtime_factor}
                  unit="×"
                />
              </div>
              {state ? (
                (() => {
                  const completed = state.tasks.filter(
                    (task) => task.status === "completed",
                  ).length;
                  const failed = state.tasks.filter(
                    (task) => task.status === "failed",
                  ).length;
                  const cancelled = state.tasks.filter(
                    (task) => task.status === "cancelled",
                  ).length;
                  const unfinished =
                    state.tasks.length - completed - failed - cancelled;
                  return (
                    <p className="muted">
                      현재 실행: 완료 {completed}건 · 실패 {failed}건 · 미종료{" "}
                      {unfinished}건
                      {cancelled > 0 ? ` · 취소 ${cancelled}건` : ""} · 전체{" "}
                      {state.tasks.length}건.
                      {completed + failed > 0
                        ? ` 성공률은 종료 작업 ${completed + failed}건 중 완료 비율이며, 미종료·취소는 제외합니다.`
                        : " 완료·실패로 종료된 작업이 없어 성공률은 아직 산출되지 않았습니다."}
                    </p>
                  );
                })()
              ) : (
                <p className="muted">
                  현재 실행의 작업 건수를 아직 받지 못했습니다.
                </p>
              )}
              <div className="split">
                <section>
                  <div className="section-head">
                    <h2>반복 실험 기록</h2>
                    <button
                      onClick={() =>
                        run("실험 목록 새로고침", async () =>
                          setExperiments(await api.experiments()),
                        )
                      }
                    >
                      <RotateCcw size={13} />
                      새로고침
                    </button>
                  </div>
                  {experiments.length ? (
                    <div style={{ minWidth: 0 }}>
                      {experiments.map((e) => {
                        const record = (
                          value: unknown,
                        ): Record<string, unknown> =>
                          value &&
                          typeof value === "object" &&
                          !Array.isArray(value)
                            ? (value as Record<string, unknown>)
                            : {};
                        const finite = (value: unknown): value is number =>
                          typeof value === "number" && Number.isFinite(value);
                        const rows = (value: unknown) =>
                          Array.isArray(value)
                            ? value
                                .filter(
                                  (v) =>
                                    v &&
                                    typeof v === "object" &&
                                    !Array.isArray(v),
                                )
                                .map(record)
                            : [];
                        const groups = rows(e.summary),
                          runs = rows(e.runs);
                        const policyName = (value: unknown) =>
                          typeof value === "string"
                            ? ({
                                nearest: "가까운 로봇 우선",
                                balanced: "작업 분산",
                                deadline: "기한 우선",
                              }[value] ?? value)
                            : "정책명 미기록";
                        const textValue = (value: unknown) =>
                          typeof value === "string" || finite(value)
                            ? String(value)
                            : "미기록";
                        const metrics: [string, string, string][] = [
                          ["completed", "완료 작업", "건"],
                          ["collisions", "충돌", "회"],
                          ["distance_m", "이동 거리", "m"],
                          ["energy_j", "사용 에너지", "J"],
                          [
                            "facility_queue_wait_seconds",
                            "시설 대기 합계",
                            "대·초",
                          ],
                          [
                            "charging_queue_wait_seconds",
                            "충전 대기 합계",
                            "대·초",
                          ],
                        ];
                        const extraMetrics: [string, string, string][] = [
                          ["physics_realtime_factor", "물리 처리 배속", "×"],
                          [
                            "facility_fault_seconds",
                            "시설 장애 합계",
                            "시설·초",
                          ],
                          ["cooperative_recovery_started", "복구 시작", "건"],
                          ["cooperative_recovery_completed", "복구 완료", "건"],
                          [
                            "cooperative_recovery_failed_or_cancelled",
                            "복구 실패·취소",
                            "건",
                          ],
                          [
                            "cooperative_recovery_mean_active_seconds",
                            "실행별 복구 소요 평균",
                            "초",
                          ],
                          [
                            "cooperative_recovery_mean_failure_to_recovery_seconds",
                            "실행별 실패 후 복구 평균",
                            "초",
                          ],
                        ];
                        const comparison = (
                          definitions: [string, string, string][],
                        ) => (
                          <div
                            className="table-wrap"
                            role="region"
                            tabIndex={0}
                            aria-label={`${e.name ?? e.id} 정책별 측정 비교`}
                          >
                            <table style={{ whiteSpace: "normal" }}>
                              <thead>
                                <tr>
                                  <th scope="col">측정 항목</th>
                                  {groups.map((group, index) => (
                                    <th
                                      scope="col"
                                      key={`${textValue(group.policy_sha256)}:${index}`}
                                    >
                                      <strong>
                                        {policyName(
                                          group.name ?? group.policy_id,
                                        )}
                                      </strong>
                                      <br />v{textValue(group.policy_version)} ·{" "}
                                      {textValue(group.policy_id)}
                                      <br />
                                      <span
                                        title={textValue(group.policy_sha256)}
                                      >
                                        정책 해시{" "}
                                        {typeof group.policy_sha256 === "string"
                                          ? group.policy_sha256.slice(0, 8)
                                          : "미기록"}
                                      </span>
                                    </th>
                                  ))}
                                </tr>
                              </thead>
                              <tbody>
                                {definitions.map(([key, label, unit]) => (
                                  <tr key={key}>
                                    <th scope="row">
                                      {label}
                                      <br />
                                      <span>({unit})</span>
                                    </th>
                                    {groups.map((group, index) => {
                                      const stat = record(
                                        record(group.metrics)[key],
                                      );
                                      const n =
                                        finite(stat.n) &&
                                        Number.isInteger(stat.n) &&
                                        stat.n >= 0
                                          ? stat.n
                                          : null;
                                      const available =
                                        finite(stat.mean) && n !== 0;
                                      return (
                                        <td key={index}>
                                          <strong>
                                            {available
                                              ? fmt(stat.mean, 3)
                                              : "미기록"}
                                          </strong>
                                          <br />
                                          <span className="muted">
                                            {n === null
                                              ? "표본수 미기록"
                                              : `n=${n}`}
                                          </span>
                                          {available && (
                                            <>
                                              <br />
                                              <span className="muted">
                                                {n === 1
                                                  ? "단일 표본 · 편차 없음"
                                                  : n !== null &&
                                                      n > 1 &&
                                                      finite(stat.stddev)
                                                    ? `표준편차 ${fmt(stat.stddev, 3)}`
                                                    : "편차 미기록"}
                                              </span>
                                            </>
                                          )}
                                          {finite(stat.unavailable_n) &&
                                            stat.unavailable_n > 0 && (
                                              <>
                                                <br />
                                                <span className="muted">
                                                  미기록 {stat.unavailable_n}회
                                                </span>
                                              </>
                                            )}
                                        </td>
                                      );
                                    })}
                                  </tr>
                                ))}
                              </tbody>
                            </table>
                          </div>
                        );
                        return (
                          <article
                            className="section"
                            key={e.id}
                            style={{ minWidth: 0 }}
                          >
                            <div className="section-head">
                              <div>
                                <h3>{e.name ?? "저장된 실험"}</h3>
                                <p>
                                  실험 {e.id}
                                  {e.created_at ? ` · ${e.created_at}` : ""}
                                </p>
                                <p>
                                  실행 시간{" "}
                                  {finite(e.duration)
                                    ? `${e.duration} s`
                                    : "미기록"}{" "}
                                  · 시드{" "}
                                  {Array.isArray(e.seeds) && e.seeds.length
                                    ? e.seeds.map(textValue).join(", ")
                                    : "미기록"}
                                </p>
                              </div>
                              <div className="toolbar">
                                <a
                                  href={`/api/experiments/${encodeURIComponent(e.id)}/export?format=json`}
                                  download
                                >
                                  JSON
                                </a>
                                <a
                                  href={`/api/experiments/${encodeURIComponent(e.id)}/export?format=csv`}
                                  download
                                >
                                  CSV
                                </a>
                              </div>
                            </div>
                            {groups.length ? (
                              <>
                                <p className="muted">
                                  실행별 측정값의 평균입니다. n은 값이 기록된
                                  실행 수이며, 1회 결과에는 표준편차가 없습니다.
                                  완료 건수가 높다는 이유만으로 모든 작업의
                                  성공을 뜻하지 않습니다.
                                </p>
                                {comparison(metrics)}
                                <details className="details">
                                  <summary>
                                    복구·시설 장애·처리 속도 비교
                                  </summary>
                                  <p className="muted">
                                    복구 시간은 각 실행의 완료 복구 평균을 같은
                                    비중으로 다시 평균한 값입니다. 전체 복구
                                    사건을 합친 평균이 아닙니다. 완료 복구가
                                    없는 실행의 시간은 미기록이며, 진행 중인
                                    복구를 완료로 세지 않습니다.
                                  </p>
                                  {comparison(extraMetrics)}
                                </details>
                              </>
                            ) : (
                              <Empty title="정책별 집계가 없습니다">
                                이전 형식이거나 집계가 기록되지 않은 결과입니다.
                                시드별 기록과 원시 데이터를 확인하세요.
                              </Empty>
                            )}
                            <details className="details">
                              <summary>
                                시드별 작업 결과 · {runs.length}회 기록
                              </summary>
                              <p className="muted">
                                성공률은 완료와 실패로 종료된 작업 중 완료
                                비율입니다. 실패 열은 작업 실패 건수이며 실행
                                엔진의 종료 상태는 이 요약에 기록되지 않습니다.
                              </p>
                              {runs.length ? (
                                <div
                                  className="table-wrap"
                                  role="region"
                                  tabIndex={0}
                                  aria-label="시드별 실행 결과"
                                >
                                  <table style={{ whiteSpace: "normal" }}>
                                    <thead>
                                      <tr>
                                        <th>실행·정책</th>
                                        <th>시드</th>
                                        <th>전체 작업</th>
                                        <th>완료</th>
                                        <th>실패</th>
                                        <th>성공률</th>
                                      </tr>
                                    </thead>
                                    <tbody>
                                      {runs.map((row, index) => {
                                        const measured = record(row.metrics);
                                        return (
                                          <tr
                                            key={`${textValue(row.run_id)}:${index}`}
                                          >
                                            <td
                                              style={{
                                                overflowWrap: "anywhere",
                                              }}
                                            >
                                              <strong>
                                                {policyName(
                                                  row.policy ?? row.policy_id,
                                                )}
                                              </strong>
                                              <br />v
                                              {textValue(row.policy_version)} ·{" "}
                                              <span
                                                title={textValue(
                                                  row.policy_sha256,
                                                )}
                                              >
                                                정책 해시{" "}
                                                {typeof row.policy_sha256 ===
                                                "string"
                                                  ? row.policy_sha256.slice(
                                                      0,
                                                      8,
                                                    )
                                                  : "미기록"}
                                              </span>
                                              <br />
                                              <span
                                                title={textValue(row.run_id)}
                                              >
                                                실행 {textValue(row.run_id)}
                                              </span>
                                            </td>
                                            <td>{textValue(row.seed)}</td>
                                            <td>
                                              {textValue(measured.task_count)}
                                            </td>
                                            <td>
                                              {textValue(measured.completed)}
                                            </td>
                                            <td>
                                              {textValue(measured.failed)}
                                            </td>
                                            <td>
                                              {finite(measured.success_rate)
                                                ? `${fmt(measured.success_rate * 100, 1)} %`
                                                : "종료 표본 없음·미기록"}
                                            </td>
                                          </tr>
                                        );
                                      })}
                                    </tbody>
                                  </table>
                                </div>
                              ) : (
                                <p className="muted">
                                  시드별 실행 기록이 없습니다. 값을 0으로
                                  대신하지 않습니다.
                                </p>
                              )}
                            </details>
                            <p className="muted">
                              같은 초기 구성·시드·시간·정밀도의 결과끼리
                              비교하세요. 실제 장비 성능을 보장하는 수치가
                              아닙니다.
                            </p>
                            <JsonDetails
                              title="원시 집계·실행 식별·검증 한계"
                              data={e}
                            />
                          </article>
                        );
                      })}
                    </div>
                  ) : (
                    <Empty title="저장된 실험이 없습니다">
                      정책과 시드를 선택하면 동일한 환경을 초기 조건부터 반복
                      계산합니다.
                    </Empty>
                  )}
                  <JsonDetails
                    title="현재 실행의 전체 측정값"
                    data={state?.metrics ?? {}}
                  />
                </section>
                <aside className="form-panel">
                  <h2>정책 비교 실험</h2>
                  <p className="muted">
                    편집 중인 초안을 초기 조건으로 사용합니다. 선택한 배차
                    기준만 바꾸며, 나머지 정책 설정은 초안과 같습니다. 현재 관제
                    실행은 이 실험과 별개입니다.
                  </p>
                  <button className="ghost" onClick={() => navigate("policy")}>
                    정책 설정 검토
                  </button>
                  <div className="form-grid">
                    <label className="span-2">
                      난수 시드 (쉼표로 구분)
                      <input
                        value={seeds}
                        onChange={(e) => setSeeds(e.target.value)}
                      />
                    </label>
                    <Field
                      label="시드별 실행 시간 (s)"
                      value={duration}
                      min={0.1}
                      step={1}
                      onChange={setDuration}
                    />
                    <div className="span-2">
                      <p className="muted" style={{ marginBottom: 10 }}>
                        비교할 배차 정책
                      </p>
                      {[
                        ["nearest", "가까운 로봇 우선"],
                        ["balanced", "작업 분산"],
                        ["deadline", "기한 우선"],
                      ].map(([id, n]) => (
                        <label style={{ marginBottom: 8 }} key={id}>
                          <input
                            type="checkbox"
                            checked={comparePolicies.includes(id)}
                            onChange={(e) =>
                              setComparePolicies(
                                e.target.checked
                                  ? [...comparePolicies, id]
                                  : comparePolicies.filter((p) => p !== id),
                              )
                            }
                          />
                          {n}
                        </label>
                      ))}
                    </div>
                  </div>
                  <button
                    className="primary"
                    disabled={
                      !project || !live || !!busy || !comparePolicies.length
                    }
                    title={
                      !project
                        ? "프로젝트를 먼저 불러오세요."
                        : !live
                          ? "실행부 연결이 복구되면 실험을 시작할 수 있습니다."
                          : busy
                            ? `${busy} 작업을 기다리세요.`
                            : !comparePolicies.length
                              ? "비교할 배차 정책을 하나 이상 선택하세요."
                              : "현재 초안의 초기 조건으로 별도 반복 실험을 실행합니다."
                    }
                    style={{ marginTop: 20 }}
                    onClick={() =>
                      run("반복 실험 실행 중", async () => {
                        const source = checkDraft();
                        const tokens = seeds.split(",").map((v) => v.trim());
                        const seedList = tokens.map(Number);
                        if (
                          tokens.length > 50 ||
                          tokens.some((v) => !v) ||
                          seedList.some(
                            (v) => !Number.isSafeInteger(v) || v < 0,
                          )
                        )
                          throw new Error(
                            "시드를 0 이상의 정수로 1~50개 입력하세요. 빈 항목 없이 쉼표로 구분합니다.",
                          );
                        if (
                          !Number.isFinite(duration) ||
                          duration <= 0 ||
                          duration > 3600
                        )
                          throw new Error(
                            "시드별 실행 시간은 0초 초과, 3600초 이하로 입력하세요.",
                          );
                        const result = await api.experiment(
                          source,
                          seedList,
                          duration,
                          comparePolicies.map((assignment) => ({
                            ...source.policy,
                            id: assignment,
                            assignment: assignment as Policy["assignment"],
                            name: assignment,
                          })),
                        );
                        setExperiments(await api.experiments());
                        setNotice(
                          `반복 실험 ${result.id}의 측정 결과를 저장했습니다. 작업 완료·실패 건수와 표본수를 확인하세요.`,
                        );
                      })
                    }
                  >
                    <Play size={14} />
                    물리 재계산
                  </button>
                  <p className="muted" style={{ fontSize: 12, marginTop: 14 }}>
                    각 실행은 구성·모델·제어기·정책·시드를 기록합니다. 저장된
                    사건을 표시하는 로그 재생과 구분됩니다.
                  </p>
                </aside>
              </div>
            </>
          )}
          {mapPage && (
            <RuntimeTimeline
              state={state}
              project={
                runtimeProject && runtimeProject.runId === state?.run_id
                  ? runtimeProject.project
                  : null
              }
              connected={live}
              onSelectEntity={chooseEntity}
              onOpenEvents={() => navigate("events")}
              defaultCollapsed={true}
              defaultHeight={220}
              key={`${page}:${state?.run_id ?? "pending"}`}
              onSeekEvent={(event) => {
                if (state) {
                  setRecordingSeek({
                    runId: state.run_id,
                    time: event.time,
                    entityId: event.entity_id,
                  });
                  navigate("events");
                  if (event.entity_id) chooseEntity(event.entity_id);
                }
              }}
            />
          )}
          <footer className="footer">
            <span>좌표: 오른손 · Z축 위 · SI 단위</span>
            <span>
              {connected
                ? `실행 상태 수신 ${new Date(lastUpdate).toLocaleTimeString("ko-KR")}`
                : "서버 실행 후 화면이 연결됩니다"}{" "}
              · 실제 장비 검증 미완료
            </span>
          </footer>
        </div>
      </main>
    </div>
  );
}
function AgvRouteEditor({
  robot,
  update,
}: {
  robot: RobotInstance;
  update: (value: Partial<RobotInstance>) => void;
}) {
  const section = useRef<HTMLElement>(null);
  const [rowRevision, setRowRevision] = useState(0);
  const [message, setMessage] = useState("");
  const points = robot.agv_route;
  const { closed, issues } = agvRouteGuidance(points);
  const applyEdit = (edit: AgvRouteEdit) => {
    if (
      edit.kind !== "point" &&
      section.current?.querySelector('input[aria-invalid="true"]')
    ) {
      setMessage(
        "숫자 입력을 먼저 완성한 뒤 경유점을 추가하거나 순서를 바꾸세요.",
      );
      return;
    }
    update({ agv_route: editAgvRoute(points, edit) });
    setMessage("");
    // A point has no persisted ID. Structural edits remount numeric drafts so
    // a blank local field cannot follow a different point after reordering.
    if (edit.kind !== "point") setRowRevision((revision) => revision + 1);
  };
  return (
    <section
      ref={section}
      className="agv-route-editor"
      aria-label="AGV 지정 경로 편집"
    >
      <div className="section-head">
        <h3>AGV 지정 경로</h3>
        <span className="muted">
          {points.length}개 점 · {closed ? "순환 연결" : "열린 경로"}
        </span>
      </div>
      <p className="muted">
        배치 층의 X·Y 좌표(m)를 입력한 순서대로 진행합니다. Z는 0이며 방향은
        rad입니다. 경로 밖 연결이나 역주행은 자동으로 만들지 않습니다.
      </p>
      <div className="agv-route-actions">
        <button
          type="button"
          onClick={() =>
            applyEdit({ kind: "first-at-placement", placement: robot.pose })
          }
          title="초기 배치의 X·Y·방향을 첫 점에 복사합니다. 순환 경로라면 마지막 점도 함께 맞춥니다."
        >
          첫 점을 초기 배치로
        </button>
        <button
          type="button"
          disabled={closed || points.length < 3}
          onClick={() => applyEdit({ kind: "close" })}
        >
          첫 점을 마지막에 복사
        </button>
        {points.some((point) => point.z !== 0) && (
          <button
            type="button"
            onClick={() => applyEdit({ kind: "zero-height" })}
          >
            경로 Z를 모두 0으로
          </button>
        )}
      </div>
      {points.length === 0 ? (
        <p className="agv-route-empty">
          첫 점을 초기 배치에 두고 다음 경유점을 추가하세요. 작업 목표도 지정
          경로 위에 있어야 합니다.
        </p>
      ) : (
        <ol className="agv-route-points">
          {points.map((point, index) => (
            <li key={`${rowRevision}-${index}`}>
              <div className="agv-route-point-head">
                <strong>
                  {index + 1}번 점
                  {closed && index === points.length - 1 ? " · 첫 점 연결" : ""}
                </strong>
                <div className="agv-route-order">
                  <button
                    type="button"
                    className="ghost"
                    disabled={index === 0}
                    aria-label={`${index + 1}번 경유점 위로`}
                    onClick={() =>
                      applyEdit({ kind: "move", index, direction: -1 })
                    }
                  >
                    위
                  </button>
                  <button
                    type="button"
                    className="ghost"
                    disabled={index === points.length - 1}
                    aria-label={`${index + 1}번 경유점 아래로`}
                    onClick={() =>
                      applyEdit({ kind: "move", index, direction: 1 })
                    }
                  >
                    아래
                  </button>
                  <button
                    type="button"
                    className="ghost danger"
                    aria-label={`${index + 1}번 경유점 제거`}
                    onClick={() => applyEdit({ kind: "remove", index })}
                  >
                    제거
                  </button>
                </div>
              </div>
              <div className="form-grid agv-route-coordinates">
                {(["x", "y", "yaw"] as const).map((axis) => (
                  <Field
                    key={axis}
                    label={`${index + 1}번 ${axis === "yaw" ? "방향 (rad)" : `${axis.toUpperCase()} (m)`}`}
                    value={point[axis]}
                    step="any"
                    onChange={(value) =>
                      applyEdit({ kind: "point", index, axis, value })
                    }
                  />
                ))}
              </div>
            </li>
          ))}
        </ol>
      )}
      <button
        type="button"
        onClick={() => applyEdit({ kind: "add", placement: robot.pose })}
      >
        <Plus size={14} /> 경유점 추가
      </button>
      <p className="muted agv-route-help">
        첫 점은 초기 배치, 다음 점은 앞 점의 방향으로 1m 앞에 제안됩니다. 순환
        경로에서는 마지막 연결점 앞에 추가합니다. 공간에 맞게 좌표를 수정하세요.
      </p>
      {message && (
        <p className="field-error" role="status">
          {message}
        </p>
      )}
      {issues.length > 0 && (
        <ul
          className="agv-route-guidance"
          aria-label="경로 구성 안내"
          role="status"
        >
          {issues.map((issue) => (
            <li key={issue}>{issue}</li>
          ))}
        </ul>
      )}
      <p className="muted agv-route-help">
        첫 점의 XY를 마지막에 명시적으로 반복해야 순환합니다. 순환할 때는 서로
        다른 점 3개 이상으로 구성하세요. 이 안내는 경로 충돌·통과 여유·충전
        복귀의 실행부 판정을 대신하지 않습니다.
      </p>
    </section>
  );
}

function RobotEditor({
  robot,
  model,
  project,
  update,
  remove,
}: {
  robot: RobotInstance;
  model?: RobotModel;
  project: Project;
  update: (v: Partial<RobotInstance>) => void;
  remove: () => void;
}) {
  return (
    <>
      <div className="section-head">
        <h2>개체 설정</h2>
        <button
          className="ghost danger"
          aria-label="로봇 개체 삭제"
          onClick={remove}
        >
          <Trash2 size={15} />
        </button>
      </div>
      <p className="muted" style={{ fontSize: 12, marginBottom: 14 }}>
        {model?.name ?? robot.model_id} · {robot.id}
      </p>
      {!gripperResearchModels.has(robot.model_id) &&
        robot.gripper_kp !== undefined &&
        robot.gripper_kp !== 400 && (
          <div className="notice" role="status">
            <span>
              이 모델은 그리퍼 강성 변경을 지원하지 않습니다. 입력값은 초안에
              보존되어 있으며, 기본값 400으로 되돌리거나 연구용 팔 모델을
              선택해야 저장·적용할 수 있습니다.
            </span>
            <button onClick={() => update({ gripper_kp: 400 })}>
              기본값 400으로 변경
            </button>
          </div>
        )}
      <div className="form-grid">
        <label className="span-2">
          개체 이름
          <input
            value={robot.name}
            onChange={(e) => update({ name: e.target.value })}
          />
        </label>
        <label>
          그룹
          <input
            value={robot.group}
            onChange={(e) => update({ group: e.target.value })}
          />
        </label>
        <label>
          배치 층
          <select
            value={robot.floor_id}
            onChange={(e) => update({ floor_id: e.target.value })}
          >
            {project.environment.floors.map((f) => (
              <option key={f.id} value={f.id}>
                {f.name}
              </option>
            ))}
          </select>
        </label>
        {(["x", "y", "z"] as const).map((axis) => (
          <Field
            key={axis}
            label={`초기 ${axis.toUpperCase()} (m)`}
            value={robot.pose[axis]}
            onChange={(v) => update({ pose: { ...robot.pose, [axis]: v } })}
          />
        ))}
        <Field
          label="방향 (rad)"
          value={robot.pose.yaw}
          onChange={(yaw) => update({ pose: { ...robot.pose, yaw } })}
        />
        <Field
          label="초기 배터리 (%)"
          value={robot.battery}
          min={0}
          max={100}
          step={1}
          onChange={(battery) => update({ battery })}
        />
        <Field
          label="적재 질량 (kg)"
          value={robot.payload_mass}
          min={0}
          onChange={(payload_mass) => update({ payload_mass })}
        />
        {gripperResearchModels.has(robot.model_id) && (
          <>
            <Field
              label="그리퍼 강성 (N/m)"
              value={robot.gripper_kp ?? 400}
              min={100}
              max={2000}
              step="any"
              onChange={(gripper_kp) => update({ gripper_kp })}
            />
            <p className="muted span-2">
              이 연구용 팔 개체의 시뮬레이션 설정입니다. 기본 400, 범위 100~2000
              N/m이며 제조사 사양이 아닙니다. 변경은 실행부 적용 시 새 실행에
              반영됩니다.
            </p>
          </>
        )}
        <Field
          label="배터리 용량 (Wh)"
          value={robot.battery_capacity_wh ?? 400}
          min={0.01}
          onChange={(battery_capacity_wh) => update({ battery_capacity_wh })}
        />
        <Field
          label="경로 예상 소비전력 (W)"
          value={robot.estimated_drive_power_w ?? 120}
          min={20}
          onChange={(estimated_drive_power_w) =>
            update({ estimated_drive_power_w })
          }
        />
        <Field
          label="최대 속도 (m/s)"
          value={robot.max_speed}
          min={0.01}
          onChange={(max_speed) => update({ max_speed })}
        />
        <label>
          초기 장애
          <select
            value={robot.fault}
            onChange={(e) =>
              update({ fault: e.target.value as RobotInstance["fault"] })
            }
          >
            {[
              ["none", "없음"],
              ["motor", "구동기"],
              ["sensor", "센서"],
              ["communication", "통신"],
              ["battery", "배터리"],
            ].map(([id, n]) => (
              <option key={id} value={id}>
                {n}
              </option>
            ))}
          </select>
        </label>
      </div>
      {robot.model_id === "agv" && (
        <AgvRouteEditor key={robot.id} robot={robot} update={update} />
      )}
      <details className="details">
        <summary>센서·관측·통신</summary>
        <div className="form-grid">
          {(
            [
              ["position_noise", "위치 오차 (m)"],
              ["yaw_noise", "방향 오차 (rad)"],
              ["observation_delay", "관측 지연 (s)"],
              ["communication_delay", "통신 지연 (s)"],
              ["dropout", "누락 확률"],
              ["rate_hz", "관측 주기 (Hz)"],
            ] as const
          ).map(([key, n]) => (
            <Field
              key={key}
              label={n}
              value={robot.sensors[key]}
              min={0}
              step={0.01}
              onChange={(v) =>
                update({ sensors: { ...robot.sensors, [key]: v } })
              }
            />
          ))}
          {(["camera", "lidar", "imu", "item_tracking"] as const).map((key) => (
            <label key={key}>
              <input
                type="checkbox"
                checked={robot.sensors[key]}
                onChange={(e) =>
                  update({
                    sensors: { ...robot.sensors, [key]: e.target.checked },
                  })
                }
              />
              {
                {
                  camera: "카메라 (영상 미구현)",
                  lidar: "평면 거리 센서",
                  imu: "관성 센서",
                  item_tracking: "이상적 물품 표식 센서",
                }[key]
              }
            </label>
          ))}
        </div>
      </details>
      <details className="details">
        <summary>장착 장비</summary>
        <p className="muted" style={{ fontSize: 12, margin: "10px 0" }}>
          장비 설정이 모델의 검증되지 않은 기능을 자동으로 부여하지 않습니다.
        </p>
        {(["cargo_tray", "arm", "gripper", "inspection_camera"] as const).map(
          (kind) => (
            <label style={{ margin: "8px 0" }} key={kind}>
              <input
                type="checkbox"
                checked={robot.equipment.some((e) => e.kind === kind)}
                onChange={(e) =>
                  update({
                    equipment: e.target.checked
                      ? [
                          ...robot.equipment,
                          {
                            kind,
                            mass: 1,
                            size: { x: 0.4, y: 0.3, z: 0.15 },
                            capacity: 5,
                          },
                        ]
                      : robot.equipment.filter((v) => v.kind !== kind),
                  })
                }
              />
              {
                {
                  cargo_tray: "적재 트레이",
                  arm: "로봇팔",
                  gripper: "그리퍼",
                  inspection_camera: "점검 카메라",
                }[kind]
              }
            </label>
          ),
        )}
      </details>
      <JsonEditor
        value={robot}
        label="제어기·장비 세부 데이터"
        onApply={(data) => update(data as RobotInstance)}
      />
    </>
  );
}
function EntityEditor({
  project,
  kind,
  floorId,
  edit,
}: {
  project: Project | null;
  kind: "people" | "items";
  floorId: string;
  edit: (fn: (p: Project) => void) => void;
}) {
  const [chosen, setChosen] = useState("");
  const entity = project?.[kind].find((e) => e.id === chosen);
  const add = () => {
    const id = uid(kind);
    edit((p) => {
      const base = {
        id,
        name: `${kind === "people" ? "보행자" : "물품"} ${p[kind].length + 1}`,
        floor_id: floorId,
        pose: pose(2, 2, 0),
      };
      if (kind === "people")
        p.people.push({
          ...base,
          path: [],
          speed: 0.8,
          reaction_time: 0.5,
          avoidance: true,
          sudden_probability: 0,
          mass: 70,
        });
      else
        p.items.push({
          ...base,
          size: { x: 0.25, y: 0.2, z: 0.15 },
          mass: 1,
          friction: 0.5,
          fragility_impulse: 15,
        });
    });
    setChosen(id);
  };
  const update = (v: Partial<Person & Item>) =>
    edit((p) => {
      const e = p[kind].find((x) => x.id === chosen);
      if (e) Object.assign(e, v);
    });
  return (
    <div className="split">
      <section>
        <div className="section-head">
          <h2>{kind === "people" ? "보행자 구성" : "물품 구성"}</h2>
          <button disabled={!project} onClick={add}>
            <Plus size={14} />
            추가
          </button>
        </div>
        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                <th>이름</th>
                <th>층</th>
                <th>초기 위치 (m)</th>
                <th>질량</th>
              </tr>
            </thead>
            <tbody>
              {project?.[kind].map((e) => (
                <tr
                  className={`selectable ${chosen === e.id ? "selected" : ""}`}
                  key={e.id}
                  onClick={() => setChosen(e.id)}
                >
                  <td>
                    <button className="ghost" onClick={() => setChosen(e.id)}>
                      {kind === "people" ? (
                        <Users size={14} />
                      ) : (
                        <Package size={14} />
                      )}{" "}
                      {e.name}
                    </button>
                  </td>
                  <td>
                    {
                      project.environment.floors.find(
                        (f) => f.id === e.floor_id,
                      )?.name
                    }
                  </td>
                  <td>
                    {fmt(e.pose.x)} / {fmt(e.pose.y)}
                  </td>
                  <td>{e.mass} kg</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
      <aside className="form-panel">
        {entity ? (
          <>
            <div className="section-head">
              <h2>개체 속성</h2>
              <button
                aria-label="개체 삭제"
                className="ghost danger"
                onClick={() => {
                  edit((p) => {
                    if (kind === "people")
                      p.people = p.people.filter((x) => x.id !== chosen);
                    else p.items = p.items.filter((x) => x.id !== chosen);
                  });
                  setChosen("");
                }}
              >
                <Trash2 size={15} />
              </button>
            </div>
            <div className="form-grid">
              <label className="span-2">
                이름
                <input
                  value={entity.name}
                  onChange={(e) => update({ name: e.target.value })}
                />
              </label>
              <label>
                층
                <select
                  value={entity.floor_id}
                  onChange={(e) => update({ floor_id: e.target.value })}
                >
                  {project?.environment.floors.map((f) => (
                    <option key={f.id} value={f.id}>
                      {f.name}
                    </option>
                  ))}
                </select>
              </label>
              <Field
                label="질량 (kg)"
                value={entity.mass}
                min={0.01}
                onChange={(mass) => update({ mass })}
              />
              {(["x", "y", "z"] as const).map((axis) => (
                <Field
                  key={axis}
                  label={`${axis.toUpperCase()} (m)`}
                  value={entity.pose[axis]}
                  onChange={(v) =>
                    update({ pose: { ...entity.pose, [axis]: v } })
                  }
                />
              ))}
              {kind === "people" ? (
                <>
                  <Field
                    label="속도 (m/s)"
                    value={(entity as Person).speed}
                    min={0}
                    onChange={(speed) => update({ speed })}
                  />
                  <Field
                    label="반응 시간 (s)"
                    value={(entity as Person).reaction_time}
                    min={0}
                    onChange={(reaction_time) => update({ reaction_time })}
                  />
                  <Field
                    label="돌발 행동 확률"
                    value={(entity as Person).sudden_probability}
                    min={0}
                    max={1}
                    step={0.01}
                    onChange={(sudden_probability) =>
                      update({ sudden_probability })
                    }
                  />
                  <label>
                    <input
                      type="checkbox"
                      checked={(entity as Person).avoidance}
                      onChange={(e) => update({ avoidance: e.target.checked })}
                    />
                    장애물 회피
                  </label>
                </>
              ) : (
                <>
                  {(["x", "y", "z"] as const).map((axis) => (
                    <Field
                      key={`size-${axis}`}
                      label={`크기 ${axis.toUpperCase()} (m)`}
                      value={(entity as Item).size[axis]}
                      min={0.01}
                      onChange={(v) =>
                        update({
                          size: { ...(entity as Item).size, [axis]: v },
                        })
                      }
                    />
                  ))}
                  <Field
                    label="마찰"
                    value={(entity as Item).friction}
                    min={0}
                    onChange={(friction) => update({ friction })}
                  />
                  <Field
                    label="손상 추정 임계 충격량 (N·s)"
                    value={(entity as Item).fragility_impulse}
                    min={0.01}
                    onChange={(fragility_impulse) =>
                      update({ fragility_impulse })
                    }
                  />
                </>
              )}
            </div>
            <JsonEditor
              label={
                kind === "people" ? "경로·반응 세부 데이터" : "물품 세부 데이터"
              }
              value={entity}
              onApply={(data) => update(data as Person & Item)}
            />
          </>
        ) : (
          <Empty
            title={
              kind === "people" ? "보행자를 선택하세요" : "물품을 선택하세요"
            }
          >
            개체별 위치, 물리 조건과 행동을 구성합니다.
          </Empty>
        )}
      </aside>
    </div>
  );
}
export default App;
