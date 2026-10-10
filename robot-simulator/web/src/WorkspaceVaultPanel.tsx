import { useEffect, useState } from 'react';
import { request, downloadJSON } from './api';
import type { Project } from './types';
type Space={id:string;title:string;revision:number;role:string};
export function WorkspaceVaultPanel({beforeRestore,onRestored}:{beforeRestore:()=>Promise<void>;onRestored:(p:Project,runId:string)=>Promise<void>}) {
  const [configured,setConfigured]=useState<boolean|null>(null),[token,setToken]=useState(''),[subject,setSubject]=useState('');
  const [spaces,setSpaces]=useState<Space[]>([]),[busy,setBusy]=useState(false),[message,setMessage]=useState('');
  const [shareSubject,setShareSubject]=useState(''),[role,setRole]=useState('reader');
  useEffect(()=>{void request<{configured:boolean}>('/vault/status').then(r=>setConfigured(r.configured)).catch(()=>setConfigured(false));},[]);
  const call=<T,>(path:string,method='GET',body?:unknown)=>request<T>(path,method,body,{Authorization:`Bearer ${token}`});
  const refresh=async()=>{const r=await call<{subject:string;spaces:Space[]}>('/vault');setSubject(r.subject);setSpaces(r.spaces);};
  const act=async(work:()=>Promise<void>)=>{setBusy(true);setMessage('');try{await work();}catch(e){setMessage(e instanceof Error?e.message:String(e));}finally{setBusy(false);}};
  return <details className="section workspace-vault"><summary>계정 보관함 · {configured?'서버 저장소 연결됨':configured===null?'연결 확인 중':'설정 필요'}</summary>
    <p>프로젝트 버전·문서 검토·지도·계획·현재 실행 기록을 함께 보관합니다. 복원은 초기 구성에서 일시 정지하며, 이전 승인을 다시 실행하지 않습니다.</p>
    {!configured?<p role="status">현재 서버에는 영구 저장소·계정 인증이 연결되지 않았습니다. 아래 작업 기록의 세션 저장과 다릅니다. Vercel 실행 공간 밖의 저장소 설정이 필요합니다.</p>:<>
      <label>계정 접근 토큰 <input type="password" autoComplete="off" value={token} onChange={e=>{setToken(e.target.value);setSubject('');setSpaces([]);}} placeholder="관리자가 제공한 계정 토큰 · LLM API 키 아님"/></label>
      <button disabled={busy||token.length<32} onClick={()=>void act(refresh)}>계정 연결</button>
      {subject&&<><p>{subject} · 토큰은 이 화면의 메모리에만 유지됩니다.</p><button disabled={busy} onClick={()=>void act(async()=>{await call('/vault','POST',{});await refresh();setMessage('현재 실행 구성과 검토 자료를 새 보관 항목으로 저장했습니다. 미적용 편집은 먼저 프로젝트 버전으로 저장하세요.');})}>현재 실행·자료 새로 보관</button>
        <ul>{spaces.map(s=><li key={s.id}><strong>{s.title}</strong> · v{s.revision} · {({owner:'소유자',editor:'편집',operator:'실행',reader:'읽기'} as Record<string,string>)[s.role]}
          <button disabled={busy} onClick={()=>void act(async()=>{downloadJSON(`workspace-${s.id}-v${s.revision}.json`,await call(`/vault/${s.id}?revision=${s.revision}`));})}>자료 내보내기</button>
          {s.role!=='reader'&&<button disabled={busy} onClick={()=>void act(async()=>{await beforeRestore();const r=await call<{project:Project;run_id:string}>(`/vault/${s.id}/restore?revision=${s.revision}`,'POST');await onRestored(r.project,r.run_id);setMessage('초기 구성으로 복원했습니다. 실행하려면 계획을 새로 검토·승인하세요.');})}>초기 구성 복원</button>}
          {['owner','editor'].includes(s.role)&&<button disabled={busy} onClick={()=>void act(async()=>{await call('/vault','POST',{id:s.id,expected_revision:s.revision});await refresh();})}>현재 자료로 새 버전 저장</button>}
          {s.role==='owner'&&<details><summary>계정별 보관함 권한</summary><p>보관 자료의 읽기·저장·복원 권한입니다. 앱 전체의 관제 권한과는 별도입니다.</p><label>받는 계정<input value={shareSubject} onChange={e=>setShareSubject(e.target.value)}/></label><label>권한<select value={role} onChange={e=>setRole(e.target.value)}><option value="reader">읽기</option><option value="editor">저장·복원</option><option value="operator">복원</option></select></label><button disabled={busy||!shareSubject} onClick={()=>void act(async()=>{await call(`/vault/${s.id}/share`,'POST',{subject:shareSubject,role});setMessage('공유 권한을 저장했습니다.');})}>권한 저장</button></details>}
        </li>)}</ul></>}
    </>}
    {message&&<p role="status">{message}</p>}
  </details>;
}
