"""Actual Session charge/undock/workflow evidence; no physical pose mutation."""
from __future__ import annotations
from copy import deepcopy
import argparse
import hashlib
import json
import math
from pathlib import Path
import statistics
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from robot_platform.catalog import model_by_id
from robot_platform.domain import Project,Element,RobotInstance,Pose,Size,SensorSettings,Policy,Task,FaultInjection
from robot_platform.experiments import manifest
from robot_platform.runtime import Session

PROCESS_SOURCE_SHA256={str(path.relative_to(ROOT/'src/robot_platform')):hashlib.sha256(path.read_bytes()).hexdigest() for path in (ROOT/'src/robot_platform').rglob('*.py')}


def unchanged(before,after):
    return before['source_sha256']==after['source_sha256']==PROCESS_SOURCE_SHA256


def project(kind='amr',seed=1,with_task=True,capacity=4.,battery=19.,charge_until=30.):
    staging=4.5-model_by_id(kind)['size']['x']/2-.062-1.
    p=Project(id=f'charging-integration-{kind}-{seed}',name='연구용 충전 통합 시험',environment={'id':'charge-floor','elements':[Element(id='charge',kind='charger',floor_id='floor-1',pose=Pose(x=4.5,y=3),size=Size(x=1,y=1,z=.5))]},
        robots=[RobotInstance(id='robot',model_id=kind,pose=Pose(x=staging,y=3),battery=battery,battery_capacity_wh=capacity,sensors=SensorSettings(position_noise=.002,yaw_noise=.001))],policy=Policy(charge_until=charge_until),
        tasks=[Task(id='after-charge',kind='patrol',destination=Pose(x=2.4,y=3.8),release_time=40,timeout=60,retries=0)] if with_task else [])
    p.physics.seed=seed
    return p


def until(session,predicate,seconds=50.,stride=10):
    end=session.time+seconds
    while session.time<end-1e-9:
        session.step(stride)
        if predicate(session):return True
    return False


def physical_connector(session,rid='robot',eid='charge'):
    return session.world.charger_observations(session.time)[eid]['contacts'][rid]


def connector_safe(reading):
    return reading['left'] and reading['right'] and reading['aligned'] and reading['relative_speed']<=.04


def run_case(kind='amr',seed=1):
    p=project(kind,seed,charge_until=40.)
    before=manifest(p)
    s=Session(p)
    initial_energy=p.robots[0].battery/100*p.robots[0].battery_capacity_wh*3600
    transitions=[];last=None;unsafe=[];powered_steps=0;idle_after_charge=False;max_energy_error=0.;peak_battery=19.;power_at_undock=[]
    while s.time<150.:
        s.step(1)
        reading=physical_connector(s)
        phase=s.facility_states['charge'].get('phase','idle')
        robot_state=s.orchestrator.robot_states['robot']['status']
        if s.charge_power['robot']>0:
            powered_steps+=1
            if not connector_safe(reading):unsafe.append({'time':s.time,'power':s.charge_power['robot'],'connector':reading})
        if phase=='undock' and s.charge_power['robot']>0:power_at_undock.append(s.time)
        peak_battery=max(peak_battery,s.batteries['robot'])
        balance=initial_energy-s.energy['robot']+s.charge_stored['robot']
        actual=s.batteries['robot']/100*p.robots[0].battery_capacity_wh*3600
        max_energy_error=max(max_energy_error,abs(balance-actual))
        if s.charge_input['robot']>0 and robot_state=='idle' and 'robot' not in s.orchestrator.charging.plans:idle_after_charge=True
        key=(phase,robot_state,s.orchestrator.tasks['after-charge']['status'])
        if key!=last:
            transitions.append({'time':s.time,'phase':phase,'robot_status':robot_state,'battery':s.batteries['robot'],'power_w':s.charge_power['robot'],'pose':s.world.truth('robot')['pose'],'connector':deepcopy(reading),'task_status':key[2],'reason':s.orchestrator.robot_states['robot']['reason']})
            last=key
        if s.orchestrator.tasks['after-charge']['status'] in ('completed','failed'):break
    after=manifest(p)
    requests=[s.orchestrator.charging.manager._receipt(r) for r in s.orchestrator.charging.manager.requests.values()]
    completed=any(r['status']=='completed' for r in requests)
    passed=completed and idle_after_charge and s.orchestrator.tasks['after-charge']['status']=='completed' and not unsafe and not power_at_undock and max_energy_error<1e-6
    return {'kind':kind,'seed':seed,'passed':passed,'sim_time':s.time,'manifest':before,'source_unchanged_during_run':unchanged(before,after),
        'experimental_capacity_wh':4.,'capacity_basis':'Test-only accelerated SOC progression, not a measured robot battery or manufacturer specification',
        'charge_until_percent':p.policy.charge_until,
        'powered_physics_steps':powered_steps,'power_without_safe_current_contact':unsafe,'power_during_undock':power_at_undock,'max_energy_balance_error_j':max_energy_error,
        'idle_after_charge':idle_after_charge,'peak_battery_percent':peak_battery,'final_battery_percent':s.batteries['robot'],'final_power_w':s.charge_power['robot'],
        'final_connector':physical_connector(s),'requests':requests,'metrics':s.metrics(),'tasks':s.orchestrator.task_rows(),'events':s.events,'transitions':transitions,
        'warnings':[int(w.number) for w in s.world.data.warning]}


def queue_case(seconds=150.):
    if not math.isfinite(seconds) or seconds<=0:raise ValueError('seconds must be finite and positive')
    p=project(with_task=False)
    p.id='charging-fifo-diagnostic'
    p.robots.append(RobotInstance(id='second',model_id='delivery',pose=Pose(x=2,y=5.5),battery=19,battery_capacity_wh=4,sensors=SensorSettings(position_noise=.002,yaw_noise=.001)))
    before=manifest(p)
    s=Session(p);samples=[];tail=[];completed=set();parking_targets={};completion_evidence={}
    audits={'physics_steps_checked':0,'timestep_seconds':p.physics.timestep,'maximum_simultaneously_powered':0,'simultaneous_power_steps':0,'unsafe_contact_power_steps':0,'unreserved_power_steps':0,'robot_robot_contact_steps':0,'fifo_violation_steps':0,'violation_examples':[],
            'powered_steps':{rid:0 for rid in ('robot','second')},'first_power_at':{},'minimum_powered_normal_force_n':{},'maximum_powered_relative_speed_m_s':{},'reservation_grants':[]}
    last_active=None;event_cursor=0;steps=math.floor(seconds/p.physics.timestep+1e-8)
    for index in range(steps):
        for rid,plan in s.orchestrator.charging.plans.items():
            if plan.get('parking'):parking_targets[rid]=deepcopy(plan['parking'])
        s.step(1)
        audits['physics_steps_checked']+=1
        connectors=s.world.charger_observations(s.time)['charge']['contacts']
        powered=[rid for rid,value in s.charge_power.items() if value>0]
        audits['maximum_simultaneously_powered']=max(audits['maximum_simultaneously_powered'],len(powered))
        problems=[]
        if len(powered)>1:
            audits['simultaneous_power_steps']+=1;problems.append('simultaneous_power')
        active=s.orchestrator.charging.manager.stations['charge'].active
        active_id=active.id if active else None
        if active_id!=last_active and active is not None:
            audits['reservation_grants'].append({'time':s.time,'request_id':active.id,'robot_id':active.robot_id,'requested_at':active.requested_at})
        last_active=active_id
        pending=[r for r in s.orchestrator.charging.manager.requests.values() if r.status in ('queued','running')]
        if active and pending and active.id!=pending[0].id:
            audits['fifo_violation_steps']+=1;problems.append('reservation_out_of_fifo_order')
        for rid in powered:
            reading=connectors[rid]
            audits['powered_steps'][rid]+=1;audits['first_power_at'].setdefault(rid,s.time)
            audits['minimum_powered_normal_force_n'][rid]=min(audits['minimum_powered_normal_force_n'].get(rid,float('inf')),reading['normal_force'])
            audits['maximum_powered_relative_speed_m_s'][rid]=max(audits['maximum_powered_relative_speed_m_s'].get(rid,0.),reading['relative_speed'])
            if not connector_safe(reading):
                audits['unsafe_contact_power_steps']+=1;problems.append('power_without_safe_physical_contacts:'+rid)
            if active is None or active.robot_id!=rid:
                audits['unreserved_power_steps']+=1;problems.append('power_without_active_reservation:'+rid)
        mutual=[c for c in s.world.contacts() if {c['a'],c['b']}=={'robot','second'}]
        if mutual:
            audits['robot_robot_contact_steps']+=1;problems.append('robot_robot_contact')
        if problems and len(audits['violation_examples'])<20:
            audits['violation_examples'].append({'time':s.time,'problems':problems,'power_w':deepcopy(s.charge_power),'connectors':deepcopy(connectors),'mutual_contacts':mutual})
        for event in s.events[event_cursor:]:
            if event['kind']=='charging_completed' and event['entity_id'] not in completed:
                rid=event['entity_id'];completed.add(rid)
                observation=s.observations[rid];target=parking_targets[rid]
                position_error=math.hypot(observation['pose']['x']-target['x'],observation['pose']['y']-target['y'])
                yaw_error=abs((observation['pose']['yaw']-target['yaw']+math.pi)%(2*math.pi)-math.pi)
                speed=math.sqrt(sum(v*v for v in observation['velocity']))
                clear=not connectors[rid]['left'] and not connectors[rid]['right'] and s.charge_power[rid]==0
                completion_evidence[rid]={'event_time':event['time'],'sampled_at':observation['sampled_at'],'observed_pose':deepcopy(observation['pose']),'actual_pose':s.world.truth(rid)['pose'],'parking_target':target,'position_error_m':position_error,'yaw_error_rad':yaw_error,'observed_speed_m_s':speed,'power_w':s.charge_power[rid],'physical_connector':deepcopy(connectors[rid]),'passed':position_error<.08 and yaw_error<.1 and speed<.04 and clear}
        event_cursor=len(s.events)
        finished={'robot','second'}<=completed
        if (index+1)%100==0 or index==steps-1 or finished:
            tail.append({'time':s.time,'robots':{rid:{'pose':s.world.truth(rid)['pose'],'battery':s.batteries[rid],'reason':state['reason'],'delivered_command':deepcopy(s.world.commands[rid]),'remaining_path':deepcopy(state['path']),'parking_target':deepcopy(s.orchestrator.charging.plans.get(rid,{}).get('parking'))} for rid,state in s.orchestrator.robot_states.items()}})
            if len(tail)>101:tail.pop(0)
        if (index+1)%1000==0 or index==steps-1 or finished:
            samples.append({'time':s.time,'station':deepcopy(s.facility_states['charge']),'robots':{rid:{'pose':s.world.truth(rid)['pose'],'battery':s.batteries[rid],'status':state['status'],'reason':state['reason']} for rid,state in s.orchestrator.robot_states.items()}})
        if finished:break
    requests=[s.orchestrator.charging.manager._receipt(r) for r in s.orchestrator.charging.manager.requests.values()]
    after=manifest(p)
    completions={rid:next((e['time'] for e in s.events if e['kind']=='charging_completed' and e['entity_id']==rid),None) for rid in ('robot','second')}
    audits['passed']=all(audits[key]==0 for key in ('simultaneous_power_steps','unsafe_contact_power_steps','unreserved_power_steps','robot_robot_contact_steps','fifo_violation_steps'))
    both_completed=all(value is not None for value in completions.values())
    warnings=[int(w.number) for w in s.world.data.warning]
    passed=both_completed and audits['passed'] and all(row['passed'] for row in completion_evidence.values()) and not any(warnings)
    source_digest=hashlib.sha256(json.dumps(before['source_sha256'],sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return {'passed':passed,'limit_seconds':seconds,'sim_time':s.time,'manifest':before,'source_digest_sha256':source_digest,'source_unchanged_during_run':unchanged(before,after),'both_completed':both_completed,'completed_at':completions,'completion_evidence':completion_evidence,'physical_step_audits':audits,'requests':requests,'samples':samples,'last_20_seconds':tail,'metrics':s.metrics(),'events':s.events,'warnings':warnings, 'scope':f'Up to {seconds:g} simulated seconds, with no follow-on task to clear the first robot; completion requires charging_completed after observed automatic clearance'}


def insufficient_energy_case():
    p=project(charge_until=30.)
    before=manifest(p);s=Session(p)
    found=until(s,lambda value:'조정 필요' in value.orchestrator.robot_states['robot']['reason'],seconds=80)
    s.step(2500)
    requests=[s.orchestrator.charging.manager._receipt(r) for r in s.orchestrator.charging.manager.requests.values()]
    state=s.orchestrator.robot_states['robot'];task=s.orchestrator.tasks['after-charge']
    passed=found and len(requests)==1 and requests[0]['status']=='completed' and state['status']=='idle' and task['status']=='waiting' and s.charge_power['robot']==0
    return {'name':'insufficient_post_charge_task_reserve','passed':passed,'manifest':before,'source_unchanged_during_run':unchanged(before,manifest(p)),'sim_time':s.time,'experimental_capacity_wh':4,'charge_until_percent':30,'battery_percent':s.batteries['robot'],'robot_state':{key:state.get(key) for key in ('status','reason','charge_needed_percent')},'task':s.orchestrator.task_rows()[0],'requests':requests,'events':s.events,'expected_behavior':'Complete observed charging and clearance, withhold energy-infeasible work, explain the insufficient endpoint/capacity/task configuration, and avoid an immediate recharge loop'}


def safety_case(name):
    """Retain measured safety outcomes even when a regression is discovered."""
    p=project(with_task=False,battery=50. if name=='forged_enable' else 19.)
    if name=='default_capacity':
        p=project(with_task=False,capacity=400.,battery=19.99,charge_until=20.1)
    before=manifest(p)
    s=Session(p);evidence={};passed=False
    if name=='forged_enable':
        s.step(500)
        s.orchestrator.charging.power_requests={'robot':{'station_id':'charge','power_w':1e9}}
        initial_battery=s.batteries['robot'];powers=[]
        for _ in range(100):
            s.world.step();s._evaluate()
            powers.append(s.charge_power['robot'])
        evidence={'forged_power_request_w':1e9,'maximum_delivered_power_w':max(powers),'input_j':s.charge_input['robot'],'stored_j':s.charge_stored['robot'],'battery_before':initial_battery,'battery_after':s.batteries['robot'],'connector':physical_connector(s),'method':'Retain forged enable while directly advancing PhysicsWorld and evaluating the local electrical interlock'}
        passed=max(powers)==0 and s.charge_input['robot']==s.charge_stored['robot']==0 and s.batteries['robot']<initial_battery
    elif name=='invalid_control_timestamps':
        ready=until(s,lambda value:value.facility_states['charge'].get('phase')=='dock',seconds=5)
        outcomes=[]
        if ready:
            original=s.observations['robot']
            valid=s.orchestrator.charging.command('robot',original,s.time)
            for case in ('stale','future','nonfinite','missing'):
                observation=deepcopy(original);now=s.time
                if case=='stale':now+=p.policy.stale_after+.1
                elif case=='future':observation['sampled_at']=now+.001
                elif case=='nonfinite':observation['sampled_at']=float('nan')
                else:observation.pop('sampled_at')
                command=s.orchestrator.charging.command('robot',observation,now)
                outcomes.append({'case':case,'command':command,'passed':command['v']==command['w']==0})
            evidence={'valid_observation_command':valid,'invalid_observation_commands':outcomes,'policy_stale_after_seconds':p.policy.stale_after}
            passed=valid['v']>0 and all(row['passed'] for row in outcomes)
    elif name=='default_capacity':
        ready=until(s,lambda value:value.charge_input['robot']>40,seconds=40)
        expected=19.99/100*400*3600-s.energy['robot']+s.charge_stored['robot']
        error=abs(s.batteries['robot']/100*400*3600-expected)
        efficiency_error=abs(s.charge_stored['robot']-.9*s.charge_input['robot'])
        evidence={'capacity_wh':400,'input_j':s.charge_input['robot'],'stored_j':s.charge_stored['robot'],'consumed_j':s.energy['robot'],'battery_percent':s.batteries['robot'],'energy_balance_error_j':error,'efficiency_error_j':efficiency_error}
        passed=ready and error<1e-5 and efficiency_error<1e-7
    else:
        ready=until(s,lambda value:value.charge_power['robot']>0,seconds=40)
        if not ready:evidence={'failure':'Did not establish actual charging before intervention'}
        elif name=='physical_loss_before_delayed_observation':
            old=deepcopy(s.observations['robot']);first_loss=None;unsafe_power=[];gap_seen=False
            s.next_sensor=s.time+1;s.next_orchestration=s.time+1
            s.world.command('robot',v=-.15,mode='drive')
            start=s.time
            for _ in range(300):
                s.step(1);reading=physical_connector(s)
                if not connector_safe(reading):
                    if first_loss is None:first_loss={'time':s.time,'power_w':s.charge_power['robot'],'connector':deepcopy(reading)}
                    if s.charge_power['robot']>0:unsafe_power.append({'time':s.time,'power_w':s.charge_power['robot']})
                if not reading['left'] and not reading['right']:gap_seen=True
            cached=s.observations['robot']
            evidence={'intervention_time':start,'first_unsafe_physical_sample':first_loss,'unsafe_positive_power':unsafe_power,'both_pads_physically_clear':gap_seen,'cached_sensor_still_connected':cached['sensors']['docking']['charge']['left'] and cached['sensors']['docking']['charge']['right'],'cached_sample_unchanged':cached['sampled_at']==old['sampled_at'],'physics_steps_checked':300}
            passed=gap_seen and not unsafe_power and evidence['cached_sample_unchanged'] and evidence['cached_sensor_still_connected']
        elif name=='sensor_dropout':
            s.bus.settings['robot'].dropout=1.;s.step(600)
            stale={'age_seconds':s.time-s.observations['robot']['sampled_at'],'power_w':s.charge_power['robot'],'fault_latched':s.orchestrator.charging.manager.stations['charge'].fault_latched}
            s.bus.settings['robot'].dropout=0.;s.step(200)
            before_resume=s.charge_power['robot'];receipt=s.resume_robot('robot')
            resumed=until(s,lambda value:value.charge_power['robot']>0,seconds=15)
            evidence={'stale_stream':stale,'power_before_explicit_resume_w':before_resume,'resume_receipt':receipt,'resumed':resumed,'connector_after_resume':physical_connector(s)}
            passed=stale['age_seconds']>p.policy.stale_after and stale['power_w']==0 and stale['fault_latched'] and before_resume==0 and resumed and connector_safe(physical_connector(s))
        else:
            initial_input=s.charge_input['robot'];start=s.time
            if name=='operator_stop':s.command('robot','stop')
            else:s.inject(FaultInjection(target_id='charge' if name=='facility_fault' else 'robot',kind='facility' if name=='facility_fault' else 'communication'))
            s.step(1)
            first={'time':s.time,'power_w':s.charge_power['robot'],'added_input_j':s.charge_input['robot']-initial_input}
            s.step(600);held=s.charge_input['robot']-initial_input
            before_resume=None
            if name!='operator_stop':
                s.inject(FaultInjection(target_id='charge' if name=='facility_fault' else 'robot',kind='recover'));s.step(200)
                before_resume=s.charge_power['robot']
            receipt=s.resume_robot('robot');resumed=until(s,lambda value:value.charge_power['robot']>0,seconds=15)
            evidence={'intervention_time':start,'first_post_intervention_physics_tick':first,'added_input_during_fault_j':held,'power_after_fault_clear_before_robot_resume_w':before_resume,'resume_receipt':receipt,'resumed':resumed,'connector_after_resume':physical_connector(s),'recovery_semantics':'Facility recover is explicit station recovery; communication clear additionally requires explicit robot resume'}
            passed=first['power_w']==0 and first['added_input_j']==0 and held==0 and resumed and connector_safe(physical_connector(s)) and (name!='communication_fault' or before_resume==0)
    after=manifest(p)
    return {'name':name,'passed':passed,'sim_time':s.time,'manifest':before,'source_unchanged_during_run':unchanged(before,after),'evidence':evidence,'events':s.events,'warnings':[int(w.number) for w in s.world.data.warning]}


def summarize(cases):
    summaries={}
    for kind in ('amr','delivery'):
        rows=[row for row in cases if row['kind']==kind]
        summaries[kind]={'n':len(rows),'passed':sum(row['passed'] for row in rows),'seeds':[row['seed'] for row in rows],'source_verified_unchanged':all(row['source_unchanged_during_run'] for row in rows)}
        for key in ('sim_time','final_battery_percent','max_energy_balance_error_j'):
            values=[row[key] for row in rows]
            summaries[kind][key]={'mean':statistics.mean(values),'sample_stddev':statistics.stdev(values) if len(values)>1 else None}
    return summaries


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fifo-seconds',type=float,help='Run only the audited FIFO follow-up with this explicit simulation limit')
    args=parser.parse_args()
    if args.fifo_seconds is not None:
        baseline_path=ROOT/'reports/charging-integration.json'
        baseline_bytes=baseline_path.read_bytes();baseline=json.loads(baseline_bytes)['fifo_diagnostic']
        followup=queue_case(seconds=args.fifo_seconds)
        comparison={'baseline_report':str(baseline_path),'baseline_report_sha256':hashlib.sha256(baseline_bytes).hexdigest(),'baseline_limit_seconds':baseline.get('limit_seconds',150.),'baseline_both_completed':baseline['both_completed'],'baseline_completed_at':baseline['completed_at'],'same_project_input':baseline['manifest']['input_sha256']==followup['manifest']['input_sha256'],'same_production_source':baseline['manifest']['source_sha256']==followup['manifest']['source_sha256']}
        result={'comparison_to_preserved_150s_diagnostic':comparison,'followup':followup,'limitations':['A single seed with two authored research wheeled robots in an open-floor scene','4Wh is a test-only accelerated capacity, not measured hardware','Actual MuJoCo contacts and delayed observations; no hardware validation','The 150s noncompletion remains unchanged in charging-integration.json; this is an explicitly longer follow-up']}
        path=ROOT/'reports/charging-fifo-followup.json'
        path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps({'report':str(path),'passed':followup['passed'],'sim_time':followup['sim_time'],'completed_at':followup['completed_at'],'audits':followup['physical_step_audits'],'source_digest_sha256':followup['source_digest_sha256'],'source_unchanged_during_run':followup['source_unchanged_during_run'],'same_project_input':comparison['same_project_input'],'same_production_source':comparison['same_production_source']},ensure_ascii=False),flush=True)
        raise SystemExit(0)
    cases=[]
    for kind in ('amr','delivery'):
        for seed in (1,2):
            result=run_case(kind,seed)
            cases.append(result)
            print(json.dumps({key:result[key] for key in ('kind','seed','passed','sim_time','source_unchanged_during_run','max_energy_balance_error_j','final_battery_percent')},ensure_ascii=False),flush=True)
    queue=queue_case()
    insufficient=insufficient_energy_case()
    safety=[]
    for name in ('forged_enable','physical_loss_before_delayed_observation','facility_fault','communication_fault','operator_stop','invalid_control_timestamps','sensor_dropout','default_capacity'):
        result=safety_case(name);safety.append(result)
        print(json.dumps({'safety_case':name,'passed':result['passed'],'source_unchanged_during_run':result['source_unchanged_during_run']},ensure_ascii=False),flush=True)
    report={'process_source_sha256':PROCESS_SOURCE_SHA256,'cases':cases,'summary':summarize(cases),'safety_cases':safety,'insufficient_reserve_case':insufficient,'fifo_diagnostic':queue,'limitations':['4Wh is an explicit accelerated experiment setting; not hardware capacity','Nominal charge_until=40; a separate charge_until=30 case checks that insufficient post-clearance task reserve is explained without fabricating work success','Actual MuJoCo body/pad contacts and delayed robot observations; no hardware validation','Electrical interlock checked after every 2ms physical step; no large recordings exported','Each run source must match both the process-start hash and its end hash; results with false source_unchanged_during_run do not describe a verified frozen source revision','Two seeds per research model in a small open-floor scenario do not establish general fleet reliability']}
    report['source_consistent']=all(row['source_unchanged_during_run'] for row in [*cases,*safety,insufficient,queue])
    path=ROOT/'reports/charging-integration.json'
    path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'report':str(path),'nominal_passed':sum(r['passed'] for r in cases),'safety_passed':sum(r['passed'] for r in safety),'insufficient_reserve_check_passed':insufficient['passed'],'fifo_both_completed':queue['both_completed'],'fifo_completed_at':queue['completed_at'],'source_consistent':report['source_consistent']},ensure_ascii=False))
