import { useEffect, useRef, useState } from "react";
import { FileUp, Layers3, Plus, RefreshCw, Check, X } from "lucide-react";
import { request } from "./api";
import type { Project } from "./types";
import "./FloorplanPanel.css";

type Candidate = {
  id: string;
  kind: string;
  name: string;
  bbox_px: [number, number, number, number];
  status: "proposed" | "confirmed" | "rejected" | "deferred";
  source: "image_geometry" | "enclosed_geometry" | "model_visual_draft" | "user_added";
  evidence: string;
  served_floors?: number[];
  vertical_link_id?: string;
  connects?: string[];
  clear_width_px?: number;
  clear_opening_bbox_px?: [number, number, number, number];
};
type TextLabel = { text: string; bbox_px: number[]; source?: string; original_text?: string;
  review_status?: "raw" | "confirmed" | "corrected" | "rejected"; review_note?: string };
type Page = {
  number: number;
  width_px: number;
  height_px: number;
  name: string;
  elevation_m: number;
  scale: number | null;
  scale_basis: string;
  calibration?: { pixels: number; metres: number; basis: "drawing" | "measured" | "assumed" | "unknown"; evidence?: string };
  candidates: Candidate[];
  text_labels: TextLabel[];
  visual_draft?: { notes: string; added_candidates: number; added_labels: number; review_required: boolean; original_ocr_status?: string };
  recognized_annotations?: { text: string; bbox_px: number[]; kind: string }[];
  ocr_status?: string;
};
type Floorplan = {
  id: string;
  title: string;
  revision: number;
  review_status: string;
  pages: Page[];
  generated_environment?: {
    revision: number;
    project: Project;
    environment: Project["environment"];
    graph: {
      nodes: { id: string; name: string; kind: string; floor_id: string }[];
      connections: { from_id: string; to_id: string; via: string; width_m: number; condition: string }[];
      isolated_zones?: string[];
      zone_components?: string[][];
      unlinked_apertures?: { id: string; name: string; floor_id: string; reason: string }[];
      overlapping_zones?: { first_id: string; second_id: string; floor_id: string; smaller_covered_ratio: number }[];
    };
  } | null;
  parent_plan_id?: string;
  resumed_from_revision?: number;
  recovered_from?: string;
  recovered_source_missing?: string;
};
type FloorRegion = { bbox_px: [number, number, number, number]; name: string; elevation_m: number };
type FloorplanSummary = { id: string; title: string; revision: number; review_status: string;
  page_count: number; unreviewed: number; deferred: number; generated: boolean;
  image_available: boolean; version_count: number; recovered?: boolean; source_warning?: string };
type FloorplanVersion = { revision: number; review_status: string; unreviewed: number;
  deferred: number; generated: boolean; recovered_from?: string };
const kinds = [
  ["room", "방"], ["corridor", "복도"], ["wall", "벽"], ["door", "문·출입구"], ["opening", "개방 통로"],
  ["stairs", "계단"], ["elevator", "엘리베이터"], ["charger", "충전소"],
  ["dock", "도킹"], ["loading", "하역"],
] as const;
const withCalibration = (plan: Floorplan): Floorplan => ({
  ...plan,
  pages: plan.pages.map((p) => ({
    ...p,
    calibration: p.calibration ?? (p.scale ? { pixels: 100, metres: p.scale * 100, basis: "unknown" } : undefined),
  })),
});
const calibrationSummary = (page: Page): string => {
  if (!page.calibration) return page.scale_basis;
  const labels = {
    drawing: "사용자가 확인한 도면 표기",
    measured: "사용자 제공 실측값",
    assumed: "시험 가정(실측 아님)",
    unknown: "입력 출처 미확인(실측 아님)",
  };
  return `${labels[page.calibration.basis]}: ${page.calibration.pixels} px = ${page.calibration.metres} m` +
    (page.calibration.evidence ? ` · ${page.calibration.evidence}` : "");
};
const errorText = (e: unknown) => e instanceof Error ? e.message : String(e);

export default function FloorplanPanel({ project, onApply, focusDrawing }: {
  project: Project;
  onApply: (next: Project) => Promise<void>;
  focusDrawing?: {id:string; sequence:number} | null;
}) {
  const [plan, setPlan] = useState<Floorplan | null>(null);
  const [list, setList] = useState<FloorplanSummary[]>([]);
  const [versions, setVersions] = useState<FloorplanVersion[]>([]);
  const [pageIndex, setPageIndex] = useState(0);
  const [expanded, setExpanded] = useState(false);
  const [selected, setSelected] = useState("");
  const [kindFilter, setKindFilter] = useState("all");
  const [statusFilter, setStatusFilter] = useState("proposed");
  const [sourceFilter, setSourceFilter] = useState("all");
  const [bulkReason, setBulkReason] = useState("");
  const [visibleCount, setVisibleCount] = useState(40);
  const [labelVisibleCount, setLabelVisibleCount] = useState(30);
  const [selectedLabelIndex, setSelectedLabelIndex] = useState<number | null>(null);
  const [splitOpen, setSplitOpen] = useState(false);
  const [drawingRegion, setDrawingRegion] = useState(false);
  const [floorRegions, setFloorRegions] = useState<FloorRegion[]>([]);
  const [addKind, setAddKind] = useState("room");
  const [adding, setAdding] = useState(false);
  const [calibrating, setCalibrating] = useState(false);
  const [measurePoints, setMeasurePoints] = useState<[number, number][]>([]);
  const [dragStart, setDragStart] = useState<[number, number] | null>(null);
  const [busy, setBusy] = useState("");
  const [dirty, setDirty] = useState(false);
  const [error, setError] = useState("");
  const [notice, setNotice] = useState("");
  const fileRef = useRef<HTMLInputElement>(null);
  const overlayRef = useRef<SVGSVGElement>(null);
  const savedCandidateReviews = useRef(new Map<string, { status: Candidate["status"]; evidence: string }>());
  const candidateDrag = useRef<{ id: string; start: [number, number]; box: Candidate["bbox_px"]; clearBox?: Candidate["bbox_px"]; corner?: string } | null>(null);
  const page = plan?.pages[pageIndex];
  const acceptSavedPlan = (incoming: Floorplan) => {
    const normalized = withCalibration(incoming);
    savedCandidateReviews.current = new Map(normalized.pages.flatMap((sheet) =>
      sheet.candidates.map((candidate) => [`${sheet.number}:${candidate.id}`,
        { status: candidate.status, evidence: candidate.evidence }] as const)));
    setPlan(normalized);
  };

  const refreshList = () => request<FloorplanSummary[]>("/floorplans").then(setList);
  const refreshVersions = (id: string) => request<FloorplanVersion[]>(`/floorplans/${id}/versions`).then(setVersions);
  useEffect(() => { void refreshList().catch(() => {}); }, []);
  const act = async (label: string, fn: () => Promise<void>) => {
    if (busy) return;
    setBusy(label); setError(""); setNotice("");
    try { await fn(); } catch (e) { setError(errorText(e)); } finally { setBusy(""); }
  };
  const updatePage = (patch: Partial<Page>) => {
    setDirty(true);
    setPlan((current) => current ? {
      ...current,
      pages: current.pages.map((p, i) => i === pageIndex ? { ...p, ...patch } : p),
    } : current);
  };
  const updateCandidate = (id: string, patch: Partial<Candidate>) => {
    if (!page) return;
    updatePage({ candidates: page.candidates.map((c) => c.id === id ? { ...c, ...patch } : c) });
  };
  const updateTextLabel = (index: number, patch: Partial<TextLabel>) => {
    if (!page) return;
    updatePage({ text_labels: page.text_labels.map((label, i) => i === index ? { ...label, ...patch } : label) });
  };
  const location = (event: React.PointerEvent<SVGElement>): [number, number] => {
    const point = overlayRef.current!.createSVGPoint();
    point.x = event.clientX; point.y = event.clientY;
    const transformed = point.matrixTransform(overlayRef.current!.getScreenCTM()!.inverse());
    return [Math.max(0, Math.min(page!.width_px, transformed.x)),
            Math.max(0, Math.min(page!.height_px, transformed.y))];
  };
  const addBox = (start: [number, number], end: [number, number]) => {
    if (!page) return;
    const box: Candidate["bbox_px"] = [Math.min(start[0], end[0]), Math.min(start[1], end[1]),
      Math.max(start[0], end[0]), Math.max(start[1], end[1])];
    if (box[2] - box[0] < 5 || box[3] - box[1] < 5) return;
    const id = `user-${Date.now().toString(36)}`;
    updatePage({ candidates: [...page.candidates, {
      id, kind: addKind, name: `${kinds.find(([k]) => k === addKind)?.[1] ?? "객체"} (검토 필요)`,
      bbox_px: box, status: "proposed", source: "user_added",
      evidence: "사용자가 원본 도면 위에서 추가한 후보", served_floors: [], connects: [],
    }] });
    setSelected(id); setAdding(false);
  };
  const beginCandidateDrag = (event: React.PointerEvent<SVGElement>, candidate: Candidate, corner?: string) => {
    if (adding || calibrating || drawingRegion || !overlayRef.current) return;
    event.stopPropagation();
    setSelected(candidate.id);
    candidateDrag.current = { id: candidate.id, start: location(event), box: [...candidate.bbox_px],
      clearBox: candidate.clear_opening_bbox_px ? [...candidate.clear_opening_bbox_px] : undefined, corner };
    overlayRef.current.setPointerCapture(event.pointerId);
  };
  const moveCandidate = (event: React.PointerEvent<SVGSVGElement>) => {
    const drag = candidateDrag.current;
    if (!drag || !page) return;
    const point = location(event);
    const dx = point[0] - drag.start[0], dy = point[1] - drag.start[1];
    const [left, top, right, bottom] = drag.box;
    let box: Candidate["bbox_px"];
    if (drag.corner) {
      box = [left, top, right, bottom];
      if (drag.corner.includes("w")) box[0] = Math.min(right - 5, Math.max(0, left + dx));
      if (drag.corner.includes("e")) box[2] = Math.max(left + 5, Math.min(page.width_px, right + dx));
      if (drag.corner.includes("n")) box[1] = Math.min(bottom - 5, Math.max(0, top + dy));
      if (drag.corner.includes("s")) box[3] = Math.max(top + 5, Math.min(page.height_px, bottom + dy));
    } else {
      const x = Math.max(0, Math.min(page.width_px - (right - left), left + dx));
      const y = Math.max(0, Math.min(page.height_px - (bottom - top), top + dy));
      box = [x, y, x + right - left, y + bottom - top];
    }
    const translatedClearBox = !drag.corner && drag.clearBox
      ? drag.clearBox.map((value,i) => Math.round(value + (i % 2 === 0 ? box[0]-left : box[1]-top))) as Candidate["bbox_px"]
      : undefined;
    updateCandidate(drag.id, { bbox_px: box.map((value) => Math.round(value)) as Candidate["bbox_px"],
      ...(translatedClearBox ? { clear_opening_bbox_px: translatedClearBox } : {}) });
  };
  const addFloorRegion = (start: [number, number], end: [number, number]) => {
    if (!page) return;
    const box: FloorRegion["bbox_px"] = [Math.round(Math.min(start[0],end[0])),Math.round(Math.min(start[1],end[1])),
      Math.round(Math.max(start[0],end[0])),Math.round(Math.max(start[1],end[1]))];
    if (box[2]-box[0]<100 || box[3]-box[1]<100) { setError("층 영역은 가로·세로 100px 이상으로 그리세요."); return; }
    setFloorRegions((rows) => [...rows,{ bbox_px:box,name:`${rows.length+1}층`,elevation_m:rows.length*3.2 }]);
    setDrawingRegion(false);
  };
  const load = async (id: string, reveal = true) => {
    if (dirty) throw new Error("현재 도면 수정이 저장되지 않았습니다. 검토 저장 후 다른 기록을 열어 주세요.");
    acceptSavedPlan(await request<Floorplan>(`/floorplans/${id}`));
    await refreshVersions(id);
    setDirty(false);
    setPageIndex(0); setSelected(""); setMeasurePoints([]); if (reveal) setExpanded(true);
    setKindFilter("all"); setStatusFilter("proposed"); setSourceFilter("all"); setVisibleCount(40);
    setLabelVisibleCount(30);
    setSelectedLabelIndex(null);
    setBulkReason("");
    setSplitOpen(false); setDrawingRegion(false); setFloorRegions([]);
  };
  const openPlan = (id: string) => void act("도면 기록 열기", () => load(id));
  useEffect(() => {
    if (focusDrawing) openPlan(focusDrawing.id);
  }, [focusDrawing?.sequence]);
  useEffect(() => {
    if (focusDrawing) return;
    const id = project.environment.id.startsWith("floorplan-")
      ? project.environment.id.slice("floorplan-".length) : "";
    if (!id) return;
    void load(id, false).catch((e) => setError(`현재 지도의 원본 도면을 열지 못했습니다: ${errorText(e)}`));
  }, [project.environment.id]);
  const upload = (file: File) => act("도면 인식 중", async () => {
    if (file.size > 20_000_000) throw new Error("도면은 20MB 이하여야 합니다.");
    const response = await fetch("/api/floorplans", {
      method: "POST", headers: { "Content-Type": file.type || "application/octet-stream",
        "X-Filename": encodeURIComponent(file.name) }, body: file,
    });
    if (!response.ok) {
      const body = await response.json().catch(() => null);
      throw new Error(body?.detail ?? `도면 등록 실패 (${response.status})`);
    }
    const result = await response.json() as Floorplan;
    acceptSavedPlan(result); setPageIndex(0); setSelected(""); setExpanded(true);
    setDirty(false);
    setKindFilter("all"); setStatusFilter("proposed"); setSourceFilter("all"); setVisibleCount(40);
    setLabelVisibleCount(30);
    setSelectedLabelIndex(null);
    setBulkReason("");
    setSplitOpen(false); setDrawingRegion(false); setFloorRegions([]);
    await refreshList();
    await refreshVersions(result.id);
    setNotice("원본 위 후보를 검토하고 픽셀·미터 비율의 근거를 선택하세요. 시험 가정은 실제 건물 치수가 아닙니다.");
  });
  const saveReview = () => plan && act("검토 저장 중", async () => {
    const payload = { revision: plan.revision, pages: plan.pages.map((p) => ({
      name: p.name, elevation_m: p.elevation_m, calibration: p.calibration ?? null,
      text_labels: p.text_labels.map(({ text, review_status, review_note }) =>
        ({ text, review_status: review_status ?? "raw", review_note: review_note ?? "" })),
      candidates: p.candidates.map(({ id, kind, name, bbox_px, status, source, evidence, served_floors, vertical_link_id, connects, clear_width_px, clear_opening_bbox_px }) =>
        ({ id, kind, name, bbox_px, status, source, evidence, served_floors: served_floors ?? [], connects: connects ?? [],
          ...(vertical_link_id === undefined ? {} : { vertical_link_id }),
          ...(clear_width_px === undefined ? {} : { clear_width_px }),
          ...(clear_opening_bbox_px === undefined ? {} : { clear_opening_bbox_px }) })),
    })) };
    acceptSavedPlan(await request<Floorplan>(`/floorplans/${plan.id}/review`, "PUT", payload));
    setDirty(false);
    await refreshList();
    await refreshVersions(plan.id);
    setNotice("검토 내용을 저장했습니다. 남은 후보는 확정·제외하거나 다음 검토로 분리한 뒤 부분 지도를 만들 수 있습니다.");
  });
  const generate = () => plan && act("공간 그래프와 환경 생성 중", async () => {
    const result = await request<NonNullable<Floorplan["generated_environment"]>>(
      `/floorplans/${plan.id}/generate`, "POST", { revision: plan.revision, project });
    await onApply(result.project);
    setExpanded(false);
    setPlan((p) => p ? { ...p, generated_environment: result } : p);
    await refreshList();
    await refreshVersions(plan.id);
    const deferred = plan.pages.reduce((n,p) => n+p.candidates.filter((c) => c.status === "deferred").length,0);
    setNotice(`환경 초안과 공간 그래프를 적용했습니다. 공간 ${result.graph.nodes.length}개, 검토된 연결 ${result.graph.connections.length}개.${deferred ? ` 미검토 후보 ${deferred}개를 제외한 부분 검토 지도입니다.` : ""} 로봇을 새 지도에 배치한 뒤 계획하세요.`);
  });
  const resumeVersion = (revision: number) => plan && act("이전 도면에서 이어가기", async () => {
    if (dirty) throw new Error("현재 도면 수정을 먼저 저장하세요. 저장하지 않은 내용을 버리지 않습니다.");
    const resumed = await request<Floorplan>(`/floorplans/${plan.id}/versions/${revision}/resume`, "POST");
    acceptSavedPlan(resumed);
    setDirty(false); setExpanded(true); setPageIndex(0); setSelected("");
    await refreshList();
    await refreshVersions(plan.id);
    setNotice(`v${revision} 기록에서 새 검토 버전 v${resumed.revision}을 만들었습니다. 이전 기록은 그대로 남아 있습니다.`);
  });
  const splitFloors = () => plan && page && act("층별 도면 분리 중", async () => {
    const result = await request<Floorplan>(`/floorplans/${plan.id}/split`,"POST",{
      revision:plan.revision,page_number:page.number,regions:floorRegions,
    });
    acceptSavedPlan(result);setPageIndex(0);setSelected("");
    setDirty(false);
    setKindFilter("all");setStatusFilter("proposed");setSourceFilter("all");setVisibleCount(40);
    setBulkReason("");
    setFloorRegions([]);setSplitOpen(false);setDrawingRegion(false);
    await refreshList();
    setNotice(`${floorRegions.length}개 층 영역을 별도 도면으로 만들었습니다. 각 층 후보와 축척을 검토하세요.`);
  });
  const inspectImage = () => plan && page && act("실제 모델로 도면 후보 분석 중", async () => {
    if (dirty) throw new Error("현재 도면 수정을 먼저 저장한 뒤 이미지 분석을 시작하세요.");
    const result = await request<Floorplan>(`/floorplans/${plan.id}/pages/${page.number}/inspect`,"POST",{revision:plan.revision});
    acceptSavedPlan(result);setSelected("");setDirty(false);
    const report=result.pages[pageIndex].visual_draft;
    setNotice(`모델이 객체 ${report?.added_candidates ?? 0}개, 문자 ${report?.added_labels ?? 0}개를 검토 후보로 제안했습니다. 원본과 대조해 확정하거나 제외하세요.`);
  });
  const retryOcr = () => plan && page && act("로컬 문자 인식 다시 시도 중", async () => {
    if (dirty) throw new Error("현재 도면 수정을 먼저 저장한 뒤 문자 인식을 다시 시도하세요.");
    const result = await request<Floorplan>(`/floorplans/${plan.id}/pages/${page.number}/ocr/retry`, "POST", { revision: plan.revision });
    acceptSavedPlan(result);
    setNotice(`${result.pages[pageIndex].ocr_status}. 기존 확정 지도와 후보는 유지했습니다.`);
  });
  const retryGeometry = () => plan && page && act("로컬 형상 다시 분석 중", async () => {
    if (dirty) throw new Error("현재 도면 수정을 먼저 저장한 뒤 형상을 다시 분석하세요.");
    const result = await request<Floorplan>(`/floorplans/${plan.id}/pages/${page.number}/geometry/retry`, "POST", { revision: plan.revision });
    acceptSavedPlan(result);setSelected("");
    const count = result.pages[pageIndex].candidates.filter((c) => c.source === "image_geometry" || c.source === "enclosed_geometry").length;
    setNotice(`로컬 형상 후보 ${count}개를 다시 찾았습니다. 원본과 대조해 각각 확정하거나 제외하세요. 확정 지도와 검토 완료 후보는 자동 변경하지 않습니다.`);
  });
  const current = page?.candidates.find((c) => c.id === selected);
  const savedReview = current && page ? savedCandidateReviews.current.get(`${page.number}:${current.id}`) : undefined;
  const needsReviewEvidence = !!current && savedReview?.status !== "confirmed" &&
    (!current.evidence.trim() || current.evidence.trim() ===
      (savedReview?.evidence.trim() ?? "사용자가 원본 도면 위에서 추가한 후보"));
  const unresolved = plan?.pages.reduce((sum, p) => sum + p.candidates.filter((c) => c.status === "proposed").length, 0) ?? 0;
  const deferredCount = plan?.pages.reduce((sum, p) => sum + p.candidates.filter((c) => c.status === "deferred").length, 0) ?? 0;
  const generated = plan && !dirty && plan.generated_environment &&
    (plan.generated_environment.revision === plan.revision ||
      plan.generated_environment.revision === plan.resumed_from_revision)
    ? plan.generated_environment : null;
  const activeMap = !!generated && project.environment.id === generated.environment.id &&
    project.environment.version === generated.environment.version;
  const floorId = plan && page ? `${plan.id.slice(0,10)}-floor-${page.number}` : "";
  const graphNames = new Map((generated?.graph.nodes ?? []).map((node) => [node.id,node.name]));
  const graphFloor = new Map((generated?.graph.nodes ?? []).map((node) => [node.id,node.floor_id]));
  const floorConnections = (generated?.graph.connections ?? []).filter((edge) =>
    graphFloor.get(edge.from_id) === floorId && graphFloor.get(edge.to_id) === floorId &&
    (edge.condition === "reviewed_door" || edge.condition === "reviewed_opening"));
  const isolatedZones = (generated?.graph.isolated_zones ?? []).filter((id) => graphFloor.get(id) === floorId);
  const floorComponents = (generated?.graph.zone_components ?? [])
    .map((component) => component.filter((id) => graphFloor.get(id) === floorId))
    .filter((component) => component.length > 0);
  const unlinkedApertures = (generated?.graph.unlinked_apertures ?? []).filter((item) => item.floor_id === floorId);
  const overlappingZones = (generated?.graph.overlapping_zones ?? []).filter((item) => item.floor_id === floorId);
  const showSource = (elementId: string) => {
    const candidate = page?.candidates.find((item) => elementId === `${floorId}-${item.id}-0`);
    if (candidate) { setSelected(candidate.id); setStatusFilter("all"); setKindFilter("all"); setSourceFilter("all"); }
  };
  const filteredCandidates = (page?.candidates ?? []).filter((c) =>
    (kindFilter === "all" || c.kind === kindFilter) &&
    (statusFilter === "all" || c.status === statusFilter) &&
    (sourceFilter === "all" || (sourceFilter === "local" ?
      c.source === "image_geometry" || c.source === "enclosed_geometry" : c.source === sourceFilter)));
  const sourceName = (source: Candidate["source"]) => source === "user_added" ? "사용자 추가" :
    source === "model_visual_draft" ? "AI 시각 제안" : "로컬 인식 후보";
  const recognizedNames = (page?.text_labels ?? []).filter((label) =>
    label.review_status !== "rejected" && /[A-Za-z가-힣]{3,}/.test(label.text) && !/^(?:OPTIONAL|TOTAL|SCALE|PLAN|FLOOR|SHEET|NOTES?)\b/i.test(label.text)
  ).slice(0, 40);
  const floorWords=Array.from(new Map((page?.text_labels ?? []).filter((label) =>
    label.review_status !== "rejected" && /\b(?:FIRST|SECOND|THIRD|1ST|2ND|3RD)\s+FLOOR\b|[1-9]층/i.test(label.text)
  ).map((label) => [label.text.trim().toLowerCase(),label])).values());
  return (
    <section className={`floorplan-panel ${expanded ? "is-expanded" : "is-collapsed"}`} aria-label="도면 인식과 공간 검토">
      <header className="floorplan-heading">
        <div><h2><Layers3 size={20} /> 도면에서 공간 만들기</h2>
          <p>{plan ? `${plan.title} · 검토 v${plan.revision}${dirty ? " · 미저장 변경" : ""}` : `PDF·PNG·JPEG 등록 · 저장된 도면 ${list.length}개`}</p></div>
        <div className="floorplan-actions">
          <button aria-expanded={expanded} onClick={() => setExpanded((v) => !v)}>{expanded ? "도면 검토 접기" : "도면 검토 펼치기"}</button>
          <input ref={fileRef} type="file" hidden accept=".pdf,.png,.jpg,.jpeg,application/pdf,image/png,image/jpeg"
            onChange={(e) => { const file = e.target.files?.[0]; if (file) void upload(file); e.target.value = ""; }} />
          <button disabled={!!busy} onClick={() => fileRef.current?.click()}><FileUp size={15} /> 도면 등록</button>
          <button disabled={!!busy} onClick={() => { setExpanded(true); void act("목록 확인 중", refreshList); }}><RefreshCw size={15} /> 목록</button>
        </div>
      </header>
      {error && <p className="notice error" role="alert">{error}</p>}
      {notice && <p className="notice" role="status">{notice}</p>}
      {busy && <p className="notice" role="status">{busy}…</p>}
      {expanded && <>
      <div className="floorplan-history" aria-label="저장된 도면 작업 기록">
        <div className="floorplan-history-heading"><strong>도면 작업 기록</strong><span>{list.length}개 도면 · 원본과 검토 버전 보존</span></div>
        {list.length === 0 ? <p>저장된 도면이 없습니다. PDF 또는 이미지를 등록해 시작하세요.</p> :
          <div className="floorplan-history-list">{list.map((row) =>
            <div className={`floorplan-history-item ${plan?.id === row.id ? "active" : ""}`} key={row.id}>
              <div><strong>{row.title}</strong><small>{row.page_count}개 층 · 최신 v{row.revision} · 기록 {row.version_count}개 · {row.generated ? "지도 생성됨" : "지도 미생성"}</small>
                <small>{row.unreviewed ? `미확정 ${row.unreviewed}개` : "미확정 없음"}{row.deferred ? ` · 보류 ${row.deferred}개` : ""}{!row.image_available ? " · 원본 이미지 없음" : ""}{row.recovered ? " · 검증 기록에서 복원" : ""}</small></div>
              <button type="button" disabled={!!busy || (dirty && plan?.id !== row.id)} onClick={() => openPlan(row.id)}>{plan?.id === row.id ? "열림" : "열기"}</button>
            </div>)}</div>}
        {plan && <details className="floorplan-version-history">
          <summary>{plan.title} · 이전 검토 버전 {versions.length}개</summary>
          <p>이전 버전을 선택하면 기존 기록은 보존하고 새 검토 버전으로 이어갑니다.</p>
          <div className="floorplan-version-list">{versions.map((row) => <div key={row.revision}>
            <span>v{row.revision}{row.revision === plan.revision ? " · 현재" : ""} · {row.generated ? "지도 있음" : "검토 중"} · 미확정 {row.unreviewed} · 보류 {row.deferred}</span>
            <button type="button" disabled={!!busy || dirty || row.revision === plan.revision} onClick={() => void resumeVersion(row.revision)}>이 버전에서 이어하기</button>
          </div>)}</div>
          {plan.generated_environment && <button type="button" disabled={!!busy} onClick={() => void act("저장된 지도 열기", async () => {
            await onApply(plan.generated_environment!.project);
            setNotice(`${plan.title}에서 생성한 지도를 작업 공간에 불러왔습니다.`);
          })}>이 도면의 지도 열기</button>}
        </details>}
      </div>
      <div className="floorplan-toolbar">
        <label>등록한 도면
          <select value={plan?.id ?? ""} onChange={(e) => { if (e.target.value) openPlan(e.target.value); }}>
            <option value="">도면 선택</option>
            {list.map((row) => <option key={row.id} value={row.id}>{row.title} · {row.page_count}쪽</option>)}
          </select>
        </label>
        {plan && <span>검토 버전 {plan.revision} · 미확정 후보 {unresolved}개 · 다음 검토 {deferredCount}개</span>}
        {!!deferredCount && <button type="button" onClick={() => {
          const index=plan!.pages.findIndex((p) => p.candidates.some((c) => c.status === "deferred"));
          if (index < 0) return;
          setPageIndex(index);setSelected(plan!.pages[index].candidates.find((c) => c.status === "deferred")!.id);
          setStatusFilter("deferred");setKindFilter("all");setSourceFilter("all");setVisibleCount(40);
        }}>다음 검토 {deferredCount}개 보기</button>}
      </div>
      {plan && page && <>
        <p className="floorplan-map-version">검토 도면: {plan.title} · v{plan.revision} · {unresolved ? `확정 전 후보 ${unresolved}개` : deferredCount ? `부분 검토 · 다음 검토 ${deferredCount}개` : plan.pages.every((p) => p.candidates.length === 0) ? "인식 후보 없음 · 원본에서 수동 추가 또는 다시 분석 필요" : "후보 검토 완료"}
          <br />현재 작업 지도: {project.environment.name} · v{project.environment.version}
          {generated && <span> · {activeMap ? "이 도면에서 생성됨" : "이 도면의 확정 지도와 다름"}</span>}
        </p>
        {plan.recovered_source_missing && <p className="floorplan-hint">복구 자료: {plan.recovered_source_missing}. 층별 검토 이미지와 확정 지도는 열 수 있으며 PDF 원본 재분석에는 원본 파일이 필요합니다.</p>}
        <nav className="floorplan-pages" aria-label="도면 층">
          {plan.pages.map((p, i) => <button key={p.number} aria-pressed={pageIndex === i} onClick={() => { setPageIndex(i); setSelected(""); setSelectedLabelIndex(null); setBulkReason(""); setMeasurePoints([]); setFloorRegions([]); setSplitOpen(false); }}>{p.name || `${p.number}층`}</button>)}
        </nav>
        <div className="floorplan-edit-grid">
          <div className="floorplan-canvas">
            <img src={`/api/floorplans/${plan.id}/pages/${page.number}/image`} alt={`${page.name} 원본 도면`} />
            <svg ref={overlayRef} viewBox={`0 0 ${page.width_px} ${page.height_px}`} preserveAspectRatio="none"
              onPointerDown={(e) => { if (adding || drawingRegion) { setDragStart(location(e)); e.currentTarget.setPointerCapture(e.pointerId); }
                else if (calibrating) { const next = [...measurePoints, location(e)].slice(-2) as [number, number][]; setMeasurePoints(next);
                  if (next.length === 2) { const d = Math.hypot(next[1][0]-next[0][0], next[1][1]-next[0][1]);
                    if (d > 1) updatePage({ calibration: { pixels: Math.round(d * 100) / 100, metres: page.calibration?.metres ?? 1,
                      basis: page.calibration?.basis ?? "assumed", evidence: page.calibration?.evidence ?? "" } });
                    setCalibrating(false); } } }}
              onPointerMove={moveCandidate}
              onPointerCancel={() => { candidateDrag.current = null; setDragStart(null); }}
              onPointerUp={(e) => { if (candidateDrag.current) { candidateDrag.current = null; return; }
                if (dragStart) { if (drawingRegion) addFloorRegion(dragStart,location(e)); else addBox(dragStart, location(e)); setDragStart(null); } }}>
              {page.candidates.filter((c) => c.id === selected || (c.status !== "rejected" &&
                (statusFilter === "all" || c.status === statusFilter) &&
                (kindFilter === "all" || c.kind === kindFilter) &&
                (sourceFilter === "all" || (sourceFilter === "local" ?
                  c.source === "image_geometry" || c.source === "enclosed_geometry" : c.source === sourceFilter)))).map((c) => <rect key={c.id}
                x={c.bbox_px[0]} y={c.bbox_px[1]} width={c.bbox_px[2]-c.bbox_px[0]} height={c.bbox_px[3]-c.bbox_px[1]}
                className={`floorplan-box ${c.kind} ${c.status} ${selected === c.id ? "selected" : ""}`}
                style={{ pointerEvents: drawingRegion ? "none" : undefined }}
                onPointerDown={(e) => beginCandidateDrag(e,c)}
                onClick={(e) => { if (!adding && !calibrating && !drawingRegion) { e.stopPropagation(); setSelected(c.id); } }} />)}
              {selectedLabelIndex !== null && page.text_labels[selectedLabelIndex] &&
                <rect className="floorplan-label-highlight" pointerEvents="none"
                  x={page.text_labels[selectedLabelIndex].bbox_px[0]}
                  y={page.text_labels[selectedLabelIndex].bbox_px[1]}
                  width={page.text_labels[selectedLabelIndex].bbox_px[2]-page.text_labels[selectedLabelIndex].bbox_px[0]}
                  height={page.text_labels[selectedLabelIndex].bbox_px[3]-page.text_labels[selectedLabelIndex].bbox_px[1]} />}
              {current?.clear_opening_bbox_px && <rect
                x={current.clear_opening_bbox_px[0]} y={current.clear_opening_bbox_px[1]}
                width={current.clear_opening_bbox_px[2]-current.clear_opening_bbox_px[0]}
                height={current.clear_opening_bbox_px[3]-current.clear_opening_bbox_px[1]}
                className="floorplan-clear-opening" pointerEvents="none" />}
              {current && !adding && !calibrating && !drawingRegion && ([
                ["nw",current.bbox_px[0],current.bbox_px[1]],
                ["ne",current.bbox_px[2],current.bbox_px[1]],
                ["sw",current.bbox_px[0],current.bbox_px[3]],
                ["se",current.bbox_px[2],current.bbox_px[3]],
              ] as const).map(([corner,x,y]) => <circle key={corner} className={`floorplan-handle ${corner}`}
                cx={x} cy={y} r="9" onPointerDown={(e) => beginCandidateDrag(e,current,corner)} />)}
              {floorRegions.map((region,i) => <rect key={`region-${i}`} x={region.bbox_px[0]} y={region.bbox_px[1]}
                width={region.bbox_px[2]-region.bbox_px[0]} height={region.bbox_px[3]-region.bbox_px[1]}
                fill="rgba(26,116,128,.08)" stroke="#147480" strokeDasharray="12 8" strokeWidth="4" pointerEvents="none" />)}
              {measurePoints.map(([x,y],i) => <circle key={i} cx={x} cy={y} r="5" fill="#d78025" />)}
              {measurePoints.length === 2 && <line x1={measurePoints[0][0]} y1={measurePoints[0][1]}
                x2={measurePoints[1][0]} y2={measurePoints[1][1]} stroke="#d78025" strokeWidth="3" />}
            </svg>
            <p>{drawingRegion ? "한 층의 평면 범위를 드래그하세요. 이름과 높이를 확인한 뒤 다음 층을 추가합니다." : adding ? "도면 위를 드래그해 새 객체 경계를 그리세요." : calibrating ? "알고 있는 실제 길이의 양 끝점을 클릭하세요." : "후보를 클릭해 원본과 비교하세요. 선택한 상자를 끌어 이동하고 모서리를 끌어 크기를 고칩니다."}</p>
          </div>
          <div className="floorplan-controls">
            <h3>층과 축척</h3>
            <label>층 이름<input value={page.name} onChange={(e) => updatePage({ name: e.target.value })} /></label>
            <label>층 기준 높이 (m) <input type="number" step="0.1" value={page.elevation_m}
              onChange={(e) => updatePage({ elevation_m: Number(e.target.value) })} /></label>
            <p className="floorplan-hint">층고·재질은 도면에서 추정하지 않습니다. 층 높이 기본 3.2m, 벽 높이 기본 2.4m입니다.</p>
            <small>문자 인식: {page.ocr_status ?? "확인 필요"}</small>
            <button disabled={!!busy || dirty} onClick={retryOcr}>로컬 문자 인식 다시 시도</button>
            <button disabled={!!busy || dirty} onClick={retryGeometry}>로컬 벽·공간 후보 다시 찾기</button>
            <button disabled={!!busy || dirty || page.candidates.some((c) => c.source === "model_visual_draft" && c.status === "proposed")}
              onClick={inspectImage}>실제 모델로 이미지 후보 보강</button>
            <p className="floorplan-hint">이미지 OCR이 실패했거나 후보가 부정확할 때 사용하세요. 실제 ChatGPT 로그인과 이미지 지원 모델이 필요하며 결과는 검토 전까지 지도에 적용되지 않습니다.</p>
            {dirty && <p className="floorplan-hint">모델 분석 전에 현재 도면 수정을 저장하세요.</p>}
            {page.visual_draft && <p className="floorplan-hint">AI 시각 제안: 객체 {page.visual_draft.added_candidates}개 · 문자 {page.visual_draft.added_labels}개. {page.visual_draft.notes}</p>}
            {floorWords.length>1 && !plan.parent_plan_id && <p className="notice">원문에 {floorWords.map((w)=>w.text).join(" · ")} 표기가 있습니다. 표제란의 층 목록일 수도 있으니 원본에서 실제 평면이 여러 개인지 확인한 경우에만 영역을 분리하세요. 분리 전에는 한 장을 한 층으로 취급합니다.</p>}
            <details open={splitOpen} onToggle={(e)=>setSplitOpen(e.currentTarget.open)}>
              <summary>한 장에 여러 층이 있을 때 영역 분리</summary>
              <p>층 경계는 원문 문자만으로 추정하지 않습니다. 각 평면의 영역·층 이름·기준 높이를 직접 확인하세요. 원본은 보존됩니다.</p>
              <div className="floorplan-actions">
                <button aria-pressed={drawingRegion} onClick={() => { setDrawingRegion(true); setAdding(false); setCalibrating(false); }}>원본 위에 층 영역 그리기</button>
                <button onClick={() => { const half=Math.round(page.width_px/2); const i=floorRegions.length;
                  setFloorRegions((rows)=>[...rows,{bbox_px:i%2===0?[0,0,half,page.height_px]:[half,0,page.width_px,page.height_px],
                    name:`${i+1}층`,elevation_m:i*3.2}]); }}>좌우 절반 영역 추가</button>
              </div>
              {floorRegions.map((region,i)=><div className="floorplan-region-row" key={i}>
                <label>층 이름<input value={region.name} onChange={(e)=>setFloorRegions((rows)=>rows.map((r,n)=>n===i?{...r,name:e.target.value}:r))} /></label>
                <label>기준 높이 (m)<input type="number" step="0.1" value={region.elevation_m} onChange={(e)=>setFloorRegions((rows)=>rows.map((r,n)=>n===i?{...r,elevation_m:Number(e.target.value)}:r))} /></label>
                {region.bbox_px.map((value,k)=><label key={k}>{["왼쪽","위","오른쪽","아래"][k]} (px)
                  <input type="number" value={value} onChange={(e)=>setFloorRegions((rows)=>rows.map((r,n)=>{
                    if(n!==i)return r; const box=[...r.bbox_px] as FloorRegion["bbox_px"];box[k]=Number(e.target.value);return {...r,bbox_px:box};
                  }))} /></label>)}
                <button onClick={()=>setFloorRegions((rows)=>rows.filter((_,n)=>n!==i))}>영역 삭제</button>
              </div>)}
              <button disabled={!!busy || floorRegions.length<2} onClick={splitFloors}>선택한 {floorRegions.length}개 층으로 분리</button>
            </details>
            {!!page.recognized_annotations?.length && <details><summary>도면의 치수·축척 표기 {page.recognized_annotations.length}개</summary>
              <ul>{page.recognized_annotations.map((a,i) => <li key={i}>{a.text} · 픽셀 위치 {Math.round(a.bbox_px[0])}, {Math.round(a.bbox_px[1])}</li>)}</ul>
              <p>표기만 인식했습니다. 대응하는 선분을 확인해 아래에서 실제 길이로 보정하세요.</p>
            </details>}
            {!!recognizedNames.length && <details><summary>원문에서 읽은 공간·시설 이름 {recognizedNames.length}개</summary>
              <ul>{recognizedNames.map((label,i) => <li key={i}>{label.text} · 픽셀 위치 {Math.round(label.bbox_px[0])}, {Math.round(label.bbox_px[1])}{label.source === "model_visual_draft" ? " · AI 제안, 원문 대조 필요" : ""}</li>)}</ul>
              <p>문자만으로 방 경계나 출입구를 확정하지 않습니다. 원본에서 위치를 확인하고 후보를 검토하거나 직접 그리세요.</p>
            </details>}
            {!!page.text_labels.length && <details className="floorplan-label-review">
              <summary>읽은 문자 정정·제외 · {page.text_labels.filter((label) => label.review_status && label.review_status !== "raw").length}/{page.text_labels.length}개 판정</summary>
              <p>오독·중복은 원본과 비교해 수정하거나 제외하세요. 인식 원문은 보존되며, 문자를 고쳐도 벽·문·경로가 자동 확정되지는 않습니다.</p>
              {page.text_labels.slice(0,labelVisibleCount).map((label,index) => <div className="floorplan-label-row" key={index}>
                <small>{label.source === "model_visual_draft" ? "AI 시각 제안" : "로컬 문자 인식"} · 원본 {label.original_text ?? label.text} · 위치 {Math.round(label.bbox_px[0])}, {Math.round(label.bbox_px[1])} px</small>
                <button type="button" aria-pressed={selectedLabelIndex === index}
                  onClick={() => { setSelectedLabelIndex(index); overlayRef.current?.scrollIntoView({block:"center"}); }}>원본 위치 보기</button>
                <label>검토할 문자<input maxLength={160} value={label.text}
                  onChange={(e) => { const original=label.original_text ?? label.text;
                    updateTextLabel(index,{ text:e.target.value,original_text:original,
                      review_status:e.target.value === original
                        ? label.review_status && label.review_status !== "raw" ? "confirmed" : "raw"
                        : "corrected" }); }} /></label>
                <label>판정<select value={label.review_status ?? "raw"}
                  onChange={(e) => updateTextLabel(index,{ review_status:e.target.value as TextLabel["review_status"] })}>
                    <option value="raw" disabled={!!label.review_status && label.review_status !== "raw"}>검토 전</option><option value="confirmed">원문 확인</option>
                    <option value="corrected">오독 수정</option><option value="rejected">중복·오검출 제외</option>
                  </select></label>
                {label.review_status && label.review_status !== "raw" &&
                  <label>원본 대조·판정 이유<input maxLength={400} value={label.review_note ?? ""}
                    placeholder="예: 원본에는 ROOM B로 인쇄됨 / 같은 글자가 겹쳐 두 번 검출됨"
                    onChange={(e) => updateTextLabel(index,{ review_note:e.target.value })} /></label>}
              </div>)}
              {page.text_labels.length>labelVisibleCount && <button onClick={() => setLabelVisibleCount((count) => count+30)}>
                문자 더 보기 · {page.text_labels.length-labelVisibleCount}개 남음
              </button>}
              <p>정정·제외 뒤 상단의 검토 저장을 누르면 치수 표기와 공간 이름 목록에 반영됩니다. 공간 후보 이름은 별도로 검토하세요.</p>
            </details>}
            <div className="floorplan-calibration">
              <button aria-pressed={calibrating} onClick={() => { setCalibrating(true); setAdding(false); setMeasurePoints([]); }}>두 점으로 픽셀 거리 재기</button>
              <label>도면 거리 (px)<input type="number" min="1" step="0.01" value={page.calibration?.pixels ?? ""}
                onChange={(e) => updatePage({ calibration: { pixels: Number(e.target.value), metres: page.calibration?.metres ?? 1,
                  basis: page.calibration?.basis ?? "assumed", evidence: page.calibration?.evidence ?? "" } })} /></label>
              <label>입력한 길이 (m)<input type="number" min="0.01" step="0.01" value={page.calibration?.metres ?? ""}
                onChange={(e) => updatePage({ calibration: { pixels: page.calibration?.pixels ?? 100, metres: Number(e.target.value),
                  basis: page.calibration?.basis ?? "assumed", evidence: page.calibration?.evidence ?? "" } })} /></label>
              <label>길이의 근거<select value={page.calibration?.basis ?? "assumed"}
                onChange={(e) => updatePage({ calibration: { pixels: page.calibration?.pixels ?? 100,
                  metres: page.calibration?.metres ?? 1, basis: e.target.value as NonNullable<Page["calibration"]>["basis"],
                  evidence: page.calibration?.evidence ?? "" } })}>
                <option value="assumed">시험 가정 · 실제 건물 치수 아님</option>
                <option value="drawing">원본 도면 표기와 대조</option>
                <option value="measured">사용자 제공 실측값</option>
                <option value="unknown">출처 미확인 · 실제 치수 아님</option>
              </select></label>
              {(page.calibration?.basis === "drawing" || page.calibration?.basis === "measured") &&
                <label>근거 위치·출처 (필수)<input maxLength={200} value={page.calibration.evidence ?? ""}
                  placeholder="예: 1쪽 북측 치수선 / 현장 실측 기록"
                  onChange={(e) => updatePage({ calibration: { ...page.calibration!, evidence: e.target.value } })} /></label>}
              <small>{calibrationSummary(page)}{dirty ? " · 저장 전" : ""}</small>
            </div>
            {generated && <details className="floorplan-graph" open={floorComponents.length>1 || isolatedZones.length>0 || unlinkedApertures.length>0 || overlappingZones.length>0}>
              <summary>확정 공간 연결 · 이 층 {floorConnections.length}개 · 단독 공간 {generated.graph.isolated_zones ? `${isolatedZones.length}개` : "진단 갱신 필요"}
                {generated.graph.zone_components && ` · 연결 묶음 ${floorComponents.length}개`}</summary>
              <p>검토한 문과 개방 통로만 연결합니다. 이 그래프는 공간 간 통행 근거이며, 실제 로봇 통과는 주변 벽·개구부·본체 크기를 포함해 계획 때 별도 확인합니다. 현재 지도에 사용 중인 도면인지 위 버전을 확인하세요.</p>
              {!generated.graph.isolated_zones && <p>이 지도는 연결 진단 기능 추가 전에 생성됐습니다. 최신 검토 버전에서 지도·그래프를 다시 생성하면 연결되지 않은 공간을 확인할 수 있습니다.</p>}
              {floorComponents.length>1 && <div><strong>같은 층의 서로 연결되지 않은 공간 묶음</strong>
                <p>각 묶음 안에는 검토한 출입구 연결이 있지만, 다른 묶음으로 가는 통로는 확정되지 않았습니다. 원본에서 벽·문·개방 통로를 확인하세요. 가까운 거리만으로 연결하지 않습니다.</p>
                <ul>{floorComponents.map((component, index) => <li key={component.join(':')}>
                  <span>묶음 {index+1} · {component.map((id) => graphNames.get(id) ?? id).join(' · ')}</span>
                  <button onClick={() => showSource(component[0])}>원본 공간 보기</button>
                </li>)}</ul></div>}
              {floorConnections.length>0 && <ul>{floorConnections.map((edge) => <li key={edge.via}>
                <span>{graphNames.get(edge.from_id)} ↔ {graphNames.get(edge.to_id)} · {edge.condition === "reviewed_door" ? "문" : "개방 통로"} · 폭 {edge.width_m.toFixed(2)} m</span>
                <button onClick={() => showSource(edge.via)}>원본 위치·근거 보기</button>
              </li>)}</ul>}
              {isolatedZones.length>0 && <div><strong>다른 확정 공간과 연결되지 않음</strong>
                <ul>{isolatedZones.map((id) => <li key={id}><span>{graphNames.get(id)} · 출입구를 확인하기 전에는 다른 공간에서 접근할 수 없습니다</span>
                  <button onClick={() => showSource(id)}>공간 보기</button></li>)}</ul></div>}
              {unlinkedApertures.length>0 && <div><strong>연결을 만들지 못한 출입구</strong>
                <ul>{unlinkedApertures.map((item) => <li key={item.id}><span>{item.name} · {item.reason}</span>
                  <button onClick={() => showSource(item.id)}>위치 수정</button></li>)}</ul></div>}
              {overlappingZones.length>0 && <div><strong>겹치는 확정 공간 · 경계 검토 필요</strong>
                <p>작은 공간의 80% 이상이 다른 방·복도 상자에 들어갑니다. 두 공간의 벽·문을 확인하기 전에는 겹침만으로 통행을 허용하지 않습니다.</p>
                <ul>{overlappingZones.map((item) => <li key={`${item.first_id}:${item.second_id}`}>
                  <span>{graphNames.get(item.first_id)} ↔ {graphNames.get(item.second_id)} · 작은 공간의 {Math.round(item.smaller_covered_ratio*100)}% 겹침</span>
                  <button onClick={() => showSource(item.second_id)}>원본 경계 보기</button>
                </li>)}</ul></div>}
            </details>}
            <h3>인식 후보 · {page.candidates.length}개</h3>
            <div className="floorplan-candidate-filters">
              <label>종류<select value={kindFilter} onChange={(e) => { setKindFilter(e.target.value); setVisibleCount(40); }}>
                <option value="all">모든 종류</option>
                {kinds.map(([key,label]) => <option key={key} value={key}>{label}</option>)}
              </select></label>
              <label>검토 상태<select value={statusFilter} onChange={(e) => { setStatusFilter(e.target.value); setVisibleCount(40); }}>
                <option value="proposed">검토 필요</option><option value="confirmed">확정</option>
                <option value="rejected">제외</option><option value="deferred">다음 검토</option><option value="all">전체</option>
              </select></label>
              <label>후보 출처<select value={sourceFilter} onChange={(e) => { setSourceFilter(e.target.value); setVisibleCount(40); }}>
                <option value="all">모든 출처</option><option value="local">로컬 인식</option>
                <option value="model_visual_draft">AI 시각 제안</option><option value="user_added">사용자 추가</option>
              </select></label>
            </div>
            <p className="floorplan-hint">현재 층: 검토 필요 {page.candidates.filter((c) => c.status === "proposed").length}개 · 확정 {page.candidates.filter((c) => c.status === "confirmed").length}개 · 제외 {page.candidates.filter((c) => c.status === "rejected").length}개 · 다음 검토 {page.candidates.filter((c) => c.status === "deferred").length}개 · 현재 필터 {filteredCandidates.length}개</p>
            <div className="floorplan-add">
              <select value={addKind} onChange={(e) => setAddKind(e.target.value)} aria-label="추가할 객체 종류">
                {kinds.map(([key,label]) => <option key={key} value={key}>{label}</option>)}
              </select>
              <button aria-pressed={adding} onClick={() => { setAdding(true); setCalibrating(false); }}><Plus size={14} /> 원본 위에 추가</button>
            </div>
            <div className="floorplan-candidate-list">
              {filteredCandidates.slice(0,visibleCount).map((c) => <button key={c.id} className={selected === c.id ? "selected" : ""}
                onClick={() => setSelected(c.id)}><span>{c.name}</span><small>{kinds.find(([k]) => k === c.kind)?.[1]} · {c.status === "confirmed" ? "확정" : c.status === "rejected" ? "제외" : c.status === "deferred" ? "다음 검토" : "검토 필요"} · {sourceName(c.source)}</small></button>)}
            </div>
            {filteredCandidates.length > visibleCount && <button onClick={() => setVisibleCount((n) => n + 40)}>
              후보 더 보기 · {filteredCandidates.length-visibleCount}개 남음
            </button>}
            {current && <div className="floorplan-inspector">
              <h4>선택 객체 검토</h4>
              <label>종류<select value={current.kind} onChange={(e) => updateCandidate(current.id,{ kind: e.target.value })}>
                {kinds.map(([key,label]) => <option key={key} value={key}>{label}</option>)}</select></label>
              <label>이름<input value={current.name} onChange={(e) => updateCandidate(current.id,{ name: e.target.value })} /></label>
              <div className="floorplan-box-inputs">{current.bbox_px.map((v,i) => <label key={i}>{["왼쪽","위","오른쪽","아래"][i]}
                <input type="number" value={Math.round(v)} onChange={(e) => { const box = [...current.bbox_px] as Candidate["bbox_px"]; box[i] = Number(e.target.value); updateCandidate(current.id,{ bbox_px: box }); }} /></label>)}</div>
              {(current.kind === "stairs" || current.kind === "elevator") && <div className="floorplan-connection-choice">
                <label>연결 층 번호 (쉼표 구분)
                  <input value={(current.served_floors ?? []).join(",")}
                    onChange={(e) => updateCandidate(current.id,{ served_floors: e.target.value.split(",").map(Number).filter((n) => Number.isInteger(n) && n > 0) })} /></label>
                <label>다른 층의 같은 시설을 잇는 이름
                  <input maxLength={100} value={current.vertical_link_id ?? ""} placeholder="예: 중앙 홀 계단 A"
                    onChange={(e) => updateCandidate(current.id,{ vertical_link_id: e.target.value })} /></label>
                <p>원본에서 같은 계단·승강기임을 확인한 양쪽 후보에 같은 연결 이름과 층 번호를 입력하세요. 시설 연결과 로봇의 실제 층간 이동 지원은 별도로 검사합니다.</p>
              </div>}
              {(current.kind === "door" || current.kind === "opening") && <div className="floorplan-connection-choice">
                <strong>통행으로 연결할 공간</strong>
                <p>원본과 대조해 양쪽 방·복도를 지정하세요. 위치가 두 공간 모두와 닿지 않으면 그래프에 연결하지 않습니다.</p>
                <label>원본에서 확인한 실제 개구 폭 (px)
                  <input type="number" min="0.1" step="0.1" value={current.clear_width_px ?? ""}
                    placeholder="상자 크기로 추정"
                    onChange={(e) => updateCandidate(current.id,{ clear_width_px: e.target.value === "" ? undefined : Number(e.target.value) })} />
                </label>
                <p>문짝 회전선까지 포함된 후보 상자는 실제 통과 폭보다 클 수 있습니다. 원본의 벽 사이 빈 폭을 입력하세요.
                  {current.clear_width_px !== undefined && page.calibration && page.calibration.pixels > 0 &&
                    ` 현재 입력 축척 기준 ${(current.clear_width_px * page.calibration.metres / page.calibration.pixels).toFixed(2)} m · ${calibrationSummary(page)}`}</p>
                <label className="floorplan-opening-toggle"><input type="checkbox"
                  checked={current.clear_opening_bbox_px !== undefined}
                  disabled={current.clear_width_px === undefined && current.clear_opening_bbox_px === undefined}
                  onChange={(e) => updateCandidate(current.id,{ clear_opening_bbox_px: e.target.checked ? [...current.bbox_px] : undefined })} />
                  원본에서 확인한 빈 개구의 위치도 지정 · 먼저 통과 폭 입력</label>
                {current.clear_opening_bbox_px && <>
                  <p>초록 테두리가 실제 빈 개구입니다. 문 기호 상자 안에서 벽 끝에 맞춰 수정하세요. 세로 벽은 개구의 위아래 길이, 가로 벽은 좌우 길이가 입력 폭과 같아야 합니다.</p>
                  <div className="floorplan-box-inputs">{current.clear_opening_bbox_px.map((v,i) => <label key={i}>{["개구 왼쪽","개구 위","개구 오른쪽","개구 아래"][i]} (px)
                    <input type="number" value={v} onChange={(e) => { const box=[...current.clear_opening_bbox_px!] as Candidate["bbox_px"];
                      box[i]=Number(e.target.value); updateCandidate(current.id,{ clear_opening_bbox_px: box }); }} /></label>)}</div>
                </>}
                {([0,1] as const).map((index) => <label key={index}>{index === 0 ? "공간 A" : "공간 B"}
                  <select value={current.connects?.[index] ?? ""} onChange={(e) => {
                    const next=[current.connects?.[0] ?? "",current.connects?.[1] ?? ""];
                    next[index]=e.target.value;
                    updateCandidate(current.id,{connects: next[0] || next[1] ? next : []});
                  }}>
                    <option value="">{index===0 ? "자동 판정 또는 공간 선택" : "공간 선택"}</option>
                    {page.candidates.filter((c) => c.status === "confirmed" && (c.kind === "room" || c.kind === "corridor"))
                      .map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}
                  </select></label>)}
                {!!current.connects?.length && <button onClick={() => updateCandidate(current.id,{connects: []})}>자동 판정으로 되돌리기</button>}
              </div>}
              <label>{current.status === "deferred" ? "보류 이유와 판단에 필요한 원본 자료" : "검토 근거·보정 메모"}
                <textarea maxLength={400} rows={2} value={current.evidence}
                  placeholder={current.status === "deferred" ? "예: 벽 끝과 빈 개구 폭이 불명확함 · 필요한 자료: 고해상도 원도면과 문 치수" : "원본에서 확인한 위치·형상과 보정 이유"}
                  onChange={(e) => updateCandidate(current.id,{ evidence: e.target.value })} />
              </label>
              {needsReviewEvidence && <p className="floorplan-hint">확정하려면 원본에서 확인한 위치·형상과 수정 이유를 적어 주세요. 근거가 부족하면 다음 검토로 남길 수 있습니다.</p>}
              <small>원래 후보 출처: {sourceName(current.source)} · 확정 전 원본 도면과 비교하세요.</small>
              <div className="floorplan-actions">
                <button disabled={needsReviewEvidence} onClick={() => updateCandidate(current.id,{ status: "confirmed" })}><Check size={14} /> 확정</button>
                <button onClick={() => updateCandidate(current.id,{ status: "rejected" })}><X size={14} /> 제외</button>
                <button onClick={() => updateCandidate(current.id,{ status: "deferred" })}>다음 검토</button>
                <button onClick={() => updateCandidate(current.id,{ status: "proposed" })}>재검토</button>
              </div>
            </div>}
            {page.candidates.some((c) => c.status === "proposed") && <div className="floorplan-bulk-exclude">
              <label>현재 층에서 남은 후보를 처리하는 이유
                <input maxLength={180} value={bulkReason} onChange={(e) => setBulkReason(e.target.value)}
                  placeholder="예: 이번 지도는 중앙·오른쪽 통로만 검토하며 나머지는 다음 검토로 남김" />
              </label>
              <button disabled={!bulkReason.trim()} onClick={() => { const reason=bulkReason.trim();
                updatePage({ candidates: page.candidates.map((c) => c.status === "proposed" ? {
                  ...c, status: "rejected", evidence: `${c.evidence} · 검토 제외: ${reason}`.slice(0,400),
                } : c) }); setBulkReason(""); }}>
                현재 층의 남은 미검토 후보 {page.candidates.filter((c) => c.status === "proposed").length}개 제외
              </button>
              <button disabled={!bulkReason.trim()} onClick={() => { const reason=bulkReason.trim();
                updatePage({ candidates: page.candidates.map((c) => c.status === "proposed" ? {
                  ...c, status: "deferred", evidence: `${c.evidence} · 다음 검토: ${reason}`.slice(0,400),
                } : c) }); setBulkReason(""); }}>
                현재 층의 남은 후보 {page.candidates.filter((c) => c.status === "proposed").length}개 다음 검토로 남기기
              </button>
            </div>}
            <div className="floorplan-actions floorplan-finish">
              <button disabled={!!busy} onClick={saveReview}>검토 저장</button>
              <button disabled={!!busy || unresolved > 0 || plan.pages.some((p) => !p.calibration)} onClick={generate}>지도·그래프 생성해 초안에 적용</button>
            </div>
          </div>
        </div>
      </>}
      </>}
    </section>
  );
}
