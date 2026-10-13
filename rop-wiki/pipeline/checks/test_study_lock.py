"""스터디 잠금 비밀번호(README 5C) 단위 테스트 — 기본값 반영, 바꾸기 명령, 환경 변수 우선, 빌드 훅의 비밀번호 확정.

실행: python3 -m unittest pipeline/checks/test_study_lock.py
config/ops.yaml 대신 임시 복사본을 ROP_OPS_CONFIG 로 쓰고, mkdocs.yml 은 임시 경로에 쓴다. 실제 설정 파일은 바꾸지 않는다.
"""
from __future__ import annotations

import importlib.util
import os
import sys
import tempfile
import types
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1]
ROOT = PIPELINE.parent
sys.path.insert(0, str(PIPELINE))

from lib import nav, notify  # noqa: E402
import private_pages as pp  # noqa: E402
import study_password as sp  # noqa: E402

ENV_KEYS = ("ROP_STUDY_PASSWORD", "ROP_OPS_CONFIG")


def _load_hook():
    spec = importlib.util.spec_from_file_location("private_pages_hook", PIPELINE / "hooks" / "private_pages.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _fake_config(inventory: dict):
    return types.SimpleNamespace(plugins={"encryptcontent": types.SimpleNamespace(config={"password_inventory": inventory})})


class _EnvCase(unittest.TestCase):
    def setUp(self):
        self._saved = {k: os.environ.get(k) for k in ENV_KEYS}
        for k in ENV_KEYS:
            os.environ.pop(k, None)
        self.tmp = Path(tempfile.mkdtemp(prefix="rop-study-lock-"))

    def tearDown(self):
        for k, v in self._saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v

    def ops_copy(self, text: str | None = None) -> Path:
        p = self.tmp / "ops.yaml"
        p.write_text(text if text is not None else (ROOT / "config" / "ops.yaml").read_text(encoding="utf-8"), encoding="utf-8")
        os.environ["ROP_OPS_CONFIG"] = str(p)
        return p


class TestDefaultInMkdocsYml(_EnvCase):
    def test_real_config_has_default_and_template_uses_it(self):
        default = nav.study_password_default()
        self.assertTrue(default, "config/ops.yaml 의 publish.study_password 가 비어 있다")
        text = nav.render_mkdocs_yml()
        self.assertIn(f"study: !ENV [ROP_STUDY_PASSWORD, {nav.yaml_quote(default)}]", text)
        self.assertIn("threshold_warning_min_entropy: 0", text)
        self.assertIn("hooks:\n  - pipeline/hooks/private_pages.py", text)

    def test_yaml_quote(self):
        self.assertEqual(nav.yaml_quote("2153"), "'2153'")
        self.assertEqual(nav.yaml_quote("a'b"), "'a''b'")
        with self.assertRaises(ValueError):
            nav.yaml_quote("a\nb")


class TestSetPassword(_EnvCase):
    def test_roundtrip_keeps_comments_and_updates_mkdocs(self):
        ops = self.ops_copy()
        before = ops.read_text(encoding="utf-8")
        original = notify.get_value("publish.study_password")
        mk = self.tmp / "mkdocs.yml"
        for value in ['ab"c#d\'e 한글', "x" * sp.MAX_LEN, "p w"]:
            msg = sp.set_password(value, mkdocs_yml=mk)
            self.assertIn(str(ops), msg)
            self.assertEqual(notify.get_value("publish.study_password"), value)
            self.assertIn(f"study: !ENV [ROP_STUDY_PASSWORD, {nav.yaml_quote(value)}]", mk.read_text(encoding="utf-8"))
            # 다른 설정은 그대로다
            self.assertEqual(notify.get_value("publish.logs_public"), notify.load_ops(ops)["publish"]["logs_public"])
        sp.set_password(original, mkdocs_yml=mk)
        self.assertEqual(ops.read_text(encoding="utf-8"), before)      # 주석·열 정렬까지 원상태

    def test_rejects_bad_values_without_touching_files(self):
        ops = self.ops_copy()
        before = ops.read_text(encoding="utf-8")
        mk = self.tmp / "mkdocs.yml"
        for bad in ["", " a", "a ", "a\nb", "a\tb", "y" * (sp.MAX_LEN + 1)]:
            with self.assertRaises(ValueError):
                sp.set_password(bad, mkdocs_yml=mk)
        self.assertEqual(ops.read_text(encoding="utf-8"), before)
        self.assertFalse(mk.exists())

    def test_missing_line_is_reported(self):
        text = (ROOT / "config" / "ops.yaml").read_text(encoding="utf-8")
        lines = [ln for ln in text.splitlines(True) if not ln.startswith("  study_password:")]
        self.ops_copy("".join(lines))
        with self.assertRaises(ValueError) as cm:
            sp.set_password("abc", mkdocs_yml=self.tmp / "mkdocs.yml")
        self.assertIn("study_password", str(cm.exception))

    def test_weakness_and_show(self):
        self.assertIn("10,000", sp.weakness("2153"))
        self.assertIn("8자 미만", sp.weakness("abc"))
        self.assertEqual(sp.weakness("long-enough-pw"), "")
        self.ops_copy()
        out = sp.show()
        self.assertIn("없음(기본값을 쓴다)", out)
        os.environ["ROP_STUDY_PASSWORD"] = "zzz"
        self.assertIn("있음", sp.show())
        self.assertNotIn("zzz", sp.show())                                # 환경 변수 값은 보여 주지 않는다


class TestEffectivePassword(_EnvCase):
    def test_env_then_config(self):
        self.ops_copy()
        default = notify.get_value("publish.study_password")
        self.assertTrue(default)
        self.assertEqual(pp.effective_password(), default)
        os.environ["ROP_STUDY_PASSWORD"] = ""
        self.assertEqual(pp.effective_password(), default)              # 비어 있는 환경 변수는 없는 것과 같다
        os.environ["ROP_STUDY_PASSWORD"] = "9876"
        self.assertEqual(pp.effective_password(), "9876")

    def test_empty_everywhere(self):
        text = (ROOT / "config" / "ops.yaml").read_text(encoding="utf-8")
        self.ops_copy(text.replace('  study_password: "2153"', '  study_password: ""', 1)
                      if '  study_password: "2153"' in text else text)
        ops = notify.load_ops()
        if ops["publish"]["study_password"]:
            self.skipTest("기본값이 2153 이 아니어서 빈 값 사례를 만들지 못했다")
        self.assertEqual(pp.effective_password(), "")


class TestHookOnConfig(_EnvCase):
    def test_runs_before_plugin_and_normalizes_values(self):
        hook = _load_hook()
        self.assertGreater(getattr(hook.on_config, "mkdocs_priority", 0), 0)
        self.ops_copy()
        default = notify.get_value("publish.study_password")
        inv = {"study": 2153, "other": ["a"], "users": {"u": "p"}}      # !ENV 가 숫자를 정수로 읽은 경우
        hook.on_config(_fake_config(inv))
        self.assertEqual(inv, {"study": default, "other": ["a"], "users": {"u": "p"}})
        os.environ["ROP_STUDY_PASSWORD"] = ""
        inv = {"study": ""}                                              # 환경 변수가 있지만 비어 있는 경우
        hook.on_config(_fake_config(inv))
        self.assertEqual(inv["study"], default)
        os.environ["ROP_STUDY_PASSWORD"] = "9876"
        inv = {"study": 9876}
        hook.on_config(_fake_config(inv))
        self.assertEqual(inv["study"], "9876")
        self.assertEqual(hook.on_config(types.SimpleNamespace(plugins={})).plugins, {})   # 플러그인이 없으면 그대로

    def test_no_password_anywhere_stops_build(self):
        hook = _load_hook()
        text = (ROOT / "config" / "ops.yaml").read_text(encoding="utf-8")
        self.ops_copy(text.replace('  study_password: "2153"', '  study_password: ""', 1))
        if notify.load_ops()["publish"]["study_password"]:
            self.skipTest("기본값이 2153 이 아니어서 빈 값 사례를 만들지 못했다")
        with self.assertRaises(ValueError):
            hook.on_config(_fake_config({"study": ""}))


if __name__ == "__main__":
    unittest.main()
