"""Local application API. Physical state is serialized behind a single run lock."""
from __future__ import annotations
from contextlib import asynccontextmanager
import json
import math
import re
from pathlib import Path
import threading
import time
from urllib.parse import parse_qs, quote

from fastapi import FastAPI,HTTPException,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.responses import Response,FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel,Field

from .catalog import models
from .domain import Project,Pose,Policy,FaultInjection
from .experiments import compare,to_csv
from .runtime import Session
from .storage import Store
from .templates import example,TEMPLATES


JSON_EXPORT_MAX_BYTES = 64 * 1024 * 1024


def _export_json_number(value):
    number = float(value)
    if not math.isfinite(number):
        raise ValueError("JSON 숫자는 유한해야 합니다")
    return number


def _reject_json_constant(value):
    raise ValueError(f"JSON에서 지원하지 않는 값: {value}")


def _export_json_filename(value):
    # Never interpolate user input into the quoted ASCII fallback header.
    name = ''.join(c for c in value if ord(c) >= 32 and ord(c) != 127
                   and c not in '<>:"/\\|?*').strip(' .')[:160]
    if not name:
        name = 'export.json'
    if not name.lower().endswith('.json'):
        name += '.json'
    return name


class Control(BaseModel):
    action: str
    steps: int = Field(default=1,ge=1,le=10000)
    speed: float | None = Field(default=None,gt=0,le=20)


class CommandRequest(BaseModel):
    kind: str
    target: Pose | None = None


class SaveRequest(BaseModel):
    project: Project
    label: str | None = None


class ExperimentRequest(BaseModel):
    project: Project
    seeds: list[int] = Field(default_factory=lambda:[42],min_length=1,max_length=50)
    duration: float = Field(default=10,gt=0,le=3600)
    policies: list[Policy] = Field(default_factory=lambda:[Policy()],min_length=1,max_length=20)


class RecoveryRequest(BaseModel):
    model_config={'extra':'forbid','allow_inf_nan':False}
    request_id: str = Field(min_length=1,pattern=r'\S')
    actor_id: str = Field(min_length=1,pattern=r'\S')
    destination: Pose | None = None
    retry: bool = Field(default=False,strict=True)
    timeout: float = Field(default=90,gt=0,le=300,strict=True)


class RecoveryCancelRequest(BaseModel):
    model_config={'extra':'forbid'}
    recovery_id: str = Field(min_length=1,pattern=r'\S')


class EngineHost:
    def __init__(self,data_dir, *, initial_template="hotel"):
        self.lock=threading.RLock()
        self.session=Session(example(initial_template))
        self.store=Store(data_dir/"projects")
        self.experiment_dir=data_dir/"experiments";self.experiment_dir.mkdir(parents=True,exist_ok=True)
        self.plan_service=None
        self.stop=threading.Event()
        self.thread=threading.Thread(target=self.run,daemon=True,name="physics-worker")

    def run(self):
        last=time.monotonic();accumulator=0.
        while not self.stop.wait(.001):
            now=time.monotonic();elapsed=min(.1,now-last);last=now
            with self.lock:
                s=self.session
                if s.status!="running":accumulator=0.;continue
                accumulator+=elapsed*s.speed
                # Yield the state lock frequently; a catch-up batch must not freeze
                # state reads and controls for half a simulated second.
                steps=min(max(1,int(.02/s.project.physics.timestep)),int(accumulator/s.project.physics.timestep))
                if steps:
                    try:s.step(steps)
                    except Exception as error:
                        s.status="failed";s.emit("simulation_failed",None,str(error),{})
                    accumulator-=steps*s.project.physics.timestep
                    if self.plan_service:self.plan_service.checkpoint(force=s.status!='running')


def create_app(data_dir:Path|None=None, *, provider_factory=None, initial_template="hotel"):
    root=Path(__file__).resolve().parents[2]
    host=EngineHost(data_dir or root/"data", initial_template=initial_template)

    @asynccontextmanager
    async def lifespan(app):
        host.thread.start()
        yield
        host.stop.set();host.thread.join(timeout=5)
        if host.plan_service:host.plan_service.provider.close()

    app=FastAPI(title="공간 · 로봇 물리 실험실",version="0.1.0",lifespan=lifespan)
    app.state.host=host
    app.add_middleware(CORS,allow_origins=["http://localhost:5173","http://127.0.0.1:5173"],allow_methods=["*"],allow_headers=["*"])

    @app.exception_handler(RequestValidationError)
    async def validation_error(request, error):
        # Validation errors normally echo invalid inputs; credentials must never be reflected.
        if request.url.path == '/api/assistant/settings':
            from fastapi.responses import JSONResponse
            return JSONResponse(status_code=422, content={'detail':'연결 설정 형식을 확인하세요.'})
        return await request_validation_exception_handler(request, error)

    @app.exception_handler(ValueError)
    async def value_error(request,error):
        from fastapi.responses import JSONResponse
        return JSONResponse(status_code=422,content={"detail":str(error)})

    @app.get("/api/session")
    def visitor_session():return {"mode":"local"}

    @app.get("/api/health")
    def health():return {"status":"ok","physics":"MuJoCo","hardware_validation":False}

    @app.head("/api/exports/json")
    def json_export_available():
        # Lets the UI keep its local Blob fallback when this server is offline
        # or an older server does not support native form downloads.
        return Response(status_code=204,headers={
            "X-JSON-Export":"form-post-v1","Cache-Control":"no-store"})

    @app.get("/api/exports/json")
    def json_export_get_rejected():
        raise HTTPException(405,"JSON 문서는 URL 대신 POST 본문으로 보내세요",
                            headers={"Allow":"HEAD, POST"})

    @app.post("/api/exports/json")
    async def json_export(request:Request):
        """Echo a validated JSON document as an attachment, without persistence.

        Native form POST keeps the document out of URLs and download handling
        in the browser. This route does not inspect or mutate EngineHost.
        """
        if request.headers.get("content-type", "").split(';',1)[0].strip().lower() != "application/x-www-form-urlencoded":
            raise HTTPException(415,"JSON 내보내기는 form POST만 지원합니다")
        body = bytearray()
        async for chunk in request.stream():
            if len(body) + len(chunk) > JSON_EXPORT_MAX_BYTES:
                raise HTTPException(413,"JSON 내보내기 요청이 너무 큽니다")
            body.extend(chunk)
        try:
            fields = parse_qs(body.decode('utf-8'),keep_blank_values=True,
                              strict_parsing=True,errors='strict',max_num_fields=2)
            if set(fields) != {'name','payload'} or any(len(v) != 1 for v in fields.values()):
                raise ValueError("name과 payload를 각각 한 번 지정하세요")
            payload = fields['payload'][0]
            json.loads(payload,parse_constant=_reject_json_constant,
                       parse_float=_export_json_number)
        except (ValueError, UnicodeError, RecursionError):
            raise HTTPException(422,"내보낼 JSON 또는 form 필드가 올바르지 않습니다")
        name = _export_json_filename(fields['name'][0])
        return Response(payload,media_type="application/json",headers={
            "Content-Disposition":f"attachment; filename=\"export.json\"; filename*=UTF-8''{quote(name,safe='')}",
            "Cache-Control":"no-store","X-Content-Type-Options":"nosniff"})

    @app.get("/api/catalog")
    def catalog():return dict(models=models(),templates=TEMPLATES,
                              documentation_models=host.plan_service.ontology.documentation_models())

    @app.get("/api/templates/{template_id}")
    def template(template_id:str):return example(template_id)

    @app.get("/api/project")
    def get_project():
        with host.lock:return host.session.project.model_copy(deep=True)

    @app.put("/api/project")
    def set_project(project:Project):
        with host.lock:
            if host.session.status=="running":raise HTTPException(409,"실행을 일시 정지한 뒤 환경을 적용하세요")
            if host.plan_service:host.plan_service.guard("project_change")
            candidate=Session(project)
            host.session=candidate
            if host.plan_service:host.plan_service.amendment_required=False
            return candidate.project

    @app.get("/api/state")
    def state():
        with host.lock:return host.session.snapshot()

    @app.get("/api/scene")
    def scene():
        with host.lock:return dict(run_id=host.session.run_id,meshes=host.session.world.meshes())

    @app.post("/api/control")
    def control(request:Control):
        with host.lock:
            s=host.session
            if request.action in ("start","resume","step") and host.plan_service and host.plan_service.stopped_run_id==s.run_id:raise HTTPException(409,"중단한 계획은 재개할 수 없습니다. 새 계획을 승인하거나 새 실행을 구성하세요.")
            if request.action=="reset" and host.plan_service:host.plan_service.guard("reset")
            if request.speed is not None:s.speed=request.speed
            if request.action in ("start","resume"):
                if host.plan_service and host.plan_service.amendment_required:raise HTTPException(409,"변경안을 다시 승인한 뒤 재개하세요.")
                if s.status in ("failed","completed","timed_out"):
                    raise HTTPException(409,"종료된 실행입니다. 초기화한 뒤 다시 시작하세요")
                s.status="running"
            elif request.action=="pause":
                if s.status not in ("failed","completed","timed_out"):s.status="paused"
            elif request.action=="reset":
                host.session=Session(s.project,stop_when_tasks_terminal=s.stop_when_tasks_terminal)
                if host.plan_service:host.plan_service.amendment_required=False
            elif request.action=="step":
                if host.plan_service and host.plan_service.amendment_required:raise HTTPException(409,"변경안을 다시 승인한 뒤 진행하세요.")
                if s.status in ("failed","completed","timed_out"):raise HTTPException(409,"종료된 실행입니다. 초기화한 뒤 진행하세요")
                if s.status=="running":raise HTTPException(409,"단계 실행 전에 일시 정지하세요")
                s.step(request.steps)
            else:raise HTTPException(422,"알 수 없는 실행 명령")
            return host.session.snapshot()

    @app.post("/api/robots/{robot_id}/command")
    def command(robot_id:str,request:CommandRequest):
        with host.lock:
            if request.kind not in ("stop","estop") and host.plan_service:host.plan_service.guard("robot_command")
            return host.session.command(robot_id,request.kind,request.target.model_dump() if request.target else None)

    @app.get("/api/commands/{command_id}")
    def command_feedback(command_id:str):
        with host.lock:
            try:return host.session.command_feedback(command_id)
            except KeyError:raise HTTPException(404,"없는 명령")

    @app.post("/api/robots/{robot_id}/resume")
    def resume_robot(robot_id:str):
        with host.lock:return host.session.resume_robot(robot_id)

    @app.post("/api/tasks/{task_id}/cancel")
    def cancel(task_id:str):
        with host.lock:
            if host.plan_service:host.plan_service.guard("task_cancel")
            if task_id not in host.session.orchestrator.tasks:raise HTTPException(404,"없는 작업")
            host.session.orchestrator.cancel(task_id,host.session.time)
            return host.session.orchestrator.task_rows()

    @app.post("/api/faults")
    def fault(request:FaultInjection):
        with host.lock:
            if host.plan_service:host.plan_service.guard("fault_configuration")
            host.session.inject(request)
            return {"status":"scheduled"}

    @app.post('/api/tasks/{task_id}/recovery')
    def recover_cooperation(task_id:str,request:RecoveryRequest):
        with host.lock:
            if request.destination is not None and host.plan_service:host.plan_service.guard("recovery_destination")
            return host.session.recover_cooperation(task_id,request.actor_id,
                request.destination.model_dump() if request.destination else None,
                request_id=request.request_id,retry=request.retry,timeout=request.timeout)

    @app.post('/api/tasks/{task_id}/recovery/cancel')
    def cancel_recovery(task_id:str,request:RecoveryCancelRequest):
        with host.lock:return host.session.cancel_cooperation_recovery(task_id,request.recovery_id)

    @app.post("/api/facilities/{facility_id}/target")
    def facility(facility_id:str,target:Pose):
        with host.lock:
            if host.plan_service:host.plan_service.guard("facility_target")
            state=host.session.facility_states.get(facility_id)
            if not state or state["kind"]!="elevator":raise HTTPException(404,"없는 승강기")
            receipt=host.session.facility_target(facility_id,target.z)
            return dict(state,request=receipt)

    @app.get("/api/projects")
    def projects():return host.store.list()

    @app.get("/api/projects/{project_id}/versions")
    def project_versions(project_id:str):
        try:return host.store.versions(project_id)
        except FileNotFoundError:raise HTTPException(404,"저장된 프로젝트 없음")

    @app.post("/api/projects/save")
    def save(request:SaveRequest):return host.store.save(request.project)

    @app.get("/api/projects/{project_id}/versions/{revision}")
    def load(project_id:str,revision:int):
        try:return host.store.load(project_id,revision)
        except FileNotFoundError:raise HTTPException(404,"저장된 버전 없음")

    @app.post("/api/projects/{project_id}/clone")
    def clone(project_id:str):
        try:return host.store.clone(project_id)
        except FileNotFoundError:raise HTTPException(404,"저장된 프로젝트 없음")

    @app.get("/api/recording")
    def recording():
        with host.lock:return host.session.recording()

    @app.get("/api/experiments")
    def experiments():
        return [json.loads(p.read_text()) for p in sorted(host.experiment_dir.glob("*/summary.json"),key=lambda x:x.stat().st_mtime,reverse=True)]

    @app.get("/api/experiments/{experiment_id}/runs/{run_id}/project")
    def experiment_project(experiment_id:str,run_id:str):
        if not re.fullmatch(r"[A-Za-z0-9_-]{1,120}",run_id):
            raise HTTPException(422,"잘못된 실행 식별자")
        folder=Store(host.experiment_dir).path(experiment_id)
        try: record=json.loads((folder/f"run-{run_id}.json").read_text(encoding="utf-8"))
        except FileNotFoundError: raise HTTPException(404,"저장된 실험 실행 없음")
        return Project.model_validate(record['manifest']['project'])

    @app.post("/api/experiments")
    def experiment(request:ExperimentRequest):
        return compare(request.project,request.seeds,request.policies,request.duration,host.experiment_dir)

    @app.get("/api/experiments/{experiment_id}/export")
    def export(experiment_id:str,format:str="json"):
        folder=Store(host.experiment_dir).path(experiment_id)
        try:result=json.loads((folder/"summary.json").read_text())
        except FileNotFoundError:raise HTTPException(404,"실험 없음")
        if format=="csv":return Response(to_csv(result),media_type="text/csv",headers={"Content-Disposition":f'attachment; filename="{experiment_id}.csv"'})
        if format!="json":raise HTTPException(422,"지원 형식은 json 또는 csv")
        return result

    from .plan_service import install_plan_routes
    install_plan_routes(app,host,(data_dir or root/"data")/"plans", provider_factory=provider_factory)

    dist=root/"web/dist"
    if dist.exists():
        if (dist/"assets").exists():app.mount("/assets",StaticFiles(directory=dist/"assets"),name="assets")
        if (dist/"materials").exists():app.mount("/materials",StaticFiles(directory=dist/"materials"),name="materials")

        @app.get("/{path:path}")
        def index(path:str):return FileResponse(dist/"index.html")
    return app


CORS=CORSMiddleware
