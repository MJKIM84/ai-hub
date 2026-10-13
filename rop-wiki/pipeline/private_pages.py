#!/usr/bin/env python3
"""비공개 원문 페이지 — 저장소에는 암호문만 두고, 빌드 때 ROP_STUDY_PASSWORD 로 복호화해 본문에 넣는다.

저장소와 사이트가 공개이므로, 원문 그대로 실어야 하는 페이지(스터디 › ROP 발표회)는 마크다운 본문을 이 모듈로
암호화해 `_private/<slug>.md.enc` 로 커밋한다. docs/ 에는 프런트매터·이동 경로·제목만 있는 틀 페이지를 두고,
mkdocs 빌드 때 훅(pipeline/hooks/private_pages.py)이 틀 페이지의 표시 자리에 복호화한 본문을 끼워 넣는다. 그 뒤
mkdocs-encryptcontent-plugin 이 같은 비밀번호로 HTML 을 다시 암호화하므로, 사이트 방문자도 비밀번호를 넣어야 본문을 본다.
비밀번호는 환경 변수로만 받는다(인수·파일·로그에 두지 않는다).

사용:
  ROP_STUDY_PASSWORD=… python3 pipeline/private_pages.py encrypt <원문.md> _private/<slug>.md.enc
  ROP_STUDY_PASSWORD=… python3 pipeline/private_pages.py check   _private/<slug>.md.enc   # 복호화 가능 여부만 확인
  ROP_STUDY_PASSWORD=… python3 pipeline/private_pages.py decrypt _private/<slug>.md.enc   # 본문을 표준 출력으로

형식: AES-256-GCM, 키는 scrypt(N=2^15, r=8, p=1, 32바이트). JSON 한 파일에 salt·nonce·tag·ciphertext 를 base64 로 담는다.
"""
from __future__ import annotations

import base64
import json
import os
import sys
from pathlib import Path

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes

ENV = "ROP_STUDY_PASSWORD"
FORMAT = "rop-private-page/1"
MARKER = "<!-- private-source -->"   # 틀 페이지에서 복호화한 본문이 들어갈 자리
NOTICE = ("> 이 페이지의 본문은 저장소에 암호화되어 있으며, `ROP_STUDY_PASSWORD` 환경 변수가 있는 빌드에서만 포함된다. "
          "이 빌드에는 비밀번호가 없어 본문을 비워 두었다.")
_KDF = {"N": 2 ** 15, "r": 8, "p": 1}


def _b64(b: bytes) -> str:
    return base64.b64encode(b).decode("ascii")


def _unb64(s: str) -> bytes:
    return base64.b64decode(s.encode("ascii"))


def encrypt(text: str, password: str) -> str:
    if not password:
        raise ValueError("비밀번호가 비어 있다")
    salt = get_random_bytes(16)
    key = scrypt(password.encode("utf-8"), salt, 32, **_KDF)
    cipher = AES.new(key, AES.MODE_GCM, nonce=get_random_bytes(12))
    ct, tag = cipher.encrypt_and_digest(text.encode("utf-8"))
    return json.dumps({"format": FORMAT, "kdf": "scrypt", **_KDF, "salt": _b64(salt), "nonce": _b64(cipher.nonce),
                       "tag": _b64(tag), "ciphertext": _b64(ct)}, indent=1) + "\n"


def decrypt(blob: str, password: str) -> str:
    data = json.loads(blob)
    if data.get("format") != FORMAT or data.get("kdf") != "scrypt":
        raise ValueError("알 수 없는 암호문 형식")
    key = scrypt(password.encode("utf-8"), _unb64(data["salt"]), 32, N=int(data["N"]), r=int(data["r"]), p=int(data["p"]))
    cipher = AES.new(key, AES.MODE_GCM, nonce=_unb64(data["nonce"]))
    try:
        return cipher.decrypt_and_verify(_unb64(data["ciphertext"]), _unb64(data["tag"])).decode("utf-8")
    except ValueError as e:
        raise ValueError("복호화 실패: 비밀번호가 다르거나 암호문이 손상됐다") from e


def password_from_env() -> str:
    pw = os.environ.get(ENV, "")
    if not pw:
        sys.exit(f"환경 변수 {ENV} 가 없다. 비밀번호는 환경 변수로만 넘긴다.")
    return pw


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[0] not in ("encrypt", "check", "decrypt"):
        print(__doc__)
        return 2
    cmd = argv[0]
    if cmd == "encrypt":
        if len(argv) != 3:
            return 2
        src, dst = Path(argv[1]), Path(argv[2])
        text = src.read_text(encoding="utf-8")
        pw = password_from_env()
        blob = encrypt(text, pw)
        assert decrypt(blob, pw) == text
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(blob, encoding="utf-8")
        print(f"암호화: {src} → {dst} ({len(text):,}자, 복호화 확인)")
        return 0
    blob = Path(argv[1]).read_text(encoding="utf-8")
    text = decrypt(blob, password_from_env())
    if cmd == "check":
        print(f"복호화 가능: {argv[1]} ({len(text):,}자)")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
