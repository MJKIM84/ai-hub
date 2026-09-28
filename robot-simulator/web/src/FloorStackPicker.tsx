import { useRef } from "react";
import { ChevronDown, X } from "lucide-react";
import type { Element, Floor } from "./types";
import "./FloorStackPicker.css";

const drawn = new Set([
  "room",
  "corridor",
  "wall",
  "door",
  "opening",
  "stairs",
  "elevator",
  "waiting",
  "restricted",
]);

function FloorSlice({
  floor,
  elements,
}: {
  floor: Floor;
  elements: Element[];
}) {
  const shapes = elements.filter(
    (element) =>
      drawn.has(element.kind) &&
      (element.floor_id === floor.id ||
        (element.kind === "elevator" &&
          element.facility.served_floors.includes(floor.id))),
  );
  return (
    <svg
      className="floor-stack__drawing"
      viewBox={`0 0 ${floor.width} ${floor.depth}`}
      aria-hidden="true"
    >
      <rect
        x="0.05"
        y="0.05"
        width={floor.width - 0.1}
        height={floor.depth - 0.1}
        className="floor-stack__outline"
      />
      <g transform={`translate(0 ${floor.depth}) scale(1 -1)`}>
        {shapes.map((element) => (
          <rect
            key={element.id}
            x={element.pose.x - element.size.x / 2}
            y={element.pose.y - element.size.y / 2}
            width={element.size.x}
            height={element.size.y}
            transform={`rotate(${(element.pose.yaw * 180) / Math.PI} ${element.pose.x} ${element.pose.y})`}
            className={`floor-stack__shape floor-stack__shape--${element.kind}`}
          />
        ))}
      </g>
    </svg>
  );
}

export function FloorStackPicker({
  floors,
  elements,
  currentId,
  robotFloorId,
  hoveredId,
  open,
  onOpen,
  onPreview,
  onCommit,
  onCancel,
}: {
  floors: Floor[];
  elements: Element[];
  currentId: string;
  robotFloorId?: string;
  hoveredId: string | null;
  open: boolean;
  onOpen: () => void;
  onPreview: (floorId: string) => void;
  onCommit: (floorId: string) => void;
  onCancel: () => void;
}) {
  const list = useRef<HTMLDivElement>(null);
  const current = floors.find((floor) => floor.id === currentId);
  return (
    <div className="floor-stack">
      <button
        type="button"
        className="floor-stack__trigger"
        aria-expanded={open}
        aria-controls="floor-stack-list"
        onClick={open ? onCancel : onOpen}
        onKeyDown={(event) => {
          if (!open) return;
          if (event.key === "Escape") {
            event.preventDefault();
            event.stopPropagation();
            onCancel();
            return;
          }
          if (event.key === "ArrowDown" || event.key === "ArrowUp") {
            event.preventDefault();
            event.stopPropagation();
            const buttons = list.current?.querySelectorAll<HTMLButtonElement>(
              ".floor-stack__floor",
            );
            (event.key === "ArrowDown"
              ? buttons?.[0]
              : buttons?.[buttons.length - 1]
            )?.focus();
          }
        }}
      >
        <span className="floor-stack__trigger-label">관찰 층</span>
        <strong>{current?.name ?? "선택 대기"}</strong>
        <ChevronDown size={15} aria-hidden="true" />
      </button>
      {open && (
        <div
          id="floor-stack-list"
          ref={list}
          className="floor-stack__panel"
          role="group"
          aria-label="분해된 층 도면"
          onKeyDown={(event) => {
            if (event.key === "Escape") {
              event.preventDefault();
              event.stopPropagation();
              onCancel();
              return;
            }
            if (event.key !== "ArrowDown" && event.key !== "ArrowUp") return;
            const buttons = [
              ...(list.current?.querySelectorAll<HTMLButtonElement>(
                ".floor-stack__floor",
              ) ?? []),
            ];
            const currentIndex = buttons.indexOf(
              document.activeElement as HTMLButtonElement,
            );
            const delta = event.key === "ArrowDown" ? 1 : -1;
            const next =
              buttons[(currentIndex + delta + buttons.length) % buttons.length];
            if (next) {
              event.preventDefault();
              event.stopPropagation();
              next.focus();
            }
          }}
        >
          <div className="floor-stack__panel-head">
            <div>
              <strong>층 단면 탐색</strong>
              <small>올려서 미리 보고, 눌러서 고정</small>
            </div>
            <button type="button" aria-label="층 탐색 취소" onClick={onCancel}>
              <X size={16} />
            </button>
          </div>
          <div className="floor-stack__levels">
            {[...floors].reverse().map((floor) => (
              <button
                type="button"
                key={floor.id}
                className={`floor-stack__floor${floor.id === currentId ? " is-current" : ""}${floor.id === hoveredId ? " is-hovered" : ""}`}
                aria-label={`${floor.name} 미리보기${floor.id === currentId ? " · 현재 관찰 층" : ""}${floor.id === robotFloorId ? " · 선택한 로봇 위치" : ""}`}
                aria-current={floor.id === currentId ? "true" : undefined}
                onPointerEnter={(event) => {
                  if (
                    event.pointerType === "mouse" ||
                    event.pointerType === "pen"
                  )
                    onPreview(floor.id);
                }}
                onFocus={() => onPreview(floor.id)}
                onClick={() => onCommit(floor.id)}
              >
                <span className="floor-stack__floor-meta">
                  <b>{floor.name}</b>
                  <small>{floor.elevation.toFixed(1)} m</small>
                </span>
                <FloorSlice floor={floor} elements={elements} />
                <span className="floor-stack__badges">
                  {floor.id === currentId && <em>현재 화면</em>}
                  {floor.id === robotFloorId && <em>선택 로봇</em>}
                </span>
              </button>
            ))}
          </div>
          <p className="floor-stack__help">
            Esc로 취소 · ↑↓로 층 이동 · Enter로 고정
          </p>
        </div>
      )}
    </div>
  );
}
