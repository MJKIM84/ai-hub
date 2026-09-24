# 페이지 템플릿 (templates/)

ROP 연구 위키의 페이지 템플릿 12종이다. 사양서 5.1(프런트매터)·5.2(상태·신뢰도)·5.3(사실·출처 표기)·5.4(섹션 구성)와 4.1·4.2·4.3·4.6·4.7의 페이지 정의를 파일로 옮긴 것이다. 각 템플릿은 스토리텔러 에이전트의 프롬프트에 그대로 들어가므로 자기완결적으로 쓰여 있다. 즉, 템플릿 하나만 읽어도 그 페이지를 쓰는 데 필요한 규칙(태그·각주·분량·시나리오 여섯 항목·번호+이름 표기·경로 규약)이 모두 들어 있다.

템플릿의 H2 문자열·표 형식·원문 인용 형식은 퍼블리셔 검사 스크립트(`pipeline/checks/protect_source.py`, `pipeline/checks/check_frontmatter.py`, `pipeline/checks/check_links.py`)와 시드 페이지(`docs/`)에 맞춘 것이다. 템플릿을 고칠 때는 아래 "검사 스크립트가 보는 것"과 함께 고친다.

## 템플릿 목록

| 파일 | type | 페이지 경로 | 섹션(고정 순서) | auto 마커 key | 갱신 주체 | 쓰임 |
|---|---|---|---|---|---|---|
| home.md | home | docs/index.md | 4.1의 11항목(제목·한 줄 설명 + 10개 절) | home-track-status, home-recent | 구축자 → 퍼블리셔(자동 영역) | 홈(소개). 원문 정의 문장·SCOR 문단·범위 문장·대분류 표(원문 3열 + 링크 2열)·다루지 않는 것 목록을 템플릿에 내장 |
| about.md | about | docs/about/{what-is-rop, scope-boundary, research-method, idea-mapping, agents, reading-guide, how-to-contribute}.md | 요약 → 본문 절(자유) → 관련 페이지 → 참고 자료 | 없음 | 구축자·사람 | 소개 하위 7페이지. 페이지별 필수 내용(4.2)을 주석 표로 수록 |
| category.md | category | docs/categories/<slug>/index.md | 핵심 질문 / 개요 / 세부 연구영역 / 이 대분류의 핵심 포인트 / 다른 대분류와의 연결 / 최근 업데이트 (+ 번호 없는 참고 자료 [가정]) | category-area-table [가정], category-recent | 구축자(원문 절) → 스토리텔러(다른 대분류와의 연결) → 퍼블리셔(세부 연구영역 표·최근 업데이트) | 대분류 7페이지. 절 제목에 번호를 붙이지 않는다 |
| area.md | area | docs/categories/<slug>/NN-<slug>.md | 5.4 세부 연구영역 13개 절(괄호 설명 포함) | area-recent | 구축자(시드) → 스토리텔러 → 퍼블리셔(12) | 세부 연구영역 28페이지. H1 아래 소속 대분류·핵심 질문은 시드와 같은 세 줄 admonition 블록(`!!! info "소속 대분류"` / 공백 4칸 + `[<대분류>](index.md) — 핵심 질문:` / 공백 4칸 + `<핵심 질문 원문> [분류원문]`) |
| topic.md | topic | docs/topics/YYYY/YYYY-MM-DD-<slug>.md | 5.4 주제 페이지 10개 절 | 없음 | 스토리텔러 | 일일 주제 페이지(2주기 이후), 트랙 주제 페이지(track 필드) |
| glossary.md | glossary | docs/glossary/<slug>.md | 용어 / 한 줄 정의 / 설명 / 관련 영역 / 출처 | 없음(색인은 glossary-index) | 구축자(시드) → 스토리텔러 제안 → 퍼블리셔 | 용어집 항목. 프런트매터 term_ko·term_en·definition 을 색인이 읽는다 [가정] |
| reference.md | reference | docs/references/ref-NNN.md | 서지 정보 / 요약 / 인용된 페이지 / 각주 형식 / 비고 | reference-cited-pages [가정] (색인은 references-index) | 구축자(시드 10건) → 리서치 제안 → 검증 확인 → 퍼블리셔(인용된 페이지) | 참고문헌 항목. 4.7 필드 전부를 프런트매터와 표에 둠 |
| daily-log.md | log | docs/logs/daily/YYYY-MM-DD.md | 실행 개요 / 단계별 결과와 소요 시간 / 검증 판정 / 생성·갱신 페이지 / 신규 출처 수 / 반려·보류 사유 / 예산 사용량 / 다음 실행 메모 | 없음(색인은 logs-index) | 퍼블리셔 | 일일 로그. 5.4의 11항목 전부 |
| track-overview.md | track | docs/tracks/<slug>/index.md | 5.4 트랙 개요 8개 절(5절은 `5. 단계 진행 현황 표`) | track-progress, track-recent-runs | 구축자 → 스토리텔러 → 퍼블리셔(5, 7) | 트랙 개요 |
| track-stage.md | track-stage | docs/tracks/<slug>/stage-N-<slug>.md | 5.4 트랙 단계 9개 절 | 없음 | 구축자(시드) → 스토리텔러 | 트랙 단계 7페이지 |
| ontology-draft.md | ontology-draft | docs/tracks/<slug>/ontology-draft.md | 5.4 온톨로지 초안 7개 절(2·3절은 `2. 개념 목록 표`·`3. 관계 목록 표`). title·H1·이동 경로의 산출물 이름은 자리 표시 `{{ontology_title}}`(첫 트랙 "능력 온톨로지 초안") | ontology-version-history | 구축자(v0) → 스토리텔러(검증 승인 변경만) → 퍼블리셔(7) | 살아있는 온톨로지 초안 |
| track-log.md | track-log | docs/tracks/<slug>/log.md | 머리말 / 항목 형식 [가정] / 실행 기록(auto 마커 안, 실행마다 8항목 표) | track-log [가정] | 구축자(머리말·항목 형식) → 퍼블리셔(실행 기록: `data/tracks/<slug>/log.json` 에서 최신순으로 렌더링) | 트랙 로그. 시드 docs/tracks/manual-capability-ontology/log.md 와 같은 구성 |

템플릿이 없는 페이지: 트랙 보조 페이지(model-standard-comparison, document-type-matrix, evaluation-and-verification, question-backlog, experiments — `type: track` + `subtype`), 횡단 페이지(용어집·참고문헌·표준·로그·주제 색인, open-questions, flow-matrix, changelog, metrics, corrections), 주간 정리(logs/weekly). 이들은 사양서 3장·4.6·4.7과 auto 마커 key(backlog, open-questions, flow-matrix, changelog, metrics, glossary-index, references-index, standards-table, topics-index, logs-index)를 따라 각 담당이 만든다.

## 템플릿의 구조

모든 템플릿은 같은 순서로 되어 있다.

1. **프런트매터** (파일 첫 줄부터). 5.1 형식. 값 자리는 `{{placeholder}}`, 줄 끝 `#` 주석이 값의 형식과 선택 여부를 설명한다. 모든 페이지에 `title, type, status, created, updated, version`이 있고, 유형별로 `category, area_no / primary_area_no, track, stage, related_areas, tags, confidence, sources, last_run`이 더 있다. 유형 전용 추가 필드(5.1에 없는 구축자 추가 필드는 [가정]): glossary 의 `term_ko, term_en, definition` [가정] (term_ko·definition 은 `pipeline/lib/frontmatter.py` TYPE_REQUIRED 의 필수 필드), reference 의 `ref_id, ref_title, org, published, url, source_type, reliability, accessed, url_verified` (`ref_title`·`url_verified` 는 시드·퍼블리셔가 쓰는 구축자 추가 필드 [가정]), ontology-draft 의 `ontology_version`.
2. **템플릿 안내 주석** (HTML 주석). 첫 블록에 페이지 유형·경로·쓰임·분량, `[공통 규칙]` 14항목(자리 표시 처리, 섹션 고정, auto 마커, 안내 주석 삭제, 문체, 번호+이름 표기, 사실 태그, 분류 원문 보호, 각주 형식과 ref id 대응, 상대 경로 링크, mermaid, 범위 경계, 27. AI·학습·적응과 모델 운영의 교차 규칙과 8. 실시간 세계 상태·데이터 일관성 대 22. 시뮬레이션·예측용 디지털 트윈의 구분, id·날짜 형식), `[경로 규약]`(대분류 7폴더·세부영역 28파일 표)이 들어 있다. about.md 의 공통 규칙 2항에는 소개 페이지의 예외(본문 절 제목 자유, 고정 절은 "관련 페이지"·"참고 자료")가 덧붙어 있다.
3. **이동 경로 줄** (`홈 › … › 현재 페이지`). 페이지 위치 기준 상대 링크. 홈은 "홈" 한 단어. 단계는 4.8 의 사이드바 구조(홈 → 소개 → 대분류 → 세부영역 → 중점 연구 트랙 → 주제 → 용어집 → 참고문헌 → …)를 따르되 시드와 같게 쓴다 [가정]: 세부영역 `[홈](../../index.md) › [<대분류>](index.md) › <세부영역>`, 대분류 `[홈](../../index.md) › <대분류>`, 소개 `[홈](../index.md) › <제목>`("소개" 단계 없음, 시드 7페이지와 같음), 주제·용어집·참고문헌·로그 `[홈](…) › [<색인 이름>](index.md 또는 ../index.md) › <제목>`, 트랙 개요 `[홈](../../index.md) › 중점 연구 트랙 › <트랙 이름>`, 트랙 하위 페이지(단계·온톨로지 초안·트랙 로그) `[홈](../../index.md) › 중점 연구 트랙 › [<트랙 이름>](index.md) › <페이지>`. "중점 연구 트랙"에는 링크가 없다(색인 페이지가 없다). 시드 가운데 `docs/tracks/manual-capability-ontology/{ontology-draft,log,question-backlog,experiments}.md` 는 "중점 연구 트랙" 단계가 없어 이 규칙·트랙 개요 시드·단계 시드 7페이지·`agents/storyteller.md` 4.2 의 새 페이지 형식과 다르다. 에이전트는 갱신 페이지의 이동 경로 줄을 입력 그대로 두므로(storyteller.md 4.2, verifier.md 11절 항목 4) 실행에는 문제가 없다. 시드 네 페이지를 이 규칙으로 통일할지는 트랙 시드(docs) 담당의 결정 사항이다(요청).
4. **H1 제목**. 상태 줄은 다음 다섯 템플릿에만 있고 형식이 서로 다르다: area·topic `> 상태: … · 신뢰도: … · 갱신일: …`, track-overview `> 트랙 상태: … · 현재 단계: 단계 n. <단계 이름> · 마지막 트랙 실행: …`(시드와 같이 "단계 " 접두어를 둔다), track-stage `> 단계 상태: … · 열린 질문: …건 · 답한 질문: …건 · 완료 조건: <충족 | 미충족> · 마지막 실행: …`, ontology-draft `> 온톨로지 버전: v… · 페이지 상태: … · 신뢰도: … · 마지막 변경 실행: …`. home·about·category·glossary·reference·daily-log·track-log 에는 상태 줄이 없다.
5. **섹션** (`## 제목`). 5.4·4.3의 제목을 그 순서로 두고, 각 섹션 아래 HTML 주석으로 무엇을 어떻게 쓰는지 안내한다. 자동 갱신 섹션은 `<!-- auto:<key>:start -->` … `<!-- auto:<key>:end -->` 사이에 "퍼블리셔가 자동으로 채운다." 한 줄을 둔다.

완성 페이지에서는 안내 주석(HTML 주석과 프런트매터 `#` 주석)을 지우고 auto 마커 주석만 남긴다. `{{`가 남아 있으면 퍼블리셔가 반려한다.

## 섹션 제목 정본

`pipeline/checks/protect_source.py` 의 `AREA_SECTIONS`·`CATEGORY_SECTIONS` 가 세부영역·대분류 페이지의 H2 문자열을 글자 단위로 검사한다. 아래 area·category 정본은 그 값 및 시드 페이지와 같다(사양서 5.4·4.3 문구 그대로: 괄호 설명 포함, 대분류는 번호 없음). 나머지 유형은 검사 스크립트가 H2 를 보지 않으며 2차 검증(사양서 6.2 "템플릿 섹션 순서 준수")이 아래 정본으로 본다. 아래 정본은 시드 페이지(세부영역 28·대분류 7·트랙 개요·트랙 단계 7·온톨로지 초안)의 실제 H2, `agents/storyteller.md` 부록 B, `agents/verifier.md` 부록 C 와 글자 단위로 같다.

해석 규칙 [가정 — 완료 보고의 사용자 결정 항목]: 세부영역·대분류의 H2 는 검사 스크립트 문자열을 그대로 따른다(세부영역은 5.4 의 괄호 설명까지 제목에 포함). 나머지 유형(주제·트랙 개요·트랙 단계·온톨로지 초안)은 5.4 의 제목 본문을 그대로 쓰고 괄호·줄표(—) 뒤 설명구만 제목에서 뺀다. 제목 본문에 있는 "표"는 설명구가 아니므로 남긴다: "5. 단계 진행 현황 표 (…)" → `5. 단계 진행 현황 표`, "2. 개념 목록 표 (…)" → `2. 개념 목록 표`, "3. 관계 목록 표 (…)" → `3. 관계 목록 표`. 설명구를 뺀 예: "5. ROP 관점의 시사점 (직접 범위 / 연계 범위 구분)" → `5. ROP 관점의 시사점`, "9. 검증 노트 — 판정, …" → `9. 검증 노트`, "7. 최근 실행 (자동)" → `7. 최근 실행`, "2. 질문 목록 (상태: …)" → `2. 질문 목록`. 같은 5.4 문구를 유형에 따라 다르게 적용한 것(세부영역만 괄호 포함)이므로 사용자 결정 항목이다. 시드 페이지·`agents/storyteller.md` 부록 B·`agents/verifier.md` 부록 C 가 같은 값을 쓴다. 설명구는 각 템플릿의 안내 주석에 옮겨 두었다.

- **area**: `1. 한 줄 정의` `2. SCM 관점의 질문` `3. 왜 중요한가` `4. 핵심 개념과 용어` `5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)` `6. 대표 접근법과 기술` `7. 관련 표준·프레임워크·오픈소스` `8. 대표 연구와 자료` `9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)` `10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)` `11. 열린 질문` `12. 최근 업데이트 (자동)` `13. 참고 자료 (각주)`
- **category**: `핵심 질문` `개요` `세부 연구영역` `이 대분류의 핵심 포인트` `다른 대분류와의 연결` `최근 업데이트` + 번호 없는 `참고 자료` [가정] (검사 스크립트는 앞 여섯 개만 본다)
- **topic**: `1. 세 줄 요약` `2. 배경` `3. 본문` `4. 현장 시나리오` `5. ROP 관점의 시사점` `6. 연결되는 연구영역` `7. 열린 질문` `8. 출처` `9. 검증 노트` `10. 이력`
- **home**: `ROP란 무엇인가` `이 위키가 다루는 범위` `대분류 표` `다루지 않는 것` `콘텐츠가 만들어지는 방식` `진행 중인 중점 연구 트랙` `표기 범례` `최근 업데이트` `시작하기 좋은 페이지` `정정과 요청`
- **track-overview**: `1. 컨셉` `2. 연구 목표` `3. 가설과 판정 상태` `4. 관련 세부영역` `5. 단계 진행 현황 표` `6. 살아있는 산출물 링크` `7. 최근 실행` `8. 참고 자료`
- **track-stage**: `1. 이 단계에서 밝힐 것` `2. 질문 목록` `3. 조사 결과` `4. 결론과 남은 불확실성` `5. 이 단계가 낳은 후속 질문` `6. 완료 조건 충족 현황` `7. 관련 세부영역` `8. 출처` `9. 이력`
- **ontology-draft**: `1. 목적과 범위` `2. 개념 목록 표` `3. 관계 목록 표` `4. 다이어그램` `5. 적용 예시` `6. 미해결 모델링 질문` `7. 버전 이력`
- **glossary**: `용어` `한 줄 정의` `설명` `관련 영역` `출처`
- **reference**: `서지 정보` `요약` `인용된 페이지` `각주 형식` `비고`
- **daily-log**: `실행 <실행 id>` 아래 `실행 개요` `단계별 결과와 소요 시간` `검증 판정` `생성·갱신 페이지` `신규 출처 수` `반려·보류 사유` `예산 사용량` `다음 실행 메모` (H3)
- **track-log**: `항목 형식` [가정] `실행 기록`(auto: track-log [가정]). 실행 기록 마커 안에 실행마다 `실행 <실행 id> — 단계 <번호>. <이름>` (H3) + 8항목 표
- **about**: 고정 절은 `관련 페이지` `참고 자료` 두 개, 본문 절 제목은 자유

**agents 파일과의 대조(2026-09-24 확인)**: `agents/storyteller.md` 부록 B(1.3)와 `agents/verifier.md` 부록 C(1.3)는 위 정본과 일치한다(세부영역 괄호 포함, 대분류 번호 없음, 트랙 개요 `5. 단계 진행 현황 표`, 온톨로지 초안 `2. 개념 목록 표`·`3. 관계 목록 표`, 대분류 "현재 상태" 열은 퍼블리셔 갱신). 세부영역 머리의 소속 대분류 블록도 시드 28페이지·area.md·storyteller.md 4.2·verifier.md 11절 항목 3·부록 C 가 같은 세 줄 형식이다: `!!! info "소속 대분류"` / 공백 4칸 + `[<대분류>](index.md) — 핵심 질문:` / 공백 4칸 + `<핵심 질문 원문> [분류원문]`. 링크와 핵심 질문을 한 줄에 합친 형식과 한 줄 `**소속 대분류:** …` 단락 형식은 쓰지 않는다(아래 "세부영역 페이지" 항목).

## 검사 스크립트가 보는 것 (다른 담당이 알아야 할 것)

- **`[분류원문]` 줄의 형식.** `pipeline/lib/verbatim.py` 의 `untag`/`strip_tags` 는 줄 끝이 정확히 ` [분류원문]` 인 경우에만 태그를 벗긴다. 태그 뒤에 각주(`[^ref-003]`)나 다른 글자가 오면 태그가 벗겨지지 않아 원문 대조에 실패한다. 따라서 원문 문장 줄은 ` [분류원문]` 으로 끝내고, 원문의 `[n]` 에 대응하는 각주는 별도 문장(예: `원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]`)에 둔다. 표는 표 아래 빈 줄 다음에 `[분류원문]` 한 줄을 둔다. 시드 페이지(대분류·세부영역·홈·소개)가 모두 이 형식이다.
- **세부영역 페이지(`check_area`).** 프런트매터 title·category·area_no·type, H2 13개(위 정본과 글자 단위 일치), H1, H2 앞 부분에 소속 대분류 이름과 핵심 질문 + ` [분류원문]`, 1절 첫 내용 줄 = 정의 + ` [분류원문]`, 2절 첫 내용 줄 = 질문 + ` [분류원문]`, 2절 안의 `> 원문 주석: <문단> [분류원문]` 인용 블록 목록 = 원문에서 그 영역을 "N번"으로 언급하는 문단 목록(5. 로봇 능력·작업 온톨로지, 6. 지도·공간·위치 모델, 7. 화물·재고·자산 식별과 추적, 8. 실시간 세계 상태·데이터 일관성, 13. 작업 배정 — MRTA, 17. 로봇 간 협업·물리적 인계, 19. 모니터링·이상 탐지·원인 분석, 21. 온보딩·설정·현장 시운전, 22. 시뮬레이션·예측용 디지털 트윈, 27. AI·학습·적응과 모델 운영만 해당. 6. 지도·공간·위치 모델은 두 문단). 원문 주석을 1절에 두거나 굵은 "**원문 주석:**" 단락으로 두면 반려된다. 시드 세부영역 페이지와 템플릿은 소속 대분류·핵심 질문을 세 줄 admonition 블록으로 둔다: 1줄 `!!! info "소속 대분류"`, 2줄 공백 4칸 + `[<대분류>](index.md) — 핵심 질문:`(콜론에서 줄이 끝난다), 3줄 공백 4칸 + `<핵심 질문 원문> [분류원문]`. 셋째 줄은 태그를 뗀 문자열이 원문 1장 표의 핵심 질문 셀과 같으므로 아래 `check_tagged_lines` 를 통과한다. 링크와 질문을 한 줄에 합치면 태그 줄(`[<대분류>](index.md) — 핵심 질문: <원문>`)이 원문 어디에도 없어 반려된다. 2차 검증(`agents/verifier.md` 11절 항목 3·부록 C)은 이 블록을 입력 시드와 들여쓰기·줄바꿈까지 글자 단위로 대조하고, 한 줄 `**소속 대분류:**` 형식이나 합친 한 줄 형식을 [분류원문] 훼손(불통과)으로 본다. 따라서 이 형식만 쓴다.
- **대분류 페이지(`check_category`).** H2 앞 여섯 개(번호 없음), "핵심 질문"·"개요" 첫 줄, "세부 연구영역" 표 각 행의 앞 3칸(첫 칸은 `**5. …**` 굵은 원문 셀, 링크 없음)과 표 아래 `[분류원문]` 줄, "이 대분류의 핵심 포인트"에서 ` [분류원문]` 으로 끝나는 줄 목록 = 원문 문단 목록. 표는 원문 3열 + "페이지" + "현재 상태" 5열이며 `auto:category-area-table` 마커 안에 있고 퍼블리셔(`pipeline/lib/render.py` `render_category_area_table`)가 현재 상태 열까지 다시 쓴다. 이 key 는 사양서에 없는 구축자 추가 key 이며 시드 페이지·`agents/shared-rules.md` 6절의 auto key 목록·`pipeline/lib/autoregion.py` `AUTO_KEYS` 가 같은 값을 쓴다 [가정 — 사용자 결정 항목].
- **홈(`check_home`).** 정의 문장, SCOR 문단(`… 범위가 다르다. [1] [분류원문]`), 범위 문장이 각각 한 줄 그대로(인용 부호 `>` 없이) 있어야 하고, 대분류 표는 첫 칸이 `A. ` 처럼 원문 대분류 이름으로 시작하는 행의 앞 3칸이 원문 표 행(대분류 / 핵심 질문 / `1–4`)과 같아야 한다. 링크는 4·5열에만 둔다. "다루지 않는 것" 목록은 원문 9장의 "경계" 셀과 "주로 연계할 외부 영역" 셀을 " — " 로 이어 붙인 줄이므로 태그를 붙이지 않는다(아래 `check_tagged_lines`). 시드 홈 페이지도 같은 방식이며 태그를 붙이지 않는 이유를 목록 위 문장으로 밝힌다.
- **태그 줄 원문 대조(`check_tagged_lines`).** docs 전체 페이지에서 ` [분류원문]` 으로 끝나는 모든 줄(코드 펜스 안과 표 아래 단독 태그 줄 제외)은 태그를 뗀 문자열이 원문의 한 줄 전체 또는 표 셀 하나(머리말의 범위 문장 포함)와 글자 단위로 같아야 한다. 두 셀을 이어 붙인 줄, 문장 일부, 인용 부호 `>` 가 붙은 줄, 링크 같은 다른 글자가 앞에 붙은 줄에는 태그를 붙일 수 없다.
- **프런트매터(`check_frontmatter`).** 필수 `title, type, status, created, updated, version` + `pipeline/lib/frontmatter.py` TYPE_REQUIRED(area: category·area_no / topic: primary_area_no / glossary: term_ko·definition / reference: ref_id·org·url·source_type·reliability·published·accessed / track·ontology-draft·track-log: track / track-stage: track, stage). 본문 첫 줄은 이동 경로. `subtype: index` 색인 페이지는 유형별 필수 필드를 면제한다.
- **각주(`check_links`).** 본문의 `[^id]` 참조마다 `[^id]:` 정의가 있어야 한다(없으면 오류, 정의만 있으면 경고). 코드 펜스 안의 정의는 세지 않으므로 reference.md 의 "각주 형식" 절은 코드 펜스로 둔다.
- **각주 정의 형식**은 시드 페이지 전체가 쓰는 `[^ref-NNN]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD` 이다. 발행일을 모르면 발행일 자리에 `미확인`, 접근일은 날짜 앞에 `접근일 ` 을 붙이고, 원문 미열람은 접근일 뒤 ` (원문 미열람)`. 예: `[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24`(docs/references/ref-003.md 의 "각주 형식" 절, docs/about/what-is-rop.md 의 각주 정의와 같다). reference.md 의 "각주 형식" 절이 이 한 줄의 원본이며, 템플릿 공통 규칙 9항, `agents/shared-rules.md` 6절, `agents/storyteller.md` 4.4 가 같은 형식을 쓴다. 프런트매터·서지 정보 표의 `published` 도 모르면 `미확인` 이다(리서치 JSON 의 `published` 는 `null`, 페이지로 옮길 때 `미확인`). 참고문헌 시드의 `status` 는 `seed` 이며 템플릿 status 주석에 반영했다. 시드 참고문헌 페이지는 "서지 정보" H2 없이 표를 H1 바로 아래에 두고 "비고" 절이 없다. 템플릿은 퍼블리셔(`pipeline/publish.py` `_apply_references`)가 새 참고문헌 페이지에 쓰는 5절 구성을 유지하되 제목 형식(`ref-003 — 제목`), 서지 표의 "원문 열람" 행, "각주 형식"·"인용된 페이지" 절(auto:reference-cited-pages 마커와 마커 위 안내 문장)은 시드에 맞췄다. 두 구성의 통일은 시드·pipeline 담당의 결정 사항이다(요청).
- **상태 줄과 현재 상태 열.** 세부영역·주제·트랙 페이지의 상태 줄(`> 상태: …` 등)은 auto 마커 밖에 있으므로 스토리텔러가 해당 페이지를 갱신할 때 맞춘다. 대분류 페이지의 "현재 상태" 열은 위와 같이 퍼블리셔가 채운다.
- **트랙 상태 값(구축자 정의, 사양서에 없음 [가정]).** 단계 상태: `대기 | 진행 중 | 완료 | 재개` (퍼블리셔 `render_track_progress` 와 `config/tracks/<slug>.yaml` 의 `stage_status` 가 같은 값) / 완료 조건: `충족 | 미충족` 두 값뿐이다(퍼블리셔 출력과 같다. 일부만 채운 조건은 단계 페이지 6절 표에서 행을 나눠 나타내고 상태 줄은 `미충족`) / 검증 판정 표시: `stage_complete` true → 충족, false → 미충족, `stage_transition_approved` true → 전환 승인, false → 미승인, 구축 시점은 `없음(구축 시점, 판정 전)`, 판정 전 실행은 `없음(판정 전)` / 질문 표 제기 근거: 사양서 8.2 대로 `<finding id> | 사용자` 두 가지뿐이다(시드 질문은 `사용자`. `data/tracks/<slug>/backlog.json` 의 `origin` 값, `schemas/pages.schema.json` 의 `backlog_updates[].origin` 패턴과 같다). 뒤 단계에서 앞 단계로 되돌아온 질문은 제기 근거 값이 아니라 앞 단계 태그(`stage` 값과 id 의 단계 부분)로 나타낸다 / 온톨로지 개념 상태: `초안 | 제안 | 확정 | 폐기` / 온톨로지 버전: v0 시드는 `"0"`, 이후 `"0.1"`, `"0.2"` … .
- 일일 로그는 퍼블리셔(`pipeline/publish.py` 의 `daily_block`·`write_daily_log_and_summary`, 사양서 6.4 순서 8)가 페이지 전체를 쓴다(마커 없음). daily-log.md 의 `## 실행 <실행 id>` 와 여덟 개 H3 구성이 그 출력과 같다. 실행이 하루에 둘 이상이면 같은 날짜 페이지에 "실행 <id>" 블록을 최신순으로 반복한다. 트랙 로그는 머리말과 "항목 형식" 절을 구축자가 쓰고(마커 밖), "실행 기록" 절 본문은 `auto:track-log` 마커 안에서 퍼블리셔가 채운다: 트랙 실행을 반영할 때 원천 `data/tracks/<slug>/log.json` 에 항목을 추가하고, 그 파일에서 8항목 블록을 최신순으로 다시 만든다(`track-log` 는 `pipeline/lib/autoregion.py` 의 `AUTO_KEYS` 와 `agents/shared-rules.md` 6절의 auto key 목록에 있는 key 다. 시드와 같은 구성).
- ontology-draft 의 `ontology_version`(문자열 `"0"`, `"0.1"`, …)은 pages.json 의 `track_updates.ontology_draft_version`과 같은 값이고, 페이지 `version`(정수)과는 별개다.
- 템플릿 안의 `{{…}}` 때문에 템플릿 파일 자체는 유효한 YAML/페이지가 아니다. 검사 스크립트는 templates/ 를 페이지로 취급하지 않는다.
- HTML 주석 안에는 `--`를 쓰지 않았다(주석 조기 종료 방지). 주석 안의 표는 구분 행을 `|-|-|`로 썼다.

## 가정 목록

- category.md 의 번호 없는 "참고 자료" 절은 4.3 여섯 섹션 밖의 구축자 추가 절이다(5.3 각주 정의 자리).
- `auto:category-area-table` key 는 사양서에 없는 구축자 추가 key 다(시드·`AUTO_KEYS`·`agents/shared-rules.md` 6절이 같은 값). 표 전체를 자동 영역으로 둘지는 사용자 결정 항목이다.
- `auto:reference-cited-pages` key 는 사양서에 없는 구축자 추가 key 다(시드·`autoregion.AUTO_KEYS`·`render.render_reference_cited_pages`·`agents/shared-rules.md` 6절이 같은 값). reference.md 의 "인용된 페이지" 절이 이 마커를 쓴다.
- `auto:track-log` key 는 사양서에 없는 구축자 추가 key 다(시드·`AUTO_KEYS`·`agents/shared-rules.md` 6절이 같은 값). track-log.md 의 "실행 기록" 절이 이 마커를 쓰고, 퍼블리셔가 `data/tracks/<slug>/log.json` 에서 최신순으로 채운다. 시드와 같은 "항목 형식" 절(5.4 의 8항목 밖의 구축자 추가 절)을 둔다.
- 섹션 제목의 해석 규칙(세부영역·대분류는 검사 스크립트 문자열, 나머지 유형은 5.4 제목 본문 그대로 두되 괄호·줄표 뒤 설명구만 뺌. "표"는 제목 본문이므로 유지)은 위 "섹션 제목 정본"의 [가정]이며 사용자 결정 항목이다.
- 분량 기준 가운데 track-stage.md 의 "단계 전체 6,000자 초과 시 주제 페이지로 분리"와 glossary.md 의 "한 항목 300~800자"는 사양서 5.4(주제 1,500~2,500자, 세부영역 4,000자 이내)에 없는 구축자 기준이다.
- 이동 경로의 단계 구성(소개 페이지는 "소개" 단계 없이 `홈 › 제목`, 트랙 하위 페이지는 `홈 › 중점 연구 트랙 › [트랙 이름] › 페이지`)은 4.8 의 사이드바 순서와 시드(트랙 개요·단계 7페이지·소개 7페이지)를 따른 구축자 결정이다.
- 세부영역 페이지 머리의 세 줄 admonition 블록 형식은 시드 28페이지를 정본으로 본 구축자 결정이다. 셋째 줄만 ` [분류원문]` 태그 줄이므로 퍼블리셔 원문 보호 검사를 통과한다.
- glossary.md 의 `term_ko, term_en, definition`, reference.md 의 `ref_title`·`url_verified` 는 5.1 에 없는 필드이며 퍼블리셔 색인과 시드 페이지가 쓰는 값이다.
- 트랙 페이지의 단계 상태·완료 조건·온톨로지 개념 상태·온톨로지 버전 표기 값은 위 "트랙 상태 값" 항목대로 구축자가 정했다. 제기 근거 값은 사양서 8.2 그대로다.
- 홈에는 각주 절이 없으므로 참고문헌은 `[^ref-NNN]` 각주 대신 페이지 링크로 가리킨다. 본문에 각주 표기 예시를 쓸 때는 백틱으로 감싼다(check_links 가 정의 없는 참조로 보지 않도록).
- ontology-draft 는 5.4 의 일곱 절에 출처 절이 없으므로 각주 정의를 7절 auto 마커 아래(페이지 끝)에 둔다.
- category 페이지의 `status` 는 시드 상태에서 `seed`, "다른 대분류와의 연결"이 채워져 게시되면 `published` 로 본다.
