import { useEffect, useId, useMemo, useRef, useState } from "react";
import type { KeyboardEvent, PointerEvent } from "react";
import {
  AlertTriangle,
  CheckCircle2,
  ChevronDown,
  ChevronUp,
  Clock3,
  ExternalLink,
  Info,
  Search,
  X,
} from "lucide-react";
import type { Project, RunState, RuntimeEvent, TaskState } from "./types";
import {
  describeRuntimeEvent,
  eventIsCommand,
  eventIsFailure,
  formatSimulationTime,
  taskStatusLabel,
} from "./uiMessages";
import type { MessageTone } from "./uiMessages";
import "./RuntimeTimeline.css";

export interface RuntimeTimelineProps {
  state: RunState | null;
  project: Project | null;
  connected: boolean;
  onSelectEntity: (id: string) => void;
  onOpenEvents?: () => void;
  onSeekEvent?: (event: RuntimeEvent) => void;
  defaultCollapsed?: boolean;
  defaultHeight?: number;
}
type Filter = "all" | "failure" | "command";
type View = "events" | "tasks";
type Selection = { runId: string; view: View; id: string };
const MIN_HEIGHT = 200;
const MAX_HEIGHT = 540;
const PAGE_SIZE = 40;
const terminal = new Set(["completed", "failed", "cancelled"]);
function heightLimit() {
  return Math.max(
    MIN_HEIGHT,
    Math.min(MAX_HEIGHT, Math.floor(window.innerHeight * 0.6)),
  );
}
function severityLabel(tone: MessageTone) {
  return {
    neutral: "기록",
    info: "안내",
    warning: "주의",
    danger: "실패",
    success: "확인",
  }[tone];
}
function Signal({ tone }: { tone: MessageTone }) {
  const Icon =
    tone === "danger" || tone === "warning"
      ? AlertTriangle
      : tone === "success"
        ? CheckCircle2
        : Info;
  return (
    <span className={`rt-signal rt-tone-${tone}`}>
      <Icon size={13} aria-hidden="true" />
      {severityLabel(tone)}
    </span>
  );
}
function taskTone(task: TaskState): MessageTone {
  if (task.status === "failed" || task.recovery?.status === "failed")
    return "danger";
  if (task.status === "cancelled" || task.status === "waiting")
    return "warning";
  return task.status === "completed" ? "success" : "neutral";
}

export default function RuntimeTimeline({
  state,
  project,
  connected,
  onSelectEntity,
  onOpenEvents,
  onSeekEvent,
  defaultCollapsed = false,
  defaultHeight = 220,
}: RuntimeTimelineProps) {
  const [collapsed, setCollapsed] = useState(defaultCollapsed);
  const [height, setHeight] = useState(() =>
    Number.isFinite(defaultHeight)
      ? Math.max(MIN_HEIGHT, Math.min(MAX_HEIGHT, defaultHeight))
      : 220,
  );
  const [view, setView] = useState<View>("events");
  const [filter, setFilter] = useState<Filter>("all");
  const [query, setQuery] = useState("");
  const [selection, setSelection] = useState<Selection | null>(null);
  const [visibleCount, setVisibleCount] = useState(PAGE_SIZE);
  const drag = useRef<{ y: number; height: number } | null>(null);
  const contentId = useId();
  const searchId = useId();
  const runId = state?.run_id ?? null;
  useEffect(() => {
    setSelection(null);
    setQuery("");
    setFilter("all");
    setVisibleCount(PAGE_SIZE);
  }, [runId]);
  useEffect(() => {
    setVisibleCount(PAGE_SIZE);
    setSelection(null);
  }, [view, filter, query]);
  useEffect(() => {
    const clamp = () =>
      setHeight((value) =>
        Math.max(MIN_HEIGHT, Math.min(value, heightLimit())),
      );
    clamp();
    window.addEventListener("resize", clamp);
    return () => window.removeEventListener("resize", clamp);
  }, []);

  const entities = useMemo(() => {
    const names = new Map<string, string>();
    for (const item of [
      ...(project?.environment.elements ?? []),
      ...(project?.robots ?? []),
      ...(project?.items ?? []),
      ...(project?.people ?? []),
    ])
      names.set(item.id, item.name || item.id);
    for (const robot of state?.robots ?? [])
      names.set(robot.id, robot.name || robot.id);
    for (const facility of state?.facilities ?? []) {
      const id =
        typeof facility.id === "string"
          ? facility.id
          : typeof facility.entity_id === "string"
            ? facility.entity_id
            : null;
      if (id && !names.has(id))
        names.set(id, typeof facility.name === "string" ? facility.name : id);
    }
    return names;
  }, [project, state?.robots, state?.facilities]);
  function relatedTask(task: TaskState): string[] {
    const spec = project?.tasks.find(
      (row) => row.id === task.id || task.id.startsWith(`${row.id}~`),
    );
    return [
      ...new Set(
        [task.robot_id, ...(task.participant_ids ?? []), spec?.item_id].filter(
          (id): id is string => typeof id === "string" && entities.has(id),
        ),
      ),
    ];
  }
  function relatedEvent(event: RuntimeEvent): string[] {
    const detail = event.details ?? {};
    const ids: unknown[] = [
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
      detail.other,
    ];
    if (detail.participants && typeof detail.participants === "object")
      ids.push(...Object.values(detail.participants));
    const task = state?.tasks.find(
      (row) => row.id === detail.task_id || row.id === event.entity_id,
    );
    if (task) ids.push(...relatedTask(task));
    return [
      ...new Set(
        ids.filter(
          (id): id is string => typeof id === "string" && entities.has(id),
        ),
      ),
    ];
  }
  const needle = query.trim().toLocaleLowerCase();
  const events = useMemo(
    () =>
      (state?.events ?? [])
        .filter((event) => {
          if (filter === "failure" && !eventIsFailure(event)) return false;
          if (filter === "command" && !eventIsCommand(event)) return false;
          if (!needle) return true;
          const description = describeRuntimeEvent(event);
          return [
            description.title,
            description.summary,
            event.kind,
            event.entity_id,
            entities.get(event.entity_id ?? ""),
            JSON.stringify(event.details),
          ]
            .join(" ")
            .toLocaleLowerCase()
            .includes(needle);
        })
        .slice()
        .sort((a, b) => b.time - a.time || b.seq - a.seq),
    [state?.events, filter, needle, entities],
  );
  const tasks = useMemo(
    () =>
      (state?.tasks ?? []).filter((task) => {
        if (
          filter === "failure" &&
          task.status !== "failed" &&
          task.recovery?.status !== "failed"
        )
          return false;
        if (!needle) return true;
        return [
          task.id,
          task.name,
          taskStatusLabel(task.status),
          task.reason,
          task.robot_id,
          entities.get(task.robot_id ?? ""),
          ...(task.participant_ids ?? []),
        ]
          .join(" ")
          .toLocaleLowerCase()
          .includes(needle);
      }),
    [state?.tasks, filter, needle, entities],
  );
  const rows = view === "events" ? events : tasks;
  // The run binding prevents one render of an old selection before the effect
  // runs, including identical event sequence numbers after a reset.
  const currentSelection =
    selection?.runId === runId && selection?.view === view ? selection : null;
  const selectedEvent =
    currentSelection?.view === "events"
      ? state?.events.find((event) => String(event.seq) === currentSelection.id)
      : undefined;
  const selectedTask =
    currentSelection?.view === "tasks"
      ? state?.tasks.find((task) => task.id === currentSelection.id)
      : undefined;
  const selectedDescription = selectedEvent
    ? describeRuntimeEvent(selectedEvent)
    : null;
  const selectedEntities = selectedEvent
    ? relatedEvent(selectedEvent)
    : selectedTask
      ? relatedTask(selectedTask)
      : [];
  const selectedTaskStart = selectedTask?.started_at;
  const taskEnd =
    selectedTask && terminal.has(selectedTask.status)
      ? selectedTask.completed_at
      : selectedTask?.status === "running"
        ? state?.sim_time
        : null;
  const elapsed =
    typeof selectedTaskStart === "number" &&
    typeof taskEnd === "number" &&
    taskEnd >= selectedTaskStart
      ? taskEnd - selectedTaskStart
      : null;
  function chooseEvent(event: RuntimeEvent) {
    if (!runId) return;
    setSelection({ runId, view: "events", id: String(event.seq) });
    const entity = relatedEvent(event)[0];
    if (entity) onSelectEntity(entity);
  }
  function chooseTask(task: TaskState) {
    if (!runId) return;
    setSelection({ runId, view: "tasks", id: task.id });
    const entity = relatedTask(task)[0];
    if (entity) onSelectEntity(entity);
  }
  function resizeKey(event: KeyboardEvent<HTMLDivElement>) {
    const change = event.shiftKey ? 60 : 20;
    if (!["ArrowUp", "ArrowDown", "Home", "End"].includes(event.key)) return;
    event.preventDefault();
    setHeight((current) =>
      event.key === "Home"
        ? MIN_HEIGHT
        : event.key === "End"
          ? heightLimit()
          : Math.max(
              MIN_HEIGHT,
              Math.min(
                heightLimit(),
                current + (event.key === "ArrowUp" ? change : -change),
              ),
            ),
    );
  }
  function resizeMove(event: PointerEvent<HTMLDivElement>) {
    if (!drag.current) return;
    setHeight(
      Math.max(
        MIN_HEIGHT,
        Math.min(
          heightLimit(),
          drag.current.height + drag.current.y - event.clientY,
        ),
      ),
    );
  }
  function endResize(event: PointerEvent<HTMLDivElement>) {
    drag.current = null;
    if (event.currentTarget.hasPointerCapture(event.pointerId))
      event.currentTarget.releasePointerCapture(event.pointerId);
  }
  const showDetail = Boolean(selectedEvent || selectedTask);
  const failureCount = (state?.events ?? []).filter(eventIsFailure).length;
  return (
    <section
      className={`runtime-timeline${collapsed ? " is-collapsed" : ""}`}
      aria-label="사건·작업 타임라인"
      style={collapsed ? undefined : { height }}
    >
      {!collapsed && (
        <div
          className="rt-resizer"
          role="separator"
          aria-label="타임라인 높이 조절. 위아래 화살표로 조절"
          title="끌어서 높이 조절 · ↑/↓ 20픽셀 · Shift 60픽셀 · Home 최소 · End 최대"
          aria-orientation="horizontal"
          aria-controls={contentId}
          aria-valuemin={MIN_HEIGHT}
          aria-valuemax={
            typeof window === "undefined" ? MAX_HEIGHT : heightLimit()
          }
          aria-valuenow={height}
          aria-valuetext={`${height}픽셀`}
          tabIndex={0}
          onKeyDown={resizeKey}
          onPointerDown={(event) => {
            if (event.button !== 0) return;
            drag.current = { y: event.clientY, height };
            event.currentTarget.setPointerCapture(event.pointerId);
          }}
          onPointerMove={resizeMove}
          onPointerUp={endResize}
          onPointerCancel={endResize}
          onLostPointerCapture={() => {
            drag.current = null;
          }}
        >
          <span />
        </div>
      )}
      <header className="rt-header">
        <button
          className="rt-toggle"
          aria-expanded={!collapsed}
          aria-controls={contentId}
          onClick={() => setCollapsed((value) => !value)}
        >
          {collapsed ? (
            <ChevronUp size={15} aria-hidden="true" />
          ) : (
            <ChevronDown size={15} aria-hidden="true" />
          )}
          <strong>사건·작업</strong>
          <span className="rt-count">
            사건 {state?.events.length ?? 0} · 작업 {state?.tasks.length ?? 0}
          </span>
        </button>
        {failureCount > 0 && (
          <span className="rt-attention">
            <AlertTriangle size={12} aria-hidden="true" />
            실패·주의 {failureCount}
          </span>
        )}
        <span className="rt-clock">
          <Clock3 size={13} aria-hidden="true" />
          {state
            ? `${connected ? "실행 시각" : "마지막 수신"} ${formatSimulationTime(state.sim_time)}`
            : connected
              ? "실행 상태 대기"
              : "연결 대기"}
        </span>
        {runId && (
          <span className="rt-run" title={`실행 ID ${runId}`}>
            실행 ID <b>{runId}</b>
          </span>
        )}
      </header>
      {!collapsed && (
        <div className="rt-expanded" id={contentId}>
          <div className="rt-toolbar">
            <div
              className="rt-view-switch"
              role="group"
              aria-label="타임라인 종류"
            >
              {(
                [
                  ["events", "사건"],
                  ["tasks", "작업"],
                ] as const
              ).map(([id, label]) => (
                <button
                  key={id}
                  aria-pressed={view === id}
                  onClick={() => {
                    setView(id);
                    if (id === "tasks" && filter === "command")
                      setFilter("all");
                  }}
                >
                  {label}
                </button>
              ))}
            </div>
            <label className="rt-search" htmlFor={searchId}>
              <Search size={14} aria-hidden="true" />
              <input
                id={searchId}
                type="search"
                value={query}
                placeholder="사건·개체·이유 검색"
                aria-label="타임라인 검색"
                onChange={(event) => setQuery(event.target.value)}
              />
            </label>
            <div className="rt-filters" role="group" aria-label="타임라인 필터">
              {(
                [
                  ["all", "전체"],
                  ["failure", "실패"],
                  ["command", "명령"],
                ] as const
              )
                .filter(([id]) => view === "events" || id !== "command")
                .map(([id, label]) => (
                  <button
                    key={id}
                    aria-pressed={filter === id}
                    title={
                      id === "failure" && view === "events"
                        ? "실패·충돌·통신 장애 및 주의 사건"
                        : undefined
                    }
                    onClick={() => setFilter(id)}
                  >
                    {label}
                  </button>
                ))}
            </div>
            {onOpenEvents && (
              <button
                className="rt-open"
                onClick={onOpenEvents}
                title="사건 기록과 재생 화면 열기"
              >
                <ExternalLink size={13} aria-hidden="true" />
                기록 화면
              </button>
            )}
          </div>
          {!connected && (
            <p className="rt-connection" role="status">
              연결이 끊겨 갱신이 멈췄습니다.
              {state
                ? " 아래는 표시된 실행 시각에 마지막으로 받은 기록입니다."
                : " 실행부에 연결되면 기록이 표시됩니다."}
            </p>
          )}
          <div className={`rt-content${showDetail ? " has-detail" : ""}`}>
            <div className="rt-records">
              <div className="rt-list-caption">
                <span>
                  {view === "events"
                    ? "최신 사건 순 · 시뮬레이션 시간"
                    : "현재 실행의 작업 상태"}
                </span>
                <span>
                  {rows.length}건
                  {view === "events" && state?.events.length
                    ? ` · 수신한 최근 ${state.events.length}건에서 검색`
                    : ""}
                </span>
              </div>
              {!state ? (
                <div className="rt-empty">
                  <strong>
                    {connected
                      ? "실행 상태를 기다리고 있습니다"
                      : "아직 받은 실행 기록이 없습니다"}
                  </strong>
                  <p>연결 후 실행부가 보낸 사건과 작업 상태를 표시합니다.</p>
                </div>
              ) : !rows.length ? (
                <div className="rt-empty">
                  <strong>
                    {needle || filter !== "all"
                      ? "조건에 맞는 기록이 없습니다"
                      : view === "events"
                        ? "아직 기록된 사건이 없습니다"
                        : "현재 실행에 작업이 없습니다"}
                  </strong>
                  <p>
                    {needle || filter !== "all"
                      ? "검색어나 필터를 바꾸어 다시 확인하세요."
                      : view === "tasks"
                        ? "시나리오에서 작업을 구성하고 실행부에 적용하면 여기에 표시됩니다."
                        : "실행부에서 명령과 상태 변화가 기록되면 표시됩니다."}
                  </p>
                  {(needle || filter !== "all") && (
                    <button
                      onClick={() => {
                        setQuery("");
                        setFilter("all");
                      }}
                    >
                      검색·필터 초기화
                    </button>
                  )}
                </div>
              ) : (
                <>
                  <ul
                    className="rt-list"
                    aria-label={view === "events" ? "사건 목록" : "작업 목록"}
                  >
                    {view === "events"
                      ? events.slice(0, visibleCount).map((event) => {
                          const description = describeRuntimeEvent(event);
                          return (
                            <li key={event.seq}>
                              <button
                                className={`rt-row${selectedEvent?.seq === event.seq ? " is-selected" : ""}`}
                                aria-pressed={selectedEvent?.seq === event.seq}
                                onClick={() => chooseEvent(event)}
                              >
                                <time className="rt-time">
                                  {formatSimulationTime(event.time)}
                                </time>
                                <Signal tone={description.tone} />
                                <span className="rt-row-copy">
                                  <strong>{description.title}</strong>
                                  <span>{description.summary}</span>
                                </span>
                                <span
                                  className="rt-entity"
                                  title={event.entity_id ?? "실행 전체"}
                                >
                                  {event.entity_id
                                    ? (entities.get(event.entity_id) ??
                                      state.tasks.find(
                                        (task) => task.id === event.entity_id,
                                      )?.name ??
                                      event.entity_id)
                                    : "실행 전체"}
                                </span>
                              </button>
                            </li>
                          );
                        })
                      : tasks.slice(0, visibleCount).map((task) => (
                          <li key={task.id}>
                            <button
                              className={`rt-row rt-task-row${selectedTask?.id === task.id ? " is-selected" : ""}`}
                              aria-pressed={selectedTask?.id === task.id}
                              onClick={() => chooseTask(task)}
                            >
                              <span className="rt-time">
                                {task.started_at === null
                                  ? "미시작"
                                  : formatSimulationTime(task.started_at)}
                              </span>
                              <span
                                className={`rt-task-status rt-tone-${taskTone(task)}`}
                              >
                                {taskStatusLabel(task.status)}
                              </span>
                              <span className="rt-row-copy">
                                <strong>{task.name || task.id}</strong>
                                <span>
                                  {task.reason ||
                                    "실행부의 사유를 기다리고 있습니다."}
                                </span>
                              </span>
                              <span className="rt-entity">
                                {task.robot_id
                                  ? (entities.get(task.robot_id) ??
                                    task.robot_id)
                                  : "배정 대기"}
                              </span>
                            </button>
                          </li>
                        ))}
                  </ul>
                  {rows.length > visibleCount && (
                    <button
                      className="rt-more"
                      onClick={() =>
                        setVisibleCount((value) => value + PAGE_SIZE)
                      }
                    >
                      다음 {Math.min(PAGE_SIZE, rows.length - visibleCount)}건
                      표시 · {visibleCount}/{rows.length}
                    </button>
                  )}
                </>
              )}
            </div>
            {showDetail && (
              <aside
                className="rt-detail"
                aria-label="선택한 기록 상세"
                key={`${runId}:${currentSelection?.view}:${currentSelection?.id}`}
              >
                <div className="rt-detail-heading">
                  <h3>
                    {selectedDescription?.title ??
                      selectedTask?.name ??
                      "작업 상세"}
                  </h3>
                  <button
                    className="rt-close"
                    aria-label="기록 상세 닫기"
                    onClick={() => setSelection(null)}
                  >
                    <X size={14} aria-hidden="true" />
                  </button>
                </div>
                {selectedEvent && selectedDescription ? (
                  <>
                    <p className="rt-detail-time">
                      시뮬레이션 {formatSimulationTime(selectedEvent.time, 3)} ·
                      사건 #{selectedEvent.seq}
                    </p>
                    <p>{selectedDescription.summary}</p>
                    {onSeekEvent && (
                      <button onClick={() => onSeekEvent(selectedEvent)}>
                        <Clock3 size={13} aria-hidden="true" />
                        기록 시점 보기
                      </button>
                    )}
                    {selectedDescription.summary !== selectedEvent.message &&
                      selectedEvent.message && (
                        <p className="rt-reported">
                          <strong>실행부 기록</strong>
                          {selectedEvent.message}
                        </p>
                      )}
                    {selectedDescription.nextAction && (
                      <p className="rt-next">
                        <strong>다음 확인</strong>
                        {selectedDescription.nextAction}
                      </p>
                    )}
                  </>
                ) : (
                  selectedTask && (
                    <>
                      <p
                        className={`rt-task-status rt-tone-${taskTone(selectedTask)}`}
                      >
                        {taskStatusLabel(selectedTask.status)}
                      </p>
                      <p>
                        {selectedTask.reason ||
                          "실행부의 사유를 기다리고 있습니다."}
                      </p>
                      <dl className="rt-task-facts">
                        <div>
                          <dt>시작</dt>
                          <dd>
                            {selectedTask.started_at === null
                              ? "미시작"
                              : formatSimulationTime(
                                  selectedTask.started_at,
                                  3,
                                )}
                          </dd>
                        </div>
                        <div>
                          <dt>종료</dt>
                          <dd>
                            {selectedTask.completed_at === null
                              ? "종료 기록 없음"
                              : formatSimulationTime(
                                  selectedTask.completed_at,
                                  3,
                                )}
                          </dd>
                        </div>
                        <div>
                          <dt>실행 경과</dt>
                          <dd>
                            {elapsed === null
                              ? "계산할 시각 없음"
                              : formatSimulationTime(elapsed)}
                          </dd>
                        </div>
                      </dl>
                      {selectedTask.cooperation && (
                        <p className="rt-next">
                          <strong>협업 상태</strong>
                          {selectedTask.cooperation.committed
                            ? "인계 소유 이전 확인"
                            : "인계 소유 이전 미확인"}{" "}
                          ·{" "}
                          {selectedTask.cooperation.resources_retained === true
                            ? "복구·작업 예약 유지"
                            : selectedTask.cooperation.resources_retained ===
                                false
                              ? "예약 반납"
                              : "예약 상태 미수신"}
                        </p>
                      )}
                      {selectedTask.status === "failed" && (
                        <p className="rt-next">
                          <strong>다음 확인</strong>담당 로봇의 관측·물품·예약
                          상태와 실패 사건을 확인한 뒤 복구 또는 재시도를
                          결정하세요.
                        </p>
                      )}
                      {selectedTask.recovery && (
                        <p className="rt-reported">
                          <strong>
                            물품 복구 ·{" "}
                            {taskStatusLabel(selectedTask.recovery.status)}
                          </strong>
                          {selectedTask.recovery.reason}
                        </p>
                      )}
                    </>
                  )
                )}
                {selectedEntities.length > 0 ? (
                  <div className="rt-related">
                    <span>관련 객체</span>
                    {selectedEntities.map((id) => (
                      <button
                        key={id}
                        onClick={() => onSelectEntity(id)}
                        title={id}
                      >
                        {entities.get(id) ?? id}
                      </button>
                    ))}
                  </div>
                ) : (
                  <p className="rt-muted">
                    이 기록에 연결된 선택 가능한 객체가 없습니다.
                  </p>
                )}
                {selectedEvent && (
                  <p className="rt-muted">
                    사건의 시각과 관련 객체를 표시합니다. 현재 공간 화면을 과거
                    물리 상태로 되돌리지는 않습니다.
                  </p>
                )}
                <details className="rt-raw">
                  <summary>원시 기록과 기술 수치</summary>
                  <pre>
                    {JSON.stringify(
                      {
                        run_id: runId,
                        ...(selectedEvent
                          ? { event: selectedEvent }
                          : { task: selectedTask }),
                      },
                      null,
                      2,
                    )}
                  </pre>
                </details>
              </aside>
            )}
          </div>
        </div>
      )}
    </section>
  );
}
