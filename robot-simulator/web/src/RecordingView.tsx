import { useEffect, useMemo, useRef, useState } from "react";
import { ArrowDownToLine, FileUp, Pause, Play, RotateCcw } from "lucide-react";
import { api, downloadJSON } from "./api";
import type { Pose, Project, Recording } from "./types";
import {
  eventKindLabel,
  formatSimulationTime,
  userFacingError,
} from "./uiMessages";
import "./RecordingView.css";

export interface RecordingSeek {
  runId: string;
  time: number;
  entityId?: string | null;
}
interface RecordingViewProps {
  adopt: (p: Project) => void;
  run: (label: string, fn: () => Promise<unknown>) => Promise<void>;
  seek?: RecordingSeek;
}
const object = (value: unknown): value is Record<string, unknown> =>
  value !== null && typeof value === "object" && !Array.isArray(value);
const finite = (value: unknown): value is number =>
  typeof value === "number" && Number.isFinite(value);
const pose = (value: unknown) =>
  object(value) && ["x", "y", "z", "yaw"].every((key) => finite(value[key]));

/** Validate the replay's rendered data. No state synthesis or simulator calls. */
export function validateRecording(value: unknown): Recording {
  if (
    !object(value) ||
    typeof value.run_id !== "string" ||
    !value.run_id.trim() ||
    !object(value.project) ||
    !object(value.project.environment)
  )
    throw new Error("실행 ID와 프로젝트가 포함된 실행 기록을 선택하세요.");
  const environment = value.project.environment;
  if (
    !Array.isArray(environment.floors) ||
    !environment.floors.length ||
    !environment.floors.every(
      (floor) =>
        object(floor) &&
        typeof floor.id === "string" &&
        typeof floor.name === "string" &&
        finite(floor.elevation) &&
        finite(floor.width) &&
        floor.width > 0 &&
        finite(floor.depth) &&
        floor.depth > 0,
    )
  )
    throw new Error("기록의 층 정보 또는 공간 치수가 올바르지 않습니다.");
  if (
    !Array.isArray(environment.elements) ||
    !environment.elements.every(
      (element) =>
        object(element) &&
        typeof element.id === "string" &&
        typeof element.floor_id === "string" &&
        typeof element.kind === "string" &&
        pose(element.pose) &&
        object(element.size) &&
        ["x", "y", "z"].every(
          (key) =>
            finite((element.size as Record<string, unknown>)[key]) &&
            Number((element.size as Record<string, unknown>)[key]) > 0,
        ),
    )
  )
    throw new Error("기록의 환경 객체 위치·치수를 확인하세요.");
  if (
    !Array.isArray(value.project.robots) ||
    !value.project.robots.every(
      (robot) =>
        object(robot) &&
        typeof robot.id === "string" &&
        typeof robot.name === "string",
    )
  )
    throw new Error("기록의 로봇 목록을 확인하세요.");
  if (!Array.isArray(value.frames) || !Array.isArray(value.events))
    throw new Error("프레임과 사건 목록이 포함된 실행 기록을 선택하세요.");
  let previous = -Infinity;
  for (const frame of value.frames) {
    if (
      !object(frame) ||
      !finite(frame.time) ||
      frame.time < 0 ||
      frame.time <= previous ||
      !object(frame.robots) ||
      !Object.values(frame.robots).every(pose)
    )
      throw new Error(
        "기록 프레임의 시각 순서 또는 로봇 위치가 올바르지 않습니다.",
      );
    for (const key of ["qpos", "qvel", "ctrl"])
      if (
        !Array.isArray(frame[key]) ||
        !(frame[key] as unknown[]).every(finite)
      )
        throw new Error("기록 프레임의 물리 수치가 없거나 유한하지 않습니다.");
    previous = frame.time;
  }
  if (
    !value.events.every(
      (event) =>
        object(event) &&
        finite(event.seq) &&
        finite(event.time) &&
        typeof event.kind === "string" &&
        typeof event.message === "string",
    )
  )
    throw new Error("기록 사건의 시각 또는 내용이 올바르지 않습니다.");
  return value as unknown as Recording;
}

/** Choose a recorded frame at/before the event, never clamp an out-of-range request. */
export function recordingFrameAtOrBefore(
  recording: Recording,
  seek: RecordingSeek,
) {
  if (!seek.runId || recording.run_id !== seek.runId)
    throw new Error(
      `선택 사건의 실행(${seek.runId || "미지정"})과 읽은 기록(${recording.run_id})이 다릅니다. 현재 실행 기록으로 이 사건을 재생할 수 없습니다.`,
    );
  if (!finite(seek.time) || seek.time < 0)
    throw new Error("선택 사건의 시각이 올바르지 않습니다.");
  const frames = recording.frames;
  if (!frames.length)
    throw new Error(
      "이 실행에는 아직 저장된 프레임이 없습니다. 사건 시각의 물리 상태를 표시할 수 없습니다.",
    );
  let previous = -Infinity;
  for (const frame of frames) {
    if (!finite(frame.time) || frame.time < 0 || frame.time <= previous)
      throw new Error("기록 프레임의 시각 순서가 올바르지 않습니다.");
    previous = frame.time;
  }
  const first = frames[0].time,
    last = frames[frames.length - 1].time;
  if (seek.time < first || seek.time > last)
    throw new Error(
      `선택 사건 ${formatSimulationTime(seek.time, 3)}는 기록 범위 ${formatSimulationTime(first, 3)}–${formatSimulationTime(last, 3)} 밖입니다. 범위 밖의 상태를 만들거나 마지막 프레임으로 대신하지 않습니다.`,
    );
  let left = 0,
    right = frames.length - 1;
  while (left < right) {
    const mid = Math.ceil((left + right) / 2);
    if (frames[mid].time <= seek.time) left = mid;
    else right = mid - 1;
  }
  return {
    index: left,
    time: frames[left].time,
    difference: seek.time - frames[left].time,
    first,
    last,
  };
}

function floorForPose(recording: Recording, position: Pose) {
  return recording.project.environment.floors
    .filter((floor) => floor.elevation <= position.z + 0.15)
    .sort((a, b) => b.elevation - a.elevation)[0]?.id;
}

export default function RecordingView({
  adopt,
  run,
  seek,
}: RecordingViewProps) {
  const requestKey = seek
    ? JSON.stringify([seek.runId, seek.time, seek.entityId ?? null])
    : "manual";
  const [loaded, setLoaded] = useState<{
    key: string;
    value: Recording;
  } | null>(null);
  const [notice, setNotice] = useState<{
    key: string;
    kind: "loading" | "error" | "ready";
    message: string;
    raw?: string;
  } | null>(null);
  const [index, setIndex] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [floorId, setFloorId] = useState("");
  const requestGeneration = useRef(0);
  const upload = useRef<HTMLInputElement>(null);
  const section = useRef<HTMLElement>(null);
  const heading = useRef<HTMLHeadingElement>(null);
  // Invalidate the rendered recording before the effect starts a new request.
  const recording = loaded?.key === requestKey ? loaded.value : null;
  const activeNotice = notice?.key === requestKey ? notice : null;
  const loading =
    activeNotice?.kind === "loading" ||
    Boolean(seek && !recording && !activeNotice);

  async function read(
    source: () => Promise<unknown>,
    target: RecordingSeek | undefined,
    key: string,
  ) {
    const generation = ++requestGeneration.current;
    setPlaying(false);
    setLoaded(null);
    setIndex(0);
    setNotice({
      key,
      kind: "loading",
      message: target
        ? "선택 사건과 같은 실행의 기록을 확인하고 있습니다."
        : "실행 기록을 읽고 있습니다.",
    });
    try {
      const value = validateRecording(await source());
      if (generation !== requestGeneration.current) return;
      const selected = target ? recordingFrameAtOrBefore(value, target) : null;
      const nextIndex = selected?.index ?? 0;
      const robotPose = target?.entityId
        ? value.frames[nextIndex]?.robots[target.entityId]
        : null;
      const staticElement = value.project.environment.elements.find(
        (element) => element.id === target?.entityId,
      );
      setFloorId(
        (robotPose
          ? floorForPose(value, robotPose)
          : staticElement?.floor_id) ?? value.project.environment.floors[0].id,
      );
      setIndex(nextIndex);
      setLoaded({ key, value });
      setNotice({
        key,
        kind: "ready",
        message: selected
          ? "같은 실행의 사건 시각 직전 프레임을 선택했습니다."
          : "기록을 불러왔습니다.",
      });
    } catch (error) {
      if (generation !== requestGeneration.current) return;
      const description = userFacingError(error);
      setNotice({
        key,
        kind: "error",
        message: description.message,
        raw: description.raw,
      });
      setLoaded(null);
      setPlaying(false);
      throw error;
    }
  }

  useEffect(() => {
    if (seek) {
      section.current?.scrollIntoView({ block: "start", behavior: "instant" });
      heading.current?.focus({ preventScroll: true });
      void read(() => api.recording(), seek, requestKey).catch(() => {
        /* Read errors are displayed locally. */
      });
    } else {
      setPlaying(false);
      setLoaded(null);
      setNotice(null);
    }
    return () => {
      requestGeneration.current += 1;
    };
    // All seek fields are in the primitive key; an equal prop object must not refetch.
  }, [requestKey]);

  useEffect(() => {
    if (!playing || !recording) return;
    const current = recording.frames[index],
      next = recording.frames[index + 1];
    if (!current || !next) {
      setPlaying(false);
      return;
    }
    const timer = setTimeout(
      () => setIndex((i) => i + 1),
      Math.max(16, (next.time - current.time) * 1000),
    );
    return () => clearTimeout(timer);
  }, [playing, recording, index]);
  const frame = recording?.frames[index];
  const floor = recording?.project.environment.floors.find(
    (value) => value.id === floorId,
  );
  const width = floor?.width ?? 20,
    depth = floor?.depth ?? 14;
  const targetRobot = seek?.entityId ? frame?.robots[seek.entityId] : undefined;
  const targetFacility = recording?.project.environment.elements.find(
    (value) => value.id === seek?.entityId,
  );
  const selectedFrame = useMemo(
    () =>
      recording && seek ? recordingFrameAtOrBefore(recording, seek) : null,
    [recording, seek?.runId, seek?.time],
  );
  const atSelectedFrame = selectedFrame?.index === index;
  return (
    <section
      ref={section}
      className="section recording-view"
      aria-busy={loading}
    >
      <div className="section-head">
        <div>
          <h2 ref={heading} tabIndex={-1}>
            기록 시점 조사
          </h2>
          <p>
            저장된 프레임을 읽습니다. 보간하거나 물리를 재계산하지 않습니다.
          </p>
        </div>
        <div className="toolbar">
          <button
            disabled={loading}
            onClick={() =>
              void run("현재 실행 기록 읽기", () =>
                read(() => api.recording(), seek, requestKey),
              )
            }
          >
            <RotateCcw size={14} aria-hidden="true" />
            {seek ? "같은 실행 기록 다시 확인" : "현재 기록 읽기"}
          </button>
          <button disabled={loading} onClick={() => upload.current?.click()}>
            <FileUp size={14} aria-hidden="true" />
            기록 가져오기
          </button>
          <button
            disabled={!recording}
            onClick={() =>
              recording &&
              downloadJSON(`recording-${recording.run_id}.json`, recording)
            }
          >
            <ArrowDownToLine size={14} aria-hidden="true" />
            기록 저장
          </button>
          <input
            className="file-input"
            ref={upload}
            type="file"
            accept=".json,application/json"
            aria-label="실행 기록 JSON 가져오기"
            onChange={(event) => {
              const file = event.target.files?.[0];
              if (file)
                void run("기록 가져오기", () =>
                  read(
                    async () => JSON.parse(await file.text()),
                    seek,
                    requestKey,
                  ),
                );
              event.target.value = "";
            }}
          />
        </div>
      </div>
      {seek && (
        <div className="recording-seek-context">
          <strong>선택 사건 {formatSimulationTime(seek.time, 3)}</strong>
          <span>실행 ID {seek.runId}</span>
          {seek.entityId && <span>관련 객체 {seek.entityId}</span>}
        </div>
      )}
      {loading && (
        <p className="recording-notice" role="status">
          {activeNotice?.message ?? "선택 사건의 실행 기록을 읽고 있습니다."}
        </p>
      )}
      {activeNotice?.kind === "error" && (
        <div className="recording-notice is-error" role="alert">
          <strong>기록 시점을 표시하지 못했습니다</strong>
          <p>{activeNotice.message}</p>
          <p>
            다른 실행의 화면은 표시하지 않습니다. 사건과 같은 실행의 저장 파일을
            가져오거나 현재 기록을 다시 확인하세요.
          </p>
          {activeNotice.raw && activeNotice.raw !== activeNotice.message && (
            <details>
              <summary>응답 원문</summary>
              <pre>{activeNotice.raw}</pre>
            </details>
          )}
        </div>
      )}
      {!recording ? (
        !loading &&
        activeNotice?.kind !== "error" && (
          <div className="empty">
            <strong>재생할 실행 기록을 선택하세요</strong>
            <p>
              현재 실행의 기록을 읽거나 저장한 JSON 파일을 불러오세요. 기록이
              없는 시점은 생성하지 않습니다.
            </p>
          </div>
        )
      ) : (
        <>
          <div className="recording-identity">
            <span>
              표시 기록 · 실행 ID <b>{recording.run_id}</b>
            </span>
            <span>
              {recording.frames.length
                ? `${formatSimulationTime(recording.frames[0].time, 3)}–${formatSimulationTime(recording.frames[recording.frames.length - 1].time, 3)}`
                : "저장된 프레임 없음"}
            </span>
          </div>
          {selectedFrame && seek && (
            <div className="recording-seek-result" role="status">
              <span>
                선택 사건 <b>{formatSimulationTime(seek.time, 3)}</b>
              </span>
              <span>
                직전 기록 <b>{formatSimulationTime(selectedFrame.time, 3)}</b>
              </span>
              <span>
                시각 차이{" "}
                <b>{formatSimulationTime(selectedFrame.difference, 3)}</b>
              </span>
              <p>
                {selectedFrame.difference === 0
                  ? "사건과 같은 시각의 기록입니다."
                  : "사건보다 뒤의 프레임은 사용하지 않았습니다. 프레임 사이의 동작은 표시하지 않습니다."}
                {!atSelectedFrame &&
                  " 현재는 재생 또는 프레임 이동으로 다른 기록 시각을 보고 있습니다."}
              </p>
              {!atSelectedFrame && (
                <button
                  onClick={() => {
                    setPlaying(false);
                    setIndex(selectedFrame.index);
                  }}
                >
                  선택 사건의 기록으로 돌아가기
                </button>
              )}
            </div>
          )}
          <div className="controlbar recording-controls">
            <div className="toolbar">
              <button
                disabled={
                  !recording.frames.length ||
                  (!playing && index >= recording.frames.length - 1)
                }
                title={
                  !playing && index >= recording.frames.length - 1
                    ? "마지막 프레임입니다. 슬라이더로 앞 프레임을 선택하세요."
                    : undefined
                }
                onClick={() => setPlaying((value) => !value)}
              >
                {playing ? (
                  <Pause size={14} aria-hidden="true" />
                ) : (
                  <Play size={14} aria-hidden="true" />
                )}
                기록 {playing ? "일시 정지" : "재생"}
              </button>
              <select
                aria-label="기록 재생 층"
                value={floorId}
                onChange={(event) => setFloorId(event.target.value)}
              >
                {recording.project.environment.floors.map((value) => (
                  <option key={value.id} value={value.id}>
                    {value.name}
                  </option>
                ))}
              </select>
              <button onClick={() => adopt(recording.project)}>
                조건을 편집기로 불러오기
              </button>
            </div>
            <span className="muted">
              표시 프레임 {formatSimulationTime(frame?.time, 3)} ·{" "}
              {recording.frames.length ? index + 1 : 0}/
              {recording.frames.length}
            </span>
          </div>
          {frame ? (
            <div className="map-view recording-map">
              <svg
                viewBox={`-1 ${-depth - 1} ${width + 2} ${depth + 2}`}
                role="img"
                aria-label={`${formatSimulationTime(frame.time, 3)}에 기록된 로봇 몸체 위치. 환경은 정적 배치입니다.`}
              >
                <rect
                  x={0}
                  y={-depth}
                  width={width}
                  height={depth}
                  fill="var(--color-panel)"
                />
                {recording.project.environment.elements
                  .filter((element) => element.floor_id === floorId)
                  .map((element) => (
                    <rect
                      key={element.id}
                      x={element.pose.x - element.size.x / 2}
                      y={-element.pose.y - element.size.y / 2}
                      width={element.size.x}
                      height={element.size.y}
                      className={`map-shape ${element.kind}${seek?.entityId === element.id ? " recording-selected" : ""}`}
                      transform={`rotate(${(-element.pose.yaw * 180) / Math.PI} ${element.pose.x} ${-element.pose.y})`}
                    />
                  ))}
                {Object.entries(frame.robots)
                  .filter(
                    ([, position]) =>
                      floorForPose(recording, position) === floorId,
                  )
                  .map(([id, position]) => (
                    <g
                      key={id}
                      transform={`translate(${position.x},${-position.y})`}
                    >
                      <rect
                        x="-.4"
                        y="-.25"
                        width=".8"
                        height=".5"
                        className={`map-robot${seek?.entityId === id ? " recording-selected" : ""}`}
                        transform={`rotate(${(-position.yaw * 180) / Math.PI})`}
                      />
                      <path
                        d="M .14 -.08 L .28 0 L .14 .08"
                        fill="none"
                        stroke="var(--color-ink)"
                        strokeWidth=".035"
                        transform={`rotate(${(-position.yaw * 180) / Math.PI})`}
                      />
                      <text
                        y=".62"
                        textAnchor="middle"
                        fontSize=".24"
                        fill="var(--color-ink)"
                      >
                        {seek?.entityId === id ? "선택 · " : ""}
                        {recording.project.robots.find(
                          (robot) => robot.id === id,
                        )?.name ?? id}
                      </text>
                    </g>
                  ))}
              </svg>
              <span className="map-label">
                기록된 몸체 위치 · 정적 환경 배치 · 보간 없음
              </span>
            </div>
          ) : (
            <div className="empty">
              <strong>저장된 물리 프레임이 없습니다</strong>
              <p>사건 기록만으로 로봇의 위치를 생성하지 않습니다.</p>
            </div>
          )}
          <p className="recording-scope">
            이 도면은 로봇 몸체 위치를 단순 심볼로 표시합니다.
            관절·물품·사람·움직이는 시설은 프레임 수치에서 도면으로 복원하지
            않습니다.
          </p>
          {seek?.entityId && (
            <p className="recording-scope">
              {targetRobot
                ? `관련 로봇의 기록 위치: x ${targetRobot.x.toFixed(3)}m, y ${targetRobot.y.toFixed(3)}m, z ${targetRobot.z.toFixed(3)}m. 다른 층을 선택하면 심볼은 보이지 않을 수 있습니다.`
                : targetFacility
                  ? "관련 시설의 초기 배치를 강조했습니다. 사건 시점의 문·승강기 동작을 복원한 표시는 아닙니다."
                  : "관련 객체의 사건 시점 위치는 이 도면에서 복원할 수 없습니다. 아래 사건·원시 프레임 기록을 확인하세요."}
            </p>
          )}
          <label className="recording-frame-slider">
            기록 프레임
            <input
              type="range"
              min={0}
              max={Math.max(0, recording.frames.length - 1)}
              disabled={!recording.frames.length}
              value={index}
              aria-valuetext={
                frame
                  ? `${index + 1}번째 프레임, ${formatSimulationTime(frame.time, 3)}`
                  : "프레임 없음"
              }
              onChange={(event) => {
                setPlaying(false);
                setIndex(Number(event.target.value));
              }}
            />
          </label>
          {frame && (
            <details className="recording-raw">
              <summary>
                표시 프레임의 실제 기록 수치 · 위치 상태(qpos){" "}
                {frame.qpos.length}개
              </summary>
              <pre>
                {JSON.stringify(
                  { run_id: recording.run_id, ...frame },
                  null,
                  2,
                )}
              </pre>
            </details>
          )}
          <div className="timeline section">
            <h3>표시 프레임까지의 최근 사건</h3>
            {frame ? (
              recording.events
                .filter((event) => event.time <= frame.time)
                .slice(-12)
                .reverse()
                .map((event) => (
                  <div className="event" key={event.seq}>
                    <time>{formatSimulationTime(event.time, 3)}</time>
                    <span className="dot" />
                    <div>
                      <strong>{event.message}</strong>
                      <p>
                        {eventKindLabel(event.kind)} ·{" "}
                        {event.entity_id ?? "실행"}
                      </p>
                    </div>
                  </div>
                ))
            ) : (
              <p className="muted">
                프레임이 없어 시점별 사건 목록을 표시하지 않습니다.
              </p>
            )}
          </div>
        </>
      )}
    </section>
  );
}
