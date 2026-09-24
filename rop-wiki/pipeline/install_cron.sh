#!/usr/bin/env bash
# ROP 연구 위키 — crontab 에 일일 실행을 등록한다 (빌드 사양서 9장 단계 4). pipeline/cron.example 을 바탕으로
# 마커 주석("# rop-wiki:begin" ~ "# rop-wiki:end") 사이에 넣으며, 이미 있으면 그 블록만 바꾼다(다른 항목은 건드리지 않는다).
#
# 사용: bash pipeline/install_cron.sh [--schedule "0 6 * * *"] [--tz Asia/Seoul] [--dry-run]
#   --schedule  cron 시각 표현(기본 "0 6 * * *" = 매일 06:00, settings.run_time 과 같다)
#   --tz        CRON_TZ 값(기본 Asia/Seoul)
#   --dry-run   crontab 을 바꾸지 않고 등록할 블록만 출력한다
# 해제: bash pipeline/uninstall_cron.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCHEDULE="0 6 * * *"
TZ_NAME="Asia/Seoul"
DRY=0
while [ $# -gt 0 ]; do
  case "$1" in
    --schedule) SCHEDULE="$2"; shift 2;;
    --tz) TZ_NAME="$2"; shift 2;;
    --dry-run) DRY=1; shift;;
    -h|--help) sed -n '2,10p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0;;
    *) echo "[install_cron] 알 수 없는 옵션: $1"; exit 2;;
  esac
done

BEGIN="# rop-wiki:begin (pipeline/install_cron.sh 가 관리한다. 손으로 고치지 말고 install/uninstall_cron.sh 를 쓴다)"
END="# rop-wiki:end"

# cron 은 로그인 셸의 PATH 를 쓰지 않으므로 claude·mkdocs·python3 가 있는 디렉터리를 PATH 에 넣는다
path_of() { command -v "$1" 2>/dev/null | xargs -r dirname; }
CRON_PATH="/usr/local/bin:/usr/bin:/bin"
for tool in claude mkdocs python3; do
  d="$(path_of "$tool" || true)"
  if [ -n "$d" ] && ! printf '%s' ":$CRON_PATH:" | grep -q ":$d:"; then CRON_PATH="$d:$CRON_PATH"; fi
done
for tool in claude mkdocs python3; do
  command -v "$tool" >/dev/null 2>&1 || echo "[install_cron] 경고: $tool 을 PATH 에서 찾지 못했다. cron 실행 전에 설치하거나 PATH 를 고친다"
done

BLOCK="$BEGIN
CRON_TZ=$TZ_NAME
PATH=$CRON_PATH
$SCHEDULE cd $ROOT && /usr/bin/env bash pipeline/run_daily.sh >> runs/cron.log 2>&1
$END"

if [ "$DRY" = 1 ]; then
  echo "$BLOCK"
  exit 0
fi
if ! command -v crontab >/dev/null 2>&1; then
  echo "[install_cron] crontab 명령이 없다. cron(cronie 등)을 설치하거나 다른 스케줄러(n8n, GitHub Actions)에 아래 명령을 등록한다:"
  echo "  $SCHEDULE ($TZ_NAME)  cd $ROOT && bash pipeline/run_daily.sh >> runs/cron.log 2>&1"
  exit 1
fi
mkdir -p "$ROOT/runs"
EXISTING="$(crontab -l 2>/dev/null || true)"
CLEANED="$(printf '%s\n' "$EXISTING" | awk -v b="$BEGIN" -v e="$END" 'index($0,"# rop-wiki:begin")==1{skip=1} !skip{print} $0==e{skip=0}')"
{
  if [ -n "$(printf '%s' "$CLEANED" | tr -d '[:space:]')" ]; then printf '%s\n' "$CLEANED"; fi
  printf '%s\n' "$BLOCK"
} | crontab -
echo "[install_cron] 등록했다. 현재 crontab:"
crontab -l
