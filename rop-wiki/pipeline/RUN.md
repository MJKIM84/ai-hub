# 일일 파이프라인 실행 절차 (pipeline/RUN.md)

이 문서는 빌드 사양서 7.2(실행 순서)·7.3(실패 처리)·6.4(퍼블리셔 9단계)·7.4(사용자 개입 지점)를 사람이 읽는 절차로 옮긴 것이다. 매일 1회 `pipeline/run_daily.sh` 가 리서치 에이전트 → 내용 검증 에이전트(1차) → 스토리텔러 에이전트 → 내용 검증 에이전트(2차) → 퍼블리셔 순으로 실행되어 그날의 연구영역(또는 중점 연구 트랙의 현재 단계)을 조사·검증·서술하고 위키에 반영한다. 독자용 설명은 [에이전트 소개](../docs/about/agents.md)에, 개입 방법은 [기여·정정 방법](../docs/about/how-to-contribute.md)에 있다.

## 1. 준비물

| 항목 | 확인 방법 | 비고 |
|---|---|---|
| Python 3.11 + `pyyaml`, `jsonschema`, `mkdocs`, `mkdocs-material` | `pip install -r requirements.txt` | `python3 -c "import yaml, jsonschema, mkdocs"` |
| Claude Code CLI(`claude`) 로그인 상태 | `claude --version`, `echo 'Return {"ok":true}' \| claude -p --model claude-opus-5-5 --output-format json --json-schema '{"type":"object","properties":{"ok":{"type":"boolean"}},"required":["ok"]}' --tools ""` | `config/settings.yaml` 의 `claude_bin` 으로 경로를 바꿀 수 있다 |
| 웹 검색 도구(WebSearch) | `python3 pipeline/agent_runner.py probe` → `web_search_available: true` (`claude -p --tools WebSearch` 로 검색 1회) | false 면 실행이 준비 단계에서 중단된다(`web_tools_required`, 7.3) |
| 페이지 열람 도구(WebFetch) | 같은 명령 → `web_fetch_available` (`claude -p --tools WebFetch` 로 `web_fetch_probe_url` 을 1회 연다. 셸 curl 결과는 `details.web_fetch_curl` 참고값일 뿐 판정에 쓰지 않는다 — 프록시 정책이 curl 과 도구에 다르게 적용될 수 있다) | false 면 준비 단계에서 즉시 중단한다(0장 `web_tools_required`, 7.3). 페이지 열람만 막힌 제한 환경에서는 `--allow-no-fetch`(또는 `ROP_ALLOW_NO_FETCH=1`, 설정 `web_fetch_required: false`)로 진행을 허용할 수 있다 — 이때 에이전트에 `web_fetch_available: false` 를 알리고(모든 출처 "원문 미열람", 신뢰도 medium 상한) 로그에 "페이지 열람 불가 — 원문 미열람 모드(사용자 override)"를 남긴다 |
| git 저장소(커밋용) | `git -C .. status` | `settings.repo_root`(기본 `..`)가 저장소 루트다. `git_commit: false` 면 커밋하지 않는다 |
| 설정 파일 | `config/settings.yaml`, `config/rotation.yaml`, `config/priority.yaml`, `config/tracks/<slug>.yaml` | YAML 이 읽히지 않으면 준비 단계에서 중단한다. 항목 설명은 `config/README.md` |
| 사용자 입력(선택) | `config/priority.yaml`(우선 영역·주제·질문·트랙 질문), `inbox/corrections.md`(정정 요청), `experiments/<날짜>-<이름>/`(사용자 실험) | 다음 실행에서 읽힌다 |

문법·구성 점검: `bash -n pipeline/run_daily.sh && python3 -m py_compile pipeline/*.py pipeline/lib/*.py` 와 `bash pipeline/checks/run_all.sh --no-build`.

## 2. 수동 실행 명령 (위키 루트 `rop-wiki/` 에서)

```bash
bash pipeline/run_daily.sh                                   # 오늘(settings.timezone) 정규 실행: 대상 선정 규칙대로
bash pipeline/run_daily.sh --date 2026-09-24 --run-type area_deep_dive --area 7      # 대상을 지정한 실행(드라이런·재현)
bash pipeline/run_daily.sh --run-type track --track manual-capability-ontology --stage 1 --question-ids q1-01,q1-02
bash pipeline/run_daily.sh --run-type weekly_review           # 주간 정리만 따로(리서치 전에 링크·출처 유효성 점검을 스크립트가 먼저 수행한다)
bash pipeline/run_daily.sh --resume 2026-09-24-01             # 있는 산출물부터 이어서(보류 폴더는 자동으로 되돌린다)
bash pipeline/run_daily.sh --resume 2026-09-24-01 --step publish    # 한 단계만
bash pipeline/run_daily.sh --no-build --no-commit             # 빌드·커밋 없이(시험)
bash pipeline/run_daily.sh --allow-no-fetch                   # 페이지 열람 도구가 막힌 환경에서 원문 미열람 모드로 진행(사용자 override)
ROP_ALLOW_NO_FETCH=1 bash pipeline/run_daily.sh               # 같은 override 를 환경변수로(cron 줄에 넣을 때)
```

| 옵션 | 뜻 |
|---|---|
| `--date YYYY-MM-DD` | 실행 날짜(실행 id 의 날짜, 페이지 `updated`·접근일). 기본은 `settings.timezone` 의 오늘. 환경변수 `ROP_TODAY` 도 같다 |
| `--run-type`, `--area`, `--track`, `--stage`, `--question-ids` | 대상 선정 규칙 대신 지정한다. `--question-ids` 는 쉼표로 구분한 백로그 질문 id |
| `--run-id` | 실행 id 를 지정한다(기본 `<date>-<NN>` 자동 부여, 같은 날 두 번째는 `-02`) |
| `--resume <run_id>` | `runs/<run_id>/`(또는 `runs/parked/<run_id>/`)의 산출물이 있는 단계는 건너뛰고 다음 단계부터 이어간다 |
| `--step {prepare\|select\|research\|verify1\|storytell\|verify2\|publish\|log}` | 단일 단계만 실행한다. `prepare`·`select` 외에는 `--resume` 이 필요하다 |
| `--skip-probe` | 드라이런 전용. 웹 도구 점검을 생략한다(기존 `probe.json` 재사용, 없으면 WebSearch 는 점검하지 않고 `web_search_available: null`·로그 "웹 도구 점검 생략(드라이런)"으로 기록, WebFetch 는 curl 참고값만 쓴다). 점검하지 않은 것을 가용으로 기록하지 않는다. 정규(cron) 실행에서는 쓰지 않는다 |
| `--allow-no-fetch` (또는 환경변수 `ROP_ALLOW_NO_FETCH=1`) | 사용자 override: 페이지 열람(WebFetch) 도구를 쓸 수 없어도 중단하지 않고 원문 미열람 모드로 진행한다. 에이전트 실행 컨텍스트에 `web_fetch_available: false` 를 주고, `runs/<id>/log.md`·`probe.json`(`web_fetch_override`)·일일 로그에 "페이지 열람 불가 — 원문 미열람 모드(사용자 override)"를 남긴다. 웹 검색 도구가 없으면 이 옵션과 관계없이 중단한다. 설정으로 계속 허용하려면 `config/settings.yaml` 의 `web_fetch_required: false` |
| `--no-build`, `--no-commit` | 퍼블리셔 6단계(사이트 빌드)·7단계(커밋)를 건너뛴다(8단계의 재빌드와 커밋 해시 기록 커밋도 함께) |

부분 도구를 직접 쓸 수도 있다.

```bash
python3 pipeline/select_target.py --date 2026-09-25 --stdout          # 그날의 대상을 미리 본다(파일·부작용 없음)
python3 pipeline/agent_runner.py probe                                 # 웹 도구 점검
python3 pipeline/agent_runner.py run --role researcher --run-id 2026-09-24-01 --dry-run   # 프롬프트만 만들어 runs/<id>/prompts/ 에 저장
python3 pipeline/publish.py 2026-09-24-01 --check-only                 # 퍼블리셔 1단계(스키마·판정 확인)와 pages.json 링크 필드의 앵커 대조만.
                                                                       # schemas/examples 로 드라이 체크하려면 실행 폴더 이름을 예시의 run_id 와 같게
                                                                       # (runs/2026-09-24-01/) 만든다 — 1단계가 run_id 일치를 검사한다
python3 pipeline/publish.py 2026-09-24-01 --dry-run                    # 1~4단계(프런트매터·원문 보호·링크 검사)까지 하고 되돌림
python3 pipeline/lib/runs.py unpark --run-id 2026-09-24-01             # 보류 산출물 재투입(폴더 되돌리기 + summary 보류 표시 해제; --resume 이 자동으로 한다)
python3 pipeline/render_run_md.py 2026-09-24-01                        # research.md·verification.md 다시 렌더링
```

## 3. 단계별로 읽고 쓰는 파일

실행 폴더는 `runs/<run_id>/` 다(`<run_id>` = `YYYY-MM-DD-NN`). 각 단계의 소요 시간과 결과는 `runs/<run_id>/log.md` 와 `timings.json` 에 남고, 마지막에 퍼블리셔가 일일 로그로 옮긴다.

| 단계 | 스크립트 | 읽는 것 | 쓰는 것 |
|---|---|---|---|
| 1 준비 | `run_daily.sh`, `agent_runner.py probe`, `lib/runs.py` | `config/*.yaml`, 웹 도구(`claude -p` 로 WebSearch 1회·WebFetch 1회, curl 은 참고값), `docs/` | `runs/<id>/log.md`, `probe.json`, `docs_tree.txt` |
| 2 대상 선정 | `select_target.py` | `config/rotation.yaml`, `config/priority.yaml`, `config/tracks/*.yaml`, `runs/*/target.json`·`summary.json`(이력), 세부영역 페이지 `status`, `data/open_questions.json`, `data/flow_matrix.json`, `data/tracks/<slug>/backlog.json`, `inbox/corrections.md` | `runs/<id>/target.json` (3회 연속 보류 영역이 있으면 `data/open_questions.json` 에 검토 요청, 트랙 실행이면 `priority.yaml` 의 `track_questions` 를 `data/tracks/<slug>/backlog.json` 에 등록) |
| 3 리서치 | `agent_runner.py run --role researcher` (주간 정리면 그 전에 `run_daily.sh` 의 `weekly_checks`: `checks/check_links.py`, `checks/check_urls.py --json`) | `agents/shared-rules.md`+`researcher.md`, `target.json`, 대상 영역 페이지, 관련 영역 요약(1·2절), `docs/glossary/index.md`, `docs/references/index.md`, `docs/open-questions.md`, `config/priority.yaml`, `inbox/corrections.md`, 최근 7회 `runs/*/research.md`(보류된 실행 `runs/parked/*/` 도 "(보류)" 라벨로 포함하고 그 `verification.md` 반려 사유를 함께 넣는다. 폐기 표시(`DISCARDED`)한 보류 실행은 뺀다); 비트랙 실행이면 대상 영역의 세부영역 반영 제안(`data/area_reflection_proposals.json` 의 status 제안 항목 — 1차 검증·스토리텔러 입력에도 넣는다); 트랙이면 `config/tracks/<slug>.yaml`, 트랙 개요·현재 단계 페이지·`backlog.json`·온톨로지 초안·단계 산출물 페이지·`experiments/`; 주간 정리면 이번 주 실행들의 산출물, `data/changelog.json`, 스크립트가 남긴 `runs/<id>/link_check.txt`·`url_check.json`(7.1 "링크·출처 유효성 점검" — 페이지 열람이 막힌 환경에서도 결과가 남는다) | `prompts/research.md`(+`.response.json`, `.meta.json`), `research.json`, `research.md`; 주간 정리면 `link_check.txt`, `url_check.json`(+`url_check.txt`) |
| 4 1차 검증 | `agent_runner.py run --role verifier --stage first` | 위 입력 + `research.json` + `_source/` 원문 전문 (+ 재검증이면 직전 `verification.json`) | `prompts/verification1.md`, `verification.json`, `verification.md` |
| 5 스토리텔러 | `agent_runner.py run --role storyteller` | `target.json`, `research.json`, `verification.json`, 대상 페이지·대분류 페이지, `templates/<유형>.md`, 용어집·참고문헌·표준·열린 질문 색인, `docs_tree.txt`, `inbox/corrections.md` (+ 트랙 입력, 재실행이면 이전 `pages.json`·`pages/`·`verification2.json`) | `prompts/storyteller.md`, `pages/<docs 상대 경로>.md`, `pages.json`(content 제거 사본), `pages.md` |
| 6 2차 검증 | `agent_runner.py run --role verifier --stage second` | `research.json`, `verification.json`, `pages.json`, `pages/*`, 갱신 대상의 현재 `docs/` 페이지, `docs_tree.txt`, 색인들, 기준 템플릿 `templates/<유형>.md`(실행 유형별 + `pages.json` 이 만진 페이지 유형별; 섹션 제목·순서 검사용. 주간 정리 페이지(`docs/logs/weekly/`, `type: log`, `tags: [weekly_review]`)는 `daily-log.md` 대신 `templates/weekly-log.md`(있으면) 또는 `agents/storyteller.md` 6절의 주간 정리 절 구성을 기준으로 준다) (+ 재검증이면 직전 `verification2.json`) | `prompts/verification2.md`, `verification2.json`, `verification2.md` |
| 7 퍼블리셔 | `publish.py <id>` (사양서 6.4 의 1~7단계: 1 스키마·판정 확인 → 2 프런트매터·사전 검사 → 3 원문 보호 → 4 링크(파일 존재·각주 정의 + 제목 앵커 대조) → 5 반영 → 6 빌드 → 7 커밋) | 위 산출물 전부, `schemas/*.json`, `pipeline/checks/*`, `mkdocs.yml`(앵커 대조에 쓰는 Markdown 확장 설정) | `docs/`(페이지·용어집·참고문헌·자동 영역 — 트랙 로그 `auto:track-log` 포함), `data/*.json`(세부영역 반영 제안의 누적·반영 표시 포함), `data/tracks/<slug>/*.json`(백로그·트랙 로그 원천 `log.json`·온톨로지 버전 이력), `config/tracks/<slug>.yaml`(단계 전환 시만), `inbox/corrections.md`(상태), `mkdocs.yml`, `site/`, git 커밋, `runs/<id>/build.log` |
| 8 일일 로그·지표 | `publish.py`(8단계 일일 로그 — 7단계 커밋 전에 실행, 9단계 알림) | `runs/<id>/*` | `docs/logs/daily/<date>.md`, `runs/<id>/summary.json`, 자동 영역(`logs-index`, `metrics`), 재빌드, 퍼블리셔 단계 기록(`timings.json`·`log.md`) → 7단계의 실행 커밋 하나에 모두 담긴다(amend 없음). 이어 `summary.json` 의 `committed`·`commit` 만 고친 커밋 해시 기록 커밋 |

프롬프트 조립(에이전트 실행 규약): `agents/shared-rules.md` 전문 + `agents/<role>.md` 전문 + `## 실행 컨텍스트`(run_id, date, run_type, 대상, 예산, 환경 알림, 역할별 `verification_stage`·`retry_count`·`next_ref_id`) + `## 입력`(파일마다 `### <경로>` 소제목과 코드 펜스) + 재실행이면 `## 반려 사유`(리서치) 또는 `## 수정 지시`(스토리텔러). `claude -p --output-format json --json-schema … --tools … --allowedTools … --max-turns N --permission-mode dontAsk` 로 호출하고 응답의 `structured_output` 을 `schemas/*.json` 으로 검사한다.

## 4. 재시도·보류 규칙 (7.3)

| 상황 | 처리 |
|---|---|
| 웹 검색 도구 없음 | 준비 단계에서 즉시 중단. `runs/<id>/log.md` 와 일일 로그에 "중단(웹 검색 도구 없음)" 기록, exit 3 |
| 페이지 열람 도구 없음 | 기본은 웹 검색 도구 없음과 같이 준비 단계에서 즉시 중단(0장 `web_tools_required`, 7.3). `runs/<id>/log.md`·일일 로그에 "즉시 중단: 페이지 열람(WebFetch) 도구를 쓸 수 없다" 기록, exit 3. 사용자 override(`--allow-no-fetch`, `ROP_ALLOW_NO_FETCH=1`, `web_fetch_required: false`)가 있으면 진행하고 실행 컨텍스트에 `web_fetch_available: false` 를 표시하며 로그·일일 로그에 "페이지 열람 불가 — 원문 미열람 모드(사용자 override)"를 남긴다 |
| 설정 YAML 오류 | 준비 단계에서 중단(exit 2) |
| 예산 초과·도달 | 리서치 결과의 `self_check.budget_used` 를 `target.json` 의 예산과 비교해 `log.md` 와 일일 로그의 "예산 사용량" 표에 표시하고 부분 결과로 진행 |
| 스키마 불일치 | 해당 에이전트를 `## 스키마 불일치 (재실행)` 절을 붙여 1회 재실행. 그래도 불일치면 보류(`runs/parked/`) |
| 1차 검증 반려 | `## 반려 사유` 를 붙여 리서치 재실행(최대 `max_retries`, 기본 2회). 직전 판정은 `verification.attemptN.json`, 직전 브리프는 `research.attemptN.json` 으로 남긴다. 여전히 반려면 보류 |
| 2차 검증 수정 후 재검증·불통과 | `## 수정 지시` 를 붙여 스토리텔러 재실행(최대 `max_retries`). 직전 판정은 `verification2.attemptN.json`, 직전 초안은 `pages.attemptN.json`. 여전히 불통과면 보류. `retry_reason` 이 "브리프 없음"으로 시작하면 재실행 없이 바로 보류 |
| 보류 | `runs/<id>/` 전체를 `runs/parked/<id>/` 로 옮기고 `summary.json` 에 `parked: true`·사유(`park_reason`)를 쓴 뒤 일일 로그를 남긴다(exit 2). 같은 영역이 3회 연속 보류되면 다음 대상 선정에서 제외하고 `data/open_questions.json` 에 사용자 검토 요청을 올린다. `config/priority.yaml` 의 `areas` 에 지정하면 제외가 풀리고 다음 실행에서 바로 대상이 된다(보류된 실행은 7일 건너뛰기·최근 감점에서 '다룬 것'으로 세지 않는다). 재투입(`--resume`)하면 `parked: false`·`end_state: 재투입` 으로 바뀌고 사유는 `resumed_from_park_reason` 으로 옮겨져 연속 보류 횟수에 더 세어지지 않는다 |
| 퍼블리셔 검사 실패(1 스키마·판정, 2 프런트매터·사전 검사, 3 원문 보호, 4 링크) | 아무것도 반영하지 않는다. docs 에 임시 복사한 페이지는 스냅숏(`runs/<id>/backup/`)으로 되돌린다. 실행 폴더는 `runs/` 에 남고 일일 로그에 "중단(퍼블리셔: …)" 을 쓴 뒤, `run_daily.sh` 가 `publish.py --log-only` 로 되돌린 상태를 재빌드하고 그 로그를 커밋한다(`run(DATE): … (중단)`, exit 4). 참고문헌 id 충돌·온톨로지 버전 불일치·deprecated 페이지의 `replaced_by` 없음은 2단계 사전 검사에서 걸린다 |
| 퍼블리셔 5단계(반영) 도중 실패 | 스냅숏으로 `docs`·`data`·`config/tracks`·`mkdocs.yml`·`inbox/corrections.md` 를 되돌린다(부분 반영을 남기지 않는다, 6.4). `git checkout` 은 쓰지 않으므로 사용자의 미커밋 `inbox/corrections.md`·`config/tracks` 수정은 보존된다 |
| 사이트 빌드 실패(6단계) | 5단계 반영을 같은 스냅숏으로 되돌리고 `runs/<id>/build.log` 와 로그에 남긴다 |
| 커밋 실패(7단계) | 파일은 반영된 채 두고 실패로 기록한다(빌드는 성공한 상태, 스냅숏은 커밋 직전에 지운다). `git` 문제를 고친 뒤 `--resume <id> --step publish` 로 다시 시도한다 |
| 확정 로그 재빌드 실패(8단계, 커밋 전) | 확정 일일 로그·자동 영역·`mkdocs.yml` 만 6단계 빌드 시점(예비 로그)으로 되돌리고 그 상태로 7단계 커밋을 한다(빌드가 깨진 상태를 커밋에 넣지 않는다). 5단계의 반영은 유지된다. `runs/<id>/build-final.log` 와 `summary.json` 의 `final_log_rebuild_failed` 를 보고 원인을 고친 뒤 `--resume <id> --step log` 로 확정 로그를 다시 쓴다 |

## 5. `--resume` 사용법

1. 어디서 멈췄는지 본다: `runs/<id>/log.md`(또는 `runs/parked/<id>/log.md`)의 마지막 줄과 `summary.json` 의 `end_state`.
2. 원인을 고친다(정정 요청·우선 지정을 손보거나, 네트워크·git 문제를 해결한다). 보류 산출물은 `verification.md`·`verification2.md` 의 사유를 읽고 `research.md`·`pages/` 를 본다.
3. 재투입: `bash pipeline/run_daily.sh --resume <id>`. `runs/parked/<id>/` 만 있으면 스크립트가 `python3 pipeline/lib/runs.py unpark` 로 `runs/<id>/` 로 되돌리고 `summary.json` 의 보류 표시를 지운다(`parked: false`, `end_state: 재투입`, `park_reason` → `resumed_from_park_reason`). 산출물이 있는 단계는 건너뛴다.
   - `target.json` 이 있으면 대상 선정을 건너뛴다.
   - `research.json` 이 있으면 리서치를 건너뛰고 1차 검증부터 한다. 1차 판정이 승인·조건부 승인이면 스토리텔러부터.
   - `pages.json` 이 있으면 스토리텔러를 건너뛰고 2차 검증부터. 2차 판정이 통과면 퍼블리셔부터.
   - `summary.json` 의 `published` 가 true 면 아무것도 하지 않는다.
4. 특정 단계만 다시 하려면 `--step` 을 더한다. 예: 브리프를 다시 쓰게 하려면 `--resume <id> --step research`, 퍼블리셔만 다시 하려면 `--resume <id> --step publish`.
5. 폐기하려면 `runs/parked/<id>/DISCARDED` 파일에 날짜와 사유를 한 줄 적는다(폴더는 기록으로 남긴다). 폐기한 실행의 `research.md`·반려 사유는 다음 실행의 입력("최근 7회 실행의 research.md")에서 빠진다(`agent_runner.py`, `lib/runs.py is_discarded`). 연속 보류 횟수에는 그대로 세므로, 그 영역을 다시 다루려면 `config/priority.yaml` 의 `areas` 에 지정한다 [가정].

## 6. 스케줄

`pipeline/cron.example` 이 예시다(`CRON_TZ=Asia/Seoul`, `0 6 * * *`, 출력은 `runs/cron.log`). 등록은 `bash pipeline/install_cron.sh`, 해제는 `bash pipeline/uninstall_cron.sh`, 등록 확인은 `crontab -l`. 등록 시각과 시간대는 `config/settings.yaml` 의 `run_time`(0장, 예 `"06:00 Asia/Seoul"` → `0 6 * * *`)과 `timezone` 에서 읽으므로 0장 설정을 바꿨으면 `install_cron.sh` 를 다시 실행하면 된다. 설정과 다르게 등록하려면 `--schedule "0 7 * * *"`·`--tz UTC` 로 덮어쓴다(`--dry-run` 으로 등록할 블록만 볼 수 있다). cron 이 `CRON_TZ` 를 지원하지 않으면 `cron.example` 의 주석대로 시각을 서버 시간대로 환산한다.

등록·해제·확인·수동 실행·문제 해결의 정본은 이 문서다. 위키 루트 `README.md`(사양서 9장 단계 4, 완료 기준 7 "README로 재현")는 다음 다섯 항목을 이 문서의 절로 링크한다(README 담당). `README.md` 가 없거나 링크가 빠져 있으면 이 표로 채운다.

| README 항목 | 명령 | 이 문서의 절 |
|---|---|---|
| 스케줄 등록 | `bash pipeline/install_cron.sh` (`--dry-run` 으로 미리 보기) | 6절 |
| 스케줄 해제 | `bash pipeline/uninstall_cron.sh` | 6절 |
| 등록 확인 | `crontab -l` (마커 `# rop-wiki:begin` ~ `# rop-wiki:end` 사이가 등록 블록), 실행 기록은 `runs/cron.log` | 6절 |
| 수동 실행 | `bash pipeline/run_daily.sh` (대상 지정·재개·단계 실행 옵션) | 2절 |
| 문제 해결 | 증상별 확인·조치 표 | 7절 (재시도·보류 규칙은 4절, `--resume` 은 5절) |

## 7. 문제 해결

| 증상 | 확인·조치 |
|---|---|
| `claude 실행 파일을 찾을 수 없다` | `which claude`; cron 이면 `install_cron.sh` 가 넣은 `PATH` 줄을 확인한다. `settings.claude_bin` 에 절대 경로를 적어도 된다 |
| `claude 오류 응답: API Error 400 … input_schema does not support oneOf/allOf` | `agent_runner.py` 가 스키마를 CLI 용으로 바꾸지 못한 경우다. `schemas/*.json` 을 고쳤다면 최상위 `allOf/oneOf/anyOf` 를 쓰지 말고 `lib/runs.py` 의 `cli_schema()` 를 확인한다 |
| `--json-schema is not a valid JSON Schema` / `strict mode: missing type` | 같은 원인. `cli_schema()` 가 `$schema`·`$id`·`$defs` 를 빼고 하위 스키마에 `type` 을 보충하는지 확인한다 |
| 에이전트 호출 시간 초과 | `settings.agent_timeout_sec`(기본 1800초)와 `max_turns` 를 본다. 재실행은 `--resume <id> --step <단계>` |
| `web_search_available: false` 로 중단 | `claude -p --tools WebSearch` 가 동작하는지, 네트워크 정책이 검색을 막는지 확인한다 |
| "즉시 중단: 페이지 열람(WebFetch) 도구를 쓸 수 없다" / `web_fetch_available: false` 인데 curl 로는 열린다(또는 반대) | 판정은 `claude -p --tools WebFetch` 결과다. `runs/<id>/probe.json` 의 `details.web_fetch`(도구)와 `details.web_fetch_curl`(참고값)을 비교하고, 도구 쪽 프록시 정책을 본다. 네트워크 정책으로 열람이 막힌 환경에서 그래도 실행하려면 `--allow-no-fetch`(또는 `ROP_ALLOW_NO_FETCH=1`)로 원문 미열람 모드를 허용한다 — 에이전트가 모든 출처에 "원문 미열람"을 표시하고 신뢰도 medium 상한을 적용하며, 로그에 "페이지 열람 불가 — 원문 미열람 모드(사용자 override)"가 남는다 |
| 퍼블리셔 2단계 사전 검사 실패(참고문헌 id 충돌·온톨로지 버전 불일치·`replaced_by` 없음) | `pages.json`·`pages/` 를 고친다. 참고문헌 id 는 `docs/references/` 의 다음 번호로, 온톨로지 초안의 `ontology_version` 은 `track_updates.ontology_draft_version` 과 같게 맞춘다. 반영 전이라 되돌릴 것은 없다 |
| 퍼블리셔 3단계 원문 보호 검사 실패 | 출력의 diff 를 본다. 스토리텔러가 `[분류원문]` 문장·절 제목을 바꾼 경우다. `pages/` 를 고쳐 `--resume <id> --step publish` 하거나 보류로 넘긴다 |
| 4단계 링크 검사 실패 | 깨진 상대 경로·정의 없는 각주. `runs/<id>/pages/` 에서 고친 뒤 재시도 |
| 4단계 제목 앵커 검사 실패(`앵커 없음 …`) | 페이지 링크 또는 `pages.json` 의 링크 필드(`open_question_updates[].link`, `flow_matrix_updates[].link`, `track_updates.backlog_updates[].answer_link`)의 `#앵커` 가 대상 페이지의 제목 id 에 없다. 오류 줄에 대상 페이지의 실제 id 목록이 나온다. `mkdocs.yml` 의 기본 toc slugify 는 한글을 버리므로 `## 3. 조사 결과` 의 앵커는 `#3` 이고 한글만인 제목은 `#_1` 같은 자동 id 가 된다. 안정된 앵커가 필요하면 `### q1-02 …` 처럼 영숫자 id 로 시작하는 소제목을 쓰거나(`#q1-02`) 앵커 없이 파일 링크만 쓴다. `schemas/examples/pages.track.json` 의 `answer_link`(`#3-조사-결과`)는 이 검사를 통과하지 못하는 형태다(예시 담당에게 `#q1-02` 형식으로 고쳐 달라고 요청) |
| `mkdocs build --strict` 실패(6단계) | `runs/<id>/build.log`. 보통 내비게이션·링크 경고. 롤백된 상태이므로 원인 수정 후 `--resume <id> --step publish` |
| 확정 로그 재빌드 실패(8단계) | `runs/<id>/build-final.log`. 반영은 유지되고 확정 로그만 예비 로그로 되돌려진 채 커밋됐다. 원인 수정 후 `--resume <id> --step log`(로그 커밋이 하나 더 생긴다) |
| git 커밋 실패(identity 없음 등) | `git config user.name`/`user.email` 을 설정한다(없으면 스크립트가 임시 identity 로 커밋한다). 푸시는 `git_push: true` 일 때만 |
| 같은 날 두 번째 실행 | 실행 id 가 `-02` 로 붙고 일일 로그에 실행 블록이 최신순으로 추가된다 |
| 예산 초과 표시 | 일일 로그 "예산 사용량" 표에 초과·도달이 보이면 에이전트가 부분 결과로 마쳤다는 뜻이다. `config/settings.yaml` 의 `daily_budget` 을 조정한다 |
| 산출물 확인 | `runs/<id>/research.md`, `verification.md`, `verification2.md`, `pages.md`, `log.md`, `summary.json`; 사이트는 `site/` 또는 `mkdocs serve` |

## 8. 사용자 개입 지점 가운데 절차가 필요한 것 (7.4)

### 8.1 에이전트 프롬프트를 고칠 때

`agents/shared-rules.md`, `researcher.md`, `verifier.md`, `storyteller.md` 를 고치면 다음 두 가지를 함께 한다(사양서 7.4 "에이전트 프롬프트 변경: `agents/` 에 버전 표기, 변경 이력에 기록").

1. 파일 머리의 `version: <major>.<minor> (<날짜>)` 줄을 올린다. 규칙을 더하거나 빼면 major, 문구·서식만 다듬으면 minor 를 올린다 [가정]. 실행 프롬프트는 파일 전문을 그대로 붙이므로 다음 실행부터 바로 적용된다.
2. `data/changelog.json` 의 `items` 에 항목을 더한다(퍼블리셔가 다음 실행에서 `docs/changelog.md` 의 auto 영역을 다시 만든다). 형식은 다른 항목과 같다.

   ```json
   {"date": "2026-09-25", "run_id": "manual-2026-09-25", "action": "갱신",
    "page": "agents/researcher.md", "summary": "리서치 에이전트 프롬프트 1.0 → 1.1: 트랙 출처 규칙 문구 보강"}
   ```

   `run_id` 는 실행이 아니므로 `manual-<날짜>` 로 쓴다 [가정]. 규칙을 완화하는 변경은 사용자 확인 없이 하지 않는다(사양서 10장).
3. 고친 뒤 `python3 pipeline/agent_runner.py run --role <역할> --run-id <최근 id> --dry-run` 으로 프롬프트가 조립되는지 본다.

### 8.2 `checkpoints: true` 의 멈춤 지점

`config/settings.yaml` 의 `checkpoints`(0장)가 `true` 면 구축 순서(사양서 9장)의 두 지점에서 사용자 확인을 받는다. 일일 파이프라인 자체는 이 값에 따라 멈추지 않는다.

| 멈춤 지점 | 시점 | 보여 주는 것 | 확인 방법 |
|---|---|---|---|
| 1 | 단계 1 뼈대 생성 뒤 | 저장소 구조, 홈·소개 페이지, 원문 보호 검사 결과(`bash pipeline/checks/run_all.sh --no-build`) | 구축자가 결과를 보고하고 사용자가 확인한 뒤 단계 2(에이전트·파이프라인)로 간다 |
| 2 | 단계 3 드라이런 두 번(7. 화물·재고·자산 식별과 추적 영역 심화, 트랙 단계 1) 뒤 | 드라이런 산출물(`runs/<id>/`), 소요 시간·예산 사용량(`docs/logs/daily/<date>.md` 의 표), 결과 페이지·변경 이력·트랙 로그 | 사용자가 확인한 뒤 단계 4(스케줄 등록, 6절)로 간다 |

`false` 면 두 지점을 멈추지 않고 지나간다. 값은 구축 순서에만 쓰이며 실행 스크립트는 읽지 않는다 [가정].

## 9. 이 절차서가 정한 것 [가정]

- `runs/<id>/pages/` 는 `docs/` 기준 상대 경로 구조로 푼다(같은 이름의 `index.md` 충돌을 피한다).
- 재실행 회차는 실행 컨텍스트 `retry_count` 로, 직전 판정·산출물은 `*.attemptN.json` 으로 남긴다.
- 스토리텔러 반환값은 `pages.schema.json` 의 `$defs/returned`(모든 페이지에 `content` 필수)로 검사한다.
- 퍼블리셔 단계 번호는 사양서 6.4 그대로다(1 스키마 → 2 프런트매터 → 3 원문 보호 → 4 링크 → 5 반영 → 6 빌드 → 7 커밋 → 8 일일 로그 → 9 알림). 판정 확인은 1단계의 일부(1b)이고, 참고문헌 id 충돌·온톨로지 버전 대조·`replaced_by` 검사는 2단계의 사전 검사로 앞당겨 스냅숏 이전에 실패시킨다.
- 퍼블리셔는 5단계에서 예비 일일 로그·요약을 쓰고, 6단계 빌드 뒤 8단계(확정 일일 로그·요약·재빌드)를 7단계 커밋 "전에" 실행한 다음 퍼블리셔 단계 기록(`timings.json`·`log.md`)까지 쓰고 한 번만 커밋한다(amend 없음). 커밋 뒤에는 실행 폴더에 로그를 쓰지 않는다(이후 메시지는 표준 출력). `run_daily.sh` 도 퍼블리셔를 부른 뒤에는 실행 폴더에 쓰지 않는다. 커밋 해시는 그 커밋 안의 `summary.json` 에 넣을 수 없으므로(파일 내용이 해시를 정한다) `summary.json` 의 `committed`·`commit` 두 필드만 고친 기록 커밋(`run(DATE): 커밋 해시 기록 <run_id> → <hash>`)을 바로 뒤에 만든다. 그래서 `commit` 은 브랜치에 있는 실행 커밋을 가리키고, 실행이 쓴 파일은 모두 커밋된다. 재빌드가 실패하면 확정 로그 변경분만 되돌리고 예비 로그로 커밋한다. 사양서 6.4 의 7 → 8 순서는 커밋에 담기는 내용으로 지킨다(번호는 그대로 쓴다).
- 커밋은 `git commit -- <퍼블리셔 경로>` 로 `docs`·`data`·`config`·`mkdocs.yml`·`inbox`·`runs/<id>`·`runs/parked/<id>` 만 담는다(사용자가 다른 파일을 스테이지해 두었어도 섞지 않는다). 실행 폴더는 두 위치를 모두 넣어 보류·재투입으로 옮긴 폴더의 이전 위치 삭제도 같은 커밋에 들어간다.
- 퍼블리셔가 실패(exit 4)하면 `run_daily.sh` 가 보류·준비 중단과 같이 `publish.py --log-only` 로 되돌린 상태를 재빌드하고 실패 일일 로그를 커밋한다(`run(DATE): … (중단)`).
- 트랙 로그 페이지의 "실행 기록"은 자동 갱신 영역 `auto:track-log` 이다. 퍼블리셔가 트랙 실행마다 `data/tracks/<slug>/log.json` 에 여덟 항목(사양서 5.4)을 담은 항목을 더하고, `refresh_all_auto_regions()`(`lib/render.py render_track_log`)가 최신순으로 다시 만든다. 퍼블리셔 5·8단계는 `refresh_all_auto_regions(strict=True)` 로 부르므로 영역 하나라도 렌더하지 못하거나 등록되지 않은 키가 있으면 반영하지 않는다(6.4).
- 세부영역 반영 제안(6.3 절차 9, 8.2 (5)): 트랙 실행의 `area_reflection_proposals` 는 `data/area_reflection_proposals.json` 에 status "제안"으로 쌓인다. 그 영역을 대상으로 하는 다음 비트랙 실행에서 `agent_runner.py` 가 그 영역의 "제안" 항목(그 실행보다 앞선 실행이 낸 것)을 리서치·1차 검증·스토리텔러 입력(`### data/area_reflection_proposals.json (…)`)과 실행 컨텍스트("세부영역 반영 제안")에 넣고, 퍼블리셔가 그 영역 페이지를 게시하면 status 를 "반영"으로 바꾸고 `reflected_run_id`·`reflected_date` 를 적는다. 영역 페이지를 갱신하지 않은 실행(주제 페이지만 쓴 경우)은 "제안"으로 남겨 다음 해당 영역 실행에 다시 넣는다. 미반영 건수는 일일 로그 "다음 실행 메모"에 남는다.
- 대상 선정의 최근 7일 건너뛰기(`priority.skip_if_targeted_within_days`)와 2주기 최근 감점은 게시까지 간 실행만 '다룬 것'으로 센다. 3회 연속 보류로 제외된 영역을 `priority.yaml` 의 `areas` 로 풀면 다음 실행에서 바로 대상이 된다.
- 트랙 실행의 대상 선정은 `priority.yaml` 의 `track_questions` 를 백로그에 제기 근거 "사용자"로 먼저 등록한 뒤 질문 id 를 고른다(퍼블리셔 5단계의 등록은 보완). 그래서 새 사용자 질문도 첫 트랙 실행에서 q-id 로 답할 수 있다.
- 스냅숏 복원은 파일 복사만 쓰고 `git checkout` 을 쓰지 않는다(사용자의 미커밋 `inbox/corrections.md`·`config/tracks` 수정 보존). 커밋(7단계) 뒤의 실패는 되돌리지 않고 기록한다.
- 보류·중단된 실행도 일일 로그(`publish.py --log-only`)를 남긴다. 그 커밋 메시지는 6.4 형식을 유지한 채 종료 상태를 괄호로 덧붙인다: `run(DATE): <실행 유형> <대상 영역 이름> — 생성 0/갱신 0 (보류)`. 사양서는 보류·중단 실행의 커밋 형식을 따로 정하지 않았다.
- 커밋 메시지의 `<대상 영역 이름>` 자리: 주간 정리는 대상 영역이 없으므로 ISO 주를 쓴다(`run(2026-09-30): 주간 정리 2026-W40 — 생성 1/갱신 0`), 월간 재검증은 대상 영역이 있으면 그 이름, 없으면 비운다(`run(2026-10-01): 월간 재검증 — 생성 1/갱신 0`). 실행 유형 라벨과 겹치는 문구("주간 정리 주간 정리", "월간 재검증 월간 재검증")를 넣지 않는다. 트랙 실행의 부가 정보(트랙 이름·단계·다룬 질문 id)는 6.4 제목 형식에 없는 요소이므로 제목이 아니라 커밋 본문(둘째 줄, `트랙: … · 단계 n. … · 질문 …`)에 둔다.
- 대상 선정 전에 중단된 실행의 실행 유형은 일일 로그에 "미선정", `summary.json` 에 `null` 로 쓴다(기본값 `topic` 을 넣지 않는다).
- 월간 재검증의 "이달 첫 실행"은 게시까지 간 비트랙 실행 또는 월간 재검증 실행으로 센다. 중단·보류된 실행과 트랙 실행은 세지 않는다. CLI 로 `--run-type` 을 지정한 실행(`target.json` 의 `forced: true`, 9장 단계 3 의 드라이런)도 게시까지 갔으면 센다 — 빼면 드라이런(9-24)·트랙 드라이런(9-25) 뒤 첫 정규 비트랙 실행(9-26)이 재검증할 게시 페이지가 거의 없는 상태에서 월간 재검증이 되어 1주기 시작이 하루 늦어진다. [사용자 결정 항목. 기본값: 드라이런을 이달 첫 실행으로 센다(9-26 은 1주기 첫 영역 심화) / 대안 1: 드라이런을 빼고 9-26 을 월간 재검증으로 한다 / 대안 2: 월간 재검증에 "재검증할 published 페이지·발행 2년 경과 출처가 있을 때만" 조건을 더한다(미구현)]
- 퍼블리셔 4단계는 파일 존재·각주 정의(`check_links.py`) 외에 `경로#앵커` 링크와 `pages.json` 의 링크 필드 세 곳의 앵커를 대상 페이지의 실제 제목 id 와 대조한다. id 는 `mkdocs.yml` 의 `markdown_extensions` 설정(`mkdocs.config.load_config`)으로 본문을 변환해 얻으므로 6단계 `mkdocs build --strict`(`validation.links.anchors`)와 같은 기준이다. 사양서 6.4 는 4단계를 "내부 링크·각주 검사"로만 적었고, 이 대조는 빌드 실패(전체 롤백)를 4단계에서 미리 잡기 위해 더한 것이다. 한글 제목에 안정된 앵커를 주려면 `mkdocs.yml` 템플릿(`lib/nav.py`)의 toc 에 유니코드 slugify(`pymdownx.slugs`)를 설정하는 방법이 있으며(nav 담당·사용자 결정), 그러면 이 검사도 그 설정을 따라간다.
- 용어집 한 줄 정의의 사실 태그는 퍼블리셔가 정하지 않는다(5.3 주장 단위 태그, 6.2 강등 판정은 검증 에이전트 몫). `glossary_updates[].tag`(사실|추정|의견)를 스토리텔러가 주면 그대로 쓰고, 없거나 값이 다르면 `[추정]` 으로 둔다(참고문헌 id 가 있어도 `[사실]` 로 올리지 않는다). `schemas/pages.schema.json` 의 `glossary_updates` 항목에 `tag` 필드를 두고 2차 검증 항목에 넣는 것은 스키마·에이전트 담당에게 요청한다(필드가 추가되기 전까지는 언제나 `[추정]`).
- 트랙 백로그의 제기 근거(8.2: finding id 또는 "사용자"): "사용자"는 `config/priority.yaml` 의 `track_questions` 에서 온 질문에만 쓴다. 에이전트가 낸 질문에 근거 finding id 가 없거나(`backlog_updates[].origin` 없음, `track.new_questions[].rationale_finding_id` 없음) 근거 없이 "사용자"라고 적혀 있으면 `run:<run_id>`(에이전트 제기, 근거 미기재)로 기록하고 퍼블리셔 메모에 남긴다. 사용자 제기와 섞이지 않게 하기 위한 것이며, 등록 거부는 하지 않는다.
- 홈·대분류·세부영역의 "최근 업데이트"는 사양서 4.1·4.3 대로 `data/changelog.json` 행에서 자동 생성한다(`lib/render.py`). 스토리텔러가 내는 `index_updates`(부록 B.3: `home_recent`, `category_recent`, `area_recent`)는 페이지에 직접 쓰지 않고 그 실행의 changelog "요약" 행에 `index_updates` 로 기록만 남긴다(기록용). 이 점을 `schemas/pages.schema.json` 의 설명과 `agents/storyteller.md` 에도 적는 것은 스키마·에이전트 담당에게 요청한다.
- 주간 정리(7.1)의 "링크·출처 유효성 점검"은 리서치 에이전트의 WebFetch 에 맡기지 않고 `run_daily.sh` 가 리서치 전에 `checks/check_links.py` 와 `checks/check_urls.py --json` 을 실행해 `runs/<id>/link_check.txt`·`url_check.json` 으로 남기고, 이를 리서치·1차 검증·스토리텔러 입력(`### runs/<id>/url_check.json (…)`)에 넣는다. 퍼블리셔는 일일 로그 "다음 실행 메모"에 URL 열림·오류·미확인 건수와 내부 링크 오류 건수를 옮긴다. 외부 접속이 막힌 환경에서는 전부 "미확인"으로 남는다(파일 결함이 아니므로 실행을 멈추지 않는다).
- 페이지 열람(WebFetch) 불가 시에는 사양서 0장·7.3 원문대로 중단한다(`web_fetch_required: true`). 예외는 사용자 override(`--allow-no-fetch`, `ROP_ALLOW_NO_FETCH=1`, `web_fetch_required: false`)뿐이며, 이때 원문 미열람 모드(모든 출처 "원문 미열람", 신뢰도 medium 상한)로 진행하고 로그·일일 로그에 "페이지 열람 불가 — 원문 미열람 모드(사용자 override)"를 남긴다(4절). override 수단은 사양서에 없어 구축자가 정했다.
- 용어집 반영은 새 파일을 만들기 전에 `docs/glossary/*.md` 의 `term_ko`·`term_en`(대소문자·공백·괄호 약어 무시)과 색인의 용어명을 대조해 같은 용어면 그 페이지를 갱신한다(예: term_en "Electronic Product Code Information Services" 는 `glossary/epcis.md` 갱신).
