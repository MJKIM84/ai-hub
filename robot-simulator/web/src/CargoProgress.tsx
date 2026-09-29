import type {Project,RunState} from './types';
import './cargo-progress.css';

const phases:Record<string,string>={loading_approach:'예약된 상차 위치로 접근',loading:'파지·상차',await_load:'적재 지지 확인',transport:'적재 운반',settle:'인계 지점 정차',await_receiver:'인수 준비',handoff_grasp:'인수 팔 파지',separating:'적재면에서 분리',confirm_handoff:'배치·지지·접촉 해제 확인'};
const labels:Record<string,string>={pending:'시작 전',waiting:'선행 작업 대기',running:'진행 중',completed:'완료',failed:'실패',cancelled:'취소',skipped:'미실행'};

export function CargoProgress({project,state,onFocus}:{project:Project;state:RunState;onFocus:(id:string)=>void}) {
  const jobs=project.tasks.filter(t=>t.cooperation);
  if(!jobs.length)return null;
  const robot=(id:string)=>project.robots.find(r=>r.id===id)?.name??id;
  return <section className="cargo-progress" aria-label="물품 업무 진행">
    <header><strong>물품 업무</strong><span>관측 완료 {state.tasks.filter(t=>t.status==='completed').length} / {state.tasks.length}단계 · 시간 예측 아님</span></header>
    <div className="cargo-progress__steps">{jobs.map(task=>{
      const live=state.tasks.find(t=>t.id===task.id);const c=task.cooperation!;
      const phase=live?.cooperation?.phase;
      const operator=phase==='loading'?c.donor_id:phase&&['handoff_grasp','separating','confirm_handoff'].includes(phase)?c.receiver_id:c.carrier_id;
      const carrier=state.robots.find(r=>r.id===c.carrier_id);
      const item=state.items?.find(i=>i.id===task.item_id);
      const wait=carrier?.pedestrian_avoidance;
      return <article key={task.id} data-status={live?.status??'pending'}>
        <strong>{task.name}</strong><span>{labels[live?.status??'pending']??live?.status}{live?.status==='running'&&phase?` · ${phases[phase]??phase}`:''}</span>
        <small>{live?.status==='running'&&wait&&['yielding','waiting','detouring','detour_align'].includes(wait.mode)?wait.reason:live?.reason??'전체 계획 승인 후 시작'}</small>
        {item&&<small>{item.damaged?'물품 손상 · ':''}{item.owner?`${robot(item.owner)} 담당`:'로봇 접촉 해제 상태'} · 높이 {item.position[2].toFixed(2)}m</small>}
        <div><button onClick={()=>onFocus(operator??c.carrier_id)}>현재 작업 보기</button><button onClick={()=>onFocus(c.carrier_id)}>운반차 보기</button>{task.item_id&&<button onClick={()=>onFocus(task.item_id!)}>물품 보기</button>}</div>
      </article>;
    })}</div>
  </section>;
}
