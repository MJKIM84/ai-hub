/** Presentation only: never changes draft fingerprints or execution guards. */
export type RunApproval = {
  plan_id: string;
  version: number;
  run_id: string;
  status?: string;
};
export function executionConfigurationDisplay(
  dirty: boolean,
  runId: string | undefined,
  approval: RunApproval | null,
) {
  if (
    runId &&
    approval?.run_id === runId &&
    approval.status === "accepted" &&
    approval.plan_id &&
    Number.isInteger(approval.version) &&
    approval.version > 0
  ) {
    return {
      value: `승인 계획 v${approval.version} · ${dirty ? "편집 초안 별도" : "구성 일치"}`,
      tone: undefined,
      description: dirty
        ? "현재 실행에는 사용자가 승인한 계획 구성이 적용되어 있습니다. 편집 초안은 이 실행과 다르며 자동 반영되지 않습니다. 변경하려면 계획 도우미에서 구성을 갱신하고 다시 승인하세요."
        : "현재 실행에는 사용자가 승인한 계획 구성이 적용되어 있으며 편집 초안과도 일치합니다.",
    };
  }
  return {
    value: dirty ? "실행부 미적용" : "실행 구성 일치",
    tone: dirty ? "warn" : undefined,
    description: dirty
      ? "편집 초안이 현재 실행 구성과 다릅니다. 실행에 반영하기 전에 구성을 확인하세요."
      : "편집 초안과 현재 실행 구성이 일치합니다.",
  };
}
