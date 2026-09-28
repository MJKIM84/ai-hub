"""Versioned scenario dialogue patches. Model text is never an executable action."""
from copy import deepcopy
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class Fact(BaseModel):
    model_config = ConfigDict(extra='forbid')
    label: str = Field(min_length=1, max_length=150)
    value: str = Field(max_length=2000)
    basis: Literal['user', 'project', 'proposed', 'unknown']
    references: list[str] = Field(default_factory=list, max_length=20)


class Choice(BaseModel):
    model_config = ConfigDict(extra='forbid')
    value: str = Field(min_length=1, max_length=1000)
    label: str = Field(min_length=1, max_length=200)
    reason: str = Field(min_length=1, max_length=500)


class Question(BaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str = Field(min_length=1, max_length=100)
    field: str = Field(min_length=1, max_length=100)
    prompt: str = Field(min_length=1, max_length=600)
    options: list[Choice] = Field(default_factory=list, max_length=6)


class ScenarioPatch(BaseModel):
    model_config = ConfigDict(extra='forbid')
    facts: dict[str, Fact] = Field(default_factory=dict, max_length=60)
    questions: list[Question] = Field(default_factory=list, max_length=30)
    resolved_question_ids: list[str] = Field(default_factory=list, max_length=30)
    remove_task_ids: list[str] = Field(default_factory=list, max_length=100)
    changes: list[str] = Field(default_factory=list, max_length=30)
    alternatives: list[str] = Field(default_factory=list, max_length=20)


def merge_selection(old, patch):
    result = deepcopy(old or {})
    for key, value in (patch or {}).items():
        result[key] = merge_selection(result.get(key, {}), value) if isinstance(value, dict) and isinstance(result.get(key, {}), dict) else deepcopy(value)
    return result


def answered_state(previous, answers):
    state = deepcopy((previous or {}).get('scenario') or {})
    questions = {q['id']: q for q in state.get('questions', [])}
    facts = state.setdefault('facts', {})
    if len(answers) > 4:
        raise ValueError('한 번에 최대 네 질문에 답할 수 있습니다')
    for key, value in answers.items():
        if key not in questions or not isinstance(value, str) or not value.strip() or len(value)>2000:
            raise ValueError('최신 질문에 대한 답변을 입력하세요')
        q = questions[key]
        facts[q['field']] = dict(label=q['prompt'], value=value.strip(), basis='user', references=[])
    state['questions'] = [q for q in questions.values() if q['id'] not in answers]
    state['answered_ids'] = sorted(set(state.get('answered_ids', [])) | set(answers))
    return state


def merge_dialogue(previous, proposal, state):
    """Stable task upserts; omission never deletes an already agreed step."""
    patch = ScenarioPatch.model_validate(proposal.get('scenario', {})).model_dump()
    facts = deepcopy(state.get('facts', {}))
    for key, value in patch['facts'].items():
        # Explicit choice controls outrank model paraphrases/defaults.
        if facts.get(key, {}).get('basis') == 'user' and value['basis'] != 'user':
            continue
        facts[key] = value
    answered = set(state.get('answered_ids', []))
    questions = {q['id']: q for q in state.get('questions', []) if q['id'] not in patch['resolved_question_ids']}
    for q in patch['questions']:
        if q['id'] not in answered:
            questions[q['id']] = q
    old = deepcopy(previous or {})
    tasks = {t.get('id') or t.get('existing_task_id') or f'intent-task-{i+1}': t for i,t in enumerate(old.get('tasks', []))}
    for key in patch['remove_task_ids']:
        if key not in tasks:
            raise ValueError('삭제할 기존 단계가 없습니다: '+key)
        del tasks[key]
    for index, task in enumerate(proposal.get('tasks', [])):
        key = task.get('id') or task.get('existing_task_id')
        if not key:
            raise ValueError('대화 시나리오의 단계에는 유지 가능한 id가 필요합니다')
        # Stable patch semantics also preserve per-step timeout, retry and
        # confirmation contracts when only the destination/order is changed.
        updated=deepcopy(tasks.get(key,{}))
        # Turning a preserved project reference into a revised executable
        # step must not leave the old reference alongside its new fields.
        if updated.get('existing_task_id') and task.get('kind') and not task.get('existing_task_id'):
            updated={}
        if task.get('destination_id') and task.get('destination_id')!=updated.get('destination_id'):
            for field in ('destination_xy','route_points'):updated.pop(field,None)
        updated.update(deepcopy(task))
        tasks[key] = updated
    old.update({k:v for k,v in proposal.items() if k not in ('tasks', 'scenario')})
    old['tasks'] = list(tasks.values())
    old['scenario'] = dict(facts=facts, questions=list(questions.values()), answered_ids=sorted(answered),
        changes=patch['changes'], alternatives=patch['alternatives'])
    return old


def blocking_questions(intent):
    state=intent.get('scenario') or {}
    return [q['prompt'] for q in state.get('questions', [])]+[fact['label']+': 미확정 조건을 확인하세요' for fact in state.get('facts',{}).values() if fact.get('basis')=='unknown']


INSTRUCTIONS = '''
When project.scenario_designer is present, design the scenario interactively instead of silently simplifying it.
Use the existing project, selection and scenario facts before asking. scenario_designer.static_execution_check is the actual compiler result for the current tasks. Do not manufacture missing-equipment clarifications from equipment=[] when the compiler validates a built-in arm gripper/body support. An authored_or_synthetic_environment uses geometry navigation; lack of an imported-floorplan graph is not itself a missing-input blocker. Let the compiler check routes. Physical contact/custody checks required during execution are not unanswered user questions. Name every new task in Korean using its action and place. Ask only 2–4 related decisive questions per turn (1 is OK when only one remains); put remaining unknowns in scenario.questions for later batches. Do not repeat answered fields. Questions include available choices, a reason for each and allow free text.
Return intent.scenario as a PATCH: {facts:{stableField:{label,value:string,basis:"user"|"project"|"proposed"|"unknown",references:string[]}},questions:[{id,field,prompt,options:[{value,label,reason}]}],resolved_question_ids:[],remove_task_ids:[],changes:[],alternatives:[]}.
Facts cover map choice, places, item count/mass/initial custody, loading/unloading actor, on-site action and observed completion, robots/equipment, people, ordering/concurrency, repetitions, deadlines and failure handling. Never invent missing items, reviewed doors or measurements. State proposed defaults explicitly and ask user to accept. Cite actual entity/document IDs for project facts.
In design mode intent.tasks is stable-ID upserts (or existing_task_id references); omitted steps are PRESERVED. Explicit deletion requires scenario.remove_task_ids. Preserve unrelated confirmed facts and constraints. Questions and unsupported actions remain blockers. A question about runtime has intent.kind=question; answer from project.scenario_designer.runtime, with sim_time/run_id, never inferred completion. It must not revise execution.
Use scenario facts from UI answers as authoritative user choices. UI selection is supplied in scenario_designer.selection. Model prose cannot replace them. If a place is absent, offer existing places, environment editing, floorplan import/review, or explicitly synthetic sample creation; do not claim creation by describing it.
Executable task additions: quantity integer 1..10, interval seconds 0..3600, retries integer 0..3; dependencies use predecessor_ids. Failure terminates dependents after bounded retries. Supported branch: condition:{task_id,outcome:"completed"|"failed"}, with that task_id in predecessor_ids; it uses terminal observed outcome AFTER bounded retries. A cancelled predecessor never activates failure branches. Other conditions and co-carry executors are unsupported and must remain clarifications. Branches are approved before execution; unchosen branches are skipped, never completed.
A patrol task can have confirmation:{label,actor:"human",criterion,timeout_s:1..3600} only when the user explicitly requires an actual external human check. It does not relocate items, load cargo, perform processing physics, or certify quality. Never insert confirmation as a substitute for autonomous loading, handoff, placement or reacquisition.
Item movement requires the contact-evidenced cooperation contract. A carrier may transport a supported item through an automatic elevator between an explicit loading source floor and the receiver's destination floor. Lift admission includes cargo mass and dimensions; physical support, slip, boarding and alighting remain execution gates. Initial loader, carrier and receiver are distinct robots; loader stays on the source floor, receiver on the destination floor. For a new cooperative task use actual source_id, item_id, workspace_id, carrier_destination_id and explicit loading_offset:[x,y] in carrier-local metres when needed. A workbench destination/source uses its real top surface (pose.z+size.z). Do not invent support height or grasp equipment.
After observed final placement, a dependent cooperative task may reacquire the same item using a loader within reach of that worktable, the carrier's preceding rendezvous pose and the exact preceding final placement as its source. The server verifies that lineage and reach. Give explicit predecessor_ids. No coordinate or custody mutation completes a step. Keep unsupported tasks as implementation gaps/clarifications; never silently replace loaded transport with empty patrol or change the requested required roles.
Never claim machine processing or loading based on a dwell timer. Each step names actor/place/action/capability/dependencies/completion/failure. Requests with unknown important conditions have intent.kind=plan plus questions/clarifications and cannot be approved. Show changed parts in scenario.changes.
'''
