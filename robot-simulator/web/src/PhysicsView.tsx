import { useEffect, useMemo, useRef, useState } from "react";
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import {
  ArrowDown,
  History,
  ArrowLeft,
  ArrowRight,
  ArrowUp,
  Box,
  Crosshair,
  Maximize2,
  Minus,
  Move,
  Plus,
  RotateCcw,
  RotateCw,
  ScanEye,
  Tags,
  X,
} from "lucide-react";
import type { Geom, MeshData, Project, RunState } from "./types";
import {
  floorAtGeometryBase,
  floorAtHeight,
  perspectiveBoxDistance,
} from "./spatial";
import {
  advanceClick,
  copyView,
  floorPairView,
  isClick,
  robotFocusView,
  sampleTravel,
  segmentHitsBox,
  type CameraSnapshot,
  type CameraTravel,
  type ClickGesture,
} from "./cameraNavigation";
import { robotStatusLabel } from "./uiMessages";
import { FloorStackPicker } from "./FloorStackPicker";
import {
  createHumanVisual,
  sampleHumanMotion,
  type HumanVisual,
  type HumanMotion,
} from "./HumanVisual";
import "./PhysicsView.css";
const geomTypes = [
  "plane",
  "hfield",
  "sphere",
  "capsule",
  "ellipsoid",
  "cylinder",
  "box",
  "mesh",
];
const modelNames: Record<string, string> = {
  person: "보행자",
  spot: "Spot · 사족보행",
  delivery: "배송 로봇",
  amr: "AMR",
  agv: "AGV",
  logistics: "물류 운반 로봇",
  arm: "고정형 로봇팔",
  mobile_manipulator: "이동형 조작 로봇",
};
const modelTags: Record<string, string> = {
  person: "사람",
  spot: "사족보행",
  delivery: "배송",
  amr: "AMR",
  agv: "AGV",
  logistics: "물류 운반",
  arm: "고정 로봇팔",
  mobile_manipulator: "이동 로봇팔",
};
function activeRide(
  state: RunState | null,
  project: Project | null,
  robotId: string,
) {
  if (!robotId) return null;
  const floors = project?.environment.floors ?? [];
  const elevators = new Set(
    (project?.environment.elements ?? [])
      .filter((element) => element.kind === "elevator")
      .map((element) => element.id),
  );
  for (const facility of state?.facilities ?? []) {
    if (
      !elevators.has(String(facility.id)) ||
      !Array.isArray(facility.requests)
    )
      continue;
    const request = facility.requests.find((value: unknown) => {
      if (!value || typeof value !== "object") return false;
      const row = value as Record<string, unknown>;
      return (
        row.robot_id === robotId &&
        !row.exited &&
        row.status !== "cancelled" &&
        row.status !== "completed"
      );
    }) as Record<string, unknown> | undefined;
    if (!request) continue;
    const source = floors.find((item) => item.id === request.source_floor);
    const dest = floors.find((item) => item.id === request.dest_floor);
    const phase = String(facility.phase ?? "idle");
    if (
      source &&
      dest &&
      [
        "opening_board",
        "boarding",
        "closing_depart",
        "moving",
        "opening_exit",
        "alighting",
      ].includes(phase)
    )
      return { source, dest, phase, facilityId: String(facility.id) };
  }
  return null;
}
const worldUp = new THREE.Vector3(0, 0, 1);
function geometryFor(
  g: Geom,
  meshes: Map<number, MeshData>,
): THREE.BufferGeometry | null {
  const type =
    typeof g.type === "number"
      ? geomTypes[g.type]
      : g.type.replace("mjGEOM_", "").toLowerCase();
  const [a = 0.1, b = 0.1, c = 0.1] = g.size;
  if (type === "mesh") {
    const source = g.mesh_id === undefined ? undefined : meshes.get(g.mesh_id);
    if (!source) return null; // Do not replace an unavailable model with an invented box.
    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute(
      "position",
      new THREE.Float32BufferAttribute(source.vertices, 3),
    );
    geometry.setIndex(source.faces);
    geometry.computeVertexNormals();
    return geometry;
  }
  if (type === "sphere") return new THREE.SphereGeometry(a, 18, 12);
  if (type === "capsule")
    return new THREE.CapsuleGeometry(a, b * 2, 6, 12).rotateX(Math.PI / 2);
  if (type === "cylinder")
    return new THREE.CylinderGeometry(a, a, b * 2, 20).rotateX(Math.PI / 2);
  if (type === "ellipsoid")
    return new THREE.SphereGeometry(1, 18, 12).scale(a, b, c);
  if (type === "plane")
    return new THREE.PlaneGeometry(a > 0 ? a * 2 : 60, b > 0 ? b * 2 : 60);
  if (type === "box") return new THREE.BoxGeometry(a * 2, b * 2, c * 2);
  return null;
}
interface Entity {
  name: string;
  floor: string;
  kind: string;
  dynamic: boolean;
  floorAnchor?: { name: string; centerOffset: number };
}
interface Runtime {
  renderer: THREE.WebGLRenderer;
  scene: THREE.Scene;
  camera: THREE.PerspectiveCamera;
  controls: OrbitControls;
  objects: Map<number, THREE.Mesh>;
  humans: Map<string, HumanVisual>;
  humanMotion: Map<string, HumanMotion>;
  selectionRing: THREE.Mesh;
  byEntity: Map<string, THREE.Mesh[]>;
  selection: THREE.Box3Helper;
  direction: THREE.ArrowHelper;
  selectedBounds: THREE.Box3;
  allBounds: THREE.Box3;
  invalidate: () => void;
  runId: string | null;
  meshSource: MeshData[] | null;
  frame: number;
  lost: boolean;
  floorId: string;
  entityFloors: Map<string, string | undefined>;
  travel: CameraTravel | null;
  focusId: string | null;
}
type View = "all" | "top" | "front" | "selected";
export function PhysicsView({
  state,
  meshes,
  selected,
  onSelect,
  project,
  floorId,
  connectionState,
  focusRequest,
  onFloorChange,
}: {
  state: RunState | null;
  meshes: MeshData[];
  selected: string;
  onSelect: (id: string) => void;
  project: Project | null;
  floorId: string;
  connectionState?: "connected" | "connecting" | "stale" | "disconnected";
  focusRequest?: { id: string; sequence: number } | null;
  onFloorChange?: (floorId: string) => void;
}) {
  const container = useRef<HTMLDivElement>(null),
    runtime = useRef<Runtime | null>(null);
  const selectRef = useRef(onSelect);
  selectRef.current = onSelect;
  const labelNodes = useRef(new Map<string, HTMLButtonElement>());
  const labelLines = useRef(new Map<string, SVGLineElement>());
  const [hiddenLabelCount, setHiddenLabelCount] = useState(0);
  const [renderedEntities, setRenderedEntities] = useState<string[]>([]);
  const [generation, setGeneration] = useState(0),
    [error, setError] = useState("");
  const [mode, setMode] = useState<"rotate" | "pan">("rotate"),
    [tracking, setTracking] = useState(false);
  const [showLabels, setShowLabels] = useState(true);
  const [showDiagnostics, setShowDiagnostics] = useState(false);
  const [humanDisplayFailure, setHumanDisplayFailure] = useState(false);
  const trackingRef = useRef(false),
    previousCenter = useRef<THREE.Vector3 | null>(null);
  const followedId = useRef<string | null>(null);
  const history = useRef<CameraSnapshot[]>([]);
  const [historyCount, setHistoryCount] = useState(0);
  const pendingView = useRef<{
    view: CameraSnapshot;
    focusId: string | null;
  } | null>(null);
  const focusRef = useRef<(id: string, follow?: boolean) => void>(() => {});
  const stopRef = useRef<() => void>(() => {});
  const handledRequest = useRef<{ id: string; sequence: number } | null>(null);
  const [travelling, setTravelling] = useState(false);
  const [fadedCount, setFadedCount] = useState(0);
  const [visibleCount, setVisibleCount] = useState(0),
    [missingCount, setMissingCount] = useState(0);
  const [hasSelection, setHasSelection] = useState(false),
    [notice, setNotice] = useState("");
  const [floorPickerOpen, setFloorPickerOpen] = useState(false);
  const [previewFloorId, setPreviewFloorId] = useState<string | null>(null);
  const [transitionPair, setTransitionPair] = useState<[string, string] | null>(
    null,
  );
  const previewOrigin = useRef<{
    view: CameraSnapshot;
    followId: string | null;
  } | null>(null);
  const previewTarget = useRef<CameraSnapshot | null>(null);
  const pairTimer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const previousRide = useRef<{ sourceId: string; destId: string } | null>(
    null,
  );
  useEffect(
    () => () => {
      if (pairTimer.current) clearTimeout(pairTimer.current);
    },
    [],
  );
  const entities = useMemo(() => {
    const result = new Map<string, Entity>();
    for (const r of project?.robots ?? [])
      result.set(r.id, {
        name: r.name,
        floor: r.floor_id,
        kind: modelNames[r.model_id] ?? r.model_id,
        dynamic: true,
      });
    for (const e of project?.environment.elements ?? [])
      result.set(e.id, {
        name: e.name,
        floor: e.floor_id,
        kind: "시설·공간",
        dynamic: e.dynamic || e.kind === "elevator",
        floorAnchor: { name: `${e.id}/shape`, centerOffset: e.size.z / 2 },
      });
    for (const e of project?.items ?? [])
      result.set(e.id, {
        name: e.name,
        floor: e.floor_id,
        kind: "물품",
        dynamic: true,
        floorAnchor: { name: `${e.id}/shape`, centerOffset: e.size.z / 2 },
      });
    for (const e of project?.people ?? [])
      result.set(e.id, {
        name: e.name,
        floor: e.floor_id,
        kind: "사람",
        dynamic: true,
        floorAnchor: { name: `${e.id}/torso`, centerOffset: 0.85 },
      });
    return result;
  }, [project]);
  const floors = useMemo(
    () =>
      [...(project?.environment.floors ?? [])].sort(
        (a, b) => a.elevation - b.elevation,
      ),
    [project],
  );
  const elevatorIds = useMemo(
    () =>
      new Set(
        (project?.environment.elements ?? [])
          .filter((element) => element.kind === "elevator")
          .map((element) => element.id),
      ),
    [project],
  );
  const displayFloor = floors.find((f) => f.id === floorId),
    selectedEntity = entities.get(selected);
  const selectedRobot = state?.robots.find((r) => r.id === selected);
  const rideContext = activeRide(state, project, selectedRobot?.id ?? "");
  const activePair =
    previewFloorId && previewFloorId !== floorId
      ? [floorId, previewFloorId]
      : rideContext
        ? [rideContext.source.id, rideContext.dest.id]
        : transitionPair;
  const visibleFloorIds = new Set(activePair ?? [floorId]);
  const visibleFloorKey = [...visibleFloorIds].sort().join("|");
  const selectedPerson = project?.people.find(
    (person) => person.id === selected,
  );
  const labelBodies = [
    ...(state?.robots ?? []),
    ...(project?.people ?? []).map((person) => ({
      id: person.id,
      name: person.name,
      model_id: "person",
    })),
  ];
  const selectedName = selectedEntity?.name ?? selectedRobot?.name ?? selected;
  const connection = connectionState ?? (state ? "connected" : "connecting");
  const selectedFloorId = selectedRobot
    ? floorAtHeight(floors, selectedRobot.pose.z, selectedEntity?.floor)
    : selectedEntity?.dynamic && selectedEntity.floorAnchor
      ? floorAtGeometryBase(
          floors,
          state?.geoms.find(
            (geom) => geom.name === selectedEntity.floorAnchor?.name,
          ),
          selectedEntity.floorAnchor.centerOffset,
          selectedEntity.floor,
        )
      : selectedEntity?.floor;
  const otherFloor =
    selectedFloorId && selectedFloorId !== floorId
      ? floors.find((floor) => floor.id === selectedFloorId)
      : undefined;
  const hasRobotPose =
    !!selectedRobot && Object.values(selectedRobot.pose).every(Number.isFinite);
  // Sensor age describes the control observation, not freshness of the actual
  // physics scene. A connected, paused scene is valid for camera following.
  const canTrack =
    hasRobotPose &&
    !error &&
    connection === "connected" &&
    renderedEntities.includes(selected);
  const canFocus = !!selected && !error && renderedEntities.includes(selected);
  const available = !!state?.geoms.length && !error && visibleCount > 0;
  const focusReason = !selected
    ? "먼저 로봇이나 객체를 선택하세요"
    : !canFocus
      ? "선택한 객체의 실제 형상을 기다립니다"
      : otherFloor
        ? `‘${otherFloor.name}’으로 이동해 선택 형상 보기`
        : selectedRobot
          ? "로봇 전방 사선으로 한 번 이동 · 따라가기는 별도 선택"
          : "선택한 실제 형상으로 한 번 이동";
  const followReason =
    connection !== "connected"
      ? "실행부 연결을 확인한 뒤 따라가기를 사용할 수 있습니다"
      : !selectedRobot
        ? "실행 장면의 로봇을 먼저 선택하세요"
        : !canTrack
          ? "로봇의 실제 형상과 위치를 기다립니다"
          : "실제 장면의 로봇 이동을 같은 거리에서 따라갑니다 · 직접 조작하면 해제";
  function snapshot(rt: Runtime): CameraSnapshot {
    return {
      position: rt.camera.position.toArray() as [number, number, number],
      target: rt.controls.target.toArray() as [number, number, number],
      up: rt.camera.up.toArray() as [number, number, number],
      floorId: rt.floorId || floorId,
    };
  }
  function rememberView(rt: Runtime) {
    const view = snapshot(rt),
      last = history.current.at(-1);
    if (!last || JSON.stringify(last) !== JSON.stringify(view)) {
      history.current = [...history.current.slice(-19), copyView(view)];
      setHistoryCount(history.current.length);
    }
  }
  function stopCamera() {
    const rt = runtime.current;
    if (rt) {
      rt.travel = null;
      rt.focusId = null;
    }
    pendingView.current = null;
    trackingRef.current = false;
    followedId.current = null;
    previousCenter.current = null;
    previousRide.current = null;
    setTracking(false);
    setTravelling(false);
    setNotice("자유 시점 · 따라가기 꺼짐");
  }
  stopRef.current = stopCamera;
  function travelTo(rt: Runtime, view: CameraSnapshot, duration = 650) {
    const reduced = window.matchMedia(
      "(prefers-reduced-motion: reduce)",
    ).matches;
    rt.travel =
      reduced || duration <= 0
        ? null
        : {
            from: snapshot(rt),
            to: copyView(view),
            started: performance.now(),
            duration,
          };
    if (!rt.travel) {
      rt.camera.position.fromArray(view.position);
      rt.camera.up.fromArray(view.up).normalize();
      rt.controls.target.fromArray(view.target);
      rt.controls.update();
    }
    const distance = new THREE.Vector3(...view.position).distanceTo(
      new THREE.Vector3(...view.target),
    );
    rt.camera.far = Math.max(300, distance * 8);
    rt.controls.maxDistance = Math.max(150, distance * 3);
    rt.camera.updateProjectionMatrix();
    setTravelling(duration > 200 && !reduced);
    rt.invalidate();
  }
  function openFloorPicker() {
    const rt = runtime.current;
    if (!rt) return;
    previewOrigin.current = {
      view: snapshot(rt),
      followId: trackingRef.current ? followedId.current : null,
    };
    previewTarget.current = null;
    stopCamera();
    rt.focusId = null;
    setFloorPickerOpen(true);
    setNotice("층 단면 탐색 · 올려서 미리 보고 눌러서 고정");
  }
  function previewFloor(id: string) {
    const rt = runtime.current,
      origin = previewOrigin.current;
    const source = floors.find((item) => item.id === origin?.view.floorId);
    const dest = floors.find((item) => item.id === id);
    if (!rt || !source || !dest || previewTarget.current?.floorId === id)
      return;
    const anchor = {
      x: Math.min(source.width, dest.width) / 2,
      y: Math.min(source.depth, dest.depth) / 2,
    };
    const view = floorPairView(
      source,
      dest,
      anchor,
      null,
      rt.camera.fov,
      rt.camera.aspect,
      rt.camera.near,
    );
    view.floorId = id;
    previewTarget.current = view;
    setPreviewFloorId(id);
    travelTo(rt, view, 380);
  }
  function cancelFloorPicker() {
    const rt = runtime.current,
      origin = previewOrigin.current;
    setFloorPickerOpen(false);
    setPreviewFloorId(null);
    previewOrigin.current = null;
    previewTarget.current = null;
    if (rt && origin) {
      travelTo(rt, origin.view, 420);
      const followed = state?.robots.find(
        (robot) => robot.id === origin.followId,
      );
      if (followed) {
        trackingRef.current = true;
        followedId.current = origin.followId;
        previousCenter.current = new THREE.Vector3(
          followed.pose.x,
          followed.pose.y,
          followed.pose.z,
        );
        rt.focusId = origin.followId;
        setTracking(true);
      }
    }
    setNotice("층 탐색 취소 · 원래 시점 복귀");
  }
  function commitFloor(id: string) {
    const rt = runtime.current,
      origin = previewOrigin.current;
    if (!rt || !origin || !onFloorChange) return;
    if (id === origin.view.floorId) {
      cancelFloorPicker();
      return;
    }
    history.current = [...history.current.slice(-19), copyView(origin.view)];
    setHistoryCount(history.current.length);
    const target =
      previewTarget.current?.floorId === id
        ? copyView(previewTarget.current)
        : null;
    const source = floors.find((item) => item.id === origin.view.floorId);
    const dest = floors.find((item) => item.id === id);
    const anchor =
      source && dest
        ? {
            x: Math.min(source.width, dest.width) / 2,
            y: Math.min(source.depth, dest.depth) / 2,
          }
        : null;
    const view =
      target ??
      (source && dest && anchor
        ? floorPairView(
            source,
            dest,
            anchor,
            null,
            rt.camera.fov,
            rt.camera.aspect,
            rt.camera.near,
          )
        : snapshot(rt));
    view.floorId = id;
    pendingView.current = { view, focusId: null };
    setFloorPickerOpen(false);
    setPreviewFloorId(null);
    previewOrigin.current = null;
    previewTarget.current = null;
    setTransitionPair([origin.view.floorId, id]);
    if (pairTimer.current) clearTimeout(pairTimer.current);
    pairTimer.current = setTimeout(() => setTransitionPair(null), 800);
    onFloorChange(id);
    setNotice(
      `${source?.name ?? "출발층"} → ${dest?.name ?? "도착층"} · 두 층을 함께 보며 이동`,
    );
  }
  function entityBounds(rt: Runtime, id: string) {
    const bounds = new THREE.Box3();
    for (const object of rt.byEntity.get(id) ?? [])
      if (object.userData.sourceOpacity > 0) bounds.expandByObject(object);
    return bounds;
  }
  function focusEntity(id: string, follow = false) {
    const rt = runtime.current;
    if (!rt) return;
    const bounds = entityBounds(rt, id);
    const robot = state?.robots.find((item) => item.id === id);
    const human = rt.humanMotion.get(id);
    const ride = robot ? activeRide(state, project, id) : null;
    const lift =
      ride &&
      project?.environment.elements.find(
        (element) => element.id === ride.facilityId,
      );
    const nextFloor = ride ? floorId : (rt.entityFloors.get(id) ?? floorId);
    const occluders = [...rt.objects.values()]
      .filter(
        (object) =>
          object.userData.cameraOccluder &&
          object.userData.physicalFloor === nextFloor,
      )
      .map((object) => new THREE.Box3().setFromObject(object));
    const view =
      ride && lift && robot
        ? floorPairView(
            ride.source,
            ride.dest,
            lift.pose,
            robot.pose,
            rt.camera.fov,
            rt.camera.aspect,
            rt.camera.near,
          )
        : robotFocusView(
            bounds,
            robot?.pose.yaw ?? human?.heading ?? 0,
            nextFloor,
            rt.camera.fov,
            rt.camera.aspect,
            rt.camera.near,
            occluders,
          );
    if (!view || (nextFloor !== floorId && !onFloorChange)) return;
    rememberView(rt);
    stopCamera();
    rt.focusId = id;
    if (follow && robot) {
      followedId.current = id;
      trackingRef.current = true;
      previousCenter.current = new THREE.Vector3(
        robot.pose.x,
        robot.pose.y,
        robot.pose.z,
      );
      setTracking(true);
    }
    if (nextFloor !== floorId) {
      pendingView.current = { view, focusId: id };
      onFloorChange?.(nextFloor);
    } else travelTo(rt, view);
    setNotice(
      follow
        ? "따라가기 켜짐 · 직접 카메라를 조작하면 해제"
        : robot
          ? "로봇 전방 사선으로 한 번 이동 · 도착 후 자유롭게 둘러보세요"
          : human
            ? "사람의 이동 방향 앞 사선으로 한 번 이동"
            : "선택 형상으로 한 번 이동",
    );
  }
  focusRef.current = focusEntity;
  function previousView() {
    const rt = runtime.current,
      view = history.current.pop();
    if (!rt || !view) return;
    setHistoryCount(history.current.length);
    stopCamera();
    rt.focusId = null;
    if (view.floorId !== floorId && onFloorChange) {
      pendingView.current = { view: copyView(view), focusId: null };
      onFloorChange(view.floorId);
    } else travelTo(rt, view);
    setNotice("이전 시점 · 따라가기 꺼짐");
  }
  function frameView(view: View, record = true, duration = 650) {
    if (view === "selected") {
      focusEntity(selected);
      return;
    }
    const rt = runtime.current;
    if (!rt || rt.allBounds.isEmpty()) return;
    if (record) rememberView(rt);
    stopCamera();
    rt.focusId = null;
    const center = rt.allBounds.getCenter(new THREE.Vector3());
    let direction = new THREE.Vector3(0.65, -0.9, 0.85).normalize();
    if (view === "top") direction = new THREE.Vector3(0, -0.025, 1).normalize();
    if (view === "front")
      direction = new THREE.Vector3(0, -1, 0.035).normalize();
    const distance = Math.max(
      rt.controls.minDistance,
      perspectiveBoxDistance(
        rt.allBounds.getSize(new THREE.Vector3()).multiplyScalar(0.5),
        direction,
        rt.camera.fov,
        rt.camera.aspect,
        rt.camera.near,
      ),
    );
    travelTo(
      rt,
      {
        position: center
          .clone()
          .addScaledVector(direction, distance)
          .toArray() as [number, number, number],
        target: center.toArray() as [number, number, number],
        up: [0, 0, 1],
        floorId,
      },
      duration,
    );
    setNotice(
      view === "top"
        ? "위에서 보기 · +Z"
        : view === "front"
          ? "앞에서 보기 · +Y"
          : "현재 층 전체 보기",
    );
  }
  function nudge(horizontal: number, vertical: number, zoom = 0) {
    const rt = runtime.current;
    if (!rt) return;
    stopCamera();
    const offset = rt.camera.position.clone().sub(rt.controls.target);
    if (zoom)
      offset
        .multiplyScalar(zoom > 0 ? 0.8 : 1.25)
        .clampLength(rt.controls.minDistance, rt.controls.maxDistance);
    else if (mode === "rotate") {
      offset.applyAxisAngle(worldUp, horizontal * 0.14);
      offset.applyAxisAngle(
        offset.clone().cross(worldUp).normalize(),
        vertical * 0.1,
      );
    } else {
      const right = new THREE.Vector3().setFromMatrixColumn(
          rt.camera.matrix,
          0,
        ),
        up = new THREE.Vector3().setFromMatrixColumn(rt.camera.matrix, 1);
      rt.controls.target.add(
        right
          .multiplyScalar(horizontal * offset.length() * 0.08)
          .addScaledVector(up, vertical * offset.length() * 0.08),
      );
    }
    rt.camera.position.copy(rt.controls.target).add(offset);
    rt.controls.update();
    rt.invalidate();
  }
  function freeTravel(right: number, forward: number, up: number) {
    const rt = runtime.current;
    if (!rt) return;
    stopCamera();
    const ahead = rt.controls.target.clone().sub(rt.camera.position);
    ahead.z = 0;
    if (ahead.lengthSq() < 1e-6) ahead.set(0, 1, 0);
    ahead.normalize();
    const side = ahead.clone().cross(worldUp).normalize();
    const step = Math.max(
      0.1,
      rt.camera.position.distanceTo(rt.controls.target) * 0.08,
    );
    const delta = side
      .multiplyScalar(right * step)
      .addScaledVector(ahead, forward * step)
      .addScaledVector(worldUp, up * step);
    rt.camera.position.add(delta);
    rt.controls.target.add(delta);
    rt.controls.update();
    rt.invalidate();
  }
  useEffect(() => {
    const node = container.current;
    if (!node) return;
    let renderer: THREE.WebGLRenderer;
    try {
      renderer = new THREE.WebGLRenderer({ antialias: true });
    } catch {
      setError(
        "WebGL을 시작하지 못했습니다. 2D 도면으로 계속 작업하거나 3D 화면을 다시 열어주세요.",
      );
      return;
    }
    setError("");
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setClearColor(0xe7ecf0);
    renderer.outputColorSpace = THREE.SRGBColorSpace;
    renderer.domElement.tabIndex = 0;
    renderer.domElement.setAttribute(
      "aria-label",
      "3D 물리 장면. 방향키 회전·이동, 더하기·빼기 확대·축소, W A S D 자유 이동, Q E 높이 이동",
    );
    node.appendChild(renderer.domElement);
    const scene = new THREE.Scene();
    scene.add(new THREE.HemisphereLight(0xfafcff, 0x8797aa, 1.8));
    const light = new THREE.DirectionalLight(0xfafcff, 1.7);
    light.position.set(3, -4, 10);
    scene.add(light);
    const camera = new THREE.PerspectiveCamera(42, 1, 0.02, 300);
    camera.up.copy(worldUp);
    camera.position.set(14, -18, 18);
    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = false;
    controls.minPolarAngle = 0.015;
    controls.maxPolarAngle = Math.PI * 0.495;
    controls.minDistance = 0.25;
    controls.maxDistance = 150;
    const selectedBounds = new THREE.Box3(),
      selection = new THREE.Box3Helper(
        selectedBounds,
        new THREE.Color(0x1d4cae),
      );
    (selection.material as THREE.LineBasicMaterial).depthTest = false;
    selection.renderOrder = 10;
    selection.visible = false;
    scene.add(selection);
    const selectionRing = new THREE.Mesh(
      new THREE.RingGeometry(0.38, 0.405, 48),
      new THREE.MeshBasicMaterial({
        color: 0x2958aa,
        side: THREE.DoubleSide,
        depthWrite: false,
      }),
    );
    selectionRing.visible = false;
    scene.add(selectionRing);
    const direction = new THREE.ArrowHelper(
      new THREE.Vector3(1, 0, 0),
      new THREE.Vector3(),
      0.7,
      0x193e84,
      0.18,
      0.12,
    );
    direction.visible = false;
    scene.add(direction);
    const rt: Runtime = {
      renderer,
      scene,
      camera,
      controls,
      objects: new Map(),
      humans: new Map(),
      humanMotion: new Map(),
      selectionRing,
      byEntity: new Map(),
      selection,
      direction,
      selectedBounds,
      allBounds: new THREE.Box3(),
      invalidate: () => {},
      runId: null,
      meshSource: null,
      frame: 0,
      lost: false,
      floorId: "",
      entityFloors: new Map(),
      travel: null,
      focusId: null,
    };
    rt.invalidate = () => {
      if (rt.frame || rt.lost) return;
      rt.frame = requestAnimationFrame(() => {
        rt.frame = 0;
        if (rt.lost) return;
        try {
          if (rt.travel) {
            const sampled = sampleTravel(rt.travel, performance.now());
            camera.position.fromArray(sampled.view.position);
            camera.up.fromArray(sampled.view.up).normalize();
            controls.target.fromArray(sampled.view.target);
            controls.update();
            if (sampled.done) {
              rt.travel = null;
              setTravelling(false);
            }
          }
          // Fade only received wall/ceiling materials intersecting the camera's
          // sight lines to the focused robot. Shapes and collision data stay intact.
          let faded = 0;
          const focusBounds = new THREE.Box3();
          for (const object of rt.byEntity.get(rt.focusId ?? "") ?? [])
            if (object.visible) focusBounds.expandByObject(object);
          const sightPoints = focusBounds.isEmpty()
            ? []
            : [
                focusBounds.getCenter(new THREE.Vector3()),
                new THREE.Vector3(
                  focusBounds.min.x,
                  focusBounds.min.y,
                  focusBounds.max.z,
                ),
                new THREE.Vector3(
                  focusBounds.max.x,
                  focusBounds.max.y,
                  focusBounds.min.z,
                ),
              ];
          for (const object of rt.objects.values()) {
            if (!object.userData.cameraOccluder) continue;
            const material = object.material as THREE.MeshStandardMaterial;
            const obscures =
              object.visible &&
              sightPoints.some((point) =>
                segmentHitsBox(
                  camera.position,
                  point,
                  new THREE.Box3().setFromObject(object),
                ),
              );
            const opacity = obscures
              ? Math.min(0.025, object.userData.sourceOpacity as number)
              : (object.userData.sourceOpacity as number);
            if (obscures) faded++;
            material.opacity = opacity;
            material.depthWrite = opacity >= 1;
            if (material.transparent !== opacity < 1) {
              material.transparent = opacity < 1;
              material.needsUpdate = true;
            }
          }
          setFadedCount(faded);
          // Names are an inspection overlay anchored to received mesh bounds;
          // no geometry, model color, collision shape or robot pose is changed.
          camera.updateMatrixWorld();
          const size = renderer.domElement.getBoundingClientRect();
          type Rect = {
            left: number;
            top: number;
            right: number;
            bottom: number;
          };
          const occupied: Rect[] = [
            ...node.querySelectorAll<HTMLElement>(
              ".physics-view__caption, .physics-view__camera, .physics-view__fine-content, .physics-view__selection, .physics-view__selection-hint, .physics-view__connection, .physics-view__human-error, .physics-view__diagnostic-note",
            ),
          ].flatMap((element) => {
            const rect = element.getBoundingClientRect();
            return rect.width && rect.height
              ? [
                  {
                    left: rect.left - size.left,
                    top: rect.top - size.top,
                    right: rect.right - size.left,
                    bottom: rect.bottom - size.top,
                  },
                ]
              : [];
          });
          for (const id of labelNodes.current.keys()) {
            const body = new THREE.Box3();
            for (const mesh of rt.byEntity.get(id) ?? [])
              if (mesh.visible) body.expandByObject(mesh);
            if (body.isEmpty()) continue;
            const projected: THREE.Vector3[] = [];
            for (const x of [body.min.x, body.max.x])
              for (const y of [body.min.y, body.max.y])
                for (const z of [body.min.z, body.max.z])
                  projected.push(new THREE.Vector3(x, y, z).project(camera));
            if (projected.some((point) => point.z < -1 || point.z > 1))
              continue;
            occupied.push({
              left: Math.min(
                ...projected.map((point) => ((point.x + 1) * size.width) / 2),
              ),
              right: Math.max(
                ...projected.map((point) => ((point.x + 1) * size.width) / 2),
              ),
              top: Math.min(
                ...projected.map((point) => ((1 - point.y) * size.height) / 2),
              ),
              bottom: Math.max(
                ...projected.map((point) => ((1 - point.y) * size.height) / 2),
              ),
            });
          }
          const labels = [...labelNodes.current].sort(
            ([a, first], [b, second]) =>
              Number(second.getAttribute("aria-pressed") === "true") -
                Number(first.getAttribute("aria-pressed") === "true") ||
              a.localeCompare(b),
          );
          let hidden = 0;
          for (const [id, label] of labels) {
            const line = labelLines.current.get(id);
            if (line) line.style.display = "none";
            const labelBounds = new THREE.Box3();
            for (const object of rt.byEntity.get(id) ?? [])
              if (object.visible) labelBounds.expandByObject(object);
            const point = labelBounds.getCenter(new THREE.Vector3());
            point.z = labelBounds.max.z + 0.18;
            point.project(camera);
            const visible =
              !labelBounds.isEmpty() &&
              [point.x, point.y, point.z].every(Number.isFinite) &&
              point.z >= -1 &&
              point.z <= 1 &&
              Math.abs(point.x) < 0.96 &&
              Math.abs(point.y) < 0.96;
            label.hidden = !visible;
            if (!visible) continue;
            const anchorX = ((point.x + 1) * size.width) / 2;
            const anchorY = ((1 - point.y) * size.height) / 2;
            const width = label.offsetWidth,
              height = label.offsetHeight;
            const column = width + 10,
              row = height + 10;
            // Selected labels get first choice. Nearby alternatives use a
            // leader to the original screen anchor; crowded labels are omitted.
            const offsets = [
              [0, 0],
              [0, -row],
              [-column, 0],
              [column, 0],
              [-column, -row],
              [column, -row],
              [0, row],
              [-column, row],
              [column, row],
              [0, -2 * row],
              [-column, -2 * row],
              [column, -2 * row],
              [0, 2 * row],
            ];
            const place = offsets
              .map(([dx, dy]) => ({
                left: anchorX + dx - width / 2,
                right: anchorX + dx + width / 2,
                top: anchorY + dy - height - 6,
                bottom: anchorY + dy - 6,
              }))
              .find(
                (rect) =>
                  rect.left >= 8 &&
                  rect.top >= 8 &&
                  rect.right <= size.width - 8 &&
                  rect.bottom <= size.height - 8 &&
                  !occupied.some(
                    (other) =>
                      rect.left < other.right + 5 &&
                      rect.right > other.left - 5 &&
                      rect.top < other.bottom + 5 &&
                      rect.bottom > other.top - 5,
                  ),
              );
            if (!place) {
              label.hidden = true;
              hidden++;
              continue;
            }
            occupied.push(place);
            label.style.left = `${(place.left + place.right) / 2}px`;
            label.style.top = `${place.bottom}px`;
            if (line) {
              const fromX = Math.max(
                place.left,
                Math.min(place.right, anchorX),
              );
              const fromY = Math.max(
                place.top,
                Math.min(place.bottom, anchorY),
              );
              if (Math.hypot(anchorX - fromX, anchorY - fromY) > 8) {
                line.setAttribute("x1", String(fromX));
                line.setAttribute("y1", String(fromY));
                line.setAttribute("x2", String(anchorX));
                line.setAttribute("y2", String(anchorY));
                line.style.display = "";
              }
            }
          }
          setHiddenLabelCount(hidden);
          renderer.render(scene, camera);
          if (rt.travel) rt.invalidate();
        } catch {
          rt.lost = true;
          setError(
            "3D 장면을 그리지 못했습니다. 화면을 다시 열거나 2D 도면을 이용하세요.",
          );
        }
      });
    };
    runtime.current = rt;
    void document.fonts.ready.then(() => {
      if (runtime.current === rt) rt.invalidate();
    });
    controls.addEventListener("change", rt.invalidate);
    const updateSize = () => {
      const { width, height } = node.getBoundingClientRect();
      if (!width || !height) return;
      renderer.setSize(width, height, false);
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
      rt.invalidate();
    };
    updateSize();
    const resize = new ResizeObserver(updateSize);
    resize.observe(node);
    const manualCamera = () => {
      stopRef.current();
      previewOrigin.current = null;
      previewTarget.current = null;
      setPreviewFloorId(null);
      setFloorPickerOpen(false);
    };
    controls.addEventListener("start", manualCamera);
    let down: ClickGesture | null = null;
    const start = (event: PointerEvent) => {
      if (!event.isPrimary) {
        down = null;
        return;
      }
      if (event.button === 0) {
        down = {
          x: event.clientX,
          y: event.clientY,
          pointerId: event.pointerId,
          started: Date.now(),
          maxExcursion: 0,
        };
        renderer.domElement.focus({ preventScroll: true });
      }
    };
    const move = (event: PointerEvent) => {
      if (down && event.pointerId === down.pointerId)
        down = advanceClick(down, event.clientX, event.clientY);
    };
    const click = (event: PointerEvent) => {
      if (down) down = advanceClick(down, event.clientX, event.clientY);
      if (
        !down ||
        event.button !== 0 ||
        !isClick(down, event.pointerId, Date.now())
      ) {
        down = null;
        return;
      }
      down = null;
      const rect = renderer.domElement.getBoundingClientRect();
      if (!rect.width || !rect.height) return;
      const ray = new THREE.Raycaster();
      ray.setFromCamera(
        new THREE.Vector2(
          ((event.clientX - rect.left) / rect.width) * 2 - 1,
          (-(event.clientY - rect.top) / rect.height) * 2 + 1,
        ),
        camera,
      );
      const hit = ray.intersectObjects(
        [...rt.byEntity.values()]
          .flat()
          .filter(
            (object) =>
              object.visible &&
              object.userData.selectable &&
              !(
                object.userData.cameraOccluder &&
                (object.material as THREE.MeshStandardMaterial).opacity <= 0.12
              ),
          ),
      )[0];
      const id = hit ? (hit.object.userData.entityId as string) : "";
      // Focus first so a parent selection callback cannot switch floors before
      // the old floor and view have been captured for Previous view.
      if (id) focusRef.current(id);
      selectRef.current(id);
    };
    const cancel = () => {
      down = null;
    };
    const lost = (event: Event) => {
      event.preventDefault();
      rt.lost = true;
      cancelAnimationFrame(rt.frame);
      rt.frame = 0;
      setError(
        "그래픽 연결이 끊겼습니다. 실행부 상태는 변경하지 않았습니다. 3D 화면을 복구하거나 2D 도면을 이용하세요.",
      );
    };
    const restored = () => setGeneration((value) => value + 1),
      canvas = renderer.domElement;
    canvas.addEventListener("pointerdown", start);
    canvas.addEventListener("pointerup", click);
    canvas.addEventListener("pointermove", move);
    canvas.addEventListener("pointercancel", cancel);
    canvas.addEventListener("webglcontextlost", lost);
    canvas.addEventListener("webglcontextrestored", restored);
    return () => {
      cancelAnimationFrame(rt.frame);
      resize.disconnect();
      controls.removeEventListener("change", rt.invalidate);
      controls.removeEventListener("start", manualCamera);
      controls.dispose();
      canvas.removeEventListener("pointerdown", start);
      canvas.removeEventListener("pointerup", click);
      canvas.removeEventListener("pointermove", move);
      canvas.removeEventListener("pointercancel", cancel);
      canvas.removeEventListener("webglcontextlost", lost);
      canvas.removeEventListener("webglcontextrestored", restored);
      rt.objects.forEach((object) => {
        object.geometry.dispose();
        (object.material as THREE.Material).dispose();
      });
      rt.humans.forEach((human) => human.dispose());
      selectionRing.geometry.dispose();
      (selectionRing.material as THREE.Material).dispose();
      selection.geometry.dispose();
      (selection.material as THREE.Material).dispose();
      direction.dispose();
      renderer.dispose();
      canvas.remove();
      if (runtime.current === rt) runtime.current = null;
    };
  }, [generation]);
  useEffect(() => {
    const rt = runtime.current;
    if (!rt) return;
    rt.controls.mouseButtons.LEFT =
      mode === "pan" ? THREE.MOUSE.PAN : THREE.MOUSE.ROTATE;
    rt.controls.touches.ONE =
      mode === "pan" ? THREE.TOUCH.PAN : THREE.TOUCH.ROTATE;
  }, [mode, generation]);
  useEffect(() => {
    const rt = runtime.current;
    if (!rt) return;
    const changedRun = rt.runId !== (state?.run_id ?? null);
    // App owns selection across run changes: live selections reset there,
    // while a selected draft remains available in the editor.
    if (changedRun || rt.meshSource !== meshes) {
      rt.objects.forEach((object) => {
        rt.scene.remove(object);
        object.geometry.dispose();
        (object.material as THREE.Material).dispose();
      });
      rt.objects.clear();
      rt.humans.forEach((human) => {
        rt.scene.remove(human.root);
        human.dispose();
      });
      rt.humans.clear();
      rt.humanMotion.clear();
      rt.runId = state?.run_id ?? null;
      rt.meshSource = meshes;
      if (changedRun) {
        stopCamera();
        history.current = [];
        setHistoryCount(0);
        rt.focusId = null;
        handledRequest.current = null;
      }
    }
    const meshData = new Map(meshes.map((mesh) => [mesh.id, mesh])),
      robots = new Map(state?.robots.map((robot) => [robot.id, robot])),
      geometryByName = new Map(state?.geoms.map((geom) => [geom.name, geom]));
    const people = new Map(
      project?.people.map((person) => [person.id, person]),
    );
    // Classify each entity once from its base anchor so tall bodies and their
    // separate parts cannot split between floors as their centers cross a landing.
    const entityFloors = new Map<string, string | undefined>();
    for (const [id, entity] of entities) {
      if (elevatorIds.has(id)) continue;
      entityFloors.set(
        id,
        !entity.dynamic
          ? entity.floor
          : entity.floorAnchor
            ? floorAtGeometryBase(
                floors,
                geometryByName.get(entity.floorAnchor.name),
                entity.floorAnchor.centerOffset,
                entity.floor,
              )
            : floorAtHeight(floors, robots.get(id)?.pose.z, entity.floor),
      );
    }
    rt.entityFloors = entityFloors;
    const cabinFloors = new Map<string, string | undefined>();
    const landingFloors = new Map<string, string>();
    for (const id of elevatorIds)
      for (const floor of floors)
        landingFloors.set(`${id}/landing-${floor.id}-panel`, floor.id);
    for (const geom of state?.geoms ?? []) {
      if (
        !elevatorIds.has(geom.entity_id) ||
        geom.name !== `${geom.entity_id}/platform`
      )
        continue;
      if (
        geom.position.length !== 3 ||
        geom.size.length !== 3 ||
        geom.quaternion.length !== 4 ||
        ![...geom.position, ...geom.size, ...geom.quaternion].every(
          Number.isFinite,
        )
      )
        continue;
      const [w, x, y, z] = geom.quaternion;
      // Use the actual box's world-Z upper extent. The plate center is 7 cm
      // below the landing, so classifying its center assigns it to the floor below.
      const top =
        geom.position[2] +
        Math.abs(2 * (x * z - w * y)) * geom.size[0] +
        Math.abs(2 * (y * z + w * x)) * geom.size[1] +
        Math.abs(1 - 2 * (x * x + y * y)) * geom.size[2];
      cabinFloors.set(geom.entity_id, floorAtHeight(floors, top));
    }
    // Match known IDs rather than splitting names; floor IDs may contain '/'.
    const namedFloors = [...floors].sort((a, b) => b.id.length - a.id.length);
    const upperFloor = activePair
      ?.map((id) => floors.find((floor) => floor.id === id))
      .filter((floor) => floor !== undefined)
      .sort((a, b) => b.elevation - a.elevation)[0]?.id;
    const live = new Set<number>();
    const bounds = new THREE.Box3();
    rt.byEntity.clear();
    rt.allBounds.makeEmpty();
    let visible = 0,
      missing = 0;
    for (const g of state?.geoms ?? []) {
      if (
        ![...g.position, ...g.quaternion, ...g.size, ...g.rgba].every(
          Number.isFinite,
        ) ||
        g.position.length !== 3 ||
        g.quaternion.length !== 4
      ) {
        missing++;
        continue;
      }
      live.add(g.id);
      const shape = `${g.type}:${g.size.join(",")}:${g.mesh_id}`;
      let object = rt.objects.get(g.id);
      if (object && object.userData.shape !== shape) {
        rt.scene.remove(object);
        object.geometry.dispose();
        (object.material as THREE.Material).dispose();
        rt.objects.delete(g.id);
        object = undefined;
      }
      if (!object) {
        const geometry = geometryFor(g, meshData);
        if (!geometry) {
          missing++;
          continue;
        }
        object = new THREE.Mesh(
          geometry,
          new THREE.MeshStandardMaterial({
            roughness: 0.76,
            metalness: 0.04,
            side: THREE.DoubleSide,
          }),
        );
        object.userData.shape = shape;
        rt.objects.set(g.id, object);
        rt.scene.add(object);
      }
      const entity = entities.get(g.entity_id),
        robot = robots.get(g.entity_id);
      const physicalFloor =
        landingFloors.get(g.name) ??
        (elevatorIds.has(g.entity_id)
          ? cabinFloors.get(g.entity_id)
          : undefined) ??
        entityFloors.get(g.entity_id) ??
        (entity?.dynamic
          ? floorAtHeight(floors, robot?.pose.z ?? g.position[2])
          : entity?.floor);
      const geometryFloor = g.name.startsWith("floor/")
        ? namedFloors.find((floor) => g.name.startsWith(`floor/${floor.id}/`))
            ?.id
        : (physicalFloor ?? floorAtHeight(floors, g.position[2]));
      object.visible =
        (g.rgba[3] ?? 1) > 0 &&
        !!geometryFloor &&
        visibleFloorIds.has(geometryFloor);
      if (people.has(g.entity_id))
        object.visible = object.visible && showDiagnostics;
      object.position.fromArray(g.position);
      object.quaternion.set(
        g.quaternion[1],
        g.quaternion[2],
        g.quaternion[3],
        g.quaternion[0],
      );
      object.updateMatrixWorld(true);
      object.userData.entityId = g.entity_id;
      object.userData.physicalFloor = physicalFloor;
      const cutaway =
        !!activePair &&
        geometryFloor === upperFloor &&
        (g.name.startsWith("floor/") ||
          project?.environment.elements.some(
            (element) => element.id === g.entity_id && element.kind === "wall",
          ));
      object.userData.sourceOpacity = cutaway
        ? Math.min(g.rgba[3] ?? 1, 0.16)
        : (g.rgba[3] ?? 1);
      object.userData.cameraOccluder =
        project?.environment.elements.some(
          (element) => element.id === g.entity_id && element.kind === "wall",
        ) ||
        /(?:^|[\/_-])ceiling(?:[\/_-]|$)/i.test(g.name) ||
        (elevatorIds.has(g.entity_id) &&
          /\/(?:wall-[^/]+|door-panel|landing-[^/]+-panel)$/.test(g.name));
      object.userData.selectable = !!entity || !!robot;
      const material = object.material as THREE.MeshStandardMaterial;
      material.color.setRGB(g.rgba[0], g.rgba[1], g.rgba[2]);
      material.opacity = people.has(g.entity_id)
        ? 0.24
        : (object.userData.sourceOpacity as number);
      material.wireframe = people.has(g.entity_id);
      const transparent = material.opacity < 1;
      // Transparent upper slabs must not write depth and hide the lower floor.
      // This only changes rendering; received positions and collision shapes stay intact.
      material.depthWrite = !transparent;
      if (material.transparent !== transparent) {
        material.transparent = transparent;
        material.needsUpdate = true;
      }
      material.emissive.setHex(g.entity_id === selected ? 0x102559 : 0);
      const group = rt.byEntity.get(g.entity_id) ?? [];
      if (!people.has(g.entity_id)) group.push(object);
      rt.byEntity.set(g.entity_id, group);
      if (object.visible) {
        visible++;
        rt.allBounds.union(bounds.setFromObject(object));
      }
    }
    for (const [id, object] of rt.objects)
      if (!live.has(id)) {
        rt.scene.remove(object);
        object.geometry.dispose();
        (object.material as THREE.Material).dispose();
        rt.objects.delete(id);
      }
    let humanFailure = false;
    const liveHumans = new Set<string>();
    for (const person of people.values()) {
      const anchor = geometryByName.get(`${person.id}/torso`);
      if (!anchor) continue;
      const actual = state?.people?.[person.id];
      const motion = sampleHumanMotion(
        rt.humanMotion.get(person.id),
        anchor.position,
        state?.sim_time ?? NaN,
        actual?.actual_velocity,
        actual?.actual_heading_rad,
        person.pose.yaw,
      );
      if (!motion) {
        humanFailure = true;
        continue;
      }
      try {
        let human = rt.humans.get(person.id);
        if (!human) {
          human = createHumanVisual(person.id);
          rt.humans.set(person.id, human);
          rt.scene.add(human.root);
        }
        human.update(motion, person.id === selected);
        rt.humanMotion.set(person.id, motion);
        const shown = visibleFloorIds.has(entityFloors.get(person.id) ?? "");
        human.root.visible = shown;
        human.meshes.forEach((mesh) => {
          mesh.visible = shown;
        });
        rt.byEntity.set(person.id, human.meshes);
        liveHumans.add(person.id);
        if (shown) {
          visible++;
          rt.allBounds.union(bounds.setFromObject(human.root));
        }
      } catch {
        humanFailure = true;
      }
    }
    for (const [id, human] of rt.humans)
      if (!liveHumans.has(id)) {
        rt.scene.remove(human.root);
        human.dispose();
        rt.humans.delete(id);
        rt.humanMotion.delete(id);
      }
    setHumanDisplayFailure(humanFailure);
    const rendered = [...rt.byEntity.keys()]
      .filter((id) => !entityBounds(rt, id).isEmpty())
      .sort();
    setRenderedEntities((previous) =>
      previous.length === rendered.length &&
      previous.every((id, index) => id === rendered[index])
        ? previous
        : rendered,
    );
    rt.selectedBounds.makeEmpty();
    for (const object of rt.byEntity.get(selected) ?? [])
      if (object.visible) rt.selectedBounds.union(bounds.setFromObject(object));
    const has = !rt.selectedBounds.isEmpty();
    rt.selection.visible = has && (!selectedPerson || showDiagnostics);
    rt.selectionRing.visible = has && !!selectedPerson;
    const selectedHumanMotion = rt.humanMotion.get(selected);
    if (selectedHumanMotion)
      rt.selectionRing.position.set(
        selectedHumanMotion.position[0],
        selectedHumanMotion.position[1],
        selectedHumanMotion.position[2] - 0.85 + 0.012,
      );
    setHasSelection(has);
    setVisibleCount(visible);
    setMissingCount(missing);
    rt.direction.visible = has && !!selectedRobot;
    if (selectedRobot && has) {
      rt.direction.position.set(
        selectedRobot.pose.x,
        selectedRobot.pose.y,
        rt.selectedBounds.max.z + 0.12,
      );
      rt.direction.setDirection(
        new THREE.Vector3(
          Math.cos(selectedRobot.pose.yaw),
          Math.sin(selectedRobot.pose.yaw),
          0,
        ),
      );
    }
    const floorChanged = rt.floorId !== floorId;
    if (pendingView.current?.view.floorId === floorId) {
      const pending = pendingView.current;
      pendingView.current = null;
      rt.floorId = floorId;
      rt.focusId = pending.focusId;
      travelTo(rt, pending.view);
    } else if (floorChanged && trackingRef.current && followedId.current) {
      // Following a body through a landing preserves offset; manual floor
      // navigation stops following and frames that floor instead.
      const followed = robots.get(followedId.current);
      if (!followed || entityFloors.get(followed.id) !== floorId)
        frameView("all", !changedRun, 0);
      rt.floorId = floorId;
    } else if (floorChanged || changedRun) {
      if (!changedRun && rt.floorId) rememberView(rt);
      rt.floorId = floorId;
      frameView("all", false, 0);
    }
    const followed = robots.get(followedId.current ?? "");
    if (
      trackingRef.current &&
      followed &&
      entityBounds(rt, followed.id).isEmpty()
    ) {
      stopCamera();
      setNotice("실제 로봇 형상을 찾을 수 없어 따라가기를 멈췄습니다");
    }
    const observedRobot =
      selectedRobot && (trackingRef.current || rt.focusId === selectedRobot.id)
        ? selectedRobot
        : null;
    const lift =
      rideContext &&
      project?.environment.elements.find(
        (element) => element.id === rideContext.facilityId,
      );
    if (rideContext && lift && observedRobot && !floorPickerOpen) {
      const view = floorPairView(
        rideContext.source,
        rideContext.dest,
        lift.pose,
        observedRobot.pose,
        rt.camera.fov,
        rt.camera.aspect,
        rt.camera.near,
      );
      view.floorId = floorId;
      const mid =
        (rideContext.source.elevation + rideContext.dest.elevation) / 2 + 0.35;
      const shift = Math.max(
        -0.3,
        Math.min(0.3, (observedRobot.pose.z - mid) * 0.16),
      );
      view.position[2] += shift;
      view.target[2] += shift;
      const freshRide =
        previousRide.current?.sourceId !== rideContext.source.id ||
        previousRide.current?.destId !== rideContext.dest.id;
      const currentTargetZ = rt.travel?.to.target[2] ?? rt.controls.target.z;
      if (freshRide || Math.abs(view.target[2] - currentTargetZ) > 0.035)
        travelTo(rt, view, freshRide ? 700 : 240);
      previousRide.current = {
        sourceId: rideContext.source.id,
        destId: rideContext.dest.id,
      };
      previousCenter.current = new THREE.Vector3(
        observedRobot.pose.x,
        observedRobot.pose.y,
        observedRobot.pose.z,
      );
    } else if (
      previousRide.current &&
      !rideContext &&
      observedRobot &&
      !floorPickerOpen
    ) {
      const last = previousRide.current;
      previousRide.current = null;
      const destination = floors.find((item) => item.id === last.destId);
      const occluders = [...rt.objects.values()]
        .filter(
          (object) =>
            object.userData.cameraOccluder &&
            object.userData.physicalFloor === destination?.id,
        )
        .map((object) => new THREE.Box3().setFromObject(object));
      const target =
        destination &&
        robotFocusView(
          entityBounds(rt, observedRobot.id),
          observedRobot.pose.yaw,
          destination.id,
          rt.camera.fov,
          rt.camera.aspect,
          rt.camera.near,
          occluders,
        );
      if (target && destination) {
        setTransitionPair([last.sourceId, last.destId]);
        if (pairTimer.current) clearTimeout(pairTimer.current);
        pairTimer.current = setTimeout(() => setTransitionPair(null), 850);
        if (destination.id !== floorId && onFloorChange) {
          pendingView.current = { view: target, focusId: observedRobot.id };
          onFloorChange(destination.id);
        } else travelTo(rt, target, 700);
        setNotice(`${destination.name} 하차 완료 · 로봇 중심 시점으로 복귀`);
      }
    } else if (trackingRef.current && followed) {
      const nextFloor = entityFloors.get(followed.id);
      const center = new THREE.Vector3(
        followed.pose.x,
        followed.pose.y,
        followed.pose.z,
      );
      const delta = center.clone().sub(previousCenter.current ?? center);
      previousCenter.current = center;
      if (delta.lengthSq() > 0) {
        if (rt.travel) {
          rt.travel.to.position = new THREE.Vector3(...rt.travel.to.position)
            .add(delta)
            .toArray() as [number, number, number];
          rt.travel.to.target = new THREE.Vector3(...rt.travel.to.target)
            .add(delta)
            .toArray() as [number, number, number];
        } else {
          const view = snapshot(rt);
          view.position = new THREE.Vector3(...view.position)
            .add(delta)
            .toArray() as [number, number, number];
          view.target = new THREE.Vector3(...view.target)
            .add(delta)
            .toArray() as [number, number, number];
          travelTo(rt, view, 140);
        }
      }
      if (nextFloor && nextFloor !== floorId && !rideContext)
        onFloorChange?.(nextFloor);
    }
    rt.invalidate();
  }, [
    state,
    meshes,
    selected,
    entities,
    floors,
    elevatorIds,
    floorId,
    generation,
    showDiagnostics,
    visibleFloorKey,
    floorPickerOpen,
  ]);
  useEffect(() => {
    if (
      focusRequest &&
      focusRequest.id === selected &&
      (handledRequest.current?.sequence !== focusRequest.sequence ||
        handledRequest.current?.id !== focusRequest.id) &&
      runtime.current?.byEntity.has(focusRequest.id)
    ) {
      handledRequest.current = { ...focusRequest };
      focusEntity(focusRequest.id);
    }
  }, [focusRequest, selected, state?.run_id, state?.geoms, meshes, generation]);
  useEffect(() => {
    const rt = runtime.current;
    if (rt?.focusId && rt.focusId !== selected) {
      stopCamera();
      rt.focusId = null;
      rt.invalidate();
    } else if (trackingRef.current && followedId.current !== selected)
      stopCamera();
    if (!selected) setNotice("선택 해제 · 자유 시점");
  }, [selected]);
  useEffect(() => {
    if (trackingRef.current && !canTrack) {
      stopCamera();
      setNotice("따라가기를 멈췄습니다 · 실행부 연결과 실제 장면을 확인하세요");
    }
  }, [canTrack]);
  useEffect(() => {
    runtime.current?.invalidate();
  }, [showLabels]);
  return (
    <div className="map-view physics-view">
      <div className="physics-view__toolbar" aria-label="3D 시점">
        <FloorStackPicker
          floors={floors}
          elements={project?.environment.elements ?? []}
          currentId={floorId}
          robotFloorId={selectedFloorId}
          hoveredId={previewFloorId}
          open={floorPickerOpen}
          onOpen={openFloorPicker}
          onPreview={previewFloor}
          onCommit={commitFloor}
          onCancel={cancelFloorPicker}
        />
        <span className="physics-view__heading">3D 시점</span>
        <button
          disabled={!available}
          onClick={() => frameView("all")}
          title="현재 층 전체 형상 보기"
        >
          <Maximize2 size={14} />
          전체 보기
        </button>
        <button
          disabled={!historyCount || !!error}
          onClick={previousView}
          title="이동 전 카메라 위치와 층으로 돌아가기"
        >
          <History size={14} />
          이전 시점
        </button>
        <button disabled={!available} onClick={() => frameView("top")}>
          위
        </button>
        <button disabled={!available} onClick={() => frameView("front")}>
          앞
        </button>
        <button
          disabled={!canFocus}
          onClick={() => frameView("selected")}
          title={focusReason}
        >
          <Crosshair size={14} />
          선택 초점
        </button>
        <button
          disabled={!canTrack}
          aria-pressed={tracking}
          title={followReason}
          onClick={() => {
            if (tracking) {
              stopCamera();
              setNotice("따라가기 꺼짐 · 현재 시점 유지");
            } else focusEntity(selected, true);
          }}
        >
          <ScanEye size={14} />
          {tracking ? "따라가는 중" : "따라가기"}
        </button>
        <button
          aria-pressed={showLabels}
          onClick={() => setShowLabels((value) => !value)}
          aria-label="로봇·사람 이름 표시"
          title="로봇과 사람 위에 이름과 종류를 표시"
        >
          <Tags size={14} />
        </button>
        <button
          aria-pressed={showDiagnostics}
          title="사람의 실제 충돌체와 선택 경계를 화면에 겹쳐 표시"
          onClick={() => setShowDiagnostics((value) => !value)}
        >
          <Box size={14} />
          물리 진단
        </button>
        {selected && (
          <button
            onClick={() => onSelect("")}
            title="객체 선택 해제"
            aria-label="객체 선택 해제"
          >
            <X size={14} />
          </button>
        )}
      </div>
      <div
        className="physics-view__stage"
        ref={container}
        data-visible-floors={visibleFloorKey}
        onKeyDown={(event) => {
          if (event.key === "Escape") {
            event.preventDefault();
            stopCamera();
            if (runtime.current) runtime.current.focusId = null;
            onSelect("");
            runtime.current?.invalidate();
            return;
          }
          if (event.target !== runtime.current?.renderer.domElement) return;
          const actions: Record<string, () => void> = {
            ArrowLeft: () => nudge(-1, 0),
            ArrowRight: () => nudge(1, 0),
            ArrowUp: () => nudge(0, 1),
            ArrowDown: () => nudge(0, -1),
            "+": () => nudge(0, 0, 1),
            "=": () => nudge(0, 0, 1),
            "-": () => nudge(0, 0, -1),
            w: () => freeTravel(0, 1, 0),
            s: () => freeTravel(0, -1, 0),
            a: () => freeTravel(-1, 0, 0),
            d: () => freeTravel(1, 0, 0),
            q: () => freeTravel(0, 0, -1),
            e: () => freeTravel(0, 0, 1),
          };
          if (actions[event.key.toLowerCase()] || actions[event.key]) {
            event.preventDefault();
            (actions[event.key.toLowerCase()] ?? actions[event.key])();
          }
        }}
      >
        <div className="physics-view__camera" aria-label="카메라 조작">
          <div className="physics-view__modes">
            <button
              aria-pressed={mode === "rotate"}
              onClick={() => setMode("rotate")}
            >
              <RotateCw size={13} />
              회전
            </button>
            <button
              aria-pressed={mode === "pan"}
              onClick={() => setMode("pan")}
              title="드래그로 화면 이동 · W/A/S/D로 자유 이동 · Q/E로 높이 이동"
            >
              <Move size={13} />
              자유 이동
            </button>
          </div>
          <details className="physics-view__fine-controls">
            <summary>미세 조작</summary>
            <div className="physics-view__fine-content">
              <div className="physics-view__arrows">
                <button
                  disabled={!available}
                  aria-label={
                    mode === "pan" ? "카메라 왼쪽 이동" : "카메라 왼쪽 회전"
                  }
                  title="방향키 ←"
                  onClick={() => nudge(-1, 0)}
                >
                  <ArrowLeft size={15} />
                </button>
                <button
                  disabled={!available}
                  aria-label={
                    mode === "pan" ? "카메라 위로 이동" : "카메라 위로 회전"
                  }
                  title="방향키 ↑"
                  onClick={() => nudge(0, 1)}
                >
                  <ArrowUp size={15} />
                </button>
                <button
                  disabled={!available}
                  aria-label={
                    mode === "pan" ? "카메라 아래 이동" : "카메라 아래 회전"
                  }
                  title="방향키 ↓"
                  onClick={() => nudge(0, -1)}
                >
                  <ArrowDown size={15} />
                </button>
                <button
                  disabled={!available}
                  aria-label={
                    mode === "pan" ? "카메라 오른쪽 이동" : "카메라 오른쪽 회전"
                  }
                  title="방향키 →"
                  onClick={() => nudge(1, 0)}
                >
                  <ArrowRight size={15} />
                </button>
              </div>
              <p>
                장면을 누른 뒤 방향키·+/− 사용
                <br />
                드래그: 선택한 회전·이동 모드
                <br />
                오른쪽 드래그: 화면 이동
                <br />
                스크롤·두 손가락: 확대·축소
                <br />
                W/A/S/D: 자유 이동 · Q/E: 높이 이동
                <br />
                이름·형상 클릭: 선택하고 한 번 이동
                <br />
                Esc: 선택 해제
                <br />
                직접 조작: 이동 애니메이션·따라가기 중단
              </p>
            </div>
          </details>
          <button
            disabled={!available}
            aria-label="3D 축소"
            title="빼기 −"
            onClick={() => nudge(0, 0, -1)}
          >
            <Minus size={15} />
          </button>
          <button
            disabled={!available}
            aria-label="3D 확대"
            title="더하기 +"
            onClick={() => nudge(0, 0, 1)}
          >
            <Plus size={15} />
          </button>
        </div>
        <div className="physics-view__caption">
          <span>
            {rideContext
              ? `${rideContext.source.name} → ${rideContext.dest.name}`
              : previewFloorId
                ? `${displayFloor?.name ?? "층"} → ${floors.find((item) => item.id === previewFloorId)?.name ?? "층"}`
                : (displayFloor?.name ?? "층 선택 대기")}
          </span>
          <span>
            {showDiagnostics
              ? "물리 충돌체 진단 · Z축 위 / m"
              : "실행 장면 · Z축 위 / m"}
          </span>
        </div>
        {rideContext && (
          <div className="physics-view__trip-status" role="status">
            <strong>
              {rideContext.source.name}{" "}
              {rideContext.dest.elevation >= rideContext.source.elevation
                ? "↑"
                : "↓"}{" "}
              {rideContext.dest.name}
            </strong>
            <span>
              승강기 ·{" "}
              {(
                {
                  opening_board: "탑승 준비",
                  boarding: "탑승",
                  closing_depart: "출발 준비",
                  moving: "이동 중",
                  opening_exit: "도착",
                  alighting: "하차",
                } as Record<string, string>
              )[rideContext.phase] ?? rideContext.phase}
            </span>
          </div>
        )}
        {showLabels && !error && (
          <svg className="physics-view__label-lines" aria-hidden="true">
            {labelBodies.map((robot) => (
              <line
                key={robot.id}
                ref={(line) => {
                  if (line) labelLines.current.set(robot.id, line);
                  else labelLines.current.delete(robot.id);
                }}
                className={selected === robot.id ? "is-selected" : undefined}
                style={{ display: "none" }}
              />
            ))}
          </svg>
        )}
        {showLabels &&
          !error &&
          labelBodies.map((robot) => (
            <button
              key={robot.id}
              ref={(node) => {
                if (node) labelNodes.current.set(robot.id, node);
                else labelNodes.current.delete(robot.id);
              }}
              hidden
              className={`physics-view__robot-label${selected === robot.id ? " is-selected" : ""}`}
              data-model={robot.model_id}
              aria-pressed={selected === robot.id}
              aria-label={`${robot.name || robot.id} · ${modelNames[robot.model_id] ?? robot.model_id} 선택`}
              title={`${robot.name || robot.id} · ${modelNames[robot.model_id] ?? robot.model_id}`}
              onClick={() => {
                focusEntity(robot.id);
                onSelect(robot.id);
              }}
            >
              <span className="physics-view__robot-type">
                {modelTags[robot.model_id] ?? robot.model_id}
              </span>
              <span className="physics-view__robot-name">
                {robot.name || robot.id}
              </span>
            </button>
          ))}
        {humanDisplayFailure && (
          <div className="physics-view__human-error" role="status">
            사람 모델을 표시하지 못했습니다. 물리 진단에서 충돌체를 확인하거나
            3D 화면을 다시 열어주세요.
          </div>
        )}
        {showDiagnostics && !humanDisplayFailure && (
          <div className="physics-view__diagnostic-note">
            사람 외형: 관절 시각 모델 · 물리: 몸통 단일 충돌체
          </div>
        )}
        {connection !== "connected" && (
          <div className="physics-view__connection" role="status">
            {connection === "stale"
              ? `상태 수신 지연 · ${state ? "마지막 수신 장면" : "장면 수신 대기"}`
              : connection === "disconnected"
                ? `실행부 연결 끊김 · ${state ? "마지막 수신 장면" : "장면 수신 대기"}`
                : "실행부 연결 중"}
          </div>
        )}
        {selected && (
          <div className="physics-view__selection">
            <strong>{selectedName}</strong>
            {selectedRobot && (
              <span
                className={`physics-view__follow-status${tracking ? " is-active" : ""}`}
                role="status"
              >
                {tracking
                  ? "따라가기 켜짐"
                  : travelling
                    ? "시점 이동 중 · 따라가기 꺼짐"
                    : "따라가기 꺼짐 · 자유 시점"}
              </span>
            )}
            <span>
              {selectedEntity?.kind}
              {selectedRobot
                ? ` · ${connection === "connected" ? "" : "마지막 보고: "}${robotStatusLabel(selectedRobot.status)}`
                : ""}
            </span>
            <small>
              {hasSelection
                ? selectedPerson
                  ? "바닥 고리: 선택한 사람 · 실제 이동 방향 기준"
                  : `외곽선: 선택 형상${selectedRobot ? " · 화살표: 로봇 방향" : ""}`
                : focusReason}
            </small>
            {selectedRobot && hasSelection && !canTrack && (
              <small>{followReason}</small>
            )}
          </div>
        )}
        {!selected && available && (
          <div className="physics-view__selection-hint">
            로봇·사람의 이름이나 형상을 누르면 전방 사선으로 이동합니다
          </div>
        )}
        {(!state?.geoms.length || error || (!visibleCount && state)) && (
          <div className="physics-view__empty" role="status">
            <Box size={24} />
            <strong>
              {error
                ? "3D 화면 복구가 필요합니다"
                : !state
                  ? "현재 실행 장면을 기다립니다"
                  : !state.geoms.length
                    ? "아직 물리 형상이 없습니다"
                    : "현재 층에 표시할 물리 형상이 없습니다"}
            </strong>
            <p>
              {error ||
                (!state
                  ? "아직 수신한 실행 장면이 없습니다. 실행부 연결과 적용 상태를 확인하세요. 편집 초안은 2D 도면에서 확인할 수 있습니다."
                  : "상단에서 다른 층을 선택하거나 실행부 적용 상태를 확인하세요. 편집 초안은 2D 도면에서 확인할 수 있습니다.")}
            </p>
            {error && (
              <button onClick={() => setGeneration((value) => value + 1)}>
                <RotateCcw size={14} />
                3D 화면 다시 열기
              </button>
            )}
          </div>
        )}
      </div>
      <div className="physics-view__footer">
        <span>
          {selected && !hasSelection && !otherFloor
            ? focusReason
            : fadedCount > 0
              ? `벽·천장 ${fadedCount}개를 화면에서만 흐리게 표시${showLabels && hiddenLabelCount > 0 ? ` · 이름 ${hiddenLabelCount}개 숨김` : ""}`
              : showLabels && hiddenLabelCount > 0
                ? `겹치는 이름 ${hiddenLabelCount}개 숨김 · 목록이나 형상에서 선택하세요`
                : notice || "형상 표시와 실제 장비 검증은 별개입니다"}
        </span>
        <span>
          실장비 미검증 · {visibleCount}개 형상
          {missingCount > 0
            ? ` · 원본 형상 데이터 미표시 ${missingCount}개`
            : ""}
        </span>
      </div>
    </div>
  );
}
