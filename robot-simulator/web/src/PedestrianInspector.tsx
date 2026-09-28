/** @jsxImportSource react */
import type { Person, PedestrianRuntime, Project } from "./types";

const behaviorNames: Record<string, string> = {
  route: "지정 경로",
  free_roam: "자유 배회",
  destinations: "여러 목적지",
  legacy: "기존 경로 이동",
};
const modeNames: Record<string, string> = {
  walking: "걷는 중",
  crossing: "로봇 경로 횡단 중",
  behavior_pause: "잠시 멈춤",
  sudden_pause: "잠시 멈춤",
  sudden_turn: "방향 전환",
  yielding: "진로 양보",
  separating: "서로 거리를 확보하며 이동",
  avoiding: "주변을 피해 이동",
  idle: "대기",
  stationary: "정지",
  perception_hold: "주변 상태 확인 대기",
  static_clearance_hold: "통행 공간 확인 대기",
  boundary_limited: "이동 경계에서 대기",
  blocked: "이동 경로 대기",
  route_blocked: "통행 가능한 경로를 찾는 중",
  no_allowed_destination: "허용 구역에서 목적지를 찾지 못함",
  outside_allowed_space: "허용 구역 밖 · 이동 대기",
  unsupported_vertical_path: "지원되지 않는 층간 이동 · 대기",
  path_outside_bounds: "환경 밖 경로 · 이동 대기",
  at_waypoint: "경유지 도착",
  at_destination: "목적지 도착",
};
const finite = (value: unknown): value is number =>
  typeof value === "number" && Number.isFinite(value);

export function pedestrianDestination(
  person: Person,
  report: PedestrianRuntime,
  project: Project,
): string {
  const goal = report.destination;
  if (!goal)
    return report.destination === null
      ? "선택된 목적지 없음"
      : "목적지 보고 대기";
  if (![goal.x, goal.y, goal.z].every(finite)) return "목적지 확인 불가";
  const place = project.environment.elements.find((element) => {
    if (
      !["room", "corridor", "waiting", "loading", "entrance"].includes(
        element.kind,
      ) ||
      element.floor_id !== person.floor_id
    )
      return false;
    const dx = goal.x - element.pose.x,
      dy = goal.y - element.pose.y;
    const c = Math.cos(element.pose.yaw),
      s = Math.sin(element.pose.yaw);
    return (
      Math.abs(c * dx + s * dy) <= element.size.x / 2 &&
      Math.abs(-s * dx + c * dy) <= element.size.y / 2
    );
  });
  if (place) return `${place.name} 안`;
  const index = person.path.findIndex(
    (point) => Math.hypot(point.x - goal.x, point.y - goal.y) < 0.001,
  );
  return index >= 0
    ? `지정 경유지 ${index + 1}`
    : "이름 없는 이동 지점 · 상세에서 위치 확인";
}

export default function PedestrianInspector({
  person,
  runtime,
  project,
  connected,
  simTime,
}: {
  person: Person;
  runtime?: PedestrianRuntime;
  project: Project;
  connected: boolean;
  simTime?: number;
}) {
  const speed = runtime?.actual_speed_m_s;
  const current =
    connected &&
    runtime &&
    finite(runtime.sampled_at) &&
    finite(simTime) &&
    Math.abs(simTime - runtime.sampled_at) < 0.001;
  const floorNames = runtime?.allowed_floor_ids?.map(
    (id) =>
      project.environment.floors.find((floor) => floor.id === id)?.name ?? id,
  );
  const zoneNames = runtime?.allowed_zone_ids?.map(
    (id) =>
      project.environment.elements.find((element) => element.id === id)?.name ??
      id,
  );
  return (
    <section className="pedestrian-inspector" aria-label="보행자 실행 상태">
      <p className="pedestrian-inspector__state" role="status">
        {!current
          ? "현재 행동 확인 대기 · 새 상태 필요"
          : (modeNames[runtime.mode ?? ""] ?? "현재 행동 상세 확인")}
      </p>
      <dl className="kv">
        <dt>이동 방식</dt>
        <dd>
          {runtime?.behavior
            ? (behaviorNames[runtime.behavior] ?? "행동 상세 확인")
            : "실행 보고 대기"}
        </dd>
        <dt>{current ? "실제 속도" : "마지막 속도"}</dt>
        <dd>
          {finite(speed)
            ? `${speed.toFixed(2)} m/s${!current ? " · 이전 상태" : ""}`
            : "확인 불가"}
        </dd>
        <dt>{current ? "현재 목적지" : "마지막 목적지"}</dt>
        <dd>
          {runtime
            ? pedestrianDestination(person, runtime, project)
            : "실행 보고 대기"}
        </dd>
        <dt>이동 허용 층</dt>
        <dd>
          {floorNames?.length ? floorNames.join(" · ") : "실행 보고 대기"}
        </dd>
        <dt>이동 허용 구역</dt>
        <dd>
          {zoneNames
            ? zoneNames.length
              ? zoneNames.join(" · ")
              : "허용 층의 통행 가능한 공간"
            : "실행 보고 대기"}
        </dd>
      </dl>
      <details className="details">
        <summary>이 사람의 설정과 현재 위치</summary>
        <dl className="kv">
          <dt>개별 이동 속도 설정</dt>
          <dd>
            {person.behavior
              ? `${person.behavior.speed_min_m_s}–${person.behavior.speed_max_m_s} m/s`
              : `${person.speed} m/s`}
          </dd>
          <dt>개별 이동 방식 설정</dt>
          <dd>{behaviorNames[person.behavior?.mode ?? "legacy"]}</dd>
          <dt>상태 시각</dt>
          <dd>
            {finite(runtime?.sampled_at)
              ? `${runtime.sampled_at.toFixed(3)} s`
              : "확인 불가"}
          </dd>
          <dt>실제 몸통 중심 (m)</dt>
          <dd>
            {runtime?.actual_position?.every(finite)
              ? runtime.actual_position.map((n) => n.toFixed(3)).join(" / ")
              : "확인 불가"}
          </dd>
          <dt>목적지 · 층 기준 (m)</dt>
          <dd>
            {runtime?.destination &&
            [
              runtime.destination.x,
              runtime.destination.y,
              runtime.destination.z,
            ].every(finite)
              ? [
                  runtime.destination.x,
                  runtime.destination.y,
                  runtime.destination.z,
                ]
                  .map((n) => n.toFixed(3))
                  .join(" / ")
              : "확인 불가"}
          </dd>
          <dt>이동 방향 (rad)</dt>
          <dd>
            {finite(runtime?.actual_heading_rad)
              ? runtime.actual_heading_rad.toFixed(3)
              : "보고 없음"}
          </dd>
          <dt>실행 상태 원문</dt>
          <dd>{runtime?.mode ?? "보고 없음"}</dd>
          <dt>이유 원문</dt>
          <dd>{runtime?.reason ?? "보고 없음"}</dd>
        </dl>
        <p className="muted">
          이 항목은 선택한 사람의 설정입니다. 전체 인원과 초기 배치는 계획
          구성에서 확인하세요. 방향은 실제 이동 방향이며 정지 중에는 마지막
          방향을 유지합니다.
        </p>
      </details>
      <details className="details">
        <summary>3D 외형과 물리 진단</summary>
        <p className="muted">
          머리·몸통·팔다리·손발·의복은 앱에 포함된 관절 시각 모델입니다. 현재
          물리는 몸통 단일 충돌체를 사용하며 인체 관절별 접촉은 검증하지
          않았습니다. 충돌체는 3D의 ‘물리 진단’에서 확인하세요.
        </p>
      </details>
    </section>
  );
}
