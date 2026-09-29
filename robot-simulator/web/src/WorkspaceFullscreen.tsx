import { useEffect, useRef, useState } from "react";
import { Maximize, Minimize } from "lucide-react";

/** Enlarge the existing scene without remounting it or changing project state. */
export function WorkspaceFullscreen() {
  const [active, setActive] = useState(false);
  const target = useRef<HTMLElement | null>(null);
  const button = useRef<HTMLButtonElement>(null);
  const native = useRef(false);

  useEffect(() => {
    if (!active || !target.current) return;
    const element = target.current;
    const previousOverflow = document.body.style.overflow;
    element.dataset.fullscreen = "true";
    document.body.classList.add("workspace-fullscreen-active");
    document.body.style.overflow = "hidden";
    const leave = () => {
      setActive(false);
      button.current?.focus({ preventScroll: true });
    };
    const onKey = (event: KeyboardEvent) => {
      if (event.key !== "Escape") return;
      event.preventDefault();
      event.stopPropagation();
      if (document.fullscreenElement === element) void document.exitFullscreen().catch(() => {});
      leave();
    };
    const onFullscreen = () => {
      if (document.fullscreenElement === element) native.current = true;
      else if (native.current) leave();
    };
    window.addEventListener("keydown", onKey, true);
    document.addEventListener("fullscreenchange", onFullscreen);
    return () => {
      window.removeEventListener("keydown", onKey, true);
      document.removeEventListener("fullscreenchange", onFullscreen);
      delete element.dataset.fullscreen;
      document.body.classList.remove("workspace-fullscreen-active");
      document.body.style.overflow = previousOverflow;
      if (document.fullscreenElement === element) void document.exitFullscreen().catch(() => {});
      native.current = false;
    };
  }, [active]);

  return (
    <button
      ref={button}
      className="ghost workspace-fullscreen-button"
      aria-pressed={active}
      title={active ? "전체 화면 닫기 (Esc)" : "메뉴와 패널을 숨기고 지도를 전체 화면으로 봅니다."}
      onClick={(event) => {
        if (active) {
          setActive(false);
          return;
        }
        const element = event.currentTarget.closest<HTMLElement>(".workspace");
        if (!element) return;
        target.current = element;
        setActive(true);
        // Embedded browsers may disallow native fullscreen; the viewport-sized
        // mode below still works and keeps the same Exit / Escape controls.
        if (element.requestFullscreen) {
          try {
            void element.requestFullscreen().then(() => { native.current = true; }).catch(() => {});
          } catch { /* Use the in-page full-window mode. */ }
        }
      }}
    >
      {active ? <Minimize size={15} /> : <Maximize size={15} />}
      {active ? "전체 화면 닫기 · Esc" : "전체 화면"}
    </button>
  );
}
