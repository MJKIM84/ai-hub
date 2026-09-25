"""운영(알림·사이트 배포·cron) 단위 테스트.

실행: python3 -m unittest pipeline/checks/test_ops.py   (위키 루트에서)

실제 crontab·네트워크·원격 저장소를 건드리지 않는다. crontab·mkdocs·git 은 임시 PATH 의 가짜 명령으로 바꾸고,
config/ops.yaml 대신 환경변수 ROP_OPS_CONFIG 로 임시 설정 파일을 쓰며, 발송은 주입한 가짜 전송 함수로 받는다.
"""
from __future__ import annotations

import copy
import fcntl
import json
import os
import smtplib
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from unittest import mock
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib import notify  # noqa: E402
from lib import runs  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
PIPELINE = ROOT / "pipeline"
WEBHOOK = "https://hooks.slack.com/services/T000/B000/SECRETTOKEN"

PUBLISHED = {
    "run_id": "2026-09-25-01", "date": "2026-09-25", "run_type": "area_deep_dive",
    "target": {"area_no": 7, "area_name": "7. 화물·재고·자산 식별과 추적", "category": "B. 공통 정보·환경 모델"},
    "end_state": "게시 완료", "published": True, "parked": False, "pages_created": 1, "pages_updated": 2,
}
PARKED = {
    "run_id": "2026-09-26-01", "date": "2026-09-26", "run_type": "track",
    "target": {"area_no": 5, "area_name": "5. 로봇 능력·자원 모델", "slug": "manual-capability-ontology", "stage": 1,
               "question_ids": ["q1-03"]},
    "end_state": "보류(runs/parked/)", "published": False, "parked": True, "park_reason": "1차 검증 반려가 재조사 2회 뒤에도 이어짐",
    "pages_created": 0, "pages_updated": 0,
}
FAILED = {"run_id": "2026-09-27-01", "date": "2026-09-27", "run_type": None, "target": {},
          "end_state": "중단(웹 검색(WebSearch) 도구를 쓸 수 없다)", "published": False, "parked": False}
LOG_REL = "docs/logs/daily/2026-09-25.md"


def ncfg(**over) -> dict:
    """notify 절 설정(기본: 켜짐, 슬랙)."""
    base = copy.deepcopy(notify.DEFAULTS["notify"])
    base.update({"enabled": True, "channel": "slack_webhook"})
    for k, v in over.items():
        if isinstance(v, dict) and isinstance(base.get(k), dict):
            base[k].update(v)
        else:
            base[k] = v
    return base


EMAIL_CFG = {"smtp_host": "smtp.example.invalid", "smtp_port": 587, "use_tls": True, "from": "bot@example.invalid",
             "to": ["a@example.invalid", "b@example.invalid"]}


class TestNotifyMessage(unittest.TestCase):
    def test_message_contains_run_id_state_and_fields(self):
        m = notify.build_message(PUBLISHED, LOG_REL)
        self.assertIn("2026-09-25-01", m["subject"])
        self.assertIn("게시", m["subject"])
        for s in ("실행 id: 2026-09-25-01", "유형: 영역 심화", "대상: 7. 화물·재고·자산 식별과 추적", "종료 상태: 게시 완료",
                  "생성 1 / 갱신 2", f"로그: {LOG_REL}"):
            self.assertIn(s, m["text"])
        self.assertNotIn("비용", m["text"])          # 요약에 비용이 없으면 줄을 두지 않는다

    def test_cost_variants(self):
        for extra, want in (({"cost_usd": 14.6234}, "$14.62"), ({"total_cost_usd": 3}, "$3.00"),
                            ({"cost": {"total_usd": 1.5}}, "$1.50"), ({"costs": {"total": 2.25}}, "$2.25")):
            self.assertIn(f"비용 합계: {want}", notify.build_message({**PUBLISHED, **extra}, LOG_REL)["text"], extra)
        self.assertIsNone(notify.cost_of({"cost_usd": True}))   # bool 은 비용으로 보지 않는다

    def test_parked_track_and_failed(self):
        m = notify.build_message(PARKED, "docs/logs/daily/2026-09-26.md")
        self.assertIn("보류", m["subject"])
        self.assertIn("트랙 manual-capability-ontology · 단계 1 · 질문 q1-03", m["text"])
        self.assertIn("보류 사유: 1차 검증 반려", m["text"])
        f = notify.build_message(FAILED, "docs/logs/daily/2026-09-27.md")
        self.assertIn("실패", f["subject"])
        self.assertIn("미선정", f["text"])
        self.assertIn("종료 상태: 중단(웹 검색", f["text"])

    def test_event_of(self):
        self.assertEqual(notify.event_of(PUBLISHED), "published")
        self.assertEqual(notify.event_of(PARKED), "parked")
        self.assertEqual(notify.event_of({**PARKED, "parked": False}), "parked")   # end_state 가 "보류…"
        self.assertEqual(notify.event_of(FAILED), "failed")

    def test_site_link(self):
        m = notify.build_message(PUBLISHED, LOG_REL, site_url="https://example.github.io/ai-hub/")
        self.assertIn("사이트: https://example.github.io/ai-hub/logs/daily/2026-09-25/", m["text"])

    def test_run_type_labels_follow_runs(self):
        for rt, label in runs.RUN_TYPE_KO.items():          # runs.py 에 실행 유형이 늘어도 같은 이름을 쓴다
            self.assertEqual(notify.run_type_label(rt), label)
        self.assertEqual(notify.run_type_label(None), "미선정")


class TestNotifySend(unittest.TestCase):
    def setUp(self):
        self.env = mock.patch.dict(os.environ, {"ROP_SLACK_WEBHOOK_URL": WEBHOOK, "ROP_SMTP_USERNAME": "bot-user",
                                                "ROP_SMTP_PASSWORD": "p@ssw0rd-secret"})
        self.env.start()
        # 기본 전송 경로(urllib·smtplib)를 쓰면 실패하게 막는다 — 주입한 전송 함수만 쓰여야 한다
        self.urlopen = mock.patch("lib.notify.urllib.request.urlopen", side_effect=AssertionError("네트워크 사용"))
        self.smtp = mock.patch("lib.notify.smtplib.SMTP", side_effect=AssertionError("SMTP 사용"))
        self.urlopen.start()
        self.smtp.start()

    def tearDown(self):
        self.urlopen.stop()
        self.smtp.stop()
        self.env.stop()

    def test_disabled_does_not_touch_transport(self):
        t = mock.Mock(side_effect=AssertionError("호출되면 안 된다"))
        r = notify.send(PUBLISHED, LOG_REL, cfg=ncfg(enabled=False, channel="both"), transport={"slack": t, "email": t})
        self.assertEqual(r["status"], "disabled")
        t.assert_not_called()
        # 전체 ops dict 형태도 받는다
        r2 = notify.send(PUBLISHED, LOG_REL, cfg={"notify": ncfg(enabled=False)}, transport=t)
        self.assertEqual(r2["status"], "disabled")

    def test_default_config_is_off(self):
        for sec in ("notify", "deploy", "cron"):
            self.assertIs(notify.DEFAULTS[sec]["enabled"], False, sec)
        missing = notify.load_ops(ROOT / "no-such-ops.yaml")
        self.assertIn("_error", missing)
        self.assertEqual(notify.send(PUBLISHED, LOG_REL, cfg=missing)["status"], "disabled")

    def test_ops_yaml_parses(self):
        ops = notify.load_ops(ROOT / "config" / "ops.yaml")
        self.assertNotIn("_error", ops)
        for key in ("notify.enabled", "notify.channel", "notify.on", "notify.slack.webhook_url_env", "notify.email.smtp_host",
                    "notify.email.password_env", "deploy.enabled", "deploy.method", "cron.enabled", "cron.lock_file"):
            self.assertIsNotNone(notify.get_value(key, None, ROOT / "config" / "ops.yaml"), key)
        self.assertIn(ops["notify"]["channel"], notify.CHANNELS)

    def test_skipped_channel_none_and_event_filter(self):
        t = mock.Mock()
        self.assertEqual(notify.send(PUBLISHED, LOG_REL, cfg=ncfg(channel="none"), transport=t)["status"], "skipped")
        self.assertEqual(notify.send(PUBLISHED, LOG_REL, cfg=ncfg(on=["failed", "parked"]), transport=t)["status"], "skipped")
        t.assert_not_called()
        self.assertEqual(notify.send(PUBLISHED, LOG_REL, cfg=ncfg(channel="sms"), transport=t)["status"], "failed")

    def test_slack_mock_payload(self):
        calls = []
        r = notify.send(PUBLISHED, LOG_REL, cfg=ncfg(), transport=lambda url, body: calls.append((url, body)) or 200)
        self.assertEqual(r["status"], "sent", r)
        self.assertEqual(len(calls), 1)
        url, body = calls[0]
        self.assertEqual(url, WEBHOOK)
        payload = json.loads(body.decode("utf-8"))
        self.assertEqual(set(payload), {"text"})
        self.assertIn("2026-09-25-01", payload["text"])
        self.assertIn("게시 완료", payload["text"])
        self.assertNotIn("SECRETTOKEN", r["detail"])

    def test_slack_missing_env_and_non_https(self):
        with mock.patch.dict(os.environ, {"ROP_SLACK_WEBHOOK_URL": ""}):
            r = notify.send(PUBLISHED, LOG_REL, cfg=ncfg(), transport=mock.Mock())
        self.assertEqual(r["status"], "failed")
        self.assertIn("ROP_SLACK_WEBHOOK_URL", r["detail"])
        with mock.patch.dict(os.environ, {"ROP_SLACK_WEBHOOK_URL": "http://insecure.example/hook"}):
            self.assertEqual(notify.send(PUBLISHED, LOG_REL, cfg=ncfg(), transport=mock.Mock())["status"], "failed")

    def test_slack_http_error_status(self):
        r = notify.send(PUBLISHED, LOG_REL, cfg=ncfg(), transport=lambda url, body: 404)
        self.assertEqual(r["status"], "failed")
        self.assertIn("404", r["detail"])

    def test_failed_transport_returns_failed_not_exception(self):
        def boom(url, body):
            raise OSError(f"connection refused to {url}")
        r = notify.send(PUBLISHED, LOG_REL, cfg=ncfg(), transport=boom)
        self.assertEqual(r["status"], "failed")
        self.assertIn("OSError", r["detail"])
        self.assertNotIn("SECRETTOKEN", r["detail"])      # 오류 문구의 웹훅 URL 은 가린다

        def smtp_boom(msg):
            raise smtplib.SMTPException("mailbox unavailable")
        r2 = notify.send(PUBLISHED, LOG_REL, cfg=ncfg(channel="email", email=EMAIL_CFG), transport=smtp_boom)
        self.assertEqual(r2["status"], "failed")
        self.assertIn("SMTPException", r2["detail"])
        # 요약이 망가져도 예외를 내보내지 않는다
        self.assertEqual(notify.send(None, LOG_REL, cfg=ncfg(), transport=lambda u, b: 200)["status"], "sent")
        self.assertEqual(notify.send({"target": "not-a-dict"}, LOG_REL, cfg=ncfg(), transport=lambda u, b: 200)["status"], "failed")

    def test_email_mock_message_fields(self):
        sent = []
        r = notify.send(PARKED, "docs/logs/daily/2026-09-26.md", cfg=ncfg(channel="email", email=EMAIL_CFG), transport=sent.append)
        self.assertEqual(r["status"], "sent", r)
        msg = sent[0]
        self.assertEqual(msg["From"], "bot@example.invalid")
        self.assertEqual(msg["To"], "a@example.invalid, b@example.invalid")
        self.assertIn("2026-09-26-01", msg["Subject"])
        self.assertIn("보류", msg["Subject"])
        self.assertTrue(msg["Date"] and msg["Message-ID"])
        self.assertEqual(msg.get_content_charset(), "utf-8")
        body = msg.get_content()
        self.assertIn("실행 id: 2026-09-26-01", body)
        self.assertIn("종료 상태: 보류", body)

    def test_email_smtp_factory_starttls_login(self):
        calls = []

        class FakeSMTP:
            def __init__(self, host, port, timeout=None, **kw):
                calls.append(("init", host, port))

            def starttls(self, context=None):
                calls.append(("starttls",))

            def login(self, user, pw):
                calls.append(("login", user, pw))

            def send_message(self, msg):
                calls.append(("send", msg["To"]))

            def quit(self):
                calls.append(("quit",))

        r = notify.send(PUBLISHED, LOG_REL, cfg=ncfg(channel="email", email=EMAIL_CFG), transport={"smtp_factory": FakeSMTP})
        self.assertEqual(r["status"], "sent", r)
        self.assertEqual([c[0] for c in calls], ["init", "starttls", "login", "send", "quit"])
        self.assertEqual(calls[0][1:], ("smtp.example.invalid", 587))
        self.assertEqual(calls[2][1:], ("bot-user", "p@ssw0rd-secret"))   # 비밀번호는 환경변수에서
        self.assertNotIn("p@ssw0rd-secret", r["detail"])

        class AuthFail(FakeSMTP):
            def login(self, user, pw):
                raise smtplib.SMTPAuthenticationError(535, f"bad credentials for {user} {pw}".encode())
        r2 = notify.send(PUBLISHED, LOG_REL, cfg=ncfg(channel="email", email=EMAIL_CFG), transport={"smtp_factory": AuthFail})
        self.assertEqual(r2["status"], "failed")
        self.assertNotIn("p@ssw0rd-secret", r2["detail"])

    def test_email_config_errors(self):
        self.assertEqual(notify.send(PUBLISHED, LOG_REL, cfg=ncfg(channel="email"), transport=mock.Mock())["status"], "failed")
        with mock.patch.dict(os.environ, {"ROP_SMTP_PASSWORD": ""}):
            r = notify.send(PUBLISHED, LOG_REL, cfg=ncfg(channel="email", email=EMAIL_CFG), transport={"smtp_factory": mock.Mock()})
        self.assertEqual(r["status"], "failed")
        self.assertIn("둘 다", r["detail"])

    def test_both_channels_partial_failure(self):
        got = []

        def email_fail(msg):
            raise ConnectionError("smtp down")
        r = notify.send(PUBLISHED, LOG_REL, cfg=ncfg(channel="both", email=EMAIL_CFG),
                        transport={"slack": lambda u, b: got.append(u) or 200, "email": email_fail})
        self.assertEqual(r["status"], "failed")
        self.assertEqual(got, [WEBHOOK])
        self.assertIn("slack: 웹훅 전송", r["detail"])
        self.assertIn("email: ConnectionError", r["detail"])


def _write(path: Path, text: str, mode: int | None = None) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    if mode is not None:
        path.chmod(mode)
    return path


class ShellCase(unittest.TestCase):
    """가짜 명령(crontab, mkdocs, git)과 임시 ops.yaml 로 셸 스크립트를 실행한다."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.bin = self.tmp / "bin"
        self.crontab_file = self.tmp / "crontab.txt"
        self.mkdocs_log = self.tmp / "mkdocs.log"
        _write(self.bin / "crontab", """#!/bin/bash
f="$FAKE_CRONTAB_FILE"; echo "$*" >> "$f.calls"
case "$1" in
  -l) if [ -f "$f" ]; then cat "$f"; else echo "no crontab for $(id -un)" >&2; exit 1; fi;;
  -r) rm -f "$f";;
  -) cat > "$f";;
  *) exit 2;;
esac
""", 0o755)
        _write(self.bin / "mkdocs", """#!/bin/bash
echo "$*" >> "$FAKE_MKDOCS_LOG"
if [ "$1" = build ] && [ "${FAKE_MKDOCS_FAIL_BUILD:-0}" = 1 ]; then exit 1; fi
exit 0
""", 0o755)
        _write(self.bin / "git", '#!/bin/bash\necho "https://example.invalid/repo.git"\n', 0o755)
        self.ops_file = self.tmp / "ops.yaml"
        self.write_ops()

    def tearDown(self):
        self._tmp.cleanup()

    def write_ops(self, **sections):
        ops = copy.deepcopy(notify.DEFAULTS)
        ops["cron"].update({"lock_file": str(self.tmp / "run.lock"), "log_file": str(self.tmp / "cron.log")})
        for sec, vals in sections.items():
            ops[sec].update(vals)
        self.ops_file.write_text(json.dumps(ops, ensure_ascii=False), encoding="utf-8")   # JSON 은 YAML 이다

    def env(self, **extra) -> dict:
        e = dict(os.environ)
        e.update({"PATH": f"{self.bin}:{os.environ.get('PATH', '/usr/bin:/bin')}", "ROP_OPS_CONFIG": str(self.ops_file),
                  "FAKE_CRONTAB_FILE": str(self.crontab_file), "FAKE_MKDOCS_LOG": str(self.mkdocs_log),
                  "ROP_ENV_FILE": str(self.tmp / "no-env-file"), "ROP_CRON_LOG": str(self.tmp / "cron.log")})
        e.update(extra)
        return e

    def sh(self, script: str, *args, env=None, timeout=60) -> subprocess.CompletedProcess:
        return subprocess.run(["bash", str(PIPELINE / script), *args], cwd=str(ROOT), env=env or self.env(),
                              capture_output=True, text=True, timeout=timeout)


def _run_time() -> tuple[int, int, str]:
    s = runs.load_settings()
    rt = str(s.get("run_time") or "06:00 Asia/Seoul")
    clock, _, tz = rt.partition(" ")
    h, m = clock.split(":")
    return int(h), int(m), tz or str(s.get("timezone") or "Asia/Seoul")


class TestInstallCron(ShellCase):
    def test_dry_run_block_has_cron_tz_flock_and_lock(self):
        p = self.sh("install_cron.sh", "--dry-run", "--tz-mode", "crontz")
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        h, m, tz = _run_time()
        out = p.stdout
        self.assertIn(f"CRON_TZ={tz}", out)
        self.assertRegex(out, r"(?m)^PATH=/")
        lock = str(self.tmp / "run.lock")
        line = next(l for l in out.splitlines() if l.startswith(f"{m} {h} * * * "))
        self.assertIn("flock -n", line)
        self.assertIn(lock, line)
        self.assertIn(str(PIPELINE / "cron_wrapper.sh"), line)
        self.assertIn("--lock-busy", line)
        self.assertIn("# rop-wiki:begin", out)
        self.assertIn("# rop-wiki:end", out)
        self.assertFalse(Path(str(self.crontab_file) + ".calls").exists())   # 미리 보기는 crontab 을 부르지 않는다

    def test_dry_run_real_config_contains_lock_path(self):
        env = self.env()
        env.pop("ROP_OPS_CONFIG")
        p = self.sh("install_cron.sh", "--dry-run", env=env)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertIn("CRON_TZ", p.stdout)
        self.assertIn("flock -n", p.stdout)
        self.assertIn(str(ROOT / "runs" / ".lock"), p.stdout)

    def test_server_tz_mode_converts_schedule(self):
        h, m, tz = _run_time()
        local = datetime.now(ZoneInfo(tz)).replace(hour=h, minute=m).astimezone(ZoneInfo("Etc/UTC"))
        p = self.sh("install_cron.sh", "--dry-run", "--tz-mode", "server", "--server-tz", "Etc/UTC")
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertIn(f"\n{local.minute} {local.hour} * * * ", p.stdout)
        self.assertNotRegex(p.stdout, r"(?m)^CRON_TZ=")          # 지원하지 않는 cron 에는 CRON_TZ 줄을 두지 않는다
        self.assertIn("CRON_TZ 를 쓰지 않는다", p.stdout)

    def test_refuses_when_disabled(self):
        p = self.sh("install_cron.sh")
        self.assertEqual(p.returncode, 3, p.stdout + p.stderr)
        self.assertIn("cron.enabled", p.stdout)
        self.assertFalse(Path(str(self.crontab_file) + ".calls").exists())   # crontab 을 읽지도 쓰지도 않았다

    def test_install_and_uninstall_keep_other_entries(self):
        other = "MAILTO=\"\"\n15 3 * * * /usr/bin/echo other-job\n"
        stale = "# rop-wiki:begin (old)\nCRON_TZ=UTC\n0 1 * * * old-line\n# rop-wiki:end\n"
        self.crontab_file.write_text(stale + other, encoding="utf-8")
        p = self.sh("install_cron.sh", "--force", "--tz-mode", "crontz")          # cron.enabled false 여도 --force 로 등록
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        tab = self.crontab_file.read_text(encoding="utf-8")
        self.assertEqual(tab.count("# rop-wiki:begin"), 1)
        self.assertNotIn("old-line", tab)
        self.assertIn("other-job", tab)
        self.assertTrue(tab.rstrip().endswith("# rop-wiki:end"))                 # 블록은 맨 끝
        self.assertIn("flock -n", tab)
        self.write_ops(cron={"enabled": True})                                    # 스위치를 켜면 --force 없이 등록(교체)
        p2 = self.sh("install_cron.sh", "--tz-mode", "crontz")
        self.assertEqual(p2.returncode, 0, p2.stdout + p2.stderr)
        self.assertEqual(self.crontab_file.read_text(encoding="utf-8").count("# rop-wiki:begin"), 1)
        u = self.sh("uninstall_cron.sh")
        self.assertEqual(u.returncode, 0, u.stdout + u.stderr)
        tab2 = self.crontab_file.read_text(encoding="utf-8")
        self.assertNotIn("rop-wiki", tab2)
        self.assertIn("other-job", tab2)
        self.assertIn("등록된 rop-wiki 블록이 없다", self.sh("uninstall_cron.sh").stdout)


class TestCronWrapper(ShellCase):
    def _stub(self, body: str) -> Path:
        return _write(self.tmp / "stub_run_daily.sh", "#!/bin/bash\n" + body + "\n", 0o755)

    def test_rotation_env_file_and_exit_code(self):
        log = self.tmp / "cron.log"
        log.write_text("old-line\n" * 50, encoding="utf-8")                       # 450B > 100B
        envf = _write(self.tmp / "env", f"ROP_SLACK_WEBHOOK_URL={WEBHOOK}\nROP_TEST_VALUE=s3cr3t-value\n", 0o600)
        stub = self._stub('echo "stub args=$* value_len=${#ROP_TEST_VALUE}"; exit 2')
        p = self.sh("cron_wrapper.sh", "--skip-probe", env=self.env(ROP_CRON_LOG_MAX_BYTES="100", ROP_ENV_FILE=str(envf),
                                                                   ROP_RUN_DAILY=str(stub)))
        self.assertEqual(p.returncode, 2)
        self.assertIn("old-line", (self.tmp / "cron.log.1").read_text(encoding="utf-8"))
        text = log.read_text(encoding="utf-8")
        self.assertNotIn("old-line", text)
        self.assertIn("stub args=--skip-probe value_len=12", text)                 # 환경 파일을 읽었다
        self.assertIn("ROP_SLACK_WEBHOOK_URL", text)                               # 설정 여부만
        self.assertNotIn("SECRETTOKEN", text)
        self.assertNotIn("s3cr3t-value", text)
        self.assertIn("종료 코드 2", text)
        self.assertNotIn("환경 파일 권한", text)

    def test_env_file_permission_warning(self):
        envf = _write(self.tmp / "env", "X=1\n", 0o644)
        p = self.sh("cron_wrapper.sh", env=self.env(ROP_ENV_FILE=str(envf), ROP_RUN_DAILY=str(self._stub("exit 0"))))
        self.assertEqual(p.returncode, 0)
        self.assertIn("환경 파일 권한이 644", (self.tmp / "cron.log").read_text(encoding="utf-8"))

    def test_timeout(self):
        self.write_ops(cron={"max_runtime_sec": 1})
        p = self.sh("cron_wrapper.sh", env=self.env(ROP_RUN_DAILY=str(self._stub("sleep 20"))), timeout=30)
        self.assertEqual(p.returncode, 124)
        self.assertIn("시간 상한", (self.tmp / "cron.log").read_text(encoding="utf-8"))

    def test_deploy_after_run_only_when_enabled(self):
        stub = self._stub("exit 0")
        self.sh("cron_wrapper.sh", env=self.env(ROP_RUN_DAILY=str(stub)))
        self.assertFalse(self.mkdocs_log.exists())                                 # deploy.enabled false → 배포 안 함
        self.write_ops(deploy={"enabled": True})
        p = self.sh("cron_wrapper.sh", env=self.env(ROP_RUN_DAILY=str(stub)))
        self.assertEqual(p.returncode, 0)
        self.assertIn("gh-deploy --force", self.mkdocs_log.read_text(encoding="utf-8"))   # 가짜 mkdocs 가 받았다

    def test_cron_line_skips_when_locked(self):
        p = self.sh("install_cron.sh", "--dry-run", "--tz-mode", "crontz")
        line = next(l for l in p.stdout.splitlines() if "flock -n" in l and not l.startswith("#"))
        cmd = line.split(None, 5)[5]                                               # 시각 5칸을 뗀 명령
        marker = self.tmp / "ran"
        env = self.env(ROP_RUN_DAILY=str(self._stub(f"touch {marker}")))
        lock = self.tmp / "run.lock"
        with open(lock, "w") as fh:
            fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)                          # 앞 실행이 진행 중인 상황
            r = subprocess.run(["/bin/sh", "-c", cmd], env=env, capture_output=True, text=True, timeout=60)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertFalse(marker.exists())
            self.assertIn("건너뜀", (self.tmp / "cron.log").read_text(encoding="utf-8"))
        r2 = subprocess.run(["/bin/sh", "-c", cmd], env=env, capture_output=True, text=True, timeout=60)
        self.assertEqual(r2.returncode, 0, r2.stdout + r2.stderr)
        self.assertTrue(marker.exists())


class TestDeploySite(ShellCase):
    def calls(self) -> str:
        return self.mkdocs_log.read_text(encoding="utf-8") if self.mkdocs_log.exists() else ""

    def test_without_yes_does_not_deploy(self):
        self.write_ops(deploy={"enabled": True})
        p = self.sh("deploy_site.sh")
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertIn("build --strict", self.calls())
        self.assertNotIn("gh-deploy", self.calls())
        self.assertIn("원격 배포하지 않는다", p.stdout)
        self.assertIn("--yes", p.stdout)

    def test_yes_but_disabled_or_actions_does_not_deploy(self):
        p = self.sh("deploy_site.sh", "--yes")
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertIn("deploy.enabled", p.stdout)
        self.write_ops(deploy={"enabled": True, "method": "actions"})
        p2 = self.sh("deploy_site.sh", "--yes")
        self.assertEqual(p2.returncode, 0, p2.stdout + p2.stderr)
        self.assertNotIn("gh-deploy", self.calls())

    def test_enabled_and_yes_runs_gh_deploy(self):
        self.write_ops(deploy={"enabled": True})
        p = self.sh("deploy_site.sh", "--yes")
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertRegex(self.calls(), r"gh-deploy --force --remote-name origin --remote-branch gh-pages")

    def test_build_failure_blocks_deploy(self):
        self.write_ops(deploy={"enabled": True})
        p = self.sh("deploy_site.sh", "--yes", env=self.env(FAKE_MKDOCS_FAIL_BUILD="1"))
        self.assertEqual(p.returncode, 1)
        self.assertNotIn("gh-deploy", self.calls())


class TestNotifyCli(ShellCase):
    def test_test_mock_prints_message(self):
        p = subprocess.run([sys.executable, str(PIPELINE / "lib" / "notify.py"), "--test", "--mock"], cwd=str(ROOT),
                           env=self.env(ROP_SLACK_WEBHOOK_URL=""), capture_output=True, text=True, timeout=60)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertIn("[시험]", p.stdout)
        self.assertIn("slack 모의 전송", p.stdout)
        self.assertIn("email 모의 전송", p.stdout)
        self.assertIn('"status": "sent"', p.stdout)

    def test_get_and_switch_roundtrip(self):
        ops_copy = _write(self.tmp / "ops_copy.yaml", (ROOT / "config" / "ops.yaml").read_text(encoding="utf-8"))
        before = ops_copy.read_text(encoding="utf-8")
        run = lambda *a: subprocess.run([sys.executable, str(PIPELINE / "lib" / "notify.py"), *a], cwd=str(ROOT),  # noqa: E731
                                        env=self.env(ROP_OPS_CONFIG=str(ops_copy)), capture_output=True, text=True, timeout=60)
        self.assertEqual(run("--enable", "cron").returncode, 0)
        self.assertEqual(run("--get", "cron.enabled").stdout.strip(), "true")
        self.assertEqual(run("--enable", "notify", "--channel", "email").returncode, 0)
        self.assertEqual(run("--get", "notify.channel").stdout.strip(), "email")
        self.assertEqual(run("--enable", "cron", "--method", "actions").returncode, 2)   # 잘못된 조합은 거부
        run("--disable", "cron")
        run("--enable", "notify", "--channel", "none")
        run("--disable", "notify")
        self.assertEqual(ops_copy.read_text(encoding="utf-8"), before)                   # 주석·정렬까지 원상태


if __name__ == "__main__":
    unittest.main()
