"""Versioned workspace storage on an operator-provided persistent volume.

Account identities come from server-provisioned hashed access tokens. This is
not Vercel Sandbox persistence: the DB must live on a durable shared service.
Never archives provider settings or credentials. Restores are review-only.
"""
import base64
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import time
from uuid import uuid4

from .domain import Project

MAX_BYTES=64*1024*1024


def permitted(name):
    parts=Path(name).parts
    if not parts or Path(name).is_absolute() or any(p in ('.','..') for p in parts):return False
    if '\\' in name:return False
    if parts[0]=='projects':
        return len(parts)==3 and bool(re.fullmatch(r'[A-Za-z0-9_-]+',parts[1])) and bool(re.fullmatch(r'\d+(\.meta)?\.json',parts[2]))
    if parts[0]!='plans':return False
    if len(parts)==2:return bool(re.fullmatch(r'[0-9a-f]{32}\.json',parts[1]))
    if parts[1] in ('ontology','floorplans'):
        return len(parts)<=5 and all(re.fullmatch(r'[A-Za-z0-9_.-]+',p) for p in parts[2:]) and Path(name).suffix in ('.json','.pdf','.png','.jpg','.jpeg')
    if parts[1] in ('history','recordings','revisions'):
        return len(parts)<=4 and all(re.fullmatch(r'[A-Za-z0-9_.-]+',p) for p in parts[2:]) and Path(name).suffix=='.json'
    return False


def capture(root,session):
    files={};total=0
    for path in sorted(Path(root).rglob('*')):
        name=path.relative_to(root).as_posix()
        if path.is_symlink() or not path.is_file() or not permitted(name):continue
        if not path.resolve().is_relative_to(Path(root).resolve()):raise ValueError('작업 공간 밖의 파일은 보관하지 않습니다')
        total+=path.stat().st_size
        if total>MAX_BYTES:raise ValueError('보관 자료가 64MB를 넘습니다. 실행 기록을 분리하세요')
        files[name]=base64.b64encode(path.read_bytes()).decode()
    return dict(format='robot-workspace-v1',project=session.project.model_dump(),files=files,
                recording=session.recording(),semantics='historical record; restore never executes approvals or resumes physics')


def validate_bundle(bundle):
    if not isinstance(bundle,dict) or set(bundle)!={'format','project','files','recording','semantics'}:
        raise ValueError('작업 공간 보관 형식 오류')
    if bundle['format']!='robot-workspace-v1':raise ValueError('지원하지 않는 보관 버전')
    project=Project.model_validate(bundle['project'])
    raw=json.dumps(bundle,ensure_ascii=False,allow_nan=False)
    if len(raw.encode())>MAX_BYTES:raise ValueError('보관 자료가 64MB를 넘습니다')
    files={}
    for name,data in bundle['files'].items():
        if not permitted(name):raise ValueError('보관할 수 없는 파일 경로')
        files[name]=base64.b64decode(data,validate=True)
    return project,files,raw


class WorkspaceVault:
    def __init__(self,path):
        self.path=Path(path);self.path.parent.mkdir(parents=True,exist_ok=True)
        with self.connect() as db:
            db.executescript('''
                CREATE TABLE IF NOT EXISTS spaces(id TEXT PRIMARY KEY,owner TEXT NOT NULL,title TEXT NOT NULL,revision INTEGER NOT NULL);
                CREATE TABLE IF NOT EXISTS grants(space TEXT,subject TEXT,role TEXT,PRIMARY KEY(space,subject));
                CREATE TABLE IF NOT EXISTS versions(space TEXT,revision INTEGER,payload TEXT,sha TEXT,saved_at REAL,PRIMARY KEY(space,revision));
            ''')

    def connect(self):
        db=sqlite3.connect(self.path,timeout=10);db.row_factory=sqlite3.Row;return db

    def role(self,db,subject,key):
        row=db.execute('SELECT owner FROM spaces WHERE id=?',(key,)).fetchone()
        if row and row['owner']==subject:return 'owner'
        row=db.execute('SELECT role FROM grants WHERE space=? AND subject=?',(key,subject)).fetchone()
        return row['role'] if row else None

    def list(self,subject):
        with self.connect() as db:
            return [dict(row,role=self.role(db,subject,row['id'])) for row in db.execute('SELECT * FROM spaces') if self.role(db,subject,row['id'])]

    def save(self,subject,bundle,key=None,expected=0):
        project,_,payload=validate_bundle(bundle)
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            if key:
                if self.role(db,subject,key) not in ('owner','editor'):raise PermissionError('편집 권한이 없습니다')
                current=db.execute('SELECT revision FROM spaces WHERE id=?',(key,)).fetchone()['revision']
                if current!=expected:raise ValueError('다른 저장이 먼저 반영됐습니다. 최신 버전을 다시 확인하세요')
                revision=current+1
                db.execute('UPDATE spaces SET revision=?,title=? WHERE id=?',(revision,project.name,key))
            else:
                key=uuid4().hex;revision=1
                db.execute('INSERT INTO spaces VALUES(?,?,?,?)',(key,subject,project.name,revision))
            db.execute('INSERT INTO versions VALUES(?,?,?,?,?)',(key,revision,payload,hashlib.sha256(payload.encode()).hexdigest(),time.time()))
            return dict(id=key,revision=revision)

    def read(self,subject,key,revision=None,*,execute=False):
        with self.connect() as db:
            role=self.role(db,subject,key)
            if not role or (execute and role not in ('owner','editor','operator')):raise PermissionError('요청한 작업의 권한이 없습니다')
            if revision is None:
                revision=db.execute('SELECT revision FROM spaces WHERE id=?',(key,)).fetchone()['revision']
            row=db.execute('SELECT * FROM versions WHERE space=? AND revision=?',(key,revision)).fetchone()
            if not row:raise ValueError('저장 버전이 없습니다')
            return dict(id=key,revision=revision,role=role,sha=row['sha'],bundle=json.loads(row['payload']))

    def grant(self,subject,key,other,role):
        if role not in ('reader','editor','operator'):raise ValueError('읽기·편집·실행 역할을 선택하세요')
        with self.connect() as db:
            if self.role(db,subject,key)!='owner':raise PermissionError('소유자만 공유 권한을 변경할 수 있습니다')
            db.execute('INSERT OR REPLACE INTO grants VALUES(?,?,?)',(key,other,role))
