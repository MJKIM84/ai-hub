#!/usr/bin/env bash
# ROP 연구 위키 — 운영 서버(항상 켜진 리눅스)의 crontab 에 일일 실행을 등록한다 (빌드 사양서 9장 단계 4).
# 마커 주석("# rop-wiki:begin" ~ "# rop-wiki:end") 사이에 넣으며, 이미 있으면 그 블록만 바꾸고 다른 항목은 건드리지 않는다.
# 블록은 언제나 crontab 맨 끝에 둔다(블록의 CRON_TZ·PATH 줄은 그 뒤 줄에도 적용되기 때문이다. 블록 뒤에 다른 항목을 넣지 않는다).
#
# 사용: bash pipeline/install_cron.sh [--dry-run] [--force] [--schedule "0 6 * * *"] [--tz Asia/Seoul]
#                                     [--tz-mode auto|crontz|server] [--server-tz Etc/UTC]
#   --dry-run    crontab 을 바꾸지 않고 등록할 블록만 출력한다(cron.enabled 와 관계없이 된다)
#   --force      config/ops.yaml 의 cron.enabled 가 false 여도 등록한다(기본은 거부, exit 3)
#   --schedule   cron 시각 표현으로 덮어쓴다(예 "0 7 * * *"). 기본은 settings.run_time("06:00 Asia/Seoul")의 HH:MM → "M H * * *"
#   --tz         시간대 덮어쓰기. 기본은 run_time 의 시간대(없으면 settings.timezone)
#   --tz-mode    auto(기본, ops.yaml cron.tz_mode): cron 데몬이 CRON_TZ 를 지원하면 crontz, 아니면 server
#                crontz: "CRON_TZ=<시간대>" 줄 + 그 시간대 시각(cronie: RHEL·Fedora·Arch 등)
#                server: 시각을 서버 시간대로 환산해 등록(Debian·Ubuntu 기본 cron 은 CRON_TZ 를 무시한다. --schedule 을 주면 환산하지 않는다)
#   --server-tz  server 모드의 서버 시간대(기본: TZ 변수 → /etc/timezone → /etc/localtime)
# 등록 줄: flock -n 으로 runs/.lock(ops.yaml cron.lock_file)을 잡고 pipeline/cron_wrapper.sh 를 실행한다(겹침 방지·로그 순환·환경 파일·시간 상한).
# 환경 파일: ~/.config/rop-wiki/env(ops.yaml cron.env_file)가 있으면 래퍼가 읽는다 — ROP_SLACK_WEBHOOK_URL, ROP_SMTP_USERNAME/PASSWORD,
#   CLAUDE_CODE_OAUTH_TOKEN 또는 ANTHROPIC_API_KEY, ROP_ALLOW_NO_FETCH. 형식은 deploy/README.md 5절.
# 켜기: python3 pipeline/lib/notify.py --enable cron && bash pipeline/install_cron.sh      해제: bash pipeline/uninstall_cron.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY="${PYTHON:-python3}"
SCHEDULE=""; TZ_NAME=""; TZ_MODE=""; SERVER_TZ=""; DRY=0; FORCE=0
while [ $# -gt 0 ]; do
  case "$1" in
    --schedule) SCHEDULE="$2"; shift 2;;
    --tz) TZ_NAME="$2"; shift 2;;
    --tz-mode) TZ_MODE="$2"; shift 2;;
    --server-tz) SERVER_TZ="$2"; shift 2;;
    --dry-run) DRY=1; shift;;
    --force) FORCE=1; shift;;
    -h|--help) sed -n '2,23p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0;;
    *) echo "[install_cron] 알 수 없는 옵션: $1"; exit 2;;
  esac
done
ops() { (cd "$ROOT" && "$PY" pipeline/lib/notify.py --get "$1" --default "${2:-}" 2>/dev/null) || printf '%s\n' "${2:-}"; }
abspath() { case "$1" in /*) printf '%s\n' "$1";; *) printf '%s\n' "$ROOT/$1";; esac; }

# --- 0. 등록 허용 스위치(ops.yaml cron.enabled) ---------------------------------------------------
CRON_ENABLED="$(ops cron.enabled false)"
if [ "$DRY" = 0 ] && [ "$CRON_ENABLED" != "true" ] && [ "$FORCE" = 0 ]; then
  echo "[install_cron] 등록하지 않았다: config/ops.yaml 의 cron.enabled 가 false 다(운영 서버 cron 등록은 기본으로 꺼 둔다)."
  echo "  켜기: python3 pipeline/lib/notify.py --enable cron && bash pipeline/install_cron.sh   (한 번만: --force, 미리 보기: --dry-run)"
  exit 3
fi

# --- 1. 시각·시간대: settings.run_time("HH:MM [시간대]")·timezone (기존 규칙) --------------------------
RUN_TIME="$(cd "$ROOT" && "$PY" pipeline/lib/runs.py setting --key run_time --default "06:00 Asia/Seoul" 2>/dev/null || echo "06:00 Asia/Seoul")"
SETTINGS_TZ="$(cd "$ROOT" && "$PY" pipeline/lib/runs.py setting --key timezone --default "Asia/Seoul" 2>/dev/null || echo "Asia/Seoul")"
RT_CLOCK="${RUN_TIME%% *}"                       # "06:00"
RT_TZ=""; [ "$RUN_TIME" != "$RT_CLOCK" ] && RT_TZ="${RUN_TIME#* }"   # "Asia/Seoul" (run_time 에 시간대가 있을 때)
USER_SCHEDULE=0; [ -n "$SCHEDULE" ] && USER_SCHEDULE=1
HH=6; MM=0
if [ -z "$SCHEDULE" ]; then
  if printf '%s' "$RT_CLOCK" | grep -Eq '^[0-9]{1,2}:[0-9]{2}$'; then
    HH=$((10#${RT_CLOCK%%:*})); MM=$((10#${RT_CLOCK##*:}))
  else
    echo "[install_cron] settings.run_time 형식(HH:MM [시간대])을 읽지 못해 기본 06:00 을 쓴다: '$RUN_TIME'"
  fi
  SCHEDULE="$MM $HH * * *"
fi
[ -z "$TZ_NAME" ] && TZ_NAME="${RT_TZ:-$SETTINGS_TZ}"

# --- 2. CRON_TZ 지원 여부 → 시간대 처리 방식 -------------------------------------------------------
# cronie 는 CRON_TZ 를 지원하고(바이너리에 문자열이 있다), Debian·Ubuntu 의 cron(vixie 3.0pl1)과 busybox crond 는 무시한다.
cron_tz_support() {
  local b
  for b in /usr/sbin/crond /usr/sbin/cron /usr/bin/crond /sbin/crond; do
    [ -f "$b" ] || continue
    if grep -a -q 'CRON_TZ' "$b" 2>/dev/null; then echo yes; else echo no; fi
    return
  done
  echo unknown
}
[ -z "$TZ_MODE" ] && TZ_MODE="$(ops cron.tz_mode auto)"
SUPPORT="$(cron_tz_support)"
case "$TZ_MODE" in
  auto) if [ "$SUPPORT" = no ]; then TZ_MODE=server; else TZ_MODE=crontz; fi;;
  crontz|server) ;;
  *) echo "[install_cron] --tz-mode 값 오류: $TZ_MODE (auto|crontz|server)"; exit 2;;
esac
[ "$SUPPORT" = unknown ] && echo "[install_cron] 경고: cron 데몬 실행 파일을 찾지 못해 CRON_TZ 지원 여부를 모른다(설치 전이면 설치 뒤 다시 실행한다)"
if [ -z "$SERVER_TZ" ]; then
  SERVER_TZ="${TZ:-}"
  [ -z "$SERVER_TZ" ] && [ -f /etc/timezone ] && SERVER_TZ="$(head -n 1 /etc/timezone)"
  [ -z "$SERVER_TZ" ] && SERVER_TZ="$(readlink /etc/localtime 2>/dev/null | sed 's#.*/zoneinfo/##')"
  [ -z "$SERVER_TZ" ] && SERVER_TZ="Etc/UTC"
fi

TZ_LINES=""
if [ "$TZ_MODE" = crontz ]; then
  TZ_LINES="CRON_TZ=$TZ_NAME"
  NOTE="시각은 CRON_TZ=$TZ_NAME 기준"
elif [ "$USER_SCHEDULE" = 1 ]; then
  NOTE="--schedule 값을 서버 시간대($SERVER_TZ) 시각으로 그대로 쓴다(CRON_TZ 미사용)"
else
  CONV="$("$PY" - "$HH" "$MM" "$TZ_NAME" "$SERVER_TZ" <<'PYEOF'
import sys
from datetime import datetime
from zoneinfo import ZoneInfo
h, m, src, dst = int(sys.argv[1]), int(sys.argv[2]), ZoneInfo(sys.argv[3]), ZoneInfo(sys.argv[4])
now = datetime.now(src)
local = now.replace(hour=h, minute=m, second=0, microsecond=0).astimezone(dst)
y = now.year
dst_shift = datetime(y, 1, 15, 12, tzinfo=dst).utcoffset() != datetime(y, 7, 15, 12, tzinfo=dst).utcoffset() \
    or datetime(y, 1, 15, 12, tzinfo=src).utcoffset() != datetime(y, 7, 15, 12, tzinfo=src).utcoffset()
print(local.minute, local.hour, "dst" if dst_shift else "fixed")
PYEOF
)" || { echo "[install_cron] 시간대 환산 실패($TZ_NAME → $SERVER_TZ). --tz-mode crontz 또는 --schedule 로 지정한다"; exit 2; }
  read -r CM CH CDST <<<"$CONV"
  SCHEDULE="$CM $CH * * *"
  NOTE="이 cron 은 CRON_TZ 를 쓰지 않는다(tz_mode=server) — $TZ_NAME $(printf '%02d:%02d' "$HH" "$MM") 을 서버 시간대 $SERVER_TZ $(printf '%02d:%02d' "$CH" "$CM") 으로 환산했다. 서버 시간대를 바꾸면 다시 등록한다"
  if [ "$CDST" = dst ]; then
    echo "[install_cron] 경고: $SERVER_TZ 또는 $TZ_NAME 에 일광 절약 시간이 있어 환산 시각이 계절마다 1시간 어긋난다. 서버 시간대를 UTC 나 $TZ_NAME 로 두거나 cronie 를 쓴다"
  fi
fi
echo "[install_cron] 스케줄 '$SCHEDULE' — $NOTE (settings.run_time='$RUN_TIME', settings.timezone='$SETTINGS_TZ', cron CRON_TZ 지원=$SUPPORT, tz_mode=$TZ_MODE)"

# --- 3. PATH(cron 은 로그인 셸의 PATH 를 쓰지 않는다)·잠금·래퍼 -----------------------------------
path_of() { command -v "$1" 2>/dev/null | xargs -r dirname; }
CRON_PATH="/usr/local/bin:/usr/bin:/bin"
for tool in claude mkdocs python3 git; do
  d="$(path_of "$tool" || true)"
  if [ -n "$d" ] && ! printf '%s' ":$CRON_PATH:" | grep -q ":$d:"; then CRON_PATH="$d:$CRON_PATH"; fi
done
MISSING=""
for tool in claude mkdocs python3 git; do
  command -v "$tool" >/dev/null 2>&1 || { echo "[install_cron] 경고: $tool 을 PATH 에서 찾지 못했다. cron 실행 전에 설치하거나 PATH 를 고친다"; MISSING="$MISSING $tool"; }
done
FLOCK="$(command -v flock 2>/dev/null || true)"
if [ -z "$FLOCK" ]; then
  if [ "$DRY" = 0 ]; then echo "[install_cron] flock 이 없다(util-linux). 겹침 방지 없이 등록하지 않는다: 설치 뒤 다시 실행한다"; exit 1; fi
  echo "[install_cron] 경고: flock 이 없다(util-linux 설치 필요). 미리 보기에는 /usr/bin/flock 으로 적는다"
  FLOCK=/usr/bin/flock
fi
LOCK="$(abspath "$(ops cron.lock_file runs/.lock)")"
WRAPPER="$ROOT/pipeline/cron_wrapper.sh"
ENV_FILE="$(ops cron.env_file '~/.config/rop-wiki/env')"

BEGIN="# rop-wiki:begin (pipeline/install_cron.sh 가 관리한다. 손으로 고치지 말고 install/uninstall_cron.sh 를 쓴다)"
END="# rop-wiki:end"
BLOCK="$BEGIN
# $NOTE. 겹침 방지 잠금 $LOCK, 출력 $(ops cron.log_file runs/cron.log)($(( $(ops cron.log_max_bytes 5242880) / 1048576 ))MB 순환), 환경 파일 $ENV_FILE(있으면)
${TZ_LINES:+$TZ_LINES
}PATH=$CRON_PATH
$SCHEDULE $FLOCK -n -E 75 $LOCK /bin/bash $WRAPPER; [ \$? -ne 75 ] || /bin/bash $WRAPPER --lock-busy
$END"

if [ "$DRY" = 1 ]; then
  echo "$BLOCK"
  [ "$CRON_ENABLED" != "true" ] && echo "[install_cron] (미리 보기) cron.enabled 가 false 라 실제 등록은 거부된다. 켜기: python3 pipeline/lib/notify.py --enable cron"
  exit 0
fi
if ! command -v crontab >/dev/null 2>&1; then
  echo "[install_cron] crontab 명령이 없다. cron(cronie 등)을 설치하거나 다른 스케줄러(systemd timer, n8n)에 아래 명령을 등록한다:"
  echo "  $SCHEDULE ($TZ_NAME)  $FLOCK -n $LOCK /bin/bash $WRAPPER"
  exit 1
fi
mkdir -p "$ROOT/runs" "$(dirname "$LOCK")"
EXISTING="$(crontab -l 2>/dev/null || true)"
CLEANED="$(printf '%s\n' "$EXISTING" | awk -v e="$END" 'index($0,"# rop-wiki:begin")==1{skip=1} !skip{print} $0==e{skip=0}')"
{
  if [ -n "$(printf '%s' "$CLEANED" | tr -d '[:space:]')" ]; then printf '%s\n' "$CLEANED"; fi
  printf '%s\n' "$BLOCK"
} | crontab -
echo "[install_cron] 등록했다$( [ "$FORCE" = 1 ] && [ "$CRON_ENABLED" != "true" ] && echo ' (--force: cron.enabled=false 무시)'). 현재 crontab:"
crontab -l
[ -n "$MISSING" ] && echo "[install_cron] 주의: 없는 도구:$MISSING — 첫 실행 전에 설치한다"
if ! pgrep -x cron >/dev/null 2>&1 && ! pgrep -x crond >/dev/null 2>&1; then
  echo "[install_cron] 주의: cron 데몬(cron/crond)이 실행 중이 아니다. 등록만 되고 실행되지 않는다(systemctl enable --now cron 또는 crond)"
fi
exit 0
