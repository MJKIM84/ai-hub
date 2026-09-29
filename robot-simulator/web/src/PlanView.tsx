import {
  useEffect,
  useId,
  useLayoutEffect,
  useMemo,
  useRef,
  useState,
} from "react";
import type { KeyboardEvent, PointerEvent } from "react";
import {
  Crosshair,
  Expand,
  Hand,
  Minus,
  MousePointer2,
  Move,
  Plus,
  RotateCw,
} from "lucide-react";
import type {
  ElementKind,
  Pose,
  Project,
  RobotModel,
  RunState,
  Size,
} from "./types";
import { fitPlanBounds, floorAtGeometryBase, floorAtHeight } from "./spatial";
import { robotStatusLabel } from "./uiMessages";
import "./PlanView.css";

type Point = { x: number; y: number };
type Camera = Point & { height: number };
type Change = { id: string; pose?: Pose; size?: Size };
type Mode = "select" | "move" | "pan";
type MapObject = {
  id: string;
  name: string;
  pose: Pose;
  size: Size;
  type: "element" | "robot" | "person" | "item";
  kind: string;
  resizable: boolean;
  sourceText: string;
  status?: string;
  statusText?: string;
  glyph?: string;
  unavailable?: boolean;
  path?: Pose[];
};
type Bounds = { left: number; right: number; bottom: number; top: number };
type Gesture = {
  pointerId: number;
  context: string;
  project: Project | null;
  start: Point;
  screen: Point;
  screenInverse: DOMMatrix | null;
  moved: boolean;
  changes: Change[];
} & (
  | { kind: "pan"; camera: Camera }
  | { kind: "move"; objects: MapObject[] }
  | { kind: "rotate"; objects: MapObject[]; center: Point; angle: number }
  | { kind: "resize"; object: MapObject; corner: Point }
  | { kind: "marquee"; end: Point; original: string[] }
  | { kind: "place"; point: Point; tool: ElementKind }
);
const names: Record<ElementKind, string> = {
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
// Fallbacks mirror the authored research catalog; live catalog dimensions win.
const robotSizes: Record<string, Size> = {
  spot: { x: 1.1, y: 0.55, z: 0.65 },
  delivery: { x: 0.65, y: 0.5, z: 0.65 },
  amr: { x: 0.8, y: 0.65, z: 0.4 },
  agv: { x: 0.9, y: 0.65, z: 0.4 },
  logistics: { x: 1, y: 0.75, z: 0.55 },
  arm: { x: 0.7, y: 0.7, z: 1.3 },
  mobile_manipulator: { x: 0.85, y: 0.65, z: 1.4 },
};
const robotNames: Record<string, string> = {
  spot: "Spot",
  delivery: "배송",
  amr: "AMR",
  agv: "AGV",
  logistics: "운반",
  arm: "고정 팔",
  mobile_manipulator: "이동 팔",
};
const clamp = (n: number, lo: number, hi: number) =>
  Math.min(hi, Math.max(lo, n));
const rounded = (n: number) => Math.round(n * 1e6) / 1e6;
// Keep rulers and zoomed-out grids on familiar 1 / 2 / 5 metric intervals.
const metricStep = (minimum: number) => {
  const magnitude = 10 ** Math.floor(Math.log10(minimum));
  return (
    [1, 2, 5, 10].find((value) => value * magnitude >= minimum)! * magnitude
  );
};
const metricLabel = (value: number) =>
  value.toLocaleString("ko-KR", { maximumFractionDigits: 3 });
const rotate = (p: Point, a: number): Point => ({
  x: p.x * Math.cos(a) - p.y * Math.sin(a),
  y: p.x * Math.sin(a) + p.y * Math.cos(a),
});
const objectBounds = (o: MapObject): Bounds => {
  const c = Math.abs(Math.cos(o.pose.yaw)),
    s = Math.abs(Math.sin(o.pose.yaw));
  const x = (o.size.x * c + o.size.y * s) / 2,
    y = (o.size.x * s + o.size.y * c) / 2;
  return {
    left: o.pose.x - x,
    right: o.pose.x + x,
    bottom: o.pose.y - y,
    top: o.pose.y + y,
  };
};
const boundsOf = (objects: MapObject[]): Bounds => {
  const boxes = objects.map(objectBounds);
  return {
    left: Math.min(...boxes.map((b) => b.left)),
    right: Math.max(...boxes.map((b) => b.right)),
    bottom: Math.min(...boxes.map((b) => b.bottom)),
    top: Math.max(...boxes.map((b) => b.top)),
  };
};
// Marquee includes complete footprints, so a large room does not capture
// every selection made inside it. Its boundary remains directly selectable.
const contains = (a: Bounds, b: Bounds) =>
  a.left <= b.left &&
  a.right >= b.right &&
  a.bottom <= b.bottom &&
  a.top >= b.top;
const backgroundKinds = new Set([
  "room",
  "corridor",
  "loading",
  "waiting",
  "entrance",
  "restricted",
  "speed_zone",
  "one_way",
]);
const placementSize = (kind: ElementKind): Size => ({
  x: kind === "wall" ? 3 : kind === "room" ? 4 : 1.5,
  y: kind === "wall" ? 0.15 : kind === "room" ? 3 : 1.5,
  z: kind === "wall" ? 2 : kind === "room" ? 0.05 : 0.4,
});

function RobotSymbol({ kind, size }: { kind: string; size: Size }) {
  const w = size.x,
    h = size.y;
  const arm = (
    <>
      <circle cx={-w * 0.12} r={h * 0.22} />
      <path
        d={`M ${-w * 0.12} 0 L ${w * 0.06} ${-h * 0.2} L ${w * 0.3} ${h * 0.02}`}
      />
      <circle cx={w * 0.06} cy={-h * 0.2} r={h * 0.07} />
      <path
        d={`M ${w * 0.36} ${-h * 0.1} H ${w * 0.26} V ${h * 0.13} H ${w * 0.36}`}
      />
    </>
  );
  return (
    <g className={`plan-robot-symbol model-${kind}`}>
      {kind === "spot" ? (
        <>
          <path
            className="plan-symbol-detail"
            d={`M ${-w * 0.27} ${-h * 0.18} L ${-w * 0.42} ${-h * 0.5} M ${w * 0.23} ${-h * 0.18} L ${w * 0.39} ${-h * 0.5} M ${-w * 0.27} ${h * 0.18} L ${-w * 0.42} ${h * 0.5} M ${w * 0.23} ${h * 0.18} L ${w * 0.39} ${h * 0.5}`}
          />
          <rect
            x={-w * 0.4}
            y={-h * 0.29}
            width={w * 0.75}
            height={h * 0.58}
            rx={h * 0.13}
          />
          <path
            d={`M ${w * 0.34} ${-h * 0.2} L ${w * 0.5} ${-h * 0.14} L ${w * 0.5} ${h * 0.14} L ${w * 0.34} ${h * 0.2} Z`}
          />
        </>
      ) : kind === "arm" ? (
        <>
          <circle r={w * 0.47} />
          {arm}
        </>
      ) : (
        <>
          <rect
            x={-w / 2}
            y={-h / 2}
            width={w}
            height={h}
            rx={kind === "agv" ? 0 : h * 0.14}
          />
          <path
            className="plan-wheel"
            d={`M ${-w * 0.25} ${-h * 0.52} H ${w * 0.2} M ${-w * 0.25} ${h * 0.52} H ${w * 0.2}`}
          />
          {kind === "mobile_manipulator" ? (
            arm
          ) : kind === "delivery" ? (
            <>
              <rect
                x={-w * 0.3}
                y={-h * 0.3}
                width={w * 0.48}
                height={h * 0.6}
                rx={h * 0.06}
              />
              <path d={`M ${-w * 0.05} ${-h * 0.28} V ${h * 0.28}`} />
            </>
          ) : kind === "agv" ? (
            <>
              <path
                d={`M ${-w * 0.38} 0 H ${w * 0.34} M ${w * 0.05} ${-h * 0.17} L ${w * 0.25} 0 L ${w * 0.05} ${h * 0.17}`}
              />
              <path
                className="plan-guide"
                d={`M ${-w * 0.65} 0 H ${w * 0.65}`}
              />
            </>
          ) : kind === "logistics" ? (
            <>
              <rect
                x={-w * 0.36}
                y={-h * 0.34}
                width={w * 0.6}
                height={h * 0.68}
              />
              <path
                d={`M ${-w * 0.16} ${-h * 0.32} V ${h * 0.32} M ${w * 0.04} ${-h * 0.32} V ${h * 0.32}`}
              />
            </>
          ) : (
            <>
              <path
                d={`M ${-w * 0.22} 0 L 0 ${-h * 0.28} L ${w * 0.22} 0 L 0 ${h * 0.28} Z`}
              />
              <circle cx={w * 0.35} r={h * 0.07} />
            </>
          )}
        </>
      )}
      <path
        className="plan-heading"
        d={`M ${w / 2 + 0.05} -.075 L ${w / 2 + 0.18} 0 L ${w / 2 + 0.05} .075 Z`}
      />
    </g>
  );
}

export function PlanView({
  project,
  state,
  floorId,
  selected,
  onSelect,
  tool,
  onPlace,
  onMove,
  editing,
  selectedIds,
  onSelectionChange,
  onTransform,
  snap = true,
  models,
  onCancelTool,
  planningPreview = false,
  previewRoutes = [],
}: {
  project: Project | null;
  state: RunState | null;
  floorId: string;
  selected: string;
  onSelect: (id: string) => void;
  tool: ElementKind | null;
  onPlace: (kind: ElementKind, x: number, y: number) => void;
  onMove: (id: string, pose: Pose) => void;
  editing: boolean;
  selectedIds?: string[];
  onSelectionChange?: (ids: string[]) => void;
  onTransform?: (changes: Change[]) => void;
  snap?: boolean;
  models?: RobotModel[];
  onCancelTool?: () => void;
  planningPreview?: boolean;
  previewRoutes?: { task_id: string; floor_id: string; points: Pose[] }[];
}) {
  const host = useRef<HTMLDivElement>(null),
    svg = useRef<SVGSVGElement>(null);
  const toolsOverlay = useRef<HTMLDivElement>(null),
    sourceOverlay = useRef<HTMLDivElement>(null),
    placementOverlay = useRef<HTMLButtonElement>(null),
    footerOverlay = useRef<HTMLDivElement>(null),
    gridOverlay = useRef<HTMLSpanElement>(null),
    helpOverlay = useRef<HTMLDivElement>(null);
  const gesture = useRef<Gesture | null>(null),
    spaceHeld = useRef(false),
    autoFit = useRef(true);
  const id = useId().replace(/:/g, "");
  const floor = project?.environment.floors.find((f) => f.id === floorId),
    w = floor?.width ?? 20,
    h = floor?.depth ?? 14;
  const [viewport, setViewport] = useState({ width: 800, height: 560 });
  const [fitInsets, setFitInsets] = useState({
    left: 36,
    right: 52,
    top: 76,
    bottom: 84,
  });
  const [camera, setCamera] = useState<Camera>({
    x: w / 2,
    y: h / 2,
    height: h + 2,
  });
  const [mode, setMode] = useState<Mode>("pan"),
    [preview, setPreview] = useState<Change[]>([]);
  const [marquee, setMarquee] = useState<Bounds | null>(null),
    [cursor, setCursor] = useState<Point | null>(null);
  const [localSelection, setLocalSelection] = useState<string[]>(
    selected ? [selected] : [],
  );
  const [toolSuspended, setToolSuspended] = useState(false),
    [panning, setPanning] = useState(false),
    [announcement, setAnnouncement] = useState("");
  const aspect = viewport.width / Math.max(1, viewport.height),
    viewWidth = camera.height * aspect,
    pixelsPerMeter = viewport.height / camera.height;
  const fittedCamera = useMemo(
    () =>
      fitPlanBounds(
        { left: 0, right: w, bottom: 0, top: h },
        viewport,
        fitInsets,
      ),
    [w, h, viewport, fitInsets],
  );
  const fitHeight = fittedCamera.height;
  const context = `${project?.id ?? ""}/${floorId}/${state?.run_id ?? ""}/${editing}`;
  const currentContext = useRef(context);
  currentContext.current = context;
  const activeTool = editing && !toolSuspended ? tool : null,
    ids = selectedIds ?? localSelection;
  const selectedSet = useMemo(() => new Set(ids), [ids]);
  const objects = useMemo<MapObject[]>(() => {
    if (!project) return [];
    const observed = new Map(state?.robots.map((r) => [r.id, r])),
      geometry = new Map(state?.geoms.map((g) => [g.name, g])),
      modelLookup = new Map(models?.map((m) => [m.id, m.size]));
    // Floor routing is a physical display concern. It must not turn truth
    // coordinates into a robot's observed XY position or control evidence.
    const geometryFloor = (
      entity: { id: string; floor_id: string },
      name: string,
      centerOffset: number,
    ) => {
      return floorAtGeometryBase(
        project.environment.floors,
        geometry.get(`${entity.id}/${name}`),
        centerOffset,
        entity.floor_id,
      );
    };
    const position = (entity: { id: string; pose: Pose }, name: string) => {
      const g = !editing ? geometry.get(`${entity.id}/${name}`) : null;
      if (!g)
        return {
          pose: entity.pose,
          sourceText: planningPreview
            ? "계획 초기 배치"
            : editing
              ? "초안"
              : "기준 배치 · 물리 미수신",
          unavailable: !editing && !planningPreview,
        };
      const [qw, qx, qy, qz] = g.quaternion;
      return {
        sourceText: "물리 표시",
        unavailable: false,
        pose: {
          ...entity.pose,
          x: g.position[0],
          y: g.position[1],
          yaw: Math.atan2(2 * (qw * qz + qx * qy), 1 - 2 * (qy * qy + qz * qz)),
        },
      };
    };
    return [
      ...project.environment.elements
        .filter(
          (e) =>
            (editing || !e.dynamic
              ? e.floor_id
              : geometryFloor(e, "shape", e.size.z / 2)) === floorId,
        )
        .map((e) => ({
          ...e,
          type: "element" as const,
          resizable: true,
          ...(e.dynamic
            ? position(e, "shape")
            : { sourceText: editing ? "초안" : "구성 도면" }),
        })),
      ...project.robots
        .filter(
          (r) =>
            (editing
              ? r.floor_id
              : floorAtHeight(
                  project.environment.floors,
                  observed.get(r.id)?.pose.z,
                  r.floor_id,
                )) === floorId,
        )
        .map((r) => {
          const live = !editing ? observed.get(r.id) : undefined,
            unavailable = !editing && !planningPreview && !live?.observed_pose;
          const stale =
            !editing &&
            live?.observation_age != null &&
            live.observation_age > project.policy.stale_after;
          const status = planningPreview
            ? "draft"
            : unavailable
              ? "unknown"
              : stale
                ? "stale"
                : !editing
                  ? (live?.status ?? "unknown")
                  : "draft";
          const failed = ["failed", "fault", "recovery_required"].includes(
              status,
            ),
            waiting = ["waiting", "blocked", "stopped", "paused"].includes(
              status,
            );
          const statusText = planningPreview
            ? "계획 초기 배치"
            : unavailable
              ? "미관측"
              : robotStatusLabel(status);
          return {
            id: r.id,
            name: r.name,
            type: "robot" as const,
            kind: r.model_id,
            pose: live?.observed_pose ?? r.pose,
            size:
              modelLookup.get(r.model_id) ??
              robotSizes[r.model_id] ??
              robotSizes.amr,
            resizable: false,
            sourceText: planningPreview
              ? "계획 초기 배치"
              : editing
                ? "초안"
                : unavailable
                  ? "기준 배치 · 관측 미수신"
                  : "관측 보고",
            status,
            statusText,
            glyph: unavailable
              ? "?"
              : stale ||
                  failed ||
                  ["disconnected", "transit_recovery"].includes(status)
                ? "!"
                : waiting
                  ? "Ⅱ"
                  : status === "charging"
                    ? "+"
                    : status === "idle" || status === "draft"
                      ? "·"
                      : [
                            "working",
                            "manipulating",
                            "manual",
                            "recovering",
                          ].includes(status)
                        ? "→"
                        : "?",
            unavailable,
            path: live?.observed_pose ? live.path : undefined,
          };
        }),
      ...project.people
        // The authored torso's center is .85m above its supporting floor.
        .filter(
          (p) =>
            (editing ? p.floor_id : geometryFloor(p, "torso", 0.85)) ===
            floorId,
        )
        .map((p) => ({
          id: p.id,
          name: p.name,
          ...position(p, "torso"),
          size: { x: 0.44, y: 0.44, z: 1.7 },
          type: "person" as const,
          kind: "person",
          resizable: false,
        })),
      ...project.items
        .filter(
          (i) =>
            (editing ? i.floor_id : geometryFloor(i, "shape", i.size.z / 2)) ===
            floorId,
        )
        .map((i) => ({
          ...i,
          ...position(i, "shape"),
          type: "item" as const,
          kind: "item",
          resizable: true,
        })),
    ];
  }, [project, state, floorId, editing, models, planningPreview]);
  const displayed = useMemo(() => {
    const changes = new Map(preview.map((p) => [p.id, p]));
    return objects.map((o) => ({ ...o, ...changes.get(o.id) }));
  }, [objects, preview]);
  // Transparent zones remain clickable without covering robots or physical
  // facilities. Larger zones go behind smaller overlapping zones.
  const paintedObjects = useMemo(
    () =>
      [...displayed].sort((a, b) => {
        const aZone = a.type === "element" && backgroundKinds.has(a.kind);
        const bZone = b.type === "element" && backgroundKinds.has(b.kind);
        return (
          Number(bZone) - Number(aZone) ||
          (aZone && bZone ? b.size.x * b.size.y - a.size.x * a.size.y : 0)
        );
      }),
    [displayed],
  );
  const selectedObjects = displayed.filter((o) => selectedSet.has(o.id)),
    selectionBounds = selectedObjects.length ? boundsOf(selectedObjects) : null;
  const selectedGuideRobot =
    editing && !tool && ids.length === 1
      ? project?.robots.find(
          (robot) =>
            robot.id === ids[0] &&
            robot.model_id === "agv" &&
            robot.floor_id === floorId,
        )
      : undefined;
  // Draw authored segments exactly as entered, including an explicit closing point.
  // A malformed point must never be dropped to invent a connection between its neighbors.
  const selectedGuide = selectedGuideRobot?.agv_route ?? [];
  const guideDrawable =
    selectedGuide.length > 0 &&
    selectedGuide.every(
      (point) => Number.isFinite(point.x) && Number.isFinite(point.y),
    );
  const guideNodes = useMemo(() => {
    const nodes = new Map<string, { point: Pose; numbers: number[] }>();
    selectedGuide.forEach((point, index) => {
      const key = `${point.x}/${point.y}`;
      const node = nodes.get(key);
      if (node) node.numbers.push(index + 1);
      else nodes.set(key, { point, numbers: [index + 1] });
    });
    return [...nodes.values()];
  }, [selectedGuide]);
  const guideNumbersReadable = guideNodes.every((node, index) =>
    guideNodes
      .slice(index + 1)
      .every(
        (other) =>
          Math.hypot(
            node.point.x - other.point.x,
            node.point.y - other.point.y,
          ) *
            pixelsPerMeter >=
          24,
      ),
  );
  const cancel = () => {
    const old = gesture.current;
    gesture.current = null;
    if (old && svg.current?.hasPointerCapture(old.pointerId))
      svg.current.releasePointerCapture(old.pointerId);
    setPreview([]);
    setMarquee(null);
    setPanning(false);
  };
  useLayoutEffect(() => {
    const element = host.current;
    if (!element) return;
    const upper = [
      toolsOverlay.current,
      sourceOverlay.current,
      placementOverlay.current,
    ];
    const lower = [
      footerOverlay.current,
      gridOverlay.current,
      helpOverlay.current,
    ];
    const measure = () => {
      const rect = element.getBoundingClientRect();
      if (rect.width <= 0 || rect.height <= 0) return;
      setViewport((old) =>
        old.width === rect.width && old.height === rect.height
          ? old
          : { width: rect.width, height: rect.height },
      );
      const top = Math.max(
        0,
        ...upper
          .filter((node) => node !== null)
          .map((node) => node.getBoundingClientRect().bottom - rect.top),
      );
      const bottom = Math.max(
        0,
        ...lower
          .filter((node) => node !== null)
          .map((node) => rect.bottom - node.getBoundingClientRect().top),
      );
      // Axis text extends beyond the floor boundary, so reserve its screen-pixel
      // space in addition to the measured, possibly wrapped floating controls.
      const next = {
        left: 36,
        right: 52,
        top: Math.ceil(top + 24),
        bottom: Math.ceil(bottom + 28),
      };
      setFitInsets((old) =>
        old.top === next.top && old.bottom === next.bottom ? old : next,
      );
    };
    const observer = new ResizeObserver(measure);
    [element, ...upper, ...lower].forEach((node) => {
      if (node) observer.observe(node);
    });
    measure();
    return () => observer.disconnect();
  }, [editing, tool, selectedGuideRobot?.id]);
  useEffect(() => {
    autoFit.current = true;
    cancel();
    setCursor(null);
    spaceHeld.current = false;
  }, [context]);
  useEffect(() => {
    if (autoFit.current && !gesture.current) setCamera(fittedCamera);
  }, [fittedCamera, context]);
  useEffect(() => {
    cancel();
  }, [project, tool]);
  useEffect(() => {
    setToolSuspended(false);
  }, [tool]);
  useEffect(() => {
    if (!selectedIds)
      setLocalSelection((old) =>
        selected ? (old.includes(selected) ? old : [selected]) : [],
      );
  }, [selected, selectedIds]);
  useEffect(() => {
    const blur = () => {
      spaceHeld.current = false;
      cancel();
    };
    window.addEventListener("blur", blur);
    return () => window.removeEventListener("blur", blur);
  }, []);
  const select = (next: string[]) => {
    const valid = [...new Set(next)].filter((value) =>
      objects.some((o) => o.id === value),
    );
    setLocalSelection(valid);
    if (onSelectionChange) onSelectionChange(valid);
    else onSelect(valid.at(-1) ?? "");
  };
  const fit = () => {
    cancel();
    autoFit.current = true;
    setCamera(fittedCamera);
  };
  const focusSelection = () => {
    if (!selectionBounds) return;
    cancel();
    autoFit.current = false;
    const b = selectionBounds,
      center = { x: (b.left + b.right) / 2, y: (b.top + b.bottom) / 2 },
      halfWidth = Math.max(1.5, (b.right - b.left) * 0.7),
      halfHeight = Math.max(1.5, (b.top - b.bottom) * 0.7);
    setCamera(
      fitPlanBounds(
        {
          left: center.x - halfWidth,
          right: center.x + halfWidth,
          bottom: center.y - halfHeight,
          top: center.y + halfHeight,
        },
        viewport,
        fitInsets,
      ),
    );
  };
  const focusGuide = () => {
    if (!guideDrawable) return;
    cancel();
    autoFit.current = false;
    setCamera(
      fitPlanBounds(
        {
          left: Math.min(...selectedGuide.map((point) => point.x)) - 1,
          right: Math.max(...selectedGuide.map((point) => point.x)) + 1,
          bottom: Math.min(...selectedGuide.map((point) => point.y)) - 1,
          top: Math.max(...selectedGuide.map((point) => point.y)) + 1,
        },
        viewport,
        fitInsets,
      ),
    );
  };
  const at = (
    clientX: number,
    clientY: number,
    inverse?: DOMMatrix | null,
  ): Point => {
    const matrix = inverse ?? svg.current?.getScreenCTM()?.inverse();
    if (!matrix) return { x: 0, y: 0 };
    const p = new DOMPoint(clientX, clientY).matrixTransform(matrix);
    return { x: p.x, y: -p.y };
  };
  const snapPoint = (p: Point): Point => ({
    x: clamp(snap ? Math.round(p.x * 4) / 4 : rounded(p.x), 0, w),
    y: clamp(snap ? Math.round(p.y * 4) / 4 : rounded(p.y), 0, h),
  });
  const zoom = (factor: number, anchor?: Point) => {
    autoFit.current = false;
    setCamera((old) => {
      const height = clamp(old.height * factor, 1.5, Math.max(w, h) * 4),
        p = anchor ?? old,
        ratio = height / old.height;
      return {
        x: p.x + (old.x - p.x) * ratio,
        y: p.y + (old.y - p.y) * ratio,
        height,
      };
    });
  };
  const wheelHandler = useRef<(e: WheelEvent) => void>(() => {});
  wheelHandler.current = (e) => {
    e.preventDefault();
    if (!gesture.current)
      zoom(
        Math.exp(clamp(e.deltaY, -120, 120) * 0.0025),
        at(e.clientX, e.clientY),
      );
  };
  useEffect(() => {
    const element = svg.current,
      listener = (event: WheelEvent) => wheelHandler.current(event);
    element?.addEventListener("wheel", listener, { passive: false });
    return () => element?.removeEventListener("wheel", listener);
  }, []);
  const setEditorMode = (next: Mode) => {
    cancel();
    setMode(next);
    setToolSuspended(true);
    onCancelTool?.();
  };
  const baseGesture = (e: PointerEvent<SVGElement>) => ({
    pointerId: e.pointerId,
    context,
    project,
    start: at(e.clientX, e.clientY),
    screen: { x: e.clientX, y: e.clientY },
    screenInverse: svg.current?.getScreenCTM()?.inverse() ?? null,
    moved: false,
    changes: [],
  });
  const capture = (e: PointerEvent<SVGElement>, next: Gesture) => {
    e.preventDefault();
    e.stopPropagation();
    // Selection reveals its information strip. That layout change must not
    // auto-fit the camera halfway through a pointer drag.
    autoFit.current = false;
    gesture.current = next;
    svg.current?.setPointerCapture(e.pointerId);
    svg.current?.focus({ preventScroll: true });
  };
  const startPan = (e: PointerEvent<SVGElement>) => {
    capture(e, { ...baseGesture(e), kind: "pan", camera });
    setPanning(true);
    autoFit.current = false;
  };
  const backgroundDown = (e: PointerEvent<SVGElement>) => {
    if (gesture.current || (e.button !== 0 && e.button !== 1)) return;
    if (e.button === 1 || spaceHeld.current || (mode === "pan" && !activeTool)) {
      startPan(e);
      return;
    }
    if (activeTool && floor) {
      const p = snapPoint(at(e.clientX, e.clientY));
      capture(e, {
        ...baseGesture(e),
        kind: "place",
        point: p,
        tool: activeTool,
      });
      return;
    }
    const start = at(e.clientX, e.clientY);
    capture(e, {
      ...baseGesture(e),
      kind: "marquee",
      end: start,
      original: e.shiftKey ? ids : [],
    });
  };
  const objectDown = (e: PointerEvent<SVGGElement>, object: MapObject) => {
    if (gesture.current) return;
    if (e.button === 1 || spaceHeld.current || (mode === "pan" && !activeTool)) {
      startPan(e);
      return;
    }
    if (e.button !== 0 || gesture.current) return;
    if (activeTool) {
      backgroundDown(e);
      return;
    }
    e.stopPropagation();
    if (e.shiftKey) {
      select(
        selectedSet.has(object.id)
          ? ids.filter((id) => id !== object.id)
          : [...ids, object.id],
      );
      return;
    }
    const nextIds = selectedSet.has(object.id) ? ids : [object.id];
    select(nextIds);
    if (!editing || mode === "select") return;
    const moving = objects.filter((o) => nextIds.includes(o.id));
    if (moving.length > 1 && !onTransform) {
      setAnnouncement(
        "여러 객체의 이동은 일괄 편집 연결 후 사용할 수 있습니다.",
      );
      return;
    }
    capture(e, {
      ...baseGesture(e),
      kind: "move",
      objects: [object, ...moving.filter((o) => o.id !== object.id)],
    });
  };
  const commit = (changes: Change[]) => {
    changes = changes.filter((change) => {
      const original = objects.find((o) => o.id === change.id);
      return (
        original &&
        ((change.pose &&
          (["x", "y", "z", "yaw"] as const).some(
            (key) => change.pose![key] !== original.pose[key],
          )) ||
          (change.size &&
            (["x", "y", "z"] as const).some(
              (key) => change.size![key] !== original.size[key],
            )))
      );
    });
    if (!editing || !changes.length) return;
    if (onTransform) onTransform(changes);
    else if (changes.length === 1 && changes[0].pose && !changes[0].size)
      onMove(changes[0].id, changes[0].pose);
    setAnnouncement(`${changes.length}개 객체 변경을 초안에 반영했습니다.`);
  };
  const moveChanges = (moving: MapObject[], delta: Point): Change[] => {
    const x = clamp(
        delta.x,
        -Math.min(...moving.map((o) => o.pose.x)),
        w - Math.max(...moving.map((o) => o.pose.x)),
      ),
      y = clamp(
        delta.y,
        -Math.min(...moving.map((o) => o.pose.y)),
        h - Math.max(...moving.map((o) => o.pose.y)),
      );
    return moving.map((o) => ({
      id: o.id,
      pose: { ...o.pose, x: rounded(o.pose.x + x), y: rounded(o.pose.y + y) },
    }));
  };
  const nudgeChanges = (
    moving: MapObject[],
    key: string,
    fast: boolean,
  ): Change[] => {
    const origin = (moving.find((o) => o.id === selected) ?? moving[0]).pose;
    const step = fast ? 1 : snap ? 0.25 : 0.05;
    const delta = {
      x: key === "ArrowLeft" ? -step : key === "ArrowRight" ? step : 0,
      y: key === "ArrowDown" ? -step : key === "ArrowUp" ? step : 0,
    };
    // Only the requested axis snaps; relative offsets of a group stay intact.
    const target = snapPoint({ x: origin.x + delta.x, y: origin.y + delta.y });
    return moveChanges(moving, {
      x: delta.x ? target.x - origin.x : 0,
      y: delta.y ? target.y - origin.y : 0,
    });
  };
  const rotationChanges = (
    moving: MapObject[],
    center: Point,
    delta: number,
  ): Change[] =>
    moving.map((o) => {
      const shifted = rotate(
          { x: o.pose.x - center.x, y: o.pose.y - center.y },
          delta,
        ),
        yaw = o.pose.yaw + delta;
      return {
        id: o.id,
        pose: {
          ...o.pose,
          x: rounded(center.x + shifted.x),
          y: rounded(center.y + shifted.y),
          yaw: Math.atan2(Math.sin(yaw), Math.cos(yaw)),
        },
      };
    });
  const updateGesture = (e: PointerEvent<SVGSVGElement>) => {
    const g = gesture.current;
    const point = at(e.clientX, e.clientY, g?.screenInverse);
    setCursor(activeTool ? snapPoint(point) : point);
    if (!g || g.pointerId !== e.pointerId) return;
    if (
      g.context !== context ||
      g.project !== project ||
      (!editing && ["move", "resize", "rotate", "place"].includes(g.kind))
    ) {
      cancel();
      return;
    }
    g.moved ||= Math.hypot(e.clientX - g.screen.x, e.clientY - g.screen.y) > 3;
    if (g.kind === "pan") {
      setCamera({
        ...g.camera,
        x: g.camera.x - (point.x - g.start.x),
        y: g.camera.y - (point.y - g.start.y),
      });
      return;
    }
    if (g.kind === "marquee") {
      g.end = point;
      if (g.moved)
        setMarquee({
          left: Math.min(g.start.x, point.x),
          right: Math.max(g.start.x, point.x),
          bottom: Math.min(g.start.y, point.y),
          top: Math.max(g.start.y, point.y),
        });
      return;
    }
    if (g.kind === "place") {
      g.point = snapPoint(point);
      return;
    }
    if (!g.moved) return;
    if (g.kind === "move") {
      const origin = g.objects[0].pose,
        snapped = snapPoint({
          x: origin.x + point.x - g.start.x,
          y: origin.y + point.y - g.start.y,
        });
      g.changes = moveChanges(g.objects, {
        x: snapped.x - origin.x,
        y: snapped.y - origin.y,
      });
    } else if (g.kind === "rotate") {
      let angle =
        Math.atan2(point.y - g.center.y, point.x - g.center.x) - g.angle;
      if (snap) angle = (Math.round(angle / (Math.PI / 12)) * Math.PI) / 12;
      g.changes = rotationChanges(g.objects, g.center, angle);
    } else {
      const o = g.object,
        d = g.corner,
        opposite = rotate(
          { x: (-d.x * o.size.x) / 2, y: (-d.y * o.size.y) / 2 },
          o.pose.yaw,
        ),
        anchor = { x: o.pose.x + opposite.x, y: o.pose.y + opposite.y };
      const local = rotate(
        { x: point.x - anchor.x, y: point.y - anchor.y },
        -o.pose.yaw,
      );
      const size = {
        ...o.size,
        x: Math.max(
          snap ? 0.25 : 0.1,
          snap ? Math.round(local.x * d.x * 4) / 4 : rounded(local.x * d.x),
        ),
        y: Math.max(
          snap ? 0.25 : 0.1,
          snap ? Math.round(local.y * d.y * 4) / 4 : rounded(local.y * d.y),
        ),
      };
      const center = rotate(
        { x: (d.x * size.x) / 2, y: (d.y * size.y) / 2 },
        o.pose.yaw,
      );
      g.changes = [
        {
          id: o.id,
          size,
          pose: {
            ...o.pose,
            x: rounded(anchor.x + center.x),
            y: rounded(anchor.y + center.y),
          },
        },
      ];
    }
    setPreview(g.changes);
  };
  const endGesture = (e: PointerEvent<SVGSVGElement>) => {
    updateGesture(e);
    const g = gesture.current;
    if (!g || g.pointerId !== e.pointerId) return;
    if (g.kind === "marquee") {
      const box = {
        left: Math.min(g.start.x, g.end.x),
        right: Math.max(g.start.x, g.end.x),
        bottom: Math.min(g.start.y, g.end.y),
        top: Math.max(g.start.y, g.end.y),
      };
      select(
        g.moved
          ? [
              ...g.original,
              ...objects
                .filter((o) => contains(box, objectBounds(o)))
                .map((o) => o.id),
            ]
          : g.original,
      );
    } else if (
      g.context === currentContext.current &&
      g.project === project &&
      editing
    ) {
      if (g.kind === "place" && !g.moved) onPlace(g.tool, g.point.x, g.point.y);
      else if (g.moved && g.changes.length)
        commit(
          g.changes.filter((change) => {
            const old = objects.find((o) => o.id === change.id);
            return (
              old &&
              ((change.size &&
                (change.size.x !== old.size.x ||
                  change.size.y !== old.size.y)) ||
                (change.pose &&
                  (change.pose.x !== old.pose.x ||
                    change.pose.y !== old.pose.y ||
                    change.pose.yaw !== old.pose.yaw)))
            );
          }),
        );
    }
    cancel();
  };
  const beginHandle = (
    e: PointerEvent<SVGElement>,
    kind: "resize" | "rotate",
    corner?: Point,
  ) => {
    if (gesture.current) return;
    if (spaceHeld.current || e.button === 1) {
      startPan(e);
      return;
    }
    if (!editing || !onTransform || !selectedObjects.length || e.button !== 0)
      return;
    if (kind === "resize" && corner)
      capture(e, {
        ...baseGesture(e),
        kind,
        object: selectedObjects[0],
        corner,
      });
    else {
      const b = boundsOf(selectedObjects),
        center =
          selectedObjects.length === 1
            ? selectedObjects[0].pose
            : { x: (b.left + b.right) / 2, y: (b.top + b.bottom) / 2 },
        p = at(e.clientX, e.clientY);
      capture(e, {
        ...baseGesture(e),
        kind: "rotate",
        objects: selectedObjects,
        center,
        angle: Math.atan2(p.y - center.y, p.x - center.x),
      });
    }
  };
  const keyDown = (event: KeyboardEvent<SVGSVGElement>) => {
    if (event.key === "Escape") {
      cancel();
      setToolSuspended(true);
      onCancelTool?.();
      setAnnouncement("진행 중인 조작을 취소했습니다.");
      return;
    }
    if (event.key === " " && event.target === event.currentTarget) {
      event.preventDefault();
      spaceHeld.current = true;
      return;
    }
    if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "a") {
      event.preventDefault();
      cancel();
      select(objects.map((o) => o.id));
      return;
    }
    if (event.ctrlKey || event.metaKey || event.altKey) return;
    if (event.key === "+" || event.key === "=") {
      event.preventDefault();
      zoom(0.8);
    } else if (event.key === "-") {
      event.preventDefault();
      zoom(1.25);
    } else if (event.key === "0") {
      event.preventDefault();
      fit();
    } else if (event.key.toLowerCase() === "f") {
      event.preventDefault();
      focusSelection();
    } else if (event.key.toLowerCase() === "v") setEditorMode("select");
    else if (event.key.toLowerCase() === "m" && editing) setEditorMode("move");
    else if (event.key.toLowerCase() === "h") setEditorMode("pan");
    else if (
      editing &&
      !activeTool &&
      !gesture.current &&
      selectedObjects.length &&
      (!!onTransform || selectedObjects.length < 2) &&
      ["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown"].includes(event.key)
    ) {
      event.preventDefault();
      commit(nudgeChanges(selectedObjects, event.key, event.shiftKey));
    }
  };
  const labelLayout = useMemo(() => {
    const occupied: { x: number; y: number; width: number; height: number }[] =
      [];
    const result: {
      object: MapObject;
      x: number;
      y: number;
      text: string;
      detail: string | null;
      font: number;
      width: number;
      height: number;
    }[] = [];
    const ordered = [...displayed].sort(
      (a, b) =>
        Number(selectedSet.has(b.id)) - Number(selectedSet.has(a.id)) ||
        Number(a.type === "element") - Number(b.type === "element"),
    );
    for (const o of ordered) {
      const chosen = selectedSet.has(o.id),
        bounds = objectBounds(o),
        screen = {
          x: (o.pose.x - camera.x) * pixelsPerMeter + viewport.width / 2,
          y: (camera.y - o.pose.y) * pixelsPerMeter + viewport.height / 2,
        };
      if (
        screen.x < -100 ||
        screen.x > viewport.width + 100 ||
        screen.y < -100 ||
        screen.y > viewport.height + 100
      )
        continue;
      if (
        !chosen &&
        o.type === "element" &&
        Math.min(o.size.x, o.size.y) * pixelsPerMeter < 28
      )
        continue;
      if (!chosen && pixelsPerMeter < 15 && o.type !== "robot") continue;
      const font = chosen ? 13 : 11.5,
        text = o.name.length > 24 ? o.name.slice(0, 23) + "…" : o.name;
      const detail = o.unavailable
        ? o.sourceText
        : chosen
          ? o.type === "robot"
            ? [
                ...new Set(
                  [
                    robotNames[o.kind] ?? o.kind,
                    o.statusText,
                    o.sourceText,
                  ].filter(Boolean),
                ),
              ].join(" · ")
            : `${o.size.x.toFixed(2)} × ${o.size.y.toFixed(2)} m · ${((o.pose.yaw * 180) / Math.PI).toFixed(0)}°${editing ? "" : ` · ${o.sourceText}`}`
          : o.type === "robot" && pixelsPerMeter > 26
            ? `${robotNames[o.kind] ?? o.kind} · ${o.statusText}`
            : null;
      const measure = (value: string) =>
        [...value].reduce(
          (total, char) =>
            total + (char.charCodeAt(0) > 255 ? font : font * 0.58),
          0,
        );
      const width =
          Math.max(measure(text), detail ? measure(detail) * 0.87 : 0) + 12,
        height = detail ? 36 : 23,
        halfH = ((bounds.top - bounds.bottom) * pixelsPerMeter) / 2,
        halfW = ((bounds.right - bounds.left) * pixelsPerMeter) / 2;
      const options = [
        { x: screen.x - width / 2, y: screen.y + halfH + 7 },
        { x: screen.x - width / 2, y: screen.y - halfH - height - 7 },
        { x: screen.x + halfW + 8, y: screen.y - height / 2 },
        { x: screen.x - halfW - width - 8, y: screen.y - height / 2 },
        ...Array.from({ length: chosen ? 12 : 3 }, (_, i) => ({
          x: screen.x + halfW + 10,
          y: screen.y + (i + 1) * (height + 3),
        })),
      ];
      const candidate = options.find(
        (p) =>
          p.x > 4 &&
          p.x + width < viewport.width - 4 &&
          p.y > fitInsets.top - 12 &&
          p.y + height < viewport.height - fitInsets.bottom + 12 &&
          !occupied.some(
            (b) =>
              p.x < b.x + b.width + 4 &&
              p.x + width + 4 > b.x &&
              p.y < b.y + b.height + 3 &&
              p.y + height + 3 > b.y,
          ),
      );
      if (!candidate && !chosen) continue;
      const place = candidate ?? {
        x: clamp(screen.x - width / 2, 6, viewport.width - width - 6),
        y: clamp(
          screen.y + halfH + 7,
          fitInsets.top - 12,
          Math.max(
            fitInsets.top - 12,
            viewport.height - fitInsets.bottom - height + 12,
          ),
        ),
      };
      occupied.push({ ...place, width, height });
      result.push({
        object: o,
        x: camera.x + (place.x - viewport.width / 2) / pixelsPerMeter,
        y: camera.y - (place.y - viewport.height / 2) / pixelsPerMeter,
        text,
        detail,
        font,
        width,
        height,
      });
    }
    return result;
  }, [
    displayed,
    selectedSet,
    camera,
    pixelsPerMeter,
    viewport,
    editing,
    activeTool,
    fitInsets,
  ]);
  const gridStep = metricStep(Math.max(1, 24 / pixelsPerMeter)),
    showMinorGrid = pixelsPerMeter >= 32,
    axisStep = metricStep(Math.max(gridStep, 56 / pixelsPerMeter)),
    ruler = metricStep(55 / pixelsPerMeter);
  const single = selectedObjects.length === 1 ? selectedObjects[0] : null,
    handleSize = 10 / pixelsPerMeter,
    handleHitSize = 28 / pixelsPerMeter;
  const transforming = preview.length ? gesture.current?.kind : null;
  const selectionAction =
    transforming === "move"
      ? "이동 미리보기"
      : transforming === "resize"
        ? "크기 미리보기"
        : transforming === "rotate"
          ? "회전 미리보기"
          : editing
            ? "선택한 초안"
            : (single?.sourceText ?? "선택 객체");
  const rotationPoint = selectionBounds
    ? {
        x: (selectionBounds.left + selectionBounds.right) / 2,
        y: selectionBounds.top + 28 / pixelsPerMeter,
      }
    : null;
  const tooltip = activeTool
    ? `${names[activeTool]} 배치 · 클릭으로 확정`
    : mode === "pan"
      ? "끌어서 화면 이동"
      : mode === "select"
        ? "클릭 또는 드래그 영역으로 선택 · Shift 추가"
        : editing
          ? single
            ? single.resizable
              ? "끌어서 이동 · 모서리로 크기 · 위쪽 손잡이로 회전"
              : "끌어서 이동 · 위쪽 손잡이로 회전"
            : "객체를 끌어서 이동 · Shift 다중 선택"
          : "객체 선택 · 끌어서 영역 선택";
  return (
    <div
      ref={host}
      className={`map-view plan-editor ${panning ? "is-panning" : ""} ${activeTool ? "is-placing" : `mode-${mode}`}`}
    >
      <div
        ref={toolsOverlay}
        className="plan-tools"
        role="toolbar"
        aria-label="2D 도면 도구"
      >
        <div className="plan-tool-group">
          <button
            type="button"
            aria-pressed={!activeTool && mode === "select"}
            title="선택 (V) · Shift로 추가 선택"
            onClick={() => setEditorMode("select")}
          >
            <MousePointer2 size={15} />
            <span>선택</span>
          </button>
          {editing && (
            <button
              type="button"
              aria-pressed={!activeTool && mode === "move"}
              title="객체 이동 (M)"
              onClick={() => setEditorMode("move")}
            >
              <Move size={15} />
              <span>이동</span>
            </button>
          )}
          <button
            type="button"
            aria-pressed={!activeTool && mode === "pan"}
            title="화면 이동 (H) · Space 또는 가운데 버튼"
            onClick={() => setEditorMode("pan")}
          >
            <Hand size={15} />
            <span>화면 이동</span>
          </button>
        </div>
        <div className="plan-tool-group plan-view-tools">
          <button
            type="button"
            title="축소 (-)"
            aria-label="도면 축소"
            onClick={() => zoom(1.25)}
          >
            <Minus size={15} />
          </button>
          <span
            className="plan-zoom"
            aria-label="전체 보기 기준 확대율"
            title="전체 보기를 100%로 표시합니다"
          >
            {Math.round((fitHeight / camera.height) * 100)}%
          </span>
          <button
            type="button"
            title="확대 (+)"
            aria-label="도면 확대"
            onClick={() => zoom(0.8)}
          >
            <Plus size={15} />
          </button>
          <button
            type="button"
            title="전체 보기 (0)"
            aria-label="도면 전체 보기"
            onClick={fit}
          >
            <Expand size={15} />
            <span>전체 보기</span>
          </button>
          <button
            type="button"
            title={
              selectedObjects.length
                ? "선택 객체로 이동 (F)"
                : "먼저 객체를 선택하세요"
            }
            disabled={!selectedObjects.length}
            aria-label="선택 객체 중심으로 보기"
            onClick={focusSelection}
          >
            <Crosshair size={15} />
            <span>선택 보기</span>
          </button>
        </div>
      </div>
      {(!editing || selectedGuideRobot) && (
        <div ref={sourceOverlay} className="plan-data-source">
          <span>
            {planningPreview
              ? "승인 전 미리보기 · 초기 배치와 정적 예상 경로 · 실제 실행 아님"
              : editing
                ? guideDrawable
                  ? `AGV 지정선 · 초안 · ${guideNumbersReadable ? "번호 순서로 진행" : "확대하면 번호 표시"} · 통과 검증 전`
                  : "AGV 지정선 · 유한한 X·Y 경유점을 입력하면 표시됩니다."
                : "로봇 XY: 관측 · 물품/사람: 물리 · 공간: 구성 · 층: 실제 위치 기준"}
          </span>
          {editing && guideDrawable && (
            <button
              type="button"
              onClick={focusGuide}
              aria-label="AGV 지정 경로 확대"
            >
              <Crosshair size={13} />
              경로 확대
            </button>
          )}
        </div>
      )}
      {tool && editing && (
        <button
          ref={placementOverlay}
          type="button"
          className={`plan-placement-mode ${activeTool ? "active" : ""}`}
          onClick={() => setToolSuspended(false)}
        >
          {names[tool]} {activeTool ? "배치 중 · Esc 취소" : "배치 계속"}
        </button>
      )}
      <svg
        ref={svg}
        viewBox={`${camera.x - viewWidth / 2} ${-camera.y - camera.height / 2} ${viewWidth} ${camera.height}`}
        preserveAspectRatio="none"
        tabIndex={0}
        role="group"
        aria-label={`${floor?.name ?? "층 없음"} 2D 작업 도면`}
        aria-describedby={`${id}-help`}
        onKeyDown={keyDown}
        onKeyUp={(event) => {
          if (event.key === " ") spaceHeld.current = false;
        }}
        onPointerDown={backgroundDown}
        onPointerMove={updateGesture}
        onPointerUp={endGesture}
        onPointerCancel={cancel}
        onLostPointerCapture={() => {
          if (gesture.current) cancel();
        }}
        onPointerLeave={() => {
          if (!gesture.current) setCursor(null);
        }}
        onContextMenu={(e) => e.preventDefault()}
      >
        <defs>
          <pattern
            id={`${id}-minor`}
            width=".25"
            height=".25"
            patternUnits="userSpaceOnUse"
          >
            <path d="M .25 0 H 0 V .25" className="plan-grid-minor" />
          </pattern>
          <pattern
            id={`${id}-major`}
            width={gridStep}
            height={gridStep}
            patternUnits="userSpaceOnUse"
          >
            <path
              d={`M ${gridStep} 0 H 0 V ${gridStep}`}
              className="plan-grid-major"
            />
          </pattern>
          <pattern
            id={`${id}-restricted`}
            width=".25"
            height=".25"
            patternUnits="userSpaceOnUse"
            patternTransform="rotate(45)"
          >
            <path d="M 0 0 V .25" className="plan-hatch" />
          </pattern>
        </defs>
        <rect x={0} y={-h} width={w} height={h} className="plan-floor" />
        {showMinorGrid && (
          <rect
            x={0}
            y={-h}
            width={w}
            height={h}
            fill={`url(#${id}-minor)`}
            pointerEvents="none"
          />
        )}
        <rect
          x={0}
          y={-h}
          width={w}
          height={h}
          fill={`url(#${id}-major)`}
          pointerEvents="none"
        />
        <g className="plan-axis" fontSize={10 / pixelsPerMeter}>
          {Array.from({ length: Math.floor(w / axisStep) + 1 }, (_, i) => (
            <text
              key={`x${i}`}
              x={i * axisStep}
              y={18 / pixelsPerMeter}
              textAnchor="middle"
            >
              {i * axisStep}
            </text>
          ))}
          {Array.from({ length: Math.floor(h / axisStep) + 1 }, (_, i) => (
            <text
              key={`y${i}`}
              x={-10 / pixelsPerMeter}
              y={-i * axisStep}
              textAnchor="end"
              dominantBaseline="central"
            >
              {i * axisStep}
            </text>
          ))}
          <text x={w + 20 / pixelsPerMeter} y={18 / pixelsPerMeter}>
            X / m
          </text>
          <text x={-10 / pixelsPerMeter} y={-h - 12 / pixelsPerMeter}>
            Y / m
          </text>
        </g>
        {!editing &&
          displayed
            .filter((o) => o.path?.length && !o.unavailable)
            .map((o) => (
              <polyline
                key={`path-${o.id}`}
                className="plan-route"
                points={[o.pose, ...o.path!]
                  .map((p) => `${p.x},${-p.y}`)
                  .join(" ")}
              />
            ))}
        {planningPreview &&
          previewRoutes
            .filter((r) => r.floor_id === floorId)
            .map((r) => (
              <polyline
                key={`preview-${r.task_id}`}
                className="plan-route"
                strokeDasharray="0.2 0.15"
                points={r.points.map((p) => `${p.x},${-p.y}`).join(" ")}
              />
            ))}
        {paintedObjects.map((o) => {
          const chosen =
            selectedSet.has(o.id) ||
            (!!marquee && contains(marquee, objectBounds(o)));
          return (
            <g
              key={o.id}
              className={`plan-object type-${o.type} kind-${o.kind} state-${o.status ?? "none"} ${chosen ? "is-selected" : ""} ${o.unavailable ? "is-unobserved" : ""}`}
              transform={`translate(${o.pose.x},${-o.pose.y})`}
              tabIndex={0}
              role="button"
              aria-pressed={selectedSet.has(o.id)}
              aria-label={`${o.name}${o.type === "robot" ? `, ${robotNames[o.kind] ?? o.kind}, ${o.statusText}` : ""} 선택`}
              onPointerDown={(event) => objectDown(event, o)}
              onKeyDown={(event) => {
                if (event.key === "Enter" || event.key === " ") {
                  event.preventDefault();
                  event.stopPropagation();
                  cancel();
                  select(
                    event.shiftKey
                      ? selectedSet.has(o.id)
                        ? ids.filter((id) => id !== o.id)
                        : [...ids, o.id]
                      : [o.id],
                  );
                } else if (
                  ["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown"].includes(
                    event.key,
                  ) &&
                  editing &&
                  !activeTool &&
                  !gesture.current &&
                  !event.ctrlKey &&
                  !event.metaKey &&
                  !event.altKey &&
                  !selectedSet.has(o.id)
                ) {
                  // A focused but unselected object must never move a different
                  // old selection when its arrow key bubbles to the canvas.
                  event.preventDefault();
                  event.stopPropagation();
                  select([o.id]);
                  commit(nudgeChanges([o], event.key, event.shiftKey));
                }
              }}
            >
              <title>
                {o.name} · X {o.pose.x.toFixed(2)}, Y {o.pose.y.toFixed(2)} m ·{" "}
                {o.sourceText}
              </title>
              <g transform={`rotate(${(-o.pose.yaw * 180) / Math.PI})`}>
                <rect
                  className="plan-hit-target"
                  x={-Math.max(o.size.x, 22 / pixelsPerMeter) / 2}
                  y={-Math.max(o.size.y, 22 / pixelsPerMeter) / 2}
                  width={Math.max(o.size.x, 22 / pixelsPerMeter)}
                  height={Math.max(o.size.y, 22 / pixelsPerMeter)}
                />
                {o.type === "robot" ? (
                  <RobotSymbol kind={o.kind} size={o.size} />
                ) : o.type === "person" ? (
                  <>
                    <circle className="plan-person" r=".22" />
                    <path
                      className="plan-person-detail"
                      d="M -.1 .03 Q 0 -.15 .1 .03 M 0 -.1 V .11 M .27 -.06 L .35 0 L .27 .06"
                    />
                  </>
                ) : (
                  <>
                    <rect
                      className="plan-geometry"
                      x={-o.size.x / 2}
                      y={-o.size.y / 2}
                      width={o.size.x}
                      height={o.size.y}
                      rx={o.type === "item" ? 0.025 : 0}
                    />
                    {o.kind === "restricted" && (
                      <rect
                        x={-o.size.x / 2}
                        y={-o.size.y / 2}
                        width={o.size.x}
                        height={o.size.y}
                        fill={`url(#${id}-restricted)`}
                        pointerEvents="none"
                      />
                    )}
                    {o.kind === "one_way" && (
                      <path
                        className="plan-feature"
                        d={`M ${-o.size.x * 0.28} 0 H ${o.size.x * 0.28} M 0 ${-o.size.y * 0.2} L ${o.size.x * 0.28} 0 L 0 ${o.size.y * 0.2}`}
                      />
                    )}
                    {o.kind === "stairs" &&
                      Array.from({ length: 5 }, (_, i) => (
                        <path
                          key={i}
                          className="plan-feature"
                          d={`M ${-o.size.x / 2} ${-o.size.y / 2 + (o.size.y * (i + 1)) / 6} h ${o.size.x}`}
                        />
                      ))}
                    {o.type === "item" && (
                      <path
                        className="plan-item-tape"
                        d={`M ${-o.size.x / 2} 0 H ${o.size.x / 2} M 0 ${-o.size.y / 2} V ${o.size.y / 2}`}
                      />
                    )}
                  </>
                )}
                {chosen && (
                  <rect
                    className="plan-selected-outline"
                    x={-o.size.x / 2 - 4 / pixelsPerMeter}
                    y={-o.size.y / 2 - 4 / pixelsPerMeter}
                    width={o.size.x + 8 / pixelsPerMeter}
                    height={o.size.y + 8 / pixelsPerMeter}
                  />
                )}
              </g>
              {o.type === "robot" && (
                <g
                  className="plan-status-symbol"
                  transform={`translate(${o.size.x / 2 + 5 / pixelsPerMeter},${-o.size.y / 2 - 4 / pixelsPerMeter})`}
                >
                  <circle r={8 / pixelsPerMeter} />
                  <text
                    fontSize={12 / pixelsPerMeter}
                    textAnchor="middle"
                    dominantBaseline="central"
                  >
                    {o.glyph}
                  </text>
                </g>
              )}
            </g>
          );
        })}
        {guideDrawable && (
          <g
            className="plan-authored-guide"
            pointerEvents="none"
            role="img"
            aria-label={`${selectedGuideRobot!.name} 지정 경로 초안, ${selectedGuide.length}개 점, 번호 순서로 진행, 통과 검증 전`}
          >
            <polyline
              points={selectedGuide
                .map((point) => `${point.x},${-point.y}`)
                .join(" ")}
            />
            {selectedGuide.slice(1).map((point, index) => {
              const previous = selectedGuide[index];
              const length = Math.hypot(
                point.x - previous.x,
                point.y - previous.y,
              );
              if (length * pixelsPerMeter < 28) return null;
              const angle =
                (Math.atan2(-point.y + previous.y, point.x - previous.x) *
                  180) /
                Math.PI;
              return (
                <path
                  key={`direction-${index}`}
                  className="plan-guide-arrow"
                  transform={`translate(${(point.x + previous.x) / 2},${-(point.y + previous.y) / 2}) rotate(${angle})`}
                  d={`M ${-5 / pixelsPerMeter} ${-4 / pixelsPerMeter} L ${2 / pixelsPerMeter} 0 L ${-5 / pixelsPerMeter} ${4 / pixelsPerMeter}`}
                />
              );
            })}
            {guideNodes.map(({ point, numbers }, index) => {
              const nearRobot =
                Math.hypot(
                  point.x - selectedGuideRobot!.pose.x,
                  point.y - selectedGuideRobot!.pose.y,
                ) < 0.8;
              const offset = Math.max(
                14 / pixelsPerMeter,
                nearRobot ? 0.75 : 0,
              );
              return (
                <g
                  key={`waypoint-${index}`}
                  transform={`translate(${point.x},${-point.y})`}
                >
                  <circle r={3 / pixelsPerMeter} />
                  {guideNumbersReadable && (
                    <>
                      <path
                        className="plan-guide-leader"
                        d={`M ${4 / pixelsPerMeter} 0 L ${offset - 3 / pixelsPerMeter} ${-6 / pixelsPerMeter}`}
                      />
                      <text
                        x={offset}
                        y={-8 / pixelsPerMeter}
                        fontSize={12 / pixelsPerMeter}
                      >
                        {numbers.join("·")}
                      </text>
                    </>
                  )}
                </g>
              );
            })}
          </g>
        )}
        <g className="plan-labels" pointerEvents="none">
          {labelLayout.map((label) => (
            <g
              key={label.object.id}
              className={`plan-nameplate ${selectedSet.has(label.object.id) ? "is-selected" : ""}`}
              transform={`translate(${label.x},${-label.y})`}
            >
              <rect
                width={label.width / pixelsPerMeter}
                height={label.height / pixelsPerMeter}
                rx={3 / pixelsPerMeter}
              />
              <text
                x={6 / pixelsPerMeter}
                y={15 / pixelsPerMeter}
                fontSize={label.font / pixelsPerMeter}
              >
                {label.text}
              </text>
              {label.detail && (
                <text
                  className="plan-label-detail"
                  x={6 / pixelsPerMeter}
                  y={29 / pixelsPerMeter}
                  fontSize={11 / pixelsPerMeter}
                >
                  {label.detail}
                </text>
              )}
            </g>
          ))}
        </g>
        {marquee && (
          <rect
            className="plan-marquee"
            x={marquee.left}
            y={-marquee.top}
            width={marquee.right - marquee.left}
            height={marquee.top - marquee.bottom}
            pointerEvents="none"
          />
        )}
        {editing &&
          onTransform &&
          !activeTool &&
          mode !== "pan" &&
          selectionBounds && (
            <g className="plan-transform-controls">
              {single?.resizable &&
                [-1, 1].flatMap((x) =>
                  [-1, 1].map((y) => {
                    const delta = rotate(
                      {
                        x: (x * single.size.x) / 2,
                        y: (y * single.size.y) / 2,
                      },
                      single.pose.yaw,
                    );
                    return (
                      <g
                        key={`${x}/${y}`}
                        className="plan-resize-control"
                        role="button"
                        tabIndex={0}
                        aria-label={`${single.name} 크기 조절 · 방향키 사용`}
                        transform={`translate(${single.pose.x + delta.x},${-single.pose.y - delta.y})`}
                        style={{
                          cursor: x * y < 0 ? "nwse-resize" : "nesw-resize",
                        }}
                        onPointerDown={(event) =>
                          beginHandle(event, "resize", { x, y })
                        }
                        onKeyDown={(event) => {
                          if (
                            event.ctrlKey ||
                            event.metaKey ||
                            event.altKey ||
                            gesture.current
                          )
                            return;
                          if (
                            ![
                              "ArrowLeft",
                              "ArrowRight",
                              "ArrowUp",
                              "ArrowDown",
                            ].includes(event.key)
                          )
                            return;
                          event.preventDefault();
                          event.stopPropagation();
                          const step = event.shiftKey ? 1 : snap ? 0.25 : 0.05;
                          const dimension = (value: number, delta: number) =>
                            delta === 0
                              ? value
                              : Math.max(
                                  snap ? 0.25 : 0.1,
                                  snap
                                    ? Math.round((value + delta) * 4) / 4
                                    : rounded(value + delta),
                                );
                          const size = {
                            ...single.size,
                            x: dimension(
                              single.size.x,
                              event.key === "ArrowRight"
                                ? x * step
                                : event.key === "ArrowLeft"
                                  ? -x * step
                                  : 0,
                            ),
                            y: dimension(
                              single.size.y,
                              event.key === "ArrowUp"
                                ? y * step
                                : event.key === "ArrowDown"
                                  ? -y * step
                                  : 0,
                            ),
                          };
                          const shift = rotate(
                            {
                              x: (x * (size.x - single.size.x)) / 2,
                              y: (y * (size.y - single.size.y)) / 2,
                            },
                            single.pose.yaw,
                          );
                          commit([
                            {
                              id: single.id,
                              size,
                              pose: {
                                ...single.pose,
                                x: rounded(single.pose.x + shift.x),
                                y: rounded(single.pose.y + shift.y),
                              },
                            },
                          ]);
                        }}
                      >
                        <title>크기 조절 · 방향키로 조절 · Shift로 1 m씩</title>
                        <rect
                          className="plan-handle-hit"
                          x={-handleHitSize / 2}
                          y={-handleHitSize / 2}
                          width={handleHitSize}
                          height={handleHitSize}
                        />
                        <rect
                          className="plan-resize-handle"
                          x={-handleSize / 2}
                          y={-handleSize / 2}
                          width={handleSize}
                          height={handleSize}
                          pointerEvents="none"
                        />
                      </g>
                    );
                  }),
                )}
              {rotationPoint && (
                <>
                  <path
                    className="plan-rotation-stem"
                    d={`M ${rotationPoint.x} ${-selectionBounds.top} V ${-rotationPoint.y}`}
                  />
                  <g
                    className="plan-rotation-handle"
                    transform={`translate(${rotationPoint.x},${-rotationPoint.y})`}
                    role="button"
                    tabIndex={0}
                    aria-label="선택 회전 · 좌우 방향키로 15도 회전"
                    onPointerDown={(event) => beginHandle(event, "rotate")}
                    onKeyDown={(event) => {
                      if (
                        event.ctrlKey ||
                        event.metaKey ||
                        event.altKey ||
                        gesture.current
                      )
                        return;
                      if (
                        ![
                          "ArrowLeft",
                          "ArrowRight",
                          "ArrowUp",
                          "ArrowDown",
                        ].includes(event.key)
                      )
                        return;
                      event.preventDefault();
                      event.stopPropagation();
                      if (event.key === "ArrowUp" || event.key === "ArrowDown")
                        return;
                      const center = {
                        x: (selectionBounds.left + selectionBounds.right) / 2,
                        y: (selectionBounds.top + selectionBounds.bottom) / 2,
                      };
                      commit(
                        rotationChanges(
                          selectedObjects,
                          center,
                          ((event.key === "ArrowLeft" ? 1 : -1) * Math.PI) / 12,
                        ),
                      );
                    }}
                  >
                    <title>회전 · 좌우 방향키로 15°씩</title>
                    <circle className="plan-handle-hit" r={handleHitSize / 2} />
                    <circle r={10 / pixelsPerMeter} />
                    <RotateCw
                      x={-6 / pixelsPerMeter}
                      y={-6 / pixelsPerMeter}
                      width={12 / pixelsPerMeter}
                      height={12 / pixelsPerMeter}
                    />
                  </g>
                </>
              )}
            </g>
          )}
        {activeTool && cursor && floor && (
          <g
            className="plan-placement-preview"
            transform={`translate(${cursor.x},${-cursor.y})`}
            pointerEvents="none"
          >
            <rect
              x={-placementSize(activeTool).x / 2}
              y={-placementSize(activeTool).y / 2}
              width={placementSize(activeTool).x}
              height={placementSize(activeTool).y}
            />
            <path d="M -.12 0 H .12 M 0 -.12 V .12" />
            <text
              x={10 / pixelsPerMeter}
              y={-12 / pixelsPerMeter}
              fontSize={12 / pixelsPerMeter}
            >
              {names[activeTool]} · {cursor.x.toFixed(2)}, {cursor.y.toFixed(2)}{" "}
              m
            </text>
          </g>
        )}
      </svg>
      {!floor && (
        <div className="plan-empty">
          <strong>작업할 층을 선택하세요</strong>
          <span>프로젝트의 층과 객체를 이 도면에서 편집할 수 있습니다.</span>
        </div>
      )}
      <div ref={footerOverlay} className="plan-bottom-stack">
        {!!selectedObjects.length && !activeTool && (
          <div
            className={`plan-selection-summary ${transforming ? "is-preview" : ""}`}
          >
            <div className="plan-selection-heading">
              <span>{selectionAction}</span>
              <strong title={single?.name}>
                {single?.name ?? `${selectedObjects.length}개 객체`}
              </strong>
            </div>
            {single ? (
              <div className="plan-selection-values">
                <span>
                  X <b>{single.pose.x.toFixed(2)}</b> · Y{" "}
                  <b>{single.pose.y.toFixed(2)}</b> m
                </span>
                <span>
                  크기{" "}
                  <b>
                    {single.size.x.toFixed(2)} × {single.size.y.toFixed(2)}
                  </b>{" "}
                  m
                </span>
                <span>
                  각도 <b>{((single.pose.yaw * 180) / Math.PI).toFixed(1)}°</b>
                </span>
              </div>
            ) : (
              <span className="plan-selection-values">
                {editing
                  ? "함께 이동·회전할 수 있습니다."
                  : "선택 보기로 위치를 확인하세요."}
              </span>
            )}
            {transforming && (
              <span className="plan-preview-note">
                놓으면 초안 반영 · Esc 취소
              </span>
            )}
          </div>
        )}
        <div className="plan-footer">
          <div className="plan-context">
            <strong>{floor?.name ?? "층 없음"}</strong>
            <span>
              {planningPreview
                ? "계획 미리보기"
                : editing
                  ? "구성 초안"
                  : "관제 보기"}
            </span>
            <span>
              {selectedObjects.length
                ? `${selectedObjects.length}개 선택`
                : `${objects.length}개 객체`}
            </span>
          </div>
          <div
            className="plan-scale"
            aria-label={`축척 막대 ${metricLabel(ruler)} m`}
          >
            <span style={{ width: ruler * pixelsPerMeter }} />
            <span>{metricLabel(ruler)} m</span>
          </div>
          <span ref={gridOverlay} className="plan-grid-caption">
            격자 {metricLabel(gridStep)} m
            {showMinorGrid ? " · 보조 0.25 m" : ""}
            {editing
              ? ` · ${snap ? "0.25 m / 15° 맞춤" : "자유 이동·회전"}`
              : ""}
          </span>
        </div>
        <div ref={helpOverlay} className="plan-help" id={`${id}-help`}>
          <span>{tooltip}</span>
          <span className="plan-coordinate">
            {cursor
              ? `X ${cursor.x.toFixed(2)} · Y ${cursor.y.toFixed(2)} m`
              : "휠 확대 · Space 화면 이동"}
          </span>
        </div>
      </div>
      <span className="plan-sr-only" aria-live="polite">
        {announcement}
      </span>
    </div>
  );
}
