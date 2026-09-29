import { useCallback, useEffect, useMemo, useState } from "react";
import { ArrowRight, FolderOpen, RefreshCw, Search } from "lucide-react";
import { request } from "./api";
import type { Catalog, Experiment, SavedProject } from "./types";
import "./HistoryLibrary.css";

type Drawing = {
  id: string; title: string; revision: number; version_count: number;
  page_count: number; unreviewed: number; deferred: number; generated: boolean;
  image_available: boolean; updated_at: number; source_warning?: string;
};
type WorkPlan = {
  id: string; version: number; created_at: number;
  intent?: { goal?: string }; origin?: string; approval?: { run_id?: string } | null;
};
type Category = "all" | "projects" | "examples" | "drawings" | "plans" | "experiments";
const categories: { id: Category; label: string }[] = [
  { id: "all", label: "전체" }, { id: "projects", label: "저장한 구성" },
  { id: "examples", label: "샘플·예제" }, { id: "drawings", label: "도면" },
  { id: "plans", label: "업무 계획" }, { id: "experiments", label: "실험 결과" },
];
const date = (value?: string | number | null) => {
  if (!value) return "저장 시각 미기록";
  const parsed = new Date(typeof value === "number" && value < 1e11 ? value * 1000 : value);
  return Number.isNaN(parsed.getTime()) ? "저장 시각 미기록" :
    new Intl.DateTimeFormat("ko-KR", { dateStyle: "medium", timeStyle: "short" }).format(parsed);
};
const message = (error: unknown) => error instanceof Error ? error.message : String(error);

export default function HistoryLibrary({ catalog, saved, currentProjectId, currentProjectRevision, currentProjectName, running, busy,
  onRefreshProjects, onOpenProject, onLoadExample, onReviewDrawing, onOpenPlan, onViewExperiments,
  onOpenExperimentRun,
}: {
  catalog: Catalog; saved: SavedProject[]; currentProjectId?: string;
  currentProjectRevision?: number; currentProjectName?: string; running: boolean; busy: boolean;
  onRefreshProjects: () => Promise<void>;
  onOpenProject: (id: string, revision: number, prepare: boolean) => void;
  onLoadExample: (id: string, prepare: boolean) => void;
  onReviewDrawing: (id: string) => void;
  onOpenPlan: (id: string, version: number) => void;
  onViewExperiments: () => void;
  onOpenExperimentRun: (experimentId: string, runId: string, prepare: boolean) => void;
}) {
  const [category, setCategory] = useState<Category>("all");
  const [query, setQuery] = useState("");
  const [drawings, setDrawings] = useState<Drawing[]>([]);
  const [plans, setPlans] = useState<WorkPlan[]>([]);
  const [experiments, setExperiments] = useState<Experiment[]>([]);
  const [loading, setLoading] = useState(false);
  const [errors, setErrors] = useState<string[]>([]);
  const refresh = useCallback(async () => {
    setLoading(true);
    const sources = [
      request<Drawing[]>("/floorplans"), request<WorkPlan[]>("/plans"),
      request<Experiment[]>("/experiments"), onRefreshProjects(),
    ] as const;
    const results = await Promise.allSettled(sources);
    if (results[0].status === "fulfilled") setDrawings(results[0].value);
    if (results[1].status === "fulfilled") setPlans(results[1].value);
    if (results[2].status === "fulfilled") setExperiments(results[2].value);
    setErrors(results.flatMap((result, index) => result.status === "rejected"
      ? [`${["도면", "계획", "실험", "프로젝트"][index]} 기록: ${message(result.reason)}`] : []));
    setLoading(false);
  }, [onRefreshProjects]);
  useEffect(() => { void refresh(); }, [refresh]);
  const matches = (value: string) => value.toLocaleLowerCase().includes(query.trim().toLocaleLowerCase());
  const projects = saved.filter((row) => matches(`${row.name} ${row.versions?.map((v) => `${v.name} ${v.map_name}`).join(" ") ?? ""}`));
  const examples = catalog.templates.filter((row) => matches(`${row.name} ${row.group ?? ""} ${row.description ?? ""}`));
  const visibleDrawings = drawings.filter((row) => matches(row.title));
  const groups = useMemo(() => {
    const grouped = new Map<string, WorkPlan[]>();
    for (const row of plans) grouped.set(row.id, [...(grouped.get(row.id) ?? []), row]);
    return [...grouped.values()].map((versions) => versions.sort((a, b) => b.version - a.version))
      .sort((a, b) => (b[0]?.created_at ?? 0) - (a[0]?.created_at ?? 0));
  }, [plans]);
  const visiblePlans = groups.filter((versions) => matches(versions[0]?.intent?.goal ?? versions[0]?.id ?? ""));
  const visibleExperiments = experiments.filter((row) => matches(`${row.name ?? ""} ${row.id}`));
  const shown = (id: Category) => category === "all" || category === id;
  const empty = (shown("projects") ? projects.length : 0) +
    (shown("examples") ? examples.length : 0) +
    (shown("drawings") ? visibleDrawings.length : 0) +
    (shown("plans") ? visiblePlans.length : 0) +
    (shown("experiments") ? visibleExperiments.length : 0) === 0;
  return <section className="history-library" aria-label="작업 기록 보관함">
    <header className="history-library-header">
      <div><span className="eyebrow">저장 · 검토 · 실행</span><h2>다시 이어서 작업하기</h2>
        <p>저장한 구성은 버전별로 복원하고, 샘플은 언제든 새 초안으로 불러올 수 있습니다. 열기만으로 시뮬레이션은 시작되지 않습니다.</p></div>
      <button type="button" onClick={() => void refresh()} disabled={loading || busy}><RefreshCw size={15} /> {loading ? "확인 중…" : "목록 새로고침"}</button>
    </header>
    <div className="history-library-controls">
      <label className="history-library-search"><Search size={17} /><span className="sr-only">기록 검색</span>
        <input value={query} onChange={(event) => setQuery(event.target.value)} placeholder="이름이나 지도명으로 찾기" aria-label="기록 검색" /></label>
      <div className="history-library-tabs" role="group" aria-label="기록 유형">
        {categories.map((item) => <button key={item.id} type="button" aria-pressed={category === item.id}
          onClick={() => setCategory(item.id)}>{item.label}</button>)}
      </div>
    </div>
    {errors.length > 0 && <div className="history-library-error" role="alert">일부 기록을 읽지 못했습니다. 연결을 확인한 뒤 새로고침하세요. {errors.join(" · ")}</div>}
    {empty && <div className="history-library-empty">검색 결과가 없습니다. 다른 이름으로 찾거나 유형을 ‘전체’로 바꿔보세요.</div>}
    {shown("projects") && projects.length > 0 && <div className="history-library-section">
      <div className="history-library-section-title"><h3>저장한 구성</h3><span>{projects.length}개 프로젝트 · 버전 {projects.reduce((n, p) => n + (p.version_count ?? p.versions?.length ?? 1), 0)}개</span></div>
      {projects.map((row) => <details key={row.id} className="history-library-group">
        <summary><span className="history-library-title"><FolderOpen size={17} /> {row.name}</span>
          <span>{row.version_count ?? row.versions?.length ?? 1}개 버전 · 최신 v{row.revision}{row.versions?.some((v) => v.name !== row.name) ? " · 이름이 다른 기록 포함" : ""}</span></summary>
        {(row.versions ?? []).map((version) => <div className="history-library-row" key={version.revision}>
          <div><strong>v{version.revision} · {version.name} {row.id === currentProjectId && version.revision === currentProjectRevision && version.name === currentProjectName && <em className="history-library-current">현재 초안</em>}</strong><small>{version.map_name} · 지도 v{version.map_version} · {version.floor_count}층 · 로봇 {version.robot_count}대 · 사람 {version.person_count ?? "—"}명 · 작업 {version.task_count ?? "—"}개</small>
            <small>정책 {version.policy_name ?? "미기록"} · 시드 {version.seed ?? "미기록"}{version.auto_stop_after_seconds ? ` · 자동 정지 ${version.auto_stop_after_seconds}초` : ""}</small>
            <small>{date(version.saved_at)} · {version.source ?? "저장 기록"}</small></div>
          <div className="history-library-actions"><button disabled={busy} onClick={() => onOpenProject(row.id, version.revision, false)}>편집으로 열기</button>
            <button className="primary" disabled={busy || running} title={running ? "먼저 현재 실행을 일시 정지하세요." : "이 버전을 실행부에 적용하고 시작할 준비를 합니다."}
              onClick={() => onOpenProject(row.id, version.revision, true)}>실행 준비 <ArrowRight size={14} /></button></div>
        </div>)}
      </details>)}
    </div>}
    {shown("examples") && examples.length > 0 && <div className="history-library-section">
      <div className="history-library-section-title"><h3>샘플·예제</h3><span>{examples.length}개 · 원본 구성 보존</span></div>
      {examples.map((row) => <div className="history-library-row" key={row.id}><div><strong>{row.name}</strong>
        <small>{row.group ?? "예제"} · 기존에 저장된 시작 구성</small>
        {row.description && <small>{row.description}</small>}</div>
        <div className="history-library-actions"><button disabled={busy} onClick={() => onLoadExample(row.id, false)}>초안으로 열기</button>
          <button className="primary" disabled={busy || running} onClick={() => onLoadExample(row.id, true)}>실행 준비 <ArrowRight size={14} /></button></div></div>)}
    </div>}
    {shown("drawings") && visibleDrawings.length > 0 && <div className="history-library-section">
      <div className="history-library-section-title"><h3>도면 작업</h3><span>{visibleDrawings.length}개 · 원본과 수정 이력</span></div>
      {visibleDrawings.map((row) => <div className="history-library-row" key={row.id}><div><strong>{row.title}</strong>
        <small>{row.page_count}개 층 · v{row.revision} · 검토 버전 {row.version_count}개 · {row.generated ? "지도 생성됨" : "지도 미생성"}</small>
        <small>미검토 {row.unreviewed}개{row.deferred ? ` · 보류 ${row.deferred}개` : ""}{!row.image_available ? " · 원본 이미지 없음" : ""}{row.source_warning ? ` · ${row.source_warning}` : ""} · {date(row.updated_at * 1000)}</small></div>
        <button disabled={busy} onClick={() => onReviewDrawing(row.id)}>도면 검토 <ArrowRight size={14} /></button></div>)}
    </div>}
    {shown("plans") && visiblePlans.length > 0 && <div className="history-library-section">
      <div className="history-library-section-title"><h3>업무 계획</h3><span>{visiblePlans.length}개 계획 · 버전 {visiblePlans.reduce((n, rows) => n + rows.length, 0)}개</span></div>
      {visiblePlans.map((versions) => <details className="history-library-group" key={versions[0].id}><summary>
        <span className="history-library-title">{versions[0].intent?.goal || "제목 없는 계획"}</span><span>{versions.length}개 버전</span></summary>
        {versions.map((row) => <div className="history-library-row" key={row.version}><div><strong>v{row.version}</strong>
          <small>{row.origin === "model" ? "모델 제안" : "저장된 계획"} · {row.approval ? "승인 기록 있음" : "승인 전"} · {date(row.created_at)}</small></div>
          <button disabled={busy} onClick={() => onOpenPlan(row.id, row.version)}>계획 검토 <ArrowRight size={14} /></button></div>)}
      </details>)}
    </div>}
    {shown("experiments") && visibleExperiments.length > 0 && <div className="history-library-section">
      <div className="history-library-section-title"><h3>실험 결과</h3><span>{visibleExperiments.length}개</span></div>
      {visibleExperiments.map((row) => <details className="history-library-group" key={row.id}><summary>
        <span className="history-library-title">{row.name || "이름 없는 실험"}</span>
        <span>{Array.isArray(row.runs) ? `${row.runs.length}회 실행` : "실행 수 미기록"} · {date(row.created_at)}</span></summary>
        <div className="history-library-row"><span>시드·정책별 결과를 비교할 수 있습니다.</span><button disabled={busy} onClick={onViewExperiments}>결과 보기 <ArrowRight size={14} /></button></div>
        {(row.runs ?? []).map((value, index) => {
          const runId = typeof value.run_id === "string" ? value.run_id : "";
          return <div className="history-library-row" key={runId || index}><div>
            <strong>{typeof value.policy === "string" ? value.policy : "정책 미기록"} · 시드 {typeof value.seed === "number" ? value.seed : "미기록"}</strong>
            <small>이 실행에 저장된 지도·로봇·사람·작업·정책·물리 설정을 다시 사용할 수 있습니다.</small></div>
            <div className="history-library-actions"><button disabled={busy || !runId} onClick={() => onOpenExperimentRun(row.id, runId, false)}>구성 열기</button>
              <button className="primary" disabled={busy || running || !runId} onClick={() => onOpenExperimentRun(row.id, runId, true)}>실행 준비 <ArrowRight size={14} /></button></div>
          </div>;
        })}
      </details>)}
    </div>}
  </section>;
}
