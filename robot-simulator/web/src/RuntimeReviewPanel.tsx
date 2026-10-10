import { useEffect, useState } from 'react';
import { request } from './api';
import type { RunState } from './types';

type Proposal={id:string;run_id:string;task_id:string;reason:string;expires_at:number;options:{id:string;label:string;changes:{field:string;before:string;after:string}[];delay_basis:string}[];excluded:{robot_id:string|null;reason:string}[]};
export function RuntimeReviewPanel({run,taskId}:{run:RunState;taskId:string}) {
  const [proposal,setProposal]=useState<Proposal|null>(null),[busy,setBusy]=useState(false),[message,setMessage]=useState('');
  const [limit,setLimit]=useState(15);
  useEffect(()=>{setProposal(null);setMessage('');},[run.run_id,taskId]);
  const task=run.tasks.find(t=>t.id===taskId);
  const reviewEvent=[...run.events].reverse().find(e=>e.entity_id===taskId&&['replan_attention_required','replan_approved','replan_proposed'].includes(e.kind));
  const timedOut=run.status==='paused'&&reviewEvent?.kind==='replan_attention_required';
  if(!task||['completed','cancelled','skipped'].includes(task.status))return null;
  const act=async(work:()=>Promise<void>)=>{setBusy(true);setMessage('');try{await work();}catch(e){setMessage(e instanceof Error?e.message:String(e));}finally{setBusy(false);}};
  return <section className="runtime-review" aria-label="실행 중 변경 검토"><h4>멈춘 이유를 확인하고 다음 조치를 선택하세요</h4>
    <p>{task.reason||'현재 실행 상태에서 가능한 대안을 확인합니다.'}</p>
    <label>승인 후 관측 시간 상한 (초) <input aria-label="재계획 관측 시간" type="number" min={1} max={300} value={limit} onChange={e=>setLimit(Number(e.target.value))}/></label>
    <button disabled={busy||!['running','paused'].includes(run.status)} onClick={()=>void act(async()=>{setProposal(await request<Proposal>('/runtime-replans','POST',{task_id:taskId,wait_seconds:limit}));})}>일시 정지하고 대안 계산</button>
    {proposal&&<div><p>실행 {proposal.run_id.slice(0,8)} · 새로운 변경 승인입니다. 물품 위치와 완료한 작업은 유지합니다.</p>
      {proposal.options.map(option=><div className="review-option" key={option.id}><strong>{option.label}</strong><p>{option.delay_basis}</p>{option.changes.map((c,i)=><p key={i}>{c.before} → {c.after}</p>)}<button disabled={busy||run.status!=='paused'||Date.now()/1000>proposal.expires_at} onClick={()=>void act(async()=>{await request('/runtime-replans/approve','POST',{proposal_id:proposal.id,option_id:option.id,request_id:crypto.randomUUID()});setProposal(null);setMessage('변경을 승인했습니다. 현재 물리 상태에서 이어갑니다.');})}>이 변경 승인·계속</button></div>)}
      {!proposal.options.length&&<p>현재 상태에서 실행 가능한 변경이 없습니다. 아래 제한과 기존 물품 복구 기능을 확인하세요.</p>}
      <details><summary>제외된 대안과 지원 범위</summary><ul>{proposal.excluded.map((e,i)=><li key={i}>{e.robot_id?`${e.robot_id}: `:''}{e.reason}</li>)}</ul></details>
    </div>}
    {timedOut?<p role="status">승인한 관측 시간 상한에 도달해 일시 정지했습니다. 작업 결과를 확인하고 대안을 다시 계산하세요.</p>:message&&<p role="status">{message}</p>}
  </section>;
}
