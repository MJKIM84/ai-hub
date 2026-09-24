# config/ — 파이프라인 설정 파일

이 폴더는 ROP 연구 위키 파이프라인이 읽는 설정 파일을 모은 곳이다. 빌드 사양서의 0장(설정), 7.1(대상 선정 규칙), 7.4(사용자 개입 지점), 8.2(트랙 공통 운영 규칙)에 대응한다. 사람이 손으로 고치는 파일은 이 폴더의 YAML 뿐이고, 실행 스크립트는 이 파일들을 읽기만 하며 다시 쓰지 않는다. 유일한 예외는 퍼블리셔가 단계 전환 승인 뒤 `tracks/<slug>.yaml` 의 `current_stage`(단계 7 뒤에는 `status: done`)와 선택 키 `stage_status`·`stage_completion` 을 갱신하는 것이다(아래 공통 규칙과 "`tracks/<slug>.yaml` — 트랙 정의" 절) [가정]. 값을 바꾸면 다음 실행부터 적용된다.

| 파일 | 무엇을 정하는가 | 주로 읽는 곳 | 누가 고치는가 |
|---|---|---|---|
| `settings.yaml` | 위키 이름, 실행 방식, 하루 예산, 에이전트 호출 옵션, 빌드·커밋 옵션 | `pipeline/run_daily.*`, `pipeline/select_target.*`, `pipeline/agent_runner.py`, `pipeline/publish.*` | 운영자(드물게) |
| `rotation.yaml` | 그날 어떤 실행 유형으로 어느 영역을 다룰지 정하는 규칙 | `pipeline/select_target.*` | 운영자(드물게) |
| `priority.yaml` | 순환보다 먼저 다룰 영역·주제·질문, 트랙 백로그에 넣을 질문 | `pipeline/select_target.*`(트랙 백로그 등록 포함), 리서치·검증 에이전트(입력), 퍼블리셔(트랙 백로그 보완 등록) | 사용자(수시) |
| `tracks/<slug>.yaml` | 중점 연구 트랙의 정의(단계, 관련 영역, 트랙 예산) | `pipeline/select_target.*`, 리서치 에이전트(입력), 퍼블리셔(`pipeline/lib/render.py`) | 트랙 담당(추가·종료 시), 퍼블리셔(단계 전환 시 `current_stage`·`status`·선택 키만) |

공통 규칙은 다음과 같다.

- 형식은 YAML 이고 인코딩은 UTF-8 이다. 파이썬 `yaml.safe_load` 로 읽히지 않으면 실행이 준비 단계에서 멈추고 로그에 남는다 [가정: 사양서 7.3 은 설정 파일 오류의 처리를 정하지 않는다. 7.2 의 준비 단계(설정 로드)에서 잘못된 설정으로 진행하지 않도록 "웹 도구 없음"과 같이 즉시 중단·로그로 다룬다].
- 상대 경로는 모두 위키 루트(`rop-wiki/`) 기준이다. `settings.yaml` 의 `repo_root` 만 git 저장소 루트를 가리키는 예외다.
- 실행 스크립트는 이 폴더의 파일을 다시 쓰지 않는다. 유일한 예외는 퍼블리셔의 단계 전환 기록이다: 2차 검증의 `track_checks.stage_transition_approved` 가 true 이고 `pages.json` 의 `track_updates.stage_transition` 이 있으면 `tracks/<slug>.yaml` 의 `current_stage` 를 `to_stage` 로 올리고, 단계 7 이 끝났으면 `status` 를 `done` 으로 바꾸며, 선택 키 `stage_status`·`stage_completion`(`pipeline/lib/render.py` 가 읽는 값)을 기록할 수 있다. 그 밖의 키와 다른 파일은 건드리지 않는다. 사양서 8.2 의 단계 전환 상태를 어디에 기록하는지는 사양서에 없어 구축자가 정했다 [가정].
- 세부영역은 데이터에서는 번호(`area_no`)로 적지만, 사람이 읽는 주석·로그·페이지에서는 항상 번호와 이름을 함께 쓴다. 예: `7. 화물·재고·자산 식별과 추적`.
- `[가정]` 이 붙은 값은 사양서에 수치나 기준이 없어 구축자가 정한 것이다. 바꿔도 사양서와 어긋나지 않는다.
- 분류 원문(`_source/ROP_SCM_연구분야_분류.md`)의 명칭·번호·정의·질문은 설정으로 바꿀 수 없고, 세부영역을 더하거나 합치는 설정도 없다.

## `settings.yaml` — 전역 설정

앞부분(`wiki_name` ~ `web_tools_required`)은 빌드 사양서 0장의 YAML 을 값과 주석 그대로 옮긴 것이다. 뒷부분(`repo_root` 이후)은 실행 스크립트가 필요로 하는 항목이며 구축자가 추가했다.

### 사양서 0장 항목

| 항목 | 기본값 | 뜻 | 읽는 곳 |
|---|---|---|---|
| `wiki_name` | `"ROP 연구 위키"` | 표시 이름. 부제는 "SCM 관점의 로봇 오케스트레이션 플랫폼 연구" | 사이트 설정, 로그 |
| `repo_path` | `"./rop-wiki"` | 저장소 루트에서 본 위키 폴더 경로 | 스케줄 파일, README |
| `storage` | `"markdown+git"` | 저장 방식. 다른 저장소로 바꿔도 4~7장의 구조와 규칙은 유지한다 | 퍼블리셔 |
| `site_generator` | `"mkdocs-material"` | 정적 사이트 생성기. 바꿔도 4.8 의 내비게이션 순서를 재현한다 | 퍼블리셔 |
| `agent_runtime` | `"claude-code-headless"` | 에이전트 실행 방식(`claude -p` 헤드리스 또는 Agent SDK) | `agent_runner.py` |
| `scheduler` | `"cron"` | 스케줄러(cron / n8n / GitHub Actions) | 스케줄 등록 파일 |
| `run_time` | `"06:00 Asia/Seoul"` | 매일 1회 실행 시각 | 스케줄 등록 파일 |
| `language` | `"ko"` | 본문 언어. 전문용어는 첫 등장 시 영문 병기 | 에이전트 실행 컨텍스트 |
| `checkpoints` | `true` | 9장의 멈춤 지점 2곳에서 사용자 확인을 받는지 | 구축 절차 |
| `tracks` | `["manual-capability-ontology"]` | 활성 중점 연구 트랙 slug 목록. 정의는 `tracks/<slug>.yaml` | `select_target.*`, 퍼블리셔 |
| `track_runs_per_week` | `2` | 주 7회 실행 중 트랙에 배정하는 횟수. 7이면 트랙 단계가 끝날 때까지 트랙만 실행. `tracks/<slug>.yaml` 의 `runs_per_week` 가 비어 있을 때 쓰는 값이다(8.2). 이 두 곳 외에 주당 트랙 실행 횟수를 정하는 설정은 없다 | `select_target.*` |
| `daily_budget.new_topic_pages` | `1` | 하루 신규 주제 페이지 상한 | 스토리텔러 컨텍스트, 퍼블리셔 |
| `daily_budget.page_updates` | `2` | 하루 기존 페이지 갱신 상한 | 스토리텔러 컨텍스트, 퍼블리셔 |
| `daily_budget.max_sources_per_run` | `15` | 회당 신규 출처 상한 | 리서치 컨텍스트 |
| `daily_budget.max_search_queries` | `30` | 회당 검색 횟수 상한 | 리서치·검증 컨텍스트 |
| `daily_budget.max_retries` | `2` | 검증 반려 시 재작업 횟수(1차·2차 각각) | `run_daily.*` |
| `daily_budget.track_max_sources_per_run` | `20` | 트랙 실행의 출처 상한 | 리서치 컨텍스트(트랙) |
| `daily_budget.track_max_search_queries` | `40` | 트랙 실행의 검색 횟수 상한 | 리서치·검증 컨텍스트(트랙) |
| `notify` | `"none"` | 알림 방식(none / slack_webhook / email) | 퍼블리셔 9단계 |
| `web_tools_required` | `true` | 웹 검색·페이지 열람 도구가 없으면 실행을 중단하고 로그에 남긴다. 이 파이프라인은 원문대로 적용한다: 준비 단계에서 웹 검색(WebSearch) 또는 페이지 열람(WebFetch) 점검이 실패하면 즉시 중단·로그(7.3). 예외는 페이지 열람만 막힌 환경의 사용자 override 하나다(`run_daily.sh --allow-no-fetch`, 환경변수 `ROP_ALLOW_NO_FETCH=1`, 또는 `web_fetch_required: false`) — 이때는 원문 미열람 모드로 진행하고 로그에 "페이지 열람 불가 — 원문 미열람 모드(사용자 override)"를 남긴다 | `run_daily.*` 준비 단계 |

### 구축자 추가 항목

| 항목 | 기본값 | 뜻 | 읽는 곳 |
|---|---|---|---|
| `repo_root` | `".."` | git 저장소 루트. 위키 루트 기준 상대 경로. 위키가 ai-hub 저장소의 하위 폴더라는 전제다 [가정] | 퍼블리셔(커밋·푸시·롤백) |
| `claude_bin` | `"claude"` | Claude Code CLI 실행 파일. PATH 에 있으면 이름만 적는다 | `agent_runner.py` |
| `model` | `"claude-opus-5-5"` | 에이전트 모델 id. `agent_runner.py` 가 `claude -p --model <id>` 로 넘긴다(웹 도구 점검 호출 포함). 비우면 CLI 기본 모델을 쓰고 `--model` 옵션을 붙이지 않는다 | `agent_runner.py` |
| `max_turns.researcher` / `.verifier` / `.storyteller` | `60` / `40` / `8` | 에이전트별 최대 턴 수(`--max-turns`). 넘으면 호출을 끊고 7.3 의 스키마 불일치와 같이 1회 재실행 뒤 보류한다 [가정: 사양서 7.3 은 턴 수·시간 초과의 처리를 정하지 않는다] | `agent_runner.py` |
| `agent_timeout_sec` | `1800` | 에이전트 1회 호출의 시간 상한(초). 넘으면 강제 종료하고 `max_turns` 초과와 같이 처리한다(1회 재실행 뒤 보류) [가정: 위와 같음] | `agent_runner.py` |
| `allowed_tools.researcher` / `.verifier` / `.storyteller` | `[WebSearch, WebFetch]` / `[WebSearch, WebFetch]` / `[]` | 에이전트별 허용 도구(`--allowedTools`). 빈 목록은 도구 없이 실행한다는 뜻이다. 파일 읽기·쓰기 도구는 어느 에이전트에도 주지 않는다 | `agent_runner.py` |
| `site_build_cmd` | `"mkdocs build --strict"` | 퍼블리셔 6단계의 사이트 빌드 명령. 위키 루트에서 실행하고, 실패하면 커밋을 되돌린다 | 퍼블리셔 |
| `git_commit` | `true` | 퍼블리셔 7단계 커밋 여부. 메시지 형식은 `run(DATE): <실행 유형> <대상 영역 이름> — 생성 n/갱신 n` | 퍼블리셔 |
| `git_push` | `false` | 커밋 후 원격 푸시 여부 | 퍼블리셔 |
| `timezone` | `"Asia/Seoul"` | `run_time`, 실행 id(`<DATE>-<NN>`), 페이지의 `created`/`updated`/접근일 계산에 쓰는 시간대 | 모든 스크립트 |
| `web_fetch_probe_url` | `"https://ref.gs1.org/epcis/"` | 준비 단계의 페이지 열람 점검용 URL(참고문헌 ref-001~010 가운데 ref-003 GS1 EPCIS). `claude -p --tools WebFetch` 로 한 번 연다. 열리지 않으면 `web_tools_required` 대로 중단한다(사용자 override 가 있으면 원문 미열람 모드로 진행) | `run_daily.*` 준비 단계 |
| `web_fetch_required` | `true` | 페이지 열람(WebFetch) 점검이 실패했을 때 즉시 중단·로그할지. 기본값 `true` 는 0장 `web_tools_required` 와 7.3 원문대로 중단한다. 페이지 열람이 네트워크 정책으로 막힌 제한 환경에서는 실행마다 `bash pipeline/run_daily.sh --allow-no-fetch`(또는 `ROP_ALLOW_NO_FETCH=1`)로 허용하거나, 이 값을 `false` 로 두어 계속 허용한다(사용자 override). override 로 진행하면 실행 컨텍스트에 `web_fetch_available: false` 를 표시하고(에이전트는 출처를 검색 결과로만 확인하고 모든 출처에 "원문 미열람"을 표시하며 신뢰도 `high` 를 주지 않는다), `runs/<id>/log.md`·`probe.json`(`web_fetch_override`, `web_fetch_override_source`)·일일 로그에 "페이지 열람 불가 — 원문 미열람 모드(사용자 override)"를 남긴다. 웹 검색 도구가 없으면 override 와 관계없이 중단한다 [가정: override 수단 — 사양서는 예외를 정하지 않는다] | `run_daily.*` 준비 단계 |
| `runs_dir` | `"runs"` | 실행 산출물 폴더. `runs/<DATE>-<NN>/` 와 보류 산출물 `runs/parked/` | 모든 스크립트 |
| `data_dir` | `"data"` | 퍼블리셔가 자동 갱신 영역을 다시 쓸 때 원천으로 삼는 JSON 폴더 | 퍼블리셔, `select_target.*` |

## `rotation.yaml` — 대상 선정 규칙

`pipeline/select_target.*` 가 매 실행에서 읽어 그날의 실행 유형(`run_type`)과 대상을 정하고 `runs/<run_id>/target.json` 에 쓴다. `run_type` 값은 `area_deep_dive | topic | update | weekly_review | monthly_recheck | track` 이다.

### 선정 순서 (`precedence`)

위에서 아래로 처음 맞는 규칙이 그날의 실행 유형을 정한다. 규칙이 겹칠 때의 우선순위는 사양서에 없어 구축자가 정했다 [가정].

1. `track_day` — 오늘이 `track_days` 에 있고 활성 트랙이 있으면 트랙 실행이다. 트랙 실행이 아닌 날은 아래 규칙을 그대로 따른다. 이날과 겹친 정기 실행은 `deferred_periodic_runs` 대로 미룬다.
2. `monthly_recheck` — 이달 첫 실행(미룬 것 포함)이면 월간 재검증이다.
3. `weekly_review` — `weekly_review_every` 번째 실행(미룬 것 포함)이면 주간 정리다.
4. `priority` — `priority.yaml` 의 `areas`·`topics`·`questions` 항목이 있으면 순환보다 먼저 고른다(사양서 7.1: 영역·주제·질문 모두). `questions` 항목은 `areas` 와 같이 `area_no` 영역을 대상으로 올린다.
5. `cycle1` — 제외되지 않은(`exclude_after_consecutive_parks` 참고) 상태 `seed` 세부영역이 남아 있으면 1주기 규칙이다.
6. `cycle2` — 그 밖에는 점수가 가장 높은 영역이고, 동점이면 `tie_break` 를 따른다.

`track_day` 가 정기 실행보다 앞이므로, 이달 첫 실행이나 `weekly_review_every` 번째 실행이 트랙 요일과 겹치면 그날은 트랙을 실행하고 정기 실행은 다음 비트랙 실행으로 미룬다(`deferred_periodic_runs`). 이때 사양서 7.1 의 "매월 첫 실행"·"매 7번째 실행"은 글자 그대로가 아니라 하루(또는 며칠) 뒤가 된다. 트랙 요일은 고정이라 매 7번째 실행과의 겹침은 매주 반복되고, 정기 실행을 앞세우면 트랙 실행이 매주 한 번씩 빠져 주당 횟수(`track_runs_per_week`)를 지킬 수 없기 때문이다. 사양서 문구를 그대로 지키려면 `monthly_recheck`·`weekly_review` 를 `track_day` 앞으로 옮기고, 그날의 트랙 실행은 다음 트랙 요일로 넘긴다(그 주의 트랙 실행이 한 번 준다) [가정 — 사용자 결정 항목. 기본값: 트랙 우선·정기 실행 미룸 / 대안: 정기 실행 우선·그날의 트랙 실행 건너뜀].

### 항목

| 항목 | 기본값 | 뜻 |
|---|---|---|
| `cycle1.run_type` | `area_deep_dive` | 1주기의 실행 유형 |
| `cycle1.order` | `[1, …, 28]` | 1주기 순서. 1. 주문·업무 시스템 연계부터 28. 표준·상호운용성·다사업자 거버넌스까지 번호순 |
| `cycle1.rule` | `"status seed 인 최저 번호 영역"` | `order` 를 따라가되 세부영역 페이지 프런트매터의 `status` 가 `seed` 인 것 가운데 가장 낮은 번호를 고른다. `exclude_after_consecutive_parks` 로 제외된 영역은 `seed` 로 남아 있어도 건너뛴다. 제외되지 않은 `seed` 영역이 하나도 없으면(남은 `seed` 가 모두 제외 영역인 경우 포함) 1주기가 끝난 것으로 보고 `cycle2` 로 넘어간다. 제외 영역은 제외가 풀릴 때까지 2주기에서도 대상이 되지 않는다 [가정: 1주기 종료 판정 기준 — 사양서의 "첫 28회 실행"을 실행 횟수가 아니라 페이지 `status` 로 판정한다] |
| `cycle2.default_run_type` | `topic` | 2주기의 기본 실행 유형은 주제 조사다 |
| `corrections.include_update` | `true` | `inbox/corrections.md` 에 `open` 요청이 걸린 페이지가 있으면 그 페이지의 갱신을 당일 작업에 포함한다. 대상 선정 자체는 바꾸지 않고 `daily_budget.page_updates` 안에서 처리한다(넘치면 다음 해당 실행으로). 사양서 7.1 은 이 문장을 2주기 항목에 두지만 정정 요청은 1주기·우선 지정 실행 중에도 들어오므로 실행 주기와 관계없이 적용한다(`docs/corrections.md` 의 처리 흐름과 같다) [가정] |
| `corrections.applies_to` | `[area_deep_dive, topic, update, monthly_recheck]` | 당일 실행 유형이 이 목록에 있을 때 갱신 작업을 붙인다. `weekly_review` 는 신규 조사를 하지 않으므로(7.1), `track` 은 트랙 페이지만 쓰므로 뺀다. 그런 날에도 리서치 에이전트는 파일 전문을 입력으로 읽고, 트랙 페이지에 걸린 요청은 트랙 실행의 1차 검증 항목 11 로 다룬다 [가정] |
| `scoring.weights.*` | 모두 `1` | 점수 = 마지막 갱신 경과일 + 열린 질문 수 + 비어 있는 매트릭스 칸 수 + 우선 가중치 − 최근 감점. 사양서 7.1 이 단순 합이므로 가중치는 모두 1 이다 |
| `scoring.recent_penalty_days` | `7` | 최근 7일 안에(오늘 제외) 다룬 영역이면 감점한다. '다룬 것'은 게시까지 간 실행만이다(보류·중단된 실행은 세지 않는다). 트랙 실행은 세부영역 페이지를 갱신하지 않으므로 세지 않는다 [가정] |
| `scoring.recent_penalty` | `5` | 감점 크기. 한 번만 뺀다 [가정] |
| `weekly_review_every` | `7` | 매 7번째 실행은 주간 정리다. 실행 번호는 `runs/<DATE>-<NN>/` 과 `runs/parked/<DATE>-<NN>/` 에 있는 실행 id 의 수로 센다(보류로 옮겨진 실행도 세고, 같은 id 는 한 번만 센다. `runs/parked/` 폴더 자체는 세지 않는다) [가정] |
| `monthly_recheck` | `"first run of month"` | 매월 첫 실행은 월간 재검증이다 |
| `deferred_periodic_runs` | `"next non-track run"` | 주간 정리·월간 재검증이 트랙 실행일과 겹치면 다음 비트랙 실행으로 미룬다. 미룬 정기 실행은 그 비트랙 실행에서 우선 지정·순환보다 먼저 온다. 둘이 같은 날이면 월간 재검증을 먼저 하고 주간 정리를 그다음 비트랙 실행으로 미룬다. 미룸은 실행 번호 세기를 바꾸지 않는다 [가정 — `precedence` 의 사용자 결정 항목과 같은 결정] |
| `track_days` | `[Tue, Fri]` | 트랙 실행 요일(`settings.timezone` 기준). 값은 `Mon Tue Wed Thu Fri Sat Sun`. 앞에서부터 주당 트랙 실행 횟수만큼 쓴다 [가정: 요일] |
| (주당 트랙 실행 횟수) | — | `rotation.yaml` 에는 없다. `tracks/<slug>.yaml` 의 `runs_per_week` 가 있으면 그 값, 비어 있으면 `settings.yaml` 의 `track_runs_per_week`(8.2). 7이면 `track_days` 를 무시하고 매일 트랙만 실행한다. `track_days` 가 그 횟수보다 짧으면 있는 요일만 쓰고 로그에 경고한다. 활성 트랙이 여럿이고 값이 다르면 가장 큰 값을 쓰고 로그에 경고한다 [가정] |
| `track_rotation` | `alternate` | 활성 트랙이 여럿이면 `settings.tracks` 순서로 번갈아 실행한다 [가정] |
| `priority.overrides_rotation` | `true` | `priority.yaml` 항목은 순환보다 우선한다 |
| `priority.pick` | `"highest weight, then file order"` | 우선 항목(`areas`·`topics`·`questions`)이 여럿이면 `weight` 가 큰 것(`questions` 는 `question_weight`), 같으면 파일에 적힌 순서(`areas` → `topics` → `questions` 키 순, 키 안에서는 항목 순) [가정] |
| `priority.run_type` | (문자열) | `areas`·`questions` 항목은 그 영역 페이지가 `seed` 면 `area_deep_dive`, 아니면 `topic`(`questions` 가 `topic` 이면 질문 문장이 주제 제목). `topics` 항목은 언제나 `topic` [가정] |
| `priority.skip_if_targeted_within_days` | `7` | 최근 7일 안에 이미 다룬 우선 항목은 건너뛴다(`questions` 는 그 질문이 조사 질문에 포함된 실행이 있었으면 다룬 것). '다룬 것'은 게시까지 간 실행만이다(보류·중단된 실행은 세지 않는다). 연속 보류로 제외됐다가 `areas` 지정으로 제외가 풀린 영역은 이 건너뛰기를 면제해 다음 실행에서 바로 고른다. 항목을 지우지 않아도 같은 항목만 매일 반복되지 않게 한다 [가정] |
| `priority.question_weight` | `3` | `questions` 항목의 가중치(항목에 `weight` 필드가 없으므로 이 값을 쓴다). `questions` 항목은 `areas` 와 같이 `area_no` 영역을 순환보다 먼저 대상으로 올리고(7.1), 이 값은 `pick` 의 비교와 2주기 점수의 우선 가중치 항(항목당 3)에 쓴다 [가정: 가중치 크기] |
| `exclude_after_consecutive_parks` | `3` | 같은 영역이 3회 연속 보류되면 대상 선정에서 제외하고 사용자 검토 요청을 열린 질문에 올린다(7.3). `priority.yaml` 의 `areas` 에 다시 지정하면 제외가 풀리고, 다음 실행에서 바로 대상이 된다(7일 건너뛰기 면제). 폐기 표시(`runs/parked/<id>/DISCARDED`)한 보류도 연속 횟수에 센다 [가정] |
| `tie_break` | `"lowest area number"` | 점수가 같으면 번호가 낮은 영역 |

### 점수 항의 계산 근거 [가정: 해석]

| 항 | 원천 | 계산 |
|---|---|---|
| 마지막 갱신 경과일 | 세부영역 페이지 프런트매터 `updated` | 오늘 − `updated` (일) |
| 열린 질문 수 | `data/open_questions.json` | 상태가 열림·조사 중이고 관련 영역에 그 영역이 포함된 항목 수 |
| 비어 있는 매트릭스 칸 수 | `data/flow_matrix.json` | 42칸(입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품 × 시작 조건, 작업 대상, 수행 자원, 제약, 완료·인계, 예외·성과) 가운데 그 영역의 페이지 링크가 없는 칸 수 |
| 우선 가중치 | `config/priority.yaml` | `areas[].weight` + `topics[].weight`(같은 `area_no`) + `questions` 항목 수 × `priority.question_weight`. 우선 항목은 보통 `priority` 단계에서 먼저 선정되므로, 이 항은 `skip_if_targeted_within_days` 로 건너뛴 항목이 2주기 점수에 남기는 보조 가중치다 |
| 최근 감점 | `runs/*/target.json`·`summary.json` | 최근 `recent_penalty_days` 일 안에 게시까지 간 비트랙 실행의 대상이면 `recent_penalty` 를 한 번 뺀다(보류·중단된 실행은 세지 않는다) |

## `priority.yaml` — 사용자 우선순위

사용자가 수시로 고치는 파일이다. 비어 있으면 순환 규칙만 따른다. 네 키는 빈 목록이라도 모두 있어야 한다. 사용법은 [기여·정정 방법](../docs/about/how-to-contribute.md) 페이지에도 있다.

| 키 | 항목 필드 | 뜻 | 반영 시점 |
|---|---|---|---|
| `areas` | `area_no`, `weight`, `reason` | 세부영역을 먼저 다루게 한다. `weight` 는 선정 점수에 더하는 가중치, `reason` 은 로그에 남는 사유 | 다음 대상 선정 |
| `topics` | `title`, `area_no`, `weight` | 특정 주제로 주제 조사를 실행하게 한다. `area_no` 는 주 연구영역 | 다음 대상 선정 |
| `questions` | `question`, `area_no` | 답을 찾게 할 질문. `area_no` 영역을 `areas` 와 같이 순환보다 먼저 대상으로 올리고(가중치는 `rotation.yaml` 의 `priority.question_weight`), 그 영역이 대상이 되면 리서치 에이전트의 조사 질문에 포함된다 | 다음 대상 선정 |
| `track_questions` | `track`, `stage`, `question`, `priority` | 트랙 백로그에 넣을 질문. 다음 트랙 실행의 대상 선정(`select_target.*`)이 제기 근거 "사용자"로 백로그에 먼저 등록하고 그 실행의 질문으로 고른다(8.2. 대상 선정 뒤에 더한 질문은 퍼블리셔가 보완 등록한다). 리서치 에이전트는 트랙 실행마다 현재 단계의 열린 질문 가운데 사용자 지정 → 앞 단계로 되돌아온 질문 → 오래된 순으로 1~3개를 고르므로(6.1) 현재 단계에 넣은 사용자 질문이 가장 앞에 온다. 사용자 질문이 여럿이면 `priority`(`high / normal / low` 순), 같으면 파일 순이다. `stage` 가 현재 단계보다 앞이면 되돌아온 질문과 같이 우선 처리하고, 뒤이면 그 단계가 될 때 다룬다 [가정] | 다음 트랙 실행 |

유의점은 다음과 같다.

- `area_no` 는 1~28 이다. 주석에 영역 이름을 함께 적는다. 예: `area_no: 7  # 7. 화물·재고·자산 식별과 추적`.
- 처리된 항목은 지워도 된다. 지우지 않으면 `rotation.yaml` 의 `priority.skip_if_targeted_within_days` 가 지난 뒤 다시 우선된다.
- 우선 지정은 조사 대상을 정할 뿐 검증 규칙과 하루 예산을 바꾸지 않는다. 우선 항목이 예산보다 많으면 여러 날에 걸쳐 처리된다.
- 틀린 문장의 정정은 이 파일이 아니라 `inbox/corrections.md` 에 적는다.

## `tracks/<slug>.yaml` — 트랙 정의

중점 연구 트랙마다 파일 하나다. 형식은 빌드 사양서 8.2 의 "트랙 정의 파일 형식"을 따르고, 트랙 담당이 만들고 고친다. 이 README 는 항목만 설명한다.

| 항목 | 뜻 |
|---|---|
| `slug` | 트랙 식별자. `docs/tracks/<slug>/`, `data/tracks/<slug>/backlog.json` 경로와 같다 |
| `name` | 표시 이름 |
| `status` | `active / paused / done`. `active` 인 트랙만 `track_days` 에 실행한다 |
| `primary_area` | 중심 세부영역 번호. 첫 트랙은 5. 로봇 능력·작업 온톨로지 |
| `related_areas` | 관련 세부영역 번호 목록 |
| `current_stage` / `stages` | 현재 단계와 단계 수. 2차 검증의 `stage_transition_approved` 가 true 이면 퍼블리셔가 `pages.json` 의 `track_updates.stage_transition.to_stage` 로 `current_stage` 를 올리고, 단계 7 뒤에는 `status` 를 `done` 으로 바꾼다. 설정 파일을 스크립트가 고치는 유일한 예외다(공통 규칙) [가정] |
| `runs_per_week` | 이 트랙의 주당 실행 횟수. 비우면 `settings.yaml` 의 `track_runs_per_week` 를 따른다(8.2). 주당 트랙 실행 횟수는 이 두 곳에서만 정하고 `rotation.yaml` 에는 없다. 활성 트랙이 여럿이고 값이 다르면 가장 큰 값을 쓰고 로그에 경고한다 [가정] |
| `budget` | 트랙 실행의 출처·검색 상한. `settings.yaml` 의 `track_max_*` 와 같은 값이 기본이다 |
| `stage_names`, `stage_pages` 등 | 트랙 담당이 추가한 표시용 항목. 그 파일의 주석을 따른다 |

새 트랙은 `tracks/<slug>.yaml` 을 추가하고 `settings.yaml` 의 `tracks` 에 slug 를 넣은 뒤, 트랙 페이지(개요·단계·백로그·로그)를 같은 템플릿으로 만든다. 트랙을 이유로 세부영역을 추가하거나 합치지 않는다.

## 검증

파일을 고친 뒤에는 위키 루트에서 다음을 실행해 읽히는지 확인한다.

```bash
python3 -c "import yaml,glob; [yaml.safe_load(open(p, encoding='utf-8')) for p in glob.glob('config/**/*.yaml', recursive=True)]; print('ok')"
```

`priority.yaml` 은 네 키가 모두 있어야 하고, `area_no` 는 1~28, `track_questions[].stage` 는 그 트랙의 `stages` 이하여야 한다. `pipeline/select_target.*` 는 이 조건이 어긋나면 해당 항목을 무시하고 로그에 남긴다 [가정].

## `[가정]` 목록

- `settings.repo_root: ".."` — 위키가 ai-hub 저장소의 하위 폴더 `rop-wiki/` 라는 전제.
- 페이지 열람 불가 시의 사용자 override(`run_daily.sh --allow-no-fetch`, `ROP_ALLOW_NO_FETCH=1`, `settings.web_fetch_required: false`) — 기본은 0장·7.3 원문대로 중단한다(`web_fetch_required: true`). override 는 페이지 열람만 막힌 제한 환경에서 사용자가 명시적으로 고를 때만 원문 미열람 모드로 진행하게 하며, 로그에 "페이지 열람 불가 — 원문 미열람 모드(사용자 override)"를 남긴다. 사양서는 이 예외를 정하지 않는다.
- `settings.model: "claude-opus-5-5"` — 헤드리스 에이전트 모델. 2026-09-24 에 `claude -p --model claude-opus-5-5 --output-format json --json-schema …` 로 `structured_output` 이 오는 것을 확인했다.
- `settings.max_turns`·`settings.agent_timeout_sec` — 턴 수·시간 초과는 7.3 의 스키마 불일치와 같이 1회 재실행 후 보류한다. 사양서 7.3 은 이 경우를 정하지 않는다.
- 퍼블리셔가 `tracks/<slug>.yaml` 의 `current_stage`(단계 7 뒤 `status: done`)와 선택 키 `stage_status`·`stage_completion` 을 단계 전환 승인 뒤 갱신한다. 실행 스크립트가 `config/` 를 다시 쓰는 유일한 예외다.
- `rotation.precedence` — 트랙 실행일 → 월간 재검증 → 주간 정리 → 우선 지정 → 1주기 → 2주기 순. 트랙 실행일이 정기 실행보다 앞이므로, 이달 첫 실행·매 7번째 실행이 트랙 요일과 겹치면 정기 실행을 다음 비트랙 실행으로 미룬다(`deferred_periodic_runs`). 사양서 7.1 의 "매월 첫 실행"·"매 7번째 실행"과 글자 그대로는 다르며, 정기 실행을 앞세우면 트랙의 주당 횟수가 매주 하나씩 빠지기 때문에 택했다. 사용자 결정 항목이다(기본값: 트랙 우선·정기 실행 미룸 / 대안: 정기 실행 우선·그날의 트랙 실행 건너뜀).
- `rotation.scoring.recent_penalty: 5`, 트랙 실행은 최근 감점에 세지 않음.
- `rotation.track_days: [Tue, Fri]`.
- `rotation.cycle1.rule` — 1주기 종료는 실행 횟수(28회)가 아니라 제외되지 않은 `status: seed` 세부영역이 남았는지로 판정한다. 남은 `seed` 가 모두 보류 3회로 제외된 영역이면 1주기가 끝난 것으로 보고 2주기로 넘어간다.
- `rotation.weekly_review_every` 의 실행 번호는 `runs/<DATE>-<NN>/` 과 `runs/parked/<DATE>-<NN>/` 의 실행 id 수로 센다(같은 id 는 한 번). 미룬 정기 실행도 실행 번호 세기를 바꾸지 않는다.
- 주당 트랙 실행 횟수는 `tracks/<slug>.yaml` 의 `runs_per_week` → `settings.track_runs_per_week` 순으로 정하고 `rotation.yaml` 에는 두지 않는다. 활성 트랙이 여럿이고 값이 다르면 가장 큰 값.
- `rotation.priority.*` — 우선 항목이 여럿일 때의 선택, 실행 유형, 7일 건너뛰기. `questions` 항목은 사양서 7.1 대로 `areas` 와 같이 해당 영역을 우선 대상으로 올리며, 그 가중치는 3.
- `rotation.corrections` — 정정 요청 갱신은 대상 선정을 바꾸지 않고 당일 작업에 더한다. 사양서 7.1 은 이 문장을 2주기 항목에 두지만, 1주기·우선 지정·월간 재검증 실행에도 적용한다(`applies_to`). 주간 정리(신규 조사 없음)와 트랙 실행(트랙 페이지만 씀)에는 갱신 작업을 붙이지 않는다.
- 보류 3회로 제외된 영역은 `priority.yaml` 의 `areas` 에 지정하면 다시 대상이 된다(다음 실행에서 바로 — 7일 건너뛰기 면제). 최근 7일 건너뛰기·최근 감점은 게시까지 간 실행만 '다룬 것'으로 센다.
- `priority.yaml` 의 `track_questions[].priority` 값은 `high / normal / low` 이고, 사용자 지정 질문이 여럿일 때 고르는 순서에만 쓴다. 사용자 지정 질문 → 앞 단계로 되돌아온 질문 → 오래된 순은 사양서 6.1 의 규칙이고, `stage` 가 현재 단계와 다른 사용자 질문의 처리 시점(앞 단계면 되돌아온 질문과 같이 우선, 뒤 단계면 그 단계가 될 때)은 구축자가 정했다.
- 설정 파일이 `yaml.safe_load` 로 읽히지 않으면 준비 단계에서 즉시 중단·로그한다. 사양서 7.3 은 설정 파일 오류의 처리를 정하지 않는다.
