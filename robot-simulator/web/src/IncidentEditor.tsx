import type { FaultInjection, Project, RunState } from './types';
import './ScenarioGraph.css';

const kinds:Record<string,string>={communication:'통신 끊김',motor:'구동 장애',sensor:'센서 장애',facility:'시설 장애',push:'외력',battery:'배터리 설정',recover:'장애 해제'};
const phases:Record<string,string>={armed:'조건 대기',active:'발생',released:'해제',blocked:'기존 장애로 차단'};
export function IncidentEditor({project,run,onChange}:{project:Project;run?:RunState|null;onChange:(faults:FaultInjection[])=>void}) {
  const patch=(i:number,update:Partial<FaultInjection>)=>onChange(project.faults.map((f,j)=>j===i?{...f,...update}:f));
  const targets=[...project.robots,...project.environment.elements.filter(e=>['elevator','door','charger','dock'].includes(e.kind))];
  return <section aria-label="돌발 상황 구성"><div className="section-head"><div><h3>작업 진행에 맞춰 상황을 바꾸세요</h3><p className="muted">실제 완료 상태나 관측 사건으로 발생합니다. 변경은 실행 전 전체 계획에 포함해 검토하세요.</p></div><button disabled={!targets.length} onClick={()=>onChange([...project.faults,{time:0,target_id:targets[0].id,kind:project.robots.some(r=>r.id===targets[0].id)?'communication':'facility',magnitude:100,duration:5,auto_recover:true,max_occurrences:1,trigger:project.tasks.length?{kind:'task_status',task_id:project.tasks[0].id,status:'completed'}:null}])}>돌발 상황 추가</button></div>
    {!project.faults.length&&<p className="empty">예: 상차가 완료되면 운반 로봇의 통신을 5초간 끊고 복구합니다.</p>}
    <div className="incident-list">{project.faults.map((f,i)=>{const observed=run?.incidents?.find(r=>r.index===i),mode=f.trigger?.kind??'time';const automatic=['motor','sensor','communication','facility'].includes(f.kind);return <article className="incident-row" key={i}>
      <header><strong>상황 {i+1} · {kinds[f.kind]}</strong><span>{observed?`${phases[observed.phase]??observed.phase} · ${observed.count}회`:'편집 초안'}</span><button onClick={()=>onChange(project.faults.filter((_,j)=>j!==i))}>삭제</button></header>
      <div className="incident-fields">
        <label>발생 조건<select value={mode} onChange={e=>patch(i,{max_occurrences:1,trigger:e.target.value==='time'?null:e.target.value==='task_status'?{kind:'task_status',task_id:project.tasks[0]?.id,status:'completed'}:{kind:'event',event_kind:'cooperation_loaded'}})}><option value="time">지정 시각</option><option value="task_status">작업 상태</option><option value="event">관측 사건</option></select></label>
        {mode==='task_status'&&<><label>조건 작업<select value={f.trigger?.task_id??''} onChange={e=>patch(i,{trigger:{...f.trigger!,task_id:e.target.value}})}><option value="">작업 선택</option>{project.tasks.map(t=><option key={t.id} value={t.id}>{t.name}</option>)}</select></label><label>작업 결과<select value={f.trigger?.status??'completed'} onChange={e=>patch(i,{trigger:{...f.trigger!,status:e.target.value as 'completed'}})}><option value="completed">완료</option><option value="failed">실패</option><option value="cancelled">취소</option></select></label></>}
        {mode==='event'&&<><label>관측 사건<select value={f.trigger?.event_kind??'cooperation_loaded'} onChange={e=>patch(i,{trigger:{...f.trigger!,event_kind:e.target.value as 'cooperation_loaded'}})}><option value="cooperation_loaded">물품 상차·지지 확인</option><option value="task_completed">작업 완료 사건</option><option value="task_failed">작업 실패 사건</option><option value="pedestrian_avoidance">보행자 회피 상태 변경</option></select></label><label>사건의 작업<select value={f.trigger?.task_id??''} onChange={e=>patch(i,{trigger:{...f.trigger!,task_id:e.target.value||null}})}><option value="">모든 작업</option>{project.tasks.map(t=><option key={t.id} value={t.id}>{t.name}</option>)}</select></label><label>최대 발생 횟수<input type="number" min={1} max={10} value={f.max_occurrences??1} onChange={e=>patch(i,{max_occurrences:Number(e.target.value)})}/></label></>}
        <label>{mode==='time'?'발생 시각 (초)':'발생 가능 시작 시각 (초)'}<input type="number" min={0} value={f.time} onChange={e=>patch(i,{time:Number(e.target.value)})}/></label>
        <label>장애 대상<select value={f.target_id} onChange={e=>{const isRobot=project.robots.some(r=>r.id===e.target.value);patch(i,{target_id:e.target.value,kind:isRobot?'communication':'facility',auto_recover:true});}}>{targets.map(t=><option key={t.id} value={t.id}>{t.name}</option>)}</select></label>
        <label>종류<select value={f.kind} onChange={e=>patch(i,{kind:e.target.value as FaultInjection['kind'],auto_recover:false})}>{Object.entries(kinds).filter(([k])=>project.robots.some(r=>r.id===f.target_id)?k!=='facility':['facility','recover'].includes(k)).map(([k,n])=><option key={k} value={k}>{n}</option>)}</select></label>
        {(f.kind==='push'||f.kind==='battery')&&<label>{f.kind==='push'?'외력 크기 (N)':'설정 잔량 (%)'}<input type="number" min={0} max={f.kind==='battery'?100:undefined} step={1} value={f.magnitude} onChange={e=>patch(i,{magnitude:Number(e.target.value)})}/></label>}
        <label>해제 방식<select disabled={!automatic} value={f.auto_recover?'automatic':'manual'} onChange={e=>patch(i,{auto_recover:e.target.value==='automatic'})}><option value="manual">자동 해제하지 않음</option><option value="automatic">지속 시간 후 해제</option></select></label>
        <label>지속 시간 (초)<input type="number" min={.1} step={.1} value={f.duration} onChange={e=>patch(i,{duration:Number(e.target.value)})}/></label>
      </div>
      {observed?.triggered_at!=null&&<p>발생 {observed.triggered_at.toFixed(2)}초{observed.release_at!=null?` · 해제 예정 ${observed.release_at.toFixed(2)}초`:''}</p>}
      {!f.auto_recover&&f.kind!=='push'&&<small>지속 시간만 입력해도 자동 복구되지는 않습니다. 명시적인 장애 해제가 필요합니다.</small>}
    </article>;})}</div>
  </section>;
}
