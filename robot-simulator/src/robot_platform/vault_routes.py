"""Optional persistent account storage. Disabled unless explicitly configured."""
import hashlib
import hmac
import json
import os
from pathlib import Path
import re

from fastapi import HTTPException, Request
from pydantic import BaseModel, ConfigDict, Field
from .workspace_vault import WorkspaceVault, capture, validate_bundle


class SaveVault(BaseModel):
    model_config=ConfigDict(extra='forbid')
    id: str | None = None
    expected_revision: int = 0


class ShareVault(BaseModel):
    model_config=ConfigDict(extra='forbid')
    subject: str = Field(pattern=r"^[A-Za-z0-9_@.+-]{1,120}$")
    role: str


def install_vault_routes(app,host,root):
    database=os.environ.get('ROBOT_VAULT_DB')
    accounts=os.environ.get('ROBOT_VAULT_ACCOUNTS_FILE')
    vault=WorkspaceVault(database) if database and accounts else None

    def identity(request):
        if not vault:raise HTTPException(503,'영구 저장소와 계정 인증 설정이 필요합니다. 현재 세션 저장과 구분하세요.')
        authorization=request.headers.get('authorization','')
        if not authorization.startswith('Bearer ') or not 32<=len(authorization[7:])<=512:
            raise HTTPException(401,'계정 접근 토큰이 필요합니다')
        signature=hashlib.sha256(authorization[7:].encode()).hexdigest()
        try:registered=json.loads(Path(accounts).read_text())
        except (OSError,ValueError):raise HTTPException(503,'계정 인증 설정을 읽을 수 없습니다')
        for account in registered:
            if (isinstance(account.get('sha256'),str) and hmac.compare_digest(signature,account['sha256'])
                    and re.fullmatch(r'[A-Za-z0-9_@.+-]{1,120}',account.get('subject',''))):
                return account['subject']
        raise HTTPException(401,'유효하지 않은 계정 접근 토큰입니다')

    def allowed(call):
        try:return call()
        except PermissionError:raise HTTPException(403,'이 작업 공간에 요청한 권한이 없습니다')

    @app.get('/api/vault/status')
    def status():
        return dict(configured=bool(vault),mode='configured_volume' if vault else 'unconfigured',
                    note='외부 영구 볼륨과 계정 설정 필요. Vercel Sandbox 내부 파일은 영구 저장이 아닙니다.')

    @app.get('/api/vault')
    def listing(request:Request):
        subject=identity(request)
        return dict(subject=subject,spaces=vault.list(subject))

    @app.post('/api/vault')
    def save(request:Request,body:SaveVault):
        subject=identity(request)
        with host.lock:
            if host.plan_service:host.plan_service.checkpoint(force=True)
            bundle=capture(root,host.session)
            return allowed(lambda:vault.save(subject,bundle,body.id,body.expected_revision))

    @app.get('/api/vault/{key}')
    def read(key:str,request:Request,revision:int|None=None):
        subject=identity(request)
        return allowed(lambda:vault.read(subject,key,revision))

    @app.post('/api/vault/{key}/share')
    def share(key:str,request:Request,body:ShareVault):
        subject=identity(request)
        allowed(lambda:vault.grant(subject,key,body.subject,body.role))
        return dict(subject=body.subject,role=body.role)

    @app.post('/api/vault/{key}/restore')
    def restore(key:str,request:Request,revision:int|None=None):
        subject=identity(request)
        record=allowed(lambda:vault.read(subject,key,revision,execute=True))
        project,files,_=validate_bundle(record['bundle'])
        with host.lock:
            if host.session.status=='running':raise HTTPException(409,'현재 실행을 먼저 일시 정지하세요')
            if host.plan_service:host.plan_service.guard('project')
            # Preflight every path before any writes. Existing material is never overwritten.
            for name,data in files.items():
                path=Path(root)/name
                if not path.resolve().is_relative_to(Path(root).resolve()):raise ValueError('복원 경로 오류')
                if path.exists() and path.read_bytes()!=data:
                    raise HTTPException(409,'같은 식별자의 다른 자료가 현재 공간에 있습니다. 새 작업 공간에서 복원하세요')
            from .runtime import Session
            session=Session(project)
            for name,data in files.items():
                path=Path(root)/name;path.parent.mkdir(parents=True,exist_ok=True)
                if not path.exists():
                    temp=path.with_suffix(path.suffix+'.restoring');temp.write_bytes(data);temp.replace(path)
            recording=record['bundle']['recording']
            if isinstance(recording,dict) and re.fullmatch(r'[0-9a-f]{32}',str(recording.get('run_id',''))):
                path=Path(root)/'plans'/'recordings'/(recording['run_id']+'.json')
                path.parent.mkdir(parents=True,exist_ok=True)
                if not path.exists():path.write_text(json.dumps(recording,ensure_ascii=False,allow_nan=False))
            saved=host.store.save(project)
            # The new session starts from this saved revision. Do not return a
            # revision different from the one later sent to plan validation.
            session.project.revision=saved.revision
            session.world.project.revision=saved.revision
            session.orchestrator.project.revision=saved.revision
            host.session=session
            session.emit('workspace_restored',None,'저장 구성 복원 · 새 실행 일시 정지 · 이전 승인은 실행하지 않음',
                         dict(id=key,revision=record['revision'],source_sha=record['sha'],account=subject))
            if host.plan_service:host.plan_service.active=None
            return dict(project=saved,run_id=session.run_id,status='paused',source_revision=record['revision'])
