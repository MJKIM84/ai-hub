#!/usr/bin/env bash
# ROP 연구 위키 — crontab 에서 일일 실행 등록을 해제한다. pipeline/install_cron.sh 가 넣은 마커 주석
# ("# rop-wiki:begin" ~ "# rop-wiki:end") 사이의 줄만 지우고 다른 항목은 건드리지 않는다.
# config/ops.yaml 의 cron.enabled 와 관계없이 언제나 해제할 수 있다(다시 등록하지 않게 하려면 python3 pipeline/lib/notify.py --disable cron).
# 진행 중인 실행은 멈추지 않는다(멈추려면 runs/.lock 을 잡은 프로세스를 찾는다: fuser -v runs/.lock).
# 사용: bash pipeline/uninstall_cron.sh [--dry-run]
set -euo pipefail

DRY=0
case "${1:-}" in
  "") ;;
  --dry-run) DRY=1;;
  -h|--help) sed -n '2,6p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0;;
  *) echo "[uninstall_cron] 알 수 없는 옵션: $1"; exit 2;;
esac
if ! command -v crontab >/dev/null 2>&1; then
  echo "[uninstall_cron] crontab 명령이 없다. 등록된 것이 없거나 다른 스케줄러를 쓰고 있다"
  exit 1
fi
END="# rop-wiki:end"
EXISTING="$(crontab -l 2>/dev/null || true)"
if ! printf '%s\n' "$EXISTING" | grep -q '^# rop-wiki:begin'; then
  echo "[uninstall_cron] 등록된 rop-wiki 블록이 없다"
  exit 0
fi
CLEANED="$(printf '%s\n' "$EXISTING" | awk -v e="$END" 'index($0,"# rop-wiki:begin")==1{skip=1} !skip{print} $0==e{skip=0}')"
if [ "$DRY" = 1 ]; then
  echo "[uninstall_cron] 해제 후 crontab(미적용):"
  printf '%s\n' "$CLEANED"
  exit 0
fi
if [ -n "$(printf '%s' "$CLEANED" | tr -d '[:space:]')" ]; then
  printf '%s\n' "$CLEANED" | crontab -
else
  crontab -r 2>/dev/null || true
fi
echo "[uninstall_cron] 해제했다. 현재 crontab:"
crontab -l 2>/dev/null || echo "(비어 있음)"
