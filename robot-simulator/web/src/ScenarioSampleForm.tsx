/** @jsxImportSource react */
import { useState } from 'react';
import type { Project } from './types';
import { request } from './api';
export function ScenarioSampleForm({onUse,onEdit}:{onUse:(p:Project)=>Promise<void>;onEdit:()=>void}) {
  const [rows,setRows]=useState('1층:창고,회수 지점\n2층:작업실');
  const [height,setHeight]=useState(3.2),[elevator,setElevator]=useState(true);
  const [error,setError]=useState(''),[busy,setBusy]=useState(false);
  return <details className="scenario-sample"><summary>장소가 없다면 · 지도 준비</summary>
    <p>기존 지도는 환경 편집에서 수정하거나 도면을 가져올 수 있습니다. 새 가상 샘플은 아래 시험 입력으로 만듭니다.</p>
    <button onClick={onEdit}>현재 지도 편집·도면 가져오기</button>
    <form onSubmit={async e=>{e.preventDefault();setBusy(true);setError('');try {
      const floors=rows.split('\n').filter(r=>r.trim()).map(row=>{const [name,...parts]=row.split(':');return {name:name.trim(),spaces:parts.join(':').split(',').map(s=>s.trim())};});
      if(!floors.length||floors.length>3)throw new Error('층을 1~3개 입력하세요.');
      if(floors.some(f=>!f.name||f.spaces.some(s=>!s)))throw new Error('층 이름과 공간 이름을 입력하세요. 예: 1층:접수 구역,검토 구역');
      const draft=await request<{project:Project}>('/scenarios/sample','POST',{name:'대화로 구성한 공간',floors,floor_height_m:height,elevator,width_m:16,depth_m:12});
      await onUse(draft.project);
    }catch(e){let message=e instanceof Error?e.message:String(e);try{const errors=JSON.parse(message);if(Array.isArray(errors))message=errors.map(x=>String(x.msg??'입력 조건을 확인하세요').replace(/^Value error, /,'')).join(' · ');}catch{/* plain server message */}setError(message);}finally{setBusy(false);}}}>
      <label>층별 공간 · 한 줄에 층:공간,공간<textarea rows={3} value={rows} onChange={e=>setRows(e.target.value)} disabled={busy}/></label>
      <label>층 높이 차이 · 시험 입력(m)<input type="number" min={3} max={6} step={.1} value={height} onChange={e=>setHeight(+e.target.value)} disabled={busy}/></label>
      <label><input type="checkbox" checked={elevator} onChange={e=>setElevator(e.target.checked)} disabled={busy}/>시험 승강기 포함</label>
      <p>층당 16×12m, 열린 작업 구역, AMR 1대. 실제 도면이 아니며 벽·문을 인식한 결과로 표시하지 않습니다. 이전 초안은 저장하고 새 환경은 승인 전 상태로 엽니다.</p>
      {error&&<p role="alert">{error}</p>}<button disabled={busy}>{busy?'초안 생성 중…':'가상 샘플 만들고 초안에 사용'}</button>
    </form>
  </details>;
}
