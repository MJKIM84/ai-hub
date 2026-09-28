"""Atomic versioned local storage; input identifiers never become unchecked paths."""
from __future__ import annotations

import json
import re
import threading
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4
from .domain import Project


class Store:
    def __init__(self, root: Path):
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()

    def path(self, key: str) -> Path:
        if not re.fullmatch(r"[A-Za-z0-9_-]{1,120}", key):
            raise ValueError("잘못된 식별자")
        return self.root / key

    def save(self, project: Project) -> Project:
        with self._lock:
            folder = self.path(project.id)
            folder.mkdir(exist_ok=True)
            revisions = [int(p.stem) for p in folder.glob("*.json") if p.stem.isdigit()]
            saved = project.model_copy(deep=True)
            saved.revision = max(revisions, default=0) + 1
            target = folder / f"{saved.revision}.json"
            temporary = folder / f"{uuid4().hex}.tmp"
            temporary.write_text(saved.model_dump_json(indent=2), encoding="utf-8")
            temporary.replace(target)
            metadata = folder / f"{saved.revision}.meta.json"
            metadata.write_text(json.dumps({"saved_at": datetime.now(timezone.utc).isoformat(), "source": "앱 저장"}, ensure_ascii=False), encoding="utf-8")
            return saved

    def load(self, key: str, revision: int | None = None) -> Project:
        with self._lock:
            folder = self.path(key)
            if revision is None:
                revision = max((int(p.stem) for p in folder.glob("*.json") if p.stem.isdigit()), default=0)
            if revision < 1:
                raise FileNotFoundError(key)
            return Project.model_validate_json((folder / f"{revision}.json").read_text(encoding="utf-8"))

    def list(self) -> list[dict]:
        rows = []
        for folder in sorted(self.root.iterdir()):
            if folder.is_dir():
                try:
                    project = self.load(folder.name)
                    versions=self.versions(project.id)
                    rows.append({"id":project.id,"name":project.name,"revision":project.revision,
                                 "version_count":len(versions),"versions":versions,
                                 "updated_at":(folder/f"{project.revision}.json").stat().st_mtime})
                except (ValueError,FileNotFoundError):
                    continue
        return sorted(rows,key=lambda row:row['updated_at'],reverse=True)

    def versions(self, key: str) -> list[dict]:
        folder = self.path(key)
        if not folder.exists():
            raise FileNotFoundError(key)
        rows = []
        for path in sorted(folder.glob("*.json"), key=lambda file: int(file.stem) if file.stem.isdigit() else -1, reverse=True):
            if not path.stem.isdigit():
                continue
            project = Project.model_validate_json(path.read_text(encoding="utf-8"))
            metadata_path = folder / f"{path.stem}.meta.json"
            metadata = json.loads(metadata_path.read_text(encoding="utf-8")) if metadata_path.exists() else {}
            rows.append({"revision": project.revision, "name": project.name,
                         "floor_count": len(project.environment.floors), "robot_count": len(project.robots),
                         "person_count":len(project.people),"task_count":len(project.tasks),
                         "seed":project.physics.seed,"policy_name":project.policy.name,
                         "auto_stop_after_seconds":project.auto_stop_after_seconds,
                         "map_name": project.environment.name, "map_version": project.environment.version,
                         "saved_at": metadata.get("saved_at"), "source": metadata.get("source", "이전 저장"),
                         "original_revision": metadata.get("original_revision"),
                         "source_file": metadata.get("source_file")})
        return rows

    def clone(self, key: str) -> Project:
        project = self.load(key).model_copy(deep=True)
        project.id = uuid4().hex[:12]
        project.name += " · 복제"
        # A reviewed floorplan's environment ID is its source pointer. Giving
        # a clone an unrelated ID silently discards source review at planning
        # time while leaving the old topology embedded in the project.
        if not project.environment.id.startswith('floorplan-'):
            project.environment.id = uuid4().hex[:12]
        return self.save(project)
