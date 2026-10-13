#!/usr/bin/env python3
"""스터디 잠금 비밀번호 바꾸기 — config/ops.yaml 의 publish.study_password 와 mkdocs.yml 을 함께 고친다(README 5C).

사용:
  python3 pipeline/study_password.py show                 # 현재 기본값, 환경 변수 ROP_STUDY_PASSWORD 유무, mkdocs.yml 일치 여부
  python3 pipeline/study_password.py set <새 비밀번호>      # ops.yaml 의 값을 바꾸고 mkdocs.yml 을 다시 생성한다
  python3 pipeline/study_password.py set                  # 비밀번호를 화면에 보이지 않게 입력받는다

바꾼 뒤 config/ops.yaml 과 mkdocs.yml 을 커밋·푸시하면 main 배포(GitHub Actions)부터 새 비밀번호로 잠긴다. 환경 변수·GitHub
secret ROP_STUDY_PASSWORD 가 비어 있지 않으면 그 값이 이 기본값보다 우선하므로, 그 secret 이 있으면 같이 바꾸거나 지운다.
저장소가 공개이므로 ops.yaml 의 기본값은 누구나 읽을 수 있다. 값은 줄바꿈·제어 문자 없이 128자 이하이며 앞뒤 공백은 둘 수 없다.
시험용으로 다른 설정 파일을 쓰려면 ROP_OPS_CONFIG=<경로> 를 준다.
"""
from __future__ import annotations

import getpass
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import nav, notify  # noqa: E402
from private_pages import ENV  # noqa: E402

KEY = "study_password"
MAX_LEN = 128
# `  study_password: <값>` 줄. 값은 큰따옴표·작은따옴표 스칼라 또는 따옴표 없는 한 단어. 뒤의 주석은 열을 유지한다
_LINE = re.compile(rf'^(  {KEY}:[ \t]*)("(?:[^"\\]|\\.)*"|\'(?:[^\']|\'\')*\'|[^\s#]*)([ \t]*)', re.M)


def validate(value: str) -> str:
    if not isinstance(value, str) or value == "":
        raise ValueError("비밀번호가 비어 있다")
    if any(ord(c) < 32 or ord(c) == 127 for c in value):
        raise ValueError("줄바꿈·탭 같은 제어 문자는 쓸 수 없다")
    if value != value.strip():
        raise ValueError("앞뒤 공백은 쓸 수 없다")
    if len(value) > MAX_LEN:
        raise ValueError(f"{MAX_LEN}자를 넘는다")
    return value


def weakness(value: str) -> str:
    """짧거나 숫자만인 값에 대한 한 줄 경고(없으면 빈 문자열). 막지는 않는다."""
    if value.isdigit():
        return f"숫자만 {len(value)}자 — 경우의 수가 {10 ** len(value):,}가지라 내려받아 추측하면 금방 열린다(README 5C)"
    if len(value) < 8:
        return f"{len(value)}자 — 8자 미만은 추측에 약하다(README 5C)"
    return ""


def set_password(new: str, mkdocs_yml: Path | None = None) -> str:
    """ops.yaml(notify.ops_path(): ROP_OPS_CONFIG 를 따른다)의 publish.study_password 줄만 바꾸고 mkdocs.yml 을 다시 생성한다.
    주석·다른 줄은 그대로 둔다. 결과 설명 문자열을 돌려준다."""
    new = validate(new)
    p = notify.ops_path()
    text = p.read_text(encoding="utf-8")
    sec = re.search(r"^publish:[ \t]*(#.*)?$", text, re.M)
    if not sec:
        raise ValueError(f"{p} 에 'publish:' 절이 없다")
    nxt = re.search(r"^\S", text[sec.end() + 1:], re.M)
    end = sec.end() + 1 + nxt.start() if nxt else len(text)
    body = text[sec.end():end]
    quoted = json.dumps(new, ensure_ascii=False)   # YAML 큰따옴표 스칼라와 호환(" 와 \ 만 이스케이프)
    m = _LINE.search(body)
    if not m:
        raise ValueError(f"{p} 의 'publish:' 절에 '  {KEY}:' 줄이 없다. 한 줄을 넣고 다시 실행한다: {KEY}: \"...\"")
    line_end = body.find("\n", m.end())
    line_end = len(body) if line_end < 0 else line_end
    rest = body[m.end():line_end]                     # 뒤에 붙은 주석(없으면 빈 문자열)
    # 뒤 주석의 열: 바로 다음 줄이 이어지는 주석 줄(공백 + #)이면 그 # 열에 맞추고, 아니면 지금 줄의 # 열을 유지한다
    nm = re.match(r"[ \t]+#", body[line_end + 1:])
    col = (nm.end() - 1) if nm else (m.end(3) - m.start())
    pad = (" " * max(1, col - len(m.group(1)) - len(quoted))) if rest else ""
    body = body[:m.start()] + m.group(1) + quoted + pad + rest + body[line_end:]
    p.write_text(text[:sec.end()] + body + text[end:], encoding="utf-8")
    check = notify.load_ops(p)
    got = (check.get("publish") or {}).get(KEY)
    if check.get("_error") or got != new:
        raise ValueError(f"{p} 수정 뒤 다시 읽은 값이 기대와 다르다: {check.get('_error') or got!r}")

    out = nav.write_mkdocs_yml(mkdocs_yml) if mkdocs_yml else nav.write_mkdocs_yml()
    expect = f"study: !ENV [{ENV}, {nav.yaml_quote(new)}]"
    if expect not in out.read_text(encoding="utf-8"):
        raise ValueError(f"{out} 에 새 기본값이 들어가지 않았다")
    return f"{p}: publish.{KEY} = {quoted}\n{out}: password_inventory.study 기본값 갱신"


def show() -> str:
    p = notify.ops_path()
    current = nav.study_password_default()
    env_set = bool(os.environ.get(ENV, ""))
    lines = [f"기본 비밀번호(config/ops.yaml publish.{KEY}): {json.dumps(current, ensure_ascii=False) if current else '(비어 있음)'}",
             f"환경 변수 {ENV}: {'있음(이 값이 우선한다. 값은 표시하지 않는다)' if env_set else '없음(기본값을 쓴다)'}",
             f"mkdocs.yml: {'설정과 일치' if nav.mkdocs_yml_is_current() else '설정과 다르다 → python3 pipeline/study_password.py set 또는 python3 pipeline/scaffold.py --refresh-auto'}",
             f"설정 파일: {p}"]
    if not current and not env_set:
        lines.append("경고: 비밀번호가 없어 빌드가 멈춘다. set 으로 기본값을 두거나 환경 변수를 준다")
    w = weakness(current) if current else ""
    if w:
        lines.append(f"참고: {w}")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in ("show", "set") or (argv[0] == "show" and len(argv) != 1) or len(argv) > 2:
        print(__doc__)
        return 2
    if argv[0] == "show":
        print(show())
        return 0
    if len(argv) == 2:
        new = argv[1]
    else:
        new = getpass.getpass("새 비밀번호: ")
        if new != getpass.getpass("다시 입력: "):
            print("두 입력이 다르다", file=sys.stderr)
            return 2
    try:
        msg = set_password(new)
    except ValueError as e:
        print(f"바꾸지 않았다: {e}", file=sys.stderr)
        return 2
    print(msg)
    w = weakness(new)
    if w:
        print(f"참고: {w}")
    print("다음: git add config/ops.yaml mkdocs.yml && git commit -m \"rop-wiki: 스터디 비밀번호 변경\" && git push\n"
          f"      main 에 들어가면 GitHub Actions 가 다시 배포한다. secret {ENV} 가 있으면 그 값이 우선하므로 같이 바꾸거나 지운다.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
