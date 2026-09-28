/** @jsxImportSource react */
import { useEffect, useState } from "react";
import { BookOpen, RefreshCw, Search } from "lucide-react";
import { request } from "./api";
import { safeExternalUrl } from "./assistantConnection";

export type CapabilitySupport = {
  document_confirmed: boolean;
  structured: boolean;
  simulation_connected: boolean;
  manual_simulation_connected?: boolean;
  adapter_connected: boolean;
  simulation_verified: boolean;
  hardware_verified: boolean;
};
export type CapabilityEvidence = {
  document_id: string;
  title: string;
  section?: string;
  line_start?: number;
  line_end?: number;
  quote?: string;
  source_url?: string;
};
export type OntologyCapability = {
  id: string;
  document_id: string;
  model_id: string;
  version: string;
  document_provenance?: string;
  document_scope?: string;
  key: string;
  name: string;
  meaning: string;
  parameters: {
    name: string;
    type?: string;
    unit?: string;
    minimum?: number | null;
    maximum?: number | null;
    required?: boolean;
  }[];
  inputs: unknown;
  outputs: unknown;
  preconditions: unknown;
  dependencies: unknown;
  constraints: unknown;
  failures: unknown;
  recovery: unknown;
  sdk_mapping: unknown;
  extraction_method: string;
  review_status?: "draft" | "confirmed" | "rejected" | "merged" | "insufficient";
  review_note?: string;
  merge_into?: string | null;
  assertion: "document_explicit" | "inferred";
  evidence: CapabilityEvidence;
  support: CapabilitySupport;
  active_execution?: boolean;
  binding?: { simulation?: unknown; simulation_manual?: unknown; adapter?: unknown; review_basis?: unknown };
  conflicts: { capability_id: string; version: string; reason: string }[];
  verification?: {
    scope: string;
    records: {
      record_id: string;
      run_id: string;
      task_id: string;
      robot_id: string;
      plan_id: string;
      plan_version: number;
      completed_at: number;
      time_basis: string;
      conditions: {
        physics?: { seed?: number };
        robot?: unknown;
        [key: string]: unknown;
      };
      outcome_metrics: {
        collisions?: number;
        near_misses?: number;
        failed?: number;
        falls?: number;
        damaged_items?: number;
      };
      scope: string;
    }[];
  };
};
type OntologyDocument = {
  id: string;
  title: string;
  model_id: string;
  version: string;
  source_url?: string;
  provenance: string;
  sha256: string;
  analyzed: boolean;
  scope?: unknown;
  text?: string;
  has_source_pdf?: boolean;
  source_import?: { format: string; source_sha256: string; basis: string;
    pages: { page: number; status: string; characters: number; extraction: string; reason?: string | null }[] };
  reviewed_facts?: { id: string; kind: string; statement: string; quote: string;
    line_start: number; line_end: number; source_sha256: string }[];
  review_coverage?: {
    candidate_count: number;
    reviewed_count: number;
    status_counts: Record<string, number>;
    unextracted: { section: string; reason: string }[];
    model_processed_characters?: number | null;
    model_total_characters?: number | null;
  };
};
function DocumentFacts({ document, disabled, onSaved }: {
  document: OntologyDocument; disabled: boolean; onSaved: (snapshot: OntologySnapshot) => void;
}) {
  const [kind, setKind] = useState("specification");
  const [statement, setStatement] = useState("");
  const [quote, setQuote] = useState("");
  const [error, setError] = useState("");
  const kinds: Record<string, string> = { specification:"수치·장비 사양", condition:"전제 조건", constraint:"운용 제약", version:"문서 버전", marketing:"홍보·용례" };
  return <details className="ontology-document-source">
    <summary>이 문서의 사양·조건·제약 검토 · {document.reviewed_facts?.length ?? 0}건</summary>
    <p>원문 구절과 대조해 기록합니다. 이 기록은 로봇 실행 기능이나 어댑터 연결을 부여하지 않습니다.</p>
    {document.reviewed_facts?.map((fact) => <details key={fact.id}>
      <summary>{kinds[fact.kind] ?? fact.kind} · {fact.statement}</summary>
      <p>원문 {fact.line_start}–{fact.line_end}행 · 문서 지문 {fact.source_sha256.slice(0,12)}</p>
      <blockquote>{fact.quote}</blockquote>
    </details>)}
    {error && <p className="notice error" role="alert">{error}</p>}
    <label>구분<select value={kind} onChange={(e) => setKind(e.target.value)}>{Object.entries(kinds).map(([value,label]) =>
      <option key={value} value={value}>{label}</option>)}</select></label>
    <label>검토 내용<input value={statement} onChange={(e) => setStatement(e.target.value)} /></label>
    <label>원문 근거 구절<textarea rows={3} value={quote} onChange={(e) => setQuote(e.target.value)} /></label>
    <button disabled={disabled || !statement.trim() || !quote.trim()} onClick={() => void request<OntologySnapshot>(
      `/ontology/documents/${document.id}/facts`,"PUT",{kind,statement,quote}).then((next) => {
        onSaved(next);setStatement("");setQuote("");setError("");
      }).catch((e) => setError(e instanceof Error ? e.message : String(e)))}>원문 대조 기록</button>
  </details>;
}
export type OntologySnapshot = {
  revision: string | number;
  documents: OntologyDocument[];
  capabilities: OntologyCapability[];
  documentation_models?: { id: string; name: string; status: string }[];
  coverage: {
    document_count: number;
    capability_count: number;
    unextracted: { document_id: string; section: string; reason: string }[];
    execution_unlinked: string[];
    manufacturer_evidence_missing: string[];
  };
};
export type PlanOntology = {
  revision: string | number;
  capabilities: OntologyCapability[];
  limitations: string[];
};
const supportNames: [keyof CapabilitySupport, string][] = [
  ["document_confirmed", "문서 확인"],
  ["structured", "온톨로지 구조화"],
  ["simulation_connected", "시뮬레이션 연결"],
  ["manual_simulation_connected", "시뮬레이션 수동 명령 연결"],
  ["adapter_connected", "실물 어댑터 연결"],
  ["simulation_verified", "시뮬레이션 검증"],
  ["hardware_verified", "실물 검증"],
];
const reviewedSimulationContracts: Record<string, { label: string; models: string[]; scope: string }> = {
  patrol: { label: "순찰", models: ["spot", "amr", "agv", "delivery", "mobile_manipulator"],
    scope: "승인한 목적지로 이동·체류합니다. 문서의 자동 데이터 수집과 실물 주행은 포함하지 않습니다." },
  transport: { label: "협업 운반", models: ["amr", "agv", "delivery", "logistics", "mobile_manipulator"],
    scope: "물품을 싣고 인수 로봇에게 넘기는 협업 작업의 운반 역할에만 연결됩니다. 단독 상하차는 포함하지 않습니다." },
  manipulate: { label: "협업 조작", models: ["arm", "mobile_manipulator"],
    scope: "물품 관측·접촉·작업 반경을 검사하는 협업 작업의 인수·제공 역할에만 연결됩니다." },
};
const provenanceNames: Record<string, string> = {
  user_supplied: "사용자가 등록한 문서",
  official_sdk_docstrings: "공식 SDK 설명에서 확보한 원문",
  project_authored_technical_document: "프로젝트에서 작성한 연구 기술 문서",
};
const extractionNames: Record<string, string> = {
  document_capability_block: "문서의 명시적 기능 블록",
  exact_sdk_section: "검토한 SDK 절",
  structured_document: "구조화 문서",
  manual_heading_draft: "일반 문서의 기능 절 · 사용자 검토 필요",
  pdf_prose_heading_draft: "PDF 서술 절 · 사용자 검토 필요",
  codex_manual_draft: "실제 모델 제안 · 원문 대조 필요",
};
const describe = (value: unknown): string => {
  if (value === null || value === undefined || value === "")
    return "명시되지 않음";
  if (typeof value === "string") return value;
  if (Array.isArray(value))
    return value.length ? value.map(describe).join(" · ") : "명시되지 않음";
  return typeof value === "object" ? JSON.stringify(value) : String(value);
};
export function CapabilityEvidenceView({
  evidence,
}: {
  evidence: CapabilityEvidence;
}) {
  const url = safeExternalUrl(evidence.source_url);
  return (
    <div className="ontology-evidence">
      <strong>{evidence.title}</strong>
      <span>
        {[
          evidence.section,
          evidence.line_start
            ? `원문 ${evidence.line_start}${evidence.line_end && evidence.line_end !== evidence.line_start ? `–${evidence.line_end}` : ""}행`
            : "",
        ]
          .filter(Boolean)
          .join(" · ")}
      </span>
      {evidence.quote && <blockquote>{evidence.quote}</blockquote>}
      {url && (
        <a href={url} target="_blank" rel="noreferrer">
          출처 문서 열기
        </a>
      )}
    </div>
  );
}
export function CapabilitySupportView({
  support,
}: {
  support: CapabilitySupport;
}) {
  return (
    <ul className="ontology-support" aria-label="기능 지원 단계">
      {supportNames.map(([key, name]) => (
        <li className={support[key] ? "confirmed" : "unconfirmed"} key={key}>
          <span aria-hidden="true">{support[key] ? "✓" : "—"}</span> {name}:{" "}
          {support[key] ? "확인됨" : "미확인"}
        </li>
      ))}
    </ul>
  );
}
export function CapabilityDetails({
  capability: c,
  selectedElsewhere = false,
  mergeTargetName,
}: {
  capability: OntologyCapability;
  selectedElsewhere?: boolean;
  mergeTargetName?: string;
}) {
  const provenance = c.document_provenance === "project_authored_technical_document"
    ? "프로젝트 연구용 실행 계약 · 제조사 기능 근거 아님"
    : c.document_provenance === "official_sdk_docstrings"
      ? "공식 SDK 문서 발췌 · 선택한 API 범위"
      : "사용자 등록 문서 · 출처와 버전 검토 필요";
  return (
    <details className="ontology-capability">
      <summary>
        <strong>{c.name || c.key}</strong>
        <span>
          {c.model_id} · {c.version} · {provenance} ·{" "}
          {c.review_status === "merged" ? "중복 병합 · 원본 기능에서 확인" :
            c.review_status === "rejected" ? "검토 제외 · 실행 불가" :
            c.review_status === "insufficient" ? "근거 부족 · 실행 불가" :
            c.review_status === "draft" ? "검토 필요 · 실행 불가" :
            c.support.simulation_connected ? selectedElsewhere ? "실행 연결됨 · 다른 문서가 배정 근거" :
            c.active_execution ? "실행 연결됨 · 배정 근거로 선택" : "시뮬레이션 연결" :
            c.support.manual_simulation_connected ? "연구용 수동 명령 연결 · 자동 작업 배정 제외" : "실행 미연결"}
        </span>
      </summary>
      <p>{c.meaning}</p>
      {c.document_scope && <p className="ontology-provenance">문서 범위: {c.document_scope}</p>}
      <p className="ontology-provenance">
        {c.assertion === "document_explicit"
          ? "등록 문서에 명시된 내용"
          : "추정 내용 · 확인 필요"}{" "}
        · 추출 방법:{" "}
        {extractionNames[c.extraction_method] ?? c.extraction_method}
      </p>
      {c.review_status && <p className="ontology-provenance">검토 상태: {({draft:"검토 필요",confirmed:"확정",rejected:"제외",merged:"중복 병합",insufficient:"근거 부족"} as Record<string,string>)[c.review_status] ?? c.review_status}
        {c.review_note ? ` · ${c.review_note}` : ""}{c.merge_into ? ` · 병합 대상 ${mergeTargetName ?? "같은 문서의 확정 기능"}` : ""}</p>}
      <CapabilitySupportView support={c.support} />
      {c.parameters?.length > 0 && (
        <div className="ontology-table-wrap">
          <table>
            <caption>입력 매개변수와 허용 범위</caption>
            <thead>
              <tr>
                <th>이름</th>
                <th>형식 / 단위</th>
                <th>허용 범위</th>
                <th>필수</th>
              </tr>
            </thead>
            <tbody>
              {c.parameters.map((p) => (
                <tr key={p.name}>
                  <td>{p.name}</td>
                  <td>
                    {p.type ?? "—"} / {p.unit ?? "—"}
                  </td>
                  <td>
                    {p.minimum ?? "제한 미명시"} ~ {p.maximum ?? "제한 미명시"}
                  </td>
                  <td>{p.required ? "필수" : "선택"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
      <dl className="ontology-properties">
        {[
          ["입력", c.inputs],
          ["출력", c.outputs],
          ["선행 조건", c.preconditions],
          ["의존 기능", c.dependencies],
          ["실행 제약", c.constraints],
          ["실패 조건", c.failures],
          ["복구 조건", c.recovery],
          ["SDK / 명령", c.sdk_mapping],
          ["시뮬레이션 실행부", c.binding?.simulation],
          ["연구용 수동 명령", c.binding?.simulation_manual],
          ["실물 어댑터", c.binding?.adapter],
          ["연결 근거", c.binding?.review_basis],
        ].map(([label, value]) => (
          <div key={String(label)}>
            <dt>{String(label)}</dt>
            <dd>{describe(value)}</dd>
          </div>
        ))}
      </dl>
      {c.conflicts?.length > 0 && <div className="notice error">
        <strong>같은 모델·기능의 다른 문서 정의가 있습니다.</strong>
        <ul>{c.conflicts.map((item) => <li key={item.capability_id}>
          {item.version} · {item.reason === "다른 버전; 별도 보존"
            ? "버전이 달라 별도로 보존합니다. 적용할 정의를 확인하세요."
            : "조건이 달라 실행 연결을 보류했습니다. 근거와 제약을 비교하세요."}
        </li>)}</ul>
      </div>}
      <CapabilityEvidenceView evidence={c.evidence} />
      {c.verification?.records.length ? (
        <section
          className="ontology-verification"
          aria-label="시뮬레이션 검증 기록"
        >
          <h4>실행으로 확인한 기록 · {c.verification.records.length}건</h4>
          <p>{c.verification.scope}</p>
          {c.verification.records.map((record) => (
            <details key={record.record_id}>
              <summary>
                작업 {record.task_id} · 완료 {record.completed_at.toFixed(3)}{" "}
                시뮬레이션 초
              </summary>
              <dl className="ontology-properties">
                <div>
                  <dt>실행</dt>
                  <dd>{record.run_id}</dd>
                </div>
                <div>
                  <dt>승인 계획</dt>
                  <dd>
                    {record.plan_id} · 버전 {record.plan_version}
                  </dd>
                </div>
                <div>
                  <dt>로봇 / 시드</dt>
                  <dd>
                    {record.robot_id} /{" "}
                    {record.conditions.physics?.seed ?? "기록 미확인"}
                  </dd>
                </div>
                <div>
                  <dt>기록 시점 사건 수</dt>
                  <dd>
                    충돌 {record.outcome_metrics.collisions ?? "미확인"} · 근접{" "}
                    {record.outcome_metrics.near_misses ?? "미확인"} · 실패{" "}
                    {record.outcome_metrics.failed ?? "미확인"}
                  </dd>
                </div>
                <div>
                  <dt>검증 범위</dt>
                  <dd>{record.scope}</dd>
                </div>
              </dl>
              <details className="ontology-document-source">
                <summary>실행 조건 보기</summary>
                <pre>{JSON.stringify(record.conditions, null, 2)}</pre>
              </details>
            </details>
          ))}
        </section>
      ) : null}
    </details>
  );
}

function ReviewCapability({ capability, siblings, disabled, onSaved }: {
  capability: OntologyCapability;
  siblings: OntologyCapability[];
  disabled: boolean;
  onSaved: (snapshot: OntologySnapshot) => void;
}) {
  const [open, setOpen] = useState(false);
  const [name, setName] = useState(capability.name);
  const [key, setKey] = useState(capability.key);
  const [meaning, setMeaning] = useState(capability.meaning);
  const [assertion, setAssertion] = useState(capability.assertion);
  const [details, setDetails] = useState(JSON.stringify({
    inputs: capability.inputs, outputs: capability.outputs,
    parameters: capability.parameters, preconditions: capability.preconditions,
    dependencies: capability.dependencies, constraints: capability.constraints,
    failures: capability.failures, recovery: capability.recovery,
    sdk_mapping: capability.sdk_mapping,
  }, null, 2));
  const [error, setError] = useState("");
  const [note, setNote] = useState(capability.review_note ?? "");
  const [mergeInto, setMergeInto] = useState(capability.merge_into ?? "");
  const save = async (status: "confirmed" | "rejected" | "merged" | "insufficient") => {
    setError("");
    try {
      if (status !== "confirmed" && !note.trim())
        throw new Error("제외·중복·근거 부족 판단의 원문 대조 이유를 입력하세요.");
      if (status === "merged" && !mergeInto)
        throw new Error("중복 병합할 확정 기능을 선택하세요.");
      const parsed = JSON.parse(details);
      if (!parsed || typeof parsed !== "object" || Array.isArray(parsed))
        throw new Error("상세 정의는 JSON 객체여야 합니다.");
      const expected = ["inputs", "outputs", "parameters", "preconditions",
        "dependencies", "constraints", "failures", "recovery", "sdk_mapping"];
      if (expected.some((field) => !(field in parsed)) ||
          Object.keys(parsed).some((field) => !expected.includes(field)))
        throw new Error("상세 정의의 필드 구성을 확인하세요. 필드 추가·누락 없이 내용을 수정할 수 있습니다.");
      const feature = { key, name, meaning, assertion, ...parsed };
      const snapshot = await request<OntologySnapshot>(
        `/ontology/documents/${capability.document_id}/capabilities/${encodeURIComponent(capability.id)}/review`,
        "PUT", { status, feature, note, ...(status === "merged" ? { merge_into: mergeInto } : {}) },
      );
      onSaved(snapshot); setOpen(false);
    } catch (e) { setError(e instanceof Error ? e.message : String(e)); }
  };
  return <details className="ontology-review" open={open} onToggle={(e) => setOpen(e.currentTarget.open)}>
    <summary>{capability.review_status === "draft" ? "추출 초안 검토·확정" : "검토 결과 수정 · 현재 " + capability.review_status}</summary>
    <p>아래 원문 근거와 비교해 수정하세요. 수정 기능은 실행부에 자동 연결되지 않습니다.</p>
    {error && <p className="notice error" role="alert">{error}</p>}
    <label>기능 식별자<input value={key} onChange={(e) => setKey(e.target.value)} /></label>
    <label>기능명<input value={name} onChange={(e) => setName(e.target.value)} /></label>
    <label>의미<textarea rows={3} value={meaning} onChange={(e) => setMeaning(e.target.value)} /></label>
    <label>근거 수준<select value={assertion} onChange={(e) => setAssertion(e.target.value as typeof assertion)}>
      <option value="inferred">추정 · 원문이 명확하지 않음</option>
      <option value="document_explicit">원문에서 명시적으로 확인</option>
    </select></label>
    <label>검토 근거·보정 내용<textarea rows={2} value={note} onChange={(e) => setNote(e.target.value)}
      placeholder="제외·중복·근거 부족 판단은 이유를 기록하세요." /></label>
    <label>중복 병합 대상<select value={mergeInto} onChange={(e) => setMergeInto(e.target.value)}>
      <option value="">확정된 같은 문서 기능 선택</option>
      {siblings.filter((c) => c.id !== capability.id && c.review_status === "confirmed").map((c) =>
        <option key={c.id} value={c.id}>{c.name}</option>)}
    </select></label>
    <details>
      <summary>입출력·매개변수·제약·실패·SDK 대응 수정</summary>
      <p>원문의 단위·허용 범위와 선행 조건을 확인하세요. 빈 SDK 대응을 임의로 채우면 실제 연결로 간주되지 않습니다.</p>
      <label>상세 기능 정의 (JSON)
        <textarea rows={16} spellCheck={false} value={details}
          onChange={(e) => setDetails(e.target.value)} />
      </label>
    </details>
    <div className="floorplan-actions">
      <button disabled={disabled} onClick={() => void save("confirmed")}>수정한 정의 확정</button>
      <button disabled={disabled} onClick={() => void save("rejected")}>후보 제외</button>
      <button disabled={disabled || !mergeInto} onClick={() => void save("merged")}>중복 병합</button>
      <button disabled={disabled} onClick={() => void save("insufficient")}>근거 부족</button>
    </div>
  </details>;
}
export function PlanOntologyEvidence({
  ontology,
}: {
  ontology?: PlanOntology;
}) {
  if (!ontology)
    return (
      <p className="notice">
        이 계획에는 기능 온톨로지 근거가 저장되어 있지 않습니다. 현재 문서와
        연결 상태를 반영해 계획을 다시 검토하세요.
      </p>
    );
  return (
    <section className="planner-options" aria-label="계획에 사용한 기능 근거">
      <h4>계획에 사용한 기능 · {ontology.capabilities.length}개</h4>
      <p>
        승인 검토 시 계획에 저장된 문서·기능 버전입니다. 문서에 있는 기능도 실행
        연결과 현재 조건을 충족해야 승인할 수 있습니다.
      </p>
      <small>온톨로지 버전 {ontology.revision}</small>
      {ontology.limitations?.length > 0 && (
        <ul className="planner-problems">
          {ontology.limitations.map((line, i) => (
            <li key={i}>{line}</li>
          ))}
        </ul>
      )}
      {!ontology.capabilities.length && (
        <p>이 계획에 연결된 문서 기능이 없습니다.</p>
      )}
      {ontology.capabilities.map((c) => (
        <CapabilityDetails key={c.id} capability={c} />
      ))}
    </section>
  );
}
export function OntologyPanel({
  modelIds,
  focusDocumentId,
  onChanged,
}: {
  modelIds: string[];
  focusDocumentId?: string;
  onChanged: () => void;
}) {
  const [data, setData] = useState<OntologySnapshot | null>(null);
  const [busy, setBusy] = useState("");
  const [error, setError] = useState("");
  const [notice, setNotice] = useState("");
  const [filter, setFilter] = useState("");
  const [documentFilter, setDocumentFilter] = useState("");
  const [query, setQuery] = useState("");
  const [visibleCount, setVisibleCount] = useState(12);
  const [formOpen, setFormOpen] = useState(false);
  const [pdfFile, setPdfFile] = useState<File | null>(null);
  const [newModel, setNewModel] = useState({ id: "", name: "" });
  const [draft, setDraft] = useState({
    title: "",
    model_id: modelIds[0] ?? "",
    version: "",
    source_url: "",
    text: "",
  });
  useEffect(() => {
    let cancelled = false;
    request<OntologySnapshot>("/ontology")
      .then((value) => {
        if (!cancelled) setData(value);
      })
      .catch((e) => {
        if (!cancelled) setError(e instanceof Error ? e.message : String(e));
      });
    return () => {
      cancelled = true;
    };
  }, []);
  const act = async (label: string, fn: () => Promise<void>) => {
    if (busy) return;
    setBusy(label);
    setError("");
    setNotice("");
    try {
      await fn();
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setBusy("");
    }
  };
  const models = [
    ...new Set([
      ...modelIds,
      ...(data?.documents.map((d) => d.model_id) ?? []),
      ...(data?.documentation_models?.map((m) => m.id) ?? []),
    ]),
  ];
  const capabilities = (data?.capabilities ?? []).filter(
    (c) =>
      (!filter || c.model_id === filter) &&
      (!documentFilter || c.document_id === documentFilter) &&
      `${c.name} ${c.meaning} ${c.key} ${c.model_id}`
        .toLowerCase()
        .includes(query.toLowerCase()),
  );
  const reviewedCount = data?.capabilities.filter((c) => c.review_status === "confirmed" && c.support.document_confirmed).length ?? 0;
  const platformContractCount = data?.capabilities.filter((c) => c.support.simulation_connected &&
    data.documents.find((d) => d.id === c.document_id)?.provenance === "project_authored_technical_document").length ?? 0;
  useEffect(() => setVisibleCount(12), [filter, query]);
  useEffect(() => {
    if (focusDocumentId) {
      setDocumentFilter(focusDocumentId);
      setFilter("");
      setQuery("");
    }
  }, [focusDocumentId]);
  useEffect(() => {
    if (focusDocumentId && data?.documents.some((item) => item.id === focusDocumentId))
      document.getElementById(`ontology-document-${focusDocumentId}`)?.scrollIntoView({ block: "nearest" });
  }, [focusDocumentId, data]);
  return (
    <section className="ontology-panel" aria-label="로봇 기능과 문서 근거">
      <div className="planner-connection-heading">
        <div>
          <h3>
            <BookOpen size={19} /> 로봇 기능과 문서 근거
          </h3>
          <p>문서에 있는 기능, 실행에 연결된 기능, 검증한 기능을 구분합니다.</p>
        </div>
        <button
          disabled={!!busy}
          onClick={() =>
            void act("문서 상태 확인 중", async () =>
              setData(await request<OntologySnapshot>("/ontology")),
            )
          }
        >
          <RefreshCw size={15} /> 새로고침
        </button>
      </div>
      {error && (
        <p className="notice error" role="alert">
          {error}
        </p>
      )}
      {focusDocumentId && data && !data.documents.some((item) => item.id === focusDocumentId) &&
        <p className="notice error" role="alert">참조한 문서를 현재 목록에서 찾을 수 없습니다. 문서 목록을 새로고침하고 계획의 근거를 다시 확인하세요.</p>}
      {notice && (
        <p className="notice" role="status">
          {notice}
        </p>
      )}
      {busy && <p role="status">{busy}… {busy === "실제 모델로 문서 추출 중" &&
        <button onClick={() => void request("/assistant/cancel", "POST").then(() => setNotice("모델 요청 취소를 전달했습니다. 기존 문서는 보존됩니다.")).catch((e) => setError(String(e)))}>추출 취소</button>}</p>}
      <div className="ontology-toolbar">
        <span>
          {data
            ? `문서 ${data.coverage.document_count}개 · 기능 후보 ${data.coverage.capability_count}개 · 검토 확정 ${reviewedCount}개 · 기존 연구 실행 계약 ${platformContractCount}개`
            : "문서 목록 확인 중"}
        </span>
        <button
          aria-expanded={formOpen}
          onClick={() => setFormOpen((value) => !value)}
        >
          문서 등록
        </button>
      </div>
      <details className="ontology-documents">
        <summary>새 로봇 모델 문서 등록</summary>
        <p>문서 전용 카탈로그에 등록합니다. 시뮬레이션 모델·어댑터가 없는 로봇은 실행에 투입할 수 없습니다.</p>
        <div className="ontology-onboard">
          <label>모델 ID<input value={newModel.id} placeholder="예: warehouse_bot"
            onChange={(e) => setNewModel({ ...newModel, id: e.target.value })} /></label>
          <label>모델 이름<input value={newModel.name}
            onChange={(e) => setNewModel({ ...newModel, name: e.target.value })} /></label>
          <button disabled={!!busy} onClick={() => void act("로봇 모델 등록 중", async () => {
            const row = await request<{id:string}>("/ontology/models", "POST", newModel);
            setData(await request<OntologySnapshot>("/ontology"));
            setDraft((v) => ({ ...v, model_id: row.id }));
            setNewModel({ id: "", name: "" }); onChanged();
            setNotice("문서 전용 모델을 등록했습니다. 실행 모델과 장비 검증은 별도로 연결해야 합니다.");
          })}>문서 전용 모델 등록</button>
        </div>
        {!!data?.documentation_models?.length && <ul>{data.documentation_models.map((m) =>
          <li key={m.id}>{m.name} ({m.id}) · {m.status}</li>)}</ul>}
      </details>
      {formOpen && (
        <form
          className="ontology-document-form"
          onSubmit={(e) => {
            e.preventDefault();
            void act("문서 등록 중", async () => {
              let doc: OntologyDocument;
              if (pdfFile) {
                const response = await fetch("/api/ontology/documents/file", { method: "POST",
                  headers: { "Content-Type": "application/pdf", "X-Model-Id": draft.model_id,
                    "X-Document-Version": draft.version, "X-Filename": encodeURIComponent(draft.title || pdfFile.name),
                    "X-Source-Url": draft.source_url }, body: pdfFile });
                if (!response.ok) {
                  const failure = await response.json().catch(() => null);
                  throw new Error(failure?.detail ?? `문서 등록 실패 (${response.status})`);
                }
                doc = await response.json() as OntologyDocument;
              } else doc = await request<OntologyDocument>("/ontology/documents", "POST", draft);
              setData(await request<OntologySnapshot>("/ontology"));
              onChanged();
              setNotice(
                `‘${doc.title}’을 등록했습니다. 문서 목록의 기능 추출을 눌러 근거와 누락 항목을 확인하세요.`,
              );
              setDraft({
                title: "",
                model_id: draft.model_id,
                version: "",
                source_url: "",
                text: "",
              });
              setPdfFile(null);
              setFormOpen(false);
            });
          }}
        >
          <label>
            문서명
            <input
              required
              value={draft.title}
              maxLength={300}
              onChange={(e) => setDraft({ ...draft, title: e.target.value })}
            />
          </label>
          <label>
            로봇 모델
            <select
              required
              value={draft.model_id}
              onChange={(e) => setDraft({ ...draft, model_id: e.target.value })}
            >
              <option value="">모델 선택</option>
              {models.map((id) => (
                <option key={id} value={id}>
                  {id}
                </option>
              ))}
            </select>
          </label>
          <label>
            문서·소프트웨어 버전
            <input
              required
              value={draft.version}
              maxLength={100}
              onChange={(e) => setDraft({ ...draft, version: e.target.value })}
              placeholder="문서에 기재된 버전 또는 미표기"
            />
          </label>
          <label>
            출처 링크
            <input
              type="url"
              value={draft.source_url}
              onChange={(e) =>
                setDraft({ ...draft, source_url: e.target.value })
              }
              placeholder="https://…"
            />
          </label>
          <label className="ontology-form-wide">
            원문 텍스트 또는 PDF 파일 가져오기
            <input
              type="file"
              accept=".txt,.md,.json,.pdf,text/plain,text/markdown,application/json,application/pdf"
              onChange={(e) => {
                const file = e.target.files?.[0];
                if (!file) return;
                if (file.type === "application/pdf" || file.name.toLowerCase().endsWith(".pdf")) {
                  if (file.size > 20_000_000) { setError("PDF는 20 MB 이하로 선택하세요."); return; }
                  setPdfFile(file);setDraft((v) => ({ ...v, title: v.title || file.name }));return;
                }
                setPdfFile(null);
                if (file.size > 2_000_000) {
                  setError("2 MB 이하의 텍스트 문서를 선택하세요.");
                  e.target.value = "";
                  return;
                }
                void file
                  .text()
                  .then((text) =>
                    setDraft((value) => ({
                      ...value,
                      title: value.title || file.name,
                      text,
                    })),
                  )
                  .catch(() =>
                    setError(
                      "파일을 읽지 못했습니다. 텍스트를 직접 붙여 넣어 주세요.",
                    ),
                  );
              }}
            />
          </label>
          <label className="ontology-form-wide">
            문서 원문
            <textarea
              required={!pdfFile}
              rows={8}
              value={draft.text}
              onChange={(e) => setDraft({ ...draft, text: e.target.value })}
              placeholder="기능 설명과 매개변수·제약이 포함된 원문을 붙여 넣으세요."
            />
          </label>
          <p className="ontology-form-wide">
            {pdfFile ? `PDF 선택: ${pdfFile.name}. 스캔 페이지는 로컬 OCR 초안으로 읽고 원본 대조가 필요합니다. ` : ""}
            출처 링크만 등록하면 원문을 자동으로 가져오지 않습니다. 문서 내용을
            함께 등록하세요. 등록한 문서와 기존 수동 카탈로그는 별도로
            표시합니다. Markdown의 capability 코드 블록 또는 Spot SDK
            RobotCommandBuilder의 정확한 API 절을 분석합니다. 일반 기능 절은
            검토할 초안으로 제시합니다. 문서 등록만으로 실행 권한이 생기지 않습니다.
          </p>
          <div>
            <button type="submit" disabled={!!busy}>
              문서 저장
            </button>
          </div>
        </form>
      )}
      {data && (
        <>
          <details className="ontology-documents" open={!!focusDocumentId}>
            <summary>등록 문서 · 원문과 분석 상태</summary>
            {data.documents.length ? (
              data.documents.map((d) => (
                <article key={d.id} id={`ontology-document-${d.id}`}>
                  <div>
                    <strong>{d.title}</strong>
                    <small>
                      {d.model_id} · {d.version} ·{" "}
                      {provenanceNames[d.provenance] ?? d.provenance}
                    </small>
                  </div>
                  <span>{d.analyzed ? "분석됨" : "기능 추출 전"}</span>
                  {d.source_import && <details><summary>PDF 페이지 판독 · {d.source_import.pages.filter((p) => p.status === "pdf_text").length}쪽 원문 텍스트 · {d.source_import.pages.filter((p) => p.status === "local_ocr_review_required").length}쪽 OCR 검토 · {d.source_import.pages.filter((p) => p.status === "unreadable").length}쪽 판독 실패</summary>
                    <p>{d.source_import.basis}</p>
                    <ul>{d.source_import.pages.map((p) => <li key={p.page}>{p.page}쪽 · {p.status === "pdf_text" ? "PDF 원문 텍스트" : p.status === "local_ocr_review_required" ? "로컬 OCR · 원본 대조 필요" : p.status === "short_pdf_text_review_required" ? "짧은 원문 텍스트 · 확인 필요" : p.reason || "읽지 못함 · 원본 확인 필요"} · {p.characters}자</li>)}</ul>
                  </details>}
                  {d.reviewed_facts?.filter((fact) => fact.kind === "version").map((fact) =>
                    <p key={fact.id} className="notice">버전 검토: {fact.statement} · 원문 {fact.line_start}행</p>)}
                  {d.review_coverage && <p>이 문서의 후보 {d.review_coverage.candidate_count}개 · 판정 {d.review_coverage.reviewed_count}개 ·
                    남은 검토 초안 {d.review_coverage.status_counts.draft ?? 0}개 · 별도 사용자 판정 없음 {d.review_coverage.status_counts.unreviewed ?? 0}개 ·
                    확정 {d.review_coverage.status_counts.confirmed ?? 0}개 · 제외 {d.review_coverage.status_counts.rejected ?? 0}개 ·
                    중복 {d.review_coverage.status_counts.merged ?? 0}개 · 근거 부족 {d.review_coverage.status_counts.insufficient ?? 0}개
                    {d.review_coverage.model_total_characters != null &&
                      ` · 모델 전달 범위 ${d.review_coverage.model_processed_characters ?? "미확인"}/${d.review_coverage.model_total_characters}자`}</p>}
                  {!!d.review_coverage?.unextracted.length && <details><summary>이 문서의 미추출·확인 필요 {d.review_coverage.unextracted.length}건</summary>
                    <ul>{d.review_coverage.unextracted.map((row, i) => <li key={i}>{row.section}: {row.reason}</li>)}</ul></details>}
                  {d.provenance === "user_supplied" && <DocumentFacts document={d} disabled={!!busy}
                    onSaved={(next) => { setData(next); onChanged(); setNotice("문서의 비실행 사양·조건·제약을 원문 근거와 함께 저장했습니다."); }} />}
                  <button
                    disabled={!!busy}
                    onClick={() =>
                      void act("문서 기능 추출 중", async () => {
                        setData(
                          await request<OntologySnapshot>(
                            `/ontology/documents/${encodeURIComponent(d.id)}/analyze`,
                            "POST",
                          ),
                        );
                        onChanged();
                        setNotice(
                          "기능 추출을 마쳤습니다. 근거·누락·실행 연결 상태를 검토하세요. 기존 계획은 갱신 후 다시 승인해야 합니다.",
                        );
                      })
                    }
                  >
                    {d.analyzed ? "다시 분석" : "기능 추출"}
                  </button>
                  {d.provenance === "user_supplied" && <button disabled={!!busy || (d.review_coverage?.model_total_characters != null &&
                    d.review_coverage.model_processed_characters === d.review_coverage.model_total_characters)}
                    onClick={() => void act("실제 모델로 문서 추출 중", async () => {
                      const next=await request<OntologySnapshot>(`/ontology/documents/${d.id}/extract/model`,"POST");
                      setData(next);
                      onChanged();
                      const coverage=next.documents.find((item) => item.id === d.id)?.review_coverage;
                      setNotice(`Codex의 이번 문서 구간 분석을 저장했습니다. 전달 범위 ${coverage?.model_processed_characters ?? "?"}/${coverage?.model_total_characters ?? "?"}자. 남은 구간이 있으면 이어서 분석하고, 기능별 원문을 검토·확정하세요. 실행 연결은 별도입니다.`);
                    })}>{d.review_coverage?.model_total_characters != null &&
                      d.review_coverage.model_processed_characters === d.review_coverage.model_total_characters
                      ? "모델 전달 범위 완료 · 기능 검토 계속"
                      : d.review_coverage?.model_processed_characters
                        ? "다음 문서 구간을 모델로 분석"
                        : "실제 모델로 기능 초안 만들기"}</button>}
                  <details className="ontology-document-source" open={focusDocumentId === d.id}>
                    <summary>원문과 출처 확인</summary>
                    <p>
                      {safeExternalUrl(d.source_url) ? (
                        <a
                          href={safeExternalUrl(d.source_url)!}
                          target="_blank"
                          rel="noreferrer"
                        >
                          출처 문서 열기
                        </a>
                      ) : (
                        "외부 출처 링크 없음"
                      )}{" "}
                      · 문서 버전 {d.version}
                    </p>
                    <p>문서 범위: {describe(d.scope)}</p>
                    {d.has_source_pdf && <a href={`/api/ontology/documents/${d.id}/source`} target="_blank" rel="noreferrer">등록한 원본 PDF 열기</a>}
                    <small>문서 지문: {d.sha256}</small>
                    <pre>
                      {d.text ?? "원문이 이 응답에 포함되지 않았습니다."}
                    </pre>
                  </details>
                </article>
              ))
            ) : (
              <p>등록한 문서가 없습니다. 먼저 로봇 문서를 등록하세요.</p>
            )}
          </details>
          <div className="ontology-filters">
            <label>문서<select value={documentFilter} onChange={(e) => setDocumentFilter(e.target.value)}>
              <option value="">모든 문서</option>
              {data.documents.map((d) => <option key={d.id} value={d.id}>{d.title} · {d.version}</option>)}
            </select></label>
            <label>
              로봇 모델
              <select
                value={filter}
                onChange={(e) => setFilter(e.target.value)}
              >
                <option value="">모든 모델</option>
                {models.map((id) => (
                  <option key={id} value={id}>
                    {id}
                  </option>
                ))}
              </select>
            </label>
            <label>
              <span>
                <Search size={14} /> 기능 검색
              </span>
              <input
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="기능명·의미·모델"
              />
            </label>
          </div>
          {capabilities.length ? (
            capabilities.slice(0, visibleCount).map((c) => (
              <div key={c.id}>
                <CapabilityDetails capability={c} selectedElsewhere={data.capabilities.some((other) =>
                  other.id !== c.id && other.model_id === c.model_id && other.key === c.key && other.active_execution)}
                  mergeTargetName={data.capabilities.find((other) => other.id === c.merge_into)?.name} />
                {data.documents.find((d) => d.id === c.document_id)?.provenance === "user_supplied" &&
                  <ReviewCapability capability={c} siblings={data.capabilities.filter((other) => other.document_id === c.document_id)} disabled={!!busy} onSaved={(next) => {
                    setData(next);onChanged();setNotice("기능 검토를 저장했습니다. 수정한 정의는 실행부에 자동 연결되지 않습니다.");
                  }} />}
                {data.documents.find((d) => d.id === c.document_id)?.provenance === "user_supplied" &&
                  c.review_status === "confirmed" && c.assertion === "document_explicit" &&
                  reviewedSimulationContracts[c.key]?.models.includes(c.model_id) &&
                  <div className="ontology-review">
                    <p>원문에서 확인한 기능을 연구용 {reviewedSimulationContracts[c.key].label} 실행 계약에 대응시킬 수 있습니다. {reviewedSimulationContracts[c.key].scope} 시뮬레이션 검증과 실물 검증은 별도 상태입니다.</p>
                    <button disabled={!!busy || !!c.active_execution} onClick={() => void act(`${reviewedSimulationContracts[c.key].label} 실행 연결`, async () => {
                      const next = await request<OntologySnapshot>(
                        `/ontology/documents/${c.document_id}/capabilities/${encodeURIComponent(c.id)}/simulation-binding`,
                        "PUT", { contract: c.key });
                      setData(next); onChanged();
                      setNotice(`이 문서·버전을 ${reviewedSimulationContracts[c.key].label} 실행 근거로 선택했습니다. 기존 계획은 다시 계산하고 승인해야 합니다.`);
                    })}>{c.active_execution ? `현재 ${reviewedSimulationContracts[c.key].label} 실행 근거로 선택됨` : `시뮬레이션 ${reviewedSimulationContracts[c.key].label}에 연결하고 이 문서 선택`}</button>
                  </div>}
              </div>
            ))
          ) : (
            <p className="planner-empty">
              표시할 기능이 없습니다. 문서 분석 상태나 검색 조건을 확인하세요.
            </p>
          )}
          {capabilities.length > visibleCount && <button onClick={() => setVisibleCount((n) => n + 12)}>
            기능 더 보기 · {capabilities.length - visibleCount}개 남음
          </button>}
          <details className="ontology-coverage">
            <summary>누락·실행 미연결·근거 미확보</summary>
            <h4>미추출·확인 필요 · {data.coverage.unextracted.length}개</h4>
            {data.coverage.unextracted.length ? (
              <ul>
                {data.coverage.unextracted.map((entry, i) => (
                  <li key={i}>
                    {data.documents.find((d) => d.id === entry.document_id)
                      ?.title ?? entry.document_id}{" "}
                    / {entry.section} — {entry.reason}
                  </li>
                ))}
              </ul>
            ) : (
              <p>
                등록 문서의 추적 범위에서 기록된 미추출 항목이 없습니다. 로봇의
                모든 기능을 확보했다는 의미는 아닙니다.
              </p>
            )}
            <h4>실행 미연결 후보 · {data.coverage.execution_unlinked.length}개</h4>
            <p>
              {data.coverage.execution_unlinked
                .map(
                  (id) =>
                    data.capabilities.find((c) => c.id === id)?.name ?? id,
                )
                .join(" · ") || "기록된 항목 없음"}
            </p>
            <h4>자동 제공된 제조사 SDK 문서가 없는 모델</h4>
            <p>
              {data.coverage.manufacturer_evidence_missing.join(" · ") ||
                "기록된 항목 없음"}
            </p>
            <p>사용자가 등록한 공식 PDF는 별도로 검토합니다. 이 목록은 그 문서가 없다는 뜻이 아닙니다.</p>
          </details>
          <p className="ontology-footer">
            실물 어댑터 연결은 실물 시험 완료를 의미하지 않습니다. 각 기능의
            실물 검증 상태를 따로 확인하세요. · 온톨로지 버전 {data.revision}
          </p>
        </>
      )}
    </section>
  );
}
