#!/usr/bin/env python3
"""실행 결과 알림(퍼블리셔 9단계)과 운영 설정(config/ops.yaml) 읽기·스위치 전환.

알림은 표준 라이브러리만 쓴다(urllib.request, smtplib, email.message). 비밀값은 환경변수에서만 읽는다.

공개 API (publish.py 에서 `from lib import notify`)
  load_ops(path=None) -> dict
      config/ops.yaml(또는 환경변수 ROP_OPS_CONFIG 의 경로)을 읽어 DEFAULTS 와 합친다. 파일이 없거나 읽을 수 없으면 DEFAULTS
      (외부 스위치 모두 꺼짐)를 돌려준다 — 설정 오류가 발송·배포·cron 을 켜는 쪽으로 흐르지 않게 한다.
  event_of(summary) -> "published" | "parked" | "failed"
  build_message(summary, daily_log_rel, site_url=None) -> {"subject": str, "text": str}
  send(summary, daily_log_rel, cfg=None, transport=None) -> {"status": "disabled|skipped|sent|failed", "detail": str}
      cfg: ops.yaml 전체 dict 또는 그 notify 절 dict. None 이면 load_ops()["notify"].
      transport(시험용 주입): 채널이 하나면 callable, both 면 {"slack": f, "email": g} dict.
        slack  — f(url: str, body: bytes) (반환값이 int 면 HTTP 상태로 보고 2xx 가 아니면 실패)
        email  — g(msg: email.message.EmailMessage), 또는 {"smtp_factory": cls} 로 smtplib.SMTP 대신 쓸 클래스를 준다
      notify.enabled 가 false 면 네트워크를 쓰지 않고 disabled 를 돌려준다. 어떤 오류도 예외로 내보내지 않는다(failed + detail).

CLI (위키 루트에서)
  python3 pipeline/lib/notify.py --test --mock            # 보낼 메시지와 모의 전송 내용을 출력(네트워크 없음, enabled 무시)
  python3 pipeline/lib/notify.py --test [--force]         # 설정대로 시험 메시지를 실제로 보낸다(--force: enabled: false 여도 보냄)
  python3 pipeline/lib/notify.py --run-id 2026-09-25-01 [--mock]   # 그 실행의 summary.json 으로 알림(설정 따름)
  python3 pipeline/lib/notify.py --status                 # 알림·배포·cron 스위치, 비밀값 환경변수 설정 여부, crontab 등록 여부
  python3 pipeline/lib/notify.py --get cron.enabled [--default x]  # 셸 스크립트용 값 읽기(bool 은 true/false)
  python3 pipeline/lib/notify.py --enable notify --channel slack_webhook | --enable deploy [--method actions] | --enable cron
  python3 pipeline/lib/notify.py --disable <notify|deploy|cron>
      ops.yaml 의 해당 절 enabled(와 channel·method) 줄만 바꾼다(주석 보존)
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import re
import smtplib
import ssl
import subprocess
import sys
import urllib.request
from email.message import EmailMessage
from email.utils import formatdate, make_msgid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OPS_FILE = ROOT / "config" / "ops.yaml"
SETTINGS_FILE = ROOT / "config" / "settings.yaml"

CHANNELS = ("none", "slack_webhook", "email", "both")
EVENTS = ("published", "parked", "failed")
EVENT_KO = {"published": "게시", "parked": "보류", "failed": "실패"}
SWITCHES = ("notify", "deploy", "cron")
DEPLOY_METHODS = ("gh-deploy", "actions")
SUBJECT_PREFIX = "[ROP 위키]"

# 실행 유형 한국어 이름: lib/runs.py 의 RUN_TYPE_KO 를 우선 쓰고(run_type_label), runs 를 읽을 수 없을 때만 이 사본을 쓴다
RUN_TYPE_KO = {
    "area_deep_dive": "영역 심화", "topic": "주제 조사", "update": "갱신",
    "weekly_review": "주간 정리", "monthly_recheck": "월간 재검증", "track": "트랙 실행",
}

DEFAULTS: dict = {
    "notify": {
        "enabled": False, "channel": "none", "on": list(EVENTS), "site_url": "",
        "slack": {"webhook_url_env": "ROP_SLACK_WEBHOOK_URL", "timeout_sec": 10},
        "email": {"smtp_host": "", "smtp_port": 587, "use_tls": True, "use_ssl": False, "from": "", "to": [],
                  "username_env": "ROP_SMTP_USERNAME", "password_env": "ROP_SMTP_PASSWORD", "timeout_sec": 20},
    },
    "deploy": {"enabled": False, "method": "gh-deploy", "remote_name": "origin", "remote_branch": "gh-pages",
               "after_daily_run": True},
    "cron": {"enabled": False, "tz_mode": "auto", "lock_file": "runs/.lock", "log_file": "runs/cron.log",
             "log_max_bytes": 5 * 1024 * 1024, "env_file": "~/.config/rop-wiki/env", "max_runtime_sec": 14400},
}

SAMPLE_SUMMARY: dict = {
    "run_id": "2026-09-25-01", "date": "2026-09-25", "run_type": "area_deep_dive",
    "target": {"area_no": 7, "area_name": "7. 화물·재고·자산 식별과 추적", "category": "B. 공통 정보·환경 모델"},
    "end_state": "게시 완료", "published": True, "parked": False, "pages_created": 1, "pages_updated": 1,
    "cost_usd": 14.62,
}


# --- 설정 ----------------------------------------------------------------------------------------

def _merge(base: dict, over: dict) -> dict:
    out = copy.deepcopy(base)
    for k, v in (over or {}).items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _merge(out[k], v)
        else:
            out[k] = v
    return out


def ops_path(path: str | os.PathLike | None = None) -> Path:
    if path:
        return Path(path)
    env = os.environ.get("ROP_OPS_CONFIG", "").strip()
    if env:
        p = Path(env)
        return p if p.is_absolute() else ROOT / p
    return OPS_FILE


def load_ops(path: str | os.PathLike | None = None) -> dict:
    """ops.yaml 을 DEFAULTS 와 합쳐 돌려준다. 파일이 없거나 YAML 오류면 DEFAULTS(모두 꺼짐)와 `_error` 키."""
    p = ops_path(path)
    out = copy.deepcopy(DEFAULTS)
    if not p.is_file():
        out["_error"] = f"설정 파일 없음: {p}"
        return out
    try:
        import yaml  # pyyaml 은 requirements.txt 의 의존성이다
        data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        if not isinstance(data, dict):
            raise ValueError("최상위가 매핑이 아니다")
    except Exception as e:  # 설정 오류는 "꺼짐"으로 처리한다
        out["_error"] = f"{p} 를 읽지 못해 기본값(모두 꺼짐)을 쓴다: {type(e).__name__}: {e}"
        return out
    return _merge(out, data)


def _truthy(v) -> bool:
    if isinstance(v, bool):
        return v
    if isinstance(v, (int, float)):
        return v != 0
    return str(v or "").strip().lower() in ("1", "true", "yes", "on")


def _notify_section(cfg: dict | None) -> dict:
    if cfg is None:
        return load_ops()["notify"]
    if isinstance(cfg.get("notify"), dict):
        return _merge(DEFAULTS["notify"], cfg["notify"])
    return _merge(DEFAULTS["notify"], cfg)


def get_value(key: str, default=None, path=None):
    cur = load_ops(path)
    for part in key.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return default
    return cur


def _fmt_value(v) -> str:
    if v is None:
        return ""
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (list, dict)):
        return json.dumps(v, ensure_ascii=False)
    return str(v)


def set_switch(name: str, on: bool, channel: str | None = None, path=None, method: str | None = None) -> str:
    """ops.yaml 의 `<name>:` 절 바로 아래 `  enabled:` 줄(과 notify 의 `  channel:`, deploy 의 `  method:` 줄)만 바꾼다.
    주석·다른 줄은 그대로 둔다."""
    if name not in SWITCHES:
        raise ValueError(f"알 수 없는 스위치: {name} (가능: {', '.join(SWITCHES)})")
    if channel is not None and (name != "notify" or channel not in CHANNELS):
        raise ValueError(f"--channel 은 notify 에만 쓰고 값은 {', '.join(CHANNELS)} 중 하나다")
    if method is not None and (name != "deploy" or method not in DEPLOY_METHODS):
        raise ValueError(f"--method 는 deploy 에만 쓰고 값은 {', '.join(DEPLOY_METHODS)} 중 하나다")
    p = ops_path(path)
    text = p.read_text(encoding="utf-8")
    sec = re.search(rf"^{name}:[ \t]*(#.*)?$", text, re.M)
    if not sec:
        raise ValueError(f"{p} 에 '{name}:' 절이 없다")
    nxt = re.search(r"^\S", text[sec.end() + 1:], re.M)
    end = sec.end() + 1 + nxt.start() if nxt else len(text)
    body = text[sec.end():end]

    def repl(key: str, value: str, body: str) -> str:
        def keep_column(m: re.Match) -> str:   # 뒤 주석의 열 위치를 유지한다
            width = len(m.group(2)) + len(m.group(3))
            pad = m.group(3) and " " * max(1, width - len(value))
            return m.group(1) + value + pad
        new, n = re.subn(rf"^(  {key}:[ \t]*)([^\s#]+)([ \t]*)", keep_column, body, count=1, flags=re.M)
        if n != 1:
            raise ValueError(f"{p} 의 '{name}:' 절에 '  {key}:' 줄이 없다")
        return new

    body = repl("enabled", "true" if on else "false", body)
    if channel is not None:
        body = repl("channel", channel, body)
    if method is not None:
        body = repl("method", method, body)
    p.write_text(text[:sec.end()] + body + text[end:], encoding="utf-8")
    check = load_ops(p)
    if check.get("_error") or _truthy(check[name]["enabled"]) != on:
        raise ValueError(f"{p} 수정 뒤 다시 읽은 값이 기대와 다르다: {check.get('_error') or check[name]}")
    state = "켬" if on else "끔"
    return (f"{p}: {name}.enabled = {'true' if on else 'false'} ({state})" + (f", notify.channel = {channel}" if channel else "")
            + (f", deploy.method = {method}" if method else ""))


# --- 메시지 --------------------------------------------------------------------------------------

def run_type_label(rt) -> str:
    labels = RUN_TYPE_KO
    try:
        try:
            from lib import runs  # publish.py 처럼 pipeline/ 이 sys.path 에 있을 때
        except ImportError:
            sys.path.insert(0, str(ROOT / "pipeline"))
            from lib import runs  # type: ignore
        labels = {**RUN_TYPE_KO, **getattr(runs, "RUN_TYPE_KO", {})}
    except Exception:
        pass
    return labels.get(rt, rt or "미선정")


def event_of(summary: dict) -> str:
    if summary.get("published") is True:
        return "published"
    if summary.get("parked") or str(summary.get("end_state") or "").startswith("보류"):
        return "parked"
    return "failed"


def _num(v):
    return float(v) if isinstance(v, (int, float)) and not isinstance(v, bool) else None


def cost_of(summary: dict) -> float | None:
    """summary 의 비용 합계(USD). cost_usd / total_cost_usd / cost(수·dict) / costs(dict) 중 먼저 있는 값. 없으면 None."""
    for key in ("cost_usd", "total_cost_usd"):
        n = _num(summary.get(key))
        if n is not None:
            return n
    for key in ("cost", "costs"):
        v = summary.get(key)
        n = _num(v)
        if n is not None:
            return n
        if isinstance(v, dict):
            for k in ("total_usd", "total_cost_usd", "usd", "total"):
                n = _num(v.get(k))
                if n is not None:
                    return n
    return None


def _target_text(summary: dict) -> str:
    t = summary.get("target") or {}
    if summary.get("run_type") == "track" or t.get("slug"):
        parts = [f"트랙 {t.get('slug') or '?'}"]
        if t.get("stage") is not None:
            parts.append(f"단계 {t.get('stage')}")
        if t.get("question_ids"):
            parts.append("질문 " + ", ".join(str(q) for q in t["question_ids"]))
        if t.get("area_name"):
            parts.append(f"중심 영역 {t['area_name']}")
        return " · ".join(parts)
    if t.get("area_name"):
        return str(t["area_name"]) + (f" · 주제: {summary['topic']}" if summary.get("topic") else "")
    if not summary.get("run_type"):
        return "미선정(대상 선정 전에 중단)"
    return "해당 없음"


def _site_link(site_url: str | None, daily_log_rel: str) -> str | None:
    if not site_url or not daily_log_rel:
        return None
    rel = daily_log_rel.replace("\\", "/").lstrip("./")
    rel = rel[len("docs/"):] if rel.startswith("docs/") else rel
    if rel.endswith(".md"):
        rel = rel[:-3]
    return site_url.rstrip("/") + "/" + rel + "/"


def build_message(summary: dict, daily_log_rel: str, site_url: str | None = None) -> dict:
    """짧은 한국어 알림 메시지. 반환: {"subject": 제목, "text": 본문}."""
    ev = event_of(summary)
    run_id = str(summary.get("run_id") or "?")
    rt = summary.get("run_type")
    rt_label = run_type_label(rt)
    target = _target_text(summary)
    subject = f"{SUBJECT_PREFIX} {EVENT_KO[ev]} · {run_id} {rt_label}"
    if target and not target.startswith(("해당 없음", "미선정")):
        subject += f" — {target}"
    lines = [
        f"ROP 연구 위키 일일 실행 결과: {EVENT_KO[ev]}",
        f"- 실행 id: {run_id}" + (f" ({summary['date']})" if summary.get("date") else ""),
        f"- 유형: {rt_label}",
        f"- 대상: {target}",
        f"- 종료 상태: {summary.get('end_state') or '알 수 없음'}",
        f"- 생성/갱신: 생성 {int(summary.get('pages_created') or 0)} / 갱신 {int(summary.get('pages_updated') or 0)}",
    ]
    if ev == "parked" and summary.get("park_reason"):
        lines.append(f"- 보류 사유: {summary['park_reason']}")
    cost = cost_of(summary)
    if cost is not None:
        lines.append(f"- 비용 합계: ${cost:,.2f}")
    lines.append(f"- 로그: {daily_log_rel}")
    link = _site_link(site_url, daily_log_rel)
    if link:
        lines.append(f"- 사이트: {link}")
    return {"subject": subject, "text": "\n".join(lines)}


# --- 발송 ----------------------------------------------------------------------------------------

def _mask(text: str, secrets: list[str | None]) -> str:
    out = str(text)
    for s in secrets:
        if s and len(s) >= 4:
            out = out.replace(s, "***")
    return out


def _pick(transport, name: str):
    if transport is None:
        return None
    if isinstance(transport, dict):
        return transport.get(name)
    return transport


def _send_slack(msg: dict, scfg: dict, transport=None) -> tuple[str, str]:
    env_name = str(scfg.get("webhook_url_env") or "ROP_SLACK_WEBHOOK_URL")
    url = os.environ.get(env_name, "").strip()
    if not url:
        return "failed", f"slack: 환경변수 {env_name} 이 비어 있다(웹훅 URL 은 환경변수로만 준다)"
    if not url.startswith("https://"):
        return "failed", f"slack: {env_name} 의 값이 https:// 로 시작하지 않는다"
    body = json.dumps({"text": f"*{msg['subject']}*\n{msg['text']}"}, ensure_ascii=False).encode("utf-8")
    try:
        if transport is not None:
            code = transport(url, body)
        else:
            req = urllib.request.Request(url, data=body, method="POST",
                                         headers={"Content-Type": "application/json; charset=utf-8"})
            with urllib.request.urlopen(req, timeout=float(scfg.get("timeout_sec") or 10)) as resp:
                code = getattr(resp, "status", None) or resp.getcode()
        if isinstance(code, int) and not isinstance(code, bool) and not 200 <= code < 300:
            return "failed", f"slack: HTTP {code}"
        return "sent", "slack: 웹훅 전송" + (f"(HTTP {code})" if isinstance(code, int) and not isinstance(code, bool) else "")
    except Exception as e:
        return "failed", _mask(f"slack: {type(e).__name__}: {e}", [url])


def _addresses(v) -> list[str]:
    if isinstance(v, str):
        v = v.split(",")
    return [str(a).strip() for a in (v or []) if str(a).strip()]


def _send_email(msg: dict, ecfg: dict, transport=None) -> tuple[str, str]:
    sender = str(ecfg.get("from") or "").strip()
    to = _addresses(ecfg.get("to"))
    host = str(ecfg.get("smtp_host") or "").strip()
    user_env = str(ecfg.get("username_env") or "ROP_SMTP_USERNAME")
    pw_env = str(ecfg.get("password_env") or "ROP_SMTP_PASSWORD")
    user = os.environ.get(user_env, "")
    pw = os.environ.get(pw_env, "")
    factory = transport.get("smtp_factory") if isinstance(transport, dict) else None
    msg_transport = _pick(transport, "email")
    if not sender or not to:
        return "failed", "email: notify.email.from 과 notify.email.to 를 채워야 한다"
    if msg_transport is None and not host:
        return "failed", "email: notify.email.smtp_host 가 비어 있다"
    if bool(user) != bool(pw):
        return "failed", f"email: 환경변수 {user_env}·{pw_env} 는 둘 다 채우거나 둘 다 비워야 한다"
    try:
        em = EmailMessage()
        em["Subject"] = msg["subject"]
        em["From"] = sender
        em["To"] = ", ".join(to)
        em["Date"] = formatdate(localtime=True)
        em["Message-ID"] = make_msgid(domain=sender.rsplit("@", 1)[-1] if "@" in sender else "rop-wiki.local")
        em.set_content(msg["text"])
        if msg_transport is not None:
            msg_transport(em)
            return "sent", f"email: {len(to)}명에게 전송(주입된 전송 함수)"
        port = int(ecfg.get("smtp_port") or 587)
        timeout = float(ecfg.get("timeout_sec") or 20)
        use_ssl = _truthy(ecfg.get("use_ssl"))
        use_tls = _truthy(ecfg.get("use_tls", True))
        ctx = ssl.create_default_context()
        if factory is None:
            factory = smtplib.SMTP_SSL if use_ssl else smtplib.SMTP
        smtp = factory(host, port, timeout=timeout, context=ctx) if use_ssl else factory(host, port, timeout=timeout)
        try:
            if use_tls and not use_ssl:
                smtp.starttls(context=ctx)
            if user and pw:
                smtp.login(user, pw)
            smtp.send_message(em)
        finally:
            try:
                smtp.quit()
            except Exception:
                pass
        return "sent", f"email: {host}:{port} 로 {len(to)}명에게 전송"
    except Exception as e:
        return "failed", _mask(f"email: {type(e).__name__}: {e}", [pw, user])


def send(summary: dict, daily_log_rel: str, cfg: dict | None = None, transport=None) -> dict:
    """알림을 보낸다. 반환 {"status": disabled|skipped|sent|failed, "detail": 설명}. 예외를 내보내지 않는다."""
    try:
        n = _notify_section(cfg)
        if not _truthy(n.get("enabled")):
            return {"status": "disabled", "detail": "notify.enabled: false — 발송하지 않았다(네트워크 사용 없음)"}
        channel = str(n.get("channel") or "none").strip()
        if channel not in CHANNELS:
            return {"status": "failed", "detail": f"notify.channel 값 오류: {channel!r} (가능: {', '.join(CHANNELS)})"}
        if channel == "none":
            return {"status": "skipped", "detail": "notify.channel: none"}
        ev = event_of(summary or {})
        on = n.get("on")
        on = [str(x) for x in on] if isinstance(on, list) else list(EVENTS)
        if ev not in on:
            return {"status": "skipped", "detail": f"결과 {ev} 는 notify.on({', '.join(on)})에 없다"}
        msg = build_message(summary or {}, daily_log_rel, site_url=n.get("site_url"))
        results: list[tuple[str, str]] = []
        if channel in ("slack_webhook", "both"):
            results.append(_send_slack(msg, n.get("slack") or {}, _pick(transport, "slack")))
        if channel in ("email", "both"):
            results.append(_send_email(msg, n.get("email") or {}, transport))
        status = "sent" if all(s == "sent" for s, _ in results) else "failed"
        return {"status": status, "detail": f"[{ev}] " + "; ".join(d for _, d in results)}
    except Exception as e:  # 알림 실패가 게시를 되돌리지 않게 한다
        return {"status": "failed", "detail": f"알림 처리 중 예외: {type(e).__name__}: {e}"}


# --- CLI ----------------------------------------------------------------------------------------

def _mock_transports(out) -> dict:
    def slack(url, body):
        shown = re.sub(r"(https://[^/]+/).*", r"\1***", url)
        out(f"[notify] slack 모의 전송 → POST {shown}\n{json.dumps(json.loads(body), ensure_ascii=False, indent=2)}")
        return 200

    def email(msg):
        out("[notify] email 모의 전송 →\n" + "\n".join(f"{k}: {v}" for k, v in msg.items() if k in ("Subject", "From", "To"))
            + "\n\n" + msg.get_content())

    return {"slack": slack, "email": email}


def _load_summary(run_id: str) -> tuple[dict, str]:
    for d in (ROOT / "runs" / run_id, ROOT / "runs" / "parked" / run_id):
        p = d / "summary.json"
        if p.is_file():
            s = json.loads(p.read_text(encoding="utf-8"))
            return s, f"docs/logs/daily/{s.get('date') or run_id[:10]}.md"
    raise SystemExit(f"[notify] summary.json 이 없다: runs/{run_id}/ 또는 runs/parked/{run_id}/")


def _crontab_has_block() -> str:
    try:
        p = subprocess.run(["crontab", "-l"], capture_output=True, text=True, timeout=10)
    except Exception:
        return "확인 불가(crontab 명령 없음)"
    return "등록됨" if re.search(r"^# rop-wiki:begin", p.stdout or "", re.M) else "등록 안 됨"


def _status() -> str:
    ops = load_ops()
    n, d, c = ops["notify"], ops["deploy"], ops["cron"]
    def env(name) -> str:
        return "설정됨" if os.environ.get(str(name or ""), "") else "비어 있음"
    lines = [f"[ops] 설정 파일: {ops_path()}" + (f" — {ops['_error']}" if ops.get("_error") else "")]
    lines.append(f"- 알림: enabled={_fmt_value(_truthy(n['enabled']))} channel={n['channel']} on={','.join(map(str, n.get('on') or []))}"
                 f" · {n['slack']['webhook_url_env']}={env(n['slack']['webhook_url_env'])}"
                 f" · SMTP {n['email'].get('smtp_host') or '(호스트 없음)'} · {n['email']['password_env']}={env(n['email']['password_env'])}")
    lines.append(f"- 원격 배포: enabled={_fmt_value(_truthy(d['enabled']))} method={d['method']} "
                 f"({d['remote_name']}/{d['remote_branch']}) after_daily_run={_fmt_value(_truthy(d.get('after_daily_run')))}")
    lines.append(f"- cron: enabled={_fmt_value(_truthy(c['enabled']))} tz_mode={c['tz_mode']} · crontab {_crontab_has_block()}"
                 f" · 환경 파일 {c['env_file']} {'있음' if Path(os.path.expanduser(str(c['env_file']))).is_file() else '없음'}")
    try:
        import yaml
        legacy = (yaml.safe_load(SETTINGS_FILE.read_text(encoding="utf-8")) or {}).get("notify")
        if legacy and str(legacy) != "none" and str(legacy) != str(n["channel"]):
            lines.append(f"  참고: settings.yaml 의 notify={legacy} 는 사양서 0장 원문 값이다. 발송 채널은 ops.yaml notify.channel({n['channel']})을 따른다")
    except Exception:
        pass
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="ROP 위키 실행 결과 알림·운영 설정(config/ops.yaml)")
    ap.add_argument("--test", action="store_true", help="시험 메시지(표본 요약)를 만든다")
    ap.add_argument("--mock", action="store_true", help="네트워크 없이 모의 전송 내용을 출력한다(enabled 무시)")
    ap.add_argument("--force", action="store_true", help="notify.enabled: false 여도 실제로 보낸다(--test/--run-id)")
    ap.add_argument("--run-id", help="runs/<run_id>/summary.json 으로 알림")
    ap.add_argument("--channel", choices=CHANNELS, help="채널 덮어쓰기(--test/--run-id) 또는 --enable notify 의 채널")
    ap.add_argument("--method", choices=DEPLOY_METHODS, help="--enable deploy 의 배포 방식(deploy.method)")
    ap.add_argument("--status", action="store_true", help="운영 스위치 현황")
    ap.add_argument("--get", metavar="KEY", help="ops.yaml 값 읽기(점 표기, 예 cron.enabled)")
    ap.add_argument("--default", default="", help="--get 의 값이 없을 때 출력할 값")
    ap.add_argument("--enable", choices=SWITCHES, help="ops.yaml 의 <이름>.enabled 를 true 로")
    ap.add_argument("--disable", choices=SWITCHES, help="ops.yaml 의 <이름>.enabled 를 false 로")
    a = ap.parse_args(argv)

    if a.get:
        v = get_value(a.get, None)
        print(a.default if v is None else _fmt_value(v))
        return 0
    if a.enable or a.disable:
        try:
            print("[ops] " + set_switch(a.enable or a.disable, bool(a.enable), a.channel if a.enable else None,
                                        method=a.method if a.enable else None))
        except (ValueError, OSError) as e:
            print(f"[ops] 실패: {e}", file=sys.stderr)
            return 2
        if a.enable == "cron":
            print("[ops] 다음: bash pipeline/install_cron.sh  (먼저 --dry-run 으로 볼 수 있다)")
        elif a.disable == "cron":
            print("[ops] 이미 등록된 블록은 bash pipeline/uninstall_cron.sh 로 지운다")
        elif a.enable == "notify":
            print("[ops] 비밀값은 환경변수로 준다(cron 은 ~/.config/rop-wiki/env). 확인: python3 pipeline/lib/notify.py --test --mock")
        elif a.enable == "deploy":
            print("[ops] 방식(deploy.method)과 GitHub 저장소 설정은 deploy/README.md 를 따른다. 실행: bash pipeline/deploy_site.sh --yes")
        return 0
    if a.status:
        print(_status())
        return 0
    if not (a.test or a.run_id):
        ap.print_help()
        return 2

    if a.run_id:
        summary, rel = _load_summary(a.run_id)
    else:
        summary, rel = copy.deepcopy(SAMPLE_SUMMARY), f"docs/logs/daily/{SAMPLE_SUMMARY['date']}.md"
    ops = load_ops()
    n = ops["notify"]
    if ops.get("_error"):
        print(f"[notify] 경고: {ops['_error']}")
    if a.test:   # 실제 채널로 보내도 시험 메시지임을 알 수 있게 실행 id 앞에 표시한다
        summary = dict(summary, run_id=f"[시험] {summary.get('run_id') or ''}".strip())
    msg = build_message(summary, rel, site_url=n.get("site_url"))
    print(f"[notify] 제목: {msg['subject']}\n[notify] 본문:\n{msg['text']}\n")

    transport = None
    if a.mock or a.force:
        n = copy.deepcopy(n)
        n["enabled"] = True
    if a.channel:
        n["channel"] = a.channel
    if a.mock:
        transport = _mock_transports(print)
        if n["channel"] == "none":
            n["channel"] = "both"
        n["on"] = list(EVENTS)
        env_name = n["slack"].get("webhook_url_env") or "ROP_SLACK_WEBHOOK_URL"
        if not os.environ.get(env_name):
            os.environ[env_name] = "https://hooks.slack.com/services/MOCK/MOCK/MOCK"   # 이 프로세스 안에서만
        n["email"]["from"] = n["email"].get("from") or "rop-wiki@example.invalid"
        n["email"]["to"] = _addresses(n["email"].get("to")) or ["team@example.invalid"]
    res = send(summary, rel, cfg=n, transport=transport)
    print(f"[notify] 결과: {json.dumps(res, ensure_ascii=False)}" + (" (모의 — 네트워크를 쓰지 않았다)" if a.mock else ""))
    return 1 if res["status"] == "failed" else 0


if __name__ == "__main__":
    sys.exit(main())
