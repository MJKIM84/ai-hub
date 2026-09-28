/** @jsxImportSource react */
import { useEffect, useState } from 'react';
import type { Project } from './types';

export type ScenarioDraft = {
  facts: Record<string, {label:string; value:string; basis:'user'|'project'|'proposed'|'unknown'; references:string[]}>;
  questions: {id:string; field:string; prompt:string; options:{value:string; label:string; reason:string}[]}[];
  changes?: string[]; alternatives?: string[];
};
export type ScenarioTask = {id?:string; existing_task_id?:string; name?:string; destination_id?:string; predecessor_ids?:string[]};
export function ScenarioDraftPanel({draft, tasks, steps=[], project, version, busy, dirty, selectedPlace, onAnswer, onDestination, onSave, onReviewMap, onReference}: {
  draft?:ScenarioDraft; tasks:ScenarioTask[]; project:Project; version?:number; busy:boolean; dirty:boolean;
  steps?:{id:string;name:string;robot_ids:string[];floor_id:string;destination:{x:number;y:number};dependencies:string[]}[];
  selectedPlace:string; onAnswer:(answers:Record<string,string>)=>void;
  onDestination:(taskId:string,placeId:string)=>void; onSave:()=>void; onReviewMap:()=>void; onReference:(id:string)=>void;
}) {
  const [answers,setAnswers]=useState<Record<string,string>>({});
  const [step,setStep]=useState('');
  useEffect(()=>{setAnswers({});},[version]);
  const questions=(draft?.questions ?? []).slice(0,4);
  const basis={user:'사용자 선택',project:'프로젝트 정보',proposed:'제안값 · 승인 전 검토',unknown:'미확정'};
  const place=project.environment.elements.find(e=>e.id===selectedPlace);
  return <section className="scenario-draft" aria-label="현재 시나리오 초안">
    <header><div><span className="scenario-eyebrow">대화로 구성하기</span><h3>현재 시나리오 초안</h3></div>
      <span className="scenario-save-state" role="status">{version ? `v${version} · ${dirty?'화면 변경 미반영':'서버에 저장됨'}`:'목표를 입력해 시작하세요'}</span>
    </header>
    <p className="scenario-map-name">{project.environment.name} · 지도 v{project.environment.version} · 로봇 {project.robots.length}대 · 사람 {project.people.length}명</p>
    {!!steps.length && <details className="scenario-current" open><summary>현재 실행 구성 · {steps.length}단계</summary>
      {dirty && <p>화면 변경은 아직 계산 전입니다. 저장·다시 검증하면 아래 구성이 갱신됩니다.</p>}
      <ol>{steps.map(step=><li key={step.id}><strong>{step.name}</strong><span>{step.robot_ids.map(id=>project.robots.find(r=>r.id===id)?.name??id).join(' + ')} · {project.environment.floors.find(f=>f.id===step.floor_id)?.name??step.floor_id} ({step.destination.x.toFixed(1)}, {step.destination.y.toFixed(1)})m</span><small>{step.dependencies.length?'선행: '+step.dependencies.map(id=>steps.find(s=>s.id===id)?.name??id).join(', '):'독립 시작 · 다른 단계와 병행 가능'}</small></li>)}</ol>
      <small>지도·화면 변경 후 다시 계산한 구성이 기준입니다. 아래 대화의 선택 기록과 구분해 확인하세요.</small>
    </details>}
    {questions.length>0 && <form onSubmit={e=>{e.preventDefault();onAnswer(Object.fromEntries(Object.entries(answers).filter(([,v])=>v.trim())));}} className="scenario-questions">
      <div><strong>다음 조건을 정해주세요</strong><span>남은 질문 {draft!.questions.length}개 · 자유 입력 가능</span></div>
      {questions.map((q,i)=><fieldset key={q.id}><legend>{i+1}. {q.prompt}</legend>
        <div className="scenario-choices">{q.options.map(o=><button key={o.value} type="button" aria-pressed={answers[q.id]===o.value}
          disabled={busy} onClick={()=>setAnswers(a=>({...a,[q.id]:o.value}))}><strong>{o.label}</strong><small>{o.reason}</small></button>)}</div>
        <label><span>답변 또는 다른 조건</span><input value={answers[q.id]??''} maxLength={2000} disabled={busy}
          onChange={e=>setAnswers(a=>({...a,[q.id]:e.target.value}))}/></label>
      </fieldset>)}
      <button className="primary" disabled={busy||!Object.values(answers).some(x=>x.trim())}>답변 반영하고 이어서 구성</button>
    </form>}
    {draft && Object.keys(draft.facts??{}).length>0 && <details open={questions.length>0}><summary>대화의 선택·가정 기록 · {Object.keys(draft.facts).length}개</summary><dl className="scenario-facts">
      {Object.entries(draft.facts).map(([key,f])=><div key={key}><dt>{f.label}<small>{basis[f.basis]}</small></dt><dd>{f.value || '아직 정하지 않음'}{!!f.references?.length && <details><summary>근거 보기</summary>{f.references.map(id=><button key={id} onClick={()=>onReference(id)}>{id.startsWith('document:')?'문서 원문 열기':project.environment.elements.find(e=>e.id===id)?.name??project.robots.find(r=>r.id===id)?.name??project.items.find(x=>x.id===id)?.name??'관련 항목 열기'}</button>)}</details>}</dd></div>)}
    </dl></details>}
    {!!draft?.changes?.length && <div className="scenario-changes"><strong>이번 변경</strong><ul>{draft.changes.map((c,i)=><li key={i}>{c}</li>)}</ul></div>}
    {!!draft?.alternatives?.length && <details open><summary>실행 제약과 가능한 대안</summary><ul>{draft.alternatives.map((c,i)=><li key={i}>{c}</li>)}</ul><button onClick={onReviewMap}>도면·연결 검토로 이동</button></details>}
    {version && <div className="scenario-map-edit"><label>지도에서 고른 장소를 적용할 단계<select value={step} onChange={e=>setStep(e.target.value)}>
      <option value="">단계 선택</option>{tasks.filter(t=>t.id&&!t.existing_task_id).map(t=><option key={t.id} value={t.id}>{t.name??t.id}</option>)}</select></label>
      <button disabled={busy||!step||!place||!['room','corridor','waiting','workbench','loading','dock'].includes(place.kind)}
        onClick={()=>onDestination(step,selectedPlace)}>{place?`${place.name}을 목적지로 적용`:'지도에서 장소를 선택하세요'}</button>
      <button disabled={busy||!dirty} onClick={onSave}>화면 구성 저장·다시 검증</button>
    </div>}
    {!draft && <p className="scenario-empty">목표만 말해도 됩니다. 필요한 조건을 몇 가지씩 정한 뒤 전체 계획을 검토합니다. 물품 처리와 단순 이동은 구분됩니다.</p>}
    <small>실행은 전체 계획 승인 후 시작합니다. 물품·사람·지도 변경은 경로와 실행 조건을 다시 검증합니다.</small>
  </section>;
}

export function ConfirmationControl({label,criterion,disabled,onConfirm}:{label:string;criterion:string;disabled:boolean;onConfirm:(note:string)=>void}) {
  const [note,setNote]=useState('');
  return <form className="scenario-confirm" onSubmit={e=>{e.preventDefault();onConfirm(note);}}>
    <strong>{label}</strong><p>{criterion}</p><label>실제로 확인한 내용<input required maxLength={1000} value={note} onChange={e=>setNote(e.target.value)}/></label>
    <button disabled={disabled||!note.trim()}>현장 확인 기록 · 다음 단계 허용</button>
    <small>확인 기록은 물품 이동·가공의 물리적 성공을 대신하지 않습니다.</small>
  </form>;
}
