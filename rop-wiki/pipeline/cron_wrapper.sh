#!/usr/bin/env bash
# ROP 연구 위키 — cron 이 부르는 일일 실행 래퍼. pipeline/install_cron.sh 가 아래 형태로 crontab 에 넣는다:
#   M H * * * /usr/bin/flock -n -E 75 <위키>/runs/.lock /bin/bash <위키>/pipeline/cron_wrapper.sh; [ $? -ne 75 ] || /bin/bash <위키>/pipeline/cron_wrapper.sh --lock-busy
# flock -n 이 잠금을 못 잡으면(앞 실행이 아직 진행 중) 75 로 끝나고, 두 번째 명령이 "건너뜀"만 cron.log 에 남긴다. 잠금은 프로세스가
# 끝나면(비정상 종료 포함) 커널이 풀어 주므로 오래된 잠금 파일을 지울 필요가 없다.
#
# 하는 일(순서):
#   1 로그 크기 순환: cron.log 가 cron.log_max_bytes(기본 5MB)를 넘으면 cron.log.1 로 옮긴다(이전 .1 은 지운다). 이후 출력은 모두 cron.log 로
#   2 환경 파일: cron.env_file(기본 ~/.config/rop-wiki/env)이 있으면 읽는다(set -a). 권한이 600/400 이 아니면 경고. 값은 로그에 쓰지 않는다
#   3 bash pipeline/run_daily.sh "$@" — cron.max_runtime_sec(기본 4시간)를 넘으면 timeout 으로 끝낸다(종료 코드 124)
#   4 정규 실행이 성공(exit 0)하고 deploy.enabled·method=gh-deploy·after_daily_run 이면 bash pipeline/deploy_site.sh --yes
#   5 종료 코드와 뜻을 cron.log 에 남기고 run_daily.sh 의 종료 코드로 끝낸다
# 사용: bash pipeline/cron_wrapper.sh [run_daily.sh 인자…]      (손으로 실행해도 된다. 겹치지 않게 하려면 flock -n runs/.lock 으로 감싼다)
#       bash pipeline/cron_wrapper.sh --lock-busy               (crontab 의 두 번째 명령: 건너뜀 기록만)
# 시험용 환경변수: ROP_OPS_CONFIG(ops.yaml 경로), ROP_CRON_LOG, ROP_CRON_LOG_MAX_BYTES, ROP_ENV_FILE, ROP_RUN_DAILY(run_daily.sh 대신 실행할 스크립트)
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT" || exit 2
PY="${PYTHON:-python3}"
ops() { "$PY" "$ROOT/pipeline/lib/notify.py" --get "$1" --default "${2:-}" 2>/dev/null || printf '%s\n' "${2:-}"; }
abspath() { case "$1" in /*) printf '%s\n' "$1";; "~"|"~/"*) printf '%s\n' "$HOME${1#\~}";; *) printf '%s\n' "$ROOT/$1";; esac; }
ts() { date '+%Y-%m-%d %H:%M:%S %Z'; }

LOG="$(abspath "${ROP_CRON_LOG:-$(ops cron.log_file runs/cron.log)}")"
MAX_BYTES="${ROP_CRON_LOG_MAX_BYTES:-$(ops cron.log_max_bytes 5242880)}"
mkdir -p "$(dirname "$LOG")"

# 1. 로그 순환(크기 기준, 1세대)
size="$(stat -c %s "$LOG" 2>/dev/null || echo 0)"
if [ "${MAX_BYTES:-0}" -gt 0 ] 2>/dev/null && [ "$size" -ge "$MAX_BYTES" ]; then
  mv -f "$LOG" "$LOG.1"
  echo "[cron_wrapper $(ts)] cron.log 순환: 이전 로그(${size}B)를 $(basename "$LOG").1 로 옮겼다" >> "$LOG"
fi
exec >> "$LOG" 2>&1

if [ "${1:-}" = "--lock-busy" ]; then
  echo "[cron_wrapper $(ts)] 건너뜀: 잠금($(ops cron.lock_file runs/.lock))을 잡지 못했다 — 앞 실행이 아직 진행 중이다"
  exit 0
fi

echo
echo "===== [cron_wrapper $(ts)] 일일 실행 시작 (pid $$, $(hostname 2>/dev/null || echo host), 사용자 $(id -un 2>/dev/null || echo '?')) ====="

# 2. 환경 파일(비밀값). 값은 출력하지 않고 알려진 변수의 설정 여부만 남긴다
ENV_FILE="$(abspath "${ROP_ENV_FILE:-$(ops cron.env_file '~/.config/rop-wiki/env')}")"
if [ -f "$ENV_FILE" ]; then
  mode="$(stat -c %a "$ENV_FILE" 2>/dev/null || echo '?')"
  case "$mode" in 600|400) ;; *) echo "[cron_wrapper] 경고: 환경 파일 권한이 $mode 이다. 비밀값이 있으므로 chmod 600 $ENV_FILE";; esac
  set -a
  # shellcheck disable=SC1090
  . "$ENV_FILE"
  set +a
  known=""
  for v in ROP_SLACK_WEBHOOK_URL ROP_SMTP_USERNAME ROP_SMTP_PASSWORD CLAUDE_CODE_OAUTH_TOKEN ANTHROPIC_API_KEY ROP_ALLOW_NO_FETCH; do
    [ -n "${!v:-}" ] && known="$known $v"
  done
  echo "[cron_wrapper] 환경 파일 읽음: $ENV_FILE (설정된 변수:${known:- 없음})"
else
  echo "[cron_wrapper] 환경 파일 없음: $ENV_FILE (없어도 된다. 형식은 deploy/README.md 5절)"
fi
echo "[cron_wrapper] PATH=$PATH"
for tool in claude python3 mkdocs git; do
  command -v "$tool" >/dev/null 2>&1 || echo "[cron_wrapper] 경고: $tool 을 PATH 에서 찾지 못했다(install_cron.sh 를 다시 실행해 PATH 줄을 갱신한다)"
done

# 3. 일일 실행(시간 상한)
RUN_DAILY="${ROP_RUN_DAILY:-$ROOT/pipeline/run_daily.sh}"
MAX_RT="$(ops cron.max_runtime_sec 14400)"
start=$(date +%s)
if [ "${MAX_RT:-0}" -gt 0 ] 2>/dev/null && command -v timeout >/dev/null 2>&1; then
  timeout --kill-after=300 "$MAX_RT" /bin/bash "$RUN_DAILY" "$@"
else
  /bin/bash "$RUN_DAILY" "$@"
fi
rc=$?
case "$rc" in
  0) meaning="완료";;
  2) meaning="보류 또는 설정·인자 오류(runs/parked/ 와 일일 로그를 본다)";;
  3) meaning="준비 단계 중단(웹 도구 없음 등)";;
  4) meaning="퍼블리셔 실패(반영은 되돌렸다)";;
  124|137) meaning="시간 상한 ${MAX_RT}초 초과로 강제 종료(cron.max_runtime_sec)";;
  *) meaning="오류";;
esac

# 4. 원격 배포(gh-deploy 방식, 켜져 있을 때만)
if [ "$rc" = 0 ] && [ "$(ops deploy.enabled false)" = "true" ] && [ "$(ops deploy.method gh-deploy)" = "gh-deploy" ] \
   && [ "$(ops deploy.after_daily_run true)" = "true" ]; then
  echo "[cron_wrapper $(ts)] 원격 배포: bash pipeline/deploy_site.sh --yes"
  drc=0
  /bin/bash "$ROOT/pipeline/deploy_site.sh" --yes || drc=$?
  echo "[cron_wrapper] 원격 배포 종료 코드 $drc$( [ "$drc" = 0 ] || echo ' — 게시·커밋은 유지된다. 수동: bash pipeline/deploy_site.sh --yes')"
fi

# 5. 종료 기록
echo "===== [cron_wrapper $(ts)] 종료 코드 $rc ($meaning), 소요 $(( $(date +%s) - start ))초 ====="
exit "$rc"
