# 일일 파이프라인 실행 절차 (pipeline/RUN.md)

이 문서는 빌드 사양서 7.2(실행 순서)·7.3(실패 처리)·6.4(퍼블리셔 9단계)·7.4(사용자 개입 지점)를 사람이 읽는 절차로 옮긴 것이다. 매일 1회 `pipeline/run_daily.sh` 가 리서치 에이전트 → 내용 검증 에이전트(1차) → 스토리텔러 에이전트 → 내용 검증 에이전트(2차) → 퍼블리셔 순으로 실행되어 그날의 연구영역(또는 중점 연구 트랙의 현재 단계)을 조사·검증·서술하고 위키에 반영한다. 독자용 설명은 [에이전트 소개](../docs/about/agents.md)에, 개입 방법은 [기여·정정 방법](../docs/about/how-to-contribute.md)에 있다.

## 1. 준비물

| 항목 | 확인 방법 | 비고 |
|---|---|---|
| Python 3.11 + `pyyaml`, `jsonschema`, `mkdocs`, `mkdocs-material` | `pip install -r requirements.txt` | `python3 -c "import yaml, jsonschema, mkdocs"` |
| Claude Code CLI(`claude`) 로그인 상태 | `claude --version`, `echo 'Return {"ok":true}' \| claude -p --output-format json --json-schema '{"type":"object","properties":{"ok":{"type":"boolean"}},"required":["ok"]}' --tools ""` | `config/settings.yaml` 의 `claude_bin` 으로 경로를 바꿀 수 있다 |
| 웹 검색 도구(WebSearch) | `python3 pipeline/agent_runner.py probe` → `web_search_available: true` | false 면 실행이 준비 단계에서 중단된다(`web_tools_required`, 7.3) |
| 페이지 열람(WebFetch, `web_fetch_probe_url` 로 curl HEAD) | 같은 명령 → `web_fetch_available` | false 면 기본 설정(`web_fetch_required: false`)에서는 계속 진행하고 에이전트에 `web_fetch_available: false` 를 알린다(모든 출처 "원문 미열람", 신뢰도 medium 상한) |
| git 저장소(커밋용) | `git -C .. status` | `settings.repo_root`(기본 `..`)가 저장소 루트다. `git_commit: false` 면 커밋하지 않는다 |
| 설정 파일 | `config/settings.yaml`, `config/rotation.yaml`, `config/priority.yaml`, `config/tracks/<slug>.yaml` | YAML 이 읽히지 않으면 준비 단계에서 중단한다. 항목 설명은 `config/README.md` |
| 사용자 입력(선택) | `config/priority.yaml`(우선 영역·주제·질문·트랙 질문), `inbox/corrections.md`(정정 요청), `experiments/<날짜>-<이름>/`(사용자 실험) | 다음 실행에서 읽힌다 |

문법·구성 점검: `bash -n pipeline/run_daily.sh && python3 -m py_compile pipeline/*.py pipeline/lib/*.py` 와 `bash pipeline/checks/run_all.sh --no-build`.

## 2. 수동 실행 명령 (위키 루트 `rop-wiki/` 에서)

```bash
bash pipeline/run_daily.sh                                   # 오늘(settings.timezone) 정규 실행: 대상 선정 규칙대로
bash pipeline/run_daily.sh --date 2026-09-24 --run-type area_deep_dive --area 7      # 대상을 지정한 실행(드라이런·재현)
bash pipeline/run_daily.sh --run-type track --track manual-capability-ontology --stage 1 --question-ids q1-01,q1-02
bash pipeline/run_daily.sh --run-type weekly_review           # 주간 정리만 따로
bash pipeline/run_daily.sh --resume 2026-09-24-01             # 있는 산출물부터 이어서(보류 폴더는 자동으로 되돌린다)
bash pipeline/run_daily.sh --resume 2026-09-24-01 --step publish    # 한 단계만
bash pipeline/run_daily.sh --no-build --no-commit             # 빌드·커밋 없이(시험)
```

| 옵션 | 뜻 |
|---|---|
| `--date YYYY-MM-DD` | 실행 날짜(실행 id 의 날짜, 페이지 `updated`·접근일). 기본은 `settings.timezone` 의 오늘. 환경변수 `ROP_TODAY` 도 같다 |
| `--run-type`, `--area`, `--track`, `--stage`, `--question-ids` | 대상 선정 규칙 대신 지정한다. `--question-ids` 는 쉼표로 구분한 백로그 질문 id |
| `--run-id` | 실행 id 를 지정한다(기본 `<date>-<NN>` 자동 부여, 같은 날 두 번째는 `-02`) |
| `--resume <run_id>` | `runs/<run_id>/`(또는 `runs/parked/<run_id>/`)의 산출물이 있는 단계는 건너뛰고 다음 단계부터 이어간다 |
| `--step {prepare\|select\|research\|verify1\|storytell\|verify2\|publish\|log}` | 단일 단계만 실행한다. `prepare`·`select` 외에는 `--resume` 이 필요하다 |
| `--skip-probe` | 웹 도구 점검을 생략한다(기존 `probe.json` 재사용, 없으면 WebSearch 점검만 생략) |
| `--no-build`, `--no-commit` | 퍼블리셔 7·8단계를 건너뛴다 |

부분 도구를 직접 쓸 수도 있다.

```bash
python3 pipeline/select_target.py --date 2026-09-25 --stdout          # 그날의 대상을 미리 본다(파일·부작용 없음)
python3 pipeline/agent_runner.py probe                                 # 웹 도구 점검
python3 pipeline/agent_runner.py run --role researcher --run-id 2026-09-24-01 --dry-run   # 프롬프트만 만들어 runs/<id>/prompts/ 에 저장
python3 pipeline/publish.py 2026-09-24-01 --check-only                 # 스키마·판정만 확인
python3 pipeline/publish.py 2026-09-24-01 --dry-run                    # 원문 보호·링크 검사까지 하고 되돌림
python3 pipeline/render_run_md.py 2026-09-24-01                        # research.md·verification.md 다시 렌더링
```

## 3. 단계별로 읽고 쓰는 파일

실행 폴더는 `runs/<run_id>/` 다(`<run_id>` = `YYYY-MM-DD-NN`). 각 단계의 소요 시간과 결과는 `runs/<run_id>/log.md` 와 `timings.json` 에 남고, 마지막에 퍼블리셔가 일일 로그로 옮긴다.

| 단계 | 스크립트 | 읽는 것 | 쓰는 것 |
|---|---|---|---|
| 1 준비 | `run_daily.sh`, `agent_runner.py probe`, `lib/runs.py` | `config/*.yaml`, 웹 도구(WebSearch 1회, `web_fetch_probe_url` HEAD), `docs/` | `runs/<id>/log.md`, `probe.json`, `docs_tree.txt` |
| 2 대상 선정 | `select_target.py` | `config/rotation.yaml`, `config/priority.yaml`, `config/tracks/*.yaml`, `runs/*/target.json`·`summary.json`(이력), 세부영역 페이지 `status`, `data/open_questions.json`, `data/flow_matrix.json`, `data/tracks/<slug>/backlog.json`, `inbox/corrections.md` | `runs/<id>/target.json` (3회 연속 보류 영역이 있으면 `data/open_questions.json` 에 검토 요청) |
| 3 리서치 | `agent_runner.py run --role researcher` | `agents/shared-rules.md`+`researcher.md`, `target.json`, 대상 영역 페이지, 관련 영역 요약(1·2절), `docs/glossary/index.md`, `docs/references/index.md`, `docs/open-questions.md`, `config/priority.yaml`, `inbox/corrections.md`, 최근 7회 `runs/*/research.md`; 트랙이면 `config/tracks/<slug>.yaml`, 트랙 개요·현재 단계 페이지·`backlog.json`·온톨로지 초안·단계 산출물 페이지·`experiments/` | `prompts/research.md`(+`.response.json`, `.meta.json`), `research.json`, `research.md` |
| 4 1차 검증 | `agent_runner.py run --role verifier --stage first` | 위 입력 + `research.json` + `_source/` 원문 전문 (+ 재검증이면 직전 `verification.json`) | `prompts/verification1.md`, `verification.json`, `verification.md` |
| 5 스토리텔러 | `agent_runner.py run --role storyteller` | `target.json`, `research.json`, `verification.json`, 대상 페이지·대분류 페이지, `templates/<유형>.md`, 용어집·참고문헌·표준·열린 질문 색인, `docs_tree.txt`, `inbox/corrections.md` (+ 트랙 입력, 재실행이면 이전 `pages.json`·`pages/`·`verification2.json`) | `prompts/storyteller.md`, `pages/<docs 상대 경로>.md`, `pages.json`(content 제거 사본), `pages.md` |
| 6 2차 검증 | `agent_runner.py run --role verifier --stage second` | `research.json`, `verification.json`, `pages.json`, `pages/*`, 갱신 대상의 현재 `docs/` 페이지, `docs_tree.txt`, 색인들 (+ 재검증이면 직전 `verification2.json`) | `prompts/verification2.md`, `verification2.json`, `verification2.md` |
| 7 퍼블리셔 | `publish.py <id>` | 위 산출물 전부, `schemas/*.json`, `pipeline/checks/*` | `docs/`(페이지·용어집·참고문헌·자동 영역), `data/*.json`, `data/tracks/<slug>/*.json`, `config/tracks/<slug>.yaml`(단계 전환 시만), `inbox/corrections.md`(상태), `mkdocs.yml`, `site/`, git 커밋, `runs/<id>/build.log` |
| 8 일일 로그·지표 | `publish.py`(9단계) | `runs/<id>/*` | `docs/logs/daily/<date>.md`, `runs/<id>/summary.json`, 자동 영역(`logs-index`, `metrics`) |

프롬프트 조립(에이전트 실행 규약): `agents/shared-rules.md` 전문 + `agents/<role>.md` 전문 + `## 실행 컨텍스트`(run_id, date, run_type, 대상, 예산, 환경 알림, 역할별 `verification_stage`·`retry_count`·`next_ref_id`) + `## 입력`(파일마다 `### <경로>` 소제목과 코드 펜스) + 재실행이면 `## 반려 사유`(리서치) 또는 `## 수정 지시`(스토리텔러). `claude -p --output-format json --json-schema … --tools … --allowedTools … --max-turns N --permission-mode dontAsk` 로 호출하고 응답의 `structured_output` 을 `schemas/*.json` 으로 검사한다.

## 4. 재시도·보류 규칙 (7.3)

| 상황 | 처리 |
|---|---|
| 웹 검색 도구 없음 | 준비 단계에서 즉시 중단. `runs/<id>/log.md` 와 일일 로그에 "중단(웹 검색 도구 없음)" 기록, exit 3 |
| 페이지 열람 불가 | 기본(`web_fetch_required: false`)은 계속 진행하고 실행 컨텍스트에 `web_fetch_available: false` 표시. `true` 면 중단 |
| 설정 YAML 오류 | 준비 단계에서 중단(exit 2) |
| 예산 초과·도달 | 리서치 결과의 `self_check.budget_used` 를 `target.json` 의 예산과 비교해 `log.md` 와 일일 로그의 "예산 사용량" 표에 표시하고 부분 결과로 진행 |
| 스키마 불일치 | 해당 에이전트를 `## 스키마 불일치 (재실행)` 절을 붙여 1회 재실행. 그래도 불일치면 보류(`runs/parked/`) |
| 1차 검증 반려 | `## 반려 사유` 를 붙여 리서치 재실행(최대 `max_retries`, 기본 2회). 직전 판정은 `verification.attemptN.json`, 직전 브리프는 `research.attemptN.json` 으로 남긴다. 여전히 반려면 보류 |
| 2차 검증 수정 후 재검증·불통과 | `## 수정 지시` 를 붙여 스토리텔러 재실행(최대 `max_retries`). 직전 판정은 `verification2.attemptN.json`, 직전 초안은 `pages.attemptN.json`. 여전히 불통과면 보류. `retry_reason` 이 "브리프 없음"으로 시작하면 재실행 없이 바로 보류 |
| 보류 | `runs/<id>/` 전체를 `runs/parked/<id>/` 로 옮기고 `summary.json` 에 `parked: true`·사유를 쓴 뒤 일일 로그를 남긴다(exit 2). 같은 영역이 3회 연속 보류되면 다음 대상 선정에서 제외하고 `data/open_questions.json` 에 사용자 검토 요청을 올린다. `config/priority.yaml` 의 `areas` 에 지정하면 제외가 풀린다 |
| 퍼블리셔 검사 실패(스키마·판정·프런트매터·원문 보호·링크) | 아무것도 반영하지 않는다. docs 에 임시 복사한 페이지는 스냅숏(`runs/<id>/backup/`)으로 되돌린다. 실행 폴더는 `runs/` 에 남고 일일 로그에 "중단(퍼블리셔: …)" 을 쓴다(exit 4) |
| 사이트 빌드 실패 | 6단계 반영을 스냅숏(+`git checkout`)으로 되돌리고 `runs/<id>/build.log` 와 로그에 남긴다 |
| 커밋 실패 | 파일은 반영된 채 두고 실패로 기록한다(빌드는 성공한 상태). `git` 문제를 고친 뒤 `--resume <id> --step publish` 로 다시 시도한다 |

## 5. `--resume` 사용법

1. 어디서 멈췄는지 본다: `runs/<id>/log.md`(또는 `runs/parked/<id>/log.md`)의 마지막 줄과 `summary.json` 의 `end_state`.
2. 원인을 고친다(정정 요청·우선 지정을 손보거나, 네트워크·git 문제를 해결한다). 보류 산출물은 `verification.md`·`verification2.md` 의 사유를 읽고 `research.md`·`pages/` 를 본다.
3. 재투입: `bash pipeline/run_daily.sh --resume <id>`. `runs/parked/<id>/` 만 있으면 스크립트가 `runs/<id>/` 로 되돌린다. 산출물이 있는 단계는 건너뛴다.
   - `target.json` 이 있으면 대상 선정을 건너뛴다.
   - `research.json` 이 있으면 리서치를 건너뛰고 1차 검증부터 한다. 1차 판정이 승인·조건부 승인이면 스토리텔러부터.
   - `pages.json` 이 있으면 스토리텔러를 건너뛰고 2차 검증부터. 2차 판정이 통과면 퍼블리셔부터.
   - `summary.json` 의 `published` 가 true 면 아무것도 하지 않는다.
4. 특정 단계만 다시 하려면 `--step` 을 더한다. 예: 브리프를 다시 쓰게 하려면 `--resume <id> --step research`, 퍼블리셔만 다시 하려면 `--resume <id> --step publish`.
5. 폐기하려면 `runs/parked/<id>/DISCARDED` 파일에 날짜와 사유를 한 줄 적는다(폴더는 기록으로 남긴다).

## 6. 스케줄

`pipeline/cron.example` 이 예시다(`CRON_TZ=Asia/Seoul`, `0 6 * * *`, 출력은 `runs/cron.log`). 등록은 `bash pipeline/install_cron.sh`, 해제는 `bash pipeline/uninstall_cron.sh`, 등록 확인은 `crontab -l`. 스케줄 시각을 바꾸려면 `bash pipeline/install_cron.sh --schedule "0 7 * * *"`. cron 이 `CRON_TZ` 를 지원하지 않으면 `cron.example` 의 주석대로 시각을 서버 시간대로 환산한다.

## 7. 문제 해결

| 증상 | 확인·조치 |
|---|---|
| `claude 실행 파일을 찾을 수 없다` | `which claude`; cron 이면 `install_cron.sh` 가 넣은 `PATH` 줄을 확인한다. `settings.claude_bin` 에 절대 경로를 적어도 된다 |
| `claude 오류 응답: API Error 400 … input_schema does not support oneOf/allOf` | `agent_runner.py` 가 스키마를 CLI 용으로 바꾸지 못한 경우다. `schemas/*.json` 을 고쳤다면 최상위 `allOf/oneOf/anyOf` 를 쓰지 말고 `lib/runs.py` 의 `cli_schema()` 를 확인한다 |
| `--json-schema is not a valid JSON Schema` / `strict mode: missing type` | 같은 원인. `cli_schema()` 가 `$schema`·`$id`·`$defs` 를 빼고 하위 스키마에 `type` 을 보충하는지 확인한다 |
| 에이전트 호출 시간 초과 | `settings.agent_timeout_sec`(기본 1800초)와 `max_turns` 를 본다. 재실행은 `--resume <id> --step <단계>` |
| `web_search_available: false` 로 중단 | `claude -p --tools WebSearch` 가 동작하는지, 네트워크 정책이 검색을 막는지 확인한다 |
| 퍼블리셔 4단계 원문 보호 검사 실패 | 출력의 diff 를 본다. 스토리텔러가 `[분류원문]` 문장·절 제목을 바꾼 경우다. `pages/` 를 고쳐 `--resume <id> --step publish` 하거나 보류로 넘긴다 |
| 5단계 링크 검사 실패 | 깨진 상대 경로·정의 없는 각주. `runs/<id>/pages/` 에서 고친 뒤 재시도 |
| `mkdocs build --strict` 실패 | `runs/<id>/build.log`. 보통 내비게이션·링크 경고. 롤백된 상태이므로 원인 수정 후 `--resume <id> --step publish` |
| git 커밋 실패(identity 없음 등) | `git config user.name`/`user.email` 을 설정한다(없으면 스크립트가 임시 identity 로 커밋한다). 푸시는 `git_push: true` 일 때만 |
| 같은 날 두 번째 실행 | 실행 id 가 `-02` 로 붙고 일일 로그에 실행 블록이 최신순으로 추가된다 |
| 예산 초과 표시 | 일일 로그 "예산 사용량" 표에 초과·도달이 보이면 에이전트가 부분 결과로 마쳤다는 뜻이다. `config/settings.yaml` 의 `daily_budget` 을 조정한다 |
| 산출물 확인 | `runs/<id>/research.md`, `verification.md`, `verification2.md`, `pages.md`, `log.md`, `summary.json`; 사이트는 `site/` 또는 `mkdocs serve` |

## 8. 이 절차서가 정한 것 [가정]

- `runs/<id>/pages/` 는 `docs/` 기준 상대 경로 구조로 푼다(같은 이름의 `index.md` 충돌을 피한다).
- 재실행 회차는 실행 컨텍스트 `retry_count` 로, 직전 판정·산출물은 `*.attemptN.json` 으로 남긴다.
- 스토리텔러 반환값은 `pages.schema.json` 의 `$defs/returned`(모든 페이지에 `content` 필수)로 검사한다.
- 퍼블리셔는 6단계에서 예비 일일 로그·요약을 쓰고 빌드·커밋 뒤 9단계에서 확정 로그로 다시 써 재빌드·커밋 수정(`--amend`)한다.
- 보류·중단된 실행도 일일 로그(`publish.py --log-only`)를 남긴다.
