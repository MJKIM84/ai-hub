#!/usr/bin/env bash
# ROP 연구 위키 — 일일 파이프라인 실행 스크립트 (빌드 사양서 7.2 의 8단계, 7.3 실패 처리)
#
# 순서: 1 준비 → 2 대상 선정 → 3 리서치 → 4 1차 검증(반려면 재조사, 최대 max_retries) → 5 스토리텔러
#       → 6 2차 검증(불통과면 재작성, 최대 max_retries) → 7 퍼블리셔(사양서 6.4 의 1~7단계: 스키마·판정 → 프런트매터 → 원문 보호
#       → 링크 → 반영 → 빌드 → 커밋) → 8 일일 로그·운영 지표(퍼블리셔 8단계 일일 로그, 9단계 알림)
# 사용:
#   bash pipeline/run_daily.sh                      # 오늘(settings.timezone) 정규 실행
#   bash pipeline/run_daily.sh --date 2026-09-24 --run-type area_deep_dive --area 7      # 대상 지정(드라이런)
#   bash pipeline/run_daily.sh --run-type track --track manual-capability-ontology --stage 1 --question-ids q1-01,q1-02
#   bash pipeline/run_daily.sh --resume 2026-09-24-01              # 있는 산출물부터 이어서(보류 폴더면 되돌려 재투입)
#   bash pipeline/run_daily.sh --resume 2026-09-24-01 --step publish   # 단일 단계만
# 옵션: --date D --run-type T --area N --track S --stage N --question-ids a,b --category A~G --resume ID --run-id ID --until verify2
#       --step {prepare|select|research|verify1|storytell|verify2|publish|log} --skip-probe --allow-no-fetch --no-build --no-commit
#       (--skip-probe: 드라이런용. 기존 probe.json 재사용, 없으면 WebSearch 점검을 생략(미점검으로 기록)하고 WebFetch 는 curl 참고값만 쓴다.
#        --allow-no-fetch(또는 환경변수 ROP_ALLOW_NO_FETCH=1): 페이지 열람 도구가 없을 때 중단하지 않고 원문 미열람 모드로 진행(사용자 override).
#        --no-build/--no-commit: 퍼블리셔 6·7단계 생략)
# 웹 도구(7.3): 웹 검색 또는 페이지 열람 도구가 없으면 즉시 중단·로그(0장 web_tools_required). 열람만 없고 override 가 있으면
#   진행하되 에이전트 컨텍스트에 web_fetch_available: false 를 주고 로그에 "페이지 열람 불가 — 원문 미열람 모드(사용자 override)"를 남긴다.
# 산출물: runs/<run_id>/ (target.json, probe.json, docs_tree.txt, prompts/, research.json·md, verification.json·md, pages/·pages.json,
#         verification2.json·md, log.md, timings.json, summary.json; 주간 정리면 link_check.txt·url_check.json 도). 보류는 runs/parked/<run_id>/.
# 단계별 소요 시간은 runs/<run_id>/log.md 와 timings.json 에 남고, 퍼블리셔가 일일 로그(docs/logs/daily/<date>.md)에 옮긴다.
# 커밋: 퍼블리셔(publish.py, 보류·중단이면 --log-only)가 실행 기록까지 한 커밋에 담는다. 이 스크립트는 퍼블리셔를 부른 뒤
#   실행 폴더에 아무것도 쓰지 않는다(커밋 뒤 미커밋 로그가 남지 않도록).
set -euo pipefail

# 스크립트 전체를 한 중괄호 묶음으로 둔다: bash 가 실행 전에 끝까지 읽어 두므로, 실행 중에 이 파일을 고쳐도 도는 실행이 깨지지 않는다
# (bash 는 스크립트를 명령 단위로 읽어 가며 실행한다 — 운영 전환 검증 실행 1이 실행 중 수정으로 문법 오류를 냈다).
{

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
PY="${PYTHON:-python3}"
LIB="pipeline/lib/runs.py"

usage() {
  sed -n '2,24p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
}

# ---------------------------------------------------------------------------------------------
# 옵션
# ---------------------------------------------------------------------------------------------
DATE=""; RUN_TYPE=""; AREA=""; TRACK=""; STAGE=""; QIDS=""; RESUME=""; STEP=""; RUN_ID_OPT=""; CATEGORY=""; UNTIL=""; MAXQ=""
SKIP_PROBE=0; NO_BUILD=0; NO_COMMIT=0; ALLOW_NO_FETCH=0; ALLOW_NO_FETCH_SRC=""
if [ "${ROP_ALLOW_NO_FETCH:-0}" = "1" ]; then ALLOW_NO_FETCH=1; ALLOW_NO_FETCH_SRC="ROP_ALLOW_NO_FETCH=1"; fi
while [ $# -gt 0 ]; do
  case "$1" in
    --date) DATE="$2"; shift 2;;
    --run-type) RUN_TYPE="$2"; shift 2;;
    --area) AREA="$2"; shift 2;;
    --track) TRACK="$2"; shift 2;;
    --stage) STAGE="$2"; shift 2;;
    --question-ids) QIDS="$2"; shift 2;;
    --category) CATEGORY="$2"; shift 2;;
    --max-questions) MAXQ="$2"; shift 2;;
    --until) UNTIL="$2"; shift 2;;
    --resume) RESUME="$2"; shift 2;;
    --run-id) RUN_ID_OPT="$2"; shift 2;;
    --step) STEP="$2"; shift 2;;
    --skip-probe) SKIP_PROBE=1; shift;;
    --allow-no-fetch) ALLOW_NO_FETCH=1; ALLOW_NO_FETCH_SRC="--allow-no-fetch"; shift;;
    --no-build) NO_BUILD=1; shift;;
    --no-commit) NO_COMMIT=1; shift;;
    -h|--help) usage; exit 0;;
    *) echo "[run_daily] 알 수 없는 옵션: $1"; usage; exit 2;;
  esac
done
case "$STEP" in ""|prepare|select|research|verify1|storytell|verify2|publish|log) ;; *) echo "[run_daily] --step 값 오류: $STEP"; exit 2;; esac
case "$UNTIL" in ""|verify2) ;; *) echo "[run_daily] --until 값 오류: $UNTIL (verify2 만 지원)"; exit 2;; esac
if [ -n "$STEP" ] && [ "$STEP" != "prepare" ] && [ "$STEP" != "select" ] && [ -z "$RESUME" ] && [ -z "$RUN_ID_OPT" ]; then
  echo "[run_daily] --step $STEP 은 --resume <run_id> (또는 --run-id) 와 함께 쓴다"; exit 2
fi

# ---------------------------------------------------------------------------------------------
# 도우미
# ---------------------------------------------------------------------------------------------
ts() { date '+%Y-%m-%d %H:%M:%S'; }
say() { echo "[run_daily $(ts)] $*"; }
rlog() { "$PY" "$LIB" log --run-id "$RUN_ID" --msg "$1" ${2:+--step "$2"}; }
rstep() { "$PY" "$LIB" step --run-id "$RUN_ID" --step "$1" --result "$2" --seconds "$3" --note "${4:-}"; }
jget() { "$PY" "$LIB" jsonget --file "$1" --key "$2" --default "${3:-}"; }
setting() { "$PY" "$LIB" setting --key "$1" --default "${2:-}"; }
now_s() { date +%s; }

CURRENT_STEP="준비"; STEP_START=$(now_s); RUN_ID=""; RD=""
begin_step() { CURRENT_STEP="$1"; STEP_START=$(now_s); say "== $1"; }
end_step() { local result="$1" note="${2:-}"; local sec=$(( $(now_s) - STEP_START )); rstep "$CURRENT_STEP" "$result" "$sec" "$note"; say "   -> $result (${sec}초) $note"; }
should_run() { if [ -n "$STEP" ]; then [ "$STEP" = "$1" ]; else return 0; fi; }
publish_log_only() { "$PY" pipeline/publish.py "$RUN_ID" --log-only $( [ "$NO_BUILD" = 1 ] && echo --no-build ) $( [ "$NO_COMMIT" = 1 ] && echo --no-commit ) || true; }

on_error() {
  local rc=$? line=$1
  say "실패: 단계 '$CURRENT_STEP' (run_daily.sh 줄 $line, exit $rc)"
  if [ -n "$RUN_ID" ] && [ -d "runs/$RUN_ID" ]; then
    rlog "실패: 단계 $CURRENT_STEP (run_daily.sh 줄 $line, exit $rc)" "$CURRENT_STEP" || true
    rstep "$CURRENT_STEP" "실패" "$(( $(now_s) - STEP_START ))" "run_daily.sh 줄 $line exit $rc" || true
    "$PY" "$LIB" summary --run-id "$RUN_ID" --set "end_state=중단($CURRENT_STEP 단계 실패, exit $rc)" published=false || true
    publish_log_only
  fi
  exit "$rc"
}
trap 'on_error $LINENO' ERR

abort() {  # 준비 단계의 즉시 중단(7.3 "웹 도구 없음 → 즉시 중단·로그")
  local reason="$1"
  rlog "즉시 중단: $reason" "$CURRENT_STEP"
  end_step "실패" "$reason"
  "$PY" "$LIB" summary --run-id "$RUN_ID" --set "end_state=중단($reason)" published=false parked=false
  publish_log_only
  say "중단: $reason"
  exit 3
}

weekly_checks() {  # 7.1 주간 정리의 "링크·출처 유효성 점검": 에이전트의 WebFetch 에 맡기지 않고 스크립트가 리서치 전에 수행해
                   # 결과 파일(runs/<id>/link_check.txt, url_check.json)을 리서치·검증·스토리텔러 입력에 넣고 일일 로그의 다음 실행 메모에 옮긴다
  begin_step "링크·출처 점검"
  local rc=0 rc2=0 links="" urls=""
  "$PY" pipeline/checks/check_links.py > "$RD/link_check.txt" 2>&1 || rc=$?
  "$PY" pipeline/checks/check_urls.py --timeout 10 --json "$RD/url_check.json" > "$RD/url_check.txt" 2>&1 || rc2=$?
  links="$(grep -o '\[check_links\].*' "$RD/link_check.txt" | tail -n 1 || true)"
  urls="$(grep -o '\[check_urls\] [0-9]*건.*' "$RD/url_check.txt" | tail -n 1 || true)"
  rlog "내부 링크·각주 검사(exit $rc): ${links:-출력 없음} → $RD/link_check.txt" "링크·출처 점검"
  rlog "참고문헌 URL 열림 확인(exit $rc2): ${urls:-출력 없음} → $RD/url_check.json" "링크·출처 점검"
  end_step "$( [ "$rc" = 0 ] && [ "$rc2" = 0 ] && echo 성공 || echo "완료(문제 있음)" )" "${links:-링크 검사 출력 없음} / ${urls:-URL 점검 출력 없음}"
}

park() {  # 검증 반려·불통과가 max_retries 뒤에도 이어지거나 스키마 불일치가 재실행 뒤에도 남을 때(7.3)
  local reason="$1"
  rlog "보류: $reason" "$CURRENT_STEP"
  end_step "재시도 후 보류" "$reason"
  "$PY" "$LIB" park --run-id "$RUN_ID" --reason "$reason" >/dev/null
  publish_log_only
  say "보류: runs/parked/$RUN_ID/ — $reason"
  exit 2
}

# ---------------------------------------------------------------------------------------------
# 1. 준비: 설정 로드, 실행 id, 웹 도구 점검, runs/<run_id>/ 생성
# ---------------------------------------------------------------------------------------------
begin_step "준비"
if ! "$PY" -c "import sys; sys.path.insert(0,'pipeline'); from lib import runs; runs.load_settings(); runs.load_rotation(); runs.load_priority()" 2>/tmp/rop_settings_err.txt; then
  say "설정 파일(config/*.yaml)을 읽을 수 없어 중단한다: $(cat /tmp/rop_settings_err.txt | tail -3)"
  exit 2
fi
if [ -n "$DATE" ]; then export ROP_TODAY="$DATE"; fi
DATE="${DATE:-$("$PY" "$LIB" today)}"
export ROP_TODAY="$DATE"
if [ -n "$RESUME" ]; then
  RUN_ID="$RESUME"
  if [ -d "runs/parked/$RUN_ID" ] && [ ! -d "runs/$RUN_ID" ]; then
    # 재투입(7.4): 폴더를 되돌리고 summary.json 의 보류 표시(parked·end_state·park_reason)를 지운다(lib/runs.py unpark).
    # 지우지 않으면 재투입해 게시까지 성공한 실행도 parked: true 로 남아 select_target 의 연속 보류 횟수에 세어지고 일일 로그에 '보류' 줄이 붙는다.
    "$PY" "$LIB" unpark --run-id "$RUN_ID" >/dev/null
    say "보류 폴더를 되돌렸다: runs/parked/$RUN_ID → runs/$RUN_ID (재투입, summary.json 의 보류 표시 해제)"
  fi
  if [ ! -d "runs/$RUN_ID" ]; then say "재개할 실행 폴더가 없다: runs/$RUN_ID"; exit 2; fi
  if [ -z "$STEP" ] && [ "$(jget "runs/$RUN_ID/summary.json" published false)" = "true" ]; then
    # 이미 게시·커밋된 실행: 실행 폴더에 기록을 더하면 커밋되지 않은 채 남으므로 아무것도 쓰지 않고 끝낸다
    say "재개: 이미 게시된 실행($RUN_ID) — 할 일이 없다"; exit 0
  fi
  DATE="$(jget "runs/$RUN_ID/target.json" date "$DATE")"; export ROP_TODAY="$DATE"
else
  RUN_ID="${RUN_ID_OPT:-$("$PY" "$LIB" new-run-id --date "$DATE")}"
fi
RD="runs/$RUN_ID"
mkdir -p "$RD/prompts"
rlog "실행 시작 (date=$DATE run_id=$RUN_ID resume=${RESUME:-없음} step=${STEP:-전체} run_type=${RUN_TYPE:-자동} area=${AREA:-자동} track=${TRACK:-자동})" "준비"
[ -n "$RESUME" ] && rlog "재개: 있는 산출물부터 이어서 실행한다" "준비"
MAX_RETRIES="$(setting daily_budget.max_retries 2)"
WEB_TOOLS_REQUIRED="$(setting web_tools_required true)"
WEB_FETCH_REQUIRED="$(setting web_fetch_required true)"
FETCH_OVERRIDE_NOTE="페이지 열람 불가 — 원문 미열람 모드(사용자 override)"
PROBE_NOTE="건너뜀"
NEEDS_PROBE=1
case "$STEP" in select|publish|log) NEEDS_PROBE=0;; esac
if [ "$NEEDS_PROBE" = 1 ]; then
  if [ "$SKIP_PROBE" = 1 ] && [ -f "$RD/probe.json" ]; then
    rlog "웹 도구 점검 생략(--skip-probe): 기존 probe.json 사용" "준비"
  else
    "$PY" pipeline/agent_runner.py probe --out "$RD/probe.json" $( [ "$SKIP_PROBE" = 1 ] && echo "--skip-search --skip-fetch" ) >/dev/null
  fi
  WS="$(jget "$RD/probe.json" web_search_available 미점검)"
  WF="$(jget "$RD/probe.json" web_fetch_available false)"
  PROBE_NOTE="web_search_available: $WS · web_fetch_available: $WF"
  rlog "웹 도구 점검: $PROBE_NOTE" "준비"
  # 7.3 "웹 도구 없음 → 즉시 중단·로그", 0장 web_tools_required("웹 검색·페이지 열람 도구가 없으면 실행을 중단")
  if [ "$WS" = "미점검" ]; then
    # --skip-probe(드라이런)로 점검하지 않은 것을 가용으로 기록하지 않는다. 정규(cron) 실행에서는 --skip-probe 를 쓰지 않는다
    rlog "웹 도구 점검 생략(--skip-probe, 드라이런): 웹 검색 도구는 점검하지 않았다(web_search_available: null)" "준비"
    PROBE_NOTE="$PROBE_NOTE · 웹 도구 점검 생략(드라이런)"
  elif [ "$WS" != "true" ] && [ "$WEB_TOOLS_REQUIRED" = "true" ]; then
    abort "웹 검색(WebSearch) 도구를 쓸 수 없다(web_tools_required)"
  fi
  FM="$(jget "$RD/probe.json" fetch_mode none)"
  if [ "$WF" != "true" ] && [ "$FM" = "mirror_only" ]; then
    # 부분 열람(운영 전환 1-1, DECISIONS D-003): 일반 페이지는 막혔지만 에이전트 WebFetch 로 공식 저장소 원문(raw.githubusercontent.com)과
    # inbox/sources 원문 텍스트는 연다. 도구가 동작하므로 중단하지 않고, 출처별 fetched 표시로 신뢰도 상한을 코드가 강제한다.
    rlog "부분 열람 모드: 일반 웹 페이지 열람은 차단, GitHub 공식 저장소 원문(raw.githubusercontent.com)과 inbox 원문만 열람 — 출처별 원문 열람 표시·신뢰도 상한 적용" "준비"
    PROBE_NOTE="$PROBE_NOTE · 부분 열람 모드(fetch_mode: mirror_only)"
  elif [ "$WF" != "true" ]; then
    SRC=""
    if [ "$ALLOW_NO_FETCH" = 1 ]; then SRC="$ALLOW_NO_FETCH_SRC"
    elif [ "$WEB_TOOLS_REQUIRED" != "true" ]; then SRC="settings.web_tools_required: false"
    elif [ "$WEB_FETCH_REQUIRED" != "true" ]; then SRC="settings.web_fetch_required: false"
    fi
    if [ -z "$SRC" ]; then
      abort "페이지 열람(WebFetch) 도구를 쓸 수 없다(web_tools_required). 원문 미열람 모드로 진행하려면 --allow-no-fetch 또는 ROP_ALLOW_NO_FETCH=1"
    fi
    # override: 진행하되 에이전트 실행 컨텍스트에 web_fetch_available: false(원문 미열람 모드)를 알리고, 로그·일일 로그에 남긴다
    "$PY" "$LIB" jsonset --file "$RD/probe.json" --set web_fetch_available=false web_fetch_override=true "web_fetch_override_source=$SRC"
    rlog "$FETCH_OVERRIDE_NOTE — override: $SRC. 실행 컨텍스트에 web_fetch_available: false 를 표시하고 진행한다" "준비"
    PROBE_NOTE="$PROBE_NOTE · $FETCH_OVERRIDE_NOTE"
  fi
fi
"$PY" "$LIB" docs-tree --run-id "$RUN_ID" >/dev/null
end_step "성공" "$PROBE_NOTE"
if [ "$STEP" = "prepare" ]; then say "완료(--step prepare)"; exit 0; fi

# ---------------------------------------------------------------------------------------------
# 2. 대상 선정 → target.json
# ---------------------------------------------------------------------------------------------
if should_run select; then
  begin_step "대상 선정"
  if [ -n "$RESUME" ] && [ -z "$STEP" ] && [ -f "$RD/target.json" ]; then
    rlog "재개: 기존 target.json 사용" "대상 선정"
    end_step "건너뜀" "재개(기존 target.json)"
  else
    "$PY" pipeline/select_target.py --date "$DATE" --run-id "$RUN_ID" \
      ${RUN_TYPE:+--run-type "$RUN_TYPE"} ${AREA:+--area "$AREA"} ${TRACK:+--track "$TRACK"} ${STAGE:+--stage "$STAGE"} ${QIDS:+--question-ids "$QIDS"} \
      ${CATEGORY:+--category "$CATEGORY"} ${MAXQ:+--max-questions "$MAXQ"}
    end_step "성공" "$(jget "$RD/target.json" run_type) · $(jget "$RD/target.json" target.area_name 없음)"
  fi
  if [ "$STEP" = "select" ]; then say "완료(--step select): $RD/target.json"; exit 0; fi
fi
if [ ! -f "$RD/target.json" ]; then say "target.json 이 없다: $RD"; exit 2; fi
SEL_TYPE="$(jget "$RD/target.json" run_type)"

# ---------------------------------------------------------------------------------------------
# 3·4. 리서치 → 1차 검증 (반려면 "## 반려 사유"를 붙여 리서치 재실행, 최대 max_retries; 그래도 반려면 보류)
# ---------------------------------------------------------------------------------------------
V1="$(jget "$RD/verification.json" verdict "")"
if [ -n "$RESUME" ] && [ -z "$STEP" ] && { [ "$V1" = "승인" ] || [ "$V1" = "조건부 승인" ]; }; then
  say "재개: 1차 검증($V1)까지 완료된 실행 — 리서치·1차 검증 건너뜀"
  rlog "재개: 1차 검증 $V1 — 리서치·1차 검증 건너뜀" "1차 검증"
elif should_run research || should_run verify1; then
  attempt=0
  research_done=0
  if [ -n "$RESUME" ] && [ -f "$RD/research.json" ] && [ "$STEP" != "research" ]; then research_done=1; fi
  if [ "$STEP" = "verify1" ]; then research_done=1; fi
  if [ "$SEL_TYPE" = "weekly_review" ] && [ "$research_done" = 0 ]; then weekly_checks; fi
  while :; do
    if [ "$research_done" = 0 ]; then
      begin_step "리서치"
      if ! "$PY" pipeline/agent_runner.py run --role researcher --run-id "$RUN_ID" --retry "$attempt"; then
        park "리서치 에이전트 실패(스키마 불일치 1회 재실행 후에도 실패 또는 호출 오류; 7.3)"
      fi
      "$PY" pipeline/validate_run.py "$RUN_ID" --stage research >/dev/null || true   # 원문 열람 여부 확정·신뢰도 상한(코드, 1-1)
      BUDGET_NOTE="$("$PY" "$LIB" budget-check --run-id "$RUN_ID")"
      rlog "예산 점검: $BUDGET_NOTE" "리서치"
      end_step "$( [ "$attempt" -gt 0 ] && echo "재시도 ${attempt}회 후 성공" || echo 성공 )" "$BUDGET_NOTE"
      if [ "$STEP" = "research" ]; then say "완료(--step research)"; exit 0; fi
    fi
    research_done=0
    begin_step "1차 검증"
    if ! "$PY" pipeline/agent_runner.py run --role verifier --stage first --run-id "$RUN_ID" --retry "$attempt"; then
      park "내용 검증 에이전트(1차) 실패(스키마 불일치 1회 재실행 후에도 실패 또는 호출 오류; 7.3)"
    fi
    "$PY" pipeline/validate_run.py "$RUN_ID" --stage verification1 >/dev/null || rlog "1차 검증 산출물 교차 검사 경고: runs/$RUN_ID/checks/verification1.json" "1차 검증"
    V1="$(jget "$RD/verification.json" verdict "")"
    case "$V1" in
      승인|"조건부 승인")
        end_step "$( [ "$attempt" -gt 0 ] && echo "재시도 ${attempt}회 후 $V1" || echo "$V1" )" "신뢰도 $(jget "$RD/verification.json" confidence)"
        break;;
      반려)
        REASON="$(jget "$RD/verification.json" retry_reason)"
        if [ "$STEP" = "verify1" ]; then end_step "반려" "$REASON"; say "완료(--step verify1): 반려"; exit 0; fi
        if [ "$attempt" -lt "$MAX_RETRIES" ]; then
          attempt=$((attempt + 1))
          cp "$RD/verification.json" "$RD/verification.attempt${attempt}.json"
          cp "$RD/research.json" "$RD/research.attempt${attempt}.json"
          rlog "반려 → 리서치 재실행 ${attempt}/${MAX_RETRIES}: $REASON" "1차 검증"
          end_step "반려(재조사 ${attempt}회차 진행)" "$REASON"
          continue
        fi
        park "1차 검증 반려가 재조사 ${MAX_RETRIES}회 뒤에도 이어짐: $REASON";;
      *)
        park "1차 검증 판정을 읽을 수 없다: '$V1'";;
    esac
  done
  if [ "$STEP" = "verify1" ]; then say "완료(--step verify1): $V1"; exit 0; fi
fi

# ---------------------------------------------------------------------------------------------
# 5·6. 스토리텔러 → 2차 검증 (불통과면 "## 수정 지시"를 붙여 스토리텔러 재실행, 최대 max_retries; 그래도 불통과면 보류)
# ---------------------------------------------------------------------------------------------
V2="$(jget "$RD/verification2.json" verdict "")"
if [ -n "$RESUME" ] && [ -z "$STEP" ] && [ "$V2" = "통과" ]; then
  say "재개: 2차 검증(통과)까지 완료된 실행 — 스토리텔러·2차 검증 건너뜀"
  rlog "재개: 2차 검증 통과 — 스토리텔러·2차 검증 건너뜀" "2차 검증"
elif should_run storytell || should_run verify2; then
  V1="$(jget "$RD/verification.json" verdict "")"
  if [ "$V1" != "승인" ] && [ "$V1" != "조건부 승인" ]; then say "1차 검증이 승인·조건부 승인이 아니어서 스토리텔러를 실행하지 않는다($V1)"; exit 2; fi
  attempt2=0
  story_done=0
  if [ -n "$RESUME" ] && [ -f "$RD/pages.json" ] && [ "$STEP" != "storytell" ]; then story_done=1; fi
  if [ "$STEP" = "verify2" ]; then story_done=1; fi
  while :; do
    if [ "$story_done" = 0 ]; then
      begin_step "스토리텔러"
      if ! "$PY" pipeline/agent_runner.py run --role storyteller --run-id "$RUN_ID" --retry "$attempt2"; then
        park "스토리텔러 에이전트 실패(스키마 불일치 1회 재실행 후에도 실패 또는 호출 오류; 7.3)"
      fi
      end_step "$( [ "$attempt2" -gt 0 ] && echo "재시도 ${attempt2}회 후 성공" || echo 성공 )" "페이지 $(jget "$RD/pages.json" pages | "$PY" -c 'import json,sys; print(len(json.load(sys.stdin)))')개"
      # 형식 검증(코드, 운영 전환 1-2·1-3): 패치 적용 → 분량 초과 절 자동 분리 → 형식 검사 → 퍼블리셔 2~4단계 사전 검사.
      # 실패하면 오류 목록을 붙여 스토리텔러에 형식 수정만 요청한다(최대 max_retries). 그래도 실패하면 보류.
      begin_step "형식 검증"
      ff=0
      while ! "$PY" pipeline/validate_run.py "$RUN_ID" --stage pages; do
        if [ "$ff" -ge "$MAX_RETRIES" ]; then
          park "형식 검증 실패가 형식 수정 재작성 ${MAX_RETRIES}회 뒤에도 남음(runs/$RUN_ID/format_check.md)"
        fi
        ff=$((ff + 1))
        rlog "형식 검증 실패 → 스토리텔러 형식 수정 재작성 ${ff}/${MAX_RETRIES} (runs/$RUN_ID/format_check.md)" "형식 검증"
        if ! "$PY" pipeline/agent_runner.py run --role storyteller --run-id "$RUN_ID" --retry "$attempt2" --format-fix "$ff"; then
          park "스토리텔러 형식 수정 재작성 실패(호출 오류 또는 스키마 불일치)"
        fi
      done
      end_step "$( [ "$ff" -gt 0 ] && echo "형식 수정 ${ff}회 후 통과" || echo 통과 )" "$(cat "$RD/checks/pages_note.txt" 2>/dev/null)"
      if [ "$STEP" = "storytell" ]; then say "완료(--step storytell)"; exit 0; fi
    fi
    story_done=0
    begin_step "2차 검증"
    if ! "$PY" pipeline/agent_runner.py run --role verifier --stage second --run-id "$RUN_ID" --retry "$attempt2"; then
      park "내용 검증 에이전트(2차) 실패(스키마 불일치 1회 재실행 후에도 실패 또는 호출 오류; 7.3)"
    fi
    "$PY" pipeline/validate_run.py "$RUN_ID" --stage verification2 >/dev/null || rlog "2차 검증 산출물 교차 검사 경고: runs/$RUN_ID/checks/verification2.json" "2차 검증"
    V2="$(jget "$RD/verification2.json" verdict "")"
    REASON="$(jget "$RD/verification2.json" retry_reason)"
    case "$V2" in
      통과)
        end_step "$( [ "$attempt2" -gt 0 ] && echo "재시도 ${attempt2}회 후 통과" || echo 통과 )" "신뢰도 $(jget "$RD/verification2.json" confidence)"
        break;;
      "수정 후 재검증"|불통과)
        if [ "$STEP" = "verify2" ]; then end_step "$V2" "$REASON"; say "완료(--step verify2): $V2"; exit 0; fi
        case "$REASON" in "브리프 없음"*) park "2차 검증 불통과(브리프 없음 — 스토리텔러 재실행으로 풀리지 않음): $REASON";; esac
        if [ "$attempt2" -lt "$MAX_RETRIES" ]; then
          attempt2=$((attempt2 + 1))
          cp "$RD/verification2.json" "$RD/verification2.attempt${attempt2}.json"
          cp "$RD/pages.json" "$RD/pages.attempt${attempt2}.json"
          rlog "$V2 → 스토리텔러 재실행 ${attempt2}/${MAX_RETRIES}: ${REASON:-required_fixes 참고}" "2차 검증"
          end_step "$V2(재작성 ${attempt2}회차 진행)" "${REASON:-required_fixes 참고}"
          continue
        fi
        park "2차 검증 ${V2}가 재작성 ${MAX_RETRIES}회 뒤에도 이어짐: ${REASON:-required_fixes 참고}";;
      *)
        park "2차 검증 판정을 읽을 수 없다: '$V2'";;
    esac
  done
  if [ "$STEP" = "verify2" ]; then say "완료(--step verify2): $V2"; exit 0; fi
fi
if [ "$UNTIL" = "verify2" ]; then
  # 배치 실행(pipeline/run_batch.py): 에이전트 단계는 병렬로, 퍼블리셔는 하나씩 따로 부른다(--resume <id> --step publish)
  say "완료(--until verify2): 2차 검증까지 끝났다. 퍼블리셔는 'bash pipeline/run_daily.sh --resume $RUN_ID --step publish'"
  exit 0
fi

# ---------------------------------------------------------------------------------------------
# 7·8. 퍼블리셔 (사양서 6.4: 1 스키마·판정 → 2 프런트매터 → 3 원문 보호 → 4 링크 → 5 반영 → 6 빌드 → 7 커밋 → 8 일일 로그 → 9 알림)
# ---------------------------------------------------------------------------------------------
# 커밋 규칙: 실행 폴더(log.md·timings.json·summary.json)에 쓰는 기록은 모두 퍼블리셔 호출 "전에" 끝낸다. 퍼블리셔(publish.py,
# 보류·중단이면 --log-only)는 자기 단계 기록까지 쓴 뒤 한 번 커밋하고, 이 스크립트는 그 뒤 실행 폴더에 아무것도 쓰지 않는다(say 는 표준 출력).
if [ "$STEP" = "log" ]; then
  begin_step "퍼블리셔"; end_step "성공" "일일 로그만(--step log)"; publish_log_only; exit 0
fi
if should_run publish; then
  begin_step "퍼블리셔"
  rlog "퍼블리셔 시작(no_build=$NO_BUILD no_commit=$NO_COMMIT)" "퍼블리셔"
  # `if ! cmd; then rc=$?` 는 부정된 값(항상 0)을 읽으므로 `cmd || rc=$?` 로 실제 종료 코드를 받는다(ERR 트랩도 걸리지 않는다).
  rc=0
  "$PY" pipeline/publish.py "$RUN_ID" $( [ "$NO_BUILD" = 1 ] && echo --no-build ) $( [ "$NO_COMMIT" = 1 ] && echo --no-commit ) || rc=$?
  if [ "$rc" -ne 0 ]; then
    # 퍼블리셔가 퍼블리셔 단계 실패 기록(timings.json·log.md)과 실패 일일 로그를 이미 썼고 반영은 스냅숏으로 되돌렸다.
    # 보류·준비 중단과 같이 되돌린 상태를 재빌드하고 일일 로그를 커밋한다("run(DATE): … (중단)", 6.4 "빌드 실패 시 롤백·로그").
    publish_log_only
    say "퍼블리셔 실패(exit $rc): $RD/log.md 와 docs/logs/daily/$DATE.md 를 본다. 고친 뒤 'bash pipeline/run_daily.sh --resume $RUN_ID --step publish' 로 다시 시도한다"
    exit 4
  fi
  # 퍼블리셔 단계 결과는 publish.py 가 커밋 전에 기록했다(여기서 end_step 을 부르면 커밋 뒤 미커밋 기록이 남는다)
  say "== 완료: $RUN_ID ($SEL_TYPE) — $(jget "$RD/summary.json" end_state) · 소요 $(jget "$RD/summary.json" duration_sec)초 · 커밋 $(jget "$RD/summary.json" commit 없음) · 로그 docs/logs/daily/$DATE.md"
fi
exit 0
}
