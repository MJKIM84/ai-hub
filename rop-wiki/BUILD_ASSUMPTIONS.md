# 구축 [가정] 전체 목록

이 문서는 [구축 완료 보고서](BUILD_REPORT.md) 2절의 부록이다. 구축 중 사양서에 없어 구축자가 정한 사항을 담당 묶음별로 모두 옮겼다. 각 항목의 근거와 맥락은 해당 파일 안의 [가정] 표시에도 있다.
초기 작성 단계의 가정 가운데 이후 검토에서 바뀐 것은 항목 끝에 "이후 변경"으로 표시했다.


## 뼈대(파서·스캐폴드·시드 페이지·검사)

- auto 키 목록에 없는 `category-area-table` 키를 하나 추가했다. 대분류 페이지의 세부 연구영역 표는 '현재 상태' 열이 페이지 상태에 따라 바뀌어야 하므로 표 전체를 이 마커 안에 두고 refresh_all_auto_regions() 가 다시 그린다(원문 3열은 파서 값 그대로 출력하며 protect_source.py 가 글자 단위로 대조한다). 마커 밖 본문 불변 규약을 지키면서 상태 열을 최신으로 유지하기 위한 선택이다.
- 대분류 페이지는 4.3의 여섯 섹션을 그 순서대로 두고, 원문 주석에 [n] 인용이 있는 대분류(A~G 전부)에는 각주 정의만 담는 7번째 섹션 '참고 자료'를 끝에 덧붙였다. 각주 정의를 둘 자리가 4.3에 없어서다.
- 목록 페이지(docs/topics/index.md, docs/glossary/index.md, docs/references/index.md, docs/logs/index.md)는 지정된 type(topic/glossary/reference/log)을 쓰되 프런트매터에 `subtype: index` 를 넣고, check_frontmatter 는 subtype: index 인 페이지에 type 별 추가 필수 필드(primary_area_no, term_ko, ref_id 등)를 요구하지 않는다.
- 참고문헌 10건의 URL 은 실행 환경의 프록시가 모든 외부 CONNECT 를 403 으로 거부해 열어 보지 못했다. 그래서 ref 페이지 status 는 seed 로 두고(검증 에이전트가 실재를 확인하면 올린다), 접근일 2026-09-24 는 '기록일'이며 원문 미열람 상태다. 유형·신뢰도는 지시받은 표(표준·논문·정부연구기관·오픈소스 문서 high, 기사 medium)를 그대로 적용했다.
- 참고문헌 페이지 title 은 내비 가독성을 위해 `ref-00n — <원문 제목>` 형식으로 하고, 원문 제목만 담는 `ref_title` 필드를 프런트매터에 추가했다(references-index 렌더러가 이 필드를 쓴다).
- 내비게이션: 4.8에 없는 '정정 요청 안내'(docs/corrections.md)는 운영 지표 뒤에 둔다. 고정 라벨은 '홈', '소개', '중점 연구 트랙', '주제', '로그', '일일 로그', '주간 정리' 이고 나머지 라벨은 파일 프런트매터 title 이다. 트랙 섹션 라벨은 트랙 index.md 의 title 을 쓴다.
- 페이지 status: 홈·소개 4·횡단·색인 페이지는 내용이 확정된 정적 페이지이므로 published, 대분류 7페이지는 '다른 대분류와의 연결' 섹션이 비어 있으므로 seed, 세부영역 28페이지는 지시대로 seed.
- 홈 2번 항목의 SCOR 오케스트레이션과 로봇 오케스트레이션 범위 차이 설명(두 문장)과 what-is-rop.md 의 안내 문장은 원문 1장을 근거로 한 구축자의 해석이므로 [의견] 태그를 붙였다.
- [분류원문] 태그 규약: 문단·목록 항목은 마지막 줄 끝에 ' [분류원문]', 표는 표 아래 빈 줄 뒤에 '[분류원문]' 한 줄. 원문 각주 표기 [n] 은 그대로 두고 그 뒤에 '원문의 [n]은 참고문헌 ref-00n에 해당한다.[^ref-00n]' 문장으로 각주를 연결한다.
- 트랙 진행 현황 렌더러(track-progress)는 config/tracks/<slug>.yaml 의 current_stage 로 단계 상태(완료/진행 중/대기)와 완료 조건 충족 여부를 유도하되, 선택 필드 stage_status({단계: 문자열})·stage_completion({단계: bool}) 이 있으면 그 값을 우선한다. 단계 이름은 stage-N-*.md 의 title 을 쓴다.
- ontology-version-history 는 data/tracks/<slug>/ontology_versions.json ({"items":[{version,date,changes,run_id}]}) 이 있을 때만 렌더링하고, standards-table 은 data/standards.json ({"items":[{name,org,kind,related_areas,ref_id,url}]}) 또는 docs/standards/*.md 프런트매터(type standard, org, kind, related_areas, ref_id, url)로 렌더링한다. 둘 다 없으면 해당 영역은 건드리지 않는다(다른 담당 소유).
- 홈과 idea-mapping.md 의 트랙 개요 링크는 사양서 0장 tracks 설정값(manual-capability-ontology)의 고정 경로 docs/tracks/manual-capability-ontology/index.md 로 두었다. about/agents.md, about/reading-guide.md, about/how-to-contribute.md 링크도 사양서 경로 그대로다. 해당 파일이 생기면 자동으로 해소된다.
- check_links.py 는 깨진 링크·정의 없는 각주 참조·절대 경로 링크·디렉터리 링크를 오류(exit 1)로, 참조 없는 각주 정의는 경고로 취급한다. check_frontmatter.py 는 본문 첫 줄이 '홈' 또는 '[홈](…' 으로 시작하는지(이동 경로 규약)도 오류로 검사한다.
- 오늘 날짜는 환경변수 ROP_TODAY 가 있으면 그 값, 없으면 date.today() 다(재현 가능한 빌드용). 실행 환경의 시스템 날짜는 2026-09-24 로 일치했다.
- 운영 지표의 검증 통과율 = summary.json 의 verdict_second 가 '통과'인 실행(2차가 없으면 verdict_first 가 승인·조건부 승인) / 전체 실행. 반려 = verdict_first '반려', 보류 = parked:true 건수와 runs/parked/ 항목 수 중 큰 값. 오래된 영역은 세부영역 페이지 updated 기준 경과일 상위 5.
- run_type 값 'track' 을 트랙 실행 식별에 쓰며, track-recent-runs 는 summary.json 의 target.slug(또는 target.track) 가 트랙 slug 와 같은 실행만 보여 준다.
- 변경 이력 항목의 page 가 디렉터리('docs/')이거나 존재하지 않는 페이지면 링크 없이 경로 텍스트만 보여 깨진 링크를 만들지 않는다.

## 템플릿

- 섹션 제목(H2)은 5.4 목록의 번호를 포함한 문구로 고정하고, 괄호 안 설명(예: '(물류 흐름의 어느 단계인지 명시)', '(자동)', '(각주)')과 '표'라는 낱말은 제목에서 뺐다. 예: '## 5. 현장 시나리오', '## 5. 단계 진행 현황', '## 2. 개념 목록'. 세부영역 1·2절의 [분류원문] 태그는 제목이 아니라 본문 문장 끝에 붙인다. 정본 목록은 templates/README.md '섹션 제목 정본'에 있다.
- 대분류 페이지에는 4.3의 여섯 섹션 뒤에 번호 없는 '참고 자료' 절을 추가해 원문 주석의 [n]에 대응하는 각주 정의를 둔다.
- 세부영역 시드의 '원문 주석'(EPCIS 언급, 지도 버전 관리, 8·22 구분, 27 교차 적용)은 1절 '한 줄 정의' 아래 '**원문 주석:**' 단락에 [분류원문]으로 둔다.
- 분류 원문 문단을 옮길 때 원문의 [1]~[10] 번호 표기는 그대로 두고, [분류원문] 태그 뒤에 대응 각주 [^ref-00n]을 덧붙일 수 있게 했다. 원문 보호 검사는 태그와 그 뒤 각주를 떼고 대조해야 한다.
- 홈 템플릿은 원문 정의 문장·범위 문장·대분류 표(링크와 세부영역 4개 이름·링크 추가)를 _source/에서 프로그램으로 추출해 내장했고, 표 끝에 [분류원문]을 둔다(4.1이 링크·이름 추가를 허용하므로 표 문구는 원문 그대로).
- 소개(about) 템플릿은 7페이지의 본문 구성이 서로 다르므로 공통 뼈대(요약 → 본문 절(제목 자유) → 관련 페이지 → 참고 자료)만 고정하고, 페이지별 필수 내용(4.2)은 주석 표로 수록했다.
- 페이지 상단에 읽기 가이드용 상태 줄('> 상태: … · 신뢰도: … · 갱신일: …')을 두었다(mkdocs 가 프런트매터를 표시하지 않으므로). 이 줄과 대분류 3절의 '현재 상태' 열은 auto 마커 밖이며 스토리텔러가 갱신할 때 맞춘다(퍼블리셔 자동 갱신 key 없음).
- 참고문헌(reference) 페이지는 5.1 공통 필드에 더해 프런트매터에 ref_id, org, published, url, source_type, reliability, accessed 를 둔다(4.7 필드를 스크립트가 읽을 수 있게). 본문에는 '각주 정본'과 '비고' 절을 추가했다.
- 온톨로지 초안 페이지는 페이지 version(정수)과 별개로 프런트매터 ontology_version(문자열 '0.2', pages.json 의 track_updates.ontology_draft_version 과 동일 값)을 둔다. 개념 상태 값은 시드 | 제안 | 확정 | 폐기 로 정했다.
- 일일 로그와 트랙 로그는 퍼블리셔가 페이지 전체를 렌더링하므로 auto 마커를 두지 않았다. 일일 로그는 날짜별 한 페이지에 '## 실행 <실행 id>' 블록을 실행마다 최신순으로 반복하고, 트랙 로그는 '## 실행 기록' 아래 '### 실행 <실행 id> — 단계 <번호>. <이름>' 블록을 반복한다. 트랙 로그 본문은 스토리텔러의 track_updates.log_entry 와 verification/research 의 track 블록에서 퍼블리셔가 채운다.
- 분량 기준의 측정 범위: 세부영역은 3~11절 텍스트(공백 포함, 표 구분 기호·각주 정의·프런트매터 제외) 4,000자 이내, 주제는 1~7절 텍스트 합계 1,500~2,500자. 트랙 단계 페이지는 6,000자를 넘으면 질문 단위로 주제 페이지로 분리.
- 트랙 단계 2절 질문 표의 상태 값은 5.4대로 '답함 | 열림 | 보류' 세 가지만 쓰고, 백로그의 '조사 중'은 '열림'으로, '폐기'는 표에서 빼고 백로그에만 남긴다.
- 각주 정의는 '[^ref-NNN]: 기관, 제목, 발행일, URL, 접근일' 다섯 필드만 쓰고, 원문 미열람은 접근일 뒤에 ' (원문 미열람)', 발행일 미상은 '발행일 미확인'으로 표기한다. **(이후 변경: 발행일 미상 표기는 이후 '미확인'으로 통일했다.)**
- 완성 페이지에서는 안내 주석(HTML 주석, 프런트매터 # 주석)을 모두 지우고 auto 마커 주석만 남긴다. 템플릿 자체는 {{…}} 때문에 유효한 YAML/페이지가 아니므로 검사 스크립트가 페이지로 취급하지 않아야 한다.
- 주간 정리(logs/weekly)와 트랙 보조 페이지(비교표·매트릭스·평가 절차·백로그·실험), 횡단 색인 페이지는 12종 목록 밖이므로 템플릿을 만들지 않았고 README 에 해당 담당이 만들 것으로 적었다.

## 스키마

- run_type enum 에 track 추가(공통 규약). run_type == track 이면 research.json 의 track 블록 필수, 그 외 실행에서 track 블록이 있으면 불합격(양방향 강제). 부록 B.1 예시는 7번 영역 대상과 track 블록을 한 JSON 에 함께 보여 주지만 필드 설명용 합성 예시로 보고 examples/ 를 일반 실행(research.json)과 트랙 실행(research.track.json)으로 나눔.
- target.area_no/area_name/category 는 weekly_review·monthly_recheck 에서만 null 허용(특정 영역이 없는 실행). area_deep_dive/topic/update/track 은 정수·문자열 필수(if/then).
- target.area_name 은 _source 원문 28개 세부영역 명칭('7. 화물·재고·자산 식별과 추적' 형식) enum, target.category 는 7개 대분류 명칭('B. 공통 정보·환경 모델') enum. 스크립트로 원문에서 추출해 넣었다.
- findings[].tag 는 지시대로 사실|추정|의견 만. [가설]·[사용자 실험]은 페이지 본문 태그로 보고 finding 태그에 넣지 않음. experiments/ 결과를 finding 으로 담을 때의 tag·sources[].type 값은 미정(남은 문제로 보고).
- findings[].tag == 사실 이면 source_ids 최소 1개(5.3 출처 없는 수치·사례 금지).
- findings[].source_unopened(지시) 외에 sources[].source_unopened 와 pages.json reference_updates[].source_unopened 도 선택 boolean 으로 추가(실행 규약 '모든 출처 항목에 원문 미열람 표시'의 구조화).
- findings[].as_of 와 sources[].published 는 YYYY / YYYY-MM / YYYY-MM-DD 허용, published 는 확인 불가 시 null 허용. findings[].evidence_excerpt 는 500자 상한.
- track.ontology_changes[] 에 선택 필드 description(변경 내용 설명) 추가. track.new_questions[].id 를 비우면 스토리텔러가 q<단계>-<두자리> 부여, 퍼블리셔가 유일성 검사.
- verification: category_fit.reassign_to 는 세부영역 번호(1~28) 또는 null. quotation_check 에 선택 issues[] 추가. verdict 가 반려·불통과면 retry_reason 문자열 필수, 조건부 승인·수정 후 재검증이면 required_fixes 1개 이상. track_checks.stage_transition_approved true 면 stage_complete true 필수.
- pages[].content 선택 필드는 '---\n' 프런트매터로 시작해야 함. pages 는 1개 이상. changelog_entry 는 'YYYY-MM-DD | <대상 이름> | <요약> | run <run_id>' 형식을 정규식으로 강제.
- glossary_updates / reference_updates / open_question_updates 는 부록 B.3 예시가 빈 배열이라 4.7 표 필드와 data/open_questions.json 형식으로 항목 형식을 구성. open_question_updates 는 action new|update 로 구분하고 update 면 id 필수. flow_matrix_updates[].title, index_updates.area_recent, glossary_updates[].action/slug/description/related_areas/sources, reference_updates[].cited_by 는 선택.
- standards_updates(지시)에 선택 ref_id 추가 — pipeline/lib/render.py render_standards_table() 이 data/standards.json 항목의 ref_id 를 읽기 때문. track_updates.stage_transition(지시) 추가. track_updates.backlog_updates[] 에 새 질문 등록용 question/stage/origin(finding id 또는 '사용자') 선택 필드 추가.
- area_reflection_proposals[].section 은 세부영역 페이지 13개 절 중 분류원문 1·2절과 자동 12절을 뺀 10개 절 제목 enum(templates/README.md 섹션 제목 정본 기준).
- answer_link 는 docs/….md#앵커 허용(한글 앵커 포함, 앵커는 공백 아닌 문자열). $id 는 https://rop-wiki.invalid/schemas/<파일명> 이며 스키마 간 $ref 없이 각 파일 자기완결.
- 예시 날짜·run_id 는 오늘 날짜 규칙에 따라 2026-09-24 / 2026-09-24-01(일반) / 2026-09-24-02(트랙)로 채움(부록 B 예시의 2026-09-25 대신).

## 공통 규칙·리서치 에이전트

- run_type 값 track 을 사양서 6.1의 '트랙 실행'에 대응하는 값으로 둔다(공통 컨텍스트의 [가정]을 그대로 적용, 부록 B.1 enum 에 추가 필요).
- WebFetch 호출은 검색 횟수(max_search_queries)에 세지 않고, 신규 출처 1건당 1~2회를 기준으로만 연다(사양서는 WebFetch 예산을 정하지 않음).
- 트랙 실행에서 단계 페이지·온톨로지 초안·비교표 등 트랙 페이지의 갱신 제안은 page_updates(하루 2) 상한과 별도로 센다.
- 실행 컨텍스트에 retry_no, next_ref_id, schema_extensions(true/false) 키가 올 수 있다고 정의했다. next_ref_id 가 없으면 입력 참고문헌 목록의 최대 번호+1 부터 신규 출처 id 를 부여한다.
- 요약본 입력은 '### <경로> (요약)' 소제목으로 오고, 반려 재실행 시 이전 브리프가 '### runs/<run_id>/research.json' 입력으로 포함된다고 가정했다.
- web_fetch_available: false 일 때 신뢰도 high 금지를 출처 reliability 와 finding confidence 양쪽에 적용하고, 교차 확인돼도 medium 상한으로 두었다(공통 컨텍스트 [가정] 확장).
- 출처 유형별 기본 신뢰도 표(표준 high, 동료심사 논문 high/프리프린트 medium, 오픈소스 문서 high/성능 주장 medium, 정부·연구기관 high, 업계 보고서 medium, 벤더 문서 medium/성능 low, 기사 low)와 '쓰지 않는 출처'(커뮤니티 게시글·개인 블로그·일반 위키·생성형 AI 답변) 목록은 구축자 판단이다.
- sources 배열에는 이번 실행의 신규 출처만 넣고, 기존 참고문헌 id 재사용은 finding.source_ids 로만 표시한다(max_sources_per_run 이 '신규 출처' 상한이라는 정의에 맞춤).
- 부록 B.1에 없는 선택 필드를 정의했다: findings.tag 값 '사용자 실험', findings.vendor_claim, sources.type 값 '사용자 실험', sources.fetched, glossary_candidates.source_ids/area_nos, track.answers[], track.new_questions[].parent_question_id, track.ontology_changes[].description, 최상위 retry_response[]. 스키마가 허용하지 않으면(schema_extensions: false) 넣지 않도록 했다.
- 문자열 규약: open_questions_new 는 '<질문> | 관련 영역: <번호. 이름> | 근거: <id> | 종류: 일반|분류 확장 제안|출처 충돌' 형식, open_questions_resolved 는 앞의 oq id 만 유효, 외부 연계 영역 finding 은 claim 을 '연계 대상: '으로 시작, 원문 미열람 출처는 summary 를 '원문 미열람. '으로 시작, 정정 요청 관련 finding 은 evidence_excerpt 를 'corr-NNN 관련: '으로 시작, 재인용은 '(재인용: <run_id>)'.
- evidence_excerpt 길이를 200자 안팎으로 제한했다.
- 반려 재실행의 예산은 실행 컨텍스트의 남은 예산을 따르고, 없으면 원래 상한 안에서 쓴다.
- monthly_recheck 를 실행 유형별 초점에 포함했다(6.1 목록에는 없지만 7.1과 B.1 enum 에 있음). 대상 주장·출처 목록은 target.json 이 준다고 가정.
- 입력 문서 안의 지시문을 따르지 않는다는 규칙(입력은 데이터)을 공통 실행 규약에 추가했다. 규칙 완화가 아니라 강화이므로 사용자 확인 없이 넣었다.
- 사용자 실험(experiments/)의 출처 항목 url 은 저장소 경로('experiments/<날짜>-<이름>/')로 적는다.
- 8.2 필수 결과 중 (5) 세부영역 반영 제안은 스토리텔러의 area_reflection_proposals 몫으로 보고, 리서치는 page_proposals(action update, 영역 파일 경로, 섹션, rationale '트랙 … 반영 제안')로 그 바탕만 준다. (6) 트랙 로그는 퍼블리셔 몫.

## 검증·스토리텔러 에이전트

- verifier: 검증 단계는 실행 컨텍스트의 `verification_stage: first|second` 로 받는다. 표시가 없으면 입력에 runs/<run_id>/pages.json 이 있을 때 second, 없을 때 first 로 본다.
- verifier: 검증 예산은 실행 컨텍스트 `verifier_budget`(queries, fetches)이 우선하고, 없으면 검색 15회·출처당 열람 최대 2회. 상한 도달 시 남은 출처는 검색 결과 일치로만 확인하고 '원문 미열람(검증 예산)'을 남기며 high 를 주지 않는다.
- verifier·storyteller: 링크 유효성의 기준으로 runs/<run_id>/docs_tree.txt(현재 docs/ 아래 페이지 경로 목록)를 입력으로 받는다. 없으면 경로 규약 부록과 입력 페이지로만 검사하고 한계를 verification_note 에 적는다.
- verifier: 6.2의 '반려' 정의를 운영 기준 6가지로 구체화했다(실재하지 않는 출처에 중심 주장이 기댐 / 태그 처분 후 실행 유형별 최소 요건 미달 / category_fit.ok false / 원문 SCM 질문 미포함·미조사 / 브리프 전반의 범위 위반 / 대상·run_id 불일치·브리프 없음).
- verifier: confidence 확정 규칙 — high = 핵심 주장이 모두 [사실] 유지·교차 확인·원문 열람, medium = 단일 출처·벤더/기사 중심·원문 미열람 혼재, low = 핵심 주장 절반 이상이 추정·의견 또는 강등. web_fetch_available: false 면 medium 상한.
- verifier: [사용자 실험]을 [사실]로 승격하려면 실험 결과와 독립된 공개 출처 1개 이상이 필요하다([가설]은 독립 출처 2개).
- verifier: 분류 원문 5번 정의에서 온 온톨로지 v0 시드 개념(로봇, 제조사, 기능, 제약, 장착 장비, 실행 조건, 작업 요구, 근거 문서)의 제거는 승인하지 않는다.
- verifier: 단계 완료 조건 판정은 1차 검증에서 예비 판정(기존 페이지 + 이번 브리프), 2차 검증에서 실제 페이지로 최종 확정하며, 퍼블리셔는 verification2.json(2차)의 track_checks 를 따른다.
- verifier: 8.2 '막힌 질문'의 운영 기준 — 현재 단계 백로그 질문 중 (1) 열림·조사 중, (2) 보류인데 보류 사유·재개 조건이 없음, (3) 사용자 지정 또는 앞 단계로 되돌아온 질문 중 미답. 보류 사유·재개 조건이 있는 보류 질문과 폐기 질문은 전환을 막지 않는다. 뒤 단계에서 되돌아온 질문이 남은 앞 단계는 '재개' 상태이며 그동안 현재 단계 전환도 미승인.
- verifier: 2차 판정 구분 — '수정 후 재검증'은 국소 수정(이전 초안 유지), '불통과'는 초안을 버리고 다시 쓰기. 둘 다 max_retries 에 센다.
- verifier·storyteller: 문체 검사의 '짧은 단락' 기준은 한 단락 5문장 이하. 분량은 공백 포함이며 프런트매터·HTML 주석·표 구분 기호·각주 정의·mermaid 코드 제외(템플릿 기준과 동일). 주제 페이지 본문은 1~7절.
- verifier: weekly_review 에서 브리프가 깨졌다고 보고한 링크·출처는 최대 5건을 다시 열어 확인한다.
- storyteller: research.json 또는 verification.json 이 없으면 대상 페이지를 변경 없이(action: update, diff_summary '변경 없음') 반환하고 additional_research_requests 에 사유를 적는다(pages 는 1개 이상이어야 하므로).
- storyteller: deprecated 페이지는 상태 줄 아래 `> 대체 페이지: [제목](경로)` 줄을 둔다.
- storyteller: 이동 경로의 주제 색인은 docs/topics/index.md, 로그 색인은 docs/logs/index.md 로 링크한다.
- storyteller: 대분류 페이지 5. 다른 대분류와의 연결은 그 대분류의 마지막 세부영역 심화 실행에서, 또는 브리프 page_proposals 가 제안할 때만 하루 갱신 상한 안에서 채운다.
- storyteller: 주제 페이지 slug 는 영문 소문자·하이픈 3~6 단어.
- storyteller: 주제 페이지 9. 검증 노트의 판정은 '1차 <verdict> / 2차 대기'로 쓰고, 퍼블리셔가 게시 시 '2차 통과'로 바꾼다(게시되는 페이지는 2차 통과뿐이므로 안전).
- storyteller: 주간 정리 페이지(docs/logs/weekly/YYYY-Www.md, type: log, tags: [weekly_review])의 절 7개를 고정했다 — 1. 이번 주 다룬 영역 / 2. 새로 확인된 사실 / 3. 강등·폐기된 주장 / 4. 열린 질문 변동 / 5. 링크·출처 유효성 점검 / 6. 용어집 정리 / 7. 다음 주 후보.
- storyteller: 하루 예산(신규 주제 1, 갱신 2)은 세부영역·주제·대분류 페이지에만 적용하고 트랙 페이지와 주간 정리 페이지는 세지 않는다.
- storyteller: 온톨로지 초안은 승인된 변경이 있을 때 ontology_version 을 0.1 올리고, 7. 버전 이력은 auto 마커 안이므로 직접 쓰지 않고 행 내용(버전/날짜/변경 내용/근거 실행 id)을 track_updates.log_entry 의 '온톨로지 변경:' 항목에 넣어 퍼블리셔가 추가한다(공통 컨텍스트의 '버전 이력 표에 행 추가'와 auto 마커 규약을 이렇게 조화시켰다).
- storyteller: 단계 3(추출 방법 비교표·파이프라인 후보안)과 단계 6(수명주기 절차 초안)은 전용 페이지가 없으므로 단계 페이지 3. 조사 결과 안에 표·소제목으로 쓴다.
- storyteller: 단계 전환이 승인돼도 다음 단계 페이지는 이 실행에서 고치지 않고 다음 트랙 실행이 다룬다.
- storyteller: 템플릿이 없는 트랙 보조 페이지(비교표·매트릭스·평가 절차·실험)의 절 제목을 정했다. 기존 페이지를 갱신할 때는 기존 절 제목·순서가 우선한다.
- storyteller: 새 페이지의 auto 마커 사이는 공통 컨텍스트 규약대로 비워 둔다(템플릿의 '퍼블리셔가 자동으로 채운다.' 안내 문구는 두지 않음). 퍼블리셔가 마커 사이를 다시 쓰므로 어느 쪽이든 결과는 같다.
- 공통 컨텍스트에서 이미 표시된 것을 그대로 따름: run_type 에 track 추가, web_fetch_available: false 처리(검색 결과 일치·원문 미열람 표시·high 금지).

## 소개 페이지(에이전트·읽기 가이드·기여)

- docs/about/agents.md 역할 표의 내용 검증 에이전트 입력(1차: 브리프와 출처 URL·기존 페이지·용어집·참고문헌·정정 요청, 2차: pages/·pages.json·원 브리프·1차 수정 목록)은 사양서 6.2에 명시가 없어 검증 항목 11개에서 역산한 것이다.
- web_fetch_available: false 환경의 처리(출처 실재성을 검색 결과로 확인, 모든 출처에 '원문 미열람', 신뢰도 high 금지·medium 상한)는 공통 컨텍스트의 [가정]을 그대로 옮긴 것이다(agents.md, reading-guide.md).
- run_type 값 track 은 사양서 부록 B 예시에 없고 공통 컨텍스트에서 추가한 값이다(agents.md 실행 유형 표).
- config/priority.yaml 의 track_questions[].priority 허용 값을 high | normal | low 로 예시했다(how-to-contribute.md). config 담당의 실제 정의와 맞춰야 한다.
- 정정 요청이 거부되면 퍼블리셔가 inbox/corrections.md 의 상태를 rejected 로 바꾸고 사유를 '처리 메모'에 적으며, 처리 시 '처리 실행'·'처리 메모' 두 줄을 블록 끝에 덧붙인다. 사양서는 applied 갱신만 명시한다(corrections.md, how-to-contribute.md).
- 정정 요청이 걸린 페이지는 대상 선정 단계에서 needs_update 로 표시된다(corrections.md 처리 흐름 2단계). 표시 주체·시점은 사양서에 없다.
- 보류 산출물 재투입은 runs/parked/<id>/ 를 runs/<id>/ 로 되돌린 뒤 pipeline/run_daily.sh --resume <id> 를 실행하고, 폐기는 runs/parked/<id>/DISCARDED 파일(날짜·사유 한 줄)을 만드는 방식으로 안내했다(how-to-contribute.md). 공통 컨텍스트가 지정한 [가정]이며 pipeline 담당의 실제 CLI 와 맞춰야 한다.
- 같은 영역 3회 연속 보류로 대상 선정에서 제외된 영역을 다시 포함시키는 방법은 config/priority.yaml 의 areas 에 지정하는 것으로 안내했다(how-to-contribute.md).
- 에이전트 규칙 변경을 변경 이력에 남길 때 data/changelog.json 에 항목을 추가하는 것으로 안내했고, 버전 줄 형식은 기존 agents/shared-rules.md 의 'version: 1.0 (2026-09-24)' 형식을 따라 'version: 1.1 (YYYY-MM-DD)' 로 예시했다(how-to-contribute.md).
- experiments/ 반영 시 리서치 에이전트는 README.md 전체와 텍스트 데이터 파일(csv, json, md, txt)을 읽고 이진·대용량 파일은 읽지 못할 수 있다고 안내했으며, finding 태그 '사용자 실험'·출처는 저장소 경로라는 agents/researcher.md 의 [가정]을 그대로 따랐다(experiments/README.md).
- 소개 페이지의 이동 경로는 템플릿의 '홈 › 소개 › 제목'이 아니라 이미 만들어진 소개 4페이지와 같은 '[홈](../index.md) › 제목' 형식을 따랐다. 소개 절에는 index 페이지가 없어 '소개'에 링크를 걸 수 없기 때문이다. docs/corrections.md 는 '[홈](index.md) › 정정 요청 안내'.
- inbox/corrections.md 의 항목 형식은 '## corr-NNN' 제목 + 여섯 개의 '- 필드: 값' 한 줄 목록(페이지, 문제 문장, 근거, 요청일, 요청자, 상태)으로 정했다. 사양서는 필드만 정하고 서식(표 또는 블록)은 정하지 않았다.
- docs/corrections.md 의 type 은 지시대로 about 으로 두었다(프런트매터 type 허용 값에 정정 안내 전용 값이 없음).
- 벤더 주장 병기 형식은 templates/ontology-draft.md 의 '[추정] 벤더 주장' 을 문장 형식 '… [추정] 벤더 주장[^ref-nnn]' 으로 확장해 예시했다(reading-guide.md, corrections.md). 사양서는 '병기'만 요구하고 형식은 정하지 않았다.

## 용어집·표준 시드

- WES/WCS/WMS/MES/TMS 다섯 약어는 시드 목록이 한 항목으로 묶여 있어 한 페이지(docs/glossary/wes-wcs-wms-mes-tms.md)에서 약어마다 행을 나누어 풀어 설명했다. 약어별 페이지가 필요해지면 분리한다.
- 용어집 시드 13개의 status 는 draft, confidence 는 medium 으로 두었다(WES/WCS/WMS/MES/TMS 페이지만 low). 5.2 의 seed 는 '본문 없음'이라 맞지 않고, 내용 검증 에이전트를 거치기 전이므로 draft 가 적절하다고 판단했다. docs/standards/index.md 는 백본의 glossary/index.md 와 같은 기준으로 published.
- WebFetch 가 네트워크 정책으로 차단되어(ref.gs1.org 로 확인) 새 출처는 모두 WebSearch 결과의 기관·제목·URL 일치로만 실재를 확인했다. 각주에 '(원문 미열람)'을 붙이고 어떤 페이지에도 confidence high 를 주지 않았다. ref-001~ref-010 각주 정의는 docs/references/ref-00n.md 의 '각주 정본' 문자열을 그대로 복사했으므로 '(원문 미열람)' 표기가 없다(백본 담당의 정본을 따름).
- 참고문헌 후보(ref-011 부터 순서대로 부여, docs/references/ 에 파일은 만들지 않고 각 용어 페이지 각주에만 정의): ref-011 Gerkey & Matarić, A Formal Analysis and Taxonomy of Task Allocation in Multi-Robot Systems (IJRR 23(9)), 2004, https://journals.sagepub.com/doi/10.1177/0278364904045564 / ref-012 Stern et al., Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks (SoCS 2019), 2019, https://arxiv.org/abs/1906.08291 / ref-013 ISO, ISO 23247-1:2021 Digital twin framework for manufacturing — Part 1, 2021-10, https://www.iso.org/standard/75066.html / ref-014 ISA, ISA95 Enterprise-Control System Integration 위원회 소개, https://www.isa.org/standards-and-publications/isa-standards/isa-standards-committees/isa95 / ref-015 ISA, ISA-95 Standard: Enterprise-Control System Integration, https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard / ref-016 ASCM, A Guide To Warehouse Management & Management Systems, https://www.ascm.org/topics/warehouse-management-wms-explained/ / ref-017 MHI, What is WCS? (MHI Blog), https://www.mhi.org/blog/126051/what-is-wcs / ref-018 MHI, Warehouse Execution Software Implementation (MHI Blog), https://www.mhi.org/blog/66378/warehouse-execution-software-implementation / ref-019 OMG, About the DDS Security Specification Version 1.2, https://www.omg.org/spec/DDS-SECURITY/1.2/About-DDS-SECURITY / ref-020 Open Robotics, Mobile Robot Fleet Integration — Programming Multiple Robots with ROS 2, https://osrf.github.io/ros2multirobotbook/integration_fleets.html / ref-021 ISO/IEC, ISO/IEC 19987:2024 EPC Information Services (EPCIS), 2024, https://www.iso.org/standard/85557.html / ref-022 ASCM, ASCM's SCOR model — Processes: Introduction, https://scor.ascm.org/processes/introduction / ref-023 TTA, TTA정보통신용어사전 — 디지털 트윈, https://terms.tta.or.kr/dictionary/dictionaryView.do?word_seq=191771-1. 모두 접근일 2026-09-24, 원문 미열람. 등록은 다음 실행에서 검증을 거쳐 이뤄진다.
- 표준·프레임워크 목록의 '종류' 배정: SCOR=프레임워크(규범 표준이 아닌 프로세스 참조 모델), ISA-95=표준, GS1 EPCIS=표준, Open-RMF=오픈소스, ROS 2 DDS-Security=오픈소스(ROS 2 설계 문서; 바탕이 되는 OMG DDS-Security 는 표준), ROS 2 위협 모델=프레임워크, NIST 협업 로봇 성능=평가 프로그램, ARIAC=평가 프로그램. 페이지 안내 문단에 [가정]으로 명시했고 검증 에이전트가 바꿀 수 있다.
- 각 항목의 관련 세부영역은 분류 원문의 인용 위치와 항목 성격으로 배정했다: SCOR 1·2·4 / ISA-95 1·2·28 / EPCIS 7·2·17 / Open-RMF 9·10·15·13 / 플릿 어댑터 9·5·12·21 / WES/WCS/WMS/MES/TMS 1·2·10 / MRTA 13·5·14·16 / MAPF 15·6·16 / Lifelong MAPF 15·14·13 / MAPD 13·15·14 / ARIAC 23·22·20 / DDS-Security 26·11·28 / 디지털 트윈 22·8·23 / ROS 2 위협 모델 26·25·28 / NIST 협업 로봇 성능 17·18·23. 세부영역 페이지 7절이 채워지면 조정한다.
- Open-RMF 의 RMF 를 'Robotics Middleware Framework' 로 풀어 썼고, 통용되는 한글 명칭이 없어 term_ko 를 '오픈 RMF' 로 두었다. 이 약어 풀이는 별도 검색으로 확인하지 않았다.
- MES 가 ISA-95 3계층(제조 운영 관리)에 대응한다는 설명과 TMS 의 정의는 발행 기관·협회 자료로 확인하지 못해 [추정]·'미확인' 으로 남겼다(CSCMP 용어집 검색 결과에 TMS 정의가 잡히지 않음). 플릿 어댑터의 중간 범주(Traffic Light), EPCIS 2.0 비준일(2022-06), SCOR DS 판본·발행일, DDS Security 1.2 판 발행일도 [추정] 또는 미확인이다.
- 용어 페이지 본문 분량은 템플릿의 '300~800자 기준' 을 넘긴다(본문 약 2,500~4,500자). 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈의 구분, 출처 미열람 표시, ROP 맥락 설명을 담기 위해 늘렸으며 필요하면 축약할 수 있다.
- wes-wcs-wms-mes-tms.md 의 ROP 경계 요약 문장 하나는 외부 각주 대신 '[사실] (근거: 분류 원문 9장)' 으로 표기하고 about/scope-boundary.md 를 링크했다. 위키 내부 원문이 근거인 경우의 표기 방식은 정해진 규칙이 없어 이렇게 두었다.
- 트랙 페이지(docs/tracks/manual-capability-ontology/*)는 다른 담당이 동시에 만드는 중이라 링크 검사 실패를 피하기 위해 fleet-adapter.md 에서 트랙 이름만 언급하고 링크는 넣지 않았다.
- docs/standards/index.md 의 시드 표 열은 과업 지시(이름/종류/발행 기관/관련 세부영역/한 줄 설명/출처)를 따랐다. 퍼블리셔 render_standards_table 의 열 구성(이름/기관/종류/관련 영역/참고문헌/URL)과 다르므로 interface_notes 에 조정 요청을 남겼다.

## 트랙 개요·백로그·로그·온톨로지 초안

- config yaml: 추가 필드 stage_names/stage_pages 는 단계 번호(정수) 키의 매핑으로 두었고, stage_names 는 "단계 n." 접두 없이 8.1 제목의 이름 부분만 담았다(표시 시 번호+이름으로 조합). render.py 가 읽는 선택 키 stage_status/stage_completion 은 활성 키로 넣지 않고 주석으로만 안내했다.
- index.md: 8.2 운영 규칙 요약을 "8. 참고 자료" 뒤에 부록 성격의 "운영 규칙(8.2 요약)" 절로 두었다(트랙 개요 8개 섹션 제목·순서 고정 규칙 유지). 8.1 트랙 출처 규칙과 검색어 후보도 이 절에 넣었다.
- index.md: 연구 목표와 단계의 대응(목표 1: 단계 1~3, 목표 2: 단계 4·6·7, 목표 3: 단계 5)은 구축자 판단이며 [가정] 표기했다.
- index.md: status seed, 참고 자료는 분류 원문 4장의 Open-RMF 문장을 [분류원문] 인용하면서 붙인 ref-004 하나만 두었다(근거 없는 각주 추가 안 함). 5절에는 auto 마커 앞에 단계별 밝힐 것·완료 조건 정적 표를 두었고, 그 안의 문장은 8.1 트랙 정의를 번호+이름 규칙에 맞춰 옮겼다.
- ontology-draft.md: 온톨로지 버전은 프런트매터 ontology_version "0"(문자열), 페이지 version 은 1(정수)로 분리했다(templates/README 규약). 페이지 상태 seed, confidence 없음.
- ontology-draft.md: 번호만 표기 금지 규칙에 따라 근거 출처를 "부록 A 5번 정의" 대신 "부록 A 5. 로봇 능력·작업 온톨로지 정의"로 썼고, 버전 이력 v0 행의 변경 내용도 "부록 A 5. 로봇 능력·작업 온톨로지 정의 기반 시드(개념 8개·관계 6개)"로 썼다(태스크의 문구 "부록 A 5번 정의 기반 시드"를 같은 뜻으로 풀어 씀).
- ontology-draft.md: 개념 "근거 문서"와 관계 "모든 개념은 근거 문서를 가리킨다"는 부록 A 5번 정의에 없으므로 근거 출처를 "트랙 정의 8.1의 온톨로지 초안 v0과 트랙 출처 규칙 — [가정]"으로 표기했다. 관계의 카디널리티는 정하지 않고 미해결 질문으로 남겼다. 범위 밖(분류 원문 9장 로봇 자체 지능·제어 경계) 서술은 [가정] 표기했다.
- ontology-draft.md: 미해결 모델링 질문 5개는 구축자 [가정]이며 시드 백로그 id(q1-03, q1-05, q1-06, q2-05, q3-04, q4-03, q4-04, q6-02)에 연결만 했고 새 백로그 항목으로 추가하지 않았다. 다이어그램에서 "모든 개념은 근거 문서를 가리킨다"는 개념 subgraph→근거 문서 점선 하나로 표현했다.
- backlog.json: origin 값은 태스크 지시대로 영문 "seed"(8.2의 "제기 근거" 값 중 시드 표기). 질문 문장은 8.1 원문 그대로라 q4-03·q4-04·q7-01 에 "(13번)", "(8번)", "(21번)" 같은 번호만 표기가 남아 있다(원문 보존 우선, 위키 본문에서 다룰 때 이름 병기). **(이후 변경: origin 값은 이후 사양서 8.2대로 '사용자'로 바꿨다.)**
- question-backlog.md·log.md·experiments.md 의 status 는 published(운영 페이지). 제목은 각각 "질문 백로그", "트랙 로그 — 매뉴얼 기반 로봇 기능 온톨로지", "실험"(템플릿·사양서 4.6 명칭).
- log.md: 항목은 시간순(오래된 것이 위)으로 쌓이고 새 항목은 파일 끝의 <!-- append-below --> 마커 뒤에 덧붙인다 — templates/track-log.md 의 "최신순" 안내와 다르며 태스크 지시(마커를 끝에)를 따랐다. 시드 항목의 실행 id 는 build-2026-09-24, 일일 로그 링크는 없음. 이 페이지에는 사실 태그를 붙이지 않는다.
- question-backlog.md: track_questions 의 처리 규칙(다른 단계 지정 시 그 단계 태그로 진입, id 는 단계의 다음 번호, 중복이면 기존 질문 우선순위만 상승)과 priority 값(high|normal|low)은 docs/about/how-to-contribute.md 의 [가정]과 맞췄다.
- experiments.md: 실험 계획 제안 형식(계획 번호 E<단계>-<두 자리>, 상태 값 제안됨/수행 중/결과 반영됨/철회)과 "단계 3·5·7 외에서도 제안할 수 있으나 필수는 아님"은 구축자 정의다.

## 트랙 단계 페이지·산출물 틀

- 단계 페이지 2절 질문 표는 태스크의 5열(id/질문/상태/답한 실행/답 링크) 대신 templates/track-stage.md 의 6열(id / 질문 / 상태 / 제기 근거 / 답한 실행 id / 답 위치)을 따랐다. 시드의 제기 근거 값은 "시드", 답한 실행 id·답 위치는 빈 칸이다.
- 6절 완료 조건 표는 템플릿의 4열(완료 조건 / 충족 여부 / 근거 / 검증 판정)을 따르고 검증 판정은 "없음(구축 시점, 판정 전)"으로 두었다. 복수 항목인 완료 조건(단계 1·2·5·7)은 행을 나눴고, 특히 단계 5의 "평가 지표 정의와 검증 절차 초안"을 "평가 지표 정의"와 "검증 절차 초안" 두 행으로 나눴다. 표 아래에 "다음 단계로 전환: 아니오(…)" 한 줄을 두었다.
- 9절 이력 표는 태스크의 3열(날짜/실행 id/변경) 대신 템플릿의 6열(날짜 / 실행 id / 답한 질문 / 새 질문 / 온톨로지 변경 / 버전)을 썼고, 시드 행의 실행 id 는 트랙 로그와 같은 "구축(build-2026-09-24)" 이다.
- H1 아래 상태 줄의 단계 상태는 config/tracks/manual-capability-ontology.yaml 의 current_stage: 1 에 따라 단계 1 만 "진행 중", 단계 2~7 은 "대기" 로 두었다.
- 7절 관련 세부영역은 태스크가 지정한 연결(단계 1~3: 5·27, 단계 4: 9·12, 단계 5: 23, 단계 6: 24·27·28, 단계 7: 21·13·25·9)을 먼저 두고, 트랙 개요(index.md)가 그 단계에 배정했거나 시작 질문이 직접 언급한 영역을 별도 소제목으로 덧붙였다: 단계 1에 9·28, 단계 2에 21, 단계 4에 8·13, 단계 4~7에 트랙 중심 영역 5. 프런트매터 related_areas 는 7절 목록과 같다.
- 1절 "밝힐 것"은 8.1 문장을 인용 블록(>)으로 한 글자도 바꾸지 않고 옮겼다. 단계 4·5·6 원문에 있는 "부록 A 9·12번" 같은 번호 표기는 원문 유지를 위해 그대로 두고, 바로 다음 문장에서 번호와 이름을 함께 쓴 링크로 풀었다.
- 단계 7 시나리오 표의 열은 항목 / 내용 / 온톨로지가 바꾸는가 / 근거(단계·실행 id) 로, 표마다 "관련 세부영역 · 물류 흐름 단계: 미정" 줄을 두었다. 가설 판정표 열은 가설 / 내용 / 판정 / 근거(단계·실행 id) 이며 가설 문장은 index.md 3절과 동일하게 [가설] 태그를 붙였다. 3절 끝에 "사용자에게 제안하는 실험 계획" 소제목(아직 없음)을 두었다.
- 단계 3(추출 방법 비교표, 파이프라인 후보안)과 단계 6(온톨로지 수명주기 절차 초안)의 완료 조건 산출물은 고정 페이지가 없으므로 해당 단계 페이지 3절에 두고, 분량이 커지면 track 프런트매터를 가진 주제 페이지로 분리해 링크한다고 적었다.
- 모델·표준 비교표: 열 순서를 후보 / 제시한 질문 / 발행 기관 / 종류 / 전제조건 / 파라미터 범위 / 적재·환경 제약 / 완료 확인 방법 / 오류의 의미 / 실행 인터페이스 연결 / 출처 / 상태 로 정했고("제시한 질문" 열은 구축자 추가), 3절에 각 열의 뜻과 값 집합(상태: 미조사 / 조사 중 / 확인 / 원문 미열람 / 제외(이유))을 정의했다. 행은 지우지 않고 제외는 상태로 표시하며, 후보 밖 모델·표준은 근거 finding id 와 함께 행 추가를 허용했다. 후보 행 이름은 8.1 질문의 괄호 안 표기를 그대로 썼다.
- 문서 유형 매트릭스: 8개 정보 항목의 뜻과 온톨로지 초안 v0 개념·비교표 열과의 대응표, 칸 값 체계(미조사 / 있음(형태) / 부분 / 없음), 공개 문서 샘플 목록 표의 열 뜻을 구축자가 정했다. 태스크에 없는 5절 "문서에 없는 정보"(q2-04 자리)를 추가했다.
- 평가 지표와 검증 절차: 지표 표에 "취지(구축자 해석)" 열을 두고 정의·필요한 자료·상태는 "미정"으로 두었다. 태스크에 없는 4절 "오류 유형과 비용·탐지"(q5-02 자리, 모든 칸 미조사), 5절 절차 초안에 들어가야 할 항목 목록, 6절 측정 결과 표 형식(대상 문서·기종 / 지표 / 값 / 측정 조건 / 근거 / 태그 / 검증 판정), 지표 정의가 바뀌면 기존 측정값에 정의 버전을 남기는 규칙을 추가했다.
- 산출물 3페이지(비교표·매트릭스·평가 절차)와 단계 페이지 7개에는 auto 마커를 두지 않았다(공통 key 목록에 해당 키가 없음). 상단 상태 줄의 숫자는 스토리텔러가 갱신 시 표와 맞춘다.
- 산출물 3페이지 프런트매터에는 stage 필드를 넣지 않았다(5.1: stage 는 트랙 단계 페이지만). 산출 단계는 본문 상단 상태 줄에 링크로 표기했다. type: track + subtype(comparison | matrix | evaluation), track, related_areas, tags, status: seed, sources: [], version: 1 을 넣었다.
- 프런트매터 tags 값과 7절의 "어느 절에 반영을 제안하는지" 문구는 구축자가 정한 것이며 조사 결과가 아니다.

## 설정

- settings.repo_root: ".." — 위키(rop-wiki/)가 ai-hub git 저장소의 하위 폴더라는 전제. git_commit/git_push 는 이 경로에서 실행한다.
- settings.web_fetch_probe_url 이 열리지 않아도 실행을 멈추지 않고 실행 컨텍스트에 web_fetch_available: false 를 표시해 진행한다. 웹 검색(WebSearch)까지 못 쓰면 web_tools_required 에 따라 중단한다.
- settings.max_turns·agent_timeout_sec 초과는 7.3 의 스키마 불일치와 같이 처리한다(해당 에이전트 1회 재실행 후 보류).
- rotation.precedence — 규칙이 겹칠 때의 순서: track_day → monthly_recheck → weekly_review → priority → cycle1 → cycle2.
- rotation.scoring.recent_penalty: 5 (감점 크기). 한 번만 빼고 누적하지 않는다. 트랙 실행은 세부영역 페이지를 갱신하지 않으므로 최근 감점 대상에 세지 않는다.
- rotation.scoring 항의 해석: open_questions = data/open_questions.json 에서 상태 열림·조사 중이고 관련 영역에 포함된 수 / empty_matrix_cells = data/flow_matrix.json 42칸 중 그 영역 링크가 없는 칸 수 / priority_weight = areas[].weight + topics[].weight(같은 area_no) + questions 수 × 3.
- rotation.track_days: [Tue, Fri] (요일). track_runs_per_week 가 7 이면 track_days 를 무시하고 매일 트랙 실행. track_days 가 부족하면 있는 요일만 쓰고 경고.
- rotation.track_runs_per_week: null 이면 settings.yaml 의 track_runs_per_week 를 따른다(문자열 "settings" 대신 null 로 표현).
- rotation.weekly_review_every 의 실행 번호는 runs/ 의 실행 폴더 수(runs/parked 포함)로 센다. 주간 정리·월간 재검증이 트랙 실행일과 겹치면 다음 비트랙 실행으로 미루고, 둘이 같은 날이면 월간 재검증을 먼저 한다(deferred_periodic_runs).
- rotation.track_rotation: alternate — 활성 트랙이 여럿이면 settings.tracks 순서로 번갈아, 직전 트랙 실행의 다음 트랙부터.
- rotation.priority.* — 우선 항목이 여럿이면 weight 큰 것·같으면 파일 순서; areas 항목의 run_type 은 페이지가 seed 면 area_deep_dive 아니면 topic, topics 는 항상 topic; 최근 7일 안에 다룬 우선 항목은 건너뜀(skip_if_targeted_within_days: 7); questions 는 대상을 직접 바꾸지 않고 해당 영역 가중치에 항목당 3(question_weight).
- rotation.cycle2.include_update_for_corrections: true — 정정 요청이 걸린 페이지의 갱신은 대상 선정을 바꾸지 않고 당일 작업에 더하며 daily_budget.page_updates 안에서 처리.
- 보류 3회로 제외된 영역은 priority.yaml 의 areas 에 다시 지정하면 제외가 풀린다(docs/about/how-to-contribute.md 의 서술과 일치시킴).
- priority.yaml 의 track_questions[].priority 값은 high | normal | low (how-to-contribute.md 의 [가정]과 동일).
- priority.yaml 의 area_no 범위(1~28)·stage 범위 위반 항목은 select_target 이 무시하고 로그에 남긴다.
- config/README.md 는 docs/ 밖의 저장소 문서이므로 5.1 프런트매터와 이동 경로(breadcrumb)를 넣지 않았다.

## 파이프라인 스크립트

- run_type 값 track 을 7.2/6.1 의 '트랙 실행'에 대응하는 값으로 쓴다(공통 규약).
- claude -p --json-schema 는 CLI(Ajv strict)·API 제약 때문에 원본 스키마를 그대로 받지 못한다(실험으로 확인: $schema URL 거부, strictTypes 로 type 없는 하위 스키마 거부, 최상위 allOf/oneOf/anyOf 거부). 따라서 lib/runs.py cli_schema() 가 $schema·$id·$defs 제거, type 보충, 최상위 조건 규칙 제거를 한 사본을 CLI 에 넘기고, 조건 규칙(if/then)은 스크립트가 원본 스키마로 jsonschema 검증해 그대로 강제한다.
- 페이지 열람 점검은 settings.web_fetch_probe_url 에 curl HEAD(403/405 면 GET) 로 하고, 이 환경에서는 프록시 403 으로 web_fetch_available: false 다. web_fetch_required: false(기본) 면 계속 진행하고 실행 컨텍스트에 표시한다. 웹 검색 점검은 claude -p 로 WebSearch 1회를 실제 호출해 구조화 출력의 searched 값으로 판단한다(usage.server_tool_use 는 0 으로 나와 신뢰하지 않음). **(이후 변경: 기본값은 이후 사양서대로 web_fetch_required: true(중단)로 바꿨고, 열람이 막힌 환경만 override 로 진행한다.)**
- 스토리텔러 산출 pages/ 는 runs/<run_id>/pages/<docs 기준 상대 경로>(예 pages/categories/b-…/07-….md, pages/tracks/<slug>/index.md) 구조로 푼다. 같은 이름(index.md) 충돌을 피하기 위해서다.
- 2차 검증 판정 파일 이름은 verification2.json/.md 다(agents 파일이 요청한 이름과 같음). 재실행 시 직전 판정·산출물은 verification.attemptN.json, research.attemptN.json, verification2.attemptN.json, pages.attemptN.json 으로 남기고, 실행 컨텍스트에 retry_count·max_retries 를 넣는다. 재실행에서 예산은 남은 예산이 아니라 원래 상한을 그대로 준다.
- 실행 컨텍스트에 역할별 추가 항목을 넣는다: verifier 는 verification_stage(first|second)·verifier_budget, researcher 는 next_ref_id(docs/references 의 최대 번호+1), 모두 언어(language)·환경 알림. 리서치 재실행 절 제목은 '## 반려 사유', 스토리텔러는 '## 수정 지시', 스키마 불일치 재실행은 '## 스키마 불일치 (재실행)'.
- 관련 영역 페이지 요약은 같은 대분류의 다른 세부영역 + 대상 페이지 프런트매터 related_areas(트랙이면 트랙 정의 related_areas)의 1·2절(원문 정의·질문)과 상태 줄이다. 주간 정리 입력은 같은 ISO 주의 실행 산출물(research.md·verification.md·verification2.md·pages.json·log.md)+data/changelog.json, 월간 재검증 입력은 참고문헌·표준·용어집 색인 + 마지막 갱신이 오래된 게시 페이지 상위 5개다. experiments/ 는 README.md 와 텍스트 파일(md/txt/csv/json/yaml)만 파일당 6만 자·전체 20만 자 상한으로 넣는다.
- 스토리텔러 템플릿 입력은 실행 유형별로 고정한다: area_deep_dive→area.md·category.md, topic→topic.md, update→area.md·topic.md, monthly_recheck→area.md·topic.md·reference.md, track→track-stage.md·ontology-draft.md·track-overview.md·topic.md, weekly_review→없음.
- 대상 선정의 규칙 우선순위는 config/rotation.yaml 의 precedence(track_day→monthly_recheck→weekly_review→priority→cycle1→cycle2)를 그대로 따른다. 월간 재검증은 '이전 실행이 있고, 이달의 이전 실행에 monthly_recheck 가 없으며, 이달의 이전 실행이 모두 트랙 실행(또는 없음)'일 때, 주간 정리는 '실행 번호가 7의 배수이거나 마지막 7의 배수 번호 이후 weekly_review 가 없을 때(미뤄진 경우)' 실행한다. 실행 번호는 runs/ 와 runs/parked/ 의 실행 id 수로 센다.
- 트랙 질문 선택: target.json 의 question_ids 는 priority.track_questions(문장 일치 또는 id 일치, priority high→normal→low)→앞 단계로 되돌아온 열린 질문(stage<current, 오래된 순)→현재 단계 열린 질문(오래된 순) 순으로 최대 3개다. 백로그에 아직 없는 사용자 질문은 target.json track.user_questions 에 문장으로 넣고, 퍼블리셔가 트랙 실행마다 priority.track_questions 를 제기 근거 '사용자'로 backlog.json 에 등록한다. 뒤 단계의 사용자 질문은 그 단계가 될 때 다룬다.
- 3회 연속 보류 판정은 그 영역을 대상으로 한 비트랙 실행(실행 id 순)의 끝에서 이어진 보류 횟수로 센다. 제외 영역에는 data/open_questions.json 에 '사용자 검토 요청: <영역 이름> …' 열린 질문을 한 번만 등록하며, priority.yaml areas 지정으로 제외가 풀린다. 우선 지정(topics·questions)이 제외 영역을 가리키면 무시한다.
- 정정 요청은 실행 유형이 rotation.corrections.applies_to 에 있을 때 target.json corrections 에 붙이고, 서로 다른 페이지 수가 daily_budget.page_updates 를 넘으면 다음 실행으로 넘긴다. update 실행 유형은 CLI --run-type 으로만 선택된다(정정 요청은 그날 실행 유형에 덧붙는다). 반영 확인(corrections_applied)된 요청만 inbox/corrections.md 의 상태를 applied 로 바꾸고 처리 실행·처리 메모 줄을 덧붙인다. rejected 판정은 스키마에 필드가 없어 자동으로 쓰지 않는다.
- 퍼블리셔 4~5단계는 pages/ 를 docs 에 복사하기 전에 docs/·data/·config/tracks/·mkdocs.yml·inbox/corrections.md 를 runs/<run_id>/backup/ 에 스냅숏하고 실패 시 그 스냅숏(+추적 파일은 git checkout)으로 되돌린다. 4단계 protect_source.py 는 --skip-nav 로 돌리고(새 페이지로 mkdocs.yml 이 낡기 때문), 6단계 반영·내비 재생성 뒤 protect_source(내비 포함)·check_links·check_frontmatter 를 다시 돌려 최종 관문으로 삼는다. 위키가 아직 git 에 추적되지 않아 git checkout 롤백은 첫 커밋 뒤부터 의미가 있다.
- 페이지 확정 규칙: status 는 published(needs_update·deprecated 는 유지), updated·last_run 은 실행 날짜, version 은 초안 값이 기존보다 크지 않으면 기존+1, 신뢰도 필드가 있는 페이지는 2차 검증 confidence 로 덮어쓴다. 주제 페이지 9. 검증 노트의 '2차 대기'는 2차 판정으로, '검증자 주의' 줄은 2차 verification_note 로 치환한다(storyteller.md·verifier.md 의 요청).
- 용어집 항목은 templates/glossary.md 절 구성으로 퍼블리셔가 생성한다. slug 는 지정값 또는 term_en 의 슬러그. 한 줄 정의는 sources 가 있으면 [사실]+각주, 없으면 [추정]과 출처 미기재 표시. 참고문헌은 reference_updates 의 id 로 docs/references/<id>.md 를 만들되 같은 id 가 다른 URL 로 이미 있으면 퍼블리셔가 실패한다(자동 재번호 없음). 표준은 data/standards.json 에 누적하고 render.py 의 standards-table 영역이 렌더링한다.
- 변경 이력에는 페이지마다 한 행(생성/갱신/폐기, diff_summary)과 changelog_entry 의 대상·요약을 담은 '요약' 행 하나, 용어집·참고문헌·표준·백로그·정정 요청의 부수 갱신 행을 넣는다.
- 트랙 로그 페이지는 auto:track-log 영역이 render.py 에 등록되어 있지 않으므로 퍼블리셔가 직접 영역 맨 앞에 새 항목(8항목 표)을 끼워 넣고 data/tracks/<slug>/log.json 에도 같은 항목을 추가한다. '<!-- append-below -->' 마커가 있으면 그 뒤에 넣는다. 온톨로지 버전은 pages.json ontology_draft_version 과 ontology-draft.md 프런트매터 ontology_version 이 다르면 실패이고, 이전 버전과 달라졌을 때만 data/tracks/<slug>/ontology_versions.json 에 이력 행을 추가한다(변경 내용은 log_entry 의 '온톨로지 변경:' 부분). 새 백로그 질문에는 origin_run_id 를 기록한다.
- 단계 전환은 2차 검증 track_checks.stage_transition_approved(없으면 1차) 가 true 이고 pages.json track_updates.stage_transition 이 있을 때만 config/tracks/<slug>.yaml 의 current_stage 값을 정규식으로 바꾸고(주석 보존), to_stage 가 stages 를 넘으면 status: done 으로, 파일 끝의 '퍼블리셔 기록' 마커 블록에 stage_status·stage_completion 을 기록한다.
- 커밋 메시지의 대상 이름은 세부영역 원문 명칭이며 트랙 실행은 뒤에 '(트랙 이름 단계 n)', 주간 정리는 '주간 정리 YYYY-Www' 를 쓴다. git add 는 docs·data·config·mkdocs.yml·inbox·runs/<run_id> 만 한다. git identity 가 없으면 임시 identity 로 커밋한다. 커밋 실패는 롤백하지 않고 실패로 기록한다. 9단계에서 확정 일일 로그·summary·자동 영역을 다시 쓴 뒤 사이트를 재빌드하고 커밋을 --amend 한다.
- 보류·중단된 실행도 publish.py --log-only 로 일일 로그·summary.json 을 남긴다(빌드·커밋은 설정대로 시도하되 실패해도 중단하지 않음). 퍼블리셔 검사 실패는 보류(parked)가 아니라 runs/ 에 남긴 채 '중단(퍼블리셔: …)' 으로 기록해 --resume --step publish 로 재시도한다. --resume 은 runs/parked/<id>/ 를 자동으로 runs/<id>/ 로 되돌린다.
- 예산 초과 판단은 research.json self_check.budget_used 를 target.json budget 과 비교해 로그와 일일 로그 '예산 사용량' 표에 초과/도달 로 표시한다. 일일 로그의 신규 주제 페이지·기존 페이지 갱신 사용량은 pages.json 에서 세되 트랙·로그 페이지는 갱신 상한에 넣지 않는다.
- 알림(notify ≠ none)은 로그에 자리만 남기고 발송은 구현하지 않았다.
- cron.example 의 CRON_TZ 는 cronie 계열 전제이며, 이 컨테이너에는 crontab 명령이 없어 install/uninstall_cron.sh 는 --dry-run 과 문법 검사만 확인했다.

## README

- cron 환경의 Claude 인증 방식(`claude setup-token` 장기 토큰 또는 환경변수 `ANTHROPIC_API_KEY`를 crontab 환경에 두는 것)은 사양서에 없어 사용자 결정 항목으로 두었다. `claude auth login`·`claude auth status`·`claude setup-token` 서브커맨드는 설치된 CLI(2.1.281)의 `--help`로 실재를 확인했고, 어느 방식을 쓸지만 [가정]이다.
- 에이전트 파일 버전 규칙(규칙 추가·삭제는 major, 문구·서식은 minor)과 변경 이력 항목의 `run_id: manual-<날짜>`는 pipeline/RUN.md 8.1절의 [가정]을 그대로 따랐다.
- 사람이 직접 커밋할 때의 메시지 형식 `<유형>(rop-wiki): <요약>`은 사양서에 없고 기존 커밋 이력(`docs(rop-wiki): …`, `wip(rop-wiki): …`)에서 가져온 것이다.
- `runs/cron.log`는 커밋하지 않는 것으로 안내했다. 퍼블리셔(`publish.py` `_git_paths`)가 `runs/<run_id>/`만 스테이지하므로 코드상 커밋되지 않는 것은 사실이며, 그것을 권장 운영으로 적은 부분이 [가정]이다.
- 페이지 열람 차단 시 '원문 미열람' 모드로 진행하는 기본값(`web_fetch_required: false`)은 config/README.md·settings.yaml의 사용자 결정 항목이며, README는 그 기본값을 설명하고 `true`로 바꾸면 사양서 원문대로 중단된다고 적었다. **(이후 변경: 기본값은 이후 web_fetch_required: true 로 바꿨다.)**

## 검토 뒤 수정(템플릿·에이전트)

- open_questions_new 항목의 종류(분류 확장 제안·출처 충돌)는 open_question_updates.question 앞에 표시로 붙이고, 근거 필드는 JSON 으로 옮기지 않는다.
- 부분 답은 백로그 `조사 중`, 단계 페이지 표 `열림`, `### q… (부분 답)` 소제목으로 나타낸다.
- 트랙 개요 페이지는 트랙 실행마다 갱신하며 하루 갱신 상한에 세지 않는다.
- 주간 정리에서 URL 상태만 기록하는 발견 사항은 새 조사로 보지 않는다.
- 온톨로지 초안 제목은 트랙 정의에서 가져오는 자리표시자({{ontology_title}})로 둔다.
- 참고문헌 템플릿에 url_verified 필드와 '원문 열람' 행을 더했다.
- 질문–발견 사항 대응 규약(rationale 문자열 형식)은 스키마 필드가 아니라 문자열 규약이다.

## 검토 뒤 수정(파이프라인)

- 실행마다 실행 커밋과 커밋 해시 기록 커밋 두 개를 만든다(커밋은 자기 해시를 담을 수 없다). 퍼블리셔 8단계를 7단계 커밋 전에 실행한다.
- '최근 다룬 영역'은 게시되고 보류되지 않은 실행만 센다.
- 제외가 해제된 영역은 7일 건너뜀 규칙을 적용하지 않는다.
- 세부영역 반영 제안은 그 영역 페이지가 pages.json 에 있을 때, 이전 실행의 제안만 '반영'으로 표시한다.
- 페이지 열람 차단 override 는 --allow-no-fetch, ROP_ALLOW_NO_FETCH=1, web_fetch_required: false 세 가지다.
- 폐기(DISCARDED) 표시한 보류 실행도 연속 보류 횟수에는 센다.
- 퍼블리셔는 등록되지 않은 자동 영역 키를 실패로 본다.
- 세부영역·주제·트랙 단계·온톨로지 초안 페이지에는 신뢰도 필드를 항상 쓴다.

## 통합·드라이런 중 결정

- 사이트 제목 앵커를 유니코드 slugify(pymdownx.slugs, 소문자)로 바꿨다. 기본 slugify 는 한글을 버려 스토리텔러가 쓰는 한글 앵커 링크가 엄격 빌드에서 깨졌다. 트랙 답 소제목은 {#q1-01} 명시 id 로 짧은 앵커를 고정한다.
- 일일 로그와 자동 영역에 옮기는 에이전트 텍스트의 각주 참조 표기는 인라인 코드로 바꾼다.
- 반영되지 않은 실행의 일일 로그는 새 페이지를 링크하지 않고 경로 글자와 '미반영'으로 적는다.
- 용어집 시드 13개에 신뢰도(출처가 있으면 medium, 없으면 low)를 넣었다. 원문을 열지 못해 medium 이 상한이다.
- 에이전트 프롬프트 변경 이력의 실행 id 는 manual-<날짜> 로 적는다.
- 헤드리스 에이전트 모델을 claude-opus-5-5 로 고정했다(세션 모델 변경에 맞춤).
- 사용자가 '그냥 진행해'라고 했으므로 멈춤 지점 1·2에서 멈추지 않고, 그 확인 자료를 이 보고서에 실었다.
- 이 환경은 페이지 열람(WebFetch)이 네트워크 정책으로 막혀 있어 두 드라이런을 --allow-no-fetch 로 실행했다.

## 운영 전환(2026-09-25~)에서 추가된 [가정]

결정 전체는 [DECISIONS.md](DECISIONS.md) 에 있다. 아래는 그 가운데 사람이 검토할 만한 것으로 표시한 항목이다.

- (D-006, 1-1 원문 열람) 열람 모드를 full / mirror_only / none 셋으로 나누고, mirror_only(일반 페이지 차단·GitHub 원문만 열림)는 override 없이 진행한다 — 이유: 페이지 열람 도구 자체는 동작하므로 "도구 없음"이 아니다. 출처별 fetched 표시와 코드 상한으로 품질을 지킨다 [가정]
- (D-010, 1-3 분량) 세부영역 3~11절이 기준(4,000자)을 넘으면 5·9절을 뺀 큰 절부터 주제 페이지로 코드가 옮기고, 원 절에는 스토리텔러가 outline 에 적은 요약과 링크를 남긴다. 400자 이하 절은 옮기지 않는다 — 이유: 줄이지 않고 나눈다는 요청. 5절은 흐름 매트릭스 앵커의 기준, 9절은 ROP 직접 범위 판단이라 원 페이지에 둔다 [가정]
- (D-011, 1-3 분리 페이지) 자동 분리로 생긴 주제 페이지는 주제 템플릿 10개 절을 코드가 채우고(본문은 옮긴 절 그대로), 하루 신규 주제 상한(new_topic_pages)에 세지 않는다 — 이유: 새 주장이 없는 분리이므로 예산의 취지(새 조사량 제한)와 다르다 [가정]
- (D-016, 2-4 트랙 비중) track_runs_per_week 를 2 → 3 으로 올리고, 트랙 사이 배분은 track_weights(기본 모두 1)로 가중 순환한다. 트랙 요일은 화·목·토 — 이유: 트랙이 1개에서 3개가 되어, 트랙마다 주 1회를 기본으로 했다. 일반 순환(4회)과 정기 실행 몫을 남긴다 [가정]
- (D-018, 3부 세부영역) 시드 세부영역 27개는 "주제 조사"가 아니라 영역 심화(area_deep_dive)로 채운다 — 이유: 비어 있는 3~11절을 채우는 실행 유형이 영역 심화다(사양서 7.1 1주기). 요청의 목적(본문 게시)과 같다 [가정]
- (D-020, 3부 순서) 3부 1(새 트랙)·2(시드 세부영역)·4(첫 트랙 백로그)는 서로 입력이 겹치지 않아 한 배치에서 동시에 돌리고(트랙마다 직렬), 3(대분류 연결)은 2가 끝난 뒤, 5(주간·월간)와 6(용어집·참고문헌·전체 검사)은 마지막에 차례로 돌린다 — 이유: "순서대로"의 목적은 앞 단계 결과를 뒤 단계가 쓰는 것이며, 의존이 없는 단계를 직렬로 두면 수십 시간이 걸린다 [가정]
- (D-021, 1-7 사용자 입력) 실험 결과 반영 검증(V3)은 작업 트리 사본(git worktree)에서 커밋 없이 돌리고 증거만 runs/validation/ 으로 옮긴다. 정정 요청 검증(V2)은 본 위키에서 돌려 반영 1건은 그대로 두고, 입력함(inbox/corrections.md)만 원상 복구한다 — 이유: 예시 실험 결과는 가짜 데이터라 위키에 남기면 안 되고, 본 위키에서 되돌리면 동시에 게시되는 다른 실행과 섞인다. 정정 반영 1건은 실제로 맞는 수정이라 남긴다 [가정]
- (D-033, 3부 배치) 리서치 에이전트를 부를 때 실행마다 참고문헌 id 구간(30개)을 잠금 아래 예약해 주고(runs/.cache/ref_id_blocks.json), 퍼블리셔의 id 재배정은 다른 실행이 예약한 구간 위로만 옮긴다. 쓰지 않은 번호는 빈 번호로 남긴다 — 이유: 병렬 실행이 같은 '다음 id'를 받아 게시 직전에 번호가 바뀌고 그 사이 다른 실행이 먼저 게시하자, 2차 검증이 본문의 id 를 다른 출처와 대조해 재작성을 반복하다 트랙 1 첫 실행(2026-09-25-06)이 보류됐다. 번호 연속성보다 id 안정성이 중요하다 [가정]
- (D-034, 1-5 비용) 리서치·1차 검증 입력의 '최근 실행 research.md'(6.1)를 대상이 같은 실행(같은 세부영역·트랙·대분류) 최대 7회 + 그 밖의 최근 실행 2회로 좁혔다 — 이유: 배치로 여러 영역을 동시에 돌리면 최근 7회가 모두 다른 대상이라 입력만 약 5만 자 늘고 중복 방지에 쓸모가 적다. 다른 대상의 최근 2회는 교차 중복 확인용으로 남긴다 [가정]
- (D-036, 3부 1 새 트랙) 트랙 2·3 의 남은 실행은 자동 질문 선택 대신 시작 질문(제기 근거 '사용자')을 단계 순서대로 하나씩 지정해 돌린다(--stage N --question-ids qN-xx). 트랙마다 실행 수는 시작 질문 수(18)와 같다. 단계 전환은 지금처럼 검증 에이전트가 승인할 때만 기록된다 — 이유: 요청은 '백로그 질문 수만큼 주제 조사를 돌려 본문과 초안 문서를 만든다'이다. 자동 선택은 매 실행 새로 생기는 같은 단계 후속 질문을 먼저 골라, 첫 세 실행 만에 단계 1 질문이 4개에서 6~8개로 늘었고 18회를 돌아도 단계 2~5 페이지가 비게 된다. 후속 질문은 백로그에 남아 이후 정규 실행이 다룬다 [가정]
- (D-043, 3부 4 첫 트랙) 트랙 1 백로그 q1-09(ECLASS·IEC CDD 의 이동로봇 능력 항목)를 '보류'로 바꾸고(사유: 이 환경에서 원문 열람 불가, 재개 조건: 원문을 inbox/sources 로 제공), 트랙 1 의 마지막 실행은 단계 2 질문 q2-01~q2-03 을 지정해 돌렸다 — 이유: 자동 선택이 단계 1 의 유일한 열린 질문 q1-09 를 네 번 연달아 골랐고 매번 '조사 중'으로 남았다. 보류는 사유·재개 조건과 함께 기록해 검증 규칙(막힌 질문 판정)과도 맞춘다 [가정]
- (D-316, 트랙·아이디어: 가설) 새 트랙마다 [가설] 3개(미판정, 단계 5에서 판정)를 아이디어 정의에서 도출했다 — 이유: 트랙 개요 템플릿이 가설과 판정 상태를 요구한다. 도출이므로 [가정]을 병기
- (D-317, 트랙·아이디어: 초안 문서) 챗봇 task-model-draft.md "업무 분해·배정 설계 초안", 도면 space-graph-schema-draft.md "공간 그래프 스키마 초안". type 은 ontology-draft 를 그대로 쓰고 v0 개념·관계는 아이디어 정의 문구에서만 도출(모두 "아이디어 정의 기반 [가정]") — 이유: 퍼블리셔·검사·에이전트가 트랙 초안을 같은 유형으로 다룬다. 요청 문구 밖의 개념은 근거 finding 없이 넣지 않는다
- (D-327, 트랙·아이디어: 아이디어 페이지 1절) 정의 문구 원문 인용 + 가장 가까운 세부영역의 SCM 관점 질문([분류원문] 인용) + 현장 문제 한 단락([가정]) — 이유: 현장 문제를 원문 질문에 묶어 근거 없는 서술을 줄인다
