import { Component, lazy, Suspense } from "react";
import type { ComponentProps, ReactNode } from "react";
export { PlanView } from "./PlanView";
const PhysicsScene = lazy(() =>
  import("./PhysicsView").then((module) => ({ default: module.PhysicsView })),
);
class SceneBoundary extends Component<
  { children: ReactNode },
  { failed: boolean }
> {
  state = { failed: false };
  static getDerivedStateFromError() {
    return { failed: true };
  }
  render() {
    return this.state.failed ? (
      <div className="empty map-view" role="alert">
        <strong>3D 화면을 불러오지 못했습니다.</strong>
        <p>
          편집 초안은 이 브라우저에 보관됩니다. 2D 화면을 사용하거나 화면을 다시
          불러오세요.
        </p>
        <button onClick={() => window.location.reload()}>화면 새로고침</button>
      </div>
    ) : (
      this.props.children
    );
  }
}
export function PhysicsView(
  props: ComponentProps<typeof import("./PhysicsView").PhysicsView>,
) {
  return (
    <SceneBoundary>
      <Suspense
        fallback={
          <div className="empty map-view" role="status">
            <strong>3D 관찰 도구를 불러오는 중입니다.</strong>
            <p>물리 장면은 실행부에서 수신한 데이터로 표시됩니다.</p>
          </div>
        }
      >
        <PhysicsScene {...props} />
      </Suspense>
    </SceneBoundary>
  );
}
