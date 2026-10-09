# 스토리텔러 산출 2026-10-09-27

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md | draft | q2-05·q2-06 답함(#q2-05·#q2-06 소절 신설), q2-07 부분 답 소절(#q2-07), 4절 결론·불확실성 갱신(VDA 5050 loads 문장에 기준일 표시), 후속 질문 q4-21·q4-22, 완료 조건 미충족·전환 아니오, 반영 제안 3건, 출처 10건 추가 |
| update | docs/tracks/chat-based-configuration-and-operation/task-model-draft.md | draft | 초안 v1.0 → v1.1: 상황 개념의 대상 표현에 해석 결과 '대상 화물 참조'(품목 단위 / 적재 단위) 짝 추가(f10·f11·f12·f13, 대응 원천은 f15 추정 메모, 상태 확정 유지), 1절 v1.1 요지, 6절에 q2-05·q2-06·q2-07 답 링크(질문은 닫지 않음) |
| update | docs/ideas/chat-based-configuration-and-operation.md | draft | 4절에 '이름 사전 형식'·'대상 화물의 두 식별 단위와 대응 원천'·'IEEE 1872.1-2024 의 공개 자료 범위 분해 구조' 소절 추가(기존 표와 '미확인' 표기 유지) |
| update | docs/tracks/chat-based-configuration-and-operation/index.md | draft | 6절 살아있는 산출물에 실행 2026-10-09-27 항목 추가(q2-05·q2-06 답함, q2-07 부분 답, 초안 v1.0 → v1.1, 전환 미승인); 상태 줄은 현재 단계 2·마지막 트랙 실행 2026-10-09 그대로 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | 채팅 기반 구성·운영 단계 2 | q2-05·q2-06 답함, q2-07 부분 답, 업무 분해·배정 설계 초안 v1.0 → v1.1(상황 개념에 대상 화물 참조), 새 질문 2건(q4-21·q4-22), 1차 조건부 승인 수정 20건 이행 | run 2026-10-09-27
- 홈 최근 업데이트: 2026-10-09 — 채팅 기반 구성·운영 단계 2: 지시 속 장소 이름 사전 형식(q2-05)과 대상 화물의 품목·적재 단위 대응(q2-06)에 답하고 IEEE 1872.1-2024 대응(q2-07)은 부분 답, 업무 분해·배정 설계 초안 v1.1
- 대분류 최근 업데이트: 2026-10-09 — C. 채팅 기반 구성·운영 · 채팅 기반 구성·운영 트랙 단계 2: 장소 이름 사전(IMDF·SKOS·GLN 확장 성분)과 대상 화물 식별 단위(VDA 5050 loads·EPCIS 집계 이벤트·SSCC) 조사, 신뢰도 low
- 세부영역 최근 업데이트: 2026-10-09 — 채팅 기반 구성·운영 트랙 단계 2: 지시 속 장소 이름 사전과 대상 화물 식별 단위 조사(신뢰도 low), 세부영역 반영 제안 3건(16. 장소 의미·지도 관리, 17. 작업 대상·자산 식별과 인계 추적, 5. 로봇 능력·작업 표현)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 단순 지식 조직 체계 | Simple Knowledge Organization System (SKOS) | 개념에 언어별 대표 이름(prefLabel)·대체 이름(altLabel)·검색용 숨은 이름(hiddenLabel)과 코드(notation)를 붙여 용어 체계를 표현하는 W3C 권고안(2009)이다. | 16, 12, 15 | ref-1394 |
| new | GLN 확장 성분 | GLN Extension Component | 물리적 위치를 가리키는 GS1 위치 코드(GLN)에 덧붙여 그 시설 안의 구역·선반 같은 하위 위치를 식별하는 GS1 의 코드 성분이다. | 16, 17, 15 | ref-1400 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-1392 | GS1 (gs1/EPCIS GitHub) | EPCIS — JSON-Schema/schemas/AggregationEvent-JSON-Schema.json | 표준 | high | https://github.com/gs1/EPCIS/blob/master/JSON-Schema/schemas/AggregationEvent-JSON-Schema.json |
| ref-1393 | OGC (Apple Inc. 기여) | Indoor Mapping Data Format (IMDF) 1.0.0 — Unit | 표준 | high | https://docs.ogc.org/cs/20-094/Unit/index.html |
| ref-1394 | W3C (Miles, A., & Bechhofer, S. 편집) | SKOS Simple Knowledge Organization System Reference | 표준 | high | https://www.w3.org/TR/skos-reference/ |
| ref-1395 | GS1 Belgium & Luxembourg | Logistic units | 표준 | medium | https://www.gs1belu.org/en/logistic-units |
| ref-1396 | Balakirsky, S. B., Schlenoff, C. I., Fiorini, S. R. 외 (NIST 게시, MSEC 2017) | Towards a Robot Task Ontology Standard | 논문 | medium | https://www.nist.gov/publications/towards-robot-task-ontology-standard |
| ref-042 | Aguado, E., Gomez, V., Hernando, M., Rossi, C., & Sanz, R. (Frontiers in Robotics and AI 11) | A survey of ontology-enabled processes for dependable robot autonomy | 논문 | high | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1377897/full |
| ref-1398 | Murata, K., Hasegawa, S., Ishikawa, T., Hagiwara, Y., Taniguchi, A., El Hafi, L., & Taniguchi, T. | Multi-Robot Task Planning for Multi-Object Retrieval Tasks with Distributed On-Site Knowledge via Large Language Models | 논문 | medium | https://arxiv.org/abs/2509.12838 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-1400 | GS1 | GLN extension component | 표준 | medium | https://gs1.org/standards/id-keys/gln/extension-component |

## 열린 질문 갱신

- 없음

## 현장 유형 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| W3C SKOS (Simple Knowledge Organization System) Reference | 표준 | W3C | 16, 12, 15 | ref-1394 | https://www.w3.org/TR/skos-reference/ |

## 추가 조사 요청

- 단계 2 q2-07: IEEE 1872.1-2024 의 실무 구현 지침 P1872.1.1, 공개 사용 사례나 OWL 파일이 있어 작업 분해·선후 의존·배정 대상 개념을 표준 본문 없이 확인할 수 있는지 조사 필요(완료 조건과 q2-07 해소에 필요)
- 단계 2 완료 조건 2: 업무 분해·배정 설계 초안의 작업 요구 적재물 속성을 매뉴얼 기반 로봇 기능 온톨로지 트랙의 능력 온톨로지 초안 작업 요구와 대조할 근거, 업무 완료 조건의 표현 원천(작업 상태 스키마·EPCIS 이벤트) 조사 필요
- q2-05 보강: 국내 WMS 로케이션 코드(동·열·연·단) 체계의 공식 자료와 GS1 Korea 의 GLN 확장 성분·SSCC 적용 자료 조사 필요(이번 한국어 검색에서 공식 자료 없음, oq-029·oq-002 관련)
- GS1 GLN 확장 성분 원문(gs1.org 403)과 IMDF LABELS 자료형 정식 정의를 열람해 이번 [사실] 근거의 원문 미열람·예시 기준 한계를 해소할 필요

## 이행한 수정 지시

- f10 표현 정정 — 단계 2 #q2-06 소절, 초안 2절 상황 행, 아이디어 4절에서 '판단할 수 있을 때 빈 배열은 무적재·판단할 수 없으면 배열 생략', 'loadId 는 식별할 수 있으나 아직 식별하지 않았으면 빈 값(식별할 수 없는 로봇은 생략 가능)'으로 원문대로 고쳐 씀
- f10 남은 불확실성 — 단계 2 4절의 'VDA 5050 상태 메시지의 적재물(loads) 필드 세부는 확인하지 못했다' 문장을 지우지 않고 '(실행 2026-09-25 기준)'을 붙인 뒤 실행 2026-10-09-27 에서 확인했다는 문장을 [q2-06](#q2-06) 링크와 함께 덧붙임
- f9 — #q2-05 공백 문장, 아이디어 4절 '공백' 항목, 세부영역 반영 제안 어디에도 '가정 환경'을 쓰지 않고 '학습한 공간 개념을 배정에 쓰는 Murata 외'로만 씀
- f7 — 47/50(무작위 28/50, 상식 기반 26/50)을 저자 보고·프리프린트(AROB-ISBC 2026 투고)·정량 실험 환경·로봇 수는 초록에 없음으로 적고 이동 매니퓰레이터 2대는 정성 평가에만 연결, 교차 규칙대로 44. 로봇 기반 모델·언어 모델 계획과 25. 작업 배정 — MRTA 에 연결(단계 2 #q2-05·7절)
- f8 — 'VDA 5050 지도 id' 바로 뒤에 기존 각주 ref-413 을 붙이고, WMS 로케이션 코드는 출처로 확인하지 못한 구성 요소임을 문장 안에 밝히며 국내 체계 미확인(f9) 문장과 함께 두고 문장 전체를 [추정](이 위키의 종합, 물류 현장 사례 미확인)으로 유지(단계 2 #q2-05, 아이디어 4절)
- f2·f3·f11·f14 — #q2-05·#q2-06 소절에서 다시 서술하지 않고 [q2-01](#q2-01)의 기존 서술을 가리키는 문장으로 쓰며 기존 각주 ref-412·ref-414·ref-411·ref-130 을 재사용
- f17 — #q2-07 소절에서 [q2-02](#q2-02)의 기존 IEEE 1872.1-2024 서술과 각주 ref-504 를 재사용하고 새로 더한 것은 이사회 승인일 2024-02-15 와 작업반 RTR 뿐이며, reference_updates 에 ref-504 를 넣지 않아 참고문헌 행을 바꾸지 않음
- f20·q2-07 — 소제목을 '### q2-07 IEEE 1872.1-2024 작업 표현과 초안 개념의 대응 (부분 답) {#q2-07}'로 두고 소절 첫머리에 표준 본문(유료) 미열람으로 선후 의존·배정 대상 개념이 미확인임을 적었으며, f19 하위 그룹을 1872.1 작업반과 같은 계열로 잇는 것이 이 위키의 추론임을 밝힘(서베이 본문에 1872.1 번호 없음도 명시)
- f6 — 각주 ref-1400 의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-1400 에 source_unopened: true 와 '원문 미열람.'으로 시작하는 요약을 넣었으며 예시 'A.12'는 쓰지 않음
- f4·f12·f13 — 각 페이지 첫 등장에서 실내 지도 데이터 형식(IMDF)·대체 이름·집계 이벤트·물류 단위 일련 코드(SSCC) 용어집 항목에 링크했고, IMDF 이름·대체 이름의 로봇 지시 해석 문제는 새 열린 질문 없이 oq-204 를 가리킴
- f13 — ref-1395 를 본문에서 'GS1 회원 기관인 GS1 Belgium & Luxembourg 의 안내(GS1 본부 표준 원문은 아님)'로 쓰고 각주 기관 칸에도 같은 내용을 밝힘
- 온톨로지 상황 변경 — 초안 2절 상황 행의 주요 속성에 '대상 표현과 그 해석 결과인 대상 화물 참조(값 후보: 품목 단위(sku·수량, Open-RMF 배송) / 적재 단위(SSCC 물류 단위 또는 로봇 보고 loadId, VDA 5050 loads))'를 짝으로 더하고 근거 칸에 f10·f11·f12·f13(실행 2026-10-09-27)과 각주 ref-051·ref-411·ref-1392·ref-1395 를 둠. GTIN 은 넣지 않았고 대응 원천은 [추정] 메모(f15)로만 두어 정의에 넣지 않았으며 상태 '확정' 유지, 작업 요구 행은 바꾸지 않고 6절 적재물 질문은 닫지 않은 채 #q2-06 링크만 덧붙임
- 온톨로지 버전 — 프런트매터 ontology_version '1.1', H1 '(v1.1)', track_updates.ontology_draft_version '1.1'로 맞추고 1절에 v1.1 변경 요지 문단을 덧붙였으며, 6절에 장소 이름 대응 규칙 항목에는 #q2-05 답 링크(f8, 추정)를, IEEE 1872.1-2024 항목에는 #q2-07 부분 답 링크(f20)를 덧붙이고 두 질문은 닫지 않음(auto 상태 줄 마커 안은 손대지 않음)
- P1872.1.1·OWL 확인 질문 — backlog_updates 에 넣지 않고 단계 2 #q2-07 소절의 '남은 불확실성과 확인 경로'와 5절 설명에 q2-07 의 확인 경로로 적음
- 새 트랙 질문 2건 — q4-21(별칭 중복 시 좁히기·되묻기 규칙, 단계 4, origin f8)과 q4-22(지시 SSCC 와 로봇 보고 loadId 불일치 처리, 단계 4, origin f10)를 '(관련: q4-20, q4-07)'·'(관련: oq-003, oq-036)' 표기를 유지한 채 backlog_updates 와 단계 2 5절 표에 등록
- 단계 2 2절 — q2-05·q2-06 을 답함(답한 실행 2026-10-09-27, 답 위치 #q2-05·#q2-06)으로 바꾸고 3절에 '### q2-05 … {#q2-05}'·'### q2-06 … {#q2-06}' 소제목을 둠. q2-07 은 열림(백로그 조사 중)으로 두고 상태 줄을 '진행 중 · 열린 질문: 1건 · 답한 질문: 6건 · 완료 조건: 미충족'으로 맞춤
- 단계 2 6절 — 완료 조건 1 은 '충족'·검증 판정 '충족 · 미승인', 완료 조건 2 는 '미충족'·'미충족 · 미승인'으로 쓰고 아래 줄을 '다음 단계로 전환: 아니오(작업 요구 적재물 속성·완료 조건 미확정; 열린 질문 q2-07)'로 둠. track_updates.stage_transition 은 넣지 않았고 트랙 개요 상태 줄은 '현재 단계: 단계 2. 필요한 데이터와 표준 조사 · 마지막 트랙 실행: 2026-10-09' 그대로 유지(개요 6절에 실행 항목 추가)
- 아이디어 4절 — '필요한 데이터 항목과 원천' 표와 '미확인' 표기는 지우지 않고 4절에 '이름 사전 형식'(f4·f5·f6, 종합 f8 추정)과 '대상 화물의 두 식별 단위와 대응 원천'(f10·f12·f13, 종합 f15 추정, f16 연계 대상) 소절을 더했으며, IEEE 1872.1-2024 행 '미확인'은 유지한다고 밝히고 공개 자료 범위의 분해 구조(f18·f19, 종합 f20 추정)를 병기하는 소절을 더함
- 세부영역 반영 제안 3건 — 16. 장소 의미·지도 관리, 17. 작업 대상·자산 식별과 인계 추적, 5. 로봇 능력·작업 표현을 area_reflection_proposals 와 트랙 로그 '세부영역 반영 제안'·단계 2 7절로만 남기고 세부영역 페이지는 고치지 않음. 16 제안에는 15. 지도·공간·위치 모델과 12. 채팅으로 업무 지시·오케스트레이션을 함께 연결하고 '가정 환경'은 쓰지 않음
- 용어집 — '단순 지식 조직 체계(Simple Knowledge Organization System, SKOS)'와 'GLN 확장 성분(GLN Extension Component)'을 브리프 정의대로 glossary_updates 에 냈고, GLN 확장 성분 설명에는 '물리적 위치를 식별하는 GLN 과 함께만 쓴다'(f6) 범위만 넣음

## 트랙 갱신

- 단계 페이지: docs/tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md
- 온톨로지 초안 버전: 1.1
- 트랙 로그 항목: 답한 질문: q2-05(이름 사전 형식·관리 분담, f1~f9, 신뢰도 low), q2-06(대상 화물 품목·적재 단위와 대응 원천, f10~f16, 신뢰도 low); 부분 답: q2-07(f17~f20, IEEE 1872.1-2024 본문 미열람, 백로그 조사 중) / 새 질문: q4-21(근거 f8), q4-22(근거 f10); P1872.1.1·OWL 확인 질문은 q2-07 과 같은 질문이라 미등록하고 #q2-07 확인 경로로 적음 / 온톨로지 변경: v1.0 → v1.1: 개념 '상황 (Situation)' 대상 표현에 해석 결과 '대상 화물 참조'(품목 단위 sku·수량 / 적재 단위 SSCC 또는 로봇 보고 loadId) 짝 추가(f10·f11·f12·f13, 대응 원천은 f15 추정 메모, GTIN 제외, 상태 확정 유지, 작업 요구 불변) — 버전 이력 행: 1.1 | 2026-10-09 | v1.0 → v1.1: 상황 개념 대상 표현에 '대상 화물 참조' 짝 추가(f10·f11·f12·f13), 대응 원천 추정 메모(f15) | 2026-10-09-27 / 완료 조건 평가: 미충족(부족: 업무 분해·배정 설계 초안 개념 목록 표의 작업 요구 적재물 속성·완료 조건 미확정; 열린 질문 q2-07), 단계 전환 미승인 / 세부영역 반영 제안: 3건 — 16. 장소 의미·지도 관리(IMDF·SKOS·GLN 확장 성분 이름 사전 형식, 15. 지도·공간·위치 모델·12. 채팅으로 업무 지시·오케스트레이션 연결), 17. 작업 대상·자산 식별과 인계 추적(VDA 5050 loads·EPCIS 집계 이벤트·SSCC), 5. 로봇 능력·작업 표현(IEEE 1872.1-2024 공개 범위) / 다음 실행 제안: q2-07(P1872.1.1·공개 사용 사례·OWL 확인 경로), 작업 요구 적재물 속성의 능력 온톨로지 초안 대조와 업무 완료 조건 원천 조사
- 개요 진행 현황: 단계 2 진행 중 — 열린 질문 1, 답함 6, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q2-05 | 답함 | docs/tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md#q2-05 | — | — | — |
| q2-06 | 답함 | docs/tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md#q2-06 | — | — | — |
| q2-07 | 조사 중 | — | — | — | — |
| q4-21 | 열림 | — | 이름 사전의 별칭(altLabel·hiddenLabel)이 여러 장소에 겹칠 때(예: '2번 도크'가 두 층에 있음) 챗봇은 층·구역 맥락으로 좁힐지 되물을지를 어떤 규칙으로 정하고, 그 규칙을 이름 사전에 어떻게 기록하는가? (q2-05 에서 파생) (관련: q4-20, q4-07) | 4 | f8 |
| q4-22 | 열림 | — | SSCC 같은 적재 단위로 받은 지시에서 로봇이 보고한 loadId 가 지시한 SSCC 와 다르거나 빈 값일 때 ROP 는 진행·보류·재스캔·사람 확인 가운데 무엇을 하는가? (q2-06 에서 파생) (관련: oq-003, oq-036) | 4 | f10 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 16 | 7. 관련 표준·프레임워크·오픈소스 | 트랙 채팅 기반 구성·운영 단계 2(실행 2026-10-09-27, q2-05): IMDF 1.0.0 Unit 의 name·alt_name(장소 운영 조직 선언, 언어 태그별 LABELS), W3C SKOS 의 prefLabel·altLabel·hiddenLabel 과 notation, GS1 GLN 확장 성분(원문 미열람)을 장소 이름·별칭 사전 형식 후보로 반영하고, 정본 키를 코드로 두고 현장 호칭을 별칭으로 붙이며 현장 운영 조직이 정본 이름을 정하는 분담(이 위키의 종합, 추정)을 6. 대표 접근법과 기술에 함께 제안. 짝 엔진 영역 15. 지도·공간·위치 모델과 대화로 이를 부르는 12. 채팅으로 업무 지시·오케스트레이션을 연결하며, 학습한 공간 개념을 배정에 쓰는 Murata 외(저자 보고, 프리프린트)는 44. 로봇 기반 모델·언어 모델 계획·25. 작업 배정 — MRTA 와 함께 연결. |
| 17 | 7. 관련 표준·프레임워크·오픈소스 | 트랙 채팅 기반 구성·운영 단계 2(실행 2026-10-09-27, q2-06): VDA 5050 상태 스키마 loads 의 loadId(바코드·RFID 값, SSCC 형식 비강제, 품목 코드·수량·SSCC 필드 없음), GS1 EPCIS 집계 이벤트 스키마의 parentID–childEPCs·childQuantityList, GS1 회원 기관 안내의 SSCC 물류 단위를 작업 대상 식별 단위(품목 단위·적재 단위) 대응 근거로 반영 제안. 단위–품목 대응과 재고 정본은 상위 업무 시스템 연계 대상(추정). |
| 5 | 7. 관련 표준·프레임워크·오픈소스 | 트랙 채팅 기반 구성·운영 단계 2(실행 2026-10-09-27, q2-07 부분 답): IEEE 1872.1-2024 의 공개 범위(이사회 승인 2024-02-15, 발행 2024-06-18, 작업반 RTR, 구현 지침 P1872.1.1 개발 중), 관련 연구 그룹의 작업 구조(하위 클래스·범주·관계로의 분해, Balakirsky 외 2017)와 목표→하위 목표 분해(Aguado 외 2024)를 반영 제안. 표준 본문 미열람으로 선후 의존·배정 대상 개념은 미확인이며, 하위 그룹과 1872.1 작업반을 잇는 것은 추론임을 명시. |
