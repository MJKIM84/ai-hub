# 데이터 스키마 (schemas/)

사양서 부록 B 의 세 예시(research.json, verification.json, pages.json)를 JSON Schema draft 2020-12 로 옮긴 것이다. 세 에이전트가 반환하는 구조화 출력은 이 스키마를 통과해야 하며, 스키마 불일치는 퍼블리셔가 반려한다(사양서 6.0 규칙 7, 6.4 순서 1, 7.3).

| 파일 | 만드는 에이전트 | 저장 위치 | 사양서 |
|---|---|---|---|
| `research.schema.json` | 리서치 에이전트 | `runs/<run_id>/research.json` | 부록 B.1, 6.1 |
| `verification.schema.json` | 내용 검증 에이전트(1차·2차 공용) | `runs/<run_id>/verification.json`, `verification2.json` | 부록 B.2, 6.2 |
| `pages.schema.json` | 스토리텔러 에이전트 | `runs/<run_id>/pages.json` (+ `pages/`) | 부록 B.3, 6.3 |
| `examples/*.json` | — | 부록 B 예시의 `…` 자리를 실제 값으로 채운 유효한 예 | 부록 B |

## 공통 규칙

- 모든 객체(최상위와 배열 항목 객체)는 `additionalProperties: false` 다. 예시에 없는 필드는 아래 표에 "선택"으로 적힌 것만 허용한다.
- `required` 는 예시의 최상위 필드 전부다. 단 `track`(research), `track_checks`(verification), `track_updates`·`area_reflection_proposals`(pages)는 트랙 실행에만 넣는 선택 필드다.
- 날짜는 `YYYY-MM-DD`(`^\d{4}-\d{2}-\d{2}$`), 실행 id 는 `YYYY-MM-DD-NN`(`^\d{4}-\d{2}-\d{2}-\d{2}$`)이다. 발행일·기준일(`published`, `as_of`)은 `YYYY`, `YYYY-MM`, `YYYY-MM-DD` 를 허용한다.
- id 형식: finding `f1`, `f2` …(`^f[0-9]+$`) / 참고문헌 `ref-003`(`^ref-\d{3}$`, ref-001~ref-010 은 부록 A 12장 1~10번) / 열린 질문 `oq-012`(`^oq-\d{3,}$`) / 트랙 백로그 질문 `q1-01`(`^q[1-9][0-9]?-\d{2}$`, 단계 부분의 상한은 스키마가 아니라 트랙 정의의 `stages` 로 스크립트가 검사) / 정정 요청 `corr-004`(`^corr-\d{3,}$`).
- 한국어 enum 은 예시 값을 그대로 쓴다. 태그 `사실|추정|의견`, 판정 `승인|조건부 승인|반려|통과|수정 후 재검증|불통과`, 태그 처분 `유지|강등|삭제|열린 질문 이동`, 출처 유형 `표준|논문|오픈소스 문서|정부·연구기관|업계 보고서|벤더 문서|기사`, 신뢰도 `high|medium|low`.
- 세부영역 명칭(`target.area_name`)과 대분류 명칭(`target.category`)은 `_source/ROP_SCM_연구분야_분류.md` 의 28개·7개 문자열 enum 이다. "7. 화물·재고·자산 식별과 추적", "B. 공통 정보·환경 모델"처럼 번호와 이름을 함께 쓴 원문 그대로만 통과한다.
- 물류 흐름 단계 enum `입고|적치|보충|피킹|포장|출하|반품`, 여섯 항목 enum `시작 조건|작업 대상|수행 자원|제약|완료·인계|예외·성과` (부록 A 11장, `pipeline/lib/paths.py` 의 `FLOW_STEPS`/`FLOW_ITEMS` 와 동일).
- 페이지 경로는 위키 루트 기준 `docs/….md` 다(`^docs/[A-Za-z0-9_./-]+\.md$`). 페이지의 특정 절을 가리키는 링크 필드 세 곳(`open_question_updates[].link`, `flow_matrix_updates[].link`, `track_updates.backlog_updates[].answer_link`)만 같은 경로에 `#앵커` 를 허용한다(`^docs/[A-Za-z0-9_./-]+\.md(#\S+)?$`). 파일을 가리키는 `pages[].path`, `page_proposals[].path`, `cited_by[]`, `stage_page` 는 앵커를 받지 않는다.
- JSON Schema 로 검사할 수 없는 것은 `pipeline/` 스크립트가 따로 검사한다: 참조 무결성(`findings[].source_ids` → `sources[].id`, `claim_checks[].finding_id` → finding id, `evidence_finding_ids`, finding id 의 유일성, 백로그 id 의 유일성) / 트랙 단계 번호의 상한(`track.stage`, `new_questions[].stage`, 백로그 id 의 단계 부분, `stage_page`, `backlog_updates[].stage`, `stage_transition.to_stage` 가 `config/tracks/<slug>.yaml` 의 `stages` 이하인지. 스키마는 1 이상만 본다) / 스토리텔러 반환값의 `pages[]` 모든 항목에 `content` 가 있는지(agent_runner 가 `pages.schema.json` 의 `$defs/returned` 로 검사하고, 없으면 스키마 불일치와 같이 7.3 절차를 밟는다) / `[사실]` finding 의 근거가 `벤더 문서` 유형 출처뿐인데 `vendor_claim: true` 가 없는 경우(퍼블리셔 또는 검증 에이전트가 6.2 항목 13 으로 잡는다) / 트랙 실행에서 `answered_question_ids` 가 비어 있을 때 `self_check.limits` 에 "답한 질문 없음: <이유>" 가 있는지와 그 이유가 예산 도달·출처 부재인지(검증 에이전트가 판단해 부분 결과가 아니면 반려).
- 실행 유형에 따른 트랙 블록의 유무도 스크립트가 검사한다. `research.json` 은 `run_type` 을 갖고 있어 스키마가 `track` 블록을 양방향으로 강제하지만, `verification.json` 과 `pages.json` 에는 `run_type` 이 없다. 따라서 퍼블리셔는 `target.json`/`research.json` 의 `run_type` 이 `track` 이 아니면 `verification.json` 의 `track_checks`, `pages.json` 의 `track_updates`·`area_reflection_proposals` 가 있을 때 반려하고, `track` 이면 그 세 필드를 필수로 본다(부록 B.2·B.3 "트랙 실행에만 넣는다", 6.4 순서 1).

## research.schema.json (부록 B.1)

| 필드 | 타입 | 의미 | 누가 채우는가 |
|---|---|---|---|
| `run_id` | string, `^\d{4}-\d{2}-\d{2}-\d{2}$` | 실행 id (실행 컨텍스트에서 그대로) | 리서치 |
| `date` | string, 날짜 | 실행 날짜 (Asia/Seoul) | 리서치 |
| `run_type` | enum `area_deep_dive\|topic\|update\|weekly_review\|monthly_recheck\|track` | 실행 유형. `track` 은 공통 규약으로 추가 | 리서치(target.json 에서) |
| `target` | object | 조사 대상. target.json 과 같아야 한다 | 리서치(target.json 에서) |
| `target.area_no` | integer 1~28 또는 null | 대상 세부영역 번호. `weekly_review`·`monthly_recheck` 만 null 허용 | 〃 |
| `target.area_name` | enum(원문 28개) 또는 null | 대상 세부영역의 원문 명칭 | 〃 |
| `target.category` | enum(원문 7개) 또는 null | 소속 대분류의 원문 명칭 | 〃 |
| `gaps` | string[] | 비어 있거나 약한 섹션(갭) | 리서치 |
| `research_questions` | string[] | 조사 질문. 5~7개(원문 질문 1개 이상)는 프롬프트 규칙이며 스키마는 개수를 강제하지 않는다 | 리서치 |
| `findings[]` | object[] | 발견 사항 | 리서치 |
| `findings[].id` | string `^f[0-9]+$` | finding id | 리서치 |
| `findings[].claim` | string | 주장 한 문장 | 리서치 |
| `findings[].tag` | enum `사실\|추정\|의견` | 사실 표기 태그(5.3). `[사실]` 이면 `source_ids` 1개 이상 필수 | 리서치(검증이 강등·삭제 지시) |
| `findings[].source_ids` | string[] `^ref-\d{3}$` | 근거 출처 id (`sources[].id` 참조) | 리서치 |
| `findings[].cross_checked` | boolean | 독립 출처 2개 이상으로 교차 확인했는가 | 리서치 |
| `findings[].confidence` | enum `high\|medium\|low` | 신뢰도. `web_fetch_available: false` 면 high 금지(프롬프트 규칙) | 리서치 |
| `findings[].evidence_excerpt` | string ≤500자 | 짧은 근거 발췌 | 리서치 |
| `findings[].as_of` | string `YYYY[-MM[-DD]]` | 기준일(발행일 또는 확인일) | 리서치 |
| `findings[].flow_step` | enum(7단계) 또는 null | 물류 흐름 단계 | 리서치 |
| `findings[].flow_item` | enum(6항목) 또는 null | 여섯 항목 | 리서치 |
| `findings[].source_unopened` | boolean, 선택 | 원문 미열람 표시 | 리서치 |
| `findings[].vendor_claim` | boolean, 선택 | 벤더(제조사·솔루션 업체) 문서에서 가져온 기능·성능 주장이면 true(5.3, 8.1, 6.2 항목 13). `cross_checked: false` 이면 `tag` 는 `추정\|의견` 만 허용(`[사실]` 불가). 해당 없으면 넣지 않는다 | 리서치 |
| `sources[]` | object[] | 이번 실행에서 쓴 출처(기존 참고문헌 재사용 포함) | 리서치 |
| `sources[].id` | string `^ref-\d{3}$` | 출처 id. 새 출처는 ref-011 부터 | 리서치 |
| `sources[].org`, `.title` | string | 기관(저자), 제목 | 리서치 |
| `sources[].published` | string `YYYY[-MM[-DD]]` 또는 null | 발행일. 확인 불가면 null | 리서치 |
| `sources[].url` | string `^https?://` | URL | 리서치 |
| `sources[].type` | enum(출처 유형 7종) | 출처 유형 | 리서치 |
| `sources[].reliability` | enum `high\|medium\|low` | 출처 신뢰도 | 리서치 |
| `sources[].accessed` | string, 날짜 | 접근일 | 리서치 |
| `sources[].summary` | string | 한두 문장 요약 | 리서치 |
| `sources[].source_unopened` | boolean, 선택 | 원문 미열람 표시(출처 단위) | 리서치 |
| `page_proposals[]` | `{action: new\|update, path, sections[], rationale}` | 페이지 제안. `sections` 항목은 `"6"` 또는 `"6. 대표 접근법과 기술"` | 리서치 |
| `glossary_candidates[]` | `{term_ko, term_en, definition}` | 용어 후보 | 리서치 |
| `open_questions_new` | string[] | 새 열린 질문(문장). id 는 퍼블리셔가 부여 | 리서치 |
| `open_questions_resolved` | string[] `^oq-\d{3,}$` | 해결 제안 열린 질문 id(해결 판정은 검증) | 리서치 |
| `self_check` | object | 자체 점검(6.1 절차 6) | 리서치 |
| `self_check.source_count`, `.cross_checked_count` | integer ≥0 | 출처 수, 교차 확인 수 | 리서치 |
| `self_check.unverified`, `.scope_violations` | string[] | 미확인 항목, 범위 경계 위반 | 리서치 |
| `self_check.budget_used` | `{queries: int, sources: int}` | 예산 사용량 | 리서치 |
| `self_check.limits` | string | 한계 서술 | 리서치 |
| `track` | object, 선택 | 트랙 실행 블록. `run_type: track` 이면 필수, 아니면 금지 | 리서치 |
| `track.slug` | string slug | 트랙 slug | 리서치(target.json 에서) |
| `track.stage` | integer ≥1 | 현재 단계. 상한은 트랙 정의(`config/tracks/<slug>.yaml` 의 `stages`)로 스크립트가 검사 | 리서치(target.json 에서) |
| `track.answered_question_ids` | string[] `^q[1-9][0-9]?-\d{2}$`, 0~3개 | 답한 백로그 질문 id. 8.2 (1)·6.1 의 "1~3개"가 목표이고 상한 3개는 스키마가 강제한다. 0개는 예산 도달·출처 부재로 답을 못 낸 부분 결과(6.0 규칙 9, 7.3)일 때만 허용하며 `self_check.limits` 에 "답한 질문 없음: <이유>", `self_check.unverified` 에 "q1-03 미답: <이유>" 를 남긴다 | 리서치(부분 결과 여부는 검증이 판단) |
| `track.new_questions[]` | `{id?, question, stage: ≥1, rationale_finding_id}` | 새 후속 질문. `id` 는 선택. 없으면 `[]` 로 두고 "없음"의 이유는 `self_check.limits` 에 "후속 질문 없음: <이유>" 로 남긴다(8.2 (2)) | 리서치 |
| `track.ontology_changes[]` | `{op: add\|modify\|remove, kind: concept\|relation, name, evidence_finding_ids[] (≥1), description?}` | 온톨로지 초안 변경 제안 | 리서치(반영 여부는 검증) |
| `track.stage_completion_self_assessment` | `{met: bool, missing: string[]}` | 단계 완료 조건 자체 평가(최종 판정은 검증) | 리서치 |

조건 규칙(if/then):

- `run_type == "track"` → `track` 필수. 그 외 → `track` 이 있으면 불합격("track 블록은 트랙 실행에만 넣는다").
- `run_type ∈ {area_deep_dive, topic, update, track}` → `target.area_no` 는 integer, `area_name`·`category` 는 string(null 불가).
- `findings[].tag == "사실"` → `source_ids` 최소 1개.
- `findings[].vendor_claim == true` 이고 `cross_checked == false` → `tag ∈ {추정, 의견}` (벤더 주장은 독립 출처로 교차 확인되기 전에는 `[사실]` 불가, 5.3).
- `track.answered_question_ids` 는 0개 이상 3개 이하(`minItems: 0, maxItems: 3`). `track.ontology_changes[].evidence_finding_ids` 는 1개 이상.

## verification.schema.json (부록 B.2)

| 필드 | 타입 | 의미 | 누가 채우는가 |
|---|---|---|---|
| `run_id` | string | 실행 id | 검증 |
| `stage` | enum `first\|second` | 1차(브리프) / 2차(서술) | 검증(실행 컨텍스트에서) |
| `verdict` | enum | 1차: `승인\|조건부 승인\|반려`, 2차: `통과\|수정 후 재검증\|불통과` (stage 로 조건화) | 검증 |
| `claim_checks[]` | object[] | 주장별 검증 결과. 2차는 브리프 밖 주장(드리프트)만 다루므로 비어 있을 수 있다 | 검증 |
| `claim_checks[].finding_id` | string `^f[0-9]+$` | 검증한 finding id | 검증 |
| `claim_checks[].source_exists` | boolean | 출처 실재성 | 검증 |
| `claim_checks[].supports_claim` | boolean | 주장–출처 일치 | 검증 |
| `claim_checks[].cross_checked` | boolean | 교차 확인 | 검증 |
| `claim_checks[].tag_decision` | enum `유지\|강등\|삭제\|열린 질문 이동` | 태그 처분 | 검증 |
| `claim_checks[].note` | string | 검증 메모 | 검증 |
| `category_fit` | `{ok: bool, reassign_to: int 1~28 \| null}` | 분류 적합성. 재배치 대상은 세부영역 번호 | 검증 |
| `scope_boundary` | `{ok: bool, issues: string[]}` | 범위 경계(부록 A 9장) | 검증 |
| `duplication` | `{ok: bool, overlaps: string[]}` | 중복·모순 | 검증 |
| `terminology` | `{ok: bool, conflicts: string[]}` | 용어 일관성 | 검증 |
| `quotation_check` | `{ok: bool, issues?: string[]}` | 인용 길이·저작권. `issues` 는 선택 | 검증 |
| `corrections_applied` | string[] `^corr-\d{3,}$` | 반영 확인한 정정 요청 id | 검증 |
| `required_fixes` | string[] | 수정 지시. `조건부 승인`·`수정 후 재검증` 이면 1개 이상 | 검증(스토리텔러가 이행) |
| `confidence` | enum `high\|medium\|low` | 페이지에 부여할 신뢰도 | 검증 |
| `verification_note` | string | 페이지 "검증 노트"에 실을 문구 | 검증 |
| `retry_reason` | string 또는 null | `반려`·`불통과` 면 문자열 필수(재조사 사유·보강 질문), 그 외 null | 검증 |
| `track_checks` | object, 선택 | 트랙 실행 추가 검증(6.2 항목 12~17). 트랙 실행에만 | 검증 |
| `track_checks.standard_sources_ok` | boolean | 표준 주장이 발행 기관 자료 근거인가(원문 미열람 표시 포함) | 검증 |
| `track_checks.vendor_claims_tagged` | boolean | 제조사 기능·성능이 벤더 주장으로 표기됐는가(`findings[].vendor_claim: true` 또는 `evidence_excerpt` 첫머리 "벤더 주장: ", 교차 확인 전 `[사실]` 없음) | 검증 |
| `track_checks.ontology_changes_grounded` | boolean | 온톨로지 변경마다 근거 finding 이 있고 충돌이 없는가 | 검증 |
| `track_checks.backlog_duplicates` | string[] | 백로그와 중복인 새 질문(항목 15 전반) | 검증 |
| `track_checks.stage_tag_issues` | string[], 선택 | 단계 태그가 질문 내용과 맞지 않는 새 질문과 맞는 단계(항목 15 후반 "단계 태그가 맞는지"). 문제가 없으면 `[]` 또는 생략 | 검증 |
| `track_checks.completeness_wording_ok` | boolean | "빠짐없이·완전" 표현 점검 | 검증 |
| `track_checks.stage_complete` | boolean | 단계 완료 조건 충족 최종 판정 | 검증 |
| `track_checks.stage_transition_approved` | boolean | 단계 전환 승인. true 면 `stage_complete` 도 true | 검증 |

조건 규칙(if/then):

- `stage == first` → `verdict ∈ {승인, 조건부 승인, 반려}` / `stage == second` → `verdict ∈ {통과, 수정 후 재검증, 불통과}`.
- `verdict ∈ {반려, 불통과}` → `retry_reason` 은 비어 있지 않은 문자열.
- `verdict ∈ {조건부 승인, 수정 후 재검증}` → `required_fixes` 1개 이상.
- `track_checks.stage_transition_approved == true` → `track_checks.stage_complete == true`.

## pages.schema.json (부록 B.3)

| 필드 | 타입 | 의미 | 누가 채우는가 |
|---|---|---|---|
| `run_id` | string | 실행 id | 스토리텔러 |
| `pages[]` | object[], 1개 이상 | 생성·갱신 페이지 | 스토리텔러 |
| `pages[].path` | string `^docs/…\.md$` | 위키 루트 기준 페이지 경로 | 스토리텔러 |
| `pages[].action` | enum `create\|update` | 생성/갱신 | 스토리텔러 |
| `pages[].status` | enum(5.2 상태 6종) | 산출 시점 상태(보통 `draft`). 2차 통과 후 `published` 는 퍼블리셔가 바꾼다 | 스토리텔러 → 퍼블리셔 |
| `pages[].diff_summary` | string | 무엇이 바뀌었는지 한 줄 | 스토리텔러 |
| `pages[].content` | string `^---\n…`, 루트 스키마에서는 선택 | 프런트매터 포함 페이지 전체 마크다운. 에이전트 반환값에는 필수이며 agent_runner 가 `$defs/returned`(루트 + `pages[]` 모든 항목에 `content` 필수)로 검사한 뒤 `runs/<run_id>/pages/` 로 풀어내고 저장 사본에서는 뺀다 | 스토리텔러 → agent_runner 가 검사·제거 |
| `changelog_entry` | string | `YYYY-MM-DD \| <대상 이름> \| <한 줄 요약> \| run <run_id>` 형식 | 스토리텔러(반영은 퍼블리셔) |
| `index_updates.home_recent` | string | 홈 "최근 업데이트" 한 줄 | 스토리텔러 |
| `index_updates.category_recent` | string | 대분류 "최근 업데이트" 한 줄 | 스토리텔러 |
| `index_updates.area_recent` | string, 선택 | 세부영역 "12. 최근 업데이트" 한 줄 | 스토리텔러 |
| `glossary_updates[]` | `{action?: new\|update, slug?, term_ko, term_en, definition, description?, related_areas?: int[], sources?: ref[]}` | 용어집 항목(4.7 필드) | 스토리텔러(반영은 퍼블리셔) |
| `reference_updates[]` | research.json `sources[]` 와 같은 필드 + `cited_by?: path[]` | 참고문헌 항목(4.7 필드). 검증이 확인한 출처만 | 스토리텔러(리서치 제안 → 검증 확인) |
| `open_question_updates[]` | `{action: new\|update, id?, question, areas: int[] (≥1), status: 열림\|조사 중\|해결\|보류, link: path(#앵커 허용)\|null}` | 열린 질문 갱신. `update` 면 `id` 필수. 트랙 전용 질문은 여기 넣지 않는다 | 스토리텔러(해결 판정은 검증) |
| `flow_matrix_updates[]` | `{step: enum7, item: enum6, link: path(#앵커 허용), title?}` | 흐름 매트릭스 칸 갱신 | 스토리텔러 |
| `additional_research_requests` | string[] | 브리프에 없어 본문에 못 넣은 사실의 추가 조사 요청 | 스토리텔러 |
| `fixes_applied` | string[] | 조건부 승인의 수정 목록 이행 표시 | 스토리텔러 |
| `track_updates` | object, 선택 | 트랙 실행 갱신 블록 | 스토리텔러 |
| `track_updates.stage_page` | string `docs/tracks/<slug>/stage-N-….md` (N ≥1) | 갱신한 단계 페이지. N 의 상한은 트랙 정의의 `stages` 로 스크립트가 검사 | 스토리텔러 |
| `track_updates.ontology_draft_version` | string `^\d+(\.\d+)?$` | 온톨로지 초안 버전(`ontology-draft.md` 프런트매터 `ontology_version` 과 같은 값). v0 시드는 `"0"`, 승인된 변경을 반영할 때마다 `"0.1"`, `"0.2"`, …. 변경이 없으면 현재 버전 그대로(첫 트랙 실행에서 변경이 없으면 `"0"`) | 스토리텔러 |
| `track_updates.backlog_updates[]` | `{id, status: 열림\|조사 중\|답함\|보류\|폐기, answer_link: path(#앵커)\|null, question?, stage?, origin?}` | 백로그 갱신. 새 질문은 `question`·`stage`(≥1)·`origin`(8.2 문구 그대로 finding id 또는 `사용자`) 을 함께. finding id 는 실행마다 `f1` 부터 다시 시작하므로 퍼블리셔가 `backlog.json` 에 저장할 때 이 파일의 `run_id` 를 `origin_run_id` 로 함께 기록한다. 8.2 항목 형식의 "답한 실행 id"(`backlog.json` 의 `answered_run_id`)는 별도 필드 없이, `status` 가 `답함` 으로 바뀌는 항목에 이 파일의 `run_id` 를 퍼블리셔가 채우고 이미 `답함` 인 항목의 값은 유지한다 | 스토리텔러(반영은 퍼블리셔) |
| `track_updates.log_entry` | string | 트랙 로그 실행 기록 | 스토리텔러(기록은 퍼블리셔) |
| `track_updates.overview_progress` | string | 트랙 개요 "단계 진행 현황" 반영 내용 | 스토리텔러 |
| `track_updates.stage_transition` | `{to_stage: ≥1, reason}`, 선택 | 단계 전환(검증의 `stage_transition_approved` 가 true 일 때만) | 스토리텔러 |
| `area_reflection_proposals[]` | `{area_no: 1~28, section: enum(세부영역 절 3~11, 13), summary}` | 세부영역 페이지 반영 제안(반영은 다음 해당 영역 실행). `section` 은 세부영역 페이지 H2 문자열 그대로(괄호 설명 포함, 예 `5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)`) | 스토리텔러 |
| `standards_updates[]` | `{name, kind: 표준\|오픈소스\|평가 프로그램\|프레임워크, org, url, related_areas: int[] (≥1), summary, ref_id?}`, 선택 | 표준·프레임워크 목록 갱신 | 스토리텔러(반영은 퍼블리셔) |

조건 규칙(if/then): `open_question_updates[].action == "update"` → `id` 필수.

반환값 변형 `$defs/returned`: 루트 스키마(`{"$ref": "#"}`)에 `pages[]` 모든 항목의 `content` 필수를 더한 것이다. agent_runner 는 스토리텔러 반환값을 이 변형으로 검사한다(`Draft202012Validator(schema).evolve(schema=schema["$defs"]["returned"])`, 또는 `$ref: "https://rop-wiki.invalid/schemas/pages.schema.json#/$defs/returned"` 를 registry 로 해석). 저장 사본 `runs/<run_id>/pages.json` 은 루트 스키마로 검사한다.

## 예시와 검증 방법

`examples/` 는 부록 B 의 세 예시를 유효한 JSON 으로 채운 것이다. 조건 규칙의 분기를 모두 밟도록 일반 실행과 트랙 실행을 나누었다.

| 파일 | 내용 |
|---|---|
| `research.json` | 7. 화물·재고·자산 식별과 추적 영역 심화(`area_deep_dive`), `track` 블록 없음. `web_fetch_available: false` 환경의 예: 모든 출처·finding 에 `source_unopened: true`, 출처 `summary` 는 "원문 미열람. "으로 시작, 신뢰도 `high` 없음, `self_check.limits` 에 차단 환경 명시 |
| `research.track.json` | 트랙 실행(`track`), 5. 로봇 능력·작업 온톨로지 대상, `track` 블록 포함 |
| `verification.first.json` | 1차 검증, `조건부 승인` + `required_fixes`. 출처 실재성을 원문 미열람(검색 결과 일치)으로 확인한 `note` 예 |
| `verification.second.json` | 2차 검증, `통과` |
| `verification.track.json` | 트랙 실행 1차 검증, `track_checks` 포함 |
| `pages.json` | 일반 실행, `pages[].content` 포함(에이전트 반환 형태, `$defs/returned` 통과) |
| `pages.track.json` | 트랙 실행, `track_updates`·`area_reflection_proposals`·`standards_updates` 포함, `content` 없음(저장 사본 형태) |

세 예시가 모두 통과하는지 확인(위키 루트에서):

```bash
python3 -c "
import json, glob
from jsonschema import Draft202012Validator as V
for name in ('research','verification','pages'):
    s = json.load(open(f'schemas/{name}.schema.json', encoding='utf-8'))
    V.check_schema(s)   # 메타스키마(draft 2020-12) 검사
    v = V(s)
    for f in sorted(glob.glob(f'schemas/examples/{name}*.json')):
        errs = list(v.iter_errors(json.load(open(f, encoding='utf-8'))))
        print(f, 'OK' if not errs else errs[0].message)
"
```

잘못된 예가 모두 거부되고 조건 분기의 허용 쪽이 통과하는지 확인(위키 루트에서). 아래 스크립트는 `examples/` 의 유효한 예를 한 군데씩 깨뜨린 잘못된 예 53건(필수 필드 누락, 예시에 없는 필드, enum 밖의 값, 날짜·id·URL 형식, 번호만 쓴 세부영역 명칭, stage 와 맞지 않는 verdict, 트랙 아닌 실행의 `track` 블록, `[사실]` 인데 출처 없음, 교차 확인 없는 벤더 주장의 `[사실]`, 답한 질문 4개, 단계 0, 반환값인데 `content` 없음, 링크 필드가 아닌 경로의 앵커, 근거 없는 온톨로지 변경, 괄호 설명을 뺀 절 제목 등)과 유효한 변형 13건(영역 null 인 주간 정리, 답한 질문 0개의 부분 결과, 벤더 주장 + `[추정]`, 단계 8·10, 링크 앵커, 저장 사본과 반환값 등)을 만들어 검사한다. 출력이 `잘못된 예 53건 중 거부 53건 / 통과해 버린 것: 없음` 과 `유효한 변형 13건 중 통과 13건 / 거부된 것: 없음` 이면 정상이다. 스키마나 예시를 고치면 이 목록도 함께 고친다(파일로 저장해 두려면 `pipeline/checks/` 아래 두는 것을 pipeline 담당에게 요청).

```bash
python3 - <<'PY'
import copy, json
from jsonschema import Draft202012Validator as V
DEL = object()
def load(p): return json.load(open(p, encoding='utf-8'))
S = {n: V(load(f'schemas/{n}.schema.json')) for n in ('research', 'verification', 'pages')}
S['pages-returned'] = S['pages'].evolve(schema=S['pages'].schema['$defs']['returned'])  # 에이전트 반환값용 변형
def mutate(doc, *changes):  # 경로, 값, 경로, 값, … (값이 DEL 이면 삭제)
    d = copy.deepcopy(doc)
    for path, value in zip(changes[::2], changes[1::2]):
        cur = d
        for k in path[:-1]: cur = cur[k]
        if value is DEL: del cur[path[-1]]
        else: cur[path[-1]] = value
    return d
E = lambda f: load(f'schemas/examples/{f}')
R, RT = E('research.json'), E('research.track.json')
V1, V2, VT = E('verification.first.json'), E('verification.second.json'), E('verification.track.json')
P, PT = E('pages.json'), E('pages.track.json')
INVALID = [  # (스키마, 예시를 한 군데 깨뜨린 문서, 설명) — 모두 거부돼야 한다
 ('research', mutate(R, ['findings'], DEL), '필수 필드 누락'),
 ('research', mutate(R, ['extra'], 1), '예시에 없는 필드'),
 ('research', mutate(R, ['run_type'], 'daily'), 'run_type enum 밖'),
 ('research', mutate(R, ['run_id'], '2026-9-24-1'), '실행 id 형식'),
 ('research', mutate(R, ['date'], '2026/09/24'), '날짜 형식'),
 ('research', mutate(R, ['target', 'area_name'], '7번'), '번호만 쓴 세부영역 명칭'),
 ('research', mutate(R, ['target', 'area_no'], 29), '세부영역 번호 범위 밖'),
 ('research', mutate(R, ['target', 'area_no'], None), '영역 심화인데 area_no null'),
 ('research', mutate(R, ['findings', 0, 'tag'], '가설'), 'finding 태그 enum 밖'),
 ('research', mutate(R, ['findings', 0, 'source_ids'], []), '[사실]인데 출처 없음'),
 ('research', mutate(R, ['findings', 0, 'vendor_claim'], True, ['findings', 0, 'cross_checked'], False), '벤더 주장인데 교차 확인 없이 [사실]'),
 ('research', mutate(R, ['findings', 0, 'vendor_claim'], 'yes'), 'vendor_claim 이 boolean 이 아님'),
 ('research', mutate(R, ['findings', 0, 'as_of'], '2024-6'), '기준일 형식'),
 ('research', mutate(R, ['findings', 0, 'flow_step'], '피킹 단계'), '흐름 단계 enum 밖'),
 ('research', mutate(R, ['sources', 0, 'type'], '블로그'), '출처 유형 enum 밖'),
 ('research', mutate(R, ['sources', 0, 'published'], '2024/06'), '발행일 형식'),
 ('research', mutate(R, ['sources', 0, 'url'], 'ftp://x'), 'URL 형식'),
 ('research', mutate(R, ['track'], RT['track']), '트랙 아닌 실행의 track 블록'),
 ('research', mutate(RT, ['track'], DEL), '트랙 실행인데 track 블록 없음'),
 ('research', mutate(RT, ['track', 'answered_question_ids'], ['q1-01', 'q1-02', 'q1-03', 'q1-04']), '답한 질문 4개'),
 ('research', mutate(RT, ['track', 'answered_question_ids'], ['q0-01']), '백로그 id 단계 0'),
 ('research', mutate(RT, ['track', 'new_questions', 0, 'stage'], 0), '단계 범위 밖(0)'),
 ('research', mutate(RT, ['track', 'stage'], 0), '현재 단계 0'),
 ('research', mutate(RT, ['track', 'ontology_changes', 0, 'evidence_finding_ids'], []), '근거 없는 온톨로지 변경'),
 ('verification', mutate(V1, ['verdict'], '통과'), '1차인데 2차 판정 값'),
 ('verification', mutate(V2, ['verdict'], '승인'), '2차인데 1차 판정 값'),
 ('verification', mutate(V1, ['stage'], 'third'), 'stage enum 밖'),
 ('verification', mutate(V1, ['required_fixes'], []), '조건부 승인인데 수정 목록 없음'),
 ('verification', mutate(V1, ['verdict'], '반려', ['retry_reason'], None), '반려인데 사유 없음'),
 ('verification', mutate(V1, ['claim_checks', 0, 'tag_decision'], '보류'), '태그 처분 enum 밖'),
 ('verification', mutate(V1, ['corrections_applied'], ['c4']), '정정 요청 id 형식'),
 ('verification', mutate(VT, ['track_checks', 'stage_transition_approved'], True), '완료 아닌데 단계 전환 승인'),
 ('verification', mutate(VT, ['track_checks', 'stage_tag_issues'], 'q1-07'), 'stage_tag_issues 가 배열이 아님'),
 ('pages', mutate(P, ['pages'], []), '페이지 0개'),
 ('pages', mutate(P, ['pages', 0, 'path'], 'categories/x.md'), 'docs/ 밖 경로'),
 ('pages', mutate(P, ['pages', 0, 'path'], 'docs/x.md#anchor'), '페이지 경로에 앵커(링크 필드가 아님)'),
 ('pages', mutate(P, ['pages', 0, 'content'], '# 프런트매터 없음'), 'content 가 프런트매터로 시작하지 않음'),
 ('pages-returned', mutate(P, ['pages', 0, 'content'], DEL), '에이전트 반환값인데 content 없음($defs/returned)'),
 ('pages-returned', mutate(P, ['extra'], 1), '반환값 변형도 루트 규칙(예시에 없는 필드)을 적용'),
 ('pages', mutate(P, ['pages', 0, 'status'], 'final'), '페이지 상태 enum 밖'),
 ('pages', mutate(P, ['changelog_entry'], '2026-09-24 7. 화물·재고·자산 식별과 추적 갱신'), '변경 이력 형식'),
 ('pages', mutate(P, ['open_question_updates', 0, 'action'], 'update'), '열린 질문 update 인데 id 없음'),
 ('pages', mutate(P, ['open_question_updates', 0, 'link'], 'open-questions.md#oq-001'), '열린 질문 링크가 docs/ 밖'),
 ('pages', mutate(P, ['flow_matrix_updates', 0, 'item'], '완료'), '여섯 항목 enum 밖'),
 ('pages', mutate(PT, ['track_updates', 'stage_page'], 'docs/tracks/manual-capability-ontology/stage-0-x.md'), '단계 0 페이지 경로'),
 ('pages', mutate(PT, ['track_updates', 'ontology_draft_version'], 'v0.1'), '온톨로지 버전 형식'),
 ('pages', mutate(PT, ['track_updates', 'backlog_updates', 0, 'status'], '완료'), '백로그 상태 enum 밖'),
 ('pages', mutate(PT, ['track_updates', 'backlog_updates', 1, 'origin'], 'seed'), '제기 근거 형식(finding id 또는 사용자)'),
 ('pages', mutate(PT, ['track_updates', 'backlog_updates', 1, 'stage'], 0), '새 질문 단계 0'),
 ('pages', mutate(PT, ['track_updates', 'stage_transition'], {'to_stage': 0, 'reason': 'x'}), '단계 0 으로 전환'),
 ('pages', mutate(PT, ['area_reflection_proposals', 0, 'section'], '1. 한 줄 정의'), '분류원문 절에 반영 제안'),
 ('pages', mutate(PT, ['area_reflection_proposals', 0, 'section'], '5. 현장 시나리오'), '괄호 설명을 뺀 절 제목'),
 ('pages', mutate(PT, ['standards_updates', 0, 'kind'], '규격'), '표준 종류 enum 밖'),
]
VALID = [  # 조건 분기의 허용 쪽 — 모두 통과해야 한다
 ('research', mutate(R, ['run_type'], 'weekly_review', ['target'], {'area_no': None, 'area_name': None, 'category': None}), '주간 정리는 영역 null 허용'),
 ('research', mutate(R, ['findings', 0, 'vendor_claim'], True, ['findings', 0, 'tag'], '추정'), '벤더 주장 + [추정]'),
 ('research', mutate(R, ['findings', 0, 'vendor_claim'], True, ['findings', 0, 'cross_checked'], True), '벤더 주장이라도 교차 확인되면 [사실] 허용'),
 ('research', mutate(RT, ['track', 'new_questions'], []), '후속 질문 없음(이유는 self_check.limits)'),
 ('research', mutate(RT, ['track', 'answered_question_ids'], [], ['self_check', 'limits'], '답한 질문 없음: 검색 예산 도달'), '답한 질문 0개(부분 결과, 이유는 self_check.limits)'),
 ('research', mutate(RT, ['track', 'stage'], 8, ['track', 'new_questions', 0, 'stage'], 10, ['track', 'answered_question_ids'], ['q8-01']), '단계 8·10(상한은 트랙 정의로 스크립트가 검사)'),
 ('verification', mutate(VT, ['track_checks', 'stage_tag_issues'], DEL), '선택 필드 stage_tag_issues 생략'),
 ('pages', mutate(PT, ['track_updates', 'ontology_draft_version'], '0'), 'v0 시드 버전 "0"'),
 ('pages', mutate(P, ['pages', 0, 'content'], DEL), '저장 사본(content 없음, 루트 스키마)'),
 ('pages-returned', P, '에이전트 반환값(content 있음, $defs/returned)'),
 ('pages', mutate(P, ['open_question_updates', 0, 'status'], '해결', ['open_question_updates', 0, 'link'], 'docs/topics/2026/2026-09-24-epcis-handover.md#3-본문'), '열린 질문 링크에 앵커'),
 ('pages', mutate(P, ['flow_matrix_updates', 0, 'link'], P['flow_matrix_updates'][0]['link'] + '#5-현장-시나리오'), '흐름 매트릭스 링크에 앵커'),
 ('pages', mutate(PT, ['track_updates', 'backlog_updates', 1, 'id'], 'q10-01', ['track_updates', 'backlog_updates', 1, 'stage'], 10, ['track_updates', 'stage_page'], 'docs/tracks/manual-capability-ontology/stage-10-x.md', ['track_updates', 'stage_transition'], {'to_stage': 8, 'reason': '예시'}), '단계 8·10 (상한은 트랙 정의로 스크립트가 검사)'),
]
passed_bad = [label for s, d, label in INVALID if not list(S[s].iter_errors(d))]
failed_good = [label for s, d, label in VALID if list(S[s].iter_errors(d))]
print(f'잘못된 예 {len(INVALID)}건 중 거부 {len(INVALID) - len(passed_bad)}건', '/ 통과해 버린 것:', passed_bad or '없음')
print(f'유효한 변형 {len(VALID)}건 중 통과 {len(VALID) - len(failed_good)}건', '/ 거부된 것:', failed_good or '없음')
PY
```

스키마만으로 막지 못하는 것(참조 무결성, 실행 유형에 따른 `track_checks`·`track_updates`·`area_reflection_proposals` 의 유무, 트랙 정의 `stages` 기준의 단계 상한, 반환값의 `content` 유무(`$defs/returned`), 벤더 문서만 근거로 한 `[사실]`, 답한 질문 0개의 부분 결과 여부)은 "공통 규칙"의 스크립트 검사 목록대로 퍼블리셔가 검사한다. 스크립트에서 쓸 때는 `jsonschema.Draft202012Validator(schema).iter_errors(data)` 로 모든 오류를 모아 `log.md` 에 남기는 것을 권한다.

## [가정] 목록

사양서 부록 B 예시에 없거나 예시만으로 정할 수 없어 구축자가 정한 것이다. 바꾸려면 스키마와 `examples/` 를 함께 고친다.

1. `run_type` enum 에 `track` 을 추가했다(공통 규약). 부록 B.1 예시의 `run_type` 문자열에는 없다.
2. `run_type` 이 `track` 이면 `track` 블록이 필수이고, 그 외 실행에서 `track` 블록이 있으면 불합격이다("track 블록은 트랙 실행에만 넣는다"를 양방향으로 강제). 부록 B.1 예시는 7. 화물·재고·자산 식별과 추적 영역 대상과 `track` 블록을 한 JSON 에 함께 보여 주지만 이는 필드 설명용 합성 예시로 보고, `examples/` 는 일반 실행과 트랙 실행으로 나누었다.
3. `target.area_no`·`area_name`·`category` 는 `weekly_review`·`monthly_recheck` 에서만 null 을 허용한다. 주간 정리·월간 재검증은 특정 영역이 없을 수 있기 때문이다. 그 외 실행은 정수·문자열 필수다.
4. `target.area_name` 과 `target.category` 를 원문 28개·7개 명칭 enum 으로 묶었다(번호+이름 표기 규칙과 원문 보호를 데이터 단계에서 강제).
5. `findings[].tag` 는 지시대로 `사실|추정|의견` 만이다. `[가설]`·`[사용자 실험]` 은 페이지 본문 태그이며 finding 태그가 아니다. `experiments/` 결과를 finding 으로 담을 때의 태그·출처 유형 값은 정해져 있지 않다(아래 "남은 문제").
6. `findings[].tag == 사실` 이면 `source_ids` 를 1개 이상 요구한다(5.3 "출처 없는 수치·사례 금지").
7. `findings[].source_unopened`(지시) 외에 `sources[].source_unopened` 와 `reference_updates[].source_unopened` 도 선택 필드로 두었다. 실행 규약의 "모든 출처 항목에 원문 미열람을 표시"를 구조화한 것이다.
8. `findings[].as_of` 와 `sources[].published` 는 `YYYY`, `YYYY-MM`, `YYYY-MM-DD` 를 허용하고(부록 B.1 예시의 `as_of: "2024-06"`, `published: "2023-06"` 이 월 단위라서), `published` 는 확인 불가 시 null 을 허용한다. `examples/research.json` 의 ref-003(GS1 EPCIS)은 부록 A 12장에 발행일이 없어 `published: null` 로 두고 `self_check.unverified` 에 "발행일 미확인"을 남겼으며, 그 finding 의 `as_of` 는 확인일이다(5.3 "확인하지 못한 것은 채우지 않는다").
9. `findings[].evidence_excerpt` 는 500자 상한이다(5.3 "짧은 구절만").
10. `track.new_questions[].id` 선택 필드(지시). id 를 비우면 스토리텔러가 `q<단계>-<두자리>` 로 부여하고 퍼블리셔가 유일성을 검사한다. `track.ontology_changes[].description` 선택 필드를 추가했다(변경 내용 설명이 없으면 스토리텔러가 반영할 수 없기 때문).
11. `category_fit.reassign_to` 는 세부영역 번호(1~28) 또는 null 이다.
12. `quotation_check.issues` 선택 필드를 추가했다(다른 검사 항목과 형식을 맞춤).
13. `verdict` 가 `반려`·`불통과` 면 `retry_reason` 문자열을 요구하고, `조건부 승인`·`수정 후 재검증` 이면 `required_fixes` 1개 이상을 요구한다(6.2 판정 정의와 7.2 재실행 절차). `stage_transition_approved: true` 는 `stage_complete: true` 를 요구한다.
14. `pages[].content` 선택 필드(실행 규약). 프런트매터로 시작(`^---\n`)해야 한다. `pages` 는 1개 이상이다.
15. `changelog_entry` 는 예시 형식 `YYYY-MM-DD | <대상 이름> | <한 줄 요약> | run <run_id>` 를 정규식으로 강제한다. 퍼블리셔는 이를 `data/changelog.json` 의 `{date, run_id, action, page, summary}` 로 옮기며 `action`(생성/갱신/폐기)은 `pages[].action` 에서 정한다.
16. `glossary_updates`, `reference_updates`, `open_question_updates` 는 부록 B.3 예시가 빈 배열이라 항목 형식을 4.7 표의 필드와 `data/open_questions.json`(`pipeline/lib/render.py` 머리말)의 형식에서 구성했다. 열린 질문은 `action: new|update` 로 구분하고 `update` 면 `id` 가 필수다. `flow_matrix_updates[].title`, `index_updates.area_recent` 는 선택으로 추가했다.
17. `standards_updates` 선택 필드(지시)에 `ref_id` 선택 필드를 더했다. `render_standards_table()` 이 `data/standards.json` 항목에서 `ref_id` 를 읽기 때문이다.
18. `track_updates.stage_transition` 선택 필드(지시). `track_updates.backlog_updates[]` 에 새 질문 등록용 `question`, `stage`, `origin` 선택 필드를 더했다(백로그 항목 형식 8.2).
19. `area_reflection_proposals[].section` 은 세부영역 페이지 13개 절 중 분류원문(1·2절)과 자동 영역(12절)을 뺀 10개 절 제목 enum 이다. 값은 `templates/area.md` 의 `## N. 제목`(사양서 5.4 세부 연구영역 페이지 템플릿)과 글자 단위로 같고, 5·9·10·13절의 괄호 설명(`5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)` 등)을 포함한다. `pipeline/checks/protect_source.py` 의 `AREA_SECTIONS` 가 같은 문자열로 H2 를 검사하므로, 괄호를 뺀 짧은 제목은 통과하지 않는다.
20. 페이지의 특정 절을 가리키는 링크 필드 세 곳(`track_updates.backlog_updates[].answer_link`, `open_question_updates[].link`, `flow_matrix_updates[].link`)은 같은 규칙으로 `docs/….md#앵커` 를 허용한다(mkdocs 의 한글 앵커 포함). 해결된 열린 질문(4.7)과 시나리오 칸(B.3)도 답이 실린 절을 가리키는 일이 많기 때문이다. 파일을 가리키는 경로 필드는 앵커를 받지 않는다.
21. `$id` 는 `https://rop-wiki.invalid/schemas/<파일명>` 이다. 실제 호스트가 아니며 스키마 간 `$ref` 도 쓰지 않는다(각 파일이 자기완결).
22. `track_updates.ontology_draft_version` 의 형식은 `^\d+(\.\d+)?$` 다. 온톨로지 초안 시드(`docs/tracks/manual-capability-ontology/ontology-draft.md` 의 `ontology_version: "0"`, `templates/ontology-draft.md`)가 v0 를 `"0"` 으로 적으므로 소수점 없는 버전을 허용해야 첫 트랙 실행(온톨로지 변경 없음)의 `"0"` 이 통과한다. 이후 버전은 `"0.1"`, `"0.2"`, … 다.
23. `track.answered_question_ids` 는 0~3개다(`minItems: 0, maxItems: 3`). 8.2 "트랙 실행 1회의 필수 결과" (1)과 6.1 의 "1~3개"는 목표로 두되, 6.0 규칙 9 와 7.3 이 예산 도달 시 "부분 결과로 마치고 로그에 남긴다/진행한다"고 정하므로 예산 소진·출처 부재로 답을 하나도 못 낸 브리프를 스키마 불일치(재실행·보류)로 보내지 않는다. 0개일 때는 `self_check.limits` 에 "답한 질문 없음: <이유>", `self_check.unverified` 에 "q1-03 미답: <이유>"(`agents/researcher.md` 10.4 형식)를 남기고, 부분 결과가 아닌 0개는 검증 에이전트가 반려한다. 4개 이상은 예산 규칙 위반으로 계속 거부한다. `research_questions` 의 5~7개는 여전히 프롬프트 규칙이며 강제하지 않는다.
24. `track_checks.stage_tag_issues` 선택 필드를 추가했다. 6.2 항목 15 의 후반 "단계 태그가 맞는지"를 담을 자리가 부록 B.2 예시에 없기 때문이다. 필수로 두지 않은 것은 부록 B.2 의 7개 필드만 내는 검증 출력도 통과시키기 위해서다.
25. `track_updates.backlog_updates[]` 에는 8.2 항목 형식의 "답한 실행 id" 필드가 없다. 퍼블리셔가 `status` 가 `답함` 으로 바뀌는 항목의 `answered_run_id` 를 `pages.json` 의 `run_id` 로 채우고, 이미 `답함` 인 항목의 값은 유지한다. `origin` 은 8.2 문구 그대로 finding id 또는 `사용자` 이며 실행 id 를 담지 않는다. finding id 는 실행마다 `f1` 부터 다시 시작하므로, 퍼블리셔가 새 질문을 `backlog.json` 에 저장할 때 `pages.json` 의 `run_id` 를 `origin_run_id` 로 함께 기록해 어느 실행의 finding 인지 남긴다(pipeline 담당 요청, 아래 "남은 문제"). "앞 단계로 되돌아온 질문"(8.2 단계 전환)은 별도 `origin` 값이 아니라 `origin_run_id` 실행의 단계보다 `stage` 가 작은 항목으로 퍼블리셔가 표시한다.
26. `track.new_questions` 가 비어 있을 때 8.2 (2)의 "없음"과 이유는 `self_check.limits` 한 곳에 남긴다(`agents/researcher.md` 10.4 의 "후속 질문 없음: <이유>" 형식과 같음). `stage_completion_self_assessment.missing` 은 완료 조건 전용이다.
27. `findings[].vendor_claim` 선택 필드(boolean)를 추가했다. 5.3 "벤더의 기능·성능 주장은 독립 출처로 확인되기 전까지 `[추정]` 에 '벤더 주장'을 병기", 8.1 트랙 출처 규칙, 6.2 항목 13(`vendor_claims_tagged`)을 뒷받침할 구조화 필드가 부록 B.1 에 없어 검증 에이전트와 퍼블리셔가 `evidence_excerpt` 첫머리 "벤더 주장: " 문자열 파싱에 기대고 있었기 때문이다. `vendor_claim: true` 이고 `cross_checked: false` 이면 `tag` 는 `추정|의견` 만 허용한다(if/then). `sources[].type` 이 `벤더 문서` 인 출처만 근거로 하는 `[사실]` 을 스키마로 거부하는 것은 배열 간 참조라 JSON Schema 로 표현할 수 없어 스크립트·검증 항목 13 에 맡긴다. `agents/researcher.md` 11.8 은 아직 이 필드를 "넣지 않는다"로 적고 있어(선택 필드라 실행은 막히지 않는다) agents 담당에게 반영을 요청한다(아래 "남은 문제").
28. 트랙 단계 번호의 상한을 스키마에서 고정하지 않는다. `track.stage`, `new_questions[].stage`, `backlog_updates[].stage`, `stage_transition.to_stage` 는 `minimum: 1` 만 두고, 백로그 id 는 `^q[1-9][0-9]?-\d{2}$`, 단계 페이지 경로는 `stage-[1-9][0-9]?-…` 다. 8.2 "트랙 추가"가 단계 수(`stages`)를 `config/tracks/<slug>.yaml` 에서 정하므로 7단계가 아닌 트랙도 통과해야 하며, 실제 상한은 퍼블리셔가 트랙 정의의 `stages` 로 검사한다("공통 규칙"의 스크립트 검사 목록). 첫 트랙(7단계)에는 영향이 없다.
29. `pages.schema.json` 에 반환값 변형 `$defs/returned`(`allOf: [{$ref: "#"}, pages[].content 필수]`)를 두었다. 루트 스키마는 저장 사본(`content` 제거) 호환을 위해 `content` 를 선택으로 두므로, 스토리텔러가 `content` 를 빠뜨린 반환값이 6.4 순서 1(스키마 검증)을 지나 파일 풀기 단계에서야 실패하는 것을 막기 위해서다. agent_runner 는 반환값을 이 변형으로 검사하고 불일치는 스키마 불일치와 같이 처리한다(pipeline 담당 요청).

## 남은 문제 (사용자 결정 필요)

- `experiments/` 의 사용자 실험 결과를 finding 으로 담을 때 `tag`(`사실|추정|의견` 뿐)와 `sources[].type`(7종 뿐)에 맞는 값이 없다. 기본안: 태그는 `추정`, 출처 유형은 `정부·연구기관` 이 아닌 별도 값 `사용자 실험` 을 두 enum 에 추가. 추가 전까지는 리서치 에이전트가 `self_check.limits` 에 실험 반영 사실을 적고 스토리텔러가 페이지에서 `[사용자 실험]` 태그를 붙인다.
- 2차(서술) 검증의 세부 항목(주장 드리프트, 태그·각주 유지, `[분류원문]` 훼손, 섹션 순서, 링크, 문체, 분량)은 구조화 필드 없이 `required_fixes`·`verification_note` 에 서술한다. 필요하면 `narrative_checks` 객체를 선택 필드로 추가할 수 있다.
- `agents/researcher.md` 11.8 이 언급한 선택 필드(`findings[].vendor_claim`, `sources[].fetched`, `glossary_candidates[].source_ids`·`area_nos`, `track.answers[]`, `track.new_questions[].parent_question_id`, 태그·출처 유형 값 `사용자 실험`) 가운데 이 스키마가 허용하는 것은 `track.ontology_changes[].description` 과 `findings[].vendor_claim`([가정] 27) 이다. 같은 절이 "스키마가 허용하지 않으면 넣지 않는다"고 정했으므로 실행은 막히지 않지만, 원문 미열람 표시는 스키마의 `source_unopened`(finding·출처 단위)로 내야 한다. **요청(agents 담당)**: `researcher.md` 11.8·6절·점검표(449·452행)의 "`vendor_claim` 은 넣지 않는다"를 "벤더 기능·성능 주장은 `vendor_claim: true` + 태그 `추정` (+ `evidence_excerpt` 첫머리 '벤더 주장: ')"로, `verifier.md` 항목 13 을 "`vendor_claim: true` 또는 '벤더 주장: ' 표시"로 고친다. `track.answers[]` 처럼 스토리텔러에게 유용한 필드는 사용자 결정 뒤 스키마·`examples/`·프롬프트를 함께 고친다.
- **요청(pipeline 담당, agent_runner·publish)**: (a) 스토리텔러 반환값은 `pages.schema.json` 의 `$defs/returned` 로 검사하고 불일치는 스키마 불일치로 처리한다([가정] 29). (b) 트랙 단계 번호(`track.stage`, `new_questions[].stage`, 백로그 id 의 단계 부분, `stage_page`, `backlog_updates[].stage`, `stage_transition.to_stage`)가 `config/tracks/<slug>.yaml` 의 `stages` 이하인지 검사한다([가정] 28). (c) 새 백로그 질문을 `data/tracks/<slug>/backlog.json` 에 저장할 때 `origin_run_id` 에 `pages.json` 의 `run_id` 를 기록한다([가정] 25). (d) 트랙 실행에서 `answered_question_ids` 가 비어 있으면 `self_check.limits` 의 "답한 질문 없음: <이유>" 를 일일 로그·트랙 로그에 남긴다(7.3 "부분 결과로 진행하되 로그에 표시").
- **백로그 `origin` 값 불일치(templates 담당과 결정 필요)**: 이 스키마의 `backlog_updates[].origin` 은 8.2 문구 그대로 `^(f[0-9]+|사용자)$` 이고 `data/tracks/manual-capability-ontology/backlog.json` 의 시드 항목도 `사용자` 를 쓴다. 그러나 `templates/README.md`(트랙 상태 값 항목)는 표시값 `시드 | <finding id> | 사용자 | 단계 n 에서 되돌아옴` 과 `backlog.json` 의 `origin` 값 `seed` 를 언급한다. 기본안: 저장값은 스키마·8.2 대로 두 가지(`f<n>`, `사용자`)만 두고, `시드` 는 `origin_run_id` 가 없는(구축 시 넣은) 항목, `단계 n 에서 되돌아옴` 은 `origin_run_id` 실행의 단계가 질문 `stage` 보다 큰 항목으로 퍼블리셔가 표시할 때만 만든다. templates 담당은 `seed` 저장값 언급을 이 규칙으로 고친다.
- `answered_question_ids` 가 0개인 트랙 브리프를 "부분 결과"(예산 도달·출처 부재)로 볼지 "필수 결과 미충족"(반려)으로 볼지는 검증 에이전트가 `self_check.limits`·`budget_used` 로 판단한다([가정] 23). `agents/verifier.md` 의 트랙 검사 항목에 이 판단 기준을 적기를 agents 담당에게 요청한다.
