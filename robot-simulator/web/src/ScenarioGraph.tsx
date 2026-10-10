import { RuntimeReviewPanel } from './RuntimeReviewPanel';
import { useMemo } from 'react';
import type { Project, RunState } from './types';
import './ScenarioGraph.css';

const statusNames: Record<string,string> = {pending:'배정 대기',waiting:'대기',running:'진행',completed:'완료',failed:'실패',cancelled:'취소',skipped:'분기 제외'};
export function ScenarioGraph({project,run,selected,onSelect,onLocate}:{project:Project;run?:RunState|null;selected:string;onSelect:(id:string)=>void;onLocate:(id:string)=>void}) {
  const layout=useMemo(()=>{
    const levels=new Map<string,number>();
    const rank=(id:string,visiting=new Set<string>()):number=>{
      if(levels.has(id)) return levels.get(id)!;
      if(visiting.has(id)) return 0;
      const next=new Set(visiting).add(id),task=project.tasks.find(t=>t.id===id);
      const value=task?.predecessor_ids.length?1+Math.max(...task.predecessor_ids.map(p=>rank(p,next))):0;
      levels.set(id,value);return value;
    };
    project.tasks.forEach(t=>rank(t.id));
    const rows=new Map<number,number>();
    return project.tasks.map(t=>{const column=levels.get(t.id)??0,row=rows.get(column)??0;rows.set(column,row+1);return {task:t,x:column*260+16,y:row*136+20};});
  },[project.tasks]);
  const width=Math.max(520,...layout.map(n=>n.x+244)),height=Math.max(166,...layout.map(n=>n.y+120));
  const task=project.tasks.find(t=>t.id===selected),observed=run?.tasks.find(t=>t.id===selected);
  const locatedRobot=observed?.robot_id??task?.preferred_robot??task?.cooperation?.carrier_id;
  return <section className="scenario-graph" aria-label="시나리오 작업 그래프">
    <header><div><span className="graph-eyebrow">SCENARIO / 작업 관계</span><h3>어떤 일이 끝나야 다음 일을 할 수 있나요?</h3></div><span>{project.tasks.length}개 작업 · {run?`실행 ${run.run_id.slice(0,8)}`:'편집 초안'}</span></header>
    <p className="muted">같은 열의 작업은 병행할 수 있습니다. 작업을 선택해 아래에서 조건을 편집하세요. 변경은 저장·검토 후 실행에 반영됩니다.</p>
    <div className="graph-scroll" tabIndex={0} aria-label="좌우로 이동하는 작업 관계도">
      <div className="graph-canvas" style={{width,height}}>
        <svg width={width} height={height} aria-hidden="true"><defs><marker id="task-arrow" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="currentColor"/></marker></defs>
          {layout.flatMap(n=>n.task.predecessor_ids.map(id=>{const from=layout.find(p=>p.task.id===id);return from?<path key={`${id}-${n.task.id}`} d={`M${from.x+224},${from.y+49} C${from.x+246},${from.y+49} ${n.x-24},${n.y+49} ${n.x},${n.y+49}`} markerEnd="url(#task-arrow)"/>:null;}))}
        </svg>
        {layout.map(({task:t,x,y})=>{const state=run?.tasks.find(r=>r.id===t.id);return <button key={t.id} className={`graph-node ${state?.status??''}`} style={{left:x,top:y}} aria-pressed={selected===t.id} onClick={()=>onSelect(t.id)}>
          <span className="graph-node-status">{state?(statusNames[state.status]??state.status):'초안'} · {project.environment.floors.find(f=>f.id===t.floor_id)?.name??t.floor_id}</span>
          <strong>{t.name}</strong><small>{project.robots.find(r=>r.id===(state?.robot_id??t.preferred_robot??t.cooperation?.carrier_id))?.name??'능력에 따라 배정'}{t.quantity>1?` · ${t.quantity}회`:''}{t.condition?' · 조건 분기':''}{t.confirmation?' · 사람 확인':''}</small>
        </button>;})}
      </div>
    </div>
    {task&&<div className="graph-evidence" aria-live="polite"><div><h4>{task.name}</h4><p>{observed?.reason||'선행 조건과 실행 가능한 로봇을 검토합니다.'}</p>
      <dl><dt>완료 조건</dt><dd>{task.cooperation?'물품의 최종 지지·배치와 인계 접촉 해제를 실행기가 확인':'목표 도착·정지 및 설정한 체류 조건 확인'}{task.confirmation?` · ${task.confirmation.criterion}`:''}</dd><dt>현재 판정</dt><dd>{observed?(statusNames[observed.status]??observed.status):'현재 초안의 실행 근거 없음'}</dd></dl>
      {observed?.evidence?<details><summary>실행기가 기록한 완료 근거</summary><pre>{JSON.stringify(observed.evidence,null,2)}</pre></details>:<small>물리 관측 근거가 없는 단계는 완료로 표시하지 않습니다.</small>}
    </div><button disabled={!locatedRobot} onClick={()=>locatedRobot&&onLocate(locatedRobot)}>담당 로봇 위치 보기</button></div>}
    {run&&task&&<RuntimeReviewPanel run={run} taskId={task.id}/>}
  </section>;
}
