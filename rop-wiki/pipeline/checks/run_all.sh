#!/usr/bin/env bash
# 모든 검사를 순서대로 실행한다: 프런트매터 → 원문 보호(내비 재생성 일치 포함) → 링크·각주 → 파서 단위 테스트
#   → 라이브러리 단위 테스트 → [ROP_CHECK_URLS=1 이면 참고문헌 URL 열림 확인] → mkdocs build --strict
# 사용: bash pipeline/checks/run_all.sh [--no-build]
#   ROP_CHECK_URLS=1 bash pipeline/checks/run_all.sh   # 외부 접속이 가능한 환경에서 URL 확인까지 실행
#     결과는 data/url_check.json 에 남는다. 그 뒤 `python3 pipeline/scaffold.py --apply-url-check` 를 실행하면
#     열림이 확인된 참고문헌의 신뢰도가 유형 기준값으로 올라간다(원문 미열람 medium 상한 해제).
set -u
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT" || exit 2
fail=0
run() {
  local name="$1"; shift
  echo "== $name"
  if "$@"; then echo "   -> 통과"; else echo "   -> 실패 (exit $?)"; fail=1; fi
  echo
}
run "프런트매터 검사"   python3 pipeline/checks/check_frontmatter.py
run "원문 보호 검사"     python3 pipeline/checks/protect_source.py
run "링크·각주 검사"     python3 pipeline/checks/check_links.py
run "파서 단위 테스트"   python3 -m unittest pipeline/checks/test_source.py
run "라이브러리 단위 테스트" python3 -m unittest pipeline/checks/test_lib.py
# 운영 전환 이후 추가된 테스트(test_pipeline_ops, test_ops, test_sources, test_tracks 등)는 파일이 있으면 모두 돈다
for tf in pipeline/checks/test_*.py; do
  case "$tf" in pipeline/checks/test_source.py|pipeline/checks/test_lib.py) continue;; esac
  run "단위 테스트 $(basename "$tf" .py)" python3 -m unittest "$tf"
done
if [ "${ROP_CHECK_URLS:-0}" = "1" ]; then
  run "참고문헌 URL 열림 확인(선택)" python3 pipeline/checks/check_urls.py --strict --json data/url_check.json
fi
if [ "${1:-}" != "--no-build" ]; then
  run "mkdocs build --strict" mkdocs build --strict
fi
if [ "$fail" -ne 0 ]; then echo "[run_all] 실패한 검사가 있다"; exit 1; fi
echo "[run_all] 모든 검사 통과"
