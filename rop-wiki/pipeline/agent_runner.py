#!/usr/bin/env python3
"""에이전트 실행기: claude -p 를 헤드리스로 호출해 리서치·검증·스토리텔러 에이전트를 실행한다.

프롬프트(에이전트 실행 규약) = agents/shared-rules.md 전문 + agents/<role>.md 전문 + "## 실행 컨텍스트"
  + "## 입력"(입력 파일마다 "### <파일 경로>" 소제목과 코드 펜스 본문) + 추가 절("## 반려 사유", "## 수정 지시")
을 이어 붙인 하나의 텍스트(stdin). runs/<run_id>/prompts/<step>.md 에 저장한 뒤 실행한다.

CLI 호출(실험으로 확인한 형식):
  claude -p --output-format json --json-schema <스키마> --tools <도구> --allowedTools <도구> --max-turns N
         --permission-mode dontAsk --no-session-persistence [--model M]
  - 응답은 JSON 봉투이며 구조화 출력은 `structured_output`(dict)에, 같은 내용이 `result`(JSON 문자열)에 온다.
    `is_error: true` 면 `result` 가 오류 문구다(예: API Error 400).
  - --json-schema 는 CLI(Ajv strict)와 API 의 제약이 있어 lib.runs.cli_schema() 로 바꿔 넘긴다
    ($schema/$id/$defs 제거, 하위 스키마 type 보충, 최상위 allOf/oneOf/anyOf 제거). 조건 규칙은 스크립트가 원본 스키마로 검사한다.
  - 위험 플래그(--dangerously-skip-permissions)는 쓰지 않는다. --permission-mode dontAsk 로 프롬프트 없이 실행됨을 확인했다.

사용:
  python3 pipeline/agent_runner.py probe [--out runs/<id>/probe.json] [--skip-search] [--skip-fetch]
      → {"web_search_available": bool (--skip-search 면 null), "web_fetch_available": bool, …}
      web_search_available 은 `claude -p --tools WebSearch`, web_fetch_available 은 `claude -p --tools WebFetch` 로
      실제 도구를 써 본 결과다(셸 curl 결과는 details.web_fetch_curl 참고값).
  python3 pipeline/agent_runner.py run --role researcher|verifier|storyteller --run-id <id>
         [--stage first|second] [--retry N] [--dry-run]
      → runs/<id>/research.json(+.md) | verification.json | verification2.json | pages.json + pages/
  파이썬에서: run_agent(role, context, inputs, schema_path, out_dir, settings, extra_sections={})
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import frontmatter as fm  # noqa: E402
from lib import paths, runs  # noqa: E402
from lib.source import load_source  # noqa: E402
import render_run_md  # noqa: E402

ROOT = paths.ROOT
ROLE_FILES = {"researcher": "researcher.md", "verifier": "verifier.md", "storyteller": "storyteller.md"}
ROLE_KIND = {"researcher": "research", "verifier": "verification", "storyteller": "pages"}
ROLE_KO = {"researcher": "리서치 에이전트", "verifier": "내용 검증 에이전트", "storyteller": "스토리텔러 에이전트"}
TEXT_EXTS = {".md", ".txt", ".csv", ".json", ".yaml", ".yml"}
EXPERIMENT_FILE_CAP = 60_000     # 실험 파일 하나의 최대 글자 수 [가정]
EXPERIMENT_TOTAL_CAP = 200_000   # 실험 입력 전체의 최대 글자 수 [가정]
STAGE_ARTIFACT_PAGES = {1: ["model-standard-comparison.md"], 2: ["document-type-matrix.md"], 3: ["experiments.md"],
                        5: ["evaluation-and-verification.md", "experiments.md"], 7: ["experiments.md"]}
TEMPLATES_BY_RUN_TYPE = {
    "area_deep_dive": ["area.md", "category.md"],
    "topic": ["topic.md"],
    "update": ["area.md", "topic.md"],
    "monthly_recheck": ["area.md", "topic.md", "reference.md"],
    "weekly_review": [],
    "track": ["track-stage.md", "track-overview.md", "topic.md"],   # 트랙 초안 문서 템플릿은 트랙 설정(draft_template)에서 더한다
    "category_link": ["category.md"],
}
# 페이지 프런트매터 type → 템플릿 파일(2차 검증의 "템플릿 섹션 순서 준수" 검사용 기준 템플릿). track 은 subtype 으로 나뉜다.
# type log 는 일일 로그(daily-log.md)가 기준이지만 주간 정리 페이지(docs/logs/weekly/, tags weekly_review)도 type log 이므로
# 그 페이지는 daily-log.md 대신 _weekly_section_spec() 의 절 구성을 기준으로 준다(6.3 절차 8, storyteller.md 6절).
TEMPLATE_BY_PAGE_TYPE = {
    "home": "home.md", "about": "about.md", "category": "category.md", "area": "area.md", "topic": "topic.md",
    "glossary": "glossary.md", "reference": "reference.md", "log": "daily-log.md", "track": "track-overview.md",
    "track-stage": "track-stage.md", "ontology-draft": "ontology-draft.md", "track-log": "track-log.md",
}
WEEKLY_TEMPLATE = "templates/weekly-log.md"   # 템플릿 담당이 만들면 그것을 주간 정리의 기준 템플릿으로 쓴다(없으면 storyteller.md 6절) [가정]
WEEKLY_CHECK_FILES = (   # 주간 정리에서 run_daily.sh 가 리서치 전에 남기는 링크·출처 유효성 점검 결과(7.1) — 리서치·검증·스토리텔러 입력
    ("url_check.json", "참고문헌 URL 열림 확인 결과, pipeline/checks/check_urls.py"),
    ("link_check.txt", "내부 링크·각주 검사 결과, pipeline/checks/check_links.py"),
)


def _is_weekly_page(rel: str, meta: dict) -> bool:
    """주간 정리 페이지인가: docs/logs/weekly/ 아래이거나 tags 에 weekly_review 가 있다(storyteller.md 4.1·6절)."""
    tags = [str(x) for x in (meta.get("tags") or [])]
    return rel.startswith("logs/weekly/") or "weekly_review" in tags


def _weekly_section_spec() -> tuple[str, str] | None:
    """주간 정리 페이지의 기준 절 구성. templates/weekly-log.md 가 있으면 그 파일, 없으면 agents/storyteller.md 6절의
    '**weekly_review(주간 정리)**' 단락(절 목록 1~7)을 떼어 준다. 둘 다 없으면 None."""
    item = _label_text(WEEKLY_TEMPLATE)
    if item:
        return item
    text = runs.read_text(runs.AGENTS_DIR / "storyteller.md")
    m = re.search(r"^\*\*weekly_review\(주간 정리\)\*\*.*?(?=\n[ \t]*\n|\Z)", text, re.S | re.M)
    if not m:
        return None
    return ("agents/storyteller.md (6절 — 주간 정리 페이지의 절 구성; templates/weekly-log.md 가 없어 기준 템플릿 대용)", m.group(0).strip())


class AgentError(RuntimeError):
    """에이전트 호출 실패(CLI 오류, 시간 초과, 스키마 불일치 재실행 후에도 실패)."""


# --- 프롬프트 조립 ---------------------------------------------------------------------

def _fence_for(text: str) -> str:
    longest = max((len(m.group(0)) for m in re.finditer(r"`{3,}", text)), default=0)
    return "`" * max(3, longest + 1)


def _lang_for(label: str) -> str:
    ext = Path(label.split(" ")[0]).suffix.lower()
    return {".md": "markdown", ".json": "json", ".yaml": "yaml", ".yml": "yaml", ".txt": "text", ".csv": "csv"}.get(ext, "text")


def render_context(context: dict) -> str:
    lines = ["## 실행 컨텍스트", ""]
    for k, v in context.items():
        if isinstance(v, dict):
            lines.append(f"- {k}:")
            for kk, vv in v.items():
                lines.append(f"    - {kk}: {vv}")
        elif isinstance(v, (list, tuple)):
            lines.append(f"- {k}: {', '.join(str(x) for x in v) if v else '없음'}")
        else:
            lines.append(f"- {k}: {v}")
    return "\n".join(lines) + "\n"


def render_inputs(inputs) -> str:
    """inputs: [(파일 경로 라벨, 본문), …] 또는 {라벨: 본문}."""
    items = list(inputs.items()) if isinstance(inputs, dict) else list(inputs)
    parts = ["## 입력", ""]
    if not items:
        parts.append("(입력 없음)")
    for label, text in items:
        text = text if isinstance(text, str) else json.dumps(text, ensure_ascii=False, indent=2)
        fence = _fence_for(text)
        parts += [f"### {label}", "", f"{fence}{_lang_for(label)}", text.rstrip("\n"), fence, ""]
    return "\n".join(parts) + "\n"


SYSTEM_CACHE_DIR = ROOT / "runs" / ".cache" / "system"


def system_prompt_file(role: str) -> tuple[Path, str]:
    """공통 규칙 + 역할 규칙(고정 텍스트)을 시스템 프롬프트 파일로 만든다(운영 전환 1-5 비용).
    내용이 같으면 같은 파일을 다시 쓰므로 호출 사이에 프롬프트 캐시가 적중한다(실험: 두 번째 호출 캐시 쓰기 5.6만 → 0 토큰).
    반환: (파일 경로, sha256 앞 12자리)."""
    shared = runs.read_text(runs.AGENTS_DIR / "shared-rules.md")
    role_text = runs.read_text(runs.AGENTS_DIR / ROLE_FILES[role])
    if not shared or not role_text:
        raise AgentError("agents/shared-rules.md 또는 역할 파일이 없다")
    text = shared.rstrip("\n") + "\n\n---\n\n" + role_text.rstrip("\n") + "\n"
    if role in ("researcher", "verifier"):
        # 자주 바뀌지 않는 참조 자료도 시스템 프롬프트에 두어 캐시에 싣는다(운영 전환 1-5): GitHub 공식 저장소 원문 경로 목록
        mirrors = runs.read_text(ROOT / "config" / "source_mirrors.yaml")
        if mirrors:
            text += ("\n---\n\n## 참조: config/source_mirrors.yaml (원문을 열 수 있는 GitHub 공식 저장소 경로, 부록 R)\n\n```yaml\n"
                     + mirrors.rstrip("\n") + "\n```\n")
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]
    SYSTEM_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = SYSTEM_CACHE_DIR / f"{role}-{sha}.md"
    if not path.is_file():
        path.write_text(text, encoding="utf-8")
    return path, sha


def build_prompt(role: str, context: dict, inputs, extra_sections: dict | None = None) -> str:
    """사용자 메시지(stdin): 실행 컨텍스트 + 입력 + 추가 절. 공통 규칙과 역할 규칙은 system_prompt_file() 로 시스템 프롬프트에 붙는다."""
    parts = [f"(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/{ROLE_FILES[role]} 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)", "",
             render_context(context), render_inputs(inputs)]
    for title, body in (extra_sections or {}).items():
        body = body if isinstance(body, str) else json.dumps(body, ensure_ascii=False, indent=2)
        t = title if title.startswith("#") else f"## {title}"
        parts += [t, "", body.rstrip("\n"), ""]
    return "\n".join(parts).rstrip("\n") + "\n"


# --- CLI 호출 ---------------------------------------------------------------------------

def claude_cmd(settings: dict, role: str | None, schema: dict | None, max_turns: int | None = None,
               tools: list[str] | None = None, system_file: Path | None = None) -> list[str]:
    cmd = [str(settings.get("claude_bin") or "claude"), "-p", "--output-format", "json",
           "--permission-mode", "dontAsk", "--no-session-persistence"]
    if system_file is not None:
        cmd += ["--append-system-prompt-file", str(system_file)]
    if schema is not None:
        cmd += ["--json-schema", json.dumps(schema, ensure_ascii=False)]
    if tools is None:
        tools = list((settings.get("allowed_tools") or {}).get(role, [])) if role else []
    if tools:
        cmd += ["--tools", ",".join(tools), "--allowedTools", ",".join(tools)]
    else:
        cmd += ["--tools", ""]
    if max_turns is None and role:
        max_turns = int((settings.get("max_turns") or {}).get(role) or 0) or None
    if max_turns:
        cmd += ["--max-turns", str(max_turns)]
    if settings.get("model"):
        cmd += ["--model", str(settings["model"])]
    return cmd


def call_claude(prompt: str, cmd: list[str], timeout: int, cwd: Path = ROOT) -> tuple[dict, float]:
    """claude -p 를 실행해 JSON 봉투와 소요 시간을 돌려준다. 시간 초과·비정상 종료·JSON 아님은 AgentError."""
    t0 = time.time()
    try:
        proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True, cwd=str(cwd), timeout=timeout)
    except subprocess.TimeoutExpired as e:
        raise AgentError(f"에이전트 호출 시간 초과({timeout}초)") from e
    except FileNotFoundError as e:
        raise AgentError(f"claude 실행 파일을 찾을 수 없다: {cmd[0]}") from e
    elapsed = time.time() - t0
    out = (proc.stdout or "").strip()
    if not out:
        raise AgentError(f"claude 출력 없음 (exit {proc.returncode}): {(proc.stderr or '')[:800]}")
    try:
        env = json.loads(out)
    except json.JSONDecodeError:
        # stream 형식이나 앞에 잡음이 섞인 경우: 마지막 JSON 객체 줄을 찾는다
        env = None
        for line in reversed(out.splitlines()):
            line = line.strip()
            if line.startswith("{"):
                try:
                    env = json.loads(line)
                    break
                except json.JSONDecodeError:
                    continue
        if env is None:
            raise AgentError(f"claude 출력이 JSON 이 아니다 (exit {proc.returncode}): {out[:800]} / stderr: {(proc.stderr or '')[:400]}")
    if isinstance(env, list):  # stream-json 을 받았을 때의 방어
        env = next((x for x in reversed(env) if isinstance(x, dict) and x.get("type") == "result"), env[-1] if env else {})
    env["_stderr"] = (proc.stderr or "")[:2000]
    env["_exit_code"] = proc.returncode
    env["_elapsed_sec"] = round(elapsed, 1)
    return env, elapsed


def extract_output(envelope: dict):
    """봉투에서 구조화 출력을 꺼낸다: structured_output(dict) → result(JSON 문자열) 순."""
    if envelope.get("is_error"):
        raise AgentError(f"claude 오류 응답: {str(envelope.get('result'))[:600]}")
    so = envelope.get("structured_output")
    if isinstance(so, (dict, list)):
        return so
    result = envelope.get("result")
    if isinstance(result, (dict, list)):
        return result
    if isinstance(result, str):
        s = result.strip()
        s = re.sub(r"^```(?:json)?\s*", "", s)
        s = re.sub(r"\s*```$", "", s)
        try:
            return json.loads(s)
        except json.JSONDecodeError:
            m = re.search(r"\{.*\}", s, re.S)
            if m:
                try:
                    return json.loads(m.group(0))
                except json.JSONDecodeError:
                    pass
    raise AgentError(f"구조화 출력을 찾을 수 없다(subtype={envelope.get('subtype')}, stop_reason={envelope.get('stop_reason')}): {str(result)[:400]}")


def _usage_summary(env: dict) -> dict:
    u = env.get("usage") or {}
    return {
        "num_turns": env.get("num_turns"), "duration_ms": env.get("duration_ms"), "elapsed_sec": env.get("_elapsed_sec"),
        "total_cost_usd": env.get("total_cost_usd"), "stop_reason": env.get("stop_reason"),
        "terminal_reason": env.get("terminal_reason"), "subtype": env.get("subtype"), "is_error": env.get("is_error"),
        "input_tokens": u.get("input_tokens"), "output_tokens": u.get("output_tokens"),
        "cache_read_input_tokens": u.get("cache_read_input_tokens"), "cache_creation_input_tokens": u.get("cache_creation_input_tokens"),
        "server_tool_use": u.get("server_tool_use"), "model_usage": list((env.get("modelUsage") or {}).keys()),
        "permission_denials": env.get("permission_denials"), "exit_code": env.get("_exit_code"),
    }


def record_usage(rd: Path | None, step: str, role: str | None, env: dict, attempt: int = 1) -> dict:
    """호출 한 번의 토큰·비용을 runs/<run_id>/usage.json 에 누적한다(운영 전환 1-5). 일일 로그와 summary.json 이 합계를 쓴다."""
    u = env.get("usage") or {}
    row = {"step": step, "role": role, "attempt": attempt, "input_tokens": u.get("input_tokens") or 0,
           "cache_creation_input_tokens": u.get("cache_creation_input_tokens") or 0,
           "cache_read_input_tokens": u.get("cache_read_input_tokens") or 0, "output_tokens": u.get("output_tokens") or 0,
           "cost_usd": round(float(env.get("total_cost_usd") or 0), 4), "seconds": env.get("_elapsed_sec"),
           "num_turns": env.get("num_turns"), "models": list((env.get("modelUsage") or {}).keys())}
    if rd is not None:
        path = Path(rd) / "usage.json"
        data = runs.read_json(path, {"calls": []}) or {"calls": []}
        data.setdefault("calls", []).append(row)
        tot = {k: sum(int(c.get(k) or 0) for c in data["calls"]) for k in
               ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")}
        tot["cost_usd"] = round(sum(float(c.get("cost_usd") or 0) for c in data["calls"]), 4)
        tot["calls"] = len(data["calls"])
        data["total"] = tot
        runs.write_json(path, data)
    return row


# --- run_agent -----------------------------------------------------------------------------

def run_agent(role: str, context: dict, inputs, schema_path, out_dir, settings: dict,
              extra_sections: dict | None = None, step: str | None = None, checks: dict | None = None,
              dry_run: bool = False, log=None) -> dict:
    """프롬프트를 조립해 저장하고 claude -p 를 호출해 스키마를 통과한 dict 를 돌려준다.

    checks: {"run_type", "track_cfg", "research"} — 스키마 밖 검사(lib.runs.semantic_checks)에 쓴다.
    스키마 불일치(또는 출력 추출 실패)면 "## 스키마 불일치 (재실행)" 절을 붙여 1회 재실행하고(7.3), 그래도 실패하면 AgentError.
    """
    if role not in ROLE_FILES:
        raise ValueError(f"알 수 없는 역할: {role}")
    out_dir = Path(out_dir)
    prompts = out_dir / "prompts"
    prompts.mkdir(parents=True, exist_ok=True)
    step = step or role
    kind = ROLE_KIND[role]
    schema = runs.read_json(schema_path) if not isinstance(schema_path, dict) else schema_path
    if schema is None:
        raise AgentError(f"스키마를 읽을 수 없다: {schema_path}")
    local_schema = runs.returned_pages_schema(schema) if role == "storyteller" else schema
    cli_sch = runs.cli_schema(local_schema)
    timeout = int(settings.get("agent_timeout_sec") or 1800)
    checks = checks or {}

    prompt = build_prompt(role, context, inputs, extra_sections)
    sys_file, sys_sha = system_prompt_file(role)
    prompt_path = prompts / f"{step}.md"
    prompt_path.write_text(prompt, encoding="utf-8")
    if log:
        log.log(f"프롬프트 저장: {prompt_path.relative_to(ROOT)} ({len(prompt):,}자, 규칙은 시스템 프롬프트 {sys_file.name})", step=ROLE_KO[role])
    if dry_run:
        return {"_dry_run": True, "_prompt": str(prompt_path), "_prompt_chars": len(prompt)}

    cmd = claude_cmd(settings, role, cli_sch, system_file=sys_file)
    errors_prev: list[str] = []
    for attempt in (1, 2):
        this_prompt = prompt
        this_step = step
        if attempt == 2:
            this_step = f"{step}-schema-retry"
            fix = ("직전 반환값이 JSON 스키마(schemas/%s.schema.json)와 맞지 않아 퍼블리셔가 반려했다. "
                   "아래 오류를 모두 고친, 스키마에 맞는 JSON 객체 하나만 다시 반환한다. 내용을 새로 조사하지 말고 형식만 고친다.\n\n"
                   % kind) + "\n".join(f"- {e}" for e in errors_prev[:60])
            this_prompt = build_prompt(role, context, inputs, {**(extra_sections or {}), "스키마 불일치 (재실행)": fix})
            (prompts / f"{this_step}.md").write_text(this_prompt, encoding="utf-8")
        try:
            env, elapsed = call_claude(this_prompt, cmd, timeout)
        except AgentError as e:
            if log:
                log.log(f"호출 실패(시도 {attempt}): {e}", step=ROLE_KO[role])
            if attempt == 2:
                raise
            errors_prev = [str(e)]
            continue
        runs.write_json(prompts / f"{this_step}.response.json", {k: v for k, v in env.items() if k != "_stderr"})
        record_usage(out_dir, this_step, role, env, attempt)
        meta = {"role": role, "step": this_step, "cmd": [c if not c.startswith("{") else "<json-schema>" for c in cmd],
                "prompt_chars": len(this_prompt), "system_prompt": sys_file.name, "system_sha": sys_sha, **_usage_summary(env)}
        runs.write_json(prompts / f"{this_step}.meta.json", meta)
        if log:
            log.log(f"호출 완료(시도 {attempt}): 턴 {env.get('num_turns')} · {runs.fmt_duration(elapsed)} · 비용 ${env.get('total_cost_usd') or 0:.4f} · subtype {env.get('subtype')}", step=ROLE_KO[role])
        errs: list[str] = []
        data = None
        try:
            data = extract_output(env)
        except AgentError as e:
            errs.append(str(e))
        if data is not None:
            if not isinstance(data, dict):
                errs.append(f"구조화 출력이 객체가 아니다: {type(data).__name__}")
            else:
                errs += runs.validate(kind, data, returned=(role == "storyteller"))
                if not errs:
                    errs += runs.semantic_checks(kind, data, checks.get("run_type"), checks.get("track_cfg"), checks.get("research"),
                                                 returned=(role == "storyteller"))
        if not errs:
            return data
        (prompts / f"{this_step}.errors.txt").write_text("\n".join(errs) + "\n", encoding="utf-8")
        if log:
            log.log(f"스키마 불일치(시도 {attempt}) {len(errs)}건: {errs[0][:200]}", step=ROLE_KO[role])
        errors_prev = errs
    raise AgentError(f"{ROLE_KO[role]} 출력이 재실행 뒤에도 스키마와 맞지 않는다: {errors_prev[:3]}")


# --- 웹 도구 점검(probe) --------------------------------------------------------------------

_PROBE_SCHEMA = {"type": "object", "properties": {"ok": {"type": "boolean"}, "searched": {"type": "boolean"}, "note": {"type": "string"}},
                 "required": ["ok", "searched"]}
_PROBE_PROMPT = ('Use the WebSearch tool exactly once with the query "GS1 EPCIS standard". Then return JSON '
                 '{"ok": true, "searched": <true if the search tool call succeeded and returned results, else false>, '
                 '"note": "<one short sentence>"}.')


def probe_web_search(settings: dict, timeout: int = 240) -> dict:
    cmd = claude_cmd(settings, None, _PROBE_SCHEMA, max_turns=4, tools=["WebSearch"])
    try:
        env, elapsed = call_claude(_PROBE_PROMPT, cmd, timeout)
        data = extract_output(env)
        ok = bool(isinstance(data, dict) and data.get("searched") is True and not env.get("is_error"))
        return {"available": ok, "detail": (data.get("note") if isinstance(data, dict) else None) or str(env.get("result"))[:200],
                "elapsed_sec": round(elapsed, 1), "num_turns": env.get("num_turns"),
                "usage": record_usage(None, "probe-search", None, env)}
    except AgentError as e:
        return {"available": False, "detail": str(e)[:400]}


_FETCH_PROBE_SCHEMA = {"type": "object", "properties": {"ok": {"type": "boolean"}, "fetched": {"type": "boolean"}, "note": {"type": "string"}},
                       "required": ["ok", "fetched"]}


def _fetch_probe_prompt(url: str) -> str:
    return (f'Use the WebFetch tool exactly once to open the URL {url} with the prompt "What is the title of this page?". '
            'Then return JSON {"ok": true, "fetched": <true if the WebFetch tool call succeeded and returned page content, '
            'false if it was denied, blocked, errored or returned no content>, "note": "<one short sentence, include the error text if any>"}.')


def probe_web_fetch_tool(settings: dict, url: str, timeout: int = 240) -> dict:
    """에이전트가 실제로 쓰는 WebFetch 도구로 probe URL 을 한 번 열게 해 가용성을 본다(probe_web_search 와 같은 방식).
    프록시 정책이 셸의 curl 과 도구에 다르게 적용될 수 있으므로 web_fetch_available 은 이 결과로만 정한다."""
    cmd = claude_cmd(settings, None, _FETCH_PROBE_SCHEMA, max_turns=4, tools=["WebFetch"])
    try:
        env, elapsed = call_claude(_fetch_probe_prompt(url), cmd, timeout)
        data = extract_output(env)
        ok = bool(isinstance(data, dict) and data.get("fetched") is True and not env.get("is_error"))
        return {"available": ok, "detail": (data.get("note") if isinstance(data, dict) else None) or str(env.get("result"))[:200],
                "elapsed_sec": round(elapsed, 1), "num_turns": env.get("num_turns"), "method": "claude -p --tools WebFetch",
                "usage": record_usage(None, "probe-fetch", None, env)}
    except AgentError as e:
        return {"available": False, "detail": str(e)[:400], "method": "claude -p --tools WebFetch"}


def probe_web_fetch(url: str, timeout: int = 20) -> dict:
    """참고값: 셸의 curl HEAD(거부되면 GET)로 probe URL 이 열리는지 본다. 2xx·3xx 면 열림.
    web_fetch_available 의 근거로는 쓰지 않는다(details.web_fetch_curl 에만 남긴다)."""
    def _curl(method_args):
        try:
            p = subprocess.run(["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code}", "-m", str(timeout), *method_args, url],
                               capture_output=True, text=True, timeout=timeout + 10)
        except (FileNotFoundError, subprocess.TimeoutExpired) as e:
            return None, str(e)
        code = (p.stdout or "").strip()
        return (int(code) if code.isdigit() else 0), (p.stderr or "").strip()[:300]
    code, err = _curl(["-I"])
    if code is None:  # curl 없음 → urllib
        import urllib.error
        import urllib.request
        try:
            req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "rop-wiki-probe/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return {"available": 200 <= r.status < 400, "status": r.status, "detail": "urllib HEAD"}
        except urllib.error.HTTPError as e:
            return {"available": False, "status": e.code, "detail": f"urllib HEAD {e.code}"}
        except Exception as e:
            return {"available": False, "status": None, "detail": f"urllib 실패: {e}"[:300]}
    if code in (403, 405, 501, 0):
        code2, err2 = _curl(["-X", "GET", "-r", "0-2047"])
        if code2:
            code, err = code2, err2
    return {"available": bool(code) and 200 <= code < 400, "status": code, "detail": err or f"curl {code}"}


def probe(settings: dict, url: str | None = None, skip_search: bool = False, skip_fetch: bool = False) -> dict:
    """웹 도구 점검(7.2 의 1단계). web_search_available 은 `claude -p --tools WebSearch`, web_fetch_available 은
    `claude -p --tools WebFetch` 로 실제 도구를 한 번씩 써 본 결과다. curl 결과는 참고값(details.web_fetch_curl)으로만 남긴다.
    skip_fetch(드라이런)면 도구 점검을 생략하고 curl 참고값을 web_fetch_available 로 쓰되 details 에 생략을 표시한다 [가정].
    skip_search(드라이런)면 web_search_available 을 null 로 둔다(점검하지 않은 것을 가용으로 기록하지 않는다). run_daily.sh 는
    null 이면 "웹 도구 점검 생략(드라이런)"을 로그에 남기고 중단하지 않는다."""
    url = url or str(settings.get("web_fetch_probe_url") or "")
    search = {"available": None, "detail": "건너뜀(--skip-search)"} if skip_search else probe_web_search(settings)
    curl = probe_web_fetch(url) if url else {"available": False, "detail": "probe URL 없음"}
    if not url:
        fetch = {"available": False, "detail": "probe URL 없음(settings.web_fetch_probe_url)"}
    elif skip_fetch:
        fetch = {"available": bool(curl.get("available")), "detail": "건너뜀(--skip-fetch): WebFetch 도구 점검을 생략하고 curl 참고값을 썼다", "method": "curl(참고값)"}
    else:
        fetch = probe_web_fetch_tool(settings, url)
    # 일반 페이지 열람이 막혀도 공식 저장소 원문(raw.githubusercontent.com)은 열릴 수 있다(DECISIONS D-002). 에이전트 도구로 한 번 확인한다.
    murl = str(settings.get("web_fetch_mirror_probe_url") or "")
    if fetch.get("available") or not murl:
        mirror = {"available": bool(fetch.get("available")), "detail": "일반 열람 가능 또는 미러 점검 URL 없음"}
    elif skip_fetch:
        mc = probe_web_fetch(murl)
        mirror = {"available": bool(mc.get("available")), "detail": "건너뜀(--skip-fetch): curl 참고값", "method": "curl(참고값)"}
    else:
        mirror = probe_web_fetch_tool(settings, murl)
    mode = "full" if fetch.get("available") else ("mirror_only" if mirror.get("available") else "none")
    return {
        "web_search_available": bool(search.get("available")) if not skip_search else None,
        "web_fetch_available": bool(fetch.get("available")),
        "web_fetch_mirror_available": bool(mirror.get("available")),
        "fetch_mode": mode,
        "probe_url": url, "mirror_probe_url": murl or None, "checked_at": runs.now_str(settings),
        "details": {"web_search": search, "web_fetch": fetch, "web_fetch_mirror": mirror, "web_fetch_curl": curl},
    }


# --- 실행 컨텍스트·입력 조립(run 서브커맨드) --------------------------------------------------------

def _label_text(rel: str) -> tuple[str, str] | None:
    p = ROOT / rel
    if not p.is_file():
        return None
    return rel, p.read_text(encoding="utf-8")


def _add(inputs: list, rel: str, text: str | None = None) -> None:
    if text is not None:
        inputs.append((rel, text))
        return
    item = _label_text(rel)
    if item:
        inputs.append(item)


def _related_area_nos(target: dict, track_cfg: dict | None) -> list[int]:
    no = target.get("area_no")
    out: list[int] = []
    if track_cfg:
        out += [int(x) for x in (track_cfg.get("related_areas") or [])]
    if no:
        letter = paths.category_letter_of(int(no))
        out += [n for n in paths.area_nos_of(letter) if n != int(no)]
        try:
            meta, _ = fm.read(paths.area_file(int(no)))
            out += [int(x) for x in (meta.get("related_areas") or []) if str(x).isdigit()]
        except Exception:
            pass
    seen: list[int] = []
    for n in out:
        if n != no and n not in seen and 1 <= n <= 28:
            seen.append(n)
    return seen


def _previous_research(run_id: str, settings: dict, n: int = 7) -> list[tuple[str, str]]:
    """최근 n회 실행의 research.md(6.1 입력, 공통 규칙 10). 보류된 실행(runs/parked/)도 포함하되 라벨에 "(보류)" 를 붙이고,
    그 실행의 verification.md(반려 사유)를 함께 넣어 같은 영역이 반복 보류될 때 직전 조사·반려 사유를 재사용하게 한다."""
    out: list[tuple[str, str]] = []
    briefs = 0
    ids = [i for i in runs.list_run_ids(settings, include_parked=True) if i < run_id]
    for rid in sorted(ids, reverse=True):
        d = runs.find_run_dir(rid, settings)
        if not d:
            continue
        p = d / "research.md"
        if not p.is_file():
            continue
        rel = d.relative_to(ROOT).as_posix()
        parked = runs.is_parked(rid, settings)
        if parked and runs.is_discarded(rid, settings):
            continue   # 사용자가 폐기한 보류 실행(runs/parked/<id>/DISCARDED, RUN.md 5절)의 브리프는 넣지 않는다
        if parked:
            reason = str(runs.read_summary(d).get("park_reason") or "").strip()
            label = f"{rel}/research.md (보류" + (f": {reason[:120]}" if reason else "") + ")"
            out.append((label, p.read_text(encoding="utf-8")))
            v = d / "verification.md"
            if v.is_file():
                out.append((f"{rel}/verification.md (보류 실행의 반려 사유)", v.read_text(encoding="utf-8")))
        else:
            out.append((f"{rel}/research.md", p.read_text(encoding="utf-8")))
        briefs += 1
        if briefs >= n:
            break
    return out


AREA_REFLECTIONS_REL = "data/area_reflection_proposals.json"


def area_reflection_items(target_json: dict, run_id: str) -> list[dict]:
    """이 실행이 반영을 검토할 세부영역 반영 제안(6.3 절차 9 "반영은 다음 해당 영역 실행에서", 8.2 (5)): 트랙이 아닌 실행의
    대상 영역에 대한 status 제안 항목 가운데 이 실행보다 앞선 실행이 낸 것. 퍼블리셔가 그 영역 페이지를 게시하면 같은 기준으로
    '반영'과 실행 id 를 적는다(publish.py pending_reflection)."""
    if target_json.get("run_type") == "track":
        return []
    no = (target_json.get("target") or {}).get("area_no")
    if not str(no).isdigit():
        return []
    data = runs.read_json(ROOT / AREA_REFLECTIONS_REL, {}) or {}
    return [it for it in (data.get("items") or [])
            if it.get("status") == "제안" and str(it.get("area_no")) == str(no) and str(it.get("run_id") or "") < str(run_id)]


def _area_reflection_input(target_json: dict, run_id: str) -> tuple[str, str] | None:
    items = area_reflection_items(target_json, run_id)
    if not items:
        return None
    t = target_json.get("target") or {}
    label = (f"{AREA_REFLECTIONS_REL} (대상 영역 {t.get('area_name')} 에 대한 트랙 반영 제안 {len(items)}건, status 제안 — "
             "반영은 이 실행에서: 사양서 6.3 절차 9·공통 규칙 11)")
    return label, json.dumps({"items": items}, ensure_ascii=False, indent=2)


def _experiment_inputs() -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    total = 0
    if not runs.EXPERIMENTS_DIR.is_dir():
        return out
    for d in sorted(p for p in runs.EXPERIMENTS_DIR.iterdir() if p.is_dir()):
        files = sorted(d.rglob("*"))
        files.sort(key=lambda p: (p.name != "README.md", p.as_posix()))
        for f in files:
            if not f.is_file() or f.suffix.lower() not in TEXT_EXTS:
                continue
            try:
                text = f.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if len(text) > EXPERIMENT_FILE_CAP:
                text = text[:EXPERIMENT_FILE_CAP] + f"\n\n[… 길이 제한으로 잘림: 전체 {len(text):,}자 중 {EXPERIMENT_FILE_CAP:,}자만 포함]"
            if total + len(text) > EXPERIMENT_TOTAL_CAP:
                out.append((f.relative_to(ROOT).as_posix() + " (생략)", "[실험 입력 전체 길이 제한으로 생략]"))
                continue
            total += len(text)
            out.append((f.relative_to(ROOT).as_posix(), text))
    return out


def _track_inputs(slug: str, stage_no: int | None) -> list[tuple[str, str]]:
    inputs: list[tuple[str, str]] = []
    _add(inputs, f"config/tracks/{slug}.yaml")
    _add(inputs, f"docs/tracks/{slug}/index.md")
    cfg = runs.load_track_config(slug) or {}
    stage_no = stage_no or int(cfg.get("current_stage") or 1)
    stage_pages = cfg.get("stage_pages") or {}
    name = stage_pages.get(stage_no) or stage_pages.get(str(stage_no))
    if name and (ROOT / "docs/tracks" / slug / str(name)).is_file():
        _add(inputs, f"docs/tracks/{slug}/{name}")
    else:
        for p in sorted((paths.DOCS / "tracks" / slug).glob(f"stage-{stage_no}-*.md")):
            _add(inputs, p.relative_to(ROOT).as_posix())
            break
    _add(inputs, f"data/tracks/{slug}/backlog.json")
    # 트랙마다 자기 초안 문서(draft_page, 기본 ontology-draft.md)와 아이디어 페이지(idea_page)를 가진다(운영 전환 2부)
    draft = str(cfg.get("draft_page") or "ontology-draft.md")
    _add(inputs, f"docs/tracks/{slug}/{draft}")
    idea = cfg.get("idea_page")
    if idea:
        _add(inputs, idea if str(idea).startswith("docs/") else f"docs/ideas/{idea}")
    arts = cfg.get("stage_artifacts")
    if isinstance(arts, dict):
        stage_files = arts.get(stage_no) or arts.get(str(stage_no)) or []
    elif slug == "manual-capability-ontology":
        stage_files = STAGE_ARTIFACT_PAGES.get(stage_no, [])
    else:
        stage_files = []
    for fn in stage_files:
        _add(inputs, f"docs/tracks/{slug}/{fn}")
    tpl = cfg.get("draft_template")
    _add(inputs, f"templates/{tpl}" if tpl else "templates/ontology-draft.md")
    inputs += _experiment_inputs()
    return inputs


def _source_inputs(role: str, target_json: dict, rd: Path) -> list[tuple[str, str]]:
    """원문 열람 입력(운영 전환 1-1): GitHub 공식 저장소 원문 경로 목록과, 사람이 inbox/sources 로 넣은 원문 텍스트 가운데
    이번 대상과 관련된 것. 리서치·1차 검증에만 넣는다."""
    out: list[tuple[str, str]] = []   # config/source_mirrors.yaml 은 시스템 프롬프트에 있다(system_prompt_file)
    try:
        from lib import sources as S
    except ImportError:
        return out
    t = target_json.get("target") or {}
    kw = [str(x) for x in (t.get("area_name"), t.get("category"), target_json.get("topic")) if x]
    tr = target_json.get("track") or {}
    if tr.get("slug"):
        kw.append(str(tr["slug"]).replace("-", " "))
    refs: list[str] = []
    rp = _target_page_rel(target_json)
    if rp and (ROOT / rp).is_file():
        try:
            meta, _ = fm.read(ROOT / rp)
            refs = [str(x) for x in (meta.get("sources") or [])]
        except Exception:  # noqa: BLE001
            pass
    if role == "verifier":
        r = runs.read_json(rd / "research.json", {}) or {}
        refs += [s.get("id") for s in r.get("sources", []) if s.get("id")]
    try:
        texts = S.select_texts_for_prompt(refs, kw, 120_000)
    except Exception:  # noqa: BLE001
        texts = []
    for ref_id, text in texts:
        out.append((f"data/source_texts/{ref_id}.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)", text))
    return out


def _category_link_inputs(target_json: dict) -> list[tuple[str, str]]:
    """대분류 연결 실행: 대상 대분류 페이지와 소속 세부영역 전문, 다른 대분류 페이지와 그 세부영역 요약."""
    out: list[tuple[str, str]] = []
    letter = (target_json.get("target") or {}).get("category_letter")
    if not letter:
        return out
    _add(out, paths.category_repo_path(letter))
    for n in paths.area_nos_of(letter):
        _add(out, paths.area_repo_path(n))
    for other in "ABCDEFG":
        if other == letter:
            continue
        _add(out, paths.category_repo_path(other))
        for n in paths.area_nos_of(other):
            out.append((f"{paths.area_repo_path(n)} (요약)", runs.area_summary(n)))
    _add(out, "docs/ideas/index.md")
    return out


def _weekly_inputs(run_id: str, day: str, settings: dict) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    week = runs.iso_week(day)
    for rid in runs.list_run_ids(settings):
        if rid == run_id or runs.iso_week(rid[:10]) != week:
            continue
        d = runs.find_run_dir(rid, settings)
        if not d:
            continue
        for fn in ("research.md", "verification.md", "verification2.md", "pages.json", "log.md"):
            p = d / fn
            if p.is_file():
                rel = p.relative_to(ROOT).as_posix()
                out.append((rel, p.read_text(encoding="utf-8")))
    _add(out, "data/changelog.json")
    # 7.1 "링크·출처 유효성 점검": run_daily.sh 가 이번 실행 폴더에 남긴 스크립트 점검 결과(에이전트는 이를 근거로 정리한다)
    rd = runs.find_run_dir(run_id, settings)
    if rd:
        for fn, label in WEEKLY_CHECK_FILES:
            p = rd / fn
            if p.is_file():
                out.append((f"{rd.relative_to(ROOT).as_posix()}/{fn} ({label})", p.read_text(encoding="utf-8")))
    return out


def _monthly_inputs() -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for rel in ("docs/references/index.md", "docs/standards/index.md", "docs/glossary/index.md"):
        _add(out, rel)
    # 마지막 갱신이 오래된 게시 페이지(세부영역·주제) 상위 5개 [가정]
    cands = []
    for p in paths.DOCS.rglob("*.md"):
        try:
            meta, _ = fm.read(p)
        except Exception:
            continue
        if meta.get("type") in ("area", "topic") and meta.get("status") not in ("seed", None):
            cands.append((str(meta.get("updated", "")), p))
    for _, p in sorted(cands)[:5]:
        _add(out, p.relative_to(ROOT).as_posix())
    return out


def _target_page_rel(target_json: dict) -> str | None:
    t = target_json.get("target") or {}
    if t.get("area_no"):
        return paths.area_repo_path(int(t["area_no"]))
    return None


def _correction_pages(target_json: dict) -> list[str]:
    pages = []
    for c in target_json.get("corrections") or []:
        pg = c.get("page")
        if pg and pg not in pages and (ROOT / pg).is_file():
            pages.append(pg)
    return pages


def _stage_label(track_cfg: dict, n: int) -> str:
    names = track_cfg.get("stage_names") or {}
    nm = names.get(n) or names.get(str(n))
    return f"단계 {n}. {nm}" if nm else f"단계 {n}"


def build_context(role: str, target_json: dict, settings: dict, probe_json: dict | None, stage: str | None,
                  retry: int, track_cfg: dict | None) -> dict:
    t = target_json.get("target") or {}
    rt = target_json.get("run_type")
    ctx: dict = {"run_id": target_json.get("run_id"), "date": target_json.get("date"),
                 "run_type": f"{rt} ({runs.RUN_TYPE_KO.get(rt, '')})"}
    tr = target_json.get("track")
    if rt == "track" and tr:
        cfg = track_cfg or {}
        ctx["대상"] = (f"트랙 {tr.get('slug')} ({cfg.get('name', '')}) · 현재 단계: {_stage_label(cfg, int(tr.get('stage') or 1))}"
                      f" · 이번에 다룰 백로그 질문 id: {', '.join(tr.get('question_ids') or []) or '없음 — 현재 단계에 열린 질문이 남지 않았다. 이번 실행은 현재 단계의 완료 조건(트랙 개요 5절·단계 페이지 6절)을 채우는 산출물 보강과 단계 완료·전환 판정에 집중한다'}"
                      f" · 중심 세부영역: {t.get('area_name')} ({t.get('category')})")
        if tr.get("user_questions"):
            ctx["사용자 지정 트랙 질문(백로그 미등록)"] = "; ".join(tr["user_questions"])
    elif rt == "category_link":
        ctx["대상"] = (f"대분류 {t.get('category')} 페이지의 '다른 대분류와의 연결' 절(대분류 연결 실행). 게시된 세부영역 페이지를 근거로 "
                      "다른 대분류와의 연결을 조사·서술한다. 스토리텔러는 그 절만 patches 로 바꾼다")
    elif t.get("area_name"):
        ctx["대상"] = f"{t.get('area_name')} ({t.get('category')})"
        if target_json.get("topic"):
            ctx["주제"] = target_json["topic"]
    else:
        ctx["대상"] = f"해당 없음({runs.RUN_TYPE_KO.get(rt, rt)})"
    if target_json.get("corrections"):
        ctx["정정 요청"] = ", ".join(f"{c.get('id')} → {c.get('page')}" for c in target_json["corrections"])
    if target_json.get("priority_reason"):
        ctx["우선 지정 사유"] = target_json["priority_reason"]
    if target_json.get("priority_questions"):
        ctx["우선 지정 질문"] = "; ".join(target_json["priority_questions"])
    budget = target_json.get("budget") or runs.budget_for(settings, rt, track_cfg)
    ctx["예산"] = dict(budget)
    wf = (probe_json or {}).get("web_fetch_available")
    mode = (probe_json or {}).get("fetch_mode") or ("full" if wf else "none")
    note = f"web_fetch_available: {'true' if wf else 'false'} · fetch_mode: {mode}" if wf is not None else "없음"
    if mode == "mirror_only":
        note += (" (일반 웹 페이지 열람은 네트워크 정책으로 막혀 있다. raw.githubusercontent.com 은 열린다: 공식 문서가 GitHub 에 있는 출처는 "
                 "입력의 config/source_mirrors.yaml 경로를 WebFetch 로 열어 원문을 읽고 sources[].fetched=true, fetched_via=github_raw, "
                 "fetch_url 을 적는다. 입력에 원문 텍스트(data/source_texts)가 있는 출처는 fetched_via=inbox. 그 밖의 출처는 fetched=false 이며 "
                 "코드가 신뢰도 상한(medium)을 강제한다 — 공통 규칙 0절 6항)")
    elif mode == "none":
        note += " (페이지 열람이 차단된 환경: 공통 규칙 0절 6항. 입력의 원문 텍스트(data/source_texts)만 fetched_via=inbox 로 쓸 수 있다)"
    if wf is False and (probe_json or {}).get("web_fetch_override"):
        note += " · 원문 미열람 모드(사용자 override: " + str(probe_json.get("web_fetch_override_source") or "사용자") + ")"
    ctx["환경 알림"] = note
    if role in ("researcher", "storyteller") or (role == "verifier" and (stage or "first") == "first"):
        arp = area_reflection_items(target_json, str(target_json.get("run_id") or ""))
        if arp:
            ctx["세부영역 반영 제안"] = (f"{len(arp)}건 — 트랙 실행이 이 영역 페이지에 반영하자고 제안한 내용(입력 {AREA_REFLECTIONS_REL}). "
                                   "이번 실행의 조사·검증을 거쳐 해당 절에 반영을 검토한다(사양서 6.3 절차 9 '반영은 다음 해당 영역 실행에서')")
    ctx["언어"] = settings.get("language", "ko")
    if role == "verifier":
        ctx["verification_stage"] = stage or "first"
        ctx["verifier_budget"] = dict(budget)
    if role == "researcher":
        ctx["next_ref_id"] = runs.next_reference_id()
    if retry:
        ctx["retry_count"] = retry
        ctx["max_retries"] = budget.get("max_retries", 2)
    return ctx


def build_inputs(role: str, run_id: str, target_json: dict, settings: dict, stage: str | None, retry: int,
                 track_cfg: dict | None, rd: Path, format_fix: int = 0) -> list[tuple[str, str]]:
    inputs: list[tuple[str, str]] = []
    rt = target_json.get("run_type")
    rel_run = f"runs/{run_id}"
    t = target_json.get("target") or {}
    target_rel = _target_page_rel(target_json)
    is_track = rt == "track" and target_json.get("track")
    slug = (target_json.get("track") or {}).get("slug") if is_track else None
    stage_no = (target_json.get("track") or {}).get("stage") if is_track else None

    reflection = _area_reflection_input(target_json, run_id)   # 비트랙 실행: 대상 영역의 트랙 반영 제안(status 제안)

    def common_context_pages():
        _add(inputs, f"{rel_run}/target.json", json.dumps(target_json, ensure_ascii=False, indent=2))
        if target_rel:
            _add(inputs, target_rel)
        if reflection:
            inputs.append(reflection)
        for pg in _correction_pages(target_json):
            if pg != target_rel:
                _add(inputs, pg)
        for n in _related_area_nos(t, track_cfg if is_track else None):
            inputs.append((f"{paths.area_repo_path(n)} (요약)", runs.area_summary(n)))
        _add(inputs, "docs/glossary/index.md")
        _add(inputs, "docs/references/index.md")
        _add(inputs, "docs/open-questions.md")
        _add(inputs, "config/priority.yaml")
        _add(inputs, "inbox/corrections.md")
        inputs.extend(_previous_research(run_id, settings))

    if role == "researcher":
        common_context_pages()
        inputs.extend(_source_inputs(role, target_json, rd))
        if rt == "category_link":
            inputs.extend(_category_link_inputs(target_json))
        if rt == "weekly_review":
            inputs.extend(_weekly_inputs(run_id, target_json.get("date", run_id[:10]), settings))
        if rt == "monthly_recheck":
            inputs.extend(_monthly_inputs())
        if is_track:
            inputs.extend(_track_inputs(slug, stage_no))
        if retry:
            _add(inputs, f"{rel_run}/research.json")
    elif role == "verifier" and (stage or "first") == "first":
        _add(inputs, f"{rel_run}/target.json", json.dumps(target_json, ensure_ascii=False, indent=2))
        _add(inputs, f"{rel_run}/research.json")
        if target_rel:
            _add(inputs, target_rel)
        if reflection:
            inputs.append(reflection)
        for pg in _correction_pages(target_json):
            if pg != target_rel:
                _add(inputs, pg)
        for n in _related_area_nos(t, track_cfg if is_track else None):
            inputs.append((f"{paths.area_repo_path(n)} (요약)", runs.area_summary(n)))
        _add(inputs, "docs/glossary/index.md")
        _add(inputs, "docs/references/index.md")
        _add(inputs, "docs/open-questions.md")
        _add(inputs, "inbox/corrections.md")
        _add(inputs, "config/priority.yaml")
        inputs.extend(_previous_research(run_id, settings))
        if retry and (rd / "verification.json").is_file():
            _add(inputs, f"{rel_run}/verification.json")
        _add(inputs, "_source/ROP_SCM_연구분야_분류.md")
        inputs.extend(_source_inputs(role, target_json, rd))
        if rt == "category_link":
            inputs.extend(_category_link_inputs(target_json))
        if rt == "weekly_review":
            inputs.extend(_weekly_inputs(run_id, target_json.get("date", run_id[:10]), settings))
        if is_track:
            inputs.extend(_track_inputs(slug, stage_no))
    elif role == "verifier":  # second
        _add(inputs, f"{rel_run}/target.json", json.dumps(target_json, ensure_ascii=False, indent=2))
        _add(inputs, f"{rel_run}/research.json")
        _add(inputs, f"{rel_run}/verification.json")
        pages_json = runs.read_json(rd / "pages.json", {}) or {}
        _add(inputs, f"{rel_run}/pages.json", json.dumps(pages_json, ensure_ascii=False, indent=2))
        page_types: list[str] = []
        weekly_page = False
        for pg in pages_json.get("pages", []):
            rel = paths.docs_rel(pg.get("path", ""))
            p = rd / "pages" / rel
            if p.is_file():
                inputs.append((f"{rel_run}/pages/{rel}", p.read_text(encoding="utf-8")))
                try:
                    meta, _ = fm.read(p)
                    if _is_weekly_page(rel, meta):
                        weekly_page = True   # 주간 정리(type log)는 일일 로그 템플릿이 기준이 아니다
                    elif meta.get("type") and meta.get("subtype") != "index":
                        page_types.append(str(meta["type"]))
                except Exception:
                    pass
            if (ROOT / pg.get("path", "")).is_file():
                _add(inputs, pg["path"])
        if target_rel and not any(l == target_rel for l, _ in inputs):
            _add(inputs, target_rel)
        # 6.2 2차 검증 항목 "템플릿 섹션 순서 준수": 스토리텔러가 받은 것과 같은 기준 템플릿(실행 유형별 + pages.json 이 만진 페이지 유형별)을 준다
        tpls: list[str] = list(TEMPLATES_BY_RUN_TYPE.get(rt, []))
        for t in page_types:
            f = TEMPLATE_BY_PAGE_TYPE.get(t)
            if f and f not in tpls:
                tpls.append(f)
        for tpl in tpls:
            _add(inputs, f"templates/{tpl}")
        if weekly_page or rt == "weekly_review":
            spec = _weekly_section_spec()   # 주간 정리 페이지의 기준 절 구성(templates/weekly-log.md 또는 storyteller.md 6절)
            if spec:
                inputs.append(spec)
        _add(inputs, f"{rel_run}/docs_tree.txt")
        _add(inputs, "docs/glossary/index.md")
        _add(inputs, "docs/references/index.md")
        _add(inputs, "docs/open-questions.md")
        _add(inputs, "_source/ROP_SCM_연구분야_분류.md")
        if retry and (rd / "verification2.json").is_file():
            _add(inputs, f"{rel_run}/verification2.json")
        if is_track:
            inputs.extend(_track_inputs(slug, stage_no))
    elif role == "storyteller":
        _add(inputs, f"{rel_run}/target.json", json.dumps(target_json, ensure_ascii=False, indent=2))
        _add(inputs, f"{rel_run}/research.json")
        _add(inputs, f"{rel_run}/verification.json")
        if target_rel:
            _add(inputs, target_rel)
            _add(inputs, paths.category_repo_path(paths.category_letter_of(int(t["area_no"]))))
        if reflection:
            inputs.append(reflection)
        for pg in _correction_pages(target_json):
            if pg != target_rel:
                _add(inputs, pg)
        for tpl in TEMPLATES_BY_RUN_TYPE.get(rt, []):
            _add(inputs, f"templates/{tpl}")
        if rt == "category_link":
            letter = t.get("category_letter")
            if letter:
                _add(inputs, paths.category_repo_path(letter))
        for rel in ("docs/glossary/index.md", "docs/references/index.md", "docs/standards/index.md", "docs/open-questions.md"):
            _add(inputs, rel)
        _add(inputs, f"{rel_run}/docs_tree.txt")
        _add(inputs, "inbox/corrections.md")
        if rt == "weekly_review":
            inputs.extend(_weekly_inputs(run_id, target_json.get("date", run_id[:10]), settings))
        if is_track:
            inputs.extend(_track_inputs(slug, stage_no))
        if retry or format_fix:
            pages_json = runs.read_json(rd / "pages.json", None)
            if pages_json is not None:
                _add(inputs, f"{rel_run}/pages.json", json.dumps(pages_json, ensure_ascii=False, indent=2))
                for pg in pages_json.get("pages", []):
                    rel = paths.docs_rel(pg.get("path", ""))
                    p = rd / "pages" / rel
                    if p.is_file():
                        inputs.append((f"{rel_run}/pages/{rel}", p.read_text(encoding="utf-8")))
            if retry:
                _add(inputs, f"{rel_run}/verification2.json")
    return inputs


def _rejection_section(verification: dict) -> str:
    """1차 검증 반려 결과를 '## 반려 사유' 절 본문으로 만든다."""
    lines = [f"- 판정(verdict): {verification.get('verdict')}",
             f"- 재조사 사유(retry_reason): {verification.get('retry_reason') or '—'}"]
    fixes = verification.get("required_fixes") or []
    if fixes:
        lines += ["- 보강할 질문·수정 목록(required_fixes):"] + [f"    - {x}" for x in fixes]
    bad = [c for c in verification.get("claim_checks") or [] if c.get("tag_decision") != "유지" or not c.get("source_exists") or not c.get("supports_claim")]
    if bad:
        lines.append("- 문제 삼은 주장(claim_checks):")
        for c in bad:
            lines.append(f"    - {c.get('finding_id')}: 출처 실재 {c.get('source_exists')} · 뒷받침 {c.get('supports_claim')} · 교차 {c.get('cross_checked')} · 처분 {c.get('tag_decision')} — {c.get('note')}")
    for key, label in (("scope_boundary", "범위 경계"), ("duplication", "중복·모순"), ("terminology", "용어 일관성"), ("category_fit", "분류 적합성")):
        v = verification.get(key) or {}
        if v and v.get("ok") is False:
            lines.append(f"- {label}: {json.dumps(v, ensure_ascii=False)}")
    lines.append(f"- 검증 노트: {verification.get('verification_note') or '—'}")
    lines.append("\n직전 브리프(runs/<run_id>/research.json)는 입력에 있다. 위 사유에 답하는 보강 조사를 하고 전체 브리프를 다시 반환한다(researcher.md 12절).")
    return "\n".join(lines)


def _fix_section(verification2: dict) -> str:
    lines = [f"- 판정(verdict): {verification2.get('verdict')}",
             f"- 재작업 사유(retry_reason): {verification2.get('retry_reason') or '—'}"]
    fixes = verification2.get("required_fixes") or []
    lines += ["- 수정 지시(required_fixes):"] + ([f"    - {x}" for x in fixes] or ["    - (없음)"])
    lines.append(f"- 검증 노트: {verification2.get('verification_note') or '—'}")
    tc = verification2.get("track_checks")
    if tc:
        lines.append(f"- 트랙 검사(track_checks): {json.dumps(tc, ensure_ascii=False)}")
    lines.append("\n이전 초안(runs/<run_id>/pages.json, pages/)과 2차 판정(verification2.json)은 입력에 있다. storyteller.md 9절대로 이행하고 모든 페이지의 content 를 포함한 전체 pages.json 을 다시 반환한다.")
    return "\n".join(lines)


def _format_fix_section(rd: Path) -> str:
    rep = runs.read_json(rd / "checks" / "pages.json", {}) or {}
    errs = rep.get("errors") or []
    lines = ["직전 원고(runs/<run_id>/pages.json, pages/)가 코드 형식 검증(pipeline/validate_run.py)을 통과하지 못했다. "
             "내용(주장·태그·각주·판정)은 바꾸지 말고 아래 형식 오류만 고친 전체 pages.json 을 다시 반환한다. "
             "차등 갱신 실행이면 patches 로, 아니면 content 로 보낸다.", ""]
    lines += [f"- {e}" for e in errs[:60]] or ["- (오류 목록 없음)"]
    return "\n".join(lines)


def save_output(role: str, stage: str | None, data: dict, rd: Path, run_id: str, log=None) -> Path:
    """검증을 통과한 출력을 runs/<run_id>/ 에 저장하고 .md 를 렌더링한다. 스토리텔러는 pages/ 로 풀어낸다."""
    if role == "researcher":
        out = runs.write_json(rd / "research.json", data)
        render_run_md.render_run(rd, "research")
    elif role == "verifier":
        name = "verification2" if (stage or "first") == "second" else "verification"
        out = runs.write_json(rd / f"{name}.json", data)
        render_run_md.render_run(rd, name)
    else:
        pages_dir = rd / "pages"
        if pages_dir.exists():
            shutil.rmtree(pages_dir)
        stored = json.loads(json.dumps(data, ensure_ascii=False))
        for pg in stored.get("pages", []):
            rel = paths.docs_rel(pg.get("path", ""))
            content = pg.pop("content", None)
            if content is None:
                continue
            runs.write_text(pages_dir / rel, content if content.endswith("\n") else content + "\n")
        out = runs.write_json(rd / "pages.json", stored)
        render_run_md.render_run(rd, "pages")
    if log:
        log.log(f"저장: {out.relative_to(ROOT)}", step=ROLE_KO[role])
    return out


def record_base(rd: Path) -> None:
    """스토리텔러가 입력으로 읽는 위키 상태의 기준 커밋을 runs/<id>/base.json 에 남긴다. 배치로 여러 실행이 동시에 돌 때 퍼블리셔가
    이 기준과 현재 페이지를 비교해 다른 실행이 먼저 바꾼 페이지를 3-way 병합한다(publish.py reconcile_concurrent_changes)."""
    p = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True)
    head = (p.stdout or "").strip()
    if p.returncode == 0 and head:
        runs.write_json(rd / "base.json", {"head": head, "recorded": time.strftime("%Y-%m-%d %H:%M:%S")})


def cmd_run(args) -> int:
    settings = runs.load_settings()
    rd = runs.find_run_dir(args.run_id, settings)
    if not rd:
        print(f"[agent_runner] 실행 폴더 없음: runs/{args.run_id}")
        return 2
    target_json = runs.read_json(rd / "target.json")
    if not target_json:
        print(f"[agent_runner] target.json 없음: {rd}")
        return 2
    log = runs.RunLog(rd, settings)
    log.ensure(args.run_id)
    rt = target_json.get("run_type")
    track_cfg = runs.load_track_config((target_json.get("track") or {}).get("slug")) if rt == "track" and target_json.get("track") else None
    probe_json = runs.read_json(rd / "probe.json", None)
    if args.web_fetch_available is not None:
        probe_json = dict(probe_json or {}, web_fetch_available=(args.web_fetch_available == "true"))
    stage = args.stage if args.role == "verifier" else None
    retry = int(args.retry or 0)
    context = build_context(args.role, target_json, settings, probe_json, stage, retry, track_cfg)
    format_fix = int(getattr(args, "format_fix", 0) or 0)
    if args.role == "storyteller" and not args.dry_run:
        record_base(rd)
    inputs = build_inputs(args.role, args.run_id, target_json, settings, stage, retry, track_cfg, rd, format_fix)
    extra: dict = {}
    if format_fix and args.role == "storyteller":
        extra["형식 검증 오류 (재작성)"] = _format_fix_section(rd)
    if retry and args.role == "researcher":
        v = runs.read_json(rd / "verification.json", None)
        if v:
            extra["반려 사유"] = _rejection_section(v)
    if retry and args.role == "storyteller":
        v2 = runs.read_json(rd / "verification2.json", None)
        if v2:
            extra["수정 지시"] = _fix_section(v2)
    base = {"researcher": "research", "verifier": "verification1" if (stage or "first") == "first" else "verification2",
            "storyteller": "storyteller"}[args.role]
    step = base + (f"-retry{retry}" if retry else "") + (f"-formatfix{format_fix}" if format_fix else "")
    checks = {"run_type": rt, "track_cfg": track_cfg, "research": runs.read_json(rd / "research.json", None) if args.role != "researcher" else None}
    schema_path = runs.SCHEMA_DIR / runs._SCHEMA_FILES[ROLE_KIND[args.role]]
    try:
        data = run_agent(args.role, context, inputs, schema_path, rd, settings, extra, step=step, checks=checks,
                         dry_run=args.dry_run, log=log)
    except AgentError as e:
        log.log(f"실패: {e}", step=ROLE_KO[args.role])
        print(f"[agent_runner] {ROLE_KO[args.role]} 실패: {e}")
        return 3
    if args.dry_run:
        print(f"[agent_runner] 드라이런: 프롬프트만 저장 {data['_prompt']} ({data['_prompt_chars']:,}자)")
        return 0
    out = save_output(args.role, stage, data, rd, args.run_id, log)
    print(f"[agent_runner] {ROLE_KO[args.role]} 완료 → {out.relative_to(ROOT)}")
    return 0


def cmd_probe(args) -> int:
    try:
        settings = runs.load_settings()
    except Exception as e:
        print(json.dumps({"web_search_available": False, "web_fetch_available": False, "error": f"설정 로드 실패: {e}"}, ensure_ascii=False))
        return 2
    result = probe(settings, url=args.url, skip_search=args.skip_search, skip_fetch=args.skip_fetch)
    if args.out:
        runs.write_json(args.out, result)
    print(json.dumps(result, ensure_ascii=False))
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("probe", help="웹 도구 점검(claude -p 로 WebSearch 1회, WebFetch 로 probe URL 1회; curl 은 참고값)")
    p.add_argument("--out", help="결과 JSON 저장 경로")
    p.add_argument("--url", help="페이지 열람 점검 URL(기본 settings.web_fetch_probe_url)")
    p.add_argument("--skip-search", action="store_true", help="WebSearch 점검을 건너뛴다(드라이런용)")
    p.add_argument("--skip-fetch", action="store_true", help="WebFetch 도구 점검을 건너뛰고 curl 참고값을 쓴다(드라이런용)")
    p.set_defaults(func=cmd_probe)
    p = sub.add_parser("run", help="에이전트 1회 실행")
    p.add_argument("--role", required=True, choices=list(ROLE_FILES))
    p.add_argument("--run-id", required=True)
    p.add_argument("--stage", choices=["first", "second"], default=None, help="검증 단계(verifier)")
    p.add_argument("--retry", type=int, default=0, help="재실행 회차(0 = 첫 실행)")
    p.add_argument("--format-fix", type=int, default=0, help="형식 검증 오류 수정 재작성 회차(스토리텔러, 0 = 아님)")
    p.add_argument("--web-fetch-available", choices=["true", "false"], default=None, help="probe.json 대신 쓸 값")
    p.add_argument("--dry-run", action="store_true", help="프롬프트만 저장하고 호출하지 않는다")
    p.set_defaults(func=cmd_run)
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "--probe":  # `agent_runner.py --probe …` 도 받는다(실행 규약의 표기)
        argv[0] = "probe"
    args = ap.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
