"""Run-local incident scheduling. Only observed terminal states/events trigger actions.

Clocks are simulation seconds. Pausing freezes deadlines; snapshots never trigger
an action. A fresh Session is an explicit new run, not a continuation of a log.
"""
from copy import deepcopy


class IncidentScheduler:
    def __init__(self):
        self.states = {}
        self.owners = {}
        self.releases = []

    def tick(self, now, faults, tasks, events, active_faults=None):
        actions = []
        effective=dict(active_faults or {})
        for release in list(self.releases):
            if now + 1e-9 < release['until']:
                continue
            self.releases.remove(release)
            # A newer/manual fault owns this target. Never clear it by an old timer.
            if self.owners.get(release['target']) != release['owner']:
                continue
            actions.append((release['fault'].model_copy(update={'kind': 'recover'}),
                            dict(index=release['owner'][0], phase='released', automatic=True)))
            self.owners.pop(release['target'], None)
            effective[release['target']]='none'
            self.states[release['owner'][0]]['phase'] = 'released'
        for index, fault in enumerate(faults):
            state = self.states.setdefault(index, dict(index=index, phase='armed', count=0,
                                                      last_event_seq=0, triggered_at=None))
            if state['count'] >= fault.max_occurrences or now < fault.time:
                continue
            trigger = fault.trigger
            evidence = None
            if trigger is None:
                evidence = dict(simulation_time=now)
            elif trigger.kind == 'task_status':
                task = tasks.get(trigger.task_id)
                if task and task['status'] == trigger.status:
                    evidence = dict(task_id=trigger.task_id, status=task['status'],
                                    completed_at=task.get('completed_at'))
            else:
                for event in events[state['last_event_seq']:] :
                    if event['seq'] <= state['last_event_seq']:
                        continue
                    state['last_event_seq'] = event['seq']
                    if (event['time'] >= fault.time and event['kind'] == trigger.event_kind
                            and (not trigger.entity_id or event['entity_id'] == trigger.entity_id)
                            and (not trigger.task_id or event.get('details', {}).get('task_id') == trigger.task_id)):
                        evidence = dict(event_seq=event['seq'], event_kind=event['kind'],
                                        observed_at=event['time'])
                        break
            if evidence is None:
                continue
            state.update(phase='active', count=state['count']+1, triggered_at=now, evidence=evidence)
            # Evaluate in action order, including faults already scheduled in
            # this tick. A rejected overlap never steals another timer's owner.
            if fault.auto_recover and effective.get(fault.target_id,'none')!='none':
                state['phase']='blocked'
                actions.append((fault,dict(index=index,phase='blocked',occurrence=state['count'],evidence=evidence)))
                continue
            owner = (index, state['count'])
            self.owners[fault.target_id] = owner
            if fault.kind!='push':effective[fault.target_id]='none' if fault.kind=='recover' else fault.kind
            if fault.auto_recover:
                self.releases.append(dict(target=fault.target_id, owner=owner,
                                          until=now+fault.duration, fault=fault))
                state['release_at'] = now+fault.duration
            actions.append((fault, dict(index=index, phase='triggered', occurrence=state['count'],
                                       evidence=evidence, release_at=state.get('release_at'))))
        return actions

    def snapshot(self, faults):
        return [dict(configuration=fault.model_dump(), **deepcopy(self.states.get(i,
                dict(index=i, phase='armed', count=0, triggered_at=None)))) for i, fault in enumerate(faults)]
